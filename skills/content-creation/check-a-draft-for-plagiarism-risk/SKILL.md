---
name: check-a-draft-for-plagiarism-risk
description: Scan a draft for passages that overlap too closely with published sources. Use when the user is worried a draft contains borrowed wording.
domain: content-creation
tags: [plagiarism, originality, sourcing]
triggers: ["check a draft for plagiarism risk", "is this draft plagiarised", "similarity check on my draft"]
---

# Scan a draft for passages that overlap too closely with published sources

## Purpose

Scan a draft for passages that overlap too closely with published sources.

## When to use

Use when the user is worried a draft contains borrowed wording.

## When NOT to use

Do not use this for internal engineering documentation; use technical-writing instead.

## Inputs required

- The platform and the format
- The audience and the tone
- The source material, the hook and the call to action

## Procedure

1. Extract the passages that sound unusually close to a known source.
2. Run each passage through a similarity checker and record the matching source.
3. Compare the matched passages with the draft's citations and reference list.
4. Rewrite overlapping sections in original language or quote them with attribution.
5. Report the remaining risky passages with the source that matched each one.

## Output contract

A publishable draft in the target format, with a title, hook, body and close.

## Validation checklist

- [ ] The opening earns the next sentence
- [ ] The draft matches the platform's format and length
- [ ] Every factual claim is sourced

## Safety notes

Never publish without approval, and never present generated statistics as real data.

## Related skills

- `edit-a-draft-for-clarity`
- `fact-check-a-draft`
- `build-a-content-brief-for-a-writer`
