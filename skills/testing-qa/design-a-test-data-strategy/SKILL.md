---
name: design-a-test-data-strategy
description: Design a test data strategy that defines fixtures, factories, cleanup, and ownership per environment. Use when the user wants a shared approach to creating and maintaining test data.
domain: testing-qa
tags: [test-data, fixtures, data-management]
triggers: ["design a test data strategy", "manage test data across environments", "test data fixtures plan"]
---

# Design a test data strategy that defines fixtures, factories, cleanup, and ownership per environment

## Purpose

Design a test data strategy that defines fixtures, factories, cleanup, and ownership per environment.

## When to use

Use when the user wants a shared approach to creating and maintaining test data.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Inventory the entities each test suite needs and mark them required or optional.
2. Choose factories for generated data and fixed fixtures for reference data.
3. Define who creates, refreshes, and deletes each record in every environment.
4. Document the seeded credentials and the reset command the suite depends on.

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
- `test-a-migration-on-a-copy-of-production-data`
- `build-a-test-fixture-that-does-not-leak-state`
