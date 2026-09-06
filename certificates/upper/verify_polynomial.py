#!/usr/bin/env python3
"""Independent sparse-polynomial certificate for the BB double-cover counterexample.
Python 3.10+ and standard library only. Does NOT import the bitset verifier or
read its matrices/circuits/results. No integer bitsets represent polynomials,
syndromes, chains or matrices.

Run: python3 verify_polynomial.py
Optional: --output-dir DIR writes independently computed matrices and JSON.

Polynomials are frozensets of exponents; addition is symmetric difference;
multiplication is convolution modulo x^L+1. Boundary membership is decided
by a polynomial Bezout congruence solver, not a binary boundary-span oracle.
Circuit search branches on EVERY odd subset of the undecided neighbors of
one odd syndrome coefficient, and fixes ALL those neighbors at once. This
is a different partition/search tree from first-present-candidate branching.
"""
import argparse
from collections import Counter
from functools import lru_cache
import hashlib
from itertools import combinations
import json
from pathlib import Path

ELL, M, ELL_TILDE, M_TILDE = 39, 1, 78, 1
A_EXP, B_EXP = (0, 8, 25), (0, 2, 13)
AT_EXP, BT_EXP = (0, 8, 25), (0, 2, 13)
ZERO = frozenset()
ONE = frozenset({0})
TOKEN = 'BB_DOUBLE_COVER_COUNTEREXAMPLE_VERIFIED'


def need(ok, reason):
    if not ok:
        raise RuntimeError(reason)


def polynomial(es):
    p = set()
    for e in es:
        need(isinstance(e, int) and e >= 0, 'invalid polynomial exponent')
        if e in p:
            p.remove(e)
        else:
            p.add(e)
    return frozenset(p)


def product(a, b):
    out = set()
    for i in a:
        for j in b:
            e = i + j
            if e in out:
                out.remove(e)
            else:
                out.add(e)
    return frozenset(out)


def divide(a, b):
    need(bool(b), 'polynomial division by zero')
    remainder, quotient = set(a), set()
    db = max(b)
    while remainder and max(remainder) >= db:
        shift = max(remainder) - db
        quotient.add(shift)
        remainder.symmetric_difference_update(i + shift for i in b)
    return frozenset(quotient), frozenset(remainder)


def xgcd(a, b):
    u, uu, v, vv = ONE, ZERO, ZERO, ONE
    while b:
        q, r = divide(a, b)
        a, b = b, r
        u, uu = uu, u ^ product(q, uu)
        v, vv = vv, v ^ product(q, vv)
    return a, u, v


def residue(a, L):
    return polynomial(i % L for i in a)


def shifted(a, j, L):
    # Shift is a permutation, so no repeated terms can occur here.
    return frozenset((i + j) % L for i in a)


def convolution(a, b, L):
    out = set()
    for i in a:
        for j in b:
            e = (i + j) % L
            if e in out:
                out.remove(e)
            else:
                out.add(e)
    return frozenset(out)


def star(p, L):
    return frozenset((-i) % L for i in p)


def flat(chain, L):
    return tuple(sorted(chain[0])) + tuple(L + i for i in sorted(chain[1]))


def unflat(support, L):
    return (frozenset(i for i in support if i < L),
            frozenset(i - L for i in support if i >= L))


def move(chain, j, L):
    return shifted(chain[0], j, L), shifted(chain[1], j, L)


def J(chain, L):
    return star(chain[1], L), star(chain[0], L)


def sparse_rank(vectors):
    """Binary symmetric-difference elimination with SMALLEST-coordinate pivots."""
    pivots = {}
    for vector in vectors:
        row = set(vector)
        while row:
            lead = min(row)
            if lead not in pivots:
                pivots[lead] = frozenset(row)
                break
            row.symmetric_difference_update(pivots[lead])
    return len(pivots), sorted(pivots)


class PolynomialCode:
    def __init__(self, L, P, Q):
        self.L, self.P, self.Q = L, P, Q
        need(len(P) == len(Q) == 3 and max(P | Q) < L, 'invalid trinomial')
        self.F = frozenset({0, L})
        g0 = xgcd(P, Q)[0]
        self.g = xgcd(g0, self.F)[0]
        self.a, ra = divide(P, self.g)
        self.b, rb = divide(Q, self.g)
        self.f, rf = divide(self.F, self.g)
        need(not (ra or rb or rf), 'invalid common gcd')
        ab, s, t = xgcd(self.a, self.b)
        one, c, d = xgcd(ab, self.f)
        need(one == ONE, 'cofactors and period are not coprime')
        self.U, self.V, self.W = product(c, s), product(c, t), d
        need(product(self.U, self.a) ^ product(self.V, self.b) ^ product(self.W, self.f) == ONE,
             'three-term Bezout identity failed')
        self.columns = {(block, j): shifted(pol, j, L)
                        for block, pol in ((0, P), (1, Q)) for j in range(L)}
        self.neighbors = [tuple(sorted([(0, (r - e) % L) for e in P]
                                     + [(1, (r - e) % L) for e in Q])) for r in range(L)]
        self.HX = [frozenset(b * L + j for b, j in ns) for ns in self.neighbors]
        self.HZ = [frozenset(flat(self.boundary(frozenset({j})), L)) for j in range(L)]
        need(all(len(row) == 6 for row in self.HX + self.HZ), 'row degree is not 6')
        need(all(len(col) == 3 for col in self.columns.values()), 'column degree is not 3')

    def syndrome(self, chain):
        return convolution(self.P, chain[0], self.L) ^ convolution(self.Q, chain[1], self.L)

    def boundary(self, h):
        return convolution(self.Q, h, self.L), convolution(self.P, h, self.L)

    def boundary_preimage(self, chain):
        """Exact simultaneous congruence solver, NOT Gaussian membership.
        If (u,v)=(Q h,P h) mod F, then g divides u,v, and
        h = U(v/g)+V(u/g) mod (F/g). Conversely we check both equations.
        The Bezout identity includes a multiple of F/g, so this also handles
        repeated-root rings and extra common factors of P,Q outside F.
        """
        u, v = chain
        uq, ur = divide(u, self.g)
        vq, vr = divide(v, self.g)
        if ur or vr:
            return None
        h = divide(product(self.U, vq) ^ product(self.V, uq), self.f)[1]
        return h if self.boundary(h) == chain else None

    def circuit(self, chain):
        supp = flat(chain, self.L)
        if not supp or self.syndrome(chain):
            return False
        r, _ = sparse_rank(self.columns[(j // self.L, j % self.L)] for j in supp)
        return r == len(supp) - 1


def canonical_matrix(rows, ncols):
    lines = ['GF2MATRIX v1', f'{len(rows)} {ncols}']
    lines.extend(''.join('1' if j in row else '0' for j in range(ncols)) for row in rows)
    return ('\n'.join(lines) + '\n').encode('ascii')


def direct_cover_check(base, cover):
    need((ELL_TILDE, M_TILDE) == (2 * ELL, M) and M == 1, 'periods')
    need(tuple(i % ELL for i in AT_EXP) == A_EXP and
         tuple(i % ELL for i in BT_EXP) == B_EXP, 'monomial projection')
    def graph(C):
        L = C.L
        out = {(t, i): set() for t in range(4) for i in range(L)}
        for t, rows in ((2, C.HX), (3, C.HZ)):
            for i, row in enumerate(rows):
                for j in row:
                    q = (j // L, j % L)
                    out[(t, i)].add(q)
                    out[q].add((t, i))
        return out
    gb, gc = graph(base), graph(cover)
    for v, ns in gc.items():
        projected = [(t, i % ELL) for t, i in ns]
        need(len(projected) == len(set(projected)) == len(gb[(v[0], v[1] % ELL)]),
             'neighborhood injectivity/size')
        need(set(projected) == gb[(v[0], v[1] % ELL)], 'neighborhood image')
    need(Counter((t, i % ELL) for t, i in gc) == Counter({v: 2 for v in gb}), 'fiber size')


def parity_subset_enumeration(C, bound, root):
    """At an odd coefficient, assign all remaining incident variables at once.
    Branch on their ODD-cardinality subsets; unused neighbors become decided 0.
    The return value includes all rooted circuits but may include extra cycles.
    """
    stats = Counter({k: 0 for k in ('nodes', 'zero_leaves', 'budget_leaves',
                                   'syndrome_bound_leaves', 'blocked_check_leaves',
                                   'expanded_nodes', 'oversize_assignments_skipped')})
    zero_hist, circ_hist = Counter(), Counter()
    leaves, circuits = set(), set()

    @lru_cache(maxsize=None)
    def assignments(candidates):
        ans = []
        for size in range(1, len(candidates) + 1, 2):
            for subset in combinations(candidates, size):
                du = frozenset(j for b, j in subset if b == 0)
                dv = frozenset(j for b, j in subset if b == 1)
                ds = C.syndrome((du, dv))
                ans.append((du, dv, ds, size))
        return tuple(ans)

    def explore(u, v, decided, syndrome):
        stats['nodes'] += 1
        weight = len(u) + len(v)
        if not syndrome:
            stats['zero_leaves'] += 1
            zero_hist[weight] += 1
            key = (u, v)
            need(key not in leaves, 'duplicate zero-syndrome leaf')
            leaves.add(key)
            h = C.boundary_preimage(key)
            need(h is not None, f'EXCLUSION FAILED: weight {weight}, {flat(key, C.L)}')
            # Direct convolution rechecks the Bezout-derived preimage.
            need(C.boundary(h) == key, 'leaf boundary preimage failed')
            if C.circuit(key):
                circuits.add(key)
                circ_hist[weight] += 1
            return
        remaining = bound - weight
        if remaining <= 0:
            stats['budget_leaves'] += 1
            return
        if len(syndrome) > 3 * remaining:
            stats['syndrome_bound_leaves'] += 1
            return
        best = None
        for row in sorted(syndrome):
            available = tuple(q for q in C.neighbors[row] if q not in decided)
            if not available:
                stats['blocked_check_leaves'] += 1
                return
            if best is None or len(available) < len(best):
                best = available
        stats['expanded_nodes'] += 1
        now_decided = decided | frozenset(best)
        for du, dv, delta, size in assignments(best):
            if size > remaining:
                stats['oversize_assignments_skipped'] += 1
                continue
            explore(u | du, v | dv, now_decided, syndrome ^ delta)

    u = frozenset({root[1]}) if root[0] == 0 else ZERO
    v = frozenset({root[1]}) if root[0] == 1 else ZERO
    explore(u, v, frozenset({root}), C.syndrome((u, v)))
    need(stats['nodes'] == sum(stats[k] for k in ('zero_leaves', 'budget_leaves',
         'syndrome_bound_leaves', 'blocked_check_leaves', 'expanded_nodes')), 'node accounting')
    report = dict(stats)
    report.update(root=root[0] * C.L + root[1], bound=bound,
                  zero_weight_histogram=dict(sorted(zero_hist.items())),
                  circuit_weight_histogram=dict(sorted(circ_hist.items())), nonboundary_leaves=0)
    return report, circuits


def classify(C, circuits):
    unseen, records = set(circuits), []
    while unseen:
        seed = min(unseen, key=lambda c: flat(c, C.L))
        orbit = {move(seed, i, C.L) for i in range(C.L)}
        need(orbit <= circuits, 'circuit set is not translation closed')
        rep = min(orbit, key=lambda c: flat(c, C.L))
        h = C.boundary_preimage(rep)
        need(h is not None and C.boundary(h) == rep, 'orbit preimage')
        stabilizer = [i for i in range(C.L) if move(rep, i, C.L) == rep]
        need(len(orbit) * len(stabilizer) == C.L, 'orbit size check')
        records.append(dict(flat_support=list(flat(rep, C.L)),
                            support={'left': sorted(rep[0]), 'right': sorted(rep[1])},
                            weight=sum(map(len, rep)), orbit_size=len(orbit),
                            boundary=True, boundary_preimage=sorted(h), stabilizer=stabilizer))
        unseen.difference_update(orbit)
    return sorted(records, key=lambda r: (r['weight'], r['flat_support']))


def circuit_bytes(circuits, L):
    ordered = sorted((flat(c, L) for c in circuits), key=lambda s: (len(s), s))
    lines = ['BB_CIRCUITS v1', f'{L} {len(ordered)}']
    lines.extend(','.join(map(str, s)) for s in ordered)
    return ('\n'.join(lines) + '\n').encode('ascii')


def pair_collision_base_check(C):
    """Independent base check: distinct nonzero columns exclude weight 2;
    colliding sums of disjoint pairs would be exactly weight-4 cycles."""
    keys = sorted(C.columns)
    cols = [C.columns[q] for q in keys]
    need(len(set(cols)) == len(cols) and all(cols), 'base weight-1/2 cycle')
    seen = {}
    count = 0
    for i, j in combinations(range(len(cols)), 2):
        s = cols[i] ^ cols[j]
        # Any collision from distinct pairs must be disjoint: sharing an index
        # would force equal columns, already excluded.
        need(s not in seen, 'base weight-4 cycle from colliding column pairs')
        seen[s] = (i, j)
        count += 1
    return {'distinct_nonzero_columns': len(cols), 'distinct_pair_sums': count,
            'collisions': 0}


def main(output_dir=None):
    out = Path(output_dir) if output_dir else None
    if out:
        out.mkdir(parents=True, exist_ok=True)
    A, B = polynomial(A_EXP), polynomial(B_EXP)
    base, cover = PolynomialCode(ELL, A, B), PolynomialCode(ELL_TILDE, polynomial(AT_EXP), polynomial(BT_EXP))
    direct_cover_check(base, cover)
    print('VALIDITY: independently reconstructed sparse-polynomial Tanner cover: PASS', flush=True)
    report = dict(implementation='sparse_polynomial_odd_subset_assignment', codes={}, enumeration=[])
    Xcodes = {}
    for C in (base, cover):
        L = C.L
        need(C.g == frozenset({0, 1, 2}), 'common gcd differs')
        record = dict(ranks={}, row_pivots={}, matrix_sha256={})
        for name, rows in (('HX', C.HX), ('HZ', C.HZ)):
            rank, pivots = sparse_rank(rows)
            need(rank == L - 2, 'sparse binary rank differs from polynomial rank')
            need(sparse_rank(rows[:L - 2])[0] == L - 2, 'first L-2 rows not independent')
            for last, residues in ((L - 2, (0, 1)), (L - 1, (0, 2))):
                relation = set()
                for i in range(L - 2):
                    if i % 3 in residues:
                        relation.symmetric_difference_update(rows[i])
                need(frozenset(relation) == rows[last], 'last-row dependency identity')
            record['ranks'][name], record['row_pivots'][name] = rank, pivots
            record.setdefault('independent_row_indices', {})[name] = list(range(L - 2))
            data = canonical_matrix(rows, 2 * L)
            record['matrix_sha256'][name] = hashlib.sha256(data).hexdigest()
            print(f'SHA256 L={L} {name} {record["matrix_sha256"][name]}', flush=True)
            if out:
                (out / f'L{L}_{name}.txt').write_bytes(data)
        record['k'] = 2 * L - sum(record['ranks'].values())
        need(record['k'] == 4, 'k != 4')
        for i in range(L):
            need(not C.syndrome(C.boundary(frozenset({i}))), 'HX HZ^T != 0')
        need(C.boundary(C.f) == (ZERO, ZERO) and C.boundary(product(C.f, frozenset({1}))) == (ZERO, ZERO),
             'annihilator basis failed')
        X = PolynomialCode(L, star(C.Q, L), star(C.P, L))
        Xcodes[L] = X
        need(X.HX == C.HZ and X.HZ == C.HX, 'independent X matrices disagree entrywise')
        for b in range(2):
            for i in range(L):
                chain = (frozenset({i}), ZERO) if b == 0 else (ZERO, frozenset({i}))
                need(X.syndrome(J(chain, L)) == star(C.syndrome(chain), L), 'J cycle identity')
        for i in range(L):
            need(J(C.boundary(frozenset({i})), L) == X.boundary(frozenset({(-i) % L})), 'J boundary identity')
        record['J_verified_on_all_basis_vectors'] = True
        report['codes'][str(L)] = record
        print(f'RANK L={L}: HX=HZ={L-2}, k=4; both X matrices checked entrywise', flush=True)

    z = (A ^ frozenset({2 * A_EXP[1]}),
         ONE ^ frozenset({B_EXP[2] - B_EXP[1]}))
    F = polynomial((0, ELL))
    c, remainder = divide(product(A, z[0]) ^ product(B, z[1]), F)
    need(not remainder, 'reconstructed base witness')
    rhs = residue(product(A, z[0]) ^ c, ELL)
    dB, inverse, _ = xgcd(B, F)
    quotient, rem = divide(rhs, dB)
    fB, rfB = divide(F, dB)
    need(not rem and not rfB and dB == frozenset({0, 1, 2}), 'right-correction congruence')
    r0 = divide(product(inverse, quotient), fB)[1]
    xfB = product(frozenset({1}), fB)
    options = (r0, r0 ^ fB, r0 ^ xfB, r0 ^ fB ^ xfB)
    need(all(convolution(B, opt, ELL) == rhs for opt in options), 'right-correction solutions')
    R = min(options, key=lambda p: (len(p), sorted(p)))
    need(sum(len(p) == len(R) for p in options) == 1, 'right-correction minimum not unique')
    need(R == polynomial((9, 22, 35, 37)), 'reconstructed witness differs from stated one')
    w = product(frozenset({ELL}), z[0]), z[1] ^ product(F, R)
    need(product(A, z[0]) ^ product(B, z[1]) == product(F, c), 'base polynomial identity')
    need(product(A, z[0]) ^ product(B, R) ^ c == product(F, polynomial((0, 2, 9))), 'cover polynomial identity')
    need(not base.syndrome(z) and sum(map(len, z)) == 6, 'base witness')
    need(base.boundary_preimage(z) is None, 'base witness is boundary')
    need(not cover.syndrome(w) and sum(map(len, w)) == 14, 'cover witness')
    need(tuple(residue(p, ELL) for p in w) == z, 'p(w) != z')
    need(cover.boundary_preimage(w) is None, 'cover witness is boundary')
    for C, y in ((base, z), (cover, w)):
        X = Xcodes[C.L]
        need(not X.syndrome(J(y, C.L)) and X.boundary_preimage(J(y, C.L)) is None, 'X witness')
    tz = tuple(product(F, p) for p in z)
    H = cover.boundary_preimage(tz)
    need(H is not None and cover.boundary(H) == tz, 'tau(z) boundary preimage')
    report['witnesses'] = dict(z={'left': sorted(z[0]), 'right': sorted(z[1])},
                               w={'left': sorted(w[0]), 'right': sorted(w[1])}, H=sorted(H))
    print('WITNESSES: cycles, nontriviality, projection, tau(z) polynomial boundary: PASS', flush=True)
    print('TAU_Z_PREIMAGE H=' + json.dumps(sorted(H), separators=(',', ':')), flush=True)
    report['base_pair_check'] = pair_collision_base_check(base)
    print('BASE_PAIR_CHECK ' + json.dumps(report['base_pair_check'], sort_keys=True), flush=True)

    zcircuits, xcircuits = set(), set()
    for C in (base, cover):
        bound = 4 if C.L == ELL else 12
        for sector, D in (('Z', C), ('X', Xcodes[C.L])):
            for root in ((0, 0), (1, 0)):
                stats, rooted = parity_subset_enumeration(D, bound, root)
                stats.update(L=C.L, sector=sector)
                report['enumeration'].append(stats)
                print('ENUM ' + json.dumps(stats, sort_keys=True, separators=(',', ':')), flush=True)
                if C.L == ELL:
                    need(not rooted and stats['zero_leaves'] == 0, 'base small circuit')
                else:
                    target = zcircuits if sector == 'Z' else xcircuits
                    for chain in rooted:
                        target.update(move(chain, j, C.L) for j in range(C.L))
    need({J(c0, ELL_TILDE) for c0 in zcircuits} == xcircuits, 'X/Z circuit sets differ')
    hist = dict(sorted(Counter(sum(map(len, c0)) for c0 in zcircuits).items()))
    need(hist == {6: 78, 10: 468, 12: 195}, 'circuit counts differ')
    orbits = classify(cover, zcircuits)
    need(len(orbits) == 10, 'orbit count differs')
    need(Counter((r['weight'], r['orbit_size']) for r in orbits)
         == Counter({(6, 78): 1, (10, 78): 6, (12, 78): 2, (12, 39): 1}), 'orbit-size counts differ')
    for weight, total in hist.items():
        rcount = sum(s['circuit_weight_histogram'].get(weight, 0) for s in report['enumeration']
                     if s['L'] == ELL_TILDE and s['sector'] == 'Z')
        need(ELL_TILDE * rcount == weight * total, 'root incidence count mismatch')
    cb = circuit_bytes(zcircuits, ELL_TILDE)
    report['circuits'] = dict(histogram=hist, total=len(zcircuits),
                               sha256=hashlib.sha256(cb).hexdigest(), orbits=orbits)
    for i, rec in enumerate(orbits, 1):
        print(f'ORBIT {i} ' + json.dumps(rec, sort_keys=True, separators=(',', ':')), flush=True)
    print('CIRCUIT_SET_SHA256 ' + report['circuits']['sha256'], flush=True)
    report['result'] = dict(base=[78, 4, 6], cover=[156, 4, 14], upper_bound_false=True)
    print('DISTANCES: base X=Z=6; cover X=Z=14; 14>12', flush=True)
    if out:
        (out / 'circuits.txt').write_bytes(cb)
        (out / 'report_polynomial.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(TOKEN, flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', help='optional directory for independently generated artifacts')
    args = parser.parse_args()
    main(args.output_dir)
