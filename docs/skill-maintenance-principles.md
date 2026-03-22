# project-doc-governance 维护原则

文档角色：用于演进这份 skill 的仓库内维护原则。
权威级别：对本仓库维护工作提供 guiding 约束。`SKILL.md` 仍是执行契约，`docs/README.md` 仍是本仓库 docs 的放置 authority。

## 原则

### 1. 本地 Taxonomy 优先

把目标仓库自己的本地 taxonomy 作为起点。
不要因为 fallback 结构看起来更整齐，就重塑别人的 docs 树。

### 2. 先判定 Authority，再决定落位

先决定这次放置决策由哪个本地文档控制，再开始分类。
不要让 `AGENTS.md` 静默覆盖一个仍在维护的人类文档 taxonomy。

### 3. 按用途分类，不按主题分类

按文档的最强功能决定落位。
如果一份文件同时混合背景说明和绑定性实现规则，就拆分它，而不是让一份文件同时承担多个角色。

### 4. Fallback 只补空白，不接管整棵树

只有在本地规则没有覆盖的那一部分决策里，才使用 fallback taxonomy。
不要让 fallback 模型成为大范围猜测性重组 docs 结构的理由。

### 5. 结构变更必须同步它的 Source Of Truth

如果一个任务新增类别、移动文档或改变类别语义，就要在同一个任务里更新仓库本地 taxonomy 或 index 文档。
不要让已移动的文件和人类可读的 source of truth 脱节。

### 6. 遇到歧义先暴露，不要猜

当本地规则出现 stale、partial 或冲突时，要报告歧义并限制推断范围。
如果这些歧义会实质影响结果，就停下来暴露冲突，而不是自行拼出一套合并规则。
