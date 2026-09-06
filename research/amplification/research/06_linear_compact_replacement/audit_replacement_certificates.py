"""Independent audit: rebuild cycles, all boundaries, dual separations, and
optimized generator images. Does not import construction or rank routines.
"""
from pathlib import Path
from math import gcd,lcm
import json

def positions(word):
    return [i for i in range(word.bit_length()) if (word>>i)&1]

def audit(record,prefix):
    up=prefix=='cover'
    L,N=record['cover_periods' if up else 'periods'];size=L*N
    def index(p):return (p[0]%L)*N+p[1]%N
    def coords(i):return divmod(i,N)
    def add(i,j):
        x,y=coords(i);a,b=coords(j)
        return ((x+a)%L)*N+(y+b)%N
    def scale(i,n):
        x,y=coords(i);return index((x*n,y*n))
    def order(i):
        x,y=coords(i);return lcm(L//gcd(L,x),N//gcd(N,y))
    def poly(indices):
        w=0
        for i in indices:w^=1<<i
        return w
    def multiply(a,b):
        out=0
        for i in positions(a):
            for j in positions(b):out^=1<<add(i,j)
        return out
    def power(a,n):
        out=1
        for _ in range(n):out=multiply(out,a)
        return out
    aa=record['cover_A' if up else 'A'];bb=record['cover_B' if up else 'B']
    assert len(aa)==len(set(aa))==len(bb)==len(set(bb))==3
    A,B=poly(aa),poly(bb)
    word=int(record[prefix+'_cycle'],16);dual=int(record[prefix+'_dual'],16)
    assert word>>(2*size)==0 and dual>>(2*size)==0
    mask=(1<<size)-1;u,v=word&mask,word>>size
    assert multiply(A,u)==multiply(B,v)
    rank_piv={}
    for j in range(size):
        bd=poly(add(i,j) for i in bb) | (poly(add(i,j) for i in aa)<<size)
        assert (bd&dual).bit_count()%2==0
        while bd:
            low=(bd&-bd).bit_length()-1
            if low not in rank_piv:rank_piv[low]=bd;break
            bd^=rank_piv[low]
    assert (word&dual).bit_count()%2==1
    assert record[prefix+'_k']==2*(size-len(rank_piv))
    # Independently reconstruct the optimized cycle from the finite images of
    # the universal torsion norms, retaining repeats modulo the finite periods.
    data=record[prefix+'_compact_data'];M,m=data['M'],data['m'];q=record['q']
    h=index(record[prefix+'_h']);k=index(record[prefix+'_k_torsion'])
    oddgens=[]
    for g in (h,k):
        n=order(g);two=n&-n;odd=n//two
        oddgens.append(0 if odd==1 else scale(g,two*pow(two,-1,odd)))
    odd={0}
    for g in oddgens:
        odd={add(v,scale(g,j)) for v in odd for j in range(order(g))}
    E=poly(odd);maxgen=index(data['max_generator'])
    norm=poly(scale(maxgen,m*j) for j in range(M//m))
    E=multiply(E,norm)
    assert u==multiply(E,power(A,q*m-1))
    assert v==multiply(E,power(B,m-1))
    predicted=data['odd_size']*(M//m)*3**(m.bit_length()-1)*(3**(q.bit_length()-1)+1)
    assert predicted==data['universal_weight'] and word.bit_count()<=predicted

def main():
    here=Path(__file__).parent
    rows=json.loads((here/'finite_replacement_certificates.json').read_text())
    for r in rows:
        l,m=r['periods'];L,M=r['cover_periods']
        assert (L,M) in ((2*l,m),(l,2*m))
        def project(i):x,y=divmod(i,M);return (x%l)*m+y%m
        assert sorted(map(project,r['cover_A']))==sorted(r['A'])
        assert sorted(map(project,r['cover_B']))==sorted(r['B'])
        for prefix in ('base','cover'):audit(r,prefix)
        b=r['base_compact_data']['universal_weight'];c=r['cover_compact_data']['universal_weight']
        assert 2*c in (2*b,3*b,4*b)
    out={'status':'all independent audits passed','pairs':len(rows),'primal_dual_certificates':2*len(rows),
         'checks':'term matching, exact cycles, every boundary, dual separation, independent rank, optimized norm formula'}
    (here/'finite_replacement_audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
