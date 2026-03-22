# Project Doc Governance Skill Review and Remediation

Reviewed on: 2026-03-22
Scope: `C:\Users\zyy\.codex\skills\project-doc-governance`
Reviewer stance: strict, portability-first, maintenance-focused

Document role: active repository-local tracker for remaining validation gaps and the next review gate.
Placement authority: `docs/README.md`
Historical archive: [archive/2026-03-21-skill-review-history.md](archive/2026-03-21-skill-review-history.md)

## Current Status

- Phases 1 through 7 were completed on 2026-03-20.
- On 2026-03-22, the rule wording in `SKILL.md` and `references/default-doc-taxonomy.md` was tightened around authority, stale-versus-partial handling, and execution-heavy pattern activation.
- On 2026-03-22, `references/default-doc-taxonomy.md` also absorbed the old-path migration rule: high-visibility old paths now default to a redirect stub, while other traceability-sensitive cases still require a breadcrumb.
- On 2026-03-22, the execution-heavy local pattern was narrowed back to repositories that already document that pattern locally; the earlier proactive-adoption branch was removed pending retained validation.
- The old-path migration convergence was treated as sufficiently validated for the narrower fallback-sync rule because `video_list_android_demo` provides a retained positive migration sample and the lower-visibility breadcrumb obligation already existed in the baseline checklist.
- The working reassessment remains `8/10` as of 2026-03-22.
- The remaining gap is retained field validation, not another immediate wording pass.

## Active Validation Gaps

- A retained trial is still missing for a repository that already has a dedicated taxonomy doc or category README with real placement semantics.
- A retained trial is still missing for a repository where `docs/README.md` is mostly navigational and should not become authority.
- A retained trial is still missing for any future re-expansion of the execution-heavy local pattern beyond repositories that already document that pattern locally.

## Next Review Gate

- Re-run the review after at least one retained migration against a repository with stronger local docs rules and at least one mixed-purpose document split.
- Do not raise the score above `8/10` until the validation gaps above have retained evidence or are explicitly retired.

## Archived Material

- Historical review evidence, the original baseline findings, the completed phase backlog, and detailed forward-test notes live in [archive/2026-03-21-skill-review-history.md](archive/2026-03-21-skill-review-history.md).
