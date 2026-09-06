[研究结果总目录](../README.md) · [结论登记表](../CLAIMS.md) · [上一章](03-polynomial-bounds.md) · [下一章](05-further-results.md)

> 本章包含完整论证，可独立于 PDF 阅读。符号、范围和引用见正文；GitHub 版命题编号独立于排版稿。

<a id="sec-size"></a>

# Ambient size and truncated distortion

The polynomial bounds can be combined with a geometry-of-numbers estimate that needs no assumption about a preferred compact sector.

<a id="thm-ambient"></a>

**Theorem 11** (Ambient distance). Every positive-dimensional strict-trinomial binary abelian code of length $n$ satisfies

<a id="eq-ambient"></a>

$$
d\le\min\left\{\frac n2,\ C_0n^{3/4}\right\},\qquad
 C_0=\frac{16}{3}\left(\frac{12}{\pi^2}\right)^{3/4}.
$$

Proof. Restrict to the normalized support group $K$, of order $M\le n/2$. Its full relation lattice $\Gamma=\ker(\mathbb Z^4\to K)$ has determinant $M$. Give $\mathbb R^4$ the positive-definite metric

$$
Q=\begin{pmatrix}
 1&1/2&0&0\\1/2&1&0&0\\0&0&1&1/2\\0&0&1/2&1
 \end{pmatrix},\qquad\det Q=9/16.
$$

Each port difference in $\mathcal D$ has $Q$ norm one. For three independent relation rows and their cofactor vector $c$, Cauchy–Schwarz and the Gram/cofactor identity give

$$
\max_{\delta\in\mathcal D}|c\cdot\delta|
 \le\sqrt{c^TQ^{-1}c}
 =\frac1{\sqrt{\det Q}}\sqrt{\det(r_iQr_j^T)_{i,j=1}^3}
 \le\frac43\prod_{i=1}^3\|r_i\|_Q.
$$

Lemma [7](03-polynomial-bounds.md#lem-strip) therefore bounds distance by $\frac{16}{3}\prod_{i=1}^3\|r_i\|_Q$.

The $Q$ unit ball has volume $2\pi^2/3$. For the successive minima $\lambda_1\le\cdots\le\lambda_4$ of $\Gamma$, Minkowski’s second theorem [Cassels, Chapter VIII](../REFERENCES.md#ref-Cassels) gives

$$
\prod_{i=1}^4\lambda_i\le\frac{24M}{\pi^2},\qquad
 \lambda_1\lambda_2\lambda_3
 \le\left(\prod_{i=1}^4\lambda_i\right)^{3/4}.
$$

Choose three independent vectors attaining the first three successive minima and substitute. This gives $d\le\frac{16}{3}(24M/\pi^2)^{3/4}\le C_0n^{3/4}$. Lemma [6](03-polynomial-bounds.md#lem-finite-check) supplies the other endpoint. ◻

Define $\mathcal C_N$ to be the set of the stipulated rectangular BB double covers with positive base dimension and base length $n\le N$, and put

$$
\gamma_-(N)=\inf_{\mathcal C_N}\frac{d_2}{d},\qquad
 \Gamma(N)=\sup_{\mathcal C_N}\frac{d_2}{d}.
$$

The same estimates hold when the collection is enlarged to all finite abelian covers. Bounds for an empty collection are not asserted.

<a id="cor-truncated"></a>

**Corollary 12** (Explicit truncated bounds). For a nonempty collection,

<a id="eq-truncated"></a>

$$
\boxed{\max\{N^{-2/3},\ c_-N^{-1/2}\}\le\gamma_-(N),\qquad
 \Gamma(N)\le c_+\sqrt N,}
$$

where

$$
c_-=\frac{\pi3^{1/6}}{2^{13/3}}\simeq0.1871573,
 \qquad c_+=2^{3/2}C_0^{2/3}\simeq9.5203204.
$$

The counterexamples also give

$$
\Gamma(N)\ge\frac73\quad(N\ge78),\qquad
 \gamma_-(N)\le\frac67\quad(N\ge156).
$$

Proof. From $d\le4d_2^3$,

$$
\frac{d_2}{d}\ge4^{-1/3}d^{-2/3}.
$$

Use $d\le n/2$ for the $n^{-2/3}$ bound, or $d\le C_0n^{3/4}$ for the $c_-n^{-1/2}$ bound. For amplification, apply the ambient estimate to the length-$2n$ cover and put $K_0=2^{3/4}C_0$. Then

$$
\frac{d_2}{d}\le\min\{8d^2,\ K_0n^{3/4}/d\}
 \le(8d^2)^{1/3}(K_0n^{3/4}/d)^{2/3}
 =c_+\sqrt n.
$$

Take the infimum or supremum with $n\le N$. The opposite inequalities follow from the explicit base lengths of Theorem [1](01-counterexamples.md#thm-examples). ◻

The exact expression for $c_+$, not its printed decimal, defines the constant. The size threshold $N\ge156$ for the degradation example follows from the now-available finite certificate; it does not require an inherited infinite-family threshold.

Combining the preceding theorems gives a fully explicit size-aware answer in the notation $d_{\rm lower}\le d_2\le d_{\rm upper}$:

<a id="eq-dlower"></a>
<a id="eq-dupper"></a>

$$
\begin{aligned}
 d_{\rm lower}(d)&=2\left\lceil \frac{(d/4)^{1/3}}2\right\rceil,\\
 d_{\rm upper}(d,n)&=2\left\lfloor \frac{\min\{8d^3,n,C_0(2n)^{3/4}\}}2\right\rfloor.
 
\end{aligned}
$$

When $k_2=2k$, also take the minimum with $2d$ in [\[eq:dupper\]](04-size-bounds.md#eq-dupper). None of these formulas claims an optimal constant or exponent. In particular [\[eq:truncated\]](04-size-bounds.md#eq-truncated) is not a two-sided asymptotic equivalence for either extremal function, and it does not prove bounded $\sup d_2/d$ or a positive $\inf d_2/d$ independent of size.
