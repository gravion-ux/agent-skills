---
name: handle-touch-gestures-safely
description: Implement touch gestures with bounded movement, conflict checks, and reversible actions. Use when the user needs to add a gesture to a mobile or desktop app.
domain: mobile-desktop
tags: [touch-input, gestures, interaction]
triggers: ["touch gesture handling", "add a safe touch gesture", "test app swipe gestures"]
---

# Implement touch gestures with bounded movement, conflict checks, and reversible actions

## Purpose

Implement touch gestures with bounded movement, conflict checks, and reversible actions.

## When to use

Use when the user needs to add a gesture to a mobile or desktop app.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Define the gesture direction, target surface, and allowed interaction zones.
2. Reject gestures that conflict with navigation or system-reserved motions.
3. Require a threshold before committing a drag or swipe action.
4. Provide a visible cancel path and restore the prior state after cancellation.
5. Verify the gesture with slow, fast, and multitouch input sequences.

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
- `handle-screen-rotation-and-resizing`
- `add-crash-reporting-to-an-app`
