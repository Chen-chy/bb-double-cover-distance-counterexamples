"""Exhaustive checks of the exact tree-contraction truth table. Uses direct
edge-energy evaluation, not the forest packing implementation."""
from itertools import product
from pathlib import Path
import json,random

def main():
 rng=random.Random(121);total=0;cases=0
 for n in range(1,5):
  T=set(range(0,3*n,3));edges=[]
  for typ,st in enumerate((1,3)):
   for i in sorted(T|{v+st for v in T}):edges.append((i,i-st,typ))
  external=sorted({v for edge in edges for v in edge[:2]}-T)
  for trial in range(6):
   preferred={v:rng.randrange(2) for v in external}
   signed=[]
   for u,v,typ in edges:
    sign=0 if u in T and v in T else 1^preferred[v if u in T else u]
    signed.append((u,v,sign))
   for bits in product((0,1),repeat=len(external)):
    outside={v for v,b in zip(external,bits) if b}
    def energy(S):
     h=outside|S
     return 2*len(S)+sum(sign^int(u in h)^int(v in h) for u,v,sign in signed)
    baseline=energy(set());best=10**9
    for inside in product((0,1),repeat=n):
     S={v for v,b in zip(sorted(T),inside) if b};best=min(best,energy(S));total+=1
    compatible=all(int(v in outside)==p for v,p in preferred.items())
    assert best==baseline-2*int(compatible)
   cases+=1
 result={'tree_sign_cases':cases,'direct_internal_external_assignments':total,
         'exact_two_unit_all_or_nothing_reward_verified':True}
 Path(__file__).with_name('tree_contraction_verification.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
