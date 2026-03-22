# project-doc-governance 候选规范（讨论稿）

文档角色：用于讨论和收敛这份 skill 的候选执行规则（shadow spec）。
状态：discussion draft，不是当前生效契约。
Baseline：`SKILL.md` 与 `references/default-doc-taxonomy.md`。
同步规则：讨论收敛后，把接受的规则回写到 `SKILL.md` 或 `references/default-doc-taxonomy.md`；`docs/README.md` 只负责本仓库 docs 的放置 authority。

## 读取方式

- 本文件只记录与 baseline 不同、或 baseline 尚未定案的候选规则。
- 未变化的现行规则只引用，不在这里复述。
- 如果本文件出现未标记提案的规则性表述，且与 baseline 不一致，应把它视为讨论稿漂移并优先修正。

## 当前状态

当前没有仍在讨论中的规则 delta。
2026-03-22 已把“高可见旧路径迁移时默认保留 redirect stub，其余仍需可追踪性的场景至少保留 breadcrumb”回写到 `references/default-doc-taxonomy.md`。
该提案的收敛说明与证据归档见 `docs/problem/archive/2026-03-21-skill-review-history.md`。

## 提案模板

### 提案：<短标题>

- Baseline 指向：`SKILL.md` 或 `references/default-doc-taxonomy.md` 中被讨论的条目
- 拟议变化：希望改成什么
- 预期行为差异：分类、停机条件或同步义务会如何变化
- 触发样本或风险：是什么案例、误判或维护问题促成了这条提案
- 开提案证据：哪个具体样本、决策记录或保留工件说明 baseline 不够
- 收敛验证：哪个真实任务回放、forward-testing 或保留证据证明提案改善了该类决策
- 边界验证：如果提案改动 authority、fallback 或 stop conditions，要补哪个相邻边界样本
- 回写目标：收敛后应修改哪个权威文件

## 讨论约束

- 单条提案应尽量独立，避免把多个行为变化捆成一条。
- 如果某条提案会改变实际分类行为，应在 `docs/problem/skill-review-and-remediation.md` 里补对应的验证缺口或收敛条件。
- 如果只有问题直觉、没有最低样本证据，先把它当作待观察假设，不要直接写成候选规则。
- 接受或否决后的提案不得长期留在本文件里充当历史堆栈；需要保留时，应移到 `docs/problem/` 或 archive。
