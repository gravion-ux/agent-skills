---
name: write-a-unit-test-for-a-pure-function
description: Write a unit test for a pure function that checks one input-output pair per assertion. Use when the user wants a fast unit test for a function with no side effects.
domain: testing-qa
tags: [unit-test, pure-function, assertions]
triggers: ["unit test for a pure function", "test a pure function", "write a unit test with no side effects"]
---

# Write a unit test for a pure function that checks one input-output pair per assertion

## Purpose

Write a unit test for a pure function that checks one input-output pair per assertion.

## When to use

Use when the user wants a fast unit test for a function with no side effects.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Pick one representative input and the exact value the function must return.
2. Call the function once and store the result in a named variable.
3. Assert the result equals the expected value with no loose matcher.
4. Run the test file with a wrong expected value and confirm it fails.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `write-a-canary-test-for-a-risk-area`
- `write-a-contract-test-for-two-services`
- `write-a-test-for-an-error-path`
