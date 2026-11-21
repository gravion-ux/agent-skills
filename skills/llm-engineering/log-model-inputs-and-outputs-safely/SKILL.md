---
name: log-model-inputs-and-outputs-safely
description: Log model inputs and outputs with redaction, sampling, and retention controls for safe diagnosis. Use when the user wants observability for LLM calls without exposing sensitive customer data.
domain: llm-engineering
tags: [logging, privacy, observability, redaction]
triggers: ["log model inputs outputs safely", "safe llm logging", "privacy aware model logs"]
---

# Log model inputs and outputs with redaction, sampling, and retention controls for safe diagnosis

## Purpose

Log model inputs and outputs with redaction, sampling, and retention controls for safe diagnosis.

## When to use

Use when the user wants observability for LLM calls without exposing sensitive customer data.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Classify fields by sensitivity and redact direct identifiers before logging.
2. Hash correlation identifiers instead of recording raw account or user identifiers.
3. Store structured metadata including model, latency, tokens, status, and error code.
4. Sample full payloads only under an approved, time-limited retention policy.
5. Test redaction rules with synthetic secrets and verify excluded fields stay absent.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `build-a-model-router-by-task-difficulty`
- `build-a-retrieval-pipeline-for-a-model`
- `build-a-shadow-deployment-for-a-model`
