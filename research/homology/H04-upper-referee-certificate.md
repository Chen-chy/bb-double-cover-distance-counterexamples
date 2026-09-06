The finalized certificates both passed, including separate exhaustive searches in the \(X\) and \(Z\) sectors. The two implementations reconstructed identical matrices, identical sets of all \(741\) cover circuits of weight at most \(12\), and identical boundary preimages for the ten circuit-orbit representatives.

**The certified counterexample is**
\[
\boxed{[[78,4,6]]\longrightarrow[[156,4,14]],\qquad 14>2\cdot6.}
\]

[Complete referee package](sandbox:/mnt/data/bb_double_cover_referee_certificate.zip)

The individual standalone files are [the bitset verifier](sandbox:/mnt/data/bb_referee_certificate/verify_bitset.py) and [the independent polynomial verifier](sandbox:/mnt/data/bb_referee_certificate/verify_polynomial.py). The package also contains the [self-contained mathematical certificate](sandbox:/mnt/data/bb_referee_certificate/CERTIFICATE.md), [first execution transcript](sandbox:/mnt/data/bb_referee_certificate/bitset_run.txt), [second execution transcript](sandbox:/mnt/data/bb_referee_certificate/polynomial_run.txt), all four matrices, the complete circuit set, machine-readable reports, execution metadata, an integrity manifest, and the pinned source PDF.

## A. Mathematical certificate

### Theorem

There exists a valid binary BB double cover with \(d_2>2d\).

More precisely, set
\[
\ell=39,\qquad m=1,\qquad
\widetilde\ell=78,\qquad \widetilde m=1,
\]
and
\[
A=\widetilde A=1+x^8+x^{25},\qquad
B=\widetilde B=1+x^2+x^{13}.
\]
Then
\[
Q(A,B,39,1)=[[78,4,6]],
\qquad
Q(\widetilde A,\widetilde B,78,1)=[[156,4,14]].
\]

The proof below is computer-assisted: the polynomial identities and completeness of the finite searches are proved explicitly; the exhaustive computations are reproduced by the two supplied implementations.

### Coordinate and matrix conventions

For \(L\in\{39,78\}\), use
\[
R_L=\mathbb F_2[x]/(x^L+1)
\]
with basis \(1,x,\ldots,x^{L-1}\).

Write physical coordinates as \(L_j,R_j\), where \(0\le j<L\). In flat integer indexing, \(L_j\) is coordinate \(j\), and \(R_j\) is coordinate \(L+j\).

For a polynomial \(P\), its multiplication matrix is
\[
(M_P)_{r,j}=[x^{\,r-j\bmod L}]P.
\]
Define
\[
H_X=(M_A\ M_B),\qquad
H_Z=(M_B^T\ M_A^T).
\]
Thus
\[
\partial_1(u,v)=Au+Bv,\qquad
\partial_2h=(Bh,Ah).
\]
These are the conventions of the polynomial complex and Equation (13) in the source. fileciteturn0file1

Explicitly, row \(r\) of \(H_X\) has support
\[
\{L_{r},L_{r-8},L_{r-25},
  R_{r},R_{r-2},R_{r-13}\},
\]
and row \(r\) of \(H_Z\) has support
\[
\{L_{r},L_{r+2},L_{r+13},
  R_{r},R_{r+8},R_{r+25}\},
\]
with indices reduced modulo \(L\). These formulas determine every matrix entry.

Commutation follows from
\[
H_XH_Z^T=M_AM_B+M_BM_A=0.
\]
Both programs also verify this computationally.

### Validity under Theorem 3.1, including \(m=1\)

Theorem 3.1 requires
\[
\widetilde\ell=u\ell,\qquad \widetilde m=tm,
\]
and termwise reduction of the lifted monomial exponents to their base exponents modulo \(\ell,m\). Here \(u=2,t=1\). The exponent pairs are
\[
A:\quad(0,0),(8,0),(25,0),
\]
\[
B:\quad(0,0),(2,0),(13,0),
\]
and the lifted pairs are identical. Every condition holds directly. The voltage group is \(\mathbb Z_2\times\mathbb Z_1\). fileciteturn0file1

**The source permits \(m=1\).** Section 2.4 defines the ring through \(\mathbb Z_\ell\times\mathbb Z_m\); Remark 5 requires three monomials in each defining polynomial, without requiring \(m>1\) or requiring both variables to occur. With \(m=1\), \(y=1\), and its multiplication matrix is the \(1\times1\) identity. The paper itself explicitly uses \(m=1\) BB codes, including the \((21,1)\) example in the text on page 35 and the base codes in Tables 2 and 4. fileciteturn0file1

There is a source typo that should not be concealed: Equation (9) interchanges the two exponent bounds as printed. The certificate uses Equation (8) and the explicit bases in the proof of Proposition 1 on page 11. Taking the interchanged bounds literally would not produce a basis of the stated ring and would conflict with the paper’s own \(m=1\) examples. This is not an additional \(m>1\) hypothesis. fileciteturn0file1

There is also a direct graph certificate, independent of invoking Theorem 3.1. Map every qubit and check at position \(j\) to the same vertex type at \(j\bmod39\). Every vertex has two preimages. The displayed neighbor formulas commute with reduction, and the three monomials in either polynomial remain distinct modulo \(39\). Consequently, projection is a bijection on every neighborhood. Both programs check this for every vertex of the full Tanner graph, including both check types.

### Polynomial derivation of \(k=k_2=4\)

Let
\[
g=1+x+x^2.
\]
Reduction modulo \(g\), using \(x^3=1\), shows \(g\mid A,B\). An explicit Bézout identity is
\[
UA+VB=g,
\]
where the exponent supports are
```text
U = [1,2,4,5,6,9,10]
V = [0,2,5,6,7,8,9,10,11,13,14,16,17,18,21,22]
```
Here an exponent list denotes the polynomial with coefficient one at precisely those exponents. Direct multiplication verifies the identity, so
\[
\gcd(A,B)=g.
\]

For either period, \(g\mid F_L=1+x^L\). Therefore
\[
(A,B)=(g)\quad\text{in }R_L,
\qquad
\dim R_L/(A,B)=2,
\]
and
\[
\operatorname{rank}\partial_1=L-2.
\]

The simultaneous annihilator satisfies
\[
Ah=Bh=0
\iff gh=0\pmod{F_L}.
\]
The forward implication uses the Bézout identity; the converse uses \(g\mid A,B\). Setting \(f_L=F_L/g\), ordinary polynomial cancellation gives
\[
F_L\mid gh\iff f_L\mid h.
\]
Thus the annihilator has basis \(f_L,xf_L\), where
\[
f_L=(1+x)\sum_{i=0}^{L/3-1}x^{3i}.
\]
Its dimension is two, so
\[
\operatorname{rank}\partial_2=L-2.
\]
Consequently,
\[
k=2L-(L-2)-(L-2)=4.
\]
This argument remains valid at the repeated-root period \(78\).

### Independent binary rank calculation

Both implementations independently eliminate the reconstructed binary matrices.

| Period \(L\) | Physical qubits | \(\operatorname{rank}H_X\) | \(\operatorname{rank}H_Z\) | \(k\) |
|---:|---:|---:|---:|---:|
| 39 | 78 | 37 | 37 | 4 |
| 78 | 156 | 76 | 76 | 4 |

For each matrix, the first \(L-2\) rows are checked to be independent. The last two rows satisfy the explicit relations
\[
r_{L-2}
=
\sum_{\substack{0\le i<L-2\\i\bmod3\in\{0,1\}}}r_i,
\qquad
r_{L-1}
=
\sum_{\substack{0\le i<L-2\\i\bmod3\in\{0,2\}}}r_i.
\]
Both programs check these relations as binary vectors.

The greatest-coordinate elimination in the first implementation produces pivot columns
\[
77,76,\ldots,41
\]
for both base matrices, and
\[
155,154,\ldots,80
\]
for both cover matrices. The second implementation uses smallest-coordinate pivots and independently obtains the same ranks.

## B. Explicit upper-bound witnesses

### Base logical of weight six

Let
\[
z_L=1+x^8+x^{16}+x^{25},\qquad
z_R=1+x^{11},\qquad z=(z_L,z_R).
\]

Its supports are
```text
Base z, period 39:
  left  = [0,8,16,25]
  right = [0,11]
  flat  = [0,8,16,25,39,50]
```

Put
\[
F=1+x^{39},\qquad c=x^2+x^{11}.
\]
The ordinary polynomial identity
\[
\boxed{Az_L+Bz_R=Fc}
\tag{1}
\]
has support \([2,11,41,50]\) on both sides. It proves \(\partial_1z=0\) modulo \(F\).

Modulo \(g\), both coordinates of \(z\) equal \(x\ne0\). Both coordinates of every boundary \((Bh,Ah)\) vanish modulo \(g\). Hence
\[
[z]\ne0.
\]

The first verifier additionally checks non-membership in the binary boundary span; the second checks non-membership through an independent polynomial-congruence solver.

### Cover logical of weight fourteen

Set
\[
R=x^9+x^{22}+x^{35}+x^{37}.
\]
A second ordinary polynomial identity is
\[
\boxed{Az_L+BR+c=F(1+x^2+x^9).}
\tag{2}
\]

Define
\[
w=(x^{39}z_L,\ z_R+FR).
\]
Its supports are
```text
Cover w, period 78:
  left  = [39,47,55,64]
  right = [0,9,11,22,35,37,48,61,74,76]
  flat  = [39,47,55,64,78,87,89,100,113,115,126,139,152,154]
```
Thus \(|w|=14\).

Using \(x^{39}=1+F\), Equations (1)–(2) give
\[
\begin{aligned}
\widetilde\partial_1w
&=Ax^{39}z_L+B(z_R+FR)\\
&=F(c+Az_L+BR)\\
&=F^2(1+x^2+x^9).
\end{aligned}
\]
This vanishes modulo \(F^2=1+x^{78}\).

Projection reduces exponents modulo \(39\), so
\[
\boxed{p(w)=z}
\]
as a literal chain. It also satisfies
\[
p(Ah)=Ap(h),\qquad p(Bh)=Bp(h),
\]
and therefore maps boundaries to boundaries. Since \([z]\ne0\),
\[
[w]\ne0.
\]
Both implementations also test the cover witness’s nontriviality directly.

## C. Exact exclusion of base logicals below weight six

### Why circuits suffice

A nonempty cycle support is a *circuit* if it contains no proper nonempty cycle support.

A minimum-weight non-boundary cycle must be a circuit. Suppose it contains a proper nonzero subcycle \(c\). If \(c\) is non-boundary, it is a smaller logical. If \(c\) is a boundary, adding \(c\) removes its support from the original logical and gives a smaller representative of the same nonzero class. Both contradict minimality.

Equivalently, every binary cycle decomposes into support-disjoint circuits: remove a minimal nonzero subcycle and repeat. Thus, if every circuit through a given weight is a boundary, every cycle through that weight is a boundary.

For a cycle with support \(S\), the exact circuit test is
\[
\boxed{\operatorname{rank}(H_X|_S)=|S|-1.}
\]
The all-one vector on \(S\) is already in the restricted kernel. Nullity one means it is the only nonzero kernel vector. Any other nonzero kernel vector would have proper support, since the all-one vector is the unique binary vector with full support \(S\).

### Odd weights are impossible

Every column of \(H_X\) and \(H_Z\) has weight three. Therefore
\[
H_Xv=0
\quad\Longrightarrow\quad
0=\mathbf1^TH_Xv=\mathbf1^Tv=|v|\pmod2.
\]
The same holds for \(H_Z\).

It is therefore enough to exclude weights \(2,4\) in the base and even weights through \(12\) in the cover. Weight \(13\) is not omitted from the argument: it is impossible by parity.

### First verifier: precise enumeration and pruning rules

Variables are ordered
\[
L_0,\ldots,L_{L-1},R_0,\ldots,R_{L-1}.
\]
Checks are ordered \(0,\ldots,L-1\). There are two rooted searches, starting at flat coordinates \(0\) and \(L\), with no additional initial forbidden coordinates.

Simultaneous cyclic translation preserves cycles and boundaries and is transitive on each block. Every circuit therefore has a translate containing one of these two roots.

A state consists of a chosen support \(U\), a forbidden support \(E\), and the exact syndrome
\[
\sigma=H_X1_U.
\]
The bound is \(4\) in the base and \(12\) in the cover.

At zero syndrome, the program tests boundary membership, records the leaf, applies the circuit test, and stops that branch. A non-boundary leaf immediately fails the certificate.

Otherwise, with \(R=b-|U|\), it stops when \(R\le0\), when \(|\sigma|>3R\), or when an odd check has no available incident qubit. Among the remaining odd checks, it chooses one with the fewest available qubits, breaking ties by check index.

If its available qubits are \(j_1<\cdots<j_t\), branch \(a\) selects \(j_a\), forbids \(j_1,\ldots,j_{a-1}\), and updates
\[
\sigma\longmapsto\sigma+H_Xe_{j_a}.
\]
Later candidates remain available in that branch.

**Completeness.** Fix a target circuit \(C\) containing the root. Inductively maintain \(U\subseteq C\) and \(E\cap C=\varnothing\). A proper subset \(U\subsetneq C\) has nonzero syndrome. At the chosen odd check, \(C\setminus U\) contains a positive odd number of available incident qubits. Its first such qubit determines the unique branch preserving both invariants. This reaches \(U=C\), where the circuit is tested.

Each pruning rule is safe:

* A nonzero syndrome with no remaining weight budget cannot be completed.
* At most \(R\) added columns of weight three cannot cancel more than \(3R\) currently odd checks.
* An odd check with no available neighbor cannot have its parity corrected.
* Forbidding earlier candidates assigns completions using them to earlier branches; it does not discard them globally.
* Stopping at zero syndrome cannot truncate a proper subset of a circuit.

There is no other pruning rule. In particular, neither a presumed logical class nor an expected circuit catalogue is used.

Boundary membership is exact Gaussian elimination in the span of the appropriate boundary columns. Each pivot retains its coefficients in the original generators; a zero residual provides a boundary preimage.

### Base counts

Each of the four base searches—\(Z\) and \(X\), at roots \(0\) and \(39\)—has exactly
\[
36\text{ nodes},\quad
7\text{ expanded nodes},\quad
5\text{ budget leaves},\quad
24\text{ syndrome-bound leaves},
\]
with zero blocked-check leaves and zero zero-syndrome leaves.

Thus there are no base circuits of weight at most four. Circuit reduction and parity exclude all nonzero base cycles of weights \(1,2,3,4,5\).

The second implementation additionally verifies that the \(78\) base columns are distinct and nonzero and that all
\[
\binom{78}{2}=3003
\]
unordered pair sums are distinct. A weight-four cycle would produce a collision between two disjoint pair sums. This supplies a separate exhaustive base exclusion.

Together with \(z\), these results prove \(d_Z=6\).

## D. Exact cover exclusion and complete circuit classification

### Explicit preimage of \(\tau(z)\)

Write
\[
a=A/g,\qquad b=B/g,\qquad f=F/g.
\]
The \(U,V\) above satisfy \(Ua+Vb=1\). Because \(g\mid c=x^2(1+x^9)\), Equation (1) implies
\[
az_L+bz_R=0\pmod F.
\]
Set
\[
v=Uz_R+Vz_L\pmod F,\qquad
H=fv\pmod{F^2}.
\]
The Bézout identity gives
\[
bv=z_L\pmod F,\qquad av=z_R\pmod F.
\]
Consequently,
\[
BH=Fz_L\pmod{F^2},\qquad
AH=Fz_R\pmod{F^2}.
\]

The explicit two-chain is
```text
H = [1,8,9,10,11,12,13,15,16,17,18,19,20,23,24,25,
     27,28,31,32,34,37,38,41,43,44,46,48,51,53,54,
     57,61,63,65,66,68,74]
```
Direct multiplication gives
```text
B H mod (1+x^78) = [0,8,16,25,39,47,55,64]
A H mod (1+x^78) = [0,11,39,50]
```
Therefore
\[
\boxed{\widetilde\partial_2H=\tau(z).}
\]

Both implementations independently reconstruct this same \(H\).

### All circuit orbits of weight at most twelve

The following representatives are exactly the canonical representatives produced by both programs. Every row is a boundary. The last column gives the exponent support of a two-chain \(s\) whose boundary is the displayed vector:
\[
C=(Bs,As).
\]

| Orbit | Left support | Right support | Weight | Orbit size | Two-chain support |
|---:|---|---|---:|---:|---|
| 1 | `[0,2,13]` | `[0,8,25]` | 6 | 78 | `[0]` |
| 2 | `[0,2,5,13,70,72]` | `[8,17,25,70]` | 10 | 78 | `[0,70]` |
| 3 | `[0,2,11,24]` | `[0,8,11,19,25,36]` | 10 | 78 | `[0,11]` |
| 4 | `[0,2,13,17,19,30]` | `[0,8,17,42]` | 10 | 78 | `[0,17]` |
| 5 | `[0,2,13,25,27,38]` | `[0,8,33,50]` | 10 | 78 | `[0,25]` |
| 6 | `[0,2,15,26]` | `[0,8,13,21,25,38]` | 10 | 78 | `[0,13]` |
| 7 | `[0,2,65,69]` | `[12,14,65,67,73,75]` | 10 | 78 | `[65,67]` |
| 8 | `[0,2,5,13,17,19,30,70,72]` | `[8,42,70]` | 12 | 78 | `[0,17,70]` |
| 9 | `[0,4,26]` | `[0,2,8,10,13,21,25,27,38]` | 12 | 78 | `[0,2,13]` |
| 10 | `[0,8,16,25,39,47,55,64]` | `[0,11,39,50]` | 12 | 39 | \(H\) above |

There are no other positive-weight circuit orbits through weight twelve.

Up to translation, this is the previously stated compact classification
\[
\partial_2(1),
\]
\[
\partial_2(1+x^a),
\qquad a\in\{2,8,11,13,17,25\},
\]
\[
\partial_2(A),\qquad \partial_2(B),\qquad \tau(z).
\]

**This table is an output, not an input, of both searches.** Each program discovers the rooted circuits, expands all translations, groups them into orbits, and solves for their preimages.

### Independent orbit-count checks

For the first nine orbits, the translation stabilizer is \(\{0\}\). For the last it is \(\{0,39\}\). Each stabilizer is checked using all \(78\) shifts.

Hence
\[
\begin{array}{c|r}
\text{weight}&\text{number of circuits}\\\hline
6&78\\
10&468\\
12&195
\end{array}
\]
and the total is
\[
9\cdot78+39=741.
\]

A separate incidence calculation gives the same counts. The numbers of circuits containing the left and right identity qubits are
\[
(3,30,16),\qquad(3,30,14)
\]
at weights \((6,10,12)\). Translation invariance implies
\[
wN_w=78\bigl(N_{w,L_0}+N_{w,R_0}\bigr).
\]
This yields \(N_6=78,N_{10}=468,N_{12}=195\), independently of orbit grouping.

Finally, the second implementation independently reconstructs the entire set of \(741\) supports and obtains the same serialized file.

### Exact first-verifier cover counts

These columns partition all visited states into expanded nodes and terminal leaves.

| Sector | Root | Nodes | Expanded | Budget leaves | Syndrome-bound leaves | Blocked leaves | Zero leaves |
|:---:|---:|---:|---:|---:|---:|---:|---:|
| Z | 0 | 985001 | 234911 | 5889 | 743178 | 924 | 99 |
| Z | 78 | 991809 | 236744 | 5488 | 748141 | 1347 | 89 |
| X | 0 | 941501 | 225282 | 4767 | 710265 | 1096 | 91 |
| X | 78 | 894576 | 213806 | 4215 | 675425 | 1039 | 91 |

The zero-leaf and actual-circuit histograms are:

| Sector | Root | Zero leaves at weights \((6,10,12)\) | Circuits at weights \((6,10,12)\) |
|:---:|---:|---|---|
| Z | 0 | \((3,30,66)\) | \((3,30,16)\) |
| Z | 78 | \((3,30,56)\) | \((3,30,14)\) |
| X | 0 | \((3,30,58)\) | \((3,30,14)\) |
| X | 78 | \((3,30,58)\) | \((3,30,16)\) |

Every non-boundary-leaf count is zero. Noncircuit zero leaves are also tested for boundary membership before the circuit filter is applied.

### Why this proves \(d_{Z,2}=14\)

Every circuit of weight at most twelve is a boundary. Every cycle of weight at most twelve decomposes into circuits of no larger weight, and is therefore also a boundary.

Odd-weight cycles, including weight thirteen, are impossible. Thus
\[
d_{Z,2}\ge14.
\]
The explicit non-boundary \(w\) has weight fourteen, proving
\[
\boxed{d_{Z,2}=14.}
\]

This exclusion covers every cover logical, not just a selected homology class or projection sector.

## E. Exact \(X/Z\) identification

Define
\[
f^\star(x)=f(x^{-1}),\qquad
J(u,v)=(v^\star,u^\star).
\]

As an explicit permutation of flat physical coordinates,
\[
J(j)=L+((-j)\bmod L),\qquad 0\le j<L,
\]
and
\[
J(L+j)=(-j)\bmod L,\qquad 0\le j<L.
\]
It is a weight-preserving involution.

Transposition corresponds to starring the multiplication polynomial, so
\[
H_ZJ(u,v)
=B^\star v^\star+A^\star u^\star
=(Au+Bv)^\star.
\]
Thus \(J\) maps \(Z\)-cycles to \(X\)-cycles. Also,
\[
J(Bh,Ah)
=(A^\star h^\star,B^\star h^\star)
=H_X^Th^\star,
\]
so it maps \(Z\)-boundaries to \(X\)-boundaries.

Since \(J^{-1}=J\), it induces a weight-preserving bijection of nontrivial logical operators in the two sectors, for both periods.

The explicit \(X\) witnesses are
```text
J(z), period 39:
  left  = [0,28]
  right = [0,14,23,31]

J(w), period 78:
  left  = [0,2,4,17,30,41,43,56,67,69]
  right = [14,23,31,39]
```

Both programs verify the \(J\) identities on every basis vector and also repeat the exclusions directly in the \(X\) sector. Therefore
\[
\boxed{
d_X=d_Z=6,\qquad
\widetilde d_X=\widetilde d_Z=14.
}
\]

For a general CSS Pauli logical, its physical support is the union of its \(X\)- and \(Z\)-component supports. At least one component represents a nonzero logical class, so its weight is at least that sector’s distance. Pure-sector witnesses achieve the minimum. Thus these are the full quantum distances.

## F. Standalone first verifier

The complete file is [verify_bitset.py](sandbox:/mnt/data/bb_referee_certificate/verify_bitset.py).

Run:
```sh
python3 verify_bitset.py
```

It requires only Python 3.10 or later and its standard library. No other files are needed. To regenerate the matrix files, complete circuit set, and JSON report:
```sh
python3 verify_bitset.py --output-dir regenerated_bitset
```

It reconstructs the matrices, ranks, boundary spaces, circuits, orbit representatives, and preimages from the defining data. The explicit witnesses are reconstructed algebraically: \(z\) from the defining exponent tuples, \(c\) by polynomial division, and \(R\) by solving its cyclic linear equation and checking all four solutions. Expected circuit supports are never used.

All checks use explicit exceptions rather than Python `assert`, so optimization mode does not disable them. The final stdout line is exactly
```text
BB_DOUBLE_COVER_COUNTEREXAMPLE_VERIFIED
```
only after every check and requested output write succeeds.

### Canonical matrix hashes

The exact ASCII encoding is:
```text
GF2MATRIX v1
r c
row_0_bits
...
row_(r-1)_bits
```
Rows list columns in increasing order with no separators. Every line, including the last, ends with one LF byte.

The resulting SHA-256 hashes are:
```text
L=39 HX:
6e84e8c9cbb4cec64bb6d04405ae0ac9d87ce71e6a1a972e8b833ab1a824eef4

L=39 HZ:
341909344e831fdcb9aaa7d117aafe474718b0e25b610ae536b20eb7b370b6b3

L=78 HX:
468b9f9db365929d4506dbcbb38e09ff8a0f42c1c1997bb64295249d36dc361e

L=78 HZ:
4825f8e81f446083b9a23cf2fde781c966007930363e8e5fb0470780d19fc0de
```

The [complete \(741\)-circuit file](sandbox:/mnt/data/bb_referee_certificate/bitset_output/circuits.txt) has SHA-256
```text
ab05b51aa41a2cea530557a6d9940877c8974472edcff3aca84815ccbe79a957
```
Its serialization is specified in the mathematical certificate.

## G. Second independent implementation

The complete file is [verify_polynomial.py](sandbox:/mnt/data/bb_referee_certificate/verify_polynomial.py).

Run:
```sh
python3 verify_polynomial.py
```
or
```sh
python3 verify_polynomial.py --output-dir regenerated_polynomial
```

It does not import the first implementation or read its outputs.

### Different representation and boundary-membership test

Polynomials are represented as frozensets of exponents. Addition is symmetric difference; multiplication is convolution with exponent reduction modulo \(L\). Chains are polynomial pairs. Binary rank uses set-based elimination with smallest-coordinate pivots.

Boundary membership is decided through a polynomial Bézout solver, not through the first implementation’s binary boundary-span calculation.

For a syndrome map \((P,Q)\), let
\[
g=\gcd(P,Q,F_L),\quad
a=P/g,\quad b=Q/g,\quad f=F_L/g.
\]
The program computes
\[
Ua+Vb+Wf=1.
\]
For a candidate \((u,v)\), both coordinates must be divisible by \(g\). If they are, compute
\[
h=U(v/g)+V(u/g)\pmod f.
\]
The candidate is a boundary exactly when
\[
Qh=u\pmod{F_L},
\qquad
Ph=v\pmod{F_L}.
\]

Sufficiency is explicit construction. For necessity, a boundary \((Qh_0,Ph_0)\) satisfies
\[
u/g=bh_0,\qquad v/g=ah_0\pmod f.
\]
The Bézout identity then gives \(h=h_0\pmod f\), producing the same boundary. This argument works at the repeated-root cover period.

### Different exhaustive search partition

The second search does **not** use first-present-candidate branching.

At an odd syndrome coefficient, let \(T\) be all incident undecided variables. Every completion chooses an odd-cardinality subset \(K\subseteq T\). The program branches on every such odd subset, selecting \(K\) and fixing all of \(T\setminus K\) to zero simultaneously.

For a target circuit, its intersection with \(T\) determines a unique continuing branch. A partial zero syndrome cannot precede completion of that circuit. Thus this different tree is also exhaustive.

The only pruning conditions are the proved budget, degree-three syndrome bound, and no-available-neighbor conditions, plus skipping an odd subset whose own cardinality exceeds the remaining budget. Local caching stores exact lists of assignments and their polynomial contributions; it removes no assignment.

### Exact secondary counts

Each of the four base searches has \(46\) nodes, \(7\) expanded nodes, \(15\) budget leaves, \(24\) syndrome-bound leaves, and no zero or blocked leaves.

The cover counts are:

| Sector | Root | Nodes | Expanded | Budget leaves | Syndrome-bound leaves | Zero leaves |
|:---:|---:|---:|---:|---:|---:|---:|
| Z | 0 | 1602436 | 227115 | 424001 | 951214 | 106 |
| Z | 78 | 1559534 | 221268 | 414024 | 924137 | 105 |
| X | 0 | 1578044 | 223528 | 415849 | 938563 | 104 |
| X | 78 | 1561758 | 218276 | 408291 | 935086 | 105 |

All blocked-leaf counts are zero. The zero-leaf histograms at weights \((6,10,12)\) are respectively
\[
(3,30,73),\quad(3,30,72),\quad
(3,30,71),\quad(3,30,72).
\]
Every non-boundary-leaf count is zero.

Despite the different search trees and extra noncircuit leaves, the actual rooted circuit histograms, full \(741\)-circuit set, ten canonical orbit records, and preimages agree exactly with the first implementation.

The [execution metadata](sandbox:/mnt/data/bb_referee_certificate/EXECUTION_METADATA.json) records both successful exit codes, script and transcript hashes, and the subsequent bytewise cross-comparison.

## H. Final status

All finalized certificates succeeded. The exact codes are
\[
A=\widetilde A=1+x^8+x^{25},
\qquad
B=\widetilde B=1+x^2+x^{13},
\]
\[
(\ell,m)=(39,1),\qquad
(\widetilde\ell,\widetilde m)=(78,1),
\]
with
\[
\boxed{[[78,4,6]]\longrightarrow[[156,4,14]].}
\]

This valid double cover violates \(d_2\le2d\), and therefore disproves the universal distance conjecture as stated in Conjecture 1 of the source. fileciteturn0file1

STATUS: UPPER_BOUND_FALSE

STATUS: ORIGINAL_DISTANCE_CONJECTURE_FALSE
