---
name: write-a-good-completion-prompt
description: Draft a completion prompt that defines the task, input, output, and success criteria. Use when the user needs a clear baseline prompt for a text completion.
domain: llm-engineering
tags: [prompt-design, completion, baseline]
triggers: ["llm completion prompt", "write an llm completion prompt", "baseline completion prompt"]
---

# Draft a completion prompt that defines the task, input, output, and success criteria

## Purpose

Draft a completion prompt that defines the task, input, output, and success criteria.

## When to use

Use when the user needs a clear baseline prompt for a text completion.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Name the model provider and the request contract.
2. Define the task, supplied context, and desired output.
3. Specify the output format and concrete acceptance criteria.
4. Run the prompt on a fixed evaluation set and record accuracy.
5. Measure token cost and latency before approving the prompt.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `write-a-regression-test-for-prompt-changes`
- `build-a-system-prompt-with-guardrails`
- `structure-a-prompt-with-context-and-instructions`
