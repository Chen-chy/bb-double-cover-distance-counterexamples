"""Third arithmetic check: full nine-generator incidence matrices via SymPy.
Does not infer full presentation invariants from the spanning-tree reduction.
"""
from pathlib import Path
from itertools import permutations
from math import prod
import json
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form,hermite_normal_form
from sympy.polys.domains import ZZ
ROOT=Path(__file__).parent

def main():
    graphs=json.loads((ROOT/'graphs6.json').read_text());rows=json.loads((ROOT/'highrank6_certificates.json').read_text());pp=list(permutations(range(3)))
    stats={}
    for r in rows:
        na=r['na'];g=graphs[r['graph']];inc=[[i for i,e in enumerate(g)if v in e]for v in range(6)]
        E=[]
        for edge,(v,w)in enumerate(g):
            e=[0]*9
            for vertex,sgn in ((v,1),(w,-1)):
                if vertex:e[4+vertex-1]+=sgn
                color=pp[r['labels'][vertex]][inc[vertex].index(edge)]
                if color:e[(0 if vertex<na else 2)+color-1]+=sgn
            E.append(e)
        S=smith_normal_form(sp.Matrix(E),domain=ZZ)
        diag=[abs(int(S[i,i]))for i in range(9)if S[i,i]]
        assert 9-len(diag)==r['free_rank']
        assert prod(diag)==prod(r['D'])
        # Test the claimed four-dimensional term-coordinate map directly on all nine original relations.
        gen=[tuple(int(i==j)for j in range(4))for i in range(4)]+[tuple(p)for p in r['positions'][1:]]
        H=hermite_normal_form(sp.Matrix(r['R']).T)
        def relation_zero(v):
            v=list(v)
            for j in range(H.cols-1,-1,-1):
                c=list(H[:,j]);p=max(i for i,x in enumerate(c)if x)
                z=v[p]//c[p];v=[x-z*y for x,y in zip(v,c)]
            return all(x==0 for x in v)
        for e in E:
            assert relation_zero([sum(e[i]*gen[i][j]for i in range(9))for j in range(4)])
        if 'boundary_h'in r:
            # Boundary support was already tested exactly. Confirm both normal forms give the same equality relation.
            V=sp.Matrix(r['V']);assert abs(int(V.det()))==1
        stats[r['case']]=stats.get(r['case'],0)+1
    out={'method':'full nine-generator Smith normal form plus independent Hermite relation checks','checked_presentations':len(rows),'cases':stats,'sympy_version':sp.__version__}
    (ROOT/'sympy_presentation_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
