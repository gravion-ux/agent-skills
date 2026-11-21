---
name: deep-link-into-an-app
description: Route deep links into validated app destinations with fallback and attribution handling. Use when the user needs external links to open a specific destination inside an app.
domain: mobile-desktop
tags: [deep-linking, routing, link-validation]
triggers: ["app deep link", "route a deep link into an app", "validate deep link parameters"]
---

# Route deep links into validated app destinations with fallback and attribution handling

## Purpose

Route deep links into validated app destinations with fallback and attribution handling.

## When to use

Use when the user needs external links to open a specific destination inside an app.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Define an allowlisted link scheme and its supported destination routes.
2. Validate every incoming parameter before constructing the destination state.
3. Route users to the intended screen and preserve campaign attribution safely.
4. Send invalid links to a relevant fallback screen with a clear recovery action.
5. Test signed links, expired links, and links opened while the app is closed.

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
- `migrate-a-desktop-app-to-an-electron-shell`
- `package-an-app-for-the-store`
