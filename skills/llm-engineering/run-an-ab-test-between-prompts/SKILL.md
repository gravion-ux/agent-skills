---
name: run-an-ab-test-between-prompts
description: Run a controlled A/B test between prompts with fixed traffic splits and confidence checks. Use when the user wants to determine which prompt performs better for a live model workflow.
domain: llm-engineering
tags: [ab-testing, prompts, experiments, statistics]
triggers: ["ab test prompts", "compare prompt variants", "run live prompt experiment"]
---

# Run a controlled A/B test between prompts with fixed traffic splits and confidence checks

## Purpose

Run a controlled A/B test between prompts with fixed traffic splits and confidence checks.

## When to use

Use when the user wants to determine which prompt performs better for a live model workflow.

## When NOT to use

Do not use this for training or fine-tuning a model from scratch; use ml-model-training instead.

## Inputs required

- The model or provider in use
- The prompt or request contract
- The evaluation signal and the cost ceiling

## Procedure

1. Define one primary metric, guardrail metrics, and the minimum detectable effect.
2. Randomize eligible requests into prompt variants with stable assignment keys.
3. Run both variants with identical model settings and sampling policy.
4. Check sample balance, metric quality, latency, and cost for each variant.
5. Report the estimate and uncertainty, and stop if a guardrail is breached.

## Output contract

A working prompt or integration plus the evaluation numbers that justify it.

## Validation checklist

- [ ] The change is scored on a fixed evaluation set
- [ ] Token cost and latency are measured
- [ ] Failure modes are documented

## Safety notes

Never log raw prompts that may contain personal data, and never ship a prompt change without its evaluation numbers.

## Related skills

- `run-an-offline-evaluation-suite`
- `build-an-agentic-rag-loop`
- `choose-between-a-chain-and-a-router`
