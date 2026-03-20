# Default Project Docs Taxonomy

Use this reference only when a repository does not already define its own documentation taxonomy.

## Read Local Docs First

Before using this default model, read repository-local structure docs when they exist:

- `AGENTS.md`
- `docs/README.md`
- `docs/taxonomy.md`
- `docs/doc-taxonomy.md`
- `docs/structure.md`
- category index files or neighboring directory README files

If those files define placement rules, follow them instead of this reference.

## Default Categories

### `docs/problem/`

Use for implementation-facing project documents such as:

- active plans
- blockers
- migration constraints
- phase definitions
- data-contract decisions
- acceptance or rebuild rules

These documents may directly affect coding, validation, migration, or review outcomes.

### `docs/problem/archive/`

Use for historical problem documents that are no longer active but still useful for traceability.

Move closed blocker documents here instead of deleting them when the history still explains past decisions.

### `docs/knowledge/`

Use for developer-facing background material such as:

- concept explanations
- learning notes
- technology overviews
- high-level implementation understanding

These documents help humans understand the domain. They are not default agent-required execution specs.

### Standalone Guide Files

Use standalone guide files for narrow operational references that are not broad enough to justify a full category.

If multiple guides of the same kind accumulate, consider introducing a dedicated category later, but only after the pattern is real.

## Placement Rules

Choose the destination by the document's strongest function.

- If the file defines what implementation must do, it belongs in `docs/problem/`.
- If the file explains how something works or how to think about it, it belongs in `docs/knowledge/`.
- If the file explains how to operate or maintain one subsystem, keep it as a guide file unless a broader guide category becomes necessary.

When a file mixes concerns:

- split background explanation from binding rules
- keep the binding rules closer to implementation docs
- keep the explanatory material in `docs/knowledge/`

## Synchronization Rules

When a repository uses this default model and the taxonomy changes, update these files in the same task:

- `docs/README.md` for human-facing structure
- `AGENTS.md` for short agent-facing operating rules

Do not rely on only one of them if both audiences are affected.

## Signals That a Doc Is Misfiled

- a `knowledge` doc is cited as the binding implementation contract
- a `problem` doc mainly teaches concepts and contains few concrete decisions
- the same rule appears in multiple docs with different wording
- a guide file starts acting like a phase plan or migration contract
- new docs require repeated debate about placement because the taxonomy is underspecified

## When to Add a New Category

Add a new top-level docs category only if all of these are true:

1. at least two or three documents already share a distinct purpose
2. that purpose is not well served by `problem`, `knowledge`, or a standalone guide
3. the new category can be explained in one or two clear sentences in `docs/README.md`

If those conditions are not met, keep the structure smaller.
