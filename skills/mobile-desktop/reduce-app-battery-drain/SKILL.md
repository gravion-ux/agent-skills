---
name: reduce-app-battery-drain
description: Reduce app battery drain by locating background work and aligning refreshes with user needs. Use when the user needs to find and fix excessive battery use in a mobile or desktop app.
domain: mobile-desktop
tags: [battery-optimization, background-work, energy]
triggers: ["app battery drain", "reduce mobile battery usage", "find desktop background power use"]
---

# Reduce app battery drain by locating background work and aligning refreshes with user needs

## Purpose

Reduce app battery drain by locating background work and aligning refreshes with user needs.

## When to use

Use when the user needs to find and fix excessive battery use in a mobile or desktop app.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Collect platform battery diagnostics across representative device states.
2. Rank background tasks by wake-ups, network transfers, and execution duration.
3. Replace fixed polling with event-driven updates and platform scheduling.
4. Stop nonessential work when the app is backgrounded or the device is low power.
5. Re-run the same diagnostic scenario and confirm measurable energy savings.

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
