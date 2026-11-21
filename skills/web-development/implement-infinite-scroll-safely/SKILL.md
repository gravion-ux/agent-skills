---
name: implement-infinite-scroll-safely
description: Implement infinite scroll with guarded pagination, scroll restoration, and an explicit retry path. Use when the user wants a long feed that loads more rows as the reader reaches the end.
domain: web-development
tags: [infinite-scroll, pagination, resilience]
triggers: ["infinite scroll feed", "load more rows while scrolling", "implement infinite scroll"]
---

# Implement infinite scroll with guarded pagination, scroll restoration, and an explicit retry path

## Purpose

Implement infinite scroll with guarded pagination, scroll restoration, and an explicit retry path.

## When to use

Use when the user wants a long feed that loads more rows as the reader reaches the end.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Expose the feed as a paginated data source with a stable cursor.
2. Trigger the next page only when a sentinel enters the viewport and no request is pending.
3. Cancel or ignore stale responses when the filter or sort key changes.
4. Show a retry control when a page request fails and preserve the loaded pages.
5. Restore the previous scroll position after navigation and check keyboard access to the sentinel.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `implement-a-navigation-header`
- `implement-client-side-routing`
- `implement-client-side-validation-messages`
