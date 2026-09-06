"""Exact symbolic sparse checks plus finite independent nonboundary certificates."""
from pathlib import Path
from itertools import combinations
from math import gcd
from collections import Counter
import random,json
from arithmetic import *
ROOT=Path(__file__).parent

def balanced(u,v,odd_small=True):
    odd=len(le(u))+len(le(v));w=len(u)+len(v)
    shift=int(odd>w/2) if odd_small else int(odd<w/2)
    return ls(u,shift),ls(v,shift)

def derivative_lift(A,B,delta,u,v):
    """Returns (physical tuple, method). None means this lemma doesn't apply."""
    oa=sorted(e for e in A if e%2);ob=sorted(e for e in B if e%2)
    if delta==0 and not ob:
        if len(oa)==1:
            u,v=balanced(u,v)
            p,q=ls(le(u),-oa[0]),ls(le(v),-oa[0])
            return eps_parts(u,v,p,q),'one_sided_monomial_derivative'
        if len(oa)==2:
            return eps_parts(u,v,u^le(u),le(v)),'one_sided_two_odd'
    if delta==1:
        if len(oa)==len(ob)==2:
            return eps_parts(u,v,le(u),le(v)),'two_sided_two_odd'
        if len(oa)==len(ob)==1:
            if oa[0]==ob[0]:
                u,v=balanced(u,v)
                return eps_parts(u,v,ls(le(u),-oa[0]),ls(le(v),-oa[0])),'matched_odd_exponents'
            ea=next(e for e in A if e!=0 and e%2==0)
            eb=next(e for e in B if e!=0 and e%2==0)
            if ea==eb:
                C={0,ea}
                return eps_parts(lm(C,u),lm(C,v),le(u),le(v)),'matched_even_exponents'
    return None

def divided_lift(A,B,u,v):
    r=next(e for e in A if e%2);t=next(e for e in B if e%2)
    aev=next(e for e in A if e and not e%2);bev=next(e for e in B if e and not e%2)
    R=(t-r)//2;S=(bev-aev)//2;g=gcd(abs(R),abs(S))
    assert g>0
    p,q=R//g,S//g
    alpha=lq(R,g);beta=lq(S,g)
    aa={2*i for i in alpha};bb={2*i for i in beta}
    R0=ls(aa,r)^ls(bb,aev);S0=ls(bb,aev)
    K=ls(lm({0,aev},aa)^ls(bb,aev),r)
    C={0,aev};D={0,bev}
    assert lm(R0,C)^lm(S0,A)==K
    assert lm(R0,D)^lm(S0,B)==K
    u,v=balanced(u,v,odd_small=False)
    uc=lm(R0,le(u))^lm(S0,u);vc=lm(R0,le(v))^lm(S0,v)
    parts=eps_parts(lm(K,u),lm(K,v),uc,vc)
    complexity=max(abs(p),abs(q),abs(p-q))
    assert sum(map(len,parts))<=2*complexity*(len(u)+len(v))
    return parts,dict(R=R,S=S,g=g,p=p,q=q,complexity=complexity,K=sorted(K))

def main():
    rng=random.Random(202609060600)
    tris=[{0,a,b} for a,b in combinations(range(1,14),2)]
    # Include genuine Laurent offsets, in particular the current 7/3 strip.
    tris += [{0,-1,4},{0,-13,-2},{0,1,-4},{0,13,2}]
    pairs=[]
    parity_counts=Counter();identity_checks=0
    for A in tris:
        for B in tris:
            if gcd(*(A-{0}),*(B-{0}))!=1:continue
            c=lgcd(A,B)
            if c==1:continue
            assert pgcd(c,deriv(c))==1
            D=ldata(A,B,1,39,0)
            oa=len(le(A));ob=len(le(B))
            if oa==ob==1:
                r=next(iter(le(A)));t=next(iter(le(B)))
                ae=next(e for e in A if e and not e%2);be=next(e for e in B if e and not e%2)
                R=(t-r)//2;S=(be-ae)//2;g=gcd(abs(R),abs(S))
                expect=c if g==0 else lgcd(A,{0,g})
                assert D['E']==expect
                parity_counts['one_odd_each']+=1
            elif oa==ob==2:
                assert D['E']==c
                parity_counts['two_odd_each']+=1
            else:
                assert D['E']==1
                parity_counts['transfer_only']+=1
            identity_checks+=1;pairs.append((A,B))
    rng.shuffle(pairs)
    methods=Counter();certs=[];generic=[];instances=0
    for A,B in pairs[:160]:
        for delta in (0,1):
            for L,kappa in ((15,0),(15,1),(24,0),(24,1),(39,0),(39,1)):
                try:C=LaurentCover(L,kappa,A,B,delta)
                except ValueError:continue
                D=ldata(A,B,delta,L,kappa)
                if D['g0']==1:continue
                for _ in range(2):
                    f=rng.randrange(1,32)
                    if rem(f,D['g0'])==0:continue
                    u=lm(D['b'],terms(f));v=lm(D['a'],terms(f));w=len(u)+len(v)
                    ans=derivative_lift(A,B,delta,u,v)
                    if ans is not None:
                        parts,method=ans
                        assert sum(map(len,parts))<=2*w
                    elif D['E']==1:
                        parts=(u,u,v,v);method='coprime_transfer'
                    elif delta==1 and len(le(A))==len(le(B))==1:
                        E0=pgcd(D['E'],D['g0'])
                        if E0==1 or rem(f,E0)==0:continue
                        parts,meta=divided_lift(A,B,u,v)
                        method='divided_euler'
                        assert lmod(meta['K'],E0)!=0 and pgcd(lmod(meta['K'],E0),E0)==1
                        generic.append(dict(A=sorted(A),B=sorted(B),L=L,kappa=kappa,
                                            f=terms(f),base_weight=w,universal_cover_weight=sum(map(len,parts)),**meta))
                    else:continue
                    assert universal_lcycle(A,B,delta,parts)
                    z=C.encode_physical(parts)
                    assert C.logical(z),(A,B,L,kappa,delta,method)
                    methods[method]+=1;instances+=1
                    if methods[method]<=70:
                        certs.append(C.certificate(z,{'source':method,'base_A':sorted(A),'base_B':sorted(B),'delta':delta,
                                                     'base_f':terms(f),'universal_base_weight':w,'universal_cover_weight':sum(map(len,parts))}))
    # A systematic independent symbolic grid for positive and negative reduced slopes.
    grids=0
    for p in range(-5,6):
        for q in range(-5,6):
            if gcd(abs(p),abs(q))!=1:continue
            for r,s,g in ((1,1,3),(-1,2,3),(1,-2,3)):
                A={0,r,2*s};B={0,r+2*g*p,2*s+2*g*q}
                if len(B)!=3:continue
                D=ldata(A,B,1,39,0)
                for f in (1,3,11):
                    u=lm(D['b'],terms(f));v=lm(D['a'],terms(f))
                    parts,meta=divided_lift(A,B,u,v)
                    assert universal_lcycle(A,B,1,parts)
                    E0=pgcd(D['E'],D['g0'])
                    if E0!=1:assert pgcd(lmod(meta['K'],E0),E0)==1
                    grids+=1
    out={'parity_gcd_classification_checks':identity_checks,'parity_cases':dict(parity_counts),
         'finite_nonboundary_checks':instances,'methods':dict(methods),'symbolic_slope_grid_checks':grids,
         'new_primal_dual_certificates':len(certs),'divided_euler_finite_checks':len(generic)}
    (ROOT/'lift_summary.json').write_text(json.dumps(out,indent=2)+'\n')
    (ROOT/'lift_certificates.json').write_text(json.dumps(certs,indent=2)+'\n')
    (ROOT/'divided_euler_cases.json').write_text(json.dumps(generic,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
