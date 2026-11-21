---
name: remove-a-background-from-a-photo
description: Remove a photo background while preserving subject edges, hair, transparency, and color. Use when the user needs a subject isolated from a photo for reuse in a new composition.
domain: image-visual
tags: [background-removal, photo-cutout, edge-refinement]
triggers: ["remove a photo background", "cut a subject out of a photo", "isolate a photo subject"]
---

# Remove a photo background while preserving subject edges, hair, transparency, and color

## Purpose

Remove a photo background while preserving subject edges, hair, transparency, and color.

## When to use

Use when the user needs a subject isolated from a photo for reuse in a new composition.

## When NOT to use

Do not use this for a motion asset; use video-audio instead.

## Inputs required

- The subject and the intended use
- The style, aspect ratio and resolution
- The licensing and brand constraints

## Procedure

1. Confirm the source image is licensed and consent exists to edit any identifiable person.
2. Select the subject with an edge-aware mask and refine hair or transparent details.
3. Check the cutout for clipped edges, halos, and leftover background fragments.
4. Export the subject with transparency or the requested solid background.
5. Record the masking and cleanup steps with the exported file.

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
- `make-a-diagram-from-a-description`
- `batch-generate-a-variant-set`
