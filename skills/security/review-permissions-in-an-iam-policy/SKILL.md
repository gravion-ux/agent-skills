---
name: review-permissions-in-an-iam-policy
description: Review an IAM policy for unsafe actions, resource scope, and missing conditions. Use when the user wants an identity policy checked for excessive permissions before deployment.
domain: security
tags: [iam-policy, policy-review, cloud-security]
triggers: ["review permissions in an iam policy", "audit wildcard permissions in a cloud policy", "find unsafe iam actions and resource scopes"]
---

# Review an IAM policy for unsafe actions, resource scope, and missing conditions

## Purpose

Review an IAM policy for unsafe actions, resource scope, and missing conditions.

## When to use

Use when the user wants an identity policy checked for excessive permissions before deployment.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Parse each statement into actions, resources, conditions, and the identities that inherit it.
2. Map high-impact actions to their data and infrastructure impact and flag wildcard scopes.
3. Confirm each action and resource is justified by a documented workload requirement.
4. Add explicit deny, resource scoping, or conditions where the review finds excess access.
5. Simulate the revised policy against required and forbidden actions and record the evidence.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `add-input-validation-to-an-endpoint`
- `detect-secret-leaks-in-ci`
- `enforce-authorisation-on-an-api`
