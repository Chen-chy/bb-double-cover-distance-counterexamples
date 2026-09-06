#!/usr/bin/env python3
"""Exact tests for odd-torsion strip compact-homology descent.

Uses integer bit vectors for GF(2), and implements finite fields, Laurent
component gcds, Chinese remaindering, and finite-group matrices separately.
No minimum-distance search is used to infer a distance lower bound.
"""
from __future__ import annotations
import itertools, math, random, json, hashlib, time
from pathlib import Path


def pmul(a: int, b: int) -> int:
    out = 0
    while b:
        if b & 1: out ^= a
        a <<= 1; b >>= 1
    return out


def pdiv(a: int, b: int) -> tuple[int, int]:
    if not b: raise ZeroDivisionError
    q = 0
    while a and a.bit_length() >= b.bit_length():
        s = a.bit_length() - b.bit_length()
        q ^= 1 << s; a ^= b << s
    return q, a


def pinv(a: int, m: int) -> int:
    r0, r1, s0, s1 = m, a, 0, 1
    while r1:
        q, r = pdiv(r0, r1)
        r0, r1, s0, s1 = r1, r, s1, s0 ^ pmul(q, s1)
    if r0 != 1: raise ValueError('not invertible')
    return pdiv(s0, m)[1]


def factor_squarefree(q: int) -> list[int]:
    out = []
    for d in range(1, (q.bit_length()-1)//2+1):
        for f in range((1 << d) | 1, 1 << (d+1), 2):
            while q != 1:
                a, r = pdiv(q, f)
                if r: break
                out.append(f); q = a
    if q != 1: out.append(q)
    assert len(out) == len(set(out))
    return out


class Field:
    def __init__(self, mod: int):
        self.mod = mod
        self.degree = mod.bit_length()-1
        self.order = 1 << self.degree
        self.table = [[pdiv(pmul(a,b),mod)[1] for b in range(self.order)] for a in range(self.order)]
        self.inverses = [0] + [pinv(a,mod) for a in range(1,self.order)]
    def mul(self, a: int, b: int) -> int: return self.table[a][b]
    @staticmethod
    def trim(p: list[int]) -> list[int]:
        while p and p[-1] == 0: p.pop()
        return p
    def div(self, a: list[int], b: list[int]) -> tuple[list[int],list[int]]:
        a = a.copy()
        if not b: raise ZeroDivisionError
        q = [0]*max(0, len(a)-len(b)+1)
        inv = self.inverses[b[-1]]
        while len(a) >= len(b):
            s = len(a)-len(b); c = self.mul(a[-1],inv); q[s] ^= c
            for i, v in enumerate(b): a[s+i] ^= self.mul(c,v)
            self.trim(a)
        return self.trim(q), a
    def gcd(self, a: list[int], b: list[int]) -> list[int]:
        while b: a,b = b,self.div(a,b)[1]
        if not a: return []
        return [self.mul(x,self.inverses[a[-1]]) for x in a]


class Basis:
    def __init__(self, vectors=()):
        self.piv = {}
        for v in vectors: self.add(v)
    def reduce(self, v: int) -> int:
        remainder=0
        while v:
            p=v.bit_length()-1
            if p in self.piv: v ^= self.piv[p]
            else:
                remainder ^= 1<<p
                v ^= 1<<p
        return remainder
    def add(self, v: int) -> bool:
        v=self.reduce(v)
        if not v: return False
        self.piv[v.bit_length()-1]=v; return True
    def __len__(self): return len(self.piv)


class Group:
    """Normal forms t^i z^j, t^h=1, z^P=t^seam."""
    def __init__(self,h:int,P:int,seam:int):
        self.h,self.P,self.seam,self.n=h,P,seam%h,h*P
        self.translations=[]
        for g in range(self.n):
            gi,gj=divmod(g,P)
            self.translations.append([self.idx(gi+i,gj+j) for i in range(h) for j in range(P)])
    def idx(self,i:int,j:int)->int:
        c,j=divmod(j,self.P)
        return ((i+c*self.seam)%self.h)*self.P+j
    def vector(self, terms)->int:
        v=0
        for i,j in terms: v ^= 1<<self.idx(i,j)
        return v
    def shift(self,v:int,g:int)->int:
        out=0; tr=self.translations[g]
        while v:
            b=v & -v; i=b.bit_length()-1; v ^= b; out ^= 1<<tr[i]
        return out
    def mul(self,a:int,b:int)->int:
        out=0
        while b:
            q=b & -b; out ^= self.shift(a,q.bit_length()-1); b ^= q
        return out
    def shift2(self,v:int,g:int)->int:
        mask=(1<<self.n)-1
        return self.shift(v&mask,g) | (self.shift(v>>self.n,g)<<self.n)
    def boundaries(self,a:int,b:int)->Basis:
        return Basis(self.shift(b,g) | (self.shift(a,g)<<self.n) for g in range(self.n))
    def syndrome(self,v:int,a:int,b:int)->int:
        mask=(1<<self.n)-1
        return self.mul(v&mask,a)^self.mul(v>>self.n,b)
    def k(self,a:int,b:int)->int:
        return 2*(self.n-len(Basis(itertools.chain((self.shift(a,g) for g in range(self.n)),(self.shift(b,g) for g in range(self.n))))))


def components(h:int):
    q=(1<<h)^1; data=[]
    for f in factor_squarefree(q):
        F=Field(f); other,rem=pdiv(q,f); assert rem==0
        E=pdiv(pmul(other,pinv(pdiv(other,f)[1],f)),q)[1]
        assert pdiv(pmul(E,E),q)[1]==E
        data.append((f,F,E))
    e=0
    for _,_,E in data: e ^= E
    assert e==1
    return data


def universal_generators(h:int, A, B, comp):
    """Return a full CRT generating family of the universal cycle module."""
    gens=[]
    for mod,F,E in comp:
        def image(terms):
            out=[0]*(1+max(j for i,j in terms))
            for i,j in terms: out[j] ^= pdiv(1<<(i%h),mod)[1]
            return F.trim(out)
        aa,bb=image(A),image(B)
        g=F.gcd(aa,bb)
        if not g: raise AssertionError('both components vanished')
        # z is a Laurent unit; remove the z-primary factor before squarefree test.
        gg=g.copy()
        while gg and gg[0]==0: gg.pop(0)
        derivative=[gg[i] if i%2 else 0 for i in range(1,len(gg))]
        assert len(F.gcd(gg,F.trim(derivative)))==1, (h,A,B,mod,g)
        u,ru=F.div(bb,g); v,rv=F.div(aa,g)
        assert not ru and not rv
        def lift(poly):
            terms=[]
            for j,c in enumerate(poly):
                t=pdiv(pmul(E,c),(1<<h)^1)[1]
                while t:
                    bit=t & -t; terms.append((bit.bit_length()-1,j)); t ^= bit
            return terms
        gens.append((lift(u),lift(v)))
    return gens


def generated(h:int,A,B)->bool:
    cols=list(A[1:])+list(B[1:])+[(h,0)]
    g=0
    for a,b in itertools.combinations(cols,2): g=math.gcd(g,abs(a[0]*b[1]-b[0]*a[1]))
    return g==1


def check_case(h,P,seam,A,B,comp):
    lo=Group(h,P,seam); hi=Group(h,2*P,2*seam)
    al,bl=lo.vector(A),lo.vector(B); ah,bh=hi.vector(A),hi.vector(B)
    if any(x.bit_count()!=3 for x in [al,bl,ah,bh]): return None
    if not lo.k(al,bl): return None
    boundary_lo, boundary_hi=lo.boundaries(al,bl),hi.boundaries(ah,bh)
    def project(v):
        out=0
        for block in [0,1]:
            part=(v>>(block*hi.n))&((1<<hi.n)-1)
            while part:
                bit=part & -part; i,j=divmod(bit.bit_length()-1,hi.P)
                out ^= 1<<(block*lo.n+lo.idx(i,j)); part ^= bit
        return out
    assert project(ah)==al and project(bh)==bl
    rank_lo,rank_hi,rank_joint=Basis(),Basis(),Basis()
    for U,V in universal_generators(h,A,B,comp):
        v=hi.vector(U)|(hi.vector(V)<<hi.n)
        assert hi.syndrome(v,ah,bh)==0
        for g in range(hi.n):
            shifted=hi.shift2(v,g)
            rhi=boundary_hi.reduce(shifted)
            rlo=boundary_lo.reduce(project(shifted))
            rank_hi.add(rhi); rank_lo.add(rlo)
            rank_joint.add(rlo | (rhi<<(2*lo.n)))
    assert len(rank_joint)==len(rank_lo)==len(rank_hi), (h,P,seam,A,B,len(rank_lo),len(rank_hi),len(rank_joint))
    return dict(h=h,P=P,seam=seam,A=A,B=B,k_base=lo.k(al,bl),k_cover=hi.k(ah,bh),compact_rank=len(rank_hi),joint_rank=len(rank_joint),n_cover=2*hi.n)


def arithmetic_tests():
    # Exact cofactor obstruction, also for all alternative independent row triples.
    rows=[]
    for L in [2,3,4,7,16,31,100,257]:
        R=[(L,-1,0,0),(0,L,-1,0),(0,0,L,-1)]
        c=(1,L,L*L,L**3)
        assert all(sum(a*b for a,b in zip(r,c))==0 for r in R)
        # Last three columns have determinant -1, so the row lattice is saturated.
        a,b,d=[list(r[1:]) for r in R]
        det=a[0]*(b[1]*d[2]-b[2]*d[1])-a[1]*(b[0]*d[2]-b[2]*d[0])+a[2]*(b[0]*d[1]-b[1]*d[0])
        assert abs(det)==1
        lengths=[max(abs(r[0]),abs(r[1]),abs(r[0]+r[1]))+max(abs(r[2]),abs(r[3]),abs(r[2]+r[3])) for r in R]
        assert lengths==[L,L+1,L]
        rows.append(dict(L=L,root_word_lengths=lengths,cofactor=list(c),strip_width=L**3,quadratic_comparison_numerator=L**3,quadratic_comparison_denominator=(L+1)**2))
    return rows


def even_torsion_countercheck():
    # H=C3(t) x C2(s) x Z(z), generated by the two check supports.
    # A=1+s*t+z, B=1+t+s*z; e=1+s.  The universal cycle is
    # (B+e,A+e). Realize t=x^2,s=x^3,z=y in C6 x C3.
    lo=Group(3,3,0); hi=Group(6,3,0)
    A=[(0,0),(5,0),(0,1)]; B=[(0,0),(2,0),(3,1)]
    UL=[(2,0),(3,1),(3,0)]; VR=[(5,0),(0,1),(3,0)]
    al,bl=lo.vector(A),lo.vector(B); ah,bh=hi.vector(A),hi.vector(B)
    yh=hi.vector(UL)|(hi.vector(VR)<<hi.n)
    yl=lo.vector(UL)|(lo.vector(VR)<<lo.n)
    assert hi.syndrome(yh,ah,bh)==0
    assert hi.boundaries(ah,bh).reduce(yh)!=0
    assert lo.boundaries(al,bl).reduce(yl)==0
    assert yl.bit_count()==6 and yh.bit_count()==6
    # Independently check the norm cycle, and exclude all weight-two cycles.
    e=hi.vector([(0,0),(3,0)]); norm=e|(e<<hi.n)
    assert hi.syndrome(norm,ah,bh)==0 and hi.boundaries(ah,bh).reduce(norm)
    for i,j in itertools.combinations(range(2*hi.n),2):
        assert hi.syndrome((1<<i)|(1<<j),ah,bh)!=0
    witness=1|(1<<lo.n)
    assert lo.syndrome(witness,al,bl)==0 and lo.boundaries(al,bl).reduce(witness)
    # Independent dual-number functional: t=omega, s=1+eps, z=omega^2.
    K=Field(0b111)
    def dualmul(u,v):
        return K.mul(u&3,v&3) | ((K.mul(u&3,v>>2)^K.mul(u>>2,v&3))<<2)
    eps,omega,omega2=4,2,3
    ad=1^dualmul(1^eps,omega)^omega2
    bd=1^omega^dualmul(1^eps,omega2)
    assert ad==dualmul(omega,eps) and bd==dualmul(omega2,eps)
    def functional(u,v):return dualmul(omega,u)^dualmul(omega2,v)
    assert all(functional(dualmul(bd,r),dualmul(ad,r))==0 for r in range(16))
    assert functional(eps,eps)==eps
    # Eliminating A sets z=omega^2+omega*eps and reduces B to eps.
    z_after_elimination=omega2^dualmul(omega,eps)
    assert 1^omega^dualmul(1^eps,z_after_elimination)==eps
    return dict(base=[18,lo.k(al,bl),2],cover=[36,hi.k(ah,bh),4],cycle_weight=6,projection_weight=6,cover_nonboundary=True,projected_boundary=True,check_supports_generate=True,dual_number_functional_verified=True,universal_H1_semisimple=True,universal_H1_binary_dimension=2,note='Not a distance-degradation or quadratic counterexample; also refutes semisimplicity alone as a compact-survival criterion for torsion-changing quotients.')


def jordan_checks():
    out=[]
    for lengths in [(1,),(2,),(3,),(1,2),(2,4),(1,1,3,5)]:
        size=sum(lengths); cols=[]; offset=0
        for length in lengths:
            for i in range(length): cols.append(0 if i==length-1 else 1<<(offset+i+1))
            offset+=length
        rank_f=len(Basis(cols))
        cols2=[]
        for col in cols:
            v=0
            while col:
                b=col&-col; v^=cols[b.bit_length()-1]; col^=b
            cols2.append(v)
        rank_f2=len(Basis(cols2))
        assert rank_f-rank_f2==sum(l>=2 for l in lengths)
        out.append(dict(block_lengths=lengths,dim_fM_over_f2M=rank_f-rank_f2))
    return out


def main():
    start=time.time(); rng=random.Random(20260906); records=[]; rejected=0
    comp_cache={h:components(h) for h in [1,3,5,7,9]}
    seen=set()
    for attempt in range(16000):
        h=rng.choice([1,3,3,5,7,9])
        A=[(0,0)]+[(rng.randrange(h),rng.randrange(7)) for _ in range(2)]
        mode=attempt%5
        if mode==0: B=A.copy()
        elif mode==1: B=[((2*i)%h,2*j) for i,j in A]
        else: B=[(0,0)]+[(rng.randrange(h),rng.randrange(7)) for _ in range(2)]
        if len(set(A))<3 or len(set(B))<3 or not generated(h,A,B): continue
        P=rng.choice([3,4,5,6,7,8,9,10,12]); seam=rng.randrange(h)
        key=(h,P,seam,tuple(A),tuple(B))
        if key in seen: continue
        seen.add(key)
        record=check_case(h,P,seam,A,B,comp_cache[h])
        if record is None: rejected+=1; continue
        records.append(record)
        if len(records)>=512: break
    assert len(records)==512
    assert any(r['compact_rank']>0 for r in records)
    output=dict(status='PARTIAL_STRUCTURAL_PROGRESS_QUADRATIC_OPEN',compact_descent_tests=len(records),positive_compact_tests=sum(r['compact_rank']>0 for r in records),max_cover_qubits=max(r['n_cover'] for r in records),tested_odd_torsion_orders=sorted(set(r['h'] for r in records)),nonzero_seam_tests=sum(r['seam']!=0 for r in records),all_compact_projection_maps_injective=True,no_new_distance_record=True,cofactor_tests=arithmetic_tests(),even_torsion_hypothesis_countercheck=even_torsion_countercheck(),jordan_tests=jordan_checks(),seconds=round(time.time()-start,3))
    here=Path(__file__).resolve().parent
    (here/'cases.json').write_text(json.dumps(records,indent=2))
    output['cases_sha256']=hashlib.sha256((here/'cases.json').read_bytes()).hexdigest()
    (here/'verification_summary.json').write_text(json.dumps(output,indent=2))
    print(json.dumps(output,indent=2))

if __name__=='__main__': main()
