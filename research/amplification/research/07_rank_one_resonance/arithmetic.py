"""Exact F_2 polynomial / Laurent and finite double-cover arithmetic."""
from __future__ import annotations

def terms(p:int)->list[int]:
    out=[]
    while p:
        x=p&-p; out.append(x.bit_length()-1); p^=x
    return out

def poly(exponents)->int:
    p=0
    for e in exponents:
        if e<0: raise ValueError('Use Laurent supports for negative exponents.')
        p^=1<<e
    return p

def pmul(a:int,b:int)->int:
    ans=0
    while b:
        x=b&-b; ans^=a<<(x.bit_length()-1); b^=x
    return ans

def pdivmod(a:int,b:int)->tuple[int,int]:
    if b==0: raise ZeroDivisionError
    q=0
    while a and a.bit_length()>=b.bit_length():
        s=a.bit_length()-b.bit_length(); q^=1<<s; a^=b<<s
    return q,a

def quo(a:int,b:int)->int:
    q,r=pdivmod(a,b)
    if r: raise AssertionError(('inexact division',terms(a),terms(b),terms(r)))
    return q

def rem(a:int,b:int)->int:return pdivmod(a,b)[1]

def pgcd(a:int,b:int)->int:
    while b:a,b=b,rem(a,b)
    return a

def egcd(a:int,b:int)->tuple[int,int,int]:
    x0,x1,y0,y1=1,0,0,1
    while b:
        q,r=pdivmod(a,b); a,b=b,r
        x0,x1=x1,x0^pmul(q,x1); y0,y1=y1,y0^pmul(q,y1)
    return a,x0,y0

def deriv(a:int)->int:return poly(i-1 for i in terms(a) if i%2)

def degree(a:int)->int:return a.bit_length()-1

def lx(a,b):return set(a)^set(b)

def lm(a,b):
    out=set()
    for x in a:
        for y in b:
            z=x+y
            if z in out:out.remove(z)
            else:out.add(z)
    return out

def ls(a,s):return {i+s for i in a}

def le(a):return {i for i in a if i%2}

def lq(n:int,g:int):
    assert g>0 and n%g==0
    p=n//g
    return {g*i for i in (range(p) if p>=0 else range(p,0))}

def lmod(a,modulus:int)->int:
    if not a:return 0
    low=min(a)
    p=poly(i-low for i in a)
    p=rem(p,modulus)
    one,z_inv,_=egcd(2,modulus)
    assert one==1
    unit=2 if low>=0 else z_inv
    for _ in range(abs(low)):p=rem(pmul(p,unit),modulus)
    return p

class Span:
    def __init__(self,vs=()):
        self.p={}
        for v in vs:self.add(v)
    def reduce(self,v:int)->int:
        for k in sorted(self.p,reverse=True):
            if v>>k&1:v^=self.p[k]
        return v
    def add(self,v:int)->bool:
        v=self.reduce(v)
        if v:self.p[v.bit_length()-1]=v;return True
        return False
    def contains(self,v:int)->bool:return self.reduce(v)==0
    def __len__(self):return len(self.p)
    def separator(self,v:int,n:int)->int:
        """Produce lambda with lambda.boundaries=0 and lambda.v=1."""
        r=self.reduce(v)
        if not r:raise ValueError('vector is in span')
        target=r.bit_length()-1
        # coefficient of target in the fully reduced basis vectors
        return sum(1<<j for j in range(n) if self.reduce(1<<j)>>target&1)

class Cover:
    """Group <z,t | t^2=1, z^L=t^kappa>, coordinates (z-exponent, sheet)."""
    def __init__(self,L:int,kappa:int,A:int,B:int,delta:int):
        if L<1 or kappa not in (0,1) or delta not in (0,1):raise ValueError
        self.L,self.kappa,self.N=L,kappa,2*L
        self.mask=(1<<self.N)-1
        self.A=self.encode(terms(A^1),0)^self.encode([0],1)
        # B+delta epsilon
        self.B=self.encode(terms(B^delta),0)^(self.encode([0],1) if delta else 0)
        if self.A.bit_count()!=3 or self.B.bit_count()!=3:raise ValueError('term collision')
        self.columns=[self.shift(C,e,t) for C in (self.A,self.B) for t in (0,1) for e in range(L)]
        self.boundaries=[self.shift(self.B,e,t)|(self.shift(self.A,e,t)<<self.N) for t in (0,1) for e in range(L)]
        self.bd=Span(self.boundaries)
        self.k=2*(self.N-len(self.bd))
    def pos(self,e:int,t:int=0)->int:
        q,r=divmod(e,self.L)
        return r+self.L*((t+self.kappa*q)%2)
    def encode(self,support,t:int=0)->int:return poly(self.pos(e,t) for e in support)
    def shift(self,v:int,e:int,t:int=0)->int:
        return poly(self.pos(i%self.L+e,i//self.L+t) for i in terms(v))
    def mul(self,a:int,b:int)->int:
        out=0
        for i in terms(b):out^=self.shift(a,i%self.L,i//self.L)
        return out
    def encode_physical(self,parts)->int:
        u=self.encode(parts[0],0)^self.encode(parts[1],1)
        v=self.encode(parts[2],0)^self.encode(parts[3],1)
        return u|(v<<self.N)
    def encode_epsilon(self,u,v,p,q)->int:
        return self.encode_physical((lx(u,p),p,lx(v,q),q))
    def cycle(self,z:int)->bool:
        return (self.mul(self.A,z&self.mask)^self.mul(self.B,z>>self.N))==0
    def logical(self,z:int)->bool:return self.cycle(z) and not self.bd.contains(z)
    def certificate(self,z:int,meta:dict)->dict:
        assert self.logical(z)
        dual=self.bd.separator(z,2*self.N)
        assert (dual&z).bit_count()%2==1
        return dict(meta,L=self.L,kappa=self.kappa,k=self.k,A_support=terms(self.A),B_support=terms(self.B),
                    witness=terms(z),dual=terms(dual),physical_weight=z.bit_count())

def data(A:int,B:int,delta:int,L:int,kappa:int)->dict:
    c=pgcd(A,B);a=quo(A,c);b=quo(B,c)
    E=pgcd(c,b^(a if delta else 0));G=pmul(c,E)
    assert G==pgcd(pmul(A,A),B^(A if delta else 0))
    F=(1<<L)|1;g0=pgcd(c,F);H=pgcd(G,F^(A if kappa else 0))
    R=quo(B^(A if delta else 0),G);S=quo(pmul(A,A),G);P=quo(pmul(A,B),G)
    gen=(P^R,R,S,0);bd=(B^delta,delta,A^1,1)
    return dict(c=c,a=a,b=b,E=E,G=G,F=F,g0=g0,H=H,gen=gen,bd=bd)

def conv_parts(gen,f:int,bd=None,h:int=0):
    if bd is None:bd=(0,0,0,0)
    return tuple(set(terms(pmul(x,f)^pmul(y,h))) for x,y in zip(gen,bd))

def universal_cycle(A:int,B:int,delta:int,parts)->bool:
    # Physical group basis, without imposing any free period.
    a0=set(terms(A^1));a1={0};b0=set(terms(B^delta));b1={0} if delta else set()
    u0,u1,v0,v1=map(set,parts)
    s0=lm(a0,u0)^lm(a1,u1)^lm(b0,v0)^lm(b1,v1)
    s1=lm(a0,u1)^lm(a1,u0)^lm(b0,v1)^lm(b1,v0)
    return not s0 and not s1

def lnormalize(a):
    a=set(a)
    if not a:return 0,0
    shift=min(a)
    return poly(i-shift for i in a),shift

def lgcd(a,b):return pgcd(lnormalize(a)[0],lnormalize(b)[0])

def lquo(a,b:int):
    p,shift=lnormalize(a)
    return ls(terms(quo(p,b)),shift)

def ldata(A,B,delta,L,kappa):
    A,B=set(A),set(B)
    c=lgcd(A,B);a=lquo(A,c);b=lquo(B,c)
    E=lgcd(terms(c),b^(a if delta else set()));G=pmul(c,E)
    assert G==lgcd(lm(A,A),B^(A if delta else set()))
    g0=pgcd(c,(1<<L)|1);H=lgcd(terms(G),{0,L}^(A if kappa else set()))
    R=lquo(B^(A if delta else set()),G);S=lquo(lm(A,A),G);P=lquo(lm(A,B),G)
    return dict(c=c,a=a,b=b,E=E,G=G,g0=g0,H=H,gen=(P^R,R,S,set()),
                bd=(B^({0} if delta else set()),{0} if delta else set(),A^{0},{0}))

class LaurentCover(Cover):
    def __init__(self,L,kappa,A,B,delta):
        self.L,self.kappa,self.N=L,kappa,2*L
        self.mask=(1<<self.N)-1
        self.A=self.encode(set(A)^{0},0)^self.encode([0],1)
        self.B=self.encode(set(B)^({0} if delta else set()),0)^(self.encode([0],1) if delta else 0)
        if self.A.bit_count()!=3 or self.B.bit_count()!=3:raise ValueError('term collision')
        self.columns=[self.shift(C,e,t) for C in (self.A,self.B) for t in (0,1) for e in range(L)]
        self.boundaries=[self.shift(self.B,e,t)|(self.shift(self.A,e,t)<<self.N) for t in (0,1) for e in range(L)]
        self.bd=Span(self.boundaries)
        self.k=2*(self.N-len(self.bd))

def universal_lcycle(A,B,delta,parts):
    a0=set(A)^{0};a1={0};b0=set(B)^({0} if delta else set());b1={0} if delta else set()
    u0,u1,v0,v1=map(set,parts)
    return not(lm(a0,u0)^lm(a1,u1)^lm(b0,v0)^lm(b1,v1)) and not(lm(a0,u1)^lm(a1,u0)^lm(b0,v1)^lm(b1,v0))

def eps_parts(u,v,p,q):return (set(u)^set(p),set(p),set(v)^set(q),set(q))
