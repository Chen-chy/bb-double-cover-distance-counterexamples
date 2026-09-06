#!/usr/bin/env python3
"""Independent exact BB distance certificate, using only Python's standard library.
No floating point, heuristic decoder, or homology-label construction is used.
"""
from collections import Counter
from time import perf_counter

def indices(v):
    while v:
        b=v & -v
        yield b.bit_length()-1
        v ^= b

def make_code(l,m,A,B):
    n=l*m
    def multiplication(poly):
        result=[]
        for a in range(l):
            for b in range(m):
                v=0
                for c,d in poly:
                    v ^= 1 << (((a+c)%l)*m+(b+d)%m)
                result.append(v)
        return result
    a,b=multiplication(A),multiplication(B)
    return a+b, [b[i] | (a[i]<<n) for i in range(n)]

def echelon(vectors):
    piv={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p in piv:
                v ^= piv[p]
            else:
                piv[p]=v
                break
    return piv

def residual(v,piv):
    for p in sorted(piv,reverse=True):
        if (v>>p)&1:
            v ^= piv[p]
    return v

def act(columns,v):
    s=0
    for j in indices(v):
        s ^= columns[j]
    return s

def circuit_test(H,G,bound,root):
    n=len(H);m=max(c.bit_length() for c in H)
    assert all(c.bit_count()==3 for c in H)
    adj=[0]*m
    for j,c in enumerate(H):
        for r in indices(c):
            adj[r] |= 1<<j
    assert all(a.bit_count()==6 for a in adj)
    piv=echelon(G)
    nodes=0;zeros=Counter();nontrivial=[]
    def visit(chosen,forbidden,syndrome,weight):
        nonlocal nodes
        nodes+=1
        if syndrome==0:
            zeros[weight]+=1
            if residual(chosen,piv):
                nontrivial.append(chosen)
            return
        remaining=bound-weight
        if remaining<=0 or syndrome.bit_count()>3*remaining:
            return
        used=chosen|forbidden
        candidates=None
        count=n+1
        # Select an odd check of minimum available degree. No packing bound.
        for row in indices(syndrome):
            available=adj[row] & ~used
            degree=available.bit_count()
            if degree==0:
                return
            if degree<count:
                candidates=available;count=degree
        # Each completion has a unique first selected candidate in this order.
        while candidates:
            bit=candidates & -candidates
            candidates ^= bit
            j=bit.bit_length()-1
            visit(chosen|bit,forbidden,syndrome^H[j],weight+1)
            forbidden |= bit
    visit(1<<root,0,H[root],1)
    return nodes,dict(sorted(zeros.items())),nontrivial

def vector(support):
    return sum(1<<i for i in support)

def run():
    A=[(0,0),(1,12),(2,8)]
    B=[(0,0),(1,2),(2,0)]
    BC=[(0,0),(1,2),(5,0)]
    H,G=make_code(3,13,A,B)
    HC,GC=make_code(6,13,A,BC)
    for h,g in [(H,G),(HC,GC)]:
        assert all(act(h,v)==0 for v in g)
    assert len(echelon(H))==37 and len(echelon(G))==37
    assert len(echelon(HC))==76 and len(echelon(GC))==76
    z=vector([0,9,18,36,49,73])
    w=vector([0,3,15,21,24,27,33,36,42,57,69,112,115,139])
    assert act(H,z)==0 and residual(z,echelon(G))
    assert act(HC,w)==0 and residual(w,echelon(GC))
    print('Ranks, commutation, and nontrivial weights 6 and 14: PASS',flush=True)
    for name,h,g,bnd in [('base',H,G,4),('cover',HC,GC,12)]:
        for root in (0,len(h)//2):
            t=perf_counter()
            nodes,zeros,nontrivial=circuit_test(h,g,bnd,root)
            print(name,'root',root,'bound',bnd,'nodes',nodes,'zero_leaves',zeros,
                  'nontrivial',len(nontrivial),'seconds',round(perf_counter()-t,3),flush=True)
            assert not nontrivial
    print('CERTIFIED: base [[78,4,6]], cover [[156,4,14]], 14 > 2*6.',flush=True)

if __name__=='__main__':run()
