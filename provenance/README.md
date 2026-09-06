# Provenance and completeness

`import_map.json` accounts for every file-member record in the three original ZIPs: 771 records, including byte-identical duplicate aliases. Every entry has a supplied-source hash and either a current `stored_path` or an explicit omission reason. Use the inventory rather than an older README's file count.

`github_reorganization.json` records the byte-preserving promotion into `research/` and restoration of previously omitted public mathematical material. The full original result ledgers are under the research branches; `results/catalog.json` retains their records and explicit current-status overlays.

`theory_render_audit.json` records complete core-theory conversion: source/output hashes, formula count, proof/theorem blocks, and internal references. `note_render_audit.json` does the same source/output association for the twenty-five complete research notes. These are text-coverage audits, not proofs of the mathematical statements.

`external_sources.json` records bibliographic information and the input third-party PDF hash without redistributing that PDF. `legacy_summaries/` retains historical reading/status pages; their old missing-file statements and relative paths are not the active navigation of this GitHub edition.

## 当前采用状态与原文保留

v0.2.1 新增的 [review_policy.json](../results/review_policy.json)是显式编者状态层，不是对源文件的改写。25 篇阅读版在原正文前加入各自的范围、失效路线和依赖缺口提示；原 `research/` 文件仍按输入哈希逐字节检查。状态分类和登记的主要依赖不声称构成独立数学审稿或形式化完整证明图。
