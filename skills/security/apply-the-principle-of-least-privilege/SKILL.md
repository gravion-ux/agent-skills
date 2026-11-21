---
name: apply-the-principle-of-least-privilege
description: Reduce identity permissions to the minimum needed for each task and verify the result. Use when the user wants service, user, or role permissions narrowed to justified access.
domain: security
tags: [least-privilege, iam, access-review]
triggers: ["apply the principle of least privilege", "reduce service permissions to minimum access", "tighten role scopes and permissions"]
---

# Reduce identity permissions to the minimum needed for each task and verify the result

## Purpose

Reduce identity permissions to the minimum needed for each task and verify the result.

## When to use

Use when the user wants service, user, or role permissions narrowed to justified access.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Inventory the actions each identity performs and link each action to a documented requirement.
2. Remove permissions without a requirement and replace broad roles with task-specific roles.
3. Set resource scopes, conditions, and expiry dates on every retained permission.
4. Test the reduced permissions against required tasks and representative denied tasks.
5. Record the justification, owner, review date, and rollback path for the final role set.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `apply-data-classification-labels`
- `design-a-privilege-escalation-test`
- `add-input-validation-to-an-endpoint`
