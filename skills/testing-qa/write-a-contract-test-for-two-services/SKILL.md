---
name: write-a-contract-test-for-two-services
description: Write a contract test that pins the request and response shape shared by two services. Use when the user wants two services checked against an agreed interface.
domain: testing-qa
tags: [contract-testing, service-interface, schema]
triggers: ["contract test for two services", "test a service consumer contract", "pin an api schema between services"]
---

# Write a contract test that pins the request and response shape shared by two services

## Purpose

Write a contract test that pins the request and response shape shared by two services.

## When to use

Use when the user wants two services checked against an agreed interface.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Locate the schema or document that defines the shared interface.
2. Write a consumer-side test that sends the smallest valid request.
3. Assert the producer response fields and types match the schema.
4. Run the consumer test against each candidate producer implementation.

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
- `write-a-test-for-an-error-path`
- `write-a-test-plan-for-a-release`
