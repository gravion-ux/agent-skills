---
name: add-subtitles-and-captions
description: Add subtitles that match the spoken audio exactly and stay readable on a small screen. Use when the user wants captions on a finished video.
domain: video-audio
tags: [subtitles, captions, accessibility]
triggers: ["add subtitles and captions to a video", "caption a finished video", "put readable subtitles on footage"]
---

# Add subtitles that match the spoken audio exactly and stay readable on a small screen

## Purpose

Add subtitles that match the spoken audio exactly and stay readable on a small screen.

## When to use

Use when the user wants captions on a finished video.

## When NOT to use

Do not use this for a still image; use image-visual instead.

## Inputs required

- The source material and the target duration
- The format, the channels and the captions
- The rights and the music licensing constraints

## Procedure

1. Transcribe the spoken audio word for word and keep the original wording.
2. Break the caption into lines of at most seven words and two lines per caption.
3. Keep each caption on screen for at least one and a half seconds.
4. Mark speaker changes and non-speech sounds in the caption style.
5. Play the video muted and check that every caption still reads clearly.

## Output contract

An edited audio or video file with a transcript or caption track and the source list.

## Validation checklist

- [ ] The audio is intelligible at normal volume
- [ ] Captions or a transcript are attached
- [ ] Every clip is licensed

## Safety notes

Never publish audio or footage of a person without consent, and never strip attribution from licensed media.

## Related skills

- `add-a-lower-third-and-branding`
- `mix-audio-levels-for-speech-and-music`
- `write-a-video-description-and-metadata`
