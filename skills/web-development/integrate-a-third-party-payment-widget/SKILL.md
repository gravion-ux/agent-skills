---
name: integrate-a-third-party-payment-widget
description: Integrate a hosted payment widget without exposing credentials or collecting unnecessary card details. Use when the user wants a browser checkout to use a third-party payment service.
domain: web-development
tags: [payment-widget, checkout, payment-security]
triggers: ["third-party payment widget", "integrate a hosted checkout payment widget", "embed a browser payment form safely"]
---

# Integrate a hosted payment widget without exposing credentials or collecting unnecessary card details

## Purpose

Integrate a hosted payment widget without exposing credentials or collecting unnecessary card details.

## When to use

Use when the user wants a browser checkout to use a third-party payment service.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Choose a provider-hosted widget that keeps payment credentials outside the application bundle.
2. Create only a publishable client key and send sensitive authorization through the server.
3. Define the product amount and currency on the server before starting the payment.
4. Render pending, cancelled, declined, and completed states without exposing provider secrets.
5. Verify the checkout with a test payment and confirm the webhook validates the server-side order.

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
