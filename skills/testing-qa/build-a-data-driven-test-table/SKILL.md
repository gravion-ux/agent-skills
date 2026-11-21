---
name: build-a-data-driven-test-table
description: Build a data-driven test table that runs one assertion body across many input cases. Use when the user has many similar cases and wants one readable test body.
domain: testing-qa
tags: [data-driven-testing, parametrisation, test-tables]
triggers: ["data-driven test table", "parametrise a test with cases", "table driven test cases"]
---

# Build a data-driven test table that runs one assertion body across many input cases

## Purpose

Build a data-driven test table that runs one assertion body across many input cases.

## When to use

Use when the user has many similar cases and wants one readable test body.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Collect the input, expected output, and label for every case.
2. Move the case list into a table of tuples or dictionaries.
3. Write one test body that reads each case from the table.
4. Parametrise the test so each case reports under its own label.

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
- `build-a-test-harness-for-multiple-environments`
- `design-a-test-data-strategy`
