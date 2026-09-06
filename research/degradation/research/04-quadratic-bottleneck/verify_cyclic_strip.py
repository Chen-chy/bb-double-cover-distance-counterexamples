#!/usr/bin/env python3
"""Exact finite-matrix checks of the cyclic-torsion gcd/specialization formula."""
from __future__ import annotations
import math,random,json,time
from pathlib import Path
from verify import pmul,pdiv,Group,Basis

def gcd(a,b):
    while b:a,b=b,pdiv(a,b)[1]
    return a

def powp(a,e):
    out=1
    while e:
        if e&1:out=pmul(out,a)
        a=pmul(a,a);e>>=1
    return out

def degree(p):return p.bit_length()-1

def terms(poly,z):
    out=[]
    while poly:
        bit=poly&-poly;out.append((bit.bit_length()-1,z));poly^=bit
    return out

def case(h,P,seam,a,b,c,d):
    Q=(1<<h)^1;two=h&-h
    Qprime,rem=pdiv(Q,powp(3,two));assert not rem
    B=[(0,0),(a,b),(c,d)];A=[(0,0),(1,0),(0,1)]
    F=1^pmul(1<<a,powp(3,b))^pmul(1<<c,powp(3,d))
    g=gcd(F,Qprime)
    if g==1:return None
    S,rem=pdiv(Q,g);assert not rem
    # B=F+A*QB as polynomials in z, with coefficients cyclic in t.
    qb={}
    for ti,zj in [(a,b),(c,d)]:
        for j in range(zj):
            coeff=pdiv(pmul(1<<ti,powp(3,zj-1-j)),Q)[1]
            qb[j]=qb.get(j,0)^coeff
    U=[]
    for j,coef in qb.items():U+=terms(pdiv(pmul(coef,S),Q)[1],j)
    V=terms(S,0)
    # Check the universal syndrome before imposing ANY z-period.
    syndrome={}
    for W,C in [(U,A),(V,B)]:
        for i,j in W:
            for ii,jj in C:
                key=((i+ii)%h,j+jj);syndrome[key]=syndrome.get(key,0)^1
    assert not any(syndrome.values())
    f=powp(3,P)^(1<<seam)
    expected=[degree(gcd(g,f)),degree(gcd(g,pmul(f,f)))]
    if expected[0]==0:return None
    measured=[];ks=[]
    for pp,ss in [(P,seam),(2*P,2*seam)]:
        G=Group(h,pp,ss);av,bv=G.vector(A),G.vector(B)
        if av.bit_count()!=3 or bv.bit_count()!=3:return None
        w=G.vector(U)|(G.vector(V)<<G.n)
        assert G.syndrome(w,av,bv)==0
        bspace=G.boundaries(av,bv);rank_b=len(bspace)
        # All translations span exactly the specialized compact module.
        for shift in range(G.n):bspace.add(G.shift2(w,shift))
        measured.append(len(bspace)-rank_b)
        ks.append(G.k(av,bv))
    assert measured==expected, (h,P,seam,a,b,c,d,expected,measured)
    assert ks==[2*x for x in expected], (ks,expected)
    return dict(h=h,P=P,seam=seam,B=B,g=g,g_degree=degree(g),g_squarefree=gcd(g,sum(((g>>i)&1)<<(i-1) for i in range(1,g.bit_length(),2)))==1,compact_dimensions=measured,compact_kernel_dimension=measured[1]-measured[0],dimensions=ks)

def main():
    start=time.time();rng=random.Random(37429);rows=[];seen=set()
    # Deliberately include transverse cases, repeated-factor cases, and saturation.
    for h in [6,12,24]:
        for P in [3,6,9,12]:
            for q in [1,2,4,8]:
                args=(h,P,0,q%h,0,0,q)
                r=case(*args)
                if r: rows.append(r);seen.add(args)
    for attempt in range(30000):
        h=rng.choice([3,6,12,15,24]);P=rng.choice([3,4,5,6,7,9,12]);seam=rng.randrange(h)
        a,c=rng.randrange(h),rng.randrange(h);b,d=rng.randrange(5),rng.randrange(5)
        args=h,P,seam,a,b,c,d
        if args in seen:continue
        seen.add(args)
        r=case(*args)
        if r:rows.append(r)
        if len(rows)>=256:break
    assert len(rows)==256
    assert any(r['compact_kernel_dimension']>0 for r in rows)
    assert all(r['compact_kernel_dimension']==0 for r in rows if r['g_squarefree'])
    here=Path(__file__).resolve().parent
    out=dict(exact_cases=len(rows),loss_cases=sum(r['compact_kernel_dimension']>0 for r in rows),squarefree_cases=sum(r['g_squarefree'] for r in rows),nonsquarefree_no_loss_cases=sum(not r['g_squarefree'] and not r['compact_kernel_dimension'] for r in rows),max_torsion_order=max(r['h'] for r in rows),all_gcd_and_matrix_dimensions_agree=True,minimum_distances_computed=False,seconds=round(time.time()-start,3))
    (here/'cyclic_strip_cases.json').write_text(json.dumps(rows,indent=2))
    (here/'cyclic_strip_verification.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
