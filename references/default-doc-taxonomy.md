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

## Authority And Conflict Resolution

Use this order when deciding which rule controls a documentation placement decision:

1. the nearest dedicated taxonomy, placement, or category index file that explicitly covers the target path
2. a repository-level taxonomy or structure document that defines category semantics
3. `docs/README.md` when it defines the human-facing docs structure
4. `AGENTS.md` for agent-operational handling, or for explicit pointers to the real source of truth
5. this default reference, only when the repository does not define the needed rule

Apply these tie-break rules:

- Prefer the more specific scope over the broader scope.
- Prefer dedicated taxonomy docs over general README or index docs when both cover the same scope.
- Prefer human-facing taxonomy docs over `AGENTS.md` for category meaning and placement.
- If two sources at the same level disagree and neither is clearly stale, report the conflict instead of inventing a merged rule.

Treat a local taxonomy source as stale when one or more of these are true:

- it points to directories or files that no longer exist
- it describes category semantics that contradict the active docs structure
- it conflicts with a more specific maintained source
- it has clearly not been updated after a known restructure

When local docs are stale or incomplete:

- follow the strongest still-valid local source when the correct outcome is still clear
- report the stale files that need synchronization
- fall back to this reference only for the uncovered portion of the decision
- avoid broad restructuring based only on inference when stale docs could change the result

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

## Common Document Class Mapping

Use these default mappings only when the repository does not already define a better local convention.

- ADRs: keep active or accepted architecture decisions with implementation-facing docs. If the repository has a dedicated ADR area, use it. Otherwise keep them with `docs/problem/` or an equivalent decision area. Superseded ADRs can be archived if the repository keeps decision history separately.
- RFCs or design proposals: keep active proposals with implementation-facing docs while they still drive implementation debate. Archive rejected or expired proposals. If a proposal becomes binding, promote the durable rules into the implementation-facing source of truth.
- Runbooks and operational playbooks: keep them as guide files or in an operations-guides area. They are operational references, not knowledge docs, unless they are purely explanatory.
- Incident reports and postmortems: keep the narrative and timeline in a historical or archive area. Split any still-open corrective actions into implementation-facing docs.
- Release notes and changelogs: keep them with release-history docs, not under `problem` or `knowledge`, unless the repository explicitly treats them that way.
- Meeting notes: treat them as historical working notes, not as the source of truth. Promote decisions, actions, and binding rules into authoritative docs and archive the notes separately.
- Investigations and spikes: keep active investigations with implementation-facing docs while they inform active decisions. Move durable explanatory findings into knowledge docs. Archive closed investigations that are no longer an active contract.

## Synchronization Rules

When a repository uses this default model and the taxonomy changes, update these files in the same task:

- `docs/README.md` for human-facing structure
- `AGENTS.md` for short agent-facing operating rules

Do not rely on only one of them if both audiences are affected.

## Migration Integrity Checklist

After moving or splitting docs under this default model, check:

- outbound links from the moved or split docs
- inbound references from `docs/README.md`, directory indexes, and neighboring docs
- archive references, replacement pointers, or historical breadcrumbs when readers still need the old path
- any navigation files that summarize category contents

If you defer any of these fixes, report them explicitly.

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
