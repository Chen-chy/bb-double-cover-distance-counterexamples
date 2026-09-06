"""Exact sparse binary Laurent arithmetic. No external dependencies."""
from __future__ import annotations
from collections.abc import Iterable

Poly = frozenset[int]
ZERO: Poly = frozenset()
ONE: Poly = frozenset({0})

def poly(exponents: Iterable[int]) -> Poly:
    out: set[int] = set()
    for e in exponents:
        if not isinstance(e, int):
            raise TypeError('Exponents must be integers')
        out.symmetric_difference_update((e,))
    return frozenset(out)

def add(*polynomials: Poly) -> Poly:
    out: set[int] = set()
    for p in polynomials:
        out.symmetric_difference_update(p)
    return frozenset(out)

def shift(p: Poly, exponent: int) -> Poly:
    return frozenset(i + exponent for i in p)

def mul(p: Poly, q: Poly) -> Poly:
    return add(*(shift(p, j) for j in q))

def square(p: Poly) -> Poly:
    return frozenset(2 * i for i in p)

def normalized(p: Poly) -> Poly:
    return shift(p, -min(p)) if p else p

def remainder(p: Poly, q: Poly) -> Poly:
    if not q:
        raise ZeroDivisionError
    q = normalized(q)
    p = normalized(p)
    result = set(p)
    degree = max(q)
    while result and max(result) >= degree:
        k = max(result) - degree
        result.symmetric_difference_update(i + k for i in q)
    return frozenset(result)

def gcd(p: Poly, q: Poly) -> Poly:
    p, q = normalized(p), normalized(q)
    while q:
        p, q = q, remainder(p, q)
    return normalized(p)

def divide(p: Poly, q: Poly) -> Poly:
    """Return an exact Laurent quotient, raising ValueError otherwise."""
    if not q:
        raise ZeroDivisionError
    if not p:
        return ZERO
    offset = min(p) - min(q)
    rest = set(normalized(p))
    qq = normalized(q)
    degree = max(qq)
    answer: set[int] = set()
    while rest and max(rest) >= degree:
        k = max(rest) - degree
        answer.symmetric_difference_update((k,))
        rest.symmetric_difference_update(i + k for i in qq)
    if rest:
        raise ValueError('Not exactly divisible')
    return shift(frozenset(answer), offset)
