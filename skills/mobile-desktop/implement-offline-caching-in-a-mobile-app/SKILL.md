---
name: implement-offline-caching-in-a-mobile-app
description: Implement mobile offline caching with explicit freshness, storage limits, and fallback states. Use when the user needs mobile app content to remain available without a network connection.
domain: mobile-desktop
tags: [offline-cache, mobile-content, fallback-states]
triggers: ["mobile offline caching", "cache mobile app content offline", "handle stale offline data"]
---

# Implement mobile offline caching with explicit freshness, storage limits, and fallback states

## Purpose

Implement mobile offline caching with explicit freshness, storage limits, and fallback states.

## When to use

Use when the user needs mobile app content to remain available without a network connection.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Classify each resource by whether it must remain available offline.
2. Store approved responses in the platform cache with source-specific expiration rules.
3. Enforce a storage quota and evict low-priority entries before fresh data.
4. Show cached, stale, and unavailable states instead of implying live accuracy.
5. Test cache hits, expiry, eviction, and behavior after the app is reinstalled.

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
- `plan-a-mobile-app-release-train`
- `test-a-mobile-app-on-real-devices`
