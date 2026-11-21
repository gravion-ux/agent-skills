---
name: router-web-development
description: Route work in the Web development domain to the right leaf skill. Use when a task clearly belongs to web-development.
domain: web-development
tags: [router, routing, web-development]
triggers: ["route a web-development task", "which web-development skill should I use"]
---

# Web development router

## Purpose

List every leaf skill in the web-development domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside web-development and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `add-a-cookie-consent-banner` | Use when the user wants a website to ask for consent before optional cookies or tracking. |
| `add-a-service-worker-for-caching` | Use when the user wants a service worker to cache front-end assets for repeat visits. |
| `add-analytics-and-track-events` | Use when the user wants measurable interactions tracked on a website. |
| `add-dark-mode-to-a-site` | Use when the user wants an existing website to support a dark appearance. |
| `add-internationalisation-to-a-site` | Use when the user wants a website to support more than one language or locale. |
| `audit-a-page-for-accessibility` | Use when the user wants an existing page checked for accessibility barriers. |
| `build-a-carousel-without-jank` | Use when the user wants an image or card carousel that scrolls smoothly on constrained devices. |
| `build-a-component-library` | Use when the user wants a shared set of reusable interface components for a product. |
| `build-a-dark-mode-theme-switch` | Use when the user wants a light and dark theme switch that survives page reloads. |
| `build-a-dropdown-menu` | Use when the user wants a dropdown menu that opens from a trigger and supports full keyboard use. |
| `build-a-form-with-inline-validation` | Use when the user wants a web form to explain invalid input before submission. |
| `build-a-modal-dialog-with-focus-management` | Use when the user wants a modal overlay that behaves correctly for keyboard and screen reader users. |
| `build-a-responsive-page-layout` | Use when the user wants a web page to adapt across supported viewport widths. |
| `build-a-search-box-with-debounced-results` | Use when the user wants a website search field to avoid a request for every keystroke. |
| `build-a-tabs-component` | Use when the user wants tabbed content with a single visible panel and clear selection state. |
| `build-a-toast-notification` | Use when the user wants transient success, warning, or error messages shown over the interface. |
| `build-an-accessible-navigation-menu` | Use when the user wants a website menu to be usable by keyboard and assistive technology. |
| `build-an-offline-first-web-app` | Use when the user wants a web app that remains usable without a network connection. |
| `compose-ui-from-design-tokens` | Use when the user wants a screen assembled from an existing design token set. |
| `debug-a-cross-browser-layout-bug` | Use when the user has a web layout that differs or breaks in one supported browser. |
| `embed-a-video-player-responsively` | Use when the user wants a video to fit a webpage without overflow or layout shifts. |
| `embed-an-svg-icon-system` | Use when the user wants a set of vector icons embedded consistently across screens. |
| `fetch-and-cache-data-in-a-browser` | Use when the user wants a web client to reuse fetched data without showing stale or broken results. |
| `handle-a-form-with-server-actions` | Use when the user wants a form submitted through server actions with validation feedback. |
| `handle-a-network-failure-gracefully` | Use when the user wants a page that degrades gracefully when a request or asset fails to load. |
| `handle-form-submission-and-errors` | Use when the user wants a web form to report submission progress and failure clearly. |
| `implement-a-navigation-header` | Use when the user wants a consistent navigation header across a website. |
| `implement-client-side-routing` | Use when the user wants a web application to navigate between screens without full page reloads. |
| `implement-client-side-validation-messages` | Use when the user wants form fields to show validation feedback before submission. |
| `implement-infinite-scroll-safely` | Use when the user wants a long feed that loads more rows as the reader reaches the end. |
| `integrate-a-third-party-payment-widget` | Use when the user wants a browser checkout to use a third-party payment service. |
| `lazy-load-below-the-fold-images` | Use when the user wants a webpage to defer images that appear below the initial viewport. |
| `make-a-page-work-without-javascript` | Use when the user wants a webpage to remain usable when scripts are unavailable. |
| `manage-a-loading-skeleton` | Use when the user wants a loading placeholder for content that is fetched asynchronously. |
| `manage-css-without-a-mess` | Use when the user wants an untidy frontend stylesheet to become easier to maintain. |
| `migrate-a-legacy-website-to-a-modern-stack` | Use when the user wants a legacy site rebuilt on a current framework without losing traffic. |
| `migrate-a-site-to-a-modern-framework` | Use when the user wants an existing website moved to a modern frontend framework. |
| `optimise-largest-contentful-paint` | Use when the user wants a web page's largest visible content to render faster. |
| `prevent-double-submit-on-a-button` | Use when the user wants a button that cannot be submitted twice while its action runs. |
| `publish-a-static-site-from-a-source-folder` | Use when the user wants a source folder published as a static website. |
| `reduce-javascript-bundle-size` | Use when the user wants a website's JavaScript download or parse cost reduced. |
| `render-a-chart-in-the-browser` | Use when the user wants a chart drawn in the browser from a data series. |
| `render-a-list-with-virtual-scrolling` | Use when the user needs a large in-browser list to remain responsive. |
| `render-a-table-with-sorting-and-pagination` | Use when the user wants a results table that sorts and pages through row data. |
| `run-a-web-bundle-analysis` | Use when the user wants to understand why a front-end bundle is large and trim it. |
| `set-up-a-content-management-system` | Use when the user wants website content maintained through a content management system. |
| `set-up-a-preview-deploy-for-a-web-app` | Use when the user wants each web change to get a shareable preview build. |
| `set-up-a-static-site-generator-pipeline` | Use when the user wants a documentation or content site built from a static generator. |
| `style-a-component-with-a-design-system` | Use when the user wants a reusable web component to follow an existing design system. |
| `test-a-web-component-in-isolation` | Use when the user wants a repeatable unit test for a single front-end component. |
| `upload-a-file-with-progress` | Use when the user wants a file upload that reports progress and can be cancelled. |
| `write-an-end-to-end-test-for-a-web-flow` | Use when the user wants an end-to-end test covering a multi-step web flow. |
