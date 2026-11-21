---
name: create-a-code-snippet-library
description: Curate a searchable code snippet library with tested examples, ownership, and usage context. Use when the user wants to capture reusable code examples for recurring developer tasks.
domain: dev-experience
tags: [code-snippets, knowledge-base, reusable-patterns]
triggers: ["create a code snippet library", "publish reusable code examples", "build an internal snippet catalog"]
---

# Curate a searchable code snippet library with tested examples, ownership, and usage context

## Purpose

Curate a searchable code snippet library with tested examples, ownership, and usage context.

## When to use

Use when the user wants to capture reusable code examples for recurring developer tasks.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Collect recurring implementation patterns and the projects that use them.
2. Select snippets that are tested, reusable, and free of organization secrets.
3. Store each snippet with its language, inputs, outputs, and failure modes.
4. Add source links, owners, review dates, and automated validation where possible.
5. Publish the catalog in a searchable location and measure its use.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `version-and-publish-a-shared-library`
- `add-a-health-check-endpoint`
- `add-editor-support-files-to-a-repo`
