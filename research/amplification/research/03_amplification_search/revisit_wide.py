from scan import *
import sys
seed=int(sys.argv[1]);a=int(sys.argv[2]);b=int(sys.argv[3]);cap=int(sys.argv[4]) if len(sys.argv)>4 else 50000000
inp=json.loads((ROOT/f'wide_{seed}.json').read_text());rows=(inp['promising']+inp['candidates'])[a:b];e=Engine();out=[];cut=[];allrows=[];stats=Counter();start=time.time()
for i,r in enumerate(rows):
 up=e.run(r['cl'],r['cm'],r['At'],r['Bt'],r['cover_test']['bound'],cap);r=r.copy();r['cover_test']=up;stats['tested']+=1
 if up['found']:stats['short_logical_found']+=1
 elif up['cutoff']:stats['cutoff']+=1;cut.append(r)
 else:
  print('EXCLUDED_THRESHOLD',json.dumps(r),flush=True);stats['certified_exclusions']+=1
  upper=e.run(r['cl'],r['cm'],r['At'],r['Bt'],r['cover_test']['bound']+2,cap)
  r['next_upper']=upper;out.append(r);print('UPPER',json.dumps(upper),flush=True)
 allrows.append(r)
e.close();(ROOT/f'revisit_wide_{seed}_{a}_{b}.json').write_text(json.dumps(dict(stats=dict(stats),seconds=time.time()-start,candidates=out,promising=cut,all_results=allrows),indent=2)+'\n');print('FINAL',dict(stats),'sec',time.time()-start,flush=True)
