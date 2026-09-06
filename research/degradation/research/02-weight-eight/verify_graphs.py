"""Independent graph and colouring completeness check.
Counts labelled regular multigraphs by a degree-sequence recurrence, not by
canonical orbit generation. Verifies representative isomorphism classes,
automorphism groups and colouring orbits using an independent backtracker.
"""
from functools import lru_cache
from itertools import product,combinations
from collections import Counter
from pathlib import Path
import math,json
ROOT=Path(__file__).resolve().parent
@lru_cache(None)
def count_degree(ds):
 ds=tuple(sorted(ds,reverse=True))
 if not ds:return 1
 if ds[0]==0:return 1
 d,*rem=ds
 if d>2*len(rem):return 0
 out=0
 def choose(i,left,new):
  nonlocal out
  if i==len(rem):
   if not left:out+=count_degree(tuple(sorted(new,reverse=True)))
   return
  for k in range(min(2,rem[i],left)+1):choose(i+1,left-k,new+[rem[i]-k])
 choose(0,d,[]);return out
T=[count_degree((3,)*n)for n in range(9)];C=[0]*9
for n in range(1,9):C[n]=T[n]-sum(math.comb(n-1,k-1)*C[k]*T[n-k]for k in range(1,n))

def mappings(A,B):
 n=len(A);p=[-1]*n;used=set();out=[]
 # Strong, isomorphism-invariant local signatures.
 sig=lambda M,i:tuple(sorted(M[i]))
 opts=[[j for j in range(n)if sig(A,i)==sig(B,j)]for i in range(n)]
 def dfs(done):
  if len(done)==n:out.append(tuple(p));return
  candidates=[]
  for i in range(n):
   if p[i]>=0:continue
   vals=[j for j in opts[i]if j not in used and all(A[i][u]==B[j][p[u]]for u in done)]
   if not vals:return
   candidates.append((len(vals),i,vals))
  _,i,vals=min(candidates)
  for j in vals:p[i]=j;used.add(j);dfs(done+[i]);used.remove(j);p[i]=-1
 dfs([]);return out
GR=[];AUT=[]
for line in (ROOT/'graph_multiplicities_8.txt').read_text().splitlines():
 ms=list(map(int,line.split()));M=[[0]*8 for _ in range(8)]
 for (i,j),v in zip(combinations(range(8),2),ms):M[i][j]=M[j][i]=v
 assert len(ms)==28 and set(ms)<={0,1,2} and all(sum(row)==3 for row in M)
 reach={0}
 while True:
  new=reach|{j for i in reach for j in range(8)if M[i][j]}
  if new==reach:break
  reach=new
 assert len(reach)==8
 assert all(not mappings(M,N)for N in GR)
 GR.append(M);AUT.append(mappings(M,M))
assert sum(math.factorial(8)//len(a)for a in AUT)==C[8]
stored={}
for line in (ROOT/'graph_auts_8.txt').read_text().splitlines():
 a=list(map(int,line.split()));gi,n=a[:2];ps=[tuple(a[i:i+8])for i in range(2,len(a),8)]
 assert len(ps)==n and set(ps)==set(AUT[gi])
col=[tuple(map(int,s.split()))for s in (ROOT/'colorings_8.txt').read_text().splitlines()]
assert len(col)==len(set(col))
for g in range(len(GR)):
 for r in range(4,8):
  masks=[m for gg,rr,m in col if (gg,rr)==(g,r)];covered=set()
  for m in masks:
   assert m.bit_count()==8-r and m not in covered
   orb={sum(((m>>i)&1)<<p[i]for i in range(8))for p in AUT[g]}
   if r==4:orb|={255^q for q in orb}
   assert not covered&orb;covered|=orb
  assert covered=={m for m in range(256)if m.bit_count()==8-r}
res={'labelled_counts_all':T,'labelled_counts_connected':C,'connected_eight_types':len(GR),'automorphism_orders':list(map(len,AUT)),'colour_orbits':len(col),'mixed_port_assignments':len(col)*6**6,'pure_port_assignments':len(GR)*6**7}
(ROOT/'graph_verification.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
