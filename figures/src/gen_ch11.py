#!/usr/bin/env python3
"""Generate every Chapter 11 (Joint Distributions / Cinnabar / Blaine) math figure.

The chapter's nine-beat arcs each end on a "Picture it" beat whose <figure>
needs a diagram of the triangular mansion-log support 0 < x < y < 1. Previously
all five figure blocks pointed at the single static ch09_joint_region.png, whose
two fixed panels could not show the five DISTINCT pictures the alt texts promise
(inner-limit sweep, marginal shadow, conditional vertical slice, independence
contrast, and the "both below 1/2" sub-triangle footprint). This script renders
one purpose-built PNG per figure so picture and caption agree:

  ch11_support_volume         Beat 8 of Concept 1: support 0<x<y<1 + the
                              sub-triangle footprint of P(X<1/2, Y<1/2)
  ch11_marginal_shadow        Beat 8 of Concept 2: marginal of Y as a horizontal
                              sweep x: 0 -> edge x=y (inner limit y, not 1)
  ch11_inner_limit            Beat 8 of Concept 3: inner integral 0->y (left)
                              and the both-below-1/2 sub-triangle (right)
  ch11_conditional_slice      Beat 8 of Concept 4: vertical slice at X=x,
                              rescaled by 1/f_X(x) into a genuine density of Y
  ch11_independence_contrast  Beat 8 of Concept 5: slanted edge x=y (dependence)
                              vs a clean rectangular box (independence possible)

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette, every color-coded element
ALSO carries a hatch / label, so the figures stay legible in grayscale.

Run: python figures/src/gen_ch11.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyArrowPatch
from cycler import cycler

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
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


def _unit_axes(ax, title=None):
    """A clean unit-square drawing surface with light x/y axes from 0 to 1."""
    ax.set_xlim(-0.08, 1.12)
    ax.set_ylim(-0.08, 1.12)
    ax.set_aspect("equal")
    ax.grid(False)
    ax.set_facecolor("white")
    for s in ax.spines.values():
        s.set_visible(False)
    # light axes through the origin
    ax.annotate("", xy=(1.12, 0), xytext=(-0.04, 0),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))
    ax.annotate("", xy=(0, 1.12), xytext=(0, -0.04),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))
    ax.text(1.13, -0.02, "$x$", fontsize=13, va="top", ha="left", color=INK)
    ax.text(-0.02, 1.14, "$y$", fontsize=13, va="bottom", ha="right", color=INK)
    for v in (0.5, 1.0):
        ax.plot([v, v], [-0.015, 0.015], color=INK, lw=1.2)
        ax.plot([-0.015, 0.015], [v, v], color=INK, lw=1.2)
        ax.text(v, -0.055, ("$\\frac{1}{2}$" if v == 0.5 else "$1$"),
                ha="center", va="top", fontsize=11, color=INK)
        ax.text(-0.045, v, ("$\\frac{1}{2}$" if v == 0.5 else "$1$"),
                ha="right", va="center", fontsize=11, color=INK)
    ax.set_xticks([])
    ax.set_yticks([])
    if title:
        ax.set_title(title, fontsize=13)


# The big triangle 0 < x < y < 1: vertices (0,0), (0,1), (1,1).
TRI = [(0, 0), (0, 1), (1, 1)]
# The sub-triangle 0 < x < y < 1/2: vertices (0,0), (0,1/2), (1/2,1/2).
SUBTRI = [(0, 0), (0, 0.5), (0.5, 0.5)]


def _draw_triangle(ax, color=KANTO_BLUE, alpha=0.30, hatch=None, label=True):
    ax.add_patch(Polygon(TRI, closed=True, facecolor=color, edgecolor="none",
                         alpha=alpha, hatch=hatch))
    # the slanted edge x = y, drawn boldly because it is the load-bearing fact
    ax.plot([0, 1], [0, 1], color=INK, lw=2.2)
    ax.plot([0, 0], [0, 1], color=INK, lw=1.6)   # left edge x = 0
    ax.plot([0, 1], [1, 1], color=INK, lw=1.6)   # top edge y = 1
    if label:
        ax.text(0.22, 0.74, "$0<x<y<1$", fontsize=12, color=INK,
                rotation=0, ha="center", fontweight="bold")
        ax.text(0.62, 0.50, "$x=y$", fontsize=11, color=INK, rotation=45,
                ha="center", va="center")


# --------------------------------------------------------------------------
# 1. Concept 1, Beat 8: the support + the P(X<1/2, Y<1/2) footprint.
# --------------------------------------------------------------------------
def fig_support_volume():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5.4))
    fig.suptitle("A joint density lives over a region; probability is volume",
                 y=1.00)

    _unit_axes(axL, "The support $0<x<y<1$")
    _draw_triangle(axL, color=KANTO_BLUE, alpha=0.32, hatch="//")
    # red arrow: for a fixed y, inner x runs 0 -> y
    y0 = 0.72
    axL.add_patch(FancyArrowPatch((0.0, y0), (y0, y0), mutation_scale=18,
                  lw=2.4, color=KANTO_RED))
    axL.plot([0, 1.05], [y0, y0], color=KANTO_RED, lw=0.9, ls=":")
    axL.text(y0 / 2, y0 + 0.045, "$x:0\\to y$", color=KANTO_RED, fontsize=11,
             ha="center", fontweight="bold")
    axL.text(1.02, y0, "fixed $y$", color=KANTO_RED, fontsize=10, va="center")

    _unit_axes(axR, r"Footprint of $P\left(X<\frac{1}{2},\,Y<\frac{1}{2}\right)$")
    # whole triangle in gray, sub-triangle in green
    axR.add_patch(Polygon(TRI, closed=True, facecolor=KANTO_GRAY, alpha=0.22,
                          edgecolor="none"))
    axR.plot([0, 1], [0, 1], color=INK, lw=2.2)
    axR.plot([0, 0], [0, 1], color=INK, lw=1.6)
    axR.plot([0, 1], [1, 1], color=INK, lw=1.6)
    axR.add_patch(Polygon(SUBTRI, closed=True, facecolor=KANTO_GREEN,
                          alpha=0.55, edgecolor=INK, lw=1.6, hatch="xx"))
    axR.text(0.14, 0.33, "$0<x<y<\\frac{1}{2}$", fontsize=10.5, color=INK,
             ha="center", fontweight="bold")
    axR.plot([0, 0.5], [0.5, 0.5], color=INK, lw=1.0, ls="--")
    axR.plot([0.5, 0.5], [0, 0.5], color=INK, lw=1.0, ls="--")

    fig.tight_layout()
    return save(fig, "ch11_support_volume")


# --------------------------------------------------------------------------
# 2. Concept 2, Beat 8: marginal of Y as a horizontal shadow sweep.
# --------------------------------------------------------------------------
def fig_marginal_shadow():
    fig, ax = plt.subplots(figsize=(6.4, 6.0))
    fig.suptitle("Marginal of $Y$: sweep $x$ from $0$ to the edge $x=y$", y=0.98)
    _unit_axes(ax)
    _draw_triangle(ax, color=KANTO_BLUE, alpha=0.30, hatch="//")

    for y0 in (0.35, 0.6, 0.85):
        ax.add_patch(FancyArrowPatch((0.0, y0), (y0, y0), mutation_scale=16,
                     lw=2.2, color=KANTO_RED))
        ax.plot([y0, 1.05], [y0, y0], color=KANTO_RED, lw=0.8, ls=":")
    ax.text(0.30, 0.6 + 0.045, "$x:\\,0\\to y$", color=KANTO_RED, fontsize=11.5,
            ha="center", fontweight="bold")
    ax.annotate("inner limit is $y$,\nnot $1$",
                xy=(0.85, 0.85), xytext=(1.0, 0.62),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.3),
                fontsize=10.5, color=INK, ha="center",
                bbox=dict(boxstyle="round,pad=0.3", fc="#FFF6D6",
                          ec=KANTO_YEL, lw=1.3))
    fig.tight_layout()
    return save(fig, "ch11_marginal_shadow")


# --------------------------------------------------------------------------
# 3. Concept 3, Beat 8: inner-limit sweep (left) + both-below-1/2 (right).
# --------------------------------------------------------------------------
def fig_inner_limit():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5.4))
    fig.suptitle("Sketch the region before writing limits", y=1.00)

    _unit_axes(axL, "Inner integral in $x$: $0\\to y$")
    _draw_triangle(axL, color=KANTO_BLUE, alpha=0.30, hatch="//")
    y0 = 0.66
    axL.add_patch(FancyArrowPatch((0.0, y0), (y0, y0), mutation_scale=18,
                  lw=2.6, color=KANTO_RED))
    axL.plot([0, 1.05], [y0, y0], color=KANTO_RED, lw=0.9, ls=":")
    axL.text(y0 / 2, y0 + 0.05, "$0\\to y$", color=KANTO_RED, fontsize=12,
             ha="center", fontweight="bold")
    axL.text(0.78, 0.66, "edge $x=y$\ncaps it", color=INK, fontsize=10,
             va="center")

    _unit_axes(axR, r"Footprint of ``both below $\frac{1}{2}$''")
    axR.add_patch(Polygon(TRI, closed=True, facecolor=KANTO_GRAY, alpha=0.22,
                          edgecolor="none"))
    axR.plot([0, 1], [0, 1], color=INK, lw=2.2)
    axR.plot([0, 0], [0, 1], color=INK, lw=1.6)
    axR.plot([0, 1], [1, 1], color=INK, lw=1.6)
    axR.add_patch(Polygon(SUBTRI, closed=True, facecolor=KANTO_GREEN,
                          alpha=0.55, edgecolor=INK, lw=1.6, hatch="xx"))
    axR.text(0.155, 0.32, "$0<x<y<\\frac{1}{2}$", fontsize=10.5, color=INK,
             ha="center", fontweight="bold")
    axR.plot([0, 0.5], [0.5, 0.5], color=INK, lw=1.0, ls="--")
    axR.plot([0.5, 0.5], [0, 0.5], color=INK, lw=1.0, ls="--")
    axR.text(0.78, 0.18, "not the\nsquare!", color=KANTO_RED, fontsize=10.5,
             ha="center", fontweight="bold")

    fig.tight_layout()
    return save(fig, "ch11_inner_limit")


# --------------------------------------------------------------------------
# 4. Concept 4, Beat 8: vertical slice at X=x, rescaled into a density of Y.
# --------------------------------------------------------------------------
def fig_conditional_slice():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5.2),
                                   gridspec_kw={"width_ratios": [1.05, 1]})
    fig.suptitle(r"Conditioning on $X=x$: slice the joint, then rescale by "
                 r"$1/f_X(x)$", y=1.00)

    # LEFT: the support with a bold vertical slice at a fixed x.
    _unit_axes(axL, "Vertical slice at $X=x$")
    _draw_triangle(axL, color=KANTO_BLUE, alpha=0.28, hatch="//")
    x0 = 0.35
    axL.add_patch(FancyArrowPatch((x0, x0), (x0, 1.0), mutation_scale=18,
                  lw=2.6, color=KANTO_RED))
    axL.plot([x0, x0], [-0.02, 1.05], color=KANTO_RED, lw=0.9, ls=":")
    axL.text(x0, -0.055, "$x$", color=KANTO_RED, ha="center", va="top",
             fontsize=12, fontweight="bold")
    axL.text(x0 + 0.03, 0.72, "$x<y<1$", color=KANTO_RED, fontsize=10.5,
             rotation=90, va="center", fontweight="bold")

    # RIGHT: the slice before/after rescaling -> a proper density of Y.
    axR.set_facecolor("white")
    axR.grid(False)
    for s in ("top", "right"):
        axR.spines[s].set_visible(False)
    yy = np.linspace(x0, 1.0, 200)
    fX = 4 * x0 * (1 - x0 ** 2)          # marginal f_X(x) for f=8xy on triangle
    raw = 8 * x0 * yy                     # the raw joint slice along y
    cond = 2 * yy / (1 - x0 ** 2)         # f_{Y|X}(y|x) = 2y/(1-x^2)
    axR.plot(yy, raw, color=KANTO_GRAY, lw=2.2, ls="--",
             label="raw slice $f(x,y)$")
    axR.fill_between(yy, 0, cond, color=KANTO_GREEN, alpha=0.40, hatch="xx",
                     edgecolor=INK, lw=1.0)
    axR.plot(yy, cond, color=KANTO_GREEN, lw=2.6,
             label=r"$f_{Y|X}(y\,|\,x)=\frac{2y}{1-x^2}$")
    axR.set_xlim(0, 1.05)
    axR.set_ylim(0, max(cond.max(), raw.max()) * 1.18)
    axR.set_xlabel("$y$")
    axR.set_title(r"$\div\,f_X(x)\Rightarrow$ area $=1$", fontsize=12)
    axR.legend(loc="upper left", fontsize=9.5)
    axR.text(0.5, max(cond) * 0.30, "area $=1$", color=INK, fontsize=10,
             ha="center", fontweight="bold")

    fig.tight_layout()
    return save(fig, "ch11_conditional_slice")


# --------------------------------------------------------------------------
# 5. Concept 5, Beat 8: slanted edge (dependence) vs rectangle (independence).
# --------------------------------------------------------------------------
def fig_independence_contrast():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5.4))
    fig.suptitle("The shape of the support tells you if independence is even "
                 "possible", y=1.00)

    _unit_axes(axL, "Triangle: range of $X$ depends on $Y$")
    _draw_triangle(axL, color=KANTO_RED, alpha=0.22, hatch="\\\\", label=False)
    axL.plot([0, 1], [0, 1], color=KANTO_RED, lw=3.0)
    axL.text(0.60, 0.46, "$x=y$", fontsize=12, color=KANTO_RED, rotation=45,
             ha="center", va="center", fontweight="bold")
    axL.annotate("slanted edge\n$\\Rightarrow$ DEPENDENT",
                 xy=(0.5, 0.5), xytext=(0.30, 0.88),
                 arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.3),
                 fontsize=10.5, color=INK, ha="center",
                 bbox=dict(boxstyle="round,pad=0.3", fc="#FFE0E0",
                           ec=KANTO_RED, lw=1.3))

    _unit_axes(axR, "Box: independence is at least possible")
    axR.add_patch(Rectangle((0, 0), 1, 1, facecolor=KANTO_GREEN, alpha=0.22,
                            edgecolor=INK, lw=2.2, hatch="//"))
    axR.text(0.5, 0.5, "rectangular\nsupport", fontsize=12, color=INK,
             ha="center", va="center", fontweight="bold")
    axR.annotate("no constraint\nbetween $x,y$",
                 xy=(0.5, 0.0), xytext=(0.5, -0.0 - 0.0),
                 fontsize=1, color="white")  # spacer-free
    axR.text(0.5, 1.045,
             "independent $\\Leftrightarrow$ $f$ also factors",
             fontsize=10, color=INK, ha="center",
             bbox=dict(boxstyle="round,pad=0.3", fc="#DFF5E1",
                       ec=KANTO_GREEN, lw=1.3))

    fig.tight_layout()
    return save(fig, "ch11_independence_contrast")


REGISTRY = [
    fig_support_volume,
    fig_marginal_shadow,
    fig_inner_limit,
    fig_conditional_slice,
    fig_independence_contrast,
]


def main() -> None:
    print(f"Generating Chapter 11 (Joint) figures -> {OUT} at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
