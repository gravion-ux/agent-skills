---
name: keep-character-consistency-across-images
description: Build a reusable character reference set that keeps appearance consistent across still images. Use when the user needs one character to remain recognizable across several still images.
domain: image-visual
tags: [character-consistency, reference-sheet, image-generation]
triggers: ["keep character consistent across images", "character consistency image set", "consistent character reference sheet"]
---

# Build a reusable character reference set that keeps appearance consistent across still images

## Purpose

Build a reusable character reference set that keeps appearance consistent across still images.

## When to use

Use when the user needs one character to remain recognizable across several still images.

## When NOT to use

Do not use this for a motion asset; use video-audio instead.

## Inputs required

- The subject and the intended use
- The style, aspect ratio and resolution
- The licensing and brand constraints

## Procedure

1. Define the character's non-sensitive facial, hair, clothing, and silhouette traits.
2. Record the fixed traits in a reusable reference sheet and prompt block.
3. Generate a neutral reference view before adding any scene.
4. Attach the same reference and trait block to every scene prompt.
5. Check each output for drift and revise only the traits that changed.
6. Confirm documented consent before using a real person's appearance.

## Output contract

A finished visual asset at the requested size, with its prompt or edit history recorded.

## Validation checklist

- [ ] The asset matches the required dimensions
- [ ] No unlicensed or trademarked material is present
- [ ] Text in the image is legible

## Safety notes

Never create or edit an image of a real person without consent, and never reuse licensed material.

## Related skills

- `batch-generate-a-variant-set`
- `build-a-moodboard`
- `build-a-product-photo-set`
