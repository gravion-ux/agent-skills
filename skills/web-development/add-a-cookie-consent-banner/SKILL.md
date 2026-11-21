---
name: add-a-cookie-consent-banner
description: Add a cookie consent banner that records choices before enabling nonessential tracking. Use when the user wants a website to ask for consent before optional cookies or tracking.
domain: web-development
tags: [cookie-consent, privacy-controls, consent-banner]
triggers: ["cookie consent web banner", "add a consent banner to a website", "gate non-essential website cookies on consent"]
---

# Add a cookie consent banner that records choices before enabling nonessential tracking

## Purpose

Add a cookie consent banner that records choices before enabling nonessential tracking.

## When to use

Use when the user wants a website to ask for consent before optional cookies or tracking.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. List each cookie category, its purpose, and the provider that receives the data.
2. Load strictly necessary cookies immediately and defer optional scripts until consent.
3. Provide equally accessible accept and reject controls that update stored choices.
4. Recheck the stored choice on later visits and stop nonessential scripts after rejection.
5. Verify the page with no console errors and confirm that rejection blocks optional requests.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `add-a-service-worker-for-caching`
- `add-dark-mode-to-a-site`
- `add-internationalisation-to-a-site`
