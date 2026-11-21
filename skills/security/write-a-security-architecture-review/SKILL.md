---
name: write-a-security-architecture-review
description: Review a design for security gaps and record each gap with the control that would close it. Use when the user wants a design checked for security before it is built.
domain: security
tags: [architecture-review, design, threats]
triggers: ["write a security architecture review", "review a design for security gaps", "check a system design for security"]
---

# Review a design for security gaps and record each gap with the control that would close it

## Purpose

Review a design for security gaps and record each gap with the control that would close it.

## When to use

Use when the user wants a design checked for security before it is built.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Read the design and list the assets, entry points and trust boundaries in it.
2. Walk each trust boundary and name the authentication and authorisation decision there.
3. Check the data at rest and in transit against the classification it holds.
4. Record each gap with the control that closes it and the design change it needs.
5. Write the review outcome as approved, approved with changes or rework required.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `write-a-security-test-case`
- `add-security-headers-to-a-web-app`
- `prepare-for-a-security-questionnaire`
