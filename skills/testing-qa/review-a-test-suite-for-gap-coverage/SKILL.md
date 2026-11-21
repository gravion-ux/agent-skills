---
name: review-a-test-suite-for-gap-coverage
description: Review a test suite for gap coverage by comparing behaviour contracts against the existing tests. Use when the user wants a risk-ranked list of untested behaviour in an existing suite.
domain: testing-qa
tags: [test-review, coverage-analysis, gap-analysis]
triggers: ["review a test suite for gap coverage", "find untested behaviour", "coverage gap analysis"]
---

# Review a test suite for gap coverage by comparing behaviour contracts against the existing tests

## Purpose

Review a test suite for gap coverage by comparing behaviour contracts against the existing tests.

## When to use

Use when the user wants a risk-ranked list of untested behaviour in an existing suite.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Collect the acceptance criteria, error contracts, and documented edge cases.
2. Map each criterion to the test that covers it or to a gap.
3. Rank the gaps by user impact and by the likelihood of a silent failure.
4. Write the top gaps as proposed test cases with their expected assertions.

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
- `run-a-test-of-the-test-suite`
- `run-a-test-suite-in-parallel`
