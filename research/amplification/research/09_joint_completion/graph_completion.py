"""Full-message signed-cut normal form and exact odd-vertex elimination.

Weights and supports are universal Laurent weights, never finite-period
weights. The elimination is exact for fixed message and even boundary field;
it does not minimize the remaining message/even-field variables.
"""
from __future__ import annotations
from dataclasses import dataclass
from laurent import Poly, ONE, add, shift, mul, square, gcd, divide, poly

@dataclass(frozen=True)
class Resonance:
    r: int
    s: int
    g: int

    def __post_init__(self) -> None:
        if self.r % 2 != 1 or self.g <= 0:
            raise ValueError('Require r odd and g positive')
        if len(self.A) != 3 or len(self.B) != 3:
            raise ValueError('Require strict trinomials')

    @property
    def A(self) -> Poly:
        return poly((0, self.r, 2 * self.s))

    @property
    def B(self) -> Poly:
        return poly((0, self.r + 4 * self.g, 2 * self.s + 2 * self.g))

    @property
    def e(self) -> Poly:
        return gcd(self.A, poly((0, self.g)))

    @property
    def j(self) -> Poly:
        return gcd(self.A, poly((0, self.r + 2 * self.g)))

    @property
    def G(self) -> Poly:
        return mul(square(self.e), self.j)

    @property
    def steps(self) -> tuple[int, int]:
        return self.r - 2 * self.s, self.r - 2 * self.s + 2 * self.g

    def coefficients(self) -> tuple[Poly, Poly, Poly]:
        A, B, G = self.A, self.B, self.G
        return (divide(add(mul(A, B), A, B), G),
                divide(add(A, B), G), divide(square(A), G))

    def physical(self, f: Poly, h: Poly) -> tuple[Poly, Poly, Poly, Poly]:
        p, q, r = self.coefficients()
        return (add(mul(p, f), mul(add(self.B, ONE), h)),
                add(mul(q, f), h),
                add(mul(r, f), mul(add(self.A, ONE), h)), h)

    def graph_data(self, f: Poly) -> tuple[Poly, Poly, Poly]:
        p, q, r = self.coefficients()
        # alpha labels b-edges, beta labels a-edges, sigma is the vertex source.
        return (shift(mul(p, f), -2 * self.s - 2 * self.g),
                shift(mul(r, f), -2 * self.s), mul(q, f))

    def energy(self, f: Poly, h: Poly) -> int:
        alpha, beta, sigma = self.graph_data(f)
        a, b = self.steps
        return (len(add(alpha, h, shift(h, b)))
                + len(add(beta, h, shift(h, a)))
                + len(add(sigma, h)) + len(h))

    def eliminate_odd(self, f: Poly, even: Poly) -> tuple[int, Poly, dict[int, int]]:
        if any(i % 2 for i in even):
            raise ValueError('The retained boundary field must have even support')
        alpha, beta, sigma = self.graph_data(f)
        a, b = self.steps
        sites = set(sigma)
        sites.update(alpha); sites.update(shift(alpha, -b))
        sites.update(beta); sites.update(shift(beta, -a))
        for step in (a, b):
            sites.update(shift(even, step)); sites.update(shift(even, -step))
        odd: set[int] = set()
        votes: dict[int, int] = {}
        cost = len(add(frozenset(i for i in sigma if i % 2 == 0), even)) + len(even)
        for i in sorted(x for x in sites if x % 2):
            k = (int((i in alpha) ^ (i - b in even))
                 + int((i + b in alpha) ^ (i + b in even))
                 + int((i in beta) ^ (i - a in even))
                 + int((i + a in beta) ^ (i + a in even))
                 + int(i in sigma))
            votes[i] = k  # the sixth vote is always zero
            cost += min(k, 6 - k)
            if k > 3:
                odd.add(i)
        h = add(even, frozenset(odd))
        assert self.energy(f, h) == cost
        return cost, h, votes
