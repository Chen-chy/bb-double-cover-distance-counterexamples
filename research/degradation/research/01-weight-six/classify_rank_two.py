from collections import Counter
import json
from pathlib import Path
ROOT=str(Path(__file__).resolve().parent)+'/'
Z=(0,0,0,0);A=[Z,(1,0,0,0),(0,1,0,0)];B=[Z,(0,0,1,0),(0,0,0,1)]
add=lambda a,b:tuple(x+y for x,y in zip(a,b))
sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
mul=lambda a,k:tuple(k*x for x in a)
class Lat:
 def __init__(self,rr):
  self.rows=[r for r in rr if any(r)]
  self.piv=[next(i for i,x in enumerate(r) if x) for r in self.rows]
 def norm(self,v):
  v=list(v)
  for p,r in zip(self.piv,self.rows):
   q=v[p]//r[p];v=[a-q*b for a,b in zip(v,r)]
  return tuple(v)
 def poly(self,S):
  ss=set()
  for v in S:
   v=self.norm(v)
   if v in ss:ss.remove(v)
   else:ss.add(v)
  return ss
 def associate(self,S,T):
  S=self.poly(S);T=self.poly(T)
  return any(S=={self.norm(add(t,sub(s,v))) for t in T} for s in S for v in T)
 def isJ(self,S):
  S=self.poly(S)
  if len(S)!=3:return None
  s=next(iter(S));ss={self.norm(sub(t,s)) for t in S}
  for d in ss-{Z}:
   if self.norm(mul(d,3))==Z and ss=={Z,d,self.norm(mul(d,2))}:return ss
  return None
rows=[l.strip().split('\t') for l in open(ROOT+'mixed_presentations.tsv')]
counts=Counter();fail=[];out=[]
for row in rows:
 r,rank,T,fill,mat,ws=row
 if int(rank)<2 or fill!='0':continue
 mm=list(map(int,mat.strip(',').split(',')));mm=[mm[i:i+4] for i in range(0,16,4)];lat=Lat(mm)
 w=[list(map(int,p.strip(',').split(','))) for p in ws.strip(';').split(';')]
 U=[tuple(p[1:]) for p in w if p[0]==0];V=[tuple(p[1:]) for p in w if p[0]==1]
 if lat.isJ(A) is not None or lat.isJ(B) is not None:cat='order_three_check'
 elif lat.associate(A,B):cat='monomial_associates'
 elif lat.associate(A,[mul(v,2) for v in B]) or lat.associate(B,[mul(v,2) for v in A]):cat='Frobenius_multiple'
 elif lat.associate([mul(v,2) for v in A],[mul(v,2) for v in B]):cat='equal_squares'
 elif (J:=lat.isJ(U)) is not None and lat.isJ(V)==J:cat='order_three_projector'
 else:cat='UNRESOLVED';fail.append(row)
 counts[(r,rank,T,cat)]+=1
 out.append({'split':r,'free_rank':rank,'torsion_order':T,'category':cat,'matrix':mm,'w':w})
print('counts',counts);print('unresolved',len(fail))
for f in fail[:10]:print(f)
json.dump({'counts':{str(k):v for k,v in counts.items()},'unresolved':fail,'certificates':out},open(ROOT+'rank_two_certificates.json','w'),indent=2)
