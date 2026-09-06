# BB double-cover distance: principal results and evidence status

**Version 0.2.1 · Primary reading entry point.**

[中文完整报告](REPORT.md) · [Home](README.en.md) · [Adoption and exclusion register](results/STATUS.md) · [Full proofs](results/README.md)

## What is actually established in this repository?

There are two exactly certified finite counterexamples: $6\to14$ disproves the proposed universal upper inequality $d_2\le2d$, and $14\to12$ disproves the proposed universal lower inequality $d_2\ge d$. The repository also supplies symbolic proofs of the replacement inequalities $d\le4d_2^3$ and $d_2\le8d^3$, with the scope and provenance below.

**The 104 entries are research records, not 104 valid or independent theorems.** They include duplicate statements, valid negative results, failed proof approaches, conditional results, unavailable inherited inputs, incomplete searches and open questions. The full process is retained for traceability, not endorsed wholesale. A supplied symbolic proof, a completed finite exact certificate, a retained experimental audit and independent peer review are different evidence levels.

## Exact counterexamples

Use $A=1+x^8+x^{25}$ and $B=1+x^2+x^{13}$. Unchanged checks and periods $(39,1)\to(78,1)$ give

$$
[[78,4,6]]\longrightarrow[[156,4,14]],\qquad14>12.
$$

From that same middle code, periods $(78,1)\to(78,2)$ with $A'=1+x^8y+x^{25}$ and $B'=1+x^2y+x^{13}$ give

$$
[[156,4,14]]\longrightarrow[[312,8,12]],\qquad12<14.
$$

Both covers are connected, term-matched and locally bijective on full Tanner neighborhoods. Two independent exact verifiers are retained for each finite example. Attaining nonboundary witnesses and exhaustive exclusion of smaller nonboundaries are both needed; a found witness alone gives only an upper bound. [Proof and witnesses](results/theory/01-counterexamples.md); [algorithm completeness](results/theory/06-certificate-algorithms.md); [certificates](certificates/README.md).

The first example kills a shortest base class under transfer. The second uses a nonzero cover class whose projection is a boundary. These are the precise failures in the naive transfer/projection arguments.

## All principal bounds together

The common scope is binary coefficients, finite abelian groups, a term-preserving quotient with kernel $C_2$, exactly three distinct supported terms in each check both before and after projection, and positive base dimension $k$. Write the base as $[[n,k,d]]$ and the cover as $[[2n,k_2,d_2]]$; $n$ is always the BASE qubit count. Period one is allowed; cancellation or collision of projected terms is not. This is not a theorem about arbitrary Tanner covers or unrestricted term counts.

The supplied [polynomial proof](results/theory/03-polynomial-bounds.md) gives

$$d\le4d_2^3,\qquad d_2\le8d^3.$$

Set $C_0=\frac{16}{3}(12/\pi^2)^{3/4}$. Then

$$
 d_{\rm lower}=2\left\lceil\frac{(d/4)^{1/3}}2\right\rceil,
 \qquad
 d_{\rm upper}=2\left\lfloor\frac{\min\{8d^3,n,C_0(2n)^{3/4}\}}2\right\rfloor,
 \qquad d_{\rm lower}\le d_2\le d_{\rm upper}.
$$

Also minimize the upper endpoint with $2d$ when $k_2=2k$. These are general guarantee intervals, not exact distance computations. Constants and exponents are not claimed optimal.

The original amplification branch supplied constant 32; constant 8 is the consolidation corollary obtained by passing to an index-at-most-two voltage-kernel relation sublattice. Its provenance and review status are retained explicitly. Finite identity tests do not establish its all-parameter validity or constitute independent review. The old constant 32 is a historical weaker bound, not a refuted theorem.

The proof extracts a circuit presentation, applies finite-subgroup or strip/cofactor bounds, and treats the remaining Laurent and torsion–Frobenius cases with an explicit active-summand argument. It does not use the unavailable small-weight exclusion input, failed support-filling shortcuts, fixed-message optimization, local majority rules, or unsuccessful searches. See the [full proof](results/theory/03-polynomial-bounds.md), including the [index-two step](results/theory/03-polynomial-bounds.md#lem-transport).

The homological statements are

$$
 k\le k_2\le2k,\qquad \operatorname{rank}\widehat p_1=\operatorname{rank}\widehat\tau_1=k_2/2,
 \qquad k_2=2k\Rightarrow d_2\le2d,
$$

and $d_2\le2\lambda_{k-k_2/2+1}$ for the logical spanning thresholds. There is an exact sector decomposition $d_2=\min(d_{\rm vis},d_{\rm ker})$ with $d_{\rm vis}\ge d$; the kernel sector cannot be omitted. [Homology proof](results/theory/02-homology.md).

The ambient bound is $d\le\min(n/2,C_0n^{3/4})$. For a nonempty collection of covers with base length at most $N$, define $\gamma_-(N)=\inf d_2/d$ and $\Gamma(N)=\sup d_2/d$. Then

$$
\gamma_-(N)\ge\max\{N^{-2/3},c_-N^{-1/2}\},\qquad \Gamma(N)\le c_+\sqrt N,
$$

where $c_-=\pi3^{1/6}/2^{13/3}$ and $c_+=2^{3/2}C_0^{2/3}$. The finite examples give $\Gamma(N)\ge7/3$ for $N\ge78$ and $\gamma_-(N)\le6/7$ for $N\ge156$. No asymptotic equivalence or size-independent ratio is claimed. [Size-bound proof](results/theory/04-size-bounds.md).

## Scoped results, gaps and failed approaches

The Bockstein/Jordan refinements use the specified rectangular fourfold thickening; the class metrics require their stated pairing and section conventions. Compact factor-two results require the stated normal form and survival conditions. The all-degree Bellman result yields the stable $8\to14$ family only for the compatible long periods. The deck-involution strip inequality $d\le3d_2^2$ is a subclass result, and the fixed-$c$ bound $\mu_+\le\mu_0^2+2$ is not a general quadratic degradation theorem. These are useful, scoped statements, not licenses to remove hypotheses.

A material evidence dependency is now explicit: the original weight-six theorem states its starting weight-four exclusions as an input. That package is not restored. Thus its $d_2=6\Rightarrow d\le56$ and related combined conclusions are not promoted to unconditional, closed-evidence headline results. By contrast, the weight-eight proof explicitly derives $d_2=8\Rightarrow d\le96$ independently of those inputs; the combined consequence $d>96\Rightarrow d_2\ge10$ still needs them. The stronger ratio term $\min(1/12,20/N)$ also retains those dependencies. This revision does not silently fill them by changing a summary.

The restored distance-four argument and early infinite families retain source-provenance limitations. An exactly certified seed does not certify its whole historical parameter family. Missing evidence is not a proof of falsity; the appropriate action is to keep the limitation visible.

Several negative results are themselves valid and important. A failed support–Bockstein or filling lemma cannot be reused positively. Restricted cover minimum 16 is not full minimum 14. Fixed-message minima 74 and $74N$ coexist with a full minimum 14 in the same class. A local-majority boundary counterexample does not refute a claim about minimum nonboundaries. Short relation rows do not automatically give quadratic cofactors. Compact classes need not survive arbitrary specialization. A naive Frobenius candidate can be killed together with transfer. A five-term lift is outside the strict-trinomial target. Timeout or failure to find a witness is not an exact lower exclusion.

The [Chinese report](REPORT.md) links each of these distinctions to its specific record; every complete reading note now opens with a current-use warning. Original source bodies remain byte-preserved. The [status register](results/STATUS.md) classifies all 104 entries: 12 headline indices, 52 scoped/supporting records, 15 negative results, 3 historical weaker bounds, 8 evidence/dependency gaps, 2 exploratory records, 8 open questions and 4 out-of-scope entries. Counts are not independent theorem counts.

Global bounded amplification, a positive size-independent degradation ratio, a general quadratic degradation bound, and the remaining factor-three subproblems are unresolved in this supplied record. This is not a claim to have checked the latest worldwide literature. [Open questions](results/OPEN_PROBLEMS.md).

## Reproduction and navigation

```bash
python -m bbcover results                  # curated headline records by default
python -m bbcover results --view negative
python -m bbcover results --view gap
python -m bbcover results --view all        # complete process, not all valid theorems
python scripts/check_report.py --check     # editorial consistency, not proof checking
python scripts/reproduce.py --profile core --output checks/new-core
```

The report revision changes presentation, evidence gates and record selection, not the mathematical constants. Earlier full-audit logs remain earlier logs; they are not advertised as freshly rerun. Local success does not imply a remote GitHub Actions run, formal verification or independent peer review.
