---
name: expose-a-stream-to-warehouse-sync
description: Stream source events into a warehouse table with ordering, deduplication and lag monitoring. Use when the user wants events from a broker or api landed continuously in the warehouse.
domain: data-engineering
tags: [streaming-ingest, change-data-capture, warehouse-sync]
triggers: ["stream to warehouse sync", "land kafka events in warehouse", "continuous ingest from source"]
---

# Stream source events into a warehouse table with ordering, deduplication and lag monitoring

## Purpose

Stream source events into a warehouse table with ordering, deduplication and lag monitoring.

## When to use

Use when the user wants events from a broker or api landed continuously in the warehouse.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Capture the source offset, event time and ingestion timestamp for each record.
2. Deduplicate on the source event id and keep the latest arrival per key.
3. Write partitions by ingestion day and drop partitions past the retention window.
4. Replay a fixed window after restart and compare replayed counts with source counts.
5. Alert when consumer lag exceeds the freshness target for two intervals.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `implement-idempotent-writes-to-a-warehouse`
- `migrate-a-warehouse-to-a-new-platform`
- `build-a-raw-to-curated-data-layer`
