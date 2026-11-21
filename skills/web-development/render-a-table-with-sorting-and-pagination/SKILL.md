---
name: render-a-table-with-sorting-and-pagination
description: Render a data table with sortable columns, paginated rows, and clear empty and loading states. Use when the user wants a results table that sorts and pages through row data.
domain: web-development
tags: [data-table, sorting, pagination]
triggers: ["sortable paginated table", "table with sorting and pagination", "add pagination to a data table"]
---

# Render a data table with sortable columns, paginated rows, and clear empty and loading states

## Purpose

Render a data table with sortable columns, paginated rows, and clear empty and loading states.

## When to use

Use when the user wants a results table that sorts and pages through row data.

## When NOT to use

Do not use this for a pure API contract change with no user interface; use api-design instead.

## Inputs required

- The framework and the rendering mode
- The screens or routes in scope
- The browser, device and accessibility targets

## Procedure

1. Define the column definitions, row shape, and sort key for each column.
2. Render header controls that set the active sort field and direction.
3. Slice the row set by the current page and page size.
4. Show an empty-state message when the filtered result set has no rows.
5. Verify keyboard navigation reaches every header and pagination control.

## Output contract

Working front-end code plus the build, lint and accessibility checks that passed.

## Validation checklist

- [ ] The page builds without console errors
- [ ] Keyboard navigation reaches every interactive element
- [ ] The layout holds at the smallest supported width

## Safety notes

Never inline secrets into client bundles and never collect personal data without a stated purpose.

## Related skills

- `render-a-list-with-virtual-scrolling`
- `build-a-form-with-inline-validation`
- `build-a-modal-dialog-with-focus-management`
