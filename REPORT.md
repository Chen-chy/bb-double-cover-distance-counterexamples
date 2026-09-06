# BB 二重覆盖距离：主要结论与有效性报告

**版本 0.2.1 · 本文件是仓库首要阅读入口。**

[仓库首页](README.md) · [English report](REPORT.en.md) · [逐项采用／排除状态](results/STATUS.md) · [完整证明](results/README.md) · [复现说明](docs/REPRODUCIBILITY.md)

## 结论先行

现有材料支持两项精确有限反例：$6\to14$ 否定普遍上界 $d_2\le2d$，$14\to12$ 否定普遍下界 $d_2\ge d$。在下述严格三项式二元交换群二重覆盖范围内，仓库提供了替代界 $d\le4d_2^3$、$d_2\le8d^3$ 的完整符号论证，并由此给出显式 $d_{\rm lower}\le d_2\le d_{\rm upper}$。

**不是所有研究过程都有效，也不是所有条目都能当作定理引用。** 仓库有 104 条研究记录，而不是 104 个已证定理；其中包括重复登记、有效的否定结果、已经失败的证明捷径、范围外构造、未完成搜索和未决问题。主报告只采用下文明确列出的结论，其他材料按[状态表](results/STATUS.md)使用。

| 主要结论 | 当前可作的陈述 | 证据层次与入口 |
|---|---|---|
| 升距反例 | $[[78,4,6]]\to[[156,4,14]]$，$d_2/d=7/3>2$ | 两套独立精确证书；[CEX-UP](results/CLAIMS.md#CEX-UP) |
| 降距反例 | $[[156,4,14]]\to[[312,8,12]]$，$d_2/d=6/7<1$ | 两套独立精确证书；[CEX-DOWN](results/CLAIMS.md#CEX-DOWN) |
| 双向替代界 | $d\le4d_2^3$、$d_2\le8d^3$ | 符号证明已提供；常数 8 为合并推论；[第三章](results/theory/03-polynomial-bounds.md) |
| 显式距离区间 | 见下节 $d_{\rm lower}$、$d_{\rm upper}$；均非最优性声明 | 上述界、偶性及长度界的推论；[第四章](results/theory/04-size-bounds.md) |
| 同调维数与满维情形 | $k\le k_2\le2k$；$k_2=2k\Rightarrow d_2\le2d$ | 符号证明已提供；[第二章](results/theory/02-homology.md) |
| projection 的两个扇区 | $d_2=\min\{d_{\rm vis},d_{\rm ker}\}$，$d_{\rm vis}\ge d$ | 不能把可见扇区下界推广到 kernel 扇区；[第二章](results/theory/02-homology.md) |
| 长度相关控制 | $d\le\min\{n/2,C_0n^{3/4}\}$，以及下面的截断比例界 | 符号证明已提供；[第四章](results/theory/04-size-bounds.md) |

表中“符号证明已提供”与“有限例独立穷尽证书通过”是不同的证据层次；二者都不意味着已有独立同行评审或形式化验证。**特别是常数 8 的新合并推论及其依赖链，不能因代码测试通过就宣布完成数学审稿。**

## 一、对象、假设和两个反例

底码参数为 $[[n,k,d]]$，覆盖码为 $[[2n,k_2,d_2]]$；$n$ 始终是底码物理比特数。主定理使用二元系数、有限交换群满射 $\widetilde G\to G$，覆盖核为 $C_2$，覆盖前后每个 check 都恰有三个互异单项式，并逐项匹配。假设 $k>0$。这里允许一个矩形周期为一，但不允许投影后单项式重合或相消。结论没有自动推广到任意 Tanner 图覆盖或任意项数。

令

$$
A=1+x^8+x^{25},\qquad B=1+x^2+x^{13}.
$$

第一例保持 $A,B$ 不变，将周期 $(39,1)$ 变为 $(78,1)$：

$$
\boxed{[[78,4,6]]\longrightarrow[[156,4,14]],\qquad14>2\cdot6.}
$$

第二例把同一个 $[[156,4,14]]$ 中间码沿第二个周期加倍，$(78,1)\to(78,2)$，取

$$
A'=1+x^8y+x^{25},\qquad B'=1+x^2y+x^{13},
$$

得到

$$
\boxed{[[156,4,14]]\longrightarrow[[312,8,12]],\qquad12<14.}
$$

这两个覆盖连通、逐项匹配，并在完整 Tanner 图邻域上局部双射。6、14、12 是完整码距，不是一个搜索器给出的上界。精确性同时需要达到该重量的非边界 logical，以及排除全部更小非边界的证明。[第一章](results/theory/01-counterexamples.md)给出具体 logical 和非边界论证；[第六章](results/theory/06-certificate-algorithms.md)说明 circuit 穷尽算法为何完备；[四个独立验证器](certificates/README.md)提供实际排除。

第一例中最短底码 logical 的重量 12 transfer 在覆盖码中成为 boundary；第二例的重量 12 logical 投影到一个底码 boundary。这正是两个直觉论证失败的位置：transfer 不必保持非平凡类，projection 也不必在所有非平凡类上非零。

## 二、当前采用的上下界放在一起

在上述统一假设下，仓库主论证给出

$$
\boxed{d\le4d_2^3,\qquad d_2\le8d^3.}
$$

取

$$
C_0=\frac{16}{3}\left(\frac{12}{\pi^2}\right)^{3/4}.
$$

利用严格三项式 cycle 重量为偶数，有

$$
\boxed{\begin{aligned}
 d_{\rm lower}(d)&=2\left\lceil\frac{(d/4)^{1/3}}2\right\rceil,\\
 d_{\rm upper}(d,n)&=2\left\lfloor
 \frac{\min\{8d^3,n,C_0(2n)^{3/4}\}}2
 \right\rfloor.
\end{aligned}}
$$

因此

$$
\boxed{d_{\rm lower}(d)\le d_2\le d_{\rm upper}(d,n).}
$$

若知道 $k_2=2k$，上端点还可与 $2d$ 取最小。若不知道 $n$，可以只用三次比较界及其偶数取整。**这些是适用于一类码的保证区间，不是对每个给定码精确计算出的 $d_2$。** 例如 CLI 对 $d=14,n=156,k=4,k_2=8$ 返回安全区间 $[2,28]$；精确距离 12 来自该具体反例的证书，不来自这个区间。

常数的来源必须一并保留：原升距支线给出 $d_2\le32d^3$，合并论证通过指数至多二的关系子格改进到 $8d^3$。当前采用较强的合并推论，但不将 8 伪装成原始支线的结论；原来的 32 是历史较弱界，并非错误。需要只引用原支线版本时，可明确使用 32，而不能混用依赖 8 导出的较强常数。[来源说明](results/HISTORY_AND_LIMITS.md)

### 证明结构与采用边界

[第三章](results/theory/03-polynomial-bounds.md)从最短非边界的 circuit 支撑提取三价 incidence 图和整数关系格。纯块情形使用有限 check 子群及短支撑引理。混合情形有三条独立关系时，端口差估计控制余因子，strip cleaning 将其转化为距离界。向下投影不增加相应关系指数；向上提升时取整个关系格到 $C_2$ 的电压同态之核，其指数至多二，得到常数 8，而不是把三条关系分别加倍。

关系秩不足三的分支另由 Laurent 共因子、Newton 多边形与 torsion–Frobenius 归约处理；非边界见证的证明保留 active-summand 条件，不能用“总码 $k>0$”任意替换该条件。之后结合长度界和偶性得到上述端点。[完整证明](results/theory/03-polynomial-bounds.md#thm-polynomial)及[指数二步骤](results/theory/03-polynomial-bounds.md#lem-transport)均可直接在 GitHub 阅读。

**这条主证明不调用尚未恢复的 weight-two/weight-four 排除输入，也不依赖搜索未发现反例、固定消息优化、局部 majority 或错误的 support–Bockstein 引理。** 本次整理的是论证与证据的采用边界，并没有把所有历史报告整体重新认证为正确。

## 三、同调和长度相关的主要推论

同调上的 projection 与 transfer 满足

$$
 k\le k_2\le2k,\qquad
 \operatorname{rank}\widehat p_1=\operatorname{rank}\widehat\tau_1=k_2/2.
$$

因此 $k_2=2k$ 时 transfer 单射，最短底码类存活，给出 $d_2\le2d$。更一般地，设 $\lambda_j$ 为由低重量 logical 生成的子空间达到维数 $j$ 所需的最小重量阈值，则

$$
 d_2\le2\lambda_{k-k_2/2+1}.
$$

这不是 $\lambda_j$ 可由 $d$ 线性控制的声明。定义 $d_{\rm vis}$ 为投影类非零的覆盖 logical 的最小重量，$d_{\rm ker}$ 为投影核中非零类的最小重量，有

$$
 d_2=\min\{d_{\rm vis},d_{\rm ker}\},\qquad d_{\rm vis}\ge d.
$$

这些结论及证明见[第二章](results/theory/02-homology.md)。矩形周期四重厚化中的 Bockstein、deck Jordan 精化另外按其专门假设使用，不把它们的适用范围自动扩大为任意群扩张。

对于长度，主文给出

$$
 d\le\min\{n/2,C_0n^{3/4}\}.
$$

以 $\mathcal C_N$ 表示底码长度 $n\le N$ 的目标覆盖集合，非空时定义

$$
 \gamma_-(N)=\inf_{\mathcal C_N}\frac{d_2}{d},\qquad
 \Gamma(N)=\sup_{\mathcal C_N}\frac{d_2}{d}.
$$

当前采用

$$
 \max\{N^{-2/3},c_-N^{-1/2}\}\le\gamma_-(N),\qquad
 \Gamma(N)\le c_+\sqrt N,
$$

其中

$$
 c_-=\frac{\pi3^{1/6}}{2^{13/3}},\qquad
 c_+=2^{3/2}C_0^{2/3}.
$$

两个有限反例还给出 $\Gamma(N)\ge7/3$（$N\ge78$）及 $\gamma_-(N)\le6/7$（$N\ge156$）。这里既不声称渐近等价，也不声称比值可独立于长度控制。[第四章](results/theory/04-size-bounds.md)

## 四、有用但需要单独保留范围的结果

| 结果 | 采用方式 | 不能推出什么 |
|---|---|---|
| Bockstein 复形、deck Jordan 分解、类级变分与二元对偶 | [H01](results/notes/H01-bockstein-and-deck-structure.md)、[H03](results/notes/H03-class-metrics-and-exchange.md)中的规定覆盖和配对约定 | 不能把 $\rho,\mu,\nu$ 一律当成 $d_2$；不能忽略四重厚化等假设 |
| $d=6\Rightarrow d_2\le112$；$d_2=8\Rightarrow d\le96$ | [A04](results/notes/A04-distance6-obstruction.md)、[D02](results/notes/D02-weight-eight.md)的计算辅助论证及其完备性 | 保留记录审计不等于本次重跑所有分类；第二条不能单独推出 $d>96\Rightarrow d_2\ge10$ |
| compact 精确度量、比值 $1,3/2,2$ | [A06](results/notes/A06-linear-compact-replacement.md)的 normal form 与 surviving compact image 范围 | 不能推出全类 $d_2\le2d$；不能删掉 winding／specialization-created sector |
| $[[2L,4,8]]\to[[4L,4,14]]$ 稳定化族 | [D07](results/notes/D07-rank-one-amplification.md)的 all-degree Bellman 证书及 $L\ge105$、$L$ 为 3 的奇倍数条件 | 不是无界升距族；比值 $7/4$ 不是超过 $7/3$ 的纪录 |
| $d\le3d_2^2$ | [D06](results/notes/D06-sparse-deck-descent.md)的 deck-involution strip 子类 | 不是一般二次退化定理 |
| fixed-$c$ 的 $\mu_+\le\mu_0^2+2$ | [D09](results/notes/D09-fixed-c-product-bound.md)完整 Laurent 消息与边界优化 | 不是全局线性放大，也不是反方向 $d\le Cd_2^2$ |

### 暂不作为闭合主结论的材料

[DEG-D01](results/CLAIMS.md#DEG-D01) 的原文 Theorem 1 明确以早期 weight-four 排除为条件，该输入包尚未恢复。因此其 $d_2=6\Rightarrow d\le56$ 及组合结论在当前展示中保留依赖，不再与独立于该输入的主三次界混列。后续 $d>96\Rightarrow d_2\ge10$、比例项 $\min\{1/12,20/N\}$ 也有同一类依赖。**本次没有通过改写摘要而悄悄补证这些输入。**

$d=4\Rightarrow d_2\le48$ 有恢复论证与转录程序，但原报告和原包未恢复，见 [AMP-D4-01](results/CLAIMS.md#AMP-D4-01)。早期 $6\to14$、$14\to12$ 无限参数族不能因有限 seed 已认证而整族升级。保留这类材料不是判其为假，而是不作超出证据的发布声明。

## 五、哪些推理不能再采用

**有效的否定结果不应删除；被它否定的证明步骤应停止使用。** 以下是主报告明确排除的推理，而不是把整份历史笔记都宣告无用。

| 不可采用的捷径或误读 | 已知问题／正确解释 | 对应材料 |
|---|---|---|
| 最短底码 logical 的 transfer 必然非零 | 第一有限反例中它成为 boundary，故不能推出 $d_2\le2d$ | [CEX-UP](results/CLAIMS.md#CEX-UP) |
| 非零覆盖 logical 的投影必非零 | projection-kernel 扇区可给出 $d_2<d$ | [CEX-DOWN](results/CLAIMS.md#CEX-DOWN) |
| support–Bockstein／短支撑 filling 总受原重量控制 | 显式无限族否定候选支撑控制；这本身不是新的全距离比例反例 | [H02](results/notes/H02-support-obstruction-family.md)、[DEG-D02](results/CLAIMS.md#DEG-D02) |
| restricted minimum 16 就是覆盖距离 | 同一实例 full minimum 为 14；两者优化范围不同 | [AMP-S21-02](results/CLAIMS.md#AMP-S21-02) |
| 固定消息最小值 $74N$ 给出无界升距 | 同一 universal class 有完整最小值 14 的代表 | [AMP-TREE-05](results/CLAIMS.md#AMP-TREE-05) |
| 局部 majority 最优等于完整最小非边界 | 反例输入可能是 boundary；局部最优与全局消息优化不可互换 | [AMP-MAJORITY-01](results/CLAIMS.md#AMP-MAJORITY-01) |
| 三条短关系可自动给二次 cofactor 界 | 有格层面的反例；但它不是码距离的反例 | [DEG-D08](results/CLAIMS.md#DEG-D08) |
| 任意 compact 类在 specialization 中都存活 | 改变 torsion 会造成 compact loss，须检查 active image | [DEG-D09](results/CLAIMS.md#DEG-D09) |
| naive Frobenius 候选自动非边界 | 它是 transfer 的倍数，transfer 被杀死时该类也被杀死 | [DEG-P06](results/CLAIMS.md#DEG-P06) |
| 五项式无界族回答严格三项式问题 | 提升支持有五项，不满足目标类假设 | [DEG-P15](results/CLAIMS.md#DEG-P15) |
| 有限样本没找到反例，或搜索超时，即证明下界 | 只能保留“样本内未发现／未完成”；无 witness 不等于排除 | [AMP-SEARCH-01](results/CLAIMS.md#AMP-SEARCH-01)、[AMP-SEARCH-02](results/CLAIMS.md#AMP-SEARCH-02) |

四项式／任意项数报告也保留在[范围外材料](results/notes/X00-beyond-trinomials.md)，但它既不是严格三项式主结论，也没有被本次补齐原独立验证包。

## 六、仍未由本仓库解决的问题

严格三项式目标类的 $\sup d_2/d$ 是否有限、是否有与长度无关的 $c>0$ 使 $d_2\ge cd$、能否得到一般 $d\le Cd_2^2$，仍未由现有材料解决。slope-(2,1)／fixed-$c$ 的剩余因子三问题及其候选充分引理也保留未决状态。未证不等于已反驳，否定某个充分引理也不等于否定主猜想。[问题与约束](results/OPEN_PROBLEMS.md)

这些是**本仓库的研究状态**，不声称本次完成了截至当前日期的全球文献新颖性检索。

## 七、如何使用仓库而不误用过程材料

本报告与[首页](README.md)给出采用后的主要结论；[七章正文](results/README.md)给出完整主证明；[逐项状态表](results/STATUS.md)将 104 条记录分为 12 条主报告索引、52 条按范围采用、15 条有效否定结果、3 条历史较弱界、8 条证据／依赖待补、2 条探索记录、8 条未决问题和 4 条范围外记录。计数不是独立定理数。

每篇 `results/notes/` 阅读版顶部都有具体的当前状态提示。`research/` 原始文本和程序保持原字节，便于追溯错误如何出现、如何被修正；不能仅因为某份旧报告标题写了 proved 或 verified 就跳过当前状态。完整登记中的“问题出处”不再标为“完整证明”。

```bash
# 默认仅显示主报告采用的记录
python -m bbcover results

# 按需查看有效的否定结果、证据缺口或全部研究过程
python -m bbcover results --view negative
python -m bbcover results --view gap
python -m bbcover results --view all

# 检查报告／目录一致性，不声称验证一般数学命题
python scripts/check_report.py --check
python scripts/check_repository.py

# 重新执行两个有限反例的四个独立精确验证器
python scripts/reproduce.py --profile core --output checks/new-core
```

既有版本的执行日志与本版检查分开保存于 `checks/release/`。本次报告修订没有新增数学常数，也没有把 47 条历史审计冒充为本次重新运行全部探索过程。每次实际运行的范围、失败、超时和未复现部分应按[复现说明](docs/REPRODUCIBILITY.md)记录；本地检查通过不等于远程 GitHub Actions 已运行。

**主报告稳定索引：** [CEX-UP](results/CLAIMS.md#CEX-UP) · [CEX-DOWN](results/CLAIMS.md#CEX-DOWN) · [HOM-RANK](results/CLAIMS.md#HOM-RANK) · [HOM-FULL](results/CLAIMS.md#HOM-FULL) · [HOM-REFINED](results/CLAIMS.md#HOM-REFINED) · [HOM-SECTORS](results/CLAIMS.md#HOM-SECTORS) · [DIST-LOWER](results/CLAIMS.md#DIST-LOWER) · [DIST-UPPER](results/CLAIMS.md#DIST-UPPER) · [DIST-INTERVAL](results/CLAIMS.md#DIST-INTERVAL) · [DIST-AMBIENT](results/CLAIMS.md#DIST-AMBIENT) · [DIST-TRUNCATED](results/CLAIMS.md#DIST-TRUNCATED) · [DIST-EXAMPLE-THRESHOLDS](results/CLAIMS.md#DIST-EXAMPLE-THRESHOLDS)。
