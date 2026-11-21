---
name: remove-dead-code-safely
description: Remove unreachable or obsolete code after proving no runtime, build, or consumer dependency remains. Use when the user wants unused code removed without deleting active behavior or user data.
domain: software-engineering
tags: [dead-code, static-analysis, safe-removal]
triggers: ["remove dead code safely", "delete unused source paths", "prune unreachable code"]
---

# Remove unreachable or obsolete code after proving no runtime, build, or consumer dependency remains

## Purpose

Remove unreachable or obsolete code after proving no runtime, build, or consumer dependency remains.

## When to use

Use when the user wants unused code removed without deleting active behavior or user data.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Identify unused symbols, routes, files, and configuration references.
2. Trace references through source, tests, build scripts, and public contracts.
3. Exclude data files and destructive cleanup from the removal.
4. Confirm the target is unobservable and remove it in a separate change.
5. Run builds and the full test suite, then record the evidence and rollback revision.

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
- `automate-a-repetitive-code-change`
