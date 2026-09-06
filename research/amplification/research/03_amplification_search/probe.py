from scan import *
import sys
seed,a,b=map(int,sys.argv[1:4]);orders=[19,73,211,2027];cap=1000000
inp=json.loads((ROOT/f'wide_{seed}.json').read_text());rows=(inp['promising']+inp['candidates'])[a:b];eng=[Engine(i) for i in orders];records=[];left=[];candidates=[];stats=Counter();st=time.time()
for row in rows:
 r=row.copy();attempts=[]
 for order,e in zip(orders,eng):
  up=e.run(r['cl'],r['cm'],r['At'],r['Bt'],r['cover_test']['bound'],cap);up['order']=order;attempts.append(up);stats['queries']+=1
  if up['found']:
   stats['short_logical_found']+=1;break
  if not up['cutoff']:
   stats['certified_exclusions']+=1;print('EXCLUDED',json.dumps(r),json.dumps(up),flush=True);candidates.append(r);break
 else:left.append(r);stats['unresolved']+=1
 r['probes']=attempts;records.append(r)
for e in eng:e.close()
out=dict(stats=dict(stats),seconds=time.time()-st,results=records,promising=left,candidates=candidates)
(ROOT/f'probe_{seed}_{a}_{b}.json').write_text(json.dumps(out,indent=2)+'\n');print('FINAL',dict(stats),'seconds',out['seconds'],flush=True)
