---
name: test-a-feature-flagged-code-path
description: Test a feature-flagged code path by exercising both flag states in separate deterministic runs. Use when the user wants proof that both sides of a feature flag behave correctly.
domain: testing-qa
tags: [feature-flags, branch-testing, variant-coverage]
triggers: ["test a feature flagged code path", "test both sides of a feature flag", "feature flag on and off test"]
---

# Test a feature-flagged code path by exercising both flag states in separate deterministic runs

## Purpose

Test a feature-flagged code path by exercising both flag states in separate deterministic runs.

## When to use

Use when the user wants proof that both sides of a feature flag behave correctly.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Find the flag evaluation point and the configuration source used in the test run.
2. Run the scenario with the flag off and record the expected legacy behaviour.
3. Run the scenario with the flag on and assert the new behaviour and side effects.
4. Assert the flag is read once per request so a mid-run change cannot alter the result.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `test-a-timezone-sensitive-feature`
- `write-a-test-for-an-error-path`
- `build-a-data-driven-test-table`
