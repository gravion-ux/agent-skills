---
name: build-a-test-fixture-that-does-not-leak-state
description: Build a test fixture that resets state so each test starts from the same known baseline. Use when the user sees order-dependent failures or dirty state between tests.
domain: testing-qa
tags: [test-fixture, test-isolation, cleanup]
triggers: ["test fixture that does not leak state", "test state leaks between tests", "reset test state fixture"]
---

# Build a test fixture that resets state so each test starts from the same known baseline

## Purpose

Build a test fixture that resets state so each test starts from the same known baseline.

## When to use

Use when the user sees order-dependent failures or dirty state between tests.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. List every table, cache key, file, and global variable the code touches.
2. Move the setup and teardown into one reusable fixture.
3. Restore or recreate each touched resource after every test.
4. Run the suite in a shuffled order and confirm the failures disappear.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `build-a-data-driven-test-table`
- `build-a-test-harness-for-multiple-environments`
- `write-a-regression-test-that-fails-first`
