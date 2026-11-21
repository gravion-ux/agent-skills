---
name: review-privileged-access-requests
description: Review a privileged access request against the justification, the scope and the expiry. Use when the user must decide whether to grant temporary elevated access.
domain: security
tags: [access-review, privilege, approval]
triggers: ["review a privileged access request", "approve temporary elevated access", "decide on a standing admin request"]
---

# Review a privileged access request against the justification, the scope and the expiry

## Purpose

Review a privileged access request against the justification, the scope and the expiry.

## When to use

Use when the user must decide whether to grant temporary elevated access.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Read the business justification and name the work that needs the access.
2. Check the requested roles against the minimum needed for that work.
3. Confirm the requester holds the approval a policy requires for that scope.
4. Set an expiry that matches the length of the task.
5. Record the decision, the scope granted and the review date.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `audit-access-to-sensitive-data`
- `investigate-a-cloud-access-anomaly`
- `review-code-for-injection-risks`
