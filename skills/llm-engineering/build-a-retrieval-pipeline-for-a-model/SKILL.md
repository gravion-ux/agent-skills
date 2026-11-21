---
name: build-a-retrieval-pipeline-for-a-model
description: Build a repeatable pipeline that ingests documents, retrieves evidence, and supplies grounded context. Use when the user wants to connect a document corpus to a model application.
domain: llm-engineering
tags: [retrieval, rag, pipeline]
triggers: ["llm retrieval pipeline", "build an llm rag pipeline", "retrieve context for an llm"]
---

# Build a repeatable pipeline that ingests documents, retrieves evidence, and supplies grounded context

## Purpose

Build a repeatable pipeline that ingests documents, retrieves evidence, and supplies grounded context.

## When to use

Use when the user wants to connect a document corpus to a model application.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Ingest documents through a repeatable parse and normalization stage.
2. Index each unit with a chosen embedding model and stable metadata.
3. Retrieve candidate evidence for every request and apply a ranking stage.
4. Pass only the selected evidence and its source identifiers to the model.
5. Score answer quality, token cost, latency, and retrieval failure modes on a fixed evaluation set.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `build-a-shadow-deployment-for-a-model`
- `build-a-batch-inference-pipeline`
- `build-a-model-router-by-task-difficulty`
