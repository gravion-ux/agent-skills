---
name: correlate-logs-metrics-and-traces
description: Correlate logs, metrics, and traces into one incident timeline for a failing request. Use when the user needs to connect multiple telemetry types for one incident.
domain: observability
tags: [correlation, tracing, incident-analysis]
triggers: ["correlate logs metrics and traces", "join telemetry for an incident", "match a trace to logs and metrics"]
---

# Correlate logs, metrics, and traces into one incident timeline for a failing request

## Purpose

Correlate logs, metrics, and traces into one incident timeline for a failing request.

## When to use

Use when the user needs to connect multiple telemetry types for one incident.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Pick one trace identifier from the affected request path.
2. Pull matching log lines, metric changes, and trace spans for the same window.
3. Order the events by timestamp to build the incident timeline.
4. Mark the first failing span and the metric that changed after it.
5. State the suspected cause and the next diagnostic action.

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
- `build-a-capacity-forecast-from-metrics`
- `instrument-a-code-path-with-metrics`
