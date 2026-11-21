---
name: write-a-technical-tutorial-for-developers
description: Write a tutorial that takes a developer from nothing to a working result. Use when the user wants to teach a developer how to do something with the product or the library.
domain: technical-writing
tags: [tutorial, developers, instruction]
triggers: ["write a technical tutorial for developers", "getting started guide for engineers", "step by step developer walkthrough"]
---

# Write a tutorial that takes a developer from nothing to a working result

## Purpose

Write a tutorial that takes a developer from nothing to a working result.

## When to use

Use when the user wants to teach a developer how to do something with the product or the library.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. State what the reader will have working at the end.
2. List the prerequisites and the version they need.
3. Give the setup steps first, so the later steps cannot fail on a missing dependency.
4. Build the tutorial in small steps, each of which leaves the code working.
5. End with the exercise that proves the reader understood it rather than copied it.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `review-a-technical-document-for-accuracy`
- `write-a-migration-plan-for-users`
- `write-a-runbook-for-an-operational-task`
