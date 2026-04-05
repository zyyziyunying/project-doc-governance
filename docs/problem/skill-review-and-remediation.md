# Project Doc Governance Skill Review and Remediation

Reviewed on: 2026-03-22
Updated on: 2026-04-04
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
- On 2026-04-04, a follow-up review found that the execution-heavy pattern rule is no longer stated consistently across the live files: `SKILL.md` still allows activation when a repository merely shows a repeated split that can be formalized locally in the same task, while `references/default-doc-taxonomy.md` and this tracker say the pattern should activate only when the repository already documents it locally.
- On 2026-04-04, the lightweight validator was confirmed to be too narrow to catch that drift: `scripts/basic_validate.py` currently checks frontmatter, local links, and `agents/openai.yaml`, but it does not verify consistency between `SKILL.md`, the fallback reference, and this active tracker.
- The working reassessment remains `8/10` as of 2026-03-22.
- The remaining gap is now split between retained field validation and one immediate contract-consistency fix around execution-heavy pattern activation.

## Active Issues

- Contract drift: the execution-heavy local pattern activation rule is materially inconsistent between `SKILL.md` and `references/default-doc-taxonomy.md`, so different agents could still reach different classification results on the same repository.
- Validation blind spot: `scripts/basic_validate.py` can still pass while the live contract and fallback reference disagree on a classification trigger, which weakens maintenance confidence.
- Evidence remains thinner than the authority model as written: there is still no retained trial for a repository with a dedicated taxonomy doc or for one where `docs/README.md` is mostly navigational, so the most important boundary cases are still under-validated.

## Active Validation Gaps

- A retained or replayable check is still missing for the exact execution-heavy activation boundary so the repeated-split branch can either be revalidated with evidence or removed from `SKILL.md`.
- A lightweight consistency check is still missing for high-risk rules shared across `SKILL.md`, `references/default-doc-taxonomy.md`, and this tracker, especially authority precedence and execution-heavy activation.
- A retained trial is still missing for a repository that already has a dedicated taxonomy doc or category README with real placement semantics.
- A retained trial is still missing for a repository where `docs/README.md` is mostly navigational and should not become authority.
- A retained trial is still missing for any future re-expansion of the execution-heavy local pattern beyond repositories that already document that pattern locally.

## Next Review Gate

- Reconcile the execution-heavy activation rule so `SKILL.md`, `references/default-doc-taxonomy.md`, and this tracker describe the same trigger before any broader rollout or score increase.
- Extend `scripts/basic_validate.py` or add an equivalent lightweight check so future cross-file rule drift is detected automatically.
- Re-run the review after at least one retained migration against a repository with stronger local docs rules and at least one mixed-purpose document split.
- Do not raise the score above `8/10` until the validation gaps above have retained evidence or are explicitly retired.

## Archived Material

- Historical review evidence, the original baseline findings, the completed phase backlog, and detailed forward-test notes live in [archive/2026-03-21-skill-review-history.md](archive/2026-03-21-skill-review-history.md).
