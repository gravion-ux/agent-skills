---
name: mock-an-external-dependency
description: Mock an external dependency with a controlled stub so tests never call the real service. Use when the user wants to test code that calls a third-party service without network access.
domain: testing-qa
tags: [mocking, stubbing, test-doubles]
triggers: ["mock an external dependency", "stub a third-party service", "replace api call with a mock"]
---

# Mock an external dependency with a controlled stub so tests never call the real service

## Purpose

Mock an external dependency with a controlled stub so tests never call the real service.

## When to use

Use when the user wants to test code that calls a third-party service without network access.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Identify the narrow interface the code calls on the external service.
2. Write a stub that returns one known response for that interface.
3. Inject the stub at the call boundary instead of patching the network.
4. Assert the stub received the expected arguments and returned the canned result.

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
- `write-an-integration-test-for-an-api`
- `assert-on-behaviour-not-implementation`
