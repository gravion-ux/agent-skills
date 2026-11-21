---
name: respond-to-a-service-outage
description: Restore a failed cloud service using the prepared rollback path while keeping an incident timeline. Use when the user needs to coordinate recovery from an active production service outage.
domain: devops-cloud
tags: [incident-response, outage, recovery, rollback]
triggers: ["respond to a cloud service outage", "service outage recovery runbook", "restore a failed service"]
---

# Restore a failed cloud service using the prepared rollback path while keeping an incident timeline

## Purpose

Restore a failed cloud service using the prepared rollback path while keeping an incident timeline.

## When to use

Use when the user needs to coordinate recovery from an active production service outage.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Declare the incident, name the incident lead, and open the incident channel.
2. Confirm the blast radius and identify the last known healthy deployment.
3. Execute the documented rollback or failover only after the lead approves it.
4. Verify recovery with health checks and customer-facing error rate.
5. Record each action, timestamp, and result in the incident timeline.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `migrate-a-workload-to-a-managed-service`
- `apply-a-cost-budget-to-cloud-resources`
- `manage-a-service-on-a-managed-cloud-platform`
