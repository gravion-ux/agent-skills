---
name: write-a-readme-for-a-project
description: Explain what a project does, how to install it, and how to verify a successful setup. Use when the user needs a project README that gives a new reader a clear path to first success.
domain: documentation
tags: [readme, project-setup, entry-point]
triggers: ["project readme", "write a project readme", "readme for a repository"]
---

# Explain what a project does, how to install it, and how to verify a successful setup

## Purpose

Explain what a project does, how to install it, and how to verify a successful setup.

## When to use

Use when the user needs a project README that gives a new reader a clear path to first success.

## When NOT to use

Do not use this for a persuasive article or campaign copy; use content-creation instead.

## Inputs required

- The audience and what they must be able to do
- The subject and the source material
- The format and the maintenance owner

## Procedure

1. Read the project manifest and existing setup instructions.
2. State the problem, supported use cases, and maintenance owner.
3. Document prerequisites, installation, verification, and common next steps.
4. Run every setup command and replace it with the recorded successful output.
5. Remove credentials, private URLs, and undocumented claims from examples.

## Output contract

A document that answers the reader's question, with structure, examples and an owner.

## Validation checklist

- [ ] The document answers its stated question
- [ ] Examples are runnable and current
- [ ] Every claim can be traced to a source

## Safety notes

Never document a command you have not run, and never leave an internal secret in an example.

## Related skills

- `write-a-decision-record-for-a-team`
- `write-a-release-note-for-users`
- `structure-a-document-for-scanning`
