---
name: sync-offline-changes-when-reconnecting
description: Synchronize queued offline changes after reconnection using conflict rules and retry limits. Use when the user needs queued device changes to synchronize after connectivity returns.
domain: mobile-desktop
tags: [offline-sync, conflict-resolution, reconnection]
triggers: ["offline change sync", "sync device changes after reconnecting", "resolve offline sync conflicts"]
---

# Synchronize queued offline changes after reconnection using conflict rules and retry limits

## Purpose

Synchronize queued offline changes after reconnection using conflict rules and retry limits.

## When to use

Use when the user needs queued device changes to synchronize after connectivity returns.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Assign each offline change a stable identifier and an operation timestamp.
2. Queue writes locally with their target record and intended outcome.
3. Replay changes in order when connectivity returns and apply explicit conflict rules.
4. Retry transient failures with backoff and stop after the configured limit.
5. Expose pending, synchronized, and failed states without logging user content.

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
- `add-crash-reporting-to-an-app`
- `automate-a-mobile-app-ui-check`
