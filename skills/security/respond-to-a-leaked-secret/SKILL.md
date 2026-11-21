---
name: respond-to-a-leaked-secret
description: Contain and recover from a leaked secret without disclosing the credential itself. Use when the user reports a credential exposed in code, logs, chat, or a public repository.
domain: security
tags: [secret-exposure, credential-revocation, incident-response]
triggers: ["respond to a leaked secret", "contain an exposed credential", "handle a secret found in a repository"]
---

# Contain and recover from a leaked secret without disclosing the credential itself

## Purpose

Contain and recover from a leaked secret without disclosing the credential itself.

## When to use

Use when the user reports a credential exposed in code, logs, chat, or a public repository.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Record the secret identifier, exposure source, and time without copying the credential value.
2. Revoke or rotate the exposed credential and invalidate dependent sessions or tokens.
3. Search logs, repositories, and artefacts for other copies and remove them.
4. Assess misuse from authentication and audit logs within the exposure window.
5. Document the containment, recovery, and monitoring actions in the incident record.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `respond-to-a-ransomware-suspicion`
- `add-security-headers-to-a-web-app`
- `add-input-validation-to-an-endpoint`
