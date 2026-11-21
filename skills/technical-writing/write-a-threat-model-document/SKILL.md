---
name: write-a-threat-model-document
description: Write a threat model that lists the assets, the attackers and the controls that matter. Use when the user wants to document the security risks of a system or a design.
domain: technical-writing
tags: [threat-model, security, risk]
triggers: ["write a threat model document", "document the security risks of a design", "threat model for a new system"]
---

# Write a threat model that lists the assets, the attackers and the controls that matter

## Purpose

Write a threat model that lists the assets, the attackers and the controls that matter.

## When to use

Use when the user wants to document the security risks of a system or a design.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. List the assets worth protecting and what makes each of them sensitive.
2. Describe the entry points where untrusted input reaches the system.
3. List the realistic attackers and what each of them wants.
4. Rate each threat by impact and likelihood using the same scale throughout.
5. Name the control for each threat and record what is accepted without a control.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `convert-a-meeting-recording-into-a-document`
- `edit-a-document-for-clarity`
- `review-a-technical-document-for-accuracy`
