"""Verify enumeration accounting, independent audit outputs and catalogue hashes."""
from pathlib import Path
import json,hashlib,sys
import sympy
ROOT=Path(__file__).resolve().parent

def counts(name):return {k:int(v)for k,v in (line.split('\t')for line in (ROOT/name).read_text().splitlines())}
h=counts('highrank_counts.tsv');lo=counts('low_free_counts.tsv');pu=counts('pure_eight_counts.tsv')
g=json.loads((ROOT/'graph_verification.json').read_text());hv=json.loads((ROOT/'highrank_verification.json').read_text());lv=json.loads((ROOT/'low_free_verification.json').read_text());pv=json.loads((ROOT/'pure_verification.json').read_text());nv=json.loads((ROOT/'nilpotent_verification.json').read_text())
for r in range(4,8):
 prefix=f'{r}:'
 assert sum(v for k,v in h.items()if k.startswith(prefix)and k!=prefix+'total')==h[prefix+'total']
 assert h.get(prefix+'exact_rank_at_least_3',0)==0
 assert sum(v for k,v in lo.items()if k.startswith(prefix)and k not in [prefix+'total',prefix+'maxfinite',prefix+'maxstrip'])==lo[prefix+'total']
 assert h[prefix+'total']==lo[prefix+'total']
 assert h[prefix+'rank_at_least_3']==lo[prefix+'total']-lo[prefix+'modrank_below_3']
assert sum(h[f'{r}:total']for r in range(4,8))==g['mixed_port_assignments']==40917312
assert sum(v for k,v in pu.items()if k!='8:total')==pu['8:total']==g['pure_port_assignments']==5598720
assert hv['retained_pairs']==312 and hv['unresolved']==0
assert lv['checked_lattices']==44619 and lv['maximum_finite_order']==56 and lv['maximum_strip_bound']==96
assert pv['checked_pure_presentations']==12 and pv['maximum_group_order']==15
expected={
 'highrank_eight.tsv':'f327dabff670a0c513f07dac76d104252aaacd63fd6a6971992ba7bfeeab9132',
 'low_free_lattices.tsv':'4df3bebab227c231f186b553f335e6caca5c592a5120bfce86690a82d4628d43',
 'pure_eight.tsv':'53cac389e0de7eedc0788c2585e977ae709b157b1051b49a0cc132bc79fef92a'}
for name,digest in expected.items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
res={'status':'D2_EQ_8_UNBOUNDED_BASE_EXCLUDED','universal_base_distance_bound_D8':96,'scope':'Any term-preserving finite abelian group quotient with positive-dimensional base and cover distance exactly eight; in particular every valid strict-trinomial BB double cover.','combined_previous_result':'With the prior weight-two, weight-four and weight-six exclusions, d>96 implies d_2>=10.','degradation_lower_bound':'gamma_3(N)>=min(1/12,20/N); hence gamma_3(N)>=20/N for N>=240.','mixed_port_assignments':g['mixed_port_assignments'],'pure_port_assignments':g['pure_port_assignments'],'low_free_lattices':lv['checked_lattices'],'high_free_pairs':hv['retained_pairs'],'high_free_categories':hv['categories'],'pure_group_types':pv['group_types'],'unresolved_presentations':0,'exact_distance_records_claimed':False,'vanishing_ratio_family_proved':False,'catalogue_hashes':expected,'finite_sanity_checks':nv,'python_version':sys.version.split()[0],'sympy_version':sympy.__version__}
(ROOT/'verification_summary.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2));print('ALL ACCOUNTING, SOURCE CERTIFICATES AND CATALOGUE HASHES VERIFIED.')
