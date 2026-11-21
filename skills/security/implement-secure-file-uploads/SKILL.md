---
name: implement-secure-file-uploads
description: Implement file uploads that constrain content, isolate storage, and block executable delivery. Use when the user needs an application to accept user files without exposing unsafe content.
domain: security
tags: [file-upload, malware-scanning, content-validation]
triggers: ["implement secure file uploads", "harden an upload endpoint", "safely accept user uploaded files"]
---

# Implement file uploads that constrain content, isolate storage, and block executable delivery

## Purpose

Implement file uploads that constrain content, isolate storage, and block executable delivery.

## When to use

Use when the user needs an application to accept user files without exposing unsafe content.

## When NOT to use

Do not use this for general availability tuning; use observability instead.

## Inputs required

- The system, asset or data in scope
- The threat model and the attacker capability
- The compliance or audit obligation

## Procedure

1. Define allowed extensions, content types, size limits, and maximum upload duration.
2. Store uploads outside the public root under random names with generated directory separation.
3. Validate the detected content type against the file signature and reject mismatches.
4. Scan uploads for malware and block executable or archive-expansion content before release.
5. Serve approved downloads with safe content headers and verify denial of oversized or disguised files.

## Output contract

A finding with evidence, impact, a concrete fix and a verification step.

## Validation checklist

- [ ] The finding is reproducible
- [ ] The fix closes the path rather than hiding the symptom
- [ ] No secret appears in the output or the diff

## Safety notes

Never test against a system without written authorisation, and never print credentials while investigating.

## Related skills

- `implement-secure-session-handling`
- `implement-data-retention-controls`
- `secure-a-ci-pipeline-with-oidc`
