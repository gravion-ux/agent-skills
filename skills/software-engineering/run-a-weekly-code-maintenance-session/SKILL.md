---
name: run-a-weekly-code-maintenance-session
description: Run a bounded weekly maintenance pass that improves code quality, preserves tests, and records remaining risks. Use when the user wants to schedule recurring repository maintenance work.
domain: software-engineering
tags: [maintenance, code-quality, refactoring]
triggers: ["run a weekly maintenance session", "schedule recurring code maintenance"]
---

# Run a bounded weekly maintenance pass that improves code quality, preserves tests, and records remaining risks

## Purpose

Run a bounded weekly maintenance pass that improves code quality, preserves tests, and records remaining risks.

## When to use

Use when the user wants to schedule recurring repository maintenance work.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Collect warnings, flaky tests, dependency alerts, and stale debt items.
2. Select maintenance work bounded to one focused session.
3. Apply small fixes without weakening tests or changing scope.
4. Run targeted and full checks for the selected changes.
5. Update the technical debt register with unresolved findings.
6. Summarize the diff, rationale, and rollback procedure.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `add-structured-logging-to-a-code-path`
- `automate-a-repetitive-code-change`
- `make-a-script-safe-to-run-twice`
