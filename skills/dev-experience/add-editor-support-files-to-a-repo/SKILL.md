---
name: add-editor-support-files-to-a-repo
description: Add editor support files that enforce shared formatting, navigation, and generation settings. Use when the user wants a repository to open consistently in the team's editors.
domain: dev-experience
tags: [editor-config, formatting, developer-tooling]
triggers: ["add editor support files", "configure VS Code for the repo", "share editor settings across developers"]
---

# Add editor support files that enforce shared formatting, navigation, and generation settings

## Purpose

Add editor support files that enforce shared formatting, navigation, and generation settings.

## When to use

Use when the user wants a repository to open consistently in the team's editors.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Collect the language, formatter, linter, and editor settings already used by the team.
2. Create shared editor and formatter configuration in the repository root.
3. Add safe code-generation, diagnostic, and file-exclusion settings.
4. Document which editors support the configuration and how to resolve conflicts.
5. Verify formatting, navigation, and generation in each supported editor.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `add-a-health-check-endpoint`
- `write-a-task-runner-for-a-repo`
- `adopt-a-new-linter-rule-safely`
