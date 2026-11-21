---
name: design-an-enterprise-wide-naming-convention
description: Define an enterprise naming convention for layers, tables and columns with enforceable validation. Use when the user wants consistent layer, table and column names across teams.
domain: data-engineering
tags: [naming-convention, data-standards, metadata]
triggers: ["enterprise naming convention", "standardize table column names", "data naming lint rules"]
---

# Define an enterprise naming convention for layers, tables and columns with enforceable validation

## Purpose

Define an enterprise naming convention for layers, tables and columns with enforceable validation.

## When to use

Use when the user wants consistent layer, table and column names across teams.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. List the platform layers and assign each one a short prefix.
2. Specify subject, entity, grain and optional partition suffix for table names.
3. Define column naming for identifiers, measures, timestamps and flags.
4. Publish the pattern with allowed separators, casing and reserved terms.
5. Add a linting rule that fails naming violations in the CI pipeline.

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
- `build-an-offline-feature-pipeline`
- `design-a-real-time-aggregation`
