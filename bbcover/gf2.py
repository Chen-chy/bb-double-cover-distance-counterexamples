"""Small exact GF(2) routines using nonnegative Python integer bit vectors."""
from collections.abc import Iterable


def bits(vector: int) -> Iterable[int]:
    if not isinstance(vector, int) or vector < 0:
        raise ValueError("A bit vector must be a nonnegative integer")
    while vector:
        bit = vector & -vector
        yield bit.bit_length() - 1
        vector ^= bit


def from_support(support: Iterable[int]) -> int:
    """Construct a binary polynomial; repeated indices cancel over GF(2)."""
    result = 0
    for index in support:
        if not isinstance(index, int) or index < 0:
            raise ValueError("Support indices must be nonnegative integers")
        result ^= 1 << index
    return result


def echelon(vectors: Iterable[int]) -> dict[int, int]:
    pivots: dict[int, int] = {}
    for vector in vectors:
        if not isinstance(vector, int) or vector < 0:
            raise ValueError("A bit vector must be a nonnegative integer")
        while vector:
            p = vector.bit_length() - 1
            if p not in pivots:
                pivots[p] = vector
                break
            vector ^= pivots[p]
    return pivots


def rank(vectors: Iterable[int]) -> int:
    return len(echelon(vectors))


def solve(columns: Iterable[int], target: int) -> int | None:
    """Return coefficient bits for a column-span representation, or None."""
    if not isinstance(target, int) or target < 0:
        raise ValueError("Target must be a nonnegative integer")
    pivots: dict[int, tuple[int, int]] = {}
    for i, vector in enumerate(columns):
        if not isinstance(vector, int) or vector < 0:
            raise ValueError("A bit vector must be a nonnegative integer")
        coefficients = 1 << i
        while vector:
            p = vector.bit_length() - 1
            if p not in pivots:
                pivots[p] = (vector, coefficients)
                break
            v, c = pivots[p]
            vector ^= v
            coefficients ^= c
    result = 0
    while target:
        p = target.bit_length() - 1
        if p not in pivots:
            return None
        v, c = pivots[p]
        target ^= v
        result ^= c
    return result
