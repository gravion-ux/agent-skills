---
name: set-up-a-preview-deploy-for-a-web-app
description: Set up a preview deploy that builds the front end, serves it, and announces the resulting URL. Use when the user wants each web change to get a shareable preview build.
domain: web-development
tags: [preview-deploy, ci, release]
triggers: ["preview deploy for a web app", "share a preview build url", "set up per branch previews"]
---

# Set up a preview deploy that builds the front end, serves it, and announces the resulting URL

## Purpose

Set up a preview deploy that builds the front end, serves it, and announces the resulting URL.

## When to use

Use when the user wants each web change to get a shareable preview build.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Configure the pipeline to install dependencies and run the production build.
2. Publish the build output to the preview host and capture the deployment URL.
3. Point the preview environment at safe, non-secret configuration values only.
4. Add an automated check that fails the preview when lint or accessibility checks break.
5. Post the preview URL and build status on the pull request.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `set-up-a-content-management-system`
- `set-up-a-static-site-generator-pipeline`
- `write-an-end-to-end-test-for-a-web-flow`
