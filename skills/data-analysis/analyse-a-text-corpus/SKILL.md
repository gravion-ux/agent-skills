---
name: analyse-a-text-corpus
description: Analyze a text corpus with transparent preprocessing, topic evidence, and document-level traceability. Use when the user needs to extract patterns from a collection of documents.
domain: data-analysis
tags: [text-analysis, corpus-analysis, topic-modeling]
triggers: ["text corpus analysis", "analyze text collection", "find topics in documents"]
---

# Analyze a text corpus with transparent preprocessing, topic evidence, and document-level traceability

## Purpose

Analyze a text corpus with transparent preprocessing, topic evidence, and document-level traceability.

## When to use

Use when the user needs to extract patterns from a collection of documents.

## When NOT to use

Do not use this for building a production pipeline; use data-engineering instead.

## Inputs required

- The dataset and its provenance
- The question to answer and the decision it informs
- The acceptable uncertainty

## Procedure

1. Define the corpus scope, time period, labels, and sampling method.
2. Document cleaning, tokenisation, stop-word, and preprocessing rules.
3. Compute frequencies or fit topics with justified parameters.
4. Inspect representative documents, common errors, and edge cases.
5. Report results with document identifiers and explicit limitations.

## Output contract

An answer with the method, the numbers, the caveats and the recommendation that follows.

## Validation checklist

- [ ] The data was profiled before it was analysed
- [ ] The conclusion is separated from the assumption
- [ ] Edge cases and outliers are addressed

## Safety notes

Never present a correlation as a cause, and never include personal data in an output that leaves the approved boundary.

## Related skills

- `analyse-a-survey-result`
- `analyse-a-time-series`
- `ask-a-clear-analytical-question`
