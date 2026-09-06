#!/usr/bin/env python3
"""Exact checks for the fixed-quadratic Laurent results.

Standard-library-only. Laurent polynomials are finite sets of exponents.
No decoder or bounded-message search is used as a minimum certificate.
"""
from __future__ import annotations
import json
import random
from collections import defaultdict, deque
from itertools import product
from pathlib import Path

Poly = frozenset[int]
Vec = tuple[int, int, int]
ONE: Poly = frozenset({0})
ZERO: Poly = frozenset()
C: Poly = frozenset({0, 1, 2})


def add(*ps: Poly) -> Poly:
    out: set[int] = set()
    for p in ps:
        out.symmetric_difference_update(p)
    return frozenset(out)


def shift(p: Poly, n: int) -> Poly:
    return frozenset(i+n for i in p)


def mul(p: Poly, q: Poly) -> Poly:
    out: set[int] = set()
    for i in p:
        out.symmetric_difference_update(j+i for j in q)
    return frozenset(out)


def quotient(p: Poly, q: Poly) -> Poly:
    """Exact Laurent division. Raises if the quotient is not Laurent."""
    if not q:
        raise ZeroDivisionError()
    if not p:
        return ZERO
    lo, lq = min(p), min(q)
    a = sum(1 << (i-lo) for i in p)
    b = sum(1 << (i-lq) for i in q)
    v = 0
    while a and a.bit_length() >= b.bit_length():
        n = a.bit_length()-b.bit_length()
        v ^= 1 << n
        a ^= b << n
    if a:
        raise ArithmeticError((p, q, a))
    return frozenset(i+lo-lq for i in range(v.bit_length()) if (v >> i) & 1)


def imod(p: Poly, modulus: int) -> int:
    """Laurent remainder for the moduli c and c^2 used below."""
    period = 3 if modulus == 7 else 6
    ans = 0
    for i in p:
        ans ^= 1 << (i % period)
    while ans.bit_length() >= modulus.bit_length():
        ans ^= modulus << (ans.bit_length()-modulus.bit_length())
    return ans


RP = tuple[Poly, Poly]
THETA: RP = (frozenset({1, 2}), ONE)


def ra(a: RP, b: RP) -> RP:
    return add(a[0], b[0]), add(a[1], b[1])


def rm(a: RP, b: RP) -> RP:
    return add(mul(a[0], b[0]), mul(a[1], b[1])), add(mul(a[0], b[1]), mul(a[1], b[0]))


def rshift(a: RP, n: int, s: int = 0) -> RP:
    v = (shift(a[0], n), shift(a[1], n))
    return v[::-1] if s else v


def rw(a: RP) -> int:
    return len(a[0])+len(a[1])


def rquot_theta(a: RP) -> RP:
    numer = rm(a, THETA)
    c2 = mul(C, C)
    q = quotient(numer[0], c2), quotient(numer[1], c2)
    assert rm(THETA, q) == a
    return q


def residue_theta(a: RP) -> int:
    return imod(add(a[0], mul(frozenset({1, 2}), a[1])), 21)


def data(E: int, O: int):
    B = frozenset({0, E, O})
    if len(B) != 3:
        raise ValueError('Non-strict support')
    b = quotient(B, C)
    P = quotient(add(B, C), mul(C, C))
    D = (add(b, P), P)
    Bt = (frozenset({E, O}), ONE)
    assert rm(THETA, D) == Bt
    assert D == ra((ONE, ZERO), rm(THETA, (P, ZERO)))
    return B, b, P, D, Bt


def vadd(a: Vec, b: Vec) -> Vec:
    return tuple(x+y for x, y in zip(a, b))  # type: ignore


def vsub(a: Vec, b: Vec) -> Vec:
    return tuple(x-y for x, y in zip(a, b))  # type: ignore


def cross(a: Vec, b: Vec) -> Vec:
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def circuit_check(E: int, O: int, F: Poly) -> dict:
    """Reconstruct incidence relations, without using polynomial gcd routines."""
    B, b, _, _, _ = data(E, O)
    U = mul(b, F)
    assert imod(F, 7)
    assert not add(mul(C, U), mul(B, F))
    nodes = [(0, i) for i in sorted(U)] + [(1, i) for i in sorted(F)]
    actual_ports = ((0, 1, 2), (0, E, O))
    formal_ports = (((0, 0, 0), (1, 0, 0), (2, 0, 0)), ((0, 0, 0), (0, 1, 0), (0, 0, 1)))
    syndrome: dict[int, list[tuple[int, Vec]]] = defaultdict(list)
    for n, (block, x) in enumerate(nodes):
        for p, d in zip(formal_ports[block], actual_ports[block]):
            syndrome[x+d].append((n, p))
    edges: list[tuple[int, int, Vec]] = []
    adj: dict[int, list[tuple[int, Vec]]] = defaultdict(list)
    for inc in syndrome.values():
        assert len(inc) % 2 == 0
        for j in range(0, len(inc), 2):
            (u, pu), (v, pv) = inc[j:j+2]
            assert u != v
            d = vsub(pu, pv)
            edges.append((u, v, d))
            adj[u].append((v, d))
            adj[v].append((u, tuple(-x for x in d)))
    seen: set[int] = set()
    selected = None
    for root in range(len(nodes)):
        if root in seen:
            continue
        component = {root}
        seen.add(root)
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v, _ in adj[u]:
                if v not in seen:
                    seen.add(v); component.add(v); queue.append(v)
        Fc = frozenset(nodes[i][1] for i in component if nodes[i][0] == 1)
        if imod(Fc, 7):
            selected = component
            break
    assert selected is not None
    a = sum(nodes[i][0] == 0 for i in selected)
    m = len(selected)-a
    assert a > 0 and m > 0
    root = next(iter(selected))
    positions: dict[int, Vec] = {root: (0, 0, 0)}
    queue = deque([root])
    while queue:
        u = queue.popleft()
        for v, d in adj[u]:
            if v not in positions:
                positions[v] = vadd(positions[u], d); queue.append(v)
    rows = []
    for u, v, d in edges:
        if u in selected:
            r = vsub(vadd(positions[u], d), positions[v])
            assert r[0] + E*r[1] + O*r[2] == 0
            assert abs(r[0]) <= 2*a
            assert max(abs(r[1]), abs(r[2]), abs(r[1]+r[2])) <= m
            if any(r):
                rows.append(r)
    pair = None
    for r in rows:
        for t in rows:
            k = cross(r, t)
            if any(k):
                pair = r, t, k
                break
        if pair:
            break
    assert pair is not None, 'The rank-two rigidity prediction failed'
    r, t, k = pair
    assert k[0] and k == (k[0], k[0]*E, k[0]*O)
    R = max(0, E, O)-min(0, E, O)
    assert R <= 4*a*m <= 4*len(U)*len(F)
    return dict(R=R, input_weight=len(F), output_weight=len(U), component_a=a, component_m=m,
                rows=[r, t], cross=k)


def main() -> None:
    rng = random.Random(6062026)
    # Order -> (3 wt(b)-2R, wt(D)-R).
    table = {
        ('0','O','E'): (-1,-1), ('0','E','O'): (1,0),
        ('E','0','O'): (-1,0), ('O','0','E'): (1,0),
        ('E','O','0'): (1,1), ('O','E','0'): (-1,0),
    }
    counts = defaultdict(int)
    for r, t in product(range(-24,25), repeat=2):
        E, O = 6*r+2, 6*t+1
        B, b, P, D, Bt = data(E,O)
        R = max(B)-min(B)
        order = tuple(sorted(('0','E','O'), key=lambda x: {'0':0,'E':E,'O':O}[x]))
        kb,kd = table[order]
        assert 3*len(b)-2*R == kb
        assert rw(D)-R == kd
        beta, nu = len(b)+1, rw(D)+1
        assert 2*nu <= 3*beta
        assert nu <= R+2
        # Evaluation at a common zero: D is 1 in the quotient by Theta.
        assert residue_theta(D) == 1
        counts['quotient_and_weight_table_instances'] += 1

    units: dict[int, tuple[int,int]] = {}
    for i in range(6):
        for j in range(2):
            q = (frozenset({i}),ZERO) if not j else (ZERO,frozenset({i}))
            a = residue_theta(q)
            assert a not in units
            units[a] = (i,j)
    allunits = {i for i in range(16) if imod(frozenset(k for k in range(4) if (i>>k)&1),7)}
    assert set(units) == allunits and len(units)==12
    counts['distinct_monomial_unit_classes'] = len(units)

    for _ in range(360):
        r,t = rng.randint(-8,8),rng.randint(-8,8)
        E,O = 6*r+2,6*t+1
        B,b,P,D,Bt = data(E,O)
        F = frozenset(rng.sample(range(-12,35),rng.randint(1,9)))
        H = frozenset(rng.sample(range(-14,38),rng.randint(0,9)))
        if not imod(F,7):
            F = add(F,ONE)
        V = (add(F,H),H)
        Y = (rm(D,V), V)
        systematic = (add(mul(add(b,P),F),mul(b,H)), add(mul(P,F),mul(b,H)),add(F,H),H)
        assert (*Y[0], *Y[1]) == systematic
        assert not any(ra(rm(THETA,Y[0]),rm(Bt,Y[1])))
        kval = residue_theta(V)
        i,j = units[kval]
        q = (frozenset({i}),ZERO) if not j else (ZERO,frozenset({i}))
        J = rquot_theta(ra(V,q))
        # Every admissible word, not just a chosen representative, is in a
        # physical translate of the single boundary coset (D,1)+im(partial_2).
        assert ra(V,rm(THETA,J)) == q
        assert ra(Y[0],rm(Bt,J)) == rm(D,q)
        assert rw(rshift(Y[0],-i,j))+rw(rshift(Y[1],-i,j)) == rw(Y[0])+rw(Y[1])
        counts['all_message_parameterization_and_orbit_checks'] += 1

    graph_examples = []
    for _ in range(240):
        r,t = rng.randint(-9,9),rng.randint(-9,9)
        E,O = 6*r+2,6*t+1
        F = frozenset(rng.sample(range(-10,40),rng.randint(1,7)))
        if not imod(F,7):
            F = add(F,ONE)
        rec = circuit_check(E,O,F)
        if len(graph_examples)<8:
            graph_examples.append(dict(E=E,O=O, F=sorted(F), **rec))
        counts['independent_incidence_product_bound_checks'] += 1

    # Exact all-message relaxation counterfamily. This is NOT a valid
    # strict-trinomial term-matched cover: its second lift has five terms.
    for N in range(1,97):
        bn = frozenset({3*N})
        pn = quotient(add(bn,ONE),C)
        assert pn == frozenset(x for j in range(N) for x in (3*j,3*j+1))
        Dn = (add(bn,pn),pn)
        BadB = rm(THETA,Dn)
        assert BadB == (add(shift(C,3*N),ONE),ONE)
        assert rw(BadB)==5
        assert rw(Dn)+1 == 4*N+2
        pprime = shift(pn,-3*N)
        assert max(pprime)==-2
        F = frozenset(rng.sample(range(0,50),rng.randint(1,7)))
        if not imod(F,7): F=add(F,ONE)
        T = mul(pprime,F)
        assert len(T)>=2*N
        assert max(F) not in T
        assert 2*len(F|T)>=4*N+2
        # H=0 attains the pointwise minimum 2|F union T|.
        assert len(add(F,T))+len(T)+len(F)==2*len(F|T)
        counts['relaxation_counterfamily_identity_checks'] += 1

    result = {
        'status':'All exact checks passed',
        'theorems': {
            'product_uncertainty':'span(B) <= 4 wt(F) wt((B/c)F) for every c-nondivisible Laurent F',
            'quadratic_bound':'mu_plus <= mu_0^2 + 2; for E,O>0, mu_plus <= mu_0^2',
            'orbit_reduction':'All 12 admissible universal cover residue classes are monomial translates',
            'factor_three':'Unproved and unrefuted for the full strict-trinomial class',
            'relaxation_control':'mu_0=2, mu_plus=4N+2 exactly, but the second lifted check has five terms and is inadmissible',
        },
        'counts':dict(counts),
        'incidence_examples':graph_examples,
        'scope':'Finite checks verify identities and constructive certificates. The uniform inequalities are proved symbolically in proof.md. No new exact strict-trinomial minimum or finite distance record is claimed.'
    }
    dest=Path(__file__).resolve().with_name('verification_summary.json')
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'counts':result['counts']},indent=2))


if __name__=='__main__':
    main()
