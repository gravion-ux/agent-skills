---
name: set-up-a-build-system-for-a-new-service
description: Set up a new service build with reproducible commands, dependency locking, and CI parity. Use when the user wants a new service to have a reliable local and CI build.
domain: software-engineering
tags: [build-system, ci-parity, reproducibility]
triggers: ["set up build system for service", "create reproducible service build", "bootstrap new service build"]
---

# Set up a new service build with reproducible commands, dependency locking, and CI parity

## Purpose

Set up a new service build with reproducible commands, dependency locking, and CI parity.

## When to use

Use when the user wants a new service to have a reliable local and CI build.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Identify the language, runtime version, dependencies, and deployment artifacts.
2. Create one documented build command with locked dependency installation.
3. Add separate test and package commands that match CI invocation.
4. Build from a clean checkout and verify the artifact starts in isolation.
5. Document the build contract, tool versions, and rollback to the previous process.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `speed-up-a-slow-build`
- `configure-formatting-and-linting-for-a-repo`
- `migrate-code-to-a-new-language-version`
