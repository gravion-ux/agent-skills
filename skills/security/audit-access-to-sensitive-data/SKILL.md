---
name: audit-access-to-sensitive-data
description: Audit access to sensitive data and produce a traceable record of unusual data exposure. Use when the user wants to review who accessed sensitive records and identify risky behaviour.
domain: security
tags: [access-audit, data-governance, log-analysis]
triggers: ["audit access to sensitive data", "review sensitive record access logs", "detect unusual exports of confidential data"]
---

# Audit access to sensitive data and produce a traceable record of unusual data exposure

## Purpose

Audit access to sensitive data and produce a traceable record of unusual data exposure.

## When to use

Use when the user wants to review who accessed sensitive records and identify risky behaviour.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Define the sensitive data classes, authorised purposes, and expected access patterns.
2. Collect read and export events with actor, resource, purpose, and timestamp from audit logs.
3. Group activity by actor and resource to expose bulk access, unusual hours, and repeated exports.
4. Investigate each anomaly with supporting log evidence without copying protected data values.
5. Deliver a findings report with impact, owner, remediation deadline, and verification evidence.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `redact-sensitive-data-from-logs`
- `add-input-validation-to-an-endpoint`
- `add-security-headers-to-a-web-app`
