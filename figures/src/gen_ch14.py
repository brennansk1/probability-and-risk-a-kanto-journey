#!/usr/bin/env python3
"""Generate every Chapter 14 (Joint Distributions / Cinnabar Mansion / Blaine) figure.

Manifest (MASTER_PLAN_V3 §16) — four required diagrams, all into assets/diagrams/:
  ch14_joint_grid         discrete pmf grid + continuous density footprint (one law for a pair)
  ch14_region_integral    the burnt-edge triangle: inner limits 0->y, true sub-triangle vs. the trap square
  ch14_marginal           integrating out a variable over a triangle (inner limit is the slanted edge)
  ch14_conditional_slice  slice the joint at X=x, rescale by f_X(x) into a conditional density

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is
ALSO distinguished by a hatch pattern / text label so figures survive grayscale
(color is never the sole channel). Sprites obey the IRON RULE: art in margins, never
over a curve, equation, axis, or number a reader must read. The chapter accent is the
fire type (Cinnabar / Blaine), via chapter_accent(14).

Run: python3 figures/src/gen_ch14.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch
from cycler import cycler

from sprite_util import front, place_sprite
from type_palette import chapter_accent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents). Fire-type chapter, so the accent
# leans on FIRE (#F08030 from the §17 type map) via chapter_accent(14).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
FIRE = chapter_accent(14)  # §17 Fire accent (banner/figure parity)
INK = "#333333"

plt.rcParams["axes.prop_cycle"] = cycler(color=[
    KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN,
    FIRE, "#7B61FF", "#00BCD4", "#FF4081", "#8D6E63", "#78909C"])

PRINT_DPI = 300


def save(fig, name: str) -> Path:
    path = OUT / f"{name}.png"
    fig.savefig(path, dpi=PRINT_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [fig] {path.relative_to(ROOT)}")
    return path


def _blank(ax):
    """Strip a panel down to a clean drawing surface (no grid/ticks/spines)."""
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_facecolor("white")
    ax.grid(False)


# --------------------------------------------------------------------------
# 1. ch14_joint_grid — discrete pmf grid (with margins) + continuous footprint.
#    Concept 1 / Beat 8: the two faces of a joint law.
# --------------------------------------------------------------------------
def fig_joint_grid():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(12.6, 5.8))
    fig.suptitle("Two faces of a joint law: discrete lumps (sum to 1) "
                 "and a continuous surface (volume = 1)", fontsize=13.5)

    # ---- LEFT: discrete pmf grid with row/column margins (WE 14.4 table) ----
    _blank(axL)
    axL.set_xlim(-0.4, 4.6)
    axL.set_ylim(-0.6, 4.6)
    axL.set_title("Discrete: $p(x,y)$ on a grid, margins = row/col sums",
                  fontsize=11)

    # p(x,y): rows x in {0,1}, cols y in {0,1,2}
    P = {(0, 0): 0.10, (0, 1): 0.20, (0, 2): 0.10,
         (1, 0): 0.15, (1, 1): 0.25, (1, 2): 0.20}
    # grid: columns y=0,1,2 -> px positions 1,2,3 ; rows x=0 (top), x=1 (bottom)
    col_x = {0: 1.0, 1: 2.0, 2: 3.0}
    row_y = {0: 3.0, 1: 2.0}
    cell = 0.92

    for (x, y), p in P.items():
        cx, cy = col_x[y], row_y[x]
        # lump size scales with probability (visual), label is exact.
        axL.add_patch(Rectangle((cx - cell / 2, cy - cell / 2), cell, cell,
                                facecolor=FIRE, edgecolor=INK, lw=1.2,
                                alpha=0.30 + 1.6 * p, hatch="..", zorder=2))
        axL.text(cx, cy, f"{p:.2f}", ha="center", va="center", fontsize=11,
                 color=INK, fontweight="bold", zorder=3)

    # axis labels
    for y, cx in col_x.items():
        axL.text(cx, 3.85, f"$y={y}$", ha="center", fontsize=10, color=KANTO_BLUE,
                 fontweight="bold")
    for x, cy in row_y.items():
        axL.text(0.25, cy, f"$x={x}$", ha="center", va="center", fontsize=10,
                 color=KANTO_RED, fontweight="bold")

    # row-sum margin (right) = marginal of X
    for x, cy in row_y.items():
        rs = sum(P[(x, y)] for y in (0, 1, 2))
        axL.add_patch(Rectangle((4.0 - cell / 2, cy - cell / 2), cell, cell,
                                facecolor=KANTO_RED, edgecolor=INK, lw=1.2,
                                alpha=0.85, hatch="xx", zorder=2))
        axL.text(4.0, cy, f"{rs:.2f}", ha="center", va="center", fontsize=10.5,
                 color="white", fontweight="bold", zorder=3)
    axL.text(4.0, 3.85, "$p_X$\n(rows)", ha="center", fontsize=8.5,
             color=KANTO_RED, fontweight="bold")

    # col-sum margin (bottom) = marginal of Y
    for y, cx in col_x.items():
        cs = sum(P[(x, y)] for x in (0, 1))
        axL.add_patch(Rectangle((cx - cell / 2, 1.0 - cell / 2), cell, cell,
                                facecolor=KANTO_BLUE, edgecolor=INK, lw=1.2,
                                alpha=0.85, hatch="//", zorder=2))
        axL.text(cx, 1.0, f"{cs:.2f}", ha="center", va="center", fontsize=10.5,
                 color="white", fontweight="bold", zorder=3)
    axL.text(0.25, 1.0, "$p_Y$\n(cols)", ha="center", va="center", fontsize=8.5,
             color=KANTO_BLUE, fontweight="bold")

    axL.text(2.3, 0.05, r"all lumps sum to $1$", ha="center", fontsize=9.5,
             style="italic", color=INK)

    # ---- RIGHT: continuous surface footprint over the unit square ----
    _blank(axR)
    axR.set_title("Continuous: $f(x,y)=x+y$, $P((X,Y)\\in A)$ = volume over $A$",
                  fontsize=11)
    axR.set_xlim(-0.15, 1.25)
    axR.set_ylim(-0.15, 1.25)

    # shade the unit square with a density gradient (darker where x+y larger).
    n = 200
    xs = np.linspace(0, 1, n)
    ys = np.linspace(0, 1, n)
    XX, YY = np.meshgrid(xs, ys)
    ZZ = XX + YY
    axR.imshow(ZZ, extent=(0, 1, 0, 1), origin="lower", cmap="Oranges",
               alpha=0.85, aspect="auto")
    axR.add_patch(Rectangle((0, 0), 1, 1, fill=False, edgecolor=INK, lw=1.6))

    # a sub-region A footprint (here A = {x<0.5, y<0.5}) outlined.
    axR.add_patch(Rectangle((0, 0), 0.5, 0.5, fill=False, edgecolor=KANTO_GREEN,
                            lw=2.2, ls="--"))
    axR.text(0.25, 0.25, "$A$", ha="center", va="center", fontsize=13,
             color=KANTO_GREEN, fontweight="bold")
    axR.annotate(r"$P((X,Y)\in A)=\iint_A f\,dx\,dy$",
                 xy=(0.5, 0.5), xytext=(0.62, 0.92), fontsize=10, color=INK,
                 arrowprops=dict(arrowstyle="->", color=KANTO_GREEN, lw=1.6))
    axR.text(0.5, -0.10, "$x$ (power)", ha="center", fontsize=10, color=INK)
    axR.text(-0.10, 0.5, "$y$ (stability)", va="center", rotation=90,
             fontsize=10, color=INK)
    axR.text(0.5, 1.14, "lighter = lower density, darker = higher", ha="center",
             fontsize=8.5, style="italic", color=INK)

    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return save(fig, "ch14_joint_grid")


# --------------------------------------------------------------------------
# 2. ch14_region_integral — the burnt-edge triangle (the load-bearing skill).
#    Left: inner limit 0->y at a fixed y. Right: true sub-triangle vs. trap square.
# --------------------------------------------------------------------------
def fig_region_integral():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(12.6, 5.8))
    fig.suptitle("The burnt edge sets the inner limit: support $0<x<y<1$, "
                 "$f(x,y)=8xy$", fontsize=13.5)

    def base(ax, title):
        _blank(ax)
        ax.set_xlim(-0.18, 1.18)
        ax.set_ylim(-0.18, 1.18)
        ax.set_title(title, fontsize=11)
        # unit square frame + diagonal edge x=y
        ax.add_patch(Rectangle((0, 0), 1, 1, fill=False, edgecolor=KANTO_GRAY,
                               lw=1.0, ls=":"))
        ax.plot([0, 1], [0, 1], color=KANTO_RED, lw=2.2, zorder=4)
        ax.text(0.82, 0.93, "edge $x=y$", color=KANTO_RED, fontsize=9.5,
                rotation=45, ha="center", va="center", fontweight="bold")
        ax.text(0.5, -0.12, "$x$ (power)", ha="center", fontsize=10, color=INK)
        ax.text(-0.12, 0.5, "$y$ (stability)", va="center", rotation=90,
                fontsize=10, color=INK)

    # LEFT: the full triangular support + inner-limit arrow at a fixed y.
    base(axL, "Inner integral in $x$ runs $0 \\to y$")
    tri = Polygon([(0, 0), (0, 1), (1, 1)], closed=True, facecolor=FIRE,
                  edgecolor=INK, lw=1.3, alpha=0.30, hatch="..", zorder=2)
    axL.add_patch(tri)
    # fixed-y inner sweep arrow.
    y0 = 0.62
    axL.add_patch(FancyArrowPatch((0.0, y0), (y0, y0), arrowstyle="->",
                                  mutation_scale=16, color=KANTO_GREEN, lw=2.4,
                                  zorder=5))
    axL.plot([0, 1], [y0, y0], color=KANTO_GREEN, lw=0.8, ls="--", zorder=3)
    axL.text(y0 / 2, y0 + 0.05, "sweep $x:0\\to y$", ha="center", fontsize=9.5,
             color=KANTO_GREEN, fontweight="bold")
    axL.text(-0.04, y0, "$y$", ha="right", va="center", fontsize=10,
             color=KANTO_GREEN, fontweight="bold")
    axL.text(0.30, 0.86,
             r"$\int_0^1\!\!\int_0^y 8xy\,dx\,dy$" + "\n" +
             r"$=\int_0^1\!\!\int_x^1 8xy\,dy\,dx$",
             ha="center", va="center", fontsize=10, color=INK,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=FIRE, lw=1.3))

    # RIGHT: true sub-triangle for "both < 1/2" vs. the trap square.
    base(axR, "'Both $<\\frac{1}{2}$' is a sub-triangle, NOT the square")
    # faint full support
    axR.add_patch(Polygon([(0, 0), (0, 1), (1, 1)], closed=True,
                          facecolor=KANTO_GRAY, edgecolor="none", alpha=0.12,
                          zorder=1))
    # trap square (dashed) 0<x<1/2, 0<y<1/2
    axR.add_patch(Rectangle((0, 0), 0.5, 0.5, fill=False, edgecolor=KANTO_BLUE,
                            lw=2.0, ls="--", zorder=3))
    axR.text(0.37, 0.13, "trap\nsquare\n$=\\frac{1}{8}$", ha="center", va="center",
             fontsize=8.5, color=KANTO_BLUE, fontweight="bold")
    # true sub-triangle 0<x<y<1/2 (above diagonal, below y=1/2)
    axR.add_patch(Polygon([(0, 0), (0, 0.5), (0.5, 0.5)], closed=True,
                          facecolor=KANTO_GREEN, edgecolor=INK, lw=1.4,
                          alpha=0.55, hatch="//", zorder=4))
    axR.text(0.12, 0.34, "true\n$=\\frac{1}{16}$", ha="center", va="center",
             fontsize=9.5, color=INK, fontweight="bold", zorder=5)
    axR.text(0.5, 1.06,
             r"square wrongly includes the forbidden half $x>y$",
             ha="center", fontsize=8.8, style="italic", color=KANTO_BLUE)

    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return save(fig, "ch14_region_integral")


# --------------------------------------------------------------------------
# 3. ch14_marginal — integrate out a variable over a triangle; strip collapses.
#    Concept 2 / Beat 8: marginal of Y = shadow of the strip; f_Y(y)=4y^3.
# --------------------------------------------------------------------------
def fig_marginal():
    fig, ax = plt.subplots(figsize=(8.6, 6.4))
    _blank(ax)
    ax.set_title("Marginal of $Y$: at height $y$, sweep $x:0\\to y$\n"
                 "the strip collapses to $f_Y(y)=4y^3$", fontsize=12)
    ax.set_xlim(-0.22, 1.55)
    ax.set_ylim(-0.18, 1.18)

    # support triangle 0<x<y<1
    ax.add_patch(Rectangle((0, 0), 1, 1, fill=False, edgecolor=KANTO_GRAY,
                           lw=1.0, ls=":"))
    ax.add_patch(Polygon([(0, 0), (0, 1), (1, 1)], closed=True, facecolor=FIRE,
                         edgecolor=INK, lw=1.3, alpha=0.28, hatch="..", zorder=2))
    ax.plot([0, 1], [0, 1], color=KANTO_RED, lw=2.2, zorder=4)
    ax.text(0.84, 0.94, "edge $x=y$", color=KANTO_RED, fontsize=9.5,
            rotation=45, ha="center", va="center", fontweight="bold")

    # a sample strip at fixed y.
    y0 = 0.7
    ax.add_patch(FancyArrowPatch((0.0, y0), (y0, y0), arrowstyle="->",
                                 mutation_scale=16, color=KANTO_GREEN, lw=2.6,
                                 zorder=5))
    ax.plot([0, 1], [y0, y0], color=KANTO_GREEN, lw=0.7, ls="--", zorder=3)
    ax.text(y0 / 2, y0 + 0.05, "$x:0\\to y$", ha="center", fontsize=10,
            color=KANTO_GREEN, fontweight="bold")
    ax.text(-0.05, y0, "$y$", ha="right", va="center", fontsize=11,
            color=KANTO_GREEN, fontweight="bold")
    ax.text(0.5, -0.12, "$x$", ha="center", fontsize=11, color=INK)
    ax.text(-0.13, 0.5, "$y$", va="center", fontsize=11, color=INK)

    # collapsed marginal f_Y(y)=4y^3 drawn to the right of the square.
    yy = np.linspace(0, 1, 100)
    fy = 4 * yy ** 3
    fy_scaled = 1.15 + fy / 4.0 * 0.35  # map [0,4] -> [1.15, ~1.5]
    ax.plot(fy_scaled, yy, color=KANTO_BLUE, lw=2.4, zorder=4)
    ax.fill_betweenx(yy, 1.15, fy_scaled, color=KANTO_BLUE, alpha=0.20, zorder=2)
    ax.plot([1.15, 1.15], [0, 1], color=INK, lw=0.8)
    ax.text(1.5, 0.55, "$f_Y(y)=4y^3$", color=KANTO_BLUE, fontsize=10.5,
            rotation=90, ha="center", va="center", fontweight="bold")
    ax.annotate("", xy=(1.16, y0), xytext=(0.78, y0),
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4, ls="-"))
    ax.text(0.97, y0 + 0.05, "collapse", ha="center", fontsize=8.5,
            style="italic", color=INK)

    fig.tight_layout()
    return save(fig, "ch14_marginal")


# --------------------------------------------------------------------------
# 4. ch14_conditional_slice — slice the joint at X=x, rescale by f_X(x).
#    Concept 4 / Beat 8: the slice is not a density; divide by f_X to fix it.
# --------------------------------------------------------------------------
def fig_conditional_slice():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(12.4, 5.6))
    fig.suptitle("Condition on $X=x$: slice the joint, then rescale by "
                 "$f_X(x)$ so it integrates to 1", fontsize=13.5)

    # joint f(x,y)=x+y on unit square; slice at x0.
    x0 = 0.5
    yy = np.linspace(0, 1, 100)

    # LEFT: the unit square with the vertical slice drawn at x0.
    _blank(axL)
    axL.set_xlim(-0.15, 1.25)
    axL.set_ylim(-0.15, 1.25)
    axL.set_title("Raw slice at $X=0.5$: $f(0.5,y)=\\frac{1}{2}+y$ "
                  "(not yet a density)", fontsize=10.5)
    n = 200
    XX, YY = np.meshgrid(np.linspace(0, 1, n), np.linspace(0, 1, n))
    axL.imshow(XX + YY, extent=(0, 1, 0, 1), origin="lower", cmap="Oranges",
               alpha=0.8, aspect="auto")
    axL.add_patch(Rectangle((0, 0), 1, 1, fill=False, edgecolor=INK, lw=1.5))
    axL.axvline(x0, color=KANTO_GREEN, lw=2.6, zorder=4)
    axL.text(x0 + 0.02, 1.08, f"slice $X={x0}$", color=KANTO_GREEN, fontsize=9.5,
             ha="left", fontweight="bold")
    axL.text(0.5, -0.10, "$x$ (power)", ha="center", fontsize=10, color=INK)
    axL.text(-0.10, 0.5, "$y$ (stability)", va="center", rotation=90,
             fontsize=10, color=INK)

    # RIGHT: the slice profile, raw vs. rescaled conditional.
    _blank(axR)
    axR.set_title("Divide by $f_X(\\frac{1}{2})=1$: conditional "
                  "$f_{Y|X}(y|\\frac{1}{2})=\\frac{1}{2}+y$", fontsize=10.5)
    raw = 0.5 + yy           # f(0.5, y) = 1/2 + y
    fx = 1.0                 # f_X(0.5) = 0.5 + 0.5 = 1
    cond = raw / fx          # equals raw here (clean demo)
    axR.set_xlim(-0.1, 1.1)
    axR.set_ylim(-0.1, 1.9)
    axR.plot(yy, raw, color=KANTO_GRAY, lw=2.2, ls="--",
             label=r"raw slice $f(\frac{1}{2},y)$")
    axR.plot(yy, cond, color=KANTO_BLUE, lw=2.6,
             label=r"conditional $f_{Y|X}(y|\frac{1}{2})$")
    axR.fill_between(yy, 0, cond, color=KANTO_BLUE, alpha=0.18)
    axR.axhline(0, color=INK, lw=0.8)
    axR.axvline(0, color=INK, lw=0.8)
    axR.text(0.5, -0.05, "$y$", ha="center", fontsize=11, color=INK)
    axR.text(0.5, 1.72,
             r"area under the conditional $=\int_0^1(\frac{1}{2}+y)\,dy=1$ "
             r"$\checkmark$", ha="center", fontsize=9.5, color=KANTO_GREEN,
             fontweight="bold")
    axR.legend(loc="upper left", fontsize=8.5, frameon=True)

    # decorative Mewtwo in the right-panel top-right margin (clear of curves).
    place_sprite(axR, front(150), (0.95, 1.45), zoom=0.22, alpha=0.9, zorder=6)

    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return save(fig, "ch14_conditional_slice")


REGISTRY = [
    fig_joint_grid,
    fig_region_integral,
    fig_marginal,
    fig_conditional_slice,
]


def main() -> None:
    print(f"Generating Chapter 14 (Joint Distributions) figures -> {OUT} "
          f"at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
