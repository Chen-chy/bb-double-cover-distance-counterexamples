# A binary BB double cover with distance greater than twice the base distance

## Certificate scope

This is a computer-assisted counterexample certificate for the fixed pair of codes
specified below. It does not depend on any previous conversation, Bockstein claim,
class-level lifting lemma, heuristic decoder, or external mathematical software.
The human-verifiable part consists of the definitions, polynomial identities,
linear-algebra statements, and proof that the finite searches are exhaustive.
The finite part consists of two standalone, separately implemented exact searches.
Both also construct and check the explicit witnesses and all four check matrices.

`verify_bitset.py` and `verify_polynomial.py` use only the Python standard library.
Neither reads a supplied circuit list or the other implementation's output. The
circuit lists in this package are outputs, not trusted inputs. The implementations
use different data representations, boundary-membership tests, and branching
rules. Their computed matrices and complete sets of short circuits agree byte for
byte. Exact stdout transcripts and machine-readable reports are included.

The source being interpreted is the attached PDF of Symons, Rajput, and Browne,
*Sequences of Bivariate Bicycle Codes from Covering Graphs*, arXiv:2511.13560v3,
47 pages, cited below as [S]. The actual PDF is pinned in `source/`; its SHA-256 is
`549f63efc9fcae20983854d924852422ff4d9056811c8aa020024914d380aecc`.

## A. The theorem, definitions, cover validity, and dimensions

**Theorem (computer-assisted).** There exists a valid binary BB double cover with
\(d_2>2d\). Specifically, let

\[
\ell=39,\qquad m=1,\qquad \widetilde\ell=78,\qquad\widetilde m=1,
\]
\[
A=\widetilde A=1+x^8+x^{25},\qquad
B=\widetilde B=1+x^2+x^{13}.
\]
Then, with the monomial basis and CSS convention specified below,

\[
Q(A,B,39,1)=[[78,4,6]],\qquad
Q(\widetilde A,\widetilde B,78,1)=[[156,4,14]].
\]

The second code is a Theorem 3.1 double cover of the first, and
\(14>2\cdot6\).

### A.1 Coordinate and matrix conventions

For \(L\in\{39,78\}\), work in

\[
R_L=\mathbb F_2[x]/(x^L+1),
\]

with basis \(1,x,\ldots,x^{L-1}\). A qubit is labelled either \(L_j\) or
\(R_j\), \(0\le j<L\). In a flat integer coordinate list, \(L_j\) is coordinate
\(j\) and \(R_j\) is coordinate \(L+j\). All check indices run from zero to
\(L-1\). Here the symbol \(L\) in a subscripted qubit label denotes the left
block; the unadorned integer \(L\) is the period.

Multiplication matrices are defined by

\[
(M_P)_{r,j}=[x^{r-j\bmod L}]P.
\]

Set

\[
H_X=(M_A\ M_B),\qquad
H_Z=(M_B^T\ M_A^T).
\]

Thus

\[
\partial_1(u,v)=Au+Bv,\qquad
\partial_2h=(Bh,Ah).
\]

The Z-logical space is \(\ker\partial_1/\operatorname{im}\partial_2\).
The X-logical space is \(\ker H_Z/\operatorname{im}H_X^T\). Since multiplication
is commutative and the characteristic is two,

\[
H_XH_Z^T=M_AM_B+M_BM_A=0.
\]

Both implementations additionally check every entry of this matrix product.

Explicitly, row \(r\) of \(H_X\) has support

\[
\{L_{r-a}:a\in\{0,8,25\}\}\cup
\{R_{r-b}:b\in\{0,2,13\}\},
\]

and row \(r\) of \(H_Z\) has support

\[
\{L_{r+b}:b\in\{0,2,13\}\}\cup
\{R_{r+a}:a\in\{0,8,25\}\}.
\]

All indices in these formulas are reduced modulo \(L\). These formulas
unambiguously reconstruct every bit of every matrix.

### A.2 Theorem 3.1 and the issue of m=1

[S, Section 2.4, Eq. (8), pp. 9-11] defines the coefficient ring as
\(\mathbb F_2[\mathbb Z_\ell\times\mathbb Z_m]\), and [S, Remark 5,
Eqs. (11)-(13), p. 11] defines BB codes by the above Koszul complex with each
of \(A,B\) consisting of three distinct monomials. The definition does not
require \(m>1\), that both variables occur, or any prescribed pattern of pure
x- and y-powers. For \(m=1\), \(\mathbb Z_1\) is the trivial group and the
relation \(y=1\) gives exactly \(R_L\). There is no collapse among our three
x-monomials at either period.

This interpretation is explicit in the source, not an extension of its scope:
[S, p. 35] uses a base code with parameters \((\ell,m)=(21,1)\), and Tables 2
and 4 on pp. 35-36 include base BB codes with \(m=1\).

There is a typographical issue worth making explicit: the exponent bounds in
[S, Eq. (9), p. 9] are interchanged as printed. This certificate uses the ring
in Eq. (8) and the explicit bases \(1,x,\ldots,x^{\ell-1}\) and
\(1,y,\ldots,y^{m-1}\) in the proof of Proposition 1 on p. 11. Taking the
interchanged bounds literally would not give a basis of the ring and would also
conflict with the paper's own m=1 examples. It is not an m>1 hypothesis.

The four conditions of [S, Theorem 3.1, pp. 13-14] are, in its notation:

\[
\widetilde\ell=u\ell,\qquad \widetilde m=t m,
\]

and the x- and y-exponents of each lifted A-monomial and each lifted B-monomial
reduce to the corresponding base exponents modulo \(\ell,m\).

Here \(u=2,t=1\). The A-exponent pairs are
\((0,0),(8,0),(25,0)\), and the B-exponent pairs are
\((0,0),(2,0),(13,0)\). The lifted pairs are identical. All four conditions
hold term by term. The voltage group is \(\mathbb Z_2\times\mathbb Z_1\).
For a forward x-shift by \(e\), its first voltage coordinate at a base label
\(c\) is \(\lfloor(c+e)/39\rfloor\bmod2\); its second coordinate is zero.
This includes the ordinary wrap carry even though the defining polynomials
are unchanged.

There is also a direct graph check independent of the theorem: send every
vertex of type left-qubit, right-qubit, X-check, or Z-check at position \(j\)
to the same type at \(j\bmod39\). Every vertex has two preimages. The displayed
neighbor formulas commute with this projection, and distinct monomials remain
distinct modulo 39 within each block. The map is therefore a bijection on each
vertex neighborhood. Both implementations check this for every vertex of the
full Tanner graph, including both check types.

### A.3 Polynomial dimension certificate

Let \(g=1+x+x^2\). Its divisibility into A and B follows from
\(x^3=1\pmod g\). An explicit Bezout identity certifies that there is no
larger common factor:

\[
UA+VB=g,
\]

where the exponent supports of U and V are

```
U = [1,2,4,5,6,9,10]
V = [0,2,5,6,7,8,9,10,11,13,14,16,17,18,21,22]
```

A list here and below denotes the polynomial with coefficient one at precisely
those exponents. Direct polynomial multiplication verifies the identity. Thus
\(\gcd(A,B)=g\). Since both periods are divisible by three, \(g\mid F_L\),
where \(F_L=1+x^L\). Consequently,

\[
(A,B)=(g)\text{ in }R_L,
\qquad
\dim R_L/(A,B)=2.
\]

Also,

\[
Ah=Bh=0\iff gh=0\pmod {F_L}.
\]

The implication to the right uses the Bezout identity; the converse uses
\(g\mid A,B\). Put \(f_L=F_L/g\). Ordinary polynomial cancellation shows
\(F_L\mid gh\iff f_L\mid h\). The simultaneous annihilator is therefore
spanned by \(f_L,xf_L\), two independent polynomials of degrees \(L-2,L-1\).
An explicit form is

\[
f_L=(1+x)\sum_{i=0}^{L/3-1}x^{3i}.
\]

It follows that

\[
\operatorname{rank}\partial_1=L-2,\quad
\operatorname{rank}\partial_2=L-2,\quad
k=2L-(L-2)-(L-2)=4.
\]

This calculation is valid also at the repeated-root period 78; no square-free
or semisimple assumption is made.

### A.4 Independent binary rank certificate

Both scripts perform binary elimination on the reconstructed coefficient
matrices, rather than using the preceding dimension formula as the calculation.
Implementation 1 uses integer bitsets and greatest-coordinate pivots;
implementation 2 uses sets and smallest-coordinate pivots.

For each of HX and HZ, in each period, the first L-2 rows are independently
checked to be linearly independent. The last two rows have the explicit
relations, with \(r_i\) denoting row i,

\[
r_{L-2}=\sum_{\substack{0\le i<L-2\\i\bmod3\in\{0,1\}}}r_i,
\qquad
r_{L-1}=\sum_{\substack{0\le i<L-2\\i\bmod3\in\{0,2\}}}r_i.
\]

These relations are checked as binary vectors in both implementations.
Implementation 1 obtains pivot columns 77,76,...,41 at L=39 and
155,154,...,80 at L=78, for both matrices.

| Period | Qubits | rank HX | rank HZ | k |
|---:|---:|---:|---:|---:|
|39|78|37|37|4|
|78|156|76|76|4|

## B. Explicit upper-bound witnesses

Put

\[
z_L=1+x^8+x^{16}+x^{25},\qquad z_R=1+x^{11},\qquad z=(z_L,z_R).
\]

Its block supports and flat physical support are

```
base z:
  left  = [0,8,16,25]
  right = [0,11]
  flat  = [0,8,16,25,39,50]
```

Let \(F=1+x^{39}\) and \(c=x^2+x^{11}\). An ordinary polynomial identity is

\[
Az_L+Bz_R=Fc.
\tag{B1}
\]

The left side has support [2,11,41,50], so it vanishes modulo F. Thus z is a
weight-six base cycle. Modulo g, both its coordinates equal x, whereas both
coordinates of every boundary \((Bh,Ah)\) vanish modulo g. Hence \([z]\ne0\).
The first script additionally checks non-membership in the binary boundary
span. The second uses an independent polynomial congruence membership test.

Now put

\[
R=x^9+x^{22}+x^{35}+x^{37}.
\]

The second ordinary polynomial identity is

\[
Az_L+BR+c=F(1+x^2+x^9).
\tag{B2}
\]

Define

\[
w=(x^{39}z_L,\ z_R+FR).
\]

Its supports are

```
cover w:
  left  = [39,47,55,64]
  right = [0,9,11,22,35,37,48,61,74,76]
  flat  = [39,47,55,64,78,87,89,100,113,115,126,139,152,154]
```

There are fourteen positions. Using \(x^{39}=1+F\), (B1) and (B2) give

\[
\begin{aligned}
\widetilde\partial_1w
 &=Ax^{39}z_L+B(z_R+FR)\\
 &=F(c+Az_L+BR)\\
 &=F^2(1+x^2+x^9).
\end{aligned}
\]

This vanishes in \(R_{78}\), since \(F^2=1+x^{78}\).

Define p on both coordinates by reducing exponents modulo 39 and adding
coefficients in \(\mathbb F_2\). Then \(p(w)=z\) as a literal chain. Moreover,
\(p(Ah)=Ap(h)\) and \(p(Bh)=Bp(h)\); thus p maps cover boundaries to base
boundaries. Since \([z]\ne0\), \([w]\ne0\). Both implementations also check
this nontriviality independently of that inference.

The scripts reconstruct z from the exponent tuples as
\(z_L=A+x^{2\cdot8}\), \(z_R=1+x^{13-2}\). They obtain c by exact division
in (B1). They reconstruct R by solving the cyclic equation
\(BR=c+Az_L\pmod F\), checking all four solutions and selecting its unique
minimum-weight solution. No circuit list or distance oracle is used to build
these witnesses.

## C. Why the exact finite exclusion proves d=6

### C.1 Circuit reduction

A nonempty binary cycle support S is a circuit if it contains no proper
nonempty cycle support. A minimum-weight non-boundary cycle must be a circuit.
Indeed, if it contains a proper nonzero subcycle c, either c is a smaller
non-boundary cycle, or c is a boundary and adding it removes its support from
the original logical, producing a smaller representative of the same nonzero
class. Either outcome contradicts minimality.

More generally, every binary cycle decomposes into support-disjoint circuits:
choose a minimal nonzero subcycle, remove it, and repeat. This terminates because
support size strictly decreases. Therefore, if all circuits through a specified
weight are boundaries, every cycle through that weight is a boundary.

For a cycle with support S, the exact test used to identify circuits is

\[
\operatorname{rank}(H_X|_S)=|S|-1.
\]

The restriction has the all-one vector on S in its kernel. Rank |S|-1 means
this is its only nonzero kernel vector. Conversely, if there were another
nonzero kernel vector, its support would be a proper nonempty subset of S,
because the all-one vector is the unique binary vector with full support S.
The circuit test is applied after a zero-syndrome leaf, not used as a pruning
heuristic.

### C.2 Odd weights are impossible

Every column of either check matrix has weight three. Thus a zero syndrome
implies, modulo two,

\[
0=\mathbf1^T H_Xv=\mathbf1^Tv=|v|\pmod2.
\]

The same holds with HZ. Equivalently A(1)=B(1)=1 in the polynomial description.
It suffices to exclude even weights 2 and 4 in the base and even weights through
12 in the cover. Weight 13, in particular, is not left unchecked.

### C.3 Exact search conventions for implementation 1

For each period and each sector, the variables are ordered
\(L_0,\ldots,L_{L-1},R_0,\ldots,R_{L-1}\), with flat indices 0 through 2L-1.
Checks are ordered 0 through L-1. Two separate rooted searches start at qubit 0
and qubit L. No additional initial forbidden coordinates are imposed.

Simultaneous cyclic translation by j in both blocks preserves the check code
and boundary space and is transitive on each block. Every circuit has a
translate containing at least one of the two roots. Therefore these two
rooted searches cover all circuits up to translation, including circuits lying
entirely in one block.

A state consists of a chosen support U, a forbidden support E disjoint from U,
and its exact syndrome sigma. Initially U contains just the root, E is empty,
and sigma is the column of that root. The bound is 4 for L=39 and 12 for L=78.

At each state:

1. If sigma is zero, test the chosen chain for membership in the appropriate
   boundary span and record it. A non-boundary causes immediate failure. Apply
   the restricted-rank circuit test for classification. Stop the branch.
2. Put R = bound - |U|. If R <= 0 while sigma is nonzero, stop the branch.
3. If |sigma| > 3R, stop the branch.
4. Scan odd checks in increasing order. For each, form its available incident
   qubits by removing U union E. If any odd check has none, stop the branch.
   Otherwise choose an odd check with the fewest available qubits, breaking
   ties by increasing check index.
5. Let the chosen check's available qubits be j1<...<jt. For branch a, add ja
   to U, update sigma by XOR with its check column, and forbid j1,...,j(a-1).
   The previous E is retained. Later candidates are not forbidden in that
   branch. Visit all branches.

**Completeness of branching.** Fix any target circuit C containing the root.
Inductively suppose U is contained in C and E is disjoint from C. If U is a
proper subset of C, its syndrome cannot be zero by the circuit property. At an
odd check, C minus U must contain an odd, hence positive, number of available
incident qubits. Its first such qubit ja determines the unique branch whose
new chosen support is still contained in C and whose new forbidden support is
still disjoint from C. This induction reaches U=C, where the circuit is tested.
Branches also partition any target completions according to their first chosen
available neighbor, so no rooted zero leaf is duplicated.

**Safety of every pruning/stopping rule.**

- The budget rule is exact: a nonzero syndrome requires at least one more qubit.
- The syndrome-weight rule is necessary: adding at most R columns of weight
  three cannot cancel more than 3R currently odd checks. Cancellations among
  added columns cannot make this bound unsafe.
- An odd check with no available neighbor cannot have its parity corrected by
  any permitted extension.
- Forbidding earlier candidates does not drop a circuit: a target using an
  earlier candidate belongs to that earlier branch, not the present one.
- Stopping on zero syndrome cannot truncate a proper subset of a circuit.
  Noncircuit cycles may be omitted by this stopping rule, but the circuit
  reduction proves that they are unnecessary for distance exclusion.
- There is no other pruning rule, decoder, random choice, numerical tolerance,
  or assumption about the desired logical class.

The first implementation's boundary test is exact Gaussian elimination in the
span of the columns of the boundary map. Every stored pivot retains its original
column coefficients. A zero residual supplies an actual boundary preimage;
a nonzero reduced residual proves non-membership in that span.

### C.4 Base enumeration certificate

All four primary base searches (Z and X, each at roots 0 and 39) have precisely
36 nodes, 7 expanded nodes, 5 budget leaves, 24 syndrome-bound leaves, zero blocked
check leaves and zero zero-syndrome leaves. Thus none has a circuit of weight
at most four. Translation and C.1-C.2 exclude every nonzero base cycle of weights
1 through 5. Together with z, this proves dZ=6; Section E handles X explicitly.

Implementation 2 independently finds 46 nodes, 7 expanded nodes, 15 budget
leaves, 24 syndrome-bound leaves, zero blocked leaves and zero zero-syndrome
leaves for each of its four base searches. It additionally checks all 78 columns
are distinct and nonzero and that all C(78,2)=3003 unordered pair sums are
nonzero and distinct. A weight-four cycle would give a collision between two
disjoint pair sums. Pairs sharing a coordinate cannot collide unless two
columns are equal. This is a further independent exhaustive exclusion of base
weights two and four.

## D. Complete cover circuit certificate and d2=14

### D.1 Explicit boundary preimage of tau(z)

Let a=A/g, b=B/g, and f=F/g. The U,V in A.3 satisfy Ua+Vb=1. Since
c=x^2(1+x^9) is divisible by g, (B1) implies
\(az_L+bz_R=0\pmod F\). Set

\[
v=Uz_R+Vz_L\pmod F,\qquad H=fv\pmod {F^2}.
\]

Then bv=zL and av=zR modulo F, by the Bezout identity and the preceding
syzygy. Multiplying by F gives

\[
BH=Fz_L\pmod {F^2},\qquad AH=Fz_R\pmod {F^2}.
\]

The explicit two-chain is the polynomial supported at

```
H = [1,8,9,10,11,12,13,15,16,17,18,19,20,23,24,25,
     27,28,31,32,34,37,38,41,43,44,46,48,51,53,54,
     57,61,63,65,66,68,74]
```

Both programs independently reconstruct this same H, by different solvers,
and check its products modulo 1+x^78. The result is exactly

```
B H mod (1+x^78) = [0,8,16,25,39,47,55,64]
A H mod (1+x^78) = [0,11,39,50]
```

Thus \(\widetilde\partial_2H=\tau(z)\), including its nontrivial-looking
weight-twelve cycle orbit.

### D.2 All cover circuit orbits through weight twelve

The following are the lexicographically canonical flat-support representatives
computed from the enumerated set. An exponent list in the preimage column
specifies s, and the representative is exactly (B s,A s) in R78. **Every row is
a boundary.** H in the last row is the explicit list in D.1.

| Orbit | Left support | Right support | Weight | Orbit size | Boundary preimage s |
|---:|---|---|---:|---:|---|
|1|`[0,2,13]`|`[0,8,25]`|6|78|`[0]`|
|2|`[0,2,5,13,70,72]`|`[8,17,25,70]`|10|78|`[0,70]`|
|3|`[0,2,11,24]`|`[0,8,11,19,25,36]`|10|78|`[0,11]`|
|4|`[0,2,13,17,19,30]`|`[0,8,17,42]`|10|78|`[0,17]`|
|5|`[0,2,13,25,27,38]`|`[0,8,33,50]`|10|78|`[0,25]`|
|6|`[0,2,15,26]`|`[0,8,13,21,25,38]`|10|78|`[0,13]`|
|7|`[0,2,65,69]`|`[12,14,65,67,73,75]`|10|78|`[65,67]`|
|8|`[0,2,5,13,17,19,30,70,72]`|`[8,42,70]`|12|78|`[0,17,70]`|
|9|`[0,4,26]`|`[0,2,8,10,13,21,25,27,38]`|12|78|`[0,2,13]`|
|10|`[0,8,16,25,39,47,55,64]`|`[0,11,39,50]`|12|39|H from D.1|

There are no other positive-weight circuit orbits of weight at most twelve.
The table is not supplied to either search. Each implementation discovers the
rooted circuits, expands their translations, groups the full set into orbits,
and solves for the preimage of each representative. Both produce the same table.

The table is equivalent, by translating some representatives, to the compact
list

\[
\partial_2(1),\quad
\partial_2(1+x^a)\ (a=2,8,11,13,17,25),\quad
\partial_2(A),\quad\partial_2(B),\quad\tau(z).
\]

The canonical representatives in rows 2,7,8 are respectively translates by
-8,-13,-8 of \(\partial_2(1+x^8)\), \(\partial_2(1+x^2)\), and
\(\partial_2(A)\). All other translations in this comparison are zero.

The nine size-78 orbits have translation stabilizer {0}; the size-39 orbit has
stabilizer {0,39}. These stabilizers are checked by all 78 shifts. Therefore the
counts are

\[
\begin{array}{c|r|r}
\text{weight}&\text{number of orbits}&\text{number of circuits}\\\hline
6&1&78\\
10&6&468\\
12&3&195
\end{array}
\]

and the total is 9*78+39=741.

A separate root-incidence count gives the same answer. The counts of actual
circuits containing the left and right identity qubits are respectively
(3,30,16) and (3,30,14) at weights (6,10,12). For weight w and total Nw,
translation invariance gives

\[
wN_w=78(N_{w,L_0}+N_{w,R_0}).
\]

This yields 78,468,195 independently of how the circuits were grouped into
orbits. Finally, the second implementation computes the full set again with a
different search tree and obtains byte-identical `circuits.txt`.

### D.3 Exact primary search accounting

The columns below partition all visited states into expanded nodes and terminal
leaves. A zero leaf is a zero-syndrome cycle; all zero leaves tested as boundaries.
The table lists all eight searches, including the independent X searches.

| Period | Sector | Root | Nodes | Expanded | Budget leaves | Syndrome leaves | Blocked leaves | Zero leaves |
|---:|:---:|---:|---:|---:|---:|---:|---:|---:|
|39|Z|0|36|7|5|24|0|0|
|39|Z|39|36|7|5|24|0|0|
|39|X|0|36|7|5|24|0|0|
|39|X|39|36|7|5|24|0|0|
|78|Z|0|985001|234911|5889|743178|924|99|
|78|Z|78|991809|236744|5488|748141|1347|89|
|78|X|0|941501|225282|4767|710265|1096|91|
|78|X|78|894576|213806|4215|675425|1039|91|

Here "syndrome" means the |sigma|>3R leaf rule, "blocked" means an odd check
has no available qubit, and "budget" means no remaining weight budget.
The primary zero-leaf and actual-circuit weight histograms are:

| Period | Sector | Root | Zero leaves (w=6,10,12) | Circuits (w=6,10,12) |
|---:|:---:|---:|---|---|
|78|Z|0|(3, 30, 66)|(3, 30, 16)|
|78|Z|78|(3, 30, 56)|(3, 30, 14)|
|78|X|0|(3, 30, 58)|(3, 30, 14)|
|78|X|78|(3, 30, 58)|(3, 30, 16)|

Every non-boundary-leaf count is zero. Notice that not every zero leaf is a
circuit; all zero leaves are checked for boundary membership before the circuit
filter is applied.

### D.4 Concluding the distance exclusion

Every circuit of weight at most twelve is a boundary, by the exhaustive search,
its completeness proof, and the explicit table. A cycle of weight at most twelve
is a sum of support-disjoint circuits of no larger weight, and hence is also a
boundary. This proves absence of every non-boundary cycle through weight twelve,
not just absence in a chosen logical class or projection sector.

Odd-weight cycles, including weight thirteen, are impossible by C.2. Thus
\(d_{Z,2}\ge14\). The explicit non-boundary w has weight fourteen, so
\(d_{Z,2}=14\).

## E. X/Z distance and physical permutation

For either period, let p-star replace x^j by x^(-j mod L), and define

\[
J(u,v)=(v^\star,u^\star).
\]

As a permutation of flat physical coordinates,

\[
J(j)=L+((-j)\bmod L)\quad(0\le j<L),
\]
\[
J(L+j)=(-j)\bmod L\quad(0\le j<L).
\]

This is a weight-preserving involution. Transposition of a multiplication matrix
is multiplication by the starred polynomial. Thus

\[
H_Z J(u,v)=B^\star v^\star+A^\star u^\star
           =(Au+Bv)^\star,
\]

so J maps Z-cycles to X-cycles. Also

\[
J(Bh,Ah)=(A^\star h^\star,B^\star h^\star)=H_X^T h^\star,
\]

so J maps Z-boundaries to X-boundaries. Its inverse is itself, so it induces a
weight-preserving bijection of nontrivial logical operators in the two sectors.

Both scripts check these matrix identities on every basis vector. Moreover,
both repeat their finite circuit exclusions directly with X-check matrix HZ
and X-boundary matrix HX^T. The resulting complete X circuit set agrees with
the J-image of the complete Z circuit set.

For completeness, the explicit X witnesses have supports

```
J(z), period 39:
  left  = [0,28]
  right = [0,14,23,31]

J(w), period 78:
  left  = [0,2,4,17,30,41,43,56,67,69]
  right = [14,23,31,39]
```

Consequently

\[
d_X=d_Z=6,\qquad \widetilde d_X=\widetilde d_Z=14.
\]

Finally, a Pauli operator represented by a binary X/Z pair has support equal
to the union of the two component supports. If it is a nontrivial logical,
at least one component is a nontrivial logical in its CSS sector. Its weight
is at least the corresponding sector distance. Conversely, a pure X or pure Z
minimum logical realizes the smaller sector distance. Thus these are also the
quantum code distances, not merely distances in a restricted Pauli sector.

## F. Standalone bitset verifier and matrix fingerprints

Run, with Python 3.10 or later,

```sh
python3 verify_bitset.py
```

No installation or other input files are required. To regenerate the stored
matrices and JSON report, the optional output-directory argument is

```sh
python3 verify_bitset.py --output-dir regenerated_bitset
```

The script checks cover validity at both the monomial and full-neighborhood
levels; commutation; polynomial identities; binary ranks and explicit row
relations; the witnesses and their nontriviality; H; all required distance
exclusions; J; independent X exclusions; and all orbit counts. It constructs
the orbit representatives and their boundary preimages from the discovered
circuits. It does not import any external packages or use randomness,
heuristics, floating point, or a precomputed circuit catalogue.

All checks use explicit exceptions, not Python `assert`, so `python -O` does
not disable them. Success is printed only after all checks and requested output
writes have completed. Its final stdout line is exactly

```
BB_DOUBLE_COVER_COUNTEREXAMPLE_VERIFIED
```

### Canonical matrix encoding

The hash input is ASCII. For a matrix with r rows and c columns, it is

```
GF2MATRIX v1\n
r c\n
row_0_bits\n
...
row_(r-1)_bits\n
```

In this display, `\n` denotes a single LF byte, not two literal characters.
The row bit strings have no separators, with columns increasing from 0 to c-1;
there is an LF after the last row. There are no spaces except the single space
between the two dimensions and the single space in the first line. The actual
matrix files are included.

```text
L=39 HX: 6e84e8c9cbb4cec64bb6d04405ae0ac9d87ce71e6a1a972e8b833ab1a824eef4
L=39 HZ: 341909344e831fdcb9aaa7d117aafe474718b0e25b610ae536b20eb7b370b6b3
L=78 HX: 468b9f9db365929d4506dbcbb38e09ff8a0f42c1c1997bb64295249d36dc361e
L=78 HZ: 4825f8e81f446083b9a23cf2fde781c966007930363e8e5fb0470780d19fc0de
```

The full cover circuit set is serialized as ASCII with first line
`BB_CIRCUITS v1`, second line `78 741`, and one sorted comma-separated flat
support per line thereafter, ordered by (weight, support tuple). Every line,
including the last, ends with LF. Its SHA-256 is

`ab05b51aa41a2cea530557a6d9940877c8974472edcff3aca84815ccbe79a957`.

Hashes identify exact data and conventions; they do not substitute for the
mathematical proof of exhaustive coverage.

## G. Second independent implementation

Run

```sh
python3 verify_polynomial.py
```

or optionally regenerate its outputs using

```sh
python3 verify_polynomial.py --output-dir regenerated_polynomial
```

It has no dependency on the first script or its files.

### G.1 Different representations and algebraic tests

Polynomials are frozensets of exponents, addition is symmetric difference,
and multiplication is convolution with exponent reduction modulo L. Chains
are pairs of polynomials. Matrix rows are sets, not bitsets. Binary rank is
computed using smallest-coordinate symmetric-difference pivots.

Boundary membership is decided by ordinary polynomial arithmetic and Bezout
identities. For the syndrome map (P,Q), let

\[
g=\gcd(P,Q,F_L),\quad a=P/g,\quad b=Q/g,\quad f=F_L/g.
\]

The program independently computes U,V,W with

\[
Ua+Vb+Wf=1.
\]

For a candidate chain (u,v), if either coordinate is not divisible by g, it is
not a boundary. Otherwise compute

\[
h=U(v/g)+V(u/g)\pmod f.
\]

The candidate is a boundary if and only if both direct congruences

\[
Qh=u\pmod {F_L},\qquad Ph=v\pmod {F_L}
\]

hold. Sufficiency is explicit construction. For necessity, if the candidate
is (Qh0,Ph0), division by g gives u/g=b h0 and v/g=a h0 modulo f. The Bezout
identity then gives h=h0 modulo f, which yields the same boundary in R_L.
This proves the oracle is exact, including in the non-semisimple period-78
ring. No binary boundary-span routine from implementation 1 is reused.

### G.2 Different exhaustive branching rule

The second search stores a chosen polynomial pair, a set of decided variables,
and the syndrome polynomial. The initial root is selected and decided one;
all other variables are undecided.

At a nonzero syndrome coefficient r, let T be all incident undecided variables.
Every completion must choose an odd-cardinality subset K of T. The search
branches on *all* odd subsets K of T. In each branch, all variables of T are
fixed at once: K becomes selected and T minus K becomes excluded. The polynomial
syndrome is updated by the convolution contributions of K. The check with fewest
available variables is used, ties broken by check index; candidate variables are
ordered by block and then exponent. Odd subsets are ordered by size and then
lexicographically. This is not first-present-candidate branching, and its search
tree and node/leaf counts are different.

For a target circuit, at every partial stage its intersection with T is one
of those odd subsets. It therefore has a unique continuing branch. A partial
zero syndrome cannot precede completion of the circuit. This proves exhaustive
coverage. The only pruning rules are the same necessary budget, degree-three
syndrome-weight, and no-available-neighbor tests, plus omission of odd subsets
whose cardinality exceeds the remaining budget. That last omission is plainly
safe because those branches alone would exceed the weight bound. Local caching
stores only already computed lists of odd assignments and their exact polynomial
contributions; it does not remove any assignment or search state.

### G.3 Exact secondary search accounting

| Period | Sector | Root | Nodes | Expanded | Budget leaves | Syndrome leaves | Blocked leaves | Zero leaves |
|---:|:---:|---:|---:|---:|---:|---:|---:|---:|
|39|Z|0|46|7|15|24|0|0|
|39|Z|39|46|7|15|24|0|0|
|39|X|0|46|7|15|24|0|0|
|39|X|39|46|7|15|24|0|0|
|78|Z|0|1602436|227115|424001|951214|0|106|
|78|Z|78|1559534|221268|414024|924137|0|105|
|78|X|0|1578044|223528|415849|938563|0|104|
|78|X|78|1561758|218276|408291|935086|0|105|

The additional counters of odd assignments skipped solely because their sizes
exceed the remaining budget are 67 for each base search, and respectively
169618,164926,165710,156186 for cover Z-left, Z-right, X-left, X-right.
The secondary zero-leaf and actual-circuit histograms are:

| Period | Sector | Root | Zero leaves (w=6,10,12) | Circuits (w=6,10,12) |
|---:|:---:|---:|---|---|
|78|Z|0|(3, 30, 73)|(3, 30, 16)|
|78|Z|78|(3, 30, 72)|(3, 30, 14)|
|78|X|0|(3, 30, 71)|(3, 30, 14)|
|78|X|78|(3, 30, 72)|(3, 30, 16)|

Every non-boundary-leaf count is zero. Both implementations agree on all four
canonical matrices, ranks, witnesses, H, all 741 cover circuits, all ten canonical
orbits and preimages, and both sector distances. The independent X search is
performed in this implementation too. `EXECUTION_METADATA.json` records the
actual interpreter, exit statuses, script hashes and transcript hashes.

## H. Conclusion

All certificates succeeded. The exact parameter pair is

\[
\boxed{[[78,4,6]]\longrightarrow[[156,4,14]]}.
\]

It is a valid binary BB double cover under the definitions and Theorem 3.1 of
[S], including its explicitly permitted m=1 instances. Its upper distance
inequality fails because 14>12. Therefore the universal upper-bound statement
and hence [S, Conjecture 1, p. 26] are false.

STATUS: UPPER_BOUND_FALSE

STATUS: ORIGINAL_DISTANCE_CONJECTURE_FALSE
