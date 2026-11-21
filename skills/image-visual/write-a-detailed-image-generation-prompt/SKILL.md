---
name: write-a-detailed-image-generation-prompt
description: Write a detailed image-generation prompt that fixes subject, composition, lighting, and finish. Use when the user needs a production-ready prompt for a specific still image.
domain: image-visual
tags: [image-prompt, generation, composition]
triggers: ["detailed image generation prompt", "write an image prompt", "prompt for a still image"]
---

# Write a detailed image-generation prompt that fixes subject, composition, lighting, and finish

## Purpose

Write a detailed image-generation prompt that fixes subject, composition, lighting, and finish.

## When to use

Use when the user needs a production-ready prompt for a specific still image.

## When NOT to use

Do not use this for a motion asset; use video-audio instead.

## Inputs required

- The subject and the intended use
- The style, aspect ratio and resolution
- The licensing and brand constraints

## Procedure

1. Record the subject, intended use, and required aspect ratio.
2. Specify composition, camera angle, lighting, palette, and material detail.
3. Name the rendering style and the exclusions that prevent common artifacts.
4. State any required text exactly and note where it must remain legible.
5. Record the final prompt alongside its format, resolution, and usage constraints.

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
- `edit-an-image-with-a-mask`
- `iterate-on-an-image-prompt`
