[全部研究结果](../README.md) · [逐项结论](../CLAIMS.md) · [原始完整文本](../../research/homology/H01-bockstein-and-deck-structure.md)

> 完整研究笔记的 GitHub 阅读版；仅调整数学分隔符、引用标记与链接。历史状态、限制和证明内容均保留。当前结论以总登记表中的逐项状态为准；这里的“验证”不等于独立同行评审。

> 历史研究报告：初稿中尚未解决的距离猜想已被 H03/H05 的精确反例推翻；报告中的候选引理与最终定理须分开阅读。有关 Bockstein 的四重厚化证明适用于文中规定的矩形周期覆盖，不自动推广到任意覆盖。旧附件链接只在可确认对应材料时重定向；文中的 current/latest 指历史撰写时点，不表示本次做了最新文献排查。原文件引用标记转换为参考文献中的 supplied v3。

# Research outcome

I did **not** obtain a complete proof of


$$
d\le d_2\le 2d
$$


and I did not find a counterexample to it.

I did obtain a characteristic-two structure theorem that substantially sharpens the paper’s projection/lifting analysis:

> **For every valid BB double cover, the connecting homomorphisms form an actual Bockstein complex**
> 

$$
> H_2(Q)\xrightarrow{\beta_2}H_1(Q)\xrightarrow{\beta_1}H_0(Q),
> \qquad
> \beta_1\beta_2=0.
>
$$


> Consequently, every base logical killed by the full-fibre lift is nevertheless in the image of projection from the cover.

This gives an exact formula for $k_2$, a complete description of the non-semisimple deck action on logical homology, and a much narrower formulation of the two unresolved metric obstructions.

I also found exact BB examples disproving several natural intermediate lemmas. One especially useful example is


$$
[[30,4,4]]\longrightarrow [[60,4,6]],
$$


in which **every minimum base logical has trivial full-fibre lift, and no minimum logical has a weight-preserving one-sheet lift**. Thus neither of the two most obvious proofs of $d_2\le 2d$ can work separately or as a simple dichotomy.

The attached v3 is still the current source formulation I used. It defines the BB chain complex, the covering conditions, the maps $p,\tau$, proves $k_2\ge k$, and leaves even covers as Conjecture 1. [SRB, supplied v3](../REFERENCES.md#ref-SRB) A current arXiv check did not reveal a later proof. A recent semisimple BB analysis also emphasizes that covering conditions do not automatically preserve distance certificates and identifies the non-semisimple setting as an open direction. ([arxiv.org](https://arxiv.org/html/2511.13560v3))

---

## 1. Exact chain-complex formulation

Let


$$
R=\frac{\mathbb F_2[x,y]}
        {(x^\ell-1,\;y^m-1)}.
$$


The monomial basis is


$$
\{x^ay^b:0\le a<\ell,\;0\le b<m\}.
$$


There is a harmless indexing typo in the displayed basis in Equation (9) of the paper, where the displayed $\ell,m$ bounds are interchanged. All subsequent constructions use $x$-exponents modulo $\ell$ and $y$-exponents modulo $m$.

The BB chain complex is the Koszul complex


$$
C=C(A,B):
\qquad
0\longrightarrow R
\xrightarrow{\partial_2}
R^2
\xrightarrow{\partial_1}
R
\longrightarrow0,
$$


where


$$
\partial_2(h)=(Bh,Ah),
\qquad
\partial_1(u,v)=Au+Bv.
$$


Because $R$ is commutative and the characteristic is two,


$$
\partial_1\partial_2(h)=ABh+BAh=0.
$$



As an $\mathbb F_2$-complex this is


$$
0\longrightarrow \mathbb F_2^{\ell m}
\xrightarrow{\binom BA}
\mathbb F_2^{2\ell m}
\xrightarrow{(A\ B)}
\mathbb F_2^{\ell m}
\longrightarrow0.
$$



The $Z$-logical space is


$$
H_1(C)=
\frac{\{(u,v):Au+Bv=0\}}
     {\{(Bh,Ah):h\in R\}}.
$$


Its dimension is $k$. The $X$-logical space is the first cohomology of the dual complex.

The other two homology groups are


$$
H_2(C)=\operatorname{ann}_R(A,B)
      =\{h:Ah=Bh=0\},
$$


and


$$
H_0(C)=R/(A,B).
$$


For a BB complex,


$$
\dim H_2(C)=\dim H_0(C)=\frac{k}{2}.
$$



The inversion involution


$$
f^\star(x,y)=f(x^{-1},y^{-1})
$$


gives a weight-preserving isomorphism from $Z$-logicals to $X$-logicals:


$$
J[(u,v)]=[(v^\star,u^\star)].
$$


This is the elementary reason for


$$
d_X=d_Z=d
$$


for BB codes.

Everything below is written for the $x$-double cover. The $y$-double cover is obtained by interchanging $x,\ell$ with $y,m$.

---

## 2. The characteristic-two short exact sequence

For an $x$-double cover, put


$$
\widetilde R=
\frac{\mathbb F_2[x,y]}
     {(x^{2\ell}-1,\;y^m-1)}.
$$


Set


$$
t=1+x^\ell.
$$


Over $\mathbb F_2$,


$$
x^{2\ell}-1=(x^\ell-1)^2=t^2,
$$


so


$$
t^2=0\qquad\text{in }\widetilde R.
$$



The natural projection


$$
p:\widetilde R\longrightarrow R
$$


is reduction of the $x$-exponent modulo $\ell$.

Define


$$
\tau:R\longrightarrow\widetilde R,
\qquad
\tau(r)=t\widehat r,
$$


where $\widehat r$ is any lift of $r$ to $\widetilde R$. This is well-defined: two lifts differ by $ts$, and


$$
t(\widehat r+ts)=t\widehat r+t^2s=t\widehat r.
$$



In the two-sheet basis,


$$
\tau(r)=(r,r),
\qquad
p(r_0,r_1)=r_0+r_1.
$$



Therefore


$$
0\longrightarrow R
\xrightarrow{\tau}
\widetilde R
\xrightarrow{p}
R
\longrightarrow0
$$


is exact.

The assumptions of Theorem 3.1 imply


$$
p(\widetilde A)=A,\qquad p(\widetilde B)=B.
$$


Moreover,


$$
\widetilde A\,\tau(r)=\tau(Ar),
\qquad
\widetilde B\,\tau(r)=\tau(Br).
$$


Thus we obtain a short exact sequence of chain complexes


$$
0\longrightarrow C
\xrightarrow{\tau_\bullet}
\widetilde C
\xrightarrow{p_\bullet}
C
\longrightarrow0,
\tag{2.1}
$$


where at degree one the maps are $\tau\oplus\tau$ and $p\oplus p$.

This is the exact-sequence structure hidden behind Lemma 4.4. The relation


$$
p\tau=0
$$


is only one part of it.

Let $T$ denote the deck transformation


$$
T(f)=x^\ell f.
$$


Then at chain level


$$
I+T=\tau p.
\tag{2.2}
$$


Hence the deck algebra is


$$
\mathbb F_2[C_2]
 \cong \mathbb F_2[\varepsilon]/(\varepsilon^2),
\qquad
\varepsilon=I+T.
$$


There is no plus/minus eigenspace decomposition.

---

## 3. The Bockstein theorem

The long exact homology sequence associated to (2.1) contains


$$
H_2(C)\xrightarrow{\beta_2}H_1(C)
\xrightarrow{\tau_*}H_1(\widetilde C)
\xrightarrow{p_*}H_1(C)
\xrightarrow{\beta_1}H_0(C).
\tag{3.1}
$$



Exactness immediately gives


$$
\ker\tau_*=\operatorname{im}\beta_2,
\tag{3.2}
$$




$$
\ker p_*=\operatorname{im}\tau_*,
\tag{3.3}
$$


and


$$
\operatorname{im}p_*=\ker\beta_1.
\tag{3.4}
$$



The key additional fact is the following.

### Theorem 3.1 — Bockstein square-zero theorem

For every valid binary BB double cover, in either orientation,


$$
\boxed{\beta_1\beta_2=0.}
\tag{3.5}
$$



#### Proof

I give the $x$-orientation proof.

Consider the fourfold coefficient ring


$$
R^{(4)}
=
\frac{\mathbb F_2[x,y]}
     {(x^{4\ell}-1,\;y^m-1)}.
$$


Since


$$
x^{4\ell}-1=(x^\ell-1)^4=t^4,
$$


this is the $t^4=0$ thickening of the base ring.

Use exactly the same integer representatives of the monomials of
$\widetilde A,\widetilde B$, now interpreted modulo $4\ell$, to define


$$
C^{(4)}=C(A^{(4)},B^{(4)})
$$


over $R^{(4)}$. Reducing modulo $t^2$ gives the original double-cover complex $\widetilde C$, while reducing modulo $t$ gives $C$.

Filter $C^{(4)}$ by


$$
F^jC^{(4)}=t^jC^{(4)},
\qquad 0\le j\le4.
$$


Each associated graded piece


$$
F^j/F^{j+1}
$$


is naturally a copy of the base complex $C$.

Choose $t$-adic bases. Because all the differentials commute with multiplication by $t$, their block matrices are lower triangular and Toeplitz:


$$
\widehat\partial_i=
\begin{pmatrix}
\partial_i&0&0&0\\
D_i&\partial_i&0&0\\
E_i&D_i&\partial_i&0\\
F_i&E_i&D_i&\partial_i
\end{pmatrix}.
\tag{3.6}
$$


The reduction modulo $t^2$ is


$$
\widetilde\partial_i=
\begin{pmatrix}
\partial_i&0\\
D_i&\partial_i
\end{pmatrix}.
\tag{3.7}
$$



For a base cycle $z$, the connecting homomorphism is


$$
\beta_i[z]=[D_i z].
\tag{3.8}
$$



The first subdiagonal of


$$
\widehat\partial_{i-1}\widehat\partial_i=0
$$


gives


$$
D_{i-1}\partial_i+\partial_{i-1}D_i=0,
\tag{3.9}
$$


so $D_i$ indeed induces a map on homology.

The second subdiagonal gives


$$
E_{i-1}\partial_i
+D_{i-1}D_i
+\partial_{i-1}E_i
=0.
\tag{3.10}
$$


If $\partial_i z=0$, then


$$
D_{i-1}D_i z=\partial_{i-1}(E_i z).
$$


Thus $D_{i-1}D_i z$ is a boundary, proving


$$
\beta_{i-1}\beta_i=0.
$$


In particular,


$$
\beta_1\beta_2=0.
\qquad\square
$$



The same proof uses $t=1+y^m$ for a $y$-double cover.

---

## 4. Consequences for $k_2$ and the deck action

Let


$$
q=\dim H_2(C)=\frac{k}{2},
\qquad
r_i=\operatorname{rank}\beta_i.
$$



At the left end of the long exact sequence,


$$
0\longrightarrow H_2(C)
\longrightarrow H_2(\widetilde C)
\longrightarrow\ker\beta_2
\longrightarrow0.
$$


Hence


$$
\dim H_2(\widetilde C)
=q+(q-r_2)=2q-r_2.
$$


Since a BB code satisfies


$$
k_2=2\dim H_2(\widetilde C),
$$


we get


$$
k_2=2k-2r_2.
\tag{4.1}
$$



At degree one, exactness gives


$$
0\longrightarrow
H_1(C)/\operatorname{im}\beta_2
\longrightarrow
H_1(\widetilde C)
\longrightarrow
\ker\beta_1
\longrightarrow0.
\tag{4.2}
$$


Therefore


$$
k_2=(k-r_2)+(k-r_1).
\tag{4.3}
$$


Comparing (4.1) and (4.3) yields


$$
r_1=r_2=:r.
$$



Because $\beta_1\beta_2=0$,


$$
\operatorname{im}\beta_2\subseteq\ker\beta_1.
$$


Consequently


$$
r\le k-r,
\qquad r\le\frac{k}{2}.
$$



We obtain:

### Corollary 4.1 — exact dimension formula

For every valid BB double cover,


$$
\boxed{k_2=2k-2r,\qquad 0\le r\le\frac{k}{2}.}
\tag{4.4}
$$


In particular,


$$
\boxed{k\le k_2\le2k.}
\tag{4.5}
$$



Moreover,


$$
\boxed{
k_2-k
=
\dim\frac{\ker\beta_1}{\operatorname{im}\beta_2}.
}
\tag{4.6}
$$


Thus the number of new logical qubits is exactly the middle homology dimension of the Bockstein complex


$$
H_2(C)\xrightarrow{\beta_2}H_1(C)
\xrightarrow{\beta_1}H_0(C).
$$



This supplies a double-cover-specific homological proof of $k_2\ge k$, independent of the quotient-ring proof in Theorem 4.6.

### Corollary 4.2 — killed logicals are projectable

From (3.2), (3.4), and $\beta_1\beta_2=0$,


$$
\boxed{
\ker\tau_*
=\operatorname{im}\beta_2
\subseteq
\ker\beta_1
=\operatorname{im}p_*.
}
\tag{4.7}
$$



So although a base logical can die under full-fibre lifting, it is then guaranteed to be the projection of some cover logical.

This is a genuine characteristic-two replacement for the odd-cover identity $p\tau=I$.

### Corollary 4.3 — the case $k_2=k$

If $k_2=k$, then $r=k/2$, and therefore


$$
\boxed{
\ker\tau_*
=
\operatorname{im}\beta_2
=
\ker\beta_1
=
\operatorname{im}p_*.
}
\tag{4.8}
$$


Furthermore, $\beta_2$ is injective and $\beta_1$ is surjective.

Thus, in the important $k_2=k$ examples, exactly half of the base logical space is killed by transfer and exactly that same half is reached by projection.

### Corollary 4.4 — non-semisimple Jordan structure

Let


$$
N=T_*+I
$$


on $H_1(\widetilde C)$. By (2.2),


$$
N=\tau_*p_*,
\qquad N^2=0.
$$


Using (4.7),


$$
\begin{aligned}
\operatorname{rank}N
&=\dim\ker\beta_1-\dim\operatorname{im}\beta_2\\
&=(k-r)-r\\
&=k-2r\\
&=k_2-k.
\end{aligned}
\tag{4.9}
$$



Therefore, as a module over


$$
D=\mathbb F_2[\varepsilon]/(\varepsilon^2),
$$


the cover logical space has the decomposition


$$
\boxed{
H_1(\widetilde C)
\cong
D^{\,k_2-k}
\oplus
\mathbb F_2^{\,2k-k_2}.
}
\tag{4.10}
$$



In particular:

- if $k_2=k$, the deck transformation acts as the identity on logical homology;
- if $k_2=2k$, the logical space is a free $D$-module of rank $k$.

This is the correct substitute for a nonexistent plus/minus eigenspace decomposition.

---

## 5. Logical $X$-$Z$ pairing

For physical binary vectors, the projection and transfer are transposes:


$$
\tau=p^T.
$$


Consequently, for a base $X$-operator $x$ and a cover $Z$-operator $\widetilde z$,


$$
\langle\tau x,\widetilde z\rangle
=
\langle x,p\widetilde z\rangle.
\tag{5.1}
$$


This descends to the perfect pairing of logical spaces:


$$
\boxed{
\langle\tau_*[x],[\widetilde z]\rangle
=
\langle[x],p_*[\widetilde z]\rangle.
}
\tag{5.2}
$$



Thus


$$
\ker\tau_Z
=
(\operatorname{im}p_X)^\perp,
\qquad
\ker\tau_X
=
(\operatorname{im}p_Z)^\perp.
\tag{5.3}
$$



This gives a useful certification criterion:

> A full lift $\tau_Z[z]$ is nontrivial precisely when some cover $X$-logical has projection pairing nontrivially with $z$.

What does not work is pairing two full lifts:


$$
\langle\tau x,\tau z\rangle
=
\langle x,p\tau z\rangle
=0.
\tag{5.4}
$$


Even if $x,z$ anticommute downstairs, their full lifts commute upstairs.

The BB involution $J$ gives the alternating form


$$
\omega((u,v),(u',v'))
=
\operatorname{ct}(uv'+vu'),
\tag{5.5}
$$


where $\operatorname{ct}$ denotes the coefficient of the identity monomial. It is nondegenerate on logical homology. Nevertheless, minimum-weight vectors need not contain an anticommuting minimum-weight pair; an explicit example appears below.

So pairing is excellent for certifying a proposed lift but does not by itself prove that a minimum logical survives.

---

## 6. The exact metric normal form

The previous results settle the algebraic part. The remaining obstruction is entirely metric.

Write a cover vector in two-sheet coordinates as


$$
(c_0,c_1).
$$


Introduce


$$
q=c_0+c_1,\qquad r=c_1.
$$


Then


$$
(c_0,c_1)=(q+r,r),
\qquad
p(c_0,c_1)=q.
$$



The physical Hamming weight is


$$
\boxed{
|(c_0,c_1)|
=
|q+r|+|r|
=
|q|+2\,|\operatorname{supp}(r)\setminus\operatorname{supp}(q)|.
}
\tag{6.1}
$$



In these coordinates, the cover differential has the triangular form


$$
\boxed{
\widetilde\partial_i(q,r)
=
\bigl(\partial_iq,\;D_iq+\partial_ir\bigr).
}
\tag{6.2}
$$



This is the precise version of the non-semisimple $D$-module normal form.

---

## 7. Exact reduction of the upper bound

Let $z$ be a minimum-weight base $Z$-logical:


$$
\partial_1z=0,\qquad [z]\ne0,\qquad |z|=d.
$$



There are two cases.

### Case 1: the full lift survives

If


$$
[z]\notin\operatorname{im}\beta_2,
$$


then $\tau_*[z]\ne0$. Its representative is


$$
(q,r)=(0,z),
$$


which is physically $(z,z)$, of weight $2d$. Hence


$$
d_2\le2d.
$$



### Case 2: the full lift dies

Suppose


$$
[z]\in\operatorname{im}\beta_2.
$$


The Bockstein theorem gives


$$
[z]\in\ker\beta_1.
$$


Therefore


$$
D_1z\in\operatorname{im}\partial_1.
$$


Choose $r\in C_1$ satisfying


$$
\partial_1r=D_1z.
\tag{7.1}
$$


Then


$$
(z,r)
$$


is a cover cycle. Its projection is $z$, so it is automatically a nontrivial cover logical.

By (6.1), its weight is


$$
d+2\,|\operatorname{supp}(r)\setminus\operatorname{supp}(z)|.
$$



Define the support-correction radius


$$
\rho(z)=
\min_{\partial_1r=D_1z}
|\operatorname{supp}(r)\setminus\operatorname{supp}(z)|.
\tag{7.2}
$$


Then


$$
\boxed{
d_2\le d+2\rho(z).
}
\tag{7.3}
$$



Thus the entire upper-bound conjecture reduces to the following concrete statement:

> **Support-Bockstein lemma.**
> For at least one weight-$d$ logical $z$,
> either
> 

$$
> [z]\notin\operatorname{im}\beta_2,
>
$$


> or
> 

$$
> \rho(z)\le \frac d2.
> \tag{7.4}
>
$$



This is now a classical, support-restricted syndrome-decoding statement for the operator $D_1$. It is much more specific than the original homological conjecture.

The stronger claim $\rho(z)=0$ is false.

---

## 8. Exact reduction of the lower bound

Let


$$
\widetilde z=(q,r)
$$


be a nontrivial cover $Z$-logical.

The first component of (6.2) gives


$$
\partial_1q=0.
$$



If $[q]\ne0$ in base homology, then


$$
|\widetilde z|\ge|q|\ge d.
$$


So the only difficult case is


$$
[q]=0.
$$



Write


$$
q=\partial_2s.
$$


Set


$$
a=r+D_2s.
\tag{8.1}
$$


Using


$$
D_1\partial_2+\partial_1D_2=0
$$


and the cover-cycle equation


$$
D_1q+\partial_1r=0,
$$


we get


$$
\partial_1a=0.
$$



Subtracting the cover boundary


$$
\widetilde\partial_2(s,0)
=
(\partial_2s,D_2s)
$$


turns $(q,r)$ into


$$
(0,a)=\tau(a).
$$


Therefore


$$
[\widetilde z]=\tau_*[a].
$$


Because $\widetilde z$ is nontrivial,


$$
[a]\notin\operatorname{im}\beta_2.
$$



Every representative of the transfer class $\tau_*[a]$ can be written, after absorbing an ordinary base boundary into $a'\in[a]$, as


$$
(q,r)=
\bigl(\partial_2s,\;a'+D_2s\bigr).
$$


Its two physical sheets are


$$
a'+(D_2+\partial_2)s,
\qquad
a'+D_2s.
$$



Define


$$
\Lambda([a])
=
\min_{\substack{a'\in[a]\\s\in C_2}}
\left(
|a'+D_2s|
+
|a'+(D_2+\partial_2)s|
\right).
\tag{8.2}
$$



Then the lower-bound conjecture is equivalent to


$$
\boxed{
\Lambda([a])\ge d
\quad
\text{for every }
[a]\notin\operatorname{im}\beta_2.
}
\tag{8.3}
$$



This is the unresolved transfer-sector inequality. It is exactly where a minimum-weight or cleaning argument must operate. The ordinary homological exact sequence gives no control over the two terms in (8.2).

---

## 9. Polynomial and voltage interpretations

Choose the low-sheet vector-space section


$$
s:R\to\widetilde R.
$$


For $f\in R$, define a Bockstein derivative $\nabla_f$ by


$$
\widetilde f\,s(g)
=
s(fg)+t\,s(\nabla_f g).
\tag{9.1}
$$


Then


$$
D_1(u,v)=\nabla_Au+\nabla_Bv,
\tag{9.2}
$$


and


$$
D_2(h)=(\nabla_Bh,\nabla_Ah).
\tag{9.3}
$$



If the doubled base period is odd, the group extension splits, and one can choose a multiplicative section. In that case $\nabla_A,\nabla_B$ are simply multiplication by the voltage parts of $\widetilde A,\widetilde B$.

If the base period is even, there is an additional carry cocycle. Consequently, $\nabla_A$ and $\nabla_B$ need not themselves be multiplication by elements of $R$. This is why writing


$$
\widetilde R\stackrel?=R\otimes
\mathbb F_2[\varepsilon]/(\varepsilon^2)
$$


without keeping track of the nonsplit group extension can give incorrect formulas.

In graph-cover language, after ordering by sheets, every lifted multiplication matrix has the form


$$
\widetilde M=
\begin{pmatrix}
M_0&M_1\\
M_1&M_0
\end{pmatrix},
\qquad
M=M_0+M_1.
\tag{9.4}
$$


The fibrewise CNOT/Gray transformation changes this to


$$
\begin{pmatrix}
M&0\\
D_M&M
\end{pmatrix}.
\tag{9.5}
$$


This is triangular, not diagonal. A true two-sheet decomposition occurs only when the voltage assignment is switching-equivalent to zero, in which case the cover is two disconnected copies and


$$
d_2=d.
$$



The ideal formulation


$$
H_2=\operatorname{ann}(A,B),\qquad
H_0=R/(A,B)
$$


completely controls dimensions and the endpoints of the Bockstein complex. It does not control the support minimizations $\rho$ and $\Lambda$. That is the precise limitation of a pure ideal/annihilator argument.

---

# 10. Exact counterexamples to tempting intermediate claims

## 10.1 A minimum logical can have trivial full-fibre lift

Take


$$
\ell=2,\qquad m=3,
$$


and


$$
A=1+y+y^2,
\qquad
B=1+y+xy^2.
$$


This is a


$$
[[12,4,2]]
$$


BB code.

Take the $x$-double cover with period $4$ and unchanged polynomials


$$
\widetilde A=A,\qquad \widetilde B=B.
$$


It has parameters


$$
[[24,4,2]].
$$



Consider


$$
z=(1+y,0).
$$


It is a base $Z$-logical. For example,


$$
x=((1+x)(1+y^2),0)
$$


is an $X$-cycle and has odd overlap with $z$, so both are nontrivial logical operators.

Let


$$
t=1+x^2
$$


and


$$
h=(1+x)(y+y^2).
$$


Direct multiplication in the cover ring gives


$$
Ah=0,
$$


and


$$
Bh=t(1+y).
$$


Therefore


$$
\widetilde\partial_2(h)
=
(Bh,Ah)
=
(t(1+y),0)
=
\tau(z).
$$


So


$$
\tau_*[z]=0.
$$



Translations give all six weight-two representatives of the minimum logical classes, and all their full-fibre lifts are boundaries.

Nevertheless, $z$ placed on one sheet is itself a cover cycle, and its projection is the nontrivial base logical $z$. Thus it is nontrivial upstairs and


$$
d_2=d=2.
$$



This disproves:



$$
\text{“At least one minimum base logical always survives full lifting.”}
$$



---

## 10.2 A minimum BB logical need not be one-block

Take


$$
\ell=1,\qquad m=6,
$$


and


$$
A=B=1+y+y^2.
$$


The resulting code has


$$
[[12,4,2]].
$$



The mixed operator


$$
z=(1,1)
$$


is a cycle because


$$
A\cdot1+B\cdot1=0.
$$


It is not a boundary: every boundary has the form


$$
(Ar,Ar),
$$


and $1\notin(A)$.

Thus $d=2$.

A pure left-block cycle $(u,0)$ requires


$$
Au=0.
$$


Since


$$
y^6-1=(y+1)^2(1+y+y^2)^2,
$$


the annihilator of $A$ is generated by


$$
\frac{y^6-1}{A}
=(y+1)^2A
=1+y+y^3+y^4.
$$


Its three nonzero words all have weight four. Consequently, the minimum pure one-block logical weight is four, while the code distance is two.

This disproves:



$$
\text{“A minimum BB logical can always be chosen on one block.”}
$$



It also disproves a natural pairing lemma. All weight-two $Z$-logicals are


$$
(y^i,y^i),
$$


and all weight-two $X$-logicals obtained through $J$ have the same form. Any two such operators overlap in either zero or two positions. Hence no minimum $Z$-logical has a minimum $X$-logical anticommuting partner.

---

## 10.3 Full transfer or weight-preserving lift is not a valid dichotomy

Take the base ring with


$$
\ell=5,\qquad m=3,
$$


and


$$
A=x^2+xy+xy^2,
$$




$$
B=x^4+x^4y+x^3y^2.
$$


Exact row reduction and support enumeration give


$$
Q=[[30,4,4]].
$$



Consider the $x$-double cover


$$
\widetilde\ell=10,\qquad\widetilde m=3
$$


with


$$
\widetilde A=x^7+xy^2+x^6y,
$$




$$
\widetilde B=x^9+x^4y+x^8y^2.
$$


Reducing exponents modulo $5$ recovers $A,B$, so this is a valid Theorem 3.1 double cover.

Let


$$
z=(1+y,\;x^3y+x^3y^2).
\tag{10.1}
$$


It is a minimum base logical of weight four.

The base parity-check matrix has no nonzero cycles of weights one, two, or three. At weight four it has exactly 15 cycles, all translates of $z$, and none is a stabilizer. This certifies $d=4$.

Now define


$$
\begin{aligned}
h={}&1+y^2+x^2+x^2y+x^3y+x^3y^2+x^4+x^4y\\
&+x^5y+x^5y^2+x^6+x^6y+x^8+x^8y^2.
\end{aligned}
$$


Direct multiplication gives


$$
\widetilde B h
=
(1+x^5)(1+y),
$$


and


$$
\widetilde A h
=
(1+x^5)(x^3y+x^3y^2).
$$


Therefore


$$
\widetilde\partial_2(h)=\tau(z).
$$


All translates of $z$ also have trivial full-fibre lift.

Now try to lift $z$ by choosing one element of each fibre. Let $s_1,s_2,s_3,s_4\in\mathbb F_2$ be the sheet choices for


$$
1_L,\quad y_L,\quad (x^3y)_R,\quad(x^3y^2)_R.
$$


Two of the cover-cycle equations, coming from the check fibres over $x$ and $x^2y$, are


$$
s_2+s_3=0
$$


and


$$
s_2+s_3=1.
$$


Hence no weight-preserving one-sheet lift of $z$ is a cycle.

Nevertheless, the support correction


$$
r=(y+y^2,0)
$$


solves


$$
\partial_1r=D_1z.
$$


The corresponding cover cycle is


$$
\widetilde z=
\left(
1+y^2+x^5y+x^5y^2,\;
x^3y+x^3y^2
\right).
\tag{10.2}
$$


It has weight six and projects to $z$, so it is nontrivial.

For the cover matrix, exact enumeration gives:



$$
\begin{array}{c|r|r}
w&\binom{60}{w}&\text{number of }Z\text{-cycles}\\ \hline
1&60&0\\
2&1770&0\\
3&34220&0\\
4&487635&0\\
5&5461512&0
\end{array}
$$


Together with (10.2), this proves


$$
\widetilde Q=[[60,4,6]].
$$



Thus


$$
4<6<8,
$$


but every minimum base logical has a trivial full transfer and no weight-preserving lift.

This disproves the proposed dichotomy


$$
\text{“For some minimum logical, either the transfer survives or a one-sheet lift works.”}
$$



For the logical $z$ above,


$$
\rho(z)=1,
$$


so the corrected lift has weight


$$
d+2\rho(z)=4+2=6.
$$



---

## 10.4 Exact sequence and logical pairing alone cannot prove the lower bound

The obstruction is not merely technical. There are regular double covers of general CSS complexes for which distance decreases.

For example, on five qubits take


$$
H_X=
\begin{pmatrix}
1&1&0&0&0\\
0&0&1&1&0
\end{pmatrix},
\qquad
H_Z=
\begin{pmatrix}
1&1&1&1&0\\
1&1&1&1&1
\end{pmatrix}.
$$


This is a


$$
[[5,1,2]]
$$


CSS code with $d_X=d_Z=2$.

Use the regular two-lift decompositions


$$
H_{X,0}=H_X,\qquad H_{X,1}=0,
$$


and


$$
H_{Z,0}=
\begin{pmatrix}
1&1&1&1&0\\
0&0&1&1&1
\end{pmatrix},
\qquad
H_{Z,1}=
\begin{pmatrix}
0&0&0&0&0\\
1&1&0&0&0
\end{pmatrix}.
$$


The lifted matrices are


$$
\widetilde H_\bullet=
\begin{pmatrix}
H_{\bullet,0}&H_{\bullet,1}\\
H_{\bullet,1}&H_{\bullet,0}
\end{pmatrix}.
$$


They commute, but the cover has


$$
d_Z=1,\qquad d_X=4.
$$



Taking the direct sum with the $X/Z$-swapped construction gives a base


$$
[[10,2,2]]
$$


code with an explicit $ZX$-duality, and a regular double cover


$$
[[20,4,1]].
$$



This is not a BB code. Its role is to prove that:

- the short exact sequence,
- square-zero deck algebra,
- perfect $X$-$Z$ pairing,
- equality $d_X=d_Z$ downstairs,
- and even a global $ZX$-duality

are still insufficient by themselves. Any proof of the BB lower bound must exploit the commutative Koszul/multiplication structure of $A,B$.

---

# 11. Exact finite searches

All searches below used exact binary arithmetic, not BP-OSD:

1. matrices were constructed as cyclic convolution matrices;
2. ranks and stabilizer membership were computed by Gaussian elimination over $\mathbb F_2$;
3. all supports up to the claimed weight were exhaustively enumerated.

For all standard trinomial BB codes with


$$
\ell m\le7
$$


and $k>0$, there are 454 base instances before quotienting by equivalences. I checked all $64$ monomial lift assignments in each orientation, for a total of


$$
58\,112
$$


valid oriented double covers.

All these bases have $d=2$, and every cover satisfied


$$
2\le d_2\le4.
$$


There were 4,272 all-minimum-transfer-killed lifts in each orientation; in every one of these small cases a weight-two one-sheet logical existed.

I also checked every oriented double lift of the standard


$$
[[36,8,4]]
$$


BB code. There was no cover logical of weight below four, and every lift had at least one minimum base logical whose full transfer survived, proving


$$
4\le d_2\le8
$$


for all those lifts.

The $[[30,4,4]]\to[[60,4,6]]$ example above is the first small case I found in which all minimum transfers die and all minimum weight-preserving lifts fail. It still obeys the conjecture through a one-pair support correction.

These searches do not prove the general statement, but they strongly distinguish the real obstruction from the false intermediate lemmas.

---

# 12. Requested final assessment

## 1. Strongest rigorous result obtained

For every valid binary BB double cover, in either orientation:



$$
0\to C\xrightarrow{\tau}\widetilde C\xrightarrow p C\to0
$$


is a short exact sequence of complexes whose connecting homomorphisms satisfy


$$
\boxed{\beta_1\beta_2=0.}
$$



Consequently,


$$
\boxed{
\ker\tau_*=\operatorname{im}\beta_2
\subseteq
\ker\beta_1=\operatorname{im}p_*.
}
$$



Thus every base logical killed by full lifting is projectable from the cover.

If $r=\operatorname{rank}\beta_2=\operatorname{rank}\beta_1$, then


$$
\boxed{k_2=2k-2r},
$$


so


$$
\boxed{k\le k_2\le2k},
$$


and


$$
\boxed{
k_2-k=
\dim\frac{\ker\beta_1}{\operatorname{im}\beta_2}.
}
$$



For the deck transformation $T$,


$$
\boxed{\operatorname{rank}(T_*+I)=k_2-k},
$$


and


$$
\boxed{
H_1(\widetilde C)
\cong
\left(\mathbb F_2[\varepsilon]/(\varepsilon^2)\right)^{k_2-k}
\oplus
\mathbb F_2^{\,2k-k_2}.
}
$$



I do not see this complete Bockstein/Jordan description stated in the attached paper, although I have not established bibliographic novelty.

## 2. Most promising proof route

The most promising route is the **support-controlled Bockstein route**.

For a minimum base logical $z$:

- if $[z]\notin\operatorname{im}\beta_2$, its transfer proves $d_2\le2d$;
- if $[z]\in\operatorname{im}\beta_2$, the square-zero theorem guarantees that $z$ lifts, and the optimal lifted weight is
  

$$
d+2\rho(z).
$$



Thus the upper bound reduces to proving that for at least one minimum logical,


$$
\boxed{\rho(z)\le d/2.}
$$



This is a support-restricted classical decoding statement on the base Tanner graph involving the explicitly computable Bockstein operator $D_1$. It is substantially more local and testable than the original distance conjecture.

The lower bound is isolated to the transfer sector and becomes


$$
\boxed{
\Lambda([a])\ge d
\quad\text{for all }[a]\notin\operatorname{im}\beta_2.
}
$$



## 3. Every unresolved gap

The unresolved upper-bound gap is proving, for a minimum logical killed by transfer, the existence of a solution


$$
\partial_1r=D_1z
$$


with at most $d/2$ support positions outside $\operatorname{supp}z$.

The unresolved lower-bound gap is proving


$$
|a'+D_2s|+
|a'+(D_2+\partial_2)s|
\ge d
$$


for every nonzero transfer class, every representative $a'$, and every $s$.

Neither ideal dimensions nor the long exact sequence control these support quantities.

Logical pairing only characterizes which classes die:


$$
\ker\tau_Z=(\operatorname{im}p_X)^\perp;
$$


it does not provide low-weight dual witnesses.

A cleaning proof would need a bounded-support filling theorem for small projected stabilizers. Ordinary cleaning can use a boundary with arbitrarily large support and therefore does not establish either metric inequality.

The carry part of $D_1,D_2$ for even base periods must be retained. Treating the cover as a split tensor product with $\mathbb F_2[\varepsilon]/(\varepsilon^2)$ loses precisely the terms that matter.

## 4. Intermediate conjectures disproved

The following are false:

1. Every minimum base logical has a nontrivial full-fibre lift.

2. At least one minimum base logical always survives full lifting.

3. If a minimum logical dies under full lifting, it has a weight-preserving one-sheet lift.

4. For some minimum logical, either the full transfer survives or a weight-preserving lift exists.

5. A minimum BB logical can always be chosen entirely on one qubit block.

6. Every minimum $Z$-logical has an anticommuting minimum $X$-logical partner.

7. A short exact sequence, square-zero deck action, and perfect logical pairing alone imply distance monotonicity for CSS double covers.

## 5. Single most valuable next mathematical step

Prove or refute the following sharply formulated lemma:

> **Support-Bockstein lemma for trinomial BB complexes.**
> Let $z$ be a minimum-weight base logical with
> 

$$
> [z]\in\operatorname{im}\beta_2.
>
$$


> Then there exists
> 

$$
> r\in C_1
>
$$


> satisfying
> 

$$
> \partial_1r=D_1z
>
$$


> and
> 

$$
> |\operatorname{supp}(r)\setminus\operatorname{supp}(z)|
> \le\frac{|z|}{2}.
>
$$



Its proof would establish


$$
d_2\le2d
$$


for every binary BB double cover. Its failure would provide an exceptionally focused search target for an upper-bound counterexample. The most promising first setting is the univariate/cyclic case $m=1$, where the first nontrivial $\rho=1,2$ examples already occur and where the syndrome equation can be attacked using cyclic-ideal and matroid methods.
