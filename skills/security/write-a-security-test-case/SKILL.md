---
name: write-a-security-test-case
description: Write a focused security test that proves a control blocks an abusive request safely. Use when the user wants a repeatable test for a specific security control or vulnerability.
domain: security
tags: [security-testing, regression-tests, abuse-cases]
triggers: ["write a security test case", "add a regression test for a vulnerability", "prove a security control with a test"]
---

# Write a focused security test that proves a control blocks an abusive request safely

## Purpose

Write a focused security test that proves a control blocks an abusive request safely.

## When to use

Use when the user wants a repeatable test for a specific security control or vulnerability.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Define the attacker capability, trust boundary, and expected denial in a test note.
2. Select a harmless payload that exercises the vulnerable path without causing damage.
3. Set up the minimum authorised test fixture and reset it after the test.
4. Assert the rejection response and verify that no protected state changed.
5. Run the test against the patched and unpatched behaviour to confirm it detects the gap.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `write-a-security-architecture-review`
- `add-security-headers-to-a-web-app`
- `design-a-privilege-escalation-test`
