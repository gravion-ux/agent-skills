---
name: sign-an-artifact-for-provenance
description: Sign a build artifact so consumers can verify its origin and integrity. Use when the user wants a released artefact protected against tampering and substitution.
domain: security
tags: [artifact-signing, provenance, supply-chain]
triggers: ["sign an artifact for provenance", "attest the origin of a build artefact", "create verifiable software release signatures"]
---

# Sign a build artifact so consumers can verify its origin and integrity

## Purpose

Sign a build artifact so consumers can verify its origin and integrity.

## When to use

Use when the user wants a released artefact protected against tampering and substitution.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Select the signing key, trusted identity, transparency log, and signing workflow approved for releases.
2. Generate a canonical digest of the immutable artefact without modifying its contents.
3. Attach a signature and provenance metadata that binds the artefact to its source commit and builder.
4. Store the signature separately from the artefact and publish verification material to consumers.
5. Verify the signature from a clean environment and confirm that a modified artefact fails validation.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `enforce-mfa-for-an-organisation`
- `add-input-validation-to-an-endpoint`
- `enable-audit-logging-for-a-cloud-account`
