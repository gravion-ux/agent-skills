---
name: quarantine-a-flaky-test-with-a-ticket
description: Quarantine a flaky test behind a tracking ticket and an expiry date instead of retrying it. Use when the user needs to unblock a suite while a flaky test is investigated.
domain: testing-qa
tags: [quarantine, flaky-test, ticket-tracking]
triggers: ["quarantine a flaky test with a ticket", "skip a flaky test and track it", "move flaky test to quarantine"]
---

# Quarantine a flaky test behind a tracking ticket and an expiry date instead of retrying it

## Purpose

Quarantine a flaky test behind a tracking ticket and an expiry date instead of retrying it.

## When to use

Use when the user needs to unblock a suite while a flaky test is investigated.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Confirm the test fails intermittently on unchanged code before quarantining it.
2. Move the test into a quarantined group that the default suite skips.
3. Open a ticket that names the failure, the owner, and a revisit date.
4. Fail the build when the quarantine passes its expiry date without a fix.

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
- `build-a-data-driven-test-table`
- `build-a-test-fixture-that-does-not-leak-state`
