---
name: render-a-chart-in-the-browser
description: Render an accessible browser chart with a data table fallback and readable axis labels. Use when the user wants a chart drawn in the browser from a data series.
domain: web-development
tags: [charts, visualization, accessibility]
triggers: ["chart in the browser", "render a data chart on the page", "browser chart with data table fallback"]
---

# Render an accessible browser chart with a data table fallback and readable axis labels

## Purpose

Render an accessible browser chart with a data table fallback and readable axis labels.

## When to use

Use when the user wants a chart drawn in the browser from a data series.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Map the source series to labelled axes, units, and a sensible value range.
2. Draw the chart with a charting library or canvas and keep the data in memory only.
3. Provide a screen-reader summary and a tabular fallback of the plotted values.
4. Redraw on resize without re-querying the data source.
5. Check labels stay legible at the smallest supported width and the build passes lint.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `fetch-and-cache-data-in-a-browser`
- `debug-a-cross-browser-layout-bug`
- `render-a-list-with-virtual-scrolling`
