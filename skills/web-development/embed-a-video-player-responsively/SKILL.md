---
name: embed-a-video-player-responsively
description: Embed a responsive video player with stable dimensions, captions, and accessible controls. Use when the user wants a video to fit a webpage without overflow or layout shifts.
domain: web-development
tags: [video-embed, responsive-media, captioned-player]
triggers: ["responsive embedded video player", "embed a responsive web video", "add a captioned responsive video iframe"]
---

# Embed a responsive video player with stable dimensions, captions, and accessible controls

## Purpose

Embed a responsive video player with stable dimensions, captions, and accessible controls.

## When to use

Use when the user wants a video to fit a webpage without overflow or layout shifts.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Wrap the player in a container with a fixed aspect ratio and no fixed pixel width.
2. Give the player frame a unique title and allow the provider controls to remain enabled.
3. Provide captions or a transcript for spoken content and meaningful fallback text.
4. Choose the provider embed size that matches the available responsive container.
5. Check the player at mobile and desktop widths with keyboard controls and no console errors.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `add-a-cookie-consent-banner`
- `add-a-service-worker-for-caching`
- `add-dark-mode-to-a-site`
