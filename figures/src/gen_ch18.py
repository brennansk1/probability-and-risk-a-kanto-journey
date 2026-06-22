#!/usr/bin/env python3
"""Generate the Chapter 18 (Checkpoint B — Act III multivariate review) figure.

Manifest (DESIGN_BLUEPRINT ch18 row · MASTER_PLAN_V3 §16, §19, §30) — one diagram
into assets/diagrams/:
  ch18_act3_mindmap   the four-topic concept map of Act III, drawn as a single
                      spine that runs joint distributions -> joint moments &
                      covariance -> conditional / double expectation -> order
                      statistics, with each node carrying its load-bearing
                      formula. Composites three REAL Act-III mascot sprites in the
                      margins (Charmander #4 = Cinnabar/Blaine joint logs,
                      Rhyhorn #111 = Giovanni's compound-mixture squads,
                      Lapras #131 = the Elite-Four bracket / order statistics).

This is a REVIEW checkpoint figure: no new theory, just a one-page map that lets a
reader retrieve the whole act at a glance.

PRINT TARGET: bound book, rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every node is distinguished
by position + text label, never color alone, so the map survives grayscale.
Real sprites obey the IRON RULE: art lives in the outer margins, never over a node
box, an arrow, or a formula a reader must read. Sprite art is REAL
(assets/sprites/front/*.png) and only ever COMPOSITED, never generated.

Run: python3 figures/src/gen_ch18.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

from sprite_util import front, place_sprite
from type_palette import chapter_accent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe). ch18 = Normal type (checkpoint), so the accent
# is the §17 normal color via chapter_accent(18).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
ACCENT = chapter_accent(18)  # normal #A8A878
INK = "#333333"

PRINT_DPI = 300

# The four Act-III topics, top to bottom: each is (title, ch-tag, formula lines,
# node fill color, hatch). Colors double as a four-step gradient down the spine but
# the position + label carry the meaning, so grayscale is fine.
TOPICS = [
    ("1. JOINT DISTRIBUTIONS", "ch14 · C.1 · 3a,3b",
     [r"$f_{X,Y}(x,y)$ over a region; $\iint f = 1$",
      r"marginal: $f_X(x)=\int f_{X,Y}\,dy$",
      r"independent $\Leftrightarrow f_{X,Y}=f_X f_Y$ on a rectangle"],
     KANTO_BLUE, "//"),
    ("2. JOINT MOMENTS & COVARIANCE", "ch15 · C.2.1-2 · 3c,3e,3g,3h",
     [r"$\mathrm{Cov}(X,Y)=E[XY]-E[X]E[Y]$",
      r"$\rho=\mathrm{Cov}/(\sigma_X\sigma_Y)\in[-1,1]$",
      r"$\mathrm{Var}(aX{+}bY)=a^2\sigma_X^2{+}b^2\sigma_Y^2{+}2ab\,\mathrm{Cov}$"],
     KANTO_GREEN, "xx"),
    ("3. CONDITIONAL & DOUBLE EXPECTATION", "ch16 · C.2.3 · 3c,3d",
     [r"$E[X]=E[\,E[X\mid Y]\,]$",
      r"$\mathrm{Var}(X)=E[\mathrm{Var}(X\mid Y)]+\mathrm{Var}(E[X\mid Y])$",
      r"compound: $E[S]{=}E[N]\mu,\ \mathrm{Var}(S){=}E[N]\sigma^2{+}\mathrm{Var}(N)\mu^2$"],
     KANTO_YEL, ".."),
    ("4. ORDER STATISTICS", "ch17 · C.3 · 3f",
     [r"$F_{\max}=[F(x)]^n$,   $F_{\min}=1-[S(x)]^n$",
      r"min of indep. exponentials: rates add",
      r"reliability: series $=$ min, parallel $=$ max"],
     KANTO_RED, "\\\\"),
]


def save(fig, name: str) -> Path:
    path = OUT / f"{name}.png"
    fig.savefig(path, dpi=PRINT_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [fig] {path.relative_to(ROOT)}")
    return path


def fig_act3_mindmap():
    fig, ax = plt.subplots(figsize=(12.5, 9.6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    ax.axis("off")
    ax.set_facecolor("white")

    # Title banner.
    ax.text(6.0, 11.55, "ACT III — THE LEAGUE  ·  Multivariate Probability",
            ha="center", va="center", fontsize=17, fontweight="bold", color=INK)
    ax.text(6.0, 11.08,
            "One spine, four landmarks: a pair of variables, how they move "
            "together, averaging over a hidden layer, and the extremes of a field.",
            ha="center", va="center", fontsize=10.5, color=KANTO_GRAY)

    # Node geometry: four stacked boxes down the centre, joined by a single spine.
    box_w, box_h = 7.4, 1.78
    cx = 6.0
    top_y = 9.55
    gap = 2.36
    centres = [top_y - i * gap for i in range(4)]

    for (title, tag, lines, fill, hatch), cy in zip(TOPICS, centres):
        x0 = cx - box_w / 2
        y0 = cy - box_h / 2
        # Node box.
        ax.add_patch(FancyBboxPatch(
            (x0, y0), box_w, box_h,
            boxstyle="round,pad=0.06,rounding_size=0.16",
            facecolor=fill, alpha=0.13, edgecolor=fill, lw=2.4, zorder=3))
        # A thin hatched accent stripe on the left edge for grayscale separation.
        ax.add_patch(FancyBboxPatch(
            (x0, y0), 0.32, box_h,
            boxstyle="round,pad=0.0,rounding_size=0.10",
            facecolor=fill, alpha=0.34, edgecolor="none", hatch=hatch, zorder=4))
        # Title + chapter tag.
        ax.text(x0 + 0.55, cy + box_h / 2 - 0.34, title, ha="left", va="center",
                fontsize=12.5, fontweight="bold", color=INK, zorder=5)
        ax.text(x0 + box_w - 0.2, cy + box_h / 2 - 0.34, tag, ha="right",
                va="center", fontsize=8.4, color=KANTO_GRAY, style="italic",
                zorder=5)
        # Load-bearing formulas.
        for j, line in enumerate(lines):
            ax.text(x0 + 0.55, cy + 0.12 - j * 0.46, line, ha="left", va="center",
                    fontsize=10.2, color=INK, zorder=5)

    # The spine: arrows connecting consecutive nodes (the dependency chain).
    for cy in centres[:-1]:
        ax.add_patch(FancyArrowPatch(
            (cx, cy - box_h / 2 - 0.02), (cx, cy - gap + box_h / 2 + 0.02),
            arrowstyle="-|>", mutation_scale=22, lw=2.2, color=KANTO_GRAY,
            zorder=2))

    # Foundation tag at the bottom: the through-line of the whole act.
    ax.text(6.0, 0.46,
            "THE THREAD:  variables now move together — a team is a sum of "
            "correlated parts, a threat is averaged over a hidden tier, a "
            "champion is the maximum of the field.",
            ha="center", va="center", fontsize=9.6, color=INK,
            bbox=dict(boxstyle="round,pad=0.4", fc=KANTO_BG, ec=ACCENT, lw=1.6))

    # --- Real Act-III mascot sprites in the OUTER margins (iron rule). ---
    # Charmander #4 — Cinnabar / Blaine joint-distribution logs (top-left margin).
    place_sprite(ax, front(4), (0.95, 9.55), zoom=0.46, alpha=0.97, zorder=6)
    ax.text(0.95, 8.92, "#4 Charmander", ha="center", fontsize=7.6, color=INK)
    # Rhyhorn #111 — Giovanni's compound-mixture squads (mid-right margin, beside
    # the conditional/double-expectation node).
    place_sprite(ax, front(111), (11.15, 4.85), zoom=0.46, alpha=0.97, zorder=6)
    ax.text(11.15, 4.22, "#111 Rhyhorn", ha="center", fontsize=7.6, color=INK)
    # Lapras #131 — the Elite-Four bracket / order statistics (bottom-left margin).
    place_sprite(ax, front(131), (0.95, 2.55), zoom=0.46, alpha=0.97, zorder=6)
    ax.text(0.95, 1.92, "#131 Lapras", ha="center", fontsize=7.6, color=INK)

    fig.tight_layout()
    return save(fig, "ch18_act3_mindmap")


REGISTRY = [fig_act3_mindmap]


def main() -> None:
    print(f"Generating Chapter 18 (Checkpoint B — Act III review) figures -> "
          f"{OUT} at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
