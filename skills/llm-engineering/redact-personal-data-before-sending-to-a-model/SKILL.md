---
name: redact-personal-data-before-sending-to-a-model
description: Redact personal data before model submission while preserving task-relevant signals and audit evidence. Use when the user wants to remove personal information from text sent to an external LLM.
domain: llm-engineering
tags: [pii, redaction, privacy, data-protection]
triggers: ["redact personal data for llm", "remove pii before model call", "mask sensitive prompt data"]
---

# Redact personal data before model submission while preserving task-relevant signals and audit evidence

## Purpose

Redact personal data before model submission while preserving task-relevant signals and audit evidence.

## When to use

Use when the user wants to remove personal information from text sent to an external LLM.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Inventory the personal data fields present in prompts, files, and tool arguments.
2. Choose tokenization, masking, or deletion for each sensitive field.
3. Replace sensitive values with stable placeholders that retain reference consistency.
4. Measure utility loss and redaction coverage on representative examples.
5. Block transmission when a detected sensitive field remains unredacted.

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
- `fall-back-to-a-second-model-provider`
- `build-a-model-router-by-task-difficulty`
