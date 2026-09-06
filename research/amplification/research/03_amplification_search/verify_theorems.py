"""Finite cross-checks of the two uniform algebraic theorems.
The uniform proofs are in REPORT.md; sampling is not their proof.
"""
from pathlib import Path
from itertools import combinations
from math import gcd
from collections import Counter
import random,json
from algebra import *
ROOT=Path(__file__).resolve().parent


def check_oneblock():
    rng=random.Random(9331);counts=Counter()
    for L in range(3,34):
        G,H=Group(L),Group(2*L);mask=(1<<L)-1
        for j in range(12):
            a,b=rng.sample(range(1,L),2);c,d=rng.sample(range(1,L),2)
            ap=a+L*rng.randrange(2);bp=b+L*rng.randrange(2)
            cp=c+L*rng.randrange(2);dp=d+L*rng.randrange(2)
            A,B=poly([0,a,b]),poly([0,c,d]);AA,BB=poly([0,ap,bp]),poly([0,cp,dp])
            C,D=Code(G,A,B),Code(H,AA,BB)
            ka=kernel(C.cols[:L]);kap=kernel(D.cols[:2*L]);q=gcd(L,gcd(ap,bp));qq=gcd(2*L,gcd(ap,bp))
            assert qq in (q,2*q)
            if qq==q:
                transferred=[v^(v<<L) for v in ka];S=Span(transferred)
                assert len(ka)==len(kap) and all(S.contains(v) for v in kap)
                # A complete equality of boundary subspaces, not just testing
                # nonzero classes one basis vector at a time.
                bbase=Span(G.mul(B,v) for v in ka)
                bcover=Span(H.mul(BB,v) for v in kap)
                expected=Span(v^(v<<L) for v in bbase.piv.values())
                assert len(bcover)==len(expected) and all(expected.contains(v) for v in bcover.piv.values())
                for v in ka:
                    assert (v^(v<<L)).bit_count()==2*v.bit_count()
                counts['exact_doubling_branch']+=1
            else:
                size=L//q;inv2=pow(2,-1,size) if size>1 else 0
                def lift_piece(v,t):
                    return poly(t+2*q*((((i-t)//q)*inv2)%size) for i in support(v))
                for v in ka:
                    for t in range(q):
                        piece=poly(i for i in support(v) if i%q==t)
                        if not piece:continue
                        vp=lift_piece(piece,t)
                        assert G.mul(A,piece)==0 and H.mul(AA,vp)==0
                        assert (vp&mask)^(vp>>L)==piece
                        assert vp.bit_count()==piece.bit_count()
                        if C.logical(piece):assert D.logical(vp)
                counts['weight_preserving_branch']+=1
            counts['instances']+=1
    return dict(counts)


def check_split():
    rng=random.Random(9332);stats=Counter()
    for l,m in [(3,1),(5,1),(7,1),(3,2),(3,3),(5,2),(3,4),(7,3)]:
        G=Group(l,m);M=G.size;mask=(1<<M)-1
        for j in range(12):
            P=poly([0,*rng.sample(range(1,M),2)]);Q=poly([0,*rng.sample(range(1,M),2)])
            for delta in (0,1):
                def smul(a,b):
                    a0,a1=a&mask,a>>M;b0,b1=b&mask,b>>M
                    return (G.mul(a0,b0)^G.mul(a1,b1))|((G.mul(a0,b1)^G.mul(a1,b0))<<M)
                AA=(P^1)|(1<<M);BB=(Q^delta)|(delta<<M)
                cols=[smul(C,1<<j) for C in (AA,BB) for j in range(2*M)]
                bd=Span(cols[2*M+j]|(cols[j]<<(2*M)) for j in range(2*M))
                cy=kernel(cols);eff=Code(G,G.mul(P,P),Q^(P if delta else 0))
                assert len(cy)-len(bd)==eff.k
                def T(z):
                    U,V=z&((1<<(2*M))-1),z>>(2*M)
                    u1=U>>M;v1=V>>M;v0=(V&mask)^v1
                    return (u1^(v1 if delta else 0))|((v0^G.mul(P,v1))<<M)
                def lift(z):
                    r,s=z&mask,z>>M
                    return (G.mul(P^1,r)^(s if delta else 0))|(r<<M)|(s<<(2*M))
                image=Span(T(z) for z in cy)
                assert all(image.contains(z) for z in eff.cycles)
                for z in cy:
                    w=T(z);assert eff.cycle(w)
                    assert bd.contains(z)==eff.bd.contains(w)
                    assert bd.contains(z^lift(w))
                    assert w.bit_count()<=(2+delta)*z.bit_count()
                for w in eff.cycles:
                    z=lift(w);assert T(z)==w
                    r,s=w&mask,w>>M
                    assert z.bit_count()<=3*r.bit_count()+(1+delta)*s.bit_count()
                stats['instances']+=1;stats['positive_k_instances']+=eff.k>0
    return dict(stats)


def reduced_example():
    G=Group(39);P=poly([0,14,22]);Q=poly([0,26,28]);base=Code(G,P,Q)
    eff=Code(G,G.mul(P,P),P^Q)
    u=poly([0,5,10,11,16,28]);v=poly([24,30,32]);z=u|(v<<39)
    assert base.k==eff.k==4 and eff.logical(z) and z.bit_count()==9
    return dict(L=39,P=support(P),Q=support(Q),effective_A=support(eff.A),effective_B=support(eff.B),k=4,effective_d=9,witness_u=support(u),witness_v=support(v))

if __name__=='__main__':
    out=dict(oneblock=check_oneblock(),split=check_split(),reduced_example=reduced_example())
    (ROOT/'theorem_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
