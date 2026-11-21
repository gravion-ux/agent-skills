---
name: chunk-a-long-document-for-a-model
description: Split a long document into retrievable chunks that preserve context and fit the context budget. Use when the user needs to process a document larger than the model context window.
domain: llm-engineering
tags: [chunking, long-context, document-processing]
triggers: ["chunk a long document for an llm", "llm document chunking", "long document context for an llm"]
---

# Split a long document into retrievable chunks that preserve context and fit the context budget

## Purpose

Split a long document into retrievable chunks that preserve context and fit the context budget.

## When to use

Use when the user needs to process a document larger than the model context window.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Choose a chunk size that fits the prompt and retrieval token budgets.
2. Split the document on semantic boundaries and retain useful overlap.
3. Attach section headings, source identifiers, and positions to every chunk.
4. Remove or redact personal data before storing chunk text.
5. Evaluate answer quality, token cost, and latency against a fixed document question set.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `build-a-retrieval-pipeline-for-a-model`
- `build-a-shadow-deployment-for-a-model`
- `pin-a-model-version-for-reproducibility`
