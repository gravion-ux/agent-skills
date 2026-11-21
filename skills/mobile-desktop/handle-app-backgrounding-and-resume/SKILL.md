---
name: handle-app-backgrounding-and-resume
description: Handle app backgrounding and resume by saving state before suspension and recovering afterward. Use when the user needs an app to remain reliable when backgrounded or resumed.
domain: mobile-desktop
tags: [app-lifecycle, backgrounding, state-recovery]
triggers: ["mobile app backgrounding", "handle app background and resume", "restore state after backgrounding"]
---

# Handle app backgrounding and resume by saving state before suspension and recovering afterward

## Purpose

Handle app backgrounding and resume by saving state before suspension and recovering afterward.

## When to use

Use when the user needs an app to remain reliable when backgrounded or resumed.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Subscribe to the platform's background and foreground lifecycle notifications.
2. Save unsaved user progress before the app enters the background.
3. Cancel or pause background work that exceeds the platform time budget.
4. On resume, refresh stale data and restore the last valid navigation state.
5. Test calls, notifications, and process termination during each transition.

## Output contract

Platform code plus the device-level verification that was performed.

## Validation checklist

- [ ] The flow works on the minimum supported OS version
- [ ] Permissions are requested at the moment of use
- [ ] The build passes for each target architecture

## Safety notes

Never request a permission earlier than the feature that needs it, and never log user content from a device.

## Related skills

- `handle-screen-rotation-and-resizing`
- `sign-and-publish-an-app-release`
- `add-crash-reporting-to-an-app`
