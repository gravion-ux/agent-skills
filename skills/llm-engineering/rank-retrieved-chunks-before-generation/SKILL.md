---
name: rank-retrieved-chunks-before-generation
description: Rerank retrieved chunks by query relevance before placing them in the model context. Use when the user has noisy retrieval results that must be ordered for generation.
domain: llm-engineering
tags: [reranking, retrieval, ranking]
triggers: ["rerank llm retrieved chunks", "llm retrieval reranking", "rank chunks for an llm"]
---

# Rerank retrieved chunks by query relevance before placing them in the model context

## Purpose

Rerank retrieved chunks by query relevance before placing them in the model context.

## When to use

Use when the user has noisy retrieval results that must be ordered for generation.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Define the retrieval candidates and the relevance criteria for each query.
2. Score every candidate with a ranker suited to the language and domain.
3. Select the top chunks within the context and token budgets.
4. Preserve source identifiers and passage order for later attribution.
5. Measure relevance, answer quality, token cost, latency, and ranking failure modes on a fixed evaluation set.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `ground-a-response-in-retrieved-citations`
- `redact-personal-data-before-sending-to-a-model`
- `add-typed-function-definitions-for-tools`
