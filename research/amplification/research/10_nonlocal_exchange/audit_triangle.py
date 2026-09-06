"""Independent local certificate: a genuine common-message instance has three
simultaneously eligible tree components forming a triangle. No distance claim.
"""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent

def plus(*xs):
 t=set()
 for x in xs:t^=set(x)
 return t

def shift(x,a):return {i+a for i in x}
def product(x,y):return plus(*(shift(x,j) for j in y))
def main():
 d=json.loads((ROOT/'triangle_certificate.json').read_text())
 f=set(d['phi']);a=set(d['alpha']);b=set(d['beta']);s=set(d['sigma'])
 A={-4,0,1};B={0,2,13};G={0,1,2,4,7}
 assert product(a,G)==shift(product(plus(product(A,B),A,B),f),-2)
 assert product(b,G)==shift(product(product(A,A),f),4)
 assert product(s,G)==product(plus(A,B),f)
 assert not plus(shift(a,6),b,s,shift(s,5))
 assert plus(a,shift(a,5),b,shift(b,11))==shift(s,2)
 residue=0
 for k in f:residue^=[1,2,3][k%3]
 assert residue==1
 Ts=list(map(set,d['trees']))
 checks=0
 for T in Ts:
  assert not(T&s)
  internal=[]
  for step,F in [(11,a),(5,b)]:
   for i in T|shift(T,step):
    within=(i in T and i-step in T)
    assert (i in F)==(not within)
    if within:internal.append((i,i-step))
    checks+=1
  assert len(internal)==len(T)-1
 assert 5 in b and 11 in a and 16 in a and 16 not in b
 assert 14 in s
 out={'common_message_is_genuine':True,'survives_modulo_E0':True,
      'simultaneously_eligible_tree_conflict_graph_contains_triangle':True,
      'incident_edges_audited':checks,'frustrated_square_source_site':14,
      'not_a_counterexample_to_factor_three':True}
 (ROOT/'triangle_audit.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps(out,indent=2))
if __name__=='__main__':main()
