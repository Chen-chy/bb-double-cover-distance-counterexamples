> **先看当前采用状态：** 完整 Laurent 优化必须保留消息和边界变量；常消息反例不等于因子三或全距离反例。
> [主报告](../../REPORT.md) · [逐项采用／排除表](../STATUS.md)。本篇为保留过程，不是整篇无条件有效的定理集合。

[全部研究结果](../README.md) · [逐项结论](../CLAIMS.md) · [原始完整文本](../../research/degradation/research/08-mixed-laurent/proof.md)

> 完整研究笔记的 GitHub 阅读版；仅调整数学分隔符、引用标记与链接。历史状态、限制和证明内容均保留。当前结论以总登记表中的逐项状态为准；这里的“验证”不等于独立同行评审。

# Mixed-parity Laurent amplification: a uniform factor-two subclass and a cancellation obstruction

Date: 2026-09-06.

**Status. The general mixed-parity inequality with factor three is neither proved nor refuted in this note.** The main new theorem proves factor two for all support-generated pairs whose two trinomials have arithmetic-progression supports. The theorem bounds the complete minima, not the weights of selected representatives relative to other selected representatives. A second, explicit infinite family disproves constant-message optimality even when one check and the common divisor are both `1+z+z^2`.

All weights below are finite-support Laurent weights, before any finite period. Put

    S=F_2[z,z^{-1}], R=S[s]/(s^2+1),
    A_tilde=s+(A+1), B_tilde=s+(B+1),
    c=gcd(A,B), rho=gcd(A,C_0,C_1),
    P=(A+B)/(c rho), Q=A^2/(c rho).

The preceding proof state supplies the full physical parameterization

    Y_0=((A+1)P+Q)k+(B+1)h,
    Y_1=Pk+h,
    Y_2=Qk+(A+1)h,
    Y_3=h.

Here `(Y_0+sY_1,Y_2+sY_3)` is a universal cycle. In the residual specialization regimes, the nonboundary condition is exactly `g_0 does not divide k`. Define `mu_+` to be the minimum of its four-block weight over **both** k and h with this condition, and

    mu_0=min_{g_0 does not divide f} [wt((B/c)f)+wt((A/c)f)].

The preceding all-representative parameterization and period-stabilization theorem are used at their supplied proof status. The new constructions are also checked directly for zero syndrome and nonboundary, rather than relying solely on the parameterization.

## 1. The arithmetic-progression mixed class

Let a,b be distinct positive integers satisfying

    gcd(a,b)=1,  a=b (mod 6),  a mod 6 in {1,5}.

Set

    A_n=1+z^n+z^{2n}, T_n=s+z^n+z^{2n},
    A=A_a, B=A_b, A_tilde=T_a, B_tilde=T_b,
    c_*=1+z+z^2.

These are instances of the requested mixed-parity form: the even exponent is 2n and the odd exponent is n. The combined translations generate Z. The parity binomials are

    C_0=z^a+z^b,
    C_1=z^{(a-1)/2}+z^{(b-1)/2}.

Both are nonzero. Their exponent differences have ratio two, not one, so the previously resolved aligned-parity condition does not apply. The allowed common parity gauge changes both signs and does not make either binomial vanish.

### Theorem 1

For every such pair and every nontrivial compatible g_0,

    c=rho=g_0=c_*,
    a+b <= mu_0,
    a+b <= mu_+ <= 2(a+b),

and consequently

    mu_+ <= 2 mu_0.

If a=b=1 (the nongenuine, associated-check endpoint), the same factor-two conclusion holds directly; it is excluded from the stated genuine mixed class.

More precise upper bounds, with epsilon=1 for a,b=1 (mod 6) and epsilon=-1 for a,b=5 (mod 6), are

    mu_0 <= [4(a+b)-2 epsilon]/3,

and

    mu_+ <= 2(a+b)-2   if epsilon=1,
    mu_+ <= 2(a+b)     if epsilon=-1.

Thus both complete Laurent minima grow on the scale a+b. This is not a bounded-distance special case.

### 1.1 The gcds

For odd n, A_n has derivative z^{n-1} and is squarefree. Its roots have order dividing 3n but not n. A common root of A_a and A_b therefore has order dividing gcd(3a,3b)=3. The root 1 is excluded. Hence their gcd is c_*.

Because a-b is divisible by six, c_* divides both C_0 and C_1. Thus rho=c_*. A nontrivial gcd of c_* with a period is necessarily c_* itself, so g_0=c_*.

## 2. A residue-recursion lower bound for all messages

This argument handles arbitrary Laurent messages, including arbitrarily long messages and any boundary adjustment.

Let f be any Laurent polynomial not divisible by c_*. After a common monomial shift, expand

    q=f/c_*

as a power series bounded below. Its tail is a nonzero period-three binary sequence. This follows from the recurrence q_i+q_{i-1}+q_{i-2}=0 beyond the support of f. If the tail were zero, q would be a Laurent polynomial and c_* would divide f.

For n relatively prime to three, suppose the Laurent polynomial A_n q vanished on an entire residue class r modulo n. The subsequence q_{r+jn} would then obey

    q_{r+jn}+q_{r+(j-1)n}+q_{r+(j-2)n}=0

for every integer j. It is zero sufficiently far to the left; forward recurrence forces it to be zero everywhere. But n is coprime to three, so its tail visits all three phases of the nonzero period-three sequence. Contradiction.

Therefore every residue class modulo n contains a supported coefficient of A_n q:

    wt(A_n q) >= n.                                      (2.1)

Applying this to n=a and n=b proves

    wt((B/c_*)f)+wt((A/c_*)f) >= a+b

for every admissible f. This proves the lower bound for the full minimum mu_0.

The elementary message f=1 gives the stated upper bound for mu_0. Direct division yields

    wt(A_n/c_*)=(4n-1)/3  for n=1 (mod 3),
    wt(A_n/c_*)=(4n+1)/3  for n=2 (mod 3).

These counts can also be obtained by expanding `(1+z)/(1+z^3)` and grouping the numerator by exponent modulo three.

### 2.1 The corresponding cover lower bound

This lower bound is not needed for factor two, but verifies that the new class includes growing cover minima as well.

Let Y=(u,v) be any universal cover cycle that is not a universal boundary. In the ring obtained from R by inverting nonzero scalar Laurent polynomials, T_a is invertible because T_a^2=A_a^2 is a nonzero scalar. There is a unique rational coefficient H such that

    u=T_b H, v=T_a H.

Since gcd(A_a^2,A_b^2)=c_*^2, scalar Bezout coefficients show that c_*^2 H belongs to R. Also H is not in R: otherwise Y would be a boundary. Its expansion bounded below therefore has a nonzero tail of period six, because c_*^2 divides 1+z^6.

For n=a or b, assume that T_n H vanished on a residue class modulo n. Along that subsequence its coefficients, which lie in F_2[s]/(s^2+1), obey the recurrence with leading coefficient s,

    s H_j+H_{j-1}+H_{j-2}=0.

The element s is a unit, so a sequence zero sufficiently far left is identically zero. Since n is coprime to six, this contradicts the nonzero period-six tail. Hence each of the n residue classes contributes at least one physical qubit to T_n H, giving

    wt(T_a H)+wt(T_b H) >= a+b.

Every class counted by mu_+ is a universal nonboundary, so this proves mu_+ >= a+b without asserting that every universal nonboundary survives every finite period.

## 3. Short cover cycles: both parity orientations

Write

    J_m=1+z^6+...+z^{6(m-1)}, J_0=0.

All displayed divisions below are exact polynomial divisions in the two scalar components of R. Their Hamming costs are calculated explicitly; division is not assumed to preserve weight.

### 3.1 The orientation n=1 (mod 6)

Put

    Theta=s+z+z^2, Theta^2=c_*^2.

In R/(Theta), z^6=1. For n=1 (mod 6), T_n is zero in this quotient, so

    D_n=T_n/Theta

is a polynomial in R. For n=6r+1, its physical components are

    (D_n)_0=J_{2r+1}+z^2 J_r+z^{6r+3}(1+z+z^2)J_r,
    (D_n)_1=(z+z^3)J_r+(z^2+z^4)J_{2r}.

The terms displayed have disjoint residue classes modulo six within each component. Thus

    wt((D_n)_0)=n, wt((D_n)_1)=n-1,
    wt(D_n)=2n-1.

The cycle

    Z=(D_b,D_a)

has weight 2(a+b)-2. Its syndrome is zero because T_a D_b=T_b D_a.

For nontriviality, evaluate at

    z=omega, s=1, omega^2+omega+1=0.

Both checks vanish. Differentiating T_n=Theta D_n with respect to s and then evaluating gives D_n=1 at this point. Therefore Z evaluates to (1,1), whereas every boundary evaluates to zero. This proves nonboundary exactly, both universally and in every compatible finite quotient admitting this evaluation.

### 3.2 The orientation n=5 (mod 6)

Put

    Psi=1+z+s z^2, Psi^2=c_*^2.

Again z^6=1 in R/(Psi), and for n=-1 (mod 6),

    s+z^n+z^{2n}=s+z^{-1}+z^{-2}=z^{-2}Psi=0.

Thus E_n=T_n/Psi is polynomial. For n=6r+5,

    (E_n)_0=z^2 J_{r+1}+z^4 J_{2r+1}
               +z^{6r+5}(1+z+z^2)J_{r+1},
    (E_n)_1=(1+z^2)J_{2r+2}+(z+z^3)J_{r+1}.

The weights are n and n+1 respectively. The initial cycle (E_b,E_a) therefore has weight 2(a+b)+2.

Assume a<b, exchanging checks if necessary. Add the single boundary with coefficient z^{2-a}:

    Z=(E_b,E_a)+(T_b,T_a)z^{2-a}.                       (3.1)

Its overlap with the initial cycle is exactly four. The overlapping positions are the two s^0 terms in each block:

    left:  b+2-a, 2b+2-a;
    right: 2, a+2.

The two s^1 boundary terms are at 2-a<0, outside both initial supports. The displayed formulas for (E_n)_0 show directly that all four stated s^0 positions are present. A boundary has six qubits, so (3.1) has weight

    [2(a+b)+2]+6-2*4=2(a+b).

This is a physical boundary adjustment, not a change of local coordinates with an untracked norm.

The same evaluation proves nontriviality. Differentiating T_n=Psi E_n with respect to s gives, at z=omega,s=1,

    1=omega^2 E_n,

so E_n=omega is nonzero. The initial cycle evaluates to (omega,omega), and adding a boundary does not change that value.

This completes the proof of Theorem 1.

### 3.3 Relation to the specified k,h optimization

For each constructed physical cycle, set h=Y_3 and

    V=Y_2+(A+1)h,
    k=V/Q.

The division is exact; substituting k,h into the four specified formulas reconstructs the cycle. The projection to s=1 is a base compact nonboundary, and equivalently k is nonzero modulo c_*.

The independent verifier explicitly reconstructs k,h and checks all four formulas. The theorem does not restrict the left-hand optimization to these representatives: their weights bound the complete left-hand minimum, while the residue argument bounds the complete right-hand minimum from below. Those two facts give the claimed comparison.

## 4. Finite realization, without new assumptions about winding classes

The termwise cover `(L,1)->(L,2)` sends s to 1 and uses checks T_a,T_b upstairs and A_a,A_b downstairs. If L>2 max(a,b), the three terms remain distinct. The translations z^a,z^b and s generated by the term differences show that the actual support group is the full C_L x C_2.

For odd L divisible by three, both compact gcd data are c_*. The base and cover dimensions are k=k_2=4. The previously established stabilization theorem therefore realizes the Laurent minima as actual distances for sufficiently large compatible L. The explicit upper bounds above give the sufficient choice

    L=3[4 b(a+b)+1]  after arranging a<b.

Indeed R=2b and L>R[2(a+b)-1]. Consequently this gives actual strict-trinomial BB families with both distances on the scale a+b and with d_2/d<=2. No exact distances beyond the proved intervals are claimed for this entire family. The preceding stabilization theorem is being applied, not reproved or replaced by a compact-only assertion.

## 5. A parametric obstruction to constant-message optimization

Even fixing A=c_*=1+z+z^2 does not justify checking only the message f=1.

For every integer j>=0 set

    E=12j+8, O=18j+13,
    B_j=1+z^E+z^O,
    f_j=1+z^{6j+3}+z^E+z^{18j+12}.

Then c=rho=g_0=c_*. Both parity binomials are nonzero and unaligned. Also f_j modulo c_* is z, so it is an admissible message.

Put b_j=B_j/c_*. Directly,

    wt(b_j)+1=12j+10.                                   (5.1)

However

    wt(b_j f_j)+wt(f_j)=8j+10.                          (5.2)

Thus for every j>=1 the constant message is strictly suboptimal, and the improvement is linear in j.

For an explicit all-parameter identity, put

    S_j=sum_{i=0}^{2j} z^{3i},
    T_j=(1+z^2)S_j+z^{6j+3}.

Then

    b_j f_j=(1+z)S_j+z^{18j+11}+z^{30j+20}T_j.          (5.3)

The three pieces are disjoint. Their weights are 4j+2, 1, and 4j+3, giving 8j+6; f_j has four terms. Multiplication by c_* verifies (5.3) directly. In particular this is not a numerical extrapolation from an optimized message.

For comparison only, the explicit cover cycle `(T_{B_j}/Theta,1)` has weight 18j+14. This is an upper bound on mu_+, not a lower bound and not a claimed minimum. Combining it with (5.2), which is another upper bound, would establish neither an upper nor a lower bound on mu_+/mu_0. **No factor-three violation or amplification ratio is claimed from this cancellation family.**

This example invalidates a generator-weight or constant-message shortcut in the full optimization. It is not used as evidence that factor three is false.

## 6. An exact systematic form of the smallest remaining case

For A=c_*, B any residual trinomial divisible by c_* with c_*^2 dividing A+B, put

    b=B/c_*, P=(b+1)/c_*.

The change of variables

    k=F+c_* H, h=H

is unimodular over S. It preserves the admissibility condition: c_* does not divide k if and only if it does not divide F. The four physical outputs become exactly

    ((b+P)F+bH, PF+bH, F+H, H).                         (6.1)

Thus the complete optimization, with no omitted messages or boundaries, is

    mu_+=min_{c_* does not divide F,H in S}
      [wt((b+P)F+bH)+wt(PF+bH)+wt(F+H)+wt(H)].           (6.2)

For supports, define

    off(X;T)=|supp(X) minus supp(T)|.

The elementary binary identity wt(X)+wt(X+T)=wt(T)+2 off(X;T) gives the exact equivalent expression

    mu_+=min_{c_* does not divide F,H in S}
       { wt(bF)+wt(F)
         +2 off(PF+bH;bF)+2 off(H;F) }.                 (6.3)

This separates the base cost from the physical cost of satisfying the second sheet. It is still the full joint optimization. Proving an upper bound on the extra term for one particular F is only sufficient, not necessary; messages of larger base weight remain eligible for a better total cost.

The cancellation family in Section 5 already lives in this fixed quadratic-divisor case. The arithmetic-progression theorem removes the special pairs in which both checks are geometric, but it does not settle (6.2) for an arbitrary second trinomial.

## 7. Verification scope and limitations

The executable verifier uses independent sparse-set Laurent arithmetic for polynomial identities and physical support counts. It checks 101 quotient identities in both orientations, 235 coprime arithmetic-progression pairs, 109 four-overlap boundary moves, and 235 recoveries of the full k,h coordinates. It also checks the residue lower bound on 367 arbitrary admissible messages; these tests are supplementary to the uniform recurrence proof.

Finite checks use a different representation: direct group translations and bit-packed binary boundary spans. Six actual rectangular covers, up to 1,356 qubits, verify zero syndrome and nonboundary status of the displayed witnesses independently of the quotient formulas. These checks are not minimum-distance searches.

The cancellation identity is verified for j=0,...,80, in addition to its symbolic proof. A separate bit-polynomial implementation verifies 480 instances of the unimodular change of variables and exact norm identity in Section 6. No heuristic output is used as a minimum-distance certificate.

A small exact base minimum is also immediate: a=1,b=7 gives mu_0=10. The residue bound gives 8. A weight-eight word would have a one-term right block and a seven-term left block, but a monomial right block forces the nine-term left block A_7/c_*. Evenness excludes weight nine, and the constant message attains ten. No new exact cover minimum is asserted for this example.

**Unresolved:** the full mixed-parity factor-three inequality, the possibility of a factor-three counterexample, a universal replacement constant for all remaining mixed pairs, and the resulting finiteness question for C_*. The present theorems do not settle any of those global assertions. The work is not proof-assistant formalized or externally refereed.

### One next lemma

Prove or refute (6.2) <= 3 min_{c_* does not divide F}[wt(bF)+wt(F)] for

    B=1+z^{6r+2}+z^{6t+1},
    b=B/c_*, P=(b+1)/c_*,

with distinct supported monomials and the genuinely mixed restrictions. This fixes A and the common divisor to a quadratic and retains every homology message and every universal boundary adjustment. A refutation must certify the complete minimum in (6.2), not one selected lift.

## Sources

The starting parameterization, gcd notation, and period-stabilization theorem are from the supplied `rank1_amplification/proof.md` (2026-09-06).

The BB term-matched covering convention is from B. C. B. Symons, A. Rajput, D. E. Browne, *Sequences of Bivariate Bicycle Codes from Covering Graphs*, arXiv:2511.13560v3, Theorem 3.1. https://arxiv.org/abs/2511.13560

The recurrence, quotient-counting, four-overlap boundary move, cancellation identity, and exact norm form in this note are derived here.
