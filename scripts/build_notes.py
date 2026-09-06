#!/usr/bin/env python3
"""Publish complete research notes as GitHub-readable copies; retain original bytes.

Only navigation, inherited citation markers and math delimiters are normalized. No proof is summarized or
silently upgraded. Source/output hashes are recorded for reproducible maintenance.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'results/notes'

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def source_list():
    paths=[]
    for p in sorted((ROOT/'research/amplification/history').glob('*.md')):
        paths.append(('A'+p.name[:2]+'-'+p.stem[3:].replace('_','-')+'.md',p))
    for p in sorted((ROOT/'research/amplification/research').glob('*/REPORT.md')):
        paths.append(('A'+p.parent.name[:2]+'-'+p.parent.name[3:].replace('_','-')+'.md',p))
    for p in sorted((ROOT/'research/degradation/research').glob('*/proof.md')):
        paths.append(('D'+p.parent.name+'.md',p))
    for p in sorted((ROOT/'research/homology').glob('H*.md')):
        paths.append((p.name,p))
    paths.append(('X00-beyond-trinomials.md', ROOT/'research/beyond-trinomials/REPORT.md'))
    return paths

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    target=ROOT/'provenance/note_render_audit.json'
    if args.check:
        data=json.loads(target.read_text())
        bad=[name for record in data['notes'] for name,key in
             [(record['source'],'source_sha256'),(record['rendered'],'rendered_sha256')]
             if not (ROOT/name).is_file() or digest(ROOT/name)!=record[key]]
        print(json.dumps({'status':'passed' if not bad else 'stale','mismatches':bad},indent=2))
        return bool(bad)
    policy=json.loads((ROOT/'results/review_policy.json').read_text())
    DEST.mkdir(parents=True,exist_ok=True)
    notes=[]
    for name,source in source_list():
        dest=DEST/name
        text=source.read_text()
        unresolved=[]
        def replace_link(match):
            title,link=match.groups()
            if urlsplit(link).scheme in ('http','https','mailto'):return match.group(0)
            if link.startswith('#'):return match.group(0)
            if urlsplit(link).scheme:
                base=link.rsplit('/',1)[-1]
                candidates=[p for folder in ('certificates','archive/early_counterexample') for p in (ROOT/folder).rglob(base) if p.is_file()]
                aliases={'bb_double_cover_referee_certificate.zip':'certificates/upper/CERTIFICATE.md',
                         'bb_lower_counterexample_certificate.zip':'certificates/lower/CERTIFICATE.md',
                         'bb_double_cover_counterexample.zip':'archive/early_counterexample/MATHEMATICAL_CERTIFICATE.md'}
                known=ROOT/aliases[base] if base in aliases else (candidates[0] if len(candidates)==1 else None)
                if known is not None and urlsplit(link).scheme=='sandbox':
                    relative=os.path.relpath(known,dest.parent).replace(os.sep,'/')
                    return '['+title+']('+relative+')'
                unresolved.append(link);return title+' (historical external reference; see original note)'
            path,sep,fragment=link.partition('#')
            resolved=(source.parent/unquote(path)).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                unresolved.append(link);return title+' (`'+link+'`, historical path unavailable)'
            relative=os.path.relpath(resolved,dest.parent).replace(os.sep,'/')
            return '['+title+']('+relative+('#'+fragment if sep else '')+')'
        # Keep code/math fenced blocks untouched; normalize ordinary LaTeX delimiters.
        segments=re.split(r'(^```[^\n]*\n.*?^```\s*$)',text,flags=re.M|re.S)
        converted=[]
        for segment in segments:
            if segment.startswith('```'):converted.append(segment);continue
            segment=re.sub(r'\\\[(.*?)\\\]',lambda m:'\n\n$$\n'+m.group(1).strip()+'\n$$\n\n',segment,flags=re.S)
            segment=re.sub(r'\\\((.*?)\\\)',lambda m:'$'+m.group(1)+'$',segment,flags=re.S)
            segment=re.sub(r'\[([^\]\n]+)\]\(([^)\n]+)\)',replace_link,segment)
            if name.startswith('H'):
                segment=re.sub(r'filecite[^]+','[SRB, supplied v3](../REFERENCES.md#ref-SRB)',segment)
            converted.append(segment)
        header=('[全部研究结果](../README.md) · [逐项结论](../CLAIMS.md) · '
                '[原始完整文本]('+os.path.relpath(source,dest.parent).replace(os.sep,'/')+')\n\n'
                '> 完整研究笔记的 GitHub 阅读版；仅调整数学分隔符、引用标记与链接。历史状态、限制和证明内容均保留。'
                '当前结论以总登记表中的逐项状态为准；这里的“验证”不等于独立同行评审。\n\n')
        code=name.split('-',1)[0]
        warning=policy['note_warnings'].get(code)
        if not warning:
            raise RuntimeError('A current scope/evidence warning is required for '+name)
        header=('> **先看当前采用状态：** '+warning+'\n> [主报告](../../REPORT.md) · '
                '[逐项采用／排除表](../STATUS.md)。本篇为保留过程，不是整篇无条件有效的定理集合。\n\n')+header
        if name.startswith('H'):
            header += '> 历史研究报告：初稿中尚未解决的距离猜想已被 H03/H05 的精确反例推翻；报告中的候选引理与最终定理须分开阅读。有关 Bockstein 的四重厚化证明适用于文中规定的矩形周期覆盖，不自动推广到任意覆盖。旧附件链接只在可确认对应材料时重定向；文中的 current/latest 指历史撰写时点，不表示本次做了最新文献排查。原文件引用标记转换为参考文献中的 supplied v3。\n\n'
        dest.write_text(header+''.join(converted))
        notes.append({'source':str(source.relative_to(ROOT)),'source_sha256':digest(source),
                      'rendered':str(dest.relative_to(ROOT)),'rendered_sha256':digest(dest),
                      'unavailable_historical_links_rendered_as_text':unresolved})
    target.write_text(json.dumps({'policy':'Complete original body preserved; display delimiters, inherited citation markers and navigation adjusted; current scope/evidence warnings are editorial front matter.','notes':notes},indent=2)+'\n')
    print(json.dumps({'full_notes':len(notes),'bytes':sum((ROOT/x['rendered']).stat().st_size for x in notes),
                      'historical_unavailable_links':sum(len(x['unavailable_historical_links_rendered_as_text']) for x in notes)},indent=2))
    return 0
if __name__=='__main__':raise SystemExit(main())
