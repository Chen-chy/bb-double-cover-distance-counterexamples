from itertools import combinations,product
from collections import defaultdict,Counter
import json
from pathlib import Path
ROOT=str(Path(__file__).resolve().parent)+'/'
class Code:
 def __init__(self,rr):
  self.rows=rr
  def norm(v):
   v=list(v)
   for i in range(4):
    t=v[i]//rr[i][i]
    v=[a-t*b for a,b in zip(v,rr[i])]
   return tuple(v)
  self.norm=norm
  self.group=list(product(*(range(rr[i][i]) for i in range(4))))
  self.N=len(self.group);self.idx={g:i for i,g in enumerate(self.group)}
  def shift(poly,g):
   v=0
   for a in poly:
    gg=norm([x+y for x,y in zip(g,a)])
    v ^=1<<self.idx[gg]
   return v
  self.A=[(0,0,0,0),(1,0,0,0),(0,1,0,0)]
  self.B=[(0,0,0,0),(0,0,1,0),(0,0,0,1)]
  aa=[shift(self.A,g) for g in self.group];bb=[shift(self.B,g) for g in self.group]
  self.cols=aa+bb
  self.bounds=[b|(a<<self.N) for a,b in zip(aa,bb)]
  self.basis={};
  for v in self.bounds:
   while v:
    p=v.bit_length()-1
    if p in self.basis:v^=self.basis[p]
    else:self.basis[p]=v;break
  self.k=2*(self.N-len(self.basis))
 def isbound(self,v):
  while v:
   p=v.bit_length()-1
   if p not in self.basis:return False
   v^=self.basis[p]
  return True
 def qbits(self,w):
  v=0
  for b,*g in w:v^=1<<(b*self.N+self.idx[self.norm(g)])
  return v
 def check_le6(self):
  cols=self.cols;n=len(cols);syns={0:[0]}
  # Every even cycle <=6 has a decomposition into two supports of <=3.
  for k in (1,2,3):
   for ss in combinations(range(n),k):
    syn=0;v=0
    for i in ss:syn^=cols[i];v^=1<<i
    bucket=syns.get(syn)
    if bucket is not None:
     for u in bucket:
      z=u^v
      if z and not self.isbound(z):return z
     bucket.append(v)
    else:syns[syn]=[v]
  return None
 def coeff_min(self,q):
  for k in range(1,self.N+1):
   for ss in combinations(range(self.N),k):
    v=0
    for i in ss:v^=self.bounds[i]
    if v==q:return ss

if __name__=='__main__':
 rows=[l.strip().split('\t') for l in open(ROOT+'mixed_presentations.tsv')]
 grouped=defaultdict(list)
 for r,rank,T,fill,mat,w in rows:
  if rank=='0' and fill=='0':grouped[mat].append((r,w))
 counts=Counter();out=[]
 for j,(mat,ww) in enumerate(grouped.items()):
  mm=list(map(int,mat.strip(',').split(',')));mm=[mm[i:i+4] for i in range(0,16,4)]
  code=Code(mm);counts['groups']+=1
  if not code.k:continue
  counts['kpos']+=1
  for r,ws in ww:
   w=[list(map(int,v.strip(',').split(','))) for v in ws.strip(';').split(';')]
   q=code.qbits(w)
   if code.isbound(q):
    counts['qboundary']+=1
    # Correctness of fill classification checked again in the finite group.
    assert all(q!=b for b in code.bounds)
    assert all(q!=(b^c) for b,c in combinations(code.bounds,2))
    small=code.check_le6()
    if small is None:
     coeff=code.coeff_min(q)
     result={'matrix':mm,'group_order':code.N,'k':code.k,'q':w,'q_integer':q,'coefficient_indices':coeff,'coefficient_positions':[code.group[i] for i in coeff]}
     print('FOUND COUNTEREXAMPLE',json.dumps(result),flush=True)
     out.append(result)
    else:counts['small_logical']+=1
    break
  if j%100==0:print('progress',j,dict(counts),flush=True)
 print('counts',dict(counts))
 json.dump({'counts':dict(counts),'counterexamples':out},open(ROOT+'finite_scan_results.json','w'),indent=2)
