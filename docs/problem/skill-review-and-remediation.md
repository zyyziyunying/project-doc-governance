# Project Doc Governance Skill Review and Remediation

Reviewed on: 2026-03-21
Scope: `C:\Users\zyy\.codex\skills\project-doc-governance`
Reviewer stance: strict, portability-first, maintenance-focused

Document role: active repository-local problem tracker and remediation queue for this skill repository.
Placement authority: `docs/README.md`
Historical archive: [archive/2026-03-21-skill-review-history.md](archive/2026-03-21-skill-review-history.md)

## Current Status

- Phases 1 through 7 were completed on 2026-03-20.
- The archived review history was expanded on 2026-03-22 so the detailed historical rationale remains preserved outside the active tracker.
- The working reassessment remains `8/10` as of 2026-03-21.
- The skill is structurally usable and no longer repository-hardcoded, but it still has open convergence and validation work before a higher score is justified.

## Active Follow-up Items

### 1. Tighten activation of the execution-heavy local pattern

Status: open

Why this remains open:

- the skill says the `problem / plan / status / analysis / discussion` pattern is repository-local
- the workflow still allows an agent to establish that pattern in the same task whenever the generic fallback feels too coarse
- this can still produce divergent outcomes across agents or across repositories with only partial local docs signals

Required changes:

- narrow when same-task establishment of that pattern is allowed
- or require an explicit repository-local adoption signal before it becomes controlling taxonomy
- make it clearer whether this path is a normal recommendation or an exception path

Validation needed:

- one retained migration where the repository already has enough local docs structure that the choice between the generic fallback and the five-category pattern could materially change placement

### 2. Align entry metadata with the narrowed authority model

Status: open

Why this remains open:

- the skill frontmatter description still groups `docs/README.md` with taxonomy docs and `AGENTS.md` in a way that can be read as default authority
- the body now uses a narrower rule: `docs/README.md` only controls placement when it explicitly defines structure or category semantics

Required changes:

- rewrite the frontmatter description so it reflects the narrowed `docs/README.md` authority
- keep any short skill metadata or UI-facing summary consistent with that boundary

Validation needed:

- confirm the skill still triggers correctly in downstream UI and agent selection after the metadata wording is tightened

### 3. Unify stale vs partial local-rule handling

Status: open

Why this remains open:

- `SKILL.md` and `references/default-doc-taxonomy.md` do not describe stale, incomplete, and partial coverage using exactly the same decision language
- one agent may extend a still-stable local pattern while another may treat the same situation as stale and partially fall back

Required changes:

- make the stale-versus-partial criteria match across `SKILL.md` and `references/default-doc-taxonomy.md`
- state more explicitly when the agent should extend a stable local pattern versus fall back only for uncovered parts
- add one or two concrete examples for this boundary

Validation needed:

- test against a repository with a dedicated local taxonomy and a partially stale docs index or category README

## Field Validation Gaps

- A retained trial is still missing for a repository that already has a dedicated taxonomy doc or category README with real placement semantics.
- A retained trial is still missing for a repository where `docs/README.md` is mostly navigational and should not become authority.
- A retained trial is still missing for the execution-heavy local pattern after owner review.

## Next Review Gate

- Re-run the review after at least one retained migration against a repository with stronger local docs rules and at least one mixed-purpose document split.
- Do not raise the score above `8/10` until the active follow-up items above have been addressed or explicitly retired.

## Archived Material

- Historical review evidence, the original baseline findings, the completed phase backlog, and detailed forward-test notes live in [archive/2026-03-21-skill-review-history.md](archive/2026-03-21-skill-review-history.md).
