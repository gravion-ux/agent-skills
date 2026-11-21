---
name: secure-a-ci-pipeline-with-oidc
description: Replace a long-lived pipeline credential with a short-lived OIDC federation token. Use when the user wants the build system to reach cloud resources without a stored access key.
domain: security
tags: [oidc, ci, identity]
triggers: ["secure a ci pipeline with oidc", "use workload identity federation in ci", "remove static cloud keys from a pipeline"]
---

# Replace a long-lived pipeline credential with a short-lived OIDC federation token

## Purpose

Replace a long-lived pipeline credential with a short-lived OIDC federation token.

## When to use

Use when the user wants the build system to reach cloud resources without a stored access key.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Create a workload identity mapping between the pipeline account and the cloud role.
2. Add the issuer, audience and subject claims to the trust policy.
3. Remove the static credential from the pipeline secret store.
4. Run the pipeline and confirm the exchange returns a short-lived session.
5. Record the trust relationship and its expiry in the access review.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `protect-a-service-with-a-rate-limit`
- `protect-secrets-in-a-cicd-pipeline`
- `secure-a-public-api-surface`
