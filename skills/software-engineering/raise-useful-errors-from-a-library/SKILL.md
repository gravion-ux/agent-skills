---
name: raise-useful-errors-from-a-library
description: Raise stable library errors with actionable context while keeping implementation details private. Use when the user wants a library failure to explain its cause and recovery path.
domain: software-engineering
tags: [error-handling, library-api, diagnostics]
triggers: ["raise useful library errors", "add actionable error context"]
---

# Raise stable library errors with actionable context while keeping implementation details private

## Purpose

Raise stable library errors with actionable context while keeping implementation details private.

## When to use

Use when the user wants a library failure to explain its cause and recovery path.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Define the public error types callers can handle.
2. Attach the operation, relevant input, and causal chain.
3. Omit secrets, stack details, and internal identifiers.
4. Map low-level exceptions at the library boundary.
5. Test error types and messages for each public failure path.
6. Document usage examples and the compatibility impact.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `implement-a-feature-from-a-ticket`
- `support-a-library-consumer`
- `verify-a-third-party-library-integration`
