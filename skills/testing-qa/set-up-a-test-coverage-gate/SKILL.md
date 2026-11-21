---
name: set-up-a-test-coverage-gate
description: Set up a coverage gate that fails the build below a documented threshold and reports gaps. Use when the user wants coverage measured and enforced in continuous integration.
domain: testing-qa
tags: [coverage-gate, code-coverage, continuous-integration]
triggers: ["set up a test coverage gate", "enforce coverage threshold in ci", "fail build on low coverage"]
---

# Set up a coverage gate that fails the build below a documented threshold and reports gaps

## Purpose

Set up a coverage gate that fails the build below a documented threshold and reports gaps.

## When to use

Use when the user wants coverage measured and enforced in continuous integration.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Instrument the source and run the suite once to produce a baseline coverage report.
2. Exclude generated code, type stubs, and defensive branches from the report.
3. Set the minimum threshold at the baseline value so no coverage is lost today.
4. Fail the build below the threshold and publish the uncovered lines.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `review-a-test-suite-for-gap-coverage`
- `build-a-data-driven-test-table`
- `build-a-test-fixture-that-does-not-leak-state`
