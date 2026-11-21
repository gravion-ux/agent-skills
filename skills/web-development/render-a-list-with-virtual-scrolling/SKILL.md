---
name: render-a-list-with-virtual-scrolling
description: Render a long browser list with virtual scrolling so only visible rows consume DOM work. Use when the user needs a large in-browser list to remain responsive.
domain: web-development
tags: [virtual-scrolling, list-performance, browser-rendering]
triggers: ["virtualized web list", "render a long browser list with windowing", "add virtual scrolling to a web list"]
---

# Render a long browser list with virtual scrolling so only visible rows consume DOM work

## Purpose

Render a long browser list with virtual scrolling so only visible rows consume DOM work.

## When to use

Use when the user needs a large in-browser list to remain responsive.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Measure or estimate a stable row height and set the scroll viewport height.
2. Render only the visible row range plus a small overscan buffer.
3. Maintain spacer height and scroll offset as the range changes.
4. Preserve keyboard focus and provide a non-virtualized fallback when required.
5. Profile scrolling and input latency in the browser after the build passes.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `render-a-table-with-sorting-and-pagination`
- `build-a-form-with-inline-validation`
- `build-a-modal-dialog-with-focus-management`
