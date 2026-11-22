---
name: write-a-network-policy
description: Write a Kubernetes network policy that limits which pods may talk to each other. Use when the user wants to restrict pod-to-pod traffic inside a Kubernetes namespace.
domain: security
tags: [network-policy, kubernetes, segmentation]
triggers: ["write a kubernetes network policy", "restrict pod to pod traffic", "limit namespace egress with a policy"]
---

# Write a Kubernetes network policy that limits which pods may talk to each other

## Purpose

Write a Kubernetes network policy that limits which pods may talk to each other.

## When to use

Use when the user wants to restrict pod-to-pod traffic inside a Kubernetes namespace.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. List the allowed connections by source pod, destination pod and port.
2. Write one ingress policy and one egress policy for the namespace.
3. Add an explicit deny-all policy as the default for any direction not allowed.
4. Apply the policies and confirm the expected connections still succeed.
5. Record the allowed flow list beside the policy for later review.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `write-a-security-architecture-review`
- `write-a-security-test-case`
- `write-a-vulnerability-report`
