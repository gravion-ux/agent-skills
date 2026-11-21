---
name: protect-secrets-in-a-cicd-pipeline
description: Keep pipeline secrets out of logs and build outputs by scoping and masking them at use time. Use when the user wants to stop credentials leaking through a build pipeline.
domain: security
tags: [secrets, pipeline, masking]
triggers: ["protect secrets in a ci pipeline", "mask pipeline credentials in logs", "keep build secrets out of artefacts"]
---

# Keep pipeline secrets out of logs and build outputs by scoping and masking them at use time

## Purpose

Keep pipeline secrets out of logs and build outputs by scoping and masking them at use time.

## When to use

Use when the user wants to stop credentials leaking through a build pipeline.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. List every secret the pipeline reads and the step that needs each one.
2. Scope each secret to the single job that requires it.
3. Mask the value in the runner output and disable command echoing around it.
4. Check the built artefacts and the generated logs for the literal value.
5. Rotate any secret that already appeared in a log or an artefact.

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
- `secure-a-ci-pipeline-with-oidc`
- `add-security-headers-to-a-web-app`
