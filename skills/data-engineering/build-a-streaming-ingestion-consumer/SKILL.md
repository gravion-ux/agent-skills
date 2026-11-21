---
name: build-a-streaming-ingestion-consumer
description: Build a streaming consumer that writes incoming events to storage as they arrive. Use when the user wants to consume a live event stream into a data store.
domain: data-engineering
tags: [streaming, consumer, events]
triggers: ["streaming ingestion consumer", "consume an event stream into storage", "build a live event consumer"]
---

# Build a streaming consumer that writes incoming events to storage as they arrive

## Purpose

Build a streaming consumer that writes incoming events to storage as they arrive.

## When to use

Use when the user wants to consume a live event stream into a data store.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Fix the offset or checkpoint strategy so the consumer can resume safely.
2. Reject events that fail the schema check into a quarantine topic.
3. Write accepted events to the target store in small idempotent batches.
4. Commit the offset only after the batch write is acknowledged.
5. Expose the consumer lag for every partition it reads.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `build-a-batch-ingestion-job`
- `build-a-metric-definition`
- `build-a-raw-to-curated-data-layer`
