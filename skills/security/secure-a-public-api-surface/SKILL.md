---
name: secure-a-public-api-surface
description: Reduce a public API's exposure with strict authentication, narrow scopes and enforced rate limits. Use when the user wants to harden an API that is reachable without a signed agreement.
domain: security
tags: [api, exposure, hardening]
triggers: ["secure a public api surface", "reduce the exposure of a public api", "tighten an unauthenticated api"]
---

# Reduce a public API's exposure with strict authentication, narrow scopes and enforced rate limits

## Purpose

Reduce a public API's exposure with strict authentication, narrow scopes and enforced rate limits.

## When to use

Use when the user wants to harden an API that is reachable without a signed agreement.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Require authentication on every endpoint except the documented public ones.
2. Scope each token to the smallest set of operations the client needs.
3. Enforce rate limits and a payload size ceiling at the edge.
4. Validate the content type and the shape of every request body.
5. Review the endpoint list against the published documentation each quarter.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `rotate-a-compromised-api-key`
- `secure-a-ci-pipeline-with-oidc`
- `add-security-headers-to-a-web-app`
