#!/usr/bin/env python3
"""Numeric verification harness (the reproducibility gate, seed=151).

For every problem in problems/bank.yaml that carries a `verify:` expression, this
evaluates it and fails the build on a mismatch. The seed is 151 (the Kanto
Pokedex count) so any Monte-Carlo checks are reproducible.

The workflow's audit stage runs this to back the claim "every printed answer is
verified." `verify:` should be a Python boolean expression (closed-form identity
or a seeded simulation tolerance check).
"""
from __future__ import annotations
import math
import random
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SEED = 151

# Namespace exposed to verify expressions. This is trusted local content, so we
# allow __import__ (expressions commonly use __import__('math')/('scipy.stats')).
NS = {"math": math, "random": random, "abs": abs, "round": round, "sum": sum,
      "min": min, "max": max, "len": len, "range": range, "pow": pow,
      "int": int, "float": float}
try:
    import scipy.stats as _st  # noqa: F401
    NS["st"] = _st
except Exception:  # noqa: BLE001
    pass
SAFE_BUILTINS = {"__import__": __import__, "abs": abs, "round": round, "min": min,
                 "max": max, "sum": sum, "len": len, "range": range, "pow": pow,
                 "all": all, "any": any, "sorted": sorted, "int": int, "float": float,
                 "list": list, "map": map, "zip": zip, "enumerate": enumerate}


def main() -> int:
    random.seed(SEED)
    problems = []
    for src in [ROOT / "problems" / "bank.yaml", *sorted((ROOT / "problems" / "bank.d").glob("*.yaml"))]:
        if src.exists():
            problems += (yaml.safe_load(src.read_text()) or {}).get("problems", []) or []
    checked = passed = 0
    failures = []
    for p in problems:
        expr = p.get("verify")
        if not expr:
            continue
        checked += 1
        try:
            # Put modules in GLOBALS (not locals) so comprehensions/lambdas in the
            # expression can see math/st/random through their enclosing scope.
            g = {"__builtins__": SAFE_BUILTINS, **NS}
            ok = bool(eval(expr, g))  # noqa: S307
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{p['id']}: verify raised {exc!r}")
            continue
        if ok:
            passed += 1
        else:
            failures.append(f"{p['id']}: verify expression is False")

    print(f"== Numeric verification (seed={SEED}) ==  "
          f"with-verify={checked}  passed={passed}  failed={len(failures)}")
    for f in failures:
        print(f"  [ERROR] {f}")
    if failures:
        print("FAIL: numeric mismatch.")
        return 1
    print("PASS." if checked else "No verify expressions yet (expected during scaffolding).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
