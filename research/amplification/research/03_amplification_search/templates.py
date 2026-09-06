from scan import *
from itertools import combinations

def pmod(a,b):
 while a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
 return a

def pquo(a,b):
 q=0
 while a.bit_length()>=b.bit_length():
  d=a.bit_length()-b.bit_length();q^=1<<d;a^=b<<d
 if a:raise ValueError('nondivisible')
 return q

def supp(a):return [i for i in range(a.bit_length()) if a>>i&1]

def make(D=45):
 rows=[];seen=set()
 for a,b in combinations(range(1,D+1),2):
  A=(1<<b)|(1<<a)|1;seenpowers={};r=1
  for c in range(1,4*b+1):
   r=pmod(r<<1,A)
   for d in seenpowers.get(r^1,[]):
    B=(1<<c)|(1<<d)|1
    if B<=A:continue
    if math.gcd(a,b,c,d)!=1:continue
    Q=pquo(B,A)
    for v in range(1,min(2*b,c)+1):
     U=Q^(Q<<v)
     if U.bit_count()!=4:continue
     key=(a,b,d,c)
     if key in seen:continue
     seen.add(key);rows.append(dict(A=[0,a,b],B=[0,d,c],Q=supp(Q),U=supp(U),V=[0,v]))
   seenpowers.setdefault(r,[]).append(c)
 (ROOT/'templates.json').write_text(json.dumps(rows,indent=2)+'\n');print('templates',len(rows));print(rows[:10])
if __name__=='__main__':make()
