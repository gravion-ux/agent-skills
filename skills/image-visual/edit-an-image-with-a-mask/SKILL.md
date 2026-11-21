---
name: edit-an-image-with-a-mask
description: Apply a masked edit to a raster image while preserving pixels outside the selected region. Use when the user wants a localized change to one part of an existing still image.
domain: image-visual
tags: [image-editing, masking, raster-edit]
triggers: ["edit an image with a mask", "masked raster image edit", "change one region of an image"]
---

# Apply a masked edit to a raster image while preserving pixels outside the selected region

## Purpose

Apply a masked edit to a raster image while preserving pixels outside the selected region.

## When to use

Use when the user wants a localized change to one part of an existing still image.

## When NOT to use

Do not use this for a motion asset; use video-audio instead.

## Inputs required

- The subject and the intended use
- The style, aspect ratio and resolution
- The licensing and brand constraints

## Procedure

1. Inspect the source dimensions, format, color space, and licensing before editing.
2. Create a mask that covers the target region with a controlled feathered edge.
3. Apply the edit only within the mask and keep the original as the source layer.
4. Check the boundary for halos, color shifts, and lost detail.
5. Export the revised image and record the mask and edit history.

## Output contract

A finished visual asset at the requested size, with its prompt or edit history recorded.

## Validation checklist

- [ ] The asset matches the required dimensions
- [ ] No unlicensed or trademarked material is present
- [ ] Text in the image is legible

## Safety notes

Never create or edit an image of a real person without consent, and never reuse licensed material.

## Related skills

- `prepare-an-image-set-for-a-release`
- `check-an-image-for-brand-and-safety-issues`
- `design-a-poster-for-an-event`
