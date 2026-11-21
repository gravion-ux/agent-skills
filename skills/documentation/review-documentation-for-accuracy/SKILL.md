---
name: review-documentation-for-accuracy
description: Audit documentation claims against current source, tests, and observable behavior. Use when the user wants a focused accuracy review of an existing document.
domain: documentation
tags: [documentation-review, accuracy, audit]
triggers: ["documentation accuracy review", "review docs for accuracy", "audit documentation against code"]
---

# Audit documentation claims against current source, tests, and observable behavior

## Purpose

Audit documentation claims against current source, tests, and observable behavior.

## When to use

Use when the user wants a focused accuracy review of an existing document.

## When NOT to use

Do not use this for a persuasive article or campaign copy; use content-creation instead.

## Inputs required

- The audience and what they must be able to do
- The subject and the source material
- The format and the maintenance owner

## Procedure

1. List each factual and procedural claim in the document.
2. Map each claim to source code, a test, or a runnable example.
3. Execute the runnable examples and record their actual results.
4. Classify mismatches by severity and affected reader task.
5. Patch confirmed errors and route ambiguous claims to the owner.

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
- `document-an-api-for-consumers`
- `keep-documentation-in-sync-with-code`
