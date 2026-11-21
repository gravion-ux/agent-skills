---
name: use-few-shot-examples-in-a-prompt
description: Add representative examples that demonstrate the inputs, reasoning pattern, and expected outputs. Use when the user wants a prompt to learn a task from demonstrations.
domain: llm-engineering
tags: [few-shot, examples, prompt-design]
triggers: ["few-shot llm prompt", "llm prompt examples", "add few-shot examples to an llm prompt"]
---

# Add representative examples that demonstrate the inputs, reasoning pattern, and expected outputs

## Purpose

Add representative examples that demonstrate the inputs, reasoning pattern, and expected outputs.

## When to use

Use when the user wants a prompt to learn a task from demonstrations.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Choose examples that cover the target format and edge cases.
2. Keep each example focused on one input and one expected output.
3. Remove contradictory examples and duplicated reasoning patterns.
4. Run the prompt with and without examples on the same evaluation set.
5. Keep the version that improves accuracy without exceeding the token cost ceiling.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `build-a-system-prompt-with-guardrails`
- `design-a-model-in-the-loop-classifier`
- `detect-hallucination-in-a-generated-answer`
