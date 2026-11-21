---
name: handle-screen-rotation-and-resizing
description: Handle rotation and resizing while preserving navigation state, focus, and user input. Use when the user needs an app to remain usable during screen rotation or window resizing.
domain: mobile-desktop
tags: [responsive-state, rotation, window-resizing]
triggers: ["screen rotation handling", "preserve state while resizing", "handle foldable app layouts"]
---

# Handle rotation and resizing while preserving navigation state, focus, and user input

## Purpose

Handle rotation and resizing while preserving navigation state, focus, and user input.

## When to use

Use when the user needs an app to remain usable during screen rotation or window resizing.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Define the state that must survive every orientation and size change.
2. Rebuild the layout from the current viewport rather than rotating stored pixels.
3. Preserve navigation position, text selection, and keyboard focus where possible.
4. Handle foldable posture and split-screen bounds using platform size classes.
5. Test rapid rotation, multitasking, and desktop window resize sequences.

## Output contract

Platform code plus the device-level verification that was performed.

## Validation checklist

- [ ] The flow works on the minimum supported OS version
- [ ] Permissions are requested at the moment of use
- [ ] The build passes for each target architecture

## Safety notes

Never request a permission earlier than the feature that needs it, and never log user content from a device.

## Related skills

- `handle-app-backgrounding-and-resume`
- `design-a-mobile-screen-flow`
- `handle-touch-gestures-safely`
