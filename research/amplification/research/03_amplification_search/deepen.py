from scan import *
import sys
seed,a,b=map(int,sys.argv[1:4]);cap=int(sys.argv[4]) if len(sys.argv)>4 else 1000000
inp=json.loads((ROOT/f'wide_{seed}.json').read_text());rows=(inp['promising']+inp['candidates'])[a:b];e=Engine();stats=Counter();done=[];left=[];st=time.time()
for r in rows:
 r=r.copy();attempts=[];success=False
 for bound in range(8,r['cover_test']['bound']+1,2):
  up=e.run(r['cl'],r['cm'],r['At'],r['Bt'],bound,cap);attempts.append(up);stats['queries']+=1
  if up['found']:success=True;stats['witness_found']+=1;stats[f'witness_at_{bound}']+=1;break
  if not up['cutoff'] and bound==r['cover_test']['bound']:
   print('CERTIFIED_RECORD_EXCLUSION',json.dumps(r),json.dumps(up),flush=True);stats['record_exclusion']+=1
 r['deepening']=attempts;done.append(r)
 if not success:stats['unresolved']+=1;left.append(r)
e.close();out=dict(seed=seed,range=[a,b],cap=cap,stats=dict(stats),seconds=time.time()-st,results=done,promising=left);(ROOT/f'deepen_{seed}_{a}_{b}.json').write_text(json.dumps(out,indent=2)+'\n');print('FINAL',dict(stats),'seconds',out['seconds'],flush=True)
