# 完整证明与研究记录：按当前状态阅读

[先读主要结论总报告](../REPORT.md) · [当前采用／排除表](STATUS.md) · [仓库首页](../README.md) · [104 条研究记录](CLAIMS.md) · [机器可读目录](catalog.json) · [复现说明](../docs/REPRODUCIBILITY.md)

**这里既有定理，也有失败路线与未决问题；104 是记录数，不是已证定理数。** 先读[主报告](../REPORT.md)，再按[状态表](STATUS.md)选择正文，不将整篇历史报告作为无条件有效结果。

本目录是仓库的数学正文。`theory/` 给出七章完整合并论证，`notes/` 给出二十五篇完整研究笔记的 GitHub 阅读版；它们不是论文摘要。原始字节、分类程序和数据保存在 `research/`，阅读版保留原文主体，调整数学分隔符与链接，并在顶部加入当前采用状态提示。两种文本的哈希与覆盖检查在 `provenance/`。

## 主理论

| 章 | 内容 |
|---|---|
| [1. 两个反例](theory/01-counterexamples.md) | 定义、具体多项式、维数、重量 6/14/12 logical、非边界证明、精确距离排除 |
| [2. 同调与 transfer](theory/02-homology.md) | 适用范围、维数界、投影和 transfer 的秩、满维结论、张成阈值、两个扇区 |
| [3. 双向多项式界](theory/03-polynomial-bounds.md) | 有限 check 子群、strip cleaning、incidence circuit、关系格、指数二 transport、全部 torsion 分支 |
| [4. 长度界与上下端点](theory/04-size-bounds.md) | $C_0n^{3/4}$、$\gamma_-(N)$ 与 $\Gamma(N)$、偶数取整的 $d_{\rm lower},d_{\rm upper}$ |
| [5. 进一步结果导读](theory/05-further-results.md) | compact metric、rank-one Laurent、Bellman 与负面对照；完整细节在下面的研究笔记 |
| [6. 精确算法的完备性](theory/06-certificate-algorithms.md) | circuit、平移归约、两种独立搜索分支、边界判定、X/Z 等距、共享中间码 |
| [7. 证据范围](theory/07-evidence-scope.md) | 数学证明、精确证书、保留审计、历史扫描和作者审阅之间的区别 |

<a id="small-weight"></a>

## 完整研究笔记

每一项链接都是完整过程笔记，不代表其中每条推理都被当前采用。旧文本的历史状态可能被新的证书修复或被更强常数改进，请同时查阅 [逐项登记表](CLAIMS.md)。

| 编号 | 笔记主题 | 必须保留的限制 |
|---|---|---|
| [A01](notes/A01-initial-family-and-baseline.md) | 早期升距参数族、有限 seed、同调基线 | 数学阅读文本已恢复；不等于原完整参数族验证包已恢复 |
| [A02](notes/A02-distance4-and-transfer-metric.md) | $d=4\Rightarrow d_2\le48$；transfer-sector metric | 恢复文本与后续检查；sector metric 不等于全距离 |
| [A03](notes/A03-amplification-search.md) | 单块 gcd 二分、split-cover 物理度量、精确及未决搜索记录 | 扫描只覆盖给定样本；无 witness 不等于排除 |
| [A04](notes/A04-distance6-obstruction.md) | $d=6\Rightarrow d_2\le112$；Frobenius 与单块界 | 完整分类代码保留；保留证据审计不等于重跑全部分类 |
| [A05](notes/A05-compact-survival.md) | 所有 circuit 重量的 higher-rank compact survival、历史全局多项式界 | finite survival 与 winding/Tor 不能忽略 |
| [A06](notes/A06-linear-compact-replacement.md) | 精确 torsion–Frobenius compact metric；比值 $1,3/2,2$ | 仅在明确的 normal-form/compact-survival 范围内 |
| [A07](notes/A07-rank-one-resonance.md) | rank-one 模、共振、fixed-slope 界、长周期实现 | slope 不是统一有界常数 |
| [A08](notes/A08-slope21-shortening.md) | slope-(2,1) shortening；full/pure/complement minima | 受限 16 与完整 14 必须区分 |
| [A09](notes/A09-joint-completion.md) | 共同消息图、majority、分量结构、Pareto frontier | 局部最优不等于完整消息/边界优化 |
| [A10](notes/A10-nonlocal-exchange.md) | 树收缩、冲突图、fixed-message $74N$ 对照 | 同一 universal class 有重量 14 代表；不是增距族 |
| [D01](notes/D01-weight-six.md) | 带继承假设的 $d_2=6\Rightarrow d\le56$；filling 反例 | 原定理明确调用早期 weight-four 排除输入，原包未恢复；不作无条件主结论 |
| [D02](notes/D02-weight-eight.md) | $d_2=8\Rightarrow d\le96$；一般有限交换群商 | 组合成 $d>96\Rightarrow d_2\ge10$ 另需早期排除 |
| [D03](notes/D03-structural-degradation.md) | $d\le4d_2^3$；显式几何与退化界 | 一般证明不依赖前面的小重量分类 |
| [D04](notes/D04-quadratic-bottleneck.md) | 奇扭率 compact descent、二次 cofactor 障碍 | 格反例不是码距离反例 |
| [D05](notes/D05-visible-two-primary.md) | 可见二主扭率、compact loss、period 商 | 不消去 specialization-created sector |
| [D06](notes/D06-sparse-deck-descent.md) | 稀疏 deck descent 和被否定的 coefficient-filling 捷径 | 子类结果不升级为全局二次退化 |
| [D07](notes/D07-rank-one-amplification.md) | 全次数 Bellman 证书；稳定化 $8\to14$ 族 | 原始有限存活条件与 winding 阈值保留 |
| [D08](notes/D08-mixed-laurent.md) | mixed-parity Laurent 物理优化与恒等式 | 保留完整 $F,H$ 自由度 |
| [D09](notes/D09-fixed-c-product-bound.md) | fixed-$c$ span/product bound；$\mu_+\le\mu_0^2+2$ | 不是全局线性放大或二次退化定理 |
| [X00](notes/X00-beyond-trinomials.md) | 四项式降距族；任意项数 $\Theta(N^{-1})$ 公开报告 | 范围外结果；原独立代码包未恢复，状态为 reported-proof-only |

## 研究记录状态与继续研究

[全部记录](CLAIMS.md)保留主线 16 条、同调/类度量 10 条、升距支线 38 条、降距支线 40 条。是否采用以[逐项状态](STATUS.md)为准。`python -m bbcover results` 默认只显示 12 条主报告索引；`--view all` 才显示全部 104 条过程记录。

[历史与限制](HISTORY_AND_LIMITS.md)解释修复了哪些证书、没有恢复哪些原始包，以及为什么不能把固定消息/受限扇区误当全距离。[开放问题](OPEN_PROBLEMS.md)汇总仍未解决的定量目标。[参考文献](REFERENCES.md)提供外部文献和内部证明的稳定引用。

<a id="homology"></a>

## 同调、类度量与反例发现链

- [H01-bockstein-and-deck-structure](notes/H01-bockstein-and-deck-structure.md)：完整历史数学报告，早期猜想状态由后续精确反例修正。
- [H02-support-obstruction-family](notes/H02-support-obstruction-family.md)：完整历史数学报告，早期猜想状态由后续精确反例修正。
- [H03-class-metrics-and-exchange](notes/H03-class-metrics-and-exchange.md)：完整历史数学报告，早期猜想状态由后续精确反例修正。
- [H04-upper-referee-certificate](notes/H04-upper-referee-certificate.md)：完整历史数学报告，早期猜想状态由后续精确反例修正。
- [H05-lower-referee-certificate](notes/H05-lower-referee-certificate.md)：完整历史数学报告，早期猜想状态由后续精确反例修正。
