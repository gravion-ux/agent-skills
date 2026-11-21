---
name: build-a-tabs-component
description: Build an accessible tabs component that links each panel to its selected trigger. Use when the user wants tabbed content with a single visible panel and clear selection state.
domain: web-development
tags: [tabs, tablist, accessibility]
triggers: ["build a tabs component", "tabbed interface with keyboard support", "accessible tabs for panels"]
---

# Build an accessible tabs component that links each panel to its selected trigger

## Purpose

Build an accessible tabs component that links each panel to its selected trigger.

## When to use

Use when the user wants tabbed content with a single visible panel and clear selection state.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Create a tab list with one button per panel and matching panel identifiers.
2. Mark the active tab with aria-selected and hide inactive panels.
3. Switch panels on click and on the arrow-key navigation pattern.
4. Keep panel content mounted only when needed to avoid stale scroll state.
5. Confirm keyboard navigation reaches every tab and the page builds without errors.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `build-a-component-library`
- `build-a-carousel-without-jank`
- `build-a-dark-mode-theme-switch`
