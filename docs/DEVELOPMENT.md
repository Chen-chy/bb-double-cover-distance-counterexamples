# 开发与维护

维护接口是 `bbcover/`；独立证书及 `research/` 的原始证明/脚本作为不可静默重写的来源快照。修正原始结论时，应另加明确的修订证明与状态覆盖，而非修改历史哈希后宣称原文未变。

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
python scripts/check_repository.py
```

修改数学 LaTeX 后，用 `python scripts/build_theory.py` 生成完整 GitHub 章，需要 Pandoc。现成阅读版已经提交，读者不需要 Pandoc。脚本保留所有展示公式和 theorem/proof 块，并修复跨章引用。修改阅读版生成逻辑后也必须重建；`--check` 可以无 Pandoc 检查源与输出哈希。

原始研究笔记的完整阅读版由 `python scripts/build_notes.py` 生成。结论登记表和安装包目录由 `python scripts/build_catalog.py` 生成。

```bash
python scripts/build_notes.py --check
python scripts/build_theory.py --check
python scripts/build_catalog.py --check
python scripts/write_manifest.py
python scripts/check_release.py
python scripts/package_repository.py --output dist
```

`SHA256SUMS.txt` 是发布快照清单，不是每次开发自动“洗白”变更的工具；生成器先核对导入原始字节。CI 在普通提交上检查结构、来源与文档同步，在发布包构建时刷新并校验快照清单。

源码 ZIP 包含研究证明、代码、数据和证书；wheel 仅包含稳定接口、示例和结论查询数据。发布脚本从允许的源文件集合生成确定元数据的归档，不包含 `.git`、虚拟环境、缓存、工作副本或个人配置。

自动化初始 Git 提交的身份只标识打包工具，不代表论文作者。正式贡献者可在正常 Git 提交中使用自己的真实身份；论文署名与许可由权利人另行确认。
