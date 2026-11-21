---
name: trace-a-slow-third-party-call
description: Trace a slow third-party call to separate client delay, network delay, and provider delay. Use when the user needs to find where time is lost in an external dependency call.
domain: observability
tags: [third-party, dependency, latency]
triggers: ["trace a slow third party call", "diagnose slow external api", "provider call latency breakdown"]
---

# Trace a slow third-party call to separate client delay, network delay, and provider delay

## Purpose

Trace a slow third-party call to separate client delay, network delay, and provider delay.

## When to use

Use when the user needs to find where time is lost in an external dependency call.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Instrument the outbound call with a span and request identifier.
2. Record DNS, connection, TLS, and response timing where the client exposes them.
3. Compare the call duration with the provider's own latency metrics.
4. Check for retries, connection reuse, and payload size effects.
5. Document the slowest observed phase and the next owner to contact.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `implement-a-distributed-trace`
- `add-a-health-and-readiness-probe`
- `add-a-synthetic-check-for-a-critical-path`
