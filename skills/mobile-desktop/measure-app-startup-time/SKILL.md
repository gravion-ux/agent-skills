---
name: measure-app-startup-time
description: Measure app startup timing from process launch to the first usable interactive screen. Use when the user needs to diagnose slow startup on a mobile or desktop app.
domain: mobile-desktop
tags: [startup-performance, profiling, launch-time]
triggers: ["app startup time", "measure mobile app launch", "profile desktop startup delay"]
---

# Measure app startup timing from process launch to the first usable interactive screen

## Purpose

Measure app startup timing from process launch to the first usable interactive screen.

## When to use

Use when the user needs to diagnose slow startup on a mobile or desktop app.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Define startup milestones from process launch to first interactive frame.
2. Measure cold starts on the minimum supported device with release instrumentation.
3. Capture repeated runs at the same device state and report the distribution.
4. Compare the slowest spans with initialization work, storage, and network calls.
5. Set a device-appropriate startup budget and add a regression check.

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
- `automate-a-mobile-app-ui-check`
- `deep-link-into-an-app`
