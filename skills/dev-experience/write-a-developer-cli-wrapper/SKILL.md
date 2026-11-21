---
name: write-a-developer-cli-wrapper
description: Wrap a developer CLI with safe defaults, readable output, and commands that match the repository workflow. Use when the user wants a repository-specific command-line tool that simplifies a developer workflow.
domain: dev-experience
tags: [cli-wrapper, developer-cli, command-line]
triggers: ["write a developer CLI wrapper", "build a repo-specific command wrapper", "add safe CLI subcommands"]
---

# Wrap a developer CLI with safe defaults, readable output, and commands that match the repository workflow

## Purpose

Wrap a developer CLI with safe defaults, readable output, and commands that match the repository workflow.

## When to use

Use when the user wants a repository-specific command-line tool that simplifies a developer workflow.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. List the raw commands developers run repeatedly and their required arguments.
2. Define stable subcommands with safe defaults and clear validation errors.
3. Delegate to existing tools instead of duplicating their core behavior.
4. Add machine-readable output and a dry-run mode for consequential actions.
5. Document installation, examples, exit codes, and migration from raw commands.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `write-a-developer-onboarding-checklist`
- `onboard-a-new-developer-in-a-week`
- `write-a-good-commit-message`
