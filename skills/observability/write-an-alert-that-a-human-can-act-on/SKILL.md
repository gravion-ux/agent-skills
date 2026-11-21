---
name: write-an-alert-that-a-human-can-act-on
description: Turn an alert into a specific, owned action with context, severity, and a tested response. Use when the user needs to reduce alert fatigue and make notifications actionable.
domain: observability
tags: [alerting, runbooks, on-call]
triggers: ["write an actionable alert", "alert with a runbook", "make alerts easier to act on"]
---

# Turn an alert into a specific, owned action with context, severity, and a tested response

## Purpose

Turn an alert into a specific, owned action with context, severity, and a tested response.

## When to use

Use when the user needs to reduce alert fatigue and make notifications actionable.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Name the user-visible symptom that the alert detects.
2. Attach the current metric values, affected service, and recent change.
3. Assign severity, owner, and a direct route to the responsible team.
4. Link one runbook with a concrete first diagnostic command.
5. Test the notification with the owning team before enabling it.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `write-an-slo-burn-rate-alert`
- `build-an-error-rate-alert`
- `plan-an-on-call-dashboard`
