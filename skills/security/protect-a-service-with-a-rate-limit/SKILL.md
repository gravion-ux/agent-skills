---
name: protect-a-service-with-a-rate-limit
description: Protect a service with a distributed rate limit keyed to abuse-prone request dimensions. Use when the user wants an endpoint or service shielded from excessive or abusive request volume.
domain: security
tags: [rate-limiting, abuse-prevention, service-protection]
triggers: ["protect a service with a rate limit", "throttle abusive api traffic", "add distributed request limiting"]
---

# Protect a service with a distributed rate limit keyed to abuse-prone request dimensions

## Purpose

Protect a service with a distributed rate limit keyed to abuse-prone request dimensions.

## When to use

Use when the user wants an endpoint or service shielded from excessive or abusive request volume.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Choose the protected routes and a limit justified by legitimate peak traffic and capacity.
2. Select a stable key such as account, tenant, or trusted client identifier for each limiter.
3. Apply the limit at the shared gateway or store using an atomic counter across replicas.
4. Return a consistent retry response and emit metrics for allowed, throttled, and bypassed traffic.
5. Load-test the limiter and verify that distributed replicas enforce the same aggregate threshold.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `protect-secrets-in-a-cicd-pipeline`
- `secure-a-ci-pipeline-with-oidc`
- `add-security-headers-to-a-web-app`
