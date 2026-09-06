> **先看当前采用状态：** 本篇在严格三项式目标类之外，且原始 verifier 包未恢复；完整推导保留但不列作目标类主结论。
> [主报告](../../REPORT.md) · [逐项采用／排除表](../STATUS.md)。本篇为保留过程，不是整篇无条件有效的定理集合。

[全部研究结果](../README.md) · [逐项结论](../CLAIMS.md) · [原始完整文本](../../research/beyond-trinomials/REPORT.md)

> 完整研究笔记的 GitHub 阅读版；仅调整数学分隔符、引用标记与链接。历史状态、限制和证明内容均保留。当前结论以总登记表中的逐项状态为准；这里的“验证”不等于独立同行评审。

# Preserved public report: arbitrary-term degradation

**Export provenance.** The mathematical content below is transcribed from the early public assistant response following the task attachment sent at 2026-09-05T16:36:47Z. It is not recovered from an original `proof.md` file. The original linked `bb_degradation/proof.md`, `verify.py`, and `verification.json` are unavailable. Citation/display wrappers and broken sandbox download links are represented by this provenance note and the source references below. No reported computation in this transcription was rerun during the export. The later strict-trinomial packages are separate evidence.

The following status and qualifications are the early report's own, not a claim that its findings were newly audited for this archive.

---

# STATUS: ASYMPTOTIC_DEGRADATION_ORDER_RESOLVED — for the arbitrary-term BB class

There is an important scope distinction. The paper initially defines BB codes using three terms in each polynomial, but §6.2 explicitly extends its construction to arbitrary term counts, including four terms each. The results below resolve the degradation order for that unrestricted extension and prove a vanishing ratio already with four terms each and weight-eight checks. They do not resolve the strictly trinomial problem. The cited paper is Symons–Rajput–Browne, arXiv:2511.13560v3.

The strongest conclusions are



$$
[[8a^2+4a,2,2a+1]]\longrightarrow[[16a^2+8a,4,2]],\qquad a\ge2,
$$



with an explicit valid BB double cover and an exact uniform distance proof. Thus no universal positive constant protects distance even in the fixed-weight-eight subclass.

Allowing the number of polynomial terms to grow gives



$$
\frac4N\le\gamma_-^{\mathrm{all}}(N)<\frac{160}{N}
$$



for all sufficiently large N. Consequently



$$
\gamma_-^{\mathrm{all}}(N)=\Theta(N^{-1}),\qquad
\Delta^{\mathrm{all}}(N)=\Theta(N).
$$



“All” denotes the arbitrary-term extension. Neither conclusion depends on the seed's claimed exact distances.

## 1. Setup and cover validity

Use the monomial basis of



$$
R=\mathbb F_2[x,y]/(x^\ell+1,y^m+1)
$$



and the BB complex



$$
R\xrightarrow{\partial_2}R^2\xrightarrow{\partial_1}R,\qquad
\partial_2s=(Bs,As),\qquad\partial_1(u,v)=Au+Bv.
$$



The distance is the minimum physical Hamming weight of a nonboundary cycle, taking the minimum of the X- and Z-distances. Inversion of group elements followed by interchange of the two qubit blocks gives a weight-preserving correspondence between X- and Z-logicals. Hence they have equal distance. The same operation gives equality of the two check ranks, so



$$
k=2\dim_{\mathbb F_2}R/(A,B).
$$



Theorem 3.1 uses enlarged periods $\tilde\ell=u\ell,\tilde m=tm$, with each supported monomial upstairs reducing to its corresponding monomial downstairs; the cover degree is ut. Its incidence argument extends to arbitrary term counts as in §6.2. Cover validity is checked on the actual supports after cancellation, not merely by checking polynomial reduction.

Projection p adds the sheets; full-fibre transfer tau duplicates a chain. In characteristic two,



$$
p\tau=0,\qquad\ker p=\operatorname{im}\tau.
$$



In triangular coordinates, with physical sheets (q+r,r),



$$
\widetilde\partial_i(q,r)=(\partial_iq,D_iq+\partial_ir).
$$



The resulting long exact sequence gives



$$
k_2=2k-\operatorname{rank}\beta_2-\operatorname{rank}\beta_1,
\qquad\ker\tau_*=\operatorname{im}\beta_2.
$$



Thus k_2=2k implies transfer injectivity, but no positive uniform comparison of Hamming norms.

## 2. A general compression construction

Let h>=2 and define



$$
R_{2h}=\mathbb F_2[x]/(x^{2h}+1),\qquad S=1+x^h,\qquad b_0=1+x.
$$



Choose a nonzero polynomial C with deg C<h and C(1)=0, and write C=b_0F by ordinary polynomial division. Define the base by



$$
A=SC,\qquad B=SC+b_0.
$$



In



$$
\widetilde R=\mathbb F_2[x,y]/(x^{2h}+1,y^2+1),
$$



put



$$
T=1+x^hy,\qquad \widetilde A=TC,\qquad\widetilde B=TC+b_0.
$$



The periods are (2h,1)->(2h,2).

### Actual support matching

The supports are



$$
\begin{aligned}
A&=C+x^hC,&\widetilde A&=C+x^hyC,\\
B&=(C+b_0)+x^hC,&\widetilde B&=(C+b_0)+x^hyC.
\end{aligned}
$$



The lower and upper x-halves are disjoint. Any cancellation inside C+b_0 happens identically in base and cover. Reduction y->1 therefore gives a bijection between supported terms, separately for each polynomial. This is a Tanner-graph double cover.

### Equality of physical codes

Both S^2=0 and T^2=0. Since (SF)^2=0, U=1+SF is a unit. Multiplying the check pair (A,b_0) by U gives



$$
U(A,b_0)=(A,A+b_0)=(A,B),
$$



because A(SF)=0. Multiplying partial_1 on its output by a unit leaves its kernel unchanged; multiplying partial_2 on its input by a unit leaves its image unchanged. Consequently (A,B) defines exactly the same physical cycle and boundary subspaces as (A,b_0), not merely an abstract weight-distorting equivalence. The analogous statement holds upstairs using 1+TF.

The ideals are



$$
(A,B)=(b_0),\qquad(\widetilde A,\widetilde B)=(b_0).
$$



Their quotient dimensions are one and two. Therefore



$$
Q=[[4h,2,d]],\qquad \widetilde Q=[[8h,4,d_2]].
$$



### Exact cover distance two

The vector w=(T,0) has weight two and is a cycle because $\widetilde A T=T^2C=0$. For nontriviality, use



$$
\phi:\widetilde R\longrightarrow\mathbb F_2[\epsilon]/(\epsilon^2),\qquad
x\mapsto1,\quad y\mapsto1+\epsilon.
$$



It annihilates both checks while $\phi(w)=(\epsilon,0)\ne0$. Every boundary maps to zero, so w is nonboundary. Both check polynomials are nonzero, so there are no zero check columns and no weight-one logicals. Hence d_2=2.

### An exact formula for the entire base distance

Let $\rho:R_{2h}\to R_h=\mathbb F_2[x]/(x^h+1)$ fold the halves and put $J_h=1+x+\cdots+x^{h-1}$. For (A,b_0), a cycle satisfies



$$
b_0(SFu+v)=0.
$$



Since $\ker b_0=\langle J_{2h}\rangle$,



$$
v=S(F\rho(u)+cJ_h),\qquad c\in\mathbb F_2.
$$



A cycle is a boundary exactly when u(1)=0 and c=0. Thus its homology labels are (rho(u)(1),c) in F_2^2. For fixed q=rho(u), the minimum left-block weight is |q| and the right-block weight is 2|Fq+cJ_h|. Therefore



$$
\boxed{d(Q)=\min_{\substack{q\in R_h,\ c\in\mathbb F_2\$q(1),c)\ne(0,0)}}
\bigl(|q|+2|Fq+cJ_h|\bigr).}\tag{1}
$$



This includes all logical sectors.

## 3. A closed-form family with weight-eight checks

Take a,b>=2, h=ab, F=I_a=1+x+...+x^{a-1}, and C=1+x^a. The physical polynomials are



$$
\begin{aligned}
A&=1+x^a+x^h+x^{h+a},\\
B&=x+x^a+x^h+x^{h+a},\\
\widetilde A&=1+x^a+x^hy+x^{h+a}y,\\
\widetilde B&=x+x^a+x^hy+x^{h+a}y.
\end{aligned}\tag{2}
$$



Each has four distinct terms. The exact parameters are



$$
\boxed{[[4ab,2,\min\{b,2a+1\}]]\longrightarrow[[8ab,4,2]].}\tag{3}
$$



The Tanner graphs are connected. Shared terms connect the two qubit blocks; 1 and x connect adjacent x-coordinates; upstairs x^hy supplies the other translation generator.

### Uniform base lower bound

Equation (1) is the weighted homological distance of



$$
R_h\xrightarrow{(1+x,\ 1+x^a)^T}R_h^2
\xrightarrow{(1+x^a,\ 1+x)}R_h.
$$



Its cycles are (q,I_aq+cJ_h), and its boundaries are exactly q(1)=0,c=0. This is the square cellulation whose edge translations are a and 1 in Z_h, with costs one and two. Its period lattice is



$$
\Lambda=\{(r,s)\in\mathbb Z^2:ar+s=0\pmod{ab}\}
=\langle(b,0),(1,-a)\rangle.
$$



A nontrivial binary homology cycle contains a closed walk of nonzero winding modulo 2Lambda. Its lifted winding is nonzero in Lambda and has weight at least |r|+2|s|. If s=0, then b divides r, so the weight is at least b. If s!=0, then a divides s. For r!=0 the weight is at least 2a+1; for r=0 it is at least 2ab. Hence d>=min{b,2a+1}.

The two cycles



$$
(1,SI_a),\qquad(1+x^a+\cdots+x^{(b-1)a},0)
$$



have weights 2a+1 and b and labels (1,0) and (b mod 2,1). Both are nontrivial, proving (3).

### Vanishing ratio

Take b=2a+1. Then n_a=8a^2+4a, d_a=2a+1, d_{2,a}=2 and



$$
\frac{d_{2,a}}{d_a}=\frac2{2a+1}=\Theta(n_a^{-1/2})\longrightarrow0.
$$



For the four-terms-each restriction, put



$$
a_N=\left\lfloor\frac{\sqrt{1+2N}-1}{4}\right\rfloor.
$$



For N>=40, \(\gamma_-^{(4)}(N)\le2/(2a_N+1)$. No alternating-cover recursion is used.

## 4. Exact transfer compression and filling distortion

The proposed transfer-class formula is



$$
\boxed{\lambda(\alpha)=\min_{\substack{a'\in\alpha\\s\in C_2}}
\bigl(|a'+D_2s|+|a'+(D_2+\partial_2)s|\bigr).}\tag{4}
$$



Add the cover boundary (partial_2 s,D_2s+partial_2t) to the transfer representative (0,a), then absorb partial_2t into a'.

For the general construction, set q_base=(S,0) and H=I_h. Then partial_2H=q_base and |q_base|=2. The minimum coefficient weight of a base filling is h: the two solutions of b_0H=S are the complementary half-intervals I_h and I_h+J_{2h}.

With epsilon=1+y,



$$
w+\widetilde\partial_2H=\epsilon a_*,\qquad
 a_*=(x^h+SF,SF).\tag{5}
$$



Thus [w]=tau_*([a_*]). Since k_2=4=2k, transfer is injective. For alpha=[a_*], whose label is (1,0),



$$
\delta(\alpha)=\min_{q(1)=1}(|q|+2|Fq|),\qquad\lambda(\alpha)=2.\tag{6}
$$



For (2), delta(alpha)=2a+1 for every a,b>=2. In the lattice basis above, this class has even coefficient on (b,0) and odd coefficient on (1,-a), forcing |s|>=a and r odd.

Holding b fixed makes delta(alpha) grow while the entire code distance stays at most b. Taking b=2a+1 removes that competing small logical.

### Exact filling invariant

Define



$$
\operatorname{Fill}(q)=\min\{|\beta|:\beta\in\operatorname{im}\widetilde\partial_2,\ p\beta=q\}.
$$



For the construction,



$$
\boxed{\operatorname{Fill}(q_{\rm base})=2\delta(\alpha).}\tag{7}
$$



Transfer injectivity implies the boundary lifts are exactly beta=w+tau(a'), a' in alpha. The support of w occupies one sheet over each of left-block sites 0,h, so



$$
|w+\tau(a')|=2+2|a'|-2(a'_L(0)+a'_L(h)).
$$



Folding gives



$$
\operatorname{Fill}(q_{\rm base})=2+2\min_{q(1)=1}(|q|-q_0+2|Fq|).
$$



The minimum is delta(alpha)-1: the lower bound is immediate, and a minimizing odd q can be translated so q_0=1. Thus in the one-parameter family,



$$
|q_{\rm base}|=2,\quad|w|=2,\quad\operatorname{Fill}(q_{\rm base})=4a+2=2d.
$$



A weight-two base boundary has increasingly expensive boundary lifts while admitting a weight-two nonboundary lift.

For any double cover, a logical Y projecting to a boundary q satisfies



$$
|Y|+\operatorname{Fill}(q)\ge2d.
$$



Adding a boundary lift gives a nontrivial full-fibre cycle of weight at least 2d. This necessary relation alone does not provide constant-factor protection.

## 5. Linear-distance bases and optimal unrestricted order

Allow term counts to grow. Let h=2^r>=2, so



$$
R_h=\mathbb F_2[x]/((1+x)^h),\qquad J_h=(1+x)^{h-1}.
$$



There is a unit f in R_h such that



$$
\mathcal C_f=\{(u,fu+cJ_h):u\in R_h,\ c\in\mathbb F_2\}
$$



has minimum distance greater than h/10. This does not assume infinitely many primes with a primitive-root property.

### Counting lemmas

For a transitive binary linear code V of length m and dimension k,



$$
\#\{v\in V:|v|\le\delta m\}\le2^{kH_2(\delta)},\qquad0\le\delta\le1/2.\tag{9}
$$



Take the uniform distribution on that weight ball. Transitivity gives equal coordinate marginals with probability of one at most delta. Projection onto an information set is injective; entropy subadditivity gives the estimate.

Every nonzero word v in a cyclic code of length h and dimension s satisfies



$$
|v|\ge h/s.\tag{10}
$$



The cyclic shifts cover every coordinate. A basis of their span uses at most s shifts and still covers every coordinate, so h<=s|v|.

### Existence proof

Choose f uniformly among the 2^{h-1} units. If u!=0 has exact (1+x)-adic valuation t, put s=h-t. Multiplication by a random unit sends u uniformly over the 2^{s-1} elements of exact valuation t.

The cases u=0 and u=J_h cannot produce a nonzero word of weight at most D=floor(h/10). In every other bad word (u,v), the two entries have the same exact valuation, including for c=1, since adding J_h preserves that valuation.

The ideal I_t=((1+x)^t) has dimension s. Equation (10) gives |u|+|v|>=2h/s, so a bad word requires s>=20. The code I_t^2 is transitive of length 2h and dimension 2s. Equation (9) bounds candidate pairs of weight at most D by 2^{2sH_2(1/20)}. Each fixed pair and c has probability 2^{-(s-1)}. Therefore



$$
\Pr(f\text{ bad})\le4\sum_{s=20}^h2^{-s(1-2H_2(1/20))}
<4\sum_{s=20}^{\infty}2^{-2s/5}<5/64<1.\tag{11}
$$



The exact estimate H_2(1/20)<3/10 follows from
20(20/19)^{19}<20e<60<64, and 2^{-2/5}<4/5 bounds the geometric series. This proves the claimed distance lower bound.

### Deterministic finite-search specification

Choose the first unit f in binary-coefficient integer order satisfying that bound. This is a terminating finite-search specification, not an efficient-construction claim.

Let C be the canonical degree-<h representative of (1+x)f modulo x^h+1, and F=C/(1+x) by ordinary division. Then F=f+eJ_h for some e in F_2, so C_F=C_f. Apply Section 2. Formula (1) gives d(Q_h)>h/10. Since F is a unit, FJ_h=J_h, and the appropriate logical has weight h. Thus



$$
\boxed{Q_h=[[4h,2,d_h]],\quad h/10<d_h\le h,\quad
\widetilde Q_h=[[8h,4,2]].}\tag{12}
$$



The ratio is less than 20/h=80/n_h. The distinguished class has delta(alpha_h)=Theta(n_h), lambda(alpha_h)=2, and filling distortion Theta(n_h).

## 6. Matching lower bound

Every nontrivial BB code satisfies d<=n/2. Put K=n/2. Equal check ranks and k>0 imply ker A intersect ker B is nonzero. Multiplication by B preserves ker A and has nonzero kernel there, so it is not onto. Choose u in ker A outside B(ker A). Then (u,0) is a nonboundary supported in one block, proving the bound.

When both defining polynomials are nonzero, so are their valid lifts, and d_2>=2. Thus d_2/d>=4/n>=4/N. If zero polynomials are admitted, a nontrivial base of that form has distance one and does not weaken the bound for N>=4.

For the upper bound take the largest power of two h with 4h<=N. Then 4h>N/2 and gamma_all(N)<20/h<160/N. This proves order N^{-1}; constants are not optimized.

For four terms each, only



$$
4/N\le\gamma_-^{(4)}(N)=O(N^{-1/2})
$$



is obtained here. Its optimal exponent is not established.

## 7. Finite checks and the provisional seed, as reported

The exact explicit family includes

| a | Base | Cover | Ratio |
|---:|---|---|---:|
| 2 | [[40,2,5]] | [[80,4,2]] | 2/5 |
| 3 | [[84,2,7]] | [[168,4,2]] | 2/7 |
| 4 | [[144,2,9]] | [[288,4,2]] | 2/9 |
| 5 | [[220,2,11]] | [[440,4,2]] | 2/11 |

The report states that the uniform proof gives exact distances and the executable checks independently verify supports, ranks, logical witnesses, and projected boundaries. It also reports that an exhaustive first-base check examined all 102,090 nonempty supports of weights one through four, found exactly 55 cycles, and found all 55 to be boundaries; a weight-five logical was checked separately. The underlying verification output is not present in this export.

### Essential seed audit, not full distance certification

For the supplied 14->12 seed the report verifies base/cover dimensions k=4,k_2=8, weight-twelve zero-syndrome nonboundary status of the proposed vector, projected-boundary membership, and transfer injectivity. The symbolic evaluation certificate uses



$$
\omega^2+\omega+1=0,\quad\eta^2=0,\quad
x\mapsto\omega(1+\eta),\quad y\mapsto1+\omega^2\eta.
$$



Both cover checks map to zero and the logical maps to



$$
(\omega^2\eta,\omega^2\eta)\ne0.
$$



This certifies d_2<=12, not d_2=12, and does not certify d>=14. The supplied ratio 6/7 remains conditional in this early report and is not used in the asymptotic theorem.

## 8. Strict trinomials, false lemmas, and the historical next obstruction

The early report states



$$
d>2\Longrightarrow d_2\ge4
$$



for strict-trinomial BB double covers. All cycles have even weight because both polynomials have augmentation one.

A cross-block weight-two cover cycle forces the cover checks to be monomial-associated, which projects to a weight-two base logical. A same-block weight-two cycle forces a trinomial support invariant under a nonidentity translation. The translation has order three, so the polynomial is a monomial multiple of 1+t+t^2. Its projected translation still has order three. The base kernel is the ideal generated by 1+p(t), and k>0 forces that generator to give a weight-two base logical. The report pointed to its original proof note for the full argument; that file is absent.

The early strict-trinomial bounds were 8/N<=gamma_3(N)<=1 for N>=8. Later stages supersede these bounds; this transcription preserves the original endpoint rather than rewriting it.

In the arbitrary-term and fixed-weight-eight classes the constructions disprove every size-independent d_2>=c d, lambda(alpha)>=c delta(alpha), and Fill(q)<=C|q| with positive constants, even with injective transfer. The two-parameter family also disproves the inference that compression of one long class necessarily degrades the entire code distance.

The early next obstruction was implementing compression with exactly three terms each and a short cycle longer than two. No strict-trinomial alternating-cover recursion was established in that report.

---

## Archive boundary

The original report linked three files: `bb_degradation/proof.md`, `bb_degradation/verify.py`, and `bb_degradation/verification.json`. They are not available here. This transcription preserves its substantive derivations and stated checks but cannot supply its missing executable audit trail. See `docs/KNOWN_GAPS.md` in the repository root for the full availability ledger.
