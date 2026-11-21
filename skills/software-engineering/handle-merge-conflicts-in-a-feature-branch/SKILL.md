---
name: handle-merge-conflicts-in-a-feature-branch
description: Resolve feature-branch merge conflicts by preserving intended changes and validating the combined result. Use when the user has merge conflicts between a feature branch and its target.
domain: software-engineering
tags: [merge-conflicts, conflict-resolution, integration]
triggers: ["resolve feature branch merge conflicts", "combine conflicting code changes", "fix git merge conflict"]
---

# Resolve feature-branch merge conflicts by preserving intended changes and validating the combined result

## Purpose

Resolve feature-branch merge conflicts by preserving intended changes and validating the combined result.

## When to use

Use when the user has merge conflicts between a feature branch and its target.

## When NOT to use

Do not use this for infrastructure provisioning; use devops-cloud instead.

## Inputs required

- The repository and the language it is written in
- The behaviour that must change
- The constraints on compatibility and time

## Procedure

1. Reproduce the conflict in a clean checkout and inspect both branch histories.
2. Map each conflict to the ticket's intended behavior before editing files.
3. Resolve semantically rather than accepting either side wholesale.
4. Run targeted tests and the full suite on the merged result.
5. Review the final diff for scope and document the resolution and rollback.

## Output contract

A reviewed change with tests, a short rationale and a rollback note.

## Validation checklist

- [ ] The new behaviour is covered by an automated test
- [ ] Existing tests still pass
- [ ] The diff is limited to the requested scope

## Safety notes

Never delete user data, never weaken a test to make a build pass, and never commit credentials.

## Related skills

- `cut-a-release-branch-and-backport-a-fix`
- `implement-a-feature-from-a-ticket`
- `introduce-a-feature-flag`
