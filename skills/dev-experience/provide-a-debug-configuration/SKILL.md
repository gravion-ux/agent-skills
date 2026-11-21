---
name: provide-a-debug-configuration
description: Create a shared debug configuration that launches the service with breakpoints, ports, and environment values. Use when the user wants a consistent local debugging configuration for a repository.
domain: dev-experience
tags: [debug-configuration, ide-setup, developer-tooling]
triggers: ["provide a debug configuration", "set up debugger launch config", "add shared VS Code debug config"]
---

# Create a shared debug configuration that launches the service with breakpoints, ports, and environment values

## Purpose

Create a shared debug configuration that launches the service with breakpoints, ports, and environment values.

## When to use

Use when the user wants a consistent local debugging configuration for a repository.

## When NOT to use

Do not use this for a one-off local script; use software-engineering instead.

## Inputs required

- The recurring friction the team hits
- Who experiences it and how often
- The tooling already in place

## Procedure

1. Identify the runtime, launch command, debug ports, and required environment variables.
2. Create a launch configuration using repository-defined commands and paths.
3. Bind source directories so breakpoints resolve without manual path mapping.
4. Document how to start dependencies before launching the debugger.
5. Verify a breakpoint, hot reload, and clean shutdown in a fresh session.

## Output contract

A working tool, template or command plus the documentation and adoption note.

## Validation checklist

- [ ] The friction is measured before and after
- [ ] The new path is documented and discoverable
- [ ] It does not add a step to the critical path

## Safety notes

Never change a shared default that silently affects every developer without a migration note.

## Related skills

- `provide-a-one-command-start-script`
- `add-a-health-check-endpoint`
- `add-editor-support-files-to-a-repo`
