---
name: configure-a-repository-template
description: Configure a repository template that standardizes structure, automation, and documentation for new projects. Use when the user wants a reusable baseline for newly created repositories.
domain: dev-experience
tags: [repository-template, scaffolding, standards]
triggers: ["configure a repository template", "create a standard repo template", "standardize new repository layout"]
---

# Configure a repository template that standardizes structure, automation, and documentation for new projects

## Purpose

Configure a repository template that standardizes structure, automation, and documentation for new projects.

## When to use

Use when the user wants a reusable baseline for newly created repositories.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Define the baseline files every new repository must include.
2. Pin shared automation versions and label intentional differences.
3. Add a validation command that fails on missing or malformed baseline files.
4. Document each template choice and the escape hatch for project-specific needs.
5. Create one reference repository and verify its setup and CI paths.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `scaffold-a-new-service-repository`
- `add-a-health-check-endpoint`
- `add-editor-support-files-to-a-repo`
