---
name: verify-a-backup-can-be-restored
description: Verify a backup by restoring it into a disposable environment and comparing row counts and checksums. Use when the user wants proof that a stored backup is actually restorable.
domain: testing-qa
tags: [backup-restore, disaster-recovery, data-integrity]
triggers: ["verify a backup can be restored", "test restore from a backup", "backup restore drill"]
---

# Verify a backup by restoring it into a disposable environment and comparing row counts and checksums

## Purpose

Verify a backup by restoring it into a disposable environment and comparing row counts and checksums.

## When to use

Use when the user wants proof that a stored backup is actually restorable.

## When NOT to use

Do not use this for production monitoring after release; use observability instead.

## Inputs required

- The behaviour under test and its acceptance criteria
- The risk areas and the environments available
- The level of coverage the team needs

## Procedure

1. Pick the most recent backup and record its identifier and creation time.
2. Restore it into a disposable environment that holds no production data.
3. Compare row counts and checksums against the source for the key tables.
4. Document the restore duration and delete the disposable copy afterwards.

## Output contract

Automated tests that fail for the right reason and a report of what remains unverified.

## Validation checklist

- [ ] The test fails when the behaviour is broken
- [ ] Flaky tests are quarantined, not retried
- [ ] The suite runs in a documented order

## Safety notes

Never weaken an assertion to make a suite green, and never delete a failing test to unblock a release.

## Related skills

- `verify-accessibility-in-a-test`
- `automate-a-visual-regression-check`
- `build-a-data-driven-test-table`
