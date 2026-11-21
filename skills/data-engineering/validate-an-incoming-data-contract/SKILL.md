---
name: validate-an-incoming-data-contract
description: Validate an incoming dataset against its declared contract before it is loaded. Use when the user wants to check that incoming data matches an agreed contract.
domain: data-engineering
tags: [contract, validation, schema]
triggers: ["validate an incoming data contract", "check incoming data against schema", "enforce a data contract on ingest"]
---

# Validate an incoming dataset against its declared contract before it is loaded

## Purpose

Validate an incoming dataset against its declared contract before it is loaded.

## When to use

Use when the user wants to check that incoming data matches an agreed contract.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Read the declared schema, field types, nullability and allowed ranges.
2. Check every column for type mismatches and unexpected nulls.
3. Verify the row count and the business key uniqueness in the incoming batch.
4. Reject the batch with a precise error when any mandatory check fails.
5. Publish the contract check result so the producer can see what broke.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `automate-data-quality-checks`
- `build-a-raw-to-curated-data-layer`
- `build-an-offline-feature-pipeline`
