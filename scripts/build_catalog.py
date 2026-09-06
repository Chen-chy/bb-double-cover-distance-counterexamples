#!/usr/bin/env python3
"""Merge every original claim with an explicit current-status overlay, without deleting history."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import os

ROOT=Path(__file__).resolve().parents[1]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    args=parser.parse_args()
    notes=json.loads((ROOT/'provenance/note_render_audit.json').read_text())['notes']
    readable={x['source']:x['rendered'] for x in notes}
    rows=json.loads((ROOT/'results/core_claims.json').read_text())
    for r in rows:r.setdefault('unavailable_historical_sources',[])
    amp=json.loads((ROOT/'research/amplification/provenance/claim_ledger.json').read_text())
    deg=json.loads((ROOT/'research/degradation/metadata/claims.json').read_text())
    def classify(path):
        clean=path.split('#',1)[0]
        return (ROOT/clean).is_file()
    def use_readable(path):return readable.get(path,path)
    for original in amp:
        base='research/amplification/'
        proof=base+original['source']
        evidence=[base+x for x in original['evidence_files']]
        missing=[p for p in [proof]+evidence if not classify(p)]
        status='historical-weaker-bound' if not original.get('current',True) else original['evidence_type']
        update=''
        if original['id'] in ('GLOBAL-01','GLOBAL-02'):
            status='historical-weaker-bound';update='Current consolidated constants are in DIST-UPPER and DIST-TRUNCATED.'
        if original['id']=='BASE-01':
            update='The finite j=0 seed is repaired by CEX-UP. The complete historical family retains its recovered-source status; checking the seed does not independently certify all j.'
        rows.append(dict(id='AMP-'+original['id'],branch='amplification',statement=original['statement'],scope=original['scope'],
                         evidence_type=original['evidence_type'],status=status,
                         proofs=[use_readable(proof)] if classify(proof) else [],
                         evidence=[p for p in evidence if classify(p)],unavailable_historical_sources=missing,
                         limitations=original.get('limits',''),current_update=update,original_record=original))
    for original in deg:
        paths=[]
        for p in original['evidence']:
            if p=='context/conversation/00-arbitrary-term-public-report.md':paths.append('research/beyond-trinomials/REPORT.md')
            else:paths.append('research/degradation/'+p)
        existing=[p for p in paths if classify(p)]
        proofs=[use_readable(p) for p in existing if p.endswith('.md')]
        status=original['status']; update=''
        if original['id']=='I01':
            status='finite-certificate-repaired';proofs=['results/theory/01-counterexamples.md','certificates/upper/CERTIFICATE.md']
            update='The third input ZIP supplies two independent exact verifiers. See CEX-UP; the original missing-certificate note is historical.'
        elif original['id']=='I02':
            status='finite-certificate-repaired-family-inherited';proofs=['results/theory/01-counterexamples.md','certificates/lower/CERTIFICATE.md','results/HISTORY_AND_LIMITS.md']
            update='The finite 14->12 example is repaired by CEX-DOWN; the entire inherited infinite family is not upgraded by testing that seed.'
        elif original['id']=='I04':
            status='related-proof-restored-with-explicit-scope';proofs=['results/notes/A06-linear-compact-replacement.md']
            update='The other branch now supplies the exact compact theorem. Its explicit normal-form and survival hypotheses replace any unqualified handoff description.'
        elif original['id']=='I03':proofs=['results/HISTORY_AND_LIMITS.md']
        rows.append(dict(id='DEG-'+original['id'],branch='degradation',statement=original['statement'],scope=original['scope'],
                         evidence_type=original['status'],status=status,proofs=proofs,
                         evidence=[p for p in existing if not p.endswith('.md')],
                         unavailable_historical_sources=[p for p in paths if not classify(p)],
                         limitations=original.get('limitations',''),current_update=update,original_record=original))
    ids=[r['id'] for r in rows]
    if len(ids)!=len(set(ids)):raise RuntimeError('Duplicate result identifiers')
    data={'schema_version':1,'version':'0.2.0','scope':'Complete supplied-result register; original statuses retained and current overlays explicit.',
          'counts':{'main':sum(r['branch']=='main' for r in rows),'homology':sum(r['branch']=='homology' for r in rows),'amplification':len(amp),'degradation':len(deg),'total':len(rows)},'results':rows}
    text=json.dumps(data,indent=2,ensure_ascii=False)+'\n'
    def link(path):
        plain,sep,frag=path.partition('#')
        relative=os.path.relpath(ROOT/plain,ROOT/'results').replace(os.sep,'/')
        return '['+plain+']('+relative+('#'+frag if sep else '')+')'
    lines=['# 全部结论登记表 / Complete result register','',
           '[阅读路线](README.md) · [机器可读目录](catalog.json) · [历史与缺失材料](HISTORY_AND_LIMITS.md)','',
           '这里逐项收录主结果和两条研究支线，不把旧状态删除，也不把有限扫描升级为一般定理。',
           '每项均列出范围、证据类型、完整证明、数据/程序和限制。`symbolic-proof` 表示文本给出证明，不表示经过形式化验证或独立同行评审。',
           '两个有限反例的缺失证书已由第三个输入包补齐；早期参数族和小重量输入必须保留各自限制。','',
           '| 分组 | 项数 |','|---|---:|']
    for b,n in data['counts'].items():lines.append(f'| {b} | {n} |')
    for r in rows:
        lines+=['',f'<a id="{r["id"]}"></a>','',f'## {r["id"]}','',r['statement'],'',
                '**Scope / 范围：** '+r['scope'],'','**Status / 状态：** `'+r['status']+'`；原证据类型：'+r['evidence_type']+'.','',
                '**完整证明：** '+(' · '.join(link(p) for p in r['proofs']) or '原始独立证明未恢复；见历史与缺失材料说明。')]
        if r['evidence']:lines+=['','**程序与数据：** '+' · '.join(link(p) for p in r['evidence'])]
        if r.get('current_update'):lines+=['','**合并后的更新：** '+r['current_update']]
        if r.get('limitations'):lines+=['','**限制：** '+r['limitations']]
        if r['unavailable_historical_sources']:
            lines+=['','**未公开或未恢复的历史路径（不是可用证据链接）：** '+', '.join('`'+p+'`' for p in r['unavailable_historical_sources'])]
    md='\n'.join(lines)+'\n'
    outputs={ROOT/'results/catalog.json':text,ROOT/'bbcover/catalog.json':text,ROOT/'results/CLAIMS.md':md}
    if args.check:
        bad=[str(p.relative_to(ROOT)) for p,s in outputs.items() if not p.exists() or p.read_text()!=s]
        print(json.dumps({'status':'passed' if not bad else 'stale','mismatches':bad,'counts':data['counts']},indent=2))
        return bool(bad)
    for p,s in outputs.items():p.write_text(s)
    print(json.dumps(data['counts'],indent=2))
    return 0
if __name__=='__main__':raise SystemExit(main())
