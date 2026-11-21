---
name: write-a-desktop-tray-and-menu-integration
description: Add a desktop tray icon and native menu with clear lifecycle and accessibility behavior. Use when the user needs a desktop application to expose status and actions from the system tray.
domain: mobile-desktop
tags: [system-tray, desktop-menu, native-integration]
triggers: ["desktop tray and menu", "add a desktop tray integration", "build a native tray menu"]
---

# Add a desktop tray icon and native menu with clear lifecycle and accessibility behavior

## Purpose

Add a desktop tray icon and native menu with clear lifecycle and accessibility behavior.

## When to use

Use when the user needs a desktop application to expose status and actions from the system tray.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Define the tray icon states, tooltip text, and left-click action.
2. Build the native context menu from the application's current user actions.
3. Remove stale menu items and tray icons when their owning window closes.
4. Keep keyboard focus, screen-reader labels, and high-contrast rendering intact.
5. Test the integration across display scaling, multi-monitor, and restart states.

## Output contract

Platform code plus the device-level verification that was performed.

## Validation checklist

- [ ] The flow works on the minimum supported OS version
- [ ] Permissions are requested at the moment of use
- [ ] The build passes for each target architecture

## Safety notes

Never request a permission earlier than the feature that needs it, and never log user content from a device.

## Related skills

- `migrate-a-desktop-app-to-an-electron-shell`
- `write-a-responsive-native-layout`
- `automate-a-mobile-app-ui-check`
