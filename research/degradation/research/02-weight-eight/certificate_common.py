"""Verify every retained high-free-rank eight-cycle independently in exact arithmetic.
Reconstructs each graph/port source, verifies its relation lattice, computes
Smith coordinates, and certifies shortening or a uniform algebraic alternative.
"""
from pathlib import Path
from itertools import permutations,combinations
from collections import Counter
import json, math, hashlib
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp
ROOT=Path(__file__).resolve().parent
Z=(0,0,0,0); A=[Z,(1,0,0,0),(0,1,0,0)];B=[Z,(0,0,1,0),(0,0,0,1)]
add=lambda a,b:tuple(x+y for x,y in zip(a,b));sub=lambda a,b:tuple(x-y for x,y in zip(a,b));scale=lambda a,n:tuple(n*x for x in a)
PERMS=list(permutations(range(3)));PAIRS=list(combinations(range(8),2))
GRAPHS=[]
for line in (ROOT/'graph_multiplicities_8.txt').read_text().splitlines():
 ms=list(map(int,line.split()));assert len(ms)==28
 GRAPHS.append([e for e,m in zip(PAIRS,ms) for _ in range(m)])
def reconstruct(source):
 gi,mask,pn=source;edges=GRAPHS[gi];inc=[[i for i,e in enumerate(edges)if v in e]for v in range(8)]
 block=[(mask>>v)&1 for v in range(8)];fixed={};vary=[]
 for v,b in enumerate(block):
  if b not in fixed:fixed[b]=v
  else:vary.append(v)
 pi=[0]*8
 for v in vary:pi[v]=pn%6;pn//=6
 labs={}
 for v in range(8):
  for j,e in enumerate(inc[v]):labs[v,e]=(A if block[v]==0 else B)[PERMS[pi[v]][j]]
 pos={0:Z};bfs=[0];tree=set()
 for v in bfs:
  for e in inc[v]:
   w=sum(edges[e])-v
   if w not in pos:pos[w]=sub(add(pos[v],labs[v,e]),labs[w,e]);tree.add(e);bfs.append(w)
 rows=[sub(add(pos[u],labs[u,e]),add(pos[v],labs[v,e]))for e,(u,v)in enumerate(edges)if e not in tree]
 assert len(rows)==5
 return rows,[(block[v],pos[v])for v in range(8)]
def reducer(rr):
 nz=[r for r in rr if any(r)];piv=[next(i for i,v in enumerate(r)if v)for r in nz]
 assert piv==sorted(piv)
 def norm(v):
  v=list(v)
  for p,r in zip(piv,nz):
   assert r[p]>0;q=v[p]//r[p];v=[x-q*y for x,y in zip(v,r)]
  return tuple(v)
 return norm

def poly(S,norm):
 s=set()
 for t in S:
  t=norm(t)
  if t in s:s.remove(t)
  else:s.add(t)
 return s

def assoc(S,T,norm):
 S=poly(S,norm);T=poly(T,norm)
 return next((sub(s,t)for s in S for t in T if S=={norm(add(q,sub(s,t)))for q in T}),None)

def cyclic_twist(A,B,norm,M):
 """A = m*(1+t^a*x+t^b*y), B = n*(1+x+y), t^M=1."""
 for a0,a1,a2 in permutations(A):
  for b0,b1,b2 in permutations(B):
   x=sub(b1,b0);y=sub(b2,b0)
   da=norm(sub(sub(a1,a0),x));db=norm(sub(sub(a2,a0),y))
   for t in [da,db]+[norm(scale(v,j))for v in [da,db]for j in range(1,M)]:
    if norm(scale(t,M))!=Z:continue
    cyc={norm(scale(t,j)):j for j in range(M)}
    if da in cyc and db in cyc:return {'t':t,'order_bound':M,'powers':[cyc[da],cyc[db]],'A_order':[a0,a1,a2],'B_order':[b0,b1,b2]}
 return None

def twisted_square(A,B,norm):
 for a0,a1,a2 in permutations(A):
  for b0,b1,b2 in permutations(B):
   x=sub(a1,a0);y=sub(a2,a0)
   t=norm(sub(sub(b1,b0),scale(x,2)))
   if norm(scale(t,2))==Z and norm(sub(sub(b2,b0),scale(y,2)))==t:return {'t':t,'A_order':[a0,a1,a2],'B_order':[b0,b1,b2]}
 return None

