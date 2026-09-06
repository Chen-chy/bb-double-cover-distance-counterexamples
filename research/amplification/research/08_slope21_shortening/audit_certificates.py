#!/usr/bin/env python3
"""Independently audit exact compact-distance certificates.

This does not run the shortest-path generator. It checks a finite sublevel
closure under every possible input, plus a primal word. All Laurent lengths
are covered: there is no bound on the number of trellis steps.
Only the Python standard library is used.
"""
from __future__ import annotations
from pathlib import Path
import hashlib
import json
import struct
import time

ROOT = Path(__file__).resolve().parent

def pmul(a: int, b: int) -> int:
    out = 0
    while b:
        if b & 1:
            out ^= a
        a <<= 1
        b >>= 1
    return out

def pdiv(a: int, b: int) -> tuple[int, int]:
    if not b:
        raise ZeroDivisionError
    q = 0
    while a and a.bit_length() >= b.bit_length():
        shift = a.bit_length() - b.bit_length()
        q ^= 1 << shift
        a ^= b << shift
    return q, a

def pmod(a: int, b: int) -> int:
    return pdiv(a, b)[1]

def inverse(a: int, modulus: int) -> int:
    r0, r1, s0, s1 = modulus, a, 0, 1
    while r1:
        q, r = pdiv(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, s0 ^ pmul(q, s1)
    if r0 != 1:
        raise ValueError('No polynomial inverse')
    return pmod(s0, modulus)

def poly(positions: list[int]) -> int:
    out = 0
    if len(set(positions)) != len(positions) or any(p < 0 for p in positions):
        raise ValueError('Bad primal support')
    for p in positions:
        out ^= 1 << p
    return out

def interleave(p0: int, p1: int, sheets: int) -> int:
    if sheets == 1:
        assert p1 == 0
        return p0
    out = 0
    for sheet, p in enumerate((p0, p1)):
        i = 0
        while p:
            if p & 1:
                out ^= 1 << (2*i+sheet)
            p >>= 1
            i += 1
    return out

def audit_word(case: dict) -> dict:
    coords = [poly(p) for p in case['result']['physical']]
    A0, A1, B0, B1 = (case[k] for k in ('A0', 'A1', 'B0', 'B1'))
    if case['kind'] == 'base':
        u, v = coords
        assert pmul(A0, u) ^ pmul(B0, v) == 0
        label = pmul(case['coef0'], v)
    else:
        u0, u1, v0, v1 = coords
        assert pmul(A0,u0)^pmul(A1,u1)^pmul(B0,v0)^pmul(B1,v1)==0
        assert pmul(A1,u0)^pmul(A0,u1)^pmul(B1,v0)^pmul(B0,v1)==0
        # Verify intrinsic compact-coordinate conditions without relying on
        # the supplied reduced label coefficients.
        W = ((v0 ^ v1) << 8) ^ (pmul(49, v1) << 4)
        coordinate, rem = pdiv(W, 11)
        assert rem == 0
        assert pmod(coordinate, 7) != 0
        if case['name'] == 'cover_resonant_purified':
            assert pmod(coordinate, 11) == 0
        label = pmul(case['coef0'],v0)^pmul(case['coef1'],v1)
    assert pmod(label,case['target']) != 0
    assert pmod(label,case['kill']) == 0
    weight = sum(c.bit_count() for c in coords)
    assert weight == case['expect'] == case['result']['distance']
    return {'weight':weight,'exact_cycle':True,'exact_label':True}

def audit(case: dict) -> dict:
    start=time.perf_counter()
    assert case['result']['certified'] and not case['result']['capped']
    W=case['expect']
    path=ROOT/case['certificate']
    data=path.read_bytes()
    assert hashlib.sha256(data).hexdigest()==case['sha256']
    assert data[:8]==b'BBSL21C1'
    count=struct.unpack_from('<Q',data,8)[0]
    assert len(data)==16+10*count
    rows=list(struct.iter_unpack('<QH',data[16:]))
    assert rows==sorted(rows) and len({s for s,d in rows})==count
    dist=dict(rows)
    assert dist[0]==0 and all(0<=d<W for d in dist.values())
    sheets=1 if case['kind']=='base' else 2
    D=max(case[k].bit_length()-1 for k in ('A0','A1','B0','B1'))
    assert D==case['result']['D']
    shift=sheets*D; mask=(1<<shift)-1
    A=[interleave(case['A0'],case['A1'],sheets)]
    B=[interleave(case['B0'],case['B1'],sheets)]
    if sheets==2:
        A.append(interleave(case['A1'],case['A0'],sheets))
        B.append(interleave(case['B1'],case['B0'],sheets))
    def column(bitmask: int, cols: list[int])->int:
        v=0
        for i,col in enumerate(cols):
            if bitmask>>i&1: v^=col
        return v
    columnsA=[column(x,A) for x in range(1<<sheets)]
    columnsB=[column(x,B) for x in range(1<<sheets)]
    lowmask=(1<<sheets)-1
    lowest_to_u={a&lowmask:i for i,a in enumerate(columnsA)}
    assert len(lowest_to_u)==1<<sheets
    modulus=case['mod']; bits=modulus.bit_length()-1
    invz=inverse(2,modulus)
    multiply_inverse=[pmod(pmul(l,invz),modulus) for l in range(1<<bits)]
    labeladdition=[]
    for right in range(1<<sheets):
        v=case['coef0'] if right&1 else 0
        if right&2:v^=case['coef1']
        assert 0<=v<1<<bits
        labeladdition.append(v)
    checked=0; required=0
    for state,d in rows:
        syndrome=state&mask;label=state>>shift
        assert 0<=label<1<<bits
        assert not(syndrome==0 and pmod(label,case['target'])!=0
                   and pmod(label,case['kill'])==0)
        for right,bc in enumerate(columnsB):
            left=lowest_to_u[(syndrome^bc)&lowmask]
            newcost=d+right.bit_count()+left.bit_count()
            checked+=1
            if newcost>=W:continue
            new_syndrome=(syndrome^bc^columnsA[left])>>sheets
            assert new_syndrome<=mask
            new_label=multiply_inverse[label^labeladdition[right]]
            destination=new_syndrome|(new_label<<shift)
            assert destination in dist, (case['name'],state,right,'missing')
            assert dist[destination]<=newcost
            required+=1
    word=audit_word(case)
    return {'name':case['name'],'minimum':W,'closure_states':count,
            'transitions_checked':checked,'subthreshold_transitions':required,
            'primal':word,'seconds':time.perf_counter()-start}

def main()->None:
    # Independent reconstruction of the label polynomials used in the last case.
    e,j=7,11
    M=pmul(e,pmul(j,j))
    assert M==475
    assert pmod(1<<8,M)==219
    assert pmod((1<<8)^(49<<4),M)==125
    cases=json.loads((ROOT/'exact_results.json').read_text())
    results=[]
    for case in cases:
        result=audit(case);results.append(result)
        print(json.dumps(result),flush=True)
    (ROOT/'independent_audit.json').write_text(json.dumps(results,indent=2)+'\n')
if __name__=='__main__':main()
