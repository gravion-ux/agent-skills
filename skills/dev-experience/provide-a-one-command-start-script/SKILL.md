---
name: provide-a-one-command-start-script
description: Provide one command that starts every required local service and confirms the stack is ready. Use when the user needs a dependable single command to start the local application stack.
domain: dev-experience
tags: [local-startup, service-orchestration, developer-tooling]
triggers: ["one command local startup", "create a one-command start script", "start the local stack in one command"]
---

# Provide one command that starts every required local service and confirms the stack is ready

## Purpose

Provide one command that starts every required local service and confirms the stack is ready.

## When to use

Use when the user needs a dependable single command to start the local application stack.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. List the local processes, ports, health checks, and startup order.
2. Implement a command that starts dependencies and waits for each readiness signal.
3. Stop already-running services cleanly instead of starting duplicate instances.
4. Print local URLs and a recovery command after every service is ready.
5. Verify the command from a stopped machine and time its total startup.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `provide-a-debug-configuration`
- `add-a-health-check-endpoint`
- `add-editor-support-files-to-a-repo`
