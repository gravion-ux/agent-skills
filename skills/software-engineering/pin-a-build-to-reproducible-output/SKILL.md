---
name: pin-a-build-to-reproducible-output
description: Pin toolchain and dependency inputs so two clean builds produce the same release artefact. Use when the user needs software builds to be reproducible across machines.
domain: software-engineering
tags: [reproducible-builds, dependency-pinning, artifacts]
triggers: ["build reproducible software output", "pin a reproducible build"]
---

# Pin toolchain and dependency inputs so two clean builds produce the same release artefact

## Purpose

Pin toolchain and dependency inputs so two clean builds produce the same release artefact.

## When to use

Use when the user needs software builds to be reproducible across machines.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Record the exact compiler, runtime, and build tool versions.
2. Pin direct and transitive dependencies with a lockfile.
3. Remove timestamps and machine-specific paths from outputs.
4. Build twice from clean directories.
5. Compare artefact hashes and record any differences.
6. Run tests and document the build inputs and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `add-structured-logging-to-a-code-path`
- `apply-solid-principles-to-a-class`
- `bisect-a-regression-to-one-commit`
