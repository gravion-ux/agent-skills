---
name: iterate-on-an-image-prompt
description: Refine an image-generation prompt through controlled revisions while preserving successful details. Use when the user wants to improve a still-image prompt after reviewing generated results.
domain: image-visual
tags: [prompt-iteration, image-generation, revision]
triggers: ["iterate on an image prompt", "revise an image generation prompt", "improve a still image prompt"]
---

# Refine an image-generation prompt through controlled revisions while preserving successful details

## Purpose

Refine an image-generation prompt through controlled revisions while preserving successful details.

## When to use

Use when the user wants to improve a still-image prompt after reviewing generated results.

## When NOT to use

Do not use this for a motion asset; use video-audio instead.

## Inputs required

- The subject and the intended use
- The style, aspect ratio and resolution
- The licensing and brand constraints

## Procedure

1. Compare the prompt against the latest output and list the mismatched requirements.
2. Change one visual variable at a time and label the intended effect.
3. Retain prompts that resolve the gap and record them as named variants.
4. Stop when the output meets the brief and record the final prompt.

## Output contract

A finished visual asset at the requested size, with its prompt or edit history recorded.

## Validation checklist

- [ ] The asset matches the required dimensions
- [ ] No unlicensed or trademarked material is present
- [ ] Text in the image is legible

## Safety notes

Never create or edit an image of a real person without consent, and never reuse licensed material.

## Related skills

- `write-an-image-prompt-for-each-brand-asset`
- `check-an-image-for-brand-and-safety-issues`
- `edit-an-image-with-a-mask`
