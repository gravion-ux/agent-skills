---
name: push-notification-permission-flow
description: Build a push notification permission flow that asks at the point of relevant user intent. Use when the user wants to request push notification access in a mobile or desktop app.
domain: mobile-desktop
tags: [push-notifications, permissions, user-consent]
triggers: ["push notification permission", "request notification permission", "add a push opt-in flow"]
---

# Build a push notification permission flow that asks at the point of relevant user intent

## Purpose

Build a push notification permission flow that asks at the point of relevant user intent.

## When to use

Use when the user wants to request push notification access in a mobile or desktop app.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Explain the notification benefit at the feature where the user enables it.
2. Request notification permission only after the user chooses that feature.
3. Handle granted, denied, and provisional outcomes without blocking the feature.
4. Provide an in-app path to system settings only when permission is denied.
5. Verify that no notification request appears before the intended action.

## Output contract

Platform code plus the device-level verification that was performed.

## Validation checklist

- [ ] The flow works on the minimum supported OS version
- [ ] Permissions are requested at the moment of use
- [ ] The build passes for each target architecture

## Safety notes

Never request a permission earlier than the feature that needs it, and never log user content from a device.

## Related skills

- `design-a-mobile-screen-flow`
- `add-crash-reporting-to-an-app`
- `automate-a-mobile-app-ui-check`
