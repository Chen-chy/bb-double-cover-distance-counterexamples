#!/usr/bin/env python3
"""Exact GF(2) checks of the two-generator 2-primary twisted-Frobenius lemma.
These are sanity checks of explicit witnesses, NOT minimum-distance certificates.
The accompanying uniform proof does not depend on these finite tests.
"""
from __future__ import annotations
import itertools, json, math, random, time
from pathlib import Path

class Ring:
    def __init__(self, periods):
        self.periods=tuple(periods)
        self.coords=list(itertools.product(*(range(m) for m in self.periods)))
        self.index={v:i for i,v in enumerate(self.coords)}
        self.n=len(self.coords); self.zero=tuple(0 for _ in self.periods)
    def add(self,a,b): return tuple((x+y)%m for x,y,m in zip(a,b,self.periods))
    def scale(self,a,n): return tuple(x*n%m for x,m in zip(a,self.periods))
    def poly(self,vs):
        out=set()
        for v in vs:
            if v in out:out.remove(v)
            else:out.add(v)
        return out
    def mul(self,a,b):return self.poly(self.add(x,y) for x in a for y in b)
    def power(self,a,n):
        out={self.zero}
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n>>=1
        return out
    def translate_bits(self,p,g):
        return sum(1<<self.index[self.add(t,g)] for t in p)
    def bits(self,p):return sum(1<<self.index[v] for v in p)

def echelon(columns):
    piv={}
    for v in columns:
        while v:
            j=v.bit_length()-1
            if j in piv:v^=piv[j]
            else:piv[j]=v;break
    return piv

def residual(v,piv):
    while v:
        j=v.bit_length()-1
        if j not in piv:return v
        v^=piv[j]
    return 0

def generates(M,N,t,s):
    # Exhaustive closure, independent of invariant-factor assumptions.
    return len({((i*t[0]+j*s[0])%M,(i*t[1]+j*s[1])%N)
                for i in range(M) for j in range(M)})==M*N

def check_case(M,N,q,t,s,odd=1,ot=0,os=0):
    R=Ring((3*M,3*N,odd)); z=R.zero
    x=(1,0,0);y=(0,1,0);g=(3,0,0)
    tt=(3*t[0]%(3*M),3*t[1]%(3*N),ot%odd)
    ss=(3*s[0]%(3*M),3*s[1]%(3*N),os%odd)
    A={z,x,y};B=R.poly([z,R.add(tt,R.scale(x,q)),R.add(ss,R.scale(y,q))])
    assert len(B)==3
    C=B^R.power(A,q)
    E={(0,0,j) for j in range(odd)}
    S=R.mul(R.mul(E,R.power({z,g} if M>1 else set(),M-N)),R.power(C,N-1))
    U=R.mul(S,R.power(A,q-1));V=S
    assert not (R.mul(A,U)^R.mul(B,V)), ('syndrome',M,N,q,t,s,odd)
    assert len(S)<=odd*M*N
    r=q.bit_length()-1
    assert q==1<<r
    assert len(U)+len(V)<=odd*M*N*(1+3**r)
    bnd=echelon(R.translate_bits(B,h)|(R.translate_bits(A,h)<<R.n) for h in R.coords)
    k=2*R.n-2*len(bnd)
    assert k>0
    w=R.bits(U)|(R.bits(V)<<R.n)
    assert residual(w,bnd), ('boundary',M,N,q,t,s,odd)
    return {'M':M,'N':N,'q':q,'t':t,'s':s,'odd_order':odd,
            'odd_twists':[ot,os], 'n':2*R.n,'k':k,
            'S_weight':len(S),'logical_weight':len(U)+len(V),
            'proved_weight_bound':odd*M*N*(1+3**r)}

def main():
    rng=random.Random(20260906);results=[];start=time.time()
    for M,N in [(1,1),(2,1),(2,2),(4,1),(4,2),(4,4),(8,1),(8,2),(8,4),(8,8),(16,1),(16,2)]:
        elems=list(itertools.product(range(M),range(N)))
        pairs=[(t,s) for t in elems for s in elems if generates(M,N,t,s)]
        if len(pairs)>20:pairs=rng.sample(pairs,20)
        for t,s in pairs:
            for q in (1,2,4,8):results.append(check_case(M,N,q,t,s))
    for M,N in [(1,1),(2,1),(2,2),(4,1),(4,2)]:
        t=(1%M,0);s=(0,1%N)
        for odd in (3,5):
            for q in (1,2,4):
                results.append(check_case(M,N,q,t,s,odd,1,2))
    report={'description':'Exact witness checks; no minimum distances computed',
            'cases':len(results),'all_zero_syndrome':True,'all_nonboundary':True,
            'max_qubits':max(v['n'] for v in results),
            'two_primary_invariants':sorted({(v['M'],v['N']) for v in results}),
            'frobenius_powers':[1,2,4,8], 'odd_norm_orders':[1,3,5],
            'seconds':round(time.time()-start,3),'details':results}
    path=Path(__file__).with_name('twist_verification.json');path.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='details'},indent=2),flush=True)

if __name__=='__main__':main()
