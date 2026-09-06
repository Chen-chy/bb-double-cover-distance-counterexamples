#!/usr/bin/env python3
"""Render the complete consolidated proofs as GitHub Markdown (requires Pandoc).

The converter preserves theorem/proof blocks and every mathematics node, expands
LaTeX macros through Pandoc, resolves chapter/equation references, and records a
coverage audit. It never replaces a proof by an abstract or a link to the PDF.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / 'results/theory'
FILENAMES = ['01-counterexamples.md', '02-homology.md', '03-polynomial-bounds.md',
             '04-size-bounds.md', '05-further-results.md', '06-certificate-algorithms.md',
             '07-evidence-scope.md']

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def walk(obj):
    if isinstance(obj, dict):
        if 't' in obj:
            yield obj
        for value in obj.values():
            yield from walk(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from walk(value)

def anchor(name: str) -> str:
    return re.sub(r'[^a-zA-Z0-9_-]', '-', name)

def raw_anchor(name: str):
    return {'t': 'RawBlock', 'c': ['html', f'<a id="{anchor(name)}"></a>']}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check source and generated-file hashes without Pandoc')
    args = parser.parse_args()
    audit_path = ROOT / 'provenance/theory_render_audit.json'
    if args.check:
        report = json.loads(audit_path.read_text())
        errors = [name for group in ('source_sha256', 'rendered_sha256')
                  for name, digest in report[group].items()
                  if not (ROOT/name).is_file() or sha(ROOT/name) != digest]
        print(json.dumps({'status':'passed' if not errors else 'stale', 'mismatches':errors}, indent=2))
        return bool(errors)
    process = subprocess.run(['pandoc','-f','latex','-t','json','main.tex'], cwd=ROOT/'paper',
                             capture_output=True, text=True, check=True)
    document = json.loads(process.stdout)
    chapters = []
    for block in document['blocks']:
        if block['t'] == 'Div' and 'thebibliography' in block['c'][0][1]:
            continue
        if block['t'] == 'Header' and block['c'][0] == 1:
            chapters.append([])
        if chapters:
            chapters[-1].append(block)
    if len(chapters) != len(FILENAMES):
        raise RuntimeError(f'Expected {len(FILENAMES)} chapters, found {len(chapters)}')
    targets = {}
    for filename, blocks in zip(FILENAMES, chapters):
        for node in walk(blocks):
            if node['t'] == 'Header':
                targets[node['c'][1][0]] = filename
            if node['t'] in ('Div','Span') and node['c'][0][0]:
                targets[node['c'][0][0]] = filename
            if node['t'] == 'Math':
                for label in re.findall(r'\\label\{([^}]+)\}', node['c'][1]):
                    targets[label] = filename
    math_audit = []
    unknown_refs = set()
    sources = {str(p.relative_to(ROOT)):sha(p) for p in sorted((ROOT/'paper').rglob('*.tex'))}

    def process_inlines(values):
        out = []
        for node in values:
            typ = node['t']; val = node.get('c')
            if typ == 'Cite':
                for i, cite in enumerate(val[0]):
                    if i: out += [{'t':'Str','c':';'}, {'t':'Space'}]
                    key = cite['citationId']
                    text = [{'t':'Str','c':key}]
                    if cite['citationSuffix']:
                        text += [{'t':'Str','c':','}, {'t':'Space'}] + cite['citationSuffix']
                    out.append({'t':'Link','c':[['',[],[]],text,['../REFERENCES.md#ref-'+anchor(key),'']]})
            elif typ == 'Link':
                dest, title = val[2]
                if dest.startswith('#'):
                    label = dest[1:]
                    if label not in targets: unknown_refs.add(label)
                    dest = targets.get(label, '')+'#'+anchor(label)
                out.append({'t':'Link','c':[['',[],[]],process_inlines(val[1]),[dest,title]]})
            elif typ == 'Emph':
                # Theorem-wide emphasis can hide display equations inside HTML.
                out.extend(process_inlines(val))
            elif typ == 'Strong':
                out.append({'t':typ,'c':process_inlines(val)})
            elif typ == 'Span':
                out.extend(process_inlines(val[1]))
            else:
                out.append(copy.deepcopy(node))
        return out

    def process_blocks(blocks):
        out = []
        for block in blocks:
            typ=block['t']; val=block.get('c')
            if typ == 'Header':
                if val[1][0]: out.append(raw_anchor(val[1][0]))
                out.append({'t':'Header','c':[val[0],['',[],[]],process_inlines(val[2])]})
            elif typ == 'Div':
                if val[0][0]:out.append(raw_anchor(val[0][0]))
                out.extend(process_blocks(val[1]))
            elif typ in ('Para','Plain'):
                current=[]
                for node in process_inlines(val):
                    if node['t']=='Math' and node['c'][0]['t']=='DisplayMath':
                        if current:
                            out.append({'t':typ,'c':current});current=[]
                        text=node['c'][1]
                        for label in re.findall(r'\\label\{([^}]+)\}',text):out.append(raw_anchor(label))
                        text=re.sub(r'\\label\{[^}]+\}', '', text).strip()
                        out.append({'t':'RawBlock','c':['markdown','$$\n'+text+'\n$$']})
                        math_audit.append(text)
                    else:
                        current.append(node)
                if current:out.append({'t':typ,'c':current})
            elif typ == 'BulletList':
                out.append({'t':typ,'c':[process_blocks(x) for x in val]})
            elif typ == 'OrderedList':
                out.append({'t':typ,'c':[val[0],[process_blocks(x) for x in val[1]]]})
            elif typ == 'BlockQuote':
                out.append({'t':typ,'c':process_blocks(val)})
            else:
                # Tables and code blocks are already native Pandoc nodes.
                out.append(copy.deepcopy(block))
        return out

    DEST.mkdir(parents=True, exist_ok=True)
    rendered={}
    source_math_count = sum(n['t']=='Math' and n['c'][0]['t']=='DisplayMath'
                            for chapter in chapters for n in walk(chapter))
    for i,(name, blocks) in enumerate(zip(FILENAMES,chapters)):
        content = {'pandoc-api-version':document['pandoc-api-version'],'meta':{},'blocks':process_blocks(blocks)}
        result = subprocess.run(['pandoc','-f','json','-t','gfm+tex_math_dollars','--wrap=none'],
                                input=json.dumps(content), capture_output=True,text=True,check=True)
        links='[研究结果总目录](../README.md) · [结论登记表](../CLAIMS.md)'
        if i:links+=' · [上一章]('+FILENAMES[i-1]+')'
        if i+1<len(FILENAMES):links+=' · [下一章]('+FILENAMES[i+1]+')'
        note='> 本章包含完整论证，可独立于 PDF 阅读。符号、范围和引用见正文；GitHub 版命题编号独立于排版稿。'
        text=links+'\n\n'+note+'\n\n'+result.stdout
        text=text.replace('</a>\n$$', '</a>\n\n$$')
        (DEST/name).write_text(text)
        rendered[str((DEST/name).relative_to(ROOT))]=sha(DEST/name)
    if unknown_refs:
        raise RuntimeError('Unresolved internal references: '+', '.join(sorted(unknown_refs)))
    if len(math_audit)!=source_math_count:
        raise RuntimeError('Display mathematics coverage mismatch')
    report={'generator':'scripts/build_theory.py','source_sha256':sources,
            'rendered_sha256':rendered,'chapters':len(chapters),
            'display_math_in_source':source_math_count,'display_math_rendered':len(math_audit),
            'theorem_like_blocks':sum(n['t']=='Div' and bool(set(n['c'][0][1]) &
                       {'theorem','lemma','proposition','corollary','definition'}) for c in chapters for n in walk(c)),
            'proof_blocks':sum(n['t']=='Div' and 'proof' in n['c'][0][1] for c in chapters for n in walk(c)),
            'resolved_label_targets':len(targets),'unresolved_internal_references':[],
            'scope':'Structural coverage audit, not mathematical validation of the proofs.'}
    audit_path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if not k.endswith('sha256')},indent=2))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
