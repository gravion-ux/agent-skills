---
name: design-a-mobile-screen-flow
description: Design a mobile screen flow with explicit states, navigation edges, and platform constraints. Use when the user needs to map a user journey across mobile screens.
domain: mobile-desktop
tags: [mobile-flow, screen-design, navigation]
triggers: ["mobile screen flow", "design a mobile screen flow", "map mobile navigation states"]
---

# Design a mobile screen flow with explicit states, navigation edges, and platform constraints

## Purpose

Design a mobile screen flow with explicit states, navigation edges, and platform constraints.

## When to use

Use when the user needs to map a user journey across mobile screens.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. List the entry screen, destination screens, and every navigation edge.
2. Define the loading, empty, success, and error state for each screen.
3. Mark back behavior, system gestures, and interruptions for every transition.
4. Specify the minimum OS version that supports the required controls.
5. Validate the flow on the smallest supported device width.

## Output contract

Platform code plus the device-level verification that was performed.

## Validation checklist

- [ ] The flow works on the minimum supported OS version
- [ ] Permissions are requested at the moment of use
- [ ] The build passes for each target architecture

## Safety notes

Never request a permission earlier than the feature that needs it, and never log user content from a device.

## Related skills

- `automate-a-mobile-app-ui-check`
- `implement-offline-caching-in-a-mobile-app`
- `plan-a-mobile-app-release-train`
