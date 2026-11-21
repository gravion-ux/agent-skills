---
name: sign-and-verify-build-artifacts
description: Sign a release artifact and verify its signature, provenance, and identity before deployment. Use when the user wants proof that a build artifact came from a trusted pipeline and was not altered.
domain: devops-cloud
tags: [artifact-signing, provenance, supply-chain, verification]
triggers: ["sign and verify build artifacts", "verify a release artifact signature", "artifact provenance check"]
---

# Sign a release artifact and verify its signature, provenance, and identity before deployment

## Purpose

Sign a release artifact and verify its signature, provenance, and identity before deployment.

## When to use

Use when the user wants proof that a build artifact came from a trusted pipeline and was not altered.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Bind the signing identity to the protected release workflow and store its public key.
2. Generate the artifact signature and provenance statement at build time.
3. Upload the signature and provenance to the release registry alongside the digest.
4. Verify the signature, subject digest, and builder identity on the target host.
5. Reject the artifact when verification fails and report the failed check.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `back-up-and-restore-a-cloud-data-store`
- `build-a-container-image`
- `promote-a-build-through-environments`
