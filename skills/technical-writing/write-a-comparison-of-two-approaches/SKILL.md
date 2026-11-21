---
name: write-a-comparison-of-two-approaches
description: Compare two approaches on the criteria that decide, with the evidence for each. Use when the user needs to choose between two technical options and wants the comparison written down.
domain: technical-writing
tags: [comparison, trade-offs, decision]
triggers: ["compare two technical approaches", "option a versus option b write up", "weigh two implementation choices"]
---

# Compare two approaches on the criteria that decide, with the evidence for each

## Purpose

Compare two approaches on the criteria that decide, with the evidence for each.

## When to use

Use when the user needs to choose between two technical options and wants the comparison written down.

## When NOT to use

Do not use this for a reference-manual API listing; use api-design instead.

## Inputs required

- The technical subject and the reader's level
- The decision the reader must make
- The evidence and examples available

## Procedure

1. Write the criteria that decide the choice before describing either option.
2. Describe each option against every criterion with the same depth.
3. Mark clearly where one option is better and where the other is.
4. State the cost of the option that is being rejected.
5. Recommend one, and name the condition under which the other becomes better.

## Output contract

A precise technical document with a clear structure, correct terminology and verified examples.

## Validation checklist

- [ ] The terminology is consistent throughout
- [ ] Every instruction was followed once end to end
- [ ] The document states its assumptions

## Safety notes

Never state a performance, security or compatibility claim that was not verified.

## Related skills

- `write-a-benchmark-report`
- `write-a-migration-plan-for-users`
- `write-a-postmortem`
