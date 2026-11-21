---
name: retire-a-noisy-alert
description: Retire a noisy alert after confirming its signal, owner, and replacement coverage. Use when the user needs to remove an alert that fires too often to be useful.
domain: observability
tags: [alerting, alert-fatigue, cleanup]
triggers: ["retire a noisy alert", "remove an overly frequent alert", "clean up alert noise"]
---

# Retire a noisy alert after confirming its signal, owner, and replacement coverage

## Purpose

Retire a noisy alert after confirming its signal, owner, and replacement coverage.

## When to use

Use when the user needs to remove an alert that fires too often to be useful.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Measure the alert's firing count and false-positive rate over a defined window.
2. Confirm the underlying symptom is covered by a better alert or dashboard.
3. Agree the replacement signal, owner, and severity with the on-call team.
4. Disable the old alert and record the retirement in the alert catalogue.
5. Watch for one full monitoring period and confirm no coverage was lost.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `set-up-a-dead-letter-alert`
- `write-an-alert-that-a-human-can-act-on`
- `add-a-health-and-readiness-probe`
