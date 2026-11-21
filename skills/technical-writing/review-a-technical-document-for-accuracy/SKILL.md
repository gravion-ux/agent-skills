---
name: review-a-technical-document-for-accuracy
description: Review a technical document for accuracy by checking every claim against its source. Use when the user wants a technical document checked before it is published or circulated.
domain: technical-writing
tags: [review, accuracy, verification]
triggers: ["review a technical document for accuracy", "fact check this technical doc", "verify the claims in my write up"]
---

# Review a technical document for accuracy by checking every claim against its source

## Purpose

Review a technical document for accuracy by checking every claim against its source.

## When to use

Use when the user wants a technical document checked before it is published or circulated.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. List every factual and technical claim in the document.
2. Check each one against the code, the measurement or the source it cites.
3. Flag the claims that cannot be verified and say what would verify them.
4. Check that the version and the date in the document match the current state.
5. Check that the examples still run and the commands still produce the stated output.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `edit-a-document-for-clarity`
- `write-a-technical-tutorial-for-developers`
- `convert-a-meeting-recording-into-a-document`
