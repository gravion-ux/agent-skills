---
name: migrate-a-desktop-app-to-an-electron-shell
description: Migrate a desktop application into an Electron shell with secure boundaries and packaged output. Use when the user needs to move a desktop application into an Electron shell.
domain: mobile-desktop
tags: [electron-migration, desktop-shell, ipc-security]
triggers: ["Electron shell migration", "migrate a desktop app to Electron", "secure an Electron desktop wrapper"]
---

# Migrate a desktop application into an Electron shell with secure boundaries and packaged output

## Purpose

Migrate a desktop application into an Electron shell with secure boundaries and packaged output.

## When to use

Use when the user needs to move a desktop application into an Electron shell.

## When NOT to use

Do not use this for server-side work; use software-engineering or devops-cloud instead.

## Inputs required

- The platform and its minimum OS version
- The screen flow being changed
- The offline, battery and permission constraints

## Procedure

1. Inventory the existing process boundaries, file access, and native integrations.
2. Define the trusted main process, isolated renderer, and narrow IPC contract.
3. Disable renderer node integration and restrict navigation to approved origins.
4. Replace unavailable native APIs with tested platform adapters or documented limits.
5. Package for each target architecture and verify signed installation and updates.

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
