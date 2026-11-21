---
name: use-property-based-testing-for-edge-cases
description: Use property-based tests to explore edge cases and shrink any counterexample into a concrete regression. Use when the user wants broader edge-case coverage than example-only tests.
domain: software-engineering
tags: [property-testing, edge-cases, generators]
triggers: ["property test edge cases", "generate and shrink counterexamples"]
---

# Use property-based tests to explore edge cases and shrink any counterexample into a concrete regression

## Purpose

Use property-based tests to explore edge cases and shrink any counterexample into a concrete regression.

## When to use

Use when the user wants broader edge-case coverage than example-only tests.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Define the invariants that must hold for every valid input.
2. Build generators for representative and boundary inputs.
3. Run generated cases with a recorded random seed.
4. Shrink and retain any failing counterexample as a regression.
5. Confirm the property fails before the relevant fix.
6. Run existing tests and document the covered invariants.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `configure-formatting-and-linting-for-a-repo`
- `prepare-a-pull-request-for-review`
- `prepare-code-for-a-code-freeze`
