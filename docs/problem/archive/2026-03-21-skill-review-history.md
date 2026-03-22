# Project Doc Governance Skill Review History

Archived on: 2026-03-21
Source document: `docs/problem/skill-review-and-remediation.md`
Archived reason: the original problem record mixed active follow-up work with completed remediation history and detailed review evidence. The active tracker was reduced, and the historical material was preserved here in summarized form for traceability.

## Archived Scope

This archive preserves the historical material that no longer needs to stay in the active tracker:

- the original baseline assessment and score change from `4/10` and `6.5/10` up to `8/10`
- the phase-by-phase remediation history for Phases 1 through 7
- the forward-test notes for `tiny_player` and `video_list_android_demo`
- the original baseline findings that motivated the completed rewrite
- the completed remediation backlog and prior target-state notes

## Progress Summary

- 2026-03-20: Recorded the baseline review and remediation backlog.
- 2026-03-20: Completed Phases 1 through 7 in the skill files, covering generic-boundary cleanup, authority rules, gray-area mappings, duplication reduction, migration-integrity checks, output-contract tightening, and a lightweight validator.
- 2026-03-21: Forward-tested the skill on `D:\dev\flutter_code\tiny_player`; the migration pattern was workable, but the repository changes were later rolled back after review, so this remained evaluation evidence only.
- 2026-03-21: Forward-tested the skill on `D:\dev\flutter_code\video_list_android_demo`; the migration was retained and provided stronger evidence for the authority model, archive handling, and sync checklist.
- 2026-03-21: Added the optional execution-heavy local taxonomy pattern and tightened the authority model so a general repository `README.md` is no longer default taxonomy input.

## Historical Assessment Snapshot

- Baseline view: usable, but not yet a mature general-purpose documentation governance skill.
- Baseline score: `4/10` as a general reusable skill, `6.5/10` as a repository-specific helper.
- Interim reassessment on 2026-03-21: `8/10` as a general reusable skill.

Why the score improved:

- the skill became genuinely generic rather than repository-hardcoded
- authority and precedence rules became explicit
- the default taxonomy gained stronger gray-area mappings
- migration-integrity checks and the output contract reduced operational drift
- a lightweight validation path became available without `PyYAML`
- a retained migration was completed in a second unrelated repository

## Historical Forward-Test Notes

### `tiny_player`

- The run validated a workable remediation pattern: add a local `docs/README.md`, archive misplaced historical discussion and status docs, preserve redirect stubs for old paths, and align `AGENTS.md` with the local docs taxonomy.
- The user later rolled back the repository changes after review.
- Treat this run as evaluation evidence, not as a retained migration.

### `video_list_android_demo`

- There was no local `docs/README.md` or dedicated taxonomy file before the trial.
- `AGENTS.md` was non-authoritative for human-facing placement semantics.
- The default taxonomy controlled the initial classification decision.
- During the migration, `docs/README.md` became the human-facing source of truth and `AGENTS.md` was reduced to a pointer back to that file.
- Closed implementation-facing review and closeout docs were moved into `docs/problem/archive/`.
- Old root paths were preserved as redirect stubs.
- Repository-wide reference search found no other inbound references that required repair.

## Historical Baseline Findings That Drove The Rewrite

These findings were recorded before the Phase 1 through 7 remediation and are now historical rather than active:

1. Generic positioning conflicted with repository-specific behavior because the workflow still hardcoded `epub_reader`.
2. The skill lacked an explicit precedence and conflict-resolution model for `AGENTS.md`, `docs/README.md`, and local taxonomy docs.
3. The taxonomy was too thin for common gray-area engineering documents.
4. `SKILL.md` and the reference file duplicated too much core taxonomy guidance.
5. Structural migration guidance did not yet require link and reference integrity checks.
6. Output expectations were still descriptive rather than operational.
7. The original validation path depended on unavailable `PyYAML`.

## Historical Backlog State

- Phases 1 through 7 are complete.
- The older recommended target state was a three-layer model: generic workflow in `SKILL.md`, reusable reference patterns, and repository-local source-of-truth docs.
- The older next review gate asked for a successful trial against a repository with preexisting local docs taxonomy and at least one mixed-purpose document split.

## Relationship To The Active Tracker

- Use [../skill-review-and-remediation.md](../skill-review-and-remediation.md) for current open issues, validation gaps, and the next review gate.
- Keep this archive for historical rationale and evidence that no longer needs to stay in the active tracker.
