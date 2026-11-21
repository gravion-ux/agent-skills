---
name: plan-a-penetration-test
description: Plan an authorised penetration test with explicit scope, safety limits, and evidence criteria. Use when the user wants a security testing engagement scoped for safe authorised execution.
domain: security
tags: [penetration-testing, authorisation, test-planning]
triggers: ["plan a penetration test", "scope an authorised security engagement", "prepare rules of engagement for red team testing"]
---

# Plan an authorised penetration test with explicit scope, safety limits, and evidence criteria

## Purpose

Plan an authorised penetration test with explicit scope, safety limits, and evidence criteria.

## When to use

Use when the user wants a security testing engagement scoped for safe authorised execution.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Record the written authorisation, systems in scope, test window, and prohibited actions.
2. Define the attacker profile, threat model, target objectives, and out-of-scope assets.
3. Establish stop conditions, emergency contacts, evidence handling, and data-protection rules.
4. Select test types and deliverables with explicit pass and failure criteria for each control.
5. Review the plan with system owners and the client before any test traffic is generated.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `scope-a-penetration-test`
- `design-a-privilege-escalation-test`
- `write-a-security-test-case`
