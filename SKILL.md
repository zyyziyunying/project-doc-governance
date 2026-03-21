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

- docs that explicitly define documentation structure or placement, such as `docs/taxonomy.md`, `docs/doc-taxonomy.md`, `docs/structure.md`, category index files, or neighboring directory README files
- the root or nearest repository `AGENTS.md`
- `docs/README.md`, but only when it clearly defines the human-facing docs structure or placement rules for the target scope
- Do not read a general repository `README.md` by default for documentation placement decisions.

3. Resolve authority before classifying.

- Use the nearest dedicated taxonomy or placement doc that covers the target path as the primary source for that scope.
- Otherwise use repository-level taxonomy or structure docs as the human-facing source of truth for category semantics and placement. Use `docs/README.md` only when it explicitly carries that role for the target scope.
- Use `AGENTS.md` for agent-operational behavior, local workflow guardrails, and pointers to the source of truth. Do not let `AGENTS.md` silently redefine human-facing taxonomy when repository docs say otherwise.
- If two local docs conflict, prefer the more specific scope. If scope is equal, prefer a dedicated taxonomy or structure doc over a general README or index, and prefer human-facing taxonomy docs over `AGENTS.md` for placement semantics.
- If the conflict still changes the outcome materially, stop and report it instead of guessing.

4. Detect missing, partial, or stale local rules.

- Treat a local doc as missing when it does not cover the current document class or destination decision. A `docs/README.md` that only links around the docs tree without defining category meaning or placement does not count as coverage.
- Treat a local doc as stale when it references categories or paths that no longer exist, contradicts the active directory structure, or disagrees with a more specific maintained taxonomy doc.
- If local docs are partial but still point to one stable pattern, extend that pattern and report what remains underspecified.
- If local docs are stale but the correct destination is still obvious from a stronger active source, follow the stronger source and include the required sync fixes in the result.
- If stale or conflicting docs would materially change the classification outcome, surface the ambiguity before doing a broad reorganization.

5. Apply the fallback taxonomy only when local rules are missing, out of scope, or unusable for the current decision.
Read [references/default-doc-taxonomy.md](references/default-doc-taxonomy.md) before creating new categories or moving docs based on default rules.
If the repository is execution-heavy and the generic fallback would stay too coarse, you may establish a small repository-local taxonomy around `problem`, `plan`, `status`, `analysis`, and `discussion`, but only by documenting it locally in `docs/README.md` or a dedicated taxonomy doc in the same task.

6. Classify the document by purpose, not by topic.

- Follow repository-local purpose categories when they are defined.
- Otherwise use [references/default-doc-taxonomy.md](references/default-doc-taxonomy.md) for the default meaning of implementation-facing docs, knowledge docs, archives, guide files, and common gray-area document classes.
- For execution-heavy repositories, a good local split often separates problem definition, accepted plans, status tracking, analysis material, and unresolved discussion instead of collapsing them into one broad bucket.
- Keep `AGENTS.md` short and agent-facing. Do not duplicate full human documentation into it.

7. Resolve mixed-purpose documents.

- If one file contains both background explanation and binding implementation rules, split it or move the binding portions closer to implementation-facing docs.
- If a knowledge document starts carrying repository-specific mandates, move those mandates into the authoritative implementation or taxonomy docs.
- If a blocker or plan is no longer active but still useful as history, archive it instead of deleting it.

8. Synchronize structure changes.

- If you add a new docs category, move documents between categories, or materially change category semantics, update the repository-local taxonomy or index docs in the same task.
- If you adopt the execution-heavy local pattern, prefer `status` as the stable category name. If the repository already uses `progress`, keep the name but define it with `status` semantics instead of letting it become a generic catch-all.
- If the repository uses `docs/README.md` as its human-facing docs index or placement guide, update it when the structure changes.
- Update `AGENTS.md` only for short agent-operational rules that should affect future Codex behavior.
- Do not make `AGENTS.md` the only source of truth for human-facing taxonomy.

9. Verify structural integrity after moves or splits.

- Check moved-file relative links and obvious inbound references from nearby docs.
- Check category indexes, directory README files, `docs/README.md`, and archive pointers that may still point at the old path.
- Report any intentionally deferred link, index, or reference fixes.

10. Review with a strict checklist.

- Is the audience explicit: developer knowledge, implementer, reviewer, or agent?
- Is the authority level explicit: informative, guiding, or binding?
- Does the file path match the document's real purpose?
- Is there one clear source of truth for each binding rule?
- Would another engineer know where to put the next related document?

## Output Expectations

When using this skill, state:

- the classification decision
- which local or fallback source of truth controlled the decision
- why the current path is correct or incorrect
- the exact action summary: move, split, archive, update in place, or no-op
- which files were updated or still need updates for consistency
- which link, index, or navigation checks were completed or deferred
- any conflicts or stale local rules that affect confidence
- any unresolved overlap, risks, or follow-up actions

## Boundaries

- Prefer the smallest change that restores structural clarity.
- Prefer moving or splitting docs over rewriting everything.
- Do not invent new top-level docs categories unless the existing taxonomy is clearly insufficient.
- Do not replace the generic fallback taxonomy with the execution-heavy pattern unless the repository context clearly benefits from that more explicit local split.
- Do not treat a general project `README.md` as taxonomy authority unless it explicitly defines placement rules for the target docs scope.
- When a repository already documents its taxonomy locally, follow the repository files over this skill's defaults.
