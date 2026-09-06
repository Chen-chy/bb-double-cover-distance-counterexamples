"""Exact negative control for a restricted divided-Euler/majority ansatz.

This is a BASE BOUNDARY, not a logical-minimum or factor-three counterexample.
It also has circuit support and is strictly stable under every single
monomial stabilizer flip. Both multivariate and primitive one-variable
arithmetic are reconstructed here, without importing the discovery code.
"""
from __future__ import annotations
from collections import Counter
from pathlib import Path
import json

ZERO=(0,0,0)


def plus(*polys):
    result={}
    for p in polys:
        for e in p:
            result[e]=result.get(e,0)^1
    return frozenset(e for e,coefficient in result.items() if coefficient)


def product(p,q):
    result={}
    for a in p:
        for b in q:
            e=tuple(x+y for x,y in zip(a,b))
            result[e]=result.get(e,0)^1
    return frozenset(e for e,coefficient in result.items() if coefficient)


def power(p,n):
    result=frozenset((ZERO,))
    for _ in range(n):result=product(result,p)
    return result


def shift(p,d):return frozenset(tuple(x+y for x,y in zip(a,d)) for a in p)


def split(p):
    assert all(j%2==0 and k%2==0 for i,j,k in p)
    return (frozenset((i//2,j//2,k//2) for i,j,k in p if i%2==0),
            frozenset(((i+1)//2,j//2,k//2) for i,j,k in p if i%2))


def votes(a,b,c,d):
    J=frozenset((ZERO,(0,0,1),(0,1,1)))
    fields=(shift(product(J,a),(0,0,-2)),
            plus(shift(a,(0,0,-1)),b),
            plus(shift(a,(0,1,0)),b,shift(b,(0,0,1))),
            product(J,c),plus(c,shift(d,(0,0,1))),
            plus(shift(c,(0,1,0)),d,shift(d,(0,0,1))))
    counts=Counter(e for p in fields for e in p)
    return sum(min(k,6-k) for k in counts.values()),fields


def map_poly(p):
    values=[i+30001*j+303*k for i,j,k in p]
    assert len(set(values))==len(p),'unwanted specialization collision'
    return frozenset(values)


def uadd(*pp):
    q=set()
    for p in pp:q.symmetric_difference_update(p)
    return frozenset(q)


def ushift(p,j):return frozenset(i+j for i in p)


def umul(p,q):
    acc=set()
    for i in p:
        for j in q:
            x=i+j
            if x in acc:acc.remove(x)
            else:acc.add(x)
    return frozenset(acc)


def umajority(u,v):
    r,s,g=1,30001,303
    a=frozenset(i//2 for i in u if i%2==0)
    b=frozenset((i+r)//2 for i in u if i%2)
    c=frozenset(i//2 for i in v if i%2==0)
    d=frozenset((i+r)//2 for i in v if i%2)
    assert not uadd(a,ushift(a,s),b,c,ushift(c,s+g),ushift(d,2*g))
    J=frozenset((0,g,s+g))
    fields=(ushift(umul(J,a),-2*g),uadd(ushift(a,-g),b),
            uadd(ushift(a,s),b,ushift(b,g)),umul(J,c),
            uadd(c,ushift(d,g)),uadd(ushift(c,s),d,ushift(d,g)))
    allsites=set().union(*fields)
    eta={i for i in allsites if sum(i in p for p in fields)>3}
    # The same eta is an arbitrary boundary coefficient in these six
    # monomial-normalized channels, not six independent adjustments.
    optimal=[uadd(p,eta) for p in fields]
    shifted=[ushift(p,j) for p,j in zip(optimal,(2*g,s+g,0,0,s,0))]
    def square(p):return frozenset(2*i for i in p)
    U0=uadd(ushift(square(shifted[0]),r),square(shifted[1]))
    U1=square(shifted[2])
    V0=uadd(ushift(square(shifted[3]),r),square(shifted[4]))
    V1=square(shifted[5])
    A0=frozenset((r,2*s));B0=frozenset((r+4*g,2*s+2*g))
    assert not uadd(umul(A0,U0),U1,umul(B0,V0),V1)
    assert not uadd(umul(A0,U1),U0,umul(B0,V1),V0)
    weight=sum(map(len,(U0,U1,V0,V1)))
    assert weight==sum(min(sum(i in p for p in fields),6-sum(i in p for p in fields)) for i in allsites)
    return weight


def matrix_rank(columns):
    rows={x:i for i,x in enumerate(sorted(set().union(*columns)))}
    basis={}
    for column in columns:
        vector=sum(1<<rows[x] for x in column)
        while vector:
            pivot=vector.bit_length()-1
            if pivot not in basis:
                basis[pivot]=vector;break
            vector^=basis[pivot]
    return len(basis),len(rows)


def main():
    X=frozenset(((1,0,0),)); one=frozenset((ZERO,))
    A=plus(one,X,frozenset(((0,2,0),)))
    B=frozenset((ZERO,(1,0,4),(0,2,2)))
    F=product(product(power(A,3),power(B,3)),
              plus(frozenset(((2,0,0),)),product(frozenset((ZERO,(1,4,0))),power(A,4))))
    u,v=product(B,F),product(A,F)
    assert not plus(product(A,u),product(B,v))
    a,b=split(u);c,d=split(v)
    m0,fields0=votes(a,b,c,d)
    m1,fields1=votes(b,shift(a,(1,0,0)),d,shift(c,(1,0,0)))
    assert len(u)+len(v)==182 and m0==m1==550
    assert min(m0,m1)>3*(len(u)+len(v))
    for p in (A,B,F,u,v,*fields0,*fields1):map_poly(p)
    uu,vv=map_poly(u),map_poly(v);AA,BB=map_poly(A),map_poly(B)
    assert umul(BB,map_poly(F))==uu and umul(AA,map_poly(F))==vv
    assert not uadd(umul(AA,uu),umul(BB,vv))
    assert umajority(uu,vv)==550
    assert umajority(ushift(uu,1),ushift(vv,1))==550
    columns=[ushift(AA,i) for i in uu]+[ushift(BB,i) for i in vv]
    rank,nrows=matrix_rank(columns)
    assert rank==181 and nrows==268
    overlaps=Counter()
    for support,check in ((uu,BB),(vv,AA)):
        for i in support:
            for j in check:overlaps[i-j]+=1
    assert max(overlaps.values())==2
    # E0=1+z+z^2 divides A and 1+z^303. Modulo E0, z^3=1.
    assert {e%3 for e in AA}=={0,1,2}
    assert 303%3==0
    result={'status':'all exact checks passed','classification':'boundary negative control; NOT a logical counterexample',
            'boundary_multiplier_weight':len(F),'base_weight':182,
            'restricted_majority_weights':[550,550],'three_times_base_weight':546,
            'primitive_specialization':{'r':1,'s':30001,'g':303},
            'selected_column_rank':rank,'selected_columns':182,'check_rows':nrows,
            'circuit_support':True,'maximum_single_boundary_overlap':2,
            'single_stabilizer_weight_increase_at_least':2}
    Path(__file__).with_name('majority_control_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
