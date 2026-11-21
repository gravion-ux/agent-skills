---
name: audit-a-service-for-missing-telemetry
description: Audit a service for blind spots and map each gap to a concrete signal to add. Use when the user needs to find missing observability coverage in an existing service.
domain: observability
tags: [audit, telemetry, coverage]
triggers: ["audit a service for missing telemetry", "find observability gaps", "telemetry coverage review"]
---

# Audit a service for blind spots and map each gap to a concrete signal to add

## Purpose

Audit a service for blind spots and map each gap to a concrete signal to add.

## When to use

Use when the user needs to find missing observability coverage in an existing service.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. List the service's critical user journeys and background workflows.
2. Map each journey to its current logs, metrics, and traces.
3. Mark missing signals for latency, errors, saturation, and outcomes.
4. Check whether any existing label or field can explode cardinality.
5. Rank the gaps by diagnostic value and record an owner for each fix.

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
- `build-a-usage-report-for-a-team`
- `create-a-log-search-for-a-failure`
