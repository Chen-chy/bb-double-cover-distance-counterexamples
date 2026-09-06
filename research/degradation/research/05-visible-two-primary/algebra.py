"""Exact binary linear algebra and small finite group-algebra tests."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Iterable

class Span:
    def __init__(self, vs: Iterable[int] = ()):
        self.rows: dict[int,int] = {}
        for v in vs: self.add(v)
    def reduce(self, v: int) -> int:
        # Full reduction (not only until the first missing pivot).
        for p in sorted(self.rows, reverse=True):
            if (v >> p) & 1: v ^= self.rows[p]
        return v
    def add(self, v: int) -> bool:
        while v:
            p=v.bit_length()-1
            if p in self.rows: v ^= self.rows[p]
            else:
                self.rows[p]=v
                return True
        return False
    def __len__(self): return len(self.rows)
    def vectors(self): return list(self.rows.values())

def kernel(columns: list[int]) -> list[int]:
    basis: dict[int,tuple[int,int]]={}; out=[]
    for i,col in enumerate(columns):
        v=col; w=1<<i
        while v:
            p=v.bit_length()-1
            if p in basis:
                vv,ww=basis[p]; v ^= vv; w ^= ww
            else:
                basis[p]=(v,w); break
        if not v: out.append(w)
    return out

def quotient_basis(vectors: Iterable[int], subspace: Span) -> list[int]:
    return Span(subspace.reduce(v) for v in vectors).vectors()

@dataclass
class Field:
    degree: int = 2
    modulus: int = 7
    def mul(self,a:int,b:int)->int:
        r=0
        while b:
            if b&1:r ^= a
            a <<= 1
            if a & (1<<self.degree):a ^= self.modulus
            b >>= 1
        return r

@dataclass
class GroupRing:
    M: int
    N: int
    field: Field
    @property
    def size(self):return self.M*self.N
    @property
    def bits(self):return self.size*self.field.degree
    def poly(self, terms:list[tuple[int,int,int]])->int:
        r=0;d=self.field.degree
        for coeff,i,j in terms:r ^= coeff << (d*((i%self.M)*self.N+(j%self.N)))
        return r
    def shift(self,v:int,di:int,dj:int,blocks:int=1)->int:
        d=self.field.degree;mask=(1<<d)-1;r=0
        for block in range(blocks):
            vv=(v>>(block*self.bits)) & ((1<<self.bits)-1)
            while vv:
                bit=(vv & -vv).bit_length()-1;cell=bit//d
                c=(vv>>(d*cell))&mask
                vv ^= c<<(d*cell)
                i,j=divmod(cell,self.N)
                idx=block*self.size+((i+di)%self.M)*self.N+(j+dj)%self.N
                r ^= c<<(d*idx)
        return r
    def scalar(self,v:int,c:int,blocks:int=1)->int:
        d=self.field.degree;mask=(1<<d)-1;r=0
        while v:
            bit=(v&-v).bit_length()-1;cell=bit//d
            z=(v>>(d*cell))&mask;v ^= z<<(d*cell)
            r ^= self.field.mul(z,c)<<(d*cell)
        return r
    def columns(self,p:int)->list[int]:
        return [self.scalar(self.shift(p,i,j),1<<k)
                for i in range(self.M) for j in range(self.N)
                for k in range(self.field.degree)]
    def project(self,v:int,base:'GroupRing',blocks:int=1)->int:
        assert self.N==base.N and self.M%base.M==0 and self.field==base.field
        d=self.field.degree;mask=(1<<d)-1;r=0
        for block in range(blocks):
            vv=(v>>(block*self.bits))&((1<<self.bits)-1)
            while vv:
                bit=(vv&-vv).bit_length()-1;cell=bit//d
                c=(vv>>(d*cell))&mask;vv ^= c<<(d*cell)
                i,j=divmod(cell,self.N)
                r ^= c<<(d*(block*base.size+(i%base.M)*base.N+j))
        return r

def code_data(r:GroupRing,A:int,B:int,homology:bool=True)->dict:
    ac=r.columns(A);bc=r.columns(B)
    check=Span(ac+bc)
    h0=quotient_basis((1<<i for i in range(r.bits)),check)
    ans={'m':len(h0)//r.field.degree,'check':check,'h0':h0}
    assert len(h0)%r.field.degree==0
    if homology:
        boundaries=Span(b | (a<<r.bits) for a,b in zip(ac,bc))
        cycles=kernel(ac+bc)
        h1=quotient_basis(cycles,boundaries)
        assert len(h1)==2*len(h0)
        ans.update(boundaries=boundaries,cycles=cycles,h1=h1)
    return ans

def loewy_profile(r:GroupRing,basis:list[int],subspace:Span,blocks:int)->list[int]:
    cur=basis;out=[]
    for _ in range(r.M+r.N+2):
        out.append(len(cur))
        if not cur:return out
        cur=quotient_basis((r.shift(v,i,j,blocks)^v for v in cur for i,j in [(1,0),(0,1)]),subspace)
    raise AssertionError('Nilpotent radical failed to terminate')
