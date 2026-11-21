---
name: document-an-api-for-consumers
description: Define a consumer-facing API contract with authentication, requests, responses, and errors. Use when the user wants API documentation that lets a consumer integrate without reading the code.
domain: documentation
tags: [api, consumers, integration]
triggers: ["consumer api documentation", "document an api for consumers", "api contract for consumers"]
---

# Define a consumer-facing API contract with authentication, requests, responses, and errors

## Purpose

Define a consumer-facing API contract with authentication, requests, responses, and errors.

## When to use

Use when the user wants API documentation that lets a consumer integrate without reading the code.

## When NOT to use

Do not use this for a persuasive article or campaign copy; use content-creation instead.

## Inputs required

- The audience and what they must be able to do
- The subject and the source material
- The format and the maintenance owner

## Procedure

1. Inspect the route schema, handler, and current contract tests.
2. Describe authentication requirements without exposing any credential value.
3. Provide request and response examples with sensitive fields removed.
4. Document validation failures, error payloads, and retry behavior.
5. Run each example against a test service and compare the output.

## Output contract

A document that answers the reader's question, with structure, examples and an owner.

## Validation checklist

- [ ] The document answers its stated question
- [ ] Examples are runnable and current
- [ ] Every claim can be traced to a source

## Safety notes

Never document a command you have not run, and never leave an internal secret in an example.

## Related skills

- `document-an-error-code-and-its-fix`
- `structure-a-document-for-scanning`
- `write-an-onboarding-guide-for-users`
