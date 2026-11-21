---
name: manage-multiple-package-versions
description: Manage multiple package versions with explicit constraints, compatibility notes, and safe upgrade paths. Use when the user must support more than one version of a package or API simultaneously.
domain: dev-experience
tags: [version-management, dependency-compat, compatibility-matrix]
triggers: ["manage multiple package versions", "support several dependency versions", "build a package compatibility matrix"]
---

# Manage multiple package versions with explicit constraints, compatibility notes, and safe upgrade paths

## Purpose

Manage multiple package versions with explicit constraints, compatibility notes, and safe upgrade paths.

## When to use

Use when the user must support more than one version of a package or API simultaneously.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Map which consumers require each package version and their dependency constraints.
2. Choose an isolation strategy such as aliases, namespaces, or separate environments.
3. Add compatibility checks for every supported version to CI.
4. Document the supported matrix, upgrade path, and removal criteria.
5. Test one representative consumer against each supported version.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `publish-an-internal-developer-package`
- `add-a-health-check-endpoint`
- `add-editor-support-files-to-a-repo`
