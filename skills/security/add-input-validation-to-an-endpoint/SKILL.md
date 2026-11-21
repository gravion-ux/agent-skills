---
name: add-input-validation-to-an-endpoint
description: Add layered input validation to an endpoint before untrusted data reaches business logic. Use when the user wants an API endpoint to reject malformed or out-of-range input.
domain: security
tags: [input-validation, api-security, schema-validation]
triggers: ["add input validation to an endpoint", "validate api request parameters", "reject malformed endpoint input"]
---

# Add layered input validation to an endpoint before untrusted data reaches business logic

## Purpose

Add layered input validation to an endpoint before untrusted data reaches business logic.

## When to use

Use when the user wants an API endpoint to reject malformed or out-of-range input.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Document the endpoint's expected types, lengths, ranges, and allowed values.
2. Apply schema validation at the request boundary and return a structured error response.
3. Reject unknown fields and normalise accepted values before invoking business logic.
4. Add tests for valid input, each invalid class, and oversized payloads.
5. Verify that validation runs before database, queue, and downstream service calls.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `add-security-headers-to-a-web-app`
- `audit-access-to-sensitive-data`
- `authenticate-service-to-service-calls`
