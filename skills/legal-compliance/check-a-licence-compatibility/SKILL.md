---
name: check-a-licence-compatibility
description: Check licence compatibility by tracing what each licence permits and forbids in combination. Use when the user wants to know whether two licences or components can legally be combined.
domain: legal-compliance
tags: [licensing, compatibility, compliance]
triggers: ["check licence compatibility", "can I combine these two open source licences", "licence obligations conflict in my stack"]
---

# Check licence compatibility by tracing what each licence permits and forbids in combination

## Purpose

Check licence compatibility by tracing what each licence permits and forbids in combination.

## When to use

Use when the user wants to know whether two licences or components can legally be combined.

## When NOT to use

Do not use this for a routine internal policy note; use documentation instead.

## Inputs required

- The document, process or data in scope
- The jurisdiction and the obligations
- The deadline and the risk of non-compliance

## Procedure

1. Identify the exact licence for each component, including any exceptions in the notice file.
2. Write the obligations each licence imposes, such as attribution, copyleft and source disclosure.
3. Check whether one licence's conditions conflict with the other's use rights.
4. Check the distribution model, because the obligations differ for internal use and for shipping.
5. State the conclusion with the clause that supports it, and flag anything for a legal review.

## Output contract

A review with the obligations mapped, the gaps listed and a recommendation per gap.

## Validation checklist

- [ ] Every requirement is traced to a source clause
- [ ] Gaps are ranked by severity
- [ ] The output states that it is not legal advice

## Safety notes

Never present the output as legal advice, and never sign, file or publish on the user's behalf.

## Related skills

- `keep-a-licence-and-notice-register`
- `build-a-compliance-checklist`
- `document-a-compliance-evidence-trail`
