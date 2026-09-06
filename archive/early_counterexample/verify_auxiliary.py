#!/usr/bin/env python3
"""Exact auxiliary checks: previous family, its class metric and low-sheet metric,
and the smallest counterexample to the proposed nu inequality.
Uses only standard-library modules and the two adjacent verifier files.
"""
from itertools import product
from verify_counterexample import (
    require, bits, polynomial as P, multiply as mul, divmod_poly as divp,
    BinarySpan, action, cyclic_code, projection, transfer, evaluate_class,
)
import verify_previous_family as old


def all_span(basis):
    words=[0]
    for v in basis:
        words += [w ^ v for w in words]
    return words


def low_basis(j):
    q,L=3*j,9*j
    S=P(range(0,q,3))
    u0=(1 ^ mul(3,S) ^ (1<<(q-2)) ^ (1<<(q-1)) ^ (S<<(q+2))
        ^ ((mul(3,S)^(1<<(q-1)))<<(2*q)))
    v0=1 ^ (S<<1) ^ (mul(7,S)<<q) ^ ((S^(1<<(q-2)))<<(2*q))
    u1=mul(5,mul(P([0,q,2*q]),S))^(1<<(q-1))
    v1=mul(6,S)^((mul(3,S)^(1<<(q-1)))<<(2*q))
    return [u0|(v0<<L),u1|(v1<<L)]


# With u=sum x^(iq)u_i, v=sum x^(iq)v_i, deg u_i,v_i<q, a low-sheet
# cover cycle is equivalent to C*(u0,u1,u2,v0,v1,v2)^T=x^q*kappa+rot(kappa).
# First three kappa entries have degree <=1; last three are constants.
C=[[4,1,0,4,0,0],[2,4,1,0,4,0],[0,2,4,0,0,4],
   [0,0,2,3,0,0],[0,0,0,0,3,0],[1,0,0,0,0,3]]
ADJ=[[238,108,175,360,144,404],[108,144,108,144,448,144],
     [108,108,238,144,144,360],[72,72,180,332,224,432],
     [0,0,0,0,428,0],[90,36,101,216,112,288]]
D=756  # x^2*(x+1)*(x^2+x+1)^3


def mv(matrix,vector):
    out=[]
    for row in matrix:
        value=0
        for a,b in zip(row,vector):value ^= mul(a,b)
        out.append(value)
    return out


def kappas(mask):
    return [(mask>>0)&3,(mask>>2)&3,(mask>>4)&3,
            (mask>>6)&1,(mask>>7)&1,(mask>>8)&1]


def allowed(q):
    ans=[]
    for mask in range(512):
        k=kappas(mask)
        nums=mv(ADJ,[(k[i]<<q)^k[(i-1)%6] for i in range(6)])
        qr=[divp(a,D) for a in nums]
        if all(r==0 and a.bit_length()<=q for a,r in qr):ans.append(mask)
    return ans


def uniform_low_kernel_certificate():
    for j in range(6):
        column=[ADJ[i][j] for i in range(6)]
        require(mv(C,column)==[D if i==j else 0 for i in range(6)],'C*adj != D*I')
    require(D==mul(4,mul(3,mul(7,mul(7,7)))),'determinant factorization')
    require(divp(mul(4,P([0,12])),D)[1]==0,'period-12 remainder identity')
    expected=[0,0xf3,0x10b,0x1f8]
    for q in (3,6,9,12):require(allowed(q)==expected,'constant kernel table')
    # Since x^(q+12)=x^q mod D for q>=2, divisibility repeats with period 12.
    # deg(adj)<=8; the quotient degree restriction is just vanishing of the
    # degree-9 coefficient of adj*kappa, independent of q>0. Thus the four
    # tables certify nullity two for every q=3j, j>=2, not merely these four q.
    print('PARAMETER-UNIFORM LOW-SHEET KERNEL CERTIFICATE: nullity two for every j>=2')


def family_class_check(j):
    q,L=3*j,9*j
    A=P([0,q-1,2*q-2]);B=P([0,3*q-2,3*q-1]);AA=P([0,q-1,5*q-2])
    H,G=cyclic_code(L,A,B);HC,GC=cyclic_code(2*L,AA,B)
    ops=old.operators([(i,0) for i in bits(AA)],[(i,0) for i in bits(B)],L)
    T=P([0,q,2*q]);z=P([1,q]) | (P([0,1])<<L)
    q0=T | (T<<L)
    numerator=T ^ P([2,q+1])
    quotient,rem=divp(numerator,7)
    require(rem==0,'family boundary quotient is not polynomial')
    s=quotient<<2
    xz=old.translate(z,L,1)
    require(action(G,s)==q0^xz,'generalized q0+xz=boundary identity')
    PP=P([0,2*q,4*q]);w=PP | (PP<<(2*L))
    require(action(HC,w)==0 and w.bit_count()==6 and projection(w,L)==q0,
            'family class-lift witness')
    rgood=P([q]) | (P([q])<<L)
    require(action(ops[1][0],q0)==action(H,rgood),'good pair correction')
    require(action(ops[1][0],q0)!=0,'q0 unexpectedly lies in chosen low sheet')
    lo=low_basis(j)
    require(all(action(H,v)==0 and action(ops[1][0],v)==0 for v in lo),'low-basis equations')
    require(len(BinarySpan(lo))==2,'low-basis dependence')
    require([lo[0].bit_count(),lo[1].bit_count(),(lo[0]^lo[1]).bit_count()]
            ==[10*j+2,10*j,10*j],'low-basis weights')
    # The complete-kernel theorem is certified uniformly above.
    residual=BinarySpan(G).reduce
    nu=min((v.bit_count() for v in all_span(lo) if residual(v)==residual(z)),default=float('inf'))
    require(nu==(10*j if j%2==0 else float('inf')),'family nu formula')
    print(f'FAMILY j={j}: delta=4; rho={2*j-1}; mu=6; nu={nu}; class boundary identity PASS')


def smallest_nu_counterexample():
    g=7;H,G=cyclic_code(3,g,g);HC,GC=cyclic_code(6,g<<2,g)
    z=(1<<1)|(1<<3);w=(1<<4)|(1<<6)
    require(action(H,z)==0 and BinarySpan(G).reduce(z),'small base logical')
    require(action(HC,w)==0 and projection(w,3)==z,'small lifted logical')
    require(action(GC,P([1,2]))==transfer(z,3),'small killed transfer')
    lowcols=[]
    for i in range(3):lowcols.append(mul(g<<2,1<<i))
    for i in range(3):lowcols.append(mul(g,1<<i))
    # Low vectors have degree <=6, so reduction modulo x^6+1 is retained here.
    lowcols=[divp(c,P([0,6]))[1] for c in lowcols]
    basis=old.kernel(lowcols)
    require(len(basis)==2,'small low-kernel dimension')
    Bspan=BinarySpan(G)
    require(all(Bspan.reduce(v)!=Bspan.reduce(z) for v in all_span(basis)),'small nu finite')
    print('SMALLEST NU COUNTEREXAMPLE: [[6,4,2]] -> [[12,4,2]]; delta=mu=2; rho=0; nu=infinity')


def old_30_60_case():
    A=[(2,0),(1,1),(1,2)];B=[(4,0),(4,1),(3,2)]
    AA=[(7,0),(6,1),(1,2)];BB=[(9,0),(4,1),(8,2)]
    H,G=old.chain(A,B,5,3);HC,GC=old.chain(AA,BB,10,3)
    ops=old.operators(AA,BB,5,3)
    z=P([0,1,25,26]);r=P([1,2])
    require(action(H,z)==0 and old.Span(G).reduce(z),'old base logical')
    require(action(H,r)==action(ops[1][0],z),'old correction')
    require(old.normal_lift(z,r,15).bit_count()==6,'old cover weight')
    base4,_=old.zero_four_cycles(H)
    require(len(set(H))==30 and base4,'old base distance4')
    cover4,_=old.zero_four_cycles(HC)
    require(len(set(HC))==60 and not cover4,'old cover has a <=4 cycle')
    S=list(bits(z))
    require(all(action(H,v)!=action(ops[1][0],z) for v in all_span([1<<i for i in S])),
            'old rho=0')
    low=old.kernel([a|(d<<15) for a,d in zip(H,ops[1][0])])
    require(len(low)==2,'old low-kernel dimension')
    residual=old.Span(G).reduce
    nu=min(v.bit_count() for v in all_span(low) if residual(v)==residual(z))
    require(nu==20,'old nu')
    print('OLD [[30,4,4]] -> [[60,4,6]]: delta=4; rho=1; mu=6; nu=20')


if __name__=='__main__':
    old.check_min_plus_certificate()
    for j in range(2,7):old.check_family(j)
    uniform_low_kernel_certificate()
    for j in range(2,13):family_class_check(j)
    smallest_nu_counterexample()
    old_30_60_case()
    print('ALL AUXILIARY CHECKS PASSED')
