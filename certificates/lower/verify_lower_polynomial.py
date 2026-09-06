#!/usr/bin/env python3
"""Independent certificate for [[156,4,14]] -> [[312,8,12]].
Python 3.10+, standard library only, no input files.

Polynomials are frozensets of exponents, with symmetric-difference addition.
Boundary membership uses polynomial Bezout congruences, not matrix-span tests.
Search branches on entire odd subsets at an odd check, rather than selecting
one candidate at a time. No expected circuit supports are used.
Run: python3 verify_lower_polynomial.py [--output-dir DIR]
"""
import argparse
from collections import Counter
from functools import lru_cache
import hashlib
from itertools import combinations
import json
from pathlib import Path

ELL=78
BASE_A=frozenset({(0,0),(8,0),(25,0)})
BASE_B=frozenset({(0,0),(2,0),(13,0)})
COVER_A=frozenset({(0,0),(8,1),(25,0)})
COVER_B=frozenset({(0,0),(2,1),(13,0)})
ZERO=frozenset();ONE=frozenset({0})
TOKEN='BB_LOWER_BOUND_COUNTEREXAMPLE_VERIFIED'


def need(ok,message):
    if not ok: raise RuntimeError(message)


def polynomial(es):
    s=set()
    for e in es:
        if e in s:s.remove(e)
        else:s.add(e)
    return frozenset(s)


def multiply(a,b):
    return polynomial(i+j for i in a for j in b)


def divide(a,b):
    need(bool(b),'division by zero')
    r=set(a);q=set();db=max(b)
    while r and max(r)>=db:
        t=max(r)-db;q.add(t)
        r.symmetric_difference_update(i+t for i in b)
    return frozenset(q),frozenset(r)


def egcd(a,b):
    u,uu,v,vv=ONE,ZERO,ZERO,ONE
    while b:
        q,r=divide(a,b)
        a,b=b,r;u,uu=uu,u^multiply(q,uu);v,vv=vv,v^multiply(q,vv)
    return a,u,v


def residue(a,L): return polynomial(i%L for i in a)

def conv(a,b,L):return residue(multiply(a,b),L)

def shift(a,j,L):return frozenset((i+j)%L for i in a)


class Congruences:
    """Solve P*h=e, Q*h=f modulo x^L+1, by a three-term Bezout identity."""
    def __init__(self,P,Q,L):
        self.P,self.Q,self.L=P,Q,L;self.F=frozenset({0,L})
        pq=egcd(P,Q)[0];self.g=egcd(pq,self.F)[0]
        a,ar=divide(P,self.g);b,br=divide(Q,self.g);self.t,tr=divide(self.F,self.g)
        need(not (ar or br or tr),'gcd divisions')
        d,s,u=egcd(a,b);one,c,w=egcd(d,self.t)
        need(one==ONE,'noncoprime cofactors')
        self.U,self.V=multiply(c,s),multiply(c,u)
        need(multiply(self.U,a)^multiply(self.V,b)^multiply(w,self.t)==ONE,'Bezout identity')
    def solve(self,e,f):
        ee,re=divide(e,self.g);ff,rf=divide(f,self.g)
        if re or rf:return None
        h=divide(multiply(self.U,ee)^multiply(self.V,ff),self.t)[1]
        return h if conv(self.P,h,self.L)==e and conv(self.Q,h,self.L)==f else None


def rank(vectors):
    table={}
    for row in vectors:
        v=set(row)
        while v:
            p=min(v)
            if p not in table:table[p]=frozenset(v);break
            v.symmetric_difference_update(table[p])
    return len(table)


class Ring:
    def __init__(self,L,m):self.L,self.m,self.N=L,m,L*m
    def mul(self,P,Q):
        return polynomial(((i+k)%self.L,(j+l)%self.m) for i,j in P for k,l in Q)
    def shifted(self,P,a,b):
        return frozenset(((i+a)%self.L,(j+b)%self.m) for i,j in P)
    def star(self,P):return frozenset((-i%self.L,-j%self.m) for i,j in P)
    def index(self,P):return frozenset(i*self.m+j for i,j in P)
    def unindex(self,S):return frozenset(divmod(i,self.m) for i in S)
    def flat(self,chain):
        return self.index(chain[0])|frozenset(self.N+i for i in self.index(chain[1]))
    def unflat(self,S):
        return self.unindex(i for i in S if i<self.N),self.unindex(i-self.N for i in S if i>=self.N)
    def J(self,chain):return self.star(chain[1]),self.star(chain[0])


class Code:
    def __init__(self,L,m,P,Q):
        self.ring=Ring(L,m);self.L,self.m,self.N=L,m,L*m;self.P,self.Q=P,Q
        need(len(P)==len(Q)==3,'trinomial condition')
        R=self.ring
        self.columns=tuple(R.index(R.shifted(pol,i,j)) for pol in (P,Q)
                           for i in range(L) for j in range(m))
        self.neighbors=[[] for _ in range(self.N)]
        for j,col in enumerate(self.columns):
            for i in col:self.neighbors[i].append(j)
        self.neighbors=tuple(tuple(sorted(ns)) for ns in self.neighbors)
        self.HX=tuple(frozenset(ns) for ns in self.neighbors)
        self.HZ=tuple(
            R.flat(self.boundary(frozenset({(i,j)}))) for i in range(L) for j in range(m))
        need(all(len(r)==6 for r in self.HX+self.HZ),'row weights')
        need(all(len(c)==3 for c in self.columns),'column weights')
        if m==1:
            self.solver=Congruences(frozenset(i for i,j in Q),frozenset(i for i,j in P),L)
        elif m==2:
            self.P0=frozenset(i for i,j in P if j==0);self.P1=frozenset(i for i,j in P if j==1)
            self.Q0=frozenset(i for i,j in Q if j==0);self.Q1=frozenset(i for i,j in Q if j==1)
            need(len(self.Q1)==1,'solver requires monomial y coefficient in Q')
            self.qinv=frozenset({(-next(iter(self.Q1)))%L})
            self.c1=conv(self.P1,self.qinv,L)
            D=conv(self.Q0,self.Q0,L)^conv(self.Q1,self.Q1,L)
            C=self.P0^conv(self.c1,self.Q0,L)
            self.solver=Congruences(D,C,L)
        else: raise RuntimeError('unsupported m')
    def syndrome(self,chain):
        return self.ring.mul(self.P,chain[0])^self.ring.mul(self.Q,chain[1])
    def boundary(self,h):return self.ring.mul(self.Q,h),self.ring.mul(self.P,h)
    def boundary_preimage(self,chain):
        u,v=chain
        if self.m==1:
            h=self.solver.solve(frozenset(i for i,j in u),frozenset(i for i,j in v))
            if h is None:return None
            out=frozenset((i,0) for i in h)
        else:
            u0=frozenset(i for i,j in u if j==0);u1=frozenset(i for i,j in u if j==1)
            v0=frozenset(i for i,j in v if j==0)
            e=conv(self.Q1,u1,self.L)^conv(self.Q0,u0,self.L)
            f=v0^conv(self.c1,u0,self.L)
            h0=self.solver.solve(e,f)
            if h0 is None:return None
            h1=conv(self.qinv,u0^conv(self.Q0,h0,self.L),self.L)
            out=frozenset((i,0) for i in h0)|frozenset((i,1) for i in h1)
        return out if self.boundary(out)==chain else None
    def circuit(self,S):return bool(S) and rank(self.columns[j] for j in S)==len(S)-1


def matrix_bytes(rows,n):
    s=f'GF2MATRIX v1\n{len(rows)} {n}\n'
    s+=''.join(''.join('1' if j in r else '0' for j in range(n))+'\n' for r in rows)
    return s.encode('ascii')


def enumerate_root(C,bound,root):
    columns=C.columns;neighbors=C.neighbors
    stats=Counter({s:0 for s in ('nodes','expanded','budget','syndrome_bound','blocked','zero')})
    wh=Counter();cw=Counter();circuits=set()
    @lru_cache(maxsize=8192)
    def options(candidates):
        entries=[];allcand=frozenset(candidates)
        for k in range(1,len(candidates)+1,2):
            for subset in combinations(candidates,k):
                yes=frozenset(subset);syn=ZERO
                for j in subset:syn=syn^columns[j]
                entries.append((yes,allcand-yes,syn,k))
        return tuple(entries)
    def visit(U,E,syn):
        stats['nodes']+=1;w=len(U)
        if not syn:
            stats['zero']+=1;wh[w]+=1
            need(C.boundary_preimage(C.ring.unflat(U)) is not None,
                 f'EXCLUSION FAILED: n={2*C.N}, support={sorted(U)}')
            if C.circuit(U):circuits.add(U);cw[w]+=1
            return
        remaining=bound-w
        if remaining<=0:stats['budget']+=1;return
        if len(syn)>3*remaining:stats['syndrome_bound']+=1;return
        excluded=U|E;candidates=None
        for i in sorted(syn):
            av=tuple(j for j in neighbors[i] if j not in excluded)
            if not av:stats['blocked']+=1;return
            if candidates is None or len(av)<len(candidates):candidates=av
        stats['expanded']+=1
        for yes,no,delta,k in options(candidates):
            if k<=remaining:visit(U|yes,E|no,syn^delta)
    visit(frozenset({root}),ZERO,columns[root])
    need(stats['nodes']==sum(stats[s] for s in ('expanded','budget','syndrome_bound','blocked','zero')),'node accounting')
    return dict(stats,root=root,bound=bound,zero_weights=dict(sorted(wh.items())),circuit_weights=dict(sorted(cw.items()))),circuits


def full_circuits(C,rooted):
    R=C.ring;result=set()
    for S in rooted:
        u,v=R.unflat(S)
        for i in range(C.L):
            for j in range(C.m):result.add(R.flat((R.shifted(u,i,j),R.shifted(v,i,j))))
    return result


def main(outdir=None):
    out=Path(outdir) if outdir else None
    if out:out.mkdir(parents=True,exist_ok=True)
    base=Code(78,1,BASE_A,BASE_B);cover=Code(78,2,COVER_A,COVER_B)
    report={'implementation':'sparse_polynomial_odd_subsets','codes':{},'searches':[]}
    need(frozenset((i,j%1) for i,j in COVER_A)==BASE_A and
         frozenset((i,j%1) for i,j in COVER_B)==BASE_B,'monomial projection')
    def p(S):return polynomial((i,0) for i,j in S)
    # Chain and graph-neighborhood checks on all basis vectors, both check types.
    for j,col in enumerate(cover.columns):
        block,k=divmod(j,156);i,y=divmod(k,2)
        pc=polynomial(e//2 for e in col)
        need(pc==base.columns[block*78+i],'projection on columns')
        need(len(pc)==len(col),'projection folds a column neighborhood')
    for hrow in range(156):
        for covermat,basemat in ((cover.HX,base.HX),(cover.HZ,base.HZ)):
            images=[(j//156)*78+(j%156)//2 for j in covermat[hrow]]
            need(len(images)==len(set(images)) and set(images)==set(basemat[hrow//2]),'row neighborhood cover')
    g=frozenset({0,1,2})
    need(base.solver.g==g,'base gcd')
    need(cover.solver.g==multiply(g,g),'cover elimination gcd')
    z14=(frozenset((i,0) for i in (39,47,55,64)),
         frozenset((i,0) for i in (0,9,11,22,35,37,48,61,74,76)))
    zL=frozenset({(0,0),(8,1),(16,0),(25,0)});zR=frozenset({(0,0),(11,1)})
    s=frozenset({(0,0),(39,1)})
    w=(cover.ring.mul(s,zL),cover.ring.mul(s,zR))
    need(not base.syndrome(z14) and base.boundary_preimage(z14) is None and len(base.ring.flat(z14))==14,'base witness')
    need(not cover.syndrome(w) and cover.boundary_preimage(w) is None and len(cover.ring.flat(w))==12,'cover witness')
    q=(p(w[0]),p(w[1]));h=base.boundary_preimage(q)
    need(h is not None and base.boundary(h)==q,'projection is boundary')
    report['witnesses']={'base':[[list(t) for t in sorted(z)] for z in z14],
                         'cover':[[list(t) for t in sorted(z)] for z in w],
                         'projected_boundary_preimage':sorted(i for i,j in h)}
    print('COVER IDENTITIES, POLYNOMIAL WITNESSES AND BOUNDARY SOLVERS: PASS',flush=True)
    for name,C,dim,bound,expected in [('base',base,4,12,{6:78,10:468,12:195}),
                                     ('cover',cover,8,10,{6:156,10:936})]:
        R=C.ring
        dual=Code(C.L,C.m,R.star(C.Q),R.star(C.P))
        need(dual.HX==C.HZ and dual.HZ==C.HX,'independently reconstructed X matrices')
        for j in range(C.N):
            h0=frozenset({divmod(j,C.m)})
            b=C.boundary(h0)
            need(not C.syndrome(b),'commutation')
            need(C.boundary_preimage(b) is not None,'membership solver rejected a generator')
            need(R.J(b)==dual.boundary(R.star(h0)),'J boundaries')
        for j in range(2*C.N):
            v=R.unflat(frozenset({j}))
            need(dual.syndrome(R.J(v))==R.star(C.syndrome(v)),'J cycle identity')
        rec={'n':2*C.N,'k':2*C.N-rank(C.HX)-rank(C.HZ),'rank_HX':rank(C.HX),'rank_HZ':rank(C.HZ),'sha256':{}}
        need(rec['k']==dim and rec['rank_HX']==rec['rank_HZ']==C.N-dim//2,'independent binary rank')
        for mat in ('HX','HZ'):
            data=matrix_bytes(getattr(C,mat),2*C.N);digest=hashlib.sha256(data).hexdigest();rec['sha256'][mat]=digest
            print('MATRIX',name,mat,digest,flush=True)
            if out:(out/f'{name}_{mat}.txt').write_bytes(data)
        rooted=set()
        for sector,D in (('Z',C),('X',dual)):
            for root in (0,C.N):
                stats,cs=enumerate_root(D,bound,root)
                report['searches'].append(dict(code=name,sector=sector,**stats))
                print('SEARCH',name,sector,json.dumps(stats,sort_keys=True),flush=True)
                if sector=='Z':rooted|=cs
        cs=full_circuits(C,rooted);hist=dict(sorted(Counter(len(S) for S in cs).items()))
        # Independently compare the completed search with the concise orbit formulas.
        diffs=set()
        for P in (C.P,C.Q):
            for a,b in combinations(sorted(P),2):
                d=((a[0]-b[0])%C.L,(a[1]-b[1])%C.m)
                nd=(-d[0]%C.L,-d[1]%C.m)
                diffs.add(min(d,nd))
        seeds={R.flat(C.boundary(frozenset({(0,0)})))}
        seeds |= {R.flat(C.boundary(frozenset({(0,0),d}))) for d in diffs}
        if name=='base':
            seeds |= {R.flat(C.boundary(C.P)),R.flat(C.boundary(C.Q)),R.flat(q)}
        need(cs==full_circuits(C,seeds),'independent post-search orbit classification')
        need(hist==expected,'independent circuit counts')
        serial='\n'.join(','.join(map(str,t)) for t in sorted((tuple(sorted(S)) for S in cs),key=lambda t:(len(t),t)))+'\n'
        data=serial.encode('ascii');digest=hashlib.sha256(data).hexdigest()
        rec['circuits']=hist;rec['circuit_sha256']=digest;rec['d']=14 if name=='base' else 12
        report['codes'][name]=rec
        if out:(out/f'{name}_circuits.txt').write_bytes(data)
        print('CIRCUITS',name,len(cs),hist,digest,flush=True)
    if out:(out/'report.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print('PARAMETERS: [[156,4,14]] -> [[312,8,12]]',flush=True)
    print(TOKEN,flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output-dir')
    args=parser.parse_args();main(args.output_dir)
