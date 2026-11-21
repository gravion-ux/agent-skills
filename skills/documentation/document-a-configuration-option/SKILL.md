---
name: document-a-configuration-option
description: Define one configuration option with its type, default, behavior, and safe examples. Use when the user needs a configuration option documented for adoption and support.
domain: documentation
tags: [configuration, options, reference]
triggers: ["configuration option reference", "document a configuration option", "configuration setting docs"]
---

# Define one configuration option with its type, default, behavior, and safe examples

## Purpose

Define one configuration option with its type, default, behavior, and safe examples.

## When to use

Use when the user needs a configuration option documented for adoption and support.

## When NOT to use

Do not use this for a persuasive article or campaign copy; use content-creation instead.

## Inputs required

- The audience and what they must be able to do
- The subject and the source material
- The format and the maintenance owner

## Procedure

1. Locate the option definition and its validation rules.
2. Record the accepted type, default value, and scope.
3. Explain the behavior when the option is enabled or omitted.
4. Show a configuration example with environment variable names but no secret values.
5. Run the example and verify the documented default behavior.

## Output contract

A document that answers the reader's question, with structure, examples and an owner.

## Validation checklist

- [ ] The document answers its stated question
- [ ] Examples are runnable and current
- [ ] Every claim can be traced to a source

## Safety notes

Never document a command you have not run, and never leave an internal secret in an example.

## Related skills

- `document-a-local-development-setup`
- `document-a-third-party-integration`
- `structure-a-document-for-scanning`
