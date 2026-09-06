#!/usr/bin/env python3
"""Independent matrix verification: no finite-field gcds or CRT.

Find all cycles in a sufficiently large *universal* finite z-window by
binary nullspace elimination. Translate their finite images and compare
raw rank increments modulo the boundary columns, using low pivots.
"""
from __future__ import annotations
import json,time,itertools,hashlib
from pathlib import Path

class LowBasis:
    def __init__(self, cols=()):
        self.b={}
        for x in cols:self.add(x)
    def add(self,x):
        while x:
            p=(x&-x).bit_length()-1
            if p in self.b:x^=self.b[p]
            else:self.b[p]=x;return True
        return False
    def __len__(self):return len(self.b)

def nullspace(columns):
    piv={}; out=[]
    for j,x in enumerate(columns):
        coeff=1<<j
        while x:
            p=(x&-x).bit_length()-1
            if p in piv:
                y,c=piv[p];x^=y;coeff^=c
            else:
                piv[p]=(x,coeff);break
        if not x:out.append(coeff)
    return out

def finite_data(h,P,seam,A,B):
    n=h*P
    def idx(i,j):
        q,r=divmod(j,P)
        return ((i+q*seam)%h)*P+r
    def vec(terms):
        x=0
        for i,j in terms:x^=1<<idx(i,j)
        return x
    def shift(x,i,j):
        out=0
        while x:
            bit=x&-x;pos=bit.bit_length()-1;block,pos=divmod(pos,n);ti,zj=divmod(pos,P)
            out^=1<<(block*n+idx(ti+i,zj+j));x^=bit
        return out
    boundaries=[vec([(ti+i,zj+j) for ti,zj in B]) | (vec([(ti+i,zj+j) for ti,zj in A])<<n) for i in range(h) for j in range(P)]
    return n,vec,shift,boundaries

def verify_case(r):
    h,P,seam,A,B=r['h'],r['P'],r['seam'],r['A'],r['B']
    D=max(j for i,j in A+B)
    window=D+1; syndrome_window=2*D+1
    columns=[]
    for check in [A,B]:
        for ti in range(h):
            for zj in range(window):
                col=0
                for a,b in check:col^=1<<(((ti+a)%h)*syndrome_window+zj+b)
                columns.append(col)
    kernel=nullspace(columns)
    # Assert the nullspace vectors independently by direct column XOR.
    for c in kernel:
        x=0
        while c:
            bit=c&-c;x^=columns[bit.bit_length()-1];c^=bit
        assert x==0
    measured=[]
    for pp,ss in [(P,seam),(2*P,2*seam)]:
        n,vec,shift,bounds=finite_data(h,pp,ss,A,B)
        span=LowBasis(bounds); rank_boundary=len(span)
        assert 2*(n-rank_boundary)==r['k_base' if pp==P else 'k_cover']
        for c in kernel:
            parts=[[],[]]
            while c:
                bit=c&-c;pos=bit.bit_length()-1;block,pos=divmod(pos,h*window);ti,zj=divmod(pos,window)
                parts[block].append((ti,zj));c^=bit
            image=vec(parts[0])|(vec(parts[1])<<n)
            # t-translates already lie in the universal window kernel.
            for j in range(pp):span.add(shift(image,0,j))
        measured.append(len(span)-rank_boundary)
    assert measured==[r['compact_rank'],r['compact_rank']], (r,measured)
    return len(kernel)

def main():
    here=Path(__file__).resolve().parent;start=time.time()
    records=json.loads((here/'cases.json').read_text())
    dimensions=[verify_case(r) for r in records]
    output=dict(independent_cases=len(records),method='Universal-window nullspaces; low-pivot raw rank increments; no finite-field gcds or CRT',all_agree=True,max_universal_kernel_dimension=max(dimensions),seconds=round(time.time()-start,3),cases_sha256=hashlib.sha256((here/'cases.json').read_bytes()).hexdigest())
    (here/'independent_verification.json').write_text(json.dumps(output,indent=2))
    print(json.dumps(output,indent=2))
if __name__=='__main__':main()
