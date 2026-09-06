# 104 条研究记录：结果、否定路线与未决问题 / Research record register

[先读主报告](../REPORT.md) · [采用与排除状态](STATUS.md) · [阅读路线](README.md) · [机器可读目录](catalog.json)

**104 是研究记录数，不是 104 个有效定理，也不是 104 个独立成果。** 包含重复登记、否定结果、未决问题、样本搜索及材料有缺口的历史输入。
每项列出当前采用方式、范围、证据类型、论证或问题出处和限制。`symbolic-proof` 表示文本给出证明，不表示形式化验证或独立同行评审；原始状态不自动等于当前采用状态。
两个有限反例的缺失证书已由第三个输入包补齐；早期参数族和小重量输入必须保留各自限制。

| 分组 | 项数 |
|---|---:|
| main | 16 |
| homology | 10 |
| amplification | 38 |
| degradation | 40 |
| total | 104 |

<a id="CEX-UP"></a>

## CEX-UP

[[78,4,6]] -> [[156,4,14]]: exact d2/d=7/3>2.

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `exact-computer-assisted-certificate`；原证据类型：exact-computer-assisted-certificate.

**当前采用方式：** 主报告采用。有限例的两套独立精确距离证书已保留；全距离 6→14，而非单个 witness 上界。

**证明／论证入口：** [results/theory/01-counterexamples.md](theory/01-counterexamples.md#thm-examples)

**已记录的主要依赖：** [CERT-COMPLETENESS](#CERT-COMPLETENESS)

**程序与数据：** [certificates/upper/CERTIFICATE.md](../certificates/upper/CERTIFICATE.md) · [certificates/upper/verify_bitset.py](../certificates/upper/verify_bitset.py) · [certificates/upper/verify_polynomial.py](../certificates/upper/verify_polynomial.py)

<a id="CEX-DOWN"></a>

## CEX-DOWN

[[156,4,14]] -> [[312,8,12]]: exact d2/d=6/7<1.

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `exact-computer-assisted-certificate`；原证据类型：exact-computer-assisted-certificate.

**当前采用方式：** 主报告采用。有限例的两套独立精确距离证书已保留；全距离 14→12，而非特定类的受限最小值。

**证明／论证入口：** [results/theory/01-counterexamples.md](theory/01-counterexamples.md#thm-examples)

**已记录的主要依赖：** [CERT-COMPLETENESS](#CERT-COMPLETENESS)

**程序与数据：** [certificates/lower/CERTIFICATE.md](../certificates/lower/CERTIFICATE.md) · [certificates/lower/verify_lower_bitset.py](../certificates/lower/verify_lower_bitset.py) · [certificates/lower/verify_lower_polynomial.py](../certificates/lower/verify_lower_polynomial.py)

<a id="HOM-RANK"></a>

## HOM-RANK

k<=k2<=2k; rank(transfer)=rank(projection)=k2/2.

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `symbolic-proof-supplied`；原证据类型：symbolic-proof-supplied.

**当前采用方式：** 主报告采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/theory/02-homology.md](theory/02-homology.md#prop-ranks)

<a id="HOM-FULL"></a>

## HOM-FULL

k2=2k implies d2<=2d.

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `symbolic-proof-supplied`；原证据类型：symbolic-proof-supplied.

**当前采用方式：** 主报告采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/theory/02-homology.md](theory/02-homology.md#eq-full-dimension)

**已记录的主要依赖：** [HOM-RANK](#HOM-RANK)

<a id="HOM-REFINED"></a>

## HOM-REFINED

d2<=2*lambda_(k-k2/2+1), where lambda_j is the logical spanning threshold.

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `symbolic-proof-supplied`；原证据类型：symbolic-proof-supplied.

**当前采用方式：** 主报告采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/theory/02-homology.md](theory/02-homology.md#prop-lambda)

**已记录的主要依赖：** [HOM-RANK](#HOM-RANK)

<a id="HOM-SECTORS"></a>

## HOM-SECTORS

d2=min(d_vis,d_ker); d_vis>=d. Projection-kernel classes must not be omitted.

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `symbolic-proof-supplied`；原证据类型：symbolic-proof-supplied.

**当前采用方式：** 主报告采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/theory/02-homology.md](theory/02-homology.md)

<a id="DIST-LOWER"></a>

## DIST-LOWER

d<=4*d2^3; equivalently d2>=2*ceil((d/4)^(1/3)/2).

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `symbolic-proof-supplied`；原证据类型：symbolic-proof-supplied.

**当前采用方式：** 主报告采用。主文提供完整三次退化论证，不调用尚未恢复的小重量排除输入。

**证明／论证入口：** [results/theory/03-polynomial-bounds.md](theory/03-polynomial-bounds.md#thm-polynomial)

**已记录的主要依赖：** [FINITE-SUBGROUP](#FINITE-SUBGROUP) · [STRIP-COFACTOR](#STRIP-COFACTOR)

**限制：** Also proved in the stated finite abelian 2-group-kernel descent extension.

<a id="DIST-UPPER"></a>

## DIST-UPPER

d2<=8*d^3.

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `symbolic-proof-consolidation`；原证据类型：symbolic-proof-consolidation.

**当前采用方式：** 主报告采用。主文提供常数 8 的合并推论；区别于原支线常数 32，不视为外部独立审稿通过。

**证明／论证入口：** [results/theory/03-polynomial-bounds.md](theory/03-polynomial-bounds.md#thm-polynomial)

**已记录的主要依赖：** [FINITE-SUBGROUP](#FINITE-SUBGROUP) · [STRIP-COFACTOR](#STRIP-COFACTOR) · [LATTICE-TRANSPORT](#LATTICE-TRANSPORT)

**程序与数据：** [scripts/verify_lattice_transport.py](../scripts/verify_lattice_transport.py)

**限制：** The imported upper constant was 32. Constant 8 is a prior consolidation corollary, not an original-archive claim. Finite identity checks do not prove the universal theorem.

<a id="DIST-INTERVAL"></a>

## DIST-INTERVAL

d_lower=2 ceil((d/4)^(1/3)/2); d_upper=2 floor(min(8d^3,n,C0(2n)^(3/4))/2), C0=(16/3)(12/pi^2)^(3/4); also minimize with 2d when k2=2k.

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `symbolic-proof-supplied`；原证据类型：symbolic-proof-supplied.

**当前采用方式：** 主报告采用。由现行三次界、长度界及偶性推导；对常数 8 的审阅依赖不能被取整消除。

**证明／论证入口：** [results/theory/04-size-bounds.md](theory/04-size-bounds.md#eq-dlower)

**已记录的主要依赖：** [DIST-LOWER](#DIST-LOWER) · [DIST-UPPER](#DIST-UPPER) · [DIST-AMBIENT](#DIST-AMBIENT) · [HOM-FULL](#HOM-FULL)

**限制：** The integer CLI implements the safe cubic/length/transfer caps only, not an unsafe floating-point rounding of the analytic cap. Constants and exponents are not claimed optimal.

<a id="DIST-AMBIENT"></a>

## DIST-AMBIENT

d<=min(n/2,C0*n^(3/4)), C0=(16/3)(12/pi^2)^(3/4).

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `symbolic-proof-supplied`；原证据类型：symbolic-proof-supplied.

**当前采用方式：** 主报告采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/theory/04-size-bounds.md](theory/04-size-bounds.md)

**已记录的主要依赖：** [FINITE-SUBGROUP](#FINITE-SUBGROUP) · [STRIP-COFACTOR](#STRIP-COFACTOR)

**限制：** The geometry-of-numbers proof cites Minkowski second theorem; see REFERENCES.md.

<a id="DIST-TRUNCATED"></a>

## DIST-TRUNCATED

gamma_-(N)>=max(N^(-2/3),c_-*N^(-1/2)); Gamma(N)<=c_+*sqrt(N); c_-=pi*3^(1/6)/2^(13/3), c_+=2^(3/2)*C0^(2/3).

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `symbolic-proof-supplied`；原证据类型：symbolic-proof-supplied.

**当前采用方式：** 主报告采用。现行两项下界不含有缺失输入的 min(1/12,20/N) 项；上界使用常数 8。

**证明／论证入口：** [results/theory/04-size-bounds.md](theory/04-size-bounds.md#cor-truncated)

**已记录的主要依赖：** [DIST-LOWER](#DIST-LOWER) · [DIST-UPPER](#DIST-UPPER) · [DIST-AMBIENT](#DIST-AMBIENT)

**限制：** Nonempty collection and N is a cap on BASE qubits, not cover qubits. Not asymptotic equality.

<a id="DIST-EXAMPLE-THRESHOLDS"></a>

## DIST-EXAMPLE-THRESHOLDS

Gamma(N)>=7/3 for N>=78; gamma_-(N)<=6/7 for N>=156.

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `symbolic-proof-supplied`；原证据类型：symbolic-proof-supplied.

**当前采用方式：** 主报告采用。由两个有限证书直接导出底码长度阈值，不依赖早期无限族。

**证明／论证入口：** [results/theory/04-size-bounds.md](theory/04-size-bounds.md#cor-truncated)

**已记录的主要依赖：** [CEX-UP](#CEX-UP) · [CEX-DOWN](#CEX-DOWN)

<a id="FINITE-SUBGROUP"></a>

## FINITE-SUBGROUP

A check supported in a finite subgroup K implies d<=|K| whenever k>0.

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `symbolic-proof-supplied`；原证据类型：symbolic-proof-supplied.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/theory/03-polynomial-bounds.md](theory/03-polynomial-bounds.md#lem-finite-check)

<a id="STRIP-COFACTOR"></a>

## STRIP-COFACTOR

d<=4|T|R0 on a finite image of T+Z; three independent relation rows give the signed-cofactor strip bound.

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `symbolic-proof-supplied`；原证据类型：symbolic-proof-supplied.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/theory/03-polynomial-bounds.md](theory/03-polynomial-bounds.md#lem-strip)

<a id="LATTICE-TRANSPORT"></a>

## LATTICE-TRANSPORT

The voltage-kernel sublattice of three base relations has index 1 or 2; its cofactor vector is multiplied by that index.

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `symbolic-proof-consolidation`；原证据类型：symbolic-proof-consolidation.

**当前采用方式：** 按范围采用。合并稿新增的指数至多二关系子格推论；有限恒等式检查不是所有参数的证明。

**证明／论证入口：** [results/theory/03-polynomial-bounds.md](theory/03-polynomial-bounds.md#lem-transport)

**已记录的主要依赖：** [STRIP-COFACTOR](#STRIP-COFACTOR)

**程序与数据：** [scripts/verify_lattice_transport.py](../scripts/verify_lattice_transport.py)

<a id="CERT-COMPLETENESS"></a>

## CERT-COMPLETENESS

Circuit minimality, even parity, translation-root reduction and both branching algorithms certify exhaustive finite distance exclusions.

**Scope / 范围：** Binary coefficients; finite abelian groups; degree-two term-preserving quotient; exactly three distinct terms in each check before and after projection; k>0; n denotes base qubits.

**Status / 状态：** `algorithm-completeness-proof`；原证据类型：algorithm-completeness-proof.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/theory/06-certificate-algorithms.md](theory/06-certificate-algorithms.md)

**程序与数据：** [scripts/reproduce.py](../scripts/reproduce.py)

**限制：** Exact searches must terminate successfully; a timeout is incomplete, not an exclusion.

<a id="HOM-BOCKSTEIN"></a>

## HOM-BOCKSTEIN

The connecting maps satisfy beta_1 beta_2 = 0. Hence ker(tau_*) = im(beta_2) is contained in im(p_*).

**Scope / 范围：** Binary rectangular x/y BB double covers with the specified fourfold coefficient-ring thickening.

**Status / 状态：** `symbolic-proof`；原证据类型：symbolic-proof.

**当前采用方式：** 按范围采用。四重厚化存在的矩形周期覆盖中的结论，不自动推广到任意抽象二重覆盖。

**证明／论证入口：** [results/notes/H01-bockstein-and-deck-structure.md](notes/H01-bockstein-and-deck-structure.md)

**合并后的更新：** Restored from the third input archive; not a new theorem claimed by the GitHub packaging step.

<a id="HOM-EXACT-DIMENSION"></a>

## HOM-EXACT-DIMENSION

rank(beta_1)=rank(beta_2)=r, k_2=2k-2r, and k_2-k=dim(ker beta_1 / im beta_2).

**Scope / 范围：** Binary rectangular x/y BB double covers with the specified fourfold coefficient-ring thickening.

**Status / 状态：** `symbolic-proof`；原证据类型：symbolic-proof.

**当前采用方式：** 按范围采用。继承 H01 四重厚化范围；不把该精化的范围与一般 rank 公式混同。

**证明／论证入口：** [results/notes/H01-bockstein-and-deck-structure.md](notes/H01-bockstein-and-deck-structure.md)

**合并后的更新：** Restored from the third input archive; not a new theorem claimed by the GitHub packaging step.

<a id="HOM-DECK-JORDAN"></a>

## HOM-DECK-JORDAN

For D=F_2[epsilon]/epsilon^2, H_1(cover) is D^(k_2-k) direct-sum F_2^(2k-k_2); rank(T_*+I)=k_2-k.

**Scope / 范围：** Binary rectangular x/y BB double covers with the specified fourfold coefficient-ring thickening.

**Status / 状态：** `symbolic-proof`；原证据类型：symbolic-proof.

**当前采用方式：** 按范围采用。继承 H01 四重厚化范围；描述 deck 在同调上的作用而非 Hamming 等距。

**证明／论证入口：** [results/notes/H01-bockstein-and-deck-structure.md](notes/H01-bockstein-and-deck-structure.md)

**已记录的主要依赖：** [HOM-BOCKSTEIN](#HOM-BOCKSTEIN) · [HOM-EXACT-DIMENSION](#HOM-EXACT-DIMENSION)

**合并后的更新：** Restored from the third input archive; not a new theorem claimed by the GitHub packaging step.

<a id="HOM-PAIRING"></a>

## HOM-PAIRING

Transfer and projection are adjoint for the perfect logical X/Z pairing; two full-fibre transfers always pair to zero.

**Scope / 范围：** Binary term-preserving double covers with the stated physical pairing conventions.

**Status / 状态：** `symbolic-proof`；原证据类型：symbolic-proof.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/H01-bockstein-and-deck-structure.md](notes/H01-bockstein-and-deck-structure.md)

**合并后的更新：** Restored from the third input archive; not a new theorem claimed by the GitHub packaging step.

<a id="METRIC-CLASS-VARIATIONAL"></a>

## METRIC-CLASS-VARIATIONAL

mu(alpha)=min (|q+r|+|r|), over [q]=alpha and partial_1 r=D_1 q; the second-order parameterization is independent of the chosen Bockstein preimage.

**Scope / 范围：** Binary rectangular x/y BB double covers with the specified fourfold coefficient-ring thickening. Projectable nonzero classes; triangular coordinates include carry terms.

**Status / 状态：** `symbolic-proof`；原证据类型：symbolic-proof.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/H03-class-metrics-and-exchange.md](notes/H03-class-metrics-and-exchange.md)

**合并后的更新：** Restored from the third input archive; not a new theorem claimed by the GitHub packaging step.

<a id="METRIC-QUOTIENT-DUAL"></a>

## METRIC-QUOTIENT-DUAL

K=cover boundaries + transfer(base cycles); mu(alpha)=dist_H(y_alpha,K). The exact binary separation dual and projected-circuit shortest-path formula hold.

**Scope / 范围：** Projectable classes for the explicitly defined binary chain maps; this is not a real-norm duality.

**Status / 状态：** `symbolic-proof`；原证据类型：symbolic-proof.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/H03-class-metrics-and-exchange.md](notes/H03-class-metrics-and-exchange.md)

**合并后的更新：** Restored from the third input archive; not a new theorem claimed by the GitHub packaging step.

<a id="CEX-SUPPORT-FAMILY"></a>

## CEX-SUPPORT-FAMILY

For every j>=2, [[18j,4,4]] -> [[36j,4,6]], every minimum logical is killed by transfer, and rho(z)=2j-1. The support-Bockstein lemma fails unboundedly, although d_2<=2d holds here.

**Scope / 范围：** The explicit cyclic family L=9j, A=1+x^(3j-1)+x^(6j-2), B=1+x^(9j-2)+x^(9j-1), with the specified term lift.

**Status / 状态：** `symbolic-proof-with-finite-audit`；原证据类型：symbolic-proof-with-finite-audit.

**当前采用方式：** 有效否定结果。support–Bockstein 支撑控制引理被无限族否定；该族并不违反 d₂≤2d。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/H02-support-obstruction-family.md](notes/H02-support-obstruction-family.md)

**程序与数据：** [archive/early_counterexample/verify_previous_family.py](../archive/early_counterexample/verify_previous_family.py) · [archive/early_counterexample/verify_auxiliary.py](../archive/early_counterexample/verify_auxiliary.py)

**合并后的更新：** Restored from the third input archive; not a new theorem claimed by the GitHub packaging step.

**限制：** The text proves the full family; finite j checks are audits, not the proof for all j.

<a id="CEX-LOW-SHEET-INFINITE"></a>

## CEX-LOW-SHEET-INFINITE

[[6,4,2]] -> [[12,4,2]] has a killed class with delta=mu=2, rho=0, but nu=infinity.

**Scope / 范围：** The period-3/period-6 example and the designated low-monomial section.

**Status / 状态：** `explicit-proof-and-finite-audit`；原证据类型：explicit-proof-and-finite-audit.

**当前采用方式：** 有效否定结果。低片指标 ν 可为无穷而覆盖距离有限；ν 不能当作 d₂。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/H03-class-metrics-and-exchange.md](notes/H03-class-metrics-and-exchange.md)

**程序与数据：** [archive/early_counterexample/verify_auxiliary.py](../archive/early_counterexample/verify_auxiliary.py)

**合并后的更新：** Restored from the third input archive; not a new theorem claimed by the GitHub packaging step.

**限制：** nu is section-dependent and is not the cover distance.

<a id="METRIC-COUNTEREXAMPLE-TABLE"></a>

## METRIC-COUNTEREXAMPLE-TABLE

For the main 6->14 counterexample: delta=6, rho=4, mu=14, nu=22. For the support family: delta=4, rho=2j-1, mu=6, nu=10j for even j and infinity for odd j.

**Scope / 范围：** Specified classes and the standard low-monomial section only.

**Status / 状态：** `symbolic-proof-with-finite-audit`；原证据类型：symbolic-proof-with-finite-audit.

**当前采用方式：** 按范围采用。δ、ρ、μ、ν 对应指定类及截面；这些指标不能互换或一律等于 d₂。

**证明／论证入口：** [results/notes/H03-class-metrics-and-exchange.md](notes/H03-class-metrics-and-exchange.md)

**程序与数据：** [archive/early_counterexample/verify_counterexample.py](../archive/early_counterexample/verify_counterexample.py) · [archive/early_counterexample/verify_auxiliary.py](../archive/early_counterexample/verify_auxiliary.py)

**合并后的更新：** Restored from the third input archive; not a new theorem claimed by the GitHub packaging step.

**限制：** Do not identify rho, mu, nu, fixed-message weight, or restricted-sector weight with an unrestricted code distance.

<a id="METRIC-EXCHANGE"></a>

## METRIC-EXCHANGE

The coupled boundary and transfer-cycle moves have exact support-overlap formulas for their physical weight changes.

**Scope / 范围：** Triangular physical sheets (q+r,r) with the stated chain differentials.

**Status / 状态：** `symbolic-proof`；原证据类型：symbolic-proof.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/H03-class-metrics-and-exchange.md](notes/H03-class-metrics-and-exchange.md)

**合并后的更新：** Restored from the third input archive; not a new theorem claimed by the GitHub packaging step.

**限制：** Local overlap restrictions alone do not imply a universal factor-two distance bound.

<a id="AMP-BASE-01"></a>

## AMP-BASE-01

Connected uniform family [[252j+78,4,6]] -> [[504j+156,4,14]], j>=0; record ratio 7/3

**Scope / 范围：** Unchanged polynomials, univariate cyclic double cover

**Status / 状态：** `conversation-derived uniform proof plus certified seed`；原证据类型：conversation-derived uniform proof plus certified seed.

**当前采用方式：** 证据或依赖待补。只对 j=0 的有限 seed 有现行独立精确证书；整个早期参数族保留恢复稿状态。

**恢复论证或继承输入（证据链尚有缺口）：** [results/notes/A01-initial-family-and-baseline.md](notes/A01-initial-family-and-baseline.md)

**程序与数据：** [research/amplification/research/03_amplification_search/search_verification.json](../research/amplification/research/03_amplification_search/search_verification.json) · [research/amplification/research/03_amplification_search/independent_exclusions.json](../research/amplification/research/03_amplification_search/independent_exclusions.json)

**合并后的更新：** The finite j=0 seed is repaired by CEX-UP. The complete historical family retains its recovered-source status; checking the seed does not independently certify all j.

**限制：** Original early full archive/fixed-box logs unavailable; finite seed has intact later verification.

<a id="AMP-BASE-02"></a>

## AMP-BASE-02

k<=k2<=2k; ranks of transfer and projection are k2/2; k2=2k implies d2<=2d

**Scope / 范围：** Binary BB double covers

**Status / 状态：** `inherited symbolic baseline`；原证据类型：inherited symbolic baseline.

**当前采用方式：** 按范围采用。旧基线在 HOM-RANK/HOM-FULL 已有现行证明；重复登记不是独立新增定理。

**证明／论证入口：** [results/notes/A01-initial-family-and-baseline.md](notes/A01-initial-family-and-baseline.md)

**已记录的主要依赖：** [HOM-RANK](#HOM-RANK) · [HOM-FULL](#HOM-FULL)

**限制：** Not a metric theorem for a killed chosen class.

<a id="AMP-BASE-03"></a>

## AMP-BASE-03

d=2 implies d2<=4

**Scope / 范围：** Weight-six BB double covers

**Status / 状态：** `inherited symbolic baseline`；原证据类型：inherited symbolic baseline.

**当前采用方式：** 证据或依赖待补。d=2⇒d₂≤4 在此条目中是继承输入，原独立完整报告未恢复。

**恢复论证或继承输入（证据链尚有缺口）：** [results/notes/A01-initial-family-and-baseline.md](notes/A01-initial-family-and-baseline.md)

**限制：** Original full early report is unavailable; downstream reports identify this as input.

<a id="AMP-D4-01"></a>

## AMP-D4-01

d=4 implies d2<=48

**Scope / 范围：** All stated term-matched weight-six covers

**Status / 状态：** `uniform computer-assisted; recovered-source provenance`；原证据类型：uniform computer-assisted; recovered-source provenance.

**当前采用方式：** 证据或依赖待补。d=4⇒d₂≤48 有恢复论证及转录验证器，但原报告和原包缺失；保留来源限制，不列作闭合的主证书结果。

**恢复论证或继承输入（证据链尚有缺口）：** [results/notes/A02-distance4-and-transfer-metric.md](notes/A02-distance4-and-transfer-metric.md)

**程序与数据：** [research/amplification/history/recovered_round2/verify4_independent.py](../research/amplification/history/recovered_round2/verify4_independent.py) · [research/amplification/history/recovered_round2/verify_weight_four_sympy.py](../research/amplification/history/recovered_round2/verify_weight_four_sympy.py)

**限制：** Recovered text is not authenticated original source bytes; not an optimality claim.

<a id="AMP-METRIC-01"></a>

## AMP-METRIC-01

For A=1+x+x^2, B=A^2, L=3q, q>=3 odd: d=d2=4, k=k2=4, mu=lambda3=lambda4=q+1

**Scope / 范围：** Transfer-sector metric, not amplification

**Status / 状态：** `symbolic exact family; recovered finite checker`；原证据类型：symbolic exact family; recovered finite checker.

**当前采用方式：** 有效否定结果。transfer 扇区指标可发散而 d=d₂=4；不能用该指标替代实际距离。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/A02-distance4-and-transfer-metric.md](notes/A02-distance4-and-transfer-metric.md)

**程序与数据：** [research/amplification/history/recovered_round2/verify_metric_family.py](../research/amplification/history/recovered_round2/verify_metric_family.py)

<a id="AMP-R3-01"></a>

## AMP-R3-01

Univariate one-block restricted distance doubles or does not increase according to the support-lift gcd dichotomy; a one-block logical w gives d2<=2w

**Scope / 范围：** Univariate strict-trinomial term-matched doubles

**Status / 状态：** `symbolic proof`；原证据类型：symbolic proof.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A03-amplification-search.md](notes/A03-amplification-search.md)

**程序与数据：** [research/amplification/research/03_amplification_search/verify_theorems.py](../research/amplification/research/03_amplification_search/verify_theorems.py)

**限制：** Does not imply factor two for mixed-block minima.

<a id="AMP-R3-02"></a>

## AMP-R3-02

Full split-cover homology reduces to (P^2,Q+delta P) with exact physical W_delta

**Scope / 范围：** Split group extensions

**Status / 状态：** `symbolic exact reduction`；原证据类型：symbolic exact reduction.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A03-amplification-search.md](notes/A03-amplification-search.md)

**程序与数据：** [research/amplification/research/03_amplification_search/theorem_checks.json](../research/amplification/research/03_amplification_search/theorem_checks.json)

**限制：** Ordinary reduced Hamming distance is not physical cover distance.

<a id="AMP-R3-03"></a>

## AMP-R3-03

A [[78,4,6]] base has auxiliary reduced code [[78,4,9]]

**Scope / 范围：** Auxiliary reduced code, not a strict-trinomial BB cover

**Status / 状态：** `exact finite counterexample to an intermediate lemma`；原证据类型：exact finite counterexample to an intermediate lemma.

**当前采用方式：** 有效否定结果。辅助约化码的距离 9 否定中间引理，不是新的严格三项式覆盖距离。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/A03-amplification-search.md](notes/A03-amplification-search.md)

**程序与数据：** [research/amplification/research/03_amplification_search/reduced_code_mitm.json](../research/amplification/research/03_amplification_search/reduced_code_mitm.json) · [research/amplification/research/03_amplification_search/mitm.cpp](../research/amplification/research/03_amplification_search/mitm.cpp) · [research/amplification/research/03_amplification_search/independent_search.py](../research/amplification/research/03_amplification_search/independent_search.py)

<a id="AMP-SEARCH-01"></a>

## AMP-SEARCH-01

16,384 selected distance-four/six cover instances certified within 7/3

**Scope / 范围：** Parameter instances; no exhaustive coverage of BB class

**Status / 状态：** `retained exact finite audits on selected corpus`；原证据类型：retained exact finite audits on selected corpus.

**当前采用方式：** 探索性记录。仅为指定样本的搜索记录；witness 给上界，未完成搜索不提供下界或全局排除。

**搜索记录出处（不是全局证明）：** [results/notes/A03-amplification-search.md](notes/A03-amplification-search.md)

**程序与数据：** [research/amplification/research/03_amplification_search/final_verification_summary.json](../research/amplification/research/03_amplification_search/final_verification_summary.json)

**限制：** Cover witnesses are upper bounds, not exact cover distances in every row.

<a id="AMP-SEARCH-02"></a>

## AMP-SEARCH-02

2,800 distance-eight instances; 1,020 unresolved at 7/3

**Scope / 范围：** Capped searches remain unresolved

**Status / 状态：** `partial discovery with exact certified subset`；原证据类型：partial discovery with exact certified subset.

**当前采用方式：** 探索性记录。仅为指定样本的搜索记录；witness 给上界，未完成搜索不提供下界或全局排除。

**搜索记录出处（不是全局证明）：** [results/notes/A03-amplification-search.md](notes/A03-amplification-search.md)

**程序与数据：** [research/amplification/research/03_amplification_search/RESULTS.json](../research/amplification/research/03_amplification_search/RESULTS.json)

**限制：** No failed search is a lower exclusion.

<a id="AMP-D6-01"></a>

## AMP-D6-01

d=6 implies d2<=112; remaining higher-rank mixed mechanisms give d2<=12

**Scope / 范围：** Finite abelian term-matched strict-trinomial covers

**Status / 状态：** `uniform computer-assisted`；原证据类型：uniform computer-assisted.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A04-distance6-obstruction.md](notes/A04-distance6-obstruction.md)

**程序与数据：** [research/amplification/research/04_distance6_obstruction/verify6_all_pairings.cpp](../research/amplification/research/04_distance6_obstruction/verify6_all_pairings.cpp) · [research/amplification/research/04_distance6_obstruction/highrank6_certificates.json](../research/amplification/research/04_distance6_obstruction/highrank6_certificates.json) · [research/amplification/research/04_distance6_obstruction/verify_presentations_sympy.py](../research/amplification/research/04_distance6_obstruction/verify_presentations_sympy.py)

**限制：** Full enumeration not rerun during export; retained full-matrix check rerun.

<a id="AMP-D6-02"></a>

## AMP-D6-02

Matched Frobenius powers with a nontrivial canonical base cycle give a bounded cover logical; odd-subgroup descent preserves relevant nontriviality

**Scope / 范围：** Power-cycle and odd-invariant mechanisms

**Status / 状态：** `symbolic proof`；原证据类型：symbolic proof.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A04-distance6-obstruction.md](notes/A04-distance6-obstruction.md)

**程序与数据：** [research/amplification/research/04_distance6_obstruction/frobenius_verification.json](../research/amplification/research/04_distance6_obstruction/frobenius_verification.json)

**限制：** Power equality alone is not a nonboundary certificate.

<a id="AMP-ONEBLOCK-01"></a>

## AMP-ONEBLOCK-01

A one-block logical of weight w gives d2<=2w^2

**Scope / 范围：** Finite abelian BB covers

**Status / 状态：** `symbolic proof`；原证据类型：symbolic proof.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A04-distance6-obstruction.md](notes/A04-distance6-obstruction.md)

<a id="AMP-COMPACT-01"></a>

## AMP-COMPACT-01

Genuinely higher-rank compact survival holds at all circuit weights through a torsion–Frobenius cyclic module

**Scope / 范围：** Four check differences generate U; free rank>=2; neither check in a finite subgroup

**Status / 状态：** `symbolic proof with supplementary checks`；原证据类型：symbolic proof with supplementary checks.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A05-compact-survival.md](notes/A05-compact-survival.md)

**程序与数据：** [research/amplification/research/05_compact_survival/finite_cover_certificates.json](../research/amplification/research/05_compact_survival/finite_cover_certificates.json) · [research/amplification/research/05_compact_survival/audit_finite_certificates.py](../research/amplification/research/05_compact_survival/audit_finite_certificates.py)

**限制：** Not an unrestricted homology base-change theorem.

<a id="AMP-COMPACT-02"></a>

## AMP-COMPACT-02

General d2<=2d^4 and refined subquartic bounds

**Scope / 范围：** All stated strict-trinomial covers

**Status / 状态：** `historical-weaker-bound`；原证据类型：symbolic corollaries with inherited and geometric dependencies.

**当前采用方式：** 历史较弱界。原较弱估计保留作为证明演进记录；现行主报告优先使用 DIST-UPPER / DIST-TRUNCATED。

**历史较弱界的论证：** [results/notes/A05-compact-survival.md](notes/A05-compact-survival.md)

**限制：** Historical bound; later cubic bound is stronger asymptotically.

<a id="AMP-GLOBAL-01"></a>

## AMP-GLOBAL-01

d2<=32d^3

**Scope / 范围：** General stated strict-trinomial BB double-cover class

**Status / 状态：** `historical-weaker-bound`；原证据类型：symbolic corollary with external geometric dependency.

**当前采用方式：** 历史较弱界。原较弱估计保留作为证明演进记录；现行主报告优先使用 DIST-UPPER / DIST-TRUNCATED。

**历史较弱界的论证：** [results/notes/A06-linear-compact-replacement.md](notes/A06-linear-compact-replacement.md)

**合并后的更新：** Current consolidated constants are in DIST-UPPER and DIST-TRUNCATED.

**限制：** Polynomial in d, not a finite universal amplification constant.

<a id="AMP-GLOBAL-02"></a>

## AMP-GLOBAL-02

Gamma(N)<=24 sqrt(N)

**Scope / 范围：** N is base physical length

**Status / 状态：** `historical-weaker-bound`；原证据类型：symbolic corollary with external geometric dependency.

**当前采用方式：** 历史较弱界。原较弱估计保留作为证明演进记录；现行主报告优先使用 DIST-UPPER / DIST-TRUNCATED。

**历史较弱界的论证：** [results/notes/A05-compact-survival.md](notes/A05-compact-survival.md)

**合并后的更新：** Current consolidated constants are in DIST-UPPER and DIST-TRUNCATED.

**限制：** Size-dependent; does not prove C_* finite.

<a id="AMP-PATHOLOGY-01"></a>

## AMP-PATHOLOGY-01

A non-BB square-zero deformation loses every compact cover class under specialization while finite H1 remains

**Scope / 范围：** Outside BB trinomial hypotheses

**Status / 状态：** `explicit symbolic negative control`；原证据类型：explicit symbolic negative control.

**当前采用方式：** 目标范围外。非 BB square-zero 变形；可作错误推广的对照，不是目标类反例。

**范围外论证或报告：** [results/notes/A05-compact-survival.md](notes/A05-compact-survival.md)

**程序与数据：** [research/amplification/research/05_compact_survival/mechanism_verification.json](../research/amplification/research/05_compact_survival/mechanism_verification.json)

<a id="AMP-LINEAR-01"></a>

## AMP-LINEAR-01

Compact minimum o*2^(a-b)*3^b*(3^s+1); cover ratios exactly 1,3/2,2

**Scope / 范围：** Torsion–Frobenius normal form with surviving compact image

**Status / 状态：** `symbolic exact theorem`；原证据类型：symbolic exact theorem.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A06-linear-compact-replacement.md](notes/A06-linear-compact-replacement.md)

**程序与数据：** [research/amplification/research/06_linear_compact_replacement/sparse_generator_checks.json](../research/amplification/research/06_linear_compact_replacement/sparse_generator_checks.json) · [research/amplification/research/06_linear_compact_replacement/embedding_checks.json](../research/amplification/research/06_linear_compact_replacement/embedding_checks.json)

**限制：** Universal support weight, not an unqualified statement about every finite logical.

<a id="AMP-LINEAR-02"></a>

## AMP-LINEAR-02

[[18,4,2]] -> [[36,4,4]] realizes compact factor-two sharpness

**Scope / 范围：** Specific matched cover

**Status / 状态：** `exact finite example`；原证据类型：exact finite example.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A06-linear-compact-replacement.md](notes/A06-linear-compact-replacement.md)

**程序与数据：** [research/amplification/research/06_linear_compact_replacement/sharpness_example.json](../research/amplification/research/06_linear_compact_replacement/sharpness_example.json) · [research/amplification/research/06_linear_compact_replacement/verify_sharpness.py](../research/amplification/research/06_linear_compact_replacement/verify_sharpness.py)

<a id="AMP-RANK1-01"></a>

## AMP-RANK1-01

Exact cyclic universal module and compact specialization sequence retain the winding/Tor sector

**Scope / 范围：** Primitive rank-one Laurent setting, stated square-free gcd hypotheses

**Status / 状态：** `symbolic exact module calculation`；原证据类型：symbolic exact module calculation.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A07-rank-one-resonance.md](notes/A07-rank-one-resonance.md)

**程序与数据：** [research/amplification/research/07_rank_one_resonance/structure_certificates.json](../research/amplification/research/07_rank_one_resonance/structure_certificates.json)

<a id="AMP-RANK1-02"></a>

## AMP-RANK1-02

One-sided defects and most two-sided parity patterns satisfy compact factor two

**Scope / 范围：** Primitive rank-one setting; finite nonboundary tests explicit

**Status / 状态：** `symbolic proof`；原证据类型：symbolic proof.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A07-rank-one-resonance.md](notes/A07-rank-one-resonance.md)

**程序与数据：** [research/amplification/research/07_rank_one_resonance/lift_certificates.json](../research/amplification/research/07_rank_one_resonance/lift_certificates.json)

<a id="AMP-RANK1-03"></a>

## AMP-RANK1-03

Remaining odd-order resonance has fixed-slope bound 2m, m=max(|p|,|q|,|p-q|)

**Scope / 范围：** Coprime primitive resonance slopes

**Status / 状态：** `symbolic constructive bound`；原证据类型：symbolic constructive bound.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A07-rank-one-resonance.md](notes/A07-rank-one-resonance.md)

**程序与数据：** [research/amplification/research/07_rank_one_resonance/divided_euler_cases.json](../research/amplification/research/07_rank_one_resonance/divided_euler_cases.json)

**限制：** m is not universally bounded; slope (2,1) gives factor four.

<a id="AMP-RANK1-04"></a>

## AMP-RANK1-04

Along compatible long periods, actual finite distances equal full compact minima

**Scope / 范围：** Fixed Laurent data and stable root divisors, explicit no-winding threshold

**Status / 状态：** `symbolic large-period realization`；原证据类型：symbolic large-period realization.

**当前采用方式：** 按范围采用。只有兼容且足够长的周期可把 full compact minima 识别为有限码距离。

**证明／论证入口：** [results/notes/A07-rank-one-resonance.md](notes/A07-rank-one-resonance.md)

**限制：** Cannot be applied to restricted-sector or fixed-message minima.

<a id="AMP-S21-01"></a>

## AMP-S21-01

Delta<=Delta_e<=2Delta and exact projection/completion formula

**Scope / 范围：** Slope (2,1) hard-core compact setting

**Status / 状态：** `symbolic exact reduction`；原证据类型：symbolic exact reduction.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A08-slope21-shortening.md](notes/A08-slope21-shortening.md)

**程序与数据：** [research/amplification/research/08_slope21_shortening/structure_verification.json](../research/amplification/research/08_slope21_shortening/structure_verification.json)

<a id="AMP-S21-02"></a>

## AMP-S21-02

Exact base full/pure/complement minima 6/12/10; cover full/pure minima 14/16

**Scope / 范围：** The explicitly gauged record example

**Status / 状态：** `exact arbitrary-support compact minima`；原证据类型：exact arbitrary-support compact minima.

**当前采用方式：** 按范围采用。完整/单块/补空间的最小值必须分开；尤其 cover full=14、pure=16。

**证明／论证入口：** [results/notes/A08-slope21-shortening.md](notes/A08-slope21-shortening.md)

**程序与数据：** [research/amplification/research/08_slope21_shortening/exact_results.json](../research/amplification/research/08_slope21_shortening/exact_results.json) · [research/amplification/research/08_slope21_shortening/audit_certificates.py](../research/amplification/research/08_slope21_shortening/audit_certificates.py)

**限制：** 12,10,16 are restricted minima, not new finite BB distances.

<a id="AMP-GRAPH-01"></a>

## AMP-GRAPH-01

Full compact energy is a common-message signed graph; half of the boundary spins eliminate exactly by majority

**Scope / 范围：** Universal slope-(2,1) graph, all messages and boundaries retained

**Status / 状态：** `symbolic exact reduction`；原证据类型：symbolic exact reduction.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A09-joint-completion.md](notes/A09-joint-completion.md)

**程序与数据：** [research/amplification/research/09_joint_completion/graph_verification.json](../research/amplification/research/09_joint_completion/graph_verification.json)

**限制：** Alternating local updates are not claimed globally optimal.

<a id="AMP-GRAPH-02"></a>

## AMP-GRAPH-02

Minimum-support optimal components satisfy b1<=number of sources, with a fixed-message support bound

**Scope / 范围：** Fixed message; no bound on message support

**Status / 状态：** `symbolic proof`；原证据类型：symbolic proof.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A09-joint-completion.md](notes/A09-joint-completion.md)

**程序与数据：** [research/amplification/research/09_joint_completion/component_verification.json](../research/amplification/research/09_joint_completion/component_verification.json)

<a id="AMP-PARETO-01"></a>

## AMP-PARETO-01

Complete projected-weight/completion frontier {(12,1),(14,0)}

**Scope / 范围：** Record example

**Status / 状态：** `exact Pareto theorem with inherited closure certificates`；原证据类型：exact Pareto theorem with inherited closure certificates.

**当前采用方式：** 按范围采用。指定实例的 Pareto frontier；须连同 closure 证书与完整消息优化范围引用。

**证明／论证入口：** [results/notes/A09-joint-completion.md](notes/A09-joint-completion.md)

**程序与数据：** [research/amplification/research/09_joint_completion/pareto_verification.json](../research/amplification/research/09_joint_completion/pareto_verification.json) · [research/amplification/research/09_joint_completion/verify_pareto.py](../research/amplification/research/09_joint_completion/verify_pareto.py)

<a id="AMP-MAJORITY-01"></a>

## AMP-MAJORITY-01

Weight-182 locally stable circuit boundary gives restricted output 550>546

**Scope / 范围：** Input is explicitly a boundary

**Status / 状态：** `exact counterexample to a restricted majority assertion`；原证据类型：exact counterexample to a restricted majority assertion.

**当前采用方式：** 有效否定结果。局部稳定 boundary 否定受限 majority 断言，不是最短非边界反例。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/A09-joint-completion.md](notes/A09-joint-completion.md)

**程序与数据：** [research/amplification/research/09_joint_completion/majority_control_verification.json](../research/amplification/research/09_joint_completion/majority_control_verification.json)

**限制：** Not a counterexample for a minimum nonboundary or full cover distance.

<a id="AMP-TREE-01"></a>

## AMP-TREE-01

Two local equations exactly characterize common-message data

**Scope / 范围：** Laurent PID slope-(2,1) setting

**Status / 状态：** `symbolic exact characterization`；原证据类型：symbolic exact characterization.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A10-nonlocal-exchange.md](notes/A10-nonlocal-exchange.md)

**程序与数据：** [research/amplification/research/10_nonlocal_exchange/identity_verification.json](../research/amplification/research/10_nonlocal_exchange/identity_verification.json)

<a id="AMP-TREE-02"></a>

## AMP-TREE-02

Canonical nonsource trees contract to all-or-nothing two-unit rewards; full fixed-message field optimum is independent-set packing

**Scope / 范围：** All source assignments and boundary fields, fixed common-message input

**Status / 状态：** `symbolic exact reduction`；原证据类型：symbolic exact reduction.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/A10-nonlocal-exchange.md](notes/A10-nonlocal-exchange.md)

**程序与数据：** [research/amplification/research/10_nonlocal_exchange/forest_verification.json](../research/amplification/research/10_nonlocal_exchange/forest_verification.json) · [research/amplification/research/10_nonlocal_exchange/tree_contraction_verification.json](../research/amplification/research/10_nonlocal_exchange/tree_contraction_verification.json)

<a id="AMP-TREE-03"></a>

## AMP-TREE-03

A genuine compact message produces a triangular conflict graph

**Scope / 范围：** Not a minimum-distance assertion

**Status / 状态：** `exact constructive negative control`；原证据类型：exact constructive negative control.

**当前采用方式：** 有效否定结果。冲突图可含三角形；只能否定所提简单图结构捷径。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/A10-nonlocal-exchange.md](notes/A10-nonlocal-exchange.md)

**程序与数据：** [research/amplification/research/10_nonlocal_exchange/triangle_certificate.json](../research/amplification/research/10_nonlocal_exchange/triangle_certificate.json) · [research/amplification/research/10_nonlocal_exchange/audit_triangle.py](../research/amplification/research/10_nonlocal_exchange/audit_triangle.py)

<a id="AMP-TREE-04"></a>

## AMP-TREE-04

Fixed-message minimum 74 with support 15; same universal class has full minimum 14

**Scope / 范围：** One explicit message in the record code

**Status / 状态：** `exact conditional minimum plus unrestricted inherited certificate`；原证据类型：exact conditional minimum plus unrestricted inherited certificate.

**当前采用方式：** 有效否定结果。固定消息最小重量 74；同一类的完整最小重量为 14，不能把 74 当码距。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/A10-nonlocal-exchange.md](notes/A10-nonlocal-exchange.md)

**程序与数据：** [research/amplification/research/10_nonlocal_exchange/fixed_message_certificate.json](../research/amplification/research/10_nonlocal_exchange/fixed_message_certificate.json) · [research/amplification/research/10_nonlocal_exchange/fixed_message_potential.bin](../research/amplification/research/10_nonlocal_exchange/fixed_message_potential.bin) · [research/amplification/research/10_nonlocal_exchange/audit_fixed_certificate.py](../research/amplification/research/10_nonlocal_exchange/audit_fixed_certificate.py)

**限制：** 74 is not code distance; explicit boundary to 14 retained.

<a id="AMP-TREE-05"></a>

## AMP-TREE-05

For positive odd N, conditional minimum 74N and support 15N in one universal class of minimum 14

**Scope / 范围：** Separated messages in one fixed code

**Status / 状态：** `symbolic parametric negative control`；原证据类型：symbolic parametric negative control.

**当前采用方式：** 有效否定结果。固定消息重量 74N 随 N 增长；同一固定码仍有重量 14 代表，不是无界升距族。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/A10-nonlocal-exchange.md](notes/A10-nonlocal-exchange.md)

**程序与数据：** [research/amplification/research/10_nonlocal_exchange/parametric_verification.json](../research/amplification/research/10_nonlocal_exchange/parametric_verification.json)

**限制：** Not an increasing-distance family.

<a id="AMP-OPEN-01"></a>

## AMP-OPEN-01

Full slope-(2,1) hat-Delta<=3Delta

**Scope / 范围：** All admissible compact messages and all boundary adjustments

**Status / 状态：** `open conjecture`；原证据类型：open conjecture.

**当前采用方式：** 未决问题。在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。

**问题出处（不是证明）：** [results/notes/A10-nonlocal-exchange.md](notes/A10-nonlocal-exchange.md)

**限制：** Neither proved nor refuted; inherited bound is four.

<a id="AMP-OPEN-02"></a>

## AMP-OPEN-02

Half-weight completion after a minimum base class and boundary adjustment

**Scope / 范围：** Stronger class-pinned statement

**Status / 状态：** `open sufficient lemma`；原证据类型：open sufficient lemma.

**当前采用方式：** 未决问题。在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。

**问题出处（不是证明）：** [results/notes/A09-joint-completion.md](notes/A09-joint-completion.md)

**限制：** Failure would not by itself refute OPEN-01.

<a id="AMP-OPEN-03"></a>

## AMP-OPEN-03

Finiteness or infiniteness of C_*

**Scope / 范围：** Entire stated strict-trinomial BB double-cover class

**Status / 状态：** `open problem`；原证据类型：open problem.

**当前采用方式：** 未决问题。在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。

**问题出处（不是证明）：** [research/amplification/docs/OPEN_PROBLEMS.md](../research/amplification/docs/OPEN_PROBLEMS.md)

**限制：** No numerical universal linear upper bound and no unbounded-ratio family established.

<a id="DEG-A00"></a>

## DEG-A00

Four-term family [[8a^2+4a,2,2a+1]] -> [[16a^2+8a,4,2]] for a>=2.

**Scope / 范围：** Arbitrary-term extension, exactly four terms each.

**Status / 状态：** `reported-proof-only`；原证据类型：reported-proof-only.

**当前采用方式：** 目标范围外。四项式族，不满足严格三项式条件；同时原验证包未恢复。

**范围外论证或报告：** [results/notes/X00-beyond-trinomials.md](notes/X00-beyond-trinomials.md)

**限制：** Original source/verifier/output package absent; public derivation retained. Not a strict-trinomial construction.

<a id="DEG-A01"></a>

## DEG-A01

gamma_all(N)=Theta(N^-1), with 4/N <= gamma_all(N) < 160/N for sufficiently large N.

**Scope / 范围：** Term counts may grow.

**Status / 状态：** `reported-proof-only`；原证据类型：reported-proof-only.

**当前采用方式：** 目标范围外。允许任意项数的 Θ(N⁻¹) 结论，不是严格三项式结论；同时原验证包未恢复。

**范围外论证或报告：** [results/notes/X00-beyond-trinomials.md](notes/X00-beyond-trinomials.md)

**限制：** Not a result for the strict-trinomial class; source code package absent.

<a id="DEG-I01"></a>

## DEG-I01

[[78,4,6]] -> [[156,4,14]], ratio 7/3, for the supplied A,B and periods 39->78.

**Scope / 范围：** Reported strict-trinomial finite example.

**Status / 状态：** `finite-certificate-repaired`；原证据类型：inherited-input.

**当前采用方式：** 按范围采用。旧“证书缺失”已修复，当前采用 CEX-UP；原限制只保留在历史记录中。

**证明／论证入口：** [results/theory/01-counterexamples.md](theory/01-counterexamples.md) · [certificates/upper/CERTIFICATE.md](../certificates/upper/CERTIFICATE.md)

**已记录的主要依赖：** [CEX-UP](#CEX-UP)

**旧版本限制（已被上面的当前状态修正）：** Independent exact-distance certificates are not present in the available filesystem.

**合并后的更新：** The third input ZIP supplies two independent exact verifiers. See CEX-UP; the original missing-certificate note is historical.

**限制：** The original missing-certificate note is superseded for this finite example; use CEX-UP. This duplicate entry is not an additional counterexample.

**未公开或未恢复的历史路径（不是可用证据链接）：** `research/degradation/context/conversation/INHERITED_INPUTS.md`, `research/degradation/context/input/Pasted text.txt`

<a id="DEG-I02"></a>

## DEG-I02

[[156,4,14]] -> [[312,8,12]] and the stated infinite 14->12 family; ratio 6/7.

**Scope / 范围：** Reported strict-trinomial degrading covers.

**Status / 状态：** `finite-certificate-repaired-family-inherited`；原证据类型：inherited-input.

**当前采用方式：** 证据或依赖待补。本条把已认证有限 14→12 例与未恢复的无限族合写；有限部分使用 CEX-DOWN，不能整体升级。

**恢复论证或继承输入（证据链尚有缺口）：** [results/theory/01-counterexamples.md](theory/01-counterexamples.md) · [certificates/lower/CERTIFICATE.md](../certificates/lower/CERTIFICATE.md) · [results/HISTORY_AND_LIMITS.md](HISTORY_AND_LIMITS.md)

**已记录的主要依赖：** [CEX-DOWN](#CEX-DOWN)

**旧版本限制（已被上面的当前状态修正）：** Early report checks a weight-12 nonboundary and dimensions, not both exact distances. Later stages inherit exactness; original independent source package absent.

**合并后的更新：** The finite 14->12 example is repaired by CEX-DOWN; the entire inherited infinite family is not upgraded by testing that seed.

**限制：** The finite example is fully certified as CEX-DOWN; the inherited infinite family remains evidence-limited. Do not promote the combined entry wholesale.

**未公开或未恢复的历史路径（不是可用证据链接）：** `research/degradation/context/input/Pasted text.txt`, `research/degradation/context/input/Pasted markdown.md`, `research/degradation/context/conversation/INHERITED_INPUTS.md`

<a id="DEG-I03"></a>

## DEG-I03

d>4 implies d_2>=6, with the stated stronger no-small-cycle fact.

**Scope / 范围：** Strict-trinomial starting assumptions.

**Status / 状态：** `inherited-input`；原证据类型：inherited-input.

**当前采用方式：** 证据或依赖待补。早期 weight-two/weight-four 排除及 stronger no-small-cycle 输入包未恢复。

**恢复论证或继承输入（证据链尚有缺口）：** [results/HISTORY_AND_LIMITS.md](HISTORY_AND_LIMITS.md)

**限制：** Prior weight-two/weight-four package unavailable; preserve the original supplied scope.

**未公开或未恢复的历史路径（不是可用证据链接）：** `research/degradation/context/input/Pasted markdown.md`

<a id="DEG-D01"></a>

## DEG-D01

d_2=6 implies d<=56; combined with the stated small-weight inputs, d>56 implies d_2>=8.

**Scope / 范围：** All valid strict-trinomial double covers in the supplied proof.

**Status / 状态：** `computer-assisted-theorem`；原证据类型：computer-assisted-theorem.

**当前采用方式：** 证据或依赖待补。原定理明确以起始 weight-four 排除为条件；本次没有补证该输入，d₂=6⇒d≤56 不作无条件主结论。

**恢复论证或继承输入（证据链尚有缺口）：** [results/notes/D01-weight-six.md](notes/D01-weight-six.md)

**已记录的主要依赖：** [DEG-I03](#DEG-I03)

**程序与数据：** [research/degradation/research/01-weight-six/mixed_presentations.tsv](../research/degradation/research/01-weight-six/mixed_presentations.tsv) · [research/degradation/research/01-weight-six/presentation_verification.json](../research/degradation/research/01-weight-six/presentation_verification.json) · [research/degradation/research/01-weight-six/pure_six_results.json](../research/degradation/research/01-weight-six/pure_six_results.json) · [research/degradation/research/01-weight-six/classify_six.cpp](../research/degradation/research/01-weight-six/classify_six.cpp) · [research/degradation/research/01-weight-six/verify_presentations.py](../research/degradation/research/01-weight-six/verify_presentations.py)

**限制：** Uniform conclusion requires the proof and exhaustive completeness argument, not only retained-catalogue checking.

<a id="DEG-D02"></a>

## DEG-D02

The weight-six two-check coefficient-filling lemma is false. For L=4^j, |q|=6 and minimum coefficient filling is 3*9^j.

**Scope / 范围：** Explicit connected strict-trinomial family; L<=d<=4L.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 有效否定结果。常重量 boundary 的 coefficient filling 可发散；线性支撑填充引理为假。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/D01-weight-six.md](notes/D01-weight-six.md)

**程序与数据：** [research/degradation/research/01-weight-six/verify_family.py](../research/degradation/research/01-weight-six/verify_family.py) · [research/degradation/research/01-weight-six/family_verification.json](../research/degradation/research/01-weight-six/family_verification.json)

**限制：** Base distances are intervals, not asserted exact distances.

<a id="DEG-D03"></a>

## DEG-D03

For that specified cover, 2+2*9^j <= Fill(q) <= 6+6*9^j.

**Scope / 范围：** Lifted filling of the particular weight-six boundary.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 有效否定结果。特定 boundary 的最小提升重量可发散；不能推出整码距离退化。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/D01-weight-six.md](notes/D01-weight-six.md)

**程序与数据：** [research/degradation/research/01-weight-six/family_verification.json](../research/degradation/research/01-weight-six/family_verification.json)

**限制：** Every cover cycle above that q also obeys the lower bound. Not a vanishing-ratio family.

<a id="DEG-D04"></a>

## DEG-D04

d_2=8 implies d<=96.

**Scope / 范围：** Term-preserving finite abelian quotients with positive-dimensional base, not only doubles.

**Status / 状态：** `computer-assisted-theorem`；原证据类型：computer-assisted-theorem.

**当前采用方式：** 按范围采用。d₂=8⇒d≤96 的正文明确独立于早期小重量输入；组合 d>96⇒d₂≥10 则仍需该输入。

**证明／论证入口：** [results/notes/D02-weight-eight.md](notes/D02-weight-eight.md)

**程序与数据：** [research/degradation/research/02-weight-eight/verification_summary.json](../research/degradation/research/02-weight-eight/verification_summary.json) · [research/degradation/research/02-weight-eight/highrank_certificates.json](../research/degradation/research/02-weight-eight/highrank_certificates.json) · [research/degradation/research/02-weight-eight/low_free_lattices.tsv](../research/degradation/research/02-weight-eight/low_free_lattices.tsv) · [research/degradation/research/02-weight-eight/verify_summary.py](../research/degradation/research/02-weight-eight/verify_summary.py)

**限制：** No new exact ratio record. Combined d>96 => d_2>=10 uses earlier exclusions.

<a id="DEG-D05"></a>

## DEG-D05

d<=4*d_2^3.

**Scope / 范围：** Strict-trinomial doubles, extended as stated to finite abelian quotients with 2-group kernel.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。与 DIST-LOWER 是同一三次退化结论的原支线登记，不能重复计算成果。

**证明／论证入口：** [results/notes/D03-structural-degradation.md](notes/D03-structural-degradation.md)

**已记录的主要依赖：** [DIST-LOWER](#DIST-LOWER)

**程序与数据：** [research/degradation/research/03-structural-degradation/verification_summary.json](../research/degradation/research/03-structural-degradation/verification_summary.json)

**限制：** Symbolic theorem independent of earlier incidence catalogues; finite tests are not its proof.

<a id="DEG-D06"></a>

## DEG-D06

gamma_3(N)>=max(min(1/12,20/N),N^(-2/3),pi*3^(1/6)/(2^(13/3)*sqrt(N))).

**Scope / 范围：** Degradation scale; first term uses earlier small-weight inputs.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 证据或依赖待补。min(1/12,20/N) 项依赖早期小重量输入；不依赖该输入的其余部分另列于 DIST-TRUNCATED。

**恢复论证或继承输入（证据链尚有缺口）：** [results/notes/D03-structural-degradation.md](notes/D03-structural-degradation.md)

**已记录的主要依赖：** [DEG-I03](#DEG-I03) · [DEG-D01](#DEG-D01) · [DEG-D04](#DEG-D04)

**程序与数据：** [research/degradation/research/03-structural-degradation/verify_geometry.py](../research/degradation/research/03-structural-degradation/verify_geometry.py) · [research/degradation/research/03-structural-degradation/geometry_verification.json](../research/degradation/research/03-structural-degradation/geometry_verification.json)

**限制：** Not a positive universal ratio and not a sharp asymptotic equivalence.

<a id="DEG-D07"></a>

## DEG-D07

Compact projection is injective for support-generated rank-one odd-torsion presentations under the stated 2-group quotients.

**Scope / 范围：** Compact homology image; gives linear descent for a nonboundary compact lift.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/D04-quadratic-bottleneck.md](notes/D04-quadratic-bottleneck.md)

**程序与数据：** [research/degradation/research/04-quadratic-bottleneck/verify.py](../research/degradation/research/04-quadratic-bottleneck/verify.py) · [research/degradation/research/04-quadratic-bottleneck/verify_independent.py](../research/degradation/research/04-quadratic-bottleneck/verify_independent.py) · [research/degradation/research/04-quadratic-bottleneck/cases.json](../research/degradation/research/04-quadratic-bottleneck/cases.json)

**限制：** Not a statement that all finite homology is compact. Visible 2-primary torsion remains.

<a id="DEG-D08"></a>

## DEG-D08

Short relation rows do not imply a quadratic cofactor bound; changing their integral basis does not repair the example.

**Scope / 范围：** Saturated rank-one lattice example.

**Status / 状态：** `disproved-approach`；原证据类型：disproved-approach.

**当前采用方式：** 有效否定结果。短关系行不保证二次 cofactor 界；格对照例不是码距离反例。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/D04-quadratic-bottleneck.md](notes/D04-quadratic-bottleneck.md)

**程序与数据：** [research/degradation/research/04-quadratic-bottleneck/summary.json](../research/degradation/research/04-quadratic-bottleneck/summary.json)

**限制：** Not an actual code-distance counterexample.

<a id="DEG-D09"></a>

## DEG-D09

A torsion-changing strict-trinomial quotient can kill the compact image even when universal H1 is simple/semisimple.

**Scope / 范围：** Specified C3 x C2 x Z example and its finite realization.

**Status / 状态：** `disproved-approach`；原证据类型：disproved-approach.

**当前采用方式：** 有效否定结果。改变 torsion 可杀死 compact image；不能假设所有 specialization 保持存活。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/D04-quadratic-bottleneck.md](notes/D04-quadratic-bottleneck.md)

**程序与数据：** [research/degradation/research/04-quadratic-bottleneck/verify.py](../research/degradation/research/04-quadratic-bottleneck/verify.py) · [research/degradation/research/04-quadratic-bottleneck/summary.json](../research/degradation/research/04-quadratic-bottleneck/summary.json)

**限制：** Not a degradation counterfamily; there is an independent short base logical.

<a id="DEG-D10"></a>

## DEG-D10

For principal-period doubles, compact loss is fH1/f^2H1; the cyclic-torsion subclass has the specified exact gcd criterion.

**Scope / 范围：** Requires the stated nonzerodivisor-period hypotheses.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/D04-quadratic-bottleneck.md](notes/D04-quadratic-bottleneck.md)

**程序与数据：** [research/degradation/research/04-quadratic-bottleneck/verify_cyclic_strip.py](../research/degradation/research/04-quadratic-bottleneck/verify_cyclic_strip.py) · [research/degradation/research/04-quadratic-bottleneck/cyclic_strip_cases.json](../research/degradation/research/04-quadratic-bottleneck/cyclic_strip_cases.json)

**限制：** The specialization-created term remains separate; not applicable unchanged to a zerodivisor torsion quotient.

<a id="DEG-D11"></a>

## DEG-D11

Active finite local H1 is N_m^2, H0=H2=N_m; m has one or two nonzero binary digits, with the stated cover projection and transfer forms.

**Scope / 范围：** Actual support-generated finite BB groups of rank at most two.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/D05-visible-two-primary.md](notes/D05-visible-two-primary.md)

**程序与数据：** [research/degradation/research/05-visible-two-primary/local_cases.json](../research/degradation/research/05-visible-two-primary/local_cases.json) · [research/degradation/research/05-visible-two-primary/structured_verification.json](../research/degradation/research/05-visible-two-primary/structured_verification.json) · [research/degradation/research/05-visible-two-primary/verify_local.py](../research/degradation/research/05-visible-two-primary/verify_local.py)

**限制：** Not arbitrary universal rank-four incidence groups; normalizing maps are not Hamming isometries.

<a id="DEG-D12"></a>

## DEG-D12

High-contact family has exact base distance 4 and cover distance at most 6, despite unbounded nilpotent lengths.

**Scope / 范围：** Q=4^j family; parameters and hypotheses in source.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/D05-visible-two-primary.md](notes/D05-visible-two-primary.md)

**程序与数据：** [research/degradation/research/05-visible-two-primary/verify_family.py](../research/degradation/research/05-visible-two-primary/verify_family.py) · [research/degradation/research/05-visible-two-primary/family_verification.json](../research/degradation/research/05-visible-two-primary/family_verification.json)

**限制：** No exact cover distance claimed; not an unbounded-degradation family.

<a id="DEG-D13"></a>

## DEG-D13

d<=3*d_2^2 for the deck-involution strip subclass.

**Scope / 范围：** Requires a weight-preserving compact incidence lift over T_odd x C2 x Z, with that involution mapping to the actual deck transformation.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。d≤3d₂² 只用于指定 deck-involution strip 子类，不能改写成一般二次退化界。

**证明／论证入口：** [results/notes/D06-sparse-deck-descent.md](notes/D06-sparse-deck-descent.md) · [research/degradation/research/06-sparse-deck-descent/audit.md](../research/degradation/research/06-sparse-deck-descent/audit.md)

**程序与数据：** [research/degradation/research/06-sparse-deck-descent/verify.py](../research/degradation/research/06-sparse-deck-descent/verify.py) · [research/degradation/research/06-sparse-deck-descent/cases.json](../research/degradation/research/06-sparse-deck-descent/cases.json)

**限制：** Not a global quadratic theorem; retained-involution period doubles and higher/finite incidence mechanisms remain outside.

<a id="DEG-D14"></a>

## DEG-D14

The deck-killing derivative operator can have nonzero syndrome in a retained-involution base.

**Scope / 范围：** Exact unchanged-check odd-period family in source.

**Status / 状态：** `disproved-approach`；原证据类型：disproved-approach.

**当前采用方式：** 有效否定结果。导数候选在 retained-involution 底码可有非零 syndrome，不能直接当 logical。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/D06-sparse-deck-descent.md](notes/D06-sparse-deck-descent.md)

**程序与数据：** [research/degradation/research/06-sparse-deck-descent/verification_summary.json](../research/degradation/research/06-sparse-deck-descent/verification_summary.json)

**限制：** Its weight-14 kernel witness is not minimum; an independent base logical has weight at most 8.

<a id="DEG-P01"></a>

## DEG-P01

Every universal physical cover cycle is parameterized by k,h; finite compact nonboundary is exactly g_plus not dividing k.

**Scope / 范围：** No-universal-torsion rank-one setting, including the stated split/nonsplit seams.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/D07-rank-one-amplification.md](notes/D07-rank-one-amplification.md) · [research/degradation/research/07-rank-one-amplification/audit.md](../research/degradation/research/07-rank-one-amplification/audit.md)

**程序与数据：** [research/degradation/research/07-rank-one-amplification/verify.py](../research/degradation/research/07-rank-one-amplification/verify.py)

**限制：** Retains separate specialization-created finite homology. No conclusion for arbitrary torsion presentations.

<a id="DEG-P02"></a>

## DEG-P02

Factor-three and factor-two replacement bounds hold for the specified single-parity and other resolved voltage subclasses.

**Scope / 范围：** Precise normalization and parity hypotheses in Sections 3-5.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/D07-rank-one-amplification.md](notes/D07-rank-one-amplification.md)

**程序与数据：** [research/degradation/research/07-rank-one-amplification/verification_summary.json](../research/degradation/research/07-rank-one-amplification/verification_summary.json)

**限制：** Not the entire residual mixed-parity inequality.

<a id="DEG-P03"></a>

## DEG-P03

Along fixed compatible gcd data and sufficiently large periods, d=mu0 and d_2=mu_plus.

**Scope / 范围：** Period stabilization for the exact full Laurent minima.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/D07-rank-one-amplification.md](notes/D07-rank-one-amplification.md) · [research/degradation/research/07-rank-one-amplification/audit.md](../research/degradation/research/07-rank-one-amplification/audit.md)

**限制：** Does not assert equality for arbitrary short periods.

<a id="DEG-P04"></a>

## DEG-P04

mu0=8 and mu_plus=14 for A=1+z^2+z^7, B=1+z+z^8 with the stated twists.

**Scope / 范围：** All Laurent degrees and all admissible messages/boundaries.

**Status / 状态：** `exact-minimum-certificate`；原证据类型：exact-minimum-certificate.

**当前采用方式：** 按范围采用。all-degree Bellman 证书支持完整 Laurent 最小值 8/14；不能只靠有限矩阵扫描。

**证明／论证入口：** 本条没有单独文本入口；证书型条目见下面的数据与验证器，缺失型条目见其限制。

**程序与数据：** [research/degradation/research/07-rank-one-amplification/family_certificate.json](../research/degradation/research/07-rank-one-amplification/family_certificate.json) · [research/degradation/research/07-rank-one-amplification/base_potential.bin](../research/degradation/research/07-rank-one-amplification/base_potential.bin) · [research/degradation/research/07-rank-one-amplification/cover_potential.bin](../research/degradation/research/07-rank-one-amplification/cover_potential.bin) · [research/degradation/research/07-rank-one-amplification/verify.py](../research/degradation/research/07-rank-one-amplification/verify.py)

**限制：** Independent Bellman edge checking gives the all-degree lower bounds. Finite matrix tests alone would not suffice.

<a id="DEG-P05"></a>

## DEG-P05

[[2L,4,8]] -> [[4L,4,14]] for odd multiples of 3 with L>=105.

**Scope / 范围：** Combination of P03 and P04 in the supplied proof.

**Status / 状态：** `symbolic-plus-exact-minimum-certificate`；原证据类型：symbolic-plus-exact-minimum-certificate.

**当前采用方式：** 按范围采用。稳定化条件 L≥105、奇数且 3|L 下的 8→14 族；比值 7/4 不是新纪录。

**证明／论证入口：** [results/notes/D07-rank-one-amplification.md](notes/D07-rank-one-amplification.md)

**已记录的主要依赖：** [DEG-P03](#DEG-P03) · [DEG-P04](#DEG-P04)

**程序与数据：** [research/degradation/research/07-rank-one-amplification/family_certificate.json](../research/degradation/research/07-rank-one-amplification/family_certificate.json) · [research/degradation/research/07-rank-one-amplification/verify.py](../research/degradation/research/07-rank-one-amplification/verify.py)

**限制：** Ratio 7/4 is not a new record or unbounded-amplification result.

<a id="DEG-P06"></a>

## DEG-P06

The naive Frobenius weight-at-most-3w candidate is a multiplier of transfer and is killed whenever that transfer is killed.

**Scope / 范围：** Exact physical and homology identity.

**Status / 状态：** `disproved-approach`；原证据类型：disproved-approach.

**当前采用方式：** 有效否定结果。naive Frobenius 候选是 transfer 的倍数，会与被杀死的 transfer 一起消失。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/D07-rank-one-amplification.md](notes/D07-rank-one-amplification.md)

**程序与数据：** [research/degradation/research/07-rank-one-amplification/verify.py](../research/degradation/research/07-rank-one-amplification/verify.py)

**限制：** Disproves the proposed nonboundary argument, not factor three.

<a id="DEG-P07"></a>

## DEG-P07

For the specified arithmetic-progression mixed pairs, a+b<=mu0 and a+b<=mu_plus<=2(a+b); hence mu_plus<=2mu0.

**Scope / 范围：** a,b>0, distinct and coprime; both congruent 1 or both 5 modulo 6.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/D08-mixed-laurent.md](notes/D08-mixed-laurent.md)

**程序与数据：** [research/degradation/research/08-mixed-laurent/verify.py](../research/degradation/research/08-mixed-laurent/verify.py) · [research/degradation/research/08-mixed-laurent/verification_summary.json](../research/degradation/research/08-mixed-laurent/verification_summary.json)

**限制：** Not exact distances for every pair and not the full mixed-parity class.

<a id="DEG-P08"></a>

## DEG-P08

The four-term message cancellation family beats the constant message by a growing additive gap.

**Scope / 范围：** Explicit B_j,F_j polynomial identity for all j>=0.

**Status / 状态：** `disproved-approach`；原证据类型：disproved-approach.

**当前采用方式：** 有效否定结果。常消息可被非常消息改进，否定常消息最优捷径；尚未求得完整覆盖最小值。

**否定结果的论证（不可反向采用被否定的路线）：** [results/notes/D08-mixed-laurent.md](notes/D08-mixed-laurent.md)

**程序与数据：** [research/degradation/research/08-mixed-laurent/verify.py](../research/degradation/research/08-mixed-laurent/verify.py) · [research/degradation/research/08-mixed-laurent/verification_summary.json](../research/degradation/research/08-mixed-laurent/verification_summary.json)

**限制：** Only constructed message weights; not complete minima and not a factor-three counterexample.

<a id="DEG-P09"></a>

## DEG-P09

The fixed-c parameterization has an exact systematic four-output and off-support penalty form.

**Scope / 范围：** All Laurent messages and boundary adjustments retained.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/D08-mixed-laurent.md](notes/D08-mixed-laurent.md)

**程序与数据：** [research/degradation/research/08-mixed-laurent/audit.py](../research/degradation/research/08-mixed-laurent/audit.py)

**限制：** No restriction to base-minimizing F or fixed H is justified by the reformulation.

<a id="DEG-P10"></a>

## DEG-P10

mu0=10 for the small arithmetic-progression pair a=1,b=7.

**Scope / 范围：** Specific base Laurent minimum.

**Status / 状态：** `symbolic-exact-small-minimum`；原证据类型：symbolic-exact-small-minimum.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/D08-mixed-laurent.md](notes/D08-mixed-laurent.md)

**程序与数据：** [research/degradation/research/08-mixed-laurent/verification_summary.json](../research/degradation/research/08-mixed-laurent/verification_summary.json)

**限制：** Not an exact cover minimum or a new finite ratio record.

<a id="DEG-P11"></a>

## DEG-P11

span(B)<=4 wt(F) wt((B/c)F) for every c-nondivisible Laurent F.

**Scope / 范围：** Fixed c=1+z+z^2; E=6r+2 and O=6t+1, including negative exponents.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/D09-fixed-c-product-bound.md](notes/D09-fixed-c-product-bound.md)

**程序与数据：** [research/degradation/research/09-fixed-c-product-bound/verify.py](../research/degradation/research/09-fixed-c-product-bound/verify.py) · [research/degradation/research/09-fixed-c-product-bound/verification_summary.json](../research/degradation/research/09-fixed-c-product-bound/verification_summary.json)

**限制：** Not a linear uncertainty bound. Uses actual strict-trinomial support structure.

<a id="DEG-P12"></a>

## DEG-P12

mu_plus<=mu0^2+2, and <=mu0^2 for positive E,O.

**Scope / 范围：** Full fixed-c Laurent minima; finite consequences only in the inherited stabilized regime.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。fixed-c 的 μ₊≤μ₀²+2；不是一般 d≤Cd₂²，也不是全局线性放大。

**证明／论证入口：** [results/notes/D09-fixed-c-product-bound.md](notes/D09-fixed-c-product-bound.md) · [research/degradation/research/09-fixed-c-product-bound/audit.md](../research/degradation/research/09-fixed-c-product-bound/audit.md)

**限制：** Not a global BB amplification bound and not the degradation inequality d<=C*d_2^2.

<a id="DEG-P13"></a>

## DEG-P13

All 12 admissible cover residue classes are physical monomial translates, yielding exact unrestricted boundary-coset minimizations.

**Scope / 范围：** Fixed c, actual monomial basis.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/D09-fixed-c-product-bound.md](notes/D09-fixed-c-product-bound.md)

**程序与数据：** [research/degradation/research/09-fixed-c-product-bound/verify.py](../research/degradation/research/09-fixed-c-product-bound/verify.py)

**限制：** The boundary variable remains arbitrary; does not imply constant-message optimality.

<a id="DEG-P14"></a>

## DEG-P14

A factor-three violation requires mu0 < (wt(b)+1)/2; unbounded ratios require both minimizing block weights to diverge.

**Scope / 范围：** Necessary conditions for the fixed-c strict-trinomial case.

**Status / 状态：** `symbolic-proof-and-exact-checks`；原证据类型：symbolic-proof-and-exact-checks.

**当前采用方式：** 按范围采用。按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。

**证明／论证入口：** [results/notes/D09-fixed-c-product-bound.md](notes/D09-fixed-c-product-bound.md)

**限制：** Necessary is not sufficient; still need a full cover lower bound.

<a id="DEG-P15"></a>

## DEG-P15

The relaxed systematic problem has exact minima mu0=2, mu_plus=4N+2 for all N>=1.

**Scope / 范围：** Second lifted numerator has five supported terms.

**Status / 状态：** `exact-inadmissible-counterfamily`；原证据类型：exact-inadmissible-counterfamily.

**当前采用方式：** 目标范围外。第二个提升分子有五项，违反目标类的逐项三项匹配。

**范围外论证或报告：** [results/notes/D09-fixed-c-product-bound.md](notes/D09-fixed-c-product-bound.md) · [research/degradation/research/09-fixed-c-product-bound/audit.md](../research/degradation/research/09-fixed-c-product-bound/audit.md)

**程序与数据：** [research/degradation/research/09-fixed-c-product-bound/verify.py](../research/degradation/research/09-fixed-c-product-bound/verify.py)

**限制：** Invalid strict-trinomial termwise support matching. Not a target BB-cover counterexample.

<a id="DEG-O01"></a>

## DEG-O01

Universal strict-trinomial positive degradation constant, or a strict-trinomial family with d->infinity and d_2/d->0.

**Scope / 范围：** Global degradation question.

**Status / 状态：** `open`；原证据类型：open.

**当前采用方式：** 未决问题。在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。

**问题出处（不是证明）：** [results/notes/D03-structural-degradation.md](notes/D03-structural-degradation.md)

**限制：** Neither established in the available record.

<a id="DEG-O02"></a>

## DEG-O02

Universal quadratic degradation improvement d<=C*d_2^2.

**Scope / 范围：** Mixed finite/strip visible-2-primary obstruction outside the proved subclasses.

**Status / 状态：** `open`；原证据类型：open.

**当前采用方式：** 未决问题。在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。

**问题出处（不是证明）：** [results/notes/D06-sparse-deck-descent.md](notes/D06-sparse-deck-descent.md)

**限制：** Finite-local classification and the deck-involution subclass do not settle the global statement.

<a id="DEG-O03"></a>

## DEG-O03

mu_plus<=3*mu0 for all remaining fixed-c mixed-parity pairs.

**Scope / 范围：** Full F,H Laurent optimization.

**Status / 状态：** `open`；原证据类型：open.

**当前采用方式：** 未决问题。在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。

**问题出处（不是证明）：** [results/notes/D09-fixed-c-product-bound.md](notes/D09-fixed-c-product-bound.md)

**限制：** Unproved and unrefuted; no certified strict-trinomial full-minimum violation.

<a id="DEG-O04"></a>

## DEG-O04

Half-generator lower bound mu0 >= (wt(b)+1)/2.

**Scope / 范围：** Sufficient proposed fixed-c lemma.

**Status / 状态：** `open`；原证据类型：open.

**当前采用方式：** 未决问题。在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。

**问题出处（不是证明）：** [results/notes/D09-fixed-c-product-bound.md](notes/D09-fixed-c-product-bound.md)

**限制：** Unproved and unrefuted. Its failure alone would not prove factor-three failure.

<a id="DEG-O05"></a>

## DEG-O05

Finiteness of C_*=sup d_2/d.

**Scope / 范围：** Global amplification including remaining rank-one torsion and other mechanisms.

**Status / 状态：** `open`；原证据类型：open.

**当前采用方式：** 未决问题。在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。

**问题出处（不是证明）：** [results/notes/D09-fixed-c-product-bound.md](notes/D09-fixed-c-product-bound.md)

**限制：** No global universal linear bound or admissible unbounded-ratio family established here.

<a id="DEG-I04"></a>

## DEG-I04

Genuinely higher-rank compact factor-two theorem described as resolved in a user handoff.

**Scope / 范围：** Other-window context; exact standalone hypotheses unavailable here.

**Status / 状态：** `related-proof-restored-with-explicit-scope`；原证据类型：inherited-branch-assertion.

**当前采用方式：** 证据或依赖待补。旧交接描述没有精确的独立假设；采用 AMP-LINEAR-01 的明确 normal-form/survival 定理，不采用旧笼统断言。

**恢复论证或继承输入（证据链尚有缺口）：** [results/notes/A06-linear-compact-replacement.md](notes/A06-linear-compact-replacement.md)

**合并后的更新：** The other branch now supplies the exact compact theorem. Its explicit normal-form and survival hypotheses replace any unqualified handoff description.

**限制：** No standalone proof package for this assertion was available; not promoted to a repository theorem.

**未公开或未恢复的历史路径（不是可用证据链接）：** `research/degradation/context/conversation/USER_HANDOFFS.md`, `research/degradation/context/conversation/INHERITED_INPUTS.md`
