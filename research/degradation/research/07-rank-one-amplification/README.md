# Rank-one amplification verification package

Read `proof.md` first. The global factor-three claim is **not** proved.

Run the independent checks, using the retained lower-bound certificates:

    python verify.py

This needs Python 3.10+ and no third-party packages. It checks the all-degree Bellman lower bounds and exact finite binary boundary spans. It does not execute Dijkstra.

To regenerate the family certificates as well, a C++17 compiler is needed:

    g++ -O3 -std=c++17 trellis.cpp -o trellis
    python generate_family.py
    python verify.py

`core.py` contains exact binary polynomial arithmetic. `try_trellis.py` wraps the certificate generator. `family_certificate.json` contains encoder bases and explicit witnesses; the two `.bin` files hold little-endian unsigned-16-bit Bellman potentials. The checker tests every edge of the corresponding finite-state graphs.

The uniform family is [[2L,4,8]] -> [[4L,4,14]] for odd multiples L of 3 with L>=105. Exactness for all these periods follows from the all-degree certificate plus the cycle-lifting theorem, not from extrapolating the four checked finite instances.
