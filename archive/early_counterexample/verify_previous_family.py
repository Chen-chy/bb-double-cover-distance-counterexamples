#!/usr/bin/env python3
"""Exact certificates for the support--Bockstein counterexample family.

Standard library only. All arithmetic is exact. This is NOT a counterexample
against d_cover <= 2*d_base. For every family index j >= 2, the proof establishes
[[18j,4,4]] -> [[36j,4,6]], while every minimum base logical has rho=2j-1.
The parameter-uniform part of the rho proof is the finite min-plus matrix
identity verified by check_min_plus_certificate(). Finite checks below are
independent consistency checks, not a substitute for that identity/proof.
"""
from itertools import combinations
from collections import defaultdict
from math import comb


def bits(x):
    while x:
        b = x & -x
        yield b.bit_length() - 1
        x ^= b


def apply(cols, x):
    out = 0
    for i in bits(x):
        out ^= cols[i]
    return out


class Span:
    def __init__(self, vectors=()):
        self.rows = {}
        for v in vectors:
            self.add(v)

    def add(self, v):
        while v:
            p = v.bit_length() - 1
            if p in self.rows:
                v ^= self.rows[p]
            else:
                self.rows[p] = v
                return True
        return False

    def reduce(self, v):
        for p in sorted(self.rows, reverse=True):
            if (v >> p) & 1:
                v ^= self.rows[p]
        return v

    def __len__(self):
        return len(self.rows)


def kernel(cols):
    rows, witnesses, out = {}, {}, []
    for i, col in enumerate(cols):
        v, w = col, 1 << i
        while v:
            p = v.bit_length() - 1
            if p in rows:
                v ^= rows[p]
                w ^= witnesses[p]
            else:
                rows[p], witnesses[p] = v, w
                break
        else:
            out.append(w)
    return out


def polys(exponents):
    v = 0
    for e in exponents:
        v ^= 1 << e
    return v


def mul_cyclic(a, b, length):
    out = 0
    mask = (1 << length) - 1
    for i in bits(a):
        out ^= ((b << i) | (b >> (length - i))) & mask if i else b
    return out


def poly_mod(p, g):
    while p.bit_length() >= g.bit_length():
        p ^= g << (p.bit_length() - g.bit_length())
    return p


def chain(A, B, L, M=1):
    def columns(terms):
        out = []
        for i in range(L):
            for j in range(M):
                col = 0
                for a, b in terms:
                    col ^= 1 << (((a + i) % L) * M + (b + j) % M)
                out.append(col)
        return out
    aa, bb = columns(A), columns(B)
    n0 = L * M
    return aa + bb, [b | (a << n0) for a, b in zip(aa, bb)]


def operators(A_lift, B_lift, L, M=1):
    """Coefficient matrices d, D, E in the low-sheet t-adic basis."""
    def columns(terms):
        out = [[], [], []]
        for i in range(L):
            for j in range(M):
                v = [0, 0, 0]
                for a, b in terms:
                    e = 1 << (((a + i) % L) * M + (b + j) % M)
                    carry = (a + i) // L
                    assert 0 <= carry <= 2
                    v[0] ^= e
                    if carry & 1:
                        v[1] ^= e
                    if carry & 2:
                        v[2] ^= e
                for k in range(3):
                    out[k].append(v[k])
        return out
    aa, bb = columns(A_lift), columns(B_lift)
    n0 = L * M
    return [(aa[k] + bb[k], [b | (a << n0) for a, b in zip(aa[k], bb[k])])
            for k in range(3)]


def check_coefficient_identities(ops):
    H, G = ops[0]
    D1, D2 = ops[1]
    E1, E2 = ops[2]
    for i in range(len(G)):
        assert apply(H, G[i]) == 0
        assert apply(H, D2[i]) ^ apply(D1, G[i]) == 0
        assert apply(H, E2[i]) ^ apply(D1, D2[i]) ^ apply(E1, G[i]) == 0
        assert apply(D1, E2[i]) ^ apply(E1, D2[i]) == 0
        assert apply(E1, E2[i]) == 0


def translate(z, N, shift):
    mask = (1 << N) - 1
    def rot(v):
        return ((v << shift) | (v >> (N - shift))) & mask if shift else v
    return rot(z & mask) | (rot(z >> N) << N)


def zero_four_cycles(H):
    sums = defaultdict(list)
    for i, j in combinations(range(len(H)), 2):
        sums[H[i] ^ H[j]].append((1 << i) | (1 << j))
    out = set()
    for pairs in sums.values():
        for a, b in combinations(pairs, 2):
            z = a ^ b
            if z.bit_count() == 4:
                out.add(z)
    return out, sums


def transfer(z, N):
    mask = (1 << N) - 1
    u, v = z & mask, z >> N
    return u | (u << N) | (v << (2 * N)) | (v << (3 * N))


def normal_lift(z, r, N):
    mask = (1 << N) - 1
    low, high = z ^ r, r
    return ((low & mask) | ((high & mask) << N)
            | ((low >> N) << (2 * N)) | ((high >> N) << (3 * N)))


def project(z, N):
    mask = (1 << N) - 1
    return ((z & mask) ^ ((z >> N) & mask)
            | ((((z >> (2 * N)) & mask) ^ ((z >> (3 * N)) & mask)) << N))


def f4mul(a, b):
    # w^2 = w+1; 0,1,w,w^2 are encoded as 0,1,2,3.
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 4:
            a ^= 7
    return out


def wpow(i):
    return (1, 2, 3)[i % 3]


def mp(A, B):
    return [[min(A[i][k] + B[k][j] for k in range(4)) for j in range(4)]
            for i in range(4)]


def mp_power(A, k):
    out = [[0 if i == j else 10**9 for j in range(4)] for i in range(4)]
    for _ in range(k):
        out = mp(out, A)
    return out


def transition(i):
    out = []
    for p in range(4):
        row = []
        for v in range(4):
            e = f4mul(wpow(i + 3), v)
            syndrome = 0 if i == 1 else wpow(i + 2)
            f = syndrome ^ f4mul(wpow(i + 2), p)
            b = f4mul(2, f ^ e)
            a = e ^ b
            free_a = {0, 2} if i == 0 else ({0, 1} if i == 1 else {0})
            free_b = {0, 1} if i in (0, 1) else {0}
            row.append(int(a not in free_a) + int(b not in free_b))
        out.append(row)
    return out


def check_min_plus_certificate():
    M = [[2, 2, 1, 1], [0, 2, 2, 2], [2, 1, 1, 2], [2, 1, 2, 1]]
    N = [[1, 2, 2, 1], [0, 1, 1, 2], [2, 1, 1, 0], [1, 2, 2, 1]]
    T2 = [[4, 4, 4, 4], [3, 4, 3, 3], [3, 3, 3, 3], [4, 4, 4, 4]]
    assert transition(2) == transition(3) == transition(4) == M
    assert mp(transition(0), transition(1)) == N
    assert mp(N, mp_power(M, 4)) == T2
    assert mp(T2, mp_power(M, 3)) == [[x + 2 for x in row] for row in T2]
    assert min(T2[f4mul(2, v)][v] for v in range(4)) == 3
    # The previous two equalities prove the formula for EVERY j >= 2 by induction.
    for j in range(2, 20):
        Tj = mp(N, mp_power(M, 3 * j - 2))
        assert min(Tj[f4mul(2, v)][v] for v in range(4)) == 2 * j - 1
    print('PARAMETER-UNIFORM F4/MIN-PLUS CERTIFICATE: PASS')


def check_family(j):
    q, L = 3 * j, 9 * j
    A = [(0, 0), (q - 1, 0), (2 * q - 2, 0)]
    B = [(0, 0), (3 * q - 2, 0), (3 * q - 1, 0)]
    AA = [(0, 0), (q - 1, 0), (5 * q - 2, 0)]
    H, G = chain(A, B, L)
    HC, GC = chain(AA, B, 2 * L)
    ops = operators(AA, B, L)
    assert ops[0] == (H, G)
    check_coefficient_identities(ops)
    assert 2 * L - len(Span(H)) - len(Span(G)) == 4
    assert 4 * L - len(Span(HC)) - len(Span(GC)) == 4
    assert len(set(H)) == 2 * L
    z = polys([1, q]) | (polys([0, 1]) << L)
    assert apply(H, z) == 0 and Span(G).reduce(z) != 0
    minima, _ = zero_four_cycles(H)
    assert minima == {translate(z, L, a) for a in range(L)}
    assert all(Span(GC).reduce(transfer(v, L)) == 0 for v in minima)
    r = polys(range(3, q, 3)) ^ polys(range(q + 2, 2 * q, 3))
    syndrome = polys([0, 2 * q - 1, 3 * q - 2])
    assert apply(ops[1][0], z) == syndrome == apply(H, r)
    assert (r & ~z).bit_count() == 2 * j - 1
    lifted = normal_lift(z, r, L)
    assert apply(HC, lifted) == 0 and project(lifted, L) == z
    assert lifted.bit_count() == 4 * j + 2
    p = polys([0, 2 * q, 4 * q])
    w = p | (p << (2 * L))
    assert w.bit_count() == 6 and apply(HC, w) == 0
    assert Span(GC).reduce(w) != 0
    assert len(set(HC)) == 4 * L
    four_cover, pairs_cover = zero_four_cycles(HC)
    assert not four_cover
    assert len(pairs_cover) == comb(4 * L, 2)
    z6 = project(w, L)
    assert z6.bit_count() == 6 and Span(G).reduce(z6) != 0
    # Three odd-weight columns per qubit imply that odd-weight cycles cannot occur.
    assert all(c.bit_count() == 3 for c in H + HC)
    if j == 2:
        # A direct quotient certificate that rho(z) >= 3, independent of min-plus.
        S = list(bits(z))
        quotient = Span([H[i] for i in S])
        target = quotient.reduce(syndrome)
        values = {quotient.reduce(c) for c in H}
        assert target == 0x41 and not values.intersection({target ^ x for x in values})
        # Explicit first- and second-order Bockstein preimage/correction audit.
        h, s = 0x36db6, 0x512b
        assert apply(G, h) == 0
        assert apply(ops[1][1], h) ^ apply(G, s) == z
        r0 = apply(ops[2][1], h) ^ apply(ops[1][1], s)
        assert apply(H, r0) == syndrome
        assert apply(H, r ^ r0) == 0
        # The six-weight projection is homologous to a translated minimum.
        s_hom = polys([2, 3, 4, 6, 7, 8, 9, 11, 12])
        assert apply(G, s_hom) == z6 ^ translate(z, L, 1)
    print(f'j={j}: [[{2*L},4,4]] -> [[{4*L},4,6]], '
          f'{len(minima)} minimum Z representatives, rho={2*j-1}, '
          f'minimum literal-projection lift weight={4*j+2}: PASS')


def check_30_60_example():
    L, M = 5, 3
    AA = [(7, 0), (6, 1), (1, 2)]
    BB = [(9, 0), (4, 1), (8, 2)]
    ops = operators(AA, BB, L, M)
    check_coefficient_identities(ops)
    H, G = ops[0]
    z = polys([0, 1, 25, 26])
    r = polys([1, 2])
    assert apply(H, z) == 0 and Span(G).reduce(z) != 0
    assert apply(ops[1][0], z) == apply(H, r)
    assert (r & ~z).bit_count() == 1
    S = list(bits(z))
    assert Span([H[i] for i in S]).reduce(apply(ops[1][0], z)) != 0
    zmin, _ = zero_four_cycles(H)
    assert len(set(H)) == 30 and len(zmin) == 15
    print('[[30,4,4]] -> [[60,4,6]] normal-form test: rho(z)=1: PASS')


if __name__ == '__main__':
    check_min_plus_certificate()
    for j in (2, 3, 4, 5, 6):
        check_family(j)
    check_30_60_example()
    print('ALL EXACT CHECKS PASSED. The support lemma is false; '
          'these examples satisfy d_cover <= 2*d_base.')
