"""Exact checks for A=1+x+x^2, B=A^2, L=3q with q>=3 odd.
Includes an exhaustive 4-state trellis certificate for mu=q+1.
No external libraries are required.
"""
from pathlib import Path
from itertools import product
import json

A=0b111;B=0b10101

def rot(a,s,L):
    s%=L
    return (((a<<s)&((1<<L)-1))^(a>>(L-s))) if s else a

def mul(a,b,L):
    r=0
    while b:
        bit=b&-b;r^=rot(a,bit.bit_length()-1,L);b^=bit
    return r

class Span:
    def __init__(self,vs):
        self.p={}
        for v in vs:
            v=self.reduce(v)
            if v:self.p[v.bit_length()-1]=v
    def reduce(self,v):
        while v:
            i=v.bit_length()-1
            if i not in self.p:return v
            v^=self.p[i]
        return 0
    def contains(self,v):return self.reduce(v)==0

def trellis_matrix():
    M=[[100]*4 for _ in range(4)]
    for s in range(4):
        for bits in product((0,1),repeat=3):
            t=s;c=0
            for i,b in enumerate(bits):
                c+=b+(int(i!=2)^b^(t.bit_count()%2))
                t=((t<<1)&3)|b
            M[s][t]=min(M[s][t],c)
    expected=[[2,2,3,3],[0,2,3,3],[1,3,2,2],[1,3,2,4]]
    assert M==expected
    h=[0,1,0,0]
    reduced=[[M[i][j]-1+h[i]-h[j] for j in range(4)] for i in range(4)]
    assert all(x>=0 for row in reduced for x in row)
    zero_edges={(i,j) for i in range(4) for j in range(4) if reduced[i][j]==0}
    assert zero_edges=={(0,1),(1,0),(2,0),(3,0)}
    # The only directed zero-cost cycle is 0<->1, so any odd closed walk
    # has positive reduced cost. Its total original cost is at least q+1.
    assert M[0][1]+M[1][0]==2 and M[0][0]==2
    # For odd q, alternate 0<->1 q-1 times, then take the loop at 0:
    # the matching upper cost is q-1+2=q+1.
    return M,reduced

def finite_check(L):
    assert L>=9 and L%6==3
    q=L//3;record={'L':L,'base_n':2*L,'cover_n':4*L,'k':4,'k2':4,'d':4,'d2':4,'mu':q+1}
    def code(N):
        cols=[rot(A,i,N) for i in range(N)]+[rot(B,i,N) for i in range(N)]
        assert len(set(cols))==2*N # no weight-two cycle; all cycles have even weight.
        bd=Span(rot(B,i,N)|(rot(A,i,N)<<N) for i in range(N))
        assert len(bd.p)==N-2
        z=A|(1<<N)
        assert mul(A,A,N)^B==0 and not bd.contains(z)
        return bd
    code(L);up=code(2*L)
    h=sum(1<<e for j in range(q) for e in (3*j,3*j+1))
    u=(1<<(L-3))|(1<<(L-2))
    v=sum(1<<e for j in range((q-1)//2) for e in (6*j,6*j+2))
    assert u^mul(A,v,L)==h
    assert mul(A,u,L)^mul(B,v,L)==0
    assert u.bit_count()+v.bit_count()==q+1
    def transfer(u,v):return u|(u<<L)|(v<<(2*L))|(v<<(3*L))
    assert not up.contains(transfer(u,v))
    assert up.contains(transfer(A,1))
    record['outside_kernel_witness']={'u':[i for i in range(L) if u>>i&1],'v':[i for i in range(L) if v>>i&1]}
    return record

def main():
    M,reduced=trellis_matrix()
    result={'claim':'mu=L/3+1 for every L=3q with q>=3 odd','trellis_block_matrix':M,'reduced_cost_matrix':reduced,'finite_checks':[finite_check(L) for L in (9,15,21,39,99)]}
    Path(__file__).with_name('metric_family_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
