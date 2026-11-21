---
name: run-a-compliance-gap-assessment
description: Map a compliance obligation to the current control and record the gap with a dated action. Use when the user wants to find where a standard is not yet met.
domain: security
tags: [compliance, gap-analysis, control]
triggers: ["run a compliance gap assessment", "map a standard to the current controls", "find where compliance is not met"]
---

# Map a compliance obligation to the current control and record the gap with a dated action

## Purpose

Map a compliance obligation to the current control and record the gap with a dated action.

## When to use

Use when the user wants to find where a standard is not yet met.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Extract the obligation list from the standard and number each item.
2. Link each item to the control that satisfies it and to its current evidence.
3. Mark each item as met, partial, not met or not applicable with a reason.
4. Open an action for every gap with an owner and a target date.
5. Summarise the count of gaps by severity for the review meeting.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `run-a-security-awareness-session`
- `add-security-headers-to-a-web-app`
- `build-a-vulnerability-management-program`
