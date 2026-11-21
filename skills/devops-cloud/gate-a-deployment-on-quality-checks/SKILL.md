---
name: gate-a-deployment-on-quality-checks
description: Block a deployment until automated tests, scans, and policy checks pass on the release artifact. Use when the user wants a ci pipeline to prevent low-quality builds from reaching production.
domain: devops-cloud
tags: [ci-gate, quality-check, pipeline, deployment]
triggers: ["deployment quality gate", "gate a deploy on checks", "ci quality gate for release"]
---

# Block a deployment until automated tests, scans, and policy checks pass on the release artifact

## Purpose

Block a deployment until automated tests, scans, and policy checks pass on the release artifact.

## When to use

Use when the user wants a ci pipeline to prevent low-quality builds from reaching production.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Run the unit, integration, and smoke tests against the release candidate.
2. Fail the gate on any failing test or severity-high vulnerability scan result.
3. Require signed provenance and an approved change record for the commit.
4. Publish the gate results and the rejected reason to the deployment status.
5. Allow promotion only when every required check reports success.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `design-a-blue-green-deployment`
- `manage-a-service-on-a-managed-cloud-platform`
- `roll-back-a-bad-deployment`
