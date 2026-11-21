---
name: write-a-data-retention-policy
description: Write a database retention policy with legal, operational, and deletion safeguards. Use when the user needs to define how long database data must be kept and removed.
domain: databases
tags: [retention-policy, data-governance, deletion]
triggers: ["write a data retention policy", "database retention schedule", "define data deletion policy"]
---

# Write a database retention policy with legal, operational, and deletion safeguards

## Purpose

Write a database retention policy with legal, operational, and deletion safeguards.

## When to use

Use when the user needs to define how long database data must be kept and removed.

## When NOT to use

Do not use this for query tuning on a warehouse at scale; use data-engineering instead.

## Inputs required

- The engine and its version
- The schema, data volume and access pattern
- The maintenance window and the recovery target

## Procedure

1. Classify data by purpose, sensitivity, and applicable retention requirements.
2. Set retention periods and deletion owners for each data class.
3. Choose archive, anonymize, or purge actions for expired records.
4. Define approval, audit, exception, and backup-expiry controls.
5. Test the policy against representative records before rollout.

## Output contract

A safe migration or tuning change with a measured before-and-after result.

## Validation checklist

- [ ] The change runs on a copy of production data first
- [ ] The rollback or rollback-to-a-known-point path is proven
- [ ] Locking and write amplification were measured

## Safety notes

Never run a destructive DDL statement against production without a confirmed backup.

## Related skills

- `seed-a-database-with-test-data`
- `write-a-safe-backfill-script`
- `write-a-sql-query-with-a-clear-plan`
