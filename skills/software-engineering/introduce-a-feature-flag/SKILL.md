---
name: introduce-a-feature-flag
description: Introduce a feature flag with a default state, cleanup owner, and tests for both branches. Use when the user wants new behavior released gradually through a controlled code flag.
domain: software-engineering
tags: [feature-flags, rollout, safe-release]
triggers: ["introduce feature flag", "roll out behavior with flag", "add controlled code switch"]
---

# Introduce a feature flag with a default state, cleanup owner, and tests for both branches

## Purpose

Introduce a feature flag with a default state, cleanup owner, and tests for both branches.

## When to use

Use when the user wants new behavior released gradually through a controlled code flag.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Define the flag name, owner, default value, and removal condition.
2. Wrap only the intended behavior and keep the disabled path compatible.
3. Add tests for enabled, disabled, and missing configuration behavior.
4. Document rollout stages, monitoring signals, and the cleanup deadline.
5. Review the diff for scope and record a rollback to the default state.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `retire-a-feature-flag-after-rollout`
- `handle-merge-conflicts-in-a-feature-branch`
- `implement-a-feature-from-a-ticket`
