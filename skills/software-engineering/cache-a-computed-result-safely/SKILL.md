---
name: cache-a-computed-result-safely
description: Cache a computed result with explicit keys, invalidation rules, concurrency control, and eviction limits. Use when the user wants repeated computation reduced without serving stale results.
domain: software-engineering
tags: [caching, invalidation, concurrency]
triggers: ["cache a computed result safely", "design a concurrent result cache"]
---

# Cache a computed result with explicit keys, invalidation rules, concurrency control, and eviction limits

## Purpose

Cache a computed result with explicit keys, invalidation rules, concurrency control, and eviction limits.

## When to use

Use when the user wants repeated computation reduced without serving stale results.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Define the cache key and the invalidation dependencies.
2. Choose bounded eviction and expiration behavior.
3. Make reads and writes atomic under concurrent access.
4. Return the same result for equivalent valid inputs.
5. Test expiry, eviction, races, and invalidation paths.
6. Run existing tests and record rationale and rollback.

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
- `add-structured-logging-to-a-code-path`
- `apply-solid-principles-to-a-class`
