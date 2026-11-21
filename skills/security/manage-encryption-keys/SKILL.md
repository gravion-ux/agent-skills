---
name: manage-encryption-keys
description: Manage encryption keys with controlled rotation, separation of duties, and recoverability. Use when the user needs an encryption key lifecycle designed for production use.
domain: security
tags: [key-management, encryption, cryptography]
triggers: ["manage encryption keys", "rotate a data encryption key safely", "design a production key lifecycle"]
---

# Manage encryption keys with controlled rotation, separation of duties, and recoverability

## Purpose

Manage encryption keys with controlled rotation, separation of duties, and recoverability.

## When to use

Use when the user needs an encryption key lifecycle designed for production use.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Classify the data and select the required key strength, algorithm, region, and rotation interval.
2. Generate the key inside the approved key-management service and restrict key-administration roles.
3. Separate encryption, decryption, and administration duties and record the key owner.
4. Rotate the key through an overlap window and re-encrypt data under the new key version.
5. Test revocation, recovery, and rotation alerts without exposing plaintext key material.

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
- `apply-data-classification-labels`
