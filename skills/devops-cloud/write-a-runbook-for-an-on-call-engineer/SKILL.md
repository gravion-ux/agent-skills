---
name: write-a-runbook-for-an-on-call-engineer
description: Write a runbook that lets an on-call engineer act without the original author. Use when the user needs an operational runbook for a service someone else will maintain.
domain: devops-cloud
tags: [runbook, on-call, operations]
triggers: ["write an on call runbook", "runbook for an on call engineer", "operational runbook for a service"]
---

# Write a runbook that lets an on-call engineer act without the original author

## Purpose

Write a runbook that lets an on-call engineer act without the original author.

## When to use

Use when the user needs an operational runbook for a service someone else will maintain.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. List the alerts that page the on-call engineer and the action each one expects.
2. Give the exact command, dashboard and log query for each alert, copied from a real run.
3. State the rollback or mitigation for every action, with the blast radius of each.
4. Add escalation contacts and the point at which to hand over to another team.
5. Test the runbook in a game day and fix every step that was ambiguous.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `write-a-dockerfile-for-a-service`
- `write-infrastructure-as-code-for-a-service`
- `gate-a-deployment-on-quality-checks`
