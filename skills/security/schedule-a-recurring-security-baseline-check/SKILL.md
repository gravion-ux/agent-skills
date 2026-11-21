---
name: schedule-a-recurring-security-baseline-check
description: Set up a recurring security baseline check that fails on drift and records the result. Use when the user wants configuration drift against the security baseline detected on a schedule.
domain: security
tags: [baseline, drift, scheduling]
triggers: ["set up a recurring security baseline check", "fail a security baseline on drift", "run a periodic security configuration review"]
---

# Set up a recurring security baseline check that fails on drift and records the result

## Purpose

Set up a recurring security baseline check that fails on drift and records the result.

## When to use

Use when the user wants configuration drift against the security baseline detected on a schedule.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Export the approved baseline configuration for every host and account in scope.
2. Write a check that compares the live configuration against that export.
3. Run the check on a schedule and publish the drift list to the owning team.
4. Raise a ticket for each drift item with the expected and observed values.
5. Keep a dated record of every run so the review shows the trend.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `add-security-headers-to-a-web-app`
- `configure-a-cloud-firewall-baseline`
- `prepare-for-a-security-questionnaire`
