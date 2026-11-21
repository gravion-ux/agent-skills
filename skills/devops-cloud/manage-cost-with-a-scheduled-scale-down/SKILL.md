---
name: manage-cost-with-a-scheduled-scale-down
description: Schedule off-hours scaling down and restore capacity at opening time with explicit cost limits. Use when the user wants predictable infrastructure savings without risking service availability.
domain: devops-cloud
tags: [cost-optimization, scheduling, auto-scaling, capacity]
triggers: ["schedule a cloud scale down", "off hours capacity cost saving", "automated scale up schedule"]
---

# Schedule off-hours scaling down and restore capacity at opening time with explicit cost limits

## Purpose

Schedule off-hours scaling down and restore capacity at opening time with explicit cost limits.

## When to use

Use when the user wants predictable infrastructure savings without risking service availability.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Capture the minimum capacity needed for expected off-hours load and the budget ceiling.
2. Define the scale-down time, scale-up time, and grace period for scheduled actions.
3. Verify the schedule respects maintenance windows and compliance controls.
4. Test a manual scale event and confirm alarms and dashboards remain visible.
5. Document the expected monthly saving and the owner of the schedule.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `apply-a-cost-budget-to-cloud-resources`
- `automate-a-release-with-a-pull-request`
- `manage-a-service-on-a-managed-cloud-platform`
