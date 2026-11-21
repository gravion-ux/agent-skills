---
name: extract-a-shared-helper
description: Extract a shared helper only where it removes verified duplication and clarifies ownership. Use when the user wants repeated code replaced by one reusable helper.
domain: software-engineering
tags: [shared-helper, duplication, interface-design]
triggers: ["extract shared helper", "consolidate repeated helper logic", "share utility across modules"]
---

# Extract a shared helper only where it removes verified duplication and clarifies ownership

## Purpose

Extract a shared helper only where it removes verified duplication and clarifies ownership.

## When to use

Use when the user wants repeated code replaced by one reusable helper.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Locate every candidate call site and compare their actual contracts.
2. Choose the smallest shared interface that preserves existing semantics.
3. Add focused tests for the helper and each adapted caller.
4. Replace call sites incrementally and keep unrelated differences untouched.
5. Run the suite and record why the helper is shared and how to roll it back.

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
- `automate-a-repetitive-code-change`
