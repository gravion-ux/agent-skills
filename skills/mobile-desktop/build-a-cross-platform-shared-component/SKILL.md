---
name: build-a-cross-platform-shared-component
description: Build a shared cross-platform component with a common API and platform-specific rendering. Use when the user needs one component to behave consistently across mobile and desktop platforms.
domain: mobile-desktop
tags: [cross-platform, shared-component, platform-adapter]
triggers: ["cross-platform shared component", "build one component for mobile and desktop", "share native UI behavior"]
---

# Build a shared cross-platform component with a common API and platform-specific rendering

## Purpose

Build a shared cross-platform component with a common API and platform-specific rendering.

## When to use

Use when the user needs one component to behave consistently across mobile and desktop platforms.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Define the shared component API around the behavior shared by every platform.
2. Keep platform-specific rendering behind a narrow adapter within the component.
3. Define accessibility, sizing, and theming semantics for each target platform.
4. Add contract tests for the shared behavior and visual checks for each platform.
5. Verify the component on the minimum supported OS and desktop environment.

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
- `design-a-mobile-screen-flow`
- `implement-offline-caching-in-a-mobile-app`
