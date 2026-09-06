[研究结果总目录](../README.md) · [结论登记表](../CLAIMS.md) · [上一章](04-size-bounds.md) · [下一章](06-certificate-algorithms.md)

> 本章包含完整论证，可独立于 PDF 阅读。符号、范围和引用见正文；GitHub 版命题编号独立于排版稿。

<a id="sec-further"></a>

# Companion results and boundaries of the present conclusions

The repository preserves two longer research branches in addition to the counterexample certificates. They contain further symbolic arguments, finite classifications, exact optimization certificates, and failed approaches. We distinguish their roles here. The main proofs in Sections [2](02-homology.md#sec-homology)–[4](04-size-bounds.md#sec-size) do not depend on a small-weight classification, an unverified decoder output, or the stronger compact-metric results summarized below.

The retained incidence classifications also give the useful specialized bounds

$$
d=6\ \Longrightarrow\ d_2\le112,\qquad
 d_2=8\ \Longrightarrow\ d\le96
$$

[WeightSixNote](../REFERENCES.md#ref-WeightSixNote); [WeightEightNote](../REFERENCES.md#ref-WeightEightNote). Their full arguments and classification code are included as companion notes. The fresh audit rechecks retained algebraic certificates, but does not rerun both expensive complete weight-six classification generators. Earlier weight-two/four assertions and the original weight-six descent note have separate provenance or starting assumptions, recorded in the repository claim map; they are not hidden dependencies of the general theorem.

<a id="an-exact-higher-rank-compact-metric"></a>

## An exact higher-rank compact metric

For the support-generated normal form

$$
T\oplus\mathbb Z^2,\qquad
 A=1+X+Y,\qquad B=1+hX^{2^s}+kY^{2^s},\qquad T=\langle h,k\rangle,
$$

the companion compact-metric note [CompactNote](../REFERENCES.md#ref-CompactNote) gives the exact minimum weight of a nonzero universal compact class:

<a id="eq-compactmetric"></a>

$$
\delta_{\rm comp}=o\,2^{a-b}3^b(3^s+1),
$$

where $o=|T_{\rm odd}|$ and $T_2\cong C_{2^a}\times C_{2^b}$, $a\ge b\ge0$. It constructs a minimum representative generating the compact module, and gives compatible double-cover replacement ratios $1,3/2,2$ in the stated normal-form setting. Its proof uses a squaring-and-coset lower bound for a finite-group kernel, two generic evaluations to bound the two physical blocks separately, and an attaining module generator. The retained audit checks 2,322 explicit primal/dual replacement certificates.

This is a factor-two theorem in its specified higher-rank regime, not a global factor-two theorem for arbitrary BB double covers. Specialization may create homology not represented by compact cycles, and a nonzero universal class can become a finite boundary. To apply a compact result to code distance, finite survival or a winding exclusion must be proved. The polynomial comparison above avoids replacing finite homology by compact homology.

<a id="a-rank-one-relative-laurent-optimization"></a>

## A rank-one relative Laurent optimization

The other branch reduces a remaining family to a physical, rather than abstract, polynomial minimization. Let

$$
S=\mathbb F_2[z^{\pm1}],\quad c=1+z+z^2,\quad
 B=1+z^E+z^O,
 \quad E=6r+2,\quad O=6t+1,
$$

with three distinct terms, and set $b=B/c$, $P=(B+c)/c^2=(b+1)/c$. For the stated finite-survival criterion, the relative Laurent minima are

<a id="eq-mu0"></a>
<a id="eq-muplus"></a>

$$
\begin{aligned}
 \mu_0&=\min_{c\nmid F}\bigl(\operatorname{wt}(bF)+\operatorname{wt}(F)\bigr),\\
 \mu_+&=\min_{\substack{F,H\in S\\c\nmid F}}
 \left[\operatorname{wt}((b+P)F+bH)+\operatorname{wt}(PF+bH)+\operatorname{wt}(F+H)+\operatorname{wt}(H)\right].
 
\end{aligned}
$$

All Laurent messages $F$ and all boundary adjustments $H$ remain unrestricted. The condition $c\nmid F$ is part of the relative problem; it must not silently be replaced by nonzero universal homology alone.

The physical source of the formula is particularly simple. In $\mathcal R=S[s]/(s^2+1)$, set $e=1+s$, $\Theta=c+e$, and $D=b+eP$. The lifted checks are

$$
\widetilde A=\Theta=s+z+z^2,\qquad
 \widetilde B=\Theta D=s+z^E+z^O.
$$

Since $\Theta^2=c^2$ is a nonzerodivisor, all universal cycles are $(DV,V)$ and universal boundaries have $V\in\Theta\mathcal R$. Writing $V=F+eH$ and expanding in the physical sheet basis $1,s$ produces exactly the four weights in [\[eq:muplus\]](05-further-results.md#eq-muplus). Thus the metric is explicit rather than assigned after a non-isometric normal-form change.

The supplied full proof [LaurentNote](../REFERENCES.md#ref-LaurentNote) establishes

<a id="eq-laurentquadratic"></a>

$$
\operatorname{span}(B)\le4\operatorname{wt}(F)\operatorname{wt}(bF),\qquad
 \mu_+\le\mu_0^2+2,
$$

with the $+2$ absent when $E,O>0$. It also shows that the twelve unit residues of $S/(c^2)$ are physical monomial translates, yielding an exact single-coset minimization with an unrestricted boundary variable. These statements concern the stated rank-one subclass and require the accompanying stabilization hypotheses before becoming equalities of finite code distances. They are not substitutes for a global linear amplification theorem or a quadratic degradation theorem.

<a id="exact-optimization-records-and-negative-controls"></a>

## Exact optimization records and negative controls

The companion rank-one package contains all-degree Bellman certificates for relative minima $8$ and $14$ for $A=1+z^2+z^7$, $B=1+z+z^8$ with the specified constant-term twists. Its stabilization theorem gives $[[2L,4,8]]\to[[4L,4,14]]$ for odd $L\ge105$ divisible by three [RankOneNote](../REFERENCES.md#ref-RankOneNote). This is useful independent evidence about complete optimizations; its ratio is not an improvement on $7/3$.

Several large values in the research history are deliberately not promoted to distance records. A sector-restricted minimum $16$ coexists with full admissible minimum $14$. A fixed-message minimum $74N$ lies in a universal class admitting a weight-fourteen representative. A relaxed family with unbounded amplification uses a five-term lifted check and violates the strict three-term matching condition. Such records refute shortcuts involving a preferred message or sector; they do not refute an inequality for the full target class. The repository’s claim map links each assertion to its proof and exact audit scope.

<a id="open-quantitative-targets"></a>

## Open quantitative targets

For the stated class, the finiteness of the unrestricted amplification constant $C_*=\sup d_2/d$ and positivity of the unrestricted degradation ratio $\inf d_2/d$ are not settled by the supplied results. A global quadratic improvement $d\le C d_2^2$ is also not established. In the fixed-$c$ rank-one problem, $\mu_+\le3\mu_0$ remains unproved and unrefuted in this record. Any proposed counterexample must bound the complete minimum over $F,H$, not a selected class or fixed-message slice.

The cubic inequalities impose concrete restrictions on further constructions. An unbounded amplification sequence must have $d\to\infty$ along a subsequence. A vanishing degradation sequence must have $d_2\to\infty$ as $d\to\infty$. These conclusions do not decide either universal constant question.
