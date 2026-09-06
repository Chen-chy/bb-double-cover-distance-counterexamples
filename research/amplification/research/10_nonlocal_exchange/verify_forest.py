"""Independent brute-force audit of forest reduction, without using its candidates
for the left-hand minimization. Verifies finite domains of the infinite graph,
with all external spins fixed to zero by the proved extremal-vertex lemma.
"""
from pathlib import Path
import random,json
from forest_model import Model

def main():
 rng=random.Random(20260906);count=0;states=0;trees=0;maxn=0
 for steps in [(1,3),(1,1),(-1,3),(3,5),(-3,-1),(2,3)]:
  for trial in range(48):
   n=rng.randrange(5,12)
   Fs=[]
   for st in steps:
    Fs.append({i for i in range(n) if 0<=i-st<n and rng.random()<0.4})
   S={i for i in range(n) if rng.random()<0.22}
   M=Model(steps,Fs,S)
   vs=M.vertices
   best=(10**9,10**9);opts=[]
   for mask in range(1<<len(vs)):
    h={v for i,v in enumerate(vs) if mask>>i&1}
    # Direct parity evaluation, not Model.energy.
    cost=len(S^h)+len(h)
    for st,F in zip(steps,Fs):
     diff=h^{i+st for i in h}
     cost+=len(set(F)^diff)
    obj=(cost,len(h));states+=1
    if obj<best:best=obj;opts=[h]
    elif obj==best:opts.append(h)
   red,rh=M.exact_reduced()
   assert best==red,(steps,Fs,S,best,red)
   for h in opts:
    for v in h-S:
     assert all((e.sign^int(e.u in h)^int(e.v in h))==0 for e in M.edges if v in (e.u,e.v))
   comps,conf=M.candidates();trees+=len(comps);maxn=max(maxn,max((len(C) for C,_ in comps),default=0))
   count+=1
 result={'tests':count,'all_spin_assignments':states,'candidate_trees':trees,'largest_candidate_tree':maxn,'all_full_and_reduced_minima_agree':True,'minimum_support_agrees':True}
 Path(__file__).with_name('forest_verification.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
