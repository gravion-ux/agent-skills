# tests/test_router.py
from agentskills.catalog import Catalogue, Skill
from agentskills.router import route, tokenize


def make_skill(
    name: str,
    description: str,
    triggers: tuple[str, ...],
    tags: tuple[str, ...],
) -> Skill:
    return Skill(
        name=name,
        domain="testing",
        summary=description,
        description=description,
        tags=tags,
        triggers=triggers,
        steps=("step one", "step two", "step three"),
        when_to_use="when the user asks",
        when_not_to_use="not for other things",
        inputs=("an input",),
        output_contract="an output",
        checks=("a check",),
        safety="be careful",
        related=(),
    )


CATALOGUE = Catalogue(
    skills=(
        make_skill(
            "migrate-postgres-schema",
            "Move a relational schema to PostgreSQL. Use when porting a database.",
            ("migrate to postgres",),
            ("postgres", "migration"),
        ),
        make_skill(
            "bake-sourdough-bread",
            "Bake sourdough bread at home. Use when baking a loaf.",
            ("bake bread",),
            ("baking", "cooking"),
        ),
    ),
    version="0.1.0",
)


def test_tokenize_splits_hyphens_and_keeps_the_compound() -> None:
    assert tokenize("voice-synthesis") == ["voice-synthesis", "voice", "synthesis"]


def test_tokenize_lowercases_and_drops_punctuation() -> None:
    assert tokenize("Deploy, the API!") == ["deploy", "the", "api"]


def test_route_ranks_the_matching_skill_first() -> None:
    results = route(CATALOGUE, "migrate to postgres", top=5)
    assert results
    assert results[0].skill.name == "migrate-postgres-schema"


def test_route_is_deterministic_and_ties_break_by_name() -> None:
    first = [item.skill.name for item in route(CATALOGUE, "use when something", top=5)]
    second = [item.skill.name for item in route(CATALOGUE, "use when something", top=5)]
    assert first == second == sorted(first)


def test_route_with_no_match_returns_nothing() -> None:
    assert route(CATALOGUE, "zzzzqqqq unrelated", top=5) == []


def test_route_with_empty_query_returns_nothing() -> None:
    assert route(CATALOGUE, "   ", top=5) == []


def test_score_is_reported_with_matched_terms() -> None:
    result = route(CATALOGUE, "bake bread", top=1)[0]
    assert result.skill.name == "bake-sourdough-bread"
    assert "bread" in result.matched
    assert result.score > 0


def test_each_matched_term_reports_the_field_it_hit() -> None:
    result = route(CATALOGUE, "bake bread", top=1)[0]
    assert len(result.fields) == len(result.matched)
    for term, field in zip(result.matched, result.fields, strict=True):
        assert term
        assert field in {"name", "triggers", "tags", "description", "domain"}


def test_route_respects_the_top_limit() -> None:
    assert len(route(CATALOGUE, "use when something", top=1)) == 1
