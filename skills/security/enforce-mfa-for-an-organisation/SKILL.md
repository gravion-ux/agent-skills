---
name: enforce-mfa-for-an-organisation
description: Require multi-factor authentication for every account, phased in by risk group. Use when the user wants to roll out mandatory second factors across an organisation.
domain: security
tags: [mfa, identity, policy]
triggers: ["enforce mfa for an organisation", "require multi factor authentication everywhere", "roll out two factor authentication"]
---

# Require multi-factor authentication for every account, phased in by risk group

## Purpose

Require multi-factor authentication for every account, phased in by risk group.

## When to use

Use when the user wants to roll out mandatory second factors across an organisation.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Inventory the accounts and rank them by the access they hold.
2. Start the rollout with admin, finance and developer accounts.
3. Choose the factor methods that work for the shift patterns and remote staff.
4. Set the grace period and the recovery path for locked-out users.
5. Measure enrolment coverage and escalate the accounts that remain unprotected.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `enforce-authorisation-on-an-api`
- `sign-an-artifact-for-provenance`
- `add-input-validation-to-an-endpoint`
