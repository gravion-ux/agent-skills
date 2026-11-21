---
name: measure-a-background-job-success-rate
description: Measure background job success by counting terminal outcomes against attempted runs. Use when the user needs a reliable success rate for scheduled or asynchronous jobs.
domain: observability
tags: [jobs, success-rate, batch]
triggers: ["measure background job success rate", "job completion percentage", "scheduled job failure rate"]
---

# Measure background job success by counting terminal outcomes against attempted runs

## Purpose

Measure background job success by counting terminal outcomes against attempted runs.

## When to use

Use when the user needs a reliable success rate for scheduled or asynchronous jobs.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Define an attempt and the terminal outcomes that count as success.
2. Count attempts and successes with one stable job identifier.
3. Separate retried attempts from distinct jobs in the rate.
4. Record the measurement window and the reporting lag.
5. Compare the rate with the expected volume for the same window.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `add-a-health-and-readiness-probe`
- `add-a-synthetic-check-for-a-critical-path`
- `audit-a-service-for-missing-telemetry`
