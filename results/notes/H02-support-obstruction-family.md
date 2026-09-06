[全部研究结果](../README.md) · [逐项结论](../CLAIMS.md) · [原始完整文本](../../research/homology/H02-support-obstruction-family.md)

> 完整研究笔记的 GitHub 阅读版；仅调整数学分隔符、引用标记与链接。历史状态、限制和证明内容均保留。当前结论以总登记表中的逐项状态为准；这里的“验证”不等于独立同行评审。

> 历史研究报告：初稿中尚未解决的距离猜想已被 H03/H05 的精确反例推翻；报告中的候选引理与最终定理须分开阅读。有关 Bockstein 的四重厚化证明适用于文中规定的矩形周期覆盖，不自动推广到任意覆盖。旧附件链接只在可确认对应材料时重定向；文中的 current/latest 指历史撰写时点，不表示本次做了最新文献排查。原文件引用标记转换为参考文献中的 supplied v3。

The three foundational claims survive the audit. The support–Bockstein lemma does not.

In fact, there is an infinite family of valid trinomial BB double covers


$$
[[18j,4,4]]\longrightarrow [[36j,4,6]],\qquad j\ge2,
$$


for which **every minimum base logical is killed by full transfer**, and


$$
\boxed{\rho(z)=2j-1}
$$


for every minimum base logical $z$.

Thus the existential version of the proposed lemma also fails: there is no alternative minimum logical satisfying $\rho(z)\le d/2=2$. The failure is unbounded, and it occurs for both odd and even doubled base periods.

These are **not** counterexamples to the upper-bound conjecture: their cover distance is exactly $6$, while $2d=8$. A weight-six, non-minimum base logical supplies the required cover logical.

Below is the audit, the correction-and-gauge calculation, and a proof of this counterexample family.

## 1. Foundation audit

Write $\partial_i$ for boundary maps, reserving $d$ for distance. The complexes and covers used here are precisely the trinomial Koszul complexes and monomial-by-monomial covers of Equations (11)–(13) and Theorem 3.1 of the paper. [SRB, supplied v3](../REFERENCES.md#ref-SRB)

### The exact sequence is valid

For an $x$-double cover, put


$$
K=\mathbb F_2[y]/(y^m-1),\qquad t=x^\ell+1,
$$


and


$$
R=K[x]/(t),\qquad \widetilde R=K[x]/(t^2).
$$



The maps are


$$
p:\widetilde R\to R,\qquad p(f)=f\bmod t,
$$


and


$$
\tau:R\to\widetilde R,\qquad \tau(f)=t\widehat f.
$$


The latter is independent of the representative $\widehat f$, since $t^2=0$.

Because $t$ is monic in $x$, polynomial division works even though $K$ can have zero divisors. In particular,


$$
\ker p=t\widetilde R=\operatorname{im}\tau,
\qquad
\ker\tau=0.
$$



For every admissible lifted polynomial,


$$
p(\widetilde A)=A,\qquad p(\widetilde B)=B,
$$


and multiplication satisfies


$$
\widetilde A\,\tau(f)=\tau(Af),\qquad
\widetilde B\,\tau(f)=\tau(Bf).
$$


Hence


$$
\boxed{0\longrightarrow C\xrightarrow{\tau}\widetilde C\xrightarrow p C\longrightarrow0}
$$


is a short exact sequence of $\mathbb F_2$-chain complexes.

This does not equip $\widetilde R$ with an unjustified $R$-algebra structure.

### The triangular form, with the carry included

Choose the section consisting of representatives of $x$-degree below $\ell$. Every cover chain has a unique expression


$$
\widehat q+t\widehat r.
$$


Its physical sheets are


$$
(q+r,r).
$$



Write a lifted multiplication matrix, in this basis, as


$$
M_{\widetilde f}(t)=M_f+tD_f+t^2E_f.
$$


The coefficient $E_f$ is visible in a higher thickening, although it vanishes upon reduction modulo $t^2$.

There is an explicit formula. Write


$$
\widetilde f=f+t\alpha,
$$


where $f,\alpha$ have $x$-degree below $\ell$, and define the carry operator $C_f$ by


$$
f\widehat u=\widehat{fu}+t\,\widehat{C_fu}.
$$


Then


$$
\boxed{D_f=C_f+M_\alpha,\qquad E_f=C_\alpha.}
\tag{1}
$$



Equivalently, for a lifted monomial


$$
x^{a+\ell v}y^b,\qquad 0\le a<\ell,\quad v\in\{0,1\},
$$


acting on $x^cy^e$, put


$$
\kappa=\left\lfloor\frac{a+c}{\ell}\right\rfloor\in\{0,1\}.
$$


The output monomial is $x^{a+c\bmod\ell}y^{b+e\bmod m}$, with coefficients


$$
M_f:\ 1,\qquad
D_f:\ v+\kappa,\qquad
E_f:\ v\kappa.
\tag{2}
$$


Thus the carry is retained explicitly.

For the Koszul maps,


$$
D_1=(D_A\ D_B),\qquad
D_2=\binom{D_B}{D_A},
$$


and similarly for $E_1,E_2$. Reduction modulo $t^2$ gives


$$
\boxed{
\widetilde\partial_i(q,r)
=
(\partial_iq,\ D_iq+\partial_ir).
}
\tag{3}
$$


Consequently,


$$
\boxed{
|\widetilde z|
=
|q+r|+|r|
=
|q|+2|\operatorname{supp}(r)\setminus\operatorname{supp}(q)|.
}
\tag{4}
$$



### The $t^4$ argument survives—and can be strengthened

The essential justification is module-theoretic. The ring $K[x]$ is free over $K[t]$, with basis


$$
1,x,\ldots,x^{\ell-1},
\qquad t=x^\ell+1.
$$


This follows directly from division by the monic polynomial $x^\ell+1$. No ring decomposition
$\widetilde R=R\otimes\mathbb F_2[\epsilon]/(\epsilon^2)$
is being assumed.

Choose the lifted monomials with exponents below $2\ell$, and regard the same polynomials as elements of $K[x]$. Their multiplication matrices over $K[t]$ have degree at most two in $t$. The Koszul identity holds over this entire polynomial module:


$$
(\partial_1+tD_1+t^2E_1)
(\partial_2+tD_2+t^2E_2)=0.
$$


Its coefficients give


$$
\begin{aligned}
\partial_1\partial_2&=0,\\
\partial_1D_2+D_1\partial_2&=0,\\
\partial_1E_2+D_1D_2+E_1\partial_2&=0,\\
D_1E_2+E_1D_2&=0,\\
E_1E_2&=0.
\end{aligned}
\tag{5}
$$



The connecting maps are


$$
\beta_i[z]=[D_i z].
$$


For $h\in H_2(C)=\ker\partial_2$, Equation (5) gives


$$
D_1D_2h=\partial_1E_2h.
$$


Therefore


$$
\boxed{\beta_1\beta_2=0.}
\tag{6}
$$



Changing a lifted monomial representative by a multiple of $2\ell$ changes its fourfold lift, but not its reduction modulo $t^2$. Thus $\partial_i,D_i$ are unchanged; the higher coefficients still satisfy the relevant coefficient identities. The proof applies to every admissible double cover, not merely a preferred choice of fourfold representatives.

For odd $\ell$, a multiplicative monomial section exists: modulo $2\ell$, it sends the base generator to $x^{\ell+1}$. In a compatible split fourfold presentation, one may choose $E_i=0$; then $D_1D_2=0$ already at chain level. For even $\ell$, formula (1) retains the nonzero carry terms.

For a $y$-double cover, interchange


$$
x,\ell\quad\text{with}\quad y,m,
$$


and use coefficient ring $\mathbb F_2[x]/(x^\ell-1)$. Every argument above remains valid.

## 2. The second-order correction and all its freedoms

Suppose


$$
z=D_2h+\partial_2s,\qquad \partial_2h=0.
$$


Then Equation (5) gives


$$
\begin{aligned}
D_1z
&=D_1D_2h+D_1\partial_2s\\
&=\partial_1E_2h+\partial_1D_2s.
\end{aligned}
$$


Thus the proposed correction is correct:


$$
\boxed{r_0=E_2h+D_2s,\qquad \partial_1r_0=D_1z.}
\tag{7}
$$



For fixed $z$, define


$$
\mathcal P_z
=
\{(h,s):\partial_2h=0,\ D_2h+\partial_2s=z\}.
$$


If $(h,s)\in\mathcal P_z$, every other pair has the form


$$
(h+g,s+u),
$$


where


$$
\partial_2g=0,\qquad D_2g+\partial_2u=0.
\tag{8}
$$


Equivalently, $g\in\ker\beta_2$, one chooses a filling $u$ of $D_2g$, and that filling is further adjustable by an arbitrary element of $H_2(C)$.

The resulting correction changes by


$$
E_2g+D_2u,
$$


which is a cycle by Equation (5). Allowing a $t^2v$ term in a higher lift also adds the boundary $\partial_2v$ to the correction.

There is an important distinction: these changes of higher-order data need not generate every possible correction. The complete solution space is


$$
\boxed{
\{r:\partial_1r=D_1z\}=r_0+\ker\partial_1.
}
\tag{9}
$$


Thus the exact optimization is


$$
\boxed{
\rho(z)
=
\min_{\substack{(h,s)\in\mathcal P_z\\c\in\ker\partial_1}}
\left|
\operatorname{supp}(E_2h+D_2s+c)\setminus\operatorname{supp}(z)
\right|.
}
\tag{10}
$$


After one pair $(h,s)$ is fixed, changing it becomes redundant if the full cycle freedom $c$ is retained.

Changing the physical section only switches choices within fibres. For a fixed projected chain $z$, this changes $r$ by a vector supported on $\operatorname{supp}z$, so it does not change $\rho(z)$.

### What minimum weight really implies

Let $S=\operatorname{supp}z$, with $|z|=d$, and define


$$
\sigma_S(v)=|v_{S^c}|-|v_S|.
$$


For every boundary $b$,


$$
\boxed{\sigma_S(b)\ge0.}
\tag{11}
$$


This is exactly the complete coset-leader condition:


$$
|z+b|-|z|=\sigma_S(b).
$$



It includes all support exchanges by sums of boundaries. For example,


$$
\sigma_S(b+c)
=
\sigma_S(b)+\sigma_S(c)-2\sigma_S(b\cap c)\ge0.
\tag{12}
$$


More generally, the corresponding inclusion–exclusion identity applies to any finite sum of boundaries.

Minimum logical weight gives a stronger structural fact: **$S$ is a circuit of the binary column matroid of $\partial_1$**. Indeed, a nonzero cycle supported on a proper subset of $S$ would either be a smaller logical, or be a boundary whose removal makes $z$ smaller. Therefore


$$
\boxed{\ker(\partial_1|_S)=\langle z\rangle,\qquad
\operatorname{rank}(\partial_1|_S)=d-1.}
\tag{13}
$$



For trinomial BB codes, each elementary boundary has weight six, so Equation (11) also gives the local condition


$$
|S\cap\operatorname{supp}(\partial_2e)|\le3.
$$



All these conditions hold in the counterexamples below. They cannot imply the proposed support bound.

## 3. An infinite counterexample family

### Theorem

For every integer $j\ge2$, put


$$
q=3j,\qquad L=3q=9j.
$$


Define the base code over


$$
R=\mathbb F_2[x]/(x^L+1)
$$


by


$$
A=1+x^{q-1}+x^{2q-2},
\qquad
B=1+x^{3q-2}+x^{3q-1}.
\tag{14}
$$


Define its $x$-double cover over


$$
\widetilde R=\mathbb F_2[x]/(x^{2L}+1)
$$


by


$$
\widetilde A=1+x^{q-1}+x^{5q-2},
\qquad
\widetilde B=B.
\tag{15}
$$



Then:



$$
\boxed{
Q=[[18j,4,4]],\qquad
\widetilde Q=[[36j,4,6]].
}
\tag{16}
$$



Every minimum $Z$-logical representative is a translate of


$$
z=(x+x^q,\ 1+x).
\tag{17}
$$


Every such representative is killed by full transfer, and


$$
\boxed{\rho(z)=2j-1.}
\tag{18}
$$



The corresponding statements hold for minimum $X$-logicals. In particular, every minimum logical fails the proposed bound


$$
\rho(z)\le d/2.
$$



### Validity and dimensions

The cover changes only the third monomial of $A$, adding exactly $L=3q$ to its exponent. Hence it satisfies Theorem 3.1.

Let


$$
g=1+x+x^2,\qquad F=x^{3q}+1.
$$


In the base ring,


$$
B=x^{-2}g,
$$


and $g\mid A$, because $q$ is divisible by three. Therefore


$$
\gcd(A,B,F)=g.
$$



For a cyclic Koszul complex,


$$
H_0\cong R/(A,B),\qquad
H_2=\left\langle\frac{F}{\gcd(A,B,F)}\right\rangle.
$$


Both have dimension $\deg g=2$. Euler characteristic then gives


$$
\dim H_1=4.
$$



For the cover, any common factor of $\widetilde A,\widetilde B,F^2$ must divide $g$. Moreover, $g$ occurs with multiplicity one in $\widetilde B$: its derivative is either $x^{L-2}$ or $x^{L-3}$, according to the parity of $L$, and is nonzero at both roots of $g$. Since $g\mid\widetilde A$,


$$
\gcd(\widetilde A,\widetilde B,F^2)=g.
$$


The cover also has $k_2=4$.

### The base distance is four

As ordinary polynomials,


$$
A(x+x^q)+B(1+x)=1+x^{3q}=F.
\tag{19}
$$


Thus $z$ is a cycle.

It is not a boundary: both coordinates of every boundary $(Bh,Ah)$ are divisible by $g$, whereas


$$
1+x\not\equiv0\pmod g.
$$



Every column of $(A\ B)$ has odd weight three, so every cycle has even weight. Its columns are distinct. Within each block this follows from the absence of a nontrivial translation symmetry of the three-term support. Between blocks, the cyclic gaps of the support of $A$ are


$$
q-1,\ q-1,\ q+2,
$$


whereas those of a translate of $B$ are


$$
1,\ 1,\ 3q-2.
$$


They cannot agree for $q\ge6$.

Hence there are no cycles of weight two, while $z$ is a nontrivial cycle of weight four:


$$
d_Z=4.
$$



### Every weight-four cycle is a translate of $z$

This classification is what rules out an alternative minimum logical.

Let $\mathbb F_4=\mathbb F_2(\omega)$, where


$$
\omega^2+\omega+1=0.
$$


Consider the ring map


$$
\Pi:R\longrightarrow
T:=\mathbb F_4[u]/(u^q-\omega),
\qquad x\longmapsto u.
\tag{20}
$$


It is well-defined because $u^{3q}=\omega^3=1$.

Every monomial has a unique form $x^{i+aq}$, with $0\le i<q$ and $a\in\{0,1,2\}$, and


$$
\Pi(x^{i+aq})=\omega^a u^i.
$$



Multiplying the check equation by $x^2$ and applying $\Pi$ gives


$$
\Pi(x^2A)=(u+1)(u+\omega^2),
\qquad
\Pi(x^2B)=(u+\omega)(u+\omega^2).
\tag{21}
$$


The factor $u+\omega^2$ is a unit in $T$, since


$$
(\omega^2)^q=1\ne\omega.
$$



Thus the projection $(U,V)$ of any base cycle satisfies


$$
(u+1)U+(u+\omega)V=0.
$$


Equivalently,


$$
\boxed{
U=(u+\omega)h,\qquad V=(u+1)h,
}
\tag{22}
$$


where one can take $h=\omega(U+V)$.

Write $h=\sum h_i u^i$. In coefficient form,


$$
U_i=\omega h_i+h_{i-1},\qquad
V_i=h_i+h_{i-1},
\tag{23}
$$


with the appropriate nonzero wrap factor $\omega$ at the cyclic boundary.

If exactly one of $h_i,h_{i-1}$ is nonzero, both $U_i,V_i$ are nonzero. If both are nonzero, at least one of $U_i,V_i$ is nonzero. Therefore a run of $a$ consecutive nonzero coefficients of $h$, bounded by zeros, contributes at least


$$
a+3
$$


to the $\mathbb F_4$-Hamming weight of $(U,V)$. If $h$ has full support, that weight is at least $q\ge6$.

Consequently, a nonzero projected pair of weight at most four must arise from


$$
h=\omega^a u^i,
$$


and has weight exactly four.

There is one other possibility to exclude: $\Pi$ could kill the entire physical vector. But for each coefficient position and block, the binary map


$$
(b_0,b_1,b_2)\longmapsto b_0+\omega b_1+\omega^2b_2
$$


has kernel $\{000,111\}$. A physical vector in the kernel therefore has weight divisible by three, and cannot have weight four.

Finally, a physical weight-four vector whose projection has weight four must use exactly one physical monomial for each nonzero projected coefficient. Equation (22) then reconstructs exactly


$$
x^a z,\qquad 0\le a<L.
$$



Thus **all** minimum representatives are translations of $z$.

### An explicit correction of weight $2j-1$

In the low-sheet normal form,


$$
\widetilde A=A+t\,x^{2q-2},\qquad t=1+x^{3q}.
$$


Equation (19) therefore gives


$$
D_1z=c,\qquad
c=1+x^{2q-1}+x^{3q-2}.
\tag{24}
$$



Define


$$
S_j=1+x^3+\cdots+x^{3(j-1)},
$$


and


$$
R_j
=
1+(1+x^{q+2})S_j
=
\sum_{a=1}^{j-1}x^{3a}
+
\sum_{a=0}^{j-1}x^{q+2+3a}.
\tag{25}
$$


Put


$$
r_*=(R_j,0).
$$



Here is a direct verification that it corrects the syndrome. Set $y=x^q$, so $y^3=1$. Then


$$
x^2A=x^2+xy+y^2
$$


and


$$
(x^2+xy+y^2)(1+x^2y)
=
(1+x^3)(xy+y^2).
$$


Since


$$
(1+x^3)S_j=1+y,
$$


we obtain


$$
\begin{aligned}
x^2 A R_j
&=(x^2+xy+y^2)+(xy+y^2)(1+y)\\
&=x^2+xy^2+1\\
&=x^2c.
\end{aligned}
$$


Therefore


$$
\partial_1r_*=AR_j=c=D_1z.
$$



All $2j-1$ monomials in $R_j$ lie outside the two left-block positions of $z$. Hence


$$
\boxed{\rho(z)\le2j-1.}
\tag{26}
$$



### Matching lower bound on $\rho(z)$

This is an exact finite-state calculation over $\mathbb F_4$, with a parameter-independent certificate.

Let $r=(r_L,r_R)$ be any correction, and write


$$
U=\Pi(r_L),\qquad V=\Pi(r_R).
$$


Using Equations (21) and (24),


$$
(u+\omega^2)\bigl((u+1)U+(u+\omega)V\bigr)
=
1+u^2+\omega^2u.
$$


Since


$$
1+u^2+\omega^2u=1+u(u+\omega^2),
$$


we get


$$
(u+1)U+(u+\omega)V
=
u+(u+\omega^2)^{-1}.
\tag{27}
$$



The inverse is explicit:


$$
(u+\omega^2)^{-1}
=
\sum_{i=0}^{q-1}\omega^{i+2}u^i.
\tag{28}
$$


Thus the syndrome on the right of (27) has coefficients


$$
s_i=
\begin{cases}
0,&i=1,\\
\omega^{i+2},&i\ne1.
\end{cases}
\tag{29}
$$



Write the coefficients of $U,V$ as $a_i,b_i$. The minimum number of physical correction positions outside $S=\operatorname{supp}z$ needed to realize these coefficients is bounded below by the following local costs:

At $i=0$, the free left coefficient is $\omega$, and the free right coefficient is $1$:


$$
c_0(a,b)
=
\mathbf1_{a\notin\{0,\omega\}}
+
\mathbf1_{b\notin\{0,1\}}.
$$


At $i=1$, both free coefficients are $1$:


$$
c_1(a,b)
=
\mathbf1_{a\notin\{0,1\}}
+
\mathbf1_{b\notin\{0,1\}}.
$$


At all other positions,


$$
c_i(a,b)=\mathbf1_{a\ne0}+\mathbf1_{b\ne0}.
\tag{30}
$$



These are exact coefficient-realization costs: each nonzero element of $\mathbb F_4$ is the image of one of the three physical sheet positions.

Set


$$
e_i=a_i+b_i,\qquad
v_i=\omega^{-(i+3)}e_i.
$$


For an incoming state $p$ and outgoing state $v$ at position $i$, put


$$
e=\omega^{i+3}v,\qquad
f=s_i+\omega^{i+2}p.
$$


The coefficient equation uniquely determines


$$
b=\omega(f+e),\qquad a=e+b.
\tag{31}
$$



Order states as $0,1,\omega,\omega^2$. Direct substitution into (30)–(31) gives the bulk transition matrix


$$
M=
\begin{pmatrix}
2&2&1&1\\
0&2&2&2\\
2&1&1&2\\
2&1&2&1
\end{pmatrix}.
\tag{32}
$$


The combined minimum-cost matrix for positions $0,1$ is


$$
N=
\begin{pmatrix}
1&2&2&1\\
0&1&1&2\\
2&1&1&0\\
1&2&2&1
\end{pmatrix}.
\tag{33}
$$



Use min-plus multiplication,


$$
(P\otimes Q)_{ab}=\min_c(P_{ac}+Q_{cb}).
$$


For $q=3j$, the total transition matrix is


$$
T_j=N\otimes M^{\otimes(3j-2)}.
$$



The following two identities are verified by ordinary $4\times4$ min-plus multiplication:


$$
T_2=
\begin{pmatrix}
4&4&4&4\\
3&4&3&3\\
3&3&3&3\\
4&4&4&4
\end{pmatrix},
\tag{34}
$$


and


$$
\boxed{T_2\otimes M^{\otimes3}=T_2+2,}
\tag{35}
$$


where $+2$ means adding two to every entry. Therefore, by induction,


$$
T_j=T_2+2(j-2),\qquad j\ge2.
\tag{36}
$$



The wrap condition $u^q=\omega$ has not been discarded. It requires


$$
p_{\mathrm{initial}}=\omega v_{\mathrm{final}}.
$$


Thus the minimum permitted cost is


$$
\min_{v\in\mathbb F_4}(T_j)_{\omega v,v}.
$$


The four relevant entries of $T_2$ are $4,3,4,3$, so this minimum equals


$$
3+2(j-2)=2j-1.
$$



Every binary correction must satisfy this projected equation and pay at least this cost. Combining with (26),


$$
\boxed{\rho(z)=2j-1.}
\tag{37}
$$



The calculation is not a finite search over $j$: Equation (35) proves the formula for every $j\ge2$.

### Every minimum logical is killed by transfer

The explicit correction proves $[z]\in\operatorname{im}p_*$.

Both base and cover have


$$
\dim H_2=2,\qquad \dim H_1=4.
$$


In the long exact sequence, the injective map


$$
H_2(C)\xrightarrow{\tau_*}H_2(\widetilde C)
$$


is consequently an isomorphism. Therefore $\beta_2$ is injective and


$$
\dim\ker\tau_*=2.
$$


Exactness also gives $\dim\operatorname{im}p_*=2$.

The audited identity $\beta_1\beta_2=0$ gives


$$
\ker\tau_*=\operatorname{im}\beta_2
\subseteq\operatorname{im}p_*.
$$


The dimensions agree, hence


$$
\ker\tau_*=\operatorname{im}p_*.
$$


Since $z$ is projectable,


$$
\boxed{\tau_*[z]=0.}
$$



Translation preserves cycles, boundaries, physical weight, and exact projection. It follows that every translate of $z$ is killed, and that its optimal fixed-projection lifting weight is the same. Since these are all minimum representatives,


$$
\boxed{
\rho(z')=2j-1>2
\quad\text{for every minimum base logical }z'.
}
\tag{38}
$$



In particular, the smallest possible weight of a cover cycle whose **literal projection** is any minimum base logical is


$$
\boxed{4+2\rho(z)=4j+2.}
\tag{39}
$$



### Nevertheless, the cover distance is six

Put


$$
P=1+x^{2q}+x^{4q},
\qquad
w=(P,P).
\tag{40}
$$


Because $x^{2q}P=P$,


$$
(\widetilde A+\widetilde B)P=0.
$$


Thus $w$ is a cover cycle of weight six.

It is nontrivial: every boundary has both coordinates divisible by $g$, whereas


$$
P\equiv1\pmod g.
$$


So $d_{Z,2}\le6$.

For completeness, its distance is exactly six. Suppose a nonzero cover cycle had weight at most four. Its projection would be a base cycle of weight zero or four, since the base has no nonzero cycles below weight four.

If the projection were zero, the cover cycle would equal $\tau(a)$ for a base cycle $a$ of weight at most two, impossible.

If the projection had weight four, it would be a translate of $z$. Equation (39) says that any cover cycle with that exact projection has weight at least $4j+2\ge10$, also impossible.

Odd-weight cycles are excluded because all check-matrix columns have odd weight three. Hence


$$
d_{Z,2}=6.
$$



The BB map


$$
J(u,v)=(v^\star,u^\star),
\qquad f^\star(x)=f(x^{-1}),
$$


is a weight-preserving isomorphism from $Z$-homology to $X$-cohomology. It also commutes with projection and transfer. Consequently,


$$
d_X=d_Z=4,\qquad d_{X,2}=d_{Z,2}=6,
$$


and the same fixed-projection obstruction holds for minimum $X$-logicals.

For odd $j$, the doubled base period $L=9j$ is odd, so the group extension splits. Thus the counterexample is not an artifact of the even-period carry cocycle. Exchanging $x$ and $y$ gives the corresponding $y$-double-cover examples.

## 4. The smallest member and the four possible escape routes

Taking $j=2$ gives


$$
\begin{aligned}
A&=1+x^5+x^{10},&
B&=1+x^{16}+x^{17},\\
\widetilde A&=1+x^5+x^{28},&
\widetilde B&=B,
\end{aligned}
$$


with periods $18$ and $36$. Thus


$$
\boxed{[[36,4,4]]\longrightarrow[[72,4,6]].}
$$



A minimum logical is


$$
z=(x+x^6,1+x),
$$


and an optimal correction is


$$
r=(x^3+x^8+x^{11},0).
$$


Its three positions are all outside $\operatorname{supp}z$, and the proof above establishes


$$
\rho(z)=3.
$$



**Another minimum logical does not rescue the reduction.** There are exactly eighteen weight-four cycle representatives, all translations of $z$. All have trivial transfer and $\rho=3$.

**A non-minimum logical does rescue the upper bound.** In the general family, the weight-six base logical


$$
q_0=(1+x^q+x^{2q},\ 1+x^q+x^{2q})
\tag{41}
$$


has the weight-preserving cover lift $w$ from (40). Therefore $\rho(q_0)=0$, and


$$
d_2=6\le8=2d.
$$



**There is no missing normal-form coordinate.** Every cover chain is represented uniquely by $(q,r)$. What the failed lemma restricts is the *literal projected chain* $q=z$, rather than allowing that projected chain to change by a base boundary.

This distinction occurs within a single cover logical class. For $j=2$, the projection $q_0$ of $w$ satisfies


$$
q_0+xz=\partial_2s,
$$


where


$$
s=x^2+x^3+x^4+x^6+x^7+x^8+x^9+x^{11}+x^{12}.
$$


Thus adding the cover boundary $\widetilde\partial_2\widehat s$ to $w$ gives another representative of the same cover class whose literal projection is $xz$. Such representatives are included in the normal form, but every representative with that literal projection has weight at least ten. The weight-six representative uses a different, homologous projected chain.

**The actual upper-bound conjecture is not contradicted.** Every member of the family has $d_2=6$, despite the minimum-logical fixed-projection lifting cost $4j+2$ growing without bound.

## 5. Check against the previous $[[30,4,4]]\to[[60,4,6]]$ example

For


$$
\begin{aligned}
A&=x^2+xy+xy^2,&
B&=x^4+x^4y+x^3y^2,\\
\widetilde A&=x^7+x^6y+xy^2,&
\widetilde B&=x^9+x^4y+x^8y^2,
\end{aligned}
$$


and


$$
z=(1+y,\ x^3y+x^3y^2),
$$


the audited carry formula gives


$$
D_1z=xy+xy^2+x^2y+x^2y^2.
$$


The correction


$$
r=(y+y^2,0)
$$


satisfies


$$
\partial_1r=D_1z
$$


and has exactly one position outside $\operatorname{supp}z$.

To exclude $\rho=0$, restrict $r$ to the four positions of $z$, with coefficients $r_1,r_2,r_3,r_4$. The syndrome equations at check positions $x$ and $x^2y$ respectively require


$$
r_2+r_3=0,\qquad r_2+r_3=1.
$$


Therefore


$$
\boxed{\rho(z)=1,}
$$


as previously claimed.

The same normal-form formulas therefore explain both this example and the new family; no weight-preserving-lift assumption has re-entered the argument.

The exact standard-library Python verifier (historical external reference; see original note) checks the coefficient identities, the parameter-uniform $4\times4$ min-plus certificate, the first five members of the family, an explicit second-order Bockstein preimage for the smallest member, and the $\rho=1$ calculation above. All checks passed.

The decisive conclusion is stronger than failure for a particular minimum representative: **the proposed minimum-logical reduction fails for every minimum representative in an infinite family, by an arbitrarily large amount.** The short exact sequence, square-zero Bockstein, and triangular normal form remain valid; the unsupported step was the metric restriction to minimum base logicals.

STATUS: SUPPORT_BOCKSTEIN_LEMMA_FALSE
