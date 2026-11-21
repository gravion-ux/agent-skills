---
name: version-a-dataset
description: Version a dataset with immutable snapshots so consumers can pin and reproduce a past result. Use when the user wants each dataset release to be identifiable and reproducible.
domain: data-engineering
tags: [data-versioning, snapshotting, reproducibility]
triggers: ["version a dataset", "immutable dataset snapshot", "pin dataset release version"]
---

# Version a dataset with immutable snapshots so consumers can pin and reproduce a past result

## Purpose

Version a dataset with immutable snapshots so consumers can pin and reproduce a past result.

## When to use

Use when the user wants each dataset release to be identifiable and reproducible.

## When NOT to use

Do not use this for exploratory analysis of a small local dataset; use data-analysis instead.

## Inputs required

- The source systems and their schemas
- The freshness, volume and quality targets
- The consumer of the output and its contract

## Procedure

1. Assign a semantic version and record the source snapshot or commit hash.
2. Write snapshots to an immutable path that existing releases never overwrite.
3. Attach the schema hash, row count and freshness timestamp to the version.
4. Publish a manifest listing the version, owner and known changes.
5. Test restoring one earlier version and rerunning its consumer query.

## Output contract

A pipeline or job that produces a documented, quality-checked dataset at the agreed freshness.

## Validation checklist

- [ ] The output matches the agreed schema
- [ ] Freshness and row-count checks pass
- [ ] A rerun is idempotent

## Safety notes

Never rewrite a production table without a backup and a dry run.

## Related skills

- `partition-a-dataset-by-date`
- `publish-a-dataset-to-a-catalog`
- `backfill-a-historical-period`
