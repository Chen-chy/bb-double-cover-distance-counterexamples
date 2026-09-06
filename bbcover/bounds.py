"""Integer-safe endpoints of the proved cubic interval (paper, Theorem 3.1).

The optional size cap is the elementary d2<=n. The sharper analytic ambient cap
is stated in the paper, not rounded with potentially unsafe floating arithmetic.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class DistanceInterval:
    lower: int
    upper: int
    source_distance: int
    base_length: int | None
    full_dimension_transfer_used: bool


def cubic_interval(d: int, n: int | None = None, *, k: int | None = None,
                   k2: int | None = None) -> DistanceInterval:
    """Return even endpoints using d<=4*d2**3 and d2<=8*d**3.

    Inputs describe a positive-dimensional strict-trinomial abelian double cover.
    They are not sufficient to prove that such a code exists. If supplied, n is
    the BASE number of qubits, and k/k2 are binary logical dimensions.
    """
    if type(d) is not int or d < 2 or d % 2:
        raise ValueError("d must be a positive even integer at least two")
    if n is not None and (type(n) is not int or n < 2 or n % 2 or 2*d > n):
        raise ValueError("n must be even and satisfy d<=n/2")
    if (k is None) != (k2 is None):
        raise ValueError("Supply both k and k2, or neither")
    transfer = False
    if k is not None:
        if any(type(x) is not int or x < 2 or x % 2 for x in (k, k2)):
            raise ValueError("k and k2 must be positive even integers")
        if not k <= k2 <= 2*k:
            raise ValueError("A double cover must satisfy k<=k2<=2k")
        if n is not None and k > n:
            raise ValueError("k cannot exceed the number of base qubits")
        transfer = (k2 == 2*k)
    # Find the smallest h>=1 such that 4*(2*h)^3>=d, exactly.
    lo, hi = 1, 1
    while 32 * hi**3 < d:
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if 32 * mid**3 >= d:
            hi = mid
        else:
            lo = mid + 1
    upper = 8 * d**3
    if n is not None:
        upper = min(upper, n)
    if transfer:
        upper = min(upper, 2*d)
    upper -= upper % 2
    return DistanceInterval(2*lo, upper, d, n, transfer)
