from pathlib import Path
import subprocess,json,random,time,math,gzip,os
from collections import Counter
ROOT=Path(__file__).resolve().parent
class Engine:
 def __init__(self,order=0):
  env=os.environ.copy();env["BB_ORDER"]=str(order)
  self.p=subprocess.Popen([os.environ.get('BB_EXECUTABLE',str(ROOT/'search'))],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True,bufsize=1,env=env)
 def run(self,l,m,A,B,bound,cap=0):
  coords=[z for pt in A+B for z in pt];s=' '.join(map(str,[l,m,*coords,bound,cap]));self.p.stdin.write(s+'\n');self.p.stdin.flush();r=json.loads(self.p.stdout.readline());
  if 'error' in r:raise RuntimeError((s,r))
  return r
 def close(self):self.p.stdin.close();self.p.wait()

def pgcd(a,b):
 while b:
  while a.bit_length()>=b.bit_length():a^=b<<(a.bit_length()-b.bit_length())
  a,b=b,a
 return a

def intpoly(A):return sum(1<<x for x,y in A)

def scan(seed=9301,trials=4000):
 rng=random.Random(seed);e=Engine();stats=Counter();start=time.time();prom=[];ret=[];seen=set();log=gzip.open(ROOT/f'scan_{seed}.jsonl.gz','wt')
 for j in range(trials):
  L=rng.choice(list(range(15,145,6))+[21,27,33,45,63,81,105,126,78,90,102]);m=1
  if rng.random()<0.65:
   A=[(0,0),(rng.randrange(1,L,3),0),(rng.randrange(2,L,3),0)]
   B=[(0,0),(rng.randrange(1,L,3),0),(rng.randrange(2,L,3),0)]
  else:
   A=[(0,0)]+[(x,0) for x in sorted(rng.sample(range(1,L),2))];B=[(0,0)]+[(x,0) for x in sorted(rng.sample(range(1,L),2))]
  if math.gcd(L,*[x for x,y in A+B])!=1:stats['disconnected_skipped']+=1;continue
  if pgcd(pgcd(intpoly(A),intpoly(B)),(1<<L)|1)==1:stats['k0_skipped']+=1;continue
  key=(L,tuple(sorted(A)),tuple(sorted(B)))
  if key in seen:continue
  seen.add(key);base=e.run(L,m,A,B,6,0);stats['base_tests']+=1
  if not base['found']:stats['base_d_gt6']+=1;continue
  lower=e.run(L,m,A,B,4,0)
  if lower['found']:
   d2=e.run(L,m,A,B,2,0)
   if d2['found']:stats['d2_skipped']+=1;continue
   d=4
  else:d=6
  stats[f'base_d{d}']+=1
  for lift in range(16):
   AA=[A[0]]+[(A[i][0]+L*((lift>>(i-1))&1),0) for i in (1,2)]
   BB=[B[0]]+[(B[i][0]+L*((lift>>(i+1))&1),0) for i in (1,2)]
   cb=8 if d==4 else 14
   up=e.run(2*L,1,AA,BB,cb,1000000)
   stats['cover_tests']+=1
   rec=dict(L=L,m=1,A=A,B=B,At=AA,Bt=BB,d=d,k=base['k'],base_witness=base['witness'],lift=lift,cover_test=up)
   log.write(json.dumps(rec)+'\n')
   if not up['found']:
    if up['k']==2*base['k']:stats['doubling_k_skipped']+=1;continue
    if up['cutoff']:stats['cutoffs']+=1;prom.append(rec)
    else:
     stats['record_lower_bound_candidates']+=1;ret.append(rec);print('EXCLUDED_RECORD_THRESHOLD',json.dumps(rec),flush=True)
  if j%100==0:print('PROGRESS',j,dict(stats),'sec',round(time.time()-start,2),flush=True)
 log.close();e.close();out=dict(seed=seed,requested_trials=trials,stats=dict(stats),seconds=time.time()-start,candidates=ret,promising=prom)
 (ROOT/f'scan_{seed}.json').write_text(json.dumps(out,indent=2)+'\n');print('FINAL',dict(stats),'sec',out['seconds'],flush=True)
if __name__=='__main__':
 import sys
 scan(int(sys.argv[1]) if len(sys.argv)>1 else 9301,int(sys.argv[2]) if len(sys.argv)>2 else 4000)
