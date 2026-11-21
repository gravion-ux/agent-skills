---
name: write-a-load-test-scenario
description: Write a load test scenario with a target rate, a latency threshold, and a duration. Use when the user wants to prove a service holds its stated throughput.
domain: testing-qa
tags: [load-testing, performance-testing, throughput]
triggers: ["write a load test scenario", "load test a service endpoint", "test throughput and latency"]
---

# Write a load test scenario with a target rate, a latency threshold, and a duration

## Purpose

Write a load test scenario with a target rate, a latency threshold, and a duration.

## When to use

Use when the user wants to prove a service holds its stated throughput.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Set the target request rate, concurrent users, and duration from the service goals.
2. Define the latency percentile and error-rate thresholds that count as a pass.
3. Exclude warm-up traffic from the reported measurements.
4. Run the scenario in a production-like environment and publish the percentile table.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `write-a-canary-test-for-a-risk-area`
- `write-a-contract-test-for-two-services`
- `write-a-property-based-invariant-test`
