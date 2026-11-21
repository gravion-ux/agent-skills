---
name: detect-secret-leaks-in-ci
description: Detect leaked secrets in continuous-integration workflows and block unsafe publication. Use when the user wants pipelines to stop committing or publishing exposed credentials.
domain: security
tags: [secret-scanning, ci-security, pipeline-gating]
triggers: ["detect secret leaks in ci", "block pipelines that expose credentials", "scan build logs and artefacts for secrets"]
---

# Detect leaked secrets in continuous-integration workflows and block unsafe publication

## Purpose

Detect leaked secrets in continuous-integration workflows and block unsafe publication.

## When to use

Use when the user wants pipelines to stop committing or publishing exposed credentials.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Configure the scanner to inspect source, build logs, artefacts, and pull-request history.
2. Redact matching values from logs and reports while retaining the location and rule identifier.
3. Fail the pipeline on confirmed secrets and route revocation tasks to the responsible owner.
4. Test the pipeline with a harmless marker to confirm detection before a merge or release.
5. Review scanner exclusions and confirm that each exclusion is narrow and documented.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `protect-secrets-in-a-cicd-pipeline`
- `respond-to-a-leaked-secret`
- `review-permissions-in-an-iam-policy`
