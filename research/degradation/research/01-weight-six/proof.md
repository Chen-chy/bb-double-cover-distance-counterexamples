# Strict-trinomial BB double-cover degradation: weight-six exclusion and filling counterexamples

**Principal status: D2_EQ_6_UNBOUNDED_BASE_EXCLUDED.**

This note proves a computer-assisted, parameter-uniform exclusion:

\[
 d>56\quad\Longrightarrow\quad d_2\ge 8.
\]

It also disproves the proposed two-check coefficient-filling lemma, and constructs strict-trinomial boundaries of weight six whose minimum coefficient filling and minimum lifted-boundary weight both diverge.

It does **not** prove a vanishing degradation ratio or a universal positive ratio. The two directions of the distance-ratio problem are not interchanged here.

## 1. Scope, inputs, and conventions

The BB framework and termwise covering convention are those of Symons, Rajput, and Browne, *Sequences of Bivariate Bicycle Codes from Covering Graphs*, arXiv:2511.13560v3, particularly Section 2.4 and Theorem 3.1. The prior-results paragraph of the supplied research brief is used as the starting point, specifically:

* every strict-trinomial binary cycle has even weight;
* a positive-dimensional strict-trinomial BB code of distance greater than four has no nonzero cycle of weight at most four;
* for a valid double cover, base distance greater than four implies cover distance at least six.

The supplied exact 14-to-12 family is retained as an established input, not independently recertified by this computation.

For a finite abelian group G, put R=F_2[G]. In the monomial basis use

\[
 \partial_1(u,v)=Au+Bv,\qquad \partial_2s=(Bs,As).
\]

The physical weight is the sum of the two block weights. Inversion of group elements, followed by block exchange, identifies X and Z homology weight-preservingly. Thus it suffices to treat the displayed complex. If M=|G|, then

\[
 k=2\dim R/(A,B).
\]

A valid double cover gives a surjective group homomorphism with kernel {1,z}, z^2=1. Its ring projection p has kernel (1+z)R_tilde, a square-zero ideal. Full-fibre transfer is multiplication by 1+z after choosing a lift. In particular, units lift through p, also after restricting to an idempotent summand.

Multiplying A or B by a monomial gives a weight-preserving code equivalence. We normalize one term in each polynomial to 1, and write their remaining translation differences as a_1,a_2,b_1,b_2.

## 2. Main exclusion theorem and numerical consequence

**Theorem 1.** Under the starting weight-four exclusions, every valid binary strict-trinomial BB double cover with k>0 satisfies

\[
 d_2=6\quad\Longrightarrow\quad d\le56.
\]

Consequently d>56 implies d_2>=8. This is a finite-presentation theorem, not an extrapolation from bounded code lengths.

The universal BB bound d<=n/2 is proved in Section 4.1 below. For d<=4 the ratio is at least 1/2. For 4<d<=56, the starting exclusion gives ratio at least 6/56=3/28. For d>56, Theorem 1 gives ratio at least 8/d>=16/n. Therefore

\[
 \gamma_-^{(3)}(N)\ge \min\{3/28,16/N\}.
\]

In particular, for integer N>=150,

\[
 \boxed{\gamma_-^{(3)}(N)\ge16/N.}
\]

Together with the supplied 14-to-12 family, this gives 16/N<=gamma<=6/7 for N>=636. The cutoff 56 and the constants here are not asserted to be sharp.

## 3. Complete weight-six incidence enumeration

### 3.1 Why the search is finite and exhaustive

A weight-six cycle contains 18 incidences, three per selected qubit. At every syndrome location the number of incidences is even. Pair them at that location, arbitrarily when the multiplicity is four or six. The pairs form a cubic multigraph on the six selected qubits.

There are no loops: the three supported monomials in each check polynomial are distinct. Every connected component has even order because its total degree is even. A disconnected pairing graph would therefore give a nonzero cycle on two or four of the selected qubits. When d_2=6 this is excluded by the starting no-small-cycle result. Thus the pairing graph is connected. A triple edge would isolate two vertices, so edge multiplicities are at most two.

Exhaustively generating degree-three loopless multigraphs on six labelled vertices gives 640 connected graphs, falling into six isomorphism types. `graphs.py` generates these, tests connectedness, and canonicalizes against all 720 vertex permutations. No list of graph types is assumed.

For an edge pairing port i of vertex r with port j of vertex s, impose

\[
 t_r+c_{r,i}=t_s+c_{s,j},
\]

where c is either 0,a_1,a_2 or 0,b_1,b_2 according to the block. A spanning tree eliminates five relative qubit positions. The other four edges give four integral relations among a_1,a_2,b_1,b_2. Hence every mixed-block case is represented by

\[
 H=\mathbb Z^4/\langle\text{four relation rows}\rangle.
\]

Every actual finite code realizing that incidence pairing is a quotient of H, on its normalized translation subgroup. Additional accidental syndrome coincidences simply give further quotients; they are not omitted.

Each graph is assigned all block colourings for splits (5,1), (4,2), and (3,3). Port labels are independently permuted at each vertex. One vertex in each block fixes the global permutation of that block's three term names. Thus there are 6^4=1296 port assignments per mixed colouring. The total mixed enumeration has

\[
 6\,(\binom61+\binom62+\binom63)\,1296=318816
\]

assignments. In the pure case one global term permutation is fixed, giving 6*6^5=46656 assignments.

Cases with formally repeated check terms or repeated qubits within a block are impossible in any admissible quotient and are discarded. A check with a term difference of two-power order is a unit and is also discarded: after dividing by its third monomial it is 1+u(1+t), with the second summand nilpotent. No other unit or zero-dimension assumption is silently used.

The mixed output is deduplicated by its exact row lattice and a translation-normalized cycle. It contains 5392 retained presentation-cycle pairs, over 3334 distinct relation lattices. These are not advertised as fully isomorphism-reduced classes.

### 3.2 Exact output

For pure (6,0) cycles, fourteen valid port assignments remain. Their universal translation groups are exactly

\[
 C_9,\qquad C_3\times C_3,\qquad C_2\times C_6.
\]

For mixed cases the classification is:

| Category | Retained pairs |
|---|---:|
| One-check boundaries | 121 |
| Two-check boundaries | 74 |
| Free rank zero | 3441 |
| Free rank one | 1668 |
| Monomial-associated checks, free rank two | 40 |
| One check a monomial multiple of the other's square | 6 |
| Squares of the two checks monomial-associated | 20 |
| An order-three check | 16 |
| Order-three projector cycles | 6 |
| Unresolved | 0 |

All free-rank-three or free-rank-four cases are one-check boundaries. The nonboundary-labelled free-rank-two cases are exhausted by the last five algebraic categories. The label “nonboundary-labelled” here means only “not an exhibited one- or two-check boundary”; actual finite nontriviality is handled by the arguments below, not inferred from that label.

For the finite and strip categories the exact maxima are:

| Split | Maximum rank-zero group order | Maximum strip bound 4|T|R |
|---|---:|---:|
| (5,1) | 12 | 40 |
| (4,2) | 22 | 56 |
| (3,3) | 27 | 48 |

Here T is the finite torsion subgroup of H and R is the larger of the two check spans in the primitive free coordinate. Free-rank-one cases include odd-torsion orders three, five, seven, and nine, and mixed even torsion; none is left to numerical stabilization. Pure cases explicitly include the order-six degeneracy above. Full Smith data and exponent presentations are in the output files.

### 3.3 Independent verification of the retained output

`classify_six.cpp` performs the complete port enumeration with integer row operations. `verify_presentations.py` independently checks every retained pair using SymPy Smith decompositions, verifies their unimodular transformations, checks zero syndrome in the presented group, verifies every claimed small boundary, computes primitive free coordinates, and checks all rank-at-least-two algebraic alternatives.

The verified catalogue SHA-256 is

`5d628c388525ffa3c78be0583cccdde43249e5d704fd425e72dc054d8692139f`.

The pure enumeration and its fourteen certificates are in `pure_six.py` and `pure_six_results.json`. Completeness is supplied by the pairing argument and exhaustive graph/port loops above; checking retained certificates alone is not substituted for completeness.

## 4. Why every category gives a uniform bound

### 4.1 A check supported on a finite subgroup

Suppose, after a monomial normalization, A is supported on a subgroup K of G. The group algebra R is free over F_2[K], and multiplication by A acts independently on its cosets. Thus ker A has an R-module generating set whose members have weight at most |K|.

If k>0, then ker A intersect ker B is nonzero. One way to see this is to transpose the non-surjective map [A B] and then use group inversion to replace transposes by the original convolution operators. Consequently B restricted to ker A is singular and is not surjective. At least one member u of the above generating set does not belong to B(ker A). Then (u,0) is a nonboundary cycle. Therefore

\[
 d\le |K|.
\]

Taking K=G proves d<=n/2. Taking the pure-cycle universal subgroup proves d<=12 for the pure case, including all its finite quotients. An order-three check gives d<=3, hence d<=2 by evenness.

For a finite mixed universal group H, the normalized code is a direct sum of identical components over its image in G. Each component has at most 2|H| qubits. Positive dimension implies positive dimension in a component, giving d<=|H|. The maximum needed is 27.

### 4.2 Rank-one presentations: a one-dimensional bound

Write H=T direct-sum Z. Its finite image is a cyclic strip with at most |T| group elements per cell; the end identification may include a torsion twist. Let

\[
 R=\max\{\operatorname{span}(0,a_1,a_2),
              \operatorname{span}(0,b_1,b_2)\}
\]

in the primitive free coordinate. After block monomial shifts, both X and Z stabilizer supports have cell span at most R. There are at most 2|T| qubits per cell.

If the strip circumference P<2R, the previous d<=n/2 bound suffices. Otherwise partition the circle into an even number of consecutive intervals, each of length between R and 2R, and colour them alternately. Such a partition exists by distributing the remainder after 2R*floor(P/(2R)) cells.

If d>4|T|R, each interval is correctable. A check cannot intersect two same-colour intervals, because they are separated by at least R cells. A union of such correctable intervals is correctable: a Pauli supported on the union and commuting with every generator has commuting restrictions on each interval, and each restriction is a stabilizer. Both complementary colour classes would then be correctable. Cleaning any nontrivial logical off one class would put it entirely in the other, a contradiction.

Hence

\[
 d\le4|T|R.
\]

The exact maximum over the retained rank-one presentations is 56. This proof applies to every finite quotient, including twisted end identifications and nontrivial bivariate embeddings.

### 4.3 Associated checks and Frobenius multiples

If A=mB, the cycle (1,m) is nontrivial whenever k>0, so d<=2. If B=mA^2, the cycle (mA,1) has weight four and is nontrivial: a boundary with second entry 1 would make A a unit. Block exchange handles the other orientation. These identities persist under projection to the base.

### 4.4 Equal squares

**Lemma.** If strict-trinomial checks have monomial-associated squares, then a positive-dimensional code has d<=6.

Their squared supports cannot contain repeated terms, since that would give a two-power term difference and a unit check. Normalize matched terms and permute the others. It is enough to consider

\[
 B=1+x+y,\qquad A=1+tx+sy,\qquad t^2=s^2=1.
\]

If t=s=1 there is a weight-two logical. Otherwise put e=1+t, f=1+s and

\[
 C=A+B=ex+fy.
\]

The weight-six vector (A,B) is a cycle. Under the invertible coordinate change (u,v) to (u+v,u), the complex has maps (B,C) and (C,B), and this cycle differs from the elementary boundary (C,B) by (0,C).

If t,s generate C_2 x C_2, R is free over F_2[e,f]/(e^2,f^2). We claim Ann(C)=CR. To prove it, let Cr=0. Modulo f, freeness implies r=ea+fb. Then

\[
 0=ef(ya+xb).
\]

Since Ann(ef)=(e,f)R, write ya+xb=ec+fd. As x is a unit,

\[
 r=C\bigl(x^{-1}a+fx^{-2}c\bigr).
\]

The reverse inclusion follows from C^2=0.

If the subgroup generated by t,s has order two, the same annihilator identity holds after localization at any common maximal ideal of B and C. Indeed C is e times x, y, or x+y; the first two are units, and x+y=1+B is a unit at such a maximal ideal.

If (0,C) were a boundary, then Cr=0 and Br=C for some r. Locally Ann(C)=CR gives r=Ca, and then C(Ba+1)=0 implies Ba+1 in CR. This puts 1 in (B,C), contradicting the chosen common maximal ideal. Such an ideal exists when k>0. Therefore (A,B) is a nonboundary cycle of weight six.

This is an algebraic assertion about actual finite group algebras, not just a formal universal cycle. Since square association projects, it gives the same d<=6 bound downstairs.

### 4.5 Order-three projector cycles

The remaining six free-rank-two presentations have cycles

\[
 w=(uJ,vJ),\qquad J=1+t+t^2,\quad t^3=1,
\]

where u,v are monomials. J is an idempotent. In the summand R_J, the cycle identity says Au=Bv, so the two checks are monomial-associated. In that summand w is a boundary exactly when B is a unit: solving its first boundary equation requires an inverse to B, and that inverse also solves the second equation.

An order-three subgroup projects injectively through a double cover. Moreover the projection between the J summands has square-zero kernel. Thus B is a unit upstairs if and only if it is a unit downstairs. A nonboundary w upstairs therefore projects to a nonboundary cycle of weight six downstairs.

This case does **not** say that every projector cycle is nontrivial whenever the entire code has k>0. The J summand can be acyclic while other summands encode. That distinction is the source of the filling counterfamily below.

### 4.6 Conclusion of Theorem 1

A weight-six logical cannot be a universally exhibited one- or two-check boundary. The pure, finite, strip, and higher-rank alternatives above give base bounds at most 12, 27, 56, and 6 respectively. This proves Theorem 1.

## 5. An explicit counterfamily to the two-check lemma

Let j>=1, L=4^j, and r=2j, so L=2^r and L=1 mod 3. Work in

\[
 R_L=\mathbb F_2[x,y]/(x^{3L}+1,y^{3L}+1),\qquad t=x^L.
\]

Define strict trinomials

\[
 A=1+tx+t^2y,
 \qquad B=1+x+y,
 \qquad J=1+t+t^2.
\]

The three terms in each polynomial are distinct. B contains the unit x and y translations, so the code is connected. Its parameters satisfy

\[
 Q_L=[[18L^2,4,d_L]],\qquad L\le d_L\le4L.
\]

The boundary

\[
 q=(J,J)
\]

has physical weight six.

Define

\[
 f_0=J\sum_{i=0}^{L-1}(1+x)^i y^{-(i+1)}.
\]

Because (1+x)^L J=(1+t)J=0 and AJ=BJ=(1+x+y)J,

\[
 Af_0=Bf_0=J.
\]

Hence q=partial_2 f_0.

### 5.1 Dimension and entire base-distance bounds

The coefficient algebra F_2[C_3] splits into its J summand, where t=1, and its complementary E=1+J=t+t^2 summand, isomorphic to F_4.

In the finite J summand, D=1+x+y is a unit. Indeed D^L J=y^L J. This summand has zero homology.

In the E summand put t=omega, with omega^2+omega+1=0. The two linear forms are

\[
 1+\omega x+\omega^2y,\qquad1+x+y.
\]

Their common equations give x=omega,y=omega^2. They are compatible with the periods because L=1 mod 3. The quotient ring is F_4, of F_2 dimension two, so k=4.

For the distance lower bound, first use the infinite group C_3 x Z^2, with t the order-three variable and x,y the two free variables. The finite quotient adds relations x^L=t and y^{3L}=1.

In the infinite J summand the checks both equal the nonzero Laurent polynomial D. Every cycle is diagonal, and its homology is represented by (Jg,Jg). In the infinite E summand, the two distinct linear forms above are relatively prime Laurent polynomials, so their Koszul first homology is zero. Thus every finite-support infinite cycle is a boundary plus a diagonal J-sector cycle. Every such cycle maps to a boundary in the finite code, since the finite J summand is acyclic.

Now take any finite-code cycle of weight less than L and pair its syndrome incidences. An edge between selected qubits changes each free coordinate by at most one: both check supports have free-coordinate projections {0,(1,0),(0,1)}. Every simple graph cycle has fewer than L edges. Its free winding therefore cannot contain a nonzero period (L,0) or (0,3L). The torsion subgroup injects into the finite quotient. Hence each pairing component lifts consistently to a finite-support cycle over C_3 x Z^2. By the preceding paragraph it is a finite-code boundary. This proves that **every** cycle of weight less than L is a boundary, not merely that one distinguished class is long. By X/Z symmetry, d_L>=L.

For the upper bound set z=x/t, which has order L, and

\[
 h=\sum_{i=0}^{L-1}z^i,
 \qquad w=((t+t^2)h,(1+t)h).
\]

The two entries each have weight 2L. The identity

\[
 E(A+t^2B)=E(x+t)
\]

shows that w is a cycle.

For nontriviality map R_L into F_4[epsilon]/(epsilon^L) by

\[
 x\mapsto\omega(1+\epsilon),\qquad y\mapsto\omega^2.
\]

Then t maps to omega, A maps to omega^2 epsilon, B maps to omega epsilon, and h maps to epsilon^{L-1}. The functional (u,v) to v+omega u annihilates every mapped boundary but sends w to epsilon^{L-1}, which is nonzero. Thus d_L<=4L.

### 5.2 Exact coefficient-filling minimum

For 0<=i<L, the polynomial (1+x)^i has 2^{popcount(i)} terms. Different i give distinct y coordinates in f_0, and multiplication by J gives three disjoint x-shifts. Therefore

\[
 |f_0|=3\sum_{i=0}^{2^r-1}2^{\operatorname{popcount}(i)}=3^{r+1}.
\]

There are exactly four coefficient fillings of q, because ker(partial_2) has dimension two. Its three nonzero words have coefficients

\[
 k_c(i,j)=\operatorname{Tr}_{\mathbb F_4/\mathbb F_2}
     (c\omega^{-i-2j}),\qquad c\in\mathbb F_4^*.
\]

These are common kernel words by direct multiplication, and they span the two-dimensional kernel. Each has weight 6L^2 and has exactly two ones on every three-element t orbit. The support of f_0 is a union of exactly 3^r complete t orbits. Therefore

\[
 |f_0+k_c|=6L^2-3^r.
\]

Since 3^{r+1}<6L^2-3^r, the exact minimum coefficient weight is

\[
 \boxed{\mu(q)=3^{r+1}=3\cdot9^j
      =3L^{\log_2 3}.}
\]

For j>=2, d_L>=16>6, while mu(q)>=243. This uniformly disproves the two-check filling lemma, including any replacement by a size-independent coefficient bound for weight-six boundaries.

## 6. Unbounded lifted filling weight, still without degradation

Use the valid double cover

\[
 (3L,3L)\longrightarrow(3L,6L).
\]

Let z_c=y^{3L} and kappa=1+z_c. Define

\[
 \widetilde A=z_c+tx+t^2y,
 \qquad\widetilde B=1+x+y.
\]

The three supported terms upstairs are distinct and project bijectively onto the three respective terms downstairs. Only the constant term of A changes its sheet. This explicitly checks termwise validity rather than only polynomial reduction.

Both codes have k=4. For the cover dimension, impose B=0, so y=1+x. Then z_c=(1+x)^{3L}=(1+t)^3=t+t^2=E. The equation A_tilde=0 becomes t+Ex=0. The J summand is eliminated, and in the E summand x=t,y=t^2, again giving quotient F_4.

Let f_tilde be the same finite expression defining f_0, evaluated in the cover ring. On the J summand D is still a unit and D f_tilde=J. Consequently

\[
 \widetilde\partial_2 f_{\rm tilde}
   =(J,J+\kappa f_{\rm tilde}).
\]

Its projection is q. The support of f_0 is disjoint from that of J, so this boundary has weight

\[
 6+2\mu(q)=6+6\cdot9^j.
\]

For the lower bound take **any cover cycle** Y with pY=q, whether a boundary or not, and multiply it by J. Write JY=(u,v). On this summand the cycle equation is

\[
 (D+\kappa)u+Dv=0.
\]

Because p(u)=J and D is invertible,

\[
 v=u+\tau(f_0).
\]

On every fibre in the support of f_0, the two-block weight is at least two. On each of the three fibres in the support of J it is at least two as well; the two supports are disjoint. Thus

\[
 |JY|\ge6+2\mu(q).
\]

Multiplication by J is a sum of three translations, so |JY|<=3|Y|. It follows that

\[
 \boxed{
 2+2\cdot9^j\ \le\operatorname{Fill}(q)
 \ \le\ 6+6\cdot9^j.
 }
\]

In fact the lower bound holds for every cycle projecting to q. Thus this gives unbounded strict-trinomial lifted filling distortion, but **not** a short nonboundary alternative lift. It is not a vanishing-ratio construction.

The three relevant quantities are therefore separately controlled:

\[
 |q|=6,\qquad
 \mu(q)=3\cdot9^j,\qquad
 \operatorname{Fill}(q)=\Theta(9^j).
\]

## 7. Finite exact checks, separate from uniform proofs

`verify_family.py` independently constructs binary convolution columns, computes both check ranks by exact GF(2) elimination, tests boundary membership and the explicit nonboundary witness, checks all four possible coefficient fillings, and verifies the lifted boundary and termwise cover matching.

The executed cases are:

| L | Base n,k | Proved distance interval | Exact mu(q) | Cover n,k | Proved Fill interval |
|---|---|---|---:|---|---|
| 4 | 288,4 | [4,16] | 27 | 576,4 | [20,60] |
| 16 | 4608,4 | [16,64] | 243 | 9216,4 | [164,492] |

These intervals are not claimed to be exact distances. Their lower endpoints come from the uniform small-cycle lifting proof, and their upper endpoints from explicit nonboundary witnesses. No decoder output or absence-of-found-errors is used.

For L=16 the two base check ranks are both 2302, the two cover ranks are both 4606, and the four coefficient-filling weights are 243,1455,1455,1455.

## 8. What remains unresolved

No family with d tending to infinity and d_2/d tending to zero is established here. No universal positive constant is proved. The supplied exact ratio 6/7 remains the retained finite ratio record; this computation does not certify a new ratio record.

The smallest fixed cover distance not excluded in the growing-base-distance regime is now eight. This does not assert that an unbounded-base d_2=8 family exists.

The next precise statement to attack is:

> **Weight-eight bounded-base lemma.** There is a finite constant D_8 such that every valid strict-trinomial binary BB double cover with k>0 and d_2=8 has base distance d<=D_8.
