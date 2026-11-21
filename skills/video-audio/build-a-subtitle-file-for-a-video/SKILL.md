---
name: build-a-subtitle-file-for-a-video
description: Build a subtitle file with correct timings, a clean cue format and a match to the final edit. Use when the user needs a caption file that matches a finished edit.
domain: video-audio
tags: [subtitle, srt, timing]
triggers: ["build a subtitle file for a video", "export a caption file for a video", "make an srt from a finished edit"]
---

# Build a subtitle file with correct timings, a clean cue format and a match to the final edit

## Purpose

Build a subtitle file with correct timings, a clean cue format and a match to the final edit.

## When to use

Use when the user needs a caption file that matches a finished edit.

## When NOT to use

Do not use this for a still image; use image-visual instead.

## Inputs required

- The source material and the target duration
- The format, the channels and the captions
- The rights and the music licensing constraints

## Procedure

1. Run the transcription pass over the final edit and write one cue per spoken sentence.
2. Split each cue into lines of at most seven words and two lines per cue.
3. Set the timing offset so the first cue lands on the spoken word.
4. Save the file in the format the delivery platform expects.
5. Play the video with the file loaded and check the first and the last cue.

## Output contract

An edited audio or video file with a transcript or caption track and the source list.

## Validation checklist

- [ ] The audio is intelligible at normal volume
- [ ] Captions or a transcript are attached
- [ ] Every clip is licensed

## Safety notes

Never publish audio or footage of a person without consent, and never strip attribution from licensed media.

## Related skills

- `check-a-video-for-accessibility`
- `compress-a-video-for-web-delivery`
- `create-a-thumbnail-for-a-video`
