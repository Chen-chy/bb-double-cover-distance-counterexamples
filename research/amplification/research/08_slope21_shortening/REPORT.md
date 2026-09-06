# Slope (2,1): sharp sector separation and the exact lifting cost

## STATUS: CONSTANT_BOUND_STILL_OPEN

The full factor-three inequality is neither proved nor refuted in this round. No new actual amplification ratio is claimed. The supplied factor-four upper bound for slope (2,1) remains the available uniform bound from this route.

The new results are structural and exactly checkable:

1. The two-binomial identity produces two complementary universal-homology projectors, each represented by a two-monomial multiplier. Projection onto the surviving resonance sector costs at most a factor two, uniformly in the exponents. This constant is sharp.
2. For the slope-(2,1) form of the supplied record, the full base compact minimum is 6, but its universally resonance-pure minimum is exactly 12. The other pure sector has minimum 10. Therefore splitting the universal sectors first is not a metric-neutral operation, and a factor-3/2 purification lemma is false.
3. The full cover compact minimum in the same example is 14, whereas its universally resonance-pure minimum is exactly 16. Thus every minimum surviving cover representative uses a universal homology component that dies in the selected finite quotient.
4. The full compact cover minimum has an exact reformulation as the minimum, over all liftable compact base projections, of the projected weight plus twice an outside-support syndrome-completion cost. This includes every homology message and every boundary adjustment.

The values 12 and 16 above are **restricted universal-support minima**, not new finite BB distances. In particular, 16/6=8/3 is not an amplification record or a counterexample to any bound on the actual distance.

All five compact minima used in the report have finite, independently audited sublevel-closure certificates covering arbitrary Laurent support lengths. The symbolic theorems do not depend on these computations. No failed or capped search is used as a lower bound.

## 1. Scope, notation, and the inherited input

Work over P=F_2[z,z^{-1}]. Set

\[
X=z^r,\qquad Y=z^{2s},\qquad H=z^{2g},\qquad r\text{ odd},\quad g>0,
\]

and assume the displayed checks are strict trinomials and their differences generate the intrinsic primitive coordinate:

\[
A=1+X+Y,\qquad B=1+XH^2+YH.
\]

The active universal double cover is over S=P[t]/(t^2+1), with epsilon=1+t:

\[
\widehat A=t+X+Y=A+\epsilon,\qquad
\widehat B=t+XH^2+YH=B+\epsilon.
\]

Compatible finite quotients impose z^L=t^kappa, where kappa is zero or one. We do not assume a split finite extension.

The preceding report, `BB_rank_one_resonance_report.md`, is the input for the compact-image labels and large-period realization theorem. The relevant statements are recalled below where used, with the needed direct algebra. The earlier global bounds and the supplied 7/3 family are not re-audited in their entirety here.

Put c=gcd(A,B), a=A/c, b=B/c. For a nonconstant square-free resonance divisor E_0, define

\[
\Delta(E_0)=\min_{E_0\nmid f}\{|bf|+|af|\}.
\]

Weights are taken over the universal Laurent group basis. A finite compact class survives precisely when its message is nonzero modulo E_0 in the reduced hard-core setting. This setting is enough for the remaining factor-three question: when transfer fails, the prior reduction selects such an E_0 in the resonance factor. We do not identify this compact minimum with the physical finite distance at an arbitrary small period.

## 2. Exact factor separation

Define the binomials

\[
C=1+H,\qquad D=1+XH,
\]

and upstairs define Dhat=t+XH. The four exact identities are

\[
B+HA=CD,\qquad A+D+XC=Y,
\]
\[
\widehat B+H\widehat A=C\widehat D,
\qquad\widehat A+\widehat D+XC=Y.
\]

Since A has exactly one odd exponent, A'=z^{r-1} is a Laurent monomial. Thus A is square-free. The same holds for B. Let

\[
e=\gcd(A,1+z^g),\qquad j=\gcd(A,D).
\]

The unit identity A+D+XC=Y implies gcd(e,j)=1. Since C=(1+z^g)^2 and A is square-free,

\[
\boxed{c=ej.}
\]

Moreover, the cover resonance factor from the preceding report is exactly e. At a common root, equality A'=B' is equivalent to H=1. At an e-root that holds; at a j-root it cannot hold, since it would make A,C,D vanish simultaneously while Y is a unit. Therefore

\[
\gcd(c,a+b)=e,\qquad G=e^2j.
\]

The universal base and cover modules are

\[
H_1(C(A,B;P))\cong P/(ej),
\qquad
H_1(C(\widehat A,\widehat B;S))\cong P/(e^2j).
\]

For the second statement, eliminate epsilon using A+epsilon. The resulting quotient is P/(A^2), and the other check becomes A+B. Since gcd(A^2,A+B)=e^2j, its annihilator is cyclic with the stated quotient. Multiplication by epsilon acts on this homology as multiplication by A. This description concerns universal homology only.

### The finite specialization in the hard core

For rho=z^L+1+kappa epsilon, multiplication by rho on the free chain modules is injective: its determinant over P is (z^L+1)^2. On universal homology it acts as z^L+1+kappa A. Thus, with

\[
H_L=\gcd(e^2j,z^L+1+\kappa A),
\]

the compact image is P/(H_L), and the finite first homology fits into

\[
0\longrightarrow P/(H_L)\longrightarrow H_1(C/\rho C)
\longrightarrow\operatorname{ann}_{P/(e^2j)}(z^L+1+\kappa A)
\longrightarrow0.
\]

The last term is specialization-created homology. No weight-preserving splitting is assumed. In the reduced hard core used below, H_L=E_0 with E_0 dividing e, while the base compact image is also P/(E_0).

## 3. Two-monomial complementary projectors

Set

\[
P_e=Y^{-1}D,\qquad P_j=XY^{-1}C,
\]

and

\[
\widehat P_e=Y^{-1}\widehat D,\qquad
\widehat P_j=XY^{-1}C.
\]

Each has two group monomials. Hence multiplication by any of these polynomials increases a chain's Hamming weight by at most two.

They satisfy

\[
P_e+P_j=1+Y^{-1}A,
\quad P_eP_j=XY^{-2}(B+HA),
\quad P_e^2+P_e=Y^{-2}(A+XB),
\]

and

\[
\widehat P_e+\widehat P_j=1+Y^{-1}\widehat A,
\quad\widehat P_e\widehat P_j=XY^{-2}(\widehat B+H\widehat A),
\]
\[
\widehat P_e^2+\widehat P_e
=Y^{-2}(t\widehat A+X\widehat B).
\]

Multiplication by either check acts as zero on first homology. Explicitly, for a cycle (u,v), multiplication by A gives the boundary (Bv,Av), and multiplication by B gives the boundary (Bu,Au). Therefore these identities make each pair complementary orthogonal idempotents on homology. The proof works directly in every finite quotient as well: no semisimplicity or generic specialization is used.

On P/(ej), P_e is one modulo e and zero modulo j. On the universal cover module, substitute epsilon=A, so

\[
\widehat P_e\equiv Y^{-1}(A+D)=1+XY^{-1}C.
\]

It is one modulo e^2 and zero modulo j. Thus the projectors identify the two primary summands exactly.

### Sharp purification theorem

Call a universal base class *resonance-pure* when its j-component is zero. Define

\[
\Delta_e(E_0)=\min_{\substack{j\mid f\\E_0\nmid f}}
\{|bf|+|af|\}.
\]

Then

\[
\boxed{\Delta(E_0)\le\Delta_e(E_0)\le2\Delta(E_0).}
\]

The first inequality is restriction of the minimum. For the second, multiply a minimum surviving cycle by P_e. This kills its universal j-component, preserves its message modulo E_0, and costs at most twice its weight. Its finite nonboundary status is unchanged because P_e is one modulo E_0.

Let Deltahat_e be the analogous cover minimum with universal j-component zero. The same reasoning gives

\[
\boxed{\widehat\Delta\le\widehat\Delta_e\le2\widehat\Delta.}
\]

The base factor two is optimal; Section 5 gives a certified equality example. No sharpness claim for the second displayed factor is made.

These statements do not prove a twofold or threefold bound between base and cover. They quantify one operation only: discarding a universal homology component. A component which later dies in a finite quotient can still be valuable for Hamming cancellation before quotienting.

## 4. The exact projection-and-completion formula

Write a universal cover cycle in epsilon coordinates as

\[
(U,V)=(p+\epsilon r,q+\epsilon s).
\]

The two equations are

\[
Ap+Bq=0,\qquad Ar+Bs=p+q.
\]

Every universal base cycle is (p,q)=(bf,af). A Laurent filling (r,s) exists exactly when

\[
c\mid(a+b)f.
\]

Because c=ej and gcd(c,a+b)=e with gcd(e,j)=1, this is equivalent to

\[
\boxed{j\mid f.}
\]

Thus the actual chain-level image of projection consists exactly of the resonance-pure base cycles, including their universal boundaries. This is stronger than saying that the image on homology is one summand.

In the core compact image P/(E_0), projection is injective on compact cover homology. In the supplied cyclic coordinates it sends the cover message phi to (A/e)phi=ja phi modulo E_0. This multiplier is a unit modulo E_0 because A is square-free and e,j are coprime. Hence every filling of a projection with E_0 not dividing f is a finite nonboundary. Different fillings differ by (bh,ah), h in P; the corresponding cover difference is a compact transfer, which vanishes in the selected finite compact image.

For a liftable (p,q), define

\[
\kappa(p,q)=
\min_{Ar+Bs=p+q}
\bigl(
|\operatorname{supp}(r)\setminus\operatorname{supp}(p)|
+|\operatorname{supp}(s)\setminus\operatorname{supp}(q)|
\bigr).
\]

In physical sheets the lift is

\[
(p+r,r,q+s,s).
\]

For binary supports,

\[
|p+r|+|r|=|p|+2|\operatorname{supp}(r)\setminus\operatorname{supp}(p)|.
\]

Therefore the exact full compact minimum is

\[
\boxed{
\widehat\Delta(E_0)=
\min_{\substack{j\mid f\\E_0\nmid f}}
\left[
|bf|+|af|+2\kappa(bf,af)
\right].
}
\]

All homology messages, every Laurent filling, all universal boundaries, and all changes by compact classes killed after finite specialization are included. This is not the cost of one chosen generator or lift.

In particular,

\[
\boxed{\Delta_e(E_0)\le\widehat\Delta(E_0).}
\]

Together with the purification theorem, this separates the remaining issue into projected length, which has a factor-two bound, and completion cost, which does not yet have the required slope-independent estimate.

For fixed projected support, kappa is an erasure/syndrome-completion problem. Coefficients of r and s on the projected support are free in this cost. A coefficient outside it creates two physical qubits. The syndrome is p+q, and changing the filling by any base cycle is permitted.

## 5. An exact sharp obstruction to sector-first shortening

Use

\[
X=z,\qquad Y=z^{-4},\qquad H=z^6,
\]

so

\[
A=1+z+z^{-4},\qquad B=1+z^2+z^{13}.
\]

For causal arithmetic, multiply the first check by z^4 and apply the corresponding qubit-coordinate gauge. The pair becomes

\[
A_*=1+z^4+z^5,\qquad B_*=1+z^2+z^{13},
\]

and the cover checks are

\[
\widehat A_*=1+z^5+t z^4,\qquad
\widehat B_*=z^2+z^{13}+t.
\]

This is a gauged/reflected version of the supplied record mechanism, not a newly discovered high-ratio family. Direct factorization gives

\[
e=1+z+z^2,\quad j=1+z+z^3,\quad c=ej=A_*,\quad G=e^2j.
\]

Take E_0=e. The following are exact minima over arbitrary finite Laurent supports:

| Optimization domain | Minimum |
|---|---:|
| Full base compact classes surviving modulo e | 6 |
| Base classes surviving modulo e, with universal j-component zero | 12 |
| Base classes surviving modulo j, with universal e-component zero | 10 |
| Full cover compact classes surviving modulo e | 14 |
| Cover classes surviving modulo e, with universal j-component zero | 16 |

### Attaining witnesses and exact nonboundary labels

A minimum base cycle is

\[
u=1+z^5+z^9+z^{10},\qquad v=1+z^2.
\]

It satisfies A_*u+B_*v=0. Since c=A_*, its base homology message is simply v. It is nonzero modulo both e and j.

Multiplying by D=1+z^7 gives a pure resonant cycle of weight twelve:

\[
\operatorname{supp}(Du)=\{0,5,7,9,10,12,16,17\},
\quad
\operatorname{supp}(Dv)=\{0,2,7,9\}.
\]

The omitted factor Y^{-1} in P_e is a translation and does not change weight or divisibility. Since the certified pure minimum is twelve, the symbolic factor-two purification bound is attained exactly.

One pure nonresonant weight-ten cycle has supports

\[
\operatorname{supp}(u_j)=\{0,2,3,4,6,9,10,11\},
\quad \operatorname{supp}(v_j)=\{0,3\}.
\]

Here e divides v_j but j does not. Thus splitting the weight-six class into its two nonzero universal sectors requires total representative weight at least 12+10=22. In particular, a proposal to obtain factor three by first splitting that class at total cost at most 3*6=18 is false.

An attaining full cover word, in physical coordinates (U_0,U_1,V_0,V_1), is

\[
\operatorname{supp}U_0=\{3,10,11\},
\]
\[
\operatorname{supp}U_1=\{0,4,6,7,9,11,12\},
\]
\[
\operatorname{supp}V_0=\{0\},\qquad
\operatorname{supp}V_1=\{2,3,4\}.
\]

Its projection has supports

\[
\operatorname{supp}p=\{0,3,4,6,7,9,10,12\},
\quad\operatorname{supp}q=\{0,2,3,4\}.
\]

In these gauged coordinates the filling equation is $A_*r+B_*s=z^4p+q$, rather than $p+q$; the physical weight identity is unchanged. The projection has weight twelve. Its epsilon coefficient lies outside projected support at exactly one coordinate, giving

\[
\boxed{14=12+2\cdot1.}
\]

This quantifies the record mechanism: the light base representative costs six, the smallest liftable projection costs twelve, and one additional pair of physical qubits is necessary and sufficient for a full compact lift.

The projection above differs from (Du,Dv) by the base boundary generated by h=z^3+z^4:

\[
(p,q)=(Du,Dv)+(B_*h,A_*h).
\]

Thus even after purification, allowing boundary changes in the projected cycle is useful. A separately displayed filling of (Du,Dv) has weight sixteen; the boundary-modified projection above has a weight-fourteen filling. No claim that that particular weight-sixteen filling is optimal for its fixed projection is needed for any theorem here.

An attaining universally resonance-pure cover word of weight sixteen is

\[
\operatorname{supp}U_0=\{4,5,6,7,10,11,12\},
\quad\operatorname{supp}U_1=\{0,3,5,9,11\},
\]
\[
\operatorname{supp}V_0=\{0,3,4\},\quad
\operatorname{supp}V_1=\{2\}.
\]

The lower certificate shows that every surviving cover word of weight fourteen has a nonzero universal j-component. That component dies at the selected finite specialization. Excluding it before minimizing therefore loses the true minimum even after all universal boundaries and all pure-sector messages are allowed.

### Complete cover label test

For any universal cycle in these gauged coordinates, set

\[
W=z^8(V_0+V_1)+z^4A_*V_1.
\]

Then j divides W, and the universal cover homology coordinate is

\[
\phi=W/j\pmod{e^2j}.
\]

To derive this, start before the gauge and eliminate epsilon using epsilon=z^{-4}A_*. The second component becomes V_0+V_1+z^{-4}A_*V_1. Its annihilator generator is z^{-8}j. Division gives the displayed coordinate exactly.

Consequently, finite compact survival modulo e is equivalent to W nonzero modulo e, or simply V_0+V_1 nonzero modulo e. Universal resonance purity is exactly j^2 dividing W. These tests include the nilpotent part of e^2 and do not misidentify the full universal module with its finite image.

### What this does and does not say about actual finite distance

For every sufficiently large odd L with 3 dividing L and 7 not dividing L, use the finite group C_L times C_2. The base compact root divisor is e, and the cover compact root divisor is also e: z^L+1 is square-free and excludes j. Both codes have k=4.

Every column has odd weight three, so every cycle has even total weight. All check offsets have span at most thirteen. A finite nonboundary circuit of weight at most twelve has zero free winding whenever L>156, and lifts to a universal compact nonboundary of the same weight. The analogous base argument excludes weights below six. The compact witnesses survive after reduction. Hence these finite codes have actual distances six and fourteen for such L>156.

At L=201, the bundle separately reconstructs the finite matrices, confirms k=k_2=4, and supplies dual functionals proving both displayed witnesses nontrivial. These checks verify upper witnesses and dimensions. Their lower bounds use the compact certificates plus the no-winding argument just stated.

The restricted cover minimum sixteen is not an actual distance. It cannot be used to claim an 8/3 record, much less a ratio above three.

## 6. Independently checkable minimum certificates

The five exact compact minima are not obtained by cutting Laurent support off at a chosen length.

### Finite-state encoding of arbitrary finite supports

After a common translation, every finite Laurent word has nonnegative support. In the gauged seed, the constant coefficient of the first check is a single sheet monomial. Therefore, at each exponent, choosing the right-block bits and the pending syndrome uniquely determines the left-block bits.

A state records the pending check syndrome and a compact label. The check memory is thirteen sites. The label is updated in reverse-Horner form by multiplication by z^{-1}. Multiplication by z is a unit modulo every label modulus, so nonzero and divisibility conditions are unchanged by translation or by this representation.

Terminated paths have zero pending syndrome. The accepted labels are:

| Case | Label modulus | Nonzero modulo | Zero modulo |
|---|---|---|---|
| Base full | e | e | 1 |
| Base resonant pure | ej | e | j |
| Base other pure | ej | j | e |
| Cover full | e | e | 1 |
| Cover resonant pure | e*j^2 | e | j^2 |

For the last case, the tracked label is W. Its two right-sheet input coefficients modulo e*j^2 are z^8 and z^8+z^4 A_*. The numerical bitset values are 219 and 125, with modulus 475. The independent auditor reconstructs these coefficients by polynomial arithmetic.

Every finite Laurent compact cycle, and every message or boundary adjustment allowed in the corresponding minimum, produces a terminated path. No path-length bound is imposed.

### The lower-bound certificate is closure, not trust in a solver

The C++ implementation performs a nonnegative-cost shortest-path search. It exports all discovered states of weight strictly below the attained minimum, with their distance labels.

The independent Python auditor does not rerun that shortest-path algorithm and does not import its arithmetic. For every exported state and every possible right input it checks:

1. The initial state is included with label zero.
2. No exported state is an accepted terminated nonboundary.
3. Whenever the stored label plus transition weight is below the proposed minimum, the next state is present with a label no larger than that sum.

By induction, every path of total weight below the claimed minimum stays inside the certified set, and cannot terminate in an accepted state. The proof does not require that the supplied labels actually be shortest distances; the inequalities suffice. A separate direct multiplication and homology-label check verifies each attaining word.

| Minimum certified | Closure states | Transitions audited |
|---|---:|---:|
| Base full: 6 | 45 | 90 |
| Base resonant pure: 12 | 3,025 | 6,050 |
| Base other pure: 10 | 1,009 | 2,018 |
| Cover full: 14 | 58,707 | 234,828 |
| Cover resonant pure: 16 | 305,220 | 1,220,880 |

The verifier checks checksums, uniqueness of records, every required transition, primal cyclehood, and the intrinsic label formula independently. The numerical claims are exact finite-state computations with a proof of completeness for unbounded Laurent support. They are not decoder estimates. These certificates are not proof-assistant formalizations or independent human referee reports.

## 7. Failed shortening routes and the remaining lemma

The binomial/unit certificate does provide uniformly sparse projectors. What fails is the stronger inference that one may discard the complementary universal sector at negligible Hamming cost.

The exact example refutes a universal base purification estimate Delta_e <= (3/2) Delta; equality in the factor-two bound occurs. It also refutes equality between full and universally purified cover minima. The latter failure is not a problem with finite homology: the discarded component really does die in the finite quotient, but is still useful in a short universal representative.

Small formal-support searches for a fixed linear derivative-based map were also attempted. They did not produce a factor-three construction. Their bounds on the map ansatz are not bounds on all homology representatives, so no impossibility theorem or distance conclusion is drawn from them. They are not used in the certified results.

### Exact unresolved inequality

For slope (2,1), the full compact factor-three question is now exactly

\[
\boxed{
\min_{\substack{j\mid f\\E_0\nmid f}}
\left[|bf|+|af|+2\kappa(bf,af)\right]
\ \le\ 3\Delta(E_0).
}
\]

The projected term alone has a sharp factor-two bound. The missing estimate is joint: a projection with suitably low weight must be paired with a suitably inexpensive syndrome filling. Two independently optimized worst-case estimates would not capture the cancellations.

A sufficient next lemma is the following, explicitly unproved.

**Half-weight completion after sparse projection.** Among minimum surviving base cycles z of weight Delta, one can choose z and a universal base boundary beta such that

\[
w=P_ez+\beta,
\qquad |w|\le2\Delta,
\qquad \kappa(w)\le\Delta/2.
\]

The message condition is automatic: P_e is one modulo E_0 and beta is a universal boundary. This lemma would imply the factor-three bound. It is stronger than the exact minimum inequality because it starts from a minimum base class; a failure of this sufficient lemma alone would not refute factor three. The exact boxed optimization must remain the counterexample criterion.

The seed demonstrates why beta must be allowed: h=z^3+z^4 moves the simplest purified projection to the projection of an attaining cover word. The general problem is to find such boundary changes with an additive outside-support budget, not to bound a prescribed generator or derivative representative.

### Relation to actual distance and other slopes

The supplied large-period realization theorem applies to this exact compact optimization. For fixed polynomial and root data, choosing sufficiently large compatible periods excludes cheaper winding logicals. A certified full compact ratio above three would therefore produce an actual finite-distance ratio above three, and indeed infinitely many periods realizing the same pair of constant compact distances. No such example is obtained here.

Since slope (2,1) itself remains unresolved, no uniform extension to all coprime primitive slopes is claimed. The two-monomial projectors use the special two-binomial factorization displayed in Section 2; general slopes introduce longer binomial quotients. The inherited bound with coefficient 2*max(|p|,|q|,|p-q|) is not improved uniformly in this round.

The supplied lower bound C_* >= 7/3 and record family remain unchanged. No finite numerical universal upper bound on C_* is proved here, and the thresholds 7/3, 5/2, and 3 remain unsettled for the full class.

**Next target:** prove the half-weight completion lemma, or falsify it in a way that can be promoted to a lower bound on the full boxed optimization. This attacks the now-isolated syndrome-completion cost while retaining the necessary simultaneous freedom in message and boundaries.
