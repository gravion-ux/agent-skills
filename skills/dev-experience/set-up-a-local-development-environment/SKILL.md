---
name: set-up-a-local-development-environment
description: Create a reproducible local setup that installs prerequisites and verifies the developer toolchain. Use when the user needs a consistent local environment for a repository.
domain: dev-experience
tags: [environment-setup, toolchain, onboarding]
triggers: ["set up local development environment", "configure a reproducible dev environment", "prepare my local developer setup"]
---

# Create a reproducible local setup that installs prerequisites and verifies the developer toolchain

## Purpose

Create a reproducible local setup that installs prerequisites and verifies the developer toolchain.

## When to use

Use when the user needs a consistent local environment for a repository.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Record the operating system, runtime versions, package manager, and required services.
2. Pin tool versions in a version file committed beside the repository.
3. Add one setup command that installs dependencies and verifies required binaries.
4. Run the setup from a clean checkout and capture any missing prerequisite.
5. Document the setup command, expected runtime, and recovery path for common failures.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `reset-a-broken-local-environment`
- `document-a-local-setup-step`
- `speed-up-the-inner-development-loop`
