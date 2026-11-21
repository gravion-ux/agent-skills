---
name: verify-accessibility-in-a-test
description: Verify accessibility in an automated test that checks roles, labels, and contrast on key screens. Use when the user wants accessibility regressions caught in the automated suite.
domain: testing-qa
tags: [accessibility, automated-testing, a11y]
triggers: ["verify accessibility in a test", "automated accessibility check", "catch a11y regressions in ci"]
---

# Verify accessibility in an automated test that checks roles, labels, and contrast on key screens

## Purpose

Verify accessibility in an automated test that checks roles, labels, and contrast on key screens.

## When to use

Use when the user wants accessibility regressions caught in the automated suite.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Choose the key screens and the accessibility rules each screen must satisfy.
2. Add role, accessible-name, and keyboard-order assertions for interactive elements.
3. Run the contrast checker on the documented text and background colour pairs.
4. Fail with the rule id and the offending element when a check breaks.

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
- `build-a-data-driven-test-table`
- `build-a-test-fixture-that-does-not-leak-state`
