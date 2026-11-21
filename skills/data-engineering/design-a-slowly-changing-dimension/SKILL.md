---
name: design-a-slowly-changing-dimension
description: Design a slowly changing dimension that keeps history without exploding row counts. Use when the user wants to track attribute changes over time in a dimension table.
domain: data-engineering
tags: [dimension, history, modelling]
triggers: ["design a slowly changing dimension", "track dimension attribute history", "implement a type two dimension"]
---

# Design a slowly changing dimension that keeps history without exploding row counts

## Purpose

Design a slowly changing dimension that keeps history without exploding row counts.

## When to use

Use when the user wants to track attribute changes over time in a dimension table.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Decide which attributes need history and which should always reflect the current value.
2. Choose the type, either a type two version row or a type one overwrite.
3. Define the effective-from and effective-to columns that bracket each version.
4. Set the current flag so queries can find the active version efficiently.
5. Document how a late-arriving change should backdate the affected version.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `design-a-real-time-aggregation`
- `design-a-semantic-layer`
- `backfill-a-historical-period`
