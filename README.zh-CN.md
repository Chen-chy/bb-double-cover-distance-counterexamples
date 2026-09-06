# BB 二重覆盖距离反例

> [!WARNING]
> **研究状态与 AI 使用说明**
>
> - **本人已亲自检验：两个显式反例的正确性。**
> - **由 AI 完成、本人尚未完整核验：** 一般证明、推导及所给界；这些内容目前应视为暂定结果。
> - **正在进行：** 严格界的研究。
> - **后续计划：** 待作者逐项检查并确认论证正确后，将整理成论文并提交至 arXiv。

**猜想的二重覆盖距离界 $d\le d_2\le2d$ 在二元 BB 码中失效。这里给出精确反例、新的双向三次界、完整证明与证书。版本 0.2.1。**

## [先读：主要结论与有效性总报告](REPORT.md)

**已认证的两个有限反例：$6\to14$ 否定 $d_2\le2d$，$14\to12$ 否定 $d_2\ge d$。仓库另提供 $d\le4d_2^3$、$d_2\le8d^3$ 及显式上下端点的符号证明。** 常数 8 的合并推论来源与审阅状态单独标明。

**104 条是研究记录，不是 104 个已证定理。** 失败路线、未决问题、范围外构造和材料缺口不进入主结论；有效的否定结果单独保留。[总报告](REPORT.md)集中回答“得到了什么、证据是什么、哪些不能用”，[逐项状态表](results/STATUS.md)给出每条记录的当前采用方式。

[完整结果与阅读路线](results/README.md) · [104 条研究记录（含未决与否定结果）](results/CLAIMS.md) · [复现方法](docs/REPRODUCIBILITY.md) · [English](README.en.md)

这是独立的研究仓库。数学正文、完整研究笔记、分类数据、验证器和探索代码都在仓库内；不需要 arXiv 页面或论文附件才能阅读、理解和复现。`paper/` 只是可选的排版稿，**不是仓库的主体，也不覆盖全部研究结果**。

## 1. 两个精确反例

设 $A=1+x^8+x^{25}$、$B=1+x^2+x^{13}$。

| 覆盖 | 精确参数 | 违反的普遍猜想 |
|---|---|---|
| $(39,1)\to(78,1)$，保持 $A,B$ 不变 | $[[78,4,6]]\to[[156,4,14]]$ | $d_2\le2d$：$14>12$ |
| $(78,1)\to(78,2)$，$A'=1+x^8y+x^{25}$、$B'=1+x^2y+x^{13}$ | $[[156,4,14]]\to[[312,8,12]]$ | $d_2\ge d$：$12<14$ |

两个反例共享同一个中间码。覆盖连通、逐项匹配，并且在完整 Tanner 图上局部双射。允许周期等于一，但不允许三项投影后相消或重合。

**完整证明与显式 logical：**[第一章](results/theory/01-counterexamples.md)。**独立精确证书：**[升距反例](certificates/upper/README.md)、[降距反例](certificates/lower/README.md)。每个反例有两个保留原始字节的独立验证器，分别重新生成短 circuit 并判断边界；没有共用 `bbcover` 中的距离判断代码。[算法完备性证明](results/theory/06-certificate-algorithms.md)说明了穷尽搜索为何充分。

这里的 6、14、12 是完整距离，不是某个译码器、固定消息、选定代表元或受限逻辑扇区的上界。

## 2. 统一的上下界

设底码为 $[[n,k,d]]$，覆盖码为 $[[2n,k_2,d_2]]$。**主定理范围**是二元系数、有限交换群、核为 $C_2$ 的逐项匹配覆盖、上下两个 check 均有恰好三个互异单项式，以及 $k>0$。

在此范围内，完整论证给出

$$
\boxed{d\le4d_2^3,\qquad d_2\le8d^3.}
$$

令

$$
C_0=\frac{16}{3}\left(\frac{12}{\pi^2}\right)^{3/4}.
$$

则

$$
\boxed{d_{\rm lower}(d)=2\left\lceil\frac{(d/4)^{1/3}}{2}\right\rceil}
$$

以及

$$
\boxed{d_{\rm upper}(d,n)=2\left\lfloor\frac{\min\{8d^3,n,C_0(2n)^{3/4}\}}{2}\right\rfloor}
$$

满足 $d_{\rm lower}\le d_2\le d_{\rm upper}$。若 $k_2=2k$，上端点还可以与 $2d$ 取最小。只知道 $d$ 时，仍可使用不含 $n$ 的三次比较界。偶数取整来自严格三项式 cycle 的重量偶性。

**证明在仓库正文中：**[双向三次界](results/theory/03-polynomial-bounds.md)、[长度界及显式区间](results/theory/04-size-bounds.md)。常数 8 来自此前合并时增加的指数二关系子格推论；原始支线的常数 32 及证明也完整保留。没有将新推论冒充为原档案结论，也不声称常数或指数最优。程序的有限恒等式检查不是一般定理的证明或独立同行评审。

## 3. 补充结果与研究过程分开使用

正文包含七章主理论，以及 **25 篇不删节的研究笔记阅读版**。两支线的 78 条原始记录、16 条主线记录及 10 条同调/类度量记录合为 [104 条研究记录](results/CLAIMS.md)。它们包含未决、失败路线和重复条目；每项显示当前采用方式、范围、论证或问题出处和限制。

| 主题 | 正文入口 |
|---|---|
| 维数、projection/transfer 秩、可见/核扇区、逻辑张成阈值 | [第二章](results/theory/02-homology.md) |
| 小重量分类：按每条证明的依赖使用；weight-six 排除有未恢复的继承输入，不能无条件并列 | [总报告中的采用边界](REPORT.md)、[完整阅读路线](results/README.md#small-weight) |
| torsion–Frobenius compact metric、有限存活条件、指定范围内的 factor-two replacement | [A05](results/notes/A05-compact-survival.md)、[A06](results/notes/A06-linear-compact-replacement.md) |
| rank-one resonance、所有次数的 Bellman 证书、稳定化 $8\to14$ 族 | [A07](results/notes/A07-rank-one-resonance.md)、[D07](results/notes/D07-rank-one-amplification.md) |
| 可见二主扭率、sparse deck descent、mixed Laurent、fixed-$c$ 乘积界 | [D05](results/notes/D05-visible-two-primary.md)、[D06](results/notes/D06-sparse-deck-descent.md)、[D08](results/notes/D08-mixed-laurent.md)、[D09](results/notes/D09-fixed-c-product-bound.md) |
| slope-(2,1)、共同消息图、Pareto 边界、非局部交换与 fixed-message 反例 | [A08](results/notes/A08-slope21-shortening.md)、[A09](results/notes/A09-joint-completion.md)、[A10](results/notes/A10-nonlocal-exchange.md) |
| 严格三项式范围外的四项式降距族与任意项数结果 | [X00 完整公开数学报告](results/notes/X00-beyond-trinomials.md) |
| 未决问题、已被否定的捷径、材料缺口 | [未决问题](results/OPEN_PROBLEMS.md)、[历史与限制](results/HISTORY_AND_LIMITS.md) |

四项式报告被明确标为**范围外、公开推导已恢复但原始验证包未恢复**。受限扇区的 16、固定消息的 $74N$、五项式 lift 都不会被误写成目标类的新全距离反例。全局常数放大界、与长度无关的正退化比例、一般二次退化界均未由现有材料解决。

## 4. 运行与复现

核心需要 Python 3.10+，不需要第三方包、求解器、随机性或网络。

```bash
python -m unittest discover -s tests -v
python scripts/check_repository.py
python scripts/reproduce.py --profile core --output checks/local
python -m bbcover compare upper
python -m bbcover compare lower
python -m bbcover bounds 14 --n 156 --k 4 --k2 8
python -m bbcover results
python -m bbcover results --view negative
python -m bbcover results DIST-UPPER
```

`bounds` 返回 `[2,28]` 是一般定理区间，**不是**重新算出的距离 12。该命令用整数运算实现三次界、长度界和满维 transfer 界，不用浮点数对含 $\pi$ 的解析端点作不安全取整。`compare` 和 `inspect` 重建矩阵、维数、覆盖和 attaining witness；全距离下界必须运行独立穷尽证书。

扩展复现需要 SymPy 和 `g++`，会运行两支线的 23+24 条保留审计命令：

```bash
python -m pip install -r requirements-research.txt
python scripts/reproduce.py --profile extended --output checks/extended
```

可选安装命令行入口：`python -m pip install -e .`，随后使用 `bbcover`。Python wheel 是轻量接口；**完整研究应使用本 Git 仓库或源码发布包，而非仅安装 wheel**。

[复现说明](docs/REPRODUCIBILITY.md)区分核心精确距离验证、保留证据审计和高开销的发现阶段重跑。超时、未完成或未排除绝不解释为成功。每次使用新的输出目录；不要以 `python -O` 运行原始验证器。

## 5. 仓库结构

```text
REPORT.md         首要阅读入口：主要结论、证据、采用边界与失败路线
results/          完整数学正文、25 篇过程笔记、104 条分状态研究记录
research/         两支线完整代码、原始证明、搜索数据和范围外公开数学报告
bbcover/          可安装的标准库接口、反例重建、精确整数界、结论查询
tests/            接口、代数、覆盖、CLI、目录一致性与发布测试
certificates/     两个反例的四个原始独立验证器及其证据
scripts/          复现、目录生成、完整性检查、源码打包和 GitHub 发布工具
.github/          持续集成、手动扩展审计、发布包构建、问题模板
checks/release/   已执行验证的记录；旧记录与本版重跑分目录保存
provenance/       三个输入 ZIP 的逐成员哈希、来源、迁移与正文覆盖审计
archive/          早期反例历史材料；不再承载主要研究支线
paper/            可选 LaTeX 排版稿与 PDF；正式署名由作者控制
docs/             使用、开发、证据格式和 GitHub 发布说明
```

## 6. 发布到 GitHub

这是可直接作为仓库根目录提交的结构，不存在 `anc/` 包装层。提供 Git bundle 时，可直接克隆已有 `main` 分支与版本标签；源码 ZIP 则可按[发布说明](docs/PUBLISH_GITHUB.md)初始化。

```bash
git clone bb-double-cover-research.bundle bb-double-cover-research
cd bb-double-cover-research
gh repo create bb-double-cover-research --source=. --remote=github --public --push
git push github v0.2.1
```

也提供 `scripts/publish_github.py`：默认只预览，指定 `--execute` 才创建并推送，不覆盖现有仓库、不强制推送。工作流已随源码提供；本地测试通过不代表 GitHub Actions 已在远端执行。

版本引用见 [CITATION.md](CITATION.md)。作者、单位、论文署名和复用许可没有被猜测或代签；当前未擅自指定 MIT/Apache/CC 等许可证，见 [NOTICE.md](NOTICE.md)。正式论文审批与仓库技术检查是分离的，未填写论文作者不会阻止阅读、测试或构建本研究仓库。

## 同调和类度量的完整结果

[五篇完整报告](results/README.md#homology) 补齐第三个输入包的数学内容：Bockstein 复形、deck Jordan 分解、类级变分与二元对偶、coupled exchange 公式、support–Bockstein 引理的无限族反例，以及低片度量 $\nu$ 的失败例子。$[[18j,4,4]]\to[[36j,4,6]]$ 家族中每个最短 logical 都被 transfer 杀死，且 $\rho=2j-1$；这不是新的 $d_2>2d$ 反例。主反例的类度量为 $\delta=6,\rho=4,\mu=14,\nu=22$。全部结论在 `homology` 分组下逐项索引。
