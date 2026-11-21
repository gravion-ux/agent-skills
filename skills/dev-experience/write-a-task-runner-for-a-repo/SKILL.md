---
name: write-a-task-runner-for-a-repo
description: Create a repository task runner that exposes common checks through consistent commands. Use when the user wants recurring repository tasks wrapped in predictable commands.
domain: dev-experience
tags: [task-runner, automation, developer-commands]
triggers: ["write a repository task runner", "add a make task runner", "standardize repo commands"]
---

# Create a repository task runner that exposes common checks through consistent commands

## Purpose

Create a repository task runner that exposes common checks through consistent commands.

## When to use

Use when the user wants recurring repository tasks wrapped in predictable commands.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Inventory the setup, build, test, lint, and release commands already in use.
2. Define one stable task name for each recurring developer action.
3. Implement tasks that fail fast and print the underlying command output.
4. Document each task with prerequisites and expected success signal.
5. Measure task duration and remove work that does not support the critical path.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `add-editor-support-files-to-a-repo`
- `write-a-developer-cli-wrapper`
- `write-a-developer-onboarding-checklist`
