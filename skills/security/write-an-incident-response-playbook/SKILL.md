---
name: write-an-incident-response-playbook
description: Write an incident-response playbook with decision points, containment actions, and recovery checks. Use when the user needs a repeatable response plan for a specific security incident type.
domain: security
tags: [incident-response, playbook, recovery]
triggers: ["write an incident response playbook", "prepare a security incident runbook", "plan containment and recovery for a breach"]
---

# Write an incident-response playbook with decision points, containment actions, and recovery checks

## Purpose

Write an incident-response playbook with decision points, containment actions, and recovery checks.

## When to use

Use when the user needs a repeatable response plan for a specific security incident type.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Define the incident scope, severity triggers, named roles, and the authorised containment actions.
2. Document the detection signal, evidence to preserve, and safe ways to share sensitive incident data.
3. Map the triage, containment, eradication, recovery, and notification phases to concrete steps.
4. Add verification checks for each containment and recovery action, including credential rotation.
5. Exercise the playbook in a tabletop scenario and record owners, gaps, and revision dates.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `add-input-validation-to-an-endpoint`
- `enforce-authorisation-on-an-api`
- `enforce-mfa-for-an-organisation`
