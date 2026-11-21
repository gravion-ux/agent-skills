---
name: set-up-a-content-management-system
description: Set up a CMS-backed website with structured content models, preview, roles, and publish checks. Use when the user wants website content maintained through a content management system.
domain: web-development
tags: [content-management, headless-cms, publishing-workflow]
triggers: ["content management system for a website", "set up cms content models for a site", "connect a website to a headless cms"]
---

# Set up a CMS-backed website with structured content models, preview, roles, and publish checks

## Purpose

Set up a CMS-backed website with structured content models, preview, roles, and publish checks.

## When to use

Use when the user wants website content maintained through a content management system.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Model pages, authors, relationships, and media as structured CMS content.
2. Define role permissions for editing, previewing, publishing, and deleting content.
3. Connect the frontend to typed content fields with a local fallback for missing entries.
4. Configure preview and draft states so unpublished content stays off the live site.
5. Validate a publish workflow with build, lint, link, and accessibility checks.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `set-up-a-preview-deploy-for-a-web-app`
- `set-up-a-static-site-generator-pipeline`
- `build-a-modal-dialog-with-focus-management`
