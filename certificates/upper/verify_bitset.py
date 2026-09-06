#!/usr/bin/env python3
"""Standalone exact certificate: [[78,4,6]] -> [[156,4,14]].
Python 3.10+; standard library only; no network, randomness or external inputs.

Run: python3 verify_bitset.py
Optional: --output-dir DIR writes matrices and a JSON report to DIR.
The last stdout line is the success token ONLY if every check passes.

Core: integer-bitset binary matrices and Tanner-incidence circuit enumeration.
No expected circuit supports are supplied to the enumeration or classification.
Expected ranks/counts are checked only after they have been computed.
See CERTIFICATE.md for proofs of enumeration completeness and each pruning rule.
"""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path

ELL, M = 39, 1
ELL_TILDE, M_TILDE = 78, 1
A_EXP, B_EXP = (0, 8, 25), (0, 2, 13)
AT_EXP, BT_EXP = (0, 8, 25), (0, 2, 13)
TOKEN = 'BB_DOUBLE_COVER_COUNTEREXAMPLE_VERIFIED'


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def bits(v):
    while v:
        b = v & -v
        yield b.bit_length() - 1
        v ^= b


def poly(exponents):
    ans = 0
    for e in exponents:
        require(isinstance(e, int) and e >= 0, 'invalid exponent')
        ans ^= 1 << e
    return ans


def mul(a, b):
    ans = 0
    for e in bits(a):
        ans ^= b << e
    return ans


def pdiv(a, b):
    require(b != 0, 'polynomial division by zero')
    q = 0
    while a and a.bit_length() >= b.bit_length():
        s = a.bit_length() - b.bit_length()
        q ^= 1 << s
        a ^= b << s
    return q, a


def egcd(a, b):
    s0, s1, t0, t1 = 1, 0, 0, 1
    while b:
        q, r = pdiv(a, b)
        a, b = b, r
        s0, s1 = s1, s0 ^ mul(q, s1)
        t0, t1 = t1, t0 ^ mul(q, t1)
    return a, s0, t0


def rot(v, s, L):
    require(0 <= v < (1 << L), 'rotation input outside block')
    s %= L
    return ((v << s) | (v >> (L - s))) & ((1 << L) - 1)


def translate(v, s, L):
    mask = (1 << L) - 1
    return rot(v & mask, s, L) | (rot(v >> L, s, L) << L)


def act(columns, v):
    ans = 0
    for i in bits(v):
        ans ^= columns[i]
    return ans


def transpose(rows, ncols):
    out = [0] * ncols
    for i, row in enumerate(rows):
        for j in bits(row):
            out[j] |= 1 << i
    return out


class Span:
    """Exact column-span elimination, retaining coefficients of each pivot."""
    def __init__(self, vectors):
        self.table = {}
        self.kernel = []
        for j, v in enumerate(vectors):
            coef = 1 << j
            while v:
                p = v.bit_length() - 1
                if p not in self.table:
                    self.table[p] = (v, coef)
                    break
                old, c = self.table[p]
                v ^= old
                coef ^= c
            if not v:
                self.kernel.append(coef)
        self.pivots = sorted(self.table, reverse=True)

    def solve(self, v):
        coef = 0
        for p in self.pivots:
            if (v >> p) & 1:
                row, c = self.table[p]
                v ^= row
                coef ^= c
        return coef if v == 0 else None

    def rank(self):
        return len(self.table)


def make_code(L, ae, be):
    require(len(set(ae)) == len(set(be)) == 3, 'not distinct trinomials')
    require(all(0 <= i < L for i in ae + be), 'noncanonical monomial')
    A, B = poly(ae), poly(be)
    ma = [rot(A, j, L) for j in range(L)]
    mb = [rot(B, j, L) for j in range(L)]
    hx_columns = ma + mb
    hx_rows = transpose(hx_columns, L)
    hz_rows = [mb[j] | (ma[j] << L) for j in range(L)]
    hz_columns = transpose(hz_rows, 2 * L)
    require(all(act(hx_columns, g) == 0 for g in hz_rows), 'HX HZ^T != 0')
    require(all(act(hz_columns, g) == 0 for g in hx_rows), 'HZ HX^T != 0')
    for mat in (hx_rows, hz_rows):
        require(all(v.bit_count() == 6 for v in mat), 'row weight is not 6')
    for mat in (hx_columns, hz_columns):
        require(all(v.bit_count() == 3 for v in mat), 'column weight is not 3')
    return dict(L=L, A=A, B=B, HX=hx_rows, HZ=hz_rows,
                Zcheck=hx_columns, Zboundary=hz_rows,
                Xcheck=hz_columns, Xboundary=hx_rows)


def matrix_bytes(rows, ncols):
    header = f'GF2MATRIX v1\n{len(rows)} {ncols}\n'
    body = ''.join(''.join(str((r >> j) & 1) for j in range(ncols)) + '\n'
                   for r in rows)
    return (header + body).encode('ascii')


def support(v, L):
    return {'left': list(bits(v & ((1 << L) - 1))), 'right': list(bits(v >> L))}


def project(v, L):
    mask = (1 << L) - 1
    u = (v & mask) ^ ((v >> L) & mask)
    w = ((v >> (2 * L)) & mask) ^ ((v >> (3 * L)) & mask)
    return u | (w << L)


def transfer(v, L):
    mask = (1 << L) - 1
    u, w = v & mask, v >> L
    return u | (u << L) | (w << (2 * L)) | (w << (3 * L))


def star(v, L):
    return poly((-j) % L for j in bits(v))


def J(v, L):
    return star(v >> L, L) | (star(v & ((1 << L) - 1), L) << L)


def tanner_graph(code):
    """Vertex labels: (0,j) left, (1,j) right, (2,j) X, (3,j) Z."""
    L = code['L']
    graph = {(t, j): set() for t in range(4) for j in range(L)}
    for check_type, name in ((2, 'HX'), (3, 'HZ')):
        for r, row in enumerate(code[name]):
            for q in bits(row):
                v = (q // L, q % L)
                graph[(check_type, r)].add(v)
                graph[v].add((check_type, r))
    return graph


def check_cover(base, cover):
    require(M == M_TILDE == 1 and ELL_TILDE == 2 * ELL, 'invalid periods')
    require(tuple(a % ELL for a in AT_EXP) == A_EXP, 'A does not project')
    require(tuple(b % ELL for b in BT_EXP) == B_EXP, 'B does not project')
    gb, gc = tanner_graph(base), tanner_graph(cover)
    projection = lambda v: (v[0], v[1] % ELL)
    require(Counter(projection(v) for v in gc) == Counter({v: 2 for v in gb}),
            'vertex fibers not size 2')
    for v, neighbors in gc.items():
        images = [projection(w) for w in neighbors]
        require(len(images) == len(set(images)) and set(images) == gb[projection(v)],
                'Tanner-neighborhood projection not bijective')
    # Chain-map identities checked on every basis vector in degrees 1 and 2.
    for j, col in enumerate(cover['Zcheck']):
        require(star(star(col, 2 * ELL), 2 * ELL) == col, 'star sanity')
        image = (col & ((1 << ELL) - 1)) ^ (col >> ELL)
        require(image == act(base['Zcheck'], project(1 << j, ELL)), 'p0 d1 != d1 p1')
    for j, col in enumerate(cover['Zboundary']):
        require(project(col, ELL) == base['Zboundary'][j % ELL], 'p1 d2 != d2 p2')


def is_circuit(columns, v):
    return (v != 0 and act(columns, v) == 0
            and Span([columns[j] for j in bits(v)]).rank() == v.bit_count() - 1)


def rooted_enumeration(columns, boundaries, bound, root):
    """First-present-candidate branching. Never uses an expected circuit list."""
    n, m = len(columns), max(v.bit_length() for v in columns)
    adjacency = [0] * m
    for j, col in enumerate(columns):
        for i in bits(col):
            adjacency[i] |= 1 << j
    span = Span(boundaries)
    stats = Counter({k: 0 for k in ('nodes', 'zero_leaves', 'budget_leaves',
                                    'syndrome_bound_leaves', 'blocked_check_leaves',
                                    'expanded_nodes')})
    zero_weights, circuit_weights = Counter(), Counter()
    leaves, circuits = set(), set()

    def visit(chosen, forbidden, syndrome, weight):
        stats['nodes'] += 1
        if syndrome == 0:
            stats['zero_leaves'] += 1
            zero_weights[weight] += 1
            require(chosen not in leaves, 'duplicate zero leaf')
            leaves.add(chosen)
            require(span.solve(chosen) is not None,
                    f'EXCLUSION FAILED: nonboundary weight {weight}, support {list(bits(chosen))}')
            if is_circuit(columns, chosen):
                circuits.add(chosen)
                circuit_weights[weight] += 1
            return
        remaining = bound - weight
        if remaining <= 0:
            stats['budget_leaves'] += 1
            return
        if syndrome.bit_count() > 3 * remaining:
            stats['syndrome_bound_leaves'] += 1
            return
        excluded = chosen | forbidden
        candidates, smallest = 0, n + 1
        for i in bits(syndrome):
            available = adjacency[i] & ~excluded
            degree = available.bit_count()
            if degree == 0:
                stats['blocked_check_leaves'] += 1
                return
            if degree < smallest:
                candidates, smallest = available, degree
        stats['expanded_nodes'] += 1
        while candidates:
            b = candidates & -candidates
            candidates ^= b
            j = b.bit_length() - 1
            visit(chosen | b, forbidden, syndrome ^ columns[j], weight + 1)
            forbidden |= b

    visit(1 << root, 0, columns[root], 1)
    require(stats['nodes'] == sum(stats[k] for k in ('zero_leaves', 'budget_leaves',
            'syndrome_bound_leaves', 'blocked_check_leaves', 'expanded_nodes')),
            'search accounting mismatch')
    ans = dict(stats)
    ans.update(root=root, bound=bound,
               zero_weight_histogram=dict(sorted(zero_weights.items())),
               circuit_weight_histogram=dict(sorted(circuit_weights.items())),
               nonboundary_leaves=0)
    return ans, circuits


def circuit_serialization(circuits, L):
    ordered = sorted((tuple(bits(v)) for v in circuits), key=lambda s: (len(s), s))
    text = f'BB_CIRCUITS v1\n{L} {len(ordered)}\n'
    text += ''.join(','.join(map(str, s)) + '\n' for s in ordered)
    return text.encode('ascii')


def classify(circuits, code):
    L = code['L']
    span = Span(code['Zboundary'])
    remaining = set(circuits)
    records = []
    while remaining:
        seed = min(remaining)
        orbit = {translate(seed, j, L) for j in range(L)}
        require(orbit <= circuits, 'enumerated set not translation closed')
        rep = poly(min(tuple(bits(v)) for v in orbit))
        preimage = span.solve(rep)
        require(preimage is not None and act(code['Zboundary'], preimage) == rep,
                'orbit boundary preimage failed')
        stabilizer = [j for j in range(L) if translate(rep, j, L) == rep]
        require(len(orbit) * len(stabilizer) == L, 'orbit-stabilizer check')
        records.append(dict(support=support(rep, L), flat_support=list(bits(rep)),
                            weight=rep.bit_count(), orbit_size=len(orbit), boundary=True,
                            boundary_preimage=list(bits(preimage)), stabilizer=stabilizer))
        remaining -= orbit
    records.sort(key=lambda d: (d['weight'], d['flat_support']))
    return records


def main(output_dir=None):
    out = Path(output_dir) if output_dir else None
    if out:
        out.mkdir(parents=True, exist_ok=True)
    base = make_code(ELL, A_EXP, B_EXP)
    cover = make_code(ELL_TILDE, AT_EXP, BT_EXP)
    check_cover(base, cover)
    report = dict(implementation='bitset_first_present_candidate',
                  input=dict(ell=ELL, m=M, ell_tilde=ELL_TILDE, m_tilde=M_TILDE,
                             A=A_EXP, B=B_EXP, A_tilde=AT_EXP, B_tilde=BT_EXP),
                  codes={}, enumeration=[])
    print('VALIDITY: Theorem-3.1 congruences, two-element fibers, all Tanner neighborhoods: PASS')
    A, B = base['A'], base['B']
    g, bezA, bezB = egcd(A, B)
    require(g == poly((0, 1, 2)), 'gcd(A,B) != 1+x+x^2')
    require(mul(bezA, A) ^ mul(bezB, B) == g, 'gcd Bezout certificate')
    for code in (base, cover):
        L = code['L']
        F = (1 << L) | 1
        require(pdiv(F, g)[1] == 0, 'g does not divide period polynomial')
        record = {'ranks': {}, 'matrix_sha256': {}, 'row_pivots': {}}
        for name in ('HX', 'HZ'):
            rows = code[name]
            rs = Span(rows)
            require(rs.rank() == Span(transpose(rows, 2 * L)).rank(), 'row/column ranks disagree')
            require(rs.rank() == L - 2, 'wrong binary rank')
            require(Span(rows[:L - 2]).rank() == L - 2, 'first L-2 rows not independent')
            for last, residues in ((L - 2, (0, 1)), (L - 1, (0, 2))):
                coefficients = poly(i for i in range(L - 2) if i % 3 in residues)
                require(act(rows, coefficients) == rows[last], 'last-row dependency identity')
            record['ranks'][name] = rs.rank()
            record['row_pivots'][name] = rs.pivots
            record.setdefault('independent_row_indices', {})[name] = list(range(L - 2))
            data = matrix_bytes(rows, 2 * L)
            digest = hashlib.sha256(data).hexdigest()
            record['matrix_sha256'][name] = digest
            print(f'SHA256 L={L} {name} {digest}')
            if out:
                (out / f'L{L}_{name}.txt').write_bytes(data)
        f = pdiv(F, g)[0]
        require(act(code['Zboundary'], f) == 0 and act(code['Zboundary'], f << 1) == 0,
                'annihilator basis failed')
        require(Span([f, f << 1]).rank() == 2, 'annihilator basis dependent')
        record['annihilator_basis'] = [list(bits(f)), list(bits(f << 1))]
        record['k'] = 2 * L - sum(record['ranks'].values())
        require(record['k'] == 4, 'k != 4')
        # Verify exact physical permutation and matrix identities, not merely a distance assertion.
        permutation = [next(bits(J(1 << j, L))) for j in range(2 * L)]
        require(sorted(permutation) == list(range(2 * L)), 'J not a permutation')
        for j in range(2 * L):
            require(act(code['Xcheck'], J(1 << j, L)) == star(code['Zcheck'][j], L),
                    'HZ J != Istar HX')
        for j in range(L):
            require(J(code['Zboundary'][j], L) == code['Xboundary'][(-j) % L],
                    'J HZ^T != HX^T Istar')
        record['J_permutation'] = permutation
        report['codes'][str(L)] = record
        print(f'RANK L={L}: HX={L-2}, HZ={L-2}, k=4; J checked on every basis vector')

    # Reconstruct the stated witness from the defining exponent tuples.
    # The short right correction is solved exactly, not supplied as a circuit list.
    zL = A ^ (1 << (2 * A_EXP[1]))
    zR = 1 ^ (1 << (B_EXP[2] - B_EXP[1]))
    z = zL | (zR << ELL)
    F = (1 << ELL) | 1
    c, remainder = pdiv(mul(A, zL) ^ mul(B, zR), F)
    require(remainder == 0, 'reconstructed base witness is not a cycle')
    Bspan = Span([rot(B, i, ELL) for i in range(ELL)])
    rhs = pdiv(c ^ mul(A, zL), F)[1]
    r0 = Bspan.solve(rhs)
    require(r0 is not None and len(Bspan.kernel) == 2, 'right-correction affine space')
    options = [r0]
    for kernel_vector in Bspan.kernel:
        options += [v0 ^ kernel_vector for v0 in options]
    R = min(options, key=lambda v0: (v0.bit_count(), v0))
    require(sum(v0.bit_count() == R.bit_count() for v0 in options) == 1,
            'right-correction minimum is not unique')
    require(R == poly((9, 22, 35, 37)), 'reconstructed witness differs from stated one')
    w = (zL << ELL) | ((zR ^ mul(F, R)) << ELL_TILDE)
    require(mul(A, zL) ^ mul(B, zR) == mul(F, c), 'base polynomial identity failed')
    require(mul(A, zL) ^ mul(B, R) ^ c == mul(F, poly((0, 2, 9))),
            'cover polynomial identity failed')
    require(act(base['Zcheck'], z) == 0 and z.bit_count() == 6, 'base cycle/weight')
    require(Span(base['Zboundary']).solve(z) is None, 'base witness is a boundary')
    require(pdiv(zL, g)[1] == 2 and pdiv(zR, g)[1] == 2, 'base mod-g witness')
    require(act(cover['Zcheck'], w) == 0 and w.bit_count() == 14, 'cover cycle/weight')
    require(project(w, ELL) == z, 'p(w) != z')
    require(Span(cover['Zboundary']).solve(w) is None, 'cover witness is a boundary')
    for code, witness in ((base, z), (cover, w)):
        xw = J(witness, code['L'])
        require(xw.bit_count() == witness.bit_count() and act(code['Xcheck'], xw) == 0,
                'X witness failed')
        require(Span(code['Xboundary']).solve(xw) is None, 'X witness is a boundary')
    report['witnesses'] = dict(z=support(z, ELL), w=support(w, ELL_TILDE),
                               Jz=support(J(z, ELL), ELL), Jw=support(J(w, ELL_TILDE), ELL_TILDE))
    print('WITNESSES: base weight 6, cover weight 14, p(w)=z, both nonboundaries: PASS')

    a, b, f = pdiv(A, g)[0], pdiv(B, g)[0], pdiv(F, g)[0]
    one, U, V = egcd(a, b)
    require(one == 1 and mul(U, a) ^ mul(V, b) == 1, 'cofactor Bezout identity')
    v = pdiv(mul(U, zR) ^ mul(V, zL), F)[1]
    H = pdiv(mul(f, v), (1 << ELL_TILDE) | 1)[1]
    tz = transfer(z, ELL)
    require(act(cover['Zboundary'], H) == tz, 'explicit tau(z) boundary failed')
    report['transfer_boundary'] = dict(a=list(bits(a)), b=list(bits(b)), U=list(bits(U)),
                                       V=list(bits(V)), v=list(bits(v)), H=list(bits(H)),
                                       tau_z=support(tz, ELL_TILDE))
    print('TAU_Z_PREIMAGE H=' + json.dumps(list(bits(H)), separators=(',', ':')))

    full_z_circuits = set()
    full_x_circuits = set()
    for code, bound in ((base, 4), (cover, 12)):
        L = code['L']
        for sector in ('Z', 'X'):
            for root in (0, L):
                stats, circuits = rooted_enumeration(code[sector + 'check'],
                                                      code[sector + 'boundary'], bound, root)
                stats.update(L=L, sector=sector)
                report['enumeration'].append(stats)
                print('ENUM ' + json.dumps(stats, sort_keys=True, separators=(',', ':')))
                if L == ELL:
                    require(not circuits and stats['zero_leaves'] == 0, 'base low cycle found')
                else:
                    dest = full_z_circuits if sector == 'Z' else full_x_circuits
                    for v0 in circuits:
                        dest.update(translate(v0, j, L) for j in range(L))
    require({J(v0, ELL_TILDE) for v0 in full_z_circuits} == full_x_circuits,
            'independent X and Z circuit enumerations disagree under J')
    histogram = dict(sorted(Counter(v0.bit_count() for v0 in full_z_circuits).items()))
    require(histogram == {6: 78, 10: 468, 12: 195}, 'circuit histogram differs')
    orbits = classify(full_z_circuits, cover)
    require(len(orbits) == 10, 'orbit count differs')
    orbit_hist = Counter((r['weight'], r['orbit_size']) for r in orbits)
    require(orbit_hist == Counter({(6, 78): 1, (10, 78): 6, (12, 78): 2, (12, 39): 1}),
            'orbit size histogram differs')
    # A separate incidence count uses rooted circuits BEFORE translation expansion.
    for weight, total in histogram.items():
        rooted_count = sum(s['circuit_weight_histogram'].get(weight, 0)
                           for s in report['enumeration'] if s['L'] == ELL_TILDE and s['sector'] == 'Z')
        require(ELL_TILDE * rooted_count == weight * total, 'root-incidence orbit count mismatch')
    require(any(poly(r['flat_support']) in {translate(tz, j, ELL_TILDE)
                                            for j in range(ELL_TILDE)} for r in orbits),
            'tau(z) orbit missing')
    cb = circuit_serialization(full_z_circuits, ELL_TILDE)
    report['circuits'] = dict(histogram=histogram, total=len(full_z_circuits),
                               sha256=hashlib.sha256(cb).hexdigest(), orbits=orbits)
    for i, rec in enumerate(orbits, 1):
        print(f'ORBIT {i} ' + json.dumps(rec, sort_keys=True, separators=(',', ':')))
    print('CIRCUIT_SET_SHA256 ' + report['circuits']['sha256'])
    # Odd weights are excluded by the exact column-degree parity already checked.
    report['result'] = dict(base=[78, 4, 6], cover=[156, 4, 14], upper_bound_false=True)
    print('DISTANCES: dX=dZ=6; cover_dX=cover_dZ=14; 14>2*6')
    if out:
        (out / 'circuits.txt').write_bytes(cb)
        (out / 'report_bitset.json').write_text(json.dumps(report, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(TOKEN)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', help='optional directory for independently generated artifacts')
    args = parser.parse_args()
    main(args.output_dir)
