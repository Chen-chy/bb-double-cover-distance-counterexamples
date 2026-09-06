"""Finite adversarial checks for the universal cyclic generator and cover witness.

Uses only standard-library exact binary arithmetic. It checks explicit cycles
and supplies dual separating certificates for non-boundaries. It does not
compute minimum distances, and these checks are not inputs to the theorem.
"""
from __future__ import annotations
from itertools import product
from math import gcd,lcm
from pathlib import Path
import json,random


def bits(v):
    while v:
        t=v & -v;yield t.bit_length()-1;v ^= t


class Group:
    def __init__(self,L,M):self.L=L;self.M=M;self.n=L*M
    def pos(self,x,y):return (x%self.L)*self.M+y%self.M
    def coords(self,i):return divmod(i,self.M)
    def add(self,a,b):
        x,y=self.coords(a);u,v=self.coords(b);return self.pos(x+u,y+v)
    def scale(self,a,c):
        x,y=self.coords(a);return self.pos(c*x,c*y)
    def order(self,a):
        x,y=self.coords(a);return lcm(self.L//gcd(x,self.L),self.M//gcd(y,self.M))
    def shift(self,v,a):
        out=0
        for i in bits(v):out ^= 1 << self.add(i,a)
        return out
    def mul(self,a,b):
        if a.bit_count()<b.bit_count():a,b=b,a
        out=0
        for j in bits(b):out ^= self.shift(a,j)
        return out
    def power(self,a,k):
        out=1
        while k:
            if k & 1:out=self.mul(out,a)
            a=self.mul(a,a);k >>= 1
        return out
    def poly(self,positions):
        out=0
        for p in positions:out ^= 1 << p
        return out


class Span:
    def __init__(self,vs=()):
        self.rows={}
        for v in vs:
            while v:
                p=v.bit_length()-1
                if p in self.rows:v ^= self.rows[p]
                else:self.rows[p]=v;break
    def reduce(self,v):
        for p in sorted(self.rows,reverse=True):
            if v>>p & 1:v ^= self.rows[p]
        return v
    def separates(self,z):
        r=self.reduce(z)
        if not r:return None
        # Construct the corresponding row of the reduction map, rather than
        # merely declaring that a nonzero remainder proves non-membership.
        j=r.bit_length()-1;phi=1 << j
        for p in sorted(self.rows):
            if (self.rows[p] & phi).bit_count() & 1:phi ^= 1 << p
        assert (phi & z).bit_count() & 1
        return phi


class Code:
    def __init__(self,G,A,B):
        self.G=G;self.A=A;self.B=B;self.n=G.n;self.mask=(1<<G.n)-1
        self.bdvec=[G.shift(B,i)|(G.shift(A,i)<<G.n) for i in range(G.n)]
        self.bd=Span(self.bdvec);self.k=2*(G.n-len(self.bd.rows))
    def syndrome(self,z):return self.G.mul(self.A,z&self.mask)^self.G.mul(self.B,z>>self.n)
    def certificate(self,z):
        if self.syndrome(z):return None
        phi=self.bd.separates(z)
        if phi is None:return None
        # Directly verified dual witness: no reliance on how phi was found.
        assert all((phi&b).bit_count()%2==0 for b in self.bdvec)
        assert (phi&z).bit_count()%2==1
        return phi


def odd_part(G,a):
    n=G.order(a);p=n & -n;o=n//p
    if o==1:return 0
    exponent=p*pow(p,-1,o)
    return G.scale(a,exponent)


def subgroup(G,gens):
    H={0};todo=[0]
    while todo:
        a=todo.pop()
        for b in gens:
            c=G.add(a,b)
            if c not in H:H.add(c);todo.append(c)
    return sorted(H)


def embed(G,H,i):
    return H.pos(*G.coords(i))


def odd_lift(G,H,i,deck):
    a=embed(G,H,i)
    if H.order(a)%2==0:a=H.add(a,deck)
    assert H.order(a)==G.order(i) and H.order(a)%2==1
    return a


def check_instance(G,q,h,k,sheetmask,direction):
    X=G.pos(1,0);Y=G.pos(0,1)
    ap=[0,X,Y];bp=[0,G.add(h,G.scale(X,q)),G.add(k,G.scale(Y,q))]
    A=G.poly(ap);B=G.poly(bp)
    if A.bit_count()!=3 or B.bit_count()!=3:return None
    Hodd=subgroup(G,[odd_part(G,h),odd_part(G,k)])
    e=G.poly(Hodd)
    M=max(G.order(h)&-G.order(h),G.order(k)&-G.order(k))
    m=q*M;n=M
    base=Code(G,A,B)
    u=G.mul(e,G.power(A,m-1));v=G.mul(e,G.power(B,n-1));z=u|(v<<G.n)
    phi=base.certificate(z)
    if phi is None:return None
    coverG=Group(G.L*(2 if direction==0 else 1),G.M*(2 if direction==1 else 1))
    deck=coverG.pos(G.L,0) if direction==0 else coverG.pos(0,G.M)
    def lift_terms(pp,offset):
        out=[embed(G,coverG,p) for p in pp]
        for j in (1,2):
            if sheetmask >> (offset+j-1)&1:out[j]=coverG.add(out[j],deck)
        return coverG.poly(out)
    AA=lift_terms(ap,0);BB=lift_terms(bp,2)
    ee=coverG.poly(odd_lift(G,coverG,i,deck) for i in Hodd)
    UU=coverG.mul(ee,coverG.power(AA,m-1));VV=coverG.mul(ee,coverG.power(BB,n-1))
    epsU=UU^coverG.shift(UU,deck);epsV=VV^coverG.shift(VV,deck)
    candidates=[('projection',UU|(VV<<coverG.n)),
                ('deck_projection',coverG.shift(UU,deck)|(VV<<coverG.n)),
                ('transfer',epsU|(epsV<<coverG.n))]
    cover=Code(coverG,AA,BB)
    result=None
    for label,w in candidates:
        psi=cover.certificate(w)
        if psi is not None:
            result=(label,w,psi);break
    assert result is not None,(G.L,G.M,q,h,k,M,sheetmask,direction)
    bound=2*len(Hodd)*(3**(m.bit_length()-1)+3**(n.bit_length()-1))
    label,w,psi=result
    assert w.bit_count()<=bound
    return {'periods':[G.L,G.M],'q':q,'h':G.coords(h),'k':G.coords(k),
            'odd_subgroup_size':len(Hodd),'M':M,'sheetmask':sheetmask,
            'doubling_direction':direction,'base_k':base.k,'cover_k':cover.k,
            'branch':label,'base_cycle_weight':z.bit_count(),'cover_witness_weight':w.bit_count(),
            'symbolic_bound':bound,'base_cycle':hex(z),'base_dual':hex(phi),
            'cover_cycle':hex(w),'cover_dual':hex(psi),
            'A':list(bits(A)),'B':list(bits(B)),
            'cover_A':list(bits(AA)),'cover_B':list(bits(BB))}


def main():
    rng=random.Random(20260906);records=[];tested=0
    periods=[(3,3),(3,6),(6,3),(6,6),(4,6),(6,8),(9,6),(12,3),(9,12),(12,6)]
    for L,N in periods:
        G=Group(L,N)
        choices=[0,G.pos(L//2,0) if L%2==0 else 0,
                 G.pos(0,N//2) if N%2==0 else 0,
                 G.pos(L//3,0) if L%3==0 else 0,
                 G.pos(0,N//3) if N%3==0 else 0]
        choices=list(set(choices))
        pairs=list(product(choices,repeat=2));rng.shuffle(pairs)
        for h,k in pairs[:8]:
            for q in (1,2,4):
                # Four distinct sheet masks, both doubling directions, including
                # unchanged representatives and odd/even coordinate periods.
                for mask in (0,3,5,15):
                    for direction in (0,1):
                        tested+=1
                        row=check_instance(G,q,h,k,mask,direction)
                        if row:records.append(row)
    assert records
    counts={}
    for r in records:counts[r['branch']]=counts.get(r['branch'],0)+1
    out={'seed':20260906,'parameter_checks':tested,'nontrivial_base_generator_cases':len(records),
         'branches':counts,'odd_norm_cases':sum(r['odd_subgroup_size']>1 for r in records),
         'even_coordinate_covers':sum(r['periods'][r['doubling_direction']]%2==0 for r in records),
         'statement':'Exact finite logical and dual-witness checks; no distance claims.'}
    here=Path(__file__).parent
    (here/'finite_cover_summary.json').write_text(json.dumps(out,indent=2)+'\n')
    (here/'finite_cover_certificates.json').write_text(json.dumps(records,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
