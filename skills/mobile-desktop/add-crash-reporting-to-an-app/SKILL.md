---
name: add-crash-reporting-to-an-app
description: Add privacy-safe crash reporting with redaction, deduplication, and release comparison. Use when the user needs to add crash reporting to a mobile or desktop application.
domain: mobile-desktop
tags: [crash-reporting, diagnostics, privacy]
triggers: ["app crash reporting", "add privacy-safe crash reports", "compare crashes across releases"]
---

# Add privacy-safe crash reporting with redaction, deduplication, and release comparison

## Purpose

Add privacy-safe crash reporting with redaction, deduplication, and release comparison.

## When to use

Use when the user needs to add crash reporting to a mobile or desktop application.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Choose crash events and diagnostic fields that exclude user content.
2. Redact identifiers, pasted text, file paths, and sensitive request data.
3. Group equivalent crashes with a stable fingerprint and separate app versions.
4. Connect the report to a source revision and compare crash-free sessions by release.
5. Test redaction with seeded sensitive strings before enabling production delivery.

## Output contract

Platform code plus the device-level verification that was performed.

## Validation checklist

- [ ] The flow works on the minimum supported OS version
- [ ] Permissions are requested at the moment of use
- [ ] The build passes for each target architecture

## Safety notes

Never request a permission earlier than the feature that needs it, and never log user content from a device.

## Related skills

- `migrate-a-desktop-app-to-an-electron-shell`
- `deep-link-into-an-app`
- `package-an-app-for-the-store`
