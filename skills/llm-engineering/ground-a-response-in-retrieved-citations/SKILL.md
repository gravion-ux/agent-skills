---
name: ground-a-response-in-retrieved-citations
description: Attach verified citations to each substantive claim and reject unsupported passages. Use when the user wants a model answer that links claims to source material.
domain: llm-engineering
tags: [citations, grounding, attribution]
triggers: ["cite llm sources", "ground llm answer in citations", "add citations to an llm response"]
---

# Attach verified citations to each substantive claim and reject unsupported passages

## Purpose

Attach verified citations to each substantive claim and reject unsupported passages.

## When to use

Use when the user wants a model answer that links claims to source material.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Retrieve source passages with stable document and passage identifiers.
2. Map each substantive claim to the passages that directly support it.
3. Verify that every citation contains the cited evidence and that the quote is exact.
4. Remove or qualify claims that lack supporting evidence.
5. Measure citation precision, recall, answer quality, token cost, latency, and failure modes on a fixed evaluation set.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `design-a-model-in-the-loop-classifier`
- `design-a-schema-validated-tool-response`
- `detect-hallucination-in-a-generated-answer`
