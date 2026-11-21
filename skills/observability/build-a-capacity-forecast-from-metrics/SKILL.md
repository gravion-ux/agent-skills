---
name: build-a-capacity-forecast-from-metrics
description: Forecast capacity from historical usage, growth, and headroom against a stated ceiling. Use when the user needs to estimate future resource needs from observed telemetry.
domain: observability
tags: [capacity, forecasting, metrics]
triggers: ["build a capacity forecast from metrics", "forecast resource usage", "project capacity from telemetry"]
---

# Forecast capacity from historical usage, growth, and headroom against a stated ceiling

## Purpose

Forecast capacity from historical usage, growth, and headroom against a stated ceiling.

## When to use

Use when the user needs to estimate future resource needs from observed telemetry.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Collect historical usage for the constrained resource and its key dimensions.
2. Separate seasonal patterns from sustained growth in the trend.
3. Choose a forecast horizon and state the assumptions behind the projection.
4. Apply a headroom target before comparing demand with the capacity ceiling.
5. Flag the date and utilisation level that would trigger a scaling decision.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `build-a-latency-dashboard`
- `build-a-usage-report-for-a-team`
- `instrument-a-code-path-with-metrics`
