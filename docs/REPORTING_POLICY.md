# 主报告与研究过程的维护规则

[主报告](../REPORT.md) · [逐项状态](../results/STATUS.md) · [本版实际检查](../checks/release/report-v0.2.1/summary.json)

`REPORT.md` 与 `REPORT.en.md` 是首页首要入口。新记录必须先在 `results/review_policy.json` 标明范围、采用方式和已知主要依赖，再生成登记表。它们不是数学审稿自动化：分类、测试和源码哈希都不能证明一般定理正确。

`main` 进入主要结论，`scoped` 按原假设使用，`negative` 是有效的否定结果，`historical` 是保留的较弱界，`gap` 有尚未闭合的证据或依赖，`exploratory` 是有限探索记录，`open` 是未决问题，`outside` 不在严格三项式目标类中。只有重新提供所缺证明／证书并审阅范围后，才允许改变有缺口记录的采用状态。

不能把 `open` 的问题出处写成完整证明，不能把 `negative` 所否定的路线放进正面证明依赖，不能把 `outside` 当成目标类反例。原始 `research/` 文件保持字节不变；在 `results/notes/` 的阅读版顶部显示具体纠正，不删除历史反例来制造一致性。

```bash
python scripts/build_notes.py
python scripts/build_catalog.py
python scripts/check_report.py --check
python scripts/check_repository.py
python -m unittest discover -s tests -v
```

更新采用状态时必须同时更新中英文主报告、受影响的阅读提示和回归测试。生成器采用范围／证据层，不以旧记录的 `proved` 字样或程序的成功退出自动升级结论。发布清单在全部修改和检查完成后重新生成。
