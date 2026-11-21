---
name: verify-a-third-party-library-integration
description: Verify a third-party library integration through version, security, failure-handling, and compatibility checks. Use when the user wants to validate a new or upgraded external library dependency.
domain: software-engineering
tags: [dependencies, integration-testing, supply-chain]
triggers: ["verify a third party integration", "validate an external library dependency"]
---

# Verify a third-party library integration through version, security, failure-handling, and compatibility checks

## Purpose

Verify a third-party library integration through version, security, failure-handling, and compatibility checks.

## When to use

Use when the user wants to validate a new or upgraded external library dependency.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Confirm the supported version, API contract, and license.
2. Pin the dependency and run a minimal integration test.
3. Check authentication, network failure, and timeout handling.
4. Run the repository suite against the pinned dependency.
5. Document known incompatibilities and upgrade limits.
6. Record rationale, monitoring needs, and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `raise-useful-errors-from-a-library`
- `support-a-library-consumer`
- `add-structured-logging-to-a-code-path`
