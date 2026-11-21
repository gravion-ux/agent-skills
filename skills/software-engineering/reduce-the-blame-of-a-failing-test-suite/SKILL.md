---
name: reduce-the-blame-of-a-failing-test-suite
description: Reduce the blame of a failing test suite by isolating the first independent failure and fixing root causes. Use when the user wants a noisy failing test suite reduced to actionable root causes.
domain: software-engineering
tags: [test-suite, triage, root-cause]
triggers: ["reduce failing test suite blame", "isolate first test failure", "triage noisy test suite"]
---

# Reduce the blame of a failing test suite by isolating the first independent failure and fixing root causes

## Purpose

Reduce the blame of a failing test suite by isolating the first independent failure and fixing root causes.

## When to use

Use when the user wants a noisy failing test suite reduced to actionable root causes.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Run the suite in the documented order and capture the first independent failure.
2. Check shared state, ordering, environment, and timing before changing assertions.
3. Reproduce the failure alone and in its original suite context.
4. Fix the root cause without weakening or deleting the failing test.
5. Re-run focused and full suites and report remaining failures with evidence.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `rename-a-symbol-across-the-codebase`
- `add-structured-logging-to-a-code-path`
- `apply-solid-principles-to-a-class`
