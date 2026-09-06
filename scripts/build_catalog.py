#!/usr/bin/env python3
"""Merge every original claim with an explicit current-status overlay, without deleting history."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import os
from collections import Counter

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
    policy=json.loads((ROOT/'results/review_policy.json').read_text())
    review={r['id']:r for r in policy['records']}
    if len(review)!=len(policy['records']) or set(review)!=set(ids):
        raise RuntimeError('Editorial review must classify each of the 104 records exactly once')
    for r in rows:
        r['review']=review[r['id']]
        if r['review']['disposition'] not in policy['categories']:
            raise RuntimeError('Unknown review category: '+r['id'])
        if r['review']['headline'] != (r['id'] in policy['headline_ids']):
            raise RuntimeError('Inconsistent headline selection: '+r['id'])
        if any(x not in review for x in r['review']['known_dependencies']):
            raise RuntimeError('Unknown dependency: '+r['id'])
        if r['id']=='DEG-I01':
            r['historical_limitations']=r['limitations']
            r['limitations']='The original missing-certificate note is superseded for this finite example; use CEX-UP. This duplicate entry is not an additional counterexample.'
        elif r['id']=='DEG-I02':
            r['historical_limitations']=r['limitations']
            r['limitations']='The finite example is fully certified as CEX-DOWN; the inherited infinite family remains evidence-limited. Do not promote the combined entry wholesale.'
    disposition_counts=dict(Counter(r['review']['disposition'] for r in rows))
    data={'schema_version':2,'version':policy['version'],'scope':'Complete supplied-result register; original statuses retained and current overlays explicit.',
          'counts':{'main':sum(r['branch']=='main' for r in rows),'homology':sum(r['branch']=='homology' for r in rows),'amplification':len(amp),'degradation':len(deg),'total':len(rows)},'results':rows}
    data['review_categories']=policy['categories']
    data['disposition_counts']=disposition_counts
    data['headline_ids']=policy['headline_ids']
    data['review_basis']=policy['basis']
    data['dependency_policy']=policy['dependency_policy']
    text=json.dumps(data,indent=2,ensure_ascii=False)+'\n'
    def link(path):
        plain,sep,frag=path.partition('#')
        relative=os.path.relpath(ROOT/plain,ROOT/'results').replace(os.sep,'/')
        return '['+plain+']('+relative+('#'+frag if sep else '')+')'
    lines=['# 104 条研究记录：结果、否定路线与未决问题 / Research record register','',
           '[先读主报告](../REPORT.md) · [采用与排除状态](STATUS.md) · [阅读路线](README.md) · [机器可读目录](catalog.json)','',
           '**104 是研究记录数，不是 104 个有效定理，也不是 104 个独立成果。** 包含重复登记、否定结果、未决问题、样本搜索及材料有缺口的历史输入。',
           '每项列出当前采用方式、范围、证据类型、论证或问题出处和限制。`symbolic-proof` 表示文本给出证明，不表示形式化验证或独立同行评审；原始状态不自动等于当前采用状态。',
           '两个有限反例的缺失证书已由第三个输入包补齐；早期参数族和小重量输入必须保留各自限制。','',
           '| 分组 | 项数 |','|---|---:|']
    for b,n in data['counts'].items():lines.append(f'| {b} | {n} |')
    for r in rows:
        rev=r['review']; kind=rev['disposition']
        evidence_label={'open':'问题出处（不是证明）','exploratory':'搜索记录出处（不是全局证明）',
                        'gap':'恢复论证或继承输入（证据链尚有缺口）','outside':'范围外论证或报告',
                        'negative':'否定结果的论证（不可反向采用被否定的路线）',
                        'historical':'历史较弱界的论证'}.get(kind,'证明／论证入口')
        lines+=['',f'<a id="{r["id"]}"></a>','',f'## {r["id"]}','',r['statement'],'',
                '**Scope / 范围：** '+r['scope'],'','**Status / 状态：** `'+r['status']+'`；原证据类型：'+r['evidence_type']+'.','',
                '**当前采用方式：** '+policy['categories'][kind]['label_zh']+'。'+rev['reason_zh'], '',
                '**'+evidence_label+'：** '+(' · '.join(link(p) for p in r['proofs']) or '本条没有单独文本入口；证书型条目见下面的数据与验证器，缺失型条目见其限制。')]
        if rev['known_dependencies']:
            lines+=['','**已记录的主要依赖：** '+' · '.join('['+i+'](#'+i+')' for i in rev['known_dependencies'])]
        if r.get('historical_limitations'):
            lines+=['','**旧版本限制（已被上面的当前状态修正）：** '+r['historical_limitations']]
        if r['evidence']:lines+=['','**程序与数据：** '+' · '.join(link(p) for p in r['evidence'])]
        if r.get('current_update'):lines+=['','**合并后的更新：** '+r['current_update']]
        if r.get('limitations'):lines+=['','**限制：** '+r['limitations']]
        if r['unavailable_historical_sources']:
            lines+=['','**未公开或未恢复的历史路径（不是可用证据链接）：** '+', '.join('`'+p+'`' for p in r['unavailable_historical_sources'])]
    md='\n'.join(lines)+'\n'
    status_lines=['# 当前采用状态：主结论与研究过程分开','',
        '[主报告](../REPORT.md) · [全部研究记录](CLAIMS.md) · [状态规则](review_policy.json)','',
        '**104 条记录不等于 104 个已证定理。** 下表是范围和证据审阅后的展示分类，不是新增的独立数学审稿。',
        '有效否定结果应保留，但被否定的推理路线不能再进入正面证明；历史较弱界不等于错误，未决问题不等于错误命题。','',
        '| 当前采用方式 | 记录数 | 使用规则 |','|---|---:|---|']
    for key,cat in policy['categories'].items():
        status_lines.append('| '+cat['label_zh']+' | '+str(disposition_counts.get(key,0))+' | '+cat['rule_zh']+' |')
    status_lines+=['','主报告 12 条索引合为若干主要结论，其中两个有限反例有独立精确证书；一般定理是仓库提供了符号证明。记录间有重复及依赖，不能把分类计数当独立成果数量。',
        '常数 8 及依赖它的区间／截断上界显式保留合并推论来源；程序通过不代表该推论通过独立审稿。',
        '登记的依赖只覆盖本次识别出的主要引用关系，不声称是一份形式化完整证明依赖图。']
    for key,cat in policy['categories'].items():
        status_lines+=['', '<a id="'+key+'"></a>', '', '## '+cat['label_zh'], '', cat['rule_zh'], '',
                       '| 记录 | 当前解释 |','|---|---|']
        for r in rows:
            if r['review']['disposition']==key:
                reason=r['review']['reason_zh'].replace('|','\\|').replace('\n',' ')
                status_lines.append('| ['+r['id']+'](CLAIMS.md#'+r['id']+') | '+reason+' |')
    status_md='\n'.join(status_lines)+'\n'
    outputs={ROOT/'results/catalog.json':text,ROOT/'bbcover/catalog.json':text,ROOT/'results/CLAIMS.md':md,
             ROOT/'results/STATUS.md':status_md}
    if args.check:
        bad=[str(p.relative_to(ROOT)) for p,s in outputs.items() if not p.exists() or p.read_text()!=s]
        print(json.dumps({'status':'passed' if not bad else 'stale','mismatches':bad,'counts':data['counts']},indent=2))
        return bool(bad)
    for p,s in outputs.items():p.write_text(s)
    print(json.dumps(data['counts'],indent=2))
    return 0
if __name__=='__main__':raise SystemExit(main())
