---
name: support-a-library-consumer
description: Resolve a library consumer issue with a minimal compatibility fix, focused regression test, and usage guidance. Use when the user is supporting a downstream consumer of a published library.
domain: software-engineering
tags: [library-support, compatibility, consumers]
triggers: ["support a library consumer", "fix a downstream library issue"]
---

# Resolve a library consumer issue with a minimal compatibility fix, focused regression test, and usage guidance

## Purpose

Resolve a library consumer issue with a minimal compatibility fix, focused regression test, and usage guidance.

## When to use

Use when the user is supporting a downstream consumer of a published library.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Reproduce the issue in a minimal consumer project.
2. Confirm the supported versions and public API expectations.
3. Identify the smallest library-side compatibility fix.
4. Add a regression test matching the consumer scenario.
5. Run the library suite and publish migration guidance.
6. Document rationale, compatibility impact, and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `raise-useful-errors-from-a-library`
- `verify-a-third-party-library-integration`
- `add-structured-logging-to-a-code-path`
