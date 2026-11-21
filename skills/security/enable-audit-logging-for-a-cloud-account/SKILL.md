---
name: enable-audit-logging-for-a-cloud-account
description: Turn on audit logging for a cloud account and confirm the trail reaches a durable destination. Use when the user wants proof that administrative actions are recorded for later investigation.
domain: security
tags: [audit-log, cloud, logging]
triggers: ["enable cloud audit logging", "turn on an organisation activity trail", "send cloud audit logs to a log store"]
---

# Turn on audit logging for a cloud account and confirm the trail reaches a durable destination

## Purpose

Turn on audit logging for a cloud account and confirm the trail reaches a durable destination.

## When to use

Use when the user wants proof that administrative actions are recorded for later investigation.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Enable the organisation trail or the account activity log for every region in use.
2. Route the log to a storage account outside the region being monitored.
3. Write a lifecycle rule that keeps the trail for the required retention period.
4. Trigger a test action and confirm the event appears in the log destination.
5. Record the log identifier and the retention setting in the security baseline.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `configure-a-cloud-firewall-baseline`
- `investigate-a-cloud-access-anomaly`
- `prepare-for-a-security-questionnaire`
