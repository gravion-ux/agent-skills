---
name: measure-tail-latency-not-just-averages
description: Measure tail latency with percentiles, exemplars, and enough samples to reveal rare slowness. Use when the user needs to find slow requests hidden by average latency metrics.
domain: observability
tags: [latency, percentiles, histogram]
triggers: ["measure tail latency not averages", "p99 latency analysis", "find slow request tail"]
---

# Measure tail latency with percentiles, exemplars, and enough samples to reveal rare slowness

## Purpose

Measure tail latency with percentiles, exemplars, and enough samples to reveal rare slowness.

## When to use

Use when the user needs to find slow requests hidden by average latency metrics.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Collect latency as a histogram rather than a pre-aggregated average.
2. Choose percentiles such as p95 and p99 for the user-facing journeys.
3. Compare segment latency by route, region, payload size, and dependency.
4. Attach exemplars that link each slow bucket to a trace identifier.
5. Confirm the sample volume covers enough requests to trust the tail.

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
- `measure-a-background-job-success-rate`
- `add-a-health-and-readiness-probe`
