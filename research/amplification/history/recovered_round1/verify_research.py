#!/usr/bin/env python3
"""Reproduce exact finite certificates and symbolic identities.

Requirements: Python 3.10+ and a C++17 compiler named g++.
No third-party Python packages, network, solver, random oracle, or heuristic
search cutoff is used. Randomness appears only in a deterministic selection
of small cross-check instances; their verification is exhaustive.
"""
from __future__ import annotations
import itertools
import json
from math import gcd as integer_gcd
from pathlib import Path
import random
import subprocess
from algebra import BB, poly, terms, mul, gcd, quo, mod, reduce
from independent_search import certify_seed

ROOT = Path(__file__).resolve().parent
EXE = ROOT / 'circuit_search'


def search(L: int, A: list[int], B: list[int], bound: int) -> dict:
    result = json.loads(subprocess.check_output(
        [str(EXE), str(L), *map(str, A + B), str(bound)], text=True))
    code = BB(L, poly(A), poly(B))
    assert result['k'] == code.k
    if result['found']:
        word = poly(result['u']) | (poly(result['v']) << L)
        assert code.logical(word)
        assert word.bit_count() == result['weight'] <= bound
    return result


def exact_pair(L: int, A: list[int], B: list[int], At: list[int], Bt: list[int],
               d: int, d2: int, label: str) -> dict:
    records = []
    for period, aa, bb, distance in ((L,A,B,d),(2*L,At,Bt,d2)):
        lower = search(period, aa, bb, distance-2)
        upper = search(period, aa, bb, distance)
        assert not lower['found'] and upper['found']
        assert upper['weight'] == distance
        records.append(dict(lower_exclusion=lower, upper_witness=upper))
    return dict(label=label, L=L, A=A, B=B, At=At, Bt=Bt,
                k=records[0]['upper_witness']['k'], d=d,
                k2=records[1]['upper_witness']['k'], d2=d2,
                classification='exact finite computation', certificates=records)


def symbolic_checks() -> dict:
    g, q = poly([0,1,2]), poly([0,2,3])
    a, b = poly([0,1,5]), poly([0,11,13])
    c = quo(b,a)
    E = (1<<13) ^ mul(2,c)
    assert a == mul(g,q)
    assert gcd(a,E) == g
    assert mod((1<<3)|1,g)==0 and mod((1<<7)|1,q)==0
    ub, vb = poly([0,1,5,10]), poly([0,2])
    assert mul(a,ub) == mul(b,vb)
    assert mod(vb,g) == 2
    # Pair coordinates are coefficients of 1 and s, where s^2=1.
    def smul(x: tuple[int,int], y: tuple[int,int]) -> tuple[int,int]:
        return (mul(x[0],y[0]) ^ mul(x[1],y[1]),
                mul(x[0],y[1]) ^ mul(x[1],y[0]))
    As, Bs = (poly([0,5]),2), (poly([0,11]),1<<13)
    U = (poly([1,4,6,8,10,11]),poly([0,3,7,8,9]))
    V = (0,q)
    assert smul(As,U) == smul(Bs,V)
    assert sum(v.bit_count() for v in U+V) == 14
    # h=(1+z^5)/z has residue 1 modulo g.
    assert mod(poly([0,5]),g) == mod(2,g)
    tested = []
    for j in (0,1,2,3,4,5,20,100):
        M, L = 42*j+13, 126*j+39
        r = 2*M-1
        assert integer_gcd(r,2*L)==1
        assert sorted([0,r,((L+5)*r)%(2*L)]) == [0,M-5,2*M-1]
        assert sorted([0,((L+11)*r)%(2*L),(13*r)%(2*L)]) == [0,M-11,2*M-13]
        assert gcd((1<<L)|1,mul(mul(g,g),q)) == g
        tested.append(j)
    # These checks illustrate, but do not replace, the uniform proofs in report.md.
    return dict(c=terms(c), E=terms(E), gcd_a_E=terms(g),
                strip_cycle_identity=True, base_cycle_identity=True,
                sample_relabeling_checks=tested)


def brute_crosschecks() -> int:
    rng = random.Random(20260905)
    count = 0
    for L in range(3,12):
        for _ in range(5):
            A = sorted(rng.sample(range(L),3))
            B = sorted(rng.sample(range(L),3))
            code = BB(L,poly(A),poly(B))
            found = False
            for weight in (2,4,6):
                for positions in itertools.combinations(range(2*L),weight):
                    syndrome = word = 0
                    for pos in positions:
                        syndrome ^= code.cols[pos]
                        word |= 1 << pos
                    if syndrome == 0 and reduce(word,code.bas):
                        found = True
                        break
                if found:
                    break
            assert search(L,A,B,6)['found'] == found
            count += 1
    return count


def main() -> None:
    subprocess.run(['g++','-O3','-std=c++17',str(ROOT/'circuit_search.cpp'),
                    '-o',str(EXE)],check=True)
    out = dict(symbolic_checks=symbolic_checks())
    seedA, seedB = [0,8,25], [0,2,13]
    out['seed'] = exact_pair(39,seedA,seedB,seedA,seedB,6,14,'original seed')
    out['second_family_member'] = exact_pair(
        165,[0,50,109],[0,44,97],[0,50,109],[0,44,97],6,14,'j=1')
    out['independent_python_exclusions'] = [certify_seed(39,4),certify_seed(78,12)]
    assert all(not result['found'] for result in out['independent_python_exclusions'])
    seed = BB(39,poly(seedA),poly(seedB))
    d, witnesses = seed.min_weight_upto6(first_only=False)
    assert d==6 and all(seed.logical(w) for w in witnesses)
    out['base_meet_in_middle'] = dict(distance=d, weight6_words=len(witnesses))
    upper = BB(78,poly(seedA),poly(seedB))
    u, v = poly([0,8,16,25]), poly([0,11])
    assert seed.logical(u | (v<<39))
    transferred = (u ^ (u<<39)) | ((v ^ (v<<39)) << 78)
    assert upper.cycle(transferred) and not upper.logical(transferred)
    out['seed_minimum_transfer_is_boundary'] = True
    templates = json.loads((ROOT/'template_results.json').read_text())
    out['template_examples'] = [exact_pair(r['L'],r['A'],r['B'],r['At'],r['Bt'],
                                           r['d'],r['d2'],f"template L={r['L']}")
                                for r in templates]
    extra = []
    for line in (ROOT/'random_progress.txt').read_text().splitlines():
        if line.startswith('{'):
            r = json.loads(line)
            extra.append(exact_pair(r['L'],r['A'],r['B'],r['A'],r['B'],6,14,
                                    'heuristically selected; distances exact'))
    out['additional_examples'] = extra
    out['small_brute_force_comparisons'] = brute_crosschecks()
    (ROOT/'verification_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(status='all checks passed',
                          template_examples=len(out['template_examples']),
                          additional_examples=len(extra),
                          independent_exclusions=out['independent_python_exclusions'],
                          small_brute_force_comparisons=out['small_brute_force_comparisons']),
                     indent=2))


if __name__ == '__main__':
    main()
