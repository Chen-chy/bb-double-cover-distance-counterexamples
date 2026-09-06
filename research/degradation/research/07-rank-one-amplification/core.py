from __future__ import annotations
from itertools import combinations

def deg(a:int)->int:return a.bit_length()-1

def mul(a:int,b:int)->int:
 r=0
 while b:
  t=b&-b; r^=a<<(t.bit_length()-1);b^=t
 return r

def divmodp(a:int,b:int):
 assert b
 q=0; d=deg(b)
 while a and deg(a)>=d:
  k=deg(a)-d;q^=1<<k;a^=b<<k
 return q,a

def mod(a,b):return divmodp(a,b)[1]
def exact(a,b):
 q,r=divmodp(a,b);assert not r,(a,b,r);return q

def gcd(a,b):
 while b:a,b=b,mod(a,b)
 return a

def square(a):
 r=0
 while a:
  v=a&-a;r|=1<<(2*(v.bit_length()-1));a^=v
 return r

def derivative(a):return sum((1<<(i-1)) for i in range(1,a.bit_length(),2) if a>>i&1)
def euler(a):return sum((1<<i) for i in range(1,a.bit_length(),2) if a>>i&1)
def parity(a,i):return sum((1<<j) for j in range(i,a.bit_length(),2) if a>>j&1)
def cartier(a,i):return sum((1<<((j-i)//2)) for j in range(i,a.bit_length(),2) if a>>j&1)
def poly(*exps):return sum(1<<i for i in exps)
def supp(a):return [i for i in range(a.bit_length()) if a>>i&1]
def fmt(a):return '+'.join('1' if i==0 else 'z' if i==1 else f'z^{i}' for i in supp(a)) or '0'
def weights(v):return sum(x.bit_count() for x in v)

def reduce_generator(cols, labels, c):
 cols=[list(v) for v in cols];labels=labels[:];steps=0
 assert len(cols)<=2
 while len(cols)==2:
  ds=[max(map(deg,v)) for v in cols]
  leads=[sum(((v[i]>>ds[j])&1)<<i for i in range(len(v))) for j,v in enumerate(cols)]
  if leads[0]!=leads[1]:break
  hi=0 if ds[0]>=ds[1] else 1;lo=1-hi;k=ds[hi]-ds[lo]
  cols[hi]=[a^(b<<k) for a,b in zip(cols[hi],cols[lo])]
  labels[hi]^=mod(labels[lo]<<k,c);steps+=1
  assert steps<10000
 return cols,labels

def cover_generator(A,B):
 # Both normalized lift constants carry s: At=s+(A+1), Bt=s+(B+1).
 C=A^B; delta=gcd(square(A),C)
 U=exact(C,delta);V=exact(square(A),delta)
 # physical order: left s^0, left s^1, right s^0, right s^1
 return [[mul(A^1,U)^V,U,V,0],[B^1,1,A^1,1]], delta

if __name__=='__main__':
 A=poly(0,1,2)
 for eb in [(8,13),(8,7),(8,19),(14,19),(14,13),(2,7)]:
  B=poly(0,*eb);c=gcd(A,B)
  if c==1:continue
  cols,delta=cover_generator(A,B)
  new,labels=reduce_generator(cols,[1,0],c)
  print(eb,'base',[exact(B,c).bit_count(),exact(A,c).bit_count()],'delta',fmt(delta),'degrees',[max(map(deg,v)) for v in new], 'labels',labels)
