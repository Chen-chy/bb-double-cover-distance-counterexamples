"""Test the finite split-cover parity lemma on winding as well as compact cycles."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from math import gcd
import random,json
from arithmetic import *
from verify_lifts import derivative_lift
ROOT=Path(__file__).parent

def ker(columns):
    piv={};out=[]
    for j,col in enumerate(columns):
        v=col;word=1<<j
        while v:
            i=v.bit_length()-1
            if i not in piv:piv[i]=(v,word);break
            s,w=piv[i];v^=s;word^=w
        if not v:out.append(word)
    return out

def rot(a,e,L):
    e%=L;mask=(1<<L)-1
    return ((a<<e)&mask)|(a>>(L-e)) if e else a

def main():
    rng=random.Random(202609060701);counts=Counter();certs=[]
    for L in (12,18,24,30):
        triples=[{0,a,b} for a,b in combinations(range(1,min(L,12)),2)]
        candidates=[]
        for A in triples:
            for B in triples:
                for delta in (0,1):
                    # Only inspect exact derivative-pattern cases, independent of c.
                    if derivative_lift(A,B,delta,{0},{0}) is not None:candidates.append((A,B,delta))
        rng.shuffle(candidates)
        for A,B,delta in candidates[:160]:
            Ap=poly(A);Bp=poly(B)
            cols=[rot(C,j,L) for C in (Ap,Bp) for j in range(L)]
            bd=Span(rot(Bp,j,L)|(rot(Ap,j,L)<<L) for j in range(L))
            cycles=ker(cols)
            if len(cycles)==len(bd):continue
            C=LaurentCover(L,0,A,B,delta)
            c=pgcd(Ap,Bp);a=quo(Ap,c);b=quo(Bp,c)
            compact=Span(bd.p.values())
            F=(1<<L)|1
            for i in range(degree(c)):
                compact.add(rem(b<<i,F)|(rem(a<<i,F)<<L))
            tested=0
            # Test every independent nullspace output that is nonboundary;
            # these are not restricted to universal Laurent syzygies.
            for z in cycles:
                if bd.contains(z):continue
                u=set(terms(z&((1<<L)-1)));v=set(terms(z>>L))
                parts,method=derivative_lift(A,B,delta,u,v)
                lift=C.encode_physical(parts)
                assert C.logical(lift)
                assert lift.bit_count()<=2*z.bit_count()
                counts['finite_logical_checks']+=1
                if not compact.contains(z):counts['outside_compact_image_checks']+=1
                counts[method]+=1;tested+=1
                if len(certs)<90:
                    certs.append(C.certificate(lift,{'source':'finite_parity_'+method,'base_A':sorted(A),'base_B':sorted(B),'delta':delta,
                                                    'input_weight':z.bit_count(),'pre_reduction_cover_weight':sum(map(len,parts)),
                                                    'base_outside_compact_image':not compact.contains(z)}))
            if tested:counts['finite_base_instances']+=1
    result=dict(counts)
    assert result['outside_compact_image_checks']>0
    (ROOT/'finite_parity_summary.json').write_text(json.dumps(result,indent=2)+'\n')
    (ROOT/'finite_parity_certificates.json').write_text(json.dumps(certs,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
