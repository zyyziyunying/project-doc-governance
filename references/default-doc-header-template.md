# Default Document Header Template

Use this only when a repository does not already define its own header or metadata pattern.

This template is intentionally small.
It only covers the opening context block of a document.

## Minimal Header

```md
# <Document Title>

Status: <draft | active | archived | superseded>
Scope: <what this document is about>
Source of truth: <owning doc, local taxonomy doc, ADR, issue, or "this file">
```

## Optional Fields

Add only when they are useful:

- Owner: who maintains the doc
- Audience: who should read it
- Last updated: `YYYY-MM-DD`
- Replaces: old path or superseded doc

## Archive Variant

```md
# <Document Title>

Status: <archived | superseded>
Scope: <what this historical file records>
Replaces: <old path or old doc>
Source of truth: <current doc or "this file">
```

## Example

```md
# Payment Retry Notes

Status: active
Scope: Retry behavior and known failure modes for payment requests.
Source of truth: docs/README.md
```

## Boundaries

- Do not force this onto repositories that already have a stable local format
- Do not turn this into a body-section template
- Skip fields that would be fake or noisy
