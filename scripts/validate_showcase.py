"""Validate the public Knowledge Core showcase without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_EXTENSIONS = {".md", ".json", ".py", ".yml", ".yaml", ".cff", ".svg", ".txt"}
FORBIDDEN_PATH_PARTS = {
    ".env",
    ".git",
    "memory",
    "conversations",
    "runtime",
    "weights",
    "adapters",
    "holdout_data",
}
FORBIDDEN_PATTERNS = {
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github_token": re.compile(r"\bgh[opsu]_[A-Za-z0-9]{20,}\b"),
    "openai_key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "absolute_windows_user_path": re.compile(r"\b[A-Za-z]:\\Users\\[^\\\s]+\\"),
    "bearer_token": re.compile(r"\bBearer\s+[A-Za-z0-9._~-]{20,}\b", re.I),
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    files = [path for path in ROOT.rglob("*") if path.is_file()]
    if not files:
        fail("showcase is empty")

    for path in files:
        relative = path.relative_to(ROOT)
        lowered = {part.lower() for part in relative.parts}
        if lowered & FORBIDDEN_PATH_PARTS:
            fail(f"forbidden path: {relative}")
        if path.suffix.lower() not in TEXT_EXTENSIONS:
            continue
        text = path.read_text(encoding="utf-8")
        if path.suffix.lower() == ".json":
            json.loads(text)
        for name, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                fail(f"{name} found in {relative}")

    required = {
        Path("README.md"),
        Path("SECURITY.md"),
        Path("docs/architecture.md"),
        Path("docs/evidence.md"),
        Path("docs/governance.md"),
        Path("examples/evaluation_contract.json"),
    }
    missing = sorted(str(path) for path in required if not (ROOT / path).is_file())
    if missing:
        fail(f"missing required files: {missing}")

    print(f"OK: {len(files)} public files validated")


if __name__ == "__main__":
    main()
