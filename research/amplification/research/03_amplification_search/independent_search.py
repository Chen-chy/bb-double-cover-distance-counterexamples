"""Independent Python circuit exclusion with a polynomial, not matrix, oracle."""
from pathlib import Path
import json,time
from algebra import poly,support
ROOT=Path(__file__).resolve().parent

def mul(a,b):
    r=0
    while b:
        bit=b&-b;r^=a<<(bit.bit_length()-1);b^=bit
    return r

def divmodp(a,b):
    if not b:raise ZeroDivisionError
    q=0
    while a.bit_length()>=b.bit_length():
        d=a.bit_length()-b.bit_length();q^=1<<d;a^=b<<d
    return q,a

def gcd(a,b):
    while b:a,b=b,divmodp(a,b)[1]
    return a

def egcd(a,b):
    r,s,t,u=1,0,0,1
    while b:
        q,z=divmodp(a,b);a,b=b,z;r,s=s,r^mul(q,s);t,u=u,t^mul(q,u)
    return a,r,t

def run(L,aa,bb,bound):
    A,B=poly(aa),poly(bb);F=(1<<L)|1;mask=(1<<L)-1
    c=gcd(A,B);a=divmodp(A,c)[0];b=divmodp(B,c)[0];one,r,s=egcd(a,b);assert one==1
    g=gcd(c,F)
    def rotate(v,j):return ((v<<j)&mask)^(v>>(L-j)) if j else v
    cols=[rotate(C,j) for C in (A,B) for j in range(L)]
    inc=[0]*L
    for j,col in enumerate(cols):
        for i in support(col):inc[i]|=1<<j
    maxweight=max(x.bit_count() for x in cols);nodes=closed=0;witness=None
    def nonboundary(w):
        u,v=w&mask,w>>L
        q=divmodp(mul(a,u)^mul(b,v),F)[1]
        rr=divmodp(mul(s,u)^mul(r,v),g)[1]
        return bool(q or rr)
    def dfs(word,syndrome,allowed,weight):
        nonlocal nodes,closed,witness
        nodes+=1
        if not syndrome:
            closed+=1
            if nonboundary(word):witness=word;return True
            return False
        left=bound-weight
        if left<=0 or syndrome.bit_count()>maxweight*left:return False
        # Independent implementation of the odd-row neighborhood packing.
        rem=syndrome;pack=0
        while rem:
            row=rem.bit_length()-1;rem^=1<<row;pack+=1
            if pack>left:return False
            cs=inc[row]&allowed
            for col in support(cs):rem&=~cols[col]
        choices=None;best=2*L+1
        for row in reversed(support(syndrome)):
            cs=inc[row]&allowed;w=cs.bit_count()
            if w==0:return False
            if w<best:choices=cs;best=w
        while choices:
            col=choices.bit_length()-1;bit=1<<col;choices^=bit;allowed&=~bit
            if dfs(word|bit,syndrome^cols[col],allowed,weight+1):return True
        return False
    start=time.time();allbits=(1<<(2*L))-1
    for root in (0,L):
        allowed=allbits^(1<<root)
        if root==L:allowed&=~mask
        if dfs(1<<root,cols[root],allowed,1):break
    out=dict(L=L,A=aa,B=bb,k=2*(g.bit_length()-1),bound=bound,found=witness is not None,nodes=nodes,closed=closed,seconds=time.time()-start)
    if witness is not None:out.update(weight=witness.bit_count(),u=support(witness&mask),v=support(witness>>L))
    return out

if __name__=='__main__':
    out=[]
    for L,A,B,bound in [(39,[0,8,25],[0,2,13],4),(78,[0,8,25],[0,2,13],12),(39,[0,5,28],[14,22,26,28],8)]:
        r=run(L,A,B,bound);assert not r['found'];out.append(r);print(json.dumps(r),flush=True)
    (ROOT/'independent_exclusions.json').write_text(json.dumps(out,indent=2)+'\n')
