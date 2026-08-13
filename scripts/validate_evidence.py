#!/usr/bin/env python3
"""Deterministic clerical validation for the controlled evidence system."""

from __future__ import annotations

import csv
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EUID_RE = re.compile(r"^[A-Z0-9]+-(?:[0-9]{8}|GEN)-[0-9]{4}[A-Z]?$")
PRINTED_PAGE_RE = re.compile(r"\bPrinted\s+p(?:age)?\.?\s*\d+", re.IGNORECASE)
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r"\bhref=[\"']([^\"']+)[\"']", re.IGNORECASE)


def read_csv(relative: str) -> list[dict[str, str]]:
    with (ROOT / relative).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def main() -> int:
    errors: list[str] = []
    fail = errors.append
    manifest = read_csv("sources/manifest/source-manifest.csv")
    registry = read_csv("sources/manifest/source-registry.csv")
    units = read_csv("evidence/atomic-units/euid-ledger.csv")
    history = read_csv("evidence/atomic-units/assignment-history.csv")
    deprecations = read_csv("evidence/atomic-units/deprecations.csv")
    comparisons = read_csv("evidence/narrative-comparison/comparison-corpus.csv")

    source_ids = {r["source_id"] for r in manifest}
    registry_ids = {r["source_id"] for r in registry}
    if len(source_ids) != len(manifest): fail("duplicate source_id in manifest")
    if len(registry_ids) != len(registry): fail("duplicate source_id in registry")
    if source_ids != registry_ids: fail("manifest and registry source IDs differ")
    if len(manifest) != 47: fail(f"expected 47 sources, found {len(manifest)}")

    euids: set[str] = set()
    euid_sources: dict[str, str] = {}
    for row in units:
        euid = row["euid"]
        if not EUID_RE.fullmatch(euid): fail(f"invalid EUID: {euid}")
        if euid in euids: fail(f"duplicate EUID: {euid}")
        euids.add(euid)
        euid_sources[euid] = row["source_id"]
        if row["source_id"] not in source_ids: fail(f"{euid} maps to absent source")
        if row["native_page"] != "UNMAPPED" and not row["native_page"].startswith("VERIFIED:"):
            fail(f"{euid} has invalid native_page")

    deprecated_ids = {r["euid"] for r in deprecations}
    if euids & deprecated_ids: fail("EUID both active and deprecated")
    historical_ids = {r["euid"] for r in history}
    for euid in sorted(historical_ids - euids - deprecated_ids):
        fail(f"assigned EUID disappeared without deprecation: {euid}")
    for row in history:
        if row["euid"] in euids and row["source_id"] != euid_sources[row["euid"]]:
            fail(f"historical source mapping changed: {row['euid']}")

    represented_paths = set()
    for row in manifest:
        path = ROOT / row["representation_path"]
        represented_paths.add(row["representation_path"])
        if not path.exists():
            fail(f"missing representation: {row['representation_path']}")
            continue
        if hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            fail(f"hash changed without manifest rebuild: {row['source_id']}")
        if row["native_page_status"] not in {"UNMAPPED", "VERIFIED"}:
            fail(f"invalid page status: {row['source_id']}")
        for field in ("title", "author", "representation_type", "transcription_status", "redaction_status", "native_status"):
            if not row[field].strip(): fail(f"{row['source_id']} lacks {field}")

    for path in (ROOT / "docs/source-records").iterdir():
        rel = str(path.relative_to(ROOT))
        if path.is_file() and path.name != "README.md" and rel not in represented_paths:
            fail(f"public source lacks manifest row: {rel}")

    for corpus_name in ("evidence-corpus.md", "clinical-corpus.md"):
        text = (ROOT / "sources/consolidated" / corpus_name).read_text(encoding="utf-8")
        corpus_euids = set(re.findall(
            r"^\[([A-Z0-9]+-(?:[0-9]{8}|GEN)-[0-9]{4}[A-Z]?)\]$",
            text,
            re.MULTILINE,
        ))
        for euid in corpus_euids - euids: fail(f"{corpus_name} has absent EUID {euid}")
        if corpus_name == "evidence-corpus.md" and corpus_euids != euids:
            fail("complete evidence corpus and ledger differ")

    for row in comparisons:
        for field in ("earlier_euid", "later_euid"):
            if row[field] not in euids: fail(f"{row['comparison_id']} unresolved {field}")
        if not (ROOT / row["analysis_path"]).exists(): fail(f"missing comparison analysis: {row['analysis_path']}")

    change_log = read_csv("sources/normalized/change-log.csv")
    logged = {r["source_id"] for r in change_log}
    for path in (ROOT / "sources/normalized").iterdir():
        if path.is_file() and path.name not in {"README.md", "change-log.csv"}:
            if path.name.split("-", 1)[0] not in logged: fail(f"normalized file lacks change log: {path.name}")

    status = (ROOT / "evidence/ANALYTICAL_DOCUMENT_STATUS_REGISTER.md").read_text(encoding="utf-8")
    for path in (ROOT / "analysis").rglob("*.md"):
        if path.name == "README.md": continue
        rel = str(path.relative_to(ROOT))
        text = path.read_text(encoding="utf-8")
        if "**Status:**" not in text: fail(f"analysis lacks status: {rel}")
        if f"`{rel}`" not in status: fail(f"analysis absent from status register: {rel}")

    matrix = (ROOT / "evidence/SOURCE_PROPOSITION_MATRIX.md").read_text(encoding="utf-8")
    for line in matrix.splitlines():
        if re.match(r"^\| P\d+ \|", line):
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 6 or not cells[3]: fail(f"proposition lacks contrary material: {cells[0]}")

    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "archive" in path.parts: continue
        if path.suffix.lower() not in {".md", ".html", ".txt", ".csv"}: continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if PRINTED_PAGE_RE.search(text): fail(f"unverified Printed-page locator: {path.relative_to(ROOT)}")
        relative = str(path.relative_to(ROOT))
        link_targets: list[str] = []
        if path.suffix.lower() == ".md" and "sources/consolidated" not in relative:
            link_targets.extend(MARKDOWN_LINK_RE.findall(text))
        if path.suffix.lower() == ".html":
            link_targets.extend(HTML_LINK_RE.findall(text))
        for raw_target in link_targets:
                target = raw_target.strip().split()[0].strip("<>")
                if target.startswith(("http://", "https://", "mailto:", "tel:", "#")): continue
                target_path = target.split("#", 1)[0]
                candidates = ((path.parent / target_path).resolve(), (ROOT / target_path).resolve())
                if target_path and not any(candidate.exists() for candidate in candidates):
                    fail(f"broken local link in {path.relative_to(ROOT)}: {target}")

    report = (ROOT / "analysis/supporting/RESTORED_FOOT_PROTEST_DEPENDENCY_AUDIT_2026-08-13.md").read_text(encoding="utf-8")
    required = [
        "stipulated fact for this audit",
        "not yet independently corroborated by a native institutional record or witness statement",
        "Liam did not mention levodopa during the protest",
        "Repetition within the Patient Statement Log or later analysis is not counted as independent corroboration",
        "no further examination or resolution is visible in the presently available record",
        "Qualitative dependency heuristic (non-statistical)",
        "## 7. Dependency matrix",
        "## 11. Source genealogy and institutional reliance",
        "## 14. Falsification",
        "### J. Decisive further evidence",
    ]
    report_folded = report.casefold()
    for phrase in required:
        if phrase.casefold() not in report_folded: fail(f"audit lost required calibration: {phrase}")
    if re.search(r"\b\d+\s*[–-]\s*\d+%", report): fail("audit still presents numerical ranges")

    if errors:
        for error in errors: print(f"ERROR: {error}")
        return 1
    print(f"OK: {len(source_ids)} sources; {len(euids)} EUIDs; {len(comparisons)} comparisons; hashes, links, statuses and controls passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
