# Default Project Docs Taxonomy

Use this reference only when repository-local docs do not already settle the placement decision.

## Local-First Rules

Read local structure docs first when they exist:

- `docs/taxonomy.md`
- `docs/doc-taxonomy.md`
- `docs/structure.md`
- category index files or neighboring directory README files
- `AGENTS.md`
- `docs/README.md`, but only when it explicitly defines human-facing docs structure or placement

Use this precedence order for placement decisions:

1. the nearest dedicated taxonomy, placement, or category index file that explicitly covers the target path
2. a repository-level taxonomy or structure document that defines category semantics
3. `docs/README.md` when it explicitly defines the human-facing docs structure or placement
4. `AGENTS.md` for agent-operational handling or explicit pointers to the real source of truth
5. this reference, only when the repository does not define the needed rule

Treat a local taxonomy source as:

- missing when it does not cover the current document class or destination decision
- partial when it defines a stable pattern for part of the tree but leaves some classes, destinations, or boundary cases unspecified
- stale when it points to removed paths, contradicts the active tree, conflicts with a more specific maintained source, or clearly predates a known restructure

When local docs are partial, extend the stable local pattern and use this reference only for the uncovered portion.
When local docs are stale but a stronger active source still makes the outcome clear, follow the stronger source and report the stale doc that needs synchronization.
If stale or conflicting local docs would materially change the result, report the ambiguity instead of inventing a merged rule.

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

Use this only as a repository-local pattern when the smaller fallback categories are too coarse for a project whose docs repeatedly revolve around problem definition, analysis, discussion, planning, and status tracking.

This is not a new global default.
Use it only when:

- the repository already documents the pattern locally
- or the existing docs already show a repeated split that the smaller fallback would materially collapse, and you can formalize that adoption locally in the same task

If that signal is absent, keep the smaller fallback categories.

Recommended categories:

- `docs/problem/`
- `docs/plan/`
- `docs/status/`
- `docs/analysis/`
- `docs/discussion/`

If a repository already uses `docs/progress/`, it can keep that directory name, but it should define it with `status` semantics rather than treating it as a generic time-based bucket.

Use these category meanings:

- `problem`: problem statements, constraints, acceptance gaps, blockers, and risks
- `plan`: accepted implementation plans, migration steps, rollout checklists, and task breakdowns
- `status`: progress snapshots, phase closeouts, completion records, and stabilization summaries
- `analysis`: root-cause analysis, technical comparison, investigations, experiments, and evaluation material
- `discussion`: unresolved design debate, RFC drafts, meeting discussion notes, and open questions

Keep mixed-purpose docs split instead of stretching one file across multiple category meanings.

## Common Document Class Mapping

Use these default mappings only when the repository does not already define a better local convention:

- ADRs: keep active or accepted architecture decisions with implementation-facing docs, unless the repository already has a dedicated ADR area
- RFCs or design proposals: keep active proposals with implementation-facing docs while they still drive implementation debate; archive rejected or expired proposals
- runbooks and operational playbooks: keep them as guide files or in an operations-guides area unless they are purely explanatory
- incident reports and postmortems: keep the narrative and timeline in a historical or archive area; split any still-open corrective actions into implementation-facing docs
- release notes and changelogs: keep them with release-history docs, not under `problem` or `knowledge`, unless the repository explicitly treats them that way
- meeting notes: treat them as historical working notes, not as the source of truth; promote decisions and actions into authoritative docs
- investigations and spikes: keep active investigations with implementation-facing docs while they inform active decisions; move durable explanatory findings into knowledge docs; archive closed investigations that are no longer an active contract

## Synchronization Checklist

When taxonomy or placement changes under this fallback model, update in the same task:

- the repository's human-facing docs index or taxonomy doc
- `AGENTS.md` only when short agent-operational rules must change

After moving or splitting docs, check:

- outbound links from moved or split docs
- inbound references from `docs/README.md`, directory indexes, and neighboring docs
- archive pointers, replacement notes, or historical breadcrumbs when readers still need the old path

If any of these fixes are deferred, report them explicitly.
