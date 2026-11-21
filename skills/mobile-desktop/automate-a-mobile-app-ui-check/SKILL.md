---
name: automate-a-mobile-app-ui-check
description: Automate a repeatable mobile UI check with stable selectors, screenshots, and failure logs. Use when the user wants an agent to run a repeatable mobile app UI check.
domain: mobile-desktop
tags: [ui-automation, mobile-testing, agents]
triggers: ["automate a mobile app UI check", "run an automated mobile UI check", "agent check on a mobile app"]
---

# Automate a repeatable mobile UI check with stable selectors, screenshots, and failure logs

## Purpose

Automate a repeatable mobile UI check with stable selectors, screenshots, and failure logs.

## When to use

Use when the user wants an agent to run a repeatable mobile app UI check.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Define the app build, device configuration, and target flow for the check.
2. Select stable accessibility identifiers instead of screen coordinates.
3. Run the flow, capture screenshots at each checkpoint, and collect device logs.
4. Compare visible text, navigation state, and control availability with expectations.
5. Report the first failing checkpoint with reproduction details and artifacts.

## Output contract

Platform code plus the device-level verification that was performed.

## Validation checklist

- [ ] The flow works on the minimum supported OS version
- [ ] Permissions are requested at the moment of use
- [ ] The build passes for each target architecture

## Safety notes

Never request a permission earlier than the feature that needs it, and never log user content from a device.

## Related skills

- `implement-offline-caching-in-a-mobile-app`
- `plan-a-mobile-app-release-train`
- `test-a-mobile-app-on-real-devices`
