"""Independent Python exact search; polynomial-normal-form boundary test.

This uses the same proved circuit-completion principle as circuit_search.cpp,
but integer bitsets, a different row/column ordering, and no Gaussian-elimination
boundary oracle. Run: python independent_search.py 78 12
"""
import json
import sys
import time
from algebra import BB, poly, gcd, quo, egcd, cmul, mul, mod, terms


def certify_seed(period: int, limit: int) -> dict:
    if period not in (39, 78):
        raise ValueError('This independent check is for the seed periods 39 and 78.')
    A, B = poly([0, 8, 25]), poly([0, 2, 13])
    D = gcd(A, B)
    a, b = quo(A, D), quo(B, D)
    one, s, t = egcd(a, b)
    assert one == 1
    F = (1 << period) | 1
    g = gcd(D, F)
    code = BB(period, A, B)
    n = 2 * period
    all_bits = (1 << n) - 1
    incident = [0] * period
    for col, syndrome in enumerate(code.cols):
        while syndrome:
            bit = syndrome & -syndrome
            incident[bit.bit_length()-1] |= 1 << col
            syndrome ^= bit
    nodes = closed = 0
    witness = None

    def boundary_test(word: int) -> bool:
        # Normal-form coordinates, independent of code.bas / Gaussian elimination.
        u, v = word & code.mask, word >> period
        q = cmul(a, u, period) ^ cmul(b, v, period)
        r = mod(mul(t, u) ^ mul(s, v), g)
        return q == 0 and r == 0

    def visit(word: int, syndrome: int, allowed: int, weight: int) -> bool:
        nonlocal nodes, closed, witness
        nodes += 1
        if syndrome == 0:
            closed += 1
            if not boundary_test(word):
                witness = word
                return True
            return False
        remaining = limit - weight
        if remaining <= 0 or syndrome.bit_count() > 3 * remaining:
            return False
        # Opposite tie-breaking and branch order to the C++ implementation.
        rows = syndrome
        choices = None
        best = n + 1
        while rows:
            row = rows.bit_length() - 1
            rows ^= 1 << row
            available = incident[row] & allowed
            size = available.bit_count()
            if size == 0:
                return False
            if size < best:
                best, choices = size, available
        while choices:
            col = choices.bit_length() - 1
            bit = 1 << col
            choices ^= bit
            allowed &= ~bit
            if visit(word | bit, syndrome ^ code.cols[col], allowed, weight + 1):
                return True
        return False

    start = time.perf_counter()
    for root in (0, period):
        allowed = all_bits ^ (1 << root)
        if root == period:
            allowed &= ~code.mask
        if visit(1 << root, code.cols[root], allowed, 1):
            break
    result = dict(L=period, k=code.k, max_weight=limit, found=witness is not None,
                  nodes=nodes, closed_cycles=closed, seconds=time.perf_counter()-start)
    if witness is not None:
        assert code.logical(witness)  # Additional Gaussian oracle cross-check.
        result.update(weight=witness.bit_count(), u=terms(witness & code.mask),
                      v=terms(witness >> period))
    return result


if __name__ == '__main__':
    L = int(sys.argv[1]) if len(sys.argv) > 1 else 78
    bound = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    print(json.dumps(certify_seed(L, bound)))
