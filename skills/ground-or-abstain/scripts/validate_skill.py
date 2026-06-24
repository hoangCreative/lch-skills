#!/usr/bin/env python3
"""Validate the ground-or-abstain skill package.

Mechanical guardrails that CI enforces so the author does not have to:
  1. No em-dash (U+2014) in any text file.
  2. SKILL.md frontmatter has name and description.
  3. version matches across SKILL.md, CITATION.cff, and the top CHANGELOG entry.
  4. Every bad-* fixture carries leak_class, pass_if, fail_if.
  5. Required files are present.

Usage: python scripts/validate_skill.py [skill_dir]
Default skill_dir is the parent of this script's directory.
Exit code 0 = pass, 1 = fail.
"""
import json
import os
import re
import sys

EMDASH = chr(0x2014)
REQUIRED = ["SKILL.md", "README.md", "METHODOLOGY.md", "CHANGELOG.md",
            "CITATION.cff", "LICENSE", "CONTRIBUTING.md", "HARNESS.md"]


def fail(errors, msg):
    errors.append(msg)


def find_version(text):
    m = re.search(r'(?<!-)version:\s*"?([0-9]+\.[0-9]+\.[0-9]+)"?', text)
    return m.group(1) if m else None


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    skill = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(here)
    errors = []

    for f in REQUIRED:
        if not os.path.isfile(os.path.join(skill, f)):
            fail(errors, f"missing required file: {f}")

    for root, _dirs, files in os.walk(skill):
        if ".git" in root:
            continue
        for fn in files:
            if fn.rsplit(".", 1)[-1] in ("md", "cff", "json", "yml", "yaml", "txt"):
                p = os.path.join(root, fn)
                try:
                    with open(p, encoding="utf-8") as fh:
                        if EMDASH in fh.read():
                            fail(errors, f"em-dash found in {os.path.relpath(p, skill)}")
                except (OSError, UnicodeDecodeError):
                    pass

    skill_md = os.path.join(skill, "SKILL.md")
    v_skill = None
    if os.path.isfile(skill_md):
        text = open(skill_md, encoding="utf-8").read()
        if not re.search(r'^\s*name:\s*\S+', text, re.M):
            fail(errors, "SKILL.md frontmatter missing name")
        if not re.search(r'description:\s*', text):
            fail(errors, "SKILL.md frontmatter missing description")
        v_skill = find_version(text)

    cit = os.path.join(skill, "CITATION.cff")
    if os.path.isfile(cit):
        v_cit = find_version(open(cit, encoding="utf-8").read())
        if v_skill and v_cit and v_skill != v_cit:
            fail(errors, f"version mismatch: SKILL.md {v_skill} vs CITATION.cff {v_cit}")

    chlog = os.path.join(skill, "CHANGELOG.md")
    if os.path.isfile(chlog):
        m = re.search(r'\[([0-9]+\.[0-9]+\.[0-9]+)\]', open(chlog, encoding="utf-8").read())
        if v_skill and m and m.group(1) != v_skill:
            fail(errors, f"version mismatch: SKILL.md {v_skill} vs top CHANGELOG {m.group(1)}")

    fxdir = os.path.join(skill, "tests", "fixtures")
    if os.path.isdir(fxdir):
        for fn in os.listdir(fxdir):
            if fn.startswith("bad-") and fn.endswith(".json"):
                data = json.load(open(os.path.join(fxdir, fn), encoding="utf-8"))
                for key in ("leak_class", "pass_if", "fail_if"):
                    if key not in data:
                        fail(errors, f"fixture {fn} missing {key}")

    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print("  - " + e)
        return 1
    print("validation OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
