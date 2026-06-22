#!/usr/bin/env python3
"""Generate every Chapter 10 (Continuous Moments / Saffron — Silph Co. /
Sabrina arc / Psychic type) figure.

Manifest (DESIGN_BLUEPRINT ch10 row · MASTER_PLAN_V3 §16, §19, §30) — two
diagrams into assets/diagrams/:
  ch10_continuous_moments   E[X] = int x f(x) dx as the BALANCE POINT (center of
                            mass) of a continuous density; the rare heavy upper
                            tail tugs the fulcrum right of the peak. The discrete
                            bars of ch03 melt into a smooth curve (Kadabra/psychic
                            margin sprite #64).
  ch10_survival_integral    the continuous Darth-Vader twin: E[X] = int_0^inf S(x) dx
                            is the AREA under the survival curve. Composite
                            Mr. Mime #122 (the barrier/mime that "props up" the
                            shaded survival region) in a clear margin.

PRINT TARGET: bound book, every PNG rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is
ALSO distinguished by a hatch pattern / text label so figures survive grayscale.
Real sprites obey the IRON RULE: art lives in margins / beside labels, never over a
curve, equation, axis, or number a reader must read. Sprite art is REAL
(assets/sprites/front/*.png) and is only ever COMPOSITED, never generated.

Run: python3 figures/src/gen_ch10.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from cycler import cycler

from sprite_util import front, place_sprite
from type_palette import chapter_accent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents). ch10 = Psychic type, so the
# accent is the §17 psychic color via chapter_accent(10).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
ACCENT = chapter_accent(10)  # psychic #F85888
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
# 1. ch10_continuous_moments -- E[X] = int x f(x) dx is the balance point.
#    A right-skewed density on [0, 6]; the mean sits to the RIGHT of the peak
#    because the long thin upper tail tugs the fulcrum. (Concept 1)
# --------------------------------------------------------------------------
def fig_continuous_moments():
    fig, ax = plt.subplots(figsize=(11, 6.0))
    _clean(ax)

    # A right-skewed density: a Gamma(shape=2, scale=1.1) restricted to [0, 6],
    # renormalized on that window so it is an honest pdf for the picture.
    from scipy import stats
    a, b = 0.0, 6.0
    shape, scale = 2.0, 1.1
    x = np.linspace(a, b, 800)
    raw = stats.gamma.pdf(x, shape, scale=scale)
    mass = np.trapz(raw, x)
    f = raw / mass                      # honest pdf on [0, 6]
    # Mean of the truncated/renormalized density, computed numerically.
    mu = np.trapz(x * f, x)
    # Mode (peak) of this shape is at (shape-1)*scale = 1.1.
    mode = (shape - 1) * scale

    # The density curve + filled probability mass.
    ax.plot(x, f, color=ACCENT, lw=2.8, zorder=5)
    ax.fill_between(x, f, color=ACCENT, alpha=0.18, zorder=2)

    # A representative thin slice f(x) dx, the "value times its probability slice"
    # that the integral sums. Place it out in the tail to show the lever arm.
    xs = 3.4
    fs = float(np.interp(xs, x, f))
    ax.fill_between([xs - 0.07, xs + 0.07], [fs, fs], color=KANTO_BLUE,
                    alpha=0.65, hatch="//", edgecolor=KANTO_BLUE, lw=0.0,
                    zorder=4)
    ax.annotate(r"a slice $f(x)\,dx$: its lever arm is $x$,"
                "\n" r"its weight is the area $f(x)\,dx$",
                xy=(xs, fs * 0.7), xytext=(4.35, 0.255), ha="center",
                fontsize=9.5, color=INK,
                arrowprops=dict(arrowstyle="->", color=KANTO_BLUE, lw=1.3),
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_BLUE,
                          lw=1.1))

    # The fulcrum (a triangle) sits UNDER the mean -- the balance point.
    tip_y = 0.0
    tri_w, tri_h = 0.26, 0.045
    fulc = Polygon([(mu - tri_w, tip_y - tri_h), (mu + tri_w, tip_y - tri_h),
                    (mu, tip_y)], closed=True, facecolor=KANTO_RED,
                   edgecolor="black", lw=1.0, zorder=8, clip_on=False)
    ax.add_patch(fulc)
    ax.axvline(mu, color=KANTO_RED, lw=1.6, ls="-", ymax=0.93, zorder=6)
    ax.text(mu, 0.305, r"$E[X]=\int_{-\infty}^{\infty}\! x\,f(x)\,dx$",
            ha="center", va="bottom", fontsize=12, color=KANTO_RED, zorder=9,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_RED, lw=1.3))
    ax.text(mu + 0.05, -0.030, f"mean $\\approx {mu:.2f}$", ha="left", va="top",
            color=KANTO_RED, fontsize=10, fontweight="bold")

    # The mode (peak) marker, to the LEFT of the mean -- the contrast that makes
    # "balance point, not most-likely value" concrete.
    ax.axvline(mode, color=KANTO_GREEN, lw=1.4, ls="--", ymax=0.82, zorder=6)
    ax.text(mode - 0.05, -0.030, f"mode $\\approx {mode:.2f}$", ha="right",
            va="top", color=KANTO_GREEN, fontsize=10)
    ax.annotate("the rare, heavy upper tail tugs the\n"
                "balance point to the RIGHT of the peak",
                xy=(mu, 0.06), xytext=(2.55, 0.16), ha="center", fontsize=9.5,
                color=INK,
                arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.2))

    ax.set_title("Continuous expectation is the balance point of the density\n"
                 r"$E[X]=\int x\,f(x)\,dx$ — value $x$ weighted by its probability "
                 r"slice $f(x)\,dx$, totalled by the integral",
                 fontsize=12.5)
    ax.set_xlabel("loss size $x$ (the value the random variable takes)",
                  fontsize=10, labelpad=22)
    ax.set_ylabel("density $f(x)$", fontsize=10)
    ax.set_yticks([])
    ax.set_xlim(-0.2, 6.3)
    ax.set_ylim(0, 0.36)

    # Real psychic-type sprite (Kadabra #64) in the upper-LEFT margin, clear of the
    # curve, equations, and axis -- it "warps" the discrete bars into a curve.
    place_sprite(ax, front(64), (0.55, 0.30), zoom=0.42, alpha=0.95, zorder=7)
    ax.text(0.55, 0.255, "#64 Kadabra", ha="center", fontsize=8, color=INK)
    fig.tight_layout()
    return save(fig, "ch10_continuous_moments")


# --------------------------------------------------------------------------
# 2. ch10_survival_integral -- E[X] = int_0^inf S(x) dx is the AREA under the
#    survival curve (the continuous Darth-Vader twin). (Concept 3)
# --------------------------------------------------------------------------
def fig_survival_integral():
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.7))

    from scipy import stats
    theta = 4.0                          # an Exp(4): S(x) = e^{-x/4}, E[X] = 4

    # Left: the density with the mean marked, for contrast with the survival route.
    axL = axes[0]
    _clean(axL)
    x = np.linspace(0, 20, 600)
    fL = stats.expon.pdf(x, scale=theta)
    axL.plot(x, fL, color=ACCENT, lw=2.6, zorder=5)
    axL.fill_between(x, fL, color=ACCENT, alpha=0.16, zorder=2)
    axL.axvline(theta, color=KANTO_RED, lw=1.6, ls="-", ymax=0.86, zorder=6)
    axL.text(theta + 0.3, stats.expon.pdf(0, scale=theta) * 0.62,
             r"$E[X]=\theta=4$", ha="left", color=KANTO_RED, fontsize=11)
    axL.set_title(r"The long road: $E[X]=\int x\,f(x)\,dx$"
                  "\n(weight every value by its density)", fontsize=11.5)
    axL.set_xlabel("value $x$", fontsize=10)
    axL.set_ylabel("density $f(x)$", fontsize=10)
    axL.set_yticks([])
    axL.set_xlim(0, 20)
    axL.set_ylim(0, 0.27)

    # Right: the shortcut -- E[X] is the whole area UNDER the survival curve.
    axR = axes[1]
    _clean(axR)
    S = stats.expon.sf(x, scale=theta)
    axR.plot(x, S, color=KANTO_BLUE, lw=2.8, zorder=5)
    axR.fill_between(x, S, color=KANTO_BLUE, alpha=0.28, hatch="//",
                     edgecolor=KANTO_BLUE, lw=0.0, zorder=2)
    axR.axhline(0, color=INK, lw=0.8)
    axR.text(5.2, 0.46,
             r"area $=\int_0^{\infty}\! S(x)\,dx = E[X] = 4$",
             ha="left", va="center", fontsize=12.5, color=INK, zorder=7,
             bbox=dict(boxstyle="round,pad=0.32", fc="white", ec=KANTO_BLUE,
                       lw=1.3))
    axR.text(1.1, 0.86, r"$S(x)=P(X>x)$", ha="left", color=KANTO_BLUE,
             fontsize=11)
    axR.annotate("each strip of width $dx$ at height $S(x)$\n"
                 "adds $S(x)\\,dx$ — total area is the mean",
                 xy=(8.0, stats.expon.sf(8.0, scale=theta)), xytext=(9.2, 0.55),
                 ha="center", fontsize=9.0, color=INK,
                 arrowprops=dict(arrowstyle="->", color=KANTO_BLUE, lw=1.2))
    axR.set_title("The shortcut (the Darth-Vader twin):\n"
                  r"$E[X]=\int_0^{\infty} S(x)\,dx$ — the area under survival "
                  r"($X\geq 0$)", fontsize=11.5)
    axR.set_xlabel(r"value $x$", fontsize=10)
    axR.set_ylabel(r"survival $S(x)$", fontsize=10)
    axR.set_xlim(0, 20)
    axR.set_ylim(0, 1.05)
    axR.set_yticks([0, 0.5, 1.0])

    fig.suptitle("Two roads to the same mean — and the survival road skips the "
                 "density entirely",
                 fontsize=13.5, y=1.02)

    # Real Mr. Mime sprite (#122) in the RIGHT panel's clear upper-right margin --
    # the barrier/mime that "props up" the shaded survival area whose total is E[X].
    place_sprite(axR, front(122), (16.8, 0.80), zoom=0.42, alpha=0.95, zorder=8)
    axR.text(16.8, 0.61, "#122 Mr. Mime", ha="center", fontsize=8, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    return save(fig, "ch10_survival_integral")


REGISTRY = [
    fig_continuous_moments,
    fig_survival_integral,
]


def main() -> None:
    print(f"Generating Chapter 10 (Continuous Moments) figures -> "
          f"{OUT} at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
