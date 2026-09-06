"""Exact binary checks for the strict-trinomial filling counterfamily.
No distance is inferred from a search. Distance bounds are proved in proof.md.
Run: python verify_family.py [j ...], where L=4**j. Defaults: j=1,2.
"""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def rank_basis(vectors):
    basis={}
    for v in vectors:
        while v:
            i=v.bit_length()-1
            if i in basis:v^=basis[i]
            else:basis[i]=v;break
    return basis

def member(v,basis):
    while v:
        i=v.bit_length()-1
        if i not in basis:return False
        v^=basis[i]
    return True

def bitpoly(points,l,m):
    z=0
    for i,j in points:z^=1<<((i%l)+l*(j%m))
    return z

def support(v,l):
    while v:
        b=v&-v;i=b.bit_length()-1;v^=b
        yield i%l,i//l

def translate(v,a,b,l,m):
    return bitpoly(((i+a,j+b) for i,j in support(v,l)),l,m)

def multiply(v,poly,l,m):
    out=0
    for a,b in poly:out^=translate(v,a,b,l,m)
    return out

def matrices(A,B,l,m):
    N=l*m
    aa=[bitpoly(((i+a,j+b) for a,b in A),l,m) for j in range(m) for i in range(l)]
    bb=[bitpoly(((i+a,j+b) for a,b in B),l,m) for j in range(m) for i in range(l)]
    return aa+bb,[b|(a<<N) for a,b in zip(aa,bb)]

def f0_polynomial(L,l,m):
    points=[]
    for j in range(L):
        s=j
        while True:
            points.extend((s+k*L,-j-1) for k in range(3))
            if s==0:break
            s=(s-1)&j
    return bitpoly(points,l,m)

def verify(j):
    L=4**j;r=2*j;l=m=3*L;N=l*m
    A=[(0,0),(L+1,0),(2*L,1)];B=[(0,0),(1,0),(0,1)]
    J=bitpoly([(0,0),(L,0),(2*L,0)],l,m);q=J|(J<<N)
    f0=f0_polynomial(L,l,m)
    mu=3**(r+1)
    assert f0.bit_count()==mu
    assert multiply(f0,A,l,m)==multiply(f0,B,l,m)==J
    # Two independent common-kernel words: Trace(c*w^(-i-2j)).
    trace=[0,1,1]  # Trace(1), Trace(w), Trace(w**2)
    kk=[bitpoly(((i,jj) for jj in range(m) for i in range(l)
                 if trace[(c-i-2*jj)%3]),l,m) for c in (0,1)]
    assert kk[0]!=kk[1] and all(kk)
    for k in [kk[0],kk[1],kk[0]^kk[1]]:
        assert k.bit_count()==6*L*L
        assert multiply(k,A,l,m)==multiply(k,B,l,m)==0
    fillings=[f0,f0^kk[0],f0^kk[1],f0^kk[0]^kk[1]]
    weights=[s.bit_count() for s in fillings]
    assert weights==[mu]+[6*L*L-3**r]*3
    hx,bcols=matrices(A,B,l,m)
    bx=rank_basis(hx);bz=rank_basis(bcols)
    assert len(bx)==len(bz)==N-2
    assert member(q,bz)
    # Explicit base logical of weight 4L.
    hz=bitpoly([((1-L)*i,0) for i in range(L)],l,m)
    u=translate(hz,L,0,l,m)^translate(hz,2*L,0,l,m)
    v=hz^translate(hz,L,0,l,m)
    w=u|(v<<N)
    assert w.bit_count()==4*L
    assert multiply(u,A,l,m)^multiply(v,B,l,m)==0
    assert not member(w,bz)
    # Valid y-period double cover, with a changed constant term in A.
    mt=2*m;Nt=l*mt
    At=[(0,m),(L+1,0),(2*L,1)];Bt=B
    for poly,base in [(At,A),(Bt,B)]:
        assert len(set(poly))==3
        assert len({(a%l,b%m) for a,b in poly})==3
        assert {(a%l,b%m) for a,b in poly}==set(base)
    ftilde=f0_polynomial(L,l,mt)
    uc=multiply(ftilde,Bt,l,mt);vc=multiply(ftilde,At,l,mt)
    lifted_boundary=uc|(vc<<Nt)
    assert lifted_boundary.bit_count()==6+2*mu
    mask=(1<<N)-1
    project=lambda v:(v&mask)^(v>>N)
    assert project(uc)==project(vc)==J
    hxt,bct=matrices(At,Bt,l,mt)
    bxt=rank_basis(hxt);bzt=rank_basis(bct)
    assert len(bxt)==len(bzt)==Nt-2
    assert member(lifted_boundary,bzt)
    result={'j':j,'L':L,'base_n':2*N,'base_k':4,
            'proved_base_distance_lower':L,'explicit_logical_weight':4*L,
            'boundary_weight':6,'exact_minimum_coefficient_weight':mu,
            'all_four_filling_weights':weights,
            'cover_n':2*Nt,'cover_k':4,
            'proved_lifted_filling_lower':2+2*3**r,
            'explicit_lifted_boundary_weight':6+2*mu,
            'base_check_ranks':[len(bx),len(bz)],
            'cover_check_ranks':[len(bxt),len(bzt)]}
    print(json.dumps(result),flush=True)
    return result

if __name__=='__main__':
    js=list(map(int,sys.argv[1:])) or [1,2]
    out=[verify(j) for j in js]
    (ROOT/'family_verification.json').write_text(json.dumps(out,indent=2)+'\n')
