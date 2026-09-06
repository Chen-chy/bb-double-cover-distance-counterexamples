[全部研究结果](../README.md) · [逐项结论](../CLAIMS.md) · [原始完整文本](../../research/degradation/research/09-fixed-c-product-bound/proof.md)

> 完整研究笔记的 GitHub 阅读版；仅调整数学分隔符、引用标记与链接。历史状态、限制和证明内容均保留。当前结论以总登记表中的逐项状态为准；这里的“验证”不等于独立同行评审。

# Fixed-quadratic mixed Laurent amplification: a product-weight obstruction and a uniform quadratic bound

Date: 2026-09-06.

**Status: the requested strict-trinomial inequality `mu_plus <= 3 mu_0` remains unproved and unrefuted.** This note proves a uniform product-weight bound for every admissible Laurent message, an ensuing quadratic upper bound for the complete cover minimum, an exact physical reduction of all admissible cover classes to translates of one boundary coset, and a necessary strong-cancellation condition for any factor-three counterexample. It does not assert a new exact strict-trinomial distance record.

The all-representative parameterization and the finite-period stabilization theorem in the supplied preceding work are starting inputs. The new weight and incidence arguments below are proved directly. In particular, no assertion that finite homology equals specialized universal homology is used.

## 1. Setting and conclusions

Let



$$
S=\mathbb F_2[z^{\pm1}],\qquad c=1+z+z^2,
 \qquad B=1+z^E+z^O,
$$



where `E=6r+2`, `O=6t+1`. Exponents may be negative. The three supported monomials of B are distinct. The genuine mixed cases in the question are included; some conclusions also apply to their simpler endpoints.

Put



$$
b=B/c,\qquad P=(B+c)/c^2=(b+1)/c,
 \qquad R=\max\{0,E,O\}-\min\{0,E,O\}.
$$



These are Laurent polynomials: modulo `c^2`, `z^6=1`, so `B+c=0`. The exact minima under study are



$$
\mu_0=\min_{c\nmid F}(|bF|+|F|)
$$



and



$$
\mu_+=\min_{c\nmid F,H\in S}
 \bigl(|(b+P)F+bH|+|PF+bH|+|F+H|+|H|\bigr).
$$



Every weight is before finite-period reduction.

### Main theorem: product-weight rigidity

For **every** finite-support Laurent F with `c` not dividing F,



$$
\boxed{R\le4\,|bF|\,|F|.} \tag{1}
$$



In particular, if an optimal base word has block weights `a=|bF|`, `m=|F|`, and `w=a+m=mu_0`, then



$$
\boxed{\mu_+\le R+2\le4am+2\le w^2+2.} \tag{2}
$$



When E and O are positive, the endpoint count sharpens the conclusion to



$$
\boxed{\mu_+\le4am\le\mu_0^2.} \tag{3}
$$



Thus unbounded amplification in this subclass would require both block weights of every minimizing base word to grow. More quantitatively,



$$
\frac{\mu_+}{\mu_0}\le4\min(a,m)+\frac2{\mu_0}.
$$



This is **not** a universal constant bound. It is a uniform bound on the full Laurent optimization, not a bound on a selected compact generator divided by a selected base representative.

## 2. Exact physical systematic form

Let



$$
\mathcal R=S[s]/(s^2+1),\quad e=1+s,\quad
 \Theta=s+z+z^2=c+e,\quad
 \widetilde B=s+z^E+z^O.
$$



Then



$$
\Theta^2=c^2,\qquad
 \widetilde B=\Theta+c^2P
               =\Theta D,\qquad
 D=1+\Theta P=b+eP.
$$



The element Theta is a nonzerodivisor. Indeed, multiplication by its square is multiplication by the nonzero scalar Laurent polynomial `c^2`, and the ring is a free S-module.

Consequently, every universal cycle is exactly



$$
(DV,V),\qquad V\in\mathcal R,
$$



and boundaries are exactly those cycles for which V belongs to `Theta R`.

Writing `V=F+eH=(F+H)+sH` gives the four physical components in the question:



$$
((b+P)F+bH,\ PF+bH,\ F+H,\ H).
$$



The admissibility condition is `c` not dividing F. This form retains every message and every boundary adjustment.

The simple word `(D,1)` is an admissible cover cycle. Evaluation at



$$
z=\omega,\quad s=1,\quad \omega^2+\omega+1=0
$$



sends both checks to zero, sends D to 1, and sends this word to `(1,1)`. Every boundary evaluates to zero. Thus the word is a genuine nonboundary, universally and in any compatible finite specialization admitting this evaluation. Its weight is `|D|+1`; this is an upper bound, not an assertion of minimum.

## 3. All admissible cover classes are physically translation-equivalent

This reduction is exact and does not select a message on faith.

There is an isomorphism



$$
\mathcal R/(\Theta)\cong S/(c^2),\qquad s\mapsto z+z^2.
$$



The residue of `V=F+eH` is `F+cH` modulo `c^2`. It is a unit precisely when `c` does not divide F. The ring `S/(c^2)` has 16 elements and 12 units.

All 12 units are represented by the physical monomials



$$
\boxed{z^i s^j,\qquad0\le i<6,\quad j\in\{0,1\}.} \tag{4}
$$



Here is an algebraic verification of distinctness. In `S/(c^2)`,



$$
z^3=1+(1+z)c,\qquad s=1+c.
$$



The three nonzero classes modulo c are represented by `1,z,z^2`. The two nilpotent units `z^3` and s are independent over `F_2`: their nilpotent coefficients modulo c are respectively `1+omega` and 1, which are independent. Their four products, times the three residue classes, give all 12 units.

It follows that for every admissible V there is a monomial q from (4) and a Laurent J in the **physical** ring such that



$$
V=q+\Theta J.
$$



Thus



$$
(DV,V)=(Dq,q)+(\widetilde B J,\Theta J).
$$



Multiplication by `q^{-1}` is a physical translation, possibly with sheet exchange, and preserves weight. Hence the full minimum is also exactly



$$
\boxed{\mu_+=\min_{J\in\mathcal R}
 \bigl(|D+\widetilde B J|+|1+\Theta J|\bigr).} \tag{5}
$$



Similarly, all three nonzero base classes are translates, and



$$
\boxed{\mu_0=\min_{J\in S}
 \bigl(|b+B J|+|1+cJ|\bigr).} \tag{6}
$$



Equations (5) and (6) are complete coset optimizations, with unrestricted Laurent J. They do not say that J=0 is optimal. The reduction is special to the small unit group in the fixed-quadratic case; arbitrary larger common divisors need not have all their units represented by physical monomials.

## 4. Proof of the product-weight bound

### 4.1 Select a nonboundary incidence component

Take any admissible F and write `U=bF`. The equation



$$
cU+BF=0
$$



has `3(|U|+|F|)` syndrome incidences. Pair equal syndrome incidences at every coordinate. Each selected qubit becomes a vertex of a cubic multigraph. Loops are absent because each check has three distinct terms.

Each connected component is itself a cycle. At least one component `(U',F')` satisfies `c` not dividing F': otherwise every component would be a boundary and so would their sum. Put



$$
a=|U'|\le |U|,\qquad m=|F'|\le|F|.
$$



Both a and m are positive, because there are no nonzero pure cycles over the Laurent domain.

### 4.2 An important rank rigidity specific to the fixed quadratic check

Use three formal translations Z,X,Y, with



$$
A_{\rm univ}=1+Z+Z^2,\qquad
 B_{\rm univ}=1+X+Y.
$$



Solve the paired-incidence equations on a spanning tree. The remaining edges give integral relation rows in `Z^3`; let L be their span and



$$
\mathsf H=\mathbb Z^3/L.
$$



The actual realization maps `Z -> z`, `X -> z^E`, `Y -> z^O`. In particular Z has infinite order in H and H maps onto Z.

**Claim: H has free rank exactly one.**

Suppose instead that it had free rank at least two. Multiplication by `1+Z+Z^2` is injective on the group algebra: that algebra is free over `F_2[Z^{\pm1}]`.

After quotienting by `1+Z+Z^2`, Z has order three and lies in the nontrivial order-three summand. More explicitly, this quotient is the complementary idempotent summand of



$$
\mathbb F_2[\mathsf H/\langle3Z\rangle]
$$



to the projector `1+Z+Z^2`. It is a Laurent ring over a possibly nonreduced finite coefficient algebra, with free rank `rank(H)-1`.

The free positions of `1,X,Y` generate that remaining free group. If its rank is positive, these three positions are not all equal. Among three monomials at nonidentical free positions, at least one is a uniquely exposed term: this is also true when two free positions coincide, since the remaining singleton can be made extremal. Its coefficient is a group monomial and hence a unit in the coefficient summand.

A Laurent polynomial with a uniquely leading unit coefficient is a nonzerodivisor, including over a coefficient algebra with nilpotents. Therefore `1+X+Y` is a nonzerodivisor after the quadratic check is killed.

Now any universal cycle `A_univ u+B_univ f=0` has f divisible by `A_univ`, by reducing modulo `A_univ`. Cancellation of `A_univ` then shows that the cycle is a boundary. This would make the realized component `(U',F')` a boundary, a contradiction.

Thus H has free rank one, and L has rational rank two. This is not an assumption that the universal presentation is torsion-free. Possible torsion is retained throughout the argument; the nonzerodivisor proof handles its coefficient algebra directly.

### 4.3 Physical support counts control the two relations

Every fundamental cycle of the spanning-tree graph is simple. At an A-vertex its contribution to the Z coordinate is a difference of two ports in `{0,1,2}`, with absolute value at most two. At a B-vertex its contribution to the X,Y coordinates belongs to



$$
\{\pm(1,0),\pm(0,1),\pm(1,-1)\}.
$$



Consequently every fundamental relation `r=(r_0,r_1,r_2)` satisfies



$$
|r_0|\le2a,\qquad
 |r_1|,|r_2|,|r_1+r_2|\le m. \tag{7}
$$



Choose two independent such rows r,t. Their cross product has the form



$$
r\times t=\Delta(1,E,O),\qquad
 \Delta\in\mathbb Z\setminus\{0\},
$$



because both rows vanish on `(1,E,O)` and that vector is primitive.

The last two cofactors and their difference obey



$$
|\Delta E|\le4am,\quad
 |\Delta O|\le4am,\quad
 |\Delta(E-O)|\le4am.
$$



Since `|Delta| >= 1`,



$$
R=\max\{|E|,|O|,|E-O|\}\le4am\le4|U||F|.
$$



This proves (1) for every admissible Laurent message. No enumeration of support weights, trellis states, or incidence graphs is involved in the proof.

## 5. Exact constant-word weights

Let



$$
\beta=|b|+1,\qquad \nu=|D|+1.
$$



These are the weights of the two constant-message words, not necessarily the optimized minima.

The exact counts are:

| Exponent order | `3|b|-2R` | `|D|-R` |
|---|---:|---:|
| `0<O<E` | -1 | -1 |
| `0<E<O` | 1 | 0 |
| `E<0<O` | -1 | 0 |
| `O<0<E` | 1 | 0 |
| `E<O<0` | 1 | 1 |
| `O<E<0` | -1 | 0 |

In particular,



$$
\boxed{\nu\le R+2,\qquad \nu\le\tfrac32\beta.} \tag{8}
$$



For positive exponents, `nu=E` if E is largest and `nu=O+1` if O is largest.

### Uniform proof of the counts

The causal coefficient sequences of the reciprocal checks are



$$
c^{-1}=(1,1,0,1,1,0,\ldots),
$$



and, in physical two-sheet coefficients,



$$
\Theta^{-1}=(s,1,1+s,1,1,0,s,1,1+s,1,1,0,\ldots).
$$



Their weights per six positions are respectively four and six.

First translate the least numerator exponent to zero. Between consecutive numerator terms, the response is periodic. Before the second term, its residue is the first monomial. After the second term, its residue modulo the check equals the last monomial, since the full numerator is divisible by the check. Both intermediate residues are therefore monomial translates, with the same complete-period weight.

Moving an endpoint outward by six adds a disjoint six-position response block, increasing the base quotient weight by four and the cover quotient weight by six. Moving the middle term by six while preserving its order exchanges two complete blocks of equal weight and changes neither weight. It is therefore enough to count one residue representative in each of the six exponent orders. Representatives `(E,O)` are `(2,1)`, `(2,7)`, `(-4,1)`, `(2,-5)`, `(-10,-5)`, and `(-4,-5)`. Direct polynomial division gives the table. The period argument, not sampled extrapolation, proves it for all r,t.

Combining (1) and (8) gives (2). For positive exponents, if O is largest it is odd, while `4am` is even. Thus `O<=4am-1` and `nu=O+1<=4am`. If E is largest, `nu=E<=4am`. This proves (3).

## 6. Necessary conditions for a factor-three or unbounded counterfamily

The complete minimum is at most nu, so a genuine violation `mu_plus > 3 mu_0` necessarily satisfies



$$
\boxed{\mu_0<\beta/2.} \tag{9}
$$



In words, the base optimization must improve the constant-message weight by **strictly more than a factor of two**. Ordinary generator cancellation, by itself, is not enough. This conclusion is necessary, not sufficient: the optimized cover minimum may still fall below three times the optimized base minimum.

Both distances are even. Thus a violation has `mu_plus >= 3 mu_0+2`. From (1) and (8), every minimizing base word must then satisfy



$$
\boxed{3\mu_0\le R\le4am\le\mu_0^2.} \tag{10}
$$



If a family had unbounded `mu_plus/mu_0`, then necessarily



$$
\frac R{\mu_0}\longrightarrow\infty,
 \qquad \min(a,m)\longrightarrow\infty
$$



for every selection of minimizing base words along a divergent subsequence. Any family admitting minimum messages with bounded weight in either block has a constant amplification bound from (2).

A sufficient next lemma is the base-only inequality



$$
\min_{c\nmid F}(|bF|+|F|)\ge\frac12(|b|+1). \tag{11}
$$



If (11) is true for all the strict trinomials here, (8) proves the full factor-three theorem immediately. This note neither proves nor refutes (11). A counterexample to (11) would only identify the strong-cancellation regime; it would not certify a violation of the full joint F,H inequality.

## 7. Adversarial control: the systematic identity alone cannot imply any constant

This section is a falsification check on an overbroad Hamming argument, **not** a strict-trinomial BB counterexample.

For N>=1 set



$$
b_N=z^{3N},\qquad
 P_N=\frac{1+z^{3N}}c=(1+z)\sum_{j=0}^{N-1}z^{3j},
 \qquad D_N=b_N+eP_N.
$$



These satisfy the same algebraic relation `cP=b+1`. With the same full systematic optimization, their exact minima are



$$
\boxed{\mu_0=2,\qquad\mu_+=4N+2.} \tag{12}
$$



The base value is immediate because multiplication by b_N is a translation.

For the cover value, translate the first qubit block by `z^{-3N}`. The resulting multiplier is `1+eP_N'`, where `P_N'=z^{-3N}P_N`. For a message `V=F+eH`, write `T=P_N'F`. The four outputs are



$$
(F+T+H,\ T+H,\ F+H,\ H).
$$



Pointwise minimization over H is exact and gives



$$
\min_H|Y|=2\,|\operatorname{supp}F\cup\operatorname{supp}T|.
$$



Modulo `1+z^{3N}`, every nonzero `P_N F` with `c` not dividing F is one of the three nonzero words in the kernel of multiplication by c. Each has weight `2N`: their supports are the pairs of residue classes modulo three. Therefore `|P_N F| >= 2N` before reduction.

The highest exponent of `P_N'` is -2. Hence the highest supported exponent of F is outside `P_N'F`, so the union has size at least `2N+1`. Taking F=1 attains that bound. This proves (12) over **all** Laurent F,H.

The reason this does not refute the target is exact:



$$
\Theta D_N=c z^{3N}+e.
$$



The second lifted check has five terms. The two extra terms in e project to zero and are not legitimate lifts of distinct base support terms. It violates the strict-trinomial termwise covering condition. Normalizing the base trinomial by a monomial does not repair that invalid support matching.

Thus a proof cannot use only the systematic identity, the small common divisor, or the abstract module. It must retain the actual three supported terms in the numerator. The proof of (1) does exactly that.

## 8. Finite realization and limits of the conclusions

For each fixed valid strict-trinomial instance, the supplied period-stabilization theorem identifies the Laurent minima with actual base and cover distances along sufficiently large compatible periods. Consequently (2) gives `d_2 <= d^2+2` **in that stabilized regime**, and (3) gives `d_2 <= d^2` for positive E,O in that regime.

This note does not infer either inequality for arbitrary short periods: their base distance can be below the Laurent benchmark. It also does not assert a quadratic upper bound for every rank-one presentation, for universal-torsion cases, or for the global constant C_*.

No strict-trinomial example with `mu_plus > 3 mu_0` has been certified here. The exact counterfamily in Section 7 is outside the permitted lift class. No universal linear constant for the remaining mixed class has been obtained.

## 9. Exact checks and independence

`verify.py` uses only the Python standard library. It performs:

- 2,401 exact quotient and weight-table checks, including all six sign/order regimes;
- an exhaustive check of the 12 monomial unit classes;
- 360 full-message/physical-boundary orbit checks;
- 240 independent incidence reconstructions and integer cross-product checks of the product-weight bound;
- 96 checks of the identities and sharp witnesses in the inadmissible relaxation control.

The incidence checker builds parity pairings directly from syndrome coordinates and reconstructs formal integral relations. It does not infer their rank or determinant from the polynomial gcd argument. Laurent multiplication uses sparse supports; exact quotient calculations use separate bit-polynomial division. All checks passed.

These computations supplement the uniform proofs. They are not minimum-distance searches and certify no new strict-trinomial minimum-distance record. The proofs are not externally refereed or proof-assistant formalized.

## Starting sources

The supplied `mixed_laurent_research/results/proof.md` and `rank1_amplification/proof.md` provide the preceding problem formulation, all-message parameterization, and finite-period stabilization theorem. The results proved in this note are distinguished above from those inputs.

The meaning of termwise BB support matching is the covering convention of B. C. B. Symons, A. Rajput, D. E. Browne, *Sequences of Bivariate Bicycle Codes from Covering Graphs*, arXiv:2511.13560v3, Theorem 3.1.
