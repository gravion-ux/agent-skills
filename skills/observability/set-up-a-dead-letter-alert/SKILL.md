---
name: set-up-a-dead-letter-alert
description: Set up a dead-letter queue alert that detects failed messages before they pile up unseen. Use when the user needs visibility into messages routed to a dead-letter queue.
domain: observability
tags: [dead-letter, queue, alerting]
triggers: ["set up a dead letter alert", "alert on dead letter queue growth", "monitor dead letter messages"]
---

# Set up a dead-letter queue alert that detects failed messages before they pile up unseen

## Purpose

Set up a dead-letter queue alert that detects failed messages before they pile up unseen.

## When to use

Use when the user needs visibility into messages routed to a dead-letter queue.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Identify the dead-letter queue and its owning consumer.
2. Create a gauge for current dead-letter depth and a counter for arrivals.
3. Alert when depth grows beyond a threshold or arrivals persist.
4. Attach the message identifier pattern and replay procedure to the alert.
5. Test the alert by injecting one disposable failed message.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `retire-a-noisy-alert`
- `write-an-alert-that-a-human-can-act-on`
- `add-a-health-and-readiness-probe`
