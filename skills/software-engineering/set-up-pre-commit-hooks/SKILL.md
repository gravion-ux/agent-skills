---
name: set-up-pre-commit-hooks
description: Add pre-commit hooks that run fast deterministic checks and remain easy to bypass deliberately. Use when the user wants local git hooks to catch quality failures before review.
domain: software-engineering
tags: [pre-commit, hooks, developer-workflow]
triggers: ["set up pre commit hooks", "add local git quality hooks", "install commit time checks"]
---

# Add pre-commit hooks that run fast deterministic checks and remain easy to bypass deliberately

## Purpose

Add pre-commit hooks that run fast deterministic checks and remain easy to bypass deliberately.

## When to use

Use when the user wants local git hooks to catch quality failures before review.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Inspect repository guidance and existing CI checks before choosing hooks.
2. Select fast deterministic checks that mirror relevant CI failures.
3. Configure hook installation in the documented developer setup path.
4. Prove each hook catches its failure and does not alter source files unexpectedly.
5. Document bypass reasons, update instructions, and how to remove the hooks.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `set-up-a-build-system-for-a-new-service`
- `bisect-a-regression-to-one-commit`
- `speed-up-a-slow-build`
