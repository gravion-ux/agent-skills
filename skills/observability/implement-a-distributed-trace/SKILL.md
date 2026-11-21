---
name: implement-a-distributed-trace
description: Instrument a request path with distributed tracing so latency and failures map across service boundaries. Use when the user needs to follow a request across multiple services.
domain: observability
tags: [tracing, distributed-tracing, latency]
triggers: ["implement distributed tracing", "trace a request across services", "add spans to a service"]
---

# Instrument a request path with distributed tracing so latency and failures map across service boundaries

## Purpose

Instrument a request path with distributed tracing so latency and failures map across service boundaries.

## When to use

Use when the user needs to follow a request across multiple services.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Choose the trace identifier and propagate it in request headers.
2. Create a span at each client call, queue publish, and service boundary.
3. Record the span name, operation, outcome, and duration as attributes.
4. Attach the trace identifier to logs emitted inside each span.
5. Verify one synthetic request produces a connected trace across every hop.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `trace-a-slow-third-party-call`
- `add-a-health-and-readiness-probe`
- `add-a-synthetic-check-for-a-critical-path`
