#!/usr/bin/env python3
"""Exact checks of the root determinant bound, Gram identity and Fermat gcds.
These checks accompany, but do not replace, the symbolic proofs.
"""
from __future__ import annotations
import itertools, json, random, time
from pathlib import Path
import sympy as sp

E=[tuple(int(i==j) for i in range(4)) for j in range(4)]
roots=[]
for v in E+[(1,-1,0,0),(0,0,1,-1)]:
    roots.extend([v,tuple(-a for a in v)])

def determinant(a):
    n=len(a)
    if n==0:return 1
    if n==1:return a[0][0]
    return sum((-1)**j*a[0][j]*determinant([r[:j]+r[j+1:] for r in a[1:]]) for j in range(n))

def v2(n):
    k=0
    while n%2==0:n//=2;k+=1
    return k,n

def main():
    start=time.time();counts={}
    for rows in itertools.product(roots,repeat=4):
        d=determinant([list(r) for r in rows]);counts[d]=counts.get(d,0)+1
        assert d in (-1,0,1)
    Q=sp.diag(sp.Matrix([[1,sp.Rational(1,2)],[sp.Rational(1,2),1]]),sp.Matrix([[1,sp.Rational(1,2)],[sp.Rational(1,2),1]]))
    assert Q.det()==sp.Rational(9,16)
    assert all((sp.Matrix([a])*Q*sp.Matrix(a))[0]==1 for a in roots)
    rng=random.Random(20260906)
    for _ in range(200):
        R=sp.Matrix([[rng.randrange(-12,13) for _ in range(4)] for _ in range(3)])
        c=sp.Matrix([(-1)**j*R[:,[k for k in range(4) if k!=j]].det() for j in range(4)])
        assert (R*Q*R.T).det()==Q.det()*(c.T*Q.inv()*c)[0]
        assert R*c==sp.zeros(3,1)
    x,y=sp.symbols('x y');checks=0
    for m in range(1,17):
        rm,om=v2(m)
        for n in range(1,17):
            rn,on=v2(n)
            a=sp.Poly(1+x**m+y**m,x,y,modulus=2)
            b=sp.Poly(1+x**n+y**n,x,y,modulus=2)
            gcd=sp.gcd(a,b)
            expected=sp.Poly(1+x**(om*2**min(rm,rn))+y**(om*2**min(rm,rn)),x,y,modulus=2) if om==on else sp.Poly(1,x,y,modulus=2)
            assert gcd==expected,(m,n,gcd,expected)
            checks+=1
    Cn=sp.Rational(16,3)*(12/sp.pi**2)**sp.Rational(3,4)
    c0=2**sp.Rational(2,3)*3**sp.Rational(1,6)*sp.pi/32
    assert sp.simplify(4*Cn**2*c0**3)==1
    out={'root_quadruples':len(roots)**4,'determinant_counts':counts,
         'max_absolute_root_determinant':1,'gram_identity_exact_tests':200,
         'fermat_gcd_exact_tests':checks,'ambient_constant':str(Cn),
         'ratio_constant':str(c0),'ratio_constant_decimal':float(c0),
         'seconds':round(time.time()-start,3)}
    Path(__file__).with_name('geometry_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
