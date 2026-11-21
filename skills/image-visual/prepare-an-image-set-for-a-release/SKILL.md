---
name: prepare-an-image-set-for-a-release
description: Prepare and package a release image set with approved variants, metadata, and final checks. Use when the user needs a still-image release bundle assembled from approved source assets.
domain: image-visual
tags: [asset-release, packaging, visual-qa]
triggers: ["prepare an image set for release", "package approved release images", "assemble a visual asset release bundle"]
---

# Prepare and package a release image set with approved variants, metadata, and final checks

## Purpose

Prepare and package a release image set with approved variants, metadata, and final checks.

## When to use

Use when the user needs a still-image release bundle assembled from approved source assets.

## When NOT to use

Do not use this for a motion asset; use video-audio instead.

## Inputs required

- The subject and the intended use
- The style, aspect ratio and resolution
- The licensing and brand constraints

## Procedure

1. Collect the approved assets and the required filenames, formats, and dimensions.
2. Export each item from its source of truth to the specified color and file format.
3. Run dimension, text-legibility, rights, and naming checks on every file.
4. Generate a manifest listing each asset, purpose, dimensions, and version.
5. Package the set in the agreed folder and archive without altering the originals.

## Output contract

A finished visual asset at the requested size, with its prompt or edit history recorded.

## Validation checklist

- [ ] The asset matches the required dimensions
- [ ] No unlicensed or trademarked material is present
- [ ] Text in the image is legible

## Safety notes

Never create or edit an image of a real person without consent, and never reuse licensed material.

## Related skills

- `check-an-image-for-brand-and-safety-issues`
- `design-a-poster-for-an-event`
- `edit-an-image-with-a-mask`
