---
name: create-a-log-search-for-a-failure
description: Build a saved log search that isolates one failure mode using fields, time range, and filters. Use when the user needs to find request failures in a log service.
domain: observability
tags: [logs, log-search, debugging]
triggers: ["create a log search for a failure", "search logs for errors", "saved failure log query"]
---

# Build a saved log search that isolates one failure mode using fields, time range, and filters

## Purpose

Build a saved log search that isolates one failure mode using fields, time range, and filters.

## When to use

Use when the user needs to find request failures in a log service.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. State the failure signature and the service affected.
2. Filter on the error code, route, status class, or structured field.
3. Bound the search by a narrow time window and environment.
4. Exclude known successful requests to reduce noise.
5. Save the query with a descriptive name and share the result link.

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
- `audit-a-service-for-missing-telemetry`
- `build-a-usage-report-for-a-team`
