[研究结果总目录](../README.md) · [结论登记表](../CLAIMS.md) · [上一章](01-counterexamples.md) · [下一章](03-polynomial-bounds.md)

> 本章包含完整论证，可独立于 PDF 阅读。符号、范围和引用见正文；GitHub 版命题编号独立于排版稿。

<a id="sec-homology"></a>

# Scope, projection, and transfer

**Definition 2**. A strict-trinomial binary abelian double cover consists of a surjection $\pi:\widetilde G\to G$ of finite abelian groups with kernel of order two, and polynomials $\widetilde A,\widetilde B\in\mathbb F_2[\widetilde G]$, each with three distinct supported group elements, whose images $A,B$ also each have three distinct supported elements. Terms are matched individually. We assume the base code has $k>0$, and write its parameters as $[[n,k,d]]$, where $n=2|G|$, and those of the cover as $[[2n,k_2,d_2]]$.

This class includes the rectangular BB covers of Section [1](01-counterexamples.md#sec-examples). The proofs below work in the larger abelian class. They do not apply without modification to arbitrary Tanner graph covers, to polynomials with canceled terms after projection, or to an unrestricted number of check terms.

Multiplying either check by a monomial induces a physical coordinate permutation on the complex. We may therefore normalize, compatibly in the two codes,

<a id="eq-normalized"></a>

$$
A=1+a_1+a_2,\qquad B=1+b_1+b_2.
$$

The normalized support subgroup $K=\langle a_1,a_2,b_1,b_2\rangle$ decomposes the code into isomorphic coset components. The distance is the distance of one component; positive dimension is equivalent to positive dimension of that component. The upstairs support subgroup maps onto $K$ with kernel of order one or two. Thus a disconnected cover creates no exceptional case: a degree-one component is isomorphic to a base component, and a degree-two component obeys the arguments below.

<a id="prop-ranks"></a>

**Proposition 3** (Homological rank constraints). Every cover in the stated class satisfies

<a id="eq-dimension-bounds"></a>

$$
k\le k_2\le2k,\qquad
 \operatorname{rank}(\widehat\tau_1)=\operatorname{rank}(\widehat p_1)=\frac{k_2}{2},
$$

where $p$ is projection and $\tau$ is the two-sheet transfer. In particular,

<a id="eq-full-dimension"></a>

$$
k_2=2k\quad\Longrightarrow\quad d_2\le2d.
$$

Proof. Let $t$ generate the deck kernel and put $\varepsilon=1+t$, so $\varepsilon^2=0$. Projection and transfer give an exact sequence of chain complexes

$$
0\longrightarrow C\xrightarrow{\tau}\widetilde C\xrightarrow p C\longrightarrow0.
$$

For a basis element $g\in G$, the transfer is the sum of its two preimages. It is independent of the chosen preimage and has weight two.

Let $M=R/(A,B)$ and $\widetilde M=\widetilde R/(\widetilde A,\widetilde B)$. Put $h=\dim M=k/2$ and $\widetilde h=\dim\widetilde M=k_2/2$. Since $\widetilde M/\varepsilon\widetilde M=M$ and $\varepsilon\widetilde M$ is a quotient of $M$,

$$
h\le\widetilde h\le2h,\qquad
 \operatorname{rank}\widehat\tau_0=\dim\varepsilon\widetilde M=\widetilde h-h.
$$

Exactness of the long homology sequence gives the connecting map rank

$$
\operatorname{rank}\beta_1=h-(\widetilde h-h)=2h-\widetilde h.
$$

Therefore $\operatorname{rank}\widehat p_1=k-\operatorname{rank}\beta_1=\widetilde h$, and then $\operatorname{rank}\widehat\tau_1=k_2-\widetilde h=\widetilde h$. When $k_2=2k$, transfer is injective on $H_1(C)$. Transferring a minimum base logical produces a nontrivial cover logical of weight $2d$. ◻

The rank formulas explain why no contradiction arises between the examples and [\[eq:full-dimension\]](02-homology.md#eq-full-dimension). The distance-increasing example has $k_2=k$, so some nonzero base classes are killed by transfer. The distance-decreasing example has $k_2=2k$, so transfer is injective, but projection still has a nonzero kernel.

<a id="prop-lambda"></a>

**Proposition 4** (A refined transfer bound). Let $\lambda_j(Q)$ be the least integer $r$ such that classes represented by cycles of weight at most $r$ span a subspace of $H_1(Q)$ of dimension at least $j$. Then

$$
d_2\le2\lambda_{k-k_2/2+1}(Q).
$$

Proof. The kernel of transfer has dimension $k-k_2/2$. A spanning space of larger dimension cannot lie in that kernel, so one of its weight-bounded generating classes survives transfer. ◻

There is also an exact, but code-dependent, separation of the two cover sectors. Let $d_{\rm vis}$ be the least weight of a cover cycle whose projected class is nonzero, and $d_{\rm ker}$ the least weight of a nonzero cover class in $\ker\widehat p_1$. Then

$$
d_2=\min\{d_{\rm vis},d_{\rm ker}\},\qquad d_{\rm vis}\ge d.
$$

This identity does not turn $d$ into a universal lower bound: the second sector remains essential. Likewise a shortest base logical need not survive transfer, and subtracting a lifted boundary has no automatic Hamming-norm control. These are metric issues, not failures of the chain maps.
