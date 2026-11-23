# tests/test_source_counts.py
from catalog.source import domain_of

TOTAL_SKILLS = 1224
TOTAL_DOMAINS = 42

EXPECTED = {
    "agent-tooling-meta": 26,
    "ai-agents": 57,
    "api-design": 22,
    "architecture-design": 26,
    "business-ops": 30,
    "code-quality": 30,
    "communication": 26,
    "content-creation": 30,
    "cooking-food": 14,
    "data-analysis": 30,
    "data-engineering": 40,
    "databases": 33,
    "design-ux": 34,
    "dev-experience": 30,
    "devops-cloud": 48,
    "documentation": 30,
    "education": 22,
    "finance-accounting": 18,
    "health-wellness": 18,
    "home-diy": 18,
    "hr-recruiting": 18,
    "image-visual": 22,
    "learning-skills": 15,
    "legal-compliance": 18,
    "llm-engineering": 44,
    "ml-model-training": 34,
    "mobile-desktop": 22,
    "networking": 26,
    "observability": 26,
    "personal-finance": 12,
    "productivity": 35,
    "project-management": 26,
    "relationships-social": 11,
    "research": 27,
    "sales-marketing": 26,
    "security": 66,
    "software-engineering": 66,
    "technical-writing": 22,
    "testing-qa": 34,
    "travel-lifestyle": 18,
    "video-audio": 22,
    "web-development": 52,
}


def _actual_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    for _, domain in domain_of():
        counts[domain] = counts.get(domain, 0) + 1
    return counts


def test_every_domain_has_the_expected_count() -> None:
    actual = _actual_counts()
    for domain, count in EXPECTED.items():
        assert actual.get(domain, 0) == count, domain


def test_no_domain_outside_the_expected_set() -> None:
    actual = _actual_counts()
    assert set(actual) == set(EXPECTED)


def test_the_catalogue_totals_match_the_published_size() -> None:
    actual = _actual_counts()
    assert len(actual) == TOTAL_DOMAINS
    assert sum(actual.values()) == TOTAL_SKILLS
