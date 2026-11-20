# Agent Skills Library — Design

**Date:** 2026-11-20
**Status:** Approved
**Repository:** `gravion-ux/agent-skills` (public)
**Distribution:** `agentskills` (Python ≥ 3.11, zero runtime dependencies)

## 1. Problem

The user's request: build a public repository containing **1000+ agent skills** covering
every kind of work an AI agent performs — from ordinary daily-assistant tasks down to
micro-tasks — plus a **master skill** that holds the whole catalogue and selects the
right skill(s) for a given task.

The failure mode of "just list 1000 skills" is a pile of near-identical files that no
agent can route through. The failure mode of "one huge master skill" is a context blowout
that scales badly. This design solves both by separating three concerns:

1. **Content** — each skill is a standalone, complete playbook.
2. **Selection** — a deterministic scorer narrows 1000+ candidates to a shortlist.
3. **Composition** — a master skill and per-domain routers decide *which* shortlisted
   skills to load, in what order, and how to validate the result.

## 2. Goals and non-goals

### Goals

- 1000+ leaf skills, every one with a full playbook body (not a stub, not a reworded
  duplicate).
- Coverage from everyday assistant work down to single-step micro-tasks, and from
  ordinary AI assistance up to autonomous-agent patterns.
- A master skill that routes any free-form task to the correct skill(s).
- A machine-readable index that is the single source of truth for routing, docs and
  validation.
- Zero runtime dependencies; everything works fully offline.
- A package that other agents and humans can consume: browse, route, export, pack.

### Non-goals

- No skill performs network access or requires an LLM at runtime.
- No two skills may be cosmetic variants of each other; the validator enforces uniqueness
  of names, descriptions and trigger sets.
- The repository is not an agent runtime. It is a catalogue plus a routing library.
- No scraping, no marketplace clone, no paid API integration.

## 3. Repository layout

```
agent-skills/
├── README.md
├── AGENTS.md                       # operating instructions for agents working in this repo
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE                         # MIT
├── VERSION
├── .gitignore
├── .gitattributes                  # * text=auto eol=lf
├── pyproject.toml
├── docs/
│   ├── superpowers/specs/2026-11-20-agent-skills-design.md
│   ├── ARCHITECTURE.md
│   ├── SKILL_FORMAT.md
│   ├── ROUTING.md
│   └── CONTRIBUTING_SKILLS.md
├── skills/
│   ├── master/SKILL.md             # the master routing skill (hand-written)
│   ├── master/APPENDIX.md          # GENERATED — domain map and scoring reference
│   └── <domain>/<skill-name>/SKILL.md
├── routers/
│   └── <domain>/SKILL.md           # ~35 domain router skills
├── catalog/
│   ├── source/                     # curated source of truth
│   │   ├── __init__.py
│   │   ├── _types.py
│   │   ├── _domains.py
│   │   └── <domain>.py
│   └── CATALOG.md                  # GENERATED — human-readable index
├── src/agentskills/
│   ├── __init__.py
│   ├── spec.py                     # canonical SkillSpec / DomainProfile / spec()
│   ├── catalog.py                  # load + model the catalogue
│   ├── frontmatter.py              # minimal YAML-subset frontmatter parser
│   ├── router.py                   # BM25 scorer
│   ├── generation.py               # catalogue -> skill files / index / routers
│   ├── validation.py               # skill validator (single implementation)
│   ├── exporters.py                # export / pack
│   ├── cli.py                      # agentskills list|show|route|validate|export|pack
│   └── data/catalog.json           # GENERATED — packaged machine-readable index
├── scripts/
│   ├── generate_skills.py          # thin wrapper over agentskills.generation
│   ├── build_index.py              # thin wrapper over agentskills.generation
│   ├── validate_skills.py          # thin wrapper over agentskills.validation
│   └── scan-secrets.py
├── tests/
│   ├── test_catalog.py
│   ├── test_router.py
│   ├── test_generation.py
│   └── test_validate.py
└── .github/workflows/
    ├── ci.yml
    └── secret-scan.yml
```

## 4. The skill format

Each leaf skill is a directory `skills/<domain>/<skill-name>/` containing `SKILL.md`.

```markdown
---
name: migrate-postgres-schema
description: Move a relational schema to PostgreSQL with a zero-downtime expand/contract runbook. Use when porting MySQL, SQLite or SQL Server DDL to PostgreSQL.
domain: data-engineering
tags: [postgres, migration, schema]
triggers: ["migrate to postgres", "port database to postgres"]
---

# Move a relational schema to PostgreSQL

## Purpose
One or two sentences on the outcome this skill guarantees.

## When to use
The concrete situations that should select this skill.

## When NOT to use
Near-neighbour tasks this skill must not be used for, and where to go instead.

## Inputs required
What must be known before the procedure can start.

## Procedure
1. Concrete, ordered, executable steps.

## Output contract
What the skill produces, in what shape, so the next skill can consume it.

## Validation checklist
- [ ] Checks the caller must pass before declaring success.

## Safety notes
Irreversible actions, data loss risks, consent boundaries, default-deny behaviour.

## Related skills
Links to sibling and follow-on skills by name.
```

Frontmatter rules: `name` matches the directory name; `description` is a single line
that states both *what* and *when* (contains an explicit trigger clause); `domain`,
`tags` and `triggers` are required. Body sections are mandatory in the order above.

**Full playbook depth applies to all 1000+ skills.** Domain-level templates supply the
`when NOT to use`, `inputs`, `output contract`, `checklist` and `safety` framing; the
per-skill `purpose`, `procedure` and `triggers` are individually authored, so no two
skills are interchangeable.

## 5. Taxonomy

~42 domains; **hard floor 1000 leaf skills**, target ≈ 1200.

| Domain | Target | Domain | Target |
|---|---|---|---|
| ai-agents | 52 | documentation | 30 |
| llm-engineering | 44 | technical-writing | 22 |
| software-engineering | 66 | content-creation | 30 |
| web-development | 52 | design-ux | 34 |
| mobile-desktop | 22 | image-visual | 22 |
| devops-cloud | 48 | video-audio | 22 |
| data-engineering | 40 | data-analysis | 30 |
| databases | 33 | ml-model-training | 34 |
| security | 60 | research | 26 |
| networking | 26 | education | 22 |
| dev-experience | 30 | productivity | 34 |
| code-quality | 30 | communication | 26 |
| architecture-design | 26 | project-management | 26 |
| testing-qa | 34 | business-ops | 30 |
| api-design | 22 | finance-accounting | 18 |
| observability | 26 | legal-compliance | 18 |
| learning-skills | 14 | hr-recruiting | 18 |
| sales-marketing | 26 | health-wellness | 18 |
| home-diy | 18 | travel-lifestyle | 18 |
| cooking-food | 14 | personal-finance | 11 |
| relationships-social | 11 | agent-tooling-meta | 26 |

The domain set deliberately spans the whole range the user asked for: ordinary daily
assistant work (`productivity`, `communication`, `cooking-food`, `home-diy`) through
professional engineering (`software-engineering`, `devops-cloud`, `security`) up to
autonomous-agent engineering (`ai-agents`, `agent-tooling-meta`).

## 6. Routing — three layers, all active

The user chose to combine all three mechanisms. They are complementary, not competing.

### Layer 1 — deterministic scorer

`agentskills route "<task>" --top K` runs a BM25-style ranking over the packaged
catalogue index (`agentskills/data/catalog.json`, overridable with the
`AGENTSKILLS_CATALOG` environment variable during development). The indexed fields are
`name`, `description`, `tags`, `triggers` and `domain`, with field-specific weights.
Tokenisation lowercases, splits on non-alphanumerics and keeps hyphenated compounds as
both a compound token and its parts. The scorer is pure Python standard library, fully
deterministic and unit-tested.

Output: ranked candidates with score, matched terms and the field each term matched.

### Layer 2 — master skill

`skills/master/SKILL.md` is the policy layer. Its procedure:

1. Restate the task; extract intent, constraints and expected artifacts.
2. Run the scorer for a shortlist.
3. Read the domain router map to check structural neighbours.
4. Choose a chain: one primary skill plus up to three supporting skills. Check each
   candidate's *When NOT to use* before committing.
5. Load only the chosen `SKILL.md` files and execute their procedures in order.
6. Run each skill's validation checklist.
7. Report which skills ran, what was produced, and what remains.

If nothing clears the score threshold, the master decomposes the task or asks the user.
It never loads the full catalogue into context.

### Layer 3 — domain routers

`routers/<domain>/SKILL.md` — one file per domain (42 files). Each lists its leaf skills,
states when to prefer which, and names the chains that recur inside that domain. These
give the master a fast structural map and give humans a browsable entry point.

### Shared source of truth

All three layers read the packaged index at `src/agentskills/data/catalog.json`, which is
generated from `catalog/source/`. The validator fails CI if the index and the files on
disk disagree, so routing can never silently drift from the catalogue.

## 7. Package and CLI

`agentskills` — src layout, zero runtime dependencies, Python ≥ 3.11, console script
`agentskills`.

| Command | Behaviour |
|---|---|
| `agentskills list [--domain D] [--json]` | list skills, optionally filtered by domain |
| `agentskills show <skill-name>` | print one skill's catalogue entry |
| `agentskills route "<task>" [--top N] [--json]` | deterministic shortlist with scores and matched terms |
| `agentskills validate` | run the skill validator over the repository |
| `agentskills export --out DIR` | copy skill files into another agent's skills directory |
| `agentskills pack --out FILE` | produce a distributable zip of the whole catalogue |

## 8. Generation and validation

### Generation

`scripts/generate_skills.py` reads `catalog/source/` and writes every leaf `SKILL.md` plus
every domain router. `scripts/build_index.py` writes the packaged index at
`src/agentskills/data/catalog.json` and the human mirror at `catalog/CATALOG.md`. The
master skill at `skills/master/SKILL.md` is **hand-written** — it encodes routing policy,
not catalogue data — and its per-domain appendix is generated from the same source into
`skills/master/APPENDIX.md`.

The canonical `SkillSpec` and `DomainProfile` types live in the installed package at
`src/agentskills/spec.py`; `catalog/source/_types.py` re-exports them so authoring modules
keep a single import path. The installed distribution never imports from `catalog/`, so
`pip install agentskills` yields a package that routes, validates and exports on its own.

Both generators are idempotent: running them twice produces no diff. The generated files
are committed, so consumers can clone and use the catalogue without running Python.

### Validation

`scripts/validate_skills.py` enforces, per skill:

- `SKILL.md` exists and is non-empty.
- YAML frontmatter parses and contains `name`, `description`, `domain`, `tags`, `triggers`.
- `name` equals the directory name and is unique repository-wide.
- `description` is a single line, within length bounds, and states a trigger condition.
- All nine body sections are present, in order, and non-empty.
- No placeholder markers (`TBD`, `TODO`, `FIXME`, `XXX`, `lorem`).
- Every name in `related` resolves to an existing skill.
- The packaged index at `src/agentskills/data/catalog.json` matches the catalogue source
  exactly, and `catalog/CATALOG.md` lists exactly the same skill set.

Repository-wide checks: router skills are unique and cover every domain; the master skill
exists and references the router map.

## 9. Testing

| Test file | Covers |
|---|---|
| `tests/test_catalog.py` | loader, schema validation, domain coverage |
| `tests/test_router.py` | scoring correctness, field weights, tie-breaks, empty query, no-match behaviour, determinism |
| `tests/test_generation.py` | generator idempotency, frontmatter validity, section presence |
| `tests/test_validate.py` | validator catches seeded defects (missing frontmatter, name mismatch, duplicate, dangling related, placeholder, stale index) |

CI mirrors the established house style: `ruff` lint, `mypy --strict`, pytest matrix on
3.11/3.12/3.13, a skills-validation job, a build job, and a separate secret-scan
workflow using the repository's own scanner plus TruffleHog without `base`/`head`
inputs.

## 10. Delivery sequence

1. Scaffold the repository: packaging, licence, contributing, security, ignore files.
2. Implement `catalog/source` domain modules and the `_types` / `_domains` support.
3. Implement the generator, index builder and validator.
4. Implement the `agentskills` package: catalog loader, BM25 router, exporters, CLI.
5. Generate the leaf catalogue, the domain routers and the index; hand-write the master skill.
6. Write tests, docs (`ARCHITECTURE`, `SKILL_FORMAT`, `ROUTING`, `CONTRIBUTING_SKILLS`),
   `AGENTS.md` and the README.
7. Wire CI and the secret-scan workflow; run the full local gate.
8. Commit, then request explicit confirmation before creating the public GitHub repository
   and pushing.
9. Verify CI is green on GitHub and report the live catalogue size.

## 11. Risks

| Risk | Mitigation |
|---|---|
| 1000+ entries degrade into repetitive filler | Per-skill unique purpose, procedure and trigger sets; duplicate-description check in the validator |
| Catalogue authoring is the bottleneck | Domain modules are independent files — author in parallel with disjoint ownership; fall back to sequential authoring if delegation is unavailable |
| Routing picks a plausible but wrong skill | Master must check *When NOT to use*; scorer exposes matched terms so the choice is auditable |
| Index and files drift | Validator compares index against disk; generation is idempotent |
| Repo becomes unusable at scale | Only a shortlist is ever loaded; the master never reads all skills |
