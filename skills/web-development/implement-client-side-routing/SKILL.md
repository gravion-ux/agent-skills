---
name: implement-client-side-routing
description: Implement client-side routing with predictable URLs, history behavior, and route-level error states. Use when the user wants a web application to navigate between screens without full page reloads.
domain: web-development
tags: [client-routing, spa-navigation, route-state]
triggers: ["client-side web routing", "implement browser route navigation", "add single-page app routing"]
---

# Implement client-side routing with predictable URLs, history behavior, and route-level error states

## Purpose

Implement client-side routing with predictable URLs, history behavior, and route-level error states.

## When to use

Use when the user wants a web application to navigate between screens without full page reloads.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Define the route table, parameter shapes, and fallback URL for each screen.
2. Render ordinary links that call the router while preserving modified-click behavior.
3. Update document metadata, focus, and scroll position after each navigation.
4. Add loading, not-found, and route-error states for invalid destinations.
5. Verify forward and back navigation with keyboard input and no console errors.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `implement-client-side-validation-messages`
- `implement-a-navigation-header`
- `implement-infinite-scroll-safely`
