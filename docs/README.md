# Skill Docs

This `docs/` tree is the repository-local documentation taxonomy for `project-doc-governance`.

It is intentionally small. This skill repository uses `docs/` mainly to record repository-local problems, review findings, and remediation work. It does not duplicate the reusable fallback reference material in `references/`, and it does not replace the execution contract in `SKILL.md`.

## Authority

- This file is the human-facing source of truth for docs placement inside this skill repository.
- `SKILL.md` remains the authority for how the skill should execute when Codex uses it on another repository.
- `references/default-doc-taxonomy.md` remains a reusable fallback reference for target repositories. It is not this repository's maintenance log.
- Root `README.md` stays as overview and navigation, not the controlling placement spec for this repository's docs.

## Categories

### `docs/problem/`

Use for active repository-local problem records, such as:

- review findings
- remediation plans and backlogs
- open authority or taxonomy ambiguities
- follow-up notes from forward tests

### `docs/problem/archive/`

Use for closed or superseded problem records that are kept only for traceability.

Create this directory when the first active problem record is retired.

## Current Docs

- `docs/problem/skill-review-and-remediation.md`: active review, remediation history, and next review gate for this skill repository.

## Placement Rules

- If a document mainly tracks repository-local issues or remediation work for this skill, place it under `docs/problem/`.
- If that record is no longer active but still worth keeping, move it to `docs/problem/archive/`.
- Keep generic, reusable guidance under `references/`.
- Keep skill execution rules in `SKILL.md`.
- Update this file in the same task if this repository later adopts more docs categories.
