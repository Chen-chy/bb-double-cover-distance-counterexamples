"""Audit the complete Pareto frontier of the supplied record example.

Lower certificates are inherited data, independently re-audited here; the
new no-extra witness is checked directly. The frontier proof uses the lower
bounds on projected weight and total physical weight and parity, not a
truncated enumeration of the two-objective optimization.
"""
from __future__ import annotations
from pathlib import Path
import importlib.util, json

ROOT=Path(__file__).resolve().parent


def poly(exponents):
    value=0
    for i in exponents:
        assert i>=0
        value^=1<<i
    return value


def multiply(a,b):
    value=0
    for i in range(b.bit_length()):
        if b>>i&1:value^=a<<i
    return value


def divmod_poly(a,b):
    q=0
    while a and a.bit_length()>=b.bit_length():
        j=a.bit_length()-b.bit_length();q^=1<<j;a^=b<<j
    return q,a


def record_word(physical):
    u0,u1,v0,v1=map(poly,physical)
    A0,A1,B0,B1=33,16,8196,1
    assert not (multiply(A0,u0)^multiply(A1,u1)^multiply(B0,v0)^multiply(B1,v1))
    assert not (multiply(A1,u0)^multiply(A0,u1)^multiply(B1,v0)^multiply(B0,v1))
    p,q=u0^u1,v0^v1
    assert not(multiply(49,p)^multiply(8197,q))
    assert divmod_poly(q,11)[1]==0
    assert divmod_poly(q,7)[1]!=0
    W=(q<<8)^(multiply(49,v1)<<4)
    label,rem=divmod_poly(W,11)
    assert rem==0 and divmod_poly(label,7)[1]!=0
    length=p.bit_count()+q.bit_count()
    extra=(u0&u1).bit_count()+(v0&v1).bit_count()
    total=sum(x.bit_count() for x in (u0,u1,v0,v1))
    assert total==length+2*extra
    return {'physical':physical,'projection_weight':length,'outside_support_cost':extra,
            'total_weight':total,'exact_cycle':True,'nonzero_compact_label':True}


def finite_audit(physical,L=201):
    mask=(1<<L)-1
    def shift(p,j):
        j%=L
        return (((p<<j)&mask)|(p>>(L-j))) if j else p
    def translate(p0,p1,j,sheet):
        v0,v1=shift(p0,j),shift(p1,j)
        return (v1|(v0<<L)) if sheet else(v0|(v1<<L))
    A0,A1,B0,B1=33,16,8196,1
    boundaries=[translate(B0,B1,i,t)|(translate(A0,A1,i,t)<<(2*L))
                for t in range(2) for i in range(L)]
    echelon={}
    def reduce(v):
        for p in sorted(echelon,reverse=True):
            if v>>p&1:v^=echelon[p]
        return v
    for v in boundaries:
        v=reduce(v)
        if v:echelon[v.bit_length()-1]=v
    assert len(echelon)==2*L-2
    word=sum(poly(p)<<(i*L) for i,p in enumerate(physical))
    remainder=reduce(word);assert remainder
    free_bit=(remainder&-remainder).bit_length()-1
    dual=1<<free_bit
    for p in sorted(echelon):
        if (dual&echelon[p]).bit_count()%2:dual^=1<<p
    assert all((dual&b).bit_count()%2==0 for b in boundaries)
    assert (dual&word).bit_count()%2==1
    return {'L':L,'physical_qubits':4*L,'k':4,'boundary_rank':len(echelon),
            'dual_support':[i for i in range(4*L) if dual>>i&1],
            'boundary_pairings_checked':len(boundaries),'witness_pairing':1}


def main():
    module_path=ROOT/'previous_certificates'/'audit_certificates.py'
    spec=importlib.util.spec_from_file_location('prior_independent_auditor',module_path)
    auditor=importlib.util.module_from_spec(spec);spec.loader.exec_module(auditor)
    allcases=json.loads((module_path.parent/'exact_results.json').read_text())
    wanted={'base_full','base_resonant_purified','cover_full'}
    lower=[auditor.audit(c) for c in allcases if c['name'] in wanted]
    assert {c['name']:c['minimum'] for c in lower}=={'base_full':6,'base_resonant_purified':12,'cover_full':14}
    old=record_word([[3,10,11],[0,4,6,7,9,11,12],[0],[2,3,4]])
    new=record_word([[4,12,20],[0,5,16,19,21],[0,4,10],[2,6,13]])
    assert (old['projection_weight'],old['outside_support_cost'])==(12,1)
    assert (new['projection_weight'],new['outside_support_cost'])==(14,0)
    # Every projection is a nonzero cycle, hence even-weight, and is in the
    # j-divisible base family. Thus projection>=12 and physical>=14. These
    # two points dominate every feasible integer pair, proving completeness.
    assert old['total_weight']==new['total_weight']==14
    result={'status':'all exact checks passed','base_minimum':6,
            'inherited_lower_certificates_reaudited':lower,
            'complete_pareto_frontier':[[12,1],[14,0]],'witnesses':[old,new],
            'finite_nonboundary_audit':finite_audit(new['physical'])}
    (ROOT/'pareto_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='finite_nonboundary_audit'},indent=2))

if __name__=='__main__':main()
