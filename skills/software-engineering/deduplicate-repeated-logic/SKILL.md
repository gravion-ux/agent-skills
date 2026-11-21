---
name: deduplicate-repeated-logic
description: Consolidate repeated implementation logic while preserving each call site's distinct requirements. Use when the user wants copy-pasted application logic reduced into one maintained implementation.
domain: software-engineering
tags: [duplication, refactoring, consistency]
triggers: ["deduplicate repeated logic", "consolidate copy pasted code", "merge duplicate implementation blocks"]
---

# Consolidate repeated implementation logic while preserving each call site's distinct requirements

## Purpose

Consolidate repeated implementation logic while preserving each call site's distinct requirements.

## When to use

Use when the user wants copy-pasted application logic reduced into one maintained implementation.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Group similar blocks by behavior and identify meaningful differences.
2. Select the canonical implementation and define its contract.
3. Write a characterization test for the shared behavior and edge differences.
4. Move callers to the canonical logic without broad formatting changes.
5. Run focused and existing tests, then document the deduplication and rollback.

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
- `add-timeouts-and-cancellation`
- `adopt-type-checking-in-an-untyped-codebase`
