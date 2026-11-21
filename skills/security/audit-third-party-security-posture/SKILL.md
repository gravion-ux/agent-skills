---
name: audit-third-party-security-posture
description: Assess a vendor's security posture with evidence and record the gaps you accept. Use when the user wants to review the controls a supplier applies to your data.
domain: security
tags: [vendor, audit, assessment]
triggers: ["audit third party security posture", "review a supplier's security controls", "assess vendor security evidence"]
---

# Assess a vendor's security posture with evidence and record the gaps you accept

## Purpose

Assess a vendor's security posture with evidence and record the gaps you accept.

## When to use

Use when the user wants to review the controls a supplier applies to your data.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. List the data the supplier holds and the access it needs to do its work.
2. Request the current assurance artefacts and note their expiry dates.
3. Test a sample of the controls against your own acceptance criteria.
4. Record each gap, its severity and the contractual remedy available.
5. Set the review date and the signal that would trigger an early re-assessment.

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
- `enable-audit-logging-for-a-cloud-account`
