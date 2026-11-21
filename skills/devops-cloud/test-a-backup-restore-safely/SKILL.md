---
name: test-a-backup-restore-safely
description: Test a backup restore in an isolated sandbox without touching production data or access. Use when the user wants proof that backups restore cleanly without risking the live environment.
domain: devops-cloud
tags: [restore-test, sandbox, data-integrity, recovery]
triggers: ["test a backup restore safely", "sandbox restore rehearsal", "prove backup recoverability"]
---

# Test a backup restore in an isolated sandbox without touching production data or access

## Purpose

Test a backup restore in an isolated sandbox without touching production data or access.

## When to use

Use when the user wants proof that backups restore cleanly without risking the live environment.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Copy the backup artefact into an isolated sandbox account with restricted network access.
2. Restore the copy using the same tooling and parameters used in production.
3. Apply schema migrations only after the restored data passes integrity checks.
4. Run application smoke tests against the restored sandbox instance.
5. Destroy the sandbox and retain the restore test evidence.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `back-up-and-restore-a-cloud-data-store`
- `configure-a-load-test-environment`
- `apply-a-cost-budget-to-cloud-resources`
