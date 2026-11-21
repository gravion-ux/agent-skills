---
name: design-a-semantic-layer
description: Design a semantic layer that exposes approved metrics and dimensions behind one consistent query interface. Use when the user wants analysts and applications to query governed metrics through a single layer.
domain: data-engineering
tags: [semantic-layer, metrics, data-contracts]
triggers: ["semantic layer design", "build a semantic layer", "expose governed metrics api"]
---

# Design a semantic layer that exposes approved metrics and dimensions behind one consistent query interface

## Purpose

Design a semantic layer that exposes approved metrics and dimensions behind one consistent query interface.

## When to use

Use when the user wants analysts and applications to query governed metrics through a single layer.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Choose the entities, joins and grain the semantic model exposes.
2. Map each published metric to its single approved definition and source.
3. Define access rules, time grains and currency handling for each entity.
4. Implement the layer against warehouse views or a read replica.
5. Publish the interface contract and one example query per consumer type.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `build-a-raw-to-curated-data-layer`
- `design-a-real-time-aggregation`
- `design-a-slowly-changing-dimension`
