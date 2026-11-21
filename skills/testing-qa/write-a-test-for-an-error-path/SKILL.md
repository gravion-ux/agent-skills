---
name: write-a-test-for-an-error-path
description: Write a test for an error path that asserts the exact error type and user-facing message. Use when the user wants the failure branch of a function covered and verified.
domain: testing-qa
tags: [error-path, exception-testing, negative-test]
triggers: ["test for an error path", "test the failure branch", "assert an error is raised"]
---

# Write a test for an error path that asserts the exact error type and user-facing message

## Purpose

Write a test for an error path that asserts the exact error type and user-facing message.

## When to use

Use when the user wants the failure branch of a function covered and verified.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Choose the input that triggers the documented failure branch.
2. Run the code and capture the raised error type and message.
3. Assert the error type and the message segment the caller depends on.
4. Add a companion test that proves the valid input still succeeds.

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
- `write-a-test-plan-for-a-release`
