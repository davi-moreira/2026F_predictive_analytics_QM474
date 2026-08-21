# -*- coding: utf-8 -*-
"""Detect non-length surface cues that let a student pick the keyed option
without knowing the material.

`audit_answer_length.py` measures ONE channel: how long the options are. The
Fall 2026 midterm passes it at exactly chance and is still exploitable, because
the cue moved into punctuation and vocabulary instead:

    "always pick the option containing a semicolon" scores 59.6% on the 85
    questions where it applies, against a 20% five-option floor.

This gate measures the channels the length audit cannot see. Run it alongside,
never instead of, `audit_answer_length.py`.

Usage:
    python3 scripts/audit_option_cues.py --bank _midterm_exam/2026F/banks
    python3 scripts/audit_option_cues.py --file <d2l.csv>
    python3 scripts/audit_option_cues.py --bank <dir> --per-form
    python3 scripts/audit_option_cues.py --bank <dir> --json      # machine-readable

Exit status is 1 if any cue is exploitable, so it can gate a build.

WHAT COUNTS AS A FAILURE
  - Any marker whose "pick the option carrying it" hit rate is significantly
    above chance on the questions where it applies (binomial, p < 0.01), and
    that applies to at least MIN_APPLICABLE questions.
  - Any vocabulary term that appears in keys and distractors at wildly different
    rates (a term that never appears in a key is just as exploitable as one that
    always does: it tells you what to eliminate).
  - Any single form whose zero-knowledge cascade score exceeds MAX_FORM_SCORE.
"""
import argparse
import csv
import glob
import io
import json
import math
import os
import re
import sys
from collections import Counter

MIN_APPLICABLE = 15       # ignore markers too rare to exploit
ALPHA = 0.01
MAX_FORM_SCORE = 0.30     # a single form must not hand over more than 30%

# marker name -> predicate on an option string
MARKERS = {
    "semicolon":        lambda t: ";" in t,
    "em dash":          lambda t: "—" in t,
    "en dash":          lambda t: "–" in t,
    "colon":            lambda t: ":" in t,
    "parenthetical":    lambda t: "(" in t,
    "comma-so":         lambda t: ", so " in t,
    "' and '":          lambda t: " and " in t,
    "' which '":        lambda t: " which " in t,
    "' because '":      lambda t: " because " in t,
    "absolute word":    lambda t: bool(re.search(r"\b(always|never|all|none|guaranteed|any)\b", t, re.I)),
    "hedge word":       lambda t: bool(re.search(r"\b(usually|typically|generally|often|may|can)\b", t, re.I)),
    "digit":            lambda t: bool(re.search(r"\d", t)),
}

# vocabulary asymmetry: terms that may mark an option as key or as distractor
VOCAB = ["concern", "should", "must", "cannot", "reject", "approve", "refuse",
         "instead", "risk", "wrong", "correct", "leak", "leakage", "baseline"]


def binom_p(k, n, p):
    """One-sided P(X >= k) for X ~ Binomial(n, p). Exact, no scipy."""
    if n == 0:
        return 1.0
    k = math.ceil(k)
    return sum(math.comb(n, i) * p**i * (1 - p)**(n - i) for i in range(k, n + 1))


def load_banks(d):
    out = []
    for f in sorted(glob.glob(os.path.join(d, "*.json"))):
        b = json.load(io.open(f, encoding="utf-8"))
        out.append((b["case_key"], [(q["options"], q["correct_index"]) for q in b["questions"]]))
    return out


def load_csv(path):
    qs, cur = [], None
    for row in csv.reader(io.open(path, encoding="utf-8")):
        if not row or not row[0]:
            continue
        if row[0] == "NewQuestion":
            if cur:
                qs.append(cur)
            cur = {"opts": [], "key": None}
        elif row[0] == "Option" and cur is not None:
            if row[1].strip() == "100.00":
                cur["key"] = len(cur["opts"])
            cur["opts"].append(row[2])
    if cur:
        qs.append(cur)
    return [(os.path.basename(path), [(q["opts"], q["key"]) for q in qs])]


def cascade_score(questions):
    """Zero-knowledge strategy: strongest marker first, then longest."""
    hit = 0.0
    order = ["semicolon", "em dash"]
    for opts, key in questions:
        picked = None
        for m in order:
            c = {i for i, t in enumerate(opts) if MARKERS[m](t)}
            if c:
                picked = c
                break
        if picked is None:
            picked = {max(range(len(opts)), key=lambda i: len(opts[i]))}
        if key in picked:
            hit += 1.0 / len(picked)
    return hit / max(len(questions), 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--bank")
    ap.add_argument("--file")
    ap.add_argument("--per-form", action="store_true")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args = ap.parse_args()
    if not (args.bank or args.file):
        sys.exit("need --bank <dir> or --file <csv>")

    forms = load_banks(args.bank) if args.bank else load_csv(args.file)
    allq = [q for _, qs in forms for q in qs]
    if not allq:
        sys.exit("no questions found")
    n_opts = Counter(len(o) for o, _ in allq)
    chance = sum((1 / k) * c for k, c in n_opts.items()) / len(allq)

    failures = []
    marker_rows = []
    for name, pred in MARKERS.items():
        appl = hit = 0
        for opts, key in allq:
            c = {i for i, t in enumerate(opts) if pred(t)}
            if not c or len(c) == len(opts):
                continue        # no signal if it marks nothing or everything
            appl += 1
            if key in c:
                hit += 1.0 / len(c)
        if appl < MIN_APPLICABLE:
            marker_rows.append((name, appl, hit, None, False))
            continue
        rate = hit / appl
        p = binom_p(hit, appl, chance)
        bad = rate > chance and p < ALPHA
        marker_rows.append((name, appl, hit, p, bad))
        if bad:
            failures.append(f"marker {name!r}: {100*rate:.1f}% on {appl} applicable questions "
                            f"(chance {100*chance:.1f}%, p={p:.2g})")

    vocab_rows = []
    for term in VOCAB:
        k = d = 0
        for opts, key in allq:
            for i, t in enumerate(opts):
                if re.search(rf"\b{re.escape(term)}\b", t, re.I):
                    if i == key:
                        k += 1
                    else:
                        d += 1
        if k + d >= MIN_APPLICABLE:
            share = k / (k + d)
            exp = chance
            bad = (k == 0 and d >= MIN_APPLICABLE) or (share > 0 and binom_p(k, k + d, exp) < ALPHA)
            vocab_rows.append((term, k, d, share, bad))
            if bad:
                failures.append(f"vocabulary {term!r}: {k} keys vs {d} distractors "
                                f"({100*share:.0f}% of occurrences are keys, expected ~{100*exp:.0f}%)")

    form_rows = []
    for name, qs in forms:
        s = cascade_score(qs)
        form_rows.append((name, s))
        if s > MAX_FORM_SCORE:
            failures.append(f"form {name!r}: zero-knowledge cascade scores {100*s:.1f}% "
                            f"(ceiling {100*MAX_FORM_SCORE:.0f}%)")

    if args.as_json:
        print(json.dumps({
            "chance": chance, "questions": len(allq),
            "markers": [{"marker": m, "applicable": a, "hit": h, "p": p, "fail": b}
                        for m, a, h, p, b in marker_rows],
            "vocab": [{"term": t, "keys": k, "distractors": d, "key_share": s, "fail": b}
                      for t, k, d, s, b in vocab_rows],
            "forms": [{"form": f, "cascade": s} for f, s in form_rows],
            "failures": failures, "pass": not failures}, indent=1))
        sys.exit(0 if not failures else 1)

    print(f"questions: {len(allq)}   options/question: {dict(n_opts)}   chance: {100*chance:.1f}%\n")
    print("MARKER CUES  (pick the option carrying the marker)")
    print(f"  {'marker':<16}{'applic.':>8}{'hits':>8}{'rate':>8}{'p':>10}  verdict")
    for m, a, h, p, bad in sorted(marker_rows, key=lambda r: -(r[2] / r[1] if r[1] else 0)):
        r = f"{100*h/a:.1f}%" if a else "-"
        ps = f"{p:.2g}" if p is not None else "-"
        print(f"  {m:<16}{a:>8}{h:>8.1f}{r:>8}{ps:>10}  {'FAIL' if bad else 'ok'}")

    print("\nVOCABULARY ASYMMETRY")
    print(f"  {'term':<14}{'keys':>7}{'distr.':>8}{'key share':>11}  verdict")
    for t, k, d, s, bad in sorted(vocab_rows, key=lambda r: -abs(r[3] - chance)):
        print(f"  {t:<14}{k:>7}{d:>8}{100*s:>10.0f}%  {'FAIL' if bad else 'ok'}")

    if args.per_form or args.bank:
        print("\nZERO-KNOWLEDGE CASCADE PER FORM  (semicolon > em dash > longest)")
        for f, s in sorted(form_rows, key=lambda r: -r[1]):
            print(f"  {f:<16}{100*s:>6.1f}%  {'FAIL' if s > MAX_FORM_SCORE else 'ok'}")
        pooled = cascade_score(allq)
        print(f"  {'POOLED':<16}{100*pooled:>6.1f}%   (chance {100*chance:.1f}%)")

    print()
    if failures:
        print(f"FAIL — {len(failures)} exploitable cue(s):")
        for f in failures:
            print("  - " + f)
        sys.exit(1)
    print("PASS — no exploitable non-length cue detected")


if __name__ == "__main__":
    main()
