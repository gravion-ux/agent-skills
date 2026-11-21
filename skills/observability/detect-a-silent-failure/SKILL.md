---
name: detect-a-silent-failure
description: Detect a silent failure by checking expected side effects instead of relying on error counts. Use when the user needs to find a failure that logs no errors but loses work.
domain: observability
tags: [silent-failure, data-integrity, reconciliation]
triggers: ["detect a silent failure", "check for missing side effects", "catch failures with no errors"]
---

# Detect a silent failure by checking expected side effects instead of relying on error counts

## Purpose

Detect a silent failure by checking expected side effects instead of relying on error counts.

## When to use

Use when the user needs to find a failure that logs no errors but loses work.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Name the expected side effect that proves the workflow completed.
2. Count successful invocations that produced no side effect.
3. Compare the side-effect count with the attempt count on a schedule.
4. Page the owner only when the gap exceeds an agreed tolerance.
5. Preserve a sample of incomplete records for root-cause analysis.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `create-a-log-search-for-a-failure`
- `add-a-health-and-readiness-probe`
- `add-a-synthetic-check-for-a-critical-path`
