---
name: audit-a-page-for-accessibility
description: Audit a webpage for accessibility defects with automated scans and manual keyboard verification. Use when the user wants an existing page checked for accessibility barriers.
domain: web-development
tags: [accessibility-audit, wcag, browser-review]
triggers: ["web page accessibility audit", "audit a webpage with automated accessibility checks", "find keyboard and screen-reader barriers in a page"]
---

# Audit a webpage for accessibility defects with automated scans and manual keyboard verification

## Purpose

Audit a webpage for accessibility defects with automated scans and manual keyboard verification.

## When to use

Use when the user wants an existing page checked for accessibility barriers.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Run an automated accessibility scan on each in-scope route and record every finding.
2. Walk the page with only a keyboard and note focus, order, and hidden traps.
3. Check names, roles, labels, contrast, zoom, and reduced-motion behavior manually.
4. Fix the confirmed defects in priority order without weakening the audit rule.
5. Rerun the scan and manual checks, then attach the remaining risks to the page.

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
- `build-a-responsive-page-layout`
- `make-a-page-work-without-javascript`
