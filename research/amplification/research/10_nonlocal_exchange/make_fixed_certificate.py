"""Construct a Bellman lower certificate for ONE fixed homology message.
It is not a certificate for the unrestricted compact minimum.
"""
from pathlib import Path
import sys,json,struct,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from laurent import *
from graph_completion import Resonance
from forest_model import Model

R=Resonance(1,-2,3)
f=poly([-15,-5,-2,-1,0,4,8,9,13,14,16,17,18,20,28,29,30,34,35,41,44,45])
h=poly([-19,-18,-14,-13,-4,0,5,6,10,13,15,20,25,28,38])
alpha,beta,sigma=R.graph_data(f)
M=Model((11,5),(alpha,beta),sigma)
lo,hi=M.lo,M.hi;memory=11;states=1<<memory;length=hi+memory-lo+1
B=hi-lo+2;INF=1<<30
# Standard forward memory encoding: bit zero is the preceding spin.
x=np.arange(states,dtype=np.int64)
V=np.full((length+1,states),INF,dtype=np.int64);V[-1,0]=0
for ii in range(length-1,-1,-1):
 i=lo+ii
 for b in ([0,1] if i<=hi else [0]):
  cost=(int(i in sigma)^b)+b
  cost=cost+(int(i in alpha)^b^((x>>10)&1))
  cost=cost+(int(i in beta)^b^((x>>4)&1))
  ns=((x<<1)&(states-1))|b
  val=np.minimum(INF,cost*B+b+V[ii+1,ns])
  V[ii]=np.minimum(V[ii],val)
energy=R.energy(f,h)
assert energy==74 and len(h)==15
claim=energy*B+len(h)
assert V[0,0]==claim
s=0;pcost=0
for ii in range(length):
 i=lo+ii;b=int(i in h)
 cost=(int(i in sigma)^b)+b+(int(i in alpha)^b^((s>>10)&1))+(int(i in beta)^b^((s>>4)&1))
 pcost+=cost*B+b;s=((s<<1)&(states-1))|b
assert s==0 and pcost==claim
physical=R.physical(f,h)
T=poly(range(0,30,5))
comps,conf=M.candidates()
assert T in [C for C,_ in comps]
assert T <= h and not (T&sigma)
# Produce a dual functional for a finite quotient, independently checked later.
L=501;n=4*L;site_mask=(1<<L)-1
A0=R.A^ONE;B0=R.B^ONE

def pbits(P):
 out=0
 for i in P:out^=1<<(i%L)
 return out

def rot(v,j):
 j%=L
 return ((v<<j)&site_mask)^(v>>(L-j)) if j else v

def twoshift(P0,P1,j,t):
 a,b=rot(pbits(P0),j),rot(pbits(P1),j)
 return (b|(a<<L)) if t else (a|(b<<L))
boundaries=[twoshift(B0,ONE,j,t)|(twoshift(A0,ONE,j,t)<<(2*L)) for t in (0,1) for j in range(L)]
basis={}
for w in boundaries:
 while w:
  p=w.bit_length()-1
  if p not in basis:basis[p]=w;break
  w^=basis[p]
primal=sum(pbits(P)<<(i*L) for i,P in enumerate(physical))
r=primal
while r and r.bit_length()-1 in basis:r^=basis[r.bit_length()-1]
assert r
k=r.bit_length()-1;dual=1<<k
for p in sorted(basis):
 if (basis[p]&dual).bit_count()%2:dual^=1<<p
assert all((v&dual).bit_count()%2==0 for v in boundaries)
assert (primal&dual).bit_count()%2==1
assert len(basis)==2*L-2
file=ROOT/'fixed_message_potential.bin'
with file.open('wb') as out:
 out.write(b'BBTREE01');out.write(struct.pack('<II',length+1,states));out.write(V.astype('<u4').tobytes())
metadata={'scope':'minimum energy and minimum field support for ONE fixed message, NOT the full compact minimum',
 'parameters':{'r':1,'s':-2,'g':3},'phi':sorted(f),'h':sorted(h),'physical':[sorted(P) for P in physical],
 'alpha':sorted(alpha),'beta':sorted(beta),'sigma':sorted(sigma),
 'anchor_interval':[lo,hi],'memory':memory,'layers':length+1,'states':states,'scale':B,'infinity':INF,
 'energy':energy,'minimum_field_support':len(h),'lexicographic_minimum':claim,
 'source_free_tree':sorted(T),'candidate_trees':len(comps),'candidate_conflicts':len(conf),
 'source_vertices':len(sigma),'finite_nonboundary':{'L':L,'dual_hex':hex(dual),'boundary_rank':len(basis)},
 'potential_sha256':hashlib.sha256(file.read_bytes()).hexdigest()}
(ROOT/'fixed_message_certificate.json').write_text(json.dumps(metadata,indent=2)+'\n')
print(json.dumps({k:metadata[k] for k in ('energy','minimum_field_support','anchor_interval','source_vertices','candidate_trees','candidate_conflicts','potential_sha256')},indent=2))
