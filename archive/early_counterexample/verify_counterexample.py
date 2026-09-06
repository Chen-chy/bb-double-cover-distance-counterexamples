#!/usr/bin/env python3
"""Exact counterexample to the BB double-cover upper-bound conjecture.

Requires Python >= 3.10; standard library only; no files or network are used.
Run: python3 verify_counterexample.py

A = 1 + x^8 + x^25; B = 1 + x^2 + x^13.
Base period 39: [[78,4,6]]. Cover period 78: [[156,4,14]].
Both defining polynomials are unchanged by the double cover.

Completeness of the finite distance certificate:
  (1) A minimum non-boundary cycle has circuit support. A proper subcycle
      would either be a smaller non-boundary or could be removed as a boundary.
  (2) Translations are transitive on each qubit block and preserve boundaries.
      It suffices to enumerate circuits containing qubit 0 of either block.
  (3) At a nonzero partial syndrome, an odd check needs an additional incident
      qubit. Branches partition completions according to their first available
      chosen incident qubit. Earlier candidates are forbidden in later branches.
  (4) The only weight prune is popcount(syndrome) > 3 * remaining_qubits:
      each additional column has weight three. A zero syndrome ends the branch;
      this never truncates a proper subset of a circuit.
  (5) Every zero-syndrome leaf is tested directly for membership in the binary
      span of the Z-boundary columns. No logical-label oracle or decoder is used.

The script additionally recovers the full set of circuits of weight <=12,
checks the polynomial witnesses, both X and Z sectors, the killed base class,
and the exact values delta=6, rho=4, mu=14, nu=22 for the stated base class.
"""
from collections import Counter
from itertools import combinations


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def bits(v):
    while v:
        bit = v & -v
        yield bit.bit_length() - 1
        v ^= bit


def polynomial(exponents):
    out = 0
    for e in exponents:
        require(e >= 0, 'negative exponent')
        out ^= 1 << e
    return out


def multiply(a, b):
    out = 0
    for e in bits(a):
        out ^= b << e
    return out


def divmod_poly(a, b):
    require(b != 0, 'division by zero polynomial')
    quotient = 0
    while a and a.bit_length() >= b.bit_length():
        shift = a.bit_length() - b.bit_length()
        quotient ^= 1 << shift
        a ^= b << shift
    return quotient, a


def extended_gcd(a, b):
    r0, r1, s0, s1, t0, t1 = a, b, 1, 0, 0, 1
    while r1:
        q, r = divmod_poly(r0, r1)
        r0, r1 = r1, r
        s0, s1 = s1, s0 ^ multiply(q, s1)
        t0, t1 = t1, t0 ^ multiply(q, t1)
    return r0, s0, t0


def rotate(v, shift, length):
    shift %= length
    mask = (1 << length) - 1
    require(v >= 0 and v <= mask, 'rotation input outside its block')
    return ((v << shift) | (v >> (length - shift))) & mask


def translate(v, shift, length):
    mask = (1 << length) - 1
    return rotate(v & mask, shift, length) | (rotate(v >> length, shift, length) << length)


def action(columns, v):
    out = 0
    for i in bits(v):
        out ^= columns[i]
    return out


class BinarySpan:
    def __init__(self, vectors=()):
        self.rows = {}
        for v in vectors:
            while v:
                p = v.bit_length() - 1
                if p in self.rows:
                    v ^= self.rows[p]
                else:
                    self.rows[p] = v
                    break
        self.pivots = sorted(self.rows, reverse=True)

    def reduce(self, v):
        for p in self.pivots:
            if (v >> p) & 1:
                v ^= self.rows[p]
        return v

    def __len__(self):
        return len(self.rows)


def cyclic_code(length, A, B):
    require(A.bit_length() <= length and B.bit_length() <= length,
            'polynomial outside chosen monomial representatives')
    ma = [rotate(A, i, length) for i in range(length)]
    mb = [rotate(B, i, length) for i in range(length)]
    H = ma + mb
    G = [mb[i] | (ma[i] << length) for i in range(length)]
    require(all(action(H, v) == 0 for v in G), 'CSS commutation failed')
    return H, G


def projection(v, base_length):
    mask = (1 << base_length) - 1
    u0 = v & mask
    u1 = (v >> base_length) & mask
    v0 = (v >> (2 * base_length)) & mask
    v1 = (v >> (3 * base_length)) & mask
    return (u0 ^ u1) | ((v0 ^ v1) << base_length)


def transfer(v, base_length):
    mask = (1 << base_length) - 1
    u, w = v & mask, v >> base_length
    return u | (u << base_length) | (w << (2 * base_length)) | (w << (3 * base_length))


def inversion(v, length):
    out = 0
    for i in bits(v):
        out ^= 1 << ((-i) % length)
    return out


def zx_duality(v, length):
    mask = (1 << length) - 1
    return inversion(v >> length, length) | (inversion(v & mask, length) << length)


def evaluate_class(v, length):
    """For the square-free base ring, evaluation in F2[x]/(1+x+x^2).
    The two coordinates encode the complete H1 class for this specific code.
    """
    mask = (1 << length) - 1
    return divmod_poly(v & mask, 7)[1] | (divmod_poly(v >> length, 7)[1] << 2)


def rooted_search(H, G, bound, root):
    """Exhaustive search containing every circuit of size <=bound through root.
    Returns actual zero-syndrome leaves, not a floating-point bound.
    """
    n = len(H)
    m = max(column.bit_length() for column in H)
    require(0 <= root < n, 'invalid root')
    require(all(column.bit_count() == 3 for column in H), 'column degree is not 3')
    adjacency = [0] * m
    for j, column in enumerate(H):
        for row in bits(column):
            adjacency[row] |= 1 << j
    require(all(v.bit_count() == 6 for v in adjacency), 'check degree is not 6')
    span = BinarySpan(G)
    nodes = 0
    leaves = []
    nonboundaries = []

    def visit(chosen, forbidden, syndrome, weight):
        nonlocal nodes
        nodes += 1
        if syndrome == 0:
            leaves.append(chosen)
            if span.reduce(chosen):
                nonboundaries.append(chosen)
            return
        remaining = bound - weight
        if remaining <= 0 or syndrome.bit_count() > 3 * remaining:
            return
        used = chosen | forbidden
        candidates, smallest_degree = 0, n + 1
        for row in bits(syndrome):
            available = adjacency[row] & ~used
            degree = available.bit_count()
            if degree == 0:
                return
            if degree < smallest_degree:
                candidates, smallest_degree = available, degree
        while candidates:
            bit = candidates & -candidates
            candidates ^= bit
            j = bit.bit_length() - 1
            visit(chosen | bit, forbidden, syndrome ^ H[j], weight + 1)
            forbidden |= bit

    visit(1 << root, 0, H[root], 1)
    return nodes, leaves, nonboundaries


def is_circuit(H, v):
    return (v != 0 and action(H, v) == 0
            and len(BinarySpan(H[i] for i in bits(v))) == v.bit_count() - 1)


def main():
    A, B = polynomial([0, 8, 25]), polynomial([0, 2, 13])
    F, g = polynomial([0, 39]), polynomial([0, 1, 2])
    H, G = cyclic_code(39, A, B)
    HC, GC = cyclic_code(78, A, B)
    require(extended_gcd(A, B)[0] == g, 'gcd(A,B) != 1+x+x^2')
    require(divmod_poly(F, g)[1] == 0, 'g does not divide base period polynomial')
    require((len(BinarySpan(H)), len(BinarySpan(G))) == (37, 37), 'base rank')
    require((len(BinarySpan(HC)), len(BinarySpan(GC))) == (76, 76), 'cover rank')
    print('VALID COVER: unchanged A={0,8,25}, B={0,2,13}; periods 39 -> 78')
    print('RANKS: base (37,37); cover (76,76); k=k_cover=4')

    zL, zR = polynomial([0, 8, 16, 25]), polynomial([0, 11])
    z = zL | (zR << 39)
    c, R = polynomial([2, 11]), polynomial([9, 22, 35, 37])
    wL = zL << 39
    wR = zR ^ multiply(F, R)
    w = wL | (wR << 78)
    require(multiply(A, zL) ^ multiply(B, zR) == multiply(F, c), 'base polynomial identity')
    require(multiply(A, zL) ^ multiply(B, R) ^ c
            == multiply(F, polynomial([0, 2, 9])), 'correction polynomial identity')
    require(action(H, z) == 0 and z.bit_count() == 6, 'base witness')
    require(evaluate_class(z, 39) == 10 and BinarySpan(G).reduce(z) != 0,
            'base witness is not nontrivial')
    require(action(HC, w) == 0 and w.bit_count() == 14, 'cover witness')
    require(projection(w, 39) == z, 'cover witness does not project literally to z')
    require(BinarySpan(GC).reduce(w) != 0, 'cover witness is a boundary')
    print('EXPLICIT WITNESSES: nontrivial base weight 6; cover weight 14 projecting to it')

    # Independent, explicit proof that full transfer of z is a boundary.
    a, ar = divmod_poly(A, g)
    b, br = divmod_poly(B, g)
    f, fr = divmod_poly(F, g)
    require(ar == br == fr == 0, 'polynomial division')
    one, U, V = extended_gcd(a, b)
    require(one == 1 and multiply(U, a) ^ multiply(V, b) == 1, 'Bezout identity')
    require(divmod_poly(c, g)[1] == 0, 'c/g is not polynomial')
    v = divmod_poly(multiply(U, zR) ^ multiply(V, zL), F)[1]
    h = divmod_poly(multiply(f, v), polynomial([0, 78]))[1]
    require(action(GC, h) == transfer(z, 39), 'transfer boundary witness')
    print('KILLED CLASS: explicit h satisfies (B h,A h)=tau(z)')

    expected_stats = {
        ('base', 'Z', 0): (36, {}),
        ('base', 'Z', 39): (36, {}),
        ('cover', 'Z', 0): (985001, {6: 3, 10: 30, 12: 66}),
        ('cover', 'Z', 78): (991809, {6: 3, 10: 30, 12: 56}),
        ('base', 'X', 0): (36, {}),
        ('base', 'X', 39): (36, {}),
        ('cover', 'X', 0): (941501, {6: 3, 10: 30, 12: 58}),
        ('cover', 'X', 78): (894576, {6: 3, 10: 30, 12: 58}),
    }
    cover_circuits = set()
    for name, length, bound, witness in [('base', 39, 4, z), ('cover', 78, 12, w)]:
        hz, gz = cyclic_code(length, A, B)
        hx, gx = cyclic_code(length, inversion(B, length), inversion(A, length))
        xw = zx_duality(witness, length)
        require(action(hx, xw) == 0 and BinarySpan(gx).reduce(xw), 'X witness')
        for sector, hh, gg in [('Z', hz, gz), ('X', hx, gx)]:
            for root in [0, length]:
                nodes, leaves, logicals = rooted_search(hh, gg, bound, root)
                histogram = dict(sorted(Counter(v.bit_count() for v in leaves).items()))
                require(not logicals, 'a forbidden low-weight logical was found')
                require((nodes, histogram) == expected_stats[(name, sector, root)],
                        'reproducibility statistics differ')
                print(f'{name.upper()} {sector} root={root}: nodes={nodes}; '
                      f'zero_leaves={histogram}; nonboundaries=0; COMPLETE')
                if name == 'cover' and sector == 'Z':
                    for v in leaves:
                        if is_circuit(hh, v):
                            cover_circuits.update(translate(v, j, length) for j in range(length))

    # A compact description of every cover circuit of size <=12.
    seeds = [GC[0]]
    seeds += [GC[0] ^ GC[d] for d in [2, 8, 11, 13, 17, 25]]
    seeds += [action(GC, A), action(GC, B), transfer(z, 39)]
    require(all(is_circuit(HC, v) for v in seeds), 'listed seed is not a circuit')
    expected_circuits = {translate(v, j, 78) for v in seeds for j in range(78)}
    require(cover_circuits == expected_circuits, 'circuit classification differs')
    histogram = dict(sorted(Counter(v.bit_count() for v in cover_circuits).items()))
    require(histogram == {6: 78, 10: 468, 12: 195}, 'circuit counts')
    print(f'COMPLETE COVER CIRCUIT CLASSIFICATION through weight 12: {histogram}')

    # All minimum base cycles: exactly 39 logical representatives, three classes.
    minimum_words = set()
    for root in [0, 39]:
        _, _, logicals = rooted_search(H, G, 6, root)
        minimum_words.update(translate(v, j, 39) for v in logicals for j in range(39))
    require(minimum_words == {translate(z, j, 39) for j in range(39)}, 'minimum base words')
    class_counts = Counter(evaluate_class(v, 39) for v in minimum_words)
    require(class_counts == Counter({5: 13, 10: 13, 15: 13}), 'minimum base classes')
    require(all(BinarySpan(GC).reduce(transfer(v, 39)) == 0 for v in minimum_words),
            'some minimum transfer survives')
    print('MINIMUM BASE LOGICALS: 39 translates; three nonzero classes; all transfers killed')

    # rho(z)=4: eliminate the free support of z, exhaust all outside corrections <=3.
    support = set(bits(z))
    inside = BinarySpan(H[i] for i in support)
    # Here the lifted polynomials have degree <39, so D1 is exactly the carry part.
    D1 = [(multiply(A if i < 39 else B, 1 << (i % 39)) >> 39)
          for i in range(78)]
    require(action(D1, z) == c, 'Bockstein syndrome')
    target = inside.reduce(c)
    outside = [inside.reduce(H[i]) for i in range(78) if i not in support]
    tested = []
    for weight in range(4):
        count = 0
        for subset in combinations(range(len(outside)), weight):
            syndrome = 0
            for i in subset:
                syndrome ^= outside[i]
            require(syndrome != target, 'rho <=3 found')
            count += 1
        tested.append(count)
    r = zL | (R << 39)
    require(action(H, r) == c and (r & ~z).bit_count() == 4, 'rho=4 witness')
    print(f'RHO: outside weights 0..3 exhaustively excluded; counts={tested}; rho=4')

    # nu(alpha)=22. A low-sheet cover cycle has degree <78 before reduction, so
    # A*u+B*v=0 as polynomials, hence (u,v)=(b*f,a*f), deg f<16. This is exhaustive.
    require(a.bit_length() == 24 and b.bit_length() == 12, 'cofactor degrees')
    nu = {}
    for f0 in range(1 << 16):
        u, v0 = multiply(b, f0), multiply(a, f0)
        require(u.bit_length() <= 39 and v0.bit_length() <= 39, 'low-sheet degree')
        vv = u | (v0 << 39)
        require(action(H, vv) == 0 and action(D1, vv) == 0, 'low-sheet cycle')
        label = evaluate_class(vv, 39)
        weight = vv.bit_count()
        nu[label] = min(nu.get(label, 10000), weight)
    require(nu == {0: 0, 5: 22, 10: 22, 15: 22}, 'nu table differs')
    print('NU: all 65536 polynomial solutions checked; each nonzero projectable class has nu=22')
    print('CLASS METRICS: delta=6, rho=4, mu=14, nu=22')
    print('CERTIFIED: [[78,4,6]] -> [[156,4,14]]; 14 > 2*6.')


if __name__ == '__main__':
    main()
