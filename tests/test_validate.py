# tests/test_validate.py
from pathlib import Path

from agentskills.validation import validate_skill_file

GOOD = """---
name: example-skill
description: Do a thing. Use when the user asks for the thing.
domain: testing
tags: [thing, example]
triggers: ["do the thing"]
---

# Do a thing

## Purpose
Do a thing well.

## When to use
Use when the user asks for the thing.

## When NOT to use
Not for unrelated work.

## Inputs required
- An input

## Procedure
1. First step
2. Second step
3. Third step

## Output contract
An output.

## Validation checklist
- [ ] It happened

## Safety notes
Be careful.

## Related skills
- None. This skill stands alone.
"""


def write(tmp_path: Path, name: str, text: str) -> Path:
    target = tmp_path / "skills" / "testing" / name / "SKILL.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8", newline="\n")
    return target


def errors(findings: list) -> list:
    return [finding for finding in findings if finding.severity == "error"]


def test_valid_skill_has_no_errors(tmp_path: Path) -> None:
    path = write(tmp_path, "example-skill", GOOD)
    assert errors(validate_skill_file(path, "example-skill")) == []


def test_missing_frontmatter_is_an_error(tmp_path: Path) -> None:
    path = write(tmp_path, "example-skill", "# No frontmatter\n")
    findings = validate_skill_file(path, "example-skill")
    assert any("frontmatter" in finding.message for finding in findings)


def test_name_mismatch_is_an_error(tmp_path: Path) -> None:
    path = write(tmp_path, "example-skill", GOOD.replace("name: example-skill", "name: other"))
    findings = validate_skill_file(path, "example-skill")
    assert any(
        finding.message == "name 'other' does not match directory 'example-skill'"
        for finding in findings
    )


def test_missing_section_is_an_error(tmp_path: Path) -> None:
    path = write(tmp_path, "example-skill", GOOD.replace("## Safety notes", "## Notes"))
    findings = validate_skill_file(path, "example-skill")
    assert any("Safety notes" in finding.message for finding in findings)


def test_sections_out_of_order_are_an_error(tmp_path: Path) -> None:
    path = write(tmp_path, "example-skill", GOOD.replace("## Safety notes", "## Related skills"))
    findings = validate_skill_file(path, "example-skill")
    assert any("order" in finding.message for finding in findings)


def test_empty_section_is_an_error(tmp_path: Path) -> None:
    path = write(tmp_path, "example-skill", GOOD.replace("Be careful.\n", ""))
    findings = validate_skill_file(path, "example-skill")
    assert any("empty" in finding.message for finding in findings)


def test_placeholder_marker_is_an_error(tmp_path: Path) -> None:
    path = write(tmp_path, "example-skill", GOOD.replace("Do a thing well.", "TODO write this."))
    findings = validate_skill_file(path, "example-skill")
    assert any("placeholder" in finding.message for finding in findings)


def test_description_without_trigger_clause_is_an_error(tmp_path: Path) -> None:
    without_trigger = GOOD.replace("Use when the user asks for the thing.", "")
    path = write(tmp_path, "example-skill", without_trigger)
    findings = validate_skill_file(path, "example-skill")
    assert any("Use when" in finding.message for finding in findings)


def test_long_description_is_an_error(tmp_path: Path) -> None:
    long_description = "Do a thing. " + ("x" * 1100)
    path = write(
        tmp_path,
        "example-skill",
        GOOD.replace("Do a thing. Use when", long_description + " Use when"),
    )
    findings = validate_skill_file(path, "example-skill")
    assert any("description is" in finding.message for finding in findings)
