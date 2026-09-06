"""Independent all-pairings verifier. Uses only Python exact integer arithmetic.
No SymPy, no retained normal forms, and no graph-type classification as input.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
from math import prod
import json,time

def diagonalize(rows):
    M=[r[:] for r in rows]; m=len(M); n=len(M[0]); V=[[int(i==j) for j in range(n)] for i in range(n)]
    def swapcols(a,b):
        for R in (M,V):
            for row in R: row[a],row[b]=row[b],row[a]
    def addcol(j,k,q):
        for R in (M,V):
            for row in R:row[j]-=q*row[k]
    k=0
    while k<min(m,n):
        nz=[(abs(M[i][j]),i,j) for i in range(k,m) for j in range(k,n) if M[i][j]]
        if not nz:break
        _,i,j=min(nz);M[k],M[i]=M[i],M[k];swapcols(k,j)
        while True:
            restart=False
            for i in range(k+1,m):
                if M[i][k]:
                    q=M[i][k]//M[k][k]
                    M[i]=[x-q*y for x,y in zip(M[i],M[k])]
                    if M[i][k]:M[k],M[i]=M[i],M[k];restart=True;break
            if restart:continue
            for j in range(k+1,n):
                if M[k][j]:
                    q=M[k][j]//M[k][k];addcol(j,k,q)
                    if M[k][j]:swapcols(k,j);restart=True;break
            if restart:continue
            break
        if M[k][k]<0:M[k]=[-x for x in M[k]]
        k+=1
    assert all(M[i][j]==0 for i in range(m) for j in range(n) if i!=j)
    D=[M[i][i] for i in range(k)]
    # Verify that every relation maps to zero in the computed quotient.
    def red(x):
        y=[sum(x[i]*V[i][j] for i in range(n)) for j in range(n)]
        return tuple(y[j]%D[j] if j<k else y[j] for j in range(n))
    assert all(red(r)==(0,)*n for r in rows)
    return D,V,red

def pairings(unpaired):
    if not unpaired:
        yield [];return
    a=unpaired[0]
    for j in range(1,len(unpaired)):
        b=unpaired[j]
        if a//3==b//3:continue
        for tail in pairings(unpaired[1:j]+unpaired[j+1:]):
            yield [(a,b)]+tail

def check(types,matching):
    n=5 if len(set(types))==1 else 7;p=n-3
    E=[]
    for a,b in matching:
        row=[0]*n
        for label,sgn in ((a,1),(b,-1)):
            v,c=divmod(label,3)
            if v:row[p+v-1]+=sgn
            if c:row[2*types[v]+c-1]+=sgn
        E.append(row)
    D,V,red=diagonalize(E);rank=len(D);free=n-rank;zero=(0,)*n
    def unit(i):return red([int(j==i) for j in range(n)])
    def add(a,b):return tuple((x+y)%D[i] if i<rank else x+y for i,(x,y) in enumerate(zip(a,b)))
    def neg(a):return tuple((-x)%D[i] if i<rank else -x for i,x in enumerate(a))
    def sub(a,b):return add(a,neg(b))
    A=[zero,unit(0),unit(1)]
    B=[zero,unit(2),unit(3)] if p==4 else A
    if len(set(A))<3 or len(set(B))<3:return 'invalid_terms',None
    positions=[zero]+[unit(i) for i in range(p,n)]
    cols=[tuple(sorted(add(positions[i],a) for a in (B if types[i] else A))) for i in range(4)]
    if len(set(cols))<4:return 'duplicate_columns',None
    # Check the full cycle and its minimality directly in the presented group.
    synd=Counter(q for col in cols for q in col)
    assert all(v%2==0 for v in synd.values())
    T=prod(D)
    if p==2:
        assert free==0 and T in (6,7),(types,matching,D,free)
        return 'finite_single_block',{'torsion':T,'bound':2*T}
    if free==1:
        wa=[x[-1] for x in A];wb=[x[-1] for x in B]
        rho=max(max(wa)-min(wa),max(wb)-min(wb))
        assert T*rho<=6 and rho>0,(types,matching,D,T,rho)
        return 'virtually_cyclic',{'torsion':T,'range':rho,'bound':8*T*rho}
    assert free==2,(types,matching,D,free)
    def order2(x):return x!=zero and add(x,x)==zero
    for P in (A,B):
        if any(order2(sub(a,b)) for a,b in combinations(P,2)):
            return 'unit_trinomial',{'bound':0}
    def equivalent(P,Q):
        for a in P:
            shift=sub(Q[0],a)
            if sorted(add(x,shift) for x in P)==sorted(Q):return True
        return False
    if equivalent([add(a,a) for a in A],B) or equivalent([add(b,b) for b in B],A):
        return 'frobenius_square',{'bound':8}
    for b in B:
        for a in A:
            shift=sub(a,b);BQ={add(x,shift) for x in B};AS=set(A)
            if len(BQ&AS)==2:
                h=sub(next(iter(BQ-AS)),next(iter(AS-BQ)))
                if order2(h):return 'involution_offset',{'bound':8}
    raise AssertionError(('UNCLASSIFIED',types,matching,D,A,B,V))

def main():
    t=time.time();ms=list(pairings(list(range(12))))
    result={'method':'all incidence pairings, integer diagonalization with unimodular column operations','pairings_per_support_type':len(ms),'support_types':{},'maximum_bound':0}
    for types in ([0,0,0,0],[0,0,0,1],[0,0,1,1]):
        counts=Counter();ranges=Counter()
        for M in ms:
            kind,info=check(types,M);counts[kind]+=1
            if info:
                result['maximum_bound']=max(result['maximum_bound'],info['bound'])
                if kind=='virtually_cyclic':ranges[(info['torsion'],info['range'])]+=1
        result['support_types'][str(types)]={'counts':dict(counts),'virtually_cyclic_parameters':{str(k):v for k,v in ranges.items()}}
        print(types,dict(counts),dict(ranges),flush=True)
    result['seconds']=time.time()-t
    assert result['maximum_bound']==48
    print(json.dumps(result,indent=2))
    with open(Path(__file__).with_name('independent_verification.json'),'w') as f:json.dump(result,f,indent=2)
if __name__=='__main__':main()
