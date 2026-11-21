---
name: write-a-replay-test-from-a-production-log
description: Write a replay test from a sanitised production log line and assert the same handling outcome. Use when the user wants a real production incident captured as a repeatable test.
domain: testing-qa
tags: [replay-testing, log-fixtures, incident-regression]
triggers: ["replay test from a production log", "turn a production log into a test", "replay a log line in a test"]
---

# Write a replay test from a sanitised production log line and assert the same handling outcome

## Purpose

Write a replay test from a sanitised production log line and assert the same handling outcome.

## When to use

Use when the user wants a real production incident captured as a repeatable test.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Extract one sanitised log entry that triggered the reported behaviour.
2. Feed the entry to the handler as a fixed fixture.
3. Assert the same output, side effect, or error as the production run.
4. Keep the fixture masked so it carries no customer identifiers.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `test-a-migration-on-a-copy-of-production-data`
- `write-a-canary-test-for-a-risk-area`
- `write-a-contract-test-for-two-services`
