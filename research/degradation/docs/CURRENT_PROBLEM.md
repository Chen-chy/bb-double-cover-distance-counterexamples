# Exact continuation handoff: fixed-$c$ mixed-parity Laurent amplification

This file restates the unresolved task and established source reductions. It proposes no new mathematical result.

## Definitions and the full target

Let $S=\mathbb F_2[z^{\pm1}]$, $c=1+z+z^2$, and

$$B=1+z^{6r+2}+z^{6t+1},\qquad b=B/c,\qquad P=(B+c)/c^2.$$

The requested genuinely mixed subclass has both parity binomials contributing after the allowed monomial gauges and normalizations. The broader endpoint estimates in the latest note also cover some simpler cases. Do not discard the hypotheses when importing a theorem from an earlier stage.

Set

$$\mu_0=\min_{c\nmid F}(|bF|+|F|),$$

$$\mu_+=\min_{\substack{F,H\in S\\c\nmid F}}
\left[|(b+P)F+bH|+|PF+bH|+|F+H|+|H|\right].$$

Weights are Laurent support weights before imposing a finite period. The target is $\mu_+\le3\mu_0$. Both $F$ and $H$ remain unrestricted. A calculation for $F=1$, a preferred logical, or $H=0$ is not a lower bound on the cover minimum.

## Exact equivalent forms already available

Use $\mathcal R=S[s]/(s^2+1)$, $e=1+s$, $\Theta=s+z+z^2$, and $D=b+eP$. The physical checks satisfy

$$\widetilde B=\Theta D,\qquad \Theta^2=c^2.$$

Every universal cycle is $(DV,V)$; boundaries correspond to $V\in\Theta\mathcal R$. For $V=F+eH$, the four sheet coordinates are exactly the four terms in the target. This is a physical parameterization, not an assumed sparse abstract module basis.

All twelve units of $S/(c^2)$ are physical monomial residue classes $z^is^j$, $0\le i<6$, $j\in\{0,1\}$. The latest proof consequently supplies the exact full-coset forms

$$\mu_+=\min_{J\in\mathcal R}(|D+\widetilde B J|+|1+\Theta J|),$$

$$\mu_0=\min_{J\in S}(|b+BJ|+|1+cJ|).$$

The earlier mixed-Laurent note also gives the exact penalty form

$$\mu_+=\min_{c\nmid F,H}
\left[|bF|+|F|+2\operatorname{off}(PF+bH;bF)+2\operatorname{off}(H;F)\right],$$

where $\operatorname{off}(X;T)=|\operatorname{supp}(X)\setminus\operatorname{supp}(T)|$. The minimizing cover message need not minimize the first two terms separately.

## Strongest current constraints

For every admissible $F$, $R=\operatorname{span}(B)\le4|bF||F|$. For a minimizing base word with block weights $a,m$,

$$\mu_+\le R+2\le4am+2\le\mu_0^2+2,$$

and the $+2$ is absent for two positive nonconstant exponents. If $\beta=|b|+1$, the explicit cover word obeys $\mu_+\le3\beta/2$. Therefore a factor-three violation requires

$$\mu_0<\beta/2,\qquad 3\mu_0\le R\le4am\le\mu_0^2.$$

A family with unbounded $\mu_+/\mu_0$ must have both block weights of every choice of minimizing base word diverge, as stated in the latest proof.

## The sufficient next lemma, still open

$$\boxed{\min_{c\nmid F}(|bF|+|F|)\ge\tfrac12(|b|+1).}$$

A proof gives factor three through the generator upper bound. A refutation only enters the stronger-cancellation regime: it still leaves the unrestricted cover minimum to be certified.

## What must not be recycled as a proof

The constant message is not universally optimal; the archived four-term message family disproves that claim. Transfer-killed classes also kill the naive Frobenius $3w$ construction. The five-term lifted relaxation has exact unbounded amplification but violates the actual three-term support matching. An abstract local-module isomorphism has no assigned physical norm bound.

A prospective factor-three counterexample must certify the **entire** $\mu_+$, including all messages and boundary adjustments. The available rank-one Bellman certificates illustrate how all-degree lower bounds can be independently checked. The inherited period-stabilization theorem then transfers a genuine relative-Laurent violation to sufficiently large compatible finite periods; no new winding-only concern is needed once that theorem's hypotheses are checked.

## Scope beyond this handoff

Neither this fixed-$c$ case nor the full no-universal-torsion mixed case is resolved. Rank-one mechanisms with universal torsion and other finite-incidence mechanisms remain relevant to global $C_*$. A claim in a prior user handoff that a genuinely higher-rank compact factor-two theorem had been obtained is preserved as external-branch context; its standalone proof is not one of the available nine packages. See [known gaps](KNOWN_GAPS.md).

Primary local sources: [rank-one proof](../research/07-rank-one-amplification/proof.md), [mixed-Laurent proof](../research/08-mixed-laurent/proof.md), [fixed-$c$ proof](../research/09-fixed-c-product-bound/proof.md), and their original audit files.
