"""Exact sparse Laurent/group-polynomial checks for the compact-distance formula.
No symbolic-algebra package and no distance-search cutoff is used.
"""
from itertools import product
from pathlib import Path
import json

class Ring:
    def __init__(self,M,m,o=1,p=1):self.mods=(M,m,o,p);self.zero=(0,0,0,0,0,0)
    def mon(self,x=0,y=0,t=0,w=0,c=0,d=0):
        return (x,y,t%self.mods[0],w%self.mods[1],c%self.mods[2],d%self.mods[3])
    def addg(self,a,b):return self.mon(*(x+y for x,y in zip(a,b)))
    def mul(self,a,b):
        out=set()
        for x in a:
            for y in b:
                z=self.addg(x,y)
                if z in out:out.remove(z)
                else:out.add(z)
        return out
    def power(self,a,n):
        out={self.zero}
        while n:
            if n&1:out=self.mul(out,a)
            a=self.mul(a,a);n//=2
        return out
    def shift(self,a,x=0,y=0):return {self.addg(z,self.mon(x=x,y=y)) for z in a}
    def div_A(self,a):
        # Divide by Y+(1+X), with group-ring coefficients in X and torsion.
        rem=set(a);out=set()
        while rem:
            degree=max(z[1] for z in rem)
            if degree==0:break
            lead=[z for z in rem if z[1]==degree]
            for z in lead:
                q=(z[0],z[1]-1,*z[2:])
                if q in out:out.remove(q)
                else:out.add(q)
                for v in (self.zero,self.mon(x=1),self.mon(y=1)):
                    w=self.addg(q,v)
                    if w in rem:rem.remove(w)
                    else:rem.add(w)
        return out,rem

def check(M,m,j,q,o=1,p=1):
    R=Ring(M,m,o,p)
    A={R.zero,R.mon(x=1),R.mon(y=1)}
    B={R.zero,R.mon(x=q,t=1,c=1),R.mon(y=q,t=j,w=1,d=1)}
    e={R.mon(c=a,d=b) for a in range(o) for b in range(p)}
    N={R.mon(t=m*i) for i in range(M//m)}
    E=R.mul(e,N)
    U=R.mul(E,R.power(A,q*m-1));V=R.mul(E,R.power(B,m-1))
    assert not (R.mul(A,U)^R.mul(B,V))
    b=m.bit_length()-1;s=q.bit_length()-1
    dv=o*p*(M//m)*3**b;du=3**s*dv
    assert (len(U),len(V))==(du,dv)
    # The optimized word is a monomial-unit multiple of the old canonical
    # generator modulo an explicitly reconstructed universal boundary.
    CU=R.mul(e,R.power(A,q*M-1));CV=R.mul(e,R.power(B,M-1))
    exponent=q*(M-m) if j%2==0 else 0
    f,rem=R.div_A(CV^R.shift(V,x=exponent))
    assert not rem
    assert R.mul(B,f)==(CU^R.shift(U,x=exponent))
    return dict(M=M,m=m,j=j,q=q,odd_factors=[o,p],u_weight=du,v_weight=dv,
                compact_distance=du+dv,canonical_weight=len(CU)+len(CV),
                boundary_adjustment_weight=len(f),generator_unit_X_power=exponent)

def main():
    rows=[]
    for M in (1,2,4,8,16):
        for m in (1,2,4,8,16):
            if m>M:continue
            for j in sorted({0,1%M,(M-1)%M}):
                for q in (1,2,4):
                    if q*M>32:continue
                    rows.append(check(M,m,j,q))
    for args in [(1,1,0,1,3,1),(2,1,1,2,3,1),(4,2,2,2,3,1),
                 (4,4,1,1,3,3),(8,2,3,2,3,1),(2,2,0,4,5,1)]:
        rows.append(check(*args))
    out={'status':'all exact sparse identities passed','cases':len(rows),'records':rows,
         'scope':'Cycle, exact universal weight, and explicit boundary equality; not finite-code distance searches.'}
    Path(__file__).with_name('sparse_generator_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))
if __name__=='__main__':main()
