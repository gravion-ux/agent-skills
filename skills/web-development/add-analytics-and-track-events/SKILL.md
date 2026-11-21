---
name: add-analytics-and-track-events
description: Instrument a website with a named analytics event taxonomy, consent controls, and privacy-safe payloads. Use when the user wants measurable interactions tracked on a website.
domain: web-development
tags: [web-analytics, event-tracking, privacy-safe-events]
triggers: ["web analytics event tracking", "track named events in a web analytics tool", "instrument a website with consent-aware analytics"]
---

# Instrument a website with a named analytics event taxonomy, consent controls, and privacy-safe payloads

## Purpose

Instrument a website with a named analytics event taxonomy, consent controls, and privacy-safe payloads.

## When to use

Use when the user wants measurable interactions tracked on a website.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Define the business questions and the exact event names that answer them.
2. Create a payload schema that excludes credentials and unnecessary personal data.
3. Gate nonessential analytics behind the site's consent choice.
4. Fire each event once at its defined trigger and ignore duplicate clicks.
5. Verify event names and payloads in a test environment without production identifiers.

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
