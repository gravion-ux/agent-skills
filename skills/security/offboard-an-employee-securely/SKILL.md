---
name: offboard-an-employee-securely
description: Remove a departing employee's access while preserving the records needed for review. Use when the user needs to revoke every access path for someone who is leaving.
domain: security
tags: [offboarding, revocation, access]
triggers: ["offboard an employee securely", "revoke access for a departing employee", "remove a leaver from every system"]
---

# Remove a departing employee's access while preserving the records needed for review

## Purpose

Remove a departing employee's access while preserving the records needed for review.

## When to use

Use when the user needs to revoke every access path for someone who is leaving.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. List the accounts, groups, keys, devices and shared vaults the person holds.
2. Revoke the active sessions and rotate any credential the person knew.
3. Transfer the owned repositories, documents and shared drives to a named owner.
4. Preserve the mailbox and the records required by the retention policy.
5. Confirm the access list is empty after the offboarding window closes.

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
