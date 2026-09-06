from pathlib import Path
from collections import Counter
from itertools import combinations
import json
from presentations import Group
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'retained6.json').read_text());C=Counter();bad=[]
def product(G,a,b):
    out=set()
    for x in a:
        for y in b:
            z=G.add(x,y)
            if z in out:out.remove(z)
            else:out.add(z)
    return out
for r in rows:
    G=Group(r['R']);A=list(map(tuple,r['A']));B=list(map(tuple,r['B']));pos=list(map(tuple,r['pos_reduced']));na=r['na'];U=set(pos[:na]);V=set(pos[na:])
    if r['kind']=='other' and na==4:
        hs=set(G.sub(v,a)for v in V for a in A)
        cert=None
        for hh in combinations(hs,2):
            if product(G,A,hh)==V and product(G,B,hh)==U:cert=hh;break
        assert cert is not None,r
        r['case']='two_boundary_sum';r['boundary_h']=cert
    elif r['kind']=='other':
        def finite_support(P):return all(not any(G.freecoord(x))for x in P)
        if finite_support(A)or finite_support(B):
            r['case']='finite_polynomial';r['bound']=6
        else:
            torsgen=next(tuple(int(i==j)if j<G.rank else 0 for j in range(G.n))for i,d in enumerate(G.D)if d>1)
            norm=[G.zero,torsgen,G.scale(torsgen,2)]
            cert=None
            for v in V:
                for a in A:
                    shift=G.sub(v,a);hh=[G.add(x,shift)for x in norm]
                    if product(G,A,hh)==V and product(G,B,hh)==U:cert=hh;break
            assert cert is not None,r
            r['case']='three_boundary_sum';r['boundary_h']=cert
    elif r['kind']=='torsion_frobenius':
        assert r['power']==1
        if G.torsion==3:
            r['case']='odd_three_twist';r['bound']=12
            # The cycle lies in the norm-of-C3 sector; verify explicitly.
            torsgens=[tuple(int(i==j)if j<G.rank else 0 for j in range(G.n))for i,d in enumerate(G.D)if d>1]
            assert len(torsgens)==1
            h=torsgens[0]
            assert G.scale(h,3)==G.zero
            assert product(G,[h],U)==U and product(G,[h],V)==V
        else:
            assert sorted(d for d in G.D if d!=1)==[2,2]
            r['case']='double_involution';r['bound']=12
            # After a monomial gauge aligns free supports, A^2=B^2.
            choices=[]
            for a in A:
                for b in B:
                    shift=G.sub(a,b);B1=[G.add(x,shift)for x in B]
                    if sorted(G.scale(x,2)for x in A)==sorted(G.scale(x,2)for x in B1):
                        # Multiplying B by monomial shift sends middle (U,V) to (shift*U,V).
                        U1={G.add(x,shift)for x in U}
                        # A six-term canonical cycle (A,B1) up to a common monomial.
                        for p in U1:
                            for aa in A:
                                hh=G.sub(p,aa)
                                if {G.add(x,hh)for x in A}==U1 and {G.add(x,hh)for x in B1}==V:
                                    choices.append((shift,hh))
            assert choices,r
            r['gauge_shift'],r['logical_shift']=choices[0]
    elif r['kind']=='frobenius':r['case']='frobenius_square';r['bound']=8
    elif r['kind']=='involution':r['case']='single_involution';r['bound']=8
    elif r['kind']=='unit':r['case']='unit';r['bound']=0
    else:bad.append(r)
    C[na,r.get('case','FAILED')]+=1
assert not bad
(ROOT/'highrank6_certificates.json').write_text(json.dumps(rows,indent=2)+'\n')
print(dict(C))
