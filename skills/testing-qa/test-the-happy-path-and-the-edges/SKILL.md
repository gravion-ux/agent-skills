---
name: test-the-happy-path-and-the-edges
description: Pair a happy-path test with boundary and empty-case tests in one focused test class. Use when the user wants one behaviour covered from the normal case to its limits.
domain: testing-qa
tags: [boundary-testing, edge-cases, happy-path]
triggers: ["test the happy path and the edges", "add boundary test cases", "cover empty and invalid input"]
---

# Pair a happy-path test with boundary and empty-case tests in one focused test class

## Purpose

Pair a happy-path test with boundary and empty-case tests in one focused test class.

## When to use

Use when the user wants one behaviour covered from the normal case to its limits.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Write the happy-path test with one representative valid input.
2. Add a case at each boundary the contract defines.
3. Add an empty and an invalid input case for the same function.
4. Name each case so the boundary it covers appears in the failure output.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `detect-and-fix-a-flaky-test`
- `run-a-test-of-the-test-suite`
- `test-a-feature-flagged-code-path`
