---
name: choose-embeddings-for-a-corpus
description: Compare embedding models on representative corpus queries before selecting one for retrieval. Use when the user needs to choose an embedding model for a document collection.
domain: llm-engineering
tags: [embeddings, semantic-search, corpus]
triggers: ["choose llm embeddings", "llm embedding model comparison", "embeddings for an llm corpus"]
---

# Compare embedding models on representative corpus queries before selecting one for retrieval

## Purpose

Compare embedding models on representative corpus queries before selecting one for retrieval.

## When to use

Use when the user needs to choose an embedding model for a document collection.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Sample representative queries and relevant passages from the corpus.
2. Run each candidate embedding model over the same evaluation set.
3. Compare retrieval relevance, dimensionality, ingestion cost, and query latency.
4. Check that the selected model fits the provider and index constraints.
5. Record the comparison, chosen threshold, and known retrieval failure modes.

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
- `choose-between-a-chain-and-a-router`
