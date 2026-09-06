"""Reconstruct finite matrices to test module, transfer and specialization formulas.
The symbolic proof, not this bounded check, establishes uniformity.
"""
from pathlib import Path
from itertools import combinations
from math import gcd
import json,random
from arithmetic import *

ROOT=Path(__file__).parent

def main():
    rng=random.Random(202609060538)
    triples=[poly([0,a,b]) for a,b in combinations(range(1,14),2)]
    records=[];certs=[];total=0;compact_checks=transfer_checks=boundary_checks=0
    orders={}
    pairs=[]
    for A in triples:
        for B in triples:
            if pgcd(A,B)==1:continue
            if gcd(*terms(A)[1:],*terms(B)[1:])!=1:continue
            pairs.append((A,B))
    rng.shuffle(pairs)
    # Preserve deterministic varied cases, not a record-ratio search.
    for A,B in pairs[:100]:
        c=pgcd(A,B)
        assert pgcd(c,deriv(c))==1
        for L in (15,21,24,30):
            for delta in (0,1):
                for kappa in (0,1):
                    D=data(A,B,delta,L,kappa)
                    if D['g0']==1:continue
                    C=Cover(L,kappa,A,B,delta)
                    assert C.k==2*degree(D['H'])
                    span=Span(C.boundaries)
                    for i in range(degree(D['G'])):
                        parts=conv_parts(D['gen'],1<<i)
                        assert universal_cycle(A,B,delta,parts)
                        span.add(C.encode_physical(parts))
                    compact_dim=len(span)-len(C.bd)
                    assert compact_dim==degree(D['H'])
                    for _ in range(4):
                        f=rng.randrange(1,1<<max(1,degree(D['G'])+2))
                        h=rng.randrange(1<<5)
                        parts=conv_parts(D['gen'],f,D['bd'],h)
                        assert universal_cycle(A,B,delta,parts)
                        z=C.encode_physical(parts)
                        assert C.logical(z)==bool(rem(f,D['H']))
                        compact_checks+=1
                        u=pmul(D['b'],f);v=pmul(D['a'],f)
                        trans=C.encode_epsilon(set(),set(),set(terms(u)),set(terms(v)))
                        assert C.cycle(trans)
                        assert C.logical(trans)==bool(rem(pmul(D['E'],f),D['H']))
                        transfer_checks+=1
                        # Exact universal boundary identity for transfer.
                        p1=conv_parts(D['gen'],pmul(D['E'],f),D['bd'],pmul(D['a'],f))
                        assert p1==(set(terms(u)),set(terms(u)),set(terms(v)),set(terms(v)))
                        boundary_checks+=1
                    if len(certs)<140 and rem(1,D['H']):
                        z=C.encode_physical(conv_parts(D['gen'],1))
                        certs.append(C.certificate(z,{'source':'canonical_compact_generator','base_A':terms(A),'base_B':terms(B),'delta':delta}))
                    # N-L multiple 2O => congruent F modulo c^2. Use finite order found by direct modular powering.
                    if c not in orders:
                        O=1;x=rem(2,c)
                        while x!=1:
                            x=rem(pmul(x,2),c);O+=1
                            assert O<100000
                        orders[c]=O
                    O=orders[c];N=L*(1+2*O)
                    def zpower(n,modulus):
                        out=1;x=2
                        while n:
                            if n&1:out=rem(pmul(out,x),modulus)
                            x=rem(pmul(x,x),modulus);n>>=1
                        return out
                    Fn=zpower(N,pmul(c,c))^1
                    assert rem(Fn^D['F'],pmul(c,c))==0
                    assert pgcd(D['G'],Fn^(A if kappa else 0))==D['H']
                    assert pgcd(c,Fn)==D['g0']
                    records.append(dict(A=terms(A),B=terms(B),L=L,delta=delta,kappa=kappa,
                                        c=terms(c),E=terms(D['E']),G=terms(D['G']),H=terms(D['H']),
                                        compact_dimension=compact_dim,k=C.k,odd_root_order=O))
                    total+=1
    out={'parameter_instances':total,'compact_membership_checks':compact_checks,
         'transfer_checks':transfer_checks,'exact_universal_transfer_boundary_checks':boundary_checks,
         'period_stability_checks':total,'canonical_nonboundary_certificates':len(certs)}
    (ROOT/'structure_summary.json').write_text(json.dumps(out,indent=2)+'\n')
    (ROOT/'structure_cases.json').write_text(json.dumps(records,indent=2)+'\n')
    (ROOT/'structure_certificates.json').write_text(json.dumps(certs,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
