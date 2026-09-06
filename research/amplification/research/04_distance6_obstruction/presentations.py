"""Exact arithmetic for Z^n modulo integer row relations."""
from math import prod

def diagonalize(rows):
    M=[r[:] for r in rows];m=len(M);n=len(M[0]);V=[[int(i==j)for j in range(n)]for i in range(n)]
    def swapcols(a,b):
        for R in (M,V):
            for row in R:row[a],row[b]=row[b],row[a]
    def addcol(j,k,q):
        for R in (M,V):
            for row in R:row[j]-=q*row[k]
    k=0
    while k<min(m,n):
        nz=[(abs(M[i][j]),i,j)for i in range(k,m)for j in range(k,n)if M[i][j]]
        if not nz:break
        _,i,j=min(nz);M[k],M[i]=M[i],M[k];swapcols(k,j)
        while True:
            restart=False
            for i in range(k+1,m):
                if M[i][k]:
                    q=M[i][k]//M[k][k];M[i]=[x-q*y for x,y in zip(M[i],M[k])]
                    if M[i][k]:M[k],M[i]=M[i],M[k];restart=True;break
            if restart:continue
            for j in range(k+1,n):
                if M[k][j]:
                    q=M[k][j]//M[k][k];addcol(j,k,q)
                    if M[k][j]:swapcols(k,j);restart=True;break
            if not restart:break
        if M[k][k]<0:M[k]=[-x for x in M[k]]
        k+=1
    assert all(M[i][j]==0 for i in range(m)for j in range(n)if i!=j)
    D=[M[i][i]for i in range(k)]
    return D,V

class Group:
    def __init__(self,rows):
        self.D,self.V=diagonalize(rows);self.n=len(rows[0]);self.rank=len(self.D);self.free=self.n-self.rank;self.torsion=prod(self.D)
        self.zero=(0,)*self.n
        assert all(self.red(r)==self.zero for r in rows)
    def red(self,x):
        y=[sum(x[i]*self.V[i][j]for i in range(self.n))for j in range(self.n)]
        return tuple(y[j]%self.D[j]if j<self.rank else y[j]for j in range(self.n))
    def add(self,x,y):return tuple((a+b)%self.D[j]if j<self.rank else a+b for j,(a,b)in enumerate(zip(x,y)))
    def neg(self,x):return tuple((-a)%self.D[j]if j<self.rank else -a for j,a in enumerate(x))
    def sub(self,x,y):return self.add(x,self.neg(y))
    def scale(self,x,s):return tuple((a*s)%self.D[j]if j<self.rank else a*s for j,a in enumerate(x))
    def unit(self,i):return self.red([int(j==i)for j in range(self.n)])
    def freecoord(self,x):return x[self.rank:]
    def order2(self,x):return x!=self.zero and self.add(x,x)==self.zero
    def equiv(self,P,Q,free=False):
        P=[self.freecoord(x)for x in P]if free else P;Q=[self.freecoord(x)for x in Q]if free else Q
        add=lambda x,y:tuple(a+b for a,b in zip(x,y))
        sub=lambda x,y:tuple(a-b for a,b in zip(x,y))
        if not free:add=self.add;sub=self.sub
        return any(sorted(add(x,sub(Q[0],p))for x in P)==sorted(Q)for p in P)

def gf2rank(vs):
    basis={}
    for v in vs:
        while v:
            k=v.bit_length()-1
            if k not in basis:basis[k]=v;break
            v^=basis[k]
    return len(basis)
