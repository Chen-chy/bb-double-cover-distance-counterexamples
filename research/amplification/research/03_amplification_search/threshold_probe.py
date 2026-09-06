from scan import *
import sys
seed,a,b=map(int,sys.argv[1:4]);e=Engine(order=73)
with gzip.open(ROOT/f'audited_{seed}.jsonl.gz','rt') as f:rows=[json.loads(x) for x in f]
rows=[r for r in rows if 'audited_upper' not in r and r['cover_test']['k']!=2*r['k']][a:b]
stats=Counter();out=[];st=time.time()
for r in rows:
 r=r.copy();rs=[]
 for bound in [20,24]:
  s=e.run(r['cl'],r['cm'],r['At'],r['Bt'],bound,300000);s['order']=73;rs.append(s);stats['queries']+=1
  if s['found']:
   stats[f'witness_weight_{len(s["witness"])}']+=1;break
 r['probes']=rs;out.append(r)
e.close();(ROOT/f'threshold_probe_{seed}_{a}_{b}.json').write_text(json.dumps(dict(stats=dict(stats),seconds=time.time()-st,results=out),indent=2)+'\n');print(dict(stats),'seconds',time.time()-st,flush=True)
