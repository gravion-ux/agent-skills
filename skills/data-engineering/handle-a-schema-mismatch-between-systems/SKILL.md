---
name: handle-a-schema-mismatch-between-systems
description: Reconcile two incompatible schemas by mapping fields, preserving nulls and quarantining bad rows. Use when the user must join or migrate data whose field types or names differ.
domain: data-engineering
tags: [schema-mapping, data-quality, integration]
triggers: ["schema mismatch between systems", "map incompatible source schemas", "fix field type mismatch"]
---

# Reconcile two incompatible schemas by mapping fields, preserving nulls and quarantining bad rows

## Purpose

Reconcile two incompatible schemas by mapping fields, preserving nulls and quarantining bad rows.

## When to use

Use when the user must join or migrate data whose field types or names differ.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Profile both schemas and list the field pairs that carry the same meaning.
2. Write an explicit cast and rename map for every matched field.
3. Send rows that fail validation to a quarantine table with a reason code.
4. Recalculate totals from the mapped fields and reconcile them against the source count.
5. Version the mapping file and rerun the job to confirm idempotent results.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `manage-schema-evolution-in-a-stream`
- `backfill-a-historical-period`
- `build-a-batch-ingestion-job`
