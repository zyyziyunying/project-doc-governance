# Skill Docs

This `docs/` tree is the repository-local documentation taxonomy for `project-doc-governance`.

It is intentionally small. This skill repository uses `docs/` mainly to record repository-local problems, review findings, remediation work, and a small number of repository-local guide files and rule-discussion drafts. It does not duplicate the reusable fallback reference material in `references/`, and it does not replace the live execution contract in `SKILL.md`.

## Authority

- This file is the human-facing source of truth for docs placement inside this skill repository.
- `SKILL.md` remains the authority for how the skill should execute when Codex uses it on another repository.
- `references/default-doc-taxonomy.md` remains a reusable fallback reference for target repositories. It is not this repository's maintenance log.
- `docs/skill-meta-principles.md` is a repository-local guide for how this skill should evolve; it does not override the live runtime contract.
- `docs/skill-shadow-spec.md` may discuss candidate rule changes, but it does not become authoritative until accepted changes are merged into `SKILL.md` or `references/default-doc-taxonomy.md`.
- Root `README.md` stays as overview and navigation, not the controlling placement spec for this repository's docs.

## Categories

### `docs/problem/`

Use for active repository-local problem records, such as:

- review findings
- remediation plans and backlogs
- open authority or taxonomy ambiguities
- follow-up notes from forward tests

### `docs/problem/archive/`

Use for closed or superseded problem records, or for archived history extracted from an active tracker when the historical detail is still useful for traceability.

## Current Docs

- `docs/skill-meta-principles.md`: repository-local meta-principles for evolving this skill without turning every maintenance note into runtime contract text.
- `docs/skill-shadow-spec.md`: repository-local shadow spec / discussion draft that records only candidate deltas against the live contract in `SKILL.md` and `references/default-doc-taxonomy.md`.
- `docs/problem/skill-review-and-remediation.md`: active follow-up tracker, current status, and next review gate for this skill repository.
- `docs/problem/archive/2026-03-21-skill-review-history.md`: archived baseline review, completed remediation phases, and forward-test evidence.

## Placement Rules

- If a document mainly tracks repository-local issues or remediation work for this skill, place it under `docs/problem/`.
- If that record is no longer active but still worth keeping, move it to `docs/problem/archive/`.
- Keep repository-local guide files and shadow-spec discussion drafts that are not active problem trackers as standalone files under `docs/`.
- Keep generic, reusable guidance under `references/`.
- Keep skill execution rules in `SKILL.md`.
- Update this file in the same task if this repository later adopts more docs categories.
