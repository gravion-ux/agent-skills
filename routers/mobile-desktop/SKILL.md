---
name: router-mobile-desktop
description: Route work in the Mobile and desktop applications domain to the right leaf skill. Use when a task clearly belongs to mobile-desktop.
domain: mobile-desktop
tags: [router, routing, mobile-desktop]
triggers: ["route a mobile-desktop task", "which mobile-desktop skill should I use"]
---

# Mobile and desktop applications router

## Purpose

List every leaf skill in the mobile-desktop domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside mobile-desktop and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

Platform code plus the device-level verification that was performed.

## Validation checklist

- [ ] The flow works on the minimum supported OS version
- [ ] Permissions are requested at the moment of use
- [ ] The build passes for each target architecture

## Safety notes

Never request a permission earlier than the feature that needs it, and never log user content from a device.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `add-crash-reporting-to-an-app` | Use when the user needs to add crash reporting to a mobile or desktop application. |
| `automate-a-mobile-app-ui-check` | Use when the user wants an agent to run a repeatable mobile app UI check. |
| `build-a-cross-platform-shared-component` | Use when the user needs one component to behave consistently across mobile and desktop platforms. |
| `deep-link-into-an-app` | Use when the user needs external links to open a specific destination inside an app. |
| `design-a-mobile-screen-flow` | Use when the user needs to map a user journey across mobile screens. |
| `handle-app-backgrounding-and-resume` | Use when the user needs an app to remain reliable when backgrounded or resumed. |
| `handle-screen-rotation-and-resizing` | Use when the user needs an app to remain usable during screen rotation or window resizing. |
| `handle-touch-gestures-safely` | Use when the user needs to add a gesture to a mobile or desktop app. |
| `implement-offline-caching-in-a-mobile-app` | Use when the user needs mobile app content to remain available without a network connection. |
| `integrate-native-device-permissions` | Use when the user needs an app to request an operating-system device permission. |
| `measure-app-startup-time` | Use when the user needs to diagnose slow startup on a mobile or desktop app. |
| `migrate-a-desktop-app-to-an-electron-shell` | Use when the user needs to move a desktop application into an Electron shell. |
| `package-an-app-for-the-store` | Use when the user needs to prepare a mobile or desktop application for store submission. |
| `persist-local-state-on-a-device` | Use when the user needs an app to retain state safely on one device. |
| `plan-a-mobile-app-release-train` | Use when the user needs to coordinate recurring mobile app releases across teams. |
| `push-notification-permission-flow` | Use when the user wants to request push notification access in a mobile or desktop app. |
| `reduce-app-battery-drain` | Use when the user needs to find and fix excessive battery use in a mobile or desktop app. |
| `sign-and-publish-an-app-release` | Use when the user needs to sign and publish a mobile or desktop application release. |
| `sync-offline-changes-when-reconnecting` | Use when the user needs queued device changes to synchronize after connectivity returns. |
| `test-a-mobile-app-on-real-devices` | Use when the user needs to validate a mobile application on physical devices. |
| `write-a-desktop-tray-and-menu-integration` | Use when the user needs a desktop application to expose status and actions from the system tray. |
| `write-a-responsive-native-layout` | Use when the user needs a native mobile or desktop layout to adapt across screen sizes. |
