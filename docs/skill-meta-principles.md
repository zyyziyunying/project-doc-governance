# project-doc-governance 元原则

文档角色：约束这份 skill 作为一个 skill 产品应如何演进。
范围边界：本文件不定义目标仓库 docs 的分类结果，也不直接构成运行时执行契约。
关系说明：`SKILL.md` 是现行执行契约，`references/default-doc-taxonomy.md` 承载 fallback 语义，`docs/skill-shadow-spec.md` 用于讨论候选规则。

## 原则

### 1. 保持单一运行时契约面

把运行时必须遵守的规则集中在 `SKILL.md` 与 `references/default-doc-taxonomy.md`。
不要让 `README.md`、`docs/README.md` 或讨论稿承担运行时补充契约的职责。

### 2. 让讨论稿以 delta 为中心

`docs/skill-shadow-spec.md` 只记录与 baseline 不同、或 baseline 尚未定案的候选规则。
未变化的现行规则只引用，不复述。
每条候选规则都应写明 baseline 指向、拟议变化、预期行为差异、触发该提案的样本或风险，以及收敛后的回写目标。
提案一旦接受或否决，就应从讨论稿移除或归档，不把讨论稿积累成第二份长期规范。

### 3. 让 `SKILL.md` 主要承载流程、边界与停机条件

把 authority 判定、fallback 触发条件、冲突处理和 stop conditions 放在 `SKILL.md`。
把类别语义、文档类型映射和较长的补充说明优先放到 `references/`，避免把 `SKILL.md` 写成案例百科。
保持 `SKILL.md` 简短，可被另一实例的 Codex 快速加载和执行。

### 4. 让规则演进由真实案例驱动

新增、收紧或拆分规则，应由真实仓库中的稳定误判、歧义或维护成本推动，而不是因为结构看起来更整齐。
把验证分成“开提案”与“收敛入契约”两级门槛。
开提案的最低门槛：至少有一个具体样本、决策记录或保留工件，能说明 baseline 为什么不够。
写回运行时契约的最低门槛：至少有一个保留的正向验证，证明候选规则在真实任务回放或 forward-testing 中改善了该类决策。
如果提案会改动 authority 优先级、fallback 触发条件或 stop conditions，还要额外有一个边界样本，证明它没有靠扩大猜测范围来“修好”主样本。
当候选规则会改变分类行为时，在 `docs/problem/skill-review-and-remediation.md` 记录对应的验证缺口、样本或收敛条件。
达不到上述门槛时，可以保留为讨论中的假设，但不要把它并入 `SKILL.md` 或 `references/default-doc-taxonomy.md`。

### 5. 把本仓库的额外文档视为有意识的维护例外

这个 skill 仓库保留少量额外文档，是为了维护、验证和讨论这份 skill，而不是为目标仓库输出更多默认结构。
新增 docs 文件前，先判断它是否承担了不可替代的角色；若只是重复已有契约、reference 或 tracker，就不要新增。
维持 `docs/` 树的小而清晰，让每个文件都能回答“它为什么不能并入现有文件”。

### 6. 把文档 header 视为长期投入，但把边界收在 header

轻量文档 header 模板值得长期维护，因为它能在不规定正文排版的前提下，稳定补足文档开头最关键的上下文：当前状态、范围和 authority。
这类模板应优先放在 `references/` 中作为 fallback scaffold，而不是写成目标仓库必须照搬的正文规范。
如果目标仓库已经有本地 header 或 metadata 约定，优先遵守本地格式。
除非有持续保留的真实样本证明“仅靠 header 仍不足以避免稳定误判”，否则不要把 fallback 模板扩张成正文结构模板或章节模板。
