---
name: write-a-service-level-objective
description: Write a measurable service level objective with a target, window, and accountable owner. Use when the user needs to set a reliability target for a service or API.
domain: observability
tags: [slo, reliability, error-budget]
triggers: ["write a service level objective", "set an slo target", "service reliability objective"]
---

# Write a measurable service level objective with a target, window, and accountable owner

## Purpose

Write a measurable service level objective with a target, window, and accountable owner.

## When to use

Use when the user needs to set a reliability target for a service or API.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Select the service level indicator that best represents user experience.
2. Choose a target percentage and a rolling measurement window.
3. Define the error budget as the allowed share of bad events.
4. Name the team that owns the objective and reviews its breaches.
5. Set a date to revisit the target against measured reliability.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `audit-a-service-for-missing-telemetry`
- `define-service-level-indicators`
- `write-an-alert-that-a-human-can-act-on`
