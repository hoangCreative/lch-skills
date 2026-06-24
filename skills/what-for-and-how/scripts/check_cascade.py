#!/usr/bin/env python3
"""
check_cascade.py - a mechanical output-checker for the what-for-and-how engine.

WHY THIS EXISTS
---------------
The engine is a prose skill read by a language model. An adversarial stress-test
(v3.2 -> v3.3) showed that prose guards do not enforce themselves: the engine
performs the ritual and self-reports compliance while still breaking the rule.
This is the engine's own honesty-note prediction, confirmed twice. The only thing
that actually catches the cheat is CODE that reads the engine's structured output
and checks it mechanically. This script is that code. It does not trust any
self-reported "anti_default_check: clean" or "banned_tiebreaker_used: none"; it
re-derives the verdict from the fields.

It is a RELEASE/TEST tool, not a runtime shield: it checks engine outputs you have
captured (for example by running the engine over tests/regression-cases.json). It
does not run inside someone else's chat session.

CASCADE-OUTPUT CONTRACT (the JSON the engine should emit; superset of Format B)
------------------------------------------------------------------------------
{
  "input": str,
  "pack": str,                       # e.g. "none" or "vietnamese"
  "no_pack": bool,                   # true when running defaults / lowered confidence
  "permissibility": "ok" | "propriety-limit",
  "shape": str,
  "mode": str,
  "cascade": [ {"layer": str, "text": str, "proposal": bool}, ... ],
  "l6_falsify": "held" | "not-landed" | "carve-out",   # REQUIRED discrete field
  "terminus": {
    "kind": "single"|"held_conjunctive"|"held_disjunctive"|"ask"|"clinical_handoff"|"propriety_limit",
    "blocked_resolution": "permissibility-blocked"|"no-turn"|"container-premature"|null,
    "resolves_when": str,
    "floors": [ {"type": str, "anchor": str, "grounding": "low"|"medium"|"high",
                 "evidence": str, "l6_survived": bool, "proposal": bool}, ... ]
  },
  "selection_audit": { "candidates": [...], "anti_default_check": str, "banned_tiebreaker_used": str },
  "phase2": str
}

CHECKS
------
Hard FAIL (exit 1):
  C1  brake fired then cascade leaked: permissibility == propriety-limit, or
      terminus.kind in {propriety_limit, clinical_handoff}, MUST have no scored
      floors and no selection_audit.
  C2  ask-evasion: a held_conjunctive (or single) terminus whose resolves_when text
      describes selecting ONE winner is really disjunctive and must be an ASK;
      a held_disjunctive MUST carry a blocked_resolution from the closed list.
  C3  resurrection: a floor with l6_survived == false seated as a held member.
  C4  no-pack grounding cap: no_pack true and any floor grounding == high.
  C5  L6 discipline: l6_falsify field missing, OR L6 content asserted inside a
      floor.evidence string instead of the discrete line.
Advisory WARN (does not fail the build):
  C6  speaker gender/role fabricated (heuristic token scan).
  C7  banned_tiebreaker_used is a bare "none" with two or more candidates.
  C8  a terminus floor type that looks coined/fused and is not in the co-equal map.

Usage:
  python3 scripts/check_cascade.py OUTPUT.json [MORE.json ...]
  python3 scripts/check_cascade.py --dir path/to/outputs
  python3 scripts/check_cascade.py --selftest      # runs tests/fixtures, used by CI
"""

import json
import os
import re
import sys

ALLOWED_KINDS = {
    "single", "held_conjunctive", "held_disjunctive", "ask",
    "clinical_handoff", "propriety_limit",
}
HELD_KINDS = {"held_conjunctive", "held_disjunctive"}
BRAKE_KINDS = {"clinical_handoff", "propriety_limit"}
BLOCKED_RESOLUTION = {"permissibility-blocked", "no-turn", "container-premature"}

# co-equal terminus map types (pack-added types are allowed, so unknown -> WARN only)
MAP_TYPES = {
    "measurable_need", "open_longing", "relational_role", "honor",
    "collective", "phatic", "proverbial", "brute_structural", "agent_intention",
    "clinical_handoff", "propriety_limit",
}

# resolves_when phrasings that betray a one-winner (disjunctive) resolution
DISJUNCTIVE_SIGNALS = [
    r"\bwhich (one|of)\b", r"\bwhether\b", r"\beither\b[^.]{0,40}\bor\b",
    r"\bif it turns out\b", r"\bturns out to be\b", r"\bwould resolve\b",
    r"\bselect(s|ed)? (a |one |the )?(single |winner)", r"\bsubstitution test\b",
    r"\bmostly [A-Za-z ]+ or mostly\b", r"\bone of (them|these|A or B)\b",
    r"\bask(ing)? (her|him|them|the user)?[^.]{0,30}\bwhich\b",
    r"\bpick(s|ed)? (the|one)\b", r"\bresolves to (a |one )?single\b",
]
# L6 content leaking into floor evidence (should be the discrete l6_falsify line)
L6_IN_EVIDENCE = [
    r"\bL6\b", r"one more why", r"one further why", r"drill(ed)? one more",
    r"\bfalsif", r"one additional why",
]
# heuristic speaker-gender fabrication tokens (advisory)
GENDER_TOKENS = [
    r"\beldest son\b", r"\beldest daughter\b", r"\bfirstborn son\b",
    r"\bas a son\b", r"\bas a daughter\b", r"\bas the son\b", r"\bas the daughter\b",
]


def _txt(*parts):
    return " ".join(str(p) for p in parts if p).lower()


def _matches(patterns, text):
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def check_output(o):
    """Return a list of (level, code, message). level is 'FAIL' or 'WARN'."""
    issues = []
    term = o.get("terminus") or {}
    kind = term.get("kind")
    floors = term.get("floors") or []
    resolves = term.get("resolves_when") or ""
    sel = o.get("selection_audit") or {}
    perm = (o.get("permissibility") or "").lower()
    no_pack = bool(o.get("no_pack"))

    if kind is not None and kind not in ALLOWED_KINDS:
        issues.append(("WARN", "C0", "terminus.kind %r is not an allowed kind" % kind))

    # C1 brake fired -> no cascade artifacts
    brake_fired = perm in ("propriety-limit", "propriety_limit") or kind in BRAKE_KINDS
    if brake_fired:
        if floors:
            issues.append(("FAIL", "C1",
                "brake fired (permissibility=%s, kind=%s) but %d scored floor(s) emitted; the cascade must not run"
                % (perm or "n/a", kind, len(floors))))
        if sel.get("candidates") or sel.get("anti_default_check") or sel.get("banned_tiebreaker_used"):
            issues.append(("FAIL", "C1",
                "brake fired but a selection_audit was emitted; no excavation is permitted past the gate"))

    # C2 ask-evasion + blocked_resolution contract
    disj_resolution = _matches(DISJUNCTIVE_SIGNALS, resolves)
    if not brake_fired:
        if kind in ("held_conjunctive", "single") and disj_resolution:
            issues.append(("FAIL", "C2",
                "kind=%s but resolves_when describes selecting one winner (disjunctive); this must be an ASK, not a %s label"
                % (kind, kind)))
        if kind == "held_disjunctive":
            br = term.get("blocked_resolution")
            if br not in BLOCKED_RESOLUTION:
                issues.append(("FAIL", "C2",
                    "held_disjunctive requires blocked_resolution in %s; got %r"
                    % (sorted(BLOCKED_RESOLUTION), br)))

    # C3 no resurrection of an L6-failed floor into a held set
    if kind in HELD_KINDS:
        for fl in floors:
            if fl.get("l6_survived") is False:
                issues.append(("FAIL", "C3",
                    "floor %r has l6_survived=false but is seated as a held member"
                    % (fl.get("type") or fl.get("anchor") or "?")))

    # C4 no-pack grounding cap
    if no_pack:
        for fl in floors:
            if (fl.get("grounding") or "").lower() == "high":
                issues.append(("FAIL", "C4",
                    "no_pack is true but floor %r is grounding=high; cap at medium under no-pack"
                    % (fl.get("type") or fl.get("anchor") or "?")))

    # C5 L6 discipline: discrete field present and not duplicated into evidence
    if not brake_fired:
        if not o.get("l6_falsify"):
            issues.append(("FAIL", "C5", "missing discrete l6_falsify field"))
    for fl in floors:
        ev = fl.get("evidence") or ""
        if _matches(L6_IN_EVIDENCE, ev):
            issues.append(("FAIL", "C5",
                "floor %r asserts L6 content inside its evidence; L6 belongs on the discrete line"
                % (fl.get("type") or fl.get("anchor") or "?")))

    # C6 (advisory) speaker gender/role fabrication
    blob = _txt(o.get("cascade"), o.get("phase2"),
                " ".join((fl.get("anchor") or "") + " " + (fl.get("evidence") or "") for fl in floors),
                sel.get("anti_default_check"))
    if _matches(GENDER_TOKENS, blob):
        issues.append(("WARN", "C6",
            "a gendered son/daughter role appears; confirm it was user-stated, not inferred"))

    # C7 (advisory) banned_tiebreaker named
    cand = sel.get("candidates") or []
    btb = (sel.get("banned_tiebreaker_used") or "").strip().lower()
    if not brake_fired and len(cand) >= 2 and btb in ("", "none", "n/a"):
        issues.append(("WARN", "C7",
            "banned_tiebreaker_used is a bare %r with %d candidates; name the cue grounding each floor"
            % (btb or "(empty)", len(cand))))

    # C8 (advisory) coined/fused terminus type
    for fl in floors:
        t = (fl.get("type") or "").lower()
        if t and t not in MAP_TYPES:
            fused = "_" in t and any(part in "".join(MAP_TYPES) for part in t.split("_"))
            note = "looks fused/coined" if fused else "not in the co-equal map (pack-added?)"
            issues.append(("WARN", "C8", "floor type %r %s" % (t, note)))

    return issues


def _load(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return data if isinstance(data, list) else [data]


def run_files(paths):
    total_fail = 0
    for path in paths:
        try:
            outputs = _load(path)
        except Exception as exc:  # noqa: BLE001
            print("ERROR reading %s: %s" % (path, exc))
            total_fail += 1
            continue
        for i, o in enumerate(outputs):
            if isinstance(o, dict) and o.get("_expect_fail") is not None:
                o = {k: v for k, v in o.items() if not k.startswith("_")}
            label = "%s[%d]" % (os.path.basename(path), i) if len(outputs) > 1 else os.path.basename(path)
            issues = check_output(o)
            fails = [x for x in issues if x[0] == "FAIL"]
            warns = [x for x in issues if x[0] == "WARN"]
            total_fail += len(fails)
            if not issues:
                print("  OK    %s" % label)
            else:
                print("  %-5s %s" % ("FAIL" if fails else "warn", label))
                for level, code, msg in issues:
                    print("        [%s %s] %s" % (level, code, msg))
    return total_fail


def selftest(here):
    fix = os.path.join(here, "tests", "fixtures")
    if not os.path.isdir(fix):
        print("no fixtures dir at %s" % fix)
        return 1
    bad = 0
    files = sorted(f for f in os.listdir(fix) if f.endswith(".json"))
    for fname in files:
        path = os.path.join(fix, fname)
        raw = _load(path)[0]
        expect_fail = raw.get("_expect_fail")  # list of check codes, or [] for clean
        o = {k: v for k, v in raw.items() if not k.startswith("_")}
        issues = check_output(o)
        got_codes = sorted({c for lvl, c, _ in issues if lvl == "FAIL"})
        if expect_fail is None:
            print("  ?     %s (no _expect_fail marker, skipped)" % fname)
            continue
        want = sorted(expect_fail)
        ok = got_codes == want
        bad += 0 if ok else 1
        print("  %-4s %-34s expected FAIL %s, got %s"
              % ("OK" if ok else "MISS", fname, want or "(none)", got_codes or "(none)"))
    if bad:
        print("\nSELFTEST FAIL: %d fixture(s) did not match expectation" % bad)
    else:
        print("\nSELFTEST OK: all %d fixtures behaved as expected" % len(files))
    return 1 if bad else 0


def main(argv):
    here = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if "--selftest" in argv:
        return selftest(here)
    if "--dir" in argv:
        d = argv[argv.index("--dir") + 1]
        paths = [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith(".json")]
    else:
        paths = [a for a in argv[1:] if not a.startswith("--")]
    if not paths:
        print(__doc__)
        return 2
    print("Checking %d output file(s):" % len(paths))
    fails = run_files(paths)
    print("\n%s" % ("All checks passed." if fails == 0 else "%d hard failure(s)." % fails))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
