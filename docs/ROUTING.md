# Routing

The catalogue is 1,209 skills across 42 domains. Routing picks the right one — or the
right chain — without loading the whole corpus into context.

Three mechanisms work together, in this order.

```
free-form task
      │
      ▼
┌───────────────────────────────────────┐
│ 1. Deterministic BM25 scorer          │  agentskills route "<task>" --top 8
│    ranks every skill, same input      │  → ranked shortlist + matched terms
│    always gives the same output       │
└───────────────────────────────────────┘
      │
      ▼
┌───────────────────────────────────────┐
│ 2. Master skill                       │  skills/master/SKILL.md
│    chooses one primary skill plus     │  → the chain to run, in order
│    up to three supporting skills       │
└───────────────────────────────────────┘
      │
      ▼
┌───────────────────────────────────────┐
│ 3. Domain routers                     │  routers/<domain>/SKILL.md
│    narrow a domain to its structural  │  → the neighbouring skills of a
│    neighbours                          │    shortlisted skill
└───────────────────────────────────────┘
```

## Layer 1 — the deterministic BM25 scorer

`agentskills route "<task>"` ranks every catalogue entry against a free-form task
description. It is implemented in `src/agentskills/router.py` with the standard
library only.

### Field weights

Each skill is treated as a document made of its fields, repeated by weight:

| Field | Weight |
|---|---|
| `name` | 3 |
| `triggers` | 3 |
| `tags` | 2 |
| `description` | 2 |
| `domain` | 1 |

### Parameters

- `K1 = 1.5` — term-frequency saturation.
- `B = 0.75` — length normalisation.

### Tokenisation

`tokenize()` lowercases the text and splits on non-alphanumerics, but keeps
hyphenated compounds whole **and** emits their parts. `blue-green-deploy` becomes
`["blue-green-deploy", "blue", "green", "deploy"]`, so a query for "green deploy"
still matches it.

### Scoring

For each query term present in the document, the scorer adds the standard BM25
contribution:

```
idf    = ln(1 + (N - df + 0.5) / (df + 0.5))
score += idf * (tf * (K1 + 1)) / (tf + K1 * (1 - B + B * len / avg_len))
```

where `N` is the number of skills, `df` the number of skills containing the term,
`tf` its frequency in this skill's weighted document, and `len` the weighted
document length.

### Determinism

- Query terms are de-duplicated while preserving order.
- Results are sorted by `(-score, skill.name)` — ties break on the name, ascending.
- Scores are rounded to six decimals before sorting, so floating-point noise cannot
  reorder equal matches.
- The same query always produces the same ranking, on any machine, with no model in
  the loop.

That property is what makes the catalogue testable: a routing test asserts an exact
skill name at rank 1, and it stays true across releases.

### Output

```console
$ agentskills route "roll back a failed blue green deploy" --top 3
1. implement-blue-green-traffic-shifting  [devops-cloud]  score=11.42
   matched: roll, back, failed, blue, green, deploy
2. write-a-kubernetes-rollback-procedure   [devops-cloud]  score=7.91
   matched: roll, back, blue, green, deploy
3. rehearse-a-disaster-recovery-drill      [devops-cloud]  score=4.18
   matched: roll, back, deploy
```

`--json` returns the same information with the query, score, matched terms and the
field each match came from.

## Layer 2 — the master skill

`skills/master/SKILL.md` is the only hand-written skill in the corpus. It turns the
scorer's shortlist into a decision.

Its procedure, in short:

1. Restate the task; extract intent, constraints and expected artefacts.
2. Run `agentskills route "<task>" --top 8`.
3. Open `routers/<domain>/SKILL.md` for each shortlisted domain.
4. Choose a chain: exactly one primary skill plus up to three supporting skills.
5. Check every candidate's *When NOT to use* clause and drop it if the task does not fit.
6. If nothing clears the bar, split the task and route each part; if it still fails,
   ask the user one precise question.
7. Load only the chosen `SKILL.md` files and run their procedures in order.
8. Run each chosen skill's validation checklist.
9. Report the skills that ran, the artefacts produced and what is left undone.

The master skill selects and sequences; it does not execute external actions itself.

## Layer 3 — the domain routers

`routers/<domain>/SKILL.md` lists every skill in one domain with its *When to use*
clause. A router's own procedure is to shortlist at most five candidates, drop any
whose *When NOT to use* clause rules it out, order the survivors from most specific
to most general, and recommend one primary plus at most three supporting skills.

This is the cheap layer: one router file is a few kilobytes, against megabytes for
the full catalogue. It lets the master skill understand a domain's structure without
reading every leaf skill in it.

The full domain map — domain, router path and skill count — is in the generated
`skills/master/APPENDIX.md`.

## When to use which

| Situation | Layer |
|---|---|
| A quick lookup, a script, a test | BM25 scorer only |
| A request that could plausibly match several skills | Scorer, then master |
| A task that spans two domains | Scorer, then master, then the routers of both domains |
| A task that exactly matches one obvious skill | Load that skill directly; skip routing |

## Using the router directly

```bash
# Rank skills for a task
agentskills route "add retry backoff to the payment client" --top 5

# Machine-readable output
agentskills route "add retry backoff" --top 5 --json

# Inspect one skill
agentskills show design-retry-backoff

# Everything in one domain
agentskills list --domain devops-cloud
```

`list`, `show` and `route` read the packaged index
(`src/agentskills/data/catalog.json`, shipped in the wheel), so they work from an
installed package with no repository checkout. Set `AGENTSKILLS_CATALOG` to point at
a different index — useful for testing a catalogue before publishing it.
