---
name: write-an-integration-test-for-an-api
description: Write an integration test for an API that exercises a real request against a disposable server. Use when the user wants an API request tested end to end against a running service.
domain: testing-qa
tags: [integration-test, api, end-to-end]
triggers: ["integration test for an api", "test an api endpoint", "api integration test request"]
---

# Write an integration test for an API that exercises a real request against a disposable server

## Purpose

Write an integration test for an API that exercises a real request against a disposable server.

## When to use

Use when the user wants an API request tested end to end against a running service.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Start the service under test on a disposable port with its own database.
2. Send one request that exercises the acceptance criteria for the endpoint.
3. Assert the status code, response fields, and persisted side effect.
4. Tear the service and database down in a fixture that runs after each test.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `write-a-test-for-an-error-path`
- `write-a-canary-test-for-a-risk-area`
- `write-a-contract-test-for-two-services`
