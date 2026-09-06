#!/usr/bin/env python3
"""Exact certificate: [[156,4,14]] -> [[312,8,12]], a BB double cover.
Python 3.10+, standard library only. No input files, network or randomness.

Representation: integer-bitset matrices and Tanner-incidence circuit search.
The search generates circuits from the check matrix, not an expected catalogue.
Run: python3 verify_lower_bitset.py [--output-dir DIR]
Success is printed only after all checks have passed.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

L=78
BASE_A=((0,0),(8,0),(25,0))
BASE_B=((0,0),(2,0),(13,0))
COVER_A=((0,0),(8,1),(25,0))
COVER_B=((0,0),(2,1),(13,0))
H_SUPPORT=(1,8,9,10,11,12,13,15,16,17,18,19,20,23,24,25,27,28,31,32,
           34,37,38,41,43,44,46,48,51,53,54,57,61,63,65,66,68,74)
TOKEN='BB_LOWER_BOUND_COUNTEREXAMPLE_VERIFIED'


def check(ok, message):
    if not ok: raise RuntimeError(message)


def bits(v):
    while v:
        b=v&-v
        yield b.bit_length()-1
        v^=b


def poly(es):
    ans=0
    for e in es: ans^=1<<e
    return ans


def mul(a,b):
    ans=0
    for i in bits(a): ans^=b<<i
    return ans


def divmod_poly(a,b):
    check(b!=0,'division by zero')
    q=0
    while a and a.bit_length()>=b.bit_length():
        i=a.bit_length()-b.bit_length()
        a^=b<<i; q^=1<<i
    return q,a


def gcd(a,b):
    while b: a,b=b,divmod_poly(a,b)[1]
    return a


def transpose(rows,n):
    out=[0]*n
    for i,row in enumerate(rows):
        for j in bits(row): out[j]|=1<<i
    return out


def act(columns,v):
    ans=0
    for i in bits(v): ans^=columns[i]
    return ans


class Span:
    def __init__(self,vectors):
        self.table={}; self.kernel=[]
        for i,v in enumerate(vectors):
            c=1<<i
            while v:
                p=v.bit_length()-1
                if p not in self.table:
                    self.table[p]=(v,c)
                    break
                row,coef=self.table[p]; v^=row; c^=coef
            if not v: self.kernel.append(c)
        self.pivots=sorted(self.table,reverse=True)
    def rank(self): return len(self.table)
    def solve(self,v):
        c=0
        for p in self.pivots:
            if (v>>p)&1:
                row,coef=self.table[p]; v^=row; c^=coef
        return c if v==0 else None


class Code:
    def __init__(self,ell,m,A,B):
        self.ell,self.m,self.N=ell,m,ell*m
        self.A,self.B=A,B
        check(len(A)==len(set(A))==len(B)==len(set(B))==3,'not distinct trinomials')
        for a,b in A+B: check(0<=a<ell and 0<=b<m,'noncanonical exponent')
        def matrix_columns(P):
            return [poly(((a+i)%ell)*m+(b+j)%m for a,b in P)
                    for i in range(ell) for j in range(m)]
        ma,mb=matrix_columns(A),matrix_columns(B)
        self.Zcheck=ma+mb
        self.HX=transpose(self.Zcheck,self.N)
        self.HZ=[b|(a<<self.N) for a,b in zip(ma,mb)]
        self.Zboundary=self.HZ
        self.Xcheck=transpose(self.HZ,2*self.N)
        self.Xboundary=self.HX
        self.hxspan=Span(self.HX); self.hzspan=Span(self.HZ)
        self.k=2*self.N-self.hxspan.rank()-self.hzspan.rank()
        check(all(act(self.Zcheck,b)==0 for b in self.HZ),'HX HZ^T != 0')
        check(all(act(self.Xcheck,b)==0 for b in self.HX),'HZ HX^T != 0')
        check(all(v.bit_count()==3 for v in self.Zcheck+self.Xcheck),'wrong column degree')
        check(all(v.bit_count()==6 for v in self.HX+self.HZ),'wrong row degree')
    def encode(self,left,right):
        return poly(i*self.m+j for i,j in left)|(poly(i*self.m+j for i,j in right)<<self.N)
    def support(self,v):
        return {'left':[[i//self.m,i%self.m] for i in bits(v&((1<<self.N)-1))],
                'right':[[i//self.m,i%self.m] for i in bits(v>>self.N)]}
    def star(self,v):
        return poly(
                    ((-(i//self.m))%self.ell)*self.m+(-(i%self.m))%self.m for i in bits(v))
    def J(self,v):
        return self.star(v>>self.N)|(self.star(v&((1<<self.N)-1))<<self.N)
    def translate(self,v,a,b):
        out=0
        for k in bits(v):
            block,j=divmod(k,self.N); i,j=divmod(j,self.m)
            out|=1<<(block*self.N+((i+a)%self.ell)*self.m+(j+b)%self.m)
        return out


def project(v):
    # Cover index block*156 + 2*x+y -> base block*78+x, by linear extension.
    return poly((i//156)*78+((i%156)//2) for i in bits(v))


def transfer(v):
    ans=0
    for i in bits(v):
        b,j=divmod(i,78); k=b*156+2*j
        ans^=(1<<k)|(1<<(k+1))
    return ans


def graph(code):
    out={(t,j):set() for t in range(4) for j in range(code.N)}
    for t,rows in ((2,code.HX),(3,code.HZ)):
        for i,row in enumerate(rows):
            for j in bits(row):
                q=(j//code.N,j%code.N)
                out[(t,i)].add(q);out[q].add((t,i))
    return out


def check_cover(base,cover):
    check((cover.ell,cover.m)==(base.ell,2*base.m),'periods do not form double cover')
    for src,dst in ((cover.A,base.A),(cover.B,base.B)):
        check(tuple((i%base.ell,j%base.m) for i,j in src)==dst,'monomial mismatch')
    gb,gc=graph(base),graph(cover)
    p=lambda v:(v[0],v[1]//2)
    check(Counter(p(v) for v in gc)==Counter({v:2 for v in gb}),'fiber cardinality')
    for v,ns in gc.items():
        images=[p(w) for w in ns]
        check(len(images)==len(set(images)) and set(images)==gb[p(v)],'neighborhood bijection')
    for C,G in ((base,gb),(cover,gc)):
        seen=set(); pending=[(0,0)]
        while pending:
            v=pending.pop()
            if v in seen: continue
            seen.add(v);pending.extend(G[v]-seen)
        check(len(seen)==4*C.N,'Tanner graph disconnected')
    for j,g in enumerate(cover.Zboundary):
        check(project(g)==base.Zboundary[j//2],'degree-2 chain identity')
    for i,col in enumerate(cover.Zcheck):
        pcol=poly(j//2 for j in bits(col))
        check(pcol==act(base.Zcheck,project(1<<i)),'degree-1 chain identity')


def check_J(C):
    permutation=[next(bits(C.J(1<<i))) for i in range(2*C.N)]
    check(sorted(permutation)==list(range(2*C.N)),'J is not a permutation')
    for i in range(2*C.N):
        check(act(C.Xcheck,C.J(1<<i))==C.star(C.Zcheck[i]),'J cycle identity')
    for j,b in enumerate(C.Zboundary):
        sj=next(bits(C.star(1<<j)))
        check(C.J(b)==C.Xboundary[sj],'J boundary identity')


def canonical_matrix(rows,ncols):
    text=f'GF2MATRIX v1\n{len(rows)} {ncols}\n'
    text+=''.join(''.join('1' if (v>>j)&1 else '0' for j in range(ncols))+'\n' for v in rows)
    return text.encode('ascii')


def enumerate_root(C,sector,bound,root):
    columns=getattr(C,sector+'check'); bd=getattr(C,sector+'boundary')
    span=Span(bd); adj=[0]*C.N
    for j,col in enumerate(columns):
        for i in bits(col): adj[i]|=1<<j
    stats=Counter({s:0 for s in ('nodes','expanded','budget','syndrome_bound','blocked','zero')})
    leaves=Counter(); circuits=set(); circuit_weights=Counter()
    def visit(U,E,syn,weight):
        stats['nodes']+=1
        if syn==0:
            stats['zero']+=1;leaves[weight]+=1
            check(span.solve(U) is not None,f'EXCLUSION FAILED: {sector}, n={2*C.N}, support={list(bits(U))}')
            if Span([columns[j] for j in bits(U)]).rank()==weight-1:
                circuits.add(U);circuit_weights[weight]+=1
            return
        remaining=bound-weight
        if remaining<=0: stats['budget']+=1;return
        if syn.bit_count()>3*remaining: stats['syndrome_bound']+=1;return
        candidates=0;smallest=7;excluded=U|E
        for i in bits(syn):
            av=adj[i]&~excluded;deg=av.bit_count()
            if not deg: stats['blocked']+=1;return
            if deg<smallest: smallest=deg;candidates=av
        stats['expanded']+=1
        while candidates:
            b=candidates&-candidates;candidates^=b
            visit(U|b,E,syn^columns[b.bit_length()-1],weight+1)
            E|=b
    visit(1<<root,0,columns[root],1)
    check(stats['nodes']==sum(stats[s] for s in ('expanded','budget','syndrome_bound','blocked','zero')),'node accounting')
    return dict(stats,sector=sector,root=root,bound=bound,
                zero_weights=dict(sorted(leaves.items())),circuit_weights=dict(sorted(circuit_weights.items()))),circuits


def classify(C,rooted):
    all_circuits={C.translate(v,a,b) for v in rooted for a in range(C.ell) for b in range(C.m)}
    remaining=set(all_circuits); records=[];span=Span(C.Zboundary)
    while remaining:
        seed=min(remaining)
        orbit={C.translate(seed,a,b) for a in range(C.ell) for b in range(C.m)}
        rep=min(orbit,key=lambda v:tuple(bits(v)))
        h=span.solve(rep)
        check(h is not None and act(C.Zboundary,h)==rep,'orbit preimage')
        records.append(dict(support=C.support(rep),flat=list(bits(rep)),weight=rep.bit_count(),
                            size=len(orbit),preimage=list(bits(h))))
        remaining-=orbit
    records.sort(key=lambda r:(r['weight'],r['flat']))
    return all_circuits,records


# F4 elements are a+b*omega, encoded a+2*b; omega^2=omega+1.
def fm(a,b):
    v=mul(a,b)
    return divmod_poly(v,7)[1]

def dm(a,b):
    # F4[eta]/eta^2: a=(constant, eta-coefficient).
    return (fm(a[0],b[0]),fm(a[0],b[1])^fm(a[1],b[0]))

def dp(a,k):
    ans=(1,0)
    while k:
        if k&1: ans=dm(ans,a)
        a=dm(a,a);k>>=1
    return ans

def evaluate(es):
    ans=(0,0)
    for i,j in es:
        v=dm(dp((2,1),i),dp((1,2),j))
        ans=(ans[0]^v[0],ans[1]^v[1])
    return ans


def main(outdir=None):
    out=Path(outdir) if outdir else None
    if out: out.mkdir(parents=True,exist_ok=True)
    base=Code(78,1,BASE_A,BASE_B); cover=Code(78,2,COVER_A,COVER_B)
    check_cover(base,cover)
    report={'inputs':{'base':[78,1,BASE_A,BASE_B],'cover':[78,2,COVER_A,COVER_B]},'codes':{},'searches':[]}
    A=poly(i for i,j in BASE_A);B=poly(i for i,j in BASE_B);F=poly([0,78]);g=7
    check(gcd(gcd(A,B),F)==g,'base gcd')
    C=mul(poly([0,6]),poly([0,19]));B2=mul(B,B)
    check(C==A^(B<<6),'elimination identity')
    check(gcd(gcd(F,C),B2)==mul(g,g),'cover elimination gcd')
    for name,Cd,rank,k in [('base',base,76,4),('cover',cover,152,8)]:
        check(Cd.hxspan.rank()==Cd.hzspan.rank()==rank and Cd.k==k,'rank/dimension')
        check_J(Cd)
        rec={'n':2*Cd.N,'k':Cd.k,'rank_HX':rank,'rank_HZ':rank,'sha256':{}}
        for mat in ('HX','HZ'):
            data=canonical_matrix(getattr(Cd,mat),2*Cd.N)
            digest=hashlib.sha256(data).hexdigest();rec['sha256'][mat]=digest
            print('MATRIX',name,mat,digest,flush=True)
            if out: (out/f'{name}_{mat}.txt').write_bytes(data)
        report['codes'][name]=rec
    print('VALIDITY, COMMUTATION, CONNECTIVITY, RANKS, J: PASS',flush=True)
    # Explicit base witness of weight 14.
    z14=base.encode(tuple((i,0) for i in (39,47,55,64)),
                    tuple((i,0) for i in (0,9,11,22,35,37,48,61,74,76)))
    check(z14.bit_count()==14 and act(base.Zcheck,z14)==0,'base witness cycle')
    mask=(1<<78)-1
    check(mul(A,z14&mask)^mul(B,z14>>78)==mul(F,poly([0,2,9])),
          'ordinary polynomial identity for the base witness')
    check(base.hzspan.solve(z14) is None,'base witness nontriviality')
    # Explicit cover witness as (1+x^39*y)*(ZL,ZR).
    zL=((0,0),(8,1),(16,0),(25,0));zR=((0,0),(11,1))
    small=cover.encode(zL,zR)
    w=small^cover.translate(small,39,1)
    check(w.bit_count()==12 and act(cover.Zcheck,w)==0,'cover witness cycle')
    # Symbolic identity over F2[x,y]/(y^2+1), before reducing the x period.
    def ymul(u,v):
        return (mul(u[0],v[0])^mul(u[1],v[1]),mul(u[0],v[1])^mul(u[1],v[0]))
    ap=(poly([0,25]),poly([8]));bp=(poly([0,13]),poly([2]))
    zl=(poly([0,16,25]),poly([8]));zr=(1,poly([11]));sigma=(1,poly([39]))
    lhs1,lhs2=ymul(ap,zl),ymul(bp,zr)
    check((lhs1[0]^lhs2[0],lhs1[1]^lhs2[1])==ymul(sigma,(0,poly([2,11]))),
          'ordinary coefficient-ring identity for the cover witness')
    check(ymul(sigma,sigma)==(F,0),'mixed square-zero element')
    check(cover.hzspan.solve(w) is None,'cover witness nontriviality')
    check(evaluate(((0,0),(78,0)))==(0,0) and evaluate(((0,0),(0,2)))==(0,0),'quotient-map periods')
    check(evaluate(COVER_A)==evaluate(COVER_B)==(0,0),'quotient-map generators')
    ws=cover.support(w)
    check(evaluate(ws['left'])==evaluate(ws['right'])==(0,2),'nonzero omega*eta certificate')
    q=project(w);H=poly(H_SUPPORT)
    check(act(base.Zboundary,H)==q,'projected cycle is the stated base boundary')
    check(q.bit_count()==12,'projection weight')
    # Exact transfer-sector formula, using the y=1+epsilon presentation.
    r=poly((i//156)*78+(i%156)//2 for i in bits(w) if i%2==1)
    def rotate(v,a):
        a%=78;return ((v<<a)|(v>>(78-a)))&((1<<78)-1)
    DH=rotate(H,2)|(rotate(H,8)<<78)
    a=r^DH
    check(act(base.Zcheck,a)==0 and base.hzspan.solve(a) is None,'base transfer class')
    lowH=poly(2*i for i in H_SUPPORT)
    check(w^act(cover.Zboundary,lowH)==transfer(a),'transfer representative identity')
    # beta_2=0 independently on a full basis of H_2(base).
    for h in base.hzspan.kernel:
        Dh=rotate(h,2)|(rotate(h,8)<<78)
        check(base.hzspan.solve(Dh) is not None,'beta_2 is not zero')
    report['witnesses']={'base_weight_14':base.support(z14),'cover_weight_12':ws,
                         'projection':base.support(q),'boundary_H':list(H_SUPPORT),
                         'r':base.support(r),'transfer_preimage_a':base.support(a)}
    print('WITNESSES, DUAL-NUMBER NONTRIVIALITY, PROJECTED BOUNDARY, TRANSFER: PASS',flush=True)
    for name,Cd,bound,expected in [('base',base,12,{6:78,10:468,12:195}),
                                 ('cover',cover,10,{6:156,10:936})]:
        rooted=set()
        for sector in ('Z','X'):
            for root in (0,Cd.N):
                stats,circuits=enumerate_root(Cd,sector,bound,root)
                report['searches'].append(dict(code=name,**stats))
                print('SEARCH',name,json.dumps(stats,sort_keys=True),flush=True)
                if sector=='Z': rooted|=circuits
        allcircs,orbits=classify(Cd,rooted)
        # Post-search classification: generated boundaries never guide pruning.
        diffs=set()
        for P in (Cd.A,Cd.B):
            for i,(a,b) in enumerate(P):
                for c,e in P[i+1:]:
                    d=((a-c)%Cd.ell,(b-e)%Cd.m)
                    nd=((-d[0])%Cd.ell,(-d[1])%Cd.m)
                    diffs.add(min(d,nd))
        seeds=[act(Cd.Zboundary,1)]
        seeds += [act(Cd.Zboundary,1^(1<<(a*Cd.m+b))) for a,b in sorted(diffs)]
        if name=='base':
            seeds += [act(Cd.Zboundary,A),act(Cd.Zboundary,B),q]
        predicted={Cd.translate(v,a,b) for v in seeds for a in range(Cd.ell) for b in range(Cd.m)}
        check(allcircs==predicted,'post-search orbit classification mismatch')
        hist=dict(sorted(Counter(v.bit_count() for v in allcircs).items()))
        check(hist==expected,'unexpected circuit counts')
        report['codes'][name]['circuits']=hist;report['codes'][name]['orbits']=orbits
        serial='\n'.join(','.join(map(str,s)) for s in sorted((tuple(bits(v)) for v in allcircs),key=lambda x:(len(x),x)))+'\n'
        data=serial.encode('ascii');digest=hashlib.sha256(data).hexdigest()
        report['codes'][name]['circuit_sha256']=digest
        if out: (out/f'{name}_circuits.txt').write_bytes(data)
        print('CIRCUITS',name,len(allcircs),len(orbits),hist,digest,flush=True)
    report['codes']['base']['d']=14;report['codes']['cover']['d']=12
    check(12<14,'not a lower-bound violation')
    if out: (out/'report.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print('PARAMETERS: [[156,4,14]] -> [[312,8,12]]',flush=True)
    print(TOKEN,flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir')
    args=parser.parse_args()
    main(args.output_dir)
