#!/usr/bin/env python3
"""Build controlled derived corpora from immutable public representations."""

from __future__ import annotations

import csv
import hashlib
import html
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "sources/manifest/source-registry.csv"
TAG_RE = re.compile(r"<[^>]+>")
CAPTURE_RE = re.compile(
    r'<(?:div\s+class="clinical"|pre(?:\s+class="[^"]*")?)[^>]*>(.*?)</(?:div|pre)>',
    re.IGNORECASE | re.DOTALL,
)
DATE_RE = re.compile(r"(20\d{2})[-/](\d{2})[-/](\d{2})")
MEDICATIONS = re.compile(
    r"\b(?:Sinemet|Stalevo|levodopa|Procyclid(?:ine|ne)|Procylidine|Kemadrin|Azilect|"
    r"rasagiline|Lyrica|pregabalin|Rivotril|clonazepam|Anxicalm|diazepam|gabapentin|"
    r"Neurontin|Comtess|entacapone|thiamine|amitriptyline)\b",
    re.IGNORECASE,
)


@dataclass
class Unit:
    euid: str
    source_id: str
    source_date: str
    author: str
    speaker: str
    kind: str
    temporal_status: str
    native_page: str
    repo_lines: str
    transcription_status: str
    certainty: str
    redaction: str
    supersedes: str
    notes: str
    text: str
    record_class: str
    corpus_scope: str


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def git_blob(path: Path) -> str:
    return subprocess.check_output(
        ["git", "hash-object", str(path.relative_to(ROOT))], cwd=ROOT, text=True
    ).strip()


def plain(raw: str) -> str:
    return html.unescape(TAG_RE.sub("", raw)).rstrip()


def date_token(text: str, fallback: str) -> tuple[str, str]:
    match = DATE_RE.search(text)
    if match:
        value = "-".join(match.groups())
        return value, "".join(match.groups())
    if fallback != "UNMAPPED":
        return fallback, fallback.replace("-", "")
    return "UNMAPPED", "GEN"


def classify(text: str) -> str:
    stripped = text.strip()
    lower = stripped.lower()
    if set(stripped) <= {"-", "=", "_", "."}:
        return "divider"
    if lower.endswith(":") or lower in {
        "impression", "recommendations", "current rx", "follow-up", "our questions"
    }:
        return "heading"
    if MEDICATIONS.search(text):
        return "medication_statement"
    if any(token in lower for token in ("plan", "recommend", "refer", "follow-up", "start ")):
        return "plan"
    if any(token in lower for token in ("think", "suspect", "likely", "impression", "not clear")):
        return "opinion"
    if "“" in text or '"' in text or "&#x27;" in text:
        return "quotation_or_report"
    return "statement"


def speaker(text: str, default: str) -> str:
    lower = text.lower()
    if "[patient]" in lower or "patient explains" in lower or "patient states" in lower:
        return "patient_via_recording_actor"
    if "[gp]" in lower:
        return "GP_or_GP_addressee"
    return default


def certainty(text: str) -> str:
    lower = text.lower()
    if "illegible" in lower:
        return "illegible"
    if "unclear" in lower or "[?" in lower:
        return "unclear"
    if "???" in text:
        return "unclear"
    return "certain_as_transcribed"


def extract_html(entry: dict[str, str], path: Path) -> list[Unit]:
    source = path.read_text(encoding="utf-8", errors="replace")
    matches = list(CAPTURE_RE.finditer(source))
    if not matches:
        raise ValueError(f"no evidential text container found in {path.relative_to(ROOT)}")
    units: list[Unit] = []
    for match in matches:
        start_line = source.count("\n", 0, match.start(1)) + 1
        raw_lines = match.group(1).splitlines()
        preview = "\n".join(plain(line) for line in raw_lines[:5])
        section_date, token = date_token(preview, entry["source_date"])
        for offset, raw in enumerate(raw_lines):
            text = plain(raw)
            if not text.strip():
                continue
            line_number = start_line + offset
            euid = f'{entry["source_id"]}-{token}-{line_number:04d}'
            units.append(make_unit(entry, section_date, euid, line_number, text))
    return units


def extract_markdown(entry: dict[str, str], path: Path) -> list[Unit]:
    units: list[Unit] = []
    section_date, token = date_token("", entry["source_date"])
    for line_number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip():
            continue
        euid = f'{entry["source_id"]}-{token}-{line_number:04d}'
        units.append(make_unit(entry, section_date, euid, line_number, raw.rstrip()))
    return units


def make_unit(
    entry: dict[str, str], source_date: str, euid: str, line_number: int, text: str
) -> Unit:
    redaction = "meaning_may_be_affected" if "[redacted]" in text.lower() else (
        "identifiers_redacted" if "[" in text and "]" in text else "none_visible"
    )
    return Unit(
        euid=euid,
        source_id=entry["source_id"],
        source_date=source_date,
        author=entry["author"],
        speaker=speaker(text, entry["speaker_default"]),
        kind=classify(text),
        temporal_status="within_record_not_independently_classified",
        native_page="UNMAPPED",
        repo_lines=f'{entry["representation_path"]}:{line_number}',
        transcription_status=entry["transcription_status"],
        certainty=certainty(text),
        redaction=redaction,
        supersedes="",
        notes="Clerical only.",
        text=text,
        record_class=entry["record_class"],
        corpus_scope=entry["corpus_scope"],
    )


def write_csv(path: Path, fieldnames: list[str], data: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(data)


def main() -> None:
    registry = rows(REGISTRY)
    units: list[Unit] = []
    manifest: list[dict[str, str]] = []
    assigned_euids: set[str] = set()
    for registry_order, entry in enumerate(registry, 1):
        path = ROOT / entry["representation_path"]
        content = path.read_bytes()
        manifest.append(
            {
                "source_id": entry["source_id"],
                "title": entry["title"],
                "source_date": entry["source_date"],
                "author": entry["author"],
                "native_status": entry["native_status"],
                "representation_path": entry["representation_path"],
                "representation_type": entry["representation_type"],
                "transcription_status": entry["transcription_status"],
                "redaction_status": entry["redaction_status"],
                "native_page_status": entry["native_page_status"],
                "sha256": hashlib.sha256(content).hexdigest(),
                "git_blob": git_blob(path),
                "record_class": entry["record_class"],
                "corpus_scope": entry["corpus_scope"],
                "registry_order": str(registry_order),
                "controlling_note": "Repository representation is derived; best available native exhibit controls.",
            }
        )
        extracted = extract_html(entry, path) if path.suffix == ".html" else extract_markdown(entry, path)
        for unit in extracted:
            # Overlapping evidential containers can begin on the same physical
            # line. Preserve the physical-line stem and add a stable insertion
            # suffix instead of renumbering any later unit.
            candidate = unit.euid
            suffix = 0
            while candidate in assigned_euids:
                suffix += 1
                candidate = f"{unit.euid}{chr(64 + suffix)}"
            unit.euid = candidate
            assigned_euids.add(candidate)
        units.extend(extracted)

    manifest_fields = list(manifest[0])
    write_csv(ROOT / "sources/manifest/source-manifest.csv", manifest_fields, manifest)

    ledger_fields = [
        "euid", "source_id", "source_date", "author", "speaker", "type",
        "temporal_status", "native_page", "repo_lines", "transcription_status",
        "certainty", "redaction", "supersedes", "notes",
    ]
    ledger = [
        {
            "euid": u.euid, "source_id": u.source_id, "source_date": u.source_date,
            "author": u.author, "speaker": u.speaker, "type": u.kind,
            "temporal_status": u.temporal_status, "native_page": u.native_page,
            "repo_lines": u.repo_lines, "transcription_status": u.transcription_status,
            "certainty": u.certainty, "redaction": u.redaction,
            "supersedes": u.supersedes, "notes": u.notes,
        }
        for u in units
    ]
    write_csv(ROOT / "evidence/atomic-units/euid-ledger.csv", ledger_fields, ledger)

    history_path = ROOT / "evidence/atomic-units/assignment-history.csv"
    prior_history = rows(history_path) if history_path.exists() else []
    historical = {row["euid"]: row for row in prior_history}
    for unit in units:
        historical.setdefault(
            unit.euid,
            {
                "euid": unit.euid,
                "source_id": unit.source_id,
                "first_assignment_baseline": "576100898c26d65b2827cbbc401a277151a9acf9+uncommitted-corpus-build",
                "status": "ACTIVE",
            },
        )
    write_csv(
        history_path,
        ["euid", "source_id", "first_assignment_baseline", "status"],
        [historical[key] for key in sorted(historical)],
    )

    def ordered(selected: list[Unit]) -> list[Unit]:
        return sorted(selected, key=lambda u: (u.source_date == "UNMAPPED", u.source_date, u.source_id, int(u.repo_lines.rsplit(":", 1)[1])))

    def corpus(title: str, selected: list[Unit], output: Path) -> None:
        header = [
        f"# {title}",
        "",
        "**Status:** DERIVED — originals and public source representations remain controlling",
        "**Generated:** 13 August 2026",
        "**Generation method:** `scripts/build_evidence_corpus.py`",
        "**Normalization:** HTML markup removed, entities decoded and terminal whitespace removed for display; spelling, syntax, punctuation, OCR damage and redaction tokens otherwise preserved. No silent clinical correction.",
        "**Ordering:** dated records first by recorded date; records or sections without an independently mapped date follow as `UNMAPPED`, ordered by stable Source ID and repository line.",
        "**Inputs and hashes:** `sources/manifest/source-manifest.csv`",
        "**Controlling rule:** this corpus never replaces the native exhibit or its public repository representation.",
        "",
        ]
        body: list[str] = header
        current = None
        for unit in ordered(selected):
            if unit.source_id != current:
                current = unit.source_id
                item = next(row for row in registry if row["source_id"] == current)
                body.extend([f'## {current} — {item["title"]}', ""])
            body.extend([f'[{unit.euid}]', unit.text, ""])
        output.write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")

    clinical = [u for u in units if u.corpus_scope == "clinical"]
    corpus("Clinical corpus — complete controlled derivation", clinical, ROOT / "sources/consolidated/clinical-corpus.md")
    corpus("Evidence corpus — 47-source controlled derivation", units, ROOT / "sources/consolidated/evidence-corpus.md")

    med_rows = []
    for unit in clinical:
        if not MEDICATIONS.search(unit.text):
            continue
        lower = unit.text.lower()
        action = "response_or_context"
        for needle, label in (
            ("start", "commencement"), ("commenc", "commencement"),
            ("stop", "cessation"), ("off ", "cessation_or_off_state"),
            ("increase", "dose_increase"), ("reduce", "dose_reduction"),
            ("decreas", "dose_reduction"), ("adverse", "adverse_effect"),
            ("dyskines", "adverse_effect_or_constraint"), ("relief", "response"),
            ("improv", "response"),
        ):
            if needle in lower:
                action = label
                break
        med_rows.append(
            {
                "event_id": f"MED-{unit.euid}", "event_date": unit.source_date,
                "medication_text": unit.text, "action": action,
                "stated_response_adverse_effect_or_rationale": unit.text,
                "euid": unit.euid, "source_id": unit.source_id,
                "native_page": "UNMAPPED", "review_status": "CLERICAL_EXTRACTION_REQUIRES_MANUAL_VERIFICATION",
            }
        )
    write_csv(
        ROOT / "evidence/chronology/medication-chronology.csv",
        ["event_id", "event_date", "medication_text", "action", "stated_response_adverse_effect_or_rationale", "euid", "source_id", "native_page", "review_status"],
        med_rows,
    )

    knowledge_rows = []
    for entry in sorted((r for r in registry if r["corpus_scope"] == "knowledge"), key=lambda r: (r["source_date"], r["source_id"])):
        source_units = [u for u in units if u.source_id == entry["source_id"]]
        knowledge_rows.append(
            {
                "event_id": f'KNOW-{entry["source_id"]}', "event_date": entry["source_date"],
                "actor": entry["author"], "recorded_or_received": entry["title"],
                "first_euid": source_units[0].euid, "last_euid": source_units[-1].euid,
                "source_id": entry["source_id"], "certainty": "source_event_established_representation_scope_only",
                "notes": "Does not infer personal reading, subjective knowledge, agreement, or legal effect beyond the source wording.",
            }
        )
    write_csv(
        ROOT / "evidence/chronology/knowledge-chronology.csv",
        ["event_id", "event_date", "actor", "recorded_or_received", "first_euid", "last_euid", "source_id", "certainty", "notes"],
        knowledge_rows,
    )
    print(f"built {len(manifest)} sources, {len(units)} EUIDs, {len(clinical)} clinical units, {len(med_rows)} medication rows")


if __name__ == "__main__":
    main()
