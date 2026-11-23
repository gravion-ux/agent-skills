---
name: enforce-authorisation-on-an-api
description: Enforce resource-level authorisation across API routes with deny-by-default access tests. Use when the user needs API endpoints to enforce per-user and per-resource access.
domain: security
tags: [authorisation, access-control, api-security]
triggers: ["enforce authorisation on an api", "add resource level access checks", "prevent cross-account api access"]
---

# Enforce resource-level authorisation across API routes with deny-by-default access tests

## Purpose

Enforce resource-level authorisation across API routes with deny-by-default access tests.

## When to use

Use when the user needs API endpoints to enforce per-user and per-resource access.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. List each route with the resource it returns and the required access decision.
2. Resolve the authenticated subject and load the resource owner or permitted role.
3. Apply the authorisation decision before reading or mutating the protected resource.
4. Return a uniform not-found or forbidden response without exposing sensitive details.
5. Add tests that cover owner access, denied access, cross-tenant access, and missing identity.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `test-object-level-authorisation-on-an-api`
- `enforce-mfa-for-an-organisation`
- `add-input-validation-to-an-endpoint`
