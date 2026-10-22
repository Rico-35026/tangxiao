---
name: commit-push-gitee
description: 提交当前项目并推送到 Gitee 仓库。当用户要求提交项目、commit 并 push、推送到 gitee、提交代码时使用此 skill。
---

# 提交项目到 Gitee

将当前项目通过 git commit 并 push 到 Gitee 仓库：https://gitee.com/Tang_xiao-gitee/tangxiaowangye.git

## 步骤

1. 运行 `git status` 查看当前变更
2. 运行 `git diff` 和 `git log --oneline -5` 了解变更内容和提交历史
3. 暂存所有变更：`git add -A`
4. 创建提交（使用简洁的中文 commit message，参考历史提交风格）：`git commit -m "描述变更内容"`
5. 检查远程仓库配置：`git remote -v`
   - 如果没有远程仓库或地址不匹配，添加/更新：
     - `git remote remove origin`（如已存在）
     - `git remote add origin git@gitee.com:Tang_xiao-gitee/tangxiaowangye.git`
6. 推送：`git push -u origin main`（如主分支为 master 则用 `master`）

## 注意事项

- 不要提交敏感信息（密钥、密码等）
- commit message 应简洁明了，描述本次变更内容
- 如果 push 被拒绝，先运行 `git pull --rebase origin <branch>` 再重试
