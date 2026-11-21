---
name: provision-preview-environments-per-branch
description: Provision an isolated preview environment for each pull-request branch with a documented lifecycle. Use when the user wants every pull-request branch to receive a disposable preview environment.
domain: dev-experience
tags: [preview-environments, pull-request-preview, infrastructure]
triggers: ["provision preview environments per branch", "create a pull request preview environment", "spin up a branch preview deployment"]
---

# Provision an isolated preview environment for each pull-request branch with a documented lifecycle

## Purpose

Provision an isolated preview environment for each pull-request branch with a documented lifecycle.

## When to use

Use when the user wants every pull-request branch to receive a disposable preview environment.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Define the branch-to-environment naming rule and required service configuration.
2. Create the environment from versioned infrastructure and application images.
3. Run migrations, seed test data, and expose the preview URL through pull-request checks.
4. Label the owner, age, and source commit on every preview resource.
5. Document the URL, costs, secrets policy, and teardown command.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `clean-up-stale-preview-environments`
- `add-a-health-check-endpoint`
- `add-editor-support-files-to-a-repo`
