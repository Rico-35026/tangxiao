---
name: commit-push-github
description: 提交当前项目并推送到 GitHub 仓库。当用户要求推送到 github、提交到 github、commit 并 push 到 GitHub 时使用此 skill。
---

# 提交项目到 GitHub

将当前项目通过 git commit 并 push 到 GitHub 仓库：https://github.com/Rico-35026/tangxiao.git

## 步骤

1. 运行 `git status` 查看当前变更
2. 运行 `git diff` 和 `git log --oneline -5` 了解变更内容和提交历史
3. 暂存所有变更：`git add -A`
4. 创建提交（使用简洁的中文 commit message，参考历史提交风格）：`git commit -m "描述变更内容"`
5. 检查远程仓库配置：`git remote -v`
   - 优先使用 SSH（已配置公钥）：
     - 添加：`git remote add github git@github.com:Rico-35026/tangxiao.git`
     - 更新：`git remote set-url github git@github.com:Rico-35026/tangxiao.git`
   - 如果 22 端口被拦截（Connection refused），改用 HTTPS：
     - `git remote set-url github https://github.com/Rico-35026/tangxiao.git`
6. 推送：`git push -u github master`（如主分支为 main 则用 `main`）
   - HTTPS 推送时浏览器会弹出 GitHub 登录授权，用户确认后即可

## 注意事项

- 不要提交敏感信息（密钥、密码等）
- commit message 应简洁明了，描述本次变更内容
- SSH 地址：`git@github.com:Rico-35026/tangxiao.git`（需 22 端口可达）
- HTTPS 地址：`https://github.com/Rico-35026/tangxiao.git`（走 443，大多数网络可用）
- 如果 push 被拒绝，先运行 `git pull --rebase github <branch>` 再重试
