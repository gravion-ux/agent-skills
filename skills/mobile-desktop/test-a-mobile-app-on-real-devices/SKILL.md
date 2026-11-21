---
name: test-a-mobile-app-on-real-devices
description: Test a mobile app on real devices by covering hardware, OS, network, and lifecycle variants. Use when the user needs to validate a mobile application on physical devices.
domain: mobile-desktop
tags: [device-testing, mobile-qa, compatibility]
triggers: ["real device app testing", "test a mobile app on devices", "run a device compatibility matrix"]
---

# Test a mobile app on real devices by covering hardware, OS, network, and lifecycle variants

## Purpose

Test a mobile app on real devices by covering hardware, OS, network, and lifecycle variants.

## When to use

Use when the user needs to validate a mobile application on physical devices.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Select devices that cover the minimum OS version, major screen sizes, and architectures.
2. Run the core flow, permission prompts, backgrounding, and offline recovery.
3. Repeat network transitions, rotation, process death, and battery-saver modes.
4. Record device model, OS version, build revision, and exact reproduction steps.
5. Classify failures by code, platform, or environment before assigning fixes.

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
