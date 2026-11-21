---
name: instrument-a-code-path-with-metrics
description: Add counters, histograms, and gauges to a code path without unbounded metric labels. Use when the user needs visibility into how often and how slowly a code path runs.
domain: observability
tags: [metrics, instrumentation, cardinality]
triggers: ["instrument a code path with metrics", "add metrics to a handler", "counter and histogram instrumentation"]
---

# Add counters, histograms, and gauges to a code path without unbounded metric labels

## Purpose

Add counters, histograms, and gauges to a code path without unbounded metric labels.

## When to use

Use when the user needs visibility into how often and how slowly a code path runs.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Map the code path to the counters, histograms, and gauges it needs.
2. Define each metric name, unit, and permitted label set.
3. Emit metrics at the outcome point rather than on every request.
4. Reject labels such as user identifiers, URLs, or raw error text.
5. Compare metric volume and label cardinality against the budget.

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
- `build-a-capacity-forecast-from-metrics`
- `instrument-a-queue-consumer`
