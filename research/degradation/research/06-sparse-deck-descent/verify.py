#!/usr/bin/env python3
"""Exact verification of sparse Cartier/derivative descent.

No decoders, floating point arithmetic, or minimum-distance heuristics are used.
The universal calculations use sets of Laurent monomials.  Finite homology
membership uses an independent bit-packed binary matrix implementation.
"""
from __future__ import annotations
import itertools, json, random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# A monomial is (odd-torsion coordinate, free exponent, involution coordinate).
ONE = frozenset({(0,0,0)})
ZERO = frozenset()
Z = frozenset({(0,1,0)})
S = frozenset({(0,0,1)})

def add(*xs):
    r=set()
    for x in xs: r.symmetric_difference_update(x)
    return frozenset(r)

def mul(a,b,T=1):
    r=set()
    for i,j,k in a:
        for ii,jj,kk in b:
            m=((i+ii)%T,j+jj,k^kk)
            if m in r:r.remove(m)
            else:r.add(m)
    return frozenset(r)

def power(a,n,T=1):
    r=ONE
    while n:
        if n&1:r=mul(r,a,T)
        a=mul(a,a,T);n//=2
    return r

def mon(j,i=0,k=0,T=1):return frozenset({(i%T,j,k)})
def split(a):
    return tuple(frozenset((i,j,0) for i,j,k in a if k==s) for s in (0,1))
def join(a,b):return add(a,mul(S,b))
def euler(a):return frozenset(m for m in a if m[1]%2)
def cartier(a,j,T=1):
    inv2=pow(2,-1,T) if T>1 else 0
    assert all(k==0 for _,_,k in a)
    return frozenset(((i*inv2)%T,(n-j)//2,0) for i,n,k in a if n%2==j)

def boundary(A,B,h,T=1):return mul(B,h,T),mul(A,h,T)
def syndrome(A,B,Y,T=1):return add(mul(A,Y[0],T),mul(B,Y[1],T))
def phi(a,c,Y,T=1):
    u0,u1=split(Y[0]);v0,v1=split(Y[1])
    return add(u1,mul(c,v1,T)),add(v0,mul(a,v1,T))
def psi(a,c,X,T=1):
    A=add(S,a)
    return add(mul(A,X[0],T),mul(c,X[1],T)),X[1]
def base_inverse(c,X,T=1):return add(X[0],mul(c,X[1],T)),X[1]
def wt(Y):return len(Y[0])+len(Y[1])
def normalize_sheets(Y):
    a=sum(len(split(f)[1]) for f in Y)
    b=sum(len(split(f)[0]) for f in Y)
    return tuple(mul(S,f) for f in Y) if a>b else Y

def constructors(a,b,c,Y,T=1):
    Y=normalize_sheets(Y)
    A0=add(ONE,a);C=add(b,mul(a,c,T))
    U,V=phi(a,c,Y,T)
    assert not syndrome(power(A0,2,T),C,(U,V),T)
    Q=mul(U,V,T)
    Cs=[cartier(C,j,T) for j in (0,1)]
    Ts=[cartier(Q,j,T) for j in (0,1)]
    out=[]
    for j in (0,1):
        X=(mul(Cs[j],U,T),Ts[j])
        assert not syndrome(A0,C,X,T), ('Cartier syndrome',T,a,b,c,Y,j)
        assert mul(A0,Ts[j],T)==mul(Cs[j],V,T)
        out.append(base_inverse(c,X,T))
    X=(add(mul(A0,euler(U),T),mul(Z,mul(Cs[1],Ts[1],T),T)),euler(V))
    assert not syndrome(A0,C,X,T), ('Derivative syndrome',T,a,b,c,Y)
    out.append(base_inverse(c,X,T))
    u,v=len(U),len(V);w=wt(Y)
    assert u<=w/2 and v<=1.5*w
    assert all(len(t)<=u*v for t in Ts)
    # Each sparse construction is checked against its actual termwise bound.
    for j in (0,1):
        assert wt(out[j])<=len(Cs[j])*u+(1+len(c))*u*v
    assert wt(out[2])<=3*u+len(Cs[1])*u*v+(1+len(c))*v
    return Y,out,Cs

# Independent finite group and GF(2) matrix implementation.
class Finite:
    def __init__(self,T,P,eps=0,seam=0,cover=False):
        self.T,self.P,self.eps,self.seam,self.cover=T,P,eps,seam,cover
        self.N=T*P*(2 if cover else 1)
    def idx(self,i,j,k=0):
        q,r=divmod(j,self.P)
        i=(i+self.seam*q)%self.T
        if self.cover:k=(k+self.eps*q)%2
        else:k=0
        return (k*self.P+r)*self.T+i
    def decode(self,x):
        i=x%self.T;jk=x//self.T
        return i,jk%self.P,jk//self.P
    def elem(self,a):
        v=0
        for i,j,k in a:v^=1<<self.idx(i,j,k)
        return v
    def translate(self,v,j):
        di,dj,dk=self.decode(j);r=0
        while v:
            bit=v&-v;v^=bit;i,k,s=self.decode(bit.bit_length()-1)
            r^=1<<self.idx(i+di,k+dj,s^dk)
        return r
    def product(self,a,b):
        r=0
        while b:
            bit=b&-b;b^=bit;r^=self.translate(a,bit.bit_length()-1)
        return r
    def vec(self,Y):return self.elem(Y[0])|(self.elem(Y[1])<<self.N)
    def syn(self,A,B,y):
        mask=(1<<self.N)-1
        return self.product(A,y&mask)^self.product(B,y>>self.N)
    def bcols(self,A,B):
        return [self.translate(B,j)|(self.translate(A,j)<<self.N) for j in range(self.N)]

def echelon(cols):
    piv={}
    for v in cols:
        while v:
            p=v.bit_length()-1
            if p in piv:v^=piv[p]
            else:piv[p]=v;break
    return piv

def inside(v,piv):
    while v:
        p=v.bit_length()-1
        if p not in piv:return False
        v^=piv[p]
    return True

def polyint(a):
    assert all(i==0 and k==0 and j>=0 for i,j,k in a)
    return sum(1<<j for _,j,_ in a)
def intpoly(a):return frozenset((0,j,0) for j in range(a.bit_length()) if (a>>j)&1)
def pmul(a,b):
    r=0
    while b:
        if b&1:r^=a
        a<<=1;b>>=1
    return r

def pdiv(a,b):
    assert b
    q=0
    while a and a.bit_length()>=b.bit_length():
        j=a.bit_length()-b.bit_length();q^=1<<j;a^=b<<j
    return q,a

def pgcd(a,b):
    while b:a,b=b,pdiv(a,b)[1]
    return a

def check_homotopies(rng):
    count=0
    for T in (1,3,5,7):
        for _ in range(24):
            def randpoly(n,sbits=False):
                return frozenset((rng.randrange(T),rng.randrange(-5,6),rng.randrange(2) if sbits else 0) for _ in range(n))
            a=randpoly(2);c=ONE if rng.randrange(2) else ZERO;b=randpoly(2 if c else 3)
            A=add(S,a);B=add(b,mul(S,c,T));A0=add(ONE,a);C=add(b,mul(a,c,T))
            Y=(randpoly(6,True),randpoly(5,True))
            X=phi(a,c,Y,T);u0,u1=split(Y[0]);v0,v1=split(Y[1])
            err=syndrome(A,B,Y,T);e0,e1=split(err)
            lhs=tuple(add(f,g) for f,g in zip(Y,psi(a,c,X,T)))
            bnd=boundary(A,B,v1,T)
            rhs=(add(bnd[0],e1),bnd[1])
            assert lhs==rhs
            assert syndrome(power(A0,2,T),C,X,T)==add(e0,mul(a,e1,T))
            # Chain-map identities in degrees 0,1,2.
            h=randpoly(4,True);h0,h1=split(h)
            assert phi(a,c,boundary(A,B,h,T),T)==boundary(power(A0,2,T),C,h1,T)
            xx=(randpoly(4),randpoly(3))
            assert phi(a,c,psi(a,c,xx,T),T)==xx
            hh=randpoly(4)
            assert psi(a,c,boundary(power(A0,2,T),C,hh,T),T)==boundary(A,B,mul(A,hh,T),T)
            # Projection and transfer diagrams before any finite specialization.
            py=tuple(add(*split(f)) for f in psi(a,c,xx,T))
            assert base_inverse(c,py,T)==(mul(A0,xx[0],T),xx[1])
            tr=tuple(mul(add(ONE,S),f,T) for f in base_inverse(c,xx,T))
            assert phi(a,c,tr,T)==(xx[0],mul(A0,xx[1],T))
            count+=1
    return count

def finite_case(T,P,eps,seam,a,b,c,Y,primitive=True):
    A=add(S,a);B=add(b,mul(S,c,T));A0=add(ONE,a);B0=add(b,c)
    assert len(A)==3 and len(B)==3 and len(A0)==3 and len(B0)==3
    assert not syndrome(A,B,Y,T)
    Y0,outputs,Cs=constructors(a,b,c,Y,T)
    up=Finite(T,P,eps,seam,True);dn=Finite(T,P,0,seam,False)
    au,bu=up.elem(A),up.elem(B);ad,bd=dn.elem(A0),dn.elem(B0)
    if any(v.bit_count()!=3 for v in (au,bu,ad,bd)):return None
    bu_basis=echelon(up.bcols(au,bu));bd_basis=echelon(dn.bcols(ad,bd))
    yu=up.vec(Y0);yd=dn.vec(Y0)
    assert not up.syn(au,bu,yu) and not dn.syn(ad,bd,yd)
    survive=not inside(yu,bu_basis);killed=inside(yd,bd_basis)
    for Zc in outputs:
        assert not dn.syn(ad,bd,dn.vec(Zc))
    # Independently verify the Cartier transfer diagrams modulo boundaries.
    for j in (0,1):
        tr=tuple(mul(add(ONE,S),f,T) for f in outputs[j])
        cy=tuple(mul(Cs[j],f,T) for f in Y0)
        assert inside(up.vec(tuple(add(f,g) for f,g in zip(tr,cy))),bu_basis)
    if survive and killed:
        if primitive:
            assert not inside(dn.vec(outputs[2]),bd_basis), ('derivative nontriviality',T,P,eps,seam,a,b,Y)
        else:
            singleton=[j for j in (0,1) if len(Cs[j])==1]
            assert singleton
            assert any(not inside(dn.vec(outputs[j]),bd_basis) for j in singleton)
        good=[Zc for Zc in outputs if not inside(dn.vec(Zc),bd_basis)]
        w=wt(Y0)
        assert min(wt(Zc) for Zc in good)<=3*w*w
        # Main cases have no collisions in the witness when specialized.
        return {'T':T,'P':P,'eps':eps,'seam':seam,'formal_weight':w,
                'physical_cover_weight':yu.bit_count(),
                'replacement_weight':min(dn.vec(z).bit_count() for z in good),
                'base_k':2*(dn.N-len(bd_basis)),
                'cover_k':2*(up.N-len(bu_basis)),
                'C_parities':[len(q) for q in Cs],
                'kind':'derivative' if primitive else 'singleton_Cartier'}
    return {'rejected_by_homology':True,'survive':survive,'projection_boundary':killed}

def run_cases(rng):
    successes=[];attempts=0;others=0
    # Independent integer-polynomial construction of universal compact generators.
    specs=[]
    for aa,bb,cc,dd in [(1,2,7,8),(1,2,4,8),(1,5,7,11),(1,2,7,14),
                        (1,5,4,8),(5,4,11,10),(7,2,1,8),(1,8,7,2),
                        (5,8,11,14),(7,8,1,2)]:
        specs.append((mon(aa)|mon(bb),mon(cc)|mon(dd),ONE,True))
    # The twisted check is not primitive; the untwisted check is primitive.
    specs.append((mon(2)|mon(4),ONE|mon(1)|mon(2),ZERO,False))
    # Only the first check is twisted, and is primitive.
    specs.append((mon(1)|mon(2),ONE|mon(2)|mon(4),ZERO,True))
    for a,b,c,prim in specs:
        aa=polyint(add(ONE,a));C=polyint(add(b,mul(a,c)));gg=pgcd(pmul(aa,aa),C)
        if gg==1:continue
        U0=intpoly(pdiv(C,gg)[0]);V0=intpoly(pdiv(pmul(aa,aa),gg)[0])
        for P,eps in [(42,0),(66,0),(39,0),(45,0),(39,1),(42,1)]:
            for kk in [1,7,5,9]:
                k=intpoly(kk)
                Y=psi(a,c,(mul(U0,k),mul(V0,k)))
                # Add an explicit arbitrary universal boundary; the detector must
                # not rely on using a distinguished homology representative.
                r=mon(rng.randrange(0,4))|mon(rng.randrange(5,9),k=rng.randrange(2))
                by=boundary(add(S,a),add(b,mul(S,c)),r)
                Y=tuple(add(f,g) for f,g in zip(Y,by))
                attempts+=1;row=finite_case(1,P,eps,0,a,b,c,Y,prim)
                if row and 'rejected_by_homology' not in row:successes.append(row)
                else:others+=1
    # Odd-torsion tests with a norm-supported ramified sector, and genuinely
    # torsion-dependent Frobenius families. All computations stay binary.
    for T in (3,5,7):
        norm=frozenset((i,0,0) for i in range(T))
        for P,eps,seam in [(42,0,0),(45,0,1),(42,1,1),(39,1,0)]:
            a=mon(1,i=1,T=T)|mon(2)
            b=mon(7,i=1,T=T)|mon(8);c=ONE
            C0=(1<<1)|(1<<2)|(1<<7)|(1<<8)
            U=intpoly(pdiv(C0,7)[0]);V=intpoly(7)
            Y=psi(mon(1)|mon(2),ONE,(U,V))
            Y=tuple(mul(norm,f,T) for f in Y)
            attempts+=1;row=finite_case(T,P,eps,seam,a,b,c,Y,True)
            if row and 'rejected_by_homology' not in row:successes.append(row)
            else:others+=1
            A0=add(ONE,a);B0=power(A0,4,T);b=add(ONE,B0)
            U=add(ONE,power(A0,3,T));V=A0
            Y=psi(a,ONE,(U,V),T)
            attempts+=1;row=finite_case(T,P,eps,seam,a,b,ONE,Y,True)
            if row and 'rejected_by_homology' not in row:successes.append(row)
            else:others+=1
        # Nonprimitive twisted check / primitive untwisted check, with odd torsion.
        B0=add(ONE,mon(1,i=1,T=T),mon(2));a=add(ONE,power(B0,2,T))
        b=B0;c=ZERO
        Y=psi(a,c,(ONE,power(B0,3,T)),T)
        attempts+=1;row=finite_case(T,42,0,1,a,b,c,Y,False)
        if row and 'rejected_by_homology' not in row:successes.append(row)
        else:others+=1
    # An adversarial zero-divisor corner: A=1+t+t^2 vanishes identically
    # in the nontrivial C3 character component. Cancellation of A is not
    # allowed there; the singleton-Cartier proof instead uses V=0.
    T=3
    a=mon(0,i=1,T=T)|mon(0,i=2,T=T)
    b=ONE|mon(1)|mon(2,i=1,T=T)
    U=ONE|mon(0,i=1,T=T)
    Y=psi(a,ZERO,(U,ZERO),T)
    for P,eps in ((15,0),(15,1),(30,0),(30,1)):
        attempts+=1;row=finite_case(T,P,eps,0,a,b,ZERO,Y,False)
        if row and 'rejected_by_homology' not in row:
            row['zero_divisor_A_corner']=True;successes.append(row)
        else:others+=1
    # Reverse the Laurent coordinate. Negative odd exponents test the exact
    # coefficient selectors without relying on ordinary polynomial degrees.
    def reverse(f):return frozenset((i,-j,k) for i,j,k in f)
    a=mon(1)|mon(2);b=mon(7)|mon(8)
    Y=psi(a,ONE,(intpoly(pdiv((1<<1)|(1<<2)|(1<<7)|(1<<8),7)[0]),intpoly(7)))
    for P,eps in ((39,0),(42,0),(39,1),(42,1)):
        attempts+=1;row=finite_case(1,P,eps,0,reverse(a),reverse(b),ONE,tuple(reverse(f) for f in Y),True)
        if row and 'rejected_by_homology' not in row:
            row['negative_Laurent_exponents']=True;successes.append(row)
        else:others+=1
    return attempts,others,successes

def verify_retained_involution_family():
    a=mon(1)|mon(2);b=mon(7)|mon(8);c=ONE;A=add(S,a);B=add(S,b)
    p=intpoly(7);D=intpoly(30) # x+x^2+x^3+x^4
    X=psi(a,c,(D,ONE));Y=tuple(mul(p,v) for v in X)
    assert wt(X)==8 and wt(Y)==14
    assert not syndrome(A,B,X) and not syndrome(A,B,Y)
    _,out,_=constructors(a,b,c,Y)
    zd=out[2]
    bad=syndrome(A,B,zd)
    assert bad==mul(add(ONE,S),intpoly(180))
    rows=[]
    for P in (9,15,21,33,45,63):
        base=Finite(1,P,0,0,True);cover=Finite(1,2*P,0,0,True)
        ab,bb=base.elem(A),base.elem(B);ac,bc=cover.elem(A),cover.elem(B)
        eb=echelon(base.bcols(ab,bb));ec=echelon(cover.bcols(ac,bc))
        assert not inside(base.vec(X),eb) and not inside(cover.vec(X),ec)
        assert inside(base.vec(Y),eb) and not inside(cover.vec(Y),ec)
        # Explicit uniform boundary coefficient in the smaller period.
        F=(1<<P)|1;num=7^pmul(2,F);u,rem=pdiv(num,pmul(7,7));assert not rem
        h=mul(intpoly(u),A)
        assert base.vec(boundary(A,B,h))==base.vec(Y)
        assert base.syn(ab,bb,base.vec(zd))!=0
        assert 2*(base.N-len(eb))==4 and 2*(cover.N-len(ec))==8
        rows.append({'P':P,'base_n':2*base.N,'base_k':4,'cover_n':2*cover.N,'cover_k':8,
                     'base_logical_weight':base.vec(X).bit_count(),
                     'cover_kernel_logical_weight':cover.vec(Y).bit_count(),
                     'wrong_target_derivative_syndrome_weight':base.syn(ab,bb,base.vec(zd)).bit_count()})
    return rows

def main():
    rng=random.Random(20260906)
    h=check_homotopies(rng)
    attempts,others,rows=run_cases(rng)
    fam=verify_retained_involution_family()
    summary={'status':'TRINOMIAL_STILL_OPEN',
             'new_theorem':'For a compact weight-w kernel logical on a support-generated one-involution strip, with that involution equal to the deck kernel, d <= 3*w^2.',
             'global_quadratic_proved':False,'global_quadratic_refuted':False,
             'universal_chain_homotopy_tests':h,'finite_test_attempts':attempts,
             'nonboundary_cover_projection_boundary_cases':len(rows),
             'other_or_inadmissible_cases':others,
             'derivative_cases':sum(r['kind']=='derivative' for r in rows),
             'singleton_Cartier_cases':sum(r['kind']=='singleton_Cartier' for r in rows),
             'odd_torsion_cases':sum(r['T']>1 for r in rows),
             'nonproduct_period_cases':sum(r['eps']==1 for r in rows),
             'largest_cover_n_tested_in_successful_cases':max(4*r['T']*r['P'] for r in rows),
             'zero_divisor_A_corner_cases':sum(r.get('zero_divisor_A_corner',False) for r in rows),
             'negative_Laurent_exponent_cases':sum(r.get('negative_Laurent_exponents',False) for r in rows),
             'collision_free_successful_witnesses':sum(r['physical_cover_weight']==r['formal_weight'] for r in rows),
             'minimum_distance_claims':False,
             'counterfamily_attempt':'Retained-involution period doubles have a weight-14 compact kernel class, but also a weight-8 base logical for every odd multiple P of 3 with P>8.',
             'retained_involution_family':fam}
    (ROOT/'cases.json').write_text(json.dumps(rows,indent=2)+'\n')
    (ROOT/'verification_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
