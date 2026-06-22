#!/usr/bin/env python3
"""Generate every Chapter 17 (Order Statistics / Indigo Plateau / Elite Four /
Ice type) figure.

Manifest (DESIGN_BLUEPRINT ch17 row · MASTER_PLAN_V3 §16, §19, §30) — three
diagrams into assets/diagrams/:
  ch17_order_max_min   the bracket: max-cdf [F]^n piles toward the ceiling, the
                       min-survival [S]^n drops toward the floor; both built by
                       multiplying independence (Lapras #131)
  ch17_kth_order       the k-th order statistic — one draw AT x, k-1 below,
                       n-k above; the sorted-dot strip and the Beta(k,n-k+1)
                       density of X_(k) for i.i.d. Unif(0,1) (Lapras #131)
  ch17_reliability_series_parallel  reliability as order statistics: a SERIES
                       chain dies with the MINIMUM (weakest link), a PARALLEL
                       bank survives to the MAXIMUM (last backup)

PRINT TARGET: bound book, every PNG rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is
ALSO distinguished by a hatch pattern / text label so figures survive grayscale.
Real sprites obey the IRON RULE: art lives in margins / atop bars / beside labels,
never over a curve, equation, axis, or number a reader must read. Sprite art is
REAL (assets/sprites/front/*.png) and is only ever COMPOSITED, never generated.

Run: python3 figures/src/gen_ch17.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from cycler import cycler
from scipy import stats

from sprite_util import front, place_sprite
from type_palette import chapter_accent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents). ch17 = Ice type (Elite Four),
# so the accent is the §17 ice color via chapter_accent(17).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
ACCENT = chapter_accent(17)  # ice #98D8D8
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


def _clean(ax):
    ax.set_facecolor("white")
    ax.grid(False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


# --------------------------------------------------------------------------
# 1. ch17_order_max_min — the bracket: max-cdf [F]^n vs min-survival [S]^n.
#    (Concepts 1 & 2)
# --------------------------------------------------------------------------
def fig_order_max_min():
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.8))
    x = np.linspace(0.0, 1.0, 600)
    ns = [(1, KANTO_GRAY, ":", "n=1 (one draw)"),
          (3, KANTO_BLUE, "--", "n=3"),
          (8, KANTO_RED, "-", "n=8 (the field)")]

    # Left: cdf of the MAXIMUM, F_max(x) = [F(x)]^n, F(x)=x on Unif(0,1).
    axL = axes[0]
    _clean(axL)
    for n, color, ls, lab in ns:
        axL.plot(x, x ** n, color=color, lw=2.6, ls=ls, zorder=5, label=lab)
    # Shade the region for "max <= 0.8" at n=8 to show how rare a small max is.
    axL.axvline(0.8, color=KANTO_GREEN, lw=1.2, ls=":", zorder=3)
    axL.plot([0.8], [0.8 ** 8], "o", color=KANTO_RED, ms=7, zorder=6)
    axL.annotate(r"$F_{\max}(0.8)=0.8^{8}\approx0.17$",
                 xy=(0.8, 0.8 ** 8), xytext=(0.30, 0.62), ha="center",
                 fontsize=10.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.4),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_RED,
                           lw=1.2))
    axL.set_title(r"MAXIMUM: $F_{\max}(x)=[F(x)]^{n}$" "\n"
                  r"all $n$ below $x$ $\Rightarrow$ raise the cdf",
                  fontsize=12)
    axL.set_xlabel(r"strength $x$  (single-draw cdf $F(x)=x$)", fontsize=10)
    axL.set_ylabel(r"$P(\max\leq x)$", fontsize=10)
    axL.set_xlim(0, 1)
    axL.set_ylim(0, 1.04)
    axL.legend(loc="upper left", fontsize=9, frameon=True)

    # Right: survival of the MINIMUM, S_min(x) = [S(x)]^n, S(x)=1-x on Unif(0,1).
    axR = axes[1]
    _clean(axR)
    for n, color, ls, lab in ns:
        axR.plot(x, (1 - x) ** n, color=color, lw=2.6, ls=ls, zorder=5,
                 label=lab)
    axR.axvline(0.2, color=KANTO_GREEN, lw=1.2, ls=":", zorder=3)
    axR.plot([0.2], [(1 - 0.2) ** 8], "o", color=KANTO_RED, ms=7, zorder=6)
    axR.annotate(r"$S_{\min}(0.2)=0.8^{8}\approx0.17$",
                 xy=(0.2, (1 - 0.2) ** 8), xytext=(0.62, 0.62), ha="center",
                 fontsize=10.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.4),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_RED,
                           lw=1.2))
    axR.set_title(r"MINIMUM: $S_{\min}(x)=[S(x)]^{n}$" "\n"
                  r"all $n$ above $x$ $\Rightarrow$ raise the survival",
                  fontsize=12)
    axR.set_xlabel(r"strength $x$  (single-draw survival $S(x)=1-x$)",
                   fontsize=10)
    axR.set_ylabel(r"$P(\min> x)$", fontsize=10)
    axR.set_xlim(0, 1)
    axR.set_ylim(0, 1.04)
    axR.legend(loc="upper right", fontsize=9, frameon=True)

    fig.suptitle("The bracket: the strongest of many ($\\max$) and the first to "
                 "fall ($\\min$), both from independence\n"
                 r"$X_i\sim\mathrm{Unif}(0,1)$ i.i.d. — more challengers push the "
                 r"max to the ceiling and the min to the floor",
                 fontsize=12.5, y=1.04)

    # Real Lapras sprite (the Elite-Four ice mascot) in the left panel's clear
    # lower-right corner, where every max-cdf curve is still near 0.
    place_sprite(axL, front(131), (0.30, 0.14), zoom=0.40, alpha=0.95, zorder=6)
    axL.text(0.30, 0.025, "#131 Lapras", ha="center", fontsize=8, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return save(fig, "ch17_order_max_min")


# --------------------------------------------------------------------------
# 2. ch17_kth_order — the k-th order statistic. (Concept 4)
# --------------------------------------------------------------------------
def fig_kth_order():
    fig, axes = plt.subplots(2, 1, figsize=(11, 7.4),
                             gridspec_kw={"height_ratios": [1, 2.6]})

    # Top strip: n=4 sorted dots on [0,1], the k=2 dot (second-lowest) circled.
    axT = axes[0]
    axT.set_xlim(0, 1)
    axT.set_ylim(0, 1)
    axT.axis("off")
    axT.axhline(0.5, color=KANTO_GRAY, lw=1.4, zorder=1)
    positions = [0.14, 0.36, 0.63, 0.88]  # an example sorted sample
    labels = [r"$X_{(1)}$", r"$X_{(2)}$", r"$X_{(3)}$", r"$X_{(4)}$"]
    for i, (px, lab) in enumerate(zip(positions, labels)):
        is_k = (i == 1)  # k = 2
        axT.plot([px], [0.5], "o", ms=15 if is_k else 11,
                 color=KANTO_RED if is_k else KANTO_BLUE,
                 zorder=5, mec=INK, mew=1.0)
        axT.text(px, 0.86, lab, ha="center", fontsize=10.5,
                 color=KANTO_RED if is_k else INK,
                 fontweight="bold" if is_k else "normal")
    # Bracket the k-1 below and n-k above the k=2 dot.
    axT.annotate("", xy=(0.02, 0.18), xytext=(0.30, 0.18),
                 arrowprops=dict(arrowstyle="<->", color=KANTO_GRAY, lw=1.1))
    axT.text(0.16, 0.04, r"$k-1=1$ below", ha="center", fontsize=9, color=INK)
    axT.annotate("", xy=(0.42, 0.18), xytext=(0.98, 0.18),
                 arrowprops=dict(arrowstyle="<->", color=KANTO_GRAY, lw=1.1))
    axT.text(0.70, 0.04, r"$n-k=2$ above", ha="center", fontsize=9, color=INK)
    axT.set_title(r"Sort $n=4$ draws; the $k=2$ order statistic $X_{(2)}$ is the "
                  r"second-lowest (one AT $x$, $k{-}1$ below, $n{-}k$ above)",
                  fontsize=11.5)

    # Bottom: the density of X_(k) for i.i.d. Unif(0,1) = Beta(k, n-k+1).
    axB = axes[1]
    _clean(axB)
    x = np.linspace(0.0001, 0.9999, 700)
    n = 4
    ks = [(1, KANTO_GREEN, "....", r"$k=1$ (min), $\mathrm{Beta}(1,4)$, mean $\frac{1}{5}$"),
          (2, KANTO_RED, "//", r"$k=2$, $\mathrm{Beta}(2,3)$, mean $\frac{2}{5}$"),
          (3, KANTO_BLUE, "xx", r"$k=3$, $\mathrm{Beta}(3,2)$, mean $\frac{3}{5}$"),
          (4, KANTO_YEL, "\\\\", r"$k=4$ (max), $\mathrm{Beta}(4,1)$, mean $\frac{4}{5}$")]
    for k, color, hatch, lab in ks:
        y = stats.beta.pdf(x, k, n - k + 1)
        axB.plot(x, y, color=color, lw=2.6, zorder=5, label=lab)
        axB.fill_between(x, y, color=color, alpha=0.12, hatch=hatch,
                         edgecolor=color, lw=0.0, zorder=2)
    # Mark the k=2 mean at 2/5 = 0.4 (matches the strip above).
    axB.axvline(0.4, color=KANTO_RED, lw=1.2, ls=":", zorder=3)
    axB.text(0.205, 1.95, r"$E[X_{(2)}]=\frac{k}{n+1}=\frac{2}{5}=0.4$",
             ha="center", color=KANTO_RED, fontsize=10, zorder=7,
             bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=KANTO_RED,
                       lw=1.0))
    axB.set_title(r"Density of the $k$-th order statistic of $n=4$ i.i.d. "
                  r"$\mathrm{Unif}(0,1)$ draws: $X_{(k)}\sim\mathrm{Beta}(k,\,n-k+1)$,"
                  r" mean $\frac{k}{n+1}$",
                  fontsize=11.5)
    axB.set_xlabel(r"value $x$", fontsize=10)
    axB.set_yticks([])
    axB.set_xlim(0, 1)
    axB.set_ylim(0, 3.0)
    axB.legend(loc="upper right", fontsize=8.5, frameon=True, ncol=1)

    # Real Lapras sprite low-left, clear of the k=1 curve which rises on the left;
    # placed at the very floor where all densities have small value.
    place_sprite(axB, front(131), (0.085, 0.40), zoom=0.34, alpha=0.95, zorder=6)
    axB.text(0.085, 0.075, "#131 Lapras", ha="center", fontsize=8, color=INK)
    fig.tight_layout()
    return save(fig, "ch17_kth_order")


# --------------------------------------------------------------------------
# 3. ch17_reliability_series_parallel — reliability as min/max. (Concept 5)
# --------------------------------------------------------------------------
def fig_reliability():
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.4))

    def _box(ax, xy, w, h, label, color):
        ax.add_patch(FancyBboxPatch(xy, w, h,
                     boxstyle="round,pad=0.012,rounding_size=0.02",
                     facecolor=color, alpha=0.30, edgecolor=color, lw=2.0,
                     zorder=3))
        ax.text(xy[0] + w / 2, xy[1] + h / 2, label, ha="center", va="center",
                fontsize=10, color=INK, zorder=4)

    # Left: SERIES chain — all in a line; fails when the FIRST dies => min.
    axL = axes[0]
    axL.set_xlim(0, 1)
    axL.set_ylim(0, 1)
    axL.axis("off")
    ys = 0.58
    axL.plot([0.02, 0.10], [ys + 0.06, ys + 0.06], color=INK, lw=1.6, zorder=2)
    xs = [0.10, 0.40, 0.70]
    for i, x0 in enumerate(xs):
        _box(axL, (x0, ys), 0.20, 0.12, f"$0.9$\ncomp {i+1}", KANTO_BLUE)
        if i < 2:
            axL.plot([x0 + 0.20, x0 + 0.30], [ys + 0.06, ys + 0.06],
                     color=INK, lw=1.6, zorder=2)
    axL.plot([0.90, 0.98], [ys + 0.06, ys + 0.06], color=INK, lw=1.6, zorder=2)
    axL.text(0.5, 0.40, r"lifetime $=\min_i X_i$  (weakest link)",
             ha="center", fontsize=11, color=KANTO_RED, fontweight="bold")
    axL.text(0.5, 0.27,
             r"$R_{\mathrm{series}}=\prod_i S_i(t)=0.9^3=0.729$",
             ha="center", fontsize=11, color=INK,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_RED,
                       lw=1.2))
    axL.set_title("SERIES — all must work; fails when the FIRST fails",
                  fontsize=12)

    # Right: PARALLEL bank — three branches; survives while ANY works => max.
    axR = axes[1]
    axR.set_xlim(0, 1)
    axR.set_ylim(0, 1)
    axR.axis("off")
    branch_y = [0.74, 0.52, 0.30]
    axR.plot([0.10, 0.10], [branch_y[-1] + 0.06, branch_y[0] + 0.06],
             color=INK, lw=1.6, zorder=2)
    axR.plot([0.90, 0.90], [branch_y[-1] + 0.06, branch_y[0] + 0.06],
             color=INK, lw=1.6, zorder=2)
    axR.plot([0.02, 0.10], [0.52 + 0.06, 0.52 + 0.06], color=INK, lw=1.6)
    axR.plot([0.90, 0.98], [0.52 + 0.06, 0.52 + 0.06], color=INK, lw=1.6)
    for i, by in enumerate(branch_y):
        axR.plot([0.10, 0.34], [by + 0.06, by + 0.06], color=INK, lw=1.6,
                 zorder=2)
        axR.plot([0.66, 0.90], [by + 0.06, by + 0.06], color=INK, lw=1.6,
                 zorder=2)
        _box(axR, (0.34, by), 0.32, 0.12, f"$0.9$  comp {i+1}", KANTO_GREEN)
    axR.text(0.5, 0.16, r"lifetime $=\max_i X_i$  (last backup standing)",
             ha="center", fontsize=11, color=KANTO_RED, fontweight="bold")
    axR.text(0.5, 0.03,
             r"$R_{\mathrm{parallel}}=1-\prod_i F_i(t)=1-0.1^3=0.999$",
             ha="center", fontsize=11, color=INK,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_RED,
                       lw=1.2))
    axR.set_title("PARALLEL — any one suffices; fails when the LAST dies",
                  fontsize=12)

    fig.suptitle("Reliability is an order-statistic question: a chain dies with "
                 "the MINIMUM, a redundant bank survives to the MAXIMUM",
                 fontsize=12.5, y=1.02)

    # Real Lapras sprite in the right panel's clear upper-right margin.
    place_sprite(axR, front(131), (0.07, 0.92), zoom=0.30, alpha=0.95,
                 xycoords="axes fraction", zorder=6)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    return save(fig, "ch17_reliability_series_parallel")


REGISTRY = [
    fig_order_max_min,
    fig_kth_order,
    fig_reliability,
]


def main() -> None:
    print(f"Generating Chapter 17 (Order Statistics) figures -> "
          f"{OUT} at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
