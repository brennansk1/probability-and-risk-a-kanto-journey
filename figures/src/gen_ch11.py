#!/usr/bin/env python3
"""Generate every Chapter 11 (Key Continuous Distributions / the smooth
continuous wilds / cross-Kanto travel / Water type) figure.

Manifest (DESIGN_BLUEPRINT ch11 row · MASTER_PLAN_V3 §16, §19, §30) — five
diagrams into assets/diagrams/:
  ch11_uniform        the flat rectangle; band probability is a length ratio
                      (Porygon #137)
  ch11_exponential    the decaying density + memorylessness: re-anchoring the
                      survival tail reproduces the identical shape (Electrode #101)
  ch11_gamma_shapes   a gamma is a SUM of alpha exponential waits; shape alpha
                      controls the hump (Magneton #82)
  ch11_beta_shapes    the beta family on [0,1] — a random proportion, U / bell /
                      flat as (alpha, beta) change (Chansey #113)
  ch11_pareto_tail    ENRICHMENT (off-syllabus): the heavy Pareto tail vs the
                      exponential's light tail, log-y (Snorlax #143)

PRINT TARGET: bound book, every PNG rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is
ALSO distinguished by a hatch pattern / text label so figures survive grayscale.
Real sprites obey the IRON RULE: art lives in margins / atop bars / beside labels,
never over a curve, equation, axis, or number a reader must read. Sprite art is
REAL (assets/sprites/front/*.png) and is only ever COMPOSITED, never generated.

Run: python3 figures/src/gen_ch11.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from cycler import cycler
from scipy import stats

from sprite_util import front, place_sprite
from type_palette import chapter_accent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents). ch11 = Water type, so the
# accent is the §17 water color via chapter_accent(11).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
ACCENT = chapter_accent(11)  # water #6890F0
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
# 1. ch11_uniform — the flat rectangle; band = length ratio. (Concept 1)
# --------------------------------------------------------------------------
def fig_uniform():
    fig, ax = plt.subplots(figsize=(11, 5.8))
    _clean(ax)
    a, b = 2.0, 10.0
    h = 1.0 / (b - a)            # 1/8
    lo, hi = 4.0, 7.0            # the worked band

    # The whole uniform density: a flat rectangle of height 1/(b-a).
    ax.add_patch(Rectangle((a, 0), b - a, h, facecolor=ACCENT, alpha=0.20,
                           edgecolor=ACCENT, lw=2.2, zorder=2))
    # The band sub-rectangle (the probability we want).
    ax.add_patch(Rectangle((lo, 0), hi - lo, h, facecolor=ACCENT, alpha=0.55,
                           edgecolor=KANTO_BLUE, lw=1.4, hatch="//", zorder=3))
    # The flat top, drawn as a heavy line for the density curve itself.
    ax.plot([a, b], [h, h], color=KANTO_BLUE, lw=2.8, zorder=4)
    ax.plot([a, a], [0, h], color=KANTO_BLUE, lw=2.8, zorder=4)
    ax.plot([b, b], [0, h], color=KANTO_BLUE, lw=2.8, zorder=4)

    # Boundary markers.
    for xv, lab in [(a, "$a=2$"), (lo, "$4$"), (hi, "$7$"), (b, "$b=10$")]:
        ax.axvline(xv, color=KANTO_GRAY, lw=0.8, ls=":", ymax=h / 0.18, zorder=1)
        ax.text(xv, -0.008, lab, ha="center", va="top", fontsize=10, color=INK)

    ax.text((lo + hi) / 2, h / 2,
            r"$P(4<X<7)=\frac{7-4}{10-2}=\frac{3}{8}$",
            ha="center", va="center", fontsize=12, color=INK, zorder=5,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_BLUE, lw=1.2))
    ax.text(b - 0.1, h + 0.012, r"height $=\frac{1}{b-a}=\frac{1}{8}$",
            ha="right", va="bottom", fontsize=11, color=KANTO_BLUE)

    ax.set_title("The continuous uniform: a flat rectangle, so probability is a "
                 "length ratio\n"
                 r"$X\sim \mathrm{Unif}(2,10)$ — every point equally likely",
                 fontsize=13)
    ax.set_xlabel("position $x$ along the corridor", fontsize=10)
    ax.set_yticks([0, h])
    ax.set_yticklabels(["0", r"$\frac{1}{8}$"], fontsize=9)
    ax.set_xticks([])
    ax.set_xlim(0.5, 11.5)
    ax.set_ylim(0, 0.185)

    # Real Porygon sprite decorates the upper-left margin (clear of the rectangle).
    place_sprite(ax, front(137), (1.15, 0.155), zoom=0.40, alpha=0.95, zorder=6)
    ax.text(1.15, 0.118, "#137 Porygon", ha="center", fontsize=8, color=INK)
    fig.tight_layout()
    return save(fig, "ch11_uniform")


# --------------------------------------------------------------------------
# 2. ch11_exponential — decaying density + memorylessness. (Concept 2)
# --------------------------------------------------------------------------
def fig_exponential():
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.6))
    theta = 6.0

    # Left: the density, with the survival tail beyond x = s shaded.
    axL = axes[0]
    _clean(axL)
    x = np.linspace(0, 30, 600)
    axL.plot(x, stats.expon.pdf(x, scale=theta), color=KANTO_BLUE, lw=2.6,
             zorder=5)
    s = 4.0
    xt = np.linspace(s, 30, 400)
    axL.fill_between(xt, stats.expon.pdf(xt, scale=theta), color=KANTO_BLUE,
                     alpha=0.30, hatch="//", edgecolor=KANTO_BLUE, lw=0.0,
                     zorder=3)
    axL.axvline(s, color=KANTO_RED, lw=1.6, ls="--", zorder=4)
    axL.text(s + 0.4, stats.expon.pdf(s, scale=theta) + 0.006,
             r"$S(x)=e^{-x/\theta}$", ha="left", color=KANTO_BLUE, fontsize=11)
    axL.text(s, -0.006, "$x=s$", ha="center", va="top", color=KANTO_RED,
             fontsize=10, fontweight="bold")
    axL.set_title(r"Density $f(x)=\frac{1}{\theta}e^{-x/\theta}$ "
                  r"($\theta=6$): a constant-rate decay", fontsize=12)
    axL.set_xlabel("waiting time $x$ (minutes)", fontsize=10)
    axL.set_yticks([])
    axL.set_xticks([0, 6, 12, 18, 24, 30])
    axL.set_ylim(0, 0.18)

    # Right: re-anchor the survival tail at s -> identical shape (memorylessness).
    axR = axes[1]
    _clean(axR)
    # Original survival curve.
    xs = np.linspace(0, 30, 600)
    axR.plot(xs, stats.expon.sf(xs, scale=theta), color=KANTO_GRAY, lw=2.0,
             ls=":", zorder=3, label=r"original $S(x)$")
    # The conditional survival given X>s: same shape re-anchored at s, rescaled.
    xc = np.linspace(s, 30, 400)
    cond = stats.expon.sf(xc, scale=theta) / stats.expon.sf(s, scale=theta)
    axR.plot(xc - s, cond, color=KANTO_RED, lw=2.8, zorder=5,
             label=r"$P(X>s+t\mid X>s)$")
    axR.axhline(0, color=INK, lw=0.8)
    axR.annotate("having waited $s$, the\nremaining wait is a\nfresh "
                 r"$\mathrm{Exp}(\theta)$ — identical curve",
                 xy=(6, stats.expon.sf(6, scale=theta)), xytext=(13, 0.62),
                 ha="center", fontsize=10, color=INK,
                 arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.4),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_RED,
                           lw=1.2))
    axR.set_title("Memorylessness: the clock resets", fontsize=12)
    axR.set_xlabel(r"extra wait $t$ past $s$", fontsize=10)
    axR.set_ylabel("survival probability", fontsize=10)
    axR.set_xticks([0, 6, 12, 18, 24, 30])
    axR.set_ylim(0, 1.05)
    axR.legend(loc="upper right", fontsize=9, frameon=True)

    fig.suptitle("The exponential wait and why it forgets — "
                 r"$P(X>s+t\mid X>s)=P(X>t)$",
                 fontsize=13.5, y=1.02)
    # Real Electrode sprite in the left panel margin (the ticking timer).
    place_sprite(axL, front(101), (26.5, 0.155), zoom=0.40, alpha=0.95, zorder=6)
    axL.text(26.5, 0.12, "#101 Electrode", ha="center", fontsize=8, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    return save(fig, "ch11_exponential")


# --------------------------------------------------------------------------
# 3. ch11_gamma_shapes — gamma = sum of alpha exponential waits. (Concept 3)
# --------------------------------------------------------------------------
def fig_gamma_shapes():
    fig, ax = plt.subplots(figsize=(11, 6.0))
    _clean(ax)
    theta = 2.0
    x = np.linspace(0, 22, 700)
    shapes = [
        (1, KANTO_GREEN, "....", r"$\alpha=1$ (exponential)"),
        (2, KANTO_BLUE, "//", r"$\alpha=2$"),
        (3, KANTO_RED, "xx", r"$\alpha=3$ (3 waits, our gate)"),
    ]
    for a, color, hatch, lab in shapes:
        y = stats.gamma.pdf(x, a, scale=theta)
        ax.plot(x, y, color=color, lw=2.6, zorder=5, label=lab)
        ax.fill_between(x, y, color=color, alpha=0.14, hatch=hatch,
                        edgecolor=color, lw=0.0, zorder=2)

    # Mark the alpha=3 mean (alpha*theta = 6) as the "our gate" anchor.
    ax.axvline(3 * theta, color=KANTO_RED, lw=1.2, ls=":", zorder=3)
    ax.text(3 * theta + 0.2, 0.20, r"$E[X]=\alpha\theta=3\cdot 2=6$",
            ha="left", color=KANTO_RED, fontsize=10)

    ax.set_title("The gamma is a sum of $\\alpha$ exponential waits — larger "
                 r"$\alpha$ pushes the hump right" "\n"
                 r"$X\sim\mathrm{Gamma}(\alpha,\theta=2)$; "
                 r"$\alpha=1$ recovers the pure-decay exponential",
                 fontsize=12.5)
    ax.set_xlabel("total waiting time $x$ (seconds)", fontsize=10)
    ax.set_yticks([])
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 0.30)
    ax.legend(loc="upper right", fontsize=10, frameon=True)

    # Real Magneton sprite (three units fused = three waits) in a clear margin:
    # the right-side region below the legend, where all three curves have decayed.
    place_sprite(ax, front(82), (17.0, 0.115), zoom=0.42, alpha=0.95, zorder=6)
    ax.text(17.0, 0.075, "#82 Magneton", ha="center", fontsize=8, color=INK)
    fig.tight_layout()
    return save(fig, "ch11_gamma_shapes")


# --------------------------------------------------------------------------
# 4. ch11_beta_shapes — the beta family on [0,1]. (Concept 4)
# --------------------------------------------------------------------------
def fig_beta_shapes():
    fig, ax = plt.subplots(figsize=(11, 6.0))
    _clean(ax)
    x = np.linspace(0.001, 0.999, 600)
    families = [
        ((1, 1), KANTO_GRAY, "..", r"$\mathrm{Beta}(1,1)=\mathrm{Unif}(0,1)$ (flat)"),
        ((2, 3), KANTO_BLUE, "//", r"$\mathrm{Beta}(2,3)$ (leans toward 0, mean 0.4)"),
        ((3, 3), KANTO_GREEN, "xx", r"$\mathrm{Beta}(3,3)$ (symmetric, mean 0.5)"),
        ((5, 2), KANTO_RED, "\\\\", r"$\mathrm{Beta}(5,2)$ (leans toward 1)"),
    ]
    for (a, b), color, hatch, lab in families:
        y = stats.beta.pdf(x, a, b)
        ax.plot(x, y, color=color, lw=2.6, zorder=5, label=lab)
        ax.fill_between(x, y, color=color, alpha=0.12, hatch=hatch,
                        edgecolor=color, lw=0.0, zorder=2)

    # Mark the Beta(2,3) mean at 0.4 (the worked barrier example). The callout
    # sits low on the axvline, in the clear band beneath the crossing curves.
    ax.axvline(0.4, color=KANTO_BLUE, lw=1.2, ls=":", zorder=3)
    ax.text(0.4, 0.42, r"$E[X]=\frac{\alpha}{\alpha+\beta}=0.4$", ha="center",
            color=KANTO_BLUE, fontsize=10, zorder=7,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=KANTO_BLUE, lw=1.0))

    ax.set_title("The beta family lives on $[0,1]$ — a flexible random "
                 "proportion\n"
                 r"shape set by $(\alpha,\beta)$: $\alpha=\beta$ symmetric; "
                 r"$\alpha<\beta$ leans toward 0; $\alpha=\beta=1$ is the uniform",
                 fontsize=12.5)
    ax.set_xlabel("proportion $x$ (a fraction between 0 and 1)", fontsize=10)
    ax.set_yticks([])
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 3.0)
    ax.set_xticks([0, 0.25, 0.4, 0.5, 0.75, 1.0])
    ax.legend(loc="upper center", fontsize=9.5, frameon=True, ncol=1)

    # Real Chansey sprite (the proportion mascot) low in the left margin, clear of
    # the flat Beta(1,1) line (at height 1.0) and the rising Beta(2,3) curve.
    place_sprite(ax, front(113), (0.075, 0.45), zoom=0.42, alpha=0.95, zorder=6)
    ax.text(0.075, 0.10, "#113 Chansey", ha="center", fontsize=8, color=INK)
    fig.tight_layout()
    return save(fig, "ch11_beta_shapes")


# --------------------------------------------------------------------------
# 5. ch11_pareto_tail — ENRICHMENT: heavy Pareto tail vs light exp tail. (Concept 5)
# --------------------------------------------------------------------------
def fig_pareto_tail():
    fig, ax = plt.subplots(figsize=(11, 6.0))
    _clean(ax)
    # Survival functions on a log-y axis: Pareto's S decays polynomially (a near
    # straight line on log-y stays high), the exponential's decays geometrically
    # (plunges). Same mean-ish scale, very different tails.
    x = np.linspace(1, 60, 600)
    alpha, xm = 2.5, 1.0                      # Pareto(alpha, x_m)
    S_par = (xm / x) ** alpha                 # Pareto survival
    theta = 6.0
    S_exp = np.exp(-x / theta)                # exponential survival

    ax.semilogy(x, S_par, color=KANTO_RED, lw=2.8, zorder=5,
                label=r"Pareto tail $S(x)=(x_m/x)^\alpha$ (heavy)")
    ax.semilogy(x, S_exp, color=KANTO_BLUE, lw=2.6, ls="--", zorder=4,
                label=r"exponential tail $e^{-x/\theta}$ (light)")
    ax.fill_between(x, S_par, 1e-12, color=KANTO_RED, alpha=0.08, zorder=2)

    # Annotation in the open mid-band: both tails have dropped below ~1e-3 for
    # x > 15, so the upper-middle region is clear.
    ax.annotate("the heavy tail stays high:\nrare but ENORMOUS losses\nare far "
                "more likely than the\nexponential would predict",
                xy=(40, (xm / 40) ** alpha), xytext=(27, 6e-2), ha="center",
                fontsize=10, color=INK,
                arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.4),
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_RED,
                          lw=1.2))

    ax.set_title("ENRICHMENT — the Pareto's heavy tail (off-syllabus)\n"
                 "polynomial decay keeps catastrophic losses on the table, "
                 "unlike the exponential's plunge",
                 fontsize=12.5)
    ax.set_xlabel("loss size $x$", fontsize=10)
    ax.set_ylabel(r"survival $S(x)=P(X>x)$ (log scale)", fontsize=10)
    ax.set_xlim(1, 60)
    ax.set_ylim(1e-9, 1.2)
    ax.legend(loc="upper right", fontsize=9.5, frameon=True)

    # Real Snorlax sprite (the huge, heavy outcome) low-right, well below both
    # decayed tails (which sit near 1e-4 to 1e-5 out there) — clear empty band.
    place_sprite(ax, front(143), (50, 3.0e-7), zoom=0.44, alpha=0.95, zorder=6)
    ax.text(50, 2.5e-8, "#143 Snorlax", ha="center", fontsize=8, color=INK)
    fig.tight_layout()
    return save(fig, "ch11_pareto_tail")


REGISTRY = [
    fig_uniform,
    fig_exponential,
    fig_gamma_shapes,
    fig_beta_shapes,
    fig_pareto_tail,
]


def main() -> None:
    print(f"Generating Chapter 11 (Key Continuous Distributions) figures -> "
          f"{OUT} at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
