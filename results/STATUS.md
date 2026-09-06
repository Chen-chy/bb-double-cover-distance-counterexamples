# 当前采用状态：主结论与研究过程分开

[主报告](../REPORT.md) · [全部研究记录](CLAIMS.md) · [状态规则](review_policy.json)

**104 条记录不等于 104 个已证定理。** 下表是范围和证据审阅后的展示分类，不是新增的独立数学审稿。
有效否定结果应保留，但被否定的推理路线不能再进入正面证明；历史较弱界不等于错误，未决问题不等于错误命题。

| 当前采用方式 | 记录数 | 使用规则 |
|---|---:|---|
| 主报告采用 | 12 | 主要结论；区分精确有限证书与仓库提供的符号证明。采用不等于独立同行评审。 |
| 按范围采用 | 52 | 仅按原假设、对象和量词使用；包含支撑引理及重复登记，不能一律解读为全距离定理。 |
| 有效否定结果 | 15 | 有效地否定某条捷径或某个辅助断言；被否定的路线不能再作为正面证明步骤。 |
| 历史较弱界 | 3 | 被更强结论取代展示优先级，不等于错误；不与现行界重复计算成果。 |
| 证据或依赖待补 | 8 | 原始包、依赖证明或精确陈述尚不齐全；不按已闭合证据链的主结论发布，不等于判定为假。 |
| 探索性记录 | 2 | 样本、上界或未完成搜索；不能从无 witness、超时或局部优化推断全局下界。 |
| 未决问题 | 8 | 在现有材料中未证未伪；问题出处不是证明，不作全球最新文献状态声明。 |
| 目标范围外 | 4 | 不是严格三项式逐项匹配 BB 二重覆盖的主结论；范围外推导仍可保留供比较。 |

主报告 12 条索引合为若干主要结论，其中两个有限反例有独立精确证书；一般定理是仓库提供了符号证明。记录间有重复及依赖，不能把分类计数当独立成果数量。
常数 8 及依赖它的区间／截断上界显式保留合并推论来源；程序通过不代表该推论通过独立审稿。
登记的依赖只覆盖本次识别出的主要引用关系，不声称是一份形式化完整证明依赖图。

<a id="main"></a>

## 主报告采用

主要结论；区分精确有限证书与仓库提供的符号证明。采用不等于独立同行评审。

| 记录 | 当前解释 |
|---|---|
| [CEX-UP](CLAIMS.md#CEX-UP) | 有限例的两套独立精确距离证书已保留；全距离 6→14，而非单个 witness 上界。 |
| [CEX-DOWN](CLAIMS.md#CEX-DOWN) | 有限例的两套独立精确距离证书已保留；全距离 14→12，而非特定类的受限最小值。 |
| [HOM-RANK](CLAIMS.md#HOM-RANK) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [HOM-FULL](CLAIMS.md#HOM-FULL) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [HOM-REFINED](CLAIMS.md#HOM-REFINED) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [HOM-SECTORS](CLAIMS.md#HOM-SECTORS) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DIST-LOWER](CLAIMS.md#DIST-LOWER) | 主文提供完整三次退化论证，不调用尚未恢复的小重量排除输入。 |
| [DIST-UPPER](CLAIMS.md#DIST-UPPER) | 主文提供常数 8 的合并推论；区别于原支线常数 32，不视为外部独立审稿通过。 |
| [DIST-INTERVAL](CLAIMS.md#DIST-INTERVAL) | 由现行三次界、长度界及偶性推导；对常数 8 的审阅依赖不能被取整消除。 |
| [DIST-AMBIENT](CLAIMS.md#DIST-AMBIENT) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DIST-TRUNCATED](CLAIMS.md#DIST-TRUNCATED) | 现行两项下界不含有缺失输入的 min(1/12,20/N) 项；上界使用常数 8。 |
| [DIST-EXAMPLE-THRESHOLDS](CLAIMS.md#DIST-EXAMPLE-THRESHOLDS) | 由两个有限证书直接导出底码长度阈值，不依赖早期无限族。 |

<a id="scoped"></a>

## 按范围采用

仅按原假设、对象和量词使用；包含支撑引理及重复登记，不能一律解读为全距离定理。

| 记录 | 当前解释 |
|---|---|
| [FINITE-SUBGROUP](CLAIMS.md#FINITE-SUBGROUP) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [STRIP-COFACTOR](CLAIMS.md#STRIP-COFACTOR) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [LATTICE-TRANSPORT](CLAIMS.md#LATTICE-TRANSPORT) | 合并稿新增的指数至多二关系子格推论；有限恒等式检查不是所有参数的证明。 |
| [CERT-COMPLETENESS](CLAIMS.md#CERT-COMPLETENESS) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [HOM-BOCKSTEIN](CLAIMS.md#HOM-BOCKSTEIN) | 四重厚化存在的矩形周期覆盖中的结论，不自动推广到任意抽象二重覆盖。 |
| [HOM-EXACT-DIMENSION](CLAIMS.md#HOM-EXACT-DIMENSION) | 继承 H01 四重厚化范围；不把该精化的范围与一般 rank 公式混同。 |
| [HOM-DECK-JORDAN](CLAIMS.md#HOM-DECK-JORDAN) | 继承 H01 四重厚化范围；描述 deck 在同调上的作用而非 Hamming 等距。 |
| [HOM-PAIRING](CLAIMS.md#HOM-PAIRING) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [METRIC-CLASS-VARIATIONAL](CLAIMS.md#METRIC-CLASS-VARIATIONAL) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [METRIC-QUOTIENT-DUAL](CLAIMS.md#METRIC-QUOTIENT-DUAL) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [METRIC-COUNTEREXAMPLE-TABLE](CLAIMS.md#METRIC-COUNTEREXAMPLE-TABLE) | δ、ρ、μ、ν 对应指定类及截面；这些指标不能互换或一律等于 d₂。 |
| [METRIC-EXCHANGE](CLAIMS.md#METRIC-EXCHANGE) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-BASE-02](CLAIMS.md#AMP-BASE-02) | 旧基线在 HOM-RANK/HOM-FULL 已有现行证明；重复登记不是独立新增定理。 |
| [AMP-R3-01](CLAIMS.md#AMP-R3-01) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-R3-02](CLAIMS.md#AMP-R3-02) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-D6-01](CLAIMS.md#AMP-D6-01) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-D6-02](CLAIMS.md#AMP-D6-02) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-ONEBLOCK-01](CLAIMS.md#AMP-ONEBLOCK-01) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-COMPACT-01](CLAIMS.md#AMP-COMPACT-01) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-LINEAR-01](CLAIMS.md#AMP-LINEAR-01) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-LINEAR-02](CLAIMS.md#AMP-LINEAR-02) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-RANK1-01](CLAIMS.md#AMP-RANK1-01) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-RANK1-02](CLAIMS.md#AMP-RANK1-02) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-RANK1-03](CLAIMS.md#AMP-RANK1-03) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-RANK1-04](CLAIMS.md#AMP-RANK1-04) | 只有兼容且足够长的周期可把 full compact minima 识别为有限码距离。 |
| [AMP-S21-01](CLAIMS.md#AMP-S21-01) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-S21-02](CLAIMS.md#AMP-S21-02) | 完整/单块/补空间的最小值必须分开；尤其 cover full=14、pure=16。 |
| [AMP-GRAPH-01](CLAIMS.md#AMP-GRAPH-01) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-GRAPH-02](CLAIMS.md#AMP-GRAPH-02) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-PARETO-01](CLAIMS.md#AMP-PARETO-01) | 指定实例的 Pareto frontier；须连同 closure 证书与完整消息优化范围引用。 |
| [AMP-TREE-01](CLAIMS.md#AMP-TREE-01) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [AMP-TREE-02](CLAIMS.md#AMP-TREE-02) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DEG-I01](CLAIMS.md#DEG-I01) | 旧“证书缺失”已修复，当前采用 CEX-UP；原限制只保留在历史记录中。 |
| [DEG-D04](CLAIMS.md#DEG-D04) | d₂=8⇒d≤96 的正文明确独立于早期小重量输入；组合 d>96⇒d₂≥10 则仍需该输入。 |
| [DEG-D05](CLAIMS.md#DEG-D05) | 与 DIST-LOWER 是同一三次退化结论的原支线登记，不能重复计算成果。 |
| [DEG-D07](CLAIMS.md#DEG-D07) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DEG-D10](CLAIMS.md#DEG-D10) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DEG-D11](CLAIMS.md#DEG-D11) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DEG-D12](CLAIMS.md#DEG-D12) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DEG-D13](CLAIMS.md#DEG-D13) | d≤3d₂² 只用于指定 deck-involution strip 子类，不能改写成一般二次退化界。 |
| [DEG-P01](CLAIMS.md#DEG-P01) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DEG-P02](CLAIMS.md#DEG-P02) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DEG-P03](CLAIMS.md#DEG-P03) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DEG-P04](CLAIMS.md#DEG-P04) | all-degree Bellman 证书支持完整 Laurent 最小值 8/14；不能只靠有限矩阵扫描。 |
| [DEG-P05](CLAIMS.md#DEG-P05) | 稳定化条件 L≥105、奇数且 3\|L 下的 8→14 族；比值 7/4 不是新纪录。 |
| [DEG-P07](CLAIMS.md#DEG-P07) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DEG-P09](CLAIMS.md#DEG-P09) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DEG-P10](CLAIMS.md#DEG-P10) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DEG-P11](CLAIMS.md#DEG-P11) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DEG-P12](CLAIMS.md#DEG-P12) | fixed-c 的 μ₊≤μ₀²+2；不是一般 d≤Cd₂²，也不是全局线性放大。 |
| [DEG-P13](CLAIMS.md#DEG-P13) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |
| [DEG-P14](CLAIMS.md#DEG-P14) | 按条目原文中的适用范围与限制使用；符号论证、有限审计与精确最小值的证据层次不互换。 |

<a id="negative"></a>

## 有效否定结果

有效地否定某条捷径或某个辅助断言；被否定的路线不能再作为正面证明步骤。

| 记录 | 当前解释 |
|---|---|
| [CEX-SUPPORT-FAMILY](CLAIMS.md#CEX-SUPPORT-FAMILY) | support–Bockstein 支撑控制引理被无限族否定；该族并不违反 d₂≤2d。 |
| [CEX-LOW-SHEET-INFINITE](CLAIMS.md#CEX-LOW-SHEET-INFINITE) | 低片指标 ν 可为无穷而覆盖距离有限；ν 不能当作 d₂。 |
| [AMP-METRIC-01](CLAIMS.md#AMP-METRIC-01) | transfer 扇区指标可发散而 d=d₂=4；不能用该指标替代实际距离。 |
| [AMP-R3-03](CLAIMS.md#AMP-R3-03) | 辅助约化码的距离 9 否定中间引理，不是新的严格三项式覆盖距离。 |
| [AMP-MAJORITY-01](CLAIMS.md#AMP-MAJORITY-01) | 局部稳定 boundary 否定受限 majority 断言，不是最短非边界反例。 |
| [AMP-TREE-03](CLAIMS.md#AMP-TREE-03) | 冲突图可含三角形；只能否定所提简单图结构捷径。 |
| [AMP-TREE-04](CLAIMS.md#AMP-TREE-04) | 固定消息最小重量 74；同一类的完整最小重量为 14，不能把 74 当码距。 |
| [AMP-TREE-05](CLAIMS.md#AMP-TREE-05) | 固定消息重量 74N 随 N 增长；同一固定码仍有重量 14 代表，不是无界升距族。 |
| [DEG-D02](CLAIMS.md#DEG-D02) | 常重量 boundary 的 coefficient filling 可发散；线性支撑填充引理为假。 |
| [DEG-D03](CLAIMS.md#DEG-D03) | 特定 boundary 的最小提升重量可发散；不能推出整码距离退化。 |
| [DEG-D08](CLAIMS.md#DEG-D08) | 短关系行不保证二次 cofactor 界；格对照例不是码距离反例。 |
| [DEG-D09](CLAIMS.md#DEG-D09) | 改变 torsion 可杀死 compact image；不能假设所有 specialization 保持存活。 |
| [DEG-D14](CLAIMS.md#DEG-D14) | 导数候选在 retained-involution 底码可有非零 syndrome，不能直接当 logical。 |
| [DEG-P06](CLAIMS.md#DEG-P06) | naive Frobenius 候选是 transfer 的倍数，会与被杀死的 transfer 一起消失。 |
| [DEG-P08](CLAIMS.md#DEG-P08) | 常消息可被非常消息改进，否定常消息最优捷径；尚未求得完整覆盖最小值。 |

<a id="historical"></a>

## 历史较弱界

被更强结论取代展示优先级，不等于错误；不与现行界重复计算成果。

| 记录 | 当前解释 |
|---|---|
| [AMP-COMPACT-02](CLAIMS.md#AMP-COMPACT-02) | 原较弱估计保留作为证明演进记录；现行主报告优先使用 DIST-UPPER / DIST-TRUNCATED。 |
| [AMP-GLOBAL-01](CLAIMS.md#AMP-GLOBAL-01) | 原较弱估计保留作为证明演进记录；现行主报告优先使用 DIST-UPPER / DIST-TRUNCATED。 |
| [AMP-GLOBAL-02](CLAIMS.md#AMP-GLOBAL-02) | 原较弱估计保留作为证明演进记录；现行主报告优先使用 DIST-UPPER / DIST-TRUNCATED。 |

<a id="gap"></a>

## 证据或依赖待补

原始包、依赖证明或精确陈述尚不齐全；不按已闭合证据链的主结论发布，不等于判定为假。

| 记录 | 当前解释 |
|---|---|
| [AMP-BASE-01](CLAIMS.md#AMP-BASE-01) | 只对 j=0 的有限 seed 有现行独立精确证书；整个早期参数族保留恢复稿状态。 |
| [AMP-BASE-03](CLAIMS.md#AMP-BASE-03) | d=2⇒d₂≤4 在此条目中是继承输入，原独立完整报告未恢复。 |
| [AMP-D4-01](CLAIMS.md#AMP-D4-01) | d=4⇒d₂≤48 有恢复论证及转录验证器，但原报告和原包缺失；保留来源限制，不列作闭合的主证书结果。 |
| [DEG-I02](CLAIMS.md#DEG-I02) | 本条把已认证有限 14→12 例与未恢复的无限族合写；有限部分使用 CEX-DOWN，不能整体升级。 |
| [DEG-I03](CLAIMS.md#DEG-I03) | 早期 weight-two/weight-four 排除及 stronger no-small-cycle 输入包未恢复。 |
| [DEG-D01](CLAIMS.md#DEG-D01) | 原定理明确以起始 weight-four 排除为条件；本次没有补证该输入，d₂=6⇒d≤56 不作无条件主结论。 |
| [DEG-D06](CLAIMS.md#DEG-D06) | min(1/12,20/N) 项依赖早期小重量输入；不依赖该输入的其余部分另列于 DIST-TRUNCATED。 |
| [DEG-I04](CLAIMS.md#DEG-I04) | 旧交接描述没有精确的独立假设；采用 AMP-LINEAR-01 的明确 normal-form/survival 定理，不采用旧笼统断言。 |

<a id="exploratory"></a>

## 探索性记录

样本、上界或未完成搜索；不能从无 witness、超时或局部优化推断全局下界。

| 记录 | 当前解释 |
|---|---|
| [AMP-SEARCH-01](CLAIMS.md#AMP-SEARCH-01) | 仅为指定样本的搜索记录；witness 给上界，未完成搜索不提供下界或全局排除。 |
| [AMP-SEARCH-02](CLAIMS.md#AMP-SEARCH-02) | 仅为指定样本的搜索记录；witness 给上界，未完成搜索不提供下界或全局排除。 |

<a id="open"></a>

## 未决问题

在现有材料中未证未伪；问题出处不是证明，不作全球最新文献状态声明。

| 记录 | 当前解释 |
|---|---|
| [AMP-OPEN-01](CLAIMS.md#AMP-OPEN-01) | 在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。 |
| [AMP-OPEN-02](CLAIMS.md#AMP-OPEN-02) | 在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。 |
| [AMP-OPEN-03](CLAIMS.md#AMP-OPEN-03) | 在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。 |
| [DEG-O01](CLAIMS.md#DEG-O01) | 在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。 |
| [DEG-O02](CLAIMS.md#DEG-O02) | 在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。 |
| [DEG-O03](CLAIMS.md#DEG-O03) | 在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。 |
| [DEG-O04](CLAIMS.md#DEG-O04) | 在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。 |
| [DEG-O05](CLAIMS.md#DEG-O05) | 在本仓库材料中未证未伪；问题的提出或数值探索不构成证明。 |

<a id="outside"></a>

## 目标范围外

不是严格三项式逐项匹配 BB 二重覆盖的主结论；范围外推导仍可保留供比较。

| 记录 | 当前解释 |
|---|---|
| [AMP-PATHOLOGY-01](CLAIMS.md#AMP-PATHOLOGY-01) | 非 BB square-zero 变形；可作错误推广的对照，不是目标类反例。 |
| [DEG-A00](CLAIMS.md#DEG-A00) | 四项式族，不满足严格三项式条件；同时原验证包未恢复。 |
| [DEG-A01](CLAIMS.md#DEG-A01) | 允许任意项数的 Θ(N⁻¹) 结论，不是严格三项式结论；同时原验证包未恢复。 |
| [DEG-P15](CLAIMS.md#DEG-P15) | 第二个提升分子有五项，违反目标类的逐项三项匹配。 |
