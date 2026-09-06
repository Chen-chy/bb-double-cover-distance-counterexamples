# Rank-one Laurent cancellation: derivative lifts, cyclotomic resonance, and finite-distance realization

## STATUS: CONSTANT_BOUND_STILL_OPEN

Research round: 6 September 2026.

The factor-three inequality is not proved or refuted for the entire rank-one class. This round proves a factor-two replacement theorem for all one-sided sheet defects, eliminates all but an explicit two-sided resonance family, supplies a constructive exponent-sensitive bound for that family, and proves that its compact metric is exactly realizable as the actual finite quantum distance at sufficiently large periods.

In particular, a genuine counterexample for the **minimum over all compact cover classes and all boundary adjustments** would yield an actual BB distance-amplification counterexample. Winding logicals cannot permanently conceal such a rank-one counterexample. No such counterexample is established here.

The higher-rank compact factor-two theorem and the previous general estimates are treated as supplied input, not re-proved in this round. The present proofs are independent of finite circuit enumeration.

## 1. Scope and principal conclusions

Let P=F_2[z,z^{-1}]. The two strict Laurent trinomials have check differences generating the infinite cyclic group. Equivalently, after normalizing one term in each to exponent zero, the gcd of their four nonconstant exponents is one. This is the intrinsic primitive coordinate of the no-universal-torsion presentation. A nonprimitive coordinate is first replaced by the generator of the check-generated subgroup.

Write

\[
c=\gcd(A,B),\quad A=ca,\quad B=cb,\quad
F_L=z^L+1,\quad g_0=\gcd(c,F_L).
\]

Gcds are normalized up to Laurent monomial units. We assume g_0 is nonconstant. The base compact minimum in the question is

\[
\Delta(g_0)=\min_{g_0\nmid f}\{|bf|+|af|\}.
\]

All weights here are universal Laurent-support weights, before imposing the finite period. A displayed universal cycle supplies a finite upper bound only after its finite nonboundary status is proved.

Every abelian universal double cover of Z splits as Z x C_2, but its finite quotient need not split. Put t^2=1 and epsilon=1+t. Every compatible finite quotient can be written

\[
z^L=t^\kappa,\qquad \kappa\in\{0,1\}.
\]

For kappa=0 the finite group is C_L x C_2; for kappa=1 it is C_{2L}. When L is odd the first group is also cyclic, so it too can be written as a univariate term-matched period-doubling cover.

After majority-sheet gauges and monomial check gauges, either both lifted checks are unchanged, or they have the form

\[
\widehat A=A+\epsilon,\qquad
\widehat B=B+\nu\epsilon,\qquad \nu\in\{0,1\},
\]

with 1 a term in A and, when nu=1, in B. These gauges preserve physical weight and the projection chain map.

The main new results are:

1. **One-sided replacement.** If nu=0, then for every compatible finite quotient,
   \[
   d_2\le2\Delta(g_0).
   \]
   This permits either period parity and either kappa. The proof adaptively uses transfer or a formal-derivative lift detected by projection.

2. **Exhaustive algebraic reduction of the two-sided case.** Outside explicitly handled factor-two cases, both normalized checks must be
   \[
   A=1+z^r+z^{2s},\qquad B=1+z^t+z^{2u},\qquad r,t\text{ odd}.
   \]
   Define
   \[
   R=(t-r)/2,\quad S=u-s,\quad g=\gcd(|R|,|S|).
   \]
   The only factors capable of killing a surviving compact transfer are in
   \[
   E=\gcd(A,1+z^g).
   \]
   A nontrivial obstruction requires a nontrivial odd-order root; in particular, g cannot be a power of two.

3. **Constructive resonant replacement.** For g>0 put p=R/g, q=S/g and
   \[
   m=\max\{|p|,|q|,|p-q|\}.
   \]
   Then
   \[
   d_2\le2m\Delta(g_0).
   \]
   Here transfer is used whenever it survives, and an explicit divided-Euler lift is used otherwise. If m=1 this is another factor-two theorem. The first unresolved slopes have m=2; the supplied 7/3 example is in this first layer. The dependence on m is not a universal constant and is not presented as one.

4. **Exact finite realization.** Fix the Laurent checks, the universal lift, and any compatible finite root data. There is an explicit arithmetic progression of periods along which the root data remain unchanged and, eventually,
   \[
   d=\Delta(g_0),\qquad d_2=\widehat\Delta(H),
   \]
   where the latter is the minimum over all surviving compact cover classes and all universal boundary adjustments. Every class outside the compact image has minimum weight at least L/rho, where rho is the maximum free-coordinate check span.

The remaining rank-one factor-three assertion is therefore equivalent to the explicit scalar-polynomial inequality in Section 8. It is not necessary to leave open an additional hypothesis saying that winding logicals might always rescue a failed compact inequality.

## 2. Exact universal and specialized modules

### 2.1 The normalized gcd is square-free

At least one of the normalized trinomials has an odd nonconstant exponent. Such a trinomial is square-free in P. If exactly one exponent r is odd, its derivative is the monomial z^{r-1}. If both are odd, then z A'=A+1, so A and A' are coprime. This remains valid for negative Laurent exponents.

Consequently c=gcd(A,B) is square-free. This uses the primitive check-generated coordinate; it is not an assertion about arbitrary nonprimitive polynomial representatives.

### 2.2 Universal cover homology is cyclic

For an active normalized lift put

\[
D=B+\nu A,\quad
E=\gcd(c,b+\nu a),\quad
G=cE.
\]

Since gcd(a,b+nu a)=1,

\[
\boxed{G=\gcd(A^2,D),\qquad E\mid c,\qquad G\mid c^2.}
\]

Multiplication by A+epsilon is injective on P[epsilon]/(epsilon^2). Eliminating epsilon gives

\[
P[\epsilon]/(\epsilon^2,A+\epsilon)\cong P/(A^2),
\]

and the other check maps to D. Thus

\[
H_0\cong P/(G),\qquad H_1\cong P/(G),\qquad H_2=0.
\]

The full explicit middle-degree reduction is as follows. Write a cover cycle as

\[
U=u_0+\epsilon u_1,\qquad V=v_0+\epsilon v_1.
\]

Set

\[
r=u_1+\nu v_1,\qquad s=v_0+A v_1.
\]

Then A^2 r+D s=0. Conversely, a reduced cycle lifts as

\[
(r,s)\longmapsto(Ar+\nu s+\epsilon r,s).
\]

The difference between an arbitrary cover cycle and this lift of its reduction is the boundary generated by v_1. Reduced boundaries are (D h,A^2 h). Since P is a PID, its reduced first homology is generated by (D/G,A^2/G), with annihilator G.

A physical, group-basis generator is therefore

\[
\mathbf g=\left(
\frac{AB+D}{G},\ \frac D G,\ \frac{A^2}{G},\ 0
\right),
\]

where the four entries are the two sheets of the first qubit block followed by the two sheets of the second block. A boundary generated by an ordinary Laurent scalar h has physical vector

\[
\mathbf b h=(B+\nu,\ \nu,\ A+1,\ 1)h.
\]

Every universal cycle has the form

\[
\boxed{\mathbf g f+\mathbf b h,\qquad f,h\in P.}
\]

Allowing all f already accounts for boundaries with epsilon coefficients: g G is the boundary generated by (A+epsilon), and a general boundary with preimage h_0+epsilon h_1 is obtained from f=G h_1 and h=h_0+A h_1.

Multiplication by epsilon acts as multiplication by A on both universal H_0 and universal H_1. On H_1 this follows either from the explicit reduction or by computing the action on g modulo boundaries.

### 2.3 One relation gives the exact compact image, with the Tor sector retained

Let

\[
\rho_L=F_L+\kappa\epsilon,\qquad
H=\gcd(G,F_L+\kappa A).
\]

Multiplication by rho_L is injective on every chain group: as a P-linear map on P[epsilon]/epsilon^2 its determinant is F_L^2. Therefore the short exact sequence of complexes

\[
0\to\mathcal C\xrightarrow{\rho_L}\mathcal C
\to\mathcal C/(\rho_L)\to0
\]

gives the exact sequence

\[
\boxed{
0\to P/(H)\to H_1(\mathcal C/(\rho_L))
\to\operatorname{ann}_{P/(G)}(F_L+\kappa A)\to0.
}
\]

The right-hand term is isomorphic to P/(H), but the displayed sequence is not being treated as a Hamming-isometric splitting. Its left-hand term is precisely the image of universal compact homology; its right-hand term is specialization-created homology. In particular,

\[
\boxed{k_2=2\deg H.}
\]

An arbitrary universal cycle g f+b h survives the finite quotient exactly when

\[
\boxed{H\nmid f.}
\]

The corresponding base statement is that (bf,af) survives exactly when g_0 does not divide f.

Since g_0 divides both G and F_L+kappa A,

\[
g_0\mid H.
\]

Thus the compact cover image is nonzero whenever the compact base image is nonzero. This conclusion is proved by a one-relation exact sequence, not by a general base-change assertion or finite generation.

### 2.4 Transfer and projection on compact labels

The formulas are

\[
\boxed{\tau(f)=E f\pmod G,\qquad
p(f)=\frac{Ac}{G}f=\frac{A}{E}f\pmod c.}
\]

An exact universal boundary identity checks the transfer formula:

\[
\mathbf g(Ef)+\mathbf b(af)
=(bf,bf,af,af).
\]

Consequently, for a given surviving compact base representative,

\[
\boxed{\tau(bf,af)\text{ is nontrivial finitely}\iff H\nmid E f.}
\]

Whenever this holds, its physical weight is at most twice the universal base weight. No assertion that transfer always survives is made.

The exact compact cover metric is now

\[
\boxed{
\widehat\Delta(H)=
\min_{H\nmid f,\ h\in P}
\sum_{i=1}^4 |g_i f+b_i h|.
}
\]

This minimization includes all compact classes, every scalar multiple, and all universal boundary adjustments. The actual finite distance can be smaller at short periods; Section 7 shows exactly how to avoid that issue in a counterexample construction.

## 3. Formal derivatives prove one-sided factor two

Let $\mathcal E=z\,d/dz$ be the Euler derivative. Over F_2 it retains exactly the odd-exponent terms, even for Laurent polynomials.

Suppose the lift is (A+epsilon,B). If B has an odd exponent, B is square-free. Then E=gcd(c,b)=1, G=c and H=g_0. Every surviving compact base class therefore has a surviving transfer of weight at most twice its base representative.

Otherwise $\mathcal E B=0$. Primitivity forces A to have an odd exponent.

### 3.1 A has exactly one odd exponent

Write $\mathcal E A=z^r$. For a universal cycle (u,v), differentiating Au+Bv=0 gives

\[
A\mathcal E u+B\mathcal E v=z^r u.
\]

Thus

\[
\boxed{
\left(u+\epsilon z^{-r}\mathcal E u,
      v+\epsilon z^{-r}\mathcal E v\right)
}
\]

is a universal cover cycle. Its projection is (u,v), so it is nontrivial in every finite cover in which the base class survives.

Let w=|u|+|v|. Translate both components by either 1 or z so that the total number o of odd-exponent terms is at most w/2. Differentiation remains valid for the translated cycle. In the physical basis,

\[
|u+\epsilon p|=|u+p|+|p|\le |u|+2|p|.
\]

The total lift weight is at most w+2o<=2w.

### 3.2 A has two odd exponents

Here $\mathcal E A=A+1$. Set

\[
p=u+\mathcal E u,\qquad q=\mathcal E v.
\]

Then A p+B q=u, so (u+epsilon p,v+epsilon q) is a lift detected by projection. The correction p is the even part of u, while q is the odd part of v. It simply assigns existing monomials to sheets, and its total physical weight is exactly w.

This proves

\[
\boxed{\widehat\Delta(H)\le2\Delta(g_0),\qquad d_2\le2\Delta(g_0)}
\]

for all one-sided defects. The statement is relative to the compact base minimum, not automatically to the actual base distance for an unrelated presentation.

For a minimum-circuit rank-one presentation, the compact minimum equals d, as in the supplied framework. The theorem then gives an actual d_2<=2d statement for that regime.

### 3.3 An actual-distance corollary beyond rank one

The derivative construction also gives a sufficient condition for a factor-two bound on **all finite logicals**, including specialization-created ones. Let R=F_2[G] for any finite abelian group, and let chi:G->F_2 be a character. The linear operator

\[
\partial_\chi\!\left(\sum_g a_g g\right)=\sum_g\chi(g)a_g g
\]

is a derivation and is a support projector onto one parity class. Suppose the finite double cover splits, so its ring is R[epsilon]/epsilon^2, with normalized checks A+epsilon, B+nu epsilon. If a monomial unit M satisfies

\[
\boxed{(\partial_\chi A,\partial_\chi B)=M(1,\nu),}
\]

then

\[
\boxed{d_2\le2d.}
\]

For any finite base cycle, apply the derivation to its exact equation in R and use corrections M^{-1}partial_chi u and M^{-1}partial_chi v. Translate by a group element of odd chi value so that the selected parity has at most half the original support. The lifted cycle projects to the original translated logical and has weight at most twice its weight. This proof takes place in the finite coefficient ring and therefore covers winding classes as well.

The split-ring hypothesis matters here. This finite-class corollary is not automatically asserted for a nonsplit finite extension. In contrast, the preceding Laurent-cycle constructions remain valid in nonsplit finite quotients because their equations hold before imposing the period.

The weight-preserving and matched-even-part variants above and below also extend when the corresponding parity derivation exists on a split finite base. In the matched-even-part variant, multiplication by C=A+M acts as multiplication by the monomial M on H_1: multiplication by A is chain-nullhomotopic, since A(u,v)=(Bv,Av) is a boundary for a cycle.

### 3.4 Sharpness of the one-sided constant

For every odd L>=9 divisible by three, let

\[
A=B=1+z+z^2,\qquad
\widehat A=t+z+z^2,\quad \widehat B=1+z+z^2,
\qquad z^L=t^2=1.
\]

The exact parameters are

\[
[[2L,4,2]]\longrightarrow[[4L,4,4]].
\]

The base logical is (1,1), and the cover logical is (epsilon,epsilon). The module formula gives c=G=g_0=H=1+z+z^2 and E=1, proving dimensions and nonboundary of the transfer. Each cover column has weight three. All columns are distinct: B columns occupy only one sheet, A columns occupy both with counts two and one, and no nonzero cyclic translation stabilizes the consecutive three-point support when L>=9. Therefore there is no weight-two cycle and no odd-weight cycle. This proves cover distance four. The base distance is two from the displayed nonboundary. Hence the factor-two constant in the one-sided theorem is optimal.

These connected covers are cyclic after the odd-period coordinate change in Section 7. They are a sharpness family, not a new amplification record.

## 4. Exhaustive two-sided parity reduction

Now take the lift (A+epsilon,B+epsilon).

At a root zeta of c, square-freeness gives c'(zeta) nonzero, and

\[
a(\zeta)=\frac{A'(\zeta)}{c'(\zeta)},\qquad
b(\zeta)=\frac{B'(\zeta)}{c'(\zeta)}.
\]

Therefore E=gcd(c,a+b) consists exactly of the common roots at which A'=B'.

If one polynomial has only even exponents, its derivative is zero and the other is square-free, so E=1.

If one polynomial has two odd exponents and the other has one, then at a common root

\[
zA'=1,\qquad zB'=z^t.
\]

Equality would imply z^t=1. The second trinomial equation would then force its remaining monomial to vanish, impossible in the Laurent torus. Again E=1.

If both have two odd exponents, E=c, but there is a weight-preserving lift:

\[
(u,v)\longmapsto(u+\epsilon\mathcal E u,
                  v+\epsilon\mathcal E v).
\]

Indeed $A\mathcal E u+B\mathcal E v=u+v$, and both corrections are subsets of the original supports.

It remains that both have exactly one odd nonconstant exponent:

\[
A=1+z^r+z^{2s},\qquad
B=1+z^t+z^{2u},\qquad r,t\text{ odd}.
\]

If r=t, then differentiating gives

\[
A\mathcal E u+B\mathcal E v=z^r(u+v),
\]

so the balanced derivative lift from Section 3 gives factor two.

There is also a direct factor-two construction if 2s=2u. Put C=1+z^{2s}. The base cycle identity gives

\[
A\mathcal E u+B\mathcal E v=C(u+v).
\]

Hence

\[
(Cu+\epsilon\mathcal E u,
 Cv+\epsilon\mathcal E v)
\]

is a cover cycle. The polynomial C is a unit modulo c, because A=C+z^r. Projection therefore preserves a nonzero base compact label. For each input component, the even part produces at most two terms and the odd part produces exactly two physical-sheet terms; the total lift weight is at most 2w.

These are sufficient factor-two cases. The next section subsumes them and an additional slope-one case in one formula.

### 4.1 The exceptional gcd is cyclotomic

Define

\[
R=(t-r)/2,\quad S=u-s,\quad g=\gcd(|R|,|S|).
\]

If R=S=0, A=B and the matched checks upstairs are also equal; there is no amplification obstruction.

Otherwise let J=1+z^R and K=1+z^S. Then

\[
A+B=z^rJ^2+z^{2s}K^2,
\qquad
(A+B)'=z^{r-1}J^2.
\]

A common root belongs to E exactly when J vanishes. In that case the equality A+B=0 forces K to vanish as well. Therefore

\[
\boxed{E=\gcd(A,1+z^R,1+z^S)
=\gcd(A,1+z^g).}
\]

The formula includes R=0 or S=0, interpreting 1+z^0=0.

Since A(1)=1 and E is square-free, E cannot be nonconstant when g is a power of two. More generally, its roots have nontrivial odd orders dividing g. The unresolved mechanism is consequently an odd-order resonance of both term pairs, not arbitrary Laurent cancellation.

## 5. An explicit divided-Euler lift for every resonant slope

Put

\[
X=z^r,\qquad Y=z^{2s},\qquad Z=z^g,
\]

and write

\[
A=1+X+Y,\qquad
B=1+XZ^{2p}+YZ^{2q},\qquad
p=R/g,\quad q=S/g,\quad\gcd(p,q)=1.
\]

Negative integers p,q are allowed. Define finite Laurent polynomials

\[
\alpha=\frac{1+Z^p}{1+Z},\qquad
\beta=\frac{1+Z^q}{1+Z}.
\]

Their exact weights are

\[
|\alpha|=|p|,\qquad|\beta|=|q|,
\qquad|\alpha+\beta|=|p-q|.
\]

Set

\[
R_0=X\alpha^2+Y\beta^2,\qquad S_0=Y\beta^2,
\]

and

\[
K_0=X\bigl((1+Y)\alpha^2+Y\beta^2\bigr).
\]

Let C=1+Y and D_0=1+YZ^{2q}. Direct identities give

\[
R_0C+S_0A=K_0,
\qquad R_0D_0+S_0B=K_0.
\]

For a base cycle z=(u,v), set

\[
u_1=R_0\mathcal E u+S_0u,\qquad
v_1=R_0\mathcal E v+S_0v.
\]

Then

\[
\boxed{\mathfrak D(z)=
(K_0u+\epsilon u_1,\ K_0v+\epsilon v_1)}
\]

is a universal cover cycle. Indeed Euler differentiation and Au+Bv=0 imply

\[
A\mathcal E u+B\mathcal E v=Cu+D_0v,
\]

and the two displayed identities yield

\[
Au_1+Bv_1=K_0(u+v).
\]

### 5.1 Exact finite nonboundary criterion for the construction

At a root of E, Z=1 and A=0. Thus alpha and beta evaluate to the parities of p and q. They are not both zero because p,q are coprime. Since 1+Y=X,

\[
K_0=X\bigl(X(p\bmod2)+Y(q\bmod2)\bigr).
\]

Its value is X^2, XY, or X. All are nonzero. Therefore K_0 is a unit modulo E and every divisor of E.

If the original surviving base class has nonzero label at a root shared by E and g_0, the projection K_0 z is a finite nonboundary. Hence the displayed cover cycle is a finite nonboundary. This is a direct projection certificate, not a claim based solely on a universal cycle equation.

If transfer of a surviving compact base class is trivial, such a root necessarily exists. Otherwise at a root where f is nonzero, E would be nonzero and H could not divide E f. Thus transfer and the divided-Euler construction are exhaustive alternatives.

### 5.2 A uniform-in-period weight bound

Let w_0,w_1 be the total counts of even and odd terms in u,v. Write an individual component as x=x_0+x_1. The correction is

\[
R_0\mathcal E x+S_0x=X\alpha^2x_1+Y\beta^2x_0.
\]

Here X is odd and all terms of Y, alpha^2, beta^2 are even. The physical output obeys the bound

\[
\bigl(|p|+|p-q|+2|q|\bigr)|x_0|
+\bigl(|p|+|p-q|\bigr)|x_1|.
\]

Translate the base cycle by 1 or z so that w_0<=w/2. Summing gives

\[
|\mathfrak D(z)|\le
\bigl(|p|+|q|+|p-q|\bigr)w
=2m w,
\]

where m=max{|p|,|q|,|p-q|}. Combining with the surviving-transfer case proves

\[
\boxed{\widehat\Delta(H)\le2m\Delta(g_0),\qquad
 d_2\le2m\Delta(g_0).}
\]

For m=1 this gives factor two, including R=S after primitive normalization. For m=2 it gives factor four, not factor three. The integers p,q can be arbitrarily large, so this is not a universal constant-factor theorem.

In particular, every fixed primitive slope has a uniform linear bound even while the overall exponents, common spacing g, periods, and base distance grow. Any unbounded-amplification mechanism governed by a minimum-circuit presentation in this residual class must therefore have m tending to infinity.

This construction removes the need for a dense Bezout inverse of A or c. What remains is a controlled but potentially long binomial prefix-sum operation: alpha and beta. Whether all compact classes and boundary adjustments always permit replacing its m-dependent cost by a universal cost remains open.

## 6. Reducing the difficult finite root data

Suppose a minimum compact base representative (bf,af) has trivial transfer. Let

\[
E_0=\gcd(E,g_0).
\]

Then E_0 is nonconstant and E_0 does not divide f. Moreover,

\[
E_0=\gcd(A,1+z^{\gcd(g,L)}).
\]

Square-freeness permits replacing gcd(g,L) by its odd part. Thus E_0 has the form

\[
\boxed{E_0=\gcd(A,1+z^d),\qquad d\text{ an odd divisor of }g.}
\]

For this smaller root filter,

\[
\Delta(E_0)\le\Delta(g_0).
\]

Any universal cover class nonzero modulo E_0 is also nonzero modulo H, since E_0 divides g_0 and g_0 divides H. Hence a replacement theorem for E_0 supplies the desired upper bound in the original finite quotient.

Conversely, choose sufficiently large odd periods in an arithmetic progression starting at d, and use kappa=0. The base root filter is exactly E_0 and the cover filter is also exactly E_0. This follows from Section 7 and from the fact that gcd(c,1+z^d)=E_0 when d divides g.

In this reduced case:

* every compact transfer is zero, because E_0 divides E;
* projection from the compact cover image to compact base image is an isomorphism, because A/E=(c/E)a is a unit modulo E_0;
* specialization still creates an equally large additional homology sector;
* the latter sector has an independently proved growing winding-weight lower bound at large periods.

Thus even-period and nonsplit complications do not form an additional obstruction for the worst compact comparison. It suffices to handle these odd-period split realizations of the resonant root filters. This is a reduction of the inequality, not an assertion that all finite codes in the class are isomorphic to them at the original period.

## 7. Winding logicals and exact finite-distance realization

This section controls all finite logicals, not just compact or transferred ones.

Fix A,B, the universal lift, and a finite period L_0 with its kappa. Let O be the multiplicative order of z modulo c. Because c is square-free over a finite field, O is a finite odd integer. Since G divides c^2,

\[
z^{2O}=1\pmod G.
\]

Set

\[
\boxed{L_j=L_0(1+2Oj),\qquad j\ge0.}
\]

Then F_{L_j} is congruent to F_{L_0} modulo c^2. Therefore both

\[
g_0=\gcd(c,F_{L_j}),\qquad
H=\gcd(G,F_{L_j}+\kappa A)
\]

are independent of j. The compact survival conditions and compact minima are exactly the same along the progression.

Let rho be the larger free-coordinate span of the support of the two checks. A monomial gauge of a check does not change this span, and sheet choices do not change it.

### 7.1 Short circuits unwrap

Consider a circuit of weight w in a finite base or cover. Its incidence graph is connected. Along a simple closed Tanner path, passage through one selected column changes the integer check position by a difference of two exponents of that column's check polynomial. The absolute value is at most rho. A simple closed path contains at most w selected columns, so its total integer displacement is at most rho w.

In the finite quotient this displacement is a multiple of L_j. If L_j>rho w, it is zero. In the cover, zero free displacement also has zero deck displacement, since the deck element remains nonidentity in the finite group. Thus all closed paths have trivial monodromy in the universal cover, and the entire circuit lifts consistently, with exactly the same support weight, to a compact universal cycle.

This argument uses the full selected incidence graph, so checks met four or six times are included. For a general cycle, split into circuits and lift the pieces. Consequently,

\[
\boxed{\text{every class outside the compact image has weight at least }
\lceil L_j/\rho\rceil.}
\]

No failed search is being used as this lower bound.

### 7.2 Both actual distances eventually equal the compact minima

Let $\Delta=\Delta(g_0)$ and $\widehat\Delta=\widehat\Delta(H)$. Both are finite because the compact images are nonzero.

A minimum compact representative gives $d\le\Delta$ and $d_2\le\widehat\Delta$. Suppose, for sufficiently large j, there were a smaller finite logical. It contains a nonboundary circuit of no larger weight. If

\[
L_j>\rho\max\{\Delta-1,\widehat\Delta-1\},
\]

that circuit unwraps to a universal cycle of the same weight. Its finite image is nontrivial, contradicting the appropriate compact minimum. Therefore

\[
\boxed{d(L_j)=\Delta(g_0),\qquad
 d_2(L_j)=\widehat\Delta(H)}
\]

for all sufficiently large j.

The threshold can be made explicit without already knowing either minimum. For example use the upper witnesses f=1 in the primitive base generator and in g, giving

\[
W=\max\{|a|+|b|,\sum_i|g_i|\}.
\]

Choosing L_j>rho W and larger than the check spans suffices. These generators survive because their labels are 1 modulo nonconstant g_0,H.

### 7.3 What a counterexample would imply

For fixed rank-one data, the assertion

\[
d_2\le C\Delta(g_0)
\]

for every compatible finite period with the fixed root data is equivalent to

\[
\widehat\Delta(H)\le C\Delta(g_0).
\]

The reverse implication uses the exhibited compact witness; the forward implication follows by taking sufficiently large periods in the progression.

Therefore a true compact-minimum violation above three produces an infinite family of actual BB pairs with the same ratio above three. That family has constant distances for those fixed polynomials; it is not itself unbounded amplification. If a sequence of rank-one data has unbounded compact-minimum ratios, choosing a sufficiently large period for each member yields actual unbounded amplification.

The condition must involve the minimum over **all** compact cover classes and boundary adjustments. An expensive chosen generator is not enough.

For the reduced hard case of Section 6, take odd periods with kappa=0. The finite cover C_L x C_2 is cyclic: with w=tz one has z=w^{L+1}, t=w^L. This gives explicit term-matched exponents for a cover on C_{2L}. The four check differences generate the universal cover group: a hypothetical index-two check subgroup mapping isomorphically to Z would require a homomorphism sending the even exponent 2s to the nontrivial deck element, impossible. Hence the stable hard-case realizations are connected.

## 8. The smallest remaining scalar inequality

Within the no-universal-torsion setting, all unresolved rank-one cases reduce to

\[
A=1+z^r+z^{2s},\qquad
B=1+z^{r+2gp}+z^{2s+2gq},
\]

where r is odd, p,q are coprime integers, the four check differences generate Z, the trinomials remain strict, and

\[
m=\max\{|p|,|q|,|p-q|\}\ge2.
\]

Let

\[
c=\gcd(A,B),\quad E=\gcd(A,1+z^g),\quad
E_0=\gcd(A,1+z^d),
\]

where d is an odd divisor of g and E_0 is nonconstant. Put G=cE and define g_i,b_i as in Section 2. The remaining factor-three assertion is exactly

\[
\boxed{
\min_{E_0\nmid F,\ h\in P}
\sum_{i=1}^4 |g_iF+b_i h|
\ \le\
3\min_{E_0\nmid f}(|bf|+|af|).
}
\]

Here a=A/c and b=B/c, while the symbols b_i are the four displayed boundary coefficients. Uppercase F in this minimization is a free message polynomial, not the finite-period polynomial F_L.

The left side is explicitly

\[
\min_{E_0\nmid F,h}
\left[
\left|\frac{AB+A+B}{cE}F+(B+1)h\right|
+\left|\frac{A+B}{cE}F+h\right|
+\left|\frac{A^2}{cE}F+(A+1)h\right|
+|h|
\right].
\]

The divided-Euler construction proves the same inequality with 3 replaced by 2m. The quantities alpha, beta, alpha+beta have lengths |p|,|q|,|p-q|. A universal constant would require controlling their genuine cancellation after allowing the entire compact module and boundary subspace, rather than bounding these lengths separately.

The first unresolved layer m=2 already contains the supplied 7/3 phenomenon. For p=2,q=1, there is an additional useful factorization. With X=z^r,Y=z^{2s},H=z^{2g},

\[
A=1+X+Y,\quad B=1+XH^2+YH,
\]

and

\[
B+HA=(1+H)(1+XH),
\qquad
A+(1+XH)+X(1+H)=Y.
\]

Thus the two binomial factors are comaximal modulo A with a monomial-unit certificate. The analogous cover identities hold with 1+XH replaced by t+XH and A by t+X+Y. This splits the algebraic sectors but has not yet produced a factor-three physical-weight bound. Comaximality alone must not be promoted to a sparse Hamming-isometric splitting.

**Most promising next lemma:** prove or refute the boxed four-output inequality for this resonant family, using the explicit divided-Euler map and the freedom to change both its message polynomial and its boundary adjustment. The first tractable mechanism to analyze is the comaximal two-binomial factorization at primitive slope (2,1), while retaining the all-class minimization. A uniform extension to all primitive slopes would settle the no-universal-torsion rank-one factor-three target. Rank-zero and finite-check linear bounds would still remain for the global C_* question.

## 9. The established 7/3 example sits in the residual case

In normalized minority-constant strip coordinates, the supplied example is

\[
A=1+z^{-1}+z^4,\qquad
B=1+z^{-13}+z^{-2},
\]

with cover (A+epsilon,B+epsilon), L=39, kappa=0. Exact polynomial arithmetic gives

\[
c=1+z+z^5,
\qquad E=E_0=1+z+z^2,
\qquad G=cE,
\qquad H=E_0.
\]

The normalized differences are R=-6,S=-3,g=3,p=-2,q=-1, so m=2. A supplied weight-six compact base cycle has trivial transfer, while the supplied weight-fourteen cover logical is nontrivial.

The new code checks these coordinate changes, the cycle equations, the killed transfer, and the cover nonboundary using a separating dual certificate. The exact distances 6 and 14 are inherited from the supplied independent distance certificates; this round does not claim a new exhaustive distance search or a new record.

The residual case is therefore not an artificial empty obstruction. It contains the already certified failure of factor two.

## 10. Verification, unsuccessful routes, and final ledger

### 10.1 What was independently checked

The symbolic proofs are the basis of the theorems. Supplemental exact checks are retained:

* `verify_structure.py`: 1,088 finite parameter instances, with 4,352 compact membership tests, 4,352 transfer tests, 4,352 exact universal transfer-boundary identities, and 1,088 period-stability tests. It reconstructs finite group-algebra matrices and checks both the compact dimension and the full dimension.
* `verify_lifts.py`: 1,009 exact polynomial-pair parity/gcd checks; 1,740 actual finite nonboundary checks of the new constructions; and 720 symbolic positive/negative slope checks. These include even periods, kappa=0 and 1, Laurent offsets, and matched odd/even exponents.
* `audit_certificates.py`: independently reconstructs the finite groups and boundary columns using coordinate tuples, imports none of the constructor arithmetic, uses the opposite pivot convention for rank, and checks 610 primal/dual nonboundary certificates against 27,594 boundary pairings.
* `verify_finite_parity.py`: 1,644 finite logical checks in 71 positive-dimension base instances; 1,028 inputs are outside the compact image. These directly test the finite split-cover extensions of the derivative arguments.
* `check_seed_coordinates.py`: the supplied seed's new coordinates, transfer behavior and weight-fourteen nonboundary.
* `verify_sharpness.py`: exact ranks, distinct-column lower bounds, and nonboundaries at L=9,15,21 for the uniformly proved sharpness family.

The general finite checks certify witnesses and exact algebraic membership, not quantum distance estimates. The sharpness family is separately certified with the explicit weight-two and odd-weight exclusions given in Section 3.4. No failure of a bounded or interrupted search is used as a distance lower bound. The recorded outputs are from completed verification runs.

### 10.2 Failed routes and remaining gaps

The parity analysis does not eliminate every two-sided lift: the odd-order resonant factors E are genuine, as shown by the supplied seed. Differentiation alone solves monomial derivative matching but does not invert two distinct derivative monomials without a binomial quotient.

The universal cover module is cyclic, but its primitive generator is not asserted to be minimum. Replacing the four-output minimum by the weight of that generator would repeat the earlier metric mistake.

The new explicit divided-Euler construction gives a factor depending on the primitive slope. Since that slope is unbounded, its existence is not a proof that any universal linear constant survives.

No parametric compact-minimum counterexample was found. The exact finite-realization theorem is conditional on such a **minimum-distance** comparison, not on a large chosen representative. It closes the winding loophole for a potential counterexample, but does not supply the missing compact lower bound.

The full rank-one factor-three inequality remains open after this round. Therefore this round does not proceed as though rank one were solved to claim a result for rank-zero or finite-check mechanisms.

### 10.3 Extremal ledger

The supplied lower bound remains C_*>=7/3, and the supplied connected 7/3 family remains the highest exact ratio established in this research state. No new exact ratio above it is claimed.

No finite numerical universal upper bound on C_* is established. The previously supplied bounds d_2<=32d^3 and Gamma(N)<=24 sqrt(N) are carried forward as input and are not improved globally here. The factor-two higher-rank theorem is also carried forward as input.

The thresholds 7/3, 5/2 and 3 remain unresolved for the entire BB class. Factor two is newly proved for the rank-one regimes specified above, and the only remaining no-universal-torsion rank-one mechanism is the explicitly parameterized two-sided cyclotomic resonance.

## Sources and dependencies

The current higher-rank result and general-bound ledger are taken from the supplied `BB_linear_compact_replacement_report.md`. Their scope is preserved; they are not silently generalized.

The matched-cover convention is the one in B. C. B. Symons, A. Rajput and D. E. Browne, *Sequences of Bivariate Bicycle Codes from Covering Graphs*, arXiv:2511.13560v3, Theorem 3.1. That paper is used for the construction convention, not for the claimed new inequalities.

The distinction between derived tensor homology and ordinary tensor of homology is standard homological algebra; Stacks Project, Example 15.63.1, tag 061Z, provides the relevant general spectral-sequence context. The one-relation exact sequence in Section 2 is proved directly here.

The interpretation of the scalar encoder minima as convolutional free-distance problems is contextual only; no classical convolutional-distance theorem is imported to bound quantum homology. All new weight and nonboundary arguments are given above.
