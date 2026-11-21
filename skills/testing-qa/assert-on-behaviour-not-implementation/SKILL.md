---
name: assert-on-behaviour-not-implementation
description: Assert on observable behaviour rather than internal calls so refactors do not break the test. Use when the user wants to stop a test from breaking on harmless internal changes.
domain: testing-qa
tags: [assertions, behaviour-testing, refactoring]
triggers: ["assert on behaviour not implementation", "test asserts on internal calls", "avoid mock assertions in test"]
---

# Assert on observable behaviour rather than internal calls so refactors do not break the test

## Purpose

Assert on observable behaviour rather than internal calls so refactors do not break the test.

## When to use

Use when the user wants to stop a test from breaking on harmless internal changes.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. List the internal calls and private fields the current test asserts on.
2. Rewrite each assertion around the public output, stored state, or emitted event.
3. Keep one test per user-visible outcome instead of one per internal step.
4. Change the implementation internals and confirm the test still passes.

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
- `test-a-migration-on-a-copy-of-production-data`
- `automate-a-visual-regression-check`
