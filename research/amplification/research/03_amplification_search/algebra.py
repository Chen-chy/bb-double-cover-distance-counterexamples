"""Exact finite abelian group-algebra arithmetic and independent BB matrices."""
from __future__ import annotations
from dataclasses import dataclass


def support(x: int) -> list[int]:
    out=[]
    while x:
        bit=x&-x;out.append(bit.bit_length()-1);x^=bit
    return out


def poly(exponents) -> int:
    p=0
    for e in exponents:p^=1<<int(e)
    return p


class Span:
    def __init__(self, vectors=()):
        self.piv={}
        for v in vectors:self.add(v)
    def reduce(self,v):
        # Fully reduce even when a leading bit is not a pivot.
        for p in sorted(self.piv,reverse=True):
            if v>>p&1:v^=self.piv[p]
        return v
    def add(self,v):
        v=self.reduce(v)
        if v:self.piv[v.bit_length()-1]=v
    def contains(self,v):return self.reduce(v)==0
    def __len__(self):return len(self.piv)


def kernel(columns: list[int]) -> list[int]:
    piv={};basis=[]
    for j,s in enumerate(columns):
        v=1<<j
        while s:
            p=s.bit_length()-1
            if p not in piv:piv[p]=(s,v);break
            t,w=piv[p];s^=t;v^=w
        if s==0:basis.append(v)
    return basis


@dataclass(frozen=True)
class Group:
    l:int
    m:int=1
    @property
    def size(self):return self.l*self.m
    def pos(self,x,y=0):return (x%self.l)*self.m+(y%self.m)
    def from_coords(self,coords):return poly(self.pos(x,y) for x,y in coords)
    def shift(self,v,x,y=0):
        return poly(self.pos(i//self.m+x,i%self.m+y) for i in support(v))
    def mul(self,a,b):
        out=0
        for i in support(a):out^=self.shift(b,i//self.m,i%self.m)
        return out


class Code:
    def __init__(self,G:Group,A:int,B:int):
        self.G,self.A,self.B=G,A,B;self.M=G.size;self.mask=(1<<self.M)-1
        self.cols=[G.shift(C,j//G.m,j%G.m) for C in (A,B) for j in range(self.M)]
        self.boundary_vectors=[self.cols[self.M+j]|(self.cols[j]<<self.M) for j in range(self.M)]
        self.bd=Span(self.boundary_vectors)
        self.cycles=kernel(self.cols)
        self.k=len(self.cycles)-len(self.bd)
        assert self.k==2*(self.M-len(self.bd))
    def cycle(self,z):
        u,v=z&self.mask,z>>self.M
        return self.G.mul(self.A,u)^self.G.mul(self.B,v)==0
    def logical(self,z):return self.cycle(z) and not self.bd.contains(z)
