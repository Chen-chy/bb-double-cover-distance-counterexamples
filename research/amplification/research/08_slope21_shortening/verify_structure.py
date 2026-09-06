#!/usr/bin/env python3
"""Exact identities and finite homology checks for the slope-(2,1) report.
Uses an independent sparse multivariate ring for all universal identities.
"""
from __future__ import annotations
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent

# Group algebra F_2[X^+-1,Y^+-1,H^+-1,t]/(t^2-1).
Mon=tuple[int,int,int,int]
Poly=frozenset[Mon]
ZERO:Poly=frozenset()
def mon(x=0,y=0,h=0,t=0)->Poly:return frozenset([(x,y,h,t%2)])
def add(*ps:Poly)->Poly:
    q=set()
    for p in ps:q.symmetric_difference_update(p)
    return frozenset(q)
def mul(a:Poly,b:Poly)->Poly:
    q=set()
    for v in a:
        for w in b:
            z=(v[0]+w[0],v[1]+w[1],v[2]+w[2],(v[3]+w[3])%2)
            if z in q:q.remove(z)
            else:q.add(z)
    return frozenset(q)

def universal_identities()->dict:
    one=mon();X=mon(x=1);Y=mon(y=1);H=mon(h=1);t=mon(t=1)
    A=add(one,X,Y);B=add(one,mul(X,mul(H,H)),mul(Y,H))
    C=add(one,H);D=add(one,mul(X,H))
    Ah=add(t,X,Y);Bh=add(t,mul(X,mul(H,H)),mul(Y,H));Dh=add(t,mul(X,H))
    assert add(B,mul(H,A))==mul(C,D)
    assert add(A,D,mul(X,C))==Y
    assert add(Bh,mul(H,Ah))==mul(C,Dh)
    assert add(Ah,Dh,mul(X,C))==Y
    pe=mul(mon(y=-1),D);pj=mul(mon(x=1,y=-1),C)
    phe=mul(mon(y=-1),Dh);phj=pj
    assert add(pe,pj)==add(one,mul(mon(y=-1),A))
    assert mul(pe,pj)==mul(mon(x=1,y=-2),add(B,mul(H,A)))
    assert add(mul(pe,pe),pe)==mul(mon(y=-2),add(A,mul(X,B)))
    assert add(phe,phj)==add(one,mul(mon(y=-1),Ah))
    assert mul(phe,phj)==mul(mon(x=1,y=-2),add(Bh,mul(H,Ah)))
    assert add(mul(phe,phe),phe)==mul(mon(y=-2),add(mul(t,Ah),mul(X,Bh)))
    assert all(len(p)==2 for p in (pe,pj,phe,phj))
    return {'identities':10,'all_exact':True,'projector_monomials':[2,2,2,2]}

# Finite F_2 vector algebra; does not use the trellis generator or auditor.
def poly(exps):
    z=0
    for x in exps:z^=1<<x
    return z
def pmul(a,b):
    z=0
    while a:
        s=(a&-a).bit_length()-1;z^=b<<s;a&=a-1
    return z
def pdiv(a,b):
    q=0
    while a.bit_length()>=b.bit_length():
        s=a.bit_length()-b.bit_length();q^=1<<s;a^=b<<s
    return q,a
def pgcd(a,b):
    while b:a,b=b,pdiv(a,b)[1]
    return a

def explicit_identities()->dict:
    e=7;j=11;c=pmul(e,j);assert c==49
    assert pgcd(c,8197)==c
    u=poly([0,5,9,10]);v=poly([0,2]);D=poly([0,7])
    p=pmul(D,u);q=pmul(D,v)
    assert p.bit_count()+q.bit_count()==12
    assert pdiv(v,e)[1]!=0 and pdiv(v,j)[1]!=0
    assert pdiv(q,j)[1]==0 and pdiv(q,e)[1]!=0
    pstar=poly([0,3,4,6,7,9,10,12]);qstar=poly([0,2,3,4])
    h=poly([3,4])
    assert p^pstar==pmul(8197,h) and q^qstar==pmul(49,h)
    # Explicit fills for the normalized cover: A*r+B*s=z^4*p+q.
    r=poly([0,2,5,6,9,16]);s=0
    assert pmul(49,r)^pmul(8197,s)==(p<<4)^q
    cost=(r&~p).bit_count()+(s&~q).bit_count();assert cost==2
    rstar=poly([0,4,6,7,9,11,12]);sstar=poly([2,3,4])
    assert pmul(49,rstar)^pmul(8197,sstar)==(pstar<<4)^qstar
    coststar=(rstar&~pstar).bit_count()+(sstar&~qstar).bit_count();assert coststar==1
    return {'base_gcd':c,'base_e':e,'base_j':j,
            'base_purification_weight':12,'projection_boundary_multiplier':[3,4],
            'first_explicit_fill_outside_support':cost,
            'improved_fill_outside_support':coststar,
            'improved_cover_weight':14}

class Span:
    def __init__(self,rows):
        self.basis={}
        for row in rows:
            v=self.reduce(row)
            if v:self.basis[v.bit_length()-1]=v
    def reduce(self,v):
        while v:
            p=v.bit_length()-1
            if p not in self.basis:return v
            v^=self.basis[p]
        return 0

def rot(x,k,L):
    k%=L;mask=(1<<L)-1
    return ((x<<k)&mask)^(x>>(L-k)) if k else x

def solve_dual(rows,witness,n):
    # Solve dot(row,l)=0 for every boundary and dot(witness,l)=1.
    basis={}
    for a,b in [(r,0) for r in rows]+[(witness,1)]:
        while a:
            p=a.bit_length()-1
            if p not in basis:basis[p]=(a,b);break
            aa,bb=basis[p];a^=aa;b^=bb
        else:assert b==0
    v=0
    for p,(a,b) in sorted(basis.items()):
        if ((a&v).bit_count()%2)^b:v^=1<<p
    assert all((r&v).bit_count()%2==0 for r in rows)
    assert (witness&v).bit_count()%2==1
    return v

def finite_check(L=201):
    assert L%2 and L%3==0 and L%7 and L>169
    mask=(1<<L)-1;A=49;B=8197
    F=(1<<L)|1
    assert pgcd(A,F)==7 and pgcd(pmul(7,49),F)==7
    base_boundaries=[rot(B,i,L)|(rot(A,i,L)<<L) for i in range(L)]
    base_span=Span(base_boundaries);assert len(base_span.basis)==L-2
    baseu=poly([0,5,9,10]);basev=poly([0,2])
    baseword=baseu|(basev<<L)
    assert pmul(A,baseu)==pmul(B,basev)
    assert base_span.reduce(baseword)
    def shift(q,i,sheet):
        lo,hi=q&mask,q>>L;lo,hi=rot(lo,i,L),rot(hi,i,L)
        if sheet:lo,hi=hi,lo
        return lo|(hi<<L)
    AC=33|(16<<L);BC=8196|(1<<L)
    cover_boundaries=[shift(BC,i,s)|(shift(AC,i,s)<<(2*L))
                      for s in (0,1) for i in range(L)]
    cover_span=Span(cover_boundaries);assert len(cover_span.basis)==2*L-2
    cases=json.loads((ROOT/'exact_results.json').read_text())
    full=next(r for r in cases if r['name']=='cover_full')
    w=sum(poly(supp)<<(i*L) for i,supp in enumerate(full['result']['physical']))
    assert w.bit_count()==14 and cover_span.reduce(w)
    dual_base=solve_dual(base_boundaries,baseword,2*L)
    dual_cover=solve_dual(cover_boundaries,w,4*L)
    output={'L':L,'base_n':2*L,'cover_n':4*L,'base_k':4,'cover_k':4,
            'base_witness_weight':6,'cover_witness_weight':14,
            'base_dual_hex':hex(dual_base),'cover_dual_hex':hex(dual_cover),
            'dual_boundary_pairings':len(base_boundaries)+len(cover_boundaries)}
    # These are witness/rank checks. The finite lower bounds use the
    # proven unwrapping theorem plus the separate compact certificates.
    return output

if __name__=='__main__':
    result={'universal':universal_identities(),'explicit':explicit_identities(),
            'finite':finite_check()}
    (ROOT/'structure_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
