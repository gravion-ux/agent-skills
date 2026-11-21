---
name: upscale-and-clean-up-a-raster-image
description: Upscale and clean a raster image while preserving detail and checking for generated artifacts. Use when the user needs a noisy or low-resolution still image prepared for larger display.
domain: image-visual
tags: [image-upscaling, restoration, raster-cleanup]
triggers: ["upscale and clean up an image", "restore a low-resolution photo", "denoise and enlarge a raster image"]
---

# Upscale and clean a raster image while preserving detail and checking for generated artifacts

## Purpose

Upscale and clean a raster image while preserving detail and checking for generated artifacts.

## When to use

Use when the user needs a noisy or low-resolution still image prepared for larger display.

## When NOT to use

Do not use this for a motion asset; use video-audio instead.

## Inputs required

- The subject and the intended use
- The style, aspect ratio and resolution
- The licensing and brand constraints

## Procedure

1. Inspect the source for sharpness, compression blocks, noise, and existing artifacts.
2. Set the target dimensions and choose an upscale method suited to the image type.
3. Apply denoising conservatively and compare detail against the original.
4. Inspect edges, faces, text, and textures for invented or smeared features.
5. Export at the requested size and record the tool, settings, and source file.

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
- `edit-an-image-with-a-mask`
- `prepare-an-image-set-for-a-release`
