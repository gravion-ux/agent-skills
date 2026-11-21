# tests/test_generation.py
import json

from agentskills.frontmatter import parse_frontmatter
from agentskills.generation import (
    SECTION_ORDER,
    build_skill,
    render_catalog_markdown,
    render_index_json,
    render_master_appendix,
    render_router_markdown,
    render_skill_markdown,
)
from agentskills.spec import DomainProfile, spec

ENTRY = spec(
    "migrate-postgres-schema",
    summary="Move a relational schema to PostgreSQL with a zero-downtime runbook.",
    when="the user needs to port MySQL, SQLite or SQL Server DDL to PostgreSQL",
    steps=(
        "Inventory the schema and every dependent object",
        "Translate dialect-specific types",
        "Apply expand DDL to the target",
        "Dual-write from the old source",
        "Backfill historical rows in batches",
    ),
    tags=("postgres", "migration", "schema"),
    triggers=("migrate to postgres", "port database to postgres"),
    related=(),
)

PROFILE = DomainProfile(
    domain="data-engineering",
    title="Data engineering",
    when_not_to_use="Do not use this for exploratory analysis; use data-analysis instead.",
    inputs=("The source systems and their schemas",),
    output_contract="A documented, quality-checked dataset.",
    checks=("The output matches the agreed schema",),
    safety="Never rewrite a production table without a backup.",
)

SKILL = build_skill(ENTRY, PROFILE, siblings=("backup-postgres",))


def test_section_order_is_the_nine_required_sections() -> None:
    assert SECTION_ORDER == (
        "Purpose",
        "When to use",
        "When NOT to use",
        "Inputs required",
        "Procedure",
        "Output contract",
        "Validation checklist",
        "Safety notes",
        "Related skills",
    )


def test_build_skill_assembles_every_field() -> None:
    assert SKILL.description == (
        "Move a relational schema to PostgreSQL with a zero-downtime runbook. "
        "Use when the user needs to port MySQL, SQLite or SQL Server DDL to PostgreSQL."
    )
    assert SKILL.when_to_use.startswith("Use when ")
    assert SKILL.related == ("backup-postgres",)


def test_rendered_skill_has_frontmatter_and_all_sections() -> None:
    text = render_skill_markdown(SKILL)
    assert text.startswith("---\n")
    assert "name: migrate-postgres-schema" in text
    assert "description: " in text
    for heading in SECTION_ORDER:
        assert f"## {heading}" in text


def test_rendered_skill_contains_the_procedure_steps() -> None:
    text = render_skill_markdown(SKILL)
    assert "1. Inventory the schema and every dependent object" in text


def test_rendered_skill_lists_related_skills() -> None:
    assert "`backup-postgres`" in render_skill_markdown(SKILL)


def test_rendered_router_lists_every_leaf_skill() -> None:
    text = render_router_markdown("data-engineering", (SKILL,), PROFILE)
    assert "migrate-postgres-schema" in text
    assert "name: router-data-engineering" in text
    for heading in SECTION_ORDER:
        assert f"## {heading}" in text


def test_rendered_router_frontmatter_declares_triggers() -> None:
    fields, _ = parse_frontmatter(render_router_markdown("data-engineering", (SKILL,), PROFILE))
    assert "triggers" in fields
    assert "trigiggers" not in fields


def test_rendered_index_is_valid_json_with_the_skill() -> None:
    payload = json.loads(render_index_json((SKILL,), "0.1.0"))
    assert payload["version"] == "0.1.0"
    assert payload["generated_from"] == "catalog/source"
    assert payload["skills"][0]["name"] == "migrate-postgres-schema"
    assert payload["skills"][0]["related"] == ["backup-postgres"]


def test_rendered_catalog_markdown_lists_the_skill() -> None:
    text = render_catalog_markdown((SKILL,), "0.1.0")
    assert "migrate-postgres-schema" in text
    assert "data-engineering" in text


def test_rendered_master_appendix_lists_the_domain() -> None:
    text = render_master_appendix((SKILL,), "0.1.0")
    assert "data-engineering" in text
    assert "routers/data-engineering/SKILL.md" in text
