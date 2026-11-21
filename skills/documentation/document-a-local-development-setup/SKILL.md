---
name: document-a-local-development-setup
description: Set up a reproducible local development environment with verified commands and checkpoints. Use when the user wants a local development setup that another contributor can reproduce.
domain: documentation
tags: [local-development, environment, reproducibility]
triggers: ["local development setup", "document a local dev setup", "reproduce the dev environment"]
---

# Set up a reproducible local development environment with verified commands and checkpoints

## Purpose

Set up a reproducible local development environment with verified commands and checkpoints.

## When to use

Use when the user wants a local development setup that another contributor can reproduce.

## When NOT to use

Do not use this for a persuasive article or campaign copy; use content-creation instead.

## Inputs required

- The audience and what they must be able to do
- The subject and the source material
- The format and the maintenance owner

## Procedure

1. State supported operating systems, runtimes, tools, and exact versions.
2. List prerequisites and clone or download steps for the project.
3. Run every installation and configuration command from a clean machine.
4. Add checks for starting the service and running the test suite.
5. Troubleshoot the first likely failure without exposing local secret values.

## Output contract

A document that answers the reader's question, with structure, examples and an owner.

## Validation checklist

- [ ] The document answers its stated question
- [ ] Examples are runnable and current
- [ ] Every claim can be traced to a source

## Safety notes

Never document a command you have not run, and never leave an internal secret in an example.

## Related skills

- `document-a-configuration-option`
- `document-a-third-party-integration`
- `structure-a-document-for-scanning`
