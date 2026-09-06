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

counts=Counter();certs=[];cache={};X,Y=sp.symbols('X Y');zero2=(0,0)
for li,line in enumerate((ROOT/'highrank_eight.tsv').read_text().splitlines()):
 r,fr,tor,fill,ov,mat,wit,source=line.split('\t');r,fr,tor,fill,ov=map(int,(r,fr,tor,fill,ov));source=list(map(int,source.split(',')))
 a=list(map(int,mat.strip(',').split(',')));rr=[tuple(a[i:i+4])for i in range(0,16,4)];norm=reducer(rr)
 orig,origw=reconstruct(source)
 assert all(norm(row)==Z for row in orig)
 if mat not in cache:
  dm=DomainMatrix.from_Matrix(sp.Matrix(rr)).convert_to(sp.ZZ);dd,ss,tt=smith_normal_decomp(dm);assert dd==ss*dm*tt
  D,S,T=dd.to_Matrix(),ss.to_Matrix(),tt.to_Matrix();assert abs(S.det())==abs(T.det())==1
  diag=[abs(int(D[i,i]))for i in range(4)];cache[mat]=(diag,T)
 diag,T=cache[mat]
 assert diag.count(0)==fr and math.prod(v for v in diag if v)==tor
 # The five original rows generate exactly the displayed row lattice.
 D0=smith_normal_decomp(DomainMatrix.from_Matrix(sp.Matrix(orig)).convert_to(sp.ZZ))[0].to_Matrix()
 od=[abs(int(D0[i,i]))for i in range(4)]
 assert od==diag
 W={(int(t[0]),tuple(map(int,t[1:])))for t in [u.strip(',').split(',')for u in wit.strip(';').split(';')]}
 assert len(W)==8 and sum(b==0 for b,_ in W)==r
 ow={(b,norm(q))for b,q in origw};assert len(ow)==8
 orbits=[sorted((b,norm(sub(q,t)))for b,q in ow)for _,t in ow]
 assert sorted(W)==min(orbits)
 assert len(poly(A,norm))==len(poly(B,norm))==3
 syndrome=[add(q,t)for b,q in W for t in (A if b==0 else B)]
 assert not poly(syndrome,norm)
 def boundary(t):return {(b,norm(add(t,a)))for b,P in enumerate((B,A))for a in P}
 cand={norm(sub(q,a))for b,q in W for a in (B if b==0 else A)}
 bs=[boundary(t)for t in cand];m=max(len(b&W)for b in bs);assert m==ov
 if fill==2:assert any(b^c==W for b,c in combinations(bs,2))
 cert={'id':li,'split':[r,8-r],'free_rank':fr,'torsion_order':tor,'source':source}
 if ov>=4:cert.update(category='shortenable',overlap=ov)
 elif assoc([scale(v,2)for v in A],[scale(v,2)for v in B],norm) is not None:cert.update(category='associated_squares',base_bound=6)
 elif (c:=cyclic_twist(A,B,norm,4)) is not None:cert.update(category='cyclic_order_four_twist',base_bound=8,certificate=c)
 elif (c:=twisted_square(A,B,norm)) is not None:cert.update(category='involution_twisted_square',base_bound=8,certificate=c)
 elif (c:=twisted_square(B,A,norm)) is not None:cert.update(category='involution_twisted_square',base_bound=8,certificate=c,exchanged=True)
 else:
  keep=[i for i,v in enumerate(diag)if v!=1]
  def trans(v):
   a=sp.Matrix([v])*T
   return tuple(int(a[i])%diag[i]if diag[i]else int(a[i])for i in keep)
  ds=[diag[i]for i in keep]
  finitecheck=next((b for b,P in enumerate((A,B))if all(all(x==0 for x,d in zip(trans(q),ds)if d==0)for q in P)),None)
  if finitecheck is not None:cert.update(category='finite_check_subgroup',base_bound=tor,check=finitecheck)
  elif tor==1 and fr==2:
   def normalized(S):
    S=list(S);mn=tuple(min(q[i]for q in S)for i in range(2));expr=sum(X**(q[0]-mn[0])*Y**(q[1]-mn[1])for q in S)
    return sp.Poly(expr,X,Y,modulus=2),mn
   ap,am=normalized(map(trans,A));bp,bm=normalized(map(trans,B));up,um=normalized(trans(q)for b,q in W if b==0)
   gd=sp.gcd(ap,bp)
   if gd.total_degree()==0:
    h,rem=sp.div(up,bp);assert rem.is_zero
    H=[(m[0]+um[0]-bm[0],m[1]+um[1]-bm[1])for m,c in h.terms()]
    Tin=T.inv();hlift=[]
    for q in H:
     full=[0]*4
     for i,v in zip(keep,q):full[i]=v
     v=sp.Matrix([full])*Tin;hlift.append(norm(tuple(map(int,v))))
    result=set()
    for q in hlift:result^=boundary(q)
    assert result==W
    cert.update(category='explicit_boundary',filling=hlift,filling_weight=len(hlift))
   else:
    # Untwisted Frobenius relations have a weight-four base logical.
    aa=assoc(A,[scale(v,2)for v in B],norm);bb=assoc(B,[scale(v,2)for v in A],norm)
    assert aa is not None or bb is not None,('unresolved',li,gd)
    cert.update(category='frobenius_multiple',base_bound=4)
  else:raise AssertionError(('unresolved',li))
 counts[cert['category']]+=1;certs.append(cert)
summary={'retained_pairs':len(certs),'categories':dict(counts),'unresolved':0,'input_sha256':hashlib.sha256((ROOT/'highrank_eight.tsv').read_bytes()).hexdigest()}
(ROOT/'highrank_verification.json').write_text(json.dumps(summary,indent=2)+'\n')
(ROOT/'highrank_certificates.json').write_text(json.dumps(certs,indent=2)+'\n')
print(json.dumps(summary,indent=2))
