"""Exact binary polynomial and univariate BB arithmetic (Python integers)."""
from itertools import combinations
from math import gcd as igcd

def poly(exponents):
    a=0
    for i in exponents:
        if i<0: raise ValueError('negative exponent')
        a ^= 1 << i
    return a

def terms(a):
    out=[]
    while a:
        b=a & -a; out.append(b.bit_length()-1); a ^=b
    return out

def mul(a,b):
    if a.bit_count()<b.bit_count(): a,b=b,a
    c=0
    while b:
        t=b & -b; c ^= a << (t.bit_length()-1); b ^=t
    return c

def divmod_poly(a,b):
    if not b: raise ZeroDivisionError
    q=0; db=b.bit_length()
    while a.bit_length()>=db:
        j=a.bit_length()-db; q^=1<<j; a^=b<<j
    return q,a

def mod(a,b): return divmod_poly(a,b)[1]
def quo(a,b):
    q,r=divmod_poly(a,b)
    if r: raise ValueError('not divisible')
    return q

def gcd(a,b):
    while b: a,b=b,mod(a,b)
    return a

def egcd(a,b):
    s0,s1,t0,t1=1,0,0,1
    while b:
        q,r=divmod_poly(a,b); a,b=b,r
        s0,s1=s1,s0^mul(q,s1); t0,t1=t1,t0^mul(q,t1)
    return a,s0,t0

def rot(a,i,L):
    i%=L; mask=(1<<L)-1
    return ((a<<i)&mask) | (a>>(L-i)) if i else a

def cmul(a,b,L):
    a=mod(a,(1<<L)|1); c=0
    while b:
        t=b&-b; c^=rot(a,t.bit_length()-1,L); b^=t
    return c

def echelon(vectors):
    bas={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p in bas: v^=bas[p]
            else:
                bas[p]=v; break
    return bas

def reduce(v,bas):
    for p in sorted(bas,reverse=True):
        if (v>>p)&1: v^=bas[p]
    return v

class BB:
    def __init__(self,L,A,B):
        self.L=L; self.F=(1<<L)|1; self.mask=(1<<L)-1
        self.A=mod(A,self.F); self.B=mod(B,self.F)
        self.cols=[rot(self.A,i,L) for i in range(L)]+[rot(self.B,i,L) for i in range(L)]
        self.boundaries=[rot(self.B,i,L)|(rot(self.A,i,L)<<L) for i in range(L)]
        self.bas=echelon(self.boundaries)
        self.g=gcd(gcd(self.A,self.B),self.F)
        self.k=2*(self.g.bit_length()-1)
        assert self.k==2*(L-len(self.bas))
    def cycle(self,v):
        return (cmul(self.A,v&self.mask,self.L)^cmul(self.B,v>>self.L,self.L))==0
    def logical(self,v):
        return self.cycle(v) and bool(reduce(v,self.bas))
    def hom_label(self,v): return reduce(v,self.bas)
    def min_weight_upto6(self,first_only=True):
        # Every word of even weight <=6 can be divided into subsets of size <=3.
        # Odd weights cannot be cycles if all columns have odd weight.
        cols=self.cols; n=len(cols)
        records={0:[0]}; found=[]
        best=7
        for w in range(1,4):
            for inds in combinations(range(n),w):
                s=0;v=0
                for i in inds: s^=cols[i];v|=1<<i
                for old in records.get(s,[]):
                    z=v^old; wt=z.bit_count()
                    if wt and wt<=min(6,best) and reduce(z,self.bas):
                        if wt<best: best=wt;found=[]
                        found.append(z)
                        if first_only and wt==2: return best,found
                records.setdefault(s,[]).append(v)
        return (best,sorted(set(found))) if found else (None,[])

if __name__=='__main__':
    A=poly([0,8,25]); B=poly([0,2,13])
    print('ordinary gcd',terms(gcd(A,B)))
    for L in [39,78]:
        c=BB(L,A,B)
        print('L,k,g:',L,c.k,terms(c.g),flush=True)
        d,ws=c.min_weight_upto6()
        print('min <=6:',d,'count',len(ws),flush=True)
        if ws:
            w=ws[0]; print('witness',terms(w&c.mask),terms(w>>L),flush=True)
