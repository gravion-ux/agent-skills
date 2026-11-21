---
name: clean-up-audio-noise
description: Clean up audio noise by removing hum, hiss and rumble while keeping the voice natural. Use when the user wants a noisy recording to sound usable.
domain: video-audio
tags: [audio, cleanup, noise]
triggers: ["clean up audio noise", "remove hiss and hum from a recording", "reduce background noise in a track"]
---

# Clean up audio noise by removing hum, hiss and rumble while keeping the voice natural

## Purpose

Clean up audio noise by removing hum, hiss and rumble while keeping the voice natural.

## When to use

Use when the user wants a noisy recording to sound usable.

## When NOT to use

Do not use this for a still image; use image-visual instead.

## Inputs required

- The source material and the target duration
- The format, the channels and the captions
- The rights and the music licensing constraints

## Procedure

1. Listen to the noise floor and name the dominant sound in it.
2. Apply a noise reduction pass at the lowest setting that removes the hiss.
3. Cut the hum at its source frequency with a narrow filter.
4. High-pass the low rumble below the lowest voice frequency you need.
5. Compare the treated track with the original and confirm the voice still sounds natural.

## Output contract

An edited audio or video file with a transcript or caption track and the source list.

## Validation checklist

- [ ] The audio is intelligible at normal volume
- [ ] Captions or a transcript are attached
- [ ] Every clip is licensed

## Safety notes

Never publish audio or footage of a person without consent, and never strip attribution from licensed media.

## Related skills

- `mix-audio-levels-for-speech-and-music`
- `add-a-lower-third-and-branding`
- `add-subtitles-and-captions`
