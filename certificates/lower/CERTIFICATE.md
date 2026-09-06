# A distance-decreasing binary BB double cover

## Theorem

With the definitions and monomial covering conditions of Theorem 3.1 of
Symons–Rajput–Browne, *Sequences of Bivariate Bicycle Codes from Covering
Graphs*, arXiv:2511.13560v3, there is a valid binary BB double cover

\[
[[156,4,14]]\longrightarrow [[312,8,12]].
\]

In particular the universal lower bound \(d_2\ge d\) is false.

This is a computer-assisted theorem. Cycle identities, nontriviality, dimensions,
and the reduction of distance to a finite circuit enumeration are proved below.
Two standalone Python implementations reproduce the exhaustive exclusions.
Neither implementation reads the other implementation or its outputs.

## 1. Input and conventions

Base lattice parameters: \((\ell,m)=(78,1)\).
Cover lattice parameters: \((\widetilde\ell,\widetilde m)=(78,2)\).

\[
A=1+x^8+x^{25},\qquad B=1+x^2+x^{13},
\]
\[
\widetilde A=1+x^8y+x^{25},\qquad
\widetilde B=1+x^2y+x^{13}.
\]

Work over
\[
R=\mathbb F_2[x]/(1+x^{78}),\qquad
\widetilde R=\mathbb F_2[x,y]/(1+x^{78},1+y^2).
\]

The Koszul maps are
\[
\partial_1(u,v)=Au+Bv,\qquad \partial_2h=(Bh,Ah),
\]
and similarly with tildes. The physical coordinates are two blocks of the
monomial basis. For periods \((\ell,m)\), index \(x^iy^j\) by \(im+j\),
and the right block by \(\ell m+im+j\).

The multiplication matrix convention is that column \(h\) is the coefficient
vector of \(Ph\). Therefore \(H_X=(M_A\ M_B)\) and
\(H_Z=(M_B^T\ M_A^T)\).

The projection is \(p(x^iy^j)=x^i\). Each vertex has two preimages. The lifted
exponents reduce term-by-term to the base exponents, and the periods are related
by \(u=1,t=2\) in Theorem 3.1. Every polynomial has three distinct terms.
The monomial conditions also directly give bijections on the six neighbors of
every check and the six neighbors (across both check types) of every qubit.
Both verifiers check these neighborhood bijections on every vertex.

The source definitions permit a period equal to one; this is the same convention
used in the preceding research rounds. Here it simply means \(y=1\) in the base
ring. No assumption \(m>1\) occurs in the covering conditions.

Both Tanner graphs are connected. Constant terms connect the four vertex types
within each cell. The monomials \(x^{25}\) and \(x^{13}\) generate all x-shifts
because \(\gcd(25,13,78)=1\); in the cover \(x^8y\) additionally gives the
y-shift. The bitset verifier also checks connectivity by a full graph traversal.

## 2. Dimensions

Let \(g=1+x+x^2\). Ordinary polynomial gcd gives
\[
\gcd(A,B,1+x^{78})=g.
\]
Thus \(\dim R/(A,B)=2\). For a BB Koszul complex the inversion-and-block-swap
permutation identifies \(\partial_2\) with \(\partial_1^T\), up to basis
permutations, so
\[
k=2\dim\operatorname{coker}\partial_1=4.
\]

For the cover, eliminate \(y\) using \(\widetilde B=0\):
\[
y=x^{-2}(1+x^{13}).
\]
The relation \(y^2=1\) becomes \(B(x)^2=0\); the other check polynomial becomes
\[
C=A+x^6B=1+x^6+x^{19}+x^{25}=(1+x^6)(1+x^{19}).
\]
Since \(x\) is already a unit modulo \(1+x^{78}\), this gives an actual quotient
ring isomorphism
\[
\widetilde R/(\widetilde A,\widetilde B)
\cong
\mathbb F_2[x]/(1+x^{78}, B^2,C).
\]
The common gcd is
\[
\gcd(1+x^{78},B^2,C)=g^2=1+x^2+x^4.
\]
One can check this by polynomial Euclidean division. Also,
\(\gcd(B,1+x^{78})=g\), \(1+x^{78}=(1+x^{39})^2\), and
\(g^2\mid 1+x^6\), which explain the extra multiplicity. Hence the quotient has
binary dimension four and \(k_2=8\).

Both implementations independently perform binary elimination, obtaining:

| Code | qubits | rank HX | rank HZ | k |
|---|---:|---:|---:|---:|
| Base | 156 | 76 | 76 | 4 |
| Cover | 312 | 152 | 152 | 8 |

No distance conclusion is inferred from these ranks.

## 3. An algebraically certified cover logical of weight 12

Set
\[
\sigma=1+x^{39}y,\quad
\zeta_L=1+x^8y+x^{16}+x^{25},\quad
\zeta_R=1+x^{11}y,
\]
and
\[
w=\sigma(\zeta_L,\zeta_R).
\]

Its coordinate supports, written as exponent pairs \((i,j)\), are

```
left  = [(0,0),(8,1),(16,0),(25,0),(39,1),(47,0),(55,1),(64,1)]
right = [(0,0),(11,1),(39,1),(50,0)]
```

The corresponding flat coordinates are

```
[0,17,32,50,79,94,111,129,156,179,235,256]
```

In \(\mathbb F_2[x,y]/(1+y^2)\), before reducing the x-period, direct
multiplication gives
\[
\widetilde A\zeta_L+\widetilde B\zeta_R
=\sigma y(x^2+x^{11}).
\]
Moreover \(\sigma^2=1+x^{78}\). Consequently \(\widetilde\partial_1w=0\)
in \(\widetilde R\). All twelve displayed coordinates are distinct.

### Nontriviality without a distance search

Let
\[
T=\mathbb F_4[\eta]/(\eta^2),\qquad
\mathbb F_4=\mathbb F_2(\omega),\quad \omega^2+\omega+1=0.
\]
Define
\[
\phi(x)=\omega+\eta,\qquad \phi(y)=1+\omega\eta.
\]
These satisfy \(\phi(x)^{78}=1\), \(\phi(y)^2=1\), so \(\phi\) is a ring map
from \(\widetilde R\) to \(T\).

Here
\[
\phi(x^8y)=\phi(x^2y)=\omega^2+\eta,
\quad \phi(x^{25})=\phi(x^{13})=\omega+\eta.
\]
Thus
\[
\phi(\widetilde A)=\phi(\widetilde B)=0.
\]
Both coordinates of every cover boundary therefore map to zero. However,
\[
\phi(\sigma)=\eta,\qquad
\phi(\zeta_L)=\omega,\qquad
\phi(\zeta_R)\equiv\omega\pmod\eta,
\]
and hence
\[
\phi(w_L)=\phi(w_R)=\omega\eta\ne0.
\]
This proves \([w]\ne0\), and thus \(d_{Z,2}\le12\).

## 4. Base distance witness and the projected boundary

An explicit weight-14 base logical is
\[
v_L=x^{39}(1+x^8+x^{16}+x^{25}),
\]
\[
v_R=1+x^{11}+(1+x^{39})(x^9+x^{22}+x^{35}+x^{37}).
\]
Its supports in the cyclic base coordinates are

```
left  = [39,47,55,64]
right = [0,9,11,22,35,37,48,61,74,76]
```

The ordinary polynomial identity
\[
Av_L+Bv_R=(1+x^{78})(1+x^2+x^9)
\]
proves it is a cycle. Modulo \(g\), both coordinates are \(x\ne0\), whereas
both coordinates of any boundary vanish. Thus \([v]\ne0\).

The new cover witness projects not to this logical but to the base boundary
\[
q=p(w)=(1+x^{39})(1+x^8+x^{16}+x^{25},\ 1+x^{11}).
\]
Its left and right supports are respectively

```
[0,8,16,25,39,47,55,64]
[0,11,39,50]
```

Here is an explicit two-chain H with \(\partial_2H=q\). Exponent lists specify
all coefficients equal to one:

```
H = [1,8,9,10,11,12,13,15,16,17,18,19,20,23,24,25,27,28,31,32,
     34,37,38,41,43,44,46,48,51,53,54,57,61,63,65,66,68,74]
```

Direct multiplication modulo \(1+x^{78}\) gives \(BH=q_L\), \(AH=q_R\).
The first verifier checks this displayed preimage; the second independently
constructs a preimage through polynomial Bezout equations.

## 5. Exhaustive distance exclusions

Every column of either check matrix has odd weight three. Thus every Z-cycle
and X-cycle has even weight. To prove distances 14 and 12 it suffices to exclude
non-boundary cycles through weight 12 and weight 10, respectively.

### Circuit reduction

A circuit is a nonempty cycle support with no proper nonempty cycle support.
A minimum-weight non-boundary cycle must be a circuit. Indeed a proper subcycle
is either a smaller non-boundary cycle, or a boundary whose removal gives a
smaller representative of the original nonzero homology class.

Alternatively every cycle is a support-disjoint sum of circuits, by repeatedly
removing a minimal nonzero subcycle. Therefore if every circuit of weight at
most b is a boundary, every cycle of weight at most b is a boundary.

For an already verified cycle with support S, the circuit test is exactly
\[
\operatorname{rank}(H_X|_S)=|S|-1.
\]
The all-one vector on S is in the restricted kernel; it is the only nonzero
kernel vector exactly when no proper nonempty subcycle exists.

### Exhaustive search 1

Variables use the flat coordinate ordering stated above; checks use increasing
monomial indices. Search separately from the identity left and identity right
qubits (roots 0 and N). All translates under the base group or cover group are
expanded after the rooted searches. This is exhaustive because translations act
transitively on each block and preserve the code and its boundary space.

A search state contains a selected set U, forbidden set E, and exact syndrome
s. At nonzero syndrome choose an odd check with the fewest available incident
variables, breaking ties by the check index. Order its candidates increasingly.
For candidate j, select j and forbid the candidates preceding j in later
branches, updating s by XOR with column j. Candidates later than j remain free
in its branch.

For any fixed target circuit containing the root there is a unique continuing
branch: choose the first of its still unselected variables incident to the chosen
odd check. This preserves U contained in the target circuit and E disjoint from
it. A proper subset of the target circuit cannot have zero syndrome, so the
branch reaches the complete target circuit.

The only pruning rules are:

* Remaining weight budget is zero while the syndrome is nonzero.
* The number of odd checks exceeds three times the remaining budget. Each
  additional column can affect at most three of the odd checks.
* An odd check has no available incident variable.
* At zero syndrome, test boundary membership and stop. Such a leaf cannot be
  a proper subset of a circuit being sought.

First-present branching partitions completions rather than discarding them.
No expected circuit list, assumed logical sector, numerical optimization,
randomized rule or decoder is used. Every zero leaf is tested for membership
in the boundary span before the circuit filter is applied. Membership uses exact
binary elimination retaining coefficients in the original boundary generators.

### Exhaustive search 2

The second program uses frozenset polynomials and a different search tree.
At an odd check it branches on every odd-cardinality subset of its undecided
neighbors, selecting that entire subset and fixing all other neighbors to zero.
Any circuit completion has one and only one such subset. A subset exceeding the
remaining weight budget is skipped; the other stopping and syndrome bounds are
as above. It does not copy first-present branching.

Ranks use smallest-coordinate set elimination. Boundary membership uses the
independent polynomial solver described in Section 8, not a binary boundary-span
oracle. Both X and Z sectors are searched directly in each implementation.

### Complete circuit classifications

In the base, all circuits through weight 12 are translations of
\[
\partial_2(1),
\]
\[
\partial_2(1+x^a),\quad a\in\{2,8,11,13,17,25\},
\]
\[
\partial_2(A),\quad\partial_2(B),\quad q=\partial_2(H).
\]
Their weights are 6, 10, and 12 in the displayed groups. The first nine orbits
have size 78; the orbit of q has size 39. All are boundaries. Counts:

| Weight | Base circuits |
|---:|---:|
| 6 | 78 |
| 10 | 468 |
| 12 | 195 |
| total | 741 |

In the cover, all circuits through weight 10 are translations of
\[
\widetilde\partial_2(1),
\]
\[
\widetilde\partial_2(1+x^a y^b),\quad
(a,b)\in\{(2,1),(8,1),(11,1),(13,0),(17,1),(25,0)\}.
\]
All seven orbits have size 156. All are boundaries. Counts:

| Weight | Cover circuits |
|---:|---:|
| 6 | 156 |
| 10 | 936 |
| total | 1092 |

There are no circuits of other positive weights within the respective bounds.
These classifications are outputs checked after both unrestricted searches;
they are never input to the search or its pruning.

The first program reconstructs individual orbit representatives and preimages.
Both programs independently reconstruct byte-identical complete circuit-support
files. All other supports in these classifications are obtained by translating
the displayed boundary preimages.

### Exact search counts (Z sector)

| Code | root | bound | implementation 1 nodes | implementation 2 nodes |
|---|---:|---:|---:|---:|
| Base | 0 | 12 | 985001 | 1602436 |
| Base | 78 | 12 | 991809 | 1559534 |
| Cover | 0 | 10 | 84843 | 153347 |
| Cover | 156 | 10 | 87785 | 155951 |

All non-boundary leaf counts are zero. The transcripts and JSON reports include
all X-sector searches, pruning counters, zero-leaf histograms and rooted circuit
counts. The first Z searches have zero-leaf histograms
(3,30,66), (3,30,56) at base weights (6,10,12), and (3,30) at cover weights (6,10)
for each root. The second Z searches have corresponding base histograms
(3,30,73), (3,30,72), and cover histograms (3,30), (3,30).
Additional zero leaves in the second implementation are noncircuit boundaries.

Circuit reduction and parity now give \(d_Z\ge14\), \(d_{Z,2}\ge12\).
The explicit nontrivial witnesses attain these bounds.

## 6. X/Z distances

In either ring let \(f^\star(x,y)=f(x^{-1},y^{-1})\). Then
\[
J(u,v)=(v^\star,u^\star)
\]
is a weight-preserving involution. It maps a coordinate
\(L_{i,j}\) to \(R_{-i\bmod\ell,-j\bmod m}\), and vice versa.

For a Z-cycle,
\[
B^\star v^\star+A^\star u^\star=(Au+Bv)^\star=0.
\]
For a Z-boundary,
\[
J(Bh,Ah)=(A^\star h^\star,B^\star h^\star),
\]
which is an X-boundary. Thus J identifies both homology sectors, preserving
weight and nontriviality. Both programs also verify these identities on every
basis vector and separately enumerate the X sector.

Therefore
\[
d_X=d_Z=14,\qquad d_{X,2}=d_{Z,2}=12.
\]
For a general CSS Pauli logical, at least one of its X and Z components is a
nontrivial pure-sector logical, and the Pauli support contains the support of
that component. This proves the stated full quantum distances.

## 7. The transfer-sector obstruction is realized

Use \(\varepsilon=1+y\), so
\[
\widetilde A=A+\varepsilon x^8,\qquad
\widetilde B=B+\varepsilon x^2.
\]
Thus
\[
D_1=(x^8\ \ x^2),\qquad D_2=\binom{x^2}{x^8}.
\]
Write \(w=q+\varepsilon r\). The second-sheet coefficients are
\[
r=(x^8+x^{39}+x^{55}+x^{64},\ x^{11}+x^{39}).
\]
Both physical sheets have weight six. Since \(q=\partial_2H\), put
\[
a=r+D_2H.
\]
Then \(\partial_1a=0\), and the exact chain identity is
\[
w+\widetilde\partial_2H=\varepsilon a=\tau(a).
\]
The independently certified nontriviality of w proves \(\tau_*[a]\ne0\),
and hence \([a]\ne0\). Since the base distance is 14, \(\delta([a])\ge14\).

For the earlier transfer-class metric,
\[
\lambda(\alpha)=\min_{a'\in\alpha,\,s\in R}
\bigl(|a'+D_2s|+|a'+(D_2+\partial_2)s|\bigr),
\]
choose \(\alpha=[a]\), \(s=H\). The two terms become \(|r|=6\) and
\(|r+q|=6\). The cover distance gives the matching lower bound. Consequently
\[
\lambda([a])=12<14\le\delta([a]).
\]
This explicitly refutes the remaining transfer-sector metric inequality.

For this new double cover, transfer is in fact injective on all base logical
classes. The end homology dimensions are two in the base and four in the cover.
The long exact sequence forces \(\beta_2=0\), hence \(\ker\tau_*=0\). The
bitset verifier independently checks \(D_2h\) is a boundary for every element
of a basis of \(H_2\). Injectivity does not prevent the stabilizer shortening
exhibited above.

A useful necessary condition used in the search is the following short-filling
observation. If a nontrivial cover cycle Y projects to \(\partial_2s\), then for
every lifted two-chain \(\widehat s\),
\[
|Y|+|\widetilde\partial_2\widehat s|\ge2d.
\]
Indeed \(Y+\widetilde\partial_2\widehat s=\tau(b)\) for a nontrivial base cycle
b, so its weight is at least \(2d\), and the triangle inequality applies.
In this example a cover boundary with the same literal projection q must have
weight at least 16, although q itself is a weight-12 base boundary.

## 8. Independent polynomial membership solver

For univariate equations \(Ph=e,Qh=f\) modulo \(F=1+x^{78}\), let
\(g=\gcd(P,Q,F)\). Compute
\[
U(P/g)+V(Q/g)+W(F/g)=1.
\]
If e or f is not divisible by g there is no solution. Otherwise set
\[
h=U(e/g)+V(f/g)\pmod{F/g}
\]
and check both equations. This is an exact criterion: any solution must have
this residue modulo F/g, and their common kernel consists of multiples of F/g.
This argument does not require F to be squarefree.

For the two-layer ring write
\[
P=P_0+yP_1,\quad Q=Q_0+yQ_1,
\]
where Q1 is a monomial (this holds in both directly searched sectors here).
Set \(c=Q_1^{-1}\),
\[
D=Q_0^2+Q_1^2,\qquad C=P_0+P_1cQ_0.
\]
For \((u,v)=(Qh,Ph)\), decompose all vectors into y coefficients and solve
\[
D h_0=Q_1u_1+Q_0u_0,\qquad
C h_0=v_0+P_1cu_0.
\]
Then
\[
h_1=c(u_0+Q_0h_0).
\]
The program checks all four original coefficient equations. Necessity follows
by eliminating h1. A change in h0 annihilated by both C and D also leaves all
four outputs unchanged, since
\[
P_1Q_1+P_0Q_0=CQ_0+P_1cD.
\]
Thus the canonical univariate solution cannot falsely reject an existing
boundary. This supplies a genuine algebraic alternative to the first program's
binary span oracle.

## 9. Reproduction and serialization

```
python3 verify_lower_bitset.py --output-dir reproduced_bitset
python3 verify_lower_polynomial.py --output-dir reproduced_polynomial
```

Each file is independently runnable with Python 3.10+ and its standard library.
Neither needs any other file from the archive. No assertions are used as proof
gates, so `python3 -O` does not disable verification.

Each script's last stdout line is

```
BB_LOWER_BOUND_COUNTEREXAMPLE_VERIFIED
```

only after every check has passed.

Matrices use this canonical ASCII encoding:

```
GF2MATRIX v1
rows columns
row_0_bits
...
row_last_bits
```

Bits appear in increasing column order, without separators, with one LF after
every line including the last. SHA-256 hashes:

```
base HX  468b9f9db365929d4506dbcbb38e09ff8a0f42c1c1997bb64295249d36dc361e
base HZ  4825f8e81f446083b9a23cf2fde781c966007930363e8e5fb0470780d19fc0de
cover HX 9fd965e3e18cf16da6313af087fabbbba2619cf5031ad4233337ea10b21c47c8
cover HZ 6a9433d6d4dc4a955d4e57fbf16f6088ef1422dc5f324161c7c1888085113bcb
```

Circuit files contain comma-separated increasing flat supports, one per line,
sorted first by weight and then lexicographically, with no header and with a
final LF. Their hashes are:

```
base (741 circuits)
78294b4b567fbcfa389e951a72edc96e6a5bb40c099ee9eaf3e2abe1571aa7fa

cover (1092 circuits)
a2361757be4c36b7bd2297ab1be4319e0658e2a2a4d07ef703c5bfbe23b3914d
```

The two independently generated versions of each of these six files agree
byte-for-byte. The execution transcripts, JSON reports, comparison results, and
an SHA-256 integrity manifest are included in the archive.

## Final conclusion

\[
\boxed{[[156,4,14]]\longrightarrow[[312,8,12]],\qquad12<14.}
\]

STATUS: LOWER_BOUND_FALSE
