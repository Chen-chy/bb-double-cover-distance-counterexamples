"""Exhaustive normalized cubic-graph classification of weight-four BB circuits.
Independent of verify4_independent.py: uses seven cubic multigraphs, HNF/SNF,
and rational nullspaces. Requires SymPy.
"""
from pathlib import Path
from itertools import permutations, product, combinations
from collections import Counter
from math import gcd, prod
from functools import reduce
import json,time,platform
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form,smith_normal_form
from sympy.polys.domains import ZZ

class PresentedGroup:
    def __init__(self,E):
        self.n=len(E[0]);self.R=sp.Matrix(E)
        H=hermite_normal_form(self.R.T)
        self.cols=[tuple(map(int,H[:,j])) for j in range(H.cols)]
        self.pivs=[max(i for i,x in enumerate(c) if x) for c in self.cols]
        assert self.pivs==sorted(self.pivs)
        assert all(self.red(r)==(0,)*self.n for r in E)
    def red(self,v):
        v=list(v)
        for c,p in reversed(list(zip(self.cols,self.pivs))):
            assert c[p]>0
            q=v[p]//c[p]
            v=[a-q*b for a,b in zip(v,c)]
        return tuple(map(int,v))
    def add(self,a,b):return self.red([x+y for x,y in zip(a,b)])
    def sub(self,a,b):return self.red([x-y for x,y in zip(a,b)])
    def unit(self,i):return self.red([int(j==i) for j in range(self.n)])

def graphs():
    yield [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    for a in range(1,4):
        b,c=[x for x in range(1,4) if x!=a]
        for cross in [[(0,b),(a,c)],[(0,c),(a,b)]]:
            yield [(0,a),(0,a),(b,c),(b,c)]+cross

def presentations(types):
    n=5 if len(set(types))==1 else 7;p=n-3
    pp=list(permutations(range(3)));first={types.index(t) for t in set(types)}
    for gi,edges in enumerate(graphs()):
        inc=[[j for j,e in enumerate(edges) if v in e] for v in range(4)]
        for labels in product(*([pp[0]] if v in first else pp for v in range(4))):
            E=[]
            for j,(v,w) in enumerate(edges):
                row=[0]*n
                for vertex,sgn in [(v,1),(w,-1)]:
                    if vertex:row[p+vertex-1]+=sgn
                    color=labels[vertex][inc[vertex].index(j)]
                    if color:row[2*types[vertex]+color-1]+=sgn
                E.append(row)
            yield {'types':types,'graph':gi,'labels':labels,'relations':E}

def classify(record):
    types,E=record['types'],record['relations'];G=PresentedGroup(E)
    n=G.n;p=n-3;zero=(0,)*n
    A=[zero,G.unit(0),G.unit(1)]
    B=[zero,G.unit(2),G.unit(3)] if p==4 else A
    if len(set(A))!=3 or len(set(B))!=3:return 'invalid_terms',None
    positions=[zero]+[G.unit(i) for i in range(p,n)]
    cols=[tuple(sorted(G.add(positions[i],x) for x in (B if types[i] else A))) for i in range(4)]
    if len(set(cols))<4:return 'duplicate_columns',None
    synd=Counter(x for col in cols for x in col)
    assert all(v%2==0 for v in synd.values())
    N=G.R.nullspace();free=len(N)
    D=smith_normal_form(G.R,domain=ZZ)
    T=prod(abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i])
    info={'free_rank':free,'torsion_order':T}
    if p==2:
        assert free==0 and T in (6,7)
        info['bound']=2*T
        return 'finite_single_block',info
    if free==1:
        v=list(N[0]);den=sp.ilcm(*[x.q for x in v]);w=[int(x*den) for x in v]
        div=reduce(gcd,w);w=[x//div for x in w]
        assert reduce(gcd,w)==1
        rho=max(max(0,*w[:2])-min(0,*w[:2]),max(0,*w[2:4])-min(0,*w[2:4]))
        assert rho>0 and T*rho<=6
        info.update(free_coordinates=w,range=rho,bound=8*T*rho)
        return 'virtually_cyclic',info
    assert free==2
    def order2(x):return x!=zero and G.add(x,x)==zero
    for P in (A,B):
        if any(order2(G.sub(a,b)) for a,b in combinations(P,2)):
            info['bound']=0
            return 'unit_trinomial',info
    def equivalent(P,Q):
        for x in P:
            delta=G.sub(Q[0],x)
            if sorted(G.add(y,delta) for y in P)==sorted(Q):return True
        return False
    if equivalent([G.add(x,x) for x in A],B) or equivalent([G.add(x,x) for x in B],A):
        info['bound']=8
        return 'frobenius_square',info
    for a in A:
        for b in B:
            delta=G.sub(a,b);P=set(A);Q={G.add(x,delta) for x in B}
            if len(P&Q)==2 and order2(G.sub(next(iter(Q-P)),next(iter(P-Q)))):
                info['bound']=8
                return 'involution_offset',info
    raise AssertionError(('UNCLASSIFIED',record,A,B,info))

def main():
    here=Path(__file__).parent;start=time.time();report={'python':platform.python_version(),'sympy':sp.__version__,'support_types':{}};retained=[]
    for types,expected in [([0,0,0,0],1512),([0,0,0,1],252),([0,0,1,1],252)]:
        counts=Counter();param=Counter();total=0
        for record in presentations(types):
            total+=1;kind,info=classify(record);counts[kind]+=1
            if info:
                record.update(case=kind,**info);retained.append(record)
                if kind=='virtually_cyclic':param[(info['torsion_order'],info['range'])]+=1
        assert total==expected
        report['support_types'][str(types)]={'tested':total,'counts':dict(counts),'virtually_cyclic_parameters':{str(k):v for k,v in param.items()}}
        print(types,total,dict(counts),flush=True)
    assert len(retained)==166
    assert max(r['bound'] for r in retained)==48
    report.update(retained_presentations=len(retained),maximum_bound=48,seconds=time.time()-start)
    (here/'sympy_verification.json').write_text(json.dumps(report,indent=2)+'\n')
    (here/'weight_four_presentations.json').write_text(json.dumps(retained,indent=2)+'\n')
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
