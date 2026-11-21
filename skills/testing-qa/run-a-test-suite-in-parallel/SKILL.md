---
name: run-a-test-suite-in-parallel
description: Run a test suite in parallel with isolated workers and record the per-worker duration. Use when the user wants a slow serial suite to finish faster in CI.
domain: testing-qa
tags: [parallel-testing, ci-runtime, test-runner]
triggers: ["run a test suite in parallel", "parallelize the test suite", "speed up ci with test workers"]
---

# Run a test suite in parallel with isolated workers and record the per-worker duration

## Purpose

Run a test suite in parallel with isolated workers and record the per-worker duration.

## When to use

Use when the user wants a slow serial suite to finish faster in CI.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Check that each test can run without shared ports, files, or databases.
2. Enable the runner's parallel worker option with a worker count under the core limit.
3. Split the suite by test file to balance the workers evenly.
4. Compare the wall-clock time against the recorded serial baseline.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `run-a-test-of-the-test-suite`
- `review-a-test-suite-for-gap-coverage`
- `run-a-smoke-test-after-a-deploy`
