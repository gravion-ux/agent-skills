---
name: design-a-real-time-aggregation
description: Design a real-time aggregation that keeps rolling windows current without overloading the source. Use when the user wants rolling counters updated continuously over event streams.
domain: data-engineering
tags: [real-time-analytics, stream-processing, aggregation]
triggers: ["real time aggregation", "rolling window stream aggregate", "live counters from events"]
---

# Design a real-time aggregation that keeps rolling windows current without overloading the source

## Purpose

Design a real-time aggregation that keeps rolling windows current without overloading the source.

## When to use

Use when the user wants rolling counters updated continuously over event streams.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Name the metric, its window length and the update interval the consumer needs.
2. Choose an incremental aggregate store keyed by window and grouping dimensions.
3. Define the watermark that marks an event late and the correction it triggers.
4. Cap per-event work and batch writes to protect the source and the sink.
5. Compare live totals against a batch recomputation for one completed window.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `design-a-semantic-layer`
- `design-a-slowly-changing-dimension`
- `backfill-a-historical-period`
