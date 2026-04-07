---
name: project-doc-governance
description: Use when project docs need placement, archiving, splitting mixed-purpose content, or adding a lightweight standard header, especially when document locations conflict or no clear taxonomy exists.
---

# Project Doc Governance

Use this skill to keep project docs organized in a lightweight way.

## Core Rules

1. Start with minimal, action-specific context.
Read the target doc first.
For placement or archive decisions, read only the rule files needed for the decision.
This can include local docs files near the target doc and a repository-level docs taxonomy, `CONTRIBUTING.md`, or similar contribution doc when it explicitly defines placement or header requirements.
For split tasks, read only the target doc, any directly relevant local rule that defines split placement for that subtree, any directly relevant repository-level docs taxonomy, `CONTRIBUTING.md`, or similar contribution doc that defines placement defaults or restrictions, any directly relevant local or repository-level header or metadata rule that applies to newly created split outputs, and any directly affected index, link, or split output files before editing them.
For header tasks, read only the target doc, the directly relevant local rule that defines the header or metadata format, any directly relevant repository-level header or metadata rule, and any directly affected files before editing them.
Do not scan broadly for conventions when a nearby or repository-level rule already answers the question.

2. Check repository-local rules first.
If the repository already has local docs taxonomy, split-placement, or header-format rules, follow them first.

3. Resolve authority before classifying.
Decide placement and header authority separately.

For placement, prefer the most specific applicable local rule in this order:

- a docs rule next to the target doc or in its nearest ancestor directory that defines placement for that subtree
- a repository-level docs taxonomy or contribution doc that defines broader placement defaults
- this skill's fallback taxonomy

Treat the nearest applicable placement rule as the default authority for that subtree, even when the repository also has broader placement guidance.
Only treat placement as a conflict when applicable rules give mutually exclusive instructions that cannot reasonably be read as "global default plus local override", or when a repository-level rule explicitly forbids local overrides for that case.
If a true placement conflict remains after that check, stop and ask the user to resolve it instead of guessing.
If two applicable rules at the same scope conflict, also stop and ask the user to resolve it instead of guessing.

For header or metadata updates, follow the most specific applicable format that is compatible with broader repository requirements.
Only carry forward repository-level required keys when the local and repository rules use the same syntax or the repository explicitly treats them as additive.
If applicable header rules use incompatible formats or their precedence is unclear, stop and ask the user instead of inventing a mixed header.
Use this skill's fallback header template only when no applicable local or repository-level rule defines the required header format.

4. Use fallback guidance only when local rules do not answer the question.
Use [references/default-doc-taxonomy.md](references/default-doc-taxonomy.md) for default placement.
Use [references/default-doc-header-template.md](references/default-doc-header-template.md) for a default header.

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
Split mixed-purpose docs only when placement cannot be made clear with a smaller change.
When splitting, place each output using the most specific applicable local rule first, then any applicable repository-level placement default, and use the fallback taxonomy only if neither answers the placement question.
For any new split output that needs a header or metadata block, follow the most specific applicable local or repository-level header rule before falling back to this skill's default header template.
Keep the result as small and obvious as possible.

6. Use a standard fallback header only when needed.
If the repository defines a repository-level or local header or metadata format, follow the most specific applicable format.
Only combine repository-level required keys with nearer subtree-specific additions when the rules are clearly additive and use compatible syntax.
If the rules use incompatible formats or do not say how precedence works, ask the user instead of creating a merged header.
Otherwise use [references/default-doc-header-template.md](references/default-doc-header-template.md) as the lightweight header template.
Only add header fields that are true and useful.

7. Keep changes small and obvious.
Prefer move, archive, or minimal metadata updates before content rewrites.
If you move docs, update obvious nearby indexes or links in the same task after reading those directly affected files.

## Output Expectations

When using this skill, state:

- the classification decision
- whether local rules were checked first
- which placement rule and which header rule controlled the decision, or that one of them fell back
- for local rules, the format or pattern that was found, such as the taxonomy path, frontmatter shape, or required metadata keys
- if no local rule was found, explicitly say that fallback guidance was used
- the exact action summary: move, split, archive, add header, update header, update in place, or no-op
- which files were updated
- any follow-up links or index updates that still need attention

## Boundaries

- Prefer the smallest change that restores structural clarity.
- Do not override a repository's local placement or archive taxonomy with this fallback.
- Do not override a repository's local split-placement or header format with this fallback.
- For `split`, do not scan broadly; read only the directly relevant local placement rules, any directly relevant repository-level placement rule, and any directly relevant local or repository-level header or metadata rule for newly created outputs.
- For `header`, do not scan broadly; read only the directly relevant local header or metadata rule and any directly relevant repository-level header or metadata rule.
- Do not treat a general `README.md` as docs taxonomy authority unless the repository clearly does.
- Do not scan broadly when a local rule or direct neighbor already answers the placement question.
- Do not guess which rule is newer when applicable rules create a true placement conflict that cannot be read as global default plus local override; ask the user to resolve it.
- Do not turn this into a heavy review or validation workflow.
