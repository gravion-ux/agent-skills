---
name: fall-back-to-a-second-model-provider
description: Route failed requests to a second provider while preserving the output contract and side-effect safety. Use when the user needs provider failover for an llm application.
domain: llm-engineering
tags: [provider-fallback, failover, resilience]
triggers: ["fallback llm provider", "switch llm provider on failure", "second llm provider failover"]
---

# Route failed requests to a second provider while preserving the output contract and side-effect safety

## Purpose

Route failed requests to a second provider while preserving the output contract and side-effect safety.

## When to use

Use when the user needs provider failover for an llm application.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Define failure classes that justify switching providers.
2. Map both providers' responses to the same request and output contracts.
3. Validate the fallback response before returning it to the caller.
4. Prevent retries from duplicating writes, charges, or other side effects.
5. Compare fixed-evaluation accuracy, token cost, latency, and failure modes across both providers.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `constrain-a-model-output-to-json-schema`
- `redact-personal-data-before-sending-to-a-model`
- `build-a-model-router-by-task-difficulty`
