# tests/test_cli.py
import json

from agentskills.cli import main


def test_list_outputs_json(capsys: object) -> None:
    code = main(["list", "--json"])
    assert code == 0
    payload = json.loads(capsys.readouterr().out)  # type: ignore[attr-defined]
    assert isinstance(payload, list)


def test_route_returns_matches(capsys: object) -> None:
    code = main(["route", "migrate a database to postgres", "--top", "3", "--json"])
    assert code == 0
    payload = json.loads(capsys.readouterr().out)  # type: ignore[attr-defined]
    assert "results" in payload


def test_show_unknown_skill_returns_one(capsys: object) -> None:
    code = main(["show", "definitely-not-a-real-skill-name"])
    assert code == 1


def test_validate_reports_findings(capsys: object) -> None:
    code = main(["validate", "--json"])
    assert code in {0, 1}
    payload = json.loads(capsys.readouterr().out)  # type: ignore[attr-defined]
    assert isinstance(payload, list)
