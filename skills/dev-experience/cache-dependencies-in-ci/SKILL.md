---
name: cache-dependencies-in-ci
description: Cache CI dependencies with keyed, verified cache entries that speed up builds safely. Use when the user wants CI builds to reuse dependencies without producing stale artifacts.
domain: dev-experience
tags: [ci-cache, dependency-cache, build-speed]
triggers: ["cache dependencies in CI", "speed up CI with dependency caching", "add a safe CI cache key"]
---

# Cache CI dependencies with keyed, verified cache entries that speed up builds safely

## Purpose

Cache CI dependencies with keyed, verified cache entries that speed up builds safely.

## When to use

Use when the user wants CI builds to reuse dependencies without producing stale artifacts.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Identify dependency downloads and build outputs that can be reused safely.
2. Define cache keys from lockfiles, runtime versions, and dependency manifests.
3. Verify cached contents and invalidate entries when relevant inputs change.
4. Measure cold-cache and warm-cache runtimes against the uncached baseline.
5. Document cache scope, fallback behavior, and retention limits.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `onboard-a-new-developer-in-a-week`
- `reduce-ci-time-for-pull-requests`
- `add-a-health-check-endpoint`
