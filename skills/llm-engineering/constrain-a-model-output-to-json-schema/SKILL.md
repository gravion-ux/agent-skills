---
name: constrain-a-model-output-to-json-schema
description: Define a JSON schema, enforce it at the model boundary, and reject responses that violate it. Use when the user needs structured model output that downstream code can parse.
domain: llm-engineering
tags: [json-schema, structured-output, validation]
triggers: ["llm json schema output", "llm structured output schema", "validate llm json output"]
---

# Define a JSON schema, enforce it at the model boundary, and reject responses that violate it

## Purpose

Define a JSON schema, enforce it at the model boundary, and reject responses that violate it.

## When to use

Use when the user needs structured model output that downstream code can parse.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Translate the response contract into a versioned JSON schema.
2. Enable the provider's structured output mode when it is available.
3. Validate every response against the schema before returning it.
4. Record validation failures without storing raw prompts or personal data.
5. Verify schema compliance, accuracy, token cost, and latency on a fixed evaluation set.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `call-a-model-with-streaming-output`
- `fall-back-to-a-second-model-provider`
- `redact-personal-data-before-sending-to-a-model`
