"""Exact independent finite-ring and Bellman-certificate checks.
No Dijkstra/trellis search is used by the certificate verifier.
"""
from __future__ import annotations
import array, json, math, random
from pathlib import Path
from core import *

# A finite monomial algebra is represented by explicit permutation tables.
class Ring:
 def __init__(self,L,eps=0,cover=True):
  self.L=L;self.eps=eps;self.cover=cover;self.N=L*(2 if cover else 1)
 def idx(self,s,j):
  q,r=divmod(j,self.L)
  return (((s+self.eps*q)&1)*self.L+r) if self.cover else r
 def element(self,p0,p1=0):
  r=0
  for s,p in enumerate((p0,p1)):
   for j in supp(p):r^=1<<self.idx(s,j)
  return r
 def shift(self,p,s,j):
  r=0
  for i in supp(p):r^=1<<self.idx(i//self.L+s,i%self.L+j)
  return r
 def multiply(self,p,q):
  r=0
  for i in supp(q):r^=self.shift(p,i//self.L,i%self.L)
  return r

def addbasis(basis,x):
 while x:
  j=x.bit_length()-1
  if j in basis:x^=basis[j]
  else:basis[j]=x;return True
 return False

def inbasis(basis,x):
 while x:
  j=x.bit_length()-1
  if j not in basis:return False
  x^=basis[j]
 return True

def code(A,B,L,eps=0,lam=1):
 R=Ring(L,eps);At=R.element(A^1,1);Bt=R.element(B^lam,lam)
 basis={}
 for i in range(R.N):
  addbasis(basis,R.shift(Bt,i//L,i%L)|(R.shift(At,i//L,i%L)<<R.N))
 def check(y):
  left=R.element(y[0],y[1]);right=R.element(y[2],y[3]);v=left|(right<<R.N)
  syndrome=R.multiply(At,left)^R.multiply(Bt,right)
  return syndrome==0,not inbasis(basis,v),v.bit_count()
 return R,basis,check

def physical(A,C,delta,k,lam=1,h=0,B=None):
 U=mul(exact(C,delta),k);V=mul(exact(square(A),delta),k)
 y=[mul(A^1,U)^(V if lam else 0),U,V,0]
 if h:
  assert B is not None
  for i,t in enumerate([B^lam,lam,A^1,1]):y[i]^=mul(t,h)
 return y

def universal_syndrome(A,B,lam,y):
 u0,u1,v0,v1=y;a=A^1;b=B^lam
 return (mul(a,u0)^u1^mul(b,v0)^(v1 if lam else 0),
         u0^mul(a,u1)^(v0 if lam else 0)^mul(b,v1))

def verify_bellman(row):
 cols=[[poly(*p) for p in col]for col in row['generator']]
 labels=row['labels'];ds=row['degrees'];c=row['modulus'];cd=deg(c);D=sum(ds);M=1<<D
 vals=array.array('H');vals.frombytes(Path(row['potential']).read_bytes());N=1<<(D+cd)
 assert len(vals)==N and vals[0]==0
 target=row['distance'];assert max(vals)<=target
 offsets=[];t=0
 for d in ds:offsets.append(t);t+=d
 # Read all input edges, recomputing outputs directly from the polynomial coefficients.
 edges=0
 for state in range(N):
  memories=[(state>>o)&((1<<d)-1)for o,d in zip(offsets,ds)]
  label=state>>D
  if (state&(M-1))==0 and label:assert vals[state]>=target
  for bits in range(1<<len(cols)):
   nxtmem=0;nxtlabel=label;out=[0]*len(cols[0])
   for j,(g,d,o,memory) in enumerate(zip(cols,ds,offsets,memories)):
    bit=(bits>>j)&1;reg=(memory<<1)|bit
    for k,p in enumerate(g):out[k]^=(reg&p).bit_count()&1
    nxtmem|=(reg&((1<<d)-1))<<o
    if bit:nxtlabel^=labels[j]
   nxtlabel=(nxtlabel>>1)^((c>>1) if nxtlabel&1 else 0)
   dest=nxtmem|(nxtlabel<<D);weight=sum(out)
   assert vals[dest]<=vals[state]+weight,(state,dest)
   edges+=1
 # Verify the supplied finite polynomial path and its nonzero class.
 fs=[poly(*v)for v in row['input_exponents']]
 out=[0]*len(cols[0]);label=0
 for f,g,l in zip(fs,cols,labels):
  label^=mod(mul(f,l),c)
  for k,p in enumerate(g):out[k]^=mul(p,f)
 assert label and weights(out)==target
 assert [supp(x)for x in out]==row['physical']
 return {'states':N,'edges_checked':edges,'distance':target}

def verify_family():
 data=json.loads(Path('family_certificate.json').read_text());A=poly(*data['A']);B=poly(*data['B']);c=poly(*data['c']);delta=poly(*data['delta'])
 assert gcd(A,B)==c and gcd(square(A),A^B)==delta and delta==square(c)
 # Verify each encoder column and its class without trusting its column reduction.
 for name in ['base','cover']:
  row=data[name]
  coordinates=[]
  for col,label in zip(row['generator'],row['labels']):
   v=[poly(*p)for p in col]
   if name=='base':
    assert mul(A,v[0])==mul(B,v[1]);k=exact(v[1],exact(A,c))
   else:
    assert universal_syndrome(A,B,1,v)==(0,0)
    U=v[1]^v[3];V=v[2]^mul(A^1,v[3]);k=exact(V,exact(square(A),delta))
    assert U==mul(exact(A^B,delta),k)
   assert mod(k,c)==label
   coordinates.append((k,v[3] if name=='cover' else 0))
  if name=='cover':
   assert mul(coordinates[0][0],coordinates[1][1])^mul(coordinates[1][0],coordinates[0][1])==1
  else:assert coordinates[0][0]==1
 summary={name:verify_bellman(data[name])for name in ['base','cover']}
 finite=[]
 for L in [105,111,117,129]:
  R,bb,check=code(A,B,L)
  y=[poly(*p)for p in data['cover']['physical']]
  assert check(y)==(True,True,14)
  assert 2*R.N-2*len(bb)==4
  R0=Ring(L,cover=False);aa=R0.element(A);bc=R0.element(B);basis={}
  for i in range(L):addbasis(basis,R0.shift(bc,0,i)|(R0.shift(aa,0,i)<<L))
  u,v=[poly(*p)for p in data['base']['physical']];uu=R0.element(u);vv=R0.element(v)
  assert R0.multiply(aa,uu)^R0.multiply(bc,vv)==0
  assert not inbasis(basis,uu|(vv<<L)) and (uu.bit_count()+vv.bit_count())==8
  assert 2*L-2*len(basis)==4
  # The entire compact base transfer image is killed: a basis 1,z of S/(c).
  for f in [1,2]:
   u=mul(exact(B,c),f);v=mul(exact(A,c),f)
   assert check([u,u,v,v])[0:2]==(True,False)
  finite.append({'L':L,'base_n':2*L,'cover_n':4*L,'base_k':4,'cover_k':4,'base_witness':8,'cover_witness':14})
 summary['finite_independent_checks']=finite
 return summary

def verify_theorems():
 rng=random.Random(20260906);checked=0;membership=0;transfers=0;selectors=0;selector_sizes={};transfer_losses=0;critical=0;frobenius=0
 # Deliberately include equal odd/even terms, no-twist B, mixed parity, and nonsplit seams.
 tris=[poly(0,i,j)for i in range(1,12)for j in range(i+1,13)]
 cases=[]
 for lam in [0,1]:
  for A in tris:
   for B in tris:
    if math.gcd(*supp(A)[1:],*supp(B)[1:])!=1:continue
    c=gcd(A,B)
    if c==1:continue
    for L in [15,18,21,30,35]:
     g0=gcd(c,(1<<L)^1)
     if g0==1:continue
     cases.append((A,B,c,L,lam))
 rng.shuffle(cases)
 for A,B,c,L,lam in cases[:180]:
  C=B^(A if lam else 0);delta=gcd(square(A),C)
  for eps in [0,1]:
   F=(1<<L)^((A^1) if eps else 1);gp=gcd(delta,F)
   assert gp!=1
   R,basis,check=code(A,B,L,eps,lam)
   assert 2*R.N-2*len(basis)==2*deg(gp)
   for _ in range(4):
    k=rng.getrandbits(16);h=rng.getrandbits(8)
    y=physical(A,C,delta,k,lam,h,B)
    assert universal_syndrome(A,B,lam,y)==(0,0)
    result=check(y)
    assert result[0] and result[1]==bool(mod(k,gp))
    membership+=1
   g0=gcd(c,(1<<L)^1)
   f=rng.getrandbits(8)
   if not mod(f,g0):f^=1
   u=mul(exact(B,c),f);v=mul(exact(A,c),f);w=u.bit_count()+v.bit_count()
   transfer=check([u,u,v,v]);expect=bool(mod(mul(exact(delta,c),f),gp))
   assert transfer[0] and transfer[1]==expect and transfer[2]<=2*w
   transfers+=1;transfer_losses+=not expect
   # The tempting 3w Frobenius cycle is a multiple of the transfer class.
   uf=square(u);vf=square(v)
   fy=[mul(A^1,uf),uf,mul(B^lam,vf),vf if lam else 0]
   assert universal_syndrome(A,B,lam,fy)==(0,0)
   aa=exact(A,c);bb=exact(B,c);q=mul(mul(aa,bb),square(f))
   bd=[mul(B^lam,q),q if lam else 0,mul(A^1,q),q]
   coefficient=mul(bb^(aa if lam else 0),square(f))
   ex=[mul(bb,coefficient),mul(bb,coefficient),mul(aa,coefficient),mul(aa,coefficient)]
   assert [x^y for x,y in zip(fy,bd)]==ex
   if not expect:assert check(fy)[0:2]==(True,False)
   frobenius+=1
   # Normalized A primitive => c squarefree.
   primitive=any(j%2 for j in supp(A))
   if primitive:assert gcd(c,derivative(c))==1
   pa=sum(j%2 for j in supp(A)[1:]);pb=sum(j%2 for j in supp(B)[1:])
   if lam==0 and pb:assert delta==c
   if lam==1 and (pa,pb) not in [(1,1),(2,2)]:assert delta==c
   if primitive and C and (parity(C,0)==0 or parity(C,1)==0):
    eta=1 if parity(C,0)==0 else 0
    assert delta==square(c)
    variants=[]
    orientations=[(A,B,u,v)]
    if lam:orientations.append((B,A,v,u))
    for AA,BB,uu,vv in orientations:
     U=uu^(vv if lam else 0);V=mul(AA,vv)
     assert (not eta)or(not(U&1))
     for i in [0,1]:
      Ui=parity(U>>eta,i)<<eta;Vi=parity(V,i)
      y=[mul(AA^1,Ui)^(Vi if lam else 0),Ui,Vi,0]
      if AA!=A or BB!=B:y=[y[2],y[3],y[0],y[1]]
      assert universal_syndrome(A,B,lam,y)==(0,0)
      rr=check(y);assert rr[0] and rr[1]
      variants.append(weights(y));selectors+=1
    bound=(3*w)//2 if lam==0 else 3*w
    assert min(variants)<=bound
    selector_sizes[(lam,eta)]=selector_sizes.get((lam,eta),0)+1
   # Both checks have one odd and one positive even nonconstant exponent.
   if lam and len([j for j in supp(A)[1:]if j%2])==1 and len([j for j in supp(B)[1:]if j%2])==1:
    C0=cartier(C,0);C1=cartier(C,1);r=gcd(gcd(A,C0),C1)
    assert delta==mul(c,r)
    if eps or L%2:assert gp==g0
    else:assert expect
    critical+=1
   checked+=1
 return dict(finite_codes=checked,compact_membership_checks=membership,transfer_checks=transfers,transfer_losses=transfer_losses,selector_witnesses=selectors,selector_cases={str(k):v for k,v in selector_sizes.items()},mixed_parity_identity_checks=critical,frobenius_class_identity_checks=frobenius)

if __name__=='__main__':
 summary={'family':verify_family(),'uniform_formulas':verify_theorems()}
 Path('verification_summary.json').write_text(json.dumps(summary,indent=2))
 print(json.dumps(summary,indent=2))
