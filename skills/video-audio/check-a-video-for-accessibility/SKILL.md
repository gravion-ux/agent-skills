---
name: check-a-video-for-accessibility
description: Check a video for accessibility by testing the captions, the overlay contrast and the audio description need. Use when the user wants a finished video checked before it is published.
domain: video-audio
tags: [accessibility, captions, review]
triggers: ["check a video for accessibility", "audit a video before publishing it", "verify a video meets accessibility rules"]
---

# Check a video for accessibility by testing the captions, the overlay contrast and the audio description need

## Purpose

Check a video for accessibility by testing the captions, the overlay contrast and the audio description need.

## When to use

Use when the user wants a finished video checked before it is published.

## When NOT to use

Do not use this for a still image; use image-visual instead.

## Inputs required

- The source material and the target duration
- The format, the channels and the captions
- The rights and the music licensing constraints

## Procedure

1. Play the video with the sound off and confirm the captions carry the meaning.
2. Extract every text overlay and compare its contrast against the frame behind it.
3. Check the caption accuracy against the transcript for every section.
4. Decide whether the visual content needs an audio description track.
5. Write the findings with the timestamp and the fix for each issue.

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
- `compress-a-video-for-web-delivery`
- `create-a-thumbnail-for-a-video`
