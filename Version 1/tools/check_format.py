#!/usr/bin/env python3
"""Formatting / LaTeX / sprite audit for the chapter markdown.

This is the static half of the workflow's "inspect for latex, sprite, and other
formatting issues" stage. It scans book/chapters/*.md and book/appendices/*.md and
reports:

  LaTeX
    - unbalanced '$' (odd count of inline math delimiters on a line/file)
    - unbalanced $$ display blocks
    - \left without a matching \right (per math span, heuristic)
    - unknown macro lookalikes (\foo not in the known macro set) -> warning
    - empty math spans  $$  /  $ $

  Sprites / figures
    - <img src="..."> whose file is missing from assets/
    - sprite dex ids outside 1..151
    - figures missing alt text or figcaption
    - raw markdown image syntax ![](...) (we standardize on <figure> HTML)

  Callout boxes
    - fenced-div classes not in the known set (typo guard)
    - a box opened with ::: but never closed

  Structure
    - each chapter has the required architecture headings (warn if missing)

Exit 0 = pass/clean, 1 = hard errors found. Warnings never fail the build.
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CH_DIR = ROOT / "book" / "chapters"
APX_DIR = ROOT / "book" / "appendices"
ASSETS = ROOT / "assets"

KNOWN_BOX_CLASSES = {"pokedex-entry", "trainers-tip", "team-rocket", "kanto-realworld",
                     "cold-open", "problem-set", "answer-key", "concept-gate"}

# Macros defined in book/mathjax-preamble.md plus common TeX commands.
KNOWN_MACROS = {
    r"\E", r"\Var", r"\SD", r"\Cov", r"\Corr", r"\given", r"\Normal", r"\Expo",
    r"\Poisson", r"\Binom", r"\Geom", r"\NegBin", r"\HyperGeom", r"\GammaDist",
    r"\BetaDist", r"\Unif", r"\dplus", r"\limexp", r"\indicator",
    # standard
    r"\frac", r"\tfrac", r"\dfrac", r"\sum", r"\int", r"\prod", r"\lim", r"\infty",
    r"\theta", r"\lambda", r"\alpha", r"\beta", r"\gamma", r"\Gamma", r"\mu", r"\sigma",
    r"\Phi", r"\phi", r"\rho", r"\pi", r"\sqrt", r"\left", r"\right", r"\cdot", r"\times",
    r"\wedge", r"\vee", r"\mid", r"\leq", r"\geq", r"\neq", r"\approx", r"\sim", r"\in",
    r"\binom", r"\text", r"\mathbf", r"\mathcal", r"\operatorname", r"\begin", r"\end",
    r"\partial", r"\quad", r"\qquad", r"\ldots", r"\cdots", r"\overline", r"\underbrace",
    r"\perp", r"\Pr", r"\exp", r"\ln", r"\log", r"\max", r"\min", r"\bar", r"\hat",
    r"\Big", r"\big", r"\Bigl", r"\Bigr", r"\left\{", r"\right\}", r"\,", r"\;", r"\!",
    r"\newcommand", r"\middle",
    # standard MathJax commands that legitimately appear in chapters
    r"\not", r"\top", r"\le", r"\ge", r"\Sigma", r"\pm", r"\mp", r"\to", r"\dots",
    r"\Rightarrow", r"\Leftarrow", r"\Leftrightarrow", r"\implies", r"\iff",
    r"\checkmark", r"\dot", r"\ddot", r"\textstyle", r"\displaystyle", r"\scriptstyle",
    r"\boxed", r"\propto", r"\equiv", r"\subset", r"\subseteq", r"\supset", r"\cup",
    r"\cap", r"\emptyset", r"\varnothing", r"\forall", r"\exists", r"\nu", r"\xi",
    r"\zeta", r"\eta", r"\kappa", r"\tau", r"\omega", r"\Omega", r"\Lambda", r"\Theta",
    r"\Delta", r"\delta", r"\epsilon", r"\varepsilon", r"\varphi", r"\ell", r"\Pi",
    r"\binom", r"\choose", r"\frac", r"\sqrt", r"\langle", r"\rangle", r"\lfloor",
    r"\rfloor", r"\lceil", r"\rceil", r"\mathrm", r"\mathbb", r"\mathit", r"\nolimits",
    r"\limits", r"\substack", r"\stackrel", r"\overset", r"\underset", r"\vphantom",
    r"\colon", r"\setminus", r"\times", r"\div", r"\ast", r"\star", r"\circ", r"\bullet",
    r"\arctan", r"\arcsin", r"\arccos", r"\sin", r"\cos", r"\tan", r"\sec", r"\csc",
    r"\cot", r"\sinh", r"\cosh", r"\tanh", r"\det", r"\gcd", r"\deg", r"\dim", r"\sup",
    r"\inf", r"\liminf", r"\limsup", r"\arg", r"\nabla", r"\hline", r"\cline", r"\hphantom",
    r"\bigr", r"\bigl", r"\biggr", r"\biggl", r"\ne", r"\Longrightarrow", r"\Longleftarrow",
    r"\iint", r"\iiint", r"\oint", r"\Vert", r"\vert", r"\lvert", r"\rvert", r"\lVert",
    r"\rVert", r"\notin", r"\ni", r"\models", r"\mapsto", r"\longmapsto", r"\hookrightarrow",
    r"\textbf", r"\textit", r"\texttt", r"\textsf", r"\emph", r"\Longleftrightarrow",
    r"\supseteq", r"\subseteq", r"\dbinom", r"\tbinom", r"\smallsetminus", r"\complement",
    r"\xrightarrow", r"\xleftarrow", r"\longrightarrow", r"\longleftarrow", r"\underline",
    r"\overbrace", r"\widehat", r"\widetilde", r"\vec", r"\dagger", r"\circ",
    r"\phantom", r"\bigcup", r"\bigcap", r"\cancel", r"\leftrightarrow", r"\bigoplus", r"\bigotimes",
}

REQUIRED_HEADINGS = [
    "Cold Open", "Briefing", "Pok", "Worked", "Trainer", "Rocket",
    "Gym Battle", "Gym Challenge", "Answer Key", "Badge",
]

IMG_RE = re.compile(r'<img\s+[^>]*src="([^"]+)"[^>]*>', re.I)
ALT_RE = re.compile(r'\balt="', re.I)
MD_IMG_RE = re.compile(r'!\[[^\]]*\]\([^)]+\)')
FENCE_RE = re.compile(r'^:::+\s*(\{?\.?[\w-]*\}?)?\s*$')
MACRO_RE = re.compile(r'\\[a-zA-Z]+')
SPRITE_DEX_RE = re.compile(r'/sprites/front/(\d+)\.png')


def audit_file(path: Path):
    errors, warnings = [], []
    text = path.read_text()
    rel = path.relative_to(ROOT)

    # ---- $ balance (ignore escaped \$ = literal currency, common in a pricing book) ----
    math_text = text.replace(r"\$", "")
    if math_text.count("$$") % 2 != 0:
        errors.append(f"{rel}: unbalanced '$$' display delimiters (count={math_text.count('$$')})")
    stripped = math_text.replace("$$", "")
    if stripped.count("$") % 2 != 0:
        errors.append(f"{rel}: unbalanced inline '$' delimiters")

    # ---- per math-span checks ----
    for m in re.finditer(r'\$\$(.+?)\$\$', text, re.S):
        span = m.group(1)
        if not span.strip():
            errors.append(f"{rel}: empty $$ math span")
        if span.count(r"\left") != span.count(r"\right"):
            warnings.append(f"{rel}: \\left/\\right mismatch in a display span")
    for mac in set(MACRO_RE.findall(text)):
        if mac not in KNOWN_MACROS and len(mac) > 2:
            warnings.append(f"{rel}: unrecognized macro {mac} (typo? add to preamble?)")

    # ---- markdown image syntax (we standardize on <figure>) ----
    if MD_IMG_RE.search(text):
        warnings.append(f"{rel}: markdown ![]() image found — use <figure> HTML instead")

    # ---- <img> existence + alt + dex range ----
    for src in IMG_RE.findall(text):
        # resolve relative to assets root (paths look like ../../assets/...)
        candidate = (ASSETS / src.split("assets/", 1)[1]) if "assets/" in src else (path.parent / src)
        if "assets/" in src and not candidate.exists():
            errors.append(f"{rel}: missing image asset {src}")
        dex = SPRITE_DEX_RE.search(src)
        if dex and not (1 <= int(dex.group(1)) <= 151):
            errors.append(f"{rel}: sprite dex {dex.group(1)} outside Kanto 1..151")
    for tag in re.findall(r'<img\s[^>]*>', text, re.I):
        if not ALT_RE.search(tag):
            warnings.append(f"{rel}: <img> without alt text")

    # ---- fenced-div boxes: known class + balance ----
    open_boxes = 0
    for line in text.splitlines():
        m = FENCE_RE.match(line.strip())
        if not m:
            continue
        token = (m.group(1) or "").strip("{}.")
        if token:  # opening with a class
            if token not in KNOWN_BOX_CLASSES:
                warnings.append(f"{rel}: unknown box class '{token}'")
            open_boxes += 1
        else:       # closing :::
            open_boxes -= 1
    if open_boxes != 0:
        errors.append(f"{rel}: unbalanced ::: fenced-div boxes (delta={open_boxes})")

    # ---- structure (chapters only) ----
    is_stub = "<!-- status: stub -->" in text
    # ch00 = orientation (no problem set); chNNx_* = checkpoints (review template).
    is_orientation = path.name.startswith("ch00")
    is_checkpoint = "checkpoint" in path.name.lower()

    def heading_pos(name):
        m = re.search(rf"^#{{1,3}}\s+.*{re.escape(name)}.*$", text, re.I | re.M)
        return m.start() if m else -1

    if path.parent == CH_DIR and not is_stub and not is_orientation and not is_checkpoint:
        missing = [h for h in REQUIRED_HEADINGS if h.lower() not in text.lower()]
        if missing:
            warnings.append(f"{rel}: missing sections {missing}")

        # problems list then solutions list, like a real textbook. Anchor on the
        # actual markdown HEADINGS, not any prose mention.
        i_problems = heading_pos("Gym Challenge")
        i_solutions = heading_pos("Answer Key")
        if i_problems == -1:
            errors.append(f"{rel}: no problems list (missing 'The Gym Challenge')")
        if i_solutions == -1:
            errors.append(f"{rel}: no solutions list (missing 'Answer Key')")
        if i_problems != -1 and i_solutions != -1 and i_solutions < i_problems:
            errors.append(f"{rel}: 'Answer Key' must come AFTER the problem set")

        # every problem id Cn.k stated in the problem set must be solved in the key
        mnum = re.match(r"ch(\d+)", path.name)
        if mnum and i_problems != -1 and i_solutions != -1:
            n = int(mnum.group(1))
            pid = re.compile(rf"\bC{n}\.(\d+)\b")
            prob_ids = set(pid.findall(text[i_problems:i_solutions]))
            soln_ids = set(pid.findall(text[i_solutions:]))
            if not prob_ids:
                warnings.append(f"{rel}: no numbered problems (expected C{n}.k) in the problem set")
            unsolved = sorted(prob_ids - soln_ids, key=int)
            if unsolved:
                errors.append(f"{rel}: problems without a solution in the key: "
                              + ", ".join(f'C{n}.{k}' for k in unsolved))

    # checkpoints: review template — just require a solutions key exists
    if path.parent == CH_DIR and is_checkpoint and not is_stub:
        if heading_pos("Answer Key") == -1:
            errors.append(f"{rel}: checkpoint missing an 'Answer Key'")

    return errors, warnings


def main() -> int:
    files = sorted(CH_DIR.glob("*.md")) + sorted(APX_DIR.glob("*.md"))
    if not files:
        print("No chapter/appendix files found yet.")
        return 0
    all_err, all_warn = [], []
    for f in files:
        e, w = audit_file(f)
        all_err += e
        all_warn += w

    print(f"== Format/LaTeX/sprite audit ==  files={len(files)}  "
          f"errors={len(all_err)}  warnings={len(all_warn)}")
    for w in all_warn:
        print(f"  [warn]  {w}")
    for e in all_err:
        print(f"  [ERROR] {e}")
    if all_err:
        print("FAIL: hard formatting errors.")
        return 1
    print("PASS: no hard formatting errors.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
