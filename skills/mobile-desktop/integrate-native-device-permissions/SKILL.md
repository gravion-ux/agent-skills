---
name: integrate-native-device-permissions
description: Integrate native device permissions with contextual prompts and explicit denied-state handling. Use when the user needs an app to request an operating-system device permission.
domain: mobile-desktop
tags: [device-permissions, native-access, privacy]
triggers: ["native device permissions", "integrate an OS permission flow", "handle a denied device permission"]
---

# Integrate native device permissions with contextual prompts and explicit denied-state handling

## Purpose

Integrate native device permissions with contextual prompts and explicit denied-state handling.

## When to use

Use when the user needs an app to request an operating-system device permission.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Map the requested permission to the exact feature that requires it.
2. Check the current authorization state before showing any permission prompt.
3. Explain the feature's purpose at the moment the user invokes it.
4. Handle denial, limited access, and later revocation without crashing the flow.
5. Revoke the permission in a test build and verify the app recovers safely.

## Output contract

Platform code plus the device-level verification that was performed.

## Validation checklist

- [ ] The flow works on the minimum supported OS version
- [ ] Permissions are requested at the moment of use
- [ ] The build passes for each target architecture

## Safety notes

Never request a permission earlier than the feature that needs it, and never log user content from a device.

## Related skills

- `persist-local-state-on-a-device`
- `write-a-responsive-native-layout`
- `add-crash-reporting-to-an-app`
