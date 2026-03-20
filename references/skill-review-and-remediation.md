# Project Doc Governance Skill Review and Remediation

Reviewed on: 2026-03-20
Scope: `C:\Users\zyy\.codex\skills\project-doc-governance`
Reviewer stance: strict, portability-first, maintenance-focused

## Progress Log

- 2026-03-20: Recorded the baseline review and remediation backlog.
- 2026-03-20: Completed Phase 1 in the skill files by removing direct `epub_reader` references from the workflow, adding repository-local taxonomy discovery, and replacing the repository-specific reference with `references/default-doc-taxonomy.md`.
- 2026-03-20: Deferred re-scoring until after Phase 2, as planned.

## Baseline Assessment

This skill is usable, but it is not yet a mature general-purpose documentation governance skill.

Current score:

- 4/10 as a general reusable skill
- 6.5/10 if interpreted as a repository-specific helper

The lower score is mainly caused by a mismatch between the metadata, which presents the skill as generic, and the body/reference design, which still assumes `epub_reader`-specific taxonomy.

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

1. Add a precedence rule for `AGENTS.md`, `docs/README.md`, and local taxonomy files.
2. Define tie-break behavior when repository docs conflict.
3. Define what to do when local docs are absent or stale.

Exit criteria:

- two agents reading the same repository should converge on the same classification outcome

### Phase 3: Strengthen the taxonomy model

1. Add mapping guidance for common doc classes that currently fall into gray areas.
2. Clarify when a standalone guide should stay standalone versus become a category.
3. Clarify archival policy for inactive plans, blockers, and investigations.

Exit criteria:

- common engineering document types have a predictable placement rule

### Phase 4: Remove duplication and improve maintainability

1. Shrink `SKILL.md` to workflow, decision logic, and boundaries.
2. Move detailed taxonomy examples into references.
3. Keep one clear source of truth for each rule.

Exit criteria:

- category definitions exist in one authoritative location per variant

### Phase 5: Add migration integrity checks

1. Add link and cross-reference verification after moves or splits.
2. Add checks for index files and local navigation docs.
3. Require reporting of stale references that were intentionally deferred.

Exit criteria:

- structural cleanup does not silently break the documentation graph

### Phase 6: Tighten output contracts

1. Require explicit action summaries.
2. Require affected-file lists.
3. Require unresolved-risk notes.
4. Require a no-op explanation when nothing should move.

Exit criteria:

- outputs are directly actionable, not just descriptive

### Phase 7: Repair the validation story

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

After Phase 1 and Phase 2 are complete, re-score the skill before further expansion.

Target for the next review:

- 7/10 as a general reusable skill

Do not optimize wording before fixing boundary, authority, and portability.
