---
name: persist-local-state-on-a-device
description: Persist device-local state with a versioned schema, atomic writes, and recovery defaults. Use when the user needs an app to retain state safely on one device.
domain: mobile-desktop
tags: [local-state, persistence, device-storage]
triggers: ["device local state", "persist state on a device", "recover saved app state"]
---

# Persist device-local state with a versioned schema, atomic writes, and recovery defaults

## Purpose

Persist device-local state with a versioned schema, atomic writes, and recovery defaults.

## When to use

Use when the user needs an app to retain state safely on one device.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Define the state fields, defaults, and schema version.
2. Write changes atomically to the platform's private application storage.
3. Apply migrations when opening state written by an older schema version.
4. Handle corrupt or unreadable data by restoring documented defaults.
5. Verify that the process can stop and restart without losing the latest state.

## Output contract

Platform code plus the device-level verification that was performed.

## Validation checklist

- [ ] The flow works on the minimum supported OS version
- [ ] Permissions are requested at the moment of use
- [ ] The build passes for each target architecture

## Safety notes

Never request a permission earlier than the feature that needs it, and never log user content from a device.

## Related skills

- `test-a-mobile-app-on-real-devices`
- `automate-a-mobile-app-ui-check`
- `build-a-cross-platform-shared-component`
