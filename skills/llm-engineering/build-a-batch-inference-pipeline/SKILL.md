---
name: build-a-batch-inference-pipeline
description: Build a batch inference pipeline with bounded concurrency, retries, and per-item result records. Use when the user wants to process many LLM requests reliably without overwhelming the provider.
domain: llm-engineering
tags: [batch-processing, inference, reliability, cost]
triggers: ["batch inference pipeline", "run llm requests in batches", "process model requests reliably"]
---

# Build a batch inference pipeline with bounded concurrency, retries, and per-item result records

## Purpose

Build a batch inference pipeline with bounded concurrency, retries, and per-item result records.

## When to use

Use when the user wants to process many LLM requests reliably without overwhelming the provider.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Read the job manifest and validate each request against the input schema.
2. Partition the manifest into batches that fit the provider's size limit.
3. Run batches with bounded concurrency and exponential retry on transient errors.
4. Persist the request key, output, latency, token count, and status per item.
5. Resume from the last completed key and quarantine permanent failures.

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
- `build-a-model-router-by-task-difficulty`
- `build-a-shadow-deployment-for-a-model`
