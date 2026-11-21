---
name: publish-an-internal-developer-package
description: Publish an internal package with discoverable metadata, versioning, and a reliable developer install path. Use when the user wants to distribute a reusable package to developers inside the organization.
domain: dev-experience
tags: [internal-package, package-publishing, developer-tooling]
triggers: ["publish an internal developer package", "distribute a package to internal devs", "release a private team package"]
---

# Publish an internal package with discoverable metadata, versioning, and a reliable developer install path

## Purpose

Publish an internal package with discoverable metadata, versioning, and a reliable developer install path.

## When to use

Use when the user wants to distribute a reusable package to developers inside the organization.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Define the package's public API, supported runtimes, and ownership.
2. Create versioned metadata with an internal registry location and access instructions.
3. Add automated tests and a publish dry run that verifies the artifact.
4. Publish to a staging registry and test installation in a clean environment.
5. Document the package, changelog, migration notes, and deprecation policy.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `write-an-internal-tooling-adoption-plan`
- `manage-multiple-package-versions`
- `measure-developer-productivity-signals`
