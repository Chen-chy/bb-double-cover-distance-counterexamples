from pathlib import Path
ROOT = Path(__file__).resolve().parent
import random,subprocess,json,time
from algebra import *
exe=str(ROOT/'circuit_search')
def run(L,A,B,w):return json.loads(subprocess.check_output([exe,str(L),*map(str,A),*map(str,B),str(w)]))
rng=random.Random(20260905)
records=[]; st=time.time();tally={}
for L in [39,57,75,93,111]:
    hit=high=0
    for j in range(400):
        A=[0,rng.choice(range(1,L,3)),rng.choice(range(2,L,3))]
        B=[0,rng.choice(range(1,L,3)),rng.choice(range(2,L,3))]
        base=run(L,A,B,6)
        if not base['found']:continue
        if run(L,A,B,4)['found']:continue
        hit+=1
        up=run(2*L,A,B,12)
        if up['found']:continue
        high+=1
        up=run(2*L,A,B,14)
        row=dict(L=L,A=A,B=B,k=base['k'],d=6,k2=up['k'],d2=14 if up['found'] else '>14',base_witness=[base['u'],base['v']],cover_witness=[up.get('u'),up.get('v')])
        records.append(row);print(json.dumps(row),flush=True)
    tally[L]=[hit,high]
    print('TALLY',L,hit,high,'seconds',time.time()-st,flush=True)
open(ROOT/'random_results.json','w').write(json.dumps({'seed':20260905,'trials':400,'records':records,'tally':tally},indent=2)+'\n')
