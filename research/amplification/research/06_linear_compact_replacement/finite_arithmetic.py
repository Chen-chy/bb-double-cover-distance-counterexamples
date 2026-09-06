"""Binary bivariate arithmetic retained from the supplied compact-survival bundle.
Used only to construct finite certificates; the separate auditor imports none
of these routines. The lower-distance theorem is symbolic.
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

