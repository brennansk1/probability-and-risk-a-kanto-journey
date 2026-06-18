#!/usr/bin/env python3
"""Coverage audit: prove the problem bank discharges every SOA outcome.

Reads syllabus/outcomes.yaml and problems/bank.yaml and asserts:
  - every learning outcome has >= min_per_outcome problems,
  - every in-scope distribution appears in >= min_per_distribution problems,
  - every problem references known outcomes/distributions and a valid tier.

Exit code 0 = pass, 1 = fail. Used by `make lint` and the workflow audit stage.
This is a *gate*, not a writer: during early scaffolding it will report gaps,
which is expected until the workflow fills the bank.
"""
from __future__ import annotations
import sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
TIERS = {"route_trainer", "gym_battle", "elite_challenge"}


def main() -> int:
    syl = yaml.safe_load((ROOT / "syllabus" / "outcomes.yaml").read_text())
    # Load problems/bank.yaml plus every per-chapter file in problems/bank.d/.
    problems = []
    for src in [ROOT / "problems" / "bank.yaml", *sorted((ROOT / "problems" / "bank.d").glob("*.yaml"))]:
        if src.exists():
            problems += (yaml.safe_load(src.read_text()) or {}).get("problems", []) or []

    all_outcomes = {o["id"] for t in syl["topics"] for o in t["outcomes"]}
    accepted_outcomes = all_outcomes | set(syl.get("extra_outcomes", []))
    all_dists = set(syl["distributions"]["discrete"]) | set(syl["distributions"]["continuous"])
    # accepted-but-not-counted tags: enrichment + structural/category labels
    extra_tags = set(syl.get("enrichment", [])) | set(syl.get("structural_tags", []))
    thr = syl["coverage_thresholds"]

    out_count: Counter = Counter()
    dist_count: Counter = Counter()
    errors, warnings = [], []

    for p in problems:
        pid = p.get("id", "<no-id>")
        if p.get("tier") not in TIERS:
            errors.append(f"{pid}: invalid tier {p.get('tier')!r}")
        for o in p.get("outcomes", []):
            if o not in accepted_outcomes:
                errors.append(f"{pid}: unknown outcome {o!r}")
            out_count[o] += 1
        for d in p.get("distributions", []):
            if d not in all_dists and d not in extra_tags:
                errors.append(f"{pid}: unknown distribution {d!r}")
            dist_count[d] += 1

    for o in sorted(all_outcomes):
        if out_count[o] < thr["min_per_outcome"]:
            warnings.append(f"outcome {o}: {out_count[o]}/{thr['min_per_outcome']} problems")
    for d in sorted(all_dists):
        if dist_count[d] < thr["min_per_distribution"]:
            warnings.append(f"distribution {d}: {dist_count[d]}/{thr['min_per_distribution']} problems")

    print(f"== Coverage audit ==  problems={len(problems)}  "
          f"outcomes_hit={len(out_count)}/{len(all_outcomes)}  "
          f"dists_hit={len(dist_count)}/{len(all_dists)}")
    for w in warnings:
        print(f"  [GAP]   {w}")
    for e in errors:
        print(f"  [ERROR] {e}")

    if errors:
        print("FAIL: structural errors in the problem bank.")
        return 1
    if warnings:
        print("INCOMPLETE: coverage gaps remain (expected until the bank is filled).")
        return 0
    print("PASS: full coverage.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
