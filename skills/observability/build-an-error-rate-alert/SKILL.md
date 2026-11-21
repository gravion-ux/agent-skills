---
name: build-an-error-rate-alert
description: Define an error-rate alert that fires on a sustained symptom instead of isolated failures. Use when the user needs a threshold alert for rising request or job failures.
domain: observability
tags: [alerting, error-rate, thresholds]
triggers: ["build an error rate alert", "alert on rising failures", "request error threshold"]
---

# Define an error-rate alert that fires on a sustained symptom instead of isolated failures

## Purpose

Define an error-rate alert that fires on a sustained symptom instead of isolated failures.

## When to use

Use when the user needs a threshold alert for rising request or job failures.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Choose the failure numerator and the total request denominator.
2. Set a minimum request volume below which the alert stays silent.
3. Select a time window long enough to exclude single-request noise.
4. Choose a threshold that matches a user-visible symptom.
5. Route the alert to the owning team with a runbook link.

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
- `write-an-alert-that-a-human-can-act-on`
- `build-a-capacity-forecast-from-metrics`
