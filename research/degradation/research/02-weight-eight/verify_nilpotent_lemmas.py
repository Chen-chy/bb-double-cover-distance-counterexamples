"""Finite GF(2) sanity checks for the two uniformly proved nilpotent lemmas.
These checks verify cycles, ranks and nonboundary status, not minimum distances.
The mathematical proof does not extrapolate from these finite tests.
"""
from pathlib import Path
import math,json
ROOT=Path(__file__).resolve().parent

def basis(vs):
 piv={}
 for v in vs:
  while v:
   j=v.bit_length()-1
   if j in piv:v^=piv[j]
   else:piv[j]=v;break
 return piv

def remainder(v,piv):
 while v:
  j=v.bit_length()-1
  if j not in piv:return v
  v^=piv[j]
 return 0

class Ring:
 def __init__(self,l,m):self.l=l;self.m=m;self.N=l*m;self.coords=[(i,j)for j in range(m)for i in range(l)]
 def add(self,a,b):return ((a[0]+b[0])%self.l,(a[1]+b[1])%self.m)
 def sc(self,a,n):return (a[0]*n%self.l,a[1]*n%self.m)
 def poly(self,ps):
  out=set()
  for a in ps:
   if a in out:out.remove(a)
   else:out.add(a)
  return out
 def prod(self,A,B):return self.poly(self.add(a,b)for a in A for b in B)
 def bits(self,P):return sum(1<<(a[0]+a[1]*self.l)for a in P)
 def test(self,A,B,U,V):
  assert len(A)==len(B)==3
  assert self.prod(A,U)==self.prod(B,V)
  checks=[self.bits({self.add(a,g)for a in B})|(self.bits({self.add(a,g)for a in A})<<self.N)for g in self.coords]
  p=basis(checks);k=2*self.N-2*len(p)
  if k:
   w=self.bits(U)|(self.bits(V)<<self.N)
   assert remainder(w,p)
  return k

cyc=[]
for M in (2,4,8,16):
 R=Ring(3*M,3);t=(3,0);x=(1,0);y=(0,1);B={(0,0),x,y}
 for a in range(M):
  for b in range(M):
   A={(0,0),R.add(R.sc(t,a),x),R.add(R.sc(t,b),y)}
   g=math.gcd(M,a,b);order=M//g;U={R.sc(t,g*j)for j in range(order)}
   k=R.test(A,B,U,U);assert k>0
   cyc.append({'M':M,'a':a,'b':b,'k':k,'logical_weight':2*len(U)})

twist_checked=0;twist_positive=0;ks=set()
for l,m in ((6,3),(6,6)):
 R=Ring(l,m);ts=[t for t in R.coords if t!=(0,0) and R.sc(t,2)==(0,0)]
 for t in ts:
  e={(0,0),t}
  for x in R.coords:
   for y in R.coords:
    A=R.poly([(0,0),x,y]);B=R.poly([(0,0),R.add(t,R.sc(x,2)),R.add(t,R.sc(y,2))])
    if len(A)!=3 or len(B)!=3:continue
    U=R.prod(e,A);k=R.test(A,B,U,e);twist_checked+=1
    if k:
     assert len(U)+len(e)<=8;twist_positive+=1;ks.add(k)
res={'cyclic_twist_test_cases':len(cyc),'cyclic_twist_orders_tested':[2,4,8,16],'cyclic_twist_all_witnesses_nonboundary':True,'twisted_square_strict_cases_checked':twist_checked,'twisted_square_positive_dimension_cases':twist_positive,'twisted_square_k_values':sorted(ks),'minimum_distances_computed':False}
(ROOT/'nilpotent_verification.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
