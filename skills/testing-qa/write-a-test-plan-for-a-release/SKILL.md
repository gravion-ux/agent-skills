---
name: write-a-test-plan-for-a-release
description: Write a release test plan that lists scope, environments, checks, owners, and the abort criteria. Use when the user needs a shared plan for verifying one release before launch.
domain: testing-qa
tags: [test-plan, release, quality-planning]
triggers: ["write a test plan for a release", "plan testing before a launch", "release verification plan"]
---

# Write a release test plan that lists scope, environments, checks, owners, and the abort criteria

## Purpose

Write a release test plan that lists scope, environments, checks, owners, and the abort criteria.

## When to use

Use when the user needs a shared plan for verifying one release before launch.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. State the release scope and the acceptance criteria that decide a pass.
2. Map each criterion to an automated test or a manual check with an owner.
3. List the environments, data, and timing for each phase of the plan.
4. Define the abort condition that stops the release and the escalation path.

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
- `write-a-test-for-an-error-path`
