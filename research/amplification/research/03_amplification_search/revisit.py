from scan import *
import sys
seed=int(sys.argv[1]) if len(sys.argv)>1 else 9301
cap=int(sys.argv[2]) if len(sys.argv)>2 else 50000000
inp=json.loads((ROOT/f'scan_{seed}.json').read_text());e=Engine();out=[];cut=[];allrows=[];stats=Counter();start=time.time()
for i,r in enumerate(inp['promising']+inp['candidates']):
 up=e.run(2*r['L'],r['m'],r['At'],r['Bt'],r['cover_test']['bound'],cap);r=r.copy();r['cover_test']=up;stats['tested']+=1
 if up['found']:stats['short_logical_found']+=1
 elif up['cutoff']:stats['cutoff']+=1;cut.append(r)
 else:
  print('EXCLUDED_THRESHOLD',json.dumps(r),flush=True);stats['certified_exclusions']+=1
  upper=e.run(2*r['L'],r['m'],r['At'],r['Bt'],r['cover_test']['bound']+2,cap)
  r['next_upper']=upper;out.append(r)
  print('UPPER',json.dumps(upper),flush=True)
 allrows.append(r)
 if i%50==0:print('PROGRESS',i,dict(stats),'sec',round(time.time()-start,2),flush=True)
e.close();(ROOT/f'revisit_{seed}_{cap}.json').write_text(json.dumps(dict(stats=dict(stats),seconds=time.time()-start,candidates=out,promising=cut,all_results=allrows),indent=2)+'\n');print('FINAL',dict(stats),'sec',time.time()-start,flush=True)
