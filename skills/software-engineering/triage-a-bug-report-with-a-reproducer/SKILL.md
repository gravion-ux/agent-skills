---
name: triage-a-bug-report-with-a-reproducer
description: Turn a bug report into a minimal reproducer, a severity decision, and an automated regression test. Use when the user wants a defect report converted into actionable engineering work.
domain: software-engineering
tags: [bug-triage, reproducer, regression-testing]
triggers: ["triage a bug with a reproducer", "minimize a defect reproduction"]
---

# Turn a bug report into a minimal reproducer, a severity decision, and an automated regression test

## Purpose

Turn a bug report into a minimal reproducer, a severity decision, and an automated regression test.

## When to use

Use when the user wants a defect report converted into actionable engineering work.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Record affected versions, environment, and observed behavior.
2. Reproduce the report and remove unrelated setup steps.
3. Trace the failing path to the likely defect boundary.
4. Assign severity and identify the first safe fix.
5. Add a regression test that fails on the old behavior.
6. Run existing tests and document rationale and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `reproduce-a-bug-in-a-local-sandbox`
- `add-structured-logging-to-a-code-path`
- `apply-solid-principles-to-a-class`
