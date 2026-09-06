"""Independent finite-dimensional checks of the faithful generic B-evaluation.
The target is a twisted finite group, with polynomial coefficients in an
indeterminate. No finite-field specialization is used in this script.
"""
from pathlib import Path
import json, random

def pmul(a,b):
    out=0
    while b:
        bit=b&-b;out^=a<<(bit.bit_length()-1);b^=bit
    return out

def ppow(a,n):
    out=1
    while n:
        if n&1:out=pmul(out,a)
        a=pmul(a,a);n//=2
    return out

def rank_binary(vectors):
    piv={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p not in piv:piv[p]=v;break
            v^=piv[p]
    return len(piv)

class Eval:
    def __init__(self,M,m,j,q):self.M=M;self.m=m;self.j=j;self.q=q
    def source(self,x,y,t,w):return (x,y,t%self.M,w%self.m)
    def plus(self,a,b):return self.source(*(x+y for x,y in zip(a,b)))
    def target(self,a,b):
        # b^(qm)=a^(j qm), a^(qM)=1.
        carry,b=divmod(b,self.q*self.m)
        return ((a+carry*self.j*self.q*self.m)%(self.q*self.M),b)
    def mon_image(self,z):
        x,y,t,w=z
        return self.target(x-self.q*t+self.q*self.j*w,y-self.q*w),pmul(1<<x,ppow(3,y))
    def image(self,poly):
        out={}
        for z in poly:
            g,c=self.mon_image(z);out[g]=out.get(g,0)^c
            if out[g]==0:del out[g]
        return out
    def multiply(self,a,b):
        out=set()
        for x in a:
            for y in b:
                z=self.plus(x,y)
                if z in out:out.remove(z)
                else:out.add(z)
        return out
    def checks(self):
        return {self.source(0,0,0,0),self.source(self.q,0,1,0),self.source(0,self.q,self.j,1)}
    def remainder(self,poly):
        rem=set(poly)
        while rem:
            y=max(z[1] for z in rem)
            if y<self.q:break
            for z in [z for z in rem if z[1]==y]:
                x,_,t,w=z
                f=self.source(x,y-self.q,t-self.j,w-1)
                rem ^= self.multiply({f},self.checks())
        return rem

def main():
    rng=random.Random(202609060404);records=[];random_cases=0
    for M,m,j,q in [(1,1,0,2),(1,1,0,4),(2,1,0,1),(2,2,0,2),
                    (4,1,3,2),(4,2,1,2),(4,4,3,1),(8,2,3,2)]:
        E=Eval(M,m,j,q);assert not E.image(E.checks())
        width=q+6;vectors=[]
        for x in range(5):
            for y in range(q):
                for t in range(M):
                    for w in range(m):
                        g,c=E.mon_image((x,y,t,w));index=g[0]*(q*m)+g[1]
                        vectors.append(c<<(index*width))
        assert rank_binary(vectors)==len(vectors)
        for _ in range(80):
            f={E.source(rng.randrange(7),rng.randrange(q*3+1),rng.randrange(M),rng.randrange(m)) for _ in range(10)}
            remainder=E.remainder(f)
            assert (not E.image(f))==(not remainder)
            assert E.image(f)==E.image(remainder)
            assert not E.image(E.multiply(f,E.checks()))
            random_cases+=1
        records.append({'M':M,'m':m,'j':j,'q':q,'independent_normal_monomials':len(vectors)})
    out={'status':'all generic evaluation checks passed','records':records,'random_polynomials':random_cases,
         'scope':'Bounded exact tests of kernel(B) and normal-form injectivity, supplementing the symbolic coset proof.'}
    Path(__file__).with_name('embedding_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
