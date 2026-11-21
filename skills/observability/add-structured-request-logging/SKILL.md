---
name: add-structured-request-logging
description: Add structured request logs with stable fields, correlation identifiers, and secret-safe redaction. Use when the user needs searchable logs for incoming service requests.
domain: observability
tags: [logging, structured-logs, redaction]
triggers: ["add structured request logging", "structured logs for requests", "log requests as json"]
---

# Add structured request logs with stable fields, correlation identifiers, and secret-safe redaction

## Purpose

Add structured request logs with stable fields, correlation identifiers, and secret-safe redaction.

## When to use

Use when the user needs searchable logs for incoming service requests.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Define a JSON schema for request fields, duration, outcome, and route.
2. Emit one structured event per completed request.
3. Add the trace or request identifier to every event.
4. Redact authorization headers, tokens, and personal fields before writing.
5. Search the new fields to confirm one request is easy to isolate.

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
- `track-a-request-across-services`
