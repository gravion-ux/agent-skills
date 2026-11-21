---
name: configure-cors-safely
description: Configure CORS with an explicit origin allowlist and safe credential handling. Use when the user needs browser cross-origin requests controlled on an API service.
domain: security
tags: [cors, cross-origin, browser-security]
triggers: ["configure cors safely", "restrict api cross-origin requests", "allowlist browser origins for an api"]
---

# Configure CORS with an explicit origin allowlist and safe credential handling

## Purpose

Configure CORS with an explicit origin allowlist and safe credential handling.

## When to use

Use when the user needs browser cross-origin requests controlled on an API service.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. List the exact browser origins and the methods and headers each origin may use.
2. Configure a strict origin allowlist instead of reflecting arbitrary origins or using a wildcard.
3. Enable credentials only when required and verify that the response omits the wildcard origin.
4. Add cache headers that prevent one origin's response from being reused by another.
5. Test allowed, denied, credentialed, preflight, and null-origin requests against the deployed policy.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `configure-a-cloud-firewall-baseline`
- `store-passwords-safely`
- `add-input-validation-to-an-endpoint`
