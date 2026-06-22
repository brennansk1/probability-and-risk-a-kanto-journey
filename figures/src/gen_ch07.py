#!/usr/bin/env python3
"""Generate the Chapter 7 (Checkpoint A — Act I review / route campfire) figure.

Manifest (MASTER_PLAN_V3 §19/§30, DESIGN_BLUEPRINT ch07 row) — ONE diagram into
assets/diagrams/:
  ch07_act1_mindmap   a six-topic concept mind-map of Act I (the "Countable Road"):
                      fundamentals -> conditional/Bayes -> discrete moments ->
                      combinatorics -> discrete distributions -> deductibles, with the
                      single load-bearing idea on each node and the dependency arrows
                      that link them. Composites three REAL Act-I mascot sprites in the
                      margins (Spearow #21 = Route 1 fundamentals, Pikachu #25 = the
                      S.S. Anne moments, Gastly #92 = the Lavender Poisson swarm).

This is a REVIEW checkpoint (no new theory); the figure is a retrieval scaffold, not a
teaching diagram. The six nodes mirror ch01-ch06 in TIA order (A.1 -> A.6).

PRINT TARGET: bound book -> the PNG at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every node is distinguished by its
position + text label (color is never the sole channel). Real Pokemon art obeys the IRON
RULE: margins/corners only, never over a node box, arrow, or word a reader must read.

Run: python3 figures/src/gen_ch07.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from cycler import cycler

from sprite_util import front, place_sprite
from type_palette import chapter_accent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
NORMAL = chapter_accent(7)  # §17 Normal accent (#A8A878) — checkpoint banner/figure parity.
INK = "#333333"

plt.rcParams["axes.prop_cycle"] = cycler(color=[
    KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN,
    "#FF7043", "#7B61FF", "#00BCD4", "#FF4081", "#8D6E63", "#78909C"])

PRINT_DPI = 300


def save(fig, name: str) -> Path:
    path = OUT / f"{name}.png"
    fig.savefig(path, dpi=PRINT_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [fig] {path.relative_to(ROOT)}")
    return path


def _blank(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_facecolor("white")
    ax.grid(False)


# --------------------------------------------------------------------------
# ch07_act1_mindmap — the six-topic concept map of Act I (the Countable Road).
#   Six nodes (ch01..ch06) in TIA order, each with its load-bearing idea, joined
#   by dependency arrows. Three real Act-I mascots in the margins (iron rule).
# --------------------------------------------------------------------------
def fig_act1_mindmap():
    fig, ax = plt.subplots(figsize=(13.5, 8.6))
    _blank(ax)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.set_title("Act I — The Countable Road: the six discrete ideas you carry forward",
                 fontsize=15, fontweight="bold", y=1.01)

    # The central spine label.
    ax.add_patch(FancyBboxPatch((5.35, 4.15), 3.3, 0.75,
                                boxstyle="round,pad=0.04,rounding_size=0.14",
                                fc=NORMAL, ec=INK, lw=2.0, zorder=4))
    ax.text(7.0, 4.52, "ACT I\nDISCRETE", ha="center", va="center",
            fontsize=12.5, fontweight="bold", color="white", zorder=5,
            linespacing=0.95)

    # node = (cx, cy, color, hatch, header, sub, idea-lines...)
    nodes = [
        # ch01 — Fundamentals (top-left)
        (3.0, 7.3, KANTO_RED, "..",
         "ch01 · Fundamentals", "A.1 — sets, events, axioms",
         ["$P(A^c)=1-P(A)$  (the",
          "  \"at least one\" trick);",
          "$P(A\\cup B)=P(A)+P(B)$",
          "$\\quad-\\,P(A\\cap B)$"]),
        # ch02 — Conditional & Bayes (top-center)
        (7.0, 7.6, KANTO_BLUE, "//",
         "ch02 · Conditional & Bayes", "A.2 — reasoning from evidence",
         ["$P(A\\mid B)=\\dfrac{P(A\\cap B)}{P(B)}$;",
          "total prob. (weighted avg)",
          "$\\to$ Bayes: flip the",
          "  conditioning"]),
        # ch03 — Discrete moments (top-right)
        (11.0, 7.3, KANTO_YEL, "xx",
         "ch03 · Discrete Moments", "A.3 — describe a whole RV",
         ["$E[X]=\\sum k\\,p(k)$;",
          "$\\mathrm{Var}=E[X^2]-(E[X])^2$;",
          "$\\mathrm{Var}(aX+b)=a^2\\mathrm{Var}(X)$;",
          "MGF, discrete uniform"]),
        # ch04 — Combinatorics (bottom-left)
        (3.0, 1.7, KANTO_GREEN, "\\\\",
         "ch04 · Combinatorics", "A.4 — counting machines",
         ["$\\binom{n}{k}$ choose; binomial",
          "(with replacement);",
          "hypergeometric (without);",
          "order? replace? classify"]),
        # ch05 — Discrete distributions (bottom-center)
        (7.0, 1.4, "#7B61FF", "..",
         "ch05 · Discrete Distributions", "A.5 — named count/wait models",
         ["geometric & memoryless;",
          "neg-binomial (wait for $r$);",
          "Poisson $P(k)=\\dfrac{e^{-\\lambda}\\lambda^k}{k!}$;",
          "Poissons add: $\\lambda_1+\\lambda_2$"]),
        # ch06 — Deductibles (bottom-right)
        (11.0, 1.7, "#FF7043", "//",
         "ch06 · Deductibles & Limits", "A.6 — payment from a loss",
         ["deductible $(X-d)_+$;",
          "limit $X\\wedge u$; budget",
          "$E[X\\wedge u]+E[(X-d)_+]$",
          "$\\quad=E[X]$; per-loss vs -pay"]),
    ]

    box_w, box_h = 3.5, 2.05
    centers = {}
    for i, (cx, cy, col, hatch, header, sub, lines) in enumerate(nodes):
        x0, y0 = cx - box_w / 2, cy - box_h / 2
        centers[i] = (cx, cy)
        ax.add_patch(FancyBboxPatch((x0, y0), box_w, box_h,
                                    boxstyle="round,pad=0.04,rounding_size=0.12",
                                    fc="white", ec=col, lw=2.4, zorder=3))
        # a thin colored+hatched header strip (grayscale-safe: hatch + text).
        ax.add_patch(FancyBboxPatch((x0, y0 + box_h - 0.62), box_w, 0.62,
                                    boxstyle="round,pad=0.0,rounding_size=0.10",
                                    fc=col, ec=col, lw=1.0, alpha=0.92,
                                    hatch=hatch, zorder=3))
        ax.text(cx, y0 + box_h - 0.31, header, ha="center", va="center",
                fontsize=10.3, fontweight="bold", color="white", zorder=5)
        ax.text(cx, y0 + box_h - 0.86, sub, ha="center", va="center",
                fontsize=8.2, style="italic", color=INK, zorder=5)
        for j, line in enumerate(lines):
            ax.text(x0 + 0.22, y0 + box_h - 1.22 - j * 0.345, line, ha="left",
                    va="center", fontsize=8.7, color=INK, zorder=5)

    # Dependency arrows along the TIA spine (ch01 -> ... -> ch06), routed via the hub.
    def arrow(a, b, rad=0.0, col=KANTO_GRAY):
        (xa, ya), (xb, yb) = centers[a], centers[b]
        ax.add_patch(FancyArrowPatch((xa, ya), (xb, yb),
                                     connectionstyle=f"arc3,rad={rad}",
                                     arrowstyle="-|>", mutation_scale=16,
                                     lw=1.8, color=col, alpha=0.55,
                                     shrinkA=46, shrinkB=46, zorder=2))

    arrow(0, 1, rad=-0.12)   # fundamentals -> conditional
    arrow(1, 2, rad=-0.12)   # conditional  -> moments
    arrow(0, 3, rad=0.12)    # fundamentals -> combinatorics (counting feeds distributions)
    arrow(3, 4, rad=-0.12)   # combinatorics -> distributions
    arrow(2, 4, rad=0.14)    # moments      -> distributions (each dist. has E,Var)
    arrow(4, 5, rad=-0.12)   # distributions -> deductibles (transform a loss RV)

    # tiny spine annotation linking to the central hub.
    ax.text(7.0, 3.05,
            "every named distribution (ch05) and every payment rule (ch06) is a\n"
            "discrete RV (ch03) built by counting (ch04) under the axioms (ch01)",
            ha="center", va="center", fontsize=8.6, color=INK, style="italic",
            bbox=dict(boxstyle="round,pad=0.3", fc="#FFF6D6", ec=KANTO_YEL, lw=1.2),
            zorder=4)

    # --- Real Act-I mascots in the margins (iron rule: corners only). ---
    # Spearow #21 = Route 1 fundamentals; Pikachu #25 = S.S. Anne moments;
    # Gastly #92 = the Lavender Poisson swarm.
    place_sprite(ax, front(21), (0.40, 8.55), zoom=0.42, alpha=0.95, zorder=6)
    place_sprite(ax, front(25), (13.6, 8.55), zoom=0.42, alpha=0.95, zorder=6)
    place_sprite(ax, front(92), (0.45, 0.55), zoom=0.42, alpha=0.95, zorder=6)

    fig.tight_layout()
    return save(fig, "ch07_act1_mindmap")


REGISTRY = [
    fig_act1_mindmap,
]


def main() -> None:
    print(f"Generating Chapter 7 (Checkpoint A) figure -> {OUT} at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figure written.")


if __name__ == "__main__":
    main()
