---
name: write-an-image-prompt-for-each-brand-asset
description: Produce a prompt matrix that adapts one visual brief to every required brand asset. Use when the user needs generation prompts for a defined set of brand deliverables.
domain: image-visual
tags: [brand-prompts, asset-matrix, image-generation]
triggers: ["write an image prompt for each brand asset", "create a brand asset prompt matrix", "prompt every planned brand image"]
---

# Produce a prompt matrix that adapts one visual brief to every required brand asset

## Purpose

Produce a prompt matrix that adapts one visual brief to every required brand asset.

## When to use

Use when the user needs generation prompts for a defined set of brand deliverables.

## When NOT to use

Do not use this for a motion asset; use video-audio instead.

## Inputs required

- The subject and the intended use
- The style, aspect ratio and resolution
- The licensing and brand constraints

## Procedure

1. List each required brand asset with its size, placement, and channel.
2. Assign the shared visual direction, palette, typography, and logo treatment.
3. Write one asset-specific prompt that states subject, composition, text, and exclusions.
4. Verify that the prompts remain consistent while fitting each asset's dimensions.
5. Store the prompt matrix with filenames, versions, and usage rights.

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
- `iterate-on-an-image-prompt`
- `prepare-an-image-set-for-a-release`
