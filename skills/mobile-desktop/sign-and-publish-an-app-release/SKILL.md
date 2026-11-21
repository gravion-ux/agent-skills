---
name: sign-and-publish-an-app-release
description: Sign, notarize, and publish an app release with retained checksums and rollout controls. Use when the user needs to sign and publish a mobile or desktop application release.
domain: mobile-desktop
tags: [release-signing, publishing, rollout]
triggers: ["sign and publish an app release", "publish a signed mobile build", "roll out a desktop app release"]
---

# Sign, notarize, and publish an app release with retained checksums and rollout controls

## Purpose

Sign, notarize, and publish an app release with retained checksums and rollout controls.

## When to use

Use when the user needs to sign and publish a mobile or desktop application release.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Build the release from the reviewed commit and record its source revision.
2. Apply the platform signing identity to the distributable artifact.
3. Verify the signature and notarization result before uploading the package.
4. Publish to a limited rollout cohort and monitor crash and install rates.
5. Promote the release or halt the rollout when the health threshold fails.

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
- `handle-app-backgrounding-and-resume`
