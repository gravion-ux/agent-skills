# agent-skills

A library of 1200+ agent skills with a deterministic router that selects the right skill
for any task, from everyday assistant work down to single-step micro-tasks.

The catalogue is under construction: the package, router, generator and validator land
first, then the domain catalogues. See `docs/superpowers/specs/2026-11-20-agent-skills-design.md`
for the design and `docs/ARCHITECTURE.md` for the pipeline.

## Install

```bash
python -m pip install agentskills
```

## Use

```bash
agentskills list --domain ai-agents
agentskills route "migrate a database to postgres" --top 5
agentskills show migrate-postgres-schema
```

Licensed under MIT.
