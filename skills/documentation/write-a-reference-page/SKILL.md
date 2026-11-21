---
name: write-a-reference-page
description: Document an interface's inputs, outputs, constraints, and behavior without hiding caveats. Use when the user needs a reference page for an interface, command, or service.
domain: documentation
tags: [reference, interface, behavior]
triggers: ["interface reference page", "write an interface reference page", "reference page for a command"]
---

# Document an interface's inputs, outputs, constraints, and behavior without hiding caveats

## Purpose

Document an interface's inputs, outputs, constraints, and behavior without hiding caveats.

## When to use

Use when the user needs a reference page for an interface, command, or service.

## When NOT to use

Do not use this for a persuasive article or campaign copy; use content-creation instead.

## Inputs required

- The audience and what they must be able to do
- The subject and the source material
- The format and the maintenance owner

## Procedure

1. Inventory every accepted input and produced output.
2. Record types, defaults, constraints, and required fields.
3. Document error conditions and their observable causes.
4. Run each example against the current interface.
5. Cite the implementation or schema behind each behavioral claim.

## Output contract

A document that answers the reader's question, with structure, examples and an owner.

## Validation checklist

- [ ] The document answers its stated question
- [ ] Examples are runnable and current
- [ ] Every claim can be traced to a source

## Safety notes

Never document a command you have not run, and never leave an internal secret in an example.

## Related skills

- `write-a-changelog`
- `write-a-checklist-in-a-runbook`
- `write-a-comparison-table-of-options`
