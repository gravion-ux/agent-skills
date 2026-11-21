---
name: test-a-timezone-sensitive-feature
description: Test a timezone-sensitive feature by pinning the clock across named zones and daylight-saving edges. Use when the user has scheduling or display logic that depends on local time.
domain: testing-qa
tags: [timezone-testing, clock-control, edge-cases]
triggers: ["test a timezone sensitive feature", "test across daylight saving", "pin the clock for time tests"]
---

# Test a timezone-sensitive feature by pinning the clock across named zones and daylight-saving edges

## Purpose

Test a timezone-sensitive feature by pinning the clock across named zones and daylight-saving edges.

## When to use

Use when the user has scheduling or display logic that depends on local time.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Pin the clock to a fixed instant and inject it into the code under test.
2. Run the same scenario in two zones with different UTC offsets.
3. Add a case on each daylight-saving transition boundary for the affected zone.
4. Assert the formatted result and the computed offset against the documented rule.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `test-a-feature-flagged-code-path`
- `build-a-data-driven-test-table`
- `build-a-test-fixture-that-does-not-leak-state`
