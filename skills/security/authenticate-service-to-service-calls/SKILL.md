---
name: authenticate-service-to-service-calls
description: Authenticate service-to-service calls with scoped identities and verified caller identity. Use when the user needs one backend service to call another with a trusted identity.
domain: security
tags: [service-identity, workload-credentials, mTLS]
triggers: ["authenticate service to service calls", "secure internal api calls with workload identity", "verify a calling service identity"]
---

# Authenticate service-to-service calls with scoped identities and verified caller identity

## Purpose

Authenticate service-to-service calls with scoped identities and verified caller identity.

## When to use

Use when the user needs one backend service to call another with a trusted identity.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Define the calling service identity, audience, and minimal scopes for the target service.
2. Issue the workload a short-lived signed credential from the approved identity provider.
3. Validate the credential signature, issuer, audience, expiry, and required scopes at the receiver.
4. Propagate the verified identity into audit records without accepting caller-supplied headers.
5. Test expired, wrong-audience, missing-scope, and valid credentials against the receiver.

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
- `add-security-headers-to-a-web-app`
- `audit-access-to-sensitive-data`
