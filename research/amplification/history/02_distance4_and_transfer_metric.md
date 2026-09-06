# Distance-four obstruction and the failed transfer-metric principle

**Source status:** archival transcription of the mathematical material in the
second round's visible final response and its visible report-writing command.
The original `BB_fixed_distance_report.md` and `BB_fixed_distance_round2.zip`
are unavailable as files. Three final verifier sources have been transcribed
from the visible tool-call text into [recovered_round2](recovered_round2/README.md).
Their export-time execution records, when present, are new rerun records, not
recovered original logs. No new mathematical exploration was performed here.

Original status: `FIXED_DISTANCE_OBSTRUCTION_PROVED`.

## 1. The retained conclusions and limitations

The round reported the uniform computer-assisted implication

\[
d=4\Longrightarrow d_2\le48
\]

for strict-trinomial binary BB double covers, including both period parities,
bivariate covers, changed-polynomial term-matched lifts, and disconnected codes.
The constant was not claimed optimal.

A separate symbolic result was

\[
\text{a one-block logical of weight at most }w\Longrightarrow d_2\le2w^2.
\]

It was later reproved in the intact distance-six report. The particularly useful
negative result was a connected family with d=d_2=4 and k=k_2=4 but

\[
\mu(Q,\ker\widehat\tau_1)=L/3+1\longrightarrow\infty.
\]

Thus neither a universal mu<=C d inequality nor a constant-k short-homological-
basis principle can prove the desired actual-distance bound.

## 2. Finite integer presentations for four-column circuits

A weight-four minimum nonboundary has circuit support: a proper cycle would
have even weight two, would be a boundary by d=4, and its complement would then
be a weight-two nonboundary.

Up to block exchange the supports are (4,0), (3,1), (2,2). Pair check incidences
at each even-degree check. A same-column pair is impossible because each
trinomial has distinct terms. A disconnected pairing component would be a
proper cycle. Thus the paired support is a connected loopless cubic multigraph
on four vertices: K_4 or one of six labeled configurations consisting of two
opposite double edges and two cross edges.

Normalize A={0,a_1,a_2}, B={0,b_1,b_2}, and the first column position p_0=0. A
paired edge between incidences (i,c) and (j,e) imposes

\[
p_i+q_{t_i,c}-p_j-q_{t_j,e}=0.
\]

The six relations define an abelian group U in five generators for (4,0), or
seven for mixed support. Every actual circuit is an image of U. Extra finite
collisions impose additional quotient relations; they are not omitted cases.

Global term relabeling fixes the first incidence permutation in each occupied
block. This gives 7*6^3=1512 normalized checks for (4,0), and 7*6^2=252 for each
mixed type. Forced term collisions and equal columns are rejected.

| Support | Tested | Finite one-block | Virtually cyclic | Square | Involution offset | Unit |
|---|---:|---:|---:|---:|---:|---:|
|(4,0)|1512|32|0|0|0|0|
|(3,1)|252|0|55|1|0|0|
|(2,2)|252|0|72|0|4|2|

These are labeled presentations, not code isomorphism classes. Their meanings:

Finite one-block presentations have order 6 or 7. Virtually cyclic presentations
are Z plus torsion T and have primitive free check range rho with

\[
(|T|,\rho)\in\{(1,4),(1,5),(3,1),(3,2),(4,1),(5,1),(6,1)\}.
\]

In particular |T|rho<=6. The square cases satisfy B=A^2 after gauges and possible
block exchange. The involution cases satisfy

\[
A=1+x+y,\qquad B=1+x+hy,\qquad h^2=1.
\]

A unit case contains two terms with ratio an involution; it has k=0.

The independent direct pairing enumeration generates 3348 pairings for each
support type, without the seven-graph list or normalization. Its retained
counts were:

| Support | Finite | Virtually cyclic | Square | Involution | Unit |
|---|---:|---:|---:|---:|---:|
|(4,0)|84|0|0|0|0|
|(3,1)|0|684|36|0|0|
|(2,2)|0|972|0|36|18|

The differing counts reflect distinct enumeration redundancies. The two
transcribed programs independently check the same structural bound.

## 3. Uniform bounds for the finite and cyclic-strip cases

If one normalized polynomial A is supported in a finite subgroup H of size s,
then a positive-k BB code has d<=s. Indeed, ann(A) is spanned by vectors on single
H cosets. The quotient ann(A)/B ann(A) is nonzero: the cokernel and kernel of B
acting on ann(A) have equal dimensions, and the latter is ann(A) intersect
ann(B), dual to R/(A,B) under the coefficient-of-identity pairing. Some local
spanning vector must therefore be a one-block logical.

The cover preimage of H has size 2s, giving d_2<=2s. The finite cases above give
at most fourteen.

A cyclic strip with h group elements per site and check range rho satisfies

\[
d\le4h\rho.
\]

If there are fewer than 2rho sites, total length gives the bound. Otherwise
partition the circle into an even number of blocks, each of length between rho
and 2rho. Were d>4h rho, each block would be correctable. No check meets two
different blocks of the same parity, so a centralizer word on their union
restricts to centralizer words on individual blocks, all stabilizers. Both
complementary unions would be correctable, contradicting positive k by cleaning.

The underlying cleaning statement follows directly from symplectic orthogonality.
If V_E is the Pauli coordinate space on a correctable region and S the stabilizer
space, S^perp intersect V_E = S intersect V_E. The orthogonal complement of the
projection of S into V_E is S^perp intersect V_E. Therefore the restriction of a
logical to E belongs to that projection and can be removed by a stabilizer.

For U=Z plus T, its finite quotient has cyclic quotient by the image of T. The
cover preimage has at most 2|T| elements per site; twists at the cyclic boundary
only permute within-site coordinates. Hence

\[
d_2\le8|T|\rho\le48.
\]

## 4. Uniform algebraic exceptions

Let t be the deck involution, epsilon=1+t. The exact group-algebra identities are
epsilon^2=0 and ann(epsilon)=epsilon R'.

### Unit trinomials

A trinomial with two terms differing by an involution can be gauged to
1+u(1+h). Its square is one. It makes (A,B) the unit ideal and k=0.

### Square case

For B=A^2, matched lifts obey B'=A'^2+epsilon D, with D a subset of the three
terms of A'^2. A deck gauge complements that subset, so D is zero or a monomial.

If D=0, (A',1) is a weight-four nonboundary: a boundary preimage would require
A'f=1. If D is a monomial, (epsilon A',epsilon) is a cycle of weight at most
eight. A boundary preimage f would imply epsilon Df=0, hence f=epsilon r. The
remaining equation would project to A p(r)=1 downstairs, impossible at positive
base k. Thus d_2<=8.

### Involution-offset case

Assume h is nonidentity downstairs; its collapse would make A=B and force d<=2.
After gauges,

\[
A'=1+X+Y,\qquad B'=1+t^aX+HY,
\]

where a is zero or one and H^2 is 1 or t.

For a=0 put N=1+H and q=ord(H) in {2,4}. Then

\[
S=N^{q-1}=1+H+\cdots+H^{q-1},\qquad
\operatorname{ann}(N)=SR',\quad\operatorname{ann}(S)=NR'.
\]

The cycle (S,S) has weight 2q<=8. A boundary preimage forces f=Sr and then
S(A'r+1)=0, so 1 belongs to (A',N)=(A',B'), contradiction.

The same argument covers a=1, H^2=t, because B'+A'=N(Y+NX) and Y+NX is a unit.

If a=1 and H^2=1, N=1+H and epsilon=1+t are independent square-zero directions.
Set Delta=B'+A'=epsilon X+NY. Then Delta^2=0 and

\[
\operatorname{ann}(\Delta)=\Delta R'.
\]

To verify this last identity, divide by Y and write D=N+epsilon U. If Df=0,
reduction modulo epsilon gives p(f)=Np(g), so f=Ng+epsilon r. Substitution yields
N(p(r)+p(Ug))=0, hence p(r)+p(Ug)=Np(s). It follows that

\[
f=(N+\epsilon U)(g+\epsilon s).
\]

The reverse inclusion follows from D^2=0. The cycle (Delta,Delta) has weight at
most eight. A boundary preimage f=Delta r would force
Delta(A'r+1)=0, hence 1 in (A',Delta)=(A',B'), contradiction.

These cases prove the distance-four bound. For disconnected codes, gauges make
components isomorphic cosets of the check-difference subgroup; cover components
have degree one or two over a base component, so the same bound applies.

## 5. Why all one-block fixed weights have a uniform obstruction

Choose a nonboundary one-block circuit of weight w'<=w. Its paired-incidence
graph is connected. A spanning tree expresses column positions in the two
trinomial differences a,b; non-tree edges impose relations in Z^2. Let U be the
resulting group.

The circuit gives a nonzero annihilator of 1+a+b in F_2[U]. Write U=T plus Z^r.
If its three free exponents are not all equal, a real linear functional makes
one term uniquely maximal. Its coefficient in F_2[T] is a monomial unit, so the
trinomial cannot be a zero divisor. Therefore all free exponents are equal and,
since a,b generate U, r=0.

A fundamental relation has length at most w' and lies in w' times the hexagon
with vertices (1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1). Any two vectors in that
hexagon have determinant of absolute value at most one. Two independent
fundamental relations therefore have determinant at most (w')^2; the full
relation-lattice index divides it. Thus |U|<=w^2. The finite-support lemma gives

\[
d_2\le2w^2.
\]

This proof and its later use are also preserved in the intact distance-six
report, so the one-block lemma does not depend solely on this transcription.

## 6. Exact failure of the transfer-sector metric principle

Let L=3q with q>=3 odd, and

\[
A=1+x+x^2,\qquad B=1+x^2+x^4=A^2.
\]

The unchanged-polynomial covers are connected and have

\[
Q_L=[[2L,4,4]],\qquad\widetilde Q_L=[[4L,4,4]].
\]

Because x^L+1 is square-free and A divides it, the common gcd at both periods is
A, so k=k_2=4. The weight-four cycle (A,1) cannot be a boundary, since that would
make A a unit.

No weight-two cycle exists. At L, nonzero vectors in ann(A) have weight 2L/3;
ann(B) has the same minimum because x->x^2 is a group automorphism. A mixed pair
would require {0,1,2} and {0,2,4} to be translates modulo L>=9, which they are
not. At 2L, ann(A) has minimum 4L/3, while the B check splits into two length-L
A checks. A mixed pair is excluded by the parity of the supports. All cycles
are even-weight, proving both distances are four.

In the univariate normal form, the first homology coordinate is

\[
w=u+Av\in\operatorname{ann}(A).
\]

Since g_2=g=A, transfer kills exactly the other sector. The three nonzero choices
of w are translates of

\[
h=(x^L+1)/A=(1+x)\sum_{j=0}^{q-1}x^{3j}.
\]

Thus

\[
\mu=\min_v\bigl(|v|+|h+Av|\bigr).
\]

An exact four-state cyclic trellis tracks integer state
s=v_{i-1}+2v_{i-2}. The target h repeats 110, and the three-bit block matrix is

\[
M=\begin{pmatrix}
2&2&3&3\\0&2&3&3\\1&3&2&2\\1&3&2&4
\end{pmatrix}.
\]

With potential a=(0,1,0,0), reduced costs M_ij-1+a_i-a_j are nonnegative. The
only zero-cost edges are 0->1, 1->0, 2->0, 3->0. Every zero-cost closed walk is
even. An odd length-q closed walk therefore has cost at least q+1. Alternating
0<->1 for q-1 edges and closing with 0->0 attains that value. Therefore

\[
\boxed{\mu=q+1=L/3+1.}
\]

An attaining cycle is

\[
u=x^{L-3}(1+x),\qquad
v=(1+x^2)\sum_{j=0}^{(q-3)/2}x^{6j}.
\]

The classes (A,1) and its translate span the transfer kernel. One outside-kernel
class and its translate span the quotient, giving

\[
\lambda_1=\lambda_2=4,\qquad\lambda_3=\lambda_4=L/3+1.
\]

| L | Base | Cover | Exact mu |
|---:|---|---|---:|
|9|[[18,4,4]]|[[36,4,4]]|4|
|15|[[30,4,4]]|[[60,4,4]]|6|
|21|[[42,4,4]]|[[84,4,4]]|8|
|39|[[78,4,4]]|[[156,4,4]]|14|
|99|[[198,4,4]]|[[396,4,4]]|34|

The cover still has its own short (A,1) logical outside the transfer image.
This is an exact counterexample to a proposed metric lemma, not amplification.

## 7. Discovery records and subsequent trajectory

The original round sampled 30,000 six-column incidence pairings for each of
(6,0),(5,1),(4,2),(3,3), with seed 20260906. It reported 21 higher-free-rank
formal circuit presentations: 2, 4, and 15 in the mixed types. This was not an
exhaustive classification or a finite nonboundary certificate. The raw sampled
JSON is not mounted in the current session; no substitute dataset was invented.
The later intact distance-six bundle supersedes that discovery stage with full
presentation enumerations and explicit algebraic certificates.

Auxiliary cyclic trellises for the previous fixed-strip 7/3 family recorded
mu=12,52,90,130 at L=39,165,291,417. They concerned the transfer metric, not new
quantum distances. Their original input/witness JSON and logs are not mounted.
The simpler exact family above is the retained structural refutation.

The original next target was mixed weight-six presentations of free rank at
least two, excluding units and universal boundaries. Rounds 04–06 subsequently
resolve that fixed-weight case, establish an all-weight compact-survival theorem
in the stated higher-rank regime, and prove its exact compact factor-two bound.
This history is retained to explain the route, not as a statement that those
old subproblems remain open.
