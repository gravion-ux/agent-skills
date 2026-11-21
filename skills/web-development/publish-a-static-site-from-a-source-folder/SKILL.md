---
name: publish-a-static-site-from-a-source-folder
description: Publish a static website by building its source folder and validating the generated artifact. Use when the user wants a source folder published as a static website.
domain: web-development
tags: [static-site, site-publishing, build-artifact]
triggers: ["static website source publishing", "publish a static website from source files", "build and deploy a static site artifact"]
---

# Publish a static website by building its source folder and validating the generated artifact

## Purpose

Publish a static website by building its source folder and validating the generated artifact.

## When to use

Use when the user wants a source folder published as a static website.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Identify the site framework and run its documented production build command.
2. Confirm the output directory contains an index file and all referenced assets.
3. Scan the build output for environment secrets and remove them before publishing.
4. Check generated links, routes, and asset paths against the local build server.
5. Upload the validated output as an immutable release and record its source revision.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `set-up-a-static-site-generator-pipeline`
- `add-dark-mode-to-a-site`
- `add-internationalisation-to-a-site`
