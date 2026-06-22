#!/usr/bin/env python3
"""Generate every Chapter 9 (Densities & CDFs / Saffron City / Sabrina /
Marsh Badge / Psychic type) figure.

Manifest (DESIGN_BLUEPRINT ch09 row · MASTER_PLAN_V3 §16, §30) — three diagrams
into assets/diagrams/:
  ch09_pdf_area      probability is AREA under the density curve: P(a<X<b) is the
                     shaded region; the WHOLE area is 1 (Kadabra #64 warps a bar
                     chart into a smooth curve)
  ch09_cdf_from_pdf  the f -> F relationship: the cdf accumulates the density's
                     area from the left; f = F' (slope) and F = integral of f
  ch09_mixed_dist    a mixed distribution: a point mass (a spike of probability at
                     a single value) PLUS a continuous part (a density over a band)
                     — the cdf has a jump of height equal to the point mass

PRINT TARGET: bound book, every PNG rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is
ALSO distinguished by a hatch pattern / text label so figures survive grayscale.
Real sprites obey the IRON RULE: art lives in margins / corners / beside labels,
never over a curve, equation, axis, or number a reader must read. Sprite art is
REAL (assets/sprites/front/*.png) and is only ever COMPOSITED, never generated.

Run: python3 figures/src/gen_ch09.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from cycler import cycler

from sprite_util import front, place_sprite
from type_palette import chapter_accent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents). ch09 = Psychic type, so the
# accent is the §17 psychic color via chapter_accent(9).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
ACCENT = chapter_accent(9)  # psychic #F85888
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


# A smooth, normalized "psychic-dial" density used across the first two figures:
# a right-skewed bump on [0, 6]. We build it numerically and normalize so the
# total area is exactly 1, so "area = probability" is literally true on the axes.
def _dial_density(x):
    # unnormalized: a gamma-ish bump (peak near x=2), zero outside [0, 6]
    y = np.where((x >= 0) & (x <= 6), (x**1.6) * np.exp(-x / 1.4), 0.0)
    return y


def _normalizer():
    xs = np.linspace(0, 6, 20000)
    area = np.trapz(_dial_density(xs), xs)
    return 1.0 / area


_C = _normalizer()


def _f(x):
    return _C * _dial_density(x)


# --------------------------------------------------------------------------
# 1. ch09_pdf_area — probability is AREA under the density. (Concept 1)
# --------------------------------------------------------------------------
def fig_pdf_area():
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.7),
                             gridspec_kw={"width_ratios": [1, 1.25]})

    # LEFT: discrete bars (the world you came from) "warping" toward a curve.
    axL = axes[0]
    _clean(axL)
    bx = np.array([0, 1, 2, 3, 4, 5])
    # bar heights chosen to echo the curve's silhouette (these are probabilities)
    bh = np.array([0.06, 0.20, 0.27, 0.22, 0.15, 0.10])
    axL.bar(bx, bh, width=0.82, color=ACCENT, alpha=0.30, edgecolor=KANTO_BLUE,
            lw=1.4, hatch="..", zorder=3)
    # the limiting smooth curve drawn over the bar silhouette
    xc = np.linspace(0, 6, 400)
    axL.plot(xc, _f(xc), color=KANTO_RED, lw=2.6, zorder=5)
    axL.set_title("Discrete bars (countable) warp into a\nsmooth density "
                  "(continuous)", fontsize=12)
    axL.set_xlabel("reading $x$", fontsize=10)
    axL.set_ylabel("mass / density", fontsize=10)
    axL.set_yticks([])
    axL.set_xticks([0, 1, 2, 3, 4, 5, 6])
    axL.set_xlim(-0.7, 6.4)
    axL.set_ylim(0, 0.34)
    # Kadabra warps the bars -> curve: sits high-left in clear space.
    place_sprite(axL, front(64), (0.0, 0.30), zoom=0.34, alpha=0.95, zorder=6)
    axL.text(0.0, 0.255, "#64 Kadabra", ha="center", fontsize=7.5, color=INK)

    # RIGHT: the density with P(a<X<b) shaded, and the whole area labelled 1.
    axR = axes[1]
    _clean(axR)
    x = np.linspace(0, 6, 600)
    y = _f(x)
    axR.plot(x, y, color=KANTO_RED, lw=2.8, zorder=5)
    # whole area, faint
    axR.fill_between(x, y, color=ACCENT, alpha=0.12, zorder=2)
    # the band (a, b) = (1.5, 3.0), shaded heavily
    a, b = 1.5, 3.0
    xb = np.linspace(a, b, 300)
    axR.fill_between(xb, _f(xb), color=ACCENT, alpha=0.55, hatch="//",
                     edgecolor=KANTO_BLUE, lw=0.0, zorder=3)
    for xv, lab in [(a, "$a$"), (b, "$b$")]:
        axR.axvline(xv, color=KANTO_GRAY, lw=0.9, ls=":", zorder=1)
        axR.text(xv, -0.012, lab, ha="center", va="top", fontsize=11, color=INK)
    axR.text((a + b) / 2, _f((a + b) / 2) * 0.42,
             r"$P(a<X<b)$" "\n" r"$=\int_a^b f(x)\,dx$",
             ha="center", va="center", fontsize=11.5, color=INK, zorder=6,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_BLUE,
                       lw=1.2))
    axR.annotate(r"whole area $=\int_{-\infty}^{\infty} f = 1$",
                 xy=(4.4, _f(4.4)), xytext=(3.7, 0.255), ha="center",
                 fontsize=10.5, color=KANTO_RED,
                 arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.3))
    axR.text(2.55, 0.31, r"density $f(x)$ — a RATE, can exceed 1;"
             "\nonly the AREA is a probability", ha="center", fontsize=9.5,
             color=INK, style="italic")
    axR.set_title("Probability is AREA under the density curve", fontsize=12.5)
    axR.set_xlabel("reading $x$", fontsize=10)
    axR.set_ylabel("density $f(x)$", fontsize=10)
    axR.set_yticks([])
    axR.set_xticks([0, 1, 2, 3, 4, 5, 6])
    axR.set_xlim(-0.3, 6.3)
    axR.set_ylim(0, 0.36)

    fig.suptitle("From countable bars to continuous area — "
                 r"$P(a<X<b)=\int_a^b f(x)\,dx$, total area $=1$",
                 fontsize=13.5, y=1.02)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    return save(fig, "ch09_pdf_area")


# --------------------------------------------------------------------------
# 2. ch09_cdf_from_pdf — the f -> F relationship. (Concept 2)
# --------------------------------------------------------------------------
def fig_cdf_from_pdf():
    fig, axes = plt.subplots(2, 1, figsize=(10.4, 7.6), sharex=True)
    x = np.linspace(0, 6, 600)
    y = _f(x)
    # numeric cdf
    F = np.array([np.trapz(_f(np.linspace(0, xi, 400)), np.linspace(0, xi, 400))
                  for xi in x])
    x0 = 2.6  # the marked point

    # TOP: the density, with area up to x0 shaded = F(x0).
    axT = axes[0]
    _clean(axT)
    axT.plot(x, y, color=KANTO_RED, lw=2.8, zorder=5, label=r"density $f(x)$")
    xs = np.linspace(0, x0, 300)
    axT.fill_between(xs, _f(xs), color=ACCENT, alpha=0.45, hatch="//",
                     edgecolor=KANTO_BLUE, lw=0.0, zorder=3,
                     label=r"area up to $x_0$ $=F(x_0)$")
    axT.axvline(x0, color=KANTO_GRAY, lw=0.9, ls=":", zorder=1)
    axT.text(x0 + 0.08, 0.30, "$x_0$", ha="left", fontsize=11, color=INK)
    axT.text(1.15, _f(1.15) * 0.5, r"$F(x_0)=\int_{-\infty}^{x_0} f$",
             ha="center", fontsize=11, color=INK, zorder=6,
             bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=KANTO_BLUE,
                       lw=1.0))
    axT.set_title("The density $f$ — its accumulated area to the left is the cdf",
                  fontsize=12)
    axT.set_ylabel("density $f(x)$", fontsize=10)
    axT.set_yticks([])
    axT.set_ylim(0, 0.36)
    axT.legend(loc="upper right", fontsize=9.5, frameon=True)
    # Kadabra in the top-right clear band above the decayed tail.
    place_sprite(axT, front(64), (5.5, 0.27), zoom=0.32, alpha=0.95, zorder=6)
    axT.text(5.5, 0.225, "#64 Kadabra", ha="center", fontsize=7.5, color=INK)

    # BOTTOM: the cdf F, rising from 0 to 1; its slope at x0 IS f(x0).
    axB = axes[1]
    _clean(axB)
    axB.plot(x, F, color=KANTO_BLUE, lw=2.8, zorder=5, label=r"cdf $F(x)$")
    axB.axhline(1.0, color=KANTO_GRAY, lw=0.9, ls="--", zorder=1)
    axB.text(0.1, 1.02, "$F=1$ (all area)", fontsize=9, color=KANTO_GRAY)
    # mark F(x0) and draw the tangent whose slope = f(x0).
    Fx0 = np.interp(x0, x, F)
    fx0 = _f(x0)
    axB.plot([x0], [Fx0], "o", color=KANTO_RED, zorder=7)
    axB.axvline(x0, color=KANTO_GRAY, lw=0.9, ls=":", zorder=1)
    axB.plot([0, x0, x0], [0, 0, Fx0], color=KANTO_GRAY, lw=0.0)
    tx = np.linspace(x0 - 1.0, x0 + 1.0, 50)
    axB.plot(tx, Fx0 + fx0 * (tx - x0), color=KANTO_RED, lw=1.8, ls="-",
             zorder=6, label=r"slope $=f(x_0)$")
    axB.annotate(r"the slope of $F$ at $x_0$ is the density:  $f(x)=F'(x)$",
                 xy=(x0, Fx0), xytext=(3.4, 0.42), ha="center", fontsize=10.5,
                 color=KANTO_RED,
                 arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.3),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_RED,
                           lw=1.1))
    axB.text(x0 + 0.08, 0.06, "$x_0$", ha="left", fontsize=11, color=INK)
    axB.set_title(r"The cdf $F$ — it climbs from 0 to 1; its slope is $f$",
                  fontsize=12)
    axB.set_xlabel("reading $x$", fontsize=10)
    axB.set_ylabel(r"cdf $F(x)=P(X\leq x)$", fontsize=10)
    axB.set_xticks([0, 1, 2, 3, 4, 5, 6])
    axB.set_xlim(-0.3, 6.3)
    axB.set_ylim(0, 1.12)
    axB.legend(loc="center right", fontsize=9.5, frameon=True)

    fig.suptitle(r"$F$ accumulates $f$'s area  ($F=\int f$),  and  "
                 r"$f$ is $F$'s slope  ($f=F'$)", fontsize=13.5, y=1.0)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    return save(fig, "ch09_cdf_from_pdf")


# --------------------------------------------------------------------------
# 3. ch09_mixed_dist — a point mass + a continuous part. (Concept 3)
# --------------------------------------------------------------------------
def fig_mixed_dist():
    fig, axes = plt.subplots(1, 2, figsize=(12.6, 5.7))
    # Mixed law: P(X=0) = 0.4 (a point mass at 0), and a UNIFORM density of
    # height 0.15 on (0, 4] carrying the other 0.6 of probability
    # (0.15 * 4 = 0.6).  Total = 0.4 + 0.6 = 1.
    mass0 = 0.40
    h = 0.15            # density height on (0, 4]
    band = (0.0, 4.0)

    # LEFT: the "density picture" — a spike (point mass) atop a flat density.
    axL = axes[0]
    _clean(axL)
    # continuous part: flat density on (0, 4]
    axL.add_patch(Rectangle((band[0], 0), band[1] - band[0], h,
                            facecolor=ACCENT, alpha=0.35, edgecolor=KANTO_BLUE,
                            lw=1.6, hatch="//", zorder=3))
    axL.plot([band[0], band[1]], [h, h], color=KANTO_BLUE, lw=2.4, zorder=4)
    # point mass: a spike (arrow) at x=0, height = the mass (drawn on a second
    # conceptual scale; we label it as a probability mass, NOT a density height).
    spike_h = 0.40
    axL.annotate("", xy=(0, spike_h), xytext=(0, 0),
                 arrowprops=dict(arrowstyle="-|>", color=KANTO_RED, lw=3.0),
                 zorder=6)
    axL.plot([0], [spike_h], "o", color=KANTO_RED, ms=9, zorder=7)
    axL.text(0.12, spike_h, r"point mass $P(X=0)=0.40$", ha="left", va="center",
             fontsize=10.5, color=KANTO_RED,
             bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=KANTO_RED,
                       lw=1.0))
    axL.text(2.0, h + 0.018, r"continuous part: density $0.15$ on $(0,4]$"
             "\n" r"carries area $0.15\times 4 = 0.60$", ha="center",
             fontsize=9.5, color=KANTO_BLUE)
    axL.set_title("A mixed law: a probability SPIKE at 0\n"
                  "plus a continuous density elsewhere", fontsize=12)
    axL.set_xlabel("payout $x$", fontsize=10)
    axL.set_ylabel("density (band) / mass (spike)", fontsize=10)
    axL.set_yticks([])
    axL.set_xticks([0, 1, 2, 3, 4])
    axL.set_xlim(-0.6, 4.6)
    axL.set_ylim(0, 0.50)
    # Kadabra in the upper-right clear corner.
    place_sprite(axL, front(64), (4.1, 0.42), zoom=0.30, alpha=0.95, zorder=8)
    axL.text(4.1, 0.375, "#64 Kadabra", ha="center", fontsize=7.5, color=INK)

    # RIGHT: the cdf — a JUMP of height 0.40 at x=0, then a smooth ramp to 1.
    axR = axes[1]
    _clean(axR)
    # before 0: F = 0
    axR.plot([-0.6, 0], [0, 0], color=KANTO_BLUE, lw=2.8, zorder=5)
    # jump at 0 from 0 to 0.40 (the point mass)
    axR.plot([0, 0], [0, mass0], color=KANTO_RED, lw=2.8, ls="-", zorder=5)
    axR.plot([0], [0], "o", mfc="white", mec=KANTO_BLUE, ms=8, zorder=7)
    axR.plot([0], [mass0], "o", color=KANTO_RED, ms=8, zorder=7)
    # smooth ramp on (0, 4]: F(x) = 0.40 + 0.15 x
    xr = np.linspace(0, 4, 300)
    axR.plot(xr, mass0 + h * xr, color=KANTO_BLUE, lw=2.8, zorder=5)
    # after 4: F = 1
    axR.plot([4, 4.6], [1.0, 1.0], color=KANTO_BLUE, lw=2.8, zorder=5)
    axR.axhline(1.0, color=KANTO_GRAY, lw=0.8, ls="--", zorder=1)
    # annotate the jump = the point mass
    axR.annotate("jump of height $0.40$\n$=P(X=0)$, the point mass",
                 xy=(0, mass0 / 2), xytext=(1.5, 0.30), ha="center",
                 fontsize=10, color=KANTO_RED,
                 arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.3),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_RED,
                           lw=1.1))
    axR.annotate("smooth ramp:\nthe continuous part",
                 xy=(2.5, mass0 + h * 2.5), xytext=(2.7, 0.55), ha="center",
                 fontsize=10, color=KANTO_BLUE,
                 arrowprops=dict(arrowstyle="->", color=KANTO_BLUE, lw=1.3),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_BLUE,
                           lw=1.1))
    axR.set_title("Its cdf: a JUMP at the mass, then a smooth climb to 1",
                  fontsize=12)
    axR.set_xlabel("payout $x$", fontsize=10)
    axR.set_ylabel(r"cdf $F(x)=P(X\leq x)$", fontsize=10)
    axR.set_xticks([0, 1, 2, 3, 4])
    axR.set_yticks([0, 0.40, 1.0])
    axR.set_yticklabels(["0", "0.40", "1"])
    axR.set_xlim(-0.6, 4.6)
    axR.set_ylim(0, 1.12)

    fig.suptitle("A mixed distribution = a point mass + a continuous part — "
                 "the cdf jumps by the mass, then ramps", fontsize=13.5, y=1.02)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    return save(fig, "ch09_mixed_dist")


REGISTRY = [
    fig_pdf_area,
    fig_cdf_from_pdf,
    fig_mixed_dist,
]


def main() -> None:
    print(f"Generating Chapter 9 (Densities & CDFs) figures -> {OUT} "
          f"at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
