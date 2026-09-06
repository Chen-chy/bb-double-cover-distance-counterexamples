#!/usr/bin/env python3
"""Exact checks for the two arithmetic-progression Laurent theorems.
Only Python's standard library is used. No distance decoder is used.
"""
from __future__ import annotations
import itertools, json, math, random
from collections import Counter
from pathlib import Path

# Independent sparse Laurent arithmetic: supports are sets, addition is xor.
P = frozenset[int]
def add(*ps:P)->P:
    ans=set()
    for p in ps: ans.symmetric_difference_update(p)
    return frozenset(ans)
def shift(p:P,n:int)->P: return frozenset(i+n for i in p)
def mul(p:P,q:P)->P:
    ans=set()
    for i in p:
        for j in q:
            if i+j in ans: ans.remove(i+j)
            else: ans.add(i+j)
    return frozenset(ans)
def poly(*es:int)->P: return frozenset(es)
ZERO=poly(); ONE=poly(0); C=poly(0,1,2); C2=poly(0,2,4)
def div(p:P,q:P)->P:
    if not q: raise ZeroDivisionError
    if not p:return ZERO
    m=min(p); n=min(q)
    r=set(shift(p,-m)); qq=shift(q,-n); result=set(); d=max(qq)
    while r and max(r)>=d:
        a=max(r)-d; result.add(a);r.symmetric_difference_update(shift(qq,a))
    if r: raise ArithmeticError(f'not divisible: {p}, {q}, remainder {r}')
    return shift(frozenset(result),m-n)
def rem(p:P,q:P)->P:
    # Used only for polynomials and normalized divisors.
    r=set(p); d=max(q)
    assert not r or min(r)>=0
    while r and max(r)>=d:r.symmetric_difference_update(shift(q,max(r)-d))
    return frozenset(r)
def gcd(p:P,q:P)->P:
    p=shift(p,-min(p)) if p else p
    q=shift(q,-min(q)) if q else q
    while q:p,q=q,rem(p,q)
    return p

def radd(x,y):return add(x[0],y[0]),add(x[1],y[1])
def rmul(x,y):return add(mul(x[0],y[0]),mul(x[1],y[1])),add(mul(x[0],y[1]),mul(x[1],y[0]))
def rshift(x,j):return shift(x[0],j),shift(x[1],j)
def a(n):return poly(0,n,2*n)
def at(n):return poly(n,2*n),ONE

def quotient(n):
    # Theta for n=1 (mod 6), Psi for n=-1 (mod 6).
    om=(poly(1,2),ONE) if n%6==1 else (poly(0,1),poly(2))
    prod=rmul(at(n),om)
    ans=(div(prod[0],C2),div(prod[1],C2))
    assert rmul(om,ans)==at(n)
    assert len(ans[0])+len(ans[1])==2*n+(-1 if n%6==1 else 1)
    return ans

def wt(y):return sum(map(len,y))
def syndrome(A,B,y):return radd(rmul(A,(y[0],y[1])),rmul(B,(y[2],y[3])))
def eval4(p):
    # F4: alpha^2+alpha+1=0; alpha^0=1, alpha^1=2, alpha^2=3.
    v=0
    for i in p:v ^= (1,2,3)[i%3]
    return v

def exact_finite(a_,b_,L,y):
    """Separate bit-packed finite matrices, independent of Laurent divisions."""
    def conv(a,b):
        out=0
        while b:
            lo=b&-b; i=lo.bit_length()-1; b^=lo
            # group coordinates: exponent=z + L*s
            zi,si=i%L,i//L
            aa=a
            while aa:
                v=aa&-aa; j=v.bit_length()-1;aa^=v
                out ^= 1<<((zi+j%L)%L + L*(si^(j//L)))
        return out
    def bits(p,ss=0):
        out=0
        for i in p:out ^= 1<<(i%L+L*ss)
        return out
    A=bits(poly(a_,2*a_))^bits(ONE,1)
    B=bits(poly(b_,2*b_))^bits(ONE,1)
    u=bits(y[0])^bits(y[1],1);v=bits(y[2])^bits(y[3],1)
    assert conv(A,u)^conv(B,v)==0
    rows={}
    for i in range(2*L):
        col=conv(B,1<<i)|(conv(A,1<<i)<<(2*L))
        while col:
            j=col.bit_length()-1
            if j in rows:col ^= rows[j]
            else: rows[j]=col;break
    vec=u|(v<<(2*L)); original=vec
    while vec:
        j=vec.bit_length()-1
        if j not in rows:break
        vec^=rows[j]
    assert vec, 'witness was a finite boundary'
    return {'a':a_,'b':b_,'L':L,'cover_n':4*L,'boundary_rank':len(rows),
            'witness_weight':original.bit_count(),'nonboundary':True}

def main():
    counts={}; witnesses=[]
    # Quotient identities and coefficient-count claims, both orientations.
    ns=[n for n in range(1,302) if n%6 in (1,5)]
    for n in ns:quotient(n)
    counts['quotient_identities']=len(ns)
    for n in ns:
        q=div(a(n),C)
        assert len(q)==(4*n+(-1 if n%3==1 else 1))//3
    counts['base_quotient_counts']=len(ns)

    pairs=[]
    for aa in range(1,80,2):
        for bb in range(aa+2,100,2):
            if aa%6==bb%6 and aa%6 in (1,5) and math.gcd(aa,bb)==1:pairs.append((aa,bb))
    for aa,bb in pairs:
        assert gcd(a(aa),a(bb))==C
        C0=poly(aa,bb);C1=poly((aa-1)//2,(bb-1)//2)
        assert gcd(a(aa),gcd(C0,C1))==C
        qa,qb=quotient(aa),quotient(bb)
        y=[*qb,*qa]
        assert syndrome(at(aa),at(bb),y)==(ZERO,ZERO)
        assert eval4(add(y[0],y[1])) and eval4(add(y[2],y[3]))
        if aa%6==5:
            bd=[*rshift(at(bb),2-aa),*rshift(at(aa),2-aa)]
            overlap=sum(len(x&z) for x,z in zip(y,bd));assert overlap==4
            y=[add(x,z) for x,z in zip(y,bd)]
            assert wt(y)==2*(aa+bb)
        else:assert wt(y)==2*(aa+bb)-2
        assert syndrome(at(aa),at(bb),y)==(ZERO,ZERO)
        assert eval4(add(y[0],y[1])) and eval4(add(y[2],y[3]))
        # Recover the full k,h coordinates to check the requested parameterization.
        A,B=a(aa),a(bb); pp=div(add(A,B),C2);qq=div(mul(A,A),C2)
        hh=y[3];V=add(y[2],mul(add(A,ONE),hh));kk=div(V,qq)
        reconstructed=[add(mul(add(mul(add(A,ONE),pp),qq),kk),mul(add(B,ONE),hh)),
                       add(mul(pp,kk),hh),add(mul(qq,kk),mul(add(A,ONE),hh)),hh]
        assert reconstructed==y and eval4(kk)
        if (aa,bb) in [(1,7),(1,13),(5,11),(5,17),(7,13),(11,17)]:
            L=3*(4*(aa+bb)+1)
            witnesses.append(exact_finite(aa,bb,L,y))
    counts['arithmetic_progression_pairs']=len(pairs)
    counts['phase_minus_boundary_moves']=sum(a_%6==5 for a_,b_ in pairs)
    counts['full_k_h_reconstructions']=len(pairs)

    # A sanity check of the residue-count lower bound for arbitrary messages.
    rng=random.Random(1847);message_checks=0
    for aa,bb in [(1,7),(5,11),(7,13),(11,17),(13,19),(17,23)]:
        da,db=div(a(aa),C),div(a(bb),C)
        for _ in range(80):
            f=poly(*rng.sample(range(140),rng.randrange(1,50)))
            if not eval4(f):continue
            u,v=mul(db,f),mul(da,f)
            assert len(u)>=bb and len(v)>=aa
            assert set(i%bb for i in u)==set(range(bb))
            assert set(i%aa for i in v)==set(range(aa))
            message_checks+=1
    counts['residue_lower_bound_message_checks']=message_checks

    # All-parameter cancellation identity, checked independently as sets.
    cancellation=[]
    for j in range(81):
        E,O=12*j+8,18*j+13
        B=poly(0,E,O);b=div(B,C)
        f=poly(0,6*j+3,E,18*j+12)
        u=mul(b,f)
        first=mul(poly(0,1),poly(*range(0,6*j+3,3)))
        tail=add(mul(poly(0,2),poly(*range(0,6*j+3,3))),poly(6*j+3))
        explicit=add(first,poly(18*j+11),shift(tail,30*j+20))
        assert explicit==u and mul(C,u)==mul(B,f)
        assert eval4(f)==2
        assert len(b)+1==12*j+10
        assert len(u)+len(f)==8*j+10
        if j in (0,1,2,5,20,80):cancellation.append({'j':j,'impulse_weight':12*j+10,'message_weight':4,'constructed_pair_weight':8*j+10})
    counts['cancellation_identity_instances']=81
    # Small exact base minimum: a=1,b=7. Lower bound 8; weight 8
    # would force v monomial, whose left block has weight 9, contradiction.
    assert len(div(a(7),C))==9
    output={'status':'all_checks_passed','counts':counts,'finite_matrix_checks':witnesses,
            'cancellation_family':cancellation,
            'exact_small_base_minimum':{'a':1,'b':7,'mu0':10,'proof':'residue lower bound, parity, then monomial right block exclusion'},
            'scope':'No general factor-three result and no factor-three counterexample. No decoder-derived minimum is asserted.'}
    Path(__file__).with_name('verification_summary.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
