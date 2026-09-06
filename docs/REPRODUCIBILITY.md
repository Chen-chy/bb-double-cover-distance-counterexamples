# 复现与验证范围

[首页](../README.md) · [完整算法证明](../results/theory/06-certificate-algorithms.md) · [证据格式](DATA_FORMATS.md)

## 核心精确复现

Python 3.10+ 标准库即可，无网络、第三方求解器或随机性。仓库代码约定 $n$ 是底码物理比特数。

```bash
python -m unittest discover -s tests -v
python scripts/check_repository.py
python scripts/reproduce.py --profile core --output checks/local
```

核心流程重新运行单元测试、端口行列式与电压核恒等式审计，以及四个独立反例验证器。两个搜索方法分别使用 bitset/二元消元与多项式/集合表示，分支规则和边界 oracle 不同。它们没有被重构为共用 `bbcover` 的一个验证器。

核心流程逐项比较上下游实现的 X/Z 矩阵、全部排除范围内的 circuit、attaining witness、连通性及完整 Tanner 邻域双射。升距覆盖和降距底码共享的 period-78 码必须逐字节相同；其 741 个短 circuit 也必须相同。

```bash
python certificates/upper/verify_bitset.py --output-dir checks/upper-bitset
python certificates/upper/verify_polynomial.py --output-dir checks/upper-polynomial
python certificates/lower/verify_lower_bitset.py --output-dir checks/lower-bitset
python certificates/lower/verify_lower_polynomial.py --output-dir checks/lower-polynomial
```

上述独立入口可脱离便利库运行。完整默认参数见各文件 `--help`。

## 保留研究审计

```bash
python -m pip install -r requirements-research.txt
# 另外需要 C++17 g++。
python scripts/reproduce.py --profile extended --output checks/extended
```

这会先执行核心流程，再在物化的工作副本中执行 amplification 的 23 条及 degradation 的 24 条保留审计命令。原始证明、潜能证书、数据和脚本字节不被修改。驱动与命令清单位于 [amplification](../research/amplification/tools/run_checks.py) 和 [degradation](../research/degradation/scripts/run_checks.py)。

这不是所有发现扫描的完全重跑，也不默认从头生成两套高开销的完整 weight-six 分类。分类源代码、原参数与重生成说明保留在相应研究目录。X00 的原始独立代码包缺失，不把其公开推导标为机器精确认证。

## 同调与类度量的保留审计

```bash
python scripts/verify_homology_history.py --output checks/homology-history
```

这会隔离运行第三个 ZIP 保留的四个早期验证器，检查 support-family、类度量与更强低片猜想的反例。有限参数检查与 all-degree min-plus/Bellman 证书的作用域以各日志和完整证明为准，不把有限枚举当全参数定理。

## 输出与失败语义

每次选择新的输出目录，避免混用旧成功记录。不要用 `python -O` 或 `PYTHONOPTIMIZE`；部分原始审计使用断言。`--timeout` 是每命令超时阈值；任何超时都会记录为 `incomplete_timeout`，而不是“没有找到所以不存在”。进程失败或证据不一致都会产生非零退出码。

`report.json` 保存命令、状态、解释器、平台、耗时、脚本与输出哈希；日志与规范化矩阵/circuit 放在同一个输出目录。平台信息和本地路径只用于审计，不是后续执行所需的硬编码路径。

`checks/release/github-v0.2.0/` 是 v0.2.0 的执行历史，不是 v0.2.1 的重跑。v0.2.1 的实际检查位于 `checks/release/report-v0.2.1/`；其中 `interrupted-core/` 是执行工具中断的未完成尝试，不能当成通过记录；完成状态以新的 `core/report.json` 和 `summary.json` 为准。以相应记录的命令、时间和作用域为准，不把旧执行的路径当新目录导航。自动生成的工作副本和编译二进制不进入 Git 发布包。

## 便利接口与完整证书

`inspect` / `compare` 验证构造、维数与一个非边界 witness；它们不是通用距离求解器。`bounds` 只计算主定理的安全整数区间。`results` 是完整结论和证据位置查询器。要证明三组精确距离的下界，必须使用穷尽证书与其算法完备性论证。

数学定理的证据是正文中的一般证明。有限行列式、电压核或某些参数的测试只能检查实现和示例，不能替代一般证明。

## GitHub Actions

CI 定义在 `.github/workflows/`：快速单元/目录检查、核心精确证书、手动扩展审计和源码打包。它们不需要个人访问令牌来执行研究计算。远端首次执行后才会有真实 Actions 结果；本仓库不伪造已通过的远端 badge。

## 报告与过程的采用方式

先读[主报告](../REPORT.md)及[状态表](../results/STATUS.md)。`python -m bbcover results` 默认只列主报告索引，`--view all` 才列全部 104 条记录。`scripts/check_report.py --check` 检查采用标签、已知依赖与报告一致性，不检查一般定理的数学正确性。原始证书、符号证明和实验扫描仍按前述不同证据层次使用。
