---
name: design-a-privilege-escalation-test
description: Design an authorised privilege-escalation test that proves role boundaries hold. Use when the user wants to test whether a low-privilege account can reach higher privileges.
domain: security
tags: [privilege-escalation, security-testing, authorised-testing]
triggers: ["design a privilege escalation test", "test vertical privilege boundaries safely", "prove role escalation is blocked"]
---

# Design an authorised privilege-escalation test that proves role boundaries hold

## Purpose

Design an authorised privilege-escalation test that proves role boundaries hold.

## When to use

Use when the user wants to test whether a low-privilege account can reach higher privileges.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Document the authorised test accounts, target privilege, and explicit stopping conditions.
2. Map every privilege boundary and define the expected denial for each attempted transition.
3. Prepare a harmless high-privilege marker or action that cannot alter production data.
4. Execute the test from the low-privilege identity and capture request and audit evidence.
5. Report the escalation path, impact, concrete fix, and a regression test for the boundary.

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
- `scope-a-penetration-test`
- `write-a-security-test-case`
