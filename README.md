# project-doc-governance

`project-doc-governance` 是一个非常轻量的文档整理 skill。

它主要做三件轻量的整理动作：

- 优先读取目标仓库自己的文档放置规则
- 在缺少本地规则时提供一个默认 docs 结构和归档边界
- 在需要时只做最小必要的 move / archive / split / header / 邻近索引更新

## 默认 docs 结构

```text
docs/
  design/
    archive/
  check/
    archive/
  plan/
    archive/
  status/
    archive/
  problem/
    archive/
  discussion/
    archive/
  product/
    archive/
```

## 目录边界

- `product`: 要做什么
- `design`: 技术方案
- `check`: 验收和检查
- `plan`: 怎么执行
- `status`: 当前状态
- `problem`: 问题和风险
- `discussion`: 讨论中的事项

每个目录下的 `archive/` 只归档本类别的旧文件。

## 文件

- [`SKILL.md`](SKILL.md): 运行时规则
- [`references/default-doc-taxonomy.md`](references/default-doc-taxonomy.md): 默认 docs 结构
- [`references/default-doc-header-template.md`](references/default-doc-header-template.md): 默认 header 模板
- [`docs/README.md`](docs/README.md): 这个仓库自己的 docs 说明

## 定位

- 这不是治理系统
- 不带校验脚本
- 不带 review 流程
- 不带复杂规范
- 不会覆盖仓库自己已经写明的本地 docs 规则
