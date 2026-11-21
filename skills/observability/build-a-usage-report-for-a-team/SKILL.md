---
name: build-a-usage-report-for-a-team
description: Build a team usage report from telemetry with fixed windows, deduplication, and budget notes. Use when the user needs recurring evidence of how a team or feature is being used.
domain: observability
tags: [usage, reporting, analytics]
triggers: ["build a usage report for a team", "weekly product usage report", "telemetry based usage summary"]
---

# Build a team usage report from telemetry with fixed windows, deduplication, and budget notes

## Purpose

Build a team usage report from telemetry with fixed windows, deduplication, and budget notes.

## When to use

Use when the user needs recurring evidence of how a team or feature is being used.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Define the usage event and the entity that should be counted once.
2. Choose the reporting window, comparison baseline, and delivery cadence.
3. Aggregate events in the telemetry platform or a scheduled query.
4. Exclude internal and test traffic from the product counts.
5. Label each metric with its source, definition, and known data gaps.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `add-a-synthetic-check-for-a-critical-path`
- `audit-a-service-for-missing-telemetry`
- `build-a-capacity-forecast-from-metrics`
