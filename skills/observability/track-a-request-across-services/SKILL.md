---
name: track-a-request-across-services
description: Track one request across service boundaries with propagated identifiers and shared timestamps. Use when the user needs to follow a specific request through downstream services.
domain: observability
tags: [request-tracking, correlation-id, distributed-tracing]
triggers: ["track a request across services", "follow one request through services", "propagate a request identifier"]
---

# Track one request across service boundaries with propagated identifiers and shared timestamps

## Purpose

Track one request across service boundaries with propagated identifiers and shared timestamps.

## When to use

Use when the user needs to follow a specific request through downstream services.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Capture the request entry point and its unique request identifier.
2. Propagate the identifier through every outgoing request header.
3. Record a timestamp at each service entry and exit point.
4. Search each service for the identifier and assemble the hop sequence.
5. Flag the first hop where latency or status changes unexpectedly.

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
- `add-structured-request-logging`
