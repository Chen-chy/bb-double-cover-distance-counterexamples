"""Independent audit. Imports no construction, polynomial, or matrix code.
Rebuilds group products with coordinate tuples and uses low-pivot elimination.
"""
from pathlib import Path
import json
ROOT=Path(__file__).parent

def bits(s):
    n=0
    for i in s:n^=1<<i
    return n

def parity(n):return n.bit_count()&1

def rank_low(vs):
    basis={}
    for v in vs:
        while v:
            b=v&-v
            if b in basis:v^=basis[b]
            else:basis[b]=v;break
    return len(basis)

def check(r):
    L,kappa=r['L'],r['kappa'];N=2*L
    def coordinate(e,s=0):
        q,x=divmod(e,L)
        return x+L*((s+kappa*q)&1)
    def shift(s,e,t):return {coordinate(i%L+e,i//L+t) for i in s}
    A=set(r['A_support']);B=set(r['B_support'])
    assert len(A)==len(B)==3
    # Check labeled polynomial-to-cover matching independently.
    Abase={e%L for e in r['base_A']};Bbase={e%L for e in r['base_B']}
    assert len(Abase)==len(Bbase)==3
    assert {e%L for e in A}==Abase and {e%L for e in B}==Bbase
    expected_A={coordinate(e) for e in r['base_A'] if e!=0}^{coordinate(0,1)}
    expected_B={coordinate(e) for e in r['base_B'] if e!=0}^{coordinate(0,r['delta'])}
    assert A==expected_A and B==expected_B
    z=set(r['witness']);u={i for i in z if i<N};v={i-N for i in z if i>=N}
    syndrome=set()
    for i in u:syndrome^=shift(A,i%L,i//L)
    for i in v:syndrome^=shift(B,i%L,i//L)
    assert not syndrome
    boundaries=[]
    for t in (0,1):
        for e in range(L):boundaries.append(bits(shift(B,e,t))|(bits(shift(A,e,t))<<N))
    dual=bits(r['dual']);word=bits(z)
    assert parity(dual&word)==1
    assert all(parity(dual&b)==0 for b in boundaries)
    rank=rank_low(boundaries)
    assert 2*(N-rank)==r['k']
    assert rank_low(boundaries+[word])==rank+1
    assert word.bit_count()==r['physical_weight']
    if 'universal_cover_weight' in r:assert word.bit_count()<=r['universal_cover_weight']
    if 'universal_cover_weight' in r and r['source'] not in ('canonical_compact_generator','divided_euler'):
        assert r['universal_cover_weight']<=2*r['universal_base_weight']
    if 'input_weight' in r:
        assert word.bit_count()<=r['pre_reduction_cover_weight']<=2*r['input_weight']
    return len(boundaries)

def main():
    counts={};total=pairings=0
    for name in ('structure_certificates.json','lift_certificates.json','seed_nonboundary_certificate.json','finite_parity_certificates.json','sharpness_certificates.json'):
        records=json.loads((ROOT/name).read_text())
        if isinstance(records,dict):records=[records]
        for r in records:pairings+=check(r);total+=1
        counts[name]=len(records)
    result={'status':'all independently audited certificates passed','certificates':total,
            'boundary_dual_pairings':pairings,'by_file':counts,
            'audit_method':'coordinate arithmetic, low-pivot ranks, explicit separating duals; no constructor imports'}
    (ROOT/'audit_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
