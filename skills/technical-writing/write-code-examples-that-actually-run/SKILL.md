---
name: write-code-examples-that-actually-run
description: Write code examples that are verified by running them before they are published. Use when the user wants examples in a document that will not be wrong when copied.
domain: technical-writing
tags: [code-example, verification, accuracy]
triggers: ["write code examples that actually run", "examples in my docs are broken", "verify every snippet before publishing"]
---

# Write code examples that are verified by running them before they are published

## Purpose

Write code examples that are verified by running them before they are published.

## When to use

Use when the user wants examples in a document that will not be wrong when copied.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. Write the example as a complete, runnable program rather than as a fragment.
2. Run it in a clean environment with the documented dependencies.
3. Check the output matches what the document says it will be.
4. Remove the setup noise from the shown output but keep the meaningful result.
5. Check the example against the current version of the interface before publishing.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `write-a-benchmark-report`
- `write-a-comparison-of-two-approaches`
- `write-a-migration-plan-for-users`
