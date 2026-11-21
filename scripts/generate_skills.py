"""Write the generated skill files and domain routers."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for _path in (ROOT, ROOT / "src"):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from agentskills import __version__
from agentskills.generation import generate
from catalog.source import domain_of
from catalog.source._domains import DOMAIN_PROFILES


def main() -> int:
    written = generate(ROOT, __version__, domain_of(), DOMAIN_PROFILES)
    print(f"wrote {len(written)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
