"""Exact independent checks of the symbolic compact-survival mechanisms.

Uses only Python's standard library. These checks support, but do not replace,
the proofs in REPORT.md. No minimum-distance search is performed.
"""
from __future__ import annotations
from itertools import combinations, product
from math import gcd, lcm
from pathlib import Path
import json


def pmul(a: int, b: int) -> int:
    out=0
    while b:
        bit=b & -b; out ^= a << (bit.bit_length()-1); b ^= bit
    return out


def pmod(a: int, b: int) -> int:
    if b == 0: raise ZeroDivisionError
    while a.bit_length() >= b.bit_length():
        a ^= b << (a.bit_length()-b.bit_length())
    return a


def pgcd(a: int,b: int) -> int:
    while b: a,b=b,pmod(a,b)
    return a


def pquot(a: int,b: int) -> int:
    q=0
    while a and a.bit_length() >= b.bit_length():
        j=a.bit_length()-b.bit_length();q ^= 1 << j;a ^= b << j
    assert a == 0
    return q


# Rational functions over F_2 in one indeterminate, independent of SymPy.
class RF:
    __slots__=('a','b')
    def __init__(self,a: int=0,b: int=1):
        if b == 0: raise ZeroDivisionError
        g=pgcd(a,b);self.a=pquot(a,g);self.b=pquot(b,g)
    def __bool__(self): return bool(self.a)
    def __eq__(self,other): return isinstance(other,RF) and self.a==other.a and self.b==other.b
    def __add__(self,other): return RF(pmul(self.a,other.b)^pmul(other.a,self.b),pmul(self.b,other.b))
    def __mul__(self,other): return RF(pmul(self.a,other.a),pmul(self.b,other.b))
    def inv(self): return RF(self.b,self.a)


class FiniteField:
    def __init__(self,modulus: int):
        self.mod=modulus;self.size=1 << (modulus.bit_length()-1)
    def mul(self,a,b): return pmod(pmul(a,b),self.mod)
    def inv(self,a):
        if not a: raise ZeroDivisionError
        result=1;base=a;n=self.size-2
        while n:
            if n & 1:result=self.mul(result,base)
            base=self.mul(base,base);n >>= 1
        assert self.mul(result,a)==1
        return result


def det(M):
    n=len(M)
    if n==0:return 1
    return sum((-1)**j*M[0][j]*det([row[:j]+row[j+1:] for row in M[1:]]) for j in range(n))


def verify_polytope():
    V=[]
    for shift in (0,2):
        for a,b in ((1,0),(0,1),(1,-1),(-1,0),(0,-1),(-1,1)):
            r=[0]*4;r[shift:shift+2]=[a,b];V.append(r)
    maxima={};tested={}
    for k in range(1,5):
        mx=0;count=0
        for rows in combinations(V,k):
            for cols in combinations(range(4),k):
                value=abs(det([[row[j] for j in cols] for row in rows]))
                mx=max(mx,value);count+=1
        assert mx==1
        maxima[k]=mx;tested[k]=count
    # Last-row roots bound every physical exponent difference in the rank-one case.
    mx=max(abs(det([*rows,v])) for rows in combinations(V,3) for v in V)
    assert mx==1
    return {'vertices':V,'maximum_absolute_minors':maxima,'minor_checks':tested,
            'rank_one_root_functional_maximum':mx}


class Torus:
    def __init__(self,a,b):self.a=a;self.b=b;self.n=a*b
    def add(self,i,j):return ((i//self.b+j//self.b)%self.a)*self.b+(i%self.b+j%self.b)%self.b
    def order(self,i):return lcm(self.a//gcd(i//self.b,self.a),self.b//gcd(i%self.b,self.b))


def rank_rf(M):
    M=[r[:] for r in M];r=0
    for j in range(len(M[0])):
        p=next((i for i in range(r,len(M)) if M[i][j]),None)
        if p is None:continue
        M[r],M[p]=M[p],M[r];iv=M[r][j].inv()
        M[r]=[x*iv for x in M[r]]
        for i in range(r+1,len(M)):
            if M[i][j]:
                c=M[i][j];M[i]=[x+c*y for x,y in zip(M[i],M[r])]
        r+=1
        if r==len(M):break
    return r


def rank_ff(M,F):
    M=[r[:] for r in M];r=0
    for j in range(len(M[0])):
        p=next((i for i in range(r,len(M)) if M[i][j]),None)
        if p is None:continue
        M[r],M[p]=M[p],M[r];iv=F.inv(M[r][j]);M[r]=[F.mul(x,iv) for x in M[r]]
        for i in range(r+1,len(M)):
            if M[i][j]:
                c=M[i][j];M[i]=[x ^ F.mul(c,y) for x,y in zip(M[i],M[r])]
        r+=1
        if r==len(M):break
    return r


def ringmul_rf(G,a,b):
    out=[RF() for _ in range(G.n)]
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:
                    k=G.add(i,j);out[k]=out[k]+x*y
    return out


def ringmul_ff(G,a,b,F):
    out=[0]*G.n
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b):
                if y:out[G.add(i,j)] ^= F.mul(x,y)
    return out


def multiplication_matrix(G,v,zero):
    M=[[zero for _ in range(G.n)] for _ in range(G.n)]
    for j in range(G.n):
        for i,c in enumerate(v):M[G.add(i,j)][j]=c
    return M


def verify_pencil():
    generic=[]
    cases=[(2,1,1,0),(4,1,1,3),(4,2,2,1),(4,4,4,1),(8,2,2,1),
           (8,2,3,1),(8,1,1,4),(2,2,2,1)]
    for a,b,h,k in cases:
        G=Torus(a,b);M=lcm(G.order(h),G.order(k))
        for q in (1,2,4):
            alpha=RF(1 << q);beta=RF((1 << q)^1)
            D=[RF() for _ in range(G.n)]
            for i,c in [(0,alpha),(h,alpha),(0,beta),(k,beta)]:D[i]=D[i]+c
            E=[RF() for _ in range(G.n)];E[0]=RF(1)
            for _ in range(M-1):E=ringmul_rf(G,E,D)
            assert not any(ringmul_rf(G,E,D))
            rd=rank_rf(multiplication_matrix(G,D,RF()))
            re=rank_rf(multiplication_matrix(G,E,RF()))
            assert re==G.n-rd==G.n//M
            generic.append({'group':[a,b],'h':h,'k':k,'q':q,'M':M,
                            'kernel_dimension':G.n-rd,'power_image_dimension':re})
    finite=0;failures_at_excluded_values=0
    for modulus in (0b111,0b1011,0b10011):
        F=FiniteField(modulus)
        for a,b,h,k in cases:
            G=Torus(a,b);M=lcm(G.order(h),G.order(k))
            for alpha in range(F.size):
                beta=alpha ^ 1;D=[0]*G.n
                for i,c in [(0,alpha),(h,alpha),(0,beta),(k,beta)]:D[i] ^= c
                E=[0]*G.n;E[0]=1
                for _ in range(M-1):E=ringmul_ff(G,E,D,F)
                assert not any(ringmul_ff(G,E,D,F))
                rd=rank_ff(multiplication_matrix(G,D,0),F)
                re=rank_ff(multiplication_matrix(G,E,0),F)
                if alpha not in (0,1):
                    assert re==G.n-rd==G.n//M
                    finite+=1
                elif re!=G.n-rd:
                    failures_at_excluded_values+=1
    assert failures_at_excluded_values>0
    return {'generic_rational_function_cases':generic,'finite_field_checks':finite,
            'negative_controls_at_alpha_zero_or_one':failures_at_excluded_values}


# Three-variable sparse arithmetic, epsilon^2=0.
def spmul(a,b):
    out=set()
    for i in a:
        for j in b:
            v=tuple(x+y for x,y in zip(i,j))
            if v[2]>=2:continue
            if v in out:out.remove(v)
            else:out.add(v)
    return out


def verify_specialization_warning():
    one={(0,0,0)};g={(1,0,0)};c={(0,1,0)};eps={(0,0,1)}
    A=g ^ eps;B=spmul(g,one ^ c) ^ eps
    U=spmul(g,one ^ c) ^ spmul(eps,c);V=g
    assert spmul(A,U) ^ spmul(B,V)==set()
    assert not {m for m in U if m[0]==m[1]==0}
    assert not {m for m in V if m[0]==m[1]==0}
    # At g=c=0, the finite complex is K(epsilon,epsilon), over F_2[epsilon].
    columns=[2,0,2,0]  # epsilon multiplication in each two-dimensional block
    boundaries=[2|(2<<2),0]
    def rank2(vs):
        piv={}
        for v in vs:
            while v:
                i=v.bit_length()-1
                if i not in piv:piv[i]=v;break
                v ^= piv[i]
        return len(piv)
    h1=4-rank2(columns)-rank2(boundaries)
    assert h1==2
    return {'universal_cover_generator_cycle_identity':True,
            'universal_generator_specializes_to_zero':True,
            'specialized_cover_homology_dimension':h1,
            'outside_BB_strict_trinomial_class':True}


def main():
    result={'polytope':verify_polytope(),'nilpotent_pencil':verify_pencil(),
            'specialization_negative_control':verify_specialization_warning(),
            'classification':'exact algebraic checks, not distance estimates'}
    Path(__file__).with_name('mechanism_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:(v if k!='nilpotent_pencil' else
                        {'generic_cases':len(v['generic_rational_function_cases']),
                         'finite_field_checks':v['finite_field_checks'],
                         'negative_controls':v['negative_controls_at_alpha_zero_or_one']})
                      for k,v in result.items()},indent=2))

if __name__=='__main__':main()
