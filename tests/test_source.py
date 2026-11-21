# tests/test_source.py
from catalog.source import all_specs, domain_of
from catalog.source._domains import DOMAIN_PROFILES
from catalog.source._types import spec


def test_every_domain_has_a_profile() -> None:
    assert len(DOMAIN_PROFILES) == 42
    for domain in DOMAIN_PROFILES:
        assert domain == domain.lower()
        assert " " not in domain
        assert DOMAIN_PROFILES[domain].domain == domain


def test_every_profile_is_complete() -> None:
    for domain, profile in DOMAIN_PROFILES.items():
        assert profile.title
        assert profile.when_not_to_use
        assert profile.inputs
        assert profile.output_contract
        assert profile.checks
        assert profile.safety
        assert domain not in profile.when_not_to_use.split(";")[0]


def test_spec_helper_builds_a_skill_spec() -> None:
    entry = spec(
        "example-skill",
        summary="Do one example thing well.",
        when="the user asks for the example thing",
        steps=("Step one", "Step two", "Step three", "Step four"),
        tags=("example",),
        triggers=("do the example thing",),
    )
    assert entry.name == "example-skill"
    assert entry.related == ()


def test_all_specs_returns_a_tuple_and_domain_pairs_match() -> None:
    specs = all_specs()
    assert isinstance(specs, tuple)
    pairs = domain_of()
    assert len(pairs) == len(specs)
    for _, domain in pairs:
        assert domain == domain.lower()
        assert " " not in domain


def test_spec_names_are_unique() -> None:
    names = [entry.name for entry in all_specs()]
    assert len(names) == len(set(names))
