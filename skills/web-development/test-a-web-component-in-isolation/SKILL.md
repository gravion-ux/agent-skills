---
name: test-a-web-component-in-isolation
description: Test a web component in isolation by rendering it with controlled props and captured events. Use when the user wants a repeatable unit test for a single front-end component.
domain: web-development
tags: [component-testing, accessibility, test-harness]
triggers: ["test a web component", "unit test a single ui component", "component test in isolation"]
---

# Test a web component in isolation by rendering it with controlled props and captured events

## Purpose

Test a web component in isolation by rendering it with controlled props and captured events.

## When to use

Use when the user wants a repeatable unit test for a single front-end component.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Mount the component in a test harness with its required providers and props.
2. Assert the rendered structure, accessible name, and state attributes.
3. Dispatch the relevant events and assert the emitted payloads.
4. Cover the empty, loading, and error states with separate cases.
5. Run the test suite and confirm the build and lint checks still pass.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `write-an-end-to-end-test-for-a-web-flow`
- `build-a-component-library`
- `build-a-tabs-component`
