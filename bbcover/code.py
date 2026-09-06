"""Rectangular strict-trinomial BB codes in the physical monomial basis.

Coordinate (i,j) has index i*m+j. The right block starts at ell*m.
HX=(M_A M_B), HZ=(M_B^T M_A^T); d1(u,v)=Au+Bv, d2(h)=(Bh,Ah).
This module constructs and audits matrices; it is not a generic distance oracle.
"""
from dataclasses import dataclass
from functools import cached_property
from collections.abc import Iterable
from .gf2 import bits, from_support, rank, solve

Term = tuple[int, int]


@dataclass(frozen=True)
class BBCode:
    ell: int
    m: int
    A: tuple[Term, ...]
    B: tuple[Term, ...]

    def __post_init__(self) -> None:
        if any(type(v) is not int or v < 1 for v in (self.ell, self.m)):
            raise ValueError("Periods must be positive integers")
        for name in ("A", "B"):
            raw = getattr(self, name)
            if len(raw) != 3 or any(len(t) != 2 or any(type(x) is not int for x in t)
                                    for t in raw):
                raise ValueError("Each check must contain three integer exponent pairs")
            terms = tuple((i % self.ell, j % self.m) for i, j in raw)
            if len(set(terms)) != 3:
                raise ValueError("Check terms must remain distinct modulo the periods")
            object.__setattr__(self, name, terms)

    @property
    def order(self) -> int:
        return self.ell * self.m

    @property
    def n(self) -> int:
        return 2 * self.order

    def index(self, term: Term) -> int:
        i, j = term
        return (i % self.ell) * self.m + j % self.m

    def monomials(self, terms: Iterable[Term]) -> int:
        return from_support(self.index(t) for t in terms)

    def _check_vector(self, vector: int, length: int) -> None:
        if type(vector) is not int or vector < 0 or vector.bit_length() > length:
            raise ValueError(f"Expected a nonnegative bit vector of length at most {length}")

    def multiply(self, terms: Iterable[Term], vector: int) -> int:
        self._check_vector(vector, self.order)
        shifts = tuple(terms)
        result = 0
        for t in bits(vector):
            i, j = divmod(t, self.m)
            for a, b in shifts:
                result ^= 1 << self.index((i + a, j + b))
        return result

    def chain(self, left: Iterable[Term], right: Iterable[Term]) -> int:
        return self.monomials(left) | (self.monomials(right) << self.order)

    def syndrome(self, vector: int) -> int:
        self._check_vector(vector, self.n)
        mask = (1 << self.order) - 1
        return self.multiply(self.A, vector & mask) ^ self.multiply(self.B, vector >> self.order)

    def boundary(self, h: int) -> int:
        self._check_vector(h, self.order)
        return self.multiply(self.B, h) | (self.multiply(self.A, h) << self.order)

    @cached_property
    def syndrome_columns(self) -> tuple[int, ...]:
        return tuple(self.multiply(P, 1 << j) for P in (self.A, self.B)
                     for j in range(self.order))

    @cached_property
    def boundary_columns(self) -> tuple[int, ...]:
        return tuple(self.boundary(1 << j) for j in range(self.order))

    @cached_property
    def hx_rows(self) -> tuple[int, ...]:
        rows = [0] * self.order
        for j, column in enumerate(self.syndrome_columns):
            for i in bits(column):
                rows[i] |= 1 << j
        return tuple(rows)

    @property
    def hz_rows(self) -> tuple[int, ...]:
        return self.boundary_columns

    @property
    def k(self) -> int:
        return self.n - rank(self.hx_rows) - rank(self.hz_rows)

    def boundary_preimage(self, vector: int) -> int | None:
        self._check_vector(vector, self.n)
        return solve(self.boundary_columns, vector)

    def is_logical(self, vector: int) -> bool:
        return self.syndrome(vector) == 0 and self.boundary_preimage(vector) is None

    def inversion_swap(self, vector: int) -> int:
        self._check_vector(vector, self.n)
        out = 0
        for t in bits(vector):
            block, pos = divmod(t, self.order)
            i, j = divmod(pos, self.m)
            out ^= 1 << ((1 - block) * self.order + self.index((-i, -j)))
        return out

    @cached_property
    def graph(self) -> tuple[frozenset[int], ...]:
        """Four vertex types: left, right, X check, Z check; include all edges."""
        graph: list[set[int]] = [set() for _ in range(4 * self.order)]
        for offset, rows in ((2 * self.order, self.hx_rows), (3 * self.order, self.hz_rows)):
            for i, row in enumerate(rows):
                for qubit in bits(row):
                    graph[offset + i].add(qubit)
                    graph[qubit].add(offset + i)
        return tuple(frozenset(v) for v in graph)

    def is_connected(self) -> bool:
        seen = {0}
        stack = [0]
        while stack:
            for v in self.graph[stack.pop()]:
                if v not in seen:
                    seen.add(v)
                    stack.append(v)
        return len(seen) == 4 * self.order

    def matrix_bytes(self, sector: str) -> bytes:
        if sector not in ("X", "Z"):
            raise ValueError("Sector must be X or Z")
        rows = self.hx_rows if sector == "X" else self.hz_rows
        text = f"GF2MATRIX v1\n{self.order} {self.n}\n"
        text += "".join("".join(str((v >> j) & 1) for j in range(self.n)) + "\n" for v in rows)
        return text.encode("ascii")


def validate_double_cover(base: BBCode, cover: BBCode) -> dict[str, int | bool]:
    """Check term projection and every full Tanner-graph neighborhood.

    This checks the rectangular coordinate-reduction covering map, not arbitrary
    group presentations. Raises ValueError rather than accepting collapsed terms.
    """
    if cover.ell % base.ell or cover.m % base.m or cover.order != 2 * base.order:
        raise ValueError("The lifted periods must define a degree-two quotient")
    for name in ("A", "B"):
        projected = tuple((i % base.ell, j % base.m) for i, j in getattr(cover, name))
        if len(set(projected)) != 3 or set(projected) != set(getattr(base, name)):
            raise ValueError("The three terms do not project bijectively to the base check")

    def project(v: int) -> int:
        kind, pos = divmod(v, cover.order)
        i, j = divmod(pos, cover.m)
        return kind * base.order + base.index((i, j))

    fibres = [0] * (4 * base.order)
    for v, neighbors in enumerate(cover.graph):
        pv = project(v)
        fibres[pv] += 1
        image = {project(u) for u in neighbors}
        if len(image) != len(neighbors) or image != set(base.graph[pv]):
            raise ValueError("The full Tanner-neighborhood map is not a bijection")
    if set(fibres) != {2}:
        raise ValueError("Not all graph vertices have exactly two preimages")
    return {"degree": 2, "term_matching": True, "neighborhood_bijections": True,
            "vertices_checked": len(cover.graph), "base_connected": base.is_connected(),
            "cover_connected": cover.is_connected()}
