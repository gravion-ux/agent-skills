---
name: run-a-test-of-the-test-suite
description: Run a test of the test suite by mutating the code and confirming the expected tests fail. Use when the user wants evidence that the test suite actually catches defects.
domain: testing-qa
tags: [mutation-testing, suite-validation, test-quality]
triggers: ["run a test of the test suite", "mutation test the suite", "prove tests catch defects"]
---

# Run a test of the test suite by mutating the code and confirming the expected tests fail

## Purpose

Run a test of the test suite by mutating the code and confirming the expected tests fail.

## When to use

Use when the user wants evidence that the test suite actually catches defects.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Select a mutation such as a removed branch, an inverted condition, or a changed boundary.
2. Apply one mutation at a time to the production code.
3. Run the suite and record which tests failed for each mutation.
4. Revert the mutation and confirm the suite passes again on the original code.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `run-a-test-suite-in-parallel`
- `review-a-test-suite-for-gap-coverage`
- `run-a-smoke-test-after-a-deploy`
