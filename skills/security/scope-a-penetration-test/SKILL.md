---
name: scope-a-penetration-test
description: Scope a penetration test by defining the targets, the rules of engagement and the emergency contacts. Use when the user needs to authorise an external security test against named systems.
domain: security
tags: [pentest, scope, authorisation]
triggers: ["scope a penetration test", "write rules of engagement for a security test", "define the bounds of an external pen test"]
---

# Scope a penetration test by defining the targets, the rules of engagement and the emergency contacts

## Purpose

Scope a penetration test by defining the targets, the rules of engagement and the emergency contacts.

## When to use

Use when the user needs to authorise an external security test against named systems.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. List the in-scope domains, applications, IP ranges and accounts.
2. Name the test types that are allowed and the ones that are excluded.
3. Set the testing window, the source addresses and the rate limits.
4. Write the rules for data handling, evidence retention and incident escalation.
5. List the emergency contacts and the stop condition for the test team.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `plan-a-penetration-test`
- `design-a-privilege-escalation-test`
- `write-a-security-test-case`
