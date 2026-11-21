---
name: instrument-a-queue-consumer
description: Instrument a queue consumer with throughput, lag, retry, and processing-duration signals. Use when the user needs visibility into message consumption and backlog health.
domain: observability
tags: [queues, consumer, lag]
triggers: ["instrument a queue consumer", "monitor queue lag", "consumer throughput metrics"]
---

# Instrument a queue consumer with throughput, lag, retry, and processing-duration signals

## Purpose

Instrument a queue consumer with throughput, lag, retry, and processing-duration signals.

## When to use

Use when the user needs visibility into message consumption and backlog health.

## When NOT to use

Do not use this for a local profiling session with no production signal; use testing-qa instead.

## Inputs required

- The service and the signals it emits
- The question the team needs answered
- The volume, retention and cost ceiling

## Procedure

1. Record processed, failed, retried, and dead-lettered message counts.
2. Track current queue depth and the age of the oldest pending message.
3. Measure processing duration per message as a histogram.
4. Add the queue, consumer group, and message class as bounded labels.
5. Confirm the consumer emits signals during idle and busy periods.

## Output contract

Logs, metrics and traces that answer the stated question, plus the dashboards or alerts that use them.

## Validation checklist

- [ ] The signals carry no secrets or personal data
- [ ] Alert thresholds match a real symptom
- [ ] Cardinality and volume stay within budget

## Safety notes

Never log credentials, tokens or raw personal data in a metric label or log line.

## Related skills

- `instrument-a-code-path-with-metrics`
- `add-a-health-and-readiness-probe`
- `add-a-synthetic-check-for-a-critical-path`
