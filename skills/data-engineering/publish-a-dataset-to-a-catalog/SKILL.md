---
name: publish-a-dataset-to-a-catalog
description: Publish a dataset to a catalog with ownership, schema, quality results and usage notes attached. Use when the user wants a production dataset discoverable in the enterprise data catalog.
domain: data-engineering
tags: [data-catalog, documentation, metadata]
triggers: ["publish dataset to catalog", "register dataset metadata", "catalog documentation for dataset"]
---

# Publish a dataset to a catalog with ownership, schema, quality results and usage notes attached

## Purpose

Publish a dataset to a catalog with ownership, schema, quality results and usage notes attached.

## When to use

Use when the user wants a production dataset discoverable in the enterprise data catalog.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Register the dataset with its owner, steward and business purpose.
2. Attach the current schema with field descriptions and sensitivity labels.
3. Record the freshness target, row count and timestamp of the last successful load.
4. Link the runbook and the downstream consumer list to the catalog entry.
5. Run the catalog scanner and confirm no missing owner or schema warnings.

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
- `expose-a-stream-to-warehouse-sync`
- `implement-idempotent-writes-to-a-warehouse`
