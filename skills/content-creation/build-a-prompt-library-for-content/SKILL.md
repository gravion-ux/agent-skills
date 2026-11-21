---
name: build-a-prompt-library-for-content
description: Assemble reusable content prompts with slots for audience, format and source material. Use when the user wants reusable prompts for drafting and editing content.
domain: content-creation
tags: [prompt-library, reusable-prompts, workflow]
triggers: ["build a prompt library for content", "reusable prompts for writing", "content prompt templates"]
---

# Assemble reusable content prompts with slots for audience, format and source material

## Purpose

Assemble reusable content prompts with slots for audience, format and source material.

## When to use

Use when the user wants reusable prompts for drafting and editing content.

## When NOT to use

Do not use this for internal engineering documentation; use technical-writing instead.

## Inputs required

- The platform and the format
- The audience and the tone
- The source material, the hook and the call to action

## Procedure

1. Collect the recurring content tasks that need a prompt.
2. Write one prompt template per task with slots for audience, format and topic.
3. Define the required output format and length inside each prompt.
4. Add a sourcing instruction and an approval step to every template.
5. Store the prompts in one named list with a short usage note each.

## Output contract

A publishable draft in the target format, with a title, hook, body and close.

## Validation checklist

- [ ] The opening earns the next sentence
- [ ] The draft matches the platform's format and length
- [ ] Every factual claim is sourced

## Safety notes

Never publish without approval, and never present generated statistics as real data.

## Related skills

- `build-a-content-brief-for-a-writer`
- `check-a-draft-for-plagiarism-risk`
- `create-a-content-series`
