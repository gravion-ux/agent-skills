---
name: add-a-health-and-readiness-probe
description: Add health and readiness probes that distinguish running processes from able to serve traffic. Use when the user needs platform probes for a deployed service.
domain: observability
tags: [health-check, readiness, kubernetes]
triggers: ["add health and readiness probes", "configure liveness and readiness", "service readiness endpoint"]
---

# Add health and readiness probes that distinguish running processes from able to serve traffic

## Purpose

Add health and readiness probes that distinguish running processes from able to serve traffic.

## When to use

Use when the user needs platform probes for a deployed service.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Define the liveness check for process liveness without external dependencies.
2. Define the readiness check for dependency and capacity availability.
3. Return a non-success status when the service cannot accept work.
4. Keep each probe fast and free of sensitive response details.
5. Verify that failed readiness removes the instance from traffic.

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
- `add-structured-request-logging`
- `audit-a-service-for-missing-telemetry`
