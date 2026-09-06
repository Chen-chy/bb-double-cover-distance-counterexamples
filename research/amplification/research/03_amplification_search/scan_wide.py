from scan import *
import sys

def connected(l,m,A,B):
 seen={(0,0)};stack=[(0,0)]
 while stack:
  x,y=stack.pop()
  for a,b in A+B:
   p=((x+a)%l,(y+b)%m)
   if p not in seen:seen.add(p);stack.append(p)
 return len(seen)==l*m

def fpowx(i,g):
 x=1
 for j in range(i):
  x<<=1
  if x.bit_length()==g.bit_length():x^=g
 return x

def run(seed=9302,trials=10000,mode='bivariate',basebound=6,cap=1000000,dmin=4):
 rng=random.Random(seed);e=Engine();stats=Counter();start=time.time();prom=[];ret=[];seen=set();log=gzip.open(ROOT/f'wide_{seed}.jsonl.gz','wt')
 shapes=[(l,m) for l in range(3,49,3) for m in range(2,16) if 15<=l*m<=240]
 gf={7:0b1011,15:0b10011,31:0b100101}
 pairsets={q:[(a,b) for a in range(1,q) for b in range(a+1,q) if fpowx(a,g)^fpowx(b,g)==1] for q,g in gf.items()}
 for j in range(trials):
  if mode=='bivariate':
   l,m=rng.choice(shapes)
   A=[(0,0),(rng.randrange(1,l,3),rng.randrange(m)),(rng.randrange(2,l,3),rng.randrange(m))]
   B=[(0,0),(rng.randrange(1,l,3),rng.randrange(m)),(rng.randrange(2,l,3),rng.randrange(m))]
   if not connected(l,m,A,B):stats['disconnected_skipped']+=1;continue
   directions=[0,1]
  elif mode=='gf':
   q=rng.choice(list(gf));l=rng.choice(list(range(q,241,q)));m=1
   aa=rng.choice(pairsets[q]);bb=rng.choice(pairsets[q]);A=[(0,0)]+[(a+q*rng.randrange(l//q),0) for a in aa];B=[(0,0)]+[(a+q*rng.randrange(l//q),0) for a in bb]
   if math.gcd(l,*[x for x,y in A+B])!=1:stats['disconnected_skipped']+=1;continue
   directions=[0]
  else:raise ValueError(mode)
  key=(l,m,tuple(sorted(A)),tuple(sorted(B)))
  if key in seen:stats['duplicates']+=1;continue
  seen.add(key);base=e.run(l,m,A,B,basebound,0);stats['base_tests']+=1
  if not base['k']:stats['k0_skipped']+=1;continue
  if not base['found']:stats['base_d_gt_bound']+=1;continue
  # Obtain exact base distance through ascending even-weight queries.
  d=None
  for dd in range(2,basebound+1,2):
   br=base if dd==basebound else e.run(l,m,A,B,dd,0)
   if br['found']:d=dd;base=br;break
  if d==2:stats['d2_skipped']+=1;continue
  assert d is not None
  stats[f'base_d{d}']+=1
  if d<dmin:stats['below_target_distance']+=1;continue
  for direction in directions:
   for lift in range(16):
    AA=[A[0]]+[tuple(A[i][c]+(l if c==0 else m)*((lift>>(i-1))&1) if c==direction else A[i][c] for c in (0,1)) for i in (1,2)]
    BB=[B[0]]+[tuple(B[i][c]+(l if c==0 else m)*((lift>>(i+1))&1) if c==direction else B[i][c] for c in (0,1)) for i in (1,2)]
    ll,mm=(2*l,m) if direction==0 else (l,2*m)
    cb=2*((7*d)//6)
    up=e.run(ll,mm,AA,BB,cb,cap);stats['cover_tests']+=1
    rec=dict(l=l,m=m,cl=ll,cm=mm,A=A,B=B,At=AA,Bt=BB,d=d,k=base['k'],base_witness=base['witness'],direction=direction,lift=lift,cover_test=up)
    log.write(json.dumps(rec)+'\n')
    if not up['found']:
     if up['k']==2*base['k']:stats['doubling_k_skipped']+=1;continue
     if up['cutoff']:stats['cutoffs']+=1;prom.append(rec)
     else:
      stats['record_lower_bound_candidates']+=1;ret.append(rec);print('EXCLUDED_RECORD_THRESHOLD',json.dumps(rec),flush=True)
  if j%100==0:print('PROGRESS',j,dict(stats),'sec',round(time.time()-start,2),flush=True)
 log.close();e.close();out=dict(seed=seed,mode=mode,requested_trials=trials,basebound=basebound,cap=cap,stats=dict(stats),seconds=time.time()-start,candidates=ret,promising=prom)
 (ROOT/f'wide_{seed}.json').write_text(json.dumps(out,indent=2)+'\n');print('FINAL',dict(stats),'sec',out['seconds'],flush=True)
if __name__=='__main__':run(int(sys.argv[1]),int(sys.argv[2]),sys.argv[3],int(sys.argv[4]) if len(sys.argv)>4 else 6,int(sys.argv[5]) if len(sys.argv)>5 else 1000000,int(sys.argv[6]) if len(sys.argv)>6 else 4)
