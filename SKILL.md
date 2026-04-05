---
name: project-doc-governance
description: Organize, classify, review, move, split, and archive project documentation with a stable purpose-based taxonomy. Use when Codex needs to decide where a doc belongs, create or relocate docs files or categories, separate background knowledge from binding implementation constraints, keep docs structure aligned with repository-local taxonomy or explicit placement docs, or clean up stale project docs.
---

# Project Doc Governance

Use this skill to keep repository documentation structurally consistent without imposing one repository's taxonomy on another.

## Core Rules

1. Build minimal context.
Read only the target document(s) and the local structure docs needed for the current decision.

2. Check repository-local taxonomy first.
Read relevant taxonomy or placement docs, category index files, neighboring directory README files, the nearest `AGENTS.md`, and `docs/README.md` only when it explicitly defines human-facing placement for the target scope.
Do not use a general project `README.md` as taxonomy authority by default.

3. Resolve authority before classifying.
Use the nearest dedicated taxonomy or placement doc first.
Otherwise use repository-level taxonomy or structure docs.
Use `docs/README.md` only when it explicitly defines placement for the target scope.
Use `AGENTS.md` for agent-operational behavior and pointers to the source of truth, not to silently rewrite human-facing taxonomy.
If same-scope local sources still conflict and the outcome would change materially, stop and report the conflict instead of guessing.

4. Decide whether local rules are usable.
Treat a local rule as:

- missing when it does not cover the current document class or destination decision
- partial when it defines a stable pattern for part of the tree but leaves this case underspecified
- stale when it points to removed paths, contradicts the active tree, conflicts with a more specific maintained source, or clearly predates a known restructure

If local rules are partial, extend the stable local pattern and use fallback rules only for the uncovered portion.
If local rules are stale but a stronger active source still makes the outcome clear, follow the stronger source and report the stale doc that needs synchronization.
If stale or conflicting local docs would materially change the result, report the ambiguity before doing a broad reorganization.

5. Use the fallback taxonomy only when local rules do not settle the current decision.
Read [references/default-doc-taxonomy.md](references/default-doc-taxonomy.md) before creating categories or moving docs by default rules.
Do not adopt the execution-heavy local pattern just because it looks cleaner.
Use that five-category pattern only when the repository already documents it locally.
If that signal is absent, keep the smaller fallback taxonomy.

6. Classify by purpose.
Follow repository-local purpose categories when they exist.
Otherwise use [references/default-doc-taxonomy.md](references/default-doc-taxonomy.md) for default category meanings.
Split mixed-purpose documents so binding implementation rules stay with implementation-facing docs and background explanation stays with knowledge or reference material.

7. Synchronize and verify.
If you add a docs category, move documents between categories, or materially change category semantics, update the repository-local taxonomy or index docs in the same task.
Update `AGENTS.md` only for short agent-operational rules.
Check obvious links, directory indexes, `docs/README.md`, archive pointers, and nearby inbound references affected by the change.
Report deferred fixes explicitly.

## Output Expectations

When using this skill, state:

- the classification decision
- which local or fallback source of truth controlled the decision
- why the current path is correct or incorrect
- the exact action summary: move, split, archive, update in place, or no-op
- which files were updated or still need updates for consistency
- which link, index, or navigation checks were completed or deferred
- any conflicts, stale local rules, or partial local rules that affect confidence
- any unresolved overlap, risks, or follow-up actions

## Boundaries

- Prefer the smallest change that restores structural clarity.
- Prefer moving or splitting docs over rewriting everything.
- Do not invent new top-level docs categories unless the existing taxonomy is clearly insufficient.
- Do not replace the generic fallback taxonomy with the execution-heavy pattern unless the repository explicitly adopts it locally.
- Do not treat a general project `README.md` as taxonomy authority unless it explicitly defines placement rules for the target docs scope.
- Do not make `AGENTS.md` the only source of truth for human-facing taxonomy.
- When a repository already documents its taxonomy locally, follow the repository files over this skill's defaults.
