from pathlib import Path
ROOT=Path(__file__).resolve().parent
import itertools, json
N=6
perms=list(itertools.permutations(range(N)))
edges=list(itertools.combinations(range(N),2))
# Canonicalize by sorted tuple under all vertex permutations, 15 coordinates.
perm_maps=[[edges.index(tuple(sorted((p[i],p[j])))) for i,j in edges] for p in perms]
count=0; graphs={}
def generate(row,deg,vals):
 global count
 if row==len(edges):
  if any(deg): return
  adj=[[] for _ in range(N)]
  for m,(i,j) in zip(vals,edges):
   if m: adj[i].append(j);adj[j].append(i)
  vis={0};stack=[0]
  while stack:
   for j in adj[stack.pop()]:
    if j not in vis:vis.add(j);stack.append(j)
  if len(vis)<N:return
  count+=1
  key=min(tuple(vals[i] for i in pm) for pm in perm_maps)
  graphs[key]=graphs.get(key,0)+1
  return
 i,j=edges[row]
 for m in range(min(2,deg[i],deg[j])+1):
  dd=deg[:];dd[i]-=m;dd[j]-=m
  if j==N-1 and dd[i]:continue
  generate(row+1,dd,vals+[m])
generate(0,[3]*N,[])
print('labelled',count,'unlabelled',len(graphs))
out=[{'multiplicities':list(k),'labelled_count':v} for k,v in sorted(graphs.items())]
json.dump(out,open(ROOT/'cubic_graphs.json','w'),indent=2)

with open(ROOT/'graph_multiplicities.txt','w') as f:
 for g in out: f.write(' '.join(map(str,g['multiplicities']))+'\n')
