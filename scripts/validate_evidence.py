#!/usr/bin/env python3
"""Deterministic clerical checks for the controlled evidence layer."""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EUID_RE = re.compile(r"^[A-Z0-9]+-(?:[0-9]{8}|GEN)-[0-9]{4}[A-Z]?$")
PRINTED_PAGE_RE = re.compile(r"\bPrinted\s+p(?:age)?\.?\s*\d+", re.IGNORECASE)


def read_csv(relative: str) -> list[dict[str, str]]:
    path = ROOT / relative
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    manifest = read_csv("sources/manifest/source-manifest.csv")
    units = read_csv("evidence/atomic-units/euid-ledger.csv")
    deprecations = read_csv("evidence/atomic-units/deprecations.csv")

    source_ids = {row["source_id"] for row in manifest}
    if len(source_ids) != len(manifest):
        fail("duplicate source_id in machine-readable manifest", errors)

    euids: set[str] = set()
    for row in units:
        euid = row["euid"]
        if not EUID_RE.fullmatch(euid):
            fail(f"invalid EUID syntax: {euid}", errors)
        if euid in euids:
            fail(f"duplicate EUID: {euid}", errors)
        euids.add(euid)
        if row["source_id"] not in source_ids:
            fail(f"EUID {euid} maps to absent source {row['source_id']}", errors)
        if row["native_page"] != "UNMAPPED" and not row["native_page"].startswith("VERIFIED:"):
            fail(f"EUID {euid} has unsupported native_page value", errors)

    deprecated_ids = {row["euid"] for row in deprecations}
    if euids & deprecated_ids:
        fail("an EUID is both active and deprecated", errors)

    for row in manifest:
        representation = ROOT / row["representation_path"]
        if not representation.exists():
            fail(f"manifest representation does not exist: {row['representation_path']}", errors)
        if row["native_page_status"] not in {"UNMAPPED", "VERIFIED"}:
            fail(f"unsupported native_page_status for {row['source_id']}", errors)

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "archive" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".html", ".txt", ".csv"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if PRINTED_PAGE_RE.search(text):
            fail(f"unverified Printed-page locator in {path.relative_to(ROOT)}", errors)

    corpus = (ROOT / "sources/consolidated/clinical-corpus-pilot.md").read_text(encoding="utf-8")
    for euid in re.findall(r"\[([A-Z0-9]+-(?:[0-9]{8}|GEN)-[0-9]{4}[A-Z]?)\]", corpus):
        if euid not in euids:
            fail(f"consolidated corpus references absent EUID {euid}", errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: {len(source_ids)} sources; {len(euids)} active EUIDs; clerical controls passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
