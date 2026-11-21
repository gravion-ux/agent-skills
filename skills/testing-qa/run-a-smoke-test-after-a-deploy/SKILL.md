---
name: run-a-smoke-test-after-a-deploy
description: Run a smoke test after a deploy that checks the critical path once against the new release. Use when the user wants a fast release check that confirms the deployment is alive.
domain: testing-qa
tags: [smoke-test, deployment, release-check]
triggers: ["smoke test after a deploy", "post-deploy smoke check", "run a deploy smoke test"]
---

# Run a smoke test after a deploy that checks the critical path once against the new release

## Purpose

Run a smoke test after a deploy that checks the critical path once against the new release.

## When to use

Use when the user wants a fast release check that confirms the deployment is alive.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. List the three to five critical user paths for the release.
2. Run one script per path against the deployed environment.
3. Assert each response and the key side effect within the timeout.
4. Report pass or fail per path and stop promotion on any failure.

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
- `run-a-test-suite-in-parallel`
- `build-a-data-driven-test-table`
