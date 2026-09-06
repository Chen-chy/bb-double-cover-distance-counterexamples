# 发布完整研究仓库到 GitHub

源码根目录就是仓库根目录；不要再放进 `anc/` 或论文附件目录。

## 从提供的 Git bundle 发布

Git bundle 包含 `main` 分支、初始提交和版本标签，不依赖远程仓库即可克隆。以下命令在你自己已经授权的 GitHub CLI 环境运行：

```bash
git clone bb-double-cover-research.bundle bb-double-cover-research
cd bb-double-cover-research
python scripts/check_repository.py
python scripts/check_release.py
gh repo create bb-double-cover-research --source=. --remote=github --public --push
git push github v0.2.1
```

`github` 是新远端名，避免覆盖 bundle 克隆产生的本地 `origin`。需要先做私有审阅时，把 `--public` 改成 `--private`。组织仓库可以把名称写为 `OWNER/bb-double-cover-research`；权限和可见性由你的实际账号控制。

## 从源码 ZIP 发布

解压后进入含 `README.md` 和 `pyproject.toml` 的目录，使用你自己的 Git 身份：

```bash
git init -b main
git add .
git commit -m "Publish complete BB double-cover research repository"
gh repo create bb-double-cover-research --source=. --remote=github --public --push
```

不要把 ZIP 文件本身作为仓库唯一内容上传。不要在 GitHub 新仓库中另行预置 README、LICENSE 或 `.gitignore` 后再强推覆盖。

## 仓库内的发布工具

```bash
python scripts/publish_github.py --repo bb-double-cover-research --public
python scripts/publish_github.py --repo bb-double-cover-research --public --execute
```

第一条仅预览本地检查和发布命令。第二条要求本地已有干净 Git 提交、GitHub CLI 已授权，然后创建新仓库并推送；如果远端已存在则拒绝覆盖。工具不读取或打印 token、不强推、不修改其他项目，不伪造成功 URL。这个工具必须在实际具备 `gh` 和账号授权的环境运行。

## 发布说明与持续集成

仓库自动执行快速检查与核心精确证书；扩展研究审计是手动工作流。发布包构建工作流生成完整源码归档，不自动创建公开 GitHub Release。要发布版本，应在检查通过后推送标签，并使用生成的 `dist/` 源码包；普通 Python wheel 不是完整研究成果包。

`NOTICE.md` 记录未擅自分配复用许可。未补充论文作者与单位只影响正式论文投稿，不阻止仓库的代码测试或源码归档；它也不自动授予任何开放源码许可。发布权、署名与许可的确认由实际作者/权利人控制。

命令依据 [GitHub 官方本地导入说明](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github) 和 [gh repo create 手册](https://cli.github.com/manual/gh_repo_create)。
