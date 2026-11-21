---
name: build-a-latency-dashboard
description: Build a latency dashboard that shows percentile distributions by route, version, and dependency. Use when the user needs a shared view of request latency across a service.
domain: observability
tags: [dashboard, latency, percentiles]
triggers: ["build a latency dashboard", "p95 latency dashboard", "percentile latency dashboard"]
---

# Build a latency dashboard that shows percentile distributions by route, version, and dependency

## Purpose

Build a latency dashboard that shows percentile distributions by route, version, and dependency.

## When to use

Use when the user needs a shared view of request latency across a service.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Choose the latency metric and define the routing dimensions for each panel.
2. Plot p50, p95, and p99 latency separately instead of a single average.
3. Split panels by route, release, and downstream dependency where available.
4. Overlay request volume so rare slow routes remain visible.
5. Set panel thresholds from observed baselines rather than defaults.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `build-a-capacity-forecast-from-metrics`
- `build-a-usage-report-for-a-team`
- `add-a-health-and-readiness-probe`
