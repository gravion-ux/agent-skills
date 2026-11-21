---
name: keep-documentation-in-sync-with-code
description: Detect and correct documentation drift by comparing code, tests, and published guides. Use when the user wants an automated way to keep published documentation aligned with code.
domain: documentation
tags: [documentation-sync, automation, drift-detection]
triggers: ["documentation sync check", "keep docs in sync with code", "scan docs for code drift"]
---

# Detect and correct documentation drift by comparing code, tests, and published guides

## Purpose

Detect and correct documentation drift by comparing code, tests, and published guides.

## When to use

Use when the user wants an automated way to keep published documentation aligned with code.

## When NOT to use

Do not use this for a persuasive article or campaign copy; use content-creation instead.

## Inputs required

- The audience and what they must be able to do
- The subject and the source material
- The format and the maintenance owner

## Procedure

1. Inventory the code, schemas, tests, and guides owned by the project.
2. Extract documented commands, options, routes, and defaults from source.
3. Compare each extracted value with its corresponding published claim.
4. Update confirmed drift in the owned guide and rerun its examples.
5. Emit a report of unresolved differences with file locations.

## Output contract

A document that answers the reader's question, with structure, examples and an owner.

## Validation checklist

- [ ] The document answers its stated question
- [ ] Examples are runnable and current
- [ ] Every claim can be traced to a source

## Safety notes

Never document a command you have not run, and never leave an internal secret in an example.

## Related skills

- `capture-a-screen-recording-as-documentation`
- `document-an-error-code-and-its-fix`
- `maintain-a-documentation-style-guide`
