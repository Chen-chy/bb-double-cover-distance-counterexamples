# Strict-trinomial degradation: a uniform cubic theorem

Read `proof.md` for the symbolic proof of

    d <= 4 d_2^3

and the resulting lower scale

    gamma_3(N) >= c_0 / sqrt(N),
    c_0 = pi * 3^(1/6) / 2^(13/3).

The proof applies to term-preserving finite abelian quotients with 2-group kernel. In particular, it covers the requested binary BB double covers.

Run `bash run_all.sh` to repeat the exact finite sanity checks. Python 3.10+ and SymPy are required. The witness and odd-sector scripts otherwise use only the Python standard library.

The computations do not certify any new exact minimum distances. They independently check explicit cycles/nonboundaries, weight bounds, determinant/Gram identities, and finite instances of the polynomial factor identities used in the symbolic proof. No earlier circuit catalogue is a dependency.

The note does not prove a positive constant lower ratio or construct a vanishing-ratio family. It excludes every bounded-cover-distance route and improves the previously size-dependent degradation lower scale.
