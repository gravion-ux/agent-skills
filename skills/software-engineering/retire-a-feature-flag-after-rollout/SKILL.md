---
name: retire-a-feature-flag-after-rollout
description: Remove a fully rolled-out feature flag and its branches after verifying every consumer is migrated. Use when the user wants an expired feature flag removed from production code.
domain: software-engineering
tags: [feature-flags, cleanup, rollout]
triggers: ["retire feature flag after rollout", "remove expired code flag", "delete completed flag branches"]
---

# Remove a fully rolled-out feature flag and its branches after verifying every consumer is migrated

## Purpose

Remove a fully rolled-out feature flag and its branches after verifying every consumer is migrated.

## When to use

Use when the user wants an expired feature flag removed from production code.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Confirm rollout completion in every environment and inspect flag usage.
2. Delete the flag branches, configuration, tests, and obsolete dependencies.
3. Verify only the winning behavior remains and update affected documentation.
4. Run the full suite and compare production metrics after removal.
5. Record the removal evidence, rationale, and rollback revision.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `introduce-a-feature-flag`
- `handle-merge-conflicts-in-a-feature-branch`
- `implement-a-feature-from-a-ticket`
