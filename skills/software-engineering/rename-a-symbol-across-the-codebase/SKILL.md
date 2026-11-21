---
name: rename-a-symbol-across-the-codebase
description: Rename a symbol across every code, test, and configuration reference without changing behavior. Use when the user wants a code symbol renamed consistently across a repository.
domain: software-engineering
tags: [symbol-rename, refactoring, codebase]
triggers: ["rename symbol across codebase", "change identifier everywhere", "rename API symbol safely"]
---

# Rename a symbol across every code, test, and configuration reference without changing behavior

## Purpose

Rename a symbol across every code, test, and configuration reference without changing behavior.

## When to use

Use when the user wants a code symbol renamed consistently across a repository.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. List the symbol definition, references, public exports, and generated artifacts.
2. Choose a collision-free name and update source definitions first.
3. Update call sites, tests, fixtures, and configuration references mechanically.
4. Run reference searches and the full suite to catch missed usages.
5. Record the compatibility impact, rationale, and rollback revision.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `reduce-the-blame-of-a-failing-test-suite`
- `work-in-a-legacy-codebase-without-tests`
- `add-structured-logging-to-a-code-path`
