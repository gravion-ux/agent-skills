---
name: document-a-third-party-integration
description: Document an integration's setup, data flow, limits, failures, and ownership boundaries. Use when the user wants documentation for a product that connects to a third-party service.
domain: documentation
tags: [integration, third-party, data-flow]
triggers: ["third-party integration guide", "document a third-party integration", "integration setup and limits"]
---

# Document an integration's setup, data flow, limits, failures, and ownership boundaries

## Purpose

Document an integration's setup, data flow, limits, failures, and ownership boundaries.

## When to use

Use when the user wants documentation for a product that connects to a third-party service.

## When NOT to use

Do not use this for a persuasive article or campaign copy; use content-creation instead.

## Inputs required

- The audience and what they must be able to do
- The subject and the source material
- The format and the maintenance owner

## Procedure

1. Read the provider contract and the local integration implementation.
2. List prerequisites and required credential names without their values.
3. Trace data from request to response and identify provider dependencies.
4. Document quotas, timeouts, retry rules, and common failure responses.
5. State which team owns configuration, support, and provider changes.

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
- `document-a-local-development-setup`
- `structure-a-document-for-scanning`
