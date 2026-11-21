---
name: triage-an-alert-fire
description: Separate urgent alerts from noise, identify the common trigger, and route each response to an owner. Use when the user receives a burst of monitoring alerts and must decide what needs action.
domain: devops-cloud
tags: [alert-triage, incident-triage, monitoring, on-call]
triggers: ["triage an alert fire", "group and route monitoring alerts", "alert storm triage"]
---

# Separate urgent alerts from noise, identify the common trigger, and route each response to an owner

## Purpose

Separate urgent alerts from noise, identify the common trigger, and route each response to an owner.

## When to use

Use when the user receives a burst of monitoring alerts and must decide what needs action.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Group alerts by service, region, and failure signature within the last fifteen minutes.
2. Check whether a deployment, scaling event, or dependency change aligns with the burst.
3. Assign each actionable alert an owner and a severity using the on-call matrix.
4. Suppress duplicate alerts with a linked grouping rule and expiry time.
5. Publish the triage summary with the first hypothesis and the next check.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `scan-an-image-for-vulnerabilities`
- `write-a-runbook-for-an-on-call-engineer`
- `write-an-incident-report`
