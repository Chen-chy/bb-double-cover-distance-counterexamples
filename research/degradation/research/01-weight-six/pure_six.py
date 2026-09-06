import itertools, json, math
from collections import Counter
from functools import reduce
from pathlib import Path
ROOT=str(Path(__file__).resolve().parent)+'/'
graphs=json.load(open(ROOT+'cubic_graphs.json'))
pairs=list(itertools.combinations(range(6),2)); perms=list(itertools.permutations(range(3)))
vec=[(0,0),(1,0),(0,1)]
add=lambda a,b:(a[0]+b[0],a[1]+b[1])
sub=lambda a,b:(a[0]-b[0],a[1]-b[1])
det=lambda a,b:a[0]*b[1]-a[1]*b[0]
cnt=Counter();survive=Counter();examples={};certificates=[]
for gi,g in enumerate(graphs):
 edges=[p for m,p in zip(g['multiplicities'],pairs) for _ in range(m)]
 inc=[[e for e,p in enumerate(edges) if i in p] for i in range(6)]
 # fixed spanning tree
 par=[None]*6;par[0]=(-1,-1);queue=[0]
 for i in queue:
  for e in inc[i]:
   a,b=edges[e];j=a+b-i
   if par[j] is None:par[j]=(i,e);queue.append(j)
 tree={p[1] for p in par[1:]}
 cotree=[e for e in range(9) if e not in tree]
 for pp in itertools.product(perms,repeat=5):
  pseq=[(0,1,2)]+list(pp)
  labels=[{e:vec[l] for e,l in zip(inc[i],pseq[i])} for i in range(6)]
  pos=[None]*6;pos[0]=(0,0)
  for j in queue[1:]:
   i,e=par[j];pos[j]=add(pos[i],sub(labels[i][e],labels[j][e]))
  rel=[sub(add(pos[a],labels[a][e]),add(pos[b],labels[b][e])) for e in cotree for a,b in [edges[e]]]
  D=reduce(math.gcd,(abs(det(a,b)) for a,b in itertools.combinations(rel,2)),0)
  if D:
   member=lambda v:all(det(r,v)%D==0 for r in rel)
  else:
   nonzero=[r for r in rel if r!=(0,0)]
   if not nonzero:member=lambda v:v==(0,0)
   else:
    r=nonzero[0];gd=math.gcd(*r);prim=(r[0]//gd,r[1]//gd)
    step=reduce(math.gcd,(abs(z[0]//prim[0] if prim[0] else z[1]//prim[1]) for z in nonzero),0)
    member=lambda v: det(v,prim)==0 and (v[0]//prim[0] if prim[0] else v[1]//prim[1])%step==0
  if any(member(sub(a,b)) for a,b in itertools.combinations(vec,2)):
   cnt['invalid_A']+=1;continue
  # In a pure cycle all columns must be distinct.
  if any(member(sub(a,b)) for a,b in itertools.combinations(pos,2)):
   cnt['invalid_columns']+=1;continue
  cnt[f'valid_order_{D}']+=1
  if not D:
   print('ERROR rank-positive valid',gi,rel,pos);raise SystemExit(1)
  orders=[D//reduce(math.gcd,[D]+[abs(det(r,sub(a,b))) for r in rel]) for a,b in itertools.combinations(vec,2)]
  if any(o&(o-1)==0 for o in orders):
   cnt['unit']+=1;continue
  inv1=reduce(math.gcd,(abs(x) for r in rel for x in r),0)
  key=(D,inv1,D//inv1)
  survive[key]+=1
  certificates.append({'graph':gi,'labels':pseq,'relations':rel,'positions':pos,'group_type':key})
  examples.setdefault(str(key),{'graph':gi,'labels':pseq,'relations':rel,'positions':pos,'term_difference_orders':orders})
print('counts',cnt)
print('surviving group types',survive)
json.dump({'counts':dict(cnt),'group_types':{str(k):v for k,v in survive.items()},'examples':examples,'certificates':certificates},open(ROOT+'pure_six_results.json','w'),indent=2)
