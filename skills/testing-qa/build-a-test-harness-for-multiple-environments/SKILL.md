---
name: build-a-test-harness-for-multiple-environments
description: Build a test harness that runs the same suite across local, CI, and staging environments. Use when the user wants one test suite to run unchanged in several environments.
domain: testing-qa
tags: [test-harness, environment-config, portability]
triggers: ["test harness for multiple environments", "run the same test suite in several environments", "parameterise tests by environment"]
---

# Build a test harness that runs the same suite across local, CI, and staging environments

## Purpose

Build a test harness that runs the same suite across local, CI, and staging environments.

## When to use

Use when the user wants one test suite to run unchanged in several environments.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Define an environment configuration object for each target environment.
2. Move URLs, credentials, and timeouts into that configuration.
3. Load the selected configuration from one environment variable before the run.
4. Run the suite locally and in CI and compare the reported environment name.

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
- `review-a-test-suite-for-gap-coverage`
