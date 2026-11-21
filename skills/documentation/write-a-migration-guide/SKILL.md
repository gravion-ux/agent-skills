---
name: write-a-migration-guide
description: Plan a safe upgrade path with prerequisites, staged changes, validation, and rollback. Use when the user needs a migration guide for moving between product or dependency versions.
domain: documentation
tags: [migration, upgrade, rollback]
triggers: ["upgrade migration guide", "write a migration guide", "migration guide for a version upgrade"]
---

# Plan a safe upgrade path with prerequisites, staged changes, validation, and rollback

## Purpose

Plan a safe upgrade path with prerequisites, staged changes, validation, and rollback.

## When to use

Use when the user needs a migration guide for moving between product or dependency versions.

## When NOT to use

Do not use this for a persuasive article or campaign copy; use content-creation instead.

## Inputs required

- The audience and what they must be able to do
- The subject and the source material
- The format and the maintenance owner

## Procedure

1. Inventory breaking changes and required prerequisites.
2. Map each old behavior or setting to its replacement.
3. Order the migration steps so data and service changes remain consistent.
4. Test the steps on a representative copy of the environment.
5. Document validation checks and a tested rollback procedure.

## Output contract

A document that answers the reader's question, with structure, examples and an owner.

## Validation checklist

- [ ] The document answers its stated question
- [ ] Examples are runnable and current
- [ ] Every claim can be traced to a source

## Safety notes

Never document a command you have not run, and never leave an internal secret in an example.

## Related skills

- `write-a-quickstart-guide`
- `write-a-troubleshooting-guide`
- `maintain-a-documentation-style-guide`
