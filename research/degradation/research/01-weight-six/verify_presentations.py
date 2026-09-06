"""Independently check retained presentations with exact SymPy arithmetic.
The complete port enumeration is in classify_six.cpp; this checks every
retained row, not a sampled subset. Requires sympy.
"""
import json, math
from collections import Counter
from pathlib import Path
from itertools import combinations
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
ROOT=Path(__file__).resolve().parent
Z=(0,0,0,0)
A=[Z,(1,0,0,0),(0,1,0,0)]
B=[Z,(0,0,1,0),(0,0,0,1)]
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
mul=lambda a,c:tuple(c*x for x in a)

def lattice(rows):
    nz=[r for r in rows if any(r)]
    piv=[next(i for i,v in enumerate(r) if v) for r in nz]
    assert piv==sorted(piv)
    assert all(r[p]>0 for r,p in zip(nz,piv))
    def norm(v):
        v=list(v)
        for p,r in zip(piv,nz):
            q=v[p]//r[p]
            v=[x-q*y for x,y in zip(v,r)]
        return tuple(v)
    return norm

def poly_norm(S,norm):
    out=set()
    for v in S:
        v=norm(v)
        if v in out:out.remove(v)
        else:out.add(v)
    return out

def associate(S,T,norm):
    S=poly_norm(S,norm);T=poly_norm(T,norm)
    return any(S=={norm(add(t,sub(s,v))) for t in T} for s in S for v in T)

def three_orbit(S,norm):
    S=poly_norm(S,norm)
    if len(S)!=3:return None
    root=min(S);s={norm(sub(v,root)) for v in S}
    for d in s-{Z}:
        if norm(mul(d,3))==Z and s=={Z,d,norm(mul(d,2))}:return s
    return None

rows=[line.strip().split('\t') for line in (ROOT/'mixed_presentations.tsv').read_text().splitlines()]
counts=Counter();cache={};rank_one_max={};finite_max={};cat_counts=Counter();seen=set()
for r,free,T,fill,mat,ws in rows:
    r,free,T,fill=map(int,(r,free,T,fill))
    rr=list(map(int,mat.strip(',').split(',')));rr=[tuple(rr[i:i+4]) for i in range(0,16,4)]
    norm=lattice(rr)
    if mat not in cache:
        M=sp.Matrix(rr)
        dm=DomainMatrix.from_Matrix(M).convert_to(sp.ZZ)
        d,s,t=smith_normal_decomp(dm)
        assert d==s*dm*t
        ss=s.to_Matrix();tt=t.to_Matrix();dd=d.to_Matrix()
        assert abs(ss.det())==abs(tt.det())==1
        diag=[abs(int(dd[i,i])) for i in range(4)]
        frank=diag.count(0);torsion=math.prod(v for v in diag if v)
        v=None;R=0
        if frank==1:
            v=M.nullspace()[0]
            den=sp.ilcm(*[x.q for x in v]);v=[int(x*den) for x in v]
            g=math.gcd(*v);v=[x//g for x in v]
            assert M*sp.Matrix(v)==sp.zeros(4,1) and math.gcd(*v)==1
            R=max(max(0,*v[:2])-min(0,*v[:2]),max(0,*v[2:])-min(0,*v[2:]))
        cache[mat]=(frank,torsion,v,R)
    frank,torsion,v,R=cache[mat]
    assert (free,T)==(frank,torsion)
    W=[tuple(map(int,p.strip(',').split(','))) for p in ws.strip(';').split(';')]
    assert len(W)==len(set(W))==6
    assert sum(p[0]==0 for p in W)==r
    assert len(poly_norm(A,norm))==len(poly_norm(B,norm))==3
    syndrome=[]
    for block,*q in W:
        syndrome.extend(add(q,s) for s in (A if block==0 else B))
    assert not poly_norm(syndrome,norm)
    key=(r,mat,ws);assert key not in seen;seen.add(key)
    def boundary(v):
        return {(b,norm(add(v,a))) for b,P in enumerate((B,A)) for a in P}
    w={(p[0],tuple(p[1:])) for p in W}
    if fill:
        candidates={norm(sub(q,s)) for block,*q in W for s in (B if block==0 else A)}
        bs=[boundary(q) for q in candidates]
        if fill==1:assert any(b==w for b in bs)
        elif fill==2:assert any(b^c==w for b,c in combinations(bs,2))
        else:raise AssertionError('invalid filling label')
        category=f'boundary_{fill}'
    elif free==0:
        finite_max[r]=max(finite_max.get(r,0),T)
        category='finite'
    elif free==1:
        rank_one_max[r]=max(rank_one_max.get(r,0),4*T*R)
        category='strip'
    else:
        U=[tuple(p[1:]) for p in W if p[0]==0];V=[tuple(p[1:]) for p in W if p[0]==1]
        if three_orbit(A,norm) is not None or three_orbit(B,norm) is not None:category='order_three_check'
        elif associate(A,B,norm):category='monomial_associates'
        elif associate(A,[mul(v,2) for v in B],norm) or associate(B,[mul(v,2) for v in A],norm):category='Frobenius_multiple'
        elif associate([mul(v,2) for v in A],[mul(v,2) for v in B],norm):category='equal_squares'
        elif (J:=three_orbit(U,norm)) is not None and three_orbit(V,norm)==J:category='order_three_projector'
        else:raise AssertionError(('unresolved',r,free,T,mat,ws))
    counts[(r,free,fill)]+=1;cat_counts[category]+=1
assert len(rows)==5392
assert finite_max=={3:27,4:22,5:12}
assert rank_one_max=={3:48,4:56,5:40}
result={'checked_presentations':len(rows),'distinct_relation_lattices':len(cache),
        'counts':{str(k):v for k,v in sorted(counts.items())},
        'categories':dict(cat_counts),'rank_zero_maximum_group_orders':finite_max,
        'rank_one_distance_bounds':rank_one_max,'uniform_base_distance_cutoff':56,
        'unresolved_presentations':0}
(ROOT/'presentation_verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
