---
name: set-up-a-static-site-generator-pipeline
description: Set up a static site generator pipeline that builds every page and deploys the output cleanly. Use when the user wants a documentation or content site built from a static generator.
domain: web-development
tags: [static-site, build-pipeline, documentation]
triggers: ["static site generator pipeline", "build a docs site from markdown", "set up a static site build"]
---

# Set up a static site generator pipeline that builds every page and deploys the output cleanly

## Purpose

Set up a static site generator pipeline that builds every page and deploys the output cleanly.

## When to use

Use when the user wants a documentation or content site built from a static generator.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Select the generator and define the content folder and front-matter schema.
2. Configure templates, asset handling, and site-level metadata for the build.
3. Generate the site locally and check that every content file produces a page.
4. Add lint and broken-link checks to the pipeline before deployment.
5. Deploy the generated output and confirm the live pages load without console errors.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `publish-a-static-site-from-a-source-folder`
- `set-up-a-content-management-system`
- `set-up-a-preview-deploy-for-a-web-app`
