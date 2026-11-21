---
name: add-a-synthetic-check-for-a-critical-path
description: Add a synthetic check that exercises a critical user path and reports its own failure. Use when the user needs continuous proof that a critical journey still works.
domain: observability
tags: [synthetic-monitoring, availability, automation]
triggers: ["add a synthetic check for a critical path", "synthetic critical path monitor", "automated journey health check"]
---

# Add a synthetic check that exercises a critical user path and reports its own failure

## Purpose

Add a synthetic check that exercises a critical user path and reports its own failure.

## When to use

Use when the user needs continuous proof that a critical journey still works.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Choose the critical journey and its smallest safe transaction.
2. Run the check from a location that resembles real user traffic.
3. Assert the expected response, side effect, and completion time.
4. Schedule the check more often than the tolerance for missed runs.
5. Route a failed synthetic check to the owning team with captured diagnostics.

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
- `audit-a-service-for-missing-telemetry`
- `build-a-usage-report-for-a-team`
