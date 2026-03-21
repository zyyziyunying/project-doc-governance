# Default Project Docs Taxonomy

Use this reference only when a repository does not already define its own documentation taxonomy.

## Read Local Docs First

Before using this default model, read repository-local structure docs when they exist:

- `docs/taxonomy.md`
- `docs/doc-taxonomy.md`
- `docs/structure.md`
- category index files or neighboring directory README files
- `AGENTS.md`
- `docs/README.md`, but only when it explicitly defines human-facing docs structure or placement

Do not infer docs placement from a general project `README.md` unless it explicitly defines taxonomy rules for the target scope.

If those files define placement rules, follow them instead of this reference.

## Authority And Conflict Resolution

Use this order when deciding which rule controls a documentation placement decision:

1. the nearest dedicated taxonomy, placement, or category index file that explicitly covers the target path
2. a repository-level taxonomy or structure document that defines category semantics
3. `docs/README.md` when it explicitly defines the human-facing docs structure or placement
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

A `docs/README.md` that is only navigational and does not define category meaning or placement is not a controlling source for classification.

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

## Optional Local Pattern For Execution-Heavy Repositories

Use this only as a repository-local taxonomy pattern when the generic fallback categories are too coarse for a project whose docs repeatedly revolve around problem definition, analysis, discussion, planning, and status tracking.

This is not a new global default. It becomes authoritative only after the repository documents it locally in `docs/README.md`, `docs/taxonomy.md`, or a similarly scoped taxonomy file.

Recommended categories:

- `docs/problem/`
- `docs/plan/`
- `docs/status/`
- `docs/analysis/`
- `docs/discussion/`

If a repository already uses `docs/progress/`, it can keep that directory name, but it should define it with `status` semantics rather than treating it as a generic bucket for anything time-related.

Each category may keep its own `archive/` subdirectory for closed material, for example:

- `docs/problem/archive/`
- `docs/plan/archive/`
- `docs/status/archive/`
- `docs/analysis/archive/`
- `docs/discussion/archive/`

Use these category meanings:

- `problem`: problem statements, constraints, acceptance gaps, blockers, and risks
- `plan`: accepted implementation plans, migration steps, rollout checklists, and task breakdowns
- `status`: progress snapshots, phase closeouts, completion records, and stabilization summaries
- `analysis`: root-cause analysis, technical comparison, investigations, experiments, and evaluation material
- `discussion`: unresolved design debate, RFC drafts, meeting discussion notes, and open questions

Use these boundary rules:

- Keep `problem` focused on what must be solved or respected, not how the work will be executed.
- Keep `plan` for chosen execution paths, not still-open debate.
- Keep `analysis` for evidence and reasoning, not final implementation mandates.
- Keep `discussion` for unresolved conversation, not durable rules.
- Keep `status` for reporting outcomes and state, not as a second home for plans or requirements.
- Split mixed-purpose docs instead of stretching one file across multiple category meanings.

Common mappings under this local pattern:

- blockers and acceptance gaps -> `problem`
- rollout plans and migration checklists -> `plan`
- weekly updates and closeout summaries -> `status`
- root-cause analysis and technical comparison -> `analysis`
- RFC drafts and meeting debate notes -> `discussion`

When a discussion becomes binding:

- promote durable requirements into `problem` or the repository's implementation-facing source of truth
- promote accepted execution steps into `plan`
- archive the historical discussion copy under `discussion/archive/` when it is no longer active

When a repository adopts this pattern, keep the structure small at first. Add extra top-level categories only after the repository has repeated documents with a clearly different purpose that does not fit these five categories or a standalone guide.

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

- the repository's human-facing docs index or taxonomy doc, often `docs/README.md` when the repository uses it for that purpose
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
