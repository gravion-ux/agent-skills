---
name: write-a-property-based-invariant-test
description: Write a property-based test that generates inputs and asserts an invariant for every case. Use when the user wants broad input coverage without hand-writing every case.
domain: testing-qa
tags: [property-based-testing, invariants, generated-inputs]
triggers: ["property based invariant test", "property based testing example", "assert an invariant over generated inputs"]
---

# Write a property-based test that generates inputs and asserts an invariant for every case

## Purpose

Write a property-based test that generates inputs and asserts an invariant for every case.

## When to use

Use when the user wants broad input coverage without hand-writing every case.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. State the invariant that must hold for every valid input.
2. Choose a generator that produces both valid and boundary inputs.
3. Assert the invariant against each generated case, including shrunk failures.
4. Record the failing seed and shrunk example in the failure output.

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
- `write-a-load-test-scenario`
