---
name: write-an-slo-burn-rate-alert
description: Write a burn-rate alert that fires when the error budget is consumed faster than planned. Use when the user needs an alert tied to service level objective consumption.
domain: observability
tags: [slo, burn-rate, alerting]
triggers: ["write an slo burn rate alert", "error budget burn alert", "notify on fast slo burn"]
---

# Write a burn-rate alert that fires when the error budget is consumed faster than planned

## Purpose

Write a burn-rate alert that fires when the error budget is consumed faster than planned.

## When to use

Use when the user needs an alert tied to service level objective consumption.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Calculate the error budget remaining from the objective and its window.
2. Choose short and long evaluation windows for fast and slow burns.
3. Set burn-rate thresholds that match the team's response urgency.
4. Require a minimum event volume before notifying the on-call engineer.
5. Document which runbook and escalation path each threshold triggers.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `build-an-error-rate-alert`
- `write-an-alert-that-a-human-can-act-on`
- `measure-a-background-job-success-rate`
