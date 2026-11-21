---
name: write-an-api-design-document
description: Write an API design document that covers the contract, the errors and the versioning. Use when the user needs to document the design of an interface before it is built.
domain: technical-writing
tags: [api, design, contract]
triggers: ["write an api design document", "document an interface before it is built", "api contract design write up"]
---

# Write an API design document that covers the contract, the errors and the versioning

## Purpose

Write an API design document that covers the contract, the errors and the versioning.

## When to use

Use when the user needs to document the design of an interface before it is built.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. Describe the resources or operations and the model they use.
2. Define each request and response with its fields and their types.
3. List the error conditions and the code each one returns.
4. State the versioning policy and how compatibility is protected.
5. Give one complete worked example for the main operation.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `write-an-engineering-design-doc`
- `write-a-runbook-for-an-operational-task`
- `write-a-threat-model-document`
