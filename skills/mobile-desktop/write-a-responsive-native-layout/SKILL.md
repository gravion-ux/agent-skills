---
name: write-a-responsive-native-layout
description: Build a responsive native layout that adapts to available space without clipping controls. Use when the user needs a native mobile or desktop layout to adapt across screen sizes.
domain: mobile-desktop
tags: [responsive-layout, native-ui, adaptive-design]
triggers: ["responsive native layout", "build an adaptive native layout", "resize native app layout"]
---

# Build a responsive native layout that adapts to available space without clipping controls

## Purpose

Build a responsive native layout that adapts to available space without clipping controls.

## When to use

Use when the user needs a native mobile or desktop layout to adapt across screen sizes.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Measure the parent container and choose a breakpoint-based layout direction.
2. Define minimum, compact, and expanded size states for each component.
3. Keep primary actions reachable when the viewport becomes narrow.
4. Test keyboard, split-screen, and resized desktop window states.
5. Confirm no text or controls overlap at the minimum supported size.

## Output contract

Platform code plus the device-level verification that was performed.

## Validation checklist

- [ ] The flow works on the minimum supported OS version
- [ ] Permissions are requested at the moment of use
- [ ] The build passes for each target architecture

## Safety notes

Never request a permission earlier than the feature that needs it, and never log user content from a device.

## Related skills

- `write-a-desktop-tray-and-menu-integration`
- `automate-a-mobile-app-ui-check`
- `build-a-cross-platform-shared-component`
