---
name: batch-generate-a-variant-set
description: Batch-generate a controlled variant set and log the parameters for every resulting asset. Use when the user needs many reproducible still-image variants from a defined prompt and grid.
domain: image-visual
tags: [batch-generation, variant-testing, image-pipeline]
triggers: ["batch generate an image variant set", "generate many prompt variants automatically", "run a controlled image variation batch"]
---

# Batch-generate a controlled variant set and log the parameters for every resulting asset

## Purpose

Batch-generate a controlled variant set and log the parameters for every resulting asset.

## When to use

Use when the user needs many reproducible still-image variants from a defined prompt and grid.

## When NOT to use

Do not use this for a motion asset; use video-audio instead.

## Inputs required

- The subject and the intended use
- The style, aspect ratio and resolution
- The licensing and brand constraints

## Procedure

1. Define the fixed prompt, variable parameters, candidate count, and output dimensions.
2. Run one generation per parameter combination with stable seeds where supported.
3. Save each output with its full parameter set and an index matching the batch order.
4. Screen candidates for anatomy, text, artifacts, and consistency with the base brief.
5. Rank the passing variants and record the selected outputs for delivery.

## Output contract

A finished visual asset at the requested size, with its prompt or edit history recorded.

## Validation checklist

- [ ] The asset matches the required dimensions
- [ ] No unlicensed or trademarked material is present
- [ ] Text in the image is legible

## Safety notes

Never create or edit an image of a real person without consent, and never reuse licensed material.

## Related skills

- `build-a-product-photo-set`
- `generate-a-product-shot`
- `generate-a-storyboard-frame`
