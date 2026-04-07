# Default Project Docs Taxonomy

Use this reference only when a repository does not already define where docs should live.

## Local-First Rules

Check local docs first.
If local docs already answer the placement question, follow them.
If not, use the fallback structure below.

## Default Structure

### `docs/design/`

Use for technical design.

Archive older or superseded design docs under `docs/design/archive/`.

### `docs/check/`

Use for validation, acceptance, and release checks.

Archive completed or expired check materials under `docs/check/archive/`.

### `docs/plan/`

Use for execution plans.

Archive old or completed plans under `docs/plan/archive/`.

### `docs/status/`

Use for progress and results.

Archive outdated status docs under `docs/status/archive/`.

### `docs/problem/`

Use for blockers, defects, risks, and constraints.

Archive resolved problem records under `docs/problem/archive/`.

### `docs/discussion/`

Use for open questions and discussion.

Archive closed discussions under `docs/discussion/archive/`.

### `docs/product/`

Use for product scope and requirements.

Archive superseded product docs under `docs/product/archive/`.

## Quick Placement Rules

- If the doc says what to build, use `docs/product/`
- If the doc says how to design it, use `docs/design/`
- If the doc says how to validate or accept it, use `docs/check/`
- If the doc says how to execute it, use `docs/plan/`
- If the doc says where things stand, use `docs/status/`
- If the doc says what is blocked or risky, use `docs/problem/`
- If the doc is still under discussion, use `docs/discussion/`
- If a doc is no longer active but still worth keeping, move it into that category's `archive/`
- If one doc tries to do too many jobs, split it
- Do not archive across categories; archive within the same category

## Notes

- Do not force this onto a repository that already has better local rules
- Keep the structure simple
- Update obvious nearby indexes or links when moving docs
- Do not use `docs/check/` for ordinary progress notes or implementation plans
