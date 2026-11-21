---
name: detect-and-fix-a-flaky-test
description: Detect a flaky test by rerunning it repeatedly and fix the shared-state cause, not the symptom. Use when the user sees a test that passes and fails on the same unchanged code.
domain: testing-qa
tags: [flaky-test, test-stability, root-cause]
triggers: ["detect and fix a flaky test", "fix a test that fails randomly", "flaky test root cause"]
---

# Detect a flaky test by rerunning it repeatedly and fix the shared-state cause, not the symptom

## Purpose

Detect a flaky test by rerunning it repeatedly and fix the shared-state cause, not the symptom.

## When to use

Use when the user sees a test that passes and fails on the same unchanged code.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Rerun the test at least twenty times and record the failure rate.
2. Capture logs and state from a failing run to find the ordering or timing dependency.
3. Fix the cause by isolating state, removing real sleeps, or controlling time.
4. Rerun the test twenty more times and confirm a zero failure rate.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `quarantine-a-flaky-test-with-a-ticket`
- `build-a-data-driven-test-table`
- `build-a-test-fixture-that-does-not-leak-state`
