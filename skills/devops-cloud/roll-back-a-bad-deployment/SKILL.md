---
name: roll-back-a-bad-deployment
description: Restore the last known-good version quickly and prove the service is healthy again. Use when the user needs to roll back a deployment that broke the service.
domain: devops-cloud
tags: [rollback, incident, recovery]
triggers: ["roll back a bad deployment", "undo a release that broke production", "deployment rollback"]
---

# Restore the last known-good version quickly and prove the service is healthy again

## Purpose

Restore the last known-good version quickly and prove the service is healthy again.

## When to use

Use when the user needs to roll back a deployment that broke the service.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Confirm the regression is real and name the version to roll back to.
2. Stop the rollout so no further traffic reaches the bad version.
3. Shift traffic and configuration back to the last known-good artefact.
4. Run the health checks and the smoke suite against the restored version.
5. Record the failure, the rollback time and the follow-up action.

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
- `design-a-blue-green-deployment`
- `gate-a-deployment-on-quality-checks`
