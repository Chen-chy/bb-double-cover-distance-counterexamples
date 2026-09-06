"""Exact square-free decomposition tests, independent of the local-chain matrices."""
import json,random,time
from collections import Counter

def mul(a,b):
    c=0
    while b:
        if b&1:c ^= a
        a <<= 1;b >>= 1
    return c

def divmod2(a,b):
    assert b
    q=0
    while a.bit_length()>=b.bit_length():
        sh=a.bit_length()-b.bit_length();q ^= 1<<sh;a ^= b<<sh
    return q,a

def div(a,b):
    q,r=divmod2(a,b);assert not r;return q

def gcd(a,b):
    while b:a,b=b,divmod2(a,b)[1]
    return a

def derivative(f):
    return sum(1<<(i-1) for i in range(1,f.bit_length(),2) if (f>>i)&1)

def sqrt2(f):
    assert derivative(f)==0
    return sum(1<<i for i in range((f.bit_length()+1)//2) if (f>>(2*i))&1)

def sqf(f):
    if f==1:return []
    c=gcd(f,derivative(f));w=div(f,c);i=1;ans=[]
    while w!=1:
        y=gcd(w,c);z=div(w,y)
        if z!=1:ans.append((z,i))
        w=y;c=div(c,y);i+=1
    if c!=1:ans += [(g,2*j) for g,j in sqf(sqrt2(c))]
    return ans

def oneplus(n):
    # Lucas expansion of (1+x)^n.
    r=1
    bit=1
    while n:
        if n&1:r ^= r<<bit
        bit <<= 1;n >>= 1
    return r

def polynomial(a,b,c,d):
    # Clear negative monomial exponents; clearing does not affect roots other than 0,1.
    aa=-min(0,a,c);bb=-min(0,b,d)
    f=(oneplus(bb)<<aa) ^ (oneplus(b+bb)<<(a+aa)) ^ (oneplus(d+bb)<<(c+aa))
    if not f:return 0
    while not(f&1):f >>= 1
    while divmod2(f,3)[1]==0:f=div(f,3)
    return f

def run():
    start=time.time();rng=random.Random(940613);hist=Counter();zero=0;checked=0
    examples={}
    # All small nonnegative exponents, and a separate signed sample.
    exponents=[(a,b,c,d) for a in range(9) for b in range(9) for c in range(9) for d in range(9)]
    exponents += [tuple(rng.randrange(-96,97) for _ in range(4)) for _ in range(4096)]
    for a,b,c,d in exponents:
        f=polynomial(a,b,c,d)
        if not f:zero+=1;continue
        factors=sqf(f);reconstruct=1
        for g,m in factors:
            assert gcd(g,derivative(g))==1
            for _ in range(m):reconstruct=mul(reconstruct,g)
            assert m.bit_count()<=2,(a,b,c,d,m)
            hist[m]+=1;examples.setdefault(m,[a,b,c,d])
        assert reconstruct==f
        checked+=1
    sharp=[]
    for r in range(1,9):
        Q=1<<r
        # P_Q = 1+x^(3Q+1)+y^(3Q+1) for even r, or 1+x*y^(3Q)+y*x^(3Q) for odd r.
        if r%2==0:F=1 ^ (1<<(3*Q+1)) ^ oneplus(3*Q+1)
        else:F=1 ^ (oneplus(3*Q)<<1) ^ (3<<(3*Q))
        expected=mul(7<<(0),1) # p=x^2+x+1
        pQ=(1<<(2*Q))^(1<<Q)^1
        expected=mul(pQ,(1<<Q)^2^(r&1))
        assert F==expected
        m=0;ff=F
        while not divmod2(ff,7)[1]:ff=div(ff,7);m+=1
        assert m==Q+1
        sharp.append({'r':r,'Q':Q,'multiplicity_at_x2_x_1':m})
    ans={'exact_contact_cases':checked,'identically_zero_cases_excluded':zero,
         'multiplicities':dict(sorted(hist.items())),'examples_by_multiplicity':examples,
         'sharp_families':sharp,'all_binary_weights_at_most_two':True,
         'seconds':round(time.time()-start,3)}
    open('contact_verification.json','w').write(json.dumps(ans,indent=2));print(json.dumps(ans,indent=2))
if __name__=='__main__':run()
