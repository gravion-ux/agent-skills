---
name: verify-software-supply-chain-integrity
description: Verify that a build's source, dependencies and artefacts match what was reviewed. Use when the user wants evidence that a released artefact came from the expected source.
domain: security
tags: [supply-chain, provenance, integrity]
triggers: ["verify software supply chain integrity", "confirm an artefact came from the expected source", "check build provenance end to end"]
---

# Verify that a build's source, dependencies and artefacts match what was reviewed

## Purpose

Verify that a build's source, dependencies and artefacts match what was reviewed.

## When to use

Use when the user wants evidence that a released artefact came from the expected source.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Pin the source revision and record the dependency lock file hash.
2. Compare the artefact digest against the digest produced by the trusted build.
3. Check the dependency list for newly added packages and unusual sources.
4. Confirm the artefact carries the expected provenance and signature.
5. Attach the digest comparison to the release record.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `verify-a-webhook-signature`
- `add-input-validation-to-an-endpoint`
- `add-security-headers-to-a-web-app`
