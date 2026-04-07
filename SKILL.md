---
name: project-doc-governance
description: Place, split, and reorganize project docs using repository-local docs rules first, then a fallback design/check/plan/status/problem/discussion/product taxonomy and a simple header template when needed.
---

# Project Doc Governance

Use this skill to keep project docs organized in a lightweight way.

## Core Rules

1. Build minimal context.
Read only the target doc and the local docs files needed for the decision.

2. Check repository-local taxonomy first.
If the repository already has local docs rules, follow them first.

3. Resolve authority before classifying.
Use the nearest local placement rule that clearly applies.
If local docs conflict, stop and report the conflict instead of guessing.

4. Use the fallback taxonomy only when local rules do not answer the question.
Use [references/default-doc-taxonomy.md](references/default-doc-taxonomy.md) as the default structure.

5. Classify by purpose.
Use these default categories when local docs do not say otherwise:

- `docs/product/`: what to build
- `docs/design/`: technical design
- `docs/check/`: validation and acceptance
- `docs/plan/`: execution plan
- `docs/status/`: current status
- `docs/problem/`: active problems
- `docs/discussion/`: open discussion

Each category keeps its own `archive/` subdirectory.
Move older or superseded files into the matching category archive, not a different one.
Split mixed-purpose docs when one file is doing too many jobs.

6. Use a simple header when needed.
If the repository has its own header pattern, follow it.
Otherwise use [references/default-doc-header-template.md](references/default-doc-header-template.md) as a lightweight fallback.

7. Keep changes small and obvious.
Prefer moving, splitting, or lightly rewriting docs over inventing new categories.
If you move docs, update obvious nearby indexes or links in the same task.

## Output Expectations

When using this skill, state:

- the classification decision
- which local rule or fallback rule controlled the decision
- the exact action summary: move, split, archive, update in place, or no-op
- which files were updated
- any follow-up links or index updates that still need attention

## Boundaries

- Prefer the smallest change that restores structural clarity.
- Do not override a repository's local docs rules with this fallback.
- Do not treat a general `README.md` as docs taxonomy authority unless the repository clearly does.
- Do not turn this into a heavy review or validation workflow.
