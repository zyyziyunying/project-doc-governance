# project-doc-governance

`project-doc-governance` 是一份用于整理项目文档结构的 Codex skill。

它解决的问题不是“把文档都塞进固定模板”，而是帮助 agent 在不同仓库里先识别本地文档分类规则，再决定文档应该保留、移动、拆分、归档还是原地修订。

## 这份 skill 做什么

- 按“文档用途”而不是“文档主题”做分类。
- 优先发现并遵守仓库本地 taxonomy，而不是把某个项目的目录习惯强行套到别的仓库。
- 区分人类文档的 source of truth 和 `AGENTS.md` 的 agent-operational 角色。
- 处理常见灰区文档，例如 review notes、status docs、closeout plans、investigations、RFCs、ADRs、meeting notes。
- 在移动或拆分文档后，同步检查 `docs/README.md`、目录索引、旧路径跳转页和明显的引用关系。

## 核心原则

1. 先读最小上下文，只加载做分类真正需要的文档。
2. 先找仓库本地 taxonomy，再决定是否回退到默认 taxonomy。
3. 先解决 authority，再做分类；不要让 `AGENTS.md` 静默改写人类文档分类语义。
4. 优先做最小变更，恢复结构清晰度，而不是大规模重写。
5. 文档移动后要同步索引、导航和旧路径可达性。

## 权威来源

- [`SKILL.md`](SKILL.md) 是这份 skill 的权威执行说明。
- [`references/default-doc-taxonomy.md`](references/default-doc-taxonomy.md) 是在目标仓库缺少本地分类规则时使用的 fallback taxonomy。
- [`references/skill-review-and-remediation.md`](references/skill-review-and-remediation.md) 记录复评、整改阶段、前向试跑证据和当前评分。

README 只负责说明这份 skill 的定位、使用场景和维护入口，不重复承载完整执行规范。

## 适用场景

在下面这些情况使用这份 skill：

- 你需要判断一个 doc 该放在哪里。
- 仓库里已经有 `docs/README.md`、`AGENTS.md` 或 taxonomy 文档，但它们的边界不清。
- 一份文档混合了背景说明和实现约束，需要拆分或重新落位。
- 历史计划、阶段状态、review findings、blocker notes 需要归档但不能直接删掉。
- 你要补齐 docs 索引、归档目录或旧路径跳转页。

## 不做什么

- 不把所有仓库强制改造成同一种 docs 树。
- 不让 `AGENTS.md` 成为唯一的人类文档分类真相。
- 不因为有一点不一致就重写整套文档。
- 不在本地 taxonomy 明确存在时绕过它直接套用默认规则。

## 典型工作流

1. 读取目标文档和最少必要的周边文档。
2. 查找目标仓库本地的 `docs/README.md`、`AGENTS.md`、taxonomy/structure/category README。
3. 用 skill 内定义的 precedence 规则判断哪个文档对当前分类决策有 authority。
4. 若本地规则缺失、失效或超出覆盖范围，再使用默认 taxonomy。
5. 给出动作结论：`move`、`split`、`archive`、`update in place` 或 `no-op`。
6. 同步更新索引文档、agent 指引、旧路径跳转页和明显引用。
7. 报告已完成和已延期的完整性检查项。

## 仓库结构

- [`SKILL.md`](SKILL.md): skill 正文，定义触发后的执行流程、输出要求和边界。
- [`references/default-doc-taxonomy.md`](references/default-doc-taxonomy.md): 默认文档分类模型和 gray-area mapping。
- [`references/skill-review-and-remediation.md`](references/skill-review-and-remediation.md): 复盘、整改阶段、试跑记录和当前评估。
- [`scripts/basic_validate.py`](scripts/basic_validate.py): 无外部依赖的轻量校验脚本。
- [`agents/openai.yaml`](agents/openai.yaml): skill 接入配置。

## 当前状态

截至 2026-03-21：

- 已完成 Phase 1-7 整改。
- 已在两个无关仓库做 forward test。
- 其中一次真实迁移样本验证了这套模式可落地：补 `docs/README.md`、归档历史文档、保留旧路径跳转页、同步 `AGENTS.md`。
- 当前复评分记录为 `8/10`，下一阶段重点是验证“目标仓库已经存在本地 taxonomy 时”的 authority 冲突处理是否依然稳定。

详细证据见 [`references/skill-review-and-remediation.md`](references/skill-review-and-remediation.md)。

## 维护建议

- 修改分类逻辑时，优先更新 `SKILL.md` 或相应 reference，不要让 README 变成第二套规范。
- 改动 authority model、gray-area mapping 或输出契约后，更新复评记录。
- 提交前运行：

```bash
python scripts/basic_validate.py
```
