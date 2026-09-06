"""Independent upper-witness audit plus fresh exact base-distance certificates.
A cutoff is never interpreted as a distance lower bound.
"""
from scan import ROOT,Engine
from algebra import poly,support,Group
from independent_search import gcd,divmodp,egcd,mul
from pathlib import Path
from collections import Counter
import gzip,json,sys,time

def norm(r):
    l=r.get('l',r.get('L'));m=r.get('m',1)
    return (l,m,r.get('cl',2*l),r.get('cm',m),tuple(sorted(map(tuple,r['A']))),tuple(sorted(map(tuple,r['B']))),tuple(sorted(map(tuple,r['At']))),tuple(sorted(map(tuple,r['Bt']))))

def harvest():
    best={}
    def add(r,s):
        if not isinstance(s,dict) or not s.get('found') or not s.get('witness'):return
        key=norm(r)
        if key not in best or len(s['witness'])<len(best[key]['witness']):best[key]=s
    def row(r):
        if not isinstance(r,dict) or 'At' not in r:return
        for field in ['cover_test','cover']:add(r,r.get(field))
        for field in ['probes','deepening']:
            for s in r.get(field,[]):add(r,s)
    for path in ROOT.glob('*.jsonl.gz'):
        try:
            with gzip.open(path,'rt') as f:
                for line in f:row(json.loads(line))
        except (EOFError,OSError):pass
    for path in ROOT.glob('*.json'):
        if path.name.startswith(('audit_','base_certificates_')):continue
        data=json.loads(path.read_text())
        if isinstance(data,list):
            for r in data:
                row(r)
                if isinstance(r,dict) and 'candidate' in r:add(r['candidate'],r.get('result'))
        elif isinstance(data,dict):
            for field in ['all_results','results']:
                for r in data.get(field,[]):row(r)
            if 'candidate' in data:add(data['candidate'],data.get('result'))
    return best

def check_witness(l,m,A,B,s):
    M=l*m;z=poly(s['witness']);assert len(set(s['witness']))==len(s['witness']);assert 0<=min(s['witness']) and max(s['witness'])<2*M
    G=Group(l,m);aa=G.from_coords(A);bb=G.from_coords(B);u=z&((1<<M)-1);v=z>>M
    assert G.mul(aa,u)^G.mul(bb,v)==0
    if m==1:
        c=gcd(aa,bb);a=divmodp(aa,c)[0];b=divmodp(bb,c)[0];one,r,t=egcd(a,b);assert one==1
        F=(1<<M)|1;g=gcd(c,F);assert s['k']==2*(g.bit_length()-1)
        first=divmodp(mul(a,u)^mul(b,v),F)[1];second=divmodp(mul(t,u)^mul(r,v),g)[1]
        assert first or second
    else:
        bas={}
        for j in range(M):
            w=G.shift(bb,j//m,j%m)|(G.shift(aa,j//m,j%m)<<M)
            while w:
                p=w.bit_length()-1
                if p not in bas:bas[p]=w;break
                w^=bas[p]
        assert s['k']==2*(M-len(bas))
        w=z
        while w:
            p=w.bit_length()-1
            if p not in bas:break
            w^=bas[p]
        assert w

def main(seed):
    prefix='scan' if seed==9301 else 'wide';best=harvest();stats=Counter();bases={};out=[];e=Engine();st=time.time()
    with gzip.open(ROOT/f'{prefix}_{seed}.jsonl.gz','rt') as f:rows=[json.loads(x) for x in f]
    for r in rows:
        l,m,cl,cm,A,B,At,Bt=norm(r);d=r['d'];stats['cover_instances']+=1
        assert (cl,cm) in [(2*l,m),(l,2*m)]
        assert len(set(A))==len(set(B))==len(set(At))==len(set(Bt))==3
        assert sorted((x%l,y%m) for x,y in At)==list(A) and sorted((x%l,y%m) for x,y in Bt)==list(B)
        bkey=(l,m,A,B)
        if bkey not in bases:
            lo=e.run(l,m,list(A),list(B),d-2);hi=e.run(l,m,list(A),list(B),d)
            assert not lo['found'] and not lo['cutoff'] and hi['found'] and len(hi['witness'])==d and hi['k']==r['k']
            check_witness(l,m,A,B,hi);bases[bkey]=dict(l=l,m=m,A=A,B=B,d=d,k=r['k'],lower=lo,upper=hi)
        assert bases[bkey]['d']==d
        s=best.get(norm(r));threshold=2*((7*d)//6)
        upper=len(s['witness']) if s is not None else float('inf')
        if r['cover_test']['k']==2*r['k']:upper=min(upper,2*d)
        stats['certified_at_7_over_3']+=3*upper<=7*d
        stats['certified_at_5_over_2']+=2*upper<=5*d
        stats['certified_at_3']+=upper<=3*d
        if s is not None:check_witness(cl,cm,At,Bt,s)
        if s is not None and len(s['witness'])<=threshold:
            check_witness(cl,cm,At,Bt,s);stats['audited_upper_witnesses']+=1;r=r.copy();r['audited_upper']=s
        elif r['cover_test']['k']==2*r['k']:
            stats['dimension_doubling_bound']+=1
        else:stats['unresolved_cutoff_cases']+=1
        out.append(r)
    e.close();stats['distinct_base_parameter_sets']=len(bases)
    with gzip.open(ROOT/f'audited_{seed}.jsonl.gz','wt') as f:
        for r in out:f.write(json.dumps(r)+'\n')
    (ROOT/f'base_certificates_{seed}.json').write_text(json.dumps(list(bases.values()),indent=2)+'\n')
    summary=dict(seed=seed,stats=dict(stats),seconds=time.time()-st);(ROOT/f'audit_{seed}.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary),flush=True)
if __name__=='__main__':main(int(sys.argv[1]))
