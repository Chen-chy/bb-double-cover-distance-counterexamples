#!/usr/bin/env python3
"""Independent bit-polynomial audit of the exact full-optimization norm form."""
import json,random
from pathlib import Path

def mul(a,b):
    ans=0
    while b:
        if b&1:ans ^=a
        b>>=1;a<<=1
    return ans

def divmodp(a,b):
    q=0
    while a and a.bit_length()>=b.bit_length():
        j=a.bit_length()-b.bit_length();q ^=1<<j;a ^=b<<j
    return q,a

def exact(a,b):
    q,r=divmodp(a,b)
    assert not r
    return q

rng=random.Random(40961);count=0
for j in range(16):
    A=7;B=1^(1<<(12*j+8))^(1<<(18*j+13));b=exact(B,A);P=exact(b^1,A)
    for _ in range(30):
        F=rng.getrandbits(50);H=rng.getrandbits(60);k=F^mul(A,H)
        y=[mul(mul(A^1,P)^1,k)^mul(B^1,H),mul(P,k)^H,k^mul(A^1,H),H]
        alt=[mul(b^P,F)^mul(b,H),mul(P,F)^mul(b,H),F^H,H]
        assert y==alt
        bf=mul(b,F);x=mul(P,F)^mul(b,H)
        assert sum(a.bit_count()for a in y)==bf.bit_count()+F.bit_count()+2*((x&~bf).bit_count()+(H&~F).bit_count())
        assert divmodp(k,A)[1]==divmodp(F,A)[1]
        count+=1
path=Path(__file__).with_name('verification_summary.json')
summary=json.loads(path.read_text())
summary['independent_bit_polynomial_checks']={'systematic_unimodular_change_and_exact_norm':count}
path.write_text(json.dumps(summary,indent=2)+'\n')
print('Independent systematic/norm checks passed:',count)
