"""Validate the generated skill corpus against the catalogue source."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for _path in (ROOT, ROOT / "src"):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from agentskills.validation import format_findings, validate_repository


def main() -> int:
    findings = validate_repository(ROOT)
    print(format_findings(findings))
    errors = [finding for finding in findings if finding.severity == "error"]
    if errors:
        print(f"\n{len(errors)} error(s) found.")
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
