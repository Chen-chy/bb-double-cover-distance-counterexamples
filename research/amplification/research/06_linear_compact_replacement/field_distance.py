"""Exhaustive small F_4 kernel-distance checks, independently using dense elimination.
These are classical finite-field code distances, not quantum BB distances.
"""
from pathlib import Path
from itertools import product
import json
F=[[0]*4 for _ in range(4)]
for a in range(4):
 for b in range(4):
  p=0
  for k in range(2):
   if b>>k&1:p^=a<<k
  if p&8:p^=14
  if p&4:p^=7
  F[a][b]=p

def kern(M,m,j):
 n=M*m
 def add(t,a,b):return (((t//m+a)%M)*m+(t%m+b)%m)
 A=[[0]*n for _ in range(n)]
 for t in range(n):
  for dest,c in [(t,1),(add(t,1,0),2),(add(t,j,1),3)]:A[dest][t]^=c
 piv=[];r=0
 for col in range(n):
  p=next((i for i in range(r,n) if A[i][col]),None)
  if p is None:continue
  A[r],A[p]=A[p],A[r];iv=next(k for k in (1,2,3) if F[A[r][col]][k]==1)
  A[r]=[F[x][iv] for x in A[r]]
  for i in range(n):
   if i!=r and A[i][col]:
    c=A[i][col];A[i]=[x^F[c][y] for x,y in zip(A[i],A[r])]
  piv.append(col);r+=1
 free=[x for x in range(n) if x not in piv];out=[]
 for c in free:
  v=[0]*n;v[c]=1
  for i,p in enumerate(piv):v[p]=A[i][c]
  out.append(v)
 return out
res=[]
for M,m,j in [(1,1,0),(2,1,0),(2,2,0),(4,1,0),(4,2,0),(4,2,1),(4,2,2),(4,4,0),(4,4,1),(8,2,0),(8,2,3),(8,4,0),(8,4,3),(8,8,0),(8,8,1)]:
 vs=kern(M,m,j);n=M*m;best=n+1
 for coeff in product(range(4),repeat=len(vs)):
  if not any(coeff):continue
  word=[0]*n
  for c,v in zip(coeff,vs):
   if c:word=[x^F[c][y] for x,y in zip(word,v)]
  wt=sum(bool(x) for x in word)
  if wt<best:best=wt;wit=word
 row=dict(M=M,m=m,j=j,dimension=len(vs),distance=best,prediction=(M//m)*3**(m.bit_length()-1))
 print(row,flush=True);res.append(row)
open(Path(__file__).with_name('field_distances.json'),'w').write(json.dumps(res,indent=2))
# Negative control: odd-character resonances can invalidate a formula obtained
# by replacing the transcendental coefficient by an arbitrary field element.
vs=kern(3,3,0);best=10
for coeff in product(range(4),repeat=len(vs)):
 if not any(coeff):continue
 word=[0]*9
 for c,v in zip(coeff,vs):word=[x^F[c][y] for x,y in zip(word,v)]
 best=min(best,sum(bool(x) for x in word))
assert len(vs)==2 and best==6
negative={'group':[3,3],'field':'F_4','alpha':2,'kernel_dimension':len(vs),
          'specialized_distance':best,'generic_transcendental_distance':9,
          'conclusion':'Odd torsion requires a genuinely generic coefficient in the lower-bound lemma.'}
Path(__file__).with_name('odd_resonance_negative_control.json').write_text(json.dumps(negative,indent=2)+'\n')
print(negative)
