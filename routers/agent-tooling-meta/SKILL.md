---
name: router-agent-tooling-meta
description: Route work in the Agent tooling and meta-skills domain to the right leaf skill. Use when a task clearly belongs to agent-tooling-meta.
domain: agent-tooling-meta
tags: [router, routing, agent-tooling-meta]
triggers: ["route a agent-tooling-meta task", "which agent-tooling-meta skill should I use"]
---

# Agent tooling and meta-skills router

## Purpose

List every leaf skill in the agent-tooling-meta domain and say when to prefer each one, so the master skill can pick a chain without loading the whole catalogue.

## When to use

Use when the task is clearly inside agent-tooling-meta and the master skill needs the structural neighbours of a shortlisted skill.

## When NOT to use

Do not use this for building a product feature; use software-engineering instead.

## Inputs required

- The agent workflow being improved
- The failure mode observed
- The harness or toolchain in use

## Procedure

1. Read the task and the domain framing above.
2. Scan the skill table below and shortlist at most five candidates.
3. Drop any candidate whose When NOT to use clause rules it out.
4. Order the survivors from most specific to most general.
5. Recommend one primary skill and at most three supporting skills.

## Output contract

An improved skill, prompt, tool wrapper or evaluation that raises the observed failure rate down.

## Validation checklist

- [ ] The change is measured against the failure it targets
- [ ] The skill follows the repository's format exactly
- [ ] The generated artefacts are reproducible

## Safety notes

Never widen an agent's permissions to work around a skill bug, and never encode a secret in a prompt or skill.

## Related skills

- `master`

## Skills in this domain

| Skill | Use when |
|---|---|
| `add-a-citation-to-a-skill` | Use when the user wants a skill to record where its guidance came from. |
| `audit-a-catalogue-for-gaps` | Use when the user wants to know what a skill catalogue is missing. |
| `build-a-skill-evaluation-harness` | Use when the user wants to measure the quality of a skill catalogue automatically. |
| `compose-two-skills-into-a-chain` | Use when the user wants two skills run in sequence to complete one larger task. |
| `create-a-skill-template` | Use when the user writes many skills and wants the structure to be identical every time. |
| `design-a-router-for-a-skill-catalogue` | Use when the user wants to build the selection layer over a large set of skills. |
| `design-a-skill-for-a-multi-domain-task` | Use when the user wants one skill for a task that needs several kinds of expertise. |
| `design-a-skill-for-a-repeated-task` | Use when the user thinks a task happens often enough to justify a skill. |
| `document-a-skill-for-another-agent` | Use when the user wants a skill documented for consumption by a different agent. |
| `keep-skill-outputs-consistent` | Use when the user wants several skills to produce results that can be handled the same way. |
| `manage-skill-dependencies-between-domains` | Use when the user wants to change or review skills that depend on each other across domains. |
| `measure-skill-routing-accuracy` | Use when the user wants to know how often the router picks the right skill. |
| `migrate-a-skill-to-a-new-format` | Use when the user changes the structure of the skill format and must move the existing catalogue. |
| `name-and-version-a-skill` | Use when the user wants to name a new skill and decide how its version will move. |
| `plan-a-skill-catalogue-growth` | Use when the user wants to grow a skill catalogue in a way that pays for itself. |
| `retire-a-skill-nobody-uses` | Use when the user wants to remove a skill that is no longer earning its place. |
| `review-a-skill-for-quality` | Use when the user wants a critical review of a skill before it is published. |
| `structure-a-skill-file` | Use when the user is writing or repairing the layout of a skill file. |
| `test-a-skill-against-real-requests` | Use when the user wants to check that a skill works on the requests that motivated it. |
| `tune-a-routing-keyword-list` | Use when the user wants to improve the words a router matches on. |
| `write-a-migration-note-for-a-skill-change` | Use when the user changes a skill in a way that alters how it should be called or used. |
| `write-a-reusable-skill` | Use when the user wants to turn a repeated manual task into a skill other agents can run. |
| `write-a-skill-regression-suite` | Use when the user wants tests that protect the routing and output of the current catalogue. |
| `write-a-skill-safety-checklist` | Use when the user wants to make the risky steps of a skill explicit. |
| `write-a-skill-trigger-phrase` | Use when the user wants better trigger phrases so a skill gets picked up for the right requests. |
| `write-a-skill-usage-guide` | Use when the user wants a guide explaining how to use a skill they have built. |
