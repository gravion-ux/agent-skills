---
name: package-an-app-for-the-store
description: Prepare an app package with release metadata, icons, privacy declarations, and signed artifacts. Use when the user needs to prepare a mobile or desktop application for store submission.
domain: mobile-desktop
tags: [store-packaging, release-build, publishing]
triggers: ["package an app for the store", "prepare a mobile store package", "validate a desktop release package"]
---

# Prepare an app package with release metadata, icons, privacy declarations, and signed artifacts

## Purpose

Prepare an app package with release metadata, icons, privacy declarations, and signed artifacts.

## When to use

Use when the user needs to prepare a mobile or desktop application for store submission.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Create a release build from a clean checkout with the intended version number.
2. Generate platform icons, screenshots, descriptions, and required privacy declarations.
3. Remove development endpoints, debug logging, and test credentials from the package.
4. Verify the packaged artifact on a supported target architecture and OS version.
5. Run the store validator and archive the validated package with its checksum.

## Output contract

Platform code plus the device-level verification that was performed.

## Validation checklist

- [ ] The flow works on the minimum supported OS version
- [ ] Permissions are requested at the moment of use
- [ ] The build passes for each target architecture

## Safety notes

Never request a permission earlier than the feature that needs it, and never log user content from a device.

## Related skills

- `add-crash-reporting-to-an-app`
- `deep-link-into-an-app`
- `migrate-a-desktop-app-to-an-electron-shell`
