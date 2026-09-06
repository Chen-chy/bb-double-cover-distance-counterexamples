# 接口与证据格式

## 物理约定

矩形群为 $\mathbb Z_\ell\times\mathbb Z_m$。单项式 $(i,j)$ 的坐标是 `i*m+j`；右块偏移 `ell*m`。`HX=(M_A M_B)`、`HZ=(M_B^T M_A^T)`。内部标准库接口用非负 Python 整数表示二元向量，最低位是索引 0。投影和边界运算始终使用物理基，不把非等距正规形后的普通重量当作物理距离。

## 规范矩阵与 circuit

矩阵文本以 `GF2MATRIX v1` 开头，第二行是行数、列数，随后为 0/1 ASCII 行。circuit 是升序物理坐标集合。历史 upper 文件有两行头，lower 文件没有；跨实现比较只移除该已记录的头，不忽略任何 support 差别。

## 结论目录

`results/catalog.json` 是维护用完整目录，`bbcover/catalog.json` 是由相同源生成的可安装副本。`schema_version=1`。每条记录含：`id`、`branch`、`statement`、`scope`、`evidence_type`、`status`、`proofs`、`evidence`、`limitations`。历史项另保留 `original_record`，状态修复放在 `current_update` 中；缺失或未公开的路径仅列在 `unavailable_historical_sources`，不假装它们可读取。

`exact-computer-assisted-certificate` 表示完整有限最小值需要证明和穷尽证书。`symbolic-proof-supplied` 表示有一般证明文本。`symbolic-proof-consolidation` 标识合并稿补充推论。`reported-proof-only` 不表示独立原代码包已恢复。`open` 不表示被解决。历史更弱界不会自动删除。

修改后执行 `python scripts/build_catalog.py` 重新生成两个 JSON 与 Markdown 表；`--check` 只比较不写入。不得仅编辑可安装副本。

## 来源与渲染

`provenance/import_map.json` 对三个输入 ZIP 的每个成员保存输入名、原路径、长度、SHA-256、当前保留路径或省略原因。重复文件可映射到同一原始字节。`github_reorganization.json` 记录本次迁移与恢复。

`theory_render_audit.json` 记录七章主文源与阅读版的哈希，以及公式/定理/证明块覆盖。`note_render_audit.json` 记录二十五篇完整笔记的源和阅读版哈希。它们验证文本对应关系，不判断数学正确性。
