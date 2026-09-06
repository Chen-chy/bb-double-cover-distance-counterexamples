"""Exact small BB distances proving sharpness of compact factor two."""
from pathlib import Path
import json

def run(L,cover):
    N=3;n=L*N
    A=[0,3,1];B=[0,12,1] if cover else A[:]
    def shift(v,j):
        x,y=divmod(j,N)
        out=0
        for i in v:
            a,b=divmod(i,N);out^=1<<(((a+x)%L)*N+(b+y)%N)
        return out
    cols=[shift(A,j) for j in range(n)]+[shift(B,j) for j in range(n)]
    bd=[shift(B,j)|(shift(A,j)<<n) for j in range(n)]
    piv={}
    def red(v):
        for p in sorted(piv,reverse=True):
            if v>>p&1:v^=piv[p]
        return v
    for v in bd:
        v=red(v)
        if v:piv[v.bit_length()-1]=v
    u=1|(1<<9) if cover else 1
    z=u|(u<<n)
    syn=0
    for i in range(2*n):
        if z>>i&1:syn^=cols[i]
    assert not syn and red(z)
    assert all(c.bit_count()==3 for c in cols)
    # Odd cycles are impossible. No zero column exists. Cover has no
    # equal pair, so every cycle below the weight-four witness is excluded.
    if cover:assert len(set(cols))==2*n
    d=4 if cover else 2
    assert z.bit_count()==d
    k=2*(n-len(piv));assert k==4
    return {'periods':[L,N],'n':2*n,'k':k,'d':d,'A':A,'B':B,
            'logical_support':[i for i in range(2*n) if z>>i&1],
            'distinct_columns':len(set(cols)),
            'lower_certificate':'nonzero odd-weight columns; cover columns pairwise distinct'}

result={'base':run(3,False),'cover':run(6,True),'exact_ratio':2}
Path(__file__).with_name('sharpness_example.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
