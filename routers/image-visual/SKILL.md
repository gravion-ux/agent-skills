---
name: router-image-visual
description: Route work in the Image and visual creation domain to the right leaf skill. Use when a task clearly belongs to image-visual.
domain: image-visual
tags: [router, routing, image-visual]
triggers: ["route a image-visual task", "which image-visual skill should I use"]
---

# Image and visual creation router

## Purpose

List every leaf skill in the image-visual domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside image-visual and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for a motion asset; use video-audio instead.

## Inputs required

- The subject and the intended use
- The style, aspect ratio and resolution
- The licensing and brand constraints

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

A finished visual asset at the requested size, with its prompt or edit history recorded.

## Validation checklist

- [ ] The asset matches the required dimensions
- [ ] No unlicensed or trademarked material is present
- [ ] Text in the image is legible

## Safety notes

Never create or edit an image of a real person without consent, and never reuse licensed material.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `batch-generate-a-variant-set` | Use when the user needs many reproducible still-image variants from a defined prompt and grid. |
| `build-a-moodboard` | Use when the user needs to collect visual references and define a shared creative direction. |
| `build-a-product-photo-set` | Use when the user needs several still views of one product for a listing or campaign. |
| `build-a-style-guide-for-visuals` | Use when the user needs an enforceable visual standard for a brand or creative team. |
| `check-an-image-for-brand-and-safety-issues` | Use when the user needs a completed still image reviewed before publication or distribution. |
| `create-a-flat-illustration` | Use when the user wants a simple vector-style illustration for digital or print use. |
| `create-a-logo-concept` | Use when the user needs an original still logo concept for brand exploration. |
| `create-an-infographic` | Use when the user needs to communicate facts, steps, or comparisons in a static visual. |
| `design-a-poster-for-an-event` | Use when the user needs a static poster for an event, announcement, or campaign. |
| `design-a-social-media-graphic` | Use when the user needs a single still graphic for a social media post or campaign. |
| `edit-an-image-with-a-mask` | Use when the user wants a localized change to one part of an existing still image. |
| `generate-a-product-shot` | Use when the user needs a still product image for a listing, catalogue, or campaign. |
| `generate-a-storyboard-frame` | Use when the user needs a still storyboard frame for planning a sequence or production. |
| `iterate-on-an-image-prompt` | Use when the user wants to improve a still-image prompt after reviewing generated results. |
| `keep-character-consistency-across-images` | Use when the user needs one character to remain recognizable across several still images. |
| `make-a-diagram-from-a-description` | Use when the user has a process or architecture description that must become a static diagram. |
| `prepare-an-image-set-for-a-release` | Use when the user needs a still-image release bundle assembled from approved source assets. |
| `remove-a-background-from-a-photo` | Use when the user needs a subject isolated from a photo for reuse in a new composition. |
| `upscale-and-clean-up-a-raster-image` | Use when the user needs a noisy or low-resolution still image prepared for larger display. |
| `write-a-detailed-image-generation-prompt` | Use when the user needs a production-ready prompt for a specific still image. |
| `write-a-visual-brief-for-a-designer` | Use when the user needs to hand a still-visual project to another designer or studio. |
| `write-an-image-prompt-for-each-brand-asset` | Use when the user needs generation prompts for a defined set of brand deliverables. |
