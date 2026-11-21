---
name: name-tests-so-failures-explain-themselves
description: Name tests so a failing test line states the behaviour, input, and expected result. Use when the user wants readable failure output from a large test suite.
domain: testing-qa
tags: [test-naming, readability, failure-output]
triggers: ["name tests so failures explain themselves", "rename a test to be clearer", "readable test names"]
---

# Name tests so a failing test line states the behaviour, input, and expected result

## Purpose

Name tests so a failing test line states the behaviour, input, and expected result.

## When to use

Use when the user wants readable failure output from a large test suite.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Write each test name as behaviour, condition, and expected result.
2. Remove ticket numbers, abbreviations, and filler words from the names.
3. Keep one scenario per test name so the failure reads unambiguously.
4. Run the suite and scan the failing test names for clarity.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `assert-on-behaviour-not-implementation`
- `automate-a-visual-regression-check`
- `build-a-data-driven-test-table`
