# GitHub v0.2.0 本地验证记录

本目录记录独立研究仓库整理过程中的实际执行。汇总见 [SUMMARY.json](SUMMARY.json)。

核心证书：[core/report.json](core/report.json)；原研究审计：[extended/report.json](extended/report.json)（23+24 条命令）；同调/类度量历史审计：[homology-history/report.json](homology-history/report.json)（4 个程序）。`extended` 先于同调阅读版补齐执行，其主证书和两支线源代码未改变；最终 `core` 和目录检查基于 104 项登记表执行。

打包接口使用隔离虚拟环境安装，从源码目录之外调用；[安装报告](installed-package.json)记录实际模块位置。GitHub Actions 只有[静态检查](workflow-static-check.json)，没有伪造远端运行。

临时工作副本和编译产物按规则移除，原始日志、退出状态、精确矩阵、circuit 集及脚本/输出哈希保留。完整 Git bundle/源码包解包验证记录在交付的独立 release report 中，避免把最终提交哈希写回同一个提交形成循环。
