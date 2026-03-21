# Project Doc Governance Skill Review and Remediation

Reviewed on: 2026-03-21
Scope: `C:\Users\zyy\.codex\skills\project-doc-governance`
Reviewer stance: strict, portability-first, maintenance-focused

Document role: active repository-local problem and remediation record for this skill repository.
Placement authority: `docs/README.md`

## Progress Log

- 2026-03-20: Recorded the baseline review and remediation backlog.
- 2026-03-20: Completed Phase 1 in the skill files by removing direct `epub_reader` references from the workflow, adding repository-local taxonomy discovery, and replacing the repository-specific reference with `references/default-doc-taxonomy.md`.
- 2026-03-20: Completed Phase 2 in the skill files by adding explicit precedence rules, conflict handling, and stale-doc handling for repository-local taxonomy decisions.
- 2026-03-20: Completed Phase 3 by adding default mappings for common gray-area document classes.
- 2026-03-20: Completed Phase 4 by shrinking `SKILL.md` toward workflow and decision logic, while moving more default taxonomy detail into the reference.
- 2026-03-20: Completed Phase 5 by adding migration-integrity checks for moved or split docs.
- 2026-03-20: Completed Phase 6 by tightening the output contract around action summaries, affected files, and deferred checks.
- 2026-03-20: Completed Phase 7 by adding `scripts/basic_validate.py` as a no-dependency fallback validator and running it successfully.
- 2026-03-20: Re-scored the skill after Phases 1 through 7.
- 2026-03-21: Forward-tested the skill on `D:\dev\flutter_code\tiny_player` and validated a workable remediation pattern: add a local `docs/README.md`, archive misplaced historical discussion and status docs, preserve redirect stubs for old paths, and align the repository `AGENTS.md` with the local docs taxonomy.
- 2026-03-21: The user later rolled back the `tiny_player` repository changes after review. Treat that run as evaluation evidence, not as a retained repository migration.
- 2026-03-21: Forward-tested the skill on `D:\dev\flutter_code\video_list_android_demo` and landed a second cross-repository migration: created `docs/README.md`, moved closed root-level status/review docs into `docs/problem/archive/`, preserved the old root paths as redirect stubs, linked the root `README.md` to the docs index, and synchronized `AGENTS.md` to point at the human-facing source of truth.
- 2026-03-21: Added an explicit optional local taxonomy pattern for execution-heavy repositories: `problem`, `plan`, `status`, `analysis`, and `discussion`, with per-category archive support and guidance for keeping it repository-local rather than elevating it to the global fallback.
- 2026-03-21: Tightened the authority model so the skill no longer treats a general repository `README.md` as default taxonomy input, and only considers `docs/README.md` when it explicitly defines docs placement or category semantics.

## Baseline Assessment

This skill is usable, but it is not yet a mature general-purpose documentation governance skill.

Baseline score:

- 4/10 as a general reusable skill
- 6.5/10 if interpreted as a repository-specific helper

The lower score is mainly caused by a mismatch between the metadata, which presents the skill as generic, and the body/reference design, which still assumes `epub_reader`-specific taxonomy.

## Interim Reassessment After Remediation

Updated score on 2026-03-21:

- 8/10 as a general reusable skill

Why the score improved:

- the skill is now genuinely generic rather than repository-hardcoded
- authority and precedence rules are explicit
- the default taxonomy now covers common gray-area document classes
- migration-integrity checks and a clearer output contract reduce operational drift
- there is now a lightweight validation path that works without `PyYAML`
- a second unrelated repository trial completed a real docs migration instead of only serving as a dry evaluation pattern

Remaining gaps that still keep it below a higher score:

- the accepted-retention signal is still limited because long-term keep-or-revert is controlled by repository owners after handoff
- the default taxonomy is still opinionated and may need field use to refine edge cases
- the new execution-heavy local taxonomy pattern is documented, but not yet validated by a retained cross-repository migration
- the narrowed `docs/README.md` role is now clearer on paper, but still needs more field use against repositories that keep a docs index without full placement semantics
- there is still some overlap between the workflow summary and the reference, even though it is smaller than before
- the authority model has now been tested in "no local taxonomy, AGENTS non-authoritative" repositories, but not yet in a repository with an existing dedicated taxonomy doc that materially constrains placement

## Second Forward Test: `video_list_android_demo`

Tested repository:

- `D:\dev\flutter_code\video_list_android_demo`

Local authority model result:

- There was no local `docs/README.md` or dedicated taxonomy file before the trial.
- The repository `AGENTS.md` only described engineering workflow and project structure; it did not define human-facing documentation placement semantics.
- Under the skill's precedence rules, the default taxonomy therefore controlled the initial classification decision.
- During the migration, `docs/README.md` became the new human-facing source of truth for repository docs placement, and `AGENTS.md` was reduced to a pointer back to that file rather than a competing taxonomy source.

Classification outcome:

- `README.md` remained at the repository root because it is the entry document for users and developers.
- `CRITIQUE_ISSUES.md` was classified as a closed implementation-facing review follow-up, so the root path was incorrect and the document was moved to `docs/problem/archive/`.
- `STABILITY_CLOSEOUT_PLAN.md` was classified as a completed implementation-facing closeout record, so the root path was incorrect and the document was moved to `docs/problem/archive/`.
- Redirect stubs were left at the old root paths because historical links or bookmarks may still exist.

Gray-area mapping result:

- The trial supports the rule that review findings, closeout plans, and status trackers are not `knowledge` docs merely because they contain narrative. Their primary function is still implementation-facing governance.
- Once those documents stop acting as active execution contracts, `docs/problem/archive/` is an appropriate default destination.
- A package-local gray-area file, `packages/video_visibility/REVIEW_NOTES.md`, was intentionally left in place because it is package-scoped and still contains partly open strategy notes. Moving it would have expanded the migration beyond the clearly misfiled root-level history docs without stronger local placement rules.

Migration integrity check result:

- `docs/README.md` was added in the same task so the new structure has a human-facing index.
- `AGENTS.md` was synchronized in the same task and now points to `docs/README.md` instead of silently carrying taxonomy semantics alone.
- The root `README.md` now links to `docs/README.md`, which improves discoverability for human readers.
- Old root paths were preserved as redirect stubs, which kept historical navigation stable after the move.
- Repository-wide reference search found no other inbound references to the moved files that required additional repair.
- Unrelated untracked files in the repository (`1.txt`, `2.txt`) were left untouched, so the migration stayed scoped to documentation governance.

Assessment from this trial:

- The authority model held for a repository that lacked a preexisting human-facing taxonomy: default rules controlled the initial move, then the repository-local `docs/README.md` became authoritative.
- The gray-area mapping for closed review/status/closeout docs held up in a real repository and produced a small, understandable archive shape.
- The migration-integrity checklist was strong enough to drive the necessary sync work in one pass: docs index, agent guidance, root README discoverability, old-path redirects, and inbound-reference verification.
- This is stronger evidence than the earlier `tiny_player` evaluation run because the migration was actually applied in a second unrelated repository rather than only prototyped and then rolled back.

## Baseline Findings

### 1. High: Generic positioning conflicts with repository-specific behavior

Status after 2026-03-20 update: addressed in Phase 1; kept here as the baseline rationale for the rewrite.

The skill description presents broad applicability, but the workflow hardcodes a repository-specific branch:

- `SKILL.md` told Codex to read `references/epub-reader-taxonomy.md` for the current `epub_reader` repository.
- The reference file was entirely framed around `epub_reader`.

Impact:

- unrelated repositories can still trigger this skill
- once triggered, the skill may apply the wrong taxonomy or overfit to one repository's structure
- this weakens trust in both triggering and execution quality

Required fix:

- decide whether this skill is truly generic or intentionally repository-specific
- if generic, move repository-local taxonomy rules out of the shared skill and make the workflow discover repository-local docs first
- if repository-specific extensions are still needed, define a generic selection mechanism instead of naming one repository in the core workflow

### 2. High: No explicit precedence or conflict-resolution model

The skill tells Codex to read `AGENTS.md` and `docs/README.md`, but it does not define what to do when they disagree.

Impact:

- different agents can reach different placement decisions
- local documentation may drift with no stable tie-break rule
- maintenance becomes argument-driven instead of rule-driven

Required fix:

- define precedence explicitly
- define when repository-local taxonomy overrides the skill defaults
- define how to handle partial conflict, stale docs, and ambiguous ownership

### 3. Medium-High: Taxonomy is too thin for common real-world doc types

The current model mostly covers:

- `docs/problem/`
- `docs/problem/archive/`
- `docs/knowledge/`
- standalone guide files

Missing or underspecified cases include:

- ADRs
- RFCs
- runbooks
- incident notes or postmortems
- release notes
- meeting notes
- temporary investigation docs

Impact:

- repeated edge-case debates
- inconsistent placement
- pressure to create ad hoc categories without strong rules

Required fix:

- either broaden the taxonomy model or define mapping rules for these document classes
- keep the model small, but make the decision boundaries explicit

### 4. Medium: SKILL body and reference file duplicate core rules

The skill repeats category definitions and synchronization guidance in both `SKILL.md` and `references/epub-reader-taxonomy.md`.

Impact:

- future edits can drift
- maintainers must update the same rule twice
- the skill body is carrying detail that should live in references

Required fix:

- keep `SKILL.md` focused on workflow and decision procedure
- move variant- or repository-level taxonomy detail into references or local project docs
- leave only the minimal generic rules in the body

### 5. Medium: Structural migration guidance is incomplete

The skill requires updates to `docs/README.md` and `AGENTS.md`, but it does not require checking:

- moved-file links
- relative path references
- document indexes
- inbound references from neighboring docs
- stale archive references

Impact:

- a classification cleanup can still leave the documentation graph broken
- post-move cleanup remains manual and easy to miss

Required fix:

- add a post-move integrity checklist
- require checking links, references, and any local navigation files after document moves or splits

### 6. Medium-Low: Output expectations are explanatory, not operational enough

The skill asks for:

- the classification decision
- path correctness
- companion file updates
- unresolved overlap

This is useful, but not sufficient for consistent execution output.

Impact:

- two agents may produce similarly worded but operationally different results
- the output may not clearly specify exact moves, splits, or follow-up actions

Required fix:

- require explicit move/split actions when applicable
- require listing affected files and unresolved risks
- require noting whether no-op was chosen and why

### 7. Low: Validation path is weak

The local validation script failed because `quick_validate.py` depends on `PyYAML` and the environment did not provide `yaml`.

Impact:

- validation cannot be assumed available during maintenance
- regressions may slip through if maintainers rely on validation that is not runnable

Required fix:

- document validator prerequisites
- or remove the dependency from the maintenance path
- or provide a lightweight fallback validation command

## Strengths Worth Keeping

- The skill stays compact and readable.
- The trigger description is reasonably clear.
- "Classify by purpose, not by topic" is the correct core principle.
- The boundary of "prefer the smallest change that restores clarity" is strong.
- The bias against inventing categories too early is healthy.

## Remediation Backlog

### Phase 1: Correct the skill boundary

Status: completed on 2026-03-20.

1. Rewrite the skill as genuinely generic.
2. Remove direct `epub_reader` references from the core workflow.
3. Define how the skill discovers repository-local taxonomy documents.
4. Make repository-local docs authoritative when present.

Exit criteria:

- no repository name appears in the generic workflow unless used as an example in a reference
- the skill can be applied to an arbitrary project without producing obviously wrong defaults

### Phase 2: Define decision authority clearly

Status: completed on 2026-03-20.

1. Add a precedence rule for `AGENTS.md`, `docs/README.md`, and local taxonomy files.
2. Define tie-break behavior when repository docs conflict.
3. Define what to do when local docs are absent or stale.

Exit criteria:

- two agents reading the same repository should converge on the same classification outcome

### Phase 3: Strengthen the taxonomy model

Status: completed on 2026-03-20.

1. Add mapping guidance for common doc classes that currently fall into gray areas.
2. Clarify when a standalone guide should stay standalone versus become a category.
3. Clarify archival policy for inactive plans, blockers, and investigations.

Exit criteria:

- common engineering document types have a predictable placement rule

### Phase 4: Remove duplication and improve maintainability

Status: completed on 2026-03-20.

1. Shrink `SKILL.md` to workflow, decision logic, and boundaries.
2. Move detailed taxonomy examples into references.
3. Keep one clear source of truth for each rule.

Exit criteria:

- category definitions exist in one authoritative location per variant

### Phase 5: Add migration integrity checks

Status: completed on 2026-03-20.

1. Add link and cross-reference verification after moves or splits.
2. Add checks for index files and local navigation docs.
3. Require reporting of stale references that were intentionally deferred.

Exit criteria:

- structural cleanup does not silently break the documentation graph

### Phase 6: Tighten output contracts

Status: completed on 2026-03-20.

1. Require explicit action summaries.
2. Require affected-file lists.
3. Require unresolved-risk notes.
4. Require a no-op explanation when nothing should move.

Exit criteria:

- outputs are directly actionable, not just descriptive

### Phase 7: Repair the validation story

Status: completed on 2026-03-20.

1. Make validator prerequisites explicit.
2. Decide whether this skill should include a lightweight self-check path.
3. Re-run validation after the structural rewrite.

Exit criteria:

- a maintainer can validate the skill without guessing hidden dependencies

## Recommended Target State

This skill should become a small, generic governance procedure with three layers:

1. Generic workflow in `SKILL.md`
2. Optional reusable reference patterns for common taxonomy designs
3. Repository-local source-of-truth docs that define the actual category semantics

That structure would preserve portability while still allowing opinionated local governance.

## Next Review Gate

Use the skill on a repository that already has a dedicated local taxonomy or category README, especially one where `AGENTS.md` and human-facing docs could plausibly conflict, then review whether the precedence rules still converge without manual interpretation.

Target for the next review:

- 8.5/10 as a general reusable skill after a successful trial against a repository with preexisting local docs taxonomy and at least one mixed-purpose document split

Do not raise the score further without evidence from real repository use against a repository with stronger local docs rules, and preferably at least one migration that remains retained after owner review.
