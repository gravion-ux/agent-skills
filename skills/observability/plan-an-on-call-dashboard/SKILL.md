---
name: plan-an-on-call-dashboard
description: Plan an on-call dashboard with service health, active incidents, and recent deploy signals. Use when the user needs to prepare the primary dashboard used during on-call shifts.
domain: observability
tags: [on-call, dashboard, incident-response]
triggers: ["plan an on call dashboard", "on call service health view", "primary responder dashboard"]
---

# Plan an on-call dashboard with service health, active incidents, and recent deploy signals

## Purpose

Plan an on-call dashboard with service health, active incidents, and recent deploy signals.

## When to use

Use when the user needs to prepare the primary dashboard used during on-call shifts.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. List the services and dependencies that require first-line awareness.
2. Choose panels for error rate, latency, saturation, and active incidents.
3. Add recent deploy and configuration-change markers for each service.
4. Set the refresh interval and ordering for alert triage.
5. Test the dashboard during a simulated incident and note missing context.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `write-an-alert-that-a-human-can-act-on`
- `build-a-latency-dashboard`
- `build-an-error-rate-alert`
