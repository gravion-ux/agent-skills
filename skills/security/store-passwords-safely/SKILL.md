---
name: store-passwords-safely
description: Implement password storage with a modern password hash and safe verification policy. Use when the user wants user passwords stored and verified without exposing plaintext.
domain: security
tags: [password-hashing, credentials, authentication]
triggers: ["store passwords safely", "hash user passwords correctly", "implement secure password storage"]
---

# Implement password storage with a modern password hash and safe verification policy

## Purpose

Implement password storage with a modern password hash and safe verification policy.

## When to use

Use when the user wants user passwords stored and verified without exposing plaintext.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Select a memory-hard password hash with a reviewed work factor and unique per-user salt.
2. Store only the encoded hash, algorithm parameters, and a rehash-on-login flag.
3. Verify passwords with a constant-time comparison and reject excessively long inputs.
4. Add tests that cover matching, wrong, malformed, and rehash-required passwords.
5. Purge plaintext or legacy weak hashes from every credential store during migration.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `configure-cors-safely`
- `add-input-validation-to-an-endpoint`
- `add-security-headers-to-a-web-app`
