---
name: build-an-offline-feature-pipeline
description: Build an offline feature pipeline that reconstructs point-in-time training rows from stored events. Use when the user needs historical training data with features computed as of each label time.
domain: data-engineering
tags: [feature-engineering, backfill, training-data]
triggers: ["offline feature pipeline", "build point-in-time training data", "backfill historical features"]
---

# Build an offline feature pipeline that reconstructs point-in-time training rows from stored events

## Purpose

Build an offline feature pipeline that reconstructs point-in-time training rows from stored events.

## When to use

Use when the user needs historical training data with features computed as of each label time.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Define each feature with its event window, source table and aggregation rule.
2. Join features to labels using an event time earlier than the label timestamp.
3. Enforce the point-in-time join so no future event leaks into a training row.
4. Backfill historical partitions and record the source watermark per partition.
5. Compare row counts and feature distributions against a hand-checked sample.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `design-an-ingestion-pipeline`
- `build-a-batch-ingestion-job`
- `build-a-metric-definition`
