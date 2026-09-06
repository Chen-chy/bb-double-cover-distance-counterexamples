> **先看当前采用状态：** 8→14 的稳定化族与 all-degree Bellman 证书可按条件使用；naive Frobenius 非边界论证已被否定。
> [主报告](../../REPORT.md) · [逐项采用／排除表](../STATUS.md)。本篇为保留过程，不是整篇无条件有效的定理集合。

[全部研究结果](../README.md) · [逐项结论](../CLAIMS.md) · [原始完整文本](../../research/degradation/research/07-rank-one-amplification/proof.md)

> 完整研究笔记的 GitHub 阅读版；仅调整数学分隔符、引用标记与链接。历史状态、限制和证明内容均保留。当前结论以总登记表中的逐项状态为准；这里的“验证”不等于独立同行评审。

# Rank-one BB amplification: sparse parity replacement and period stabilization

Date: 2026-09-06.

**Status: factor three is proved for the subclasses specified below, but not for the final mixed-parity Laurent inequality. No counterexample to factor three is claimed.** This note concerns amplification, d_2/d, not the degradation problem in some earlier attachments.

## 1. Definitions and scope

Let S = F_2[z,z^{-1}]. A and B are strict trinomials. Their normalized term differences generate Z. For a positive period L put

    P_L = z^L + 1,
    g = gcd(A,B),
    g_0 = gcd(g,P_L),
    mu_0 = min_{g_0 does not divide f} (wt((B/g)f)+wt((A/g)f)).

Assume g_0 is not a unit. Weights in mu_0 are **finite-support Laurent weights**, before imposing a period. They are not weights of the reductions modulo P_L. Monomial shifts are isometries. We use the BB complex

    R --(B,A)^T--> R^2 --[A B]--> R.

For actual finite group algebras the X and Z distances agree: invert all group monomials and exchange the qubit blocks. Thus proving the first homology distance proves the quantum distance. The termwise support-matching convention is that of Symons--Rajput--Browne [1].

Every double cover of a finite cyclic support group can be pulled back to an extension of Z by C_2. This extension splits. Choose a lift z and write s for the deck involution. The universal cover coefficient ring is

    R_infty = S[s]/(s^2+1),

and the actual finite cover imposes

    F = z^L + s^epsilon,  epsilon in {0,1}.

The split case epsilon=0 is C_L x C_2; epsilon=1 is the cyclic nonsplit cover. Each lifted term is its original z-monomial times 1 or s. Both the universal representation and the actual finite supports are required to be strict trinomials. The results also apply componentwise when these support groups sit inside larger BB groups.

Multiplying a check by a group monomial and the corresponding qubit block by the inverse monomial preserves weight. Multiplication by s and the gauge z -> sz may also be used; the latter changes epsilon to epsilon+L modulo two. After these operations any genuinely twisted check can be normalized to have its unique exceptional s-parity term equal to s. Unless both checks can be made untwisted, take

    A_tilde = s+a,
    B_tilde = b+lambda s,  lambda in {0,1},
    A = 1+a,
    B = b+lambda,
    C = b+lambda a = B+lambda A,
    delta = gcd(A^2,C).

If lambda=0, b is a trinomial. If lambda=1, a and b are binomials. Laurent units in gcds are immaterial.

Since the normalized term differences generate Z, at least one of A,B has a nonzero odd free exponent. Such a trinomial is squarefree in S. Indeed, for D=z d/dz, its derivative is either a monomial or the trinomial plus 1, and is nonzero at every nonzero root. Consequently g is squarefree. This observation is used only where needed below; no Hamming isometry is inferred from a field decomposition.

## 2. Exact universal-to-finite compact homology

### 2.1 Chain-level reduction

Write a universal cover cycle as

    Y=(u_0+s u_1, v_0+s v_1).

Define

    U=u_1+lambda v_1,
    V=v_0+a v_1.

The cycle equation is exactly

    A^2 U + C V = 0.                                      (2.1)

Conversely, from any solution of (2.1) form

    Phi(U,V)=((s+a)U+lambda V, V).                          (2.2)

For an original cycle Y,

    Y + Phi(U,V) = (B_tilde v_1, A_tilde v_1).             (2.3)

For a boundary with coefficient r_0+s r_1, its effective coordinates are

    (U,V)=(C r_1,A^2 r_1).

Thus this is an actual homology isomorphism, not just a dimension calculation:

    H_1(K(A_tilde,B_tilde;R_infty)) = S/(delta).

A general universal physical cycle is therefore exactly

    Y(k,h)=Phi((C/delta)k,(A^2/delta)k)
             +(B_tilde h,A_tilde h),       k,h in S.      (2.4)

Here h in S, rather than R_infty, is sufficient: (2.3) uses h=v_1, while changes of k account for the other boundary coefficients. In particular (2.4) includes all universal boundary adjustments.

Multiplication by s acts on this H_1 as multiplication by a. This follows either from (2.2)-(2.3), or by recomputing the effective coordinates of s Phi(U,V), which are (aU,aV).

### 2.2 Finite specialization

Multiplication by F=z^L+s^epsilon is injective on R_infty. For epsilon=0 this is scalar multiplication by a nonzero Laurent polynomial. For epsilon=1, F^2=(z^L+1)^2 is a nonzero scalar, which proves injectivity as well.

The short exact sequence of free complexes therefore gives the natural injection [2]

    H_1(universal)/F H_1(universal) -> H_1(actual cover).

Consequently the **compact image**, and not necessarily all finite homology, is

    S/(g_+),  where g_+=gcd(delta,z^L+a^epsilon).           (2.5)

A universal cycle (2.4) is an actual finite nonboundary if and only if

    g_+ does not divide k.                                (2.6)

The corresponding base statement is S/(g_0), with universal cycles ((B/g)f,(A/g)f). A direct proof of the base boundary test uses Bezout coefficients of A/g and B/g: the finite boundary equation is equivalent to f lying in the ideal (g,P_L).

The missing specialization-created part is retained in the exact sequence

    0 -> H_1(universal)/F H_1(universal)
      -> H_1(actual cover)
      -> H_0(universal)[F] -> 0.                          (2.7)

Nothing here identifies finite homology with compact homology.

### 2.3 Exact transfer test

Let X=(u,v)=((B/g)f,(A/g)f). The full-fibre transfer is (1+s)X, of weight at most 2 wt(X). Its effective coordinates are

    (u+lambda v,A v)=((C/g)f,(A^2/g)f).

Its compact coefficient is thus

    k_transfer=(delta/g) f.

The exact finite criterion is

    transfer(X) is nonboundary
        iff g_+ does not divide (delta/g)f.               (2.8)

In particular, if delta=g, then g_+=g_0 and every nontrivial compact base class transfers nontrivially. This proves d_2 <= 2 mu_0 in that case.

If the checks can both be made untwisted, the original universal cycle itself is a cover cycle and projects to a base nonboundary, giving d_2 <= mu_0.

## 3. Sparse parity replacement: a factor-three theorem

Suppose A is squarefree, and

    C=z^eta D_0^2,  eta in {0,1},

up to a Laurent unit square. Equivalently, all supported exponents of C have the same parity. The zero case C=0 gives associated checks and can be treated directly.

Let X=(u,v) be any universal base cycle nontrivial after imposing P_L, with weight w. Put

    U=u+lambda v,
    V=A v.

Then A^2 U+C V=0. Both coefficients in

    A^2 (z^{-eta}U)+D_0^2 V=0

are squares. Let E_i retain exactly the monomials of exponent parity i, without halving their exponents. Define

    U_i=z^eta E_i(z^{-eta}U),
    V_i=E_i(V),
    Z_i=((s+a)U_i+lambda V_i,V_i),   i=0,1.               (3.1)

These are exact universal cover cycles in the original monomial basis. No polynomial division is used to form them.

### 3.1 Nonboundary proof

Here delta=g^2. Writing A=g A_1 and D_0=g D_1, the effective transfer pair before parity selection is

    (z^{-eta}U,V)=(D_1^2 g f,A_1^2 g f).

The compact coefficient of Z_i is E_i(gf). Choose an irreducible factor p of g_0 not dividing f. The polynomial g is squarefree, so

    E_1(gf)=D(gf) = (Dg)f modulo p

is nonzero modulo p. Since gf is zero modulo p, E_0(gf) has the same nonzero residue. The factor p also divides g_+, because a=1 at every common root. Hence **both** Z_i are actual finite nonboundaries, irrespective of the seam and the multiplicity with which the period meets p.

### 3.2 Physical weights

The selectors partition supports, so

    sum_i wt(Z_i) <= 3 wt(U)+(lambda+1)wt(A v).

If lambda=0 this is at most 3w; one of the two nonboundaries therefore has weight at most 3w/2.

If lambda=1 this is at most

    3 wt(u+v)+6 wt(v).

Repeat with the two checks and qubit blocks exchanged, and choose the orientation with the smaller second-block weight. Both checks are squarefree in the active case: at a common root their derivatives agree, since D C=eta C vanishes there. Thus the same argument is valid in either orientation. It follows that

    min wt(Z_i) <= (3 wt(u+v)+6 min(wt(u),wt(v)))/2
                 <= 3w.

**Theorem 3.** For the normalized voltage covers above, a single-parity C gives

    d_2 <= 3 mu_0,

and when lambda=0 the stronger d_2 <= (3/2)mu_0 holds. The proof works with all boundary adjustments in the original input X and returns actual finite nonboundaries.

## 4. Reduction of the no-universal-torsion voltage patterns

All assertions in this section are uniform; no incidence catalogue is used.

If exactly one check is twisted, either the untwisted check is primitive in free-coordinate parity, or it is not. In the first case it is squarefree and delta=g, giving factor two. In the second case the untwisted check can be normalized to be a square, and support generation forces the twisted check to be primitive; Theorem 3 applies with lambda=0. Thus **every one-twisted-check case has factor at most two**.

Suppose both checks are twisted. Normalize them to

    A_tilde=s+z^i+z^j,  B_tilde=s+z^k+z^l.

If just one reduced check is primitive, D C is nonzero at every common root, hence delta=g. If both are primitive, there are two possible parity types for their two nonconstant exponents: odd/odd or even/odd.

* Both odd/odd: the gauge z -> sz followed by multiplication of each check by s makes both checks untwisted. Factor one applies.
* One odd/odd and one even/odd: the two derivatives cannot agree at a common root. The first equals 1 there; the second is its odd monomial, which cannot equal 1 at a trinomial zero because its remaining even monomial is nonzero. Thus delta=g, and factor two applies.
* Both even/odd: this is the only residual type.

Write it as

    A=1+z^{2p}+z^{2q+1},   B=1+z^{2r}+z^{2t+1},
    A_tilde=s+z^{2p}+z^{2q+1},
    B_tilde=s+z^{2r}+z^{2t+1}.                            (4.1)

Put

    C_0=z^p+z^r,  C_1=z^q+z^t,
    C=A+B=C_0^2+z C_1^2,
    h=gcd(A,C_0,C_1).

Then, exactly,

    delta=g h.                                           (4.2)

Indeed, A is squarefree; a common root becomes double in C precisely when both C_0 and C_1 vanish there. Up to Laurent units,

    h=gcd(A,z^D+1), D=gcd(|p-r|,|q-t|),                  (4.3)

when both differences are nonzero. In particular h is a unit if D is a power of two, because A(1)=1. Large coefficients or a formal relation alone therefore do not imply transfer failure.

If either C_i is zero, Theorem 3 applies. Also, if p-r=q-t, the gauge z -> sz followed by the allowed normalizations changes the differences to (-(p-r),(q-t)-(p-r)); one parity component then vanishes. These aligned cases are resolved as well.

For the remaining cases, the period test is explicit. At a common root, write O=z^{2q+1}; then 0 != O != 1. The derivative of z^L+a is (L mod 2)+O there, and is always nonzero. Consequently

    g_+=g_0  if epsilon=1 or L is odd.                    (4.4)

If epsilon=0 and L is even, the period already has multiplicity at least two at every active root. Formula (2.8) then shows that every nonzero compact base class transfers nontrivially, giving factor two.

Thus a still-unresolved instance must have (4.1), two nonzero parity binomials (after the stated gauge alternatives), a nontrivial active factor of h, and either an odd split period or a nonsplit period. For a selected base class, transfer failure is exactly

    g_0 divides h f,   while g_0 does not divide f.        (4.5)

This is an explicit cancellation obstruction, not an unclassified local module.

### 4.1 A failed factor-three construction, exactly diagnosed

A tempting universal construction takes a base cycle X=(u,v) and forms

    W_F=(A_tilde u^2,B_tilde v^2).

This is always a cycle of weight at most 3 wt(X), because A_tilde^2=A^2 and B_tilde^2=B^2. It does not solve the problem.

More generally write A_tilde=A+e alpha, B_tilde=B+e beta, e=1+s, and A=c A_1, B=c B_1. For X=(B_1 f,A_1 f), direct multiplication gives

    W_F + partial_2(A_1 B_1 f^2)
      = e (B_1,A_1)(alpha B_1+beta A_1)f^2.

Consequently in actual finite homology,

    [W_F]=(alpha B_1+beta A_1) f * tau_*[X].

Whenever the transfer of X is killed, W_F is killed too. Thus this sparse 3w candidate cannot resolve any transfer-killed case, even after boundary adjustments.

In the all-critical normalized case alpha=beta=1 and c^2 divides A+B, let D=(A+B)/c^2. There is even an explicit universal filling:

    W_F = partial_2((A_1 B_1+e D) f^2).

This is a counterexample to the proposed *nonboundary argument*, not a counterexample to the factor-three distance bound. The family in Section 6 lies in this all-critical case.

## 5. Period stabilization: when a Laurent obstruction becomes actual amplification

The next theorem does not require the factor-three conjecture.

For fixed A,B, voltages, and period/seam data, define the full relative compact distances

    mu_base = min wt((B/g)f,(A/g)f),  g_0 does not divide f,

    mu_cover = min wt(Y(k,h)),       g_+ does not divide k,
                                            k,h in S.     (5.1)

The second minimization includes the boundary parameter h in (2.4). It is not a minimization over a single chosen compact generator or a transferred class.

### 5.1 Exact period congruences

There is a positive integer T for which g_0 and g_+ stay exactly the same whenever L is replaced by L+jT. For example, take the multiplicative order of z in the finite ring S/(g delta). Equality of z^L in this ring fixes both gcds. Thus (5.1) is constant along this progression.

### 5.2 Exclusion of short winding cycles

Normalize the free-coordinate check supports into an interval of diameter R. A finite cycle of weight w has 3w incidences. Pair equal syndrome incidences. Each edge of the resulting graph changes the free coordinate by at most R. Every simple graph cycle has at most w edges.

If

    Rw < L,

a graph cycle cannot wind through a nonzero multiple of the period L. Since the universal deck subgroup C_2 injects into the actual cover, zero free winding also leaves no hidden torsion obstruction. Lifting a spanning tree therefore lifts all paired edges consistently. The result is a universal cycle of the same physical weight. The same argument, without C_2, applies to the base.

This argument includes arbitrary multiplicities at syndrome sites and does not assume the cycle is a boundary or has a specified homology sector.

### 5.3 Stabilization theorem

A minimizing universal relative cycle always specializes to a finite nonboundary of no larger weight. Conversely, when

    L > R(mu_base-1),

any hypothetical smaller base nonboundary would lift to a universal cycle contradicting mu_base. Similarly for the cover. Therefore, in every fixed period congruence class and for all sufficiently large L,

    d(L)=mu_base,   d_2(L)=mu_cover.                       (5.2)

One sufficient threshold is

    L > R(max(mu_base,mu_cover)-1).                       (5.3)

The specialization-created group in (2.7) is not discarded: (5.3) proves that it cannot furnish a shorter logical. A representative mixing compact and period-created sectors is covered by the same lifting argument.

### 5.4 Counterfamily promotion

Suppose the relative Laurent inequality mu_cover <= C mu_base fails for some fixed polynomial data and a realizable period class. By increasing the period in that class, (5.2) gives actual strict-trinomial double covers with d_2/d=mu_cover/mu_base>C.

More strongly, if a sequence of such relative ratios tends to infinity, choose a sufficiently large period separately for each member. This produces actual BB double covers with d_2/d -> infinity. There can be no universal rescue by short winding logicals.

This statement does **not** say that every finite base minimum is compact for its original period. Nor does it identify the compact benchmark with d at small periods. It is an eventual realization theorem, with an explicit sufficient threshold.

## 6. An exactly certified mixed-parity family

Take

    A=1+z^2+z^7,
    B=1+z+z^8,
    A_tilde=s+z^2+z^7,
    B_tilde=s+z+z^8.

For every odd L divisible by three and L >= 105, use (L,1)->(L,2), so s is the second-coordinate variable. All terms remain distinct and match individually. The normalized support differences generate both actual groups.

Here

    g=1+z+z^2,
    delta=g^2=1+z^2+z^4,
    C/delta=z+z^2+z^3+z^4,
    A^2/delta=1+z^2+z^4+z^8+z^10.

Odd periods divisible by three give g_0=g_+=g. The dimensions are exactly k=k_2=4. An exact free-coset certificate gives

    mu_base=8,   mu_cover=14.                             (6.1)

Since R=8 and 105>8(14-1), stabilization proves the actual parameters

    [[2L,4,8]] -> [[4L,4,14]],
       3 | L, L odd, L >=105.                            (6.2)

This is not a new ratio record: 7/4 is below the 7/3 example in the supplied research state. It is a certified realization of the remaining two-parity mechanism, with all finite winding sectors controlled.

The entire compact base transfer image is killed: its cover coefficient is g f, which is zero modulo g_+=g. Nevertheless, a shorter primitive compact cover class survives. This illustrates why transfer failure does not itself yield a counterexample to factor three.

### 6.1 Explicit upper witnesses

A weight-eight base cycle is

    u=1+z^7+z^9+z^12,
    v=1+z+z^8+z^11.

A weight-fourteen cover cycle has the four physical sheet components

    u_0=1+z^2+z^3+z^4+z^7+z^8,
    u_1=z^2+z^6,
    v_0=1+z^3+z^6+z^7,
    v_1=z+z^5.

Its chain is (u_0+s u_1,v_0+s v_1). Direct multiplication gives zero syndrome. The effective coefficient k is nonzero modulo g, proving nonboundary status for every stated period.

### 6.2 Exact all-degree lower certificates

The base universal cycle encoder has one input, degree 6, and homology-label modulus g of degree 2. Its augmented finite-state graph has 256 states.

The cover universal cycle encoder has two inputs and four physical outputs, with reduced column degrees (6,6), and the same degree-two label. It has 16,384 states. Its two columns are

    [1+z^3+z^4+z^5+z^6, z^2+z^4,
       1+z^2+z^3+z^4+z^5, z+z^3]^T,

    [z^2+z^4, 1+z^3+z^4+z^5+z^6,
       z+z^3, 1+z^2+z^3+z^4+z^5]^T.

Both have compact label 1 modulo g. These are an entire polynomial cycle basis, not a chosen subcode. The independent verifier recovers each column's (k,h) coordinates from the chain equations and checks that the determinant of their coordinate matrix is 1.

An encoder state records previous input coefficients and the current homology residue. If l is that residue and the current input contribution is b, the label updates to z^{-1}(l+b) modulo g. A finite input is nontrivial exactly when, after flushing the encoder memory, the label is nonzero.

The search exports a truncated Bellman potential pi. The independent checker verifies pi(0)=0, pi>=8 or 14 respectively on every zero-memory/nonzero-label terminal, and

    pi(next) <= pi(current)+output_weight

on every edge. Telescoping proves the lower bounds for all path lengths, hence for all Laurent degrees. The supplied polynomial input gives equality. This is not a bounded-window search.

The verifier checks 512 base edges and 65,536 cover edges, and independently checks the witnesses, ranks, and killed transfers by binary boundary-span calculations at L=105,111,117,129.

## 7. Verification scope

`verify.py` uses no shortest-path search when checking the Bellman certificates. Its finite-ring part represents monomial translations directly and computes binary boundary spans independently of the gcd membership predictions.

The executed formula tests cover 360 finite codes, 1,440 universal-cycle/finite-boundary tests, 360 transfer tests (including 40 losses), 132 nonboundary parity-selector witnesses, 40 mixed-parity delta/period identities, and 360 Frobenius/transfer class identities. Both split and nonsplit periods and both odd and even base periods are included. These are checks of the uniform algebra, not an exhaustive classification of codes.

The proof is not proof-assistant formalized or externally refereed. The global factor-three statement is not claimed.

## 8. The exact remaining Laurent inequality

In the mixed case (4.1), put

    P=(A+B)/(g h),  Q=A^2/(g h).

In the only still-dangerous period regimes, g_+=g_0. All universal physical cycles, with all boundary adjustments, have the four components

    ((A+1)P+Q)k+(B+1)t,
    Pk+t,
    Qk+(A+1)t,
    t,                                                     (8.1)

where k,t range over S. Such a cycle survives the finite cover exactly when g_0 does not divide k.

The remaining question is the purely Laurent metric inequality

    min_{g_0 does not divide k, t in S} wt((8.1))
        <= 3 min_{g_0 does not divide f}
                    [wt((B/g)f)+wt((A/g)f)].              (8.2)

Both parity binomials must be nonzero after the allowed gauges, the active h must be nontrivial, and a counterexample must avoid all of the transfer-surviving alternatives in Section 4. The minimization is over all active compact sectors, not a prescribed class.

Theorem 5 makes this reduction decisive: a violation of (8.2) gives an actual finite-distance violation at sufficiently large periods, and an unbounded sequence of its ratios gives C_* = infinity. Conversely, proving (8.2) supplies the missing no-universal-torsion rank-one factor-three bound. Higher universal torsion remains outside this note.

## References

[1] B. C. B. Symons, A. Rajput, D. E. Browne, *Sequences of Bivariate Bicycle Codes from Covering Graphs*, arXiv:2511.13560v3, especially Theorem 3.1 and the chain-complex formulation. https://arxiv.org/html/2511.13560v3

[2] The Stacks Project, Lemma 12.13.6, Tag 0111: the long exact homology sequence of a short exact sequence of chain complexes. https://stacks.math.columbia.edu/tag/0111

[3] R. Wang and L. P. Pryadko, *Distance bounds for generalized bicycle codes*, arXiv:2203.17216. Used for comparison with standard GB dimension and distance conventions, not as a source for the new parity or stabilization theorems. https://arxiv.org/html/2203.17216v1
