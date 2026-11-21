---
name: use-a-test-double-for-slow-io
description: Use a test double for slow IO so the suite runs fast without skipping real behaviour checks. Use when the user has tests that take too long because of slow network or disk access.
domain: testing-qa
tags: [test-doubles, slow-io, test-speed]
triggers: ["test double for slow io", "speed up a slow test", "replace slow network call in test"]
---

# Use a test double for slow IO so the suite runs fast without skipping real behaviour checks

## Purpose

Use a test double for slow IO so the suite runs fast without skipping real behaviour checks.

## When to use

Use when the user has tests that take too long because of slow network or disk access.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Measure which IO call dominates the runtime of the slow test.
2. Wrap that call behind a double that returns a captured or crafted result.
3. Keep one slower test against the real dependency as a nightly check.
4. Compare the suite duration before and after the replacement.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `build-a-test-harness-for-multiple-environments`
- `review-a-test-suite-for-gap-coverage`
- `write-a-canary-test-for-a-risk-area`
