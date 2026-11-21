---
name: compress-a-video-for-web-delivery
description: Compress a video for the web by choosing a target size, an encoding preset and a checked result. Use when the user wants a video file that loads quickly without visible damage.
domain: video-audio
tags: [compression, encoding, delivery]
triggers: ["compress a video for web delivery", "make a video file smaller for the web", "re-encode a video for faster loading"]
---

# Compress a video for the web by choosing a target size, an encoding preset and a checked result

## Purpose

Compress a video for the web by choosing a target size, an encoding preset and a checked result.

## When to use

Use when the user wants a video file that loads quickly without visible damage.

## When NOT to use

Do not use this for a still image; use image-visual instead.

## Inputs required

- The source material and the target duration
- The format, the channels and the captions
- The rights and the music licensing constraints

## Procedure

1. Set the target file size and the resolution the page actually renders.
2. Choose the codec and a constant quality preset for that target.
3. Export a short sample at that setting and watch it on a real screen.
4. Adjust the quality value and re-export the sample until the artefacts are gone.
5. Render the full file and confirm the size and the duration match the source.

## Output contract

An edited audio or video file with a transcript or caption track and the source list.

## Validation checklist

- [ ] The audio is intelligible at normal volume
- [ ] Captions or a transcript are attached
- [ ] Every clip is licensed

## Safety notes

Never publish audio or footage of a person without consent, and never strip attribution from licensed media.

## Related skills

- `build-a-subtitle-file-for-a-video`
- `check-a-video-for-accessibility`
- `create-a-thumbnail-for-a-video`
