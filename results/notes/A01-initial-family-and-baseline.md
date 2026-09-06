[全部研究结果](../README.md) · [逐项结论](../CLAIMS.md) · [原始完整文本](../../research/amplification/history/01_initial_family_and_baseline.md)

> 完整研究笔记的 GitHub 阅读版；仅调整数学分隔符、引用标记与链接。历史状态、限制和证明内容均保留。当前结论以总登记表中的逐项状态为准；这里的“验证”不等于独立同行评审。

# Initial amplification round: conversation-derived preservation

**Provenance:** this is an archival reading copy of material present in the earlier
visible assistant response and tool-call text, not the originally linked report
or its ZIP. Those original files are not mounted in this export session. The
finite seed now also has intact independent verifiers in
[round 03](../../research/amplification/research/03_amplification_search/README.md). No new mathematical
argument or claim of original-file byte identity is made here.

The original principal status was `NEW_PARAMETRIC_LOWER_BOUND`. At that stage,
bounded versus unbounded amplification was unresolved. The original response
reported an infinite connected 7/3 family, transfer/homology formulas, special
factor-two results, and an O(N^(3/4)) geometric upper bound. Later reports improve
the general bounds but not the record ratio.

## 1. The original family and its exact parameters

For every integer j >= 0, let



$$
q=42j+13,\qquad L=3q=126j+39,
$$




$$
A_j=1+x^{q-5}+x^{2q-1},\qquad
B_j=1+x^{q-11}+x^{2q-13}.
$$



The unchanged-polynomial cover from period L to 2L was established as



$$
[[252j+78,4,6]]\longrightarrow[[504j+156,4,14]].
$$



In particular, j=0 gives A=1+x^8+x^25, B=1+x^2+x^13 and
[[78,4,6]] -> [[156,4,14]]. The distances remain 6 and 14; neither grows with j.
The family is not a disjoint union construction.

### Fixed-strip coordinate change

Put b=2q-1. Since q=42j+13, gcd(b,2L)=1. The substitution w -> x^b converts the
cover polynomials to



$$
1+w+w^{L+5},\qquad 1+w^{L+11}+w^{13}.
$$



For odd L, let z=w^(L+1) and t=w^L. Then w=tz, z^L=t^2=1, and the cover becomes



$$
\mathcal A=1+tz+z^5,\qquad
\mathcal B=1+z^{11}+tz^{13}.
$$



The base is



$$
a_0=1+z+z^5,\qquad b_0=1+z^{11}+z^{13}.
$$



The support of A_j contains the identity and x^b, where b generates both finite
cyclic groups. The corresponding Tanner graphs are connected. The transformation
also shows why large original exponents do not imply growing interaction range.

### Dimension and logical labels

Set



$$
g=1+z+z^2,\quad p=1+z^2+z^3,
$$




$$
a_0=gp,\qquad b_0=a_0S,\qquad
S=1+z+z^2+z^3+z^4+z^6+z^8.
$$



The root orders of g and p are 3 and 7. Each L is odd, divisible by 3, and not
by 7, so the base gcd is g and k=4.

Over the infinite strip T=F_2[z^(+/-1),t]/(t^2+1), the following explicit
factorization was recorded:



$$
G=z^2+t(1+z),
$$




$$
P=(z+z^3)+t(1+z+z^2),
$$




$$
Q=z^2+z^4+z^8+z^{10}
+t(1+z+z^2+z^3+z^6+z^7+z^8+z^9+z^{11}),
$$




$$
\mathcal A=GP,\qquad\mathcal B=GQ.
$$



The monic G is a non-zero-divisor in T. Hence every infinite-strip cycle obeys
Pu+Qv=0. At the relevant finite periods, P is a unit because its t=1 reduction
is p. Every such compact cycle therefore has the form alpha(Q,P); boundaries
are its G-multiples. Writing epsilon=1+t gives G=g+epsilon(1+z) and G^2=g^2.
Square-freeness of z^L+1 gives



$$
R_L^{\rm strip}/(G)\cong\mathbf F_2[z]/(g).
$$



Thus k_2=4, and **for an infinite-strip cycle specialized at these periods** its
nonboundary test is



$$
v(z,1)\bmod g\ne0.
$$



This label is not asserted to classify arbitrary finite winding cycles.

### Uniform attaining words

The base word



$$
U_0=1+z+z^5+z^{10},\qquad V_0=1+z^2
$$



has weight six, satisfies a_0 U_0+b_0 V_0=0, and has V_0 mod g=z != 0.

One weight-fourteen strip word in the earlier visible final response is



$$
U=1+z^2+z^5+z^9+z^{10}+z^{14}
+t(z+z^3+z^6+z^8+z^{10}),
$$




$$
V=1+z^4+tz^6.
$$



It satisfies the strip cycle equation and has V(z,1) mod g=z != 0.
An earlier tool-visible draft used a different weight-fourteen representative;
these should not be treated as inconsistent supports for a uniquely specified
logical. Later rounds retain their own independently audited words and gauges.

### Uniform lower bounds

A minimum nonboundary has column-matroid circuit support. Every cycle has even
weight because each column has odd weight three. In the fixed strip all offsets
lie in [0,13]. A simple Tanner path through at most w selected columns has
integer displacement at most 13w. If L>13w, a closed finite path cannot have
nonzero winding and its circuit lifts to the infinite strip.

For w<=12, the lifted column-position diameter is at most 13(w-1)<=143.
Normalize a leftmost column to position zero. At the leftmost occupied check,
parity forces both an A and B column in an occupied sheet; a sheet exchange
normalizes the A column to A(0,0).

The earlier final response reported two exhaustive searches of this fixed box:

| Implementation | Nodes | Terminal zero-syndrome supports | Nonzero labels |
|---|---:|---:|---:|
| C++, mutable | 4,471 | 10 | 0 |
| Python, immutable sets | 4,572 | 15 | 0 |

**Availability warning:** the original fixed-box scripts, tables, and raw logs
for these exact counts are not in the mounted bundles. These counts are preserved
as conversation evidence, not newly re-certified outputs. The later retained
slope-(2,1) closure certificates provide separate arbitrary-support compact
minima and large-period realizations; their gauges and arguments are in their
own reports.

For j>=1, L>=165>156; exclusion through twelve and the weight-fourteen witness
therefore give d_2=14. The base lower bound for j>=1 was symbolic. A compact base
cycle has form (Sf,f). A nonzero such pair cannot have total weight <=4. The only
nontrivial candidate not immediately excluded by weight/noninvertibility is a
binomial f=1+z^a with Sf=1+z^b. Divisibility makes a divide b and makes S a
geometric sum. Weight seven and degree eight would force 8=6a, impossible.

The j=0 finite seed was separately checked. Its original-coordinate base witness
was



$$
u=1+x^8+x^{16}+x^{25},\qquad v=1+x^{11}.
$$



A recorded cover witness had supports



$$
\operatorname{supp}u=\{0,5,8,16,25,30,33,38,50,55,75\},
\quad \operatorname{supp}v=\{0,22,33\}.
$$



The earlier response quoted distinct finite lower-search counts
1,726,052 (strip/Gaussian) and 1,976,812 (cyclic/Bezout) through weight twelve.
Their original logs are unavailable; the independent finite seed audit in
round 03 is available and was rerun during this export.

## 2. Univariate normal form and repeated-root transfer

Let S=F_2[x], F=x^L+1, R=S/(F), c=gcd(A,B), A=ca, B=cb, and ar+bs=1.
Set g=gcd(c,F), h=F/g. The middle-coordinate change



$$
(u,v)\longmapsto (au+bv,\;su+rv)
$$



turns the differentials into (c,0) and (0,c)^T. Hence



$$
H_0\cong S/(g),\quad H_2=(h)\cong S/(g),\quad
H_1\cong(S/(g))^2,\quad k=2\deg g.
$$



For a cycle, write au+bv=h alpha and su+rv=beta mod g. It is a boundary exactly
when alpha=beta=0. Representatives are



$$
(u,v)=\bigl(rh\alpha+b(\beta+c\eta),\;sh\alpha+a(\beta+c\eta)\bigr)\pmod F.
$$



This is not an isometric splitting. Hamming distance still minimizes in the
original coordinates over eta and all nonzero classes.

For unchanged-polynomial doubling put g_2=gcd(c,F^2). Then



$$
\widehat\tau(\alpha,\beta)=((g_2/g)\alpha,F\beta)\pmod{g_2},
$$




$$
\widehat p(\widetilde\alpha,\widetilde\beta)
=((Fg/g_2)\widetilde\alpha,\widetilde\beta)\pmod g.
$$



When g_2=g, transfer keeps the first component and kills the second. The
trinomial multiplicity argument gives the univariate dichotomy k_2 in {k,2k}
in the term-matched setting described in the original response.

## 3. Homological rank and small-distance baseline

For a binary double cover, epsilon=1+t has square zero and the complexes fit in



$$
0\longrightarrow C\xrightarrow{\tau}\widetilde C\xrightarrow p C\longrightarrow0.
$$



For M=R/(A,B) and its cover analogue, quotienting by epsilon gives M while the
epsilon image is a quotient of M. This yields k<=k_2<=2k. Counting the two
connecting-map ranks in the long exact sequence gives



$$
\operatorname{rank}\widehat\tau_1
=\operatorname{rank}\widehat p_1=k_2/2.
$$



Thus k_2=2k makes transfer injective and gives d_2<=2d. More generally, for
homological spanning thresholds lambda_r,



$$
d_2\le2\lambda_{k-k_2/2+1}(Q).
$$



The earlier response also gave d=2 => d_2<=4 for weight-six BB covers, including
bivariate cases. Its two mechanisms were recorded as follows.

For a mixed weight-two class, gauges give (1,1) and A=B=C. A cover has
B'=A'+epsilon D, with p(D) a subset of three C terms. Empty/full subsets give a
short projected lift. Otherwise p(D) or C+p(D) is a monomial, so (C,p(D))=R.
A boundary preimage for (epsilon,epsilon) would first be forced into epsilon R'
and would then make C invertible, contradicting positive dimension.

For a one-block class (1+h,0), its three-term support is translation invariant
under h, so h has order three and A=1+h+h^2 after a gauge. The unique odd-order
lift H and the idempotent S_H=1+H+H^2 split the cover into summands. Either the
weight-two class lifts, or its weight-four transfer has a boundary preimage only
if the original class was a boundary. The original linked full report containing
that final idempotent calculation is unavailable. Later retained arguments
explicitly list this small-distance result as inherited input.

## 4. Early metric failures and historical upper bounds

The weight-twelve cycle epsilon(U_0,V_0) is a nonboundary over the infinite strip
but a boundary after the relevant finite periods are imposed. This was an early
negative control for confusing universal homology with its finite image.

The primitive divided-polynomial word (Q,P) has weight eighteen, while smaller
sixteen- and fourteen-weight representatives exist. A gcd or primitive-syzygy
weight is only an upper bound.

The natural Frobenius construction (Au^2,Bv^2) satisfies a cycle equation modulo
F^2, but



$$
(Au^2,Bv^2)+(Buv,Auv)=(u(Au+Bv),v(Au+Bv)).
$$



Writing Au+Bv=Fh shows why its class can be a killed transfer. This is a failed
proof of factor three, not a counterexample to factor three.

The initial final response's historical bound was



$$
7/3\le\Gamma(N)\le
\max\{2,\min(N/4,3\sqrt{\gamma_4}\,N^{3/4})\},\qquad N\ge78.
$$



It combined the d=2 special case with a published four-generator quotient-lattice
bound. A tool-visible draft used a different conservative constant and a direct
character/cleaning argument. These are historical formulations, not the current
best bound; no numerical reconciliation was attempted during export. The later
intact reports state the square-root Gamma bound and cubic f(d) bound with their
own dependencies.

## 5. Finite members preserved in the conversation

| j | L | Nonconstant A exponents | Nonconstant B exponents | Base | Cover |
|---:|---:|---|---|---|---|
|0|39|8,25|2,13|[[78,4,6]]|[[156,4,14]]|
|1|165|50,109|44,97|[[330,4,6]]|[[660,4,14]]|
|2|291|92,193|86,181|[[582,4,6]]|[[1164,4,14]]|
|3|417|134,277|128,265|[[834,4,6]]|[[1668,4,14]]|

These are uniform-family claims, not independent exhaustive finite searches at
all four lengths. The original response said j=1 also received a direct finite
cross-check. No inequivalence or maximality claim was made.

## Appendix A. Alternative compact-specialization proof in the early tool-visible draft

The earlier report-writing command also contained the following uniform route,
which avoids relying on a bounded-box circuit count. It is preserved here as an
existing alternative derivation, not a new argument introduced during export.

Let P=F_2[z,z^-1], S=P[epsilon]/(epsilon^2), and use t=1+epsilon. Write



$$
a=1+z+z^5=gp,\quad b=aS_0=1+z^{11}+z^{13},
$$




$$
S_0=1+z+z^2+z^3+z^4+z^6+z^8,\quad E=z^{13}+zS_0.
$$



The strip checks are a+epsilon z and aS_0+epsilon z^13. Direct division gives
gcd(a,E)=g. The first check is a non-zero-divisor, and



$$
S/(a+\epsilon z)\cong P/(a^2),\qquad\epsilon\mapsto a/z.
$$



The second check becomes aE/z. Consequently the draft computed



$$
H_0(C_\infty)\cong P/(ag)=P/(g^2p),\quad H_2(C_\infty)=0,
$$




$$
H_1(C_\infty)\cong\operatorname{ann}_{P/(a^2)}(aE/z)
=(p)/(a^2)\cong P/(ag).
$$



For a cycle whose right component is v=v_0+epsilon v_1, its coordinate is



$$
\frac{v_0+(a/z)v_1}{p}\pmod{ag}.
$$



For a free complex over the domain P and a nonzero F, the compact edge map
H_1(C)/F H_1(C) -> H_1(C/FC) is injective: if z=partial h+F w and partial z=0,
then F partial w=0, so w is a cycle. Thus [z]=F[w], with the converse immediate.
This is one principal period relation, not an assertion for arbitrary ideals.

For odd L with 3|L and 7 not dividing L,



$$
\gcd(z^L+1,g^2p)=g.
$$



The coordinate's nonzero residue modulo g therefore detects compact survival
independently of L within that arithmetic class. The analogous base module is
P/(a), with the same selected residue g.

The draft's alternative explicit cover word was



$$
U=(z+z^4+z^6+z^8+z^{10}+z^{11})
+t(1+z^3+z^7+z^8+z^9),\qquad V=tp.
$$



Its homology coordinate is 1+a/z=(1+z^5)/z, equal to one modulo g; its weight is
fourteen. A hypothetical finite cover logical of weight <=12 at L>156 contains
a nonboundary circuit that unwraps to an infinite-strip cycle of the same
weight. That compact coordinate survives at L=39 as well. Reduction at 39
cannot increase weight, contradicting the exact finite seed exclusion. The base
argument uses weight <=4. This proves the same uniform family for j>=1, with
j=0 certified directly. The recovered early finite search and the later intact
round 03 verifier both address those finite seed exclusions.

## Appendix B. Additional finite records stated in the tool-visible draft

The draft also recorded a 19-period changed-polynomial template search, with
base A=1+z+z^5, B=1+z^11+z^13 and cover lifts
A'=1+z+z^(L+5), B'=1+z^(L+11)+z^13:

| L | k | d | k_2 | d_2 |
|---|---:|---:|---:|---:|
|15|4|6|4|6|
|21|10|4|10|6|
|27,33|4|6|4|12|
|39,45,51,57,69,75,81,87,93,99,111,117,123|4|6|4|14|
|63,105|10|6|10|12|

Three additional unchanged-polynomial representatives were reported with
k=k_2=4 and distances 6->14:

| L | A exponents | B exponents |
|---:|---|---|
|39|0,11,37|0,17,31|
|39|0,5,31|0,4,23|
|75|0,7,65|0,4,41|

The draft described these as exactly re-certified after heuristic selection,
without an inequivalence claim. Their original JSON/witness logs are unavailable;
this appendix is a source-text record, not new export-time certification of the
table. The original partial random run completed batches at L=39,57,75,93 and did
not justify claiming its later intended batch complete. The recovered discovery
scripts must not be confused with preserved outputs of a fully completed run.
