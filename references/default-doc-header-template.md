# Default Document Header Template

Use this reference only when a repository does not already define its own document header or metadata pattern.

This template governs only the opening metadata block of a document.
It does not prescribe body sections, heading depth, or narrative layout.

## Purpose

Use a lightweight header when:

- creating a new project doc under fallback rules
- normalizing an existing doc whose opening context is unclear
- splitting a mixed-purpose doc and needing each new file to declare its role clearly

Skip fields that would be fake, redundant, or repo-local noise.
If the repository already has a stable local header format, use that instead.

## Minimal Header

```md
# <Document Title>

Status: <draft | active | archived | superseded>
Scope: <what this document governs or describes>
Source of truth: <local taxonomy doc, owning directory README, issue, ADR, or "this file">
```

## Archive Or Migration Variant

```md
# <Document Title>

Status: <archived | superseded>
Scope: <what this historical file records or what old path it replaces>
Replaces: <old path or superseded doc>
Source of truth: <current controlling doc or "this file">
```

## Optional Fields

Add only when they help readers make a placement or usage decision:

- Owner: person, team, or module responsible for keeping the doc current
- Audience: who should read or act on the doc
- Depends on: upstream spec, plan, or decision this doc relies on
- Last updated: `YYYY-MM-DD` when the repository relies on an in-doc freshness signal
- Replaces: old path or superseded doc when the file is part of a migration
- Review cadence: when the doc should be revisited if staleness is likely

## Field Notes

- `Status` should describe lifecycle state, not emotional confidence.
- Recommended fallback status set: `draft`, `active`, `archived`, `superseded`.
- `Scope` should be short and concrete enough that a reader can tell why the file exists.
- `Source of truth` should point to the controlling authority when one exists; use `this file` only when the file itself is authoritative for its narrow purpose.
- `Last updated` should stay optional unless the repository actually uses it to manage freshness.
- `Replaces` is most useful for archived redirects, migration notes, and superseded docs.

## Example

```md
# Playback Stability Closeout

Status: archived
Scope: Historical closeout record for the Android playback stabilization pass completed in March 2026.
Replaces: STABILITY_CLOSEOUT_PLAN.md
Source of truth: docs/README.md
```

## Boundaries

- Do not force this template onto repositories that already use frontmatter, ADR headers, RFC headers, or another local metadata convention.
- Do not pad the header with fields that have no active owner or decision value.
- Do not infer detailed body structure from this template.
- If a document is intentionally lightweight, keep the header lightweight too.
