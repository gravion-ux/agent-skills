---
name: rotate-a-compromised-api-key
description: Rotate a compromised API key while preserving service continuity and audit evidence. Use when the user needs an exposed API key revoked and replaced safely.
domain: security
tags: [api-keys, credential-rotation, incident-response]
triggers: ["rotate a compromised api key", "replace an exposed api credential", "revoke and issue a new api key"]
---

# Rotate a compromised API key while preserving service continuity and audit evidence

## Purpose

Rotate a compromised API key while preserving service continuity and audit evidence.

## When to use

Use when the user needs an exposed API key revoked and replaced safely.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Confirm the exposure in the incident record and identify every service that uses the key.
2. Create a replacement key with the minimum required scope and a clear expiry.
3. Move consumers to the replacement key through a staged configuration rollout.
4. Revoke the compromised key and invalidate any cached copies of its credentials.
5. Verify authenticated traffic under the new key and confirm the old key is rejected.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `secure-a-public-api-surface`
- `add-security-headers-to-a-web-app`
- `build-a-vulnerability-management-program`
