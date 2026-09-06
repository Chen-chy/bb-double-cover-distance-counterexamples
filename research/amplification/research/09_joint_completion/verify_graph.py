"""Exact audits of the normal form and odd elimination.

The independent cost/cycle oracle here uses dictionary convolution and
explicit graph edges rather than the construction's sparse operations.
"""
from __future__ import annotations
from pathlib import Path
from itertools import product
import json
import random
from graph_completion import Resonance
from laurent import poly, add, mul, shift, divide, gcd, ONE

def xor(*sets):
    ans: dict[int, int] = {}
    for ss in sets:
        for x in ss:
            ans[x] = 1 - ans.get(x, 0)
    return {x for x, v in ans.items() if v}

def convolution(p, q):
    ans: dict[int, int] = {}
    for i in p:
        for j in q:
            ans[i + j] = 1 - ans.get(i + j, 0)
    return {x for x, v in ans.items() if v}

def explicit_edge_cost(alpha, beta, sigma, h, a, b):
    edge_cost = 0
    for bias, step in ((alpha, b), (beta, a)):
        indices = set(bias) | set(h) | {i + step for i in h}
        edge_cost += sum((i in bias) ^ (i in h) ^ (i - step in h) for i in indices)
    vertices = set(sigma) | set(h)
    return edge_cost + sum(((i in sigma) ^ (i in h)) + int(i in h) for i in vertices)

def main():
    rng = random.Random(20260906)
    configurations = [(1,-2,3),(1,1,3),(-1,-1,3),(-1,2,3),(5,2,7),(1,-2,6)]
    tests = odd_patterns = 0
    for args in configurations:
        code = Resonance(*args)
        assert code.e != ONE
        assert gcd(code.A, code.B) == mul(code.e, code.j)
        a,b = code.steps
        assert a % 2 == b % 2 == 1
        for _ in range(40):
            f = poly(i for i in range(-4,9) if rng.randrange(2))
            h = poly(i for i in range(-7,12) if rng.randrange(2))
            coords = code.physical(f,h)
            u0,u1,v0,v1 = coords
            A0=set(code.A)-{0};B0=set(code.B)-{0}
            assert not xor(convolution(A0,u0),u1,convolution(B0,v0),v1)
            assert not xor(convolution(A0,u1),u0,convolution(B0,v1),v0)
            alpha,beta,sigma = code.graph_data(f)
            cost = explicit_edge_cost(alpha,beta,sigma,set(h),a,b)
            assert cost == sum(map(len,coords)) == code.energy(f,h)
            # Exact curvature/source identity, independently evaluated.
            lhs=xor(alpha,{i+a for i in alpha},beta,{i+b for i in beta})
            assert lhs == {i-4*code.s-2*code.g for i in sigma}
            even=poly(i for i in range(-8,13,2) if rng.randrange(2))
            minimum,opt,votes=code.eliminate_odd(f,even)
            assert explicit_edge_cost(alpha,beta,sigma,set(opt),a,b)==minimum
            # Every odd variable is independent given even variables.
            for i,k in votes.items():
                flipped=set(opt);flipped.symmetric_difference_update((i,))
                delta=explicit_edge_cost(alpha,beta,sigma,flipped,a,b)-minimum
                assert delta==abs(6-2*k)
                odd_patterns += 1
            # Independent simultaneous flips add their individual costs.
            sites=list(votes)[:8]
            for bits in product((0,1),repeat=len(sites)):
                hh=set(opt);prediction=minimum
                for i,bit in zip(sites,bits):
                    if bit:
                        hh.symmetric_difference_update((i,));prediction+=abs(6-2*votes[i])
                assert explicit_edge_cost(alpha,beta,sigma,hh,a,b)==prediction
            tests+=1
    out={'normal_form_cases':tests,'independent_odd_vertex_tests':odd_patterns,
         'per_case_joint_odd_flips':'all subsets of up to eight odd vertices',
         'status':'all exact checks passed'}
    Path(__file__).with_name('graph_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
