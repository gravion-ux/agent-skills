---
name: write-a-canary-test-for-a-risk-area
description: Write a canary test that exercises the riskiest changed path before wider release traffic. Use when the user wants a narrow check on the riskiest part of a release.
domain: testing-qa
tags: [canary-testing, risk-based-testing, release-safety]
triggers: ["canary test for a risk area", "canary check on a risky path", "shadow traffic test"]
---

# Write a canary test that exercises the riskiest changed path before wider release traffic

## Purpose

Write a canary test that exercises the riskiest changed path before wider release traffic.

## When to use

Use when the user wants a narrow check on the riskiest part of a release.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Identify the changed path with the highest blast radius or weakest coverage.
2. Define the expected behaviour for that path under normal traffic.
3. Run the canary against a small percentage of real or shadow traffic.
4. Compare canary error and latency rates with the baseline before widening.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `write-a-contract-test-for-two-services`
- `write-a-test-for-an-error-path`
- `write-a-test-plan-for-a-release`
