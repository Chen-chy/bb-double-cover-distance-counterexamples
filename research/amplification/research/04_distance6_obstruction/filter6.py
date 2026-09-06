from pathlib import Path
import json,time
from collections import Counter
from itertools import combinations
from presentations import Group,gf2rank
ROOT=Path(__file__).parent
counts=Counter();retained=[];start=time.time()
for line in (ROOT/'rank2_candidates.jsonl').open():
    r=json.loads(line);G=Group(r['R']);na=r['na'];Z=G.zero
    A=[Z,G.unit(0),G.unit(1)];B=[Z,G.unit(2),G.unit(3)]
    if len(set(A))!=3 or len(set(B))!=3:counts[na,'invalid_terms']+=1;continue
    pos=list(map(G.red,r['positions']))
    cols=[set(G.add(pos[i],x)for x in (A if i<na else B))for i in range(6)]
    checks={x:j for j,x in enumerate(set().union(*cols))}
    bits=[sum(1<<checks[x]for x in c)for c in cols]
    syn=0
    for b in bits:syn^=b
    assert syn==0
    if gf2rank(bits)!=5:counts[na,'not_circuit']+=1;continue
    if na==3:
        boundary=False
        for p in pos[:3]:
            for b in B:
                shift=G.sub(p,b)
                if sorted(G.add(b,shift)for b in B)==sorted(pos[:3])and sorted(G.add(a,shift)for a in A)==sorted(pos[3:]):boundary=True
        if boundary:counts[na,'cofactor_boundary']+=1;continue
    kind='other'
    if any(G.order2(G.sub(a,b))for P in (A,B)for a,b in combinations(P,2)):kind='unit'
    elif G.equiv(A,B):kind='equal'
    elif any(G.equiv([G.scale(a,1<<i)for a in A],B)or G.equiv([G.scale(b,1<<i)for b in B],A)for i in range(1,5)):kind='frobenius'
    else:
        for a in A:
            for b in B:
                shift=G.sub(a,b);AS=set(A);BS={G.add(x,shift)for x in B}
                if len(AS&BS)==2 and G.order2(G.sub(next(iter(BS-AS)),next(iter(AS-BS)))):kind='involution'
    if kind=='other':
        for i in range(5):
            if G.equiv([G.scale(a,1<<i)for a in A],B,free=True)or G.equiv([G.scale(b,1<<i)for b in B],A,free=True):kind='torsion_frobenius';r['power']=1<<i;break
    r.update(kind=kind,free_rank=G.free,D=G.D,V=G.V,A=A,B=B,pos_reduced=pos)
    counts[na,kind]+=1;retained.append(r)
print('seconds',time.time()-start)
for na in (5,4,3):print(na,{k[1]:v for k,v in counts.items()if k[0]==na})
print('retained parameters',Counter((r['kind'],r['free_rank'],tuple(d for d in r['D']if d!=1))for r in retained))
(ROOT/'retained6.json').write_text(json.dumps(retained)+'\n')
(ROOT/'filter6_summary.json').write_text(json.dumps({'counts':{str(k):v for k,v in counts.items()},'retained':len(retained),'seconds':time.time()-start},indent=2)+'\n')
