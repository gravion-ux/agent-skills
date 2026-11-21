---
name: migrate-code-to-a-new-language-version
description: Upgrade code to a new language version while preserving compatibility and controlling migration risk. Use when the user wants to migrate a repository to a newer language version.
domain: software-engineering
tags: [language-version, compatibility, migration]
triggers: ["migrate to a new language version", "upgrade code for a new language release"]
---

# Upgrade code to a new language version while preserving compatibility and controlling migration risk

## Purpose

Upgrade code to a new language version while preserving compatibility and controlling migration risk.

## When to use

Use when the user wants to migrate a repository to a newer language version.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Inventory removed features, deprecations, and dependency requirements.
2. Upgrade the toolchain and establish a compatible baseline.
3. Apply language migrations in small, reviewable changes.
4. Preserve runtime behavior for supported environments.
5. Run the full suite against the new version.
6. Document compatibility limits, rationale, and rollback.

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
- `port-a-module-to-another-language`
- `apply-solid-principles-to-a-class`
