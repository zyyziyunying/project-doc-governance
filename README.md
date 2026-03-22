# project-doc-governance

`project-doc-governance` 是一份用于治理项目文档结构的 Codex skill。

它的目标不是把所有仓库套进同一套 docs 树，而是让 agent 先识别目标仓库自己的文档规则，再决定某份文档应该保留、移动、拆分、归档还是原地修订。

## 这份 skill 负责什么

- 优先发现并遵守仓库本地 taxonomy。
- 先解决 authority，再做文档分类。
- 只在本地规则没有覆盖当前决策时使用 fallback taxonomy。
- 按文档用途处理 mixed-purpose docs、归档和结构同步。

## 文件分层

- [`SKILL.md`](SKILL.md): 这份 skill 的执行契约。这里放 agent 必须遵守的最小治理规则。
- [`docs/README.md`](docs/README.md): 这个 skill 仓库自己的人类文档放置规则。
- [`docs/skill-maintenance-principles.md`](docs/skill-maintenance-principles.md): 维护这份 skill 时使用的高层原则。
- [`references/default-doc-taxonomy.md`](references/default-doc-taxonomy.md): 目标仓库缺少本地规则时使用的 fallback taxonomy。
- [`docs/problem/skill-review-and-remediation.md`](docs/problem/skill-review-and-remediation.md): 当前仍然活跃的验证缺口和下一道 review gate。
- [`docs/problem/archive/2026-03-21-skill-review-history.md`](docs/problem/archive/2026-03-21-skill-review-history.md): 已归档的历史评审、整改阶段和试跑证据。

## 适用场景

- 需要判断一份 doc 应该放在哪里。
- 本地 taxonomy、`docs/README.md`、`AGENTS.md` 的边界不清。
- 一份文档同时混合背景说明和绑定性规则。
- 历史计划、review findings 或 blocker notes 需要归档但不能直接删除。
- 调整 docs 结构后需要同步索引、导航或旧路径说明。

## 维护约束

- 改分类规则时，优先更新 [`SKILL.md`](SKILL.md) 或 [`references/default-doc-taxonomy.md`](references/default-doc-taxonomy.md)。
- 改这个仓库自己的 docs 放置规则时，更新 [`docs/README.md`](docs/README.md)。
- 活跃问题和验证缺口只留在 [`docs/problem/skill-review-and-remediation.md`](docs/problem/skill-review-and-remediation.md)；详细历史留在 archive。
- 提交前运行：

```bash
python scripts/basic_validate.py
```
