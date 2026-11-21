---
name: split-an-oversized-module
description: Split an oversized module into cohesive units with explicit imports and unchanged behavior. Use when the user wants one oversized source module divided without changing its contract.
domain: software-engineering
tags: [module-refactoring, code-organization, compatibility]
triggers: ["split oversized module", "divide giant source file", "break module into units"]
---

# Split an oversized module into cohesive units with explicit imports and unchanged behavior

## Purpose

Split an oversized module into cohesive units with explicit imports and unchanged behavior.

## When to use

Use when the user wants one oversized source module divided without changing its contract.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Map the module's responsibilities, public symbols, and import consumers.
2. Group responsibilities into cohesive target modules with narrow interfaces.
3. Move code in small batches and preserve public import paths where required.
4. Add or update import-level tests before removing compatibility exports.
5. Run the full suite and document module boundaries and a rollback note.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `adopt-type-checking-in-an-untyped-codebase`
- `fix-an-off-by-one-error`
- `port-a-module-to-another-language`
