---
name: measure-test-suite-duration
description: Measure test suite duration per test file to find the slowest cases and the bottleneck. Use when the user wants data on which tests make the suite slow.
domain: testing-qa
tags: [test-metrics, duration-profiling, performance]
triggers: ["measure test suite duration", "find the slowest tests", "profile test runtime"]
---

# Measure test suite duration per test file to find the slowest cases and the bottleneck

## Purpose

Measure test suite duration per test file to find the slowest cases and the bottleneck.

## When to use

Use when the user wants data on which tests make the suite slow.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Run the suite once with per-test timing enabled and save the raw output.
2. Rank the slowest test files and tests by total duration.
3. Group the slow tests by cause such as sleeps, IO, or setup.
4. Record a baseline duration and the top ten contributors in the report.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `review-a-test-suite-for-gap-coverage`
- `run-a-test-of-the-test-suite`
- `run-a-test-suite-in-parallel`
