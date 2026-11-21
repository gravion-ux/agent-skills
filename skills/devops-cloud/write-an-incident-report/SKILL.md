---
name: write-an-incident-report
description: Write a blameless incident report with timeline, contributing factors, and verified corrective actions. Use when the user wants a clear incident review document after an outage or degradation.
domain: devops-cloud
tags: [incident-report, postmortem, timeline, corrective-action]
triggers: ["write an incident report", "blameless postmortem for an outage", "incident review document"]
---

# Write a blameless incident report with timeline, contributing factors, and verified corrective actions

## Purpose

Write a blameless incident report with timeline, contributing factors, and verified corrective actions.

## When to use

Use when the user wants a clear incident review document after an outage or degradation.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Build the timeline from alert, deploy, and chat timestamps in one timeline view.
2. State the customer impact in requests, users, and duration.
3. List contributing conditions without assigning individual blame.
4. Assign each corrective action an owner, due date, and verification signal.
5. Attach the final timeline and link the evidence used for every claim.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `write-a-runbook-for-an-on-call-engineer`
- `scan-an-image-for-vulnerabilities`
- `triage-an-alert-fire`
