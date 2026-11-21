---
name: migrate-a-warehouse-to-a-new-platform
description: Move warehouse workloads to a new platform by mapping schemas, validating output and cutting over safely. Use when the user wants an existing warehouse and its workloads moved to another platform.
domain: data-engineering
tags: [warehouse-migration, platform-migration, cutover]
triggers: ["migrate warehouse to new platform", "move warehouse workloads", "warehouse cutover plan"]
---

# Move warehouse workloads to a new platform by mapping schemas, validating output and cutting over safely

## Purpose

Move warehouse workloads to a new platform by mapping schemas, validating output and cutting over safely.

## When to use

Use when the user wants an existing warehouse and its workloads moved to another platform.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Inventory the schemas, views, jobs and service accounts in scope.
2. Translate dialect-specific SQL and confirm the target types match the source.
3. Copy historical data and compare row counts and checksums for every table.
4. Back up the source and dry-run the cutover against a shadow copy first.
5. Switch consumers in stages while keeping the old platform readable for rollback.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `migrate-a-pipeline-to-a-new-engine`
- `expose-a-stream-to-warehouse-sync`
- `implement-idempotent-writes-to-a-warehouse`
