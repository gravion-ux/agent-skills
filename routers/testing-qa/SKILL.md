---
name: router-testing-qa
description: Route work in the Testing and quality assurance domain to the right leaf skill. Use when a task clearly belongs to testing-qa.
domain: testing-qa
tags: [router, routing, testing-qa]
triggers: ["route a testing-qa task", "which testing-qa skill should I use"]
---

# Testing and quality assurance router

## Purpose

List every leaf skill in the testing-qa domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside testing-qa and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `assert-on-behaviour-not-implementation` | Use when the user wants to stop a test from breaking on harmless internal changes. |
| `automate-a-visual-regression-check` | Use when the user wants interface changes caught automatically after a build. |
| `build-a-data-driven-test-table` | Use when the user has many similar cases and wants one readable test body. |
| `build-a-test-fixture-that-does-not-leak-state` | Use when the user sees order-dependent failures or dirty state between tests. |
| `build-a-test-harness-for-multiple-environments` | Use when the user wants one test suite to run unchanged in several environments. |
| `design-a-test-data-strategy` | Use when the user wants a shared approach to creating and maintaining test data. |
| `detect-and-fix-a-flaky-test` | Use when the user sees a test that passes and fails on the same unchanged code. |
| `measure-test-suite-duration` | Use when the user wants data on which tests make the suite slow. |
| `mock-an-external-dependency` | Use when the user wants to test code that calls a third-party service without network access. |
| `name-tests-so-failures-explain-themselves` | Use when the user wants readable failure output from a large test suite. |
| `quarantine-a-flaky-test-with-a-ticket` | Use when the user needs to unblock a suite while a flaky test is investigated. |
| `review-a-test-suite-for-gap-coverage` | Use when the user wants a risk-ranked list of untested behaviour in an existing suite. |
| `run-a-smoke-test-after-a-deploy` | Use when the user wants a fast release check that confirms the deployment is alive. |
| `run-a-test-of-the-test-suite` | Use when the user wants evidence that the test suite actually catches defects. |
| `run-a-test-suite-in-parallel` | Use when the user wants a slow serial suite to finish faster in CI. |
| `set-up-a-test-coverage-gate` | Use when the user wants coverage measured and enforced in continuous integration. |
| `test-a-background-worker-end-to-end` | Use when the user wants proof that a queued job completes and writes the right result. |
| `test-a-feature-flagged-code-path` | Use when the user wants proof that both sides of a feature flag behave correctly. |
| `test-a-migration-on-a-copy-of-production-data` | Use when the user wants confidence that a schema migration works on real-world data. |
| `test-a-timezone-sensitive-feature` | Use when the user has scheduling or display logic that depends on local time. |
| `test-the-happy-path-and-the-edges` | Use when the user wants one behaviour covered from the normal case to its limits. |
| `use-a-test-double-for-slow-io` | Use when the user has tests that take too long because of slow network or disk access. |
| `verify-a-backup-can-be-restored` | Use when the user wants proof that a stored backup is actually restorable. |
| `verify-accessibility-in-a-test` | Use when the user wants accessibility regressions caught in the automated suite. |
| `write-a-canary-test-for-a-risk-area` | Use when the user wants a narrow check on the riskiest part of a release. |
| `write-a-contract-test-for-two-services` | Use when the user wants two services checked against an agreed interface. |
| `write-a-load-test-scenario` | Use when the user wants to prove a service holds its stated throughput. |
| `write-a-property-based-invariant-test` | Use when the user wants broad input coverage without hand-writing every case. |
| `write-a-regression-test-that-fails-first` | Use when the user wants a test that locks in a recently fixed defect. |
| `write-a-replay-test-from-a-production-log` | Use when the user wants a real production incident captured as a repeatable test. |
| `write-a-test-for-an-error-path` | Use when the user wants the failure branch of a function covered and verified. |
| `write-a-test-plan-for-a-release` | Use when the user needs a shared plan for verifying one release before launch. |
| `write-a-unit-test-for-a-pure-function` | Use when the user wants a fast unit test for a function with no side effects. |
| `write-an-integration-test-for-an-api` | Use when the user wants an API request tested end to end against a running service. |
