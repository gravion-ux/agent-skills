---
name: report-on-the-reliability-of-a-dependency
description: Report dependency reliability using success rate, latency distribution, and attributed failures. Use when the user needs a current reliability assessment for an upstream or downstream service.
domain: observability
tags: [dependency, reliability, reporting]
triggers: ["report on dependency reliability", "upstream service reliability report", "assess external service uptime"]
---

# Report dependency reliability using success rate, latency distribution, and attributed failures

## Purpose

Report dependency reliability using success rate, latency distribution, and attributed failures.

## When to use

Use when the user needs a current reliability assessment for an upstream or downstream service.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Define the dependency's critical operations and the request population.
2. Measure success rate and latency percentiles over a stated window.
3. Separate provider failures from local errors and client cancellations.
4. List the incidents or deploys that align with the reliability changes.
5. Summarize the current level and the residual risk to dependent services.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `build-a-usage-report-for-a-team`
- `write-an-alert-that-a-human-can-act-on`
- `add-a-health-and-readiness-probe`
