---
name: define-service-level-indicators
description: Choose service level indicators that measure user-visible outcomes rather than internal activity. Use when the user needs to define measurable reliability indicators for a service.
domain: observability
tags: [sli, reliability, service-level]
triggers: ["define service level indicators", "select user-visible reliability indicators", "choose service level indicator set"]
---

# Choose service level indicators that measure user-visible outcomes rather than internal activity

## Purpose

Choose service level indicators that measure user-visible outcomes rather than internal activity.

## When to use

Use when the user needs to define measurable reliability indicators for a service.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. List the user journeys that the service must keep working.
2. Group each journey into a successful outcome and a failed outcome.
3. Define the numerator, denominator, and observation window for each indicator.
4. Reject indicators that track deployment or host activity instead of user outcomes.
5. Record a baseline value and owner for every accepted indicator.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `write-a-service-level-objective`
- `audit-a-service-for-missing-telemetry`
- `add-a-health-and-readiness-probe`
