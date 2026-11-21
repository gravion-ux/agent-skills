---
name: speed-up-a-slow-build
description: Reduce build duration by measuring stages, removing waste, and proving equivalent outputs. Use when the user wants a slow repository build made faster without changing its result.
domain: software-engineering
tags: [build-performance, profiling, caching]
triggers: ["speed up slow build", "reduce repository build time", "optimize build pipeline duration"]
---

# Reduce build duration by measuring stages, removing waste, and proving equivalent outputs

## Purpose

Reduce build duration by measuring stages, removing waste, and proving equivalent outputs.

## When to use

Use when the user wants a slow repository build made faster without changing its result.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Measure cold and warm build durations by stage on representative machines.
2. Identify the slowest cache miss, repeated work, and unnecessary network calls.
3. Prototype one improvement and compare artifacts or test outcomes.
4. Apply the change and verify build output and full tests remain equivalent.
5. Record before-and-after timings, trade-offs, and the rollback procedure.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `set-up-a-build-system-for-a-new-service`
- `pin-a-build-to-reproducible-output`
- `profile-a-slow-function`
