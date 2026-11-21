---
name: reset-a-broken-local-environment
description: Diagnose and reset a broken local environment while preserving source changes and recoverable state. Use when the user's local development environment is broken or inconsistent.
domain: dev-experience
tags: [environment-recovery, local-reset, diagnostics]
triggers: ["reset a broken local environment", "repair my local dev setup", "recover a broken local toolchain"]
---

# Diagnose and reset a broken local environment while preserving source changes and recoverable state

## Purpose

Diagnose and reset a broken local environment while preserving source changes and recoverable state.

## When to use

Use when the user's local development environment is broken or inconsistent.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Capture the failing command, environment versions, and recent setup changes.
2. Distinguish dependency, service, cache, and configuration failures before resetting anything.
3. Back up local configuration and source work that the reset could remove.
4. Run the repository's supported reset path and reinstall only affected components.
5. Verify a clean startup and record the recovery steps in the setup guide.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `set-up-a-local-development-environment`
- `document-a-local-setup-step`
- `add-a-health-check-endpoint`
