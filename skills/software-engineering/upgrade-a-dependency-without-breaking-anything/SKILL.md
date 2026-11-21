---
name: upgrade-a-dependency-without-breaking-anything
description: Upgrade a dependency with compatibility checks, pinned versions, and a tested rollback. Use when the user wants a package upgraded without breaking the application.
domain: software-engineering
tags: [dependencies, upgrade, compatibility]
triggers: ["upgrade dependency without breaking", "bump package version safely", "test library upgrade compatibility"]
---

# Upgrade a dependency with compatibility checks, pinned versions, and a tested rollback

## Purpose

Upgrade a dependency with compatibility checks, pinned versions, and a tested rollback.

## When to use

Use when the user wants a package upgraded without breaking the application.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Review the release notes, supported versions, and dependency constraints.
2. Upgrade the package in the smallest possible commit and resolve the lockfile.
3. Run focused compatibility tests, the full suite, and build checks.
4. Inspect the diff for unrelated upstream changes and secret exposure.
5. Document the tested version, rationale, migration needs, and rollback version.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `remove-a-dependency-safely`
- `work-in-a-legacy-codebase-without-tests`
- `add-structured-logging-to-a-code-path`
