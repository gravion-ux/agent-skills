---
name: design-a-search-and-filter-interface
description: Design search and filters that let users narrow results while preserving a clear way back. Use when the user needs to find, refine, and understand results in a large collection.
domain: design-ux
tags: [search-interface, filtering, faceted-search, results]
triggers: ["search and filter interface", "design search and filters", "create a faceted filter ui"]
---

# Design search and filters that let users narrow results while preserving a clear way back

## Purpose

Design search and filters that let users narrow results while preserving a clear way back.

## When to use

Use when the user needs to find, refine, and understand results in a large collection.

## When NOT to use

Do not use this for the visual asset itself; use image-visual instead.

## Inputs required

- The user problem and the success criteria
- The platform and the accessibility target
- The existing design system

## Procedure

1. Define searchable attributes, filter groups, defaults, and result counts.
2. Specify query states for typing, suggestions, no results, and errors.
3. Show active filters and provide clear individual and bulk removal controls.
4. Preserve filters in the URL and support back navigation when feasible.
5. Test zero-result queries, multi-filter combinations, and keyboard operation.

## Output contract

A design specification with flows, states, tokens and the accessibility notes attached.

## Validation checklist

- [ ] Every state is specified, including empty and error
- [ ] Contrast and focus order are defined
- [ ] The design reuses existing tokens

## Safety notes

Never collect personal data in a flow without a stated purpose and consent point.

## Related skills

- `design-a-card-and-list-pattern`
- `apply-design-tokens-to-a-ui`
- `create-a-design-handoff-specification`
