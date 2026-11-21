---
name: write-a-regression-test-for-prompt-changes
description: Create a repeatable regression gate that compares prompt versions on fixed quality, cost, and latency checks. Use when the user wants to prevent a prompt change from degrading production behavior.
domain: llm-engineering
tags: [prompt-regression, evaluation, release-gate]
triggers: ["llm prompt regression test", "regression test an llm prompt", "llm prompt release gate"]
---

# Create a repeatable regression gate that compares prompt versions on fixed quality, cost, and latency checks

## Purpose

Create a repeatable regression gate that compares prompt versions on fixed quality, cost, and latency checks.

## When to use

Use when the user wants to prevent a prompt change from degrading production behavior.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Freeze a representative evaluation set with expected outcomes and thresholds.
2. Record the current prompt's quality, token cost, latency, and failure modes as the baseline.
3. Run the candidate prompt against the same set without changing the request contract.
4. Fail the test when any quality threshold regresses or the token ceiling is exceeded.
5. Store the comparison report without raw prompts or personal data.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `write-a-good-completion-prompt`
- `build-a-retrieval-pipeline-for-a-model`
- `build-a-shadow-deployment-for-a-model`
