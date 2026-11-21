---
name: write-a-regression-test-that-fails-first
description: Write a regression test that fails on the old bug and passes only after the fix lands. Use when the user wants a test that locks in a recently fixed defect.
domain: testing-qa
tags: [regression-test, bug-fix, red-green]
triggers: ["regression test that fails first", "write a test for this bug", "lock in a bug fix with a test"]
---

# Write a regression test that fails on the old bug and passes only after the fix lands

## Purpose

Write a regression test that fails on the old bug and passes only after the fix lands.

## When to use

Use when the user wants a test that locks in a recently fixed defect.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Reproduce the reported defect with the smallest input that triggers it.
2. Run the new test against the unfixed code and confirm it fails for the reported reason.
3. Apply the fix and rerun the test to confirm it passes.
4. Record the defect identifier in the test comment.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `build-a-test-fixture-that-does-not-leak-state`
- `write-a-canary-test-for-a-risk-area`
- `write-a-contract-test-for-two-services`
