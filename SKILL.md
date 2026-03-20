---
name: project-doc-governance
description: Organize, classify, review, move, split, and archive project documentation with a stable purpose-based taxonomy. Use when Codex needs to decide where a doc belongs, create or relocate docs files or categories, separate background knowledge from binding implementation constraints, keep docs structure aligned with repository-local taxonomy docs plus AGENTS.md and docs/README.md, or clean up stale project docs.
---

# Project Doc Governance

Use this skill to keep repository documentation structurally consistent without imposing one repository's taxonomy on another.

## Workflow

1. Build minimal context.
Read only the target document(s), nearby docs, and repository structure docs needed to classify or restructure the task.

2. Discover repository-local taxonomy first.
Read these files when they exist and are relevant:

- `docs/README.md`
- the root or nearest repository `AGENTS.md`
- docs that explicitly define documentation structure or placement, such as `docs/taxonomy.md`, `docs/doc-taxonomy.md`, `docs/structure.md`, category index files, or neighboring directory README files

3. Treat repository-local taxonomy as authoritative.

- Follow repository-local placement rules when they are explicit.
- Use this skill's fallback taxonomy only when the repository does not define the rule you need.
- Extend from the closest local pattern before importing a new structure wholesale.
- If repository-local docs conflict or appear stale, surface the conflict instead of silently imposing a new taxonomy.

4. Apply the fallback taxonomy only when local rules are missing or incomplete.
Read [references/default-doc-taxonomy.md](references/default-doc-taxonomy.md) before creating new categories or moving docs based on default rules.

5. Classify the document by purpose, not by topic.

- Keep binding implementation constraints, blockers, migration rules, phase plans, acceptance rules, and data-contract decisions in implementation-facing docs.
- Keep background knowledge, concept explanations, learning notes, and high-level technical understanding in knowledge-oriented docs.
- Keep subsystem-specific standalone guides as dedicated guide files when they are operational references rather than project-wide constraints.
- Keep `AGENTS.md` short and agent-facing. Do not duplicate full human documentation into it.

6. Resolve mixed-purpose documents.

- If one file contains both background explanation and binding implementation rules, split it or move the binding portions closer to implementation-facing docs.
- If a knowledge document starts carrying repository-specific mandates, move those mandates into the authoritative implementation or taxonomy docs.
- If a blocker or plan is no longer active but still useful as history, archive it instead of deleting it.

7. Synchronize structure changes.

- If you add a new docs category, move documents between categories, or materially change category semantics, update the repository-local taxonomy or index docs in the same task.
- Update `docs/README.md` when the human-facing structure changes.
- Update `AGENTS.md` only for short agent-operational rules that should affect future Codex behavior.
- Do not make `AGENTS.md` the only source of truth for human-facing taxonomy.

8. Review with a strict checklist.

- Is the audience explicit: developer knowledge, implementer, reviewer, or agent?
- Is the authority level explicit: informative, guiding, or binding?
- Does the file path match the document's real purpose?
- Is there one clear source of truth for each binding rule?
- Would another engineer know where to put the next related document?

## Output Expectations

When using this skill, state:

- the classification decision
- why the current path is correct or incorrect
- which companion files must be updated for consistency
- any unresolved overlap between knowledge docs and implementation docs

## Boundaries

- Prefer the smallest change that restores structural clarity.
- Prefer moving or splitting docs over rewriting everything.
- Do not invent new top-level docs categories unless the existing taxonomy is clearly insufficient.
- When a repository already documents its taxonomy locally, follow the repository files over this skill's defaults.
