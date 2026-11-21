---
name: remove-a-dependency-safely
description: Remove an unused dependency after verifying imports, plugins, runtime features, and lockfile effects. Use when the user wants an unused package removed from a maintained project.
domain: software-engineering
tags: [dependencies, cleanup, dependency-audit]
triggers: ["remove dependency safely", "drop unused package", "prune project dependency"]
---

# Remove an unused dependency after verifying imports, plugins, runtime features, and lockfile effects

## Purpose

Remove an unused dependency after verifying imports, plugins, runtime features, and lockfile effects.

## When to use

Use when the user wants an unused package removed from a maintained project.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Identify all imports, scripts, plugins, and runtime references to the package.
2. Reproduce the current build and test baseline before removing it.
3. Remove the dependency and regenerate the lockfile in a focused change.
4. Run builds, tests, and runtime smoke checks to catch indirect use.
5. Document the evidence, transitive removals, rationale, and rollback revision.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `cache-a-computed-result-safely`
- `remove-a-hot-path-allocation`
- `remove-dead-code-safely`
