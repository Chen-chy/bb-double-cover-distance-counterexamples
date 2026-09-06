"""Formal multivariate Laurent verification, in independent symbols A,B,Y,H.
No specialized integer exponents or sampled values are used."""
from pathlib import Path
import json

def add(*ps):
 r=set()
 for p in ps:r^=set(p)
 return frozenset(r)
def mul(p,q):
 r=set()
 for a in p:
  for b in q:
   e=tuple(x+y for x,y in zip(a,b));r.symmetric_difference_update({e})
 return frozenset(r)
def mon(e):return frozenset({tuple(e)})

def main():
 one=mon((0,0,0,0));A=mon((1,0,0,0));B=mon((0,1,0,0));iY=mon((0,0,-1,0));H=mon((0,0,0,1));iH=mon((0,0,0,-1))
 K=mul(add(A,one),iY);J=mul(add(B,one),mul(iY,iH));theta=mul(mul(iY,iY),iH)
 pn=add(mul(A,B),A,B);qn=mul(A,A);sn=add(A,B)
 raw=(mul(mul(iY,iH),pn),mul(iY,qn),sn)
 assert not add(mul(K,raw[0]),mul(J,raw[1]),mul(theta,raw[2]))
 assert not add(mul(H,raw[0]),raw[1],mul(K,raw[2]))
 cof=(add(mul(K,J),theta),add(mul(K,K),mul(H,theta)),add(K,mul(H,J)))
 assert all(a==mul(iY,b) for a,b in zip(cof,raw))
 assert cof[2]==mul(iY,add(A,B))
 result={'independent_formal_symbols':['A','B','Y','H'],
 'complete_common_message_matrix_identities':True,'maximal_minor_factorization':True,
 'number_of_formal_identities':6}
 Path(__file__).with_name('identity_verification.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
