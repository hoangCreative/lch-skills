#!/usr/bin/env python3
"""
Validate culture-packs against the mechanical items of the pack rubric.

Checks every packs/<name>/PACK.md (the _template folder is skipped) for:
  1. required frontmatter fields
  2. required section headings
  3. at least one resolvable-looking source URL and one [Cn] citation marker
  4. no em-dash (U+2014) in non-English packs
  5. an examples.md beside PACK.md

Exit code 0 if all packs pass, 1 otherwise. No third-party dependencies.
Run locally:  python3 scripts/validate_packs.py
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PACKS_DIR = os.path.join(ROOT, "packs")

REQUIRED_FIELDS = [
    "pack", "name", "for_engine", "engine_version", "language",
    "status", "author", "license", "version", "created", "provenance",
]

# Each entry: a human label and a regex that must match somewhere in the body.
REQUIRED_SECTIONS = [
    ("terminus map additions", r"terminus map addition"),
    ("speech-act repertoire", r"speech-act repertoire"),
    ("parser signals", r"parser signal"),
    ("provenance", r"provenance"),
    ("citations", r"citation"),
]

EM_DASH = chr(0x2014)
URL_RE = re.compile(r"https?://[^\s)>\]]+")
CITE_MARKER_RE = re.compile(r"\[C\d+\]")


def parse_frontmatter(text):
    """Return dict of top-level frontmatter keys, or None if no frontmatter."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    fields = {}
    for line in block.splitlines():
        m = re.match(r"^([a-zA-Z_][\w]*):\s*(.*)$", line)
        if m:
            fields[m.group(1)] = m.group(2).strip()
    return fields


def validate_pack(pack_dir):
    """Return a list of error strings for one pack folder (empty == pass)."""
    errors = []
    pack_md = os.path.join(pack_dir, "PACK.md")
    name = os.path.basename(pack_dir)

    if not os.path.isfile(pack_md):
        return [f"{name}: missing PACK.md"]

    with open(pack_md, encoding="utf-8") as f:
        text = f.read()

    fm = parse_frontmatter(text)
    if fm is None:
        errors.append(f"{name}: PACK.md has no parseable frontmatter block")
        fm = {}

    for field in REQUIRED_FIELDS:
        if field not in fm or not fm[field]:
            errors.append(f"{name}: frontmatter missing required field '{field}'")

    body = text.lower()
    for label, pattern in REQUIRED_SECTIONS:
        if not re.search(pattern, body, re.IGNORECASE):
            errors.append(f"{name}: missing required section '{label}'")

    if not URL_RE.search(text):
        errors.append(f"{name}: no source URL found (citations required)")
    if not CITE_MARKER_RE.search(text):
        errors.append(f"{name}: no [Cn] citation markers found in body")

    lang = fm.get("language", "").strip().lower()
    if lang and lang != "en" and EM_DASH in text:
        errors.append(
            f"{name}: em-dash (U+2014) found in non-English pack; "
            "use comma, colon, or sentence break"
        )

    if not os.path.isfile(os.path.join(pack_dir, "examples.md")):
        errors.append(f"{name}: missing examples.md")

    return errors


def main():
    if not os.path.isdir(PACKS_DIR):
        print(f"No packs/ directory at {PACKS_DIR}")
        return 1

    pack_dirs = sorted(
        os.path.join(PACKS_DIR, d)
        for d in os.listdir(PACKS_DIR)
        if os.path.isdir(os.path.join(PACKS_DIR, d)) and not d.startswith("_")
    )

    if not pack_dirs:
        print("No packs to validate (only the template is present). OK.")
        return 0

    all_errors = []
    for pack_dir in pack_dirs:
        errs = validate_pack(pack_dir)
        if errs:
            all_errors.extend(errs)
        else:
            print(f"OK: {os.path.basename(pack_dir)}")

    if all_errors:
        print("\nPACK VALIDATION FAILED:")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    print(f"\nAll {len(pack_dirs)} pack(s) passed mechanical validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
