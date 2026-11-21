---
name: test-a-background-worker-end-to-end
description: Test a background worker end to end by enqueueing a job and asserting its committed effect. Use when the user wants proof that a queued job completes and writes the right result.
domain: testing-qa
tags: [end-to-end-testing, background-jobs, queue]
triggers: ["test a background worker end to end", "test a queued job processing", "assert a worker job side effect"]
---

# Test a background worker end to end by enqueueing a job and asserting its committed effect

## Purpose

Test a background worker end to end by enqueueing a job and asserting its committed effect.

## When to use

Use when the user wants proof that a queued job completes and writes the right result.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Enqueue one job with a unique correlation id and a deterministic payload.
2. Wait for the worker to pick up the job without polling in a tight loop.
3. Assert the produced record, the side effect, and the final job status.
4. Assert the job ran exactly once by checking for duplicate output records.

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
- `build-a-test-fixture-that-does-not-leak-state`
- `build-a-test-harness-for-multiple-environments`
