---
name: clean-up-stale-preview-environments
description: Identify and remove stale preview environments by age, ownership, and last activity thresholds. Use when the user needs to reclaim resources from abandoned pull-request previews.
domain: dev-experience
tags: [preview-cleanup, resource-hygiene, preview-environments]
triggers: ["clean up stale preview environments", "delete abandoned branch previews", "prune old preview deployments"]
---

# Identify and remove stale preview environments by age, ownership, and last activity thresholds

## Purpose

Identify and remove stale preview environments by age, ownership, and last activity thresholds.

## When to use

Use when the user needs to reclaim resources from abandoned pull-request previews.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. List preview environments with their branch, owner, age, and last activity.
2. Apply the documented threshold and preserve environments with an active release hold.
3. Report the proposed deletions and request confirmation when policy requires it.
4. Delete matching resources through the provider and remove their labels and secrets.
5. Verify the remaining inventory and record reclaimed resource counts.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `provision-preview-environments-per-branch`
- `set-up-a-local-development-environment`
- `speed-up-the-inner-development-loop`
