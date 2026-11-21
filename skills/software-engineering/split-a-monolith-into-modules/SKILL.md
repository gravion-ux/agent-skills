---
name: split-a-monolith-into-modules
description: Split a monolithic module along real responsibilities while preserving behavior through incremental module boundaries. Use when the user wants a large module divided into maintainable parts.
domain: software-engineering
tags: [refactoring, modularization, architecture]
triggers: ["split a monolith into modules", "extract cohesive code modules"]
---

# Split a monolithic module along real responsibilities while preserving behavior through incremental module boundaries

## Purpose

Split a monolithic module along real responsibilities while preserving behavior through incremental module boundaries.

## When to use

Use when the user wants a large module divided into maintainable parts.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Map responsibilities and dependencies across the monolith.
2. Choose module boundaries with explicit public interfaces.
3. Move one cohesive responsibility at a time.
4. Keep internal changes behind the new boundaries.
5. Run focused and full tests after each move.
6. Record the rationale, remaining dependencies, and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `split-a-large-pull-request`
- `add-structured-logging-to-a-code-path`
- `apply-solid-principles-to-a-class`
