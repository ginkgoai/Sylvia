"""Append-only, evidence-aware memory ledger for Sexta-feira."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(r"C:\sexta-feira")
LEDGER = ROOT / "ginkgo-vault" / "00_Cerebro" / "LEDGER.jsonl"
MAX_TITLE = 180
MAX_CONTENT = 4_000
ALLOWED_KINDS = {"observation", "learning_candidate", "confirmed_learning"}


def normalized(value: str, limit: int, field: str) -> str:
    cleaned = " ".join(value.strip().split())
    if not cleaned:
        raise ValueError(f"{field}_required")
    if len(cleaned) > limit:
        raise ValueError(f"{field}_too_long")
    return cleaned


def contains_sensitive_value(value: str) -> bool:
    lowered = value.lower()
    markers = ("authorization: bearer", "api_key=", "api key=", "password=", "senha=", "secret=", "token=", "sk-", "ghp_")
    return any(marker in lowered for marker in markers)


def append_entry(kind: str, title: str, content: str, source: str, confidence: str, scope: str) -> dict[str, str]:
    if kind not in ALLOWED_KINDS:
        raise ValueError("invalid_kind")
    if scope not in {"personal", "corporate"}:
        raise ValueError("invalid_scope")
    if contains_sensitive_value(title) or contains_sensitive_value(content) or contains_sensitive_value(source):
        raise ValueError("sensitive_value_detected")
    entry = {
        "at": datetime.now(timezone.utc).isoformat(),
        "kind": kind,
        "title": normalized(title, MAX_TITLE, "title"),
        "content": normalized(content, MAX_CONTENT, "content"),
        "source": normalized(source, 300, "source"),
        "confidence": confidence,
        "scope": scope,
    }
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    with LEDGER.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=True) + "\n")
    return entry


def main() -> int:
    parser = argparse.ArgumentParser(description="Persist a Sexta-feira memory entry")
    parser.add_argument("kind", choices=sorted(ALLOWED_KINDS))
    parser.add_argument("--title", required=True)
    parser.add_argument("--content", required=True)
    parser.add_argument("--source", required=True)
    parser.add_argument("--confidence", choices=["low", "medium", "high"], default="medium")
    parser.add_argument("--scope", choices=["personal", "corporate"], default="corporate")
    args = parser.parse_args()
    try:
        entry = append_entry(args.kind, args.title, args.content, args.source, args.confidence, args.scope)
    except ValueError as error:
        print(json.dumps({"ok": False, "error": str(error)}))
        return 2
    print(json.dumps({"ok": True, "entry": entry}, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
