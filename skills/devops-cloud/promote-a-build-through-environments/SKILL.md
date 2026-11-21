---
name: promote-a-build-through-environments
description: Advance one immutable build artifact from development to production through approval gates. Use when the user wants to move the same tested build through successive release environments.
domain: devops-cloud
tags: [promotion, build-artifact, release, approval]
triggers: ["promote a build through environments", "build promotion from staging to production", "promote an immutable build"]
---

# Advance one immutable build artifact from development to production through approval gates

## Purpose

Advance one immutable build artifact from development to production through approval gates.

## When to use

Use when the user wants to move the same tested build through successive release environments.

## When NOT to use

Do not use this for application code changes; use software-engineering instead.

## Inputs required

- The target environment and its account
- The desired end state
- The rollback window and the budget ceiling

## Procedure

1. Identify the immutable artifact digest approved for promotion.
2. Promote the digest to staging with environment-specific configuration applied.
3. Run the smoke test suite and attach its output to the promotion record.
4. Obtain the required approval before promoting to production.
5. Record each environment, digest, and approver in the release log.

## Output contract

Applied infrastructure changes plus the state diff, the rollback path and the verification output.

## Validation checklist

- [ ] The plan was reviewed before it was applied
- [ ] The rollback path was tested or proven
- [ ] Cost and quota impact is known

## Safety notes

Never apply a destructive infrastructure change without explicit confirmation and a rollback plan.

## Related skills

- `build-a-container-image`
- `apply-a-cost-budget-to-cloud-resources`
- `automate-a-release-with-a-pull-request`
