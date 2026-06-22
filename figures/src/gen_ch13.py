#!/usr/bin/env python3
"""Generate every Chapter 13 (Continuous Deductibles & Review / Cinnabar Lab /
Fire type) figure.

Manifest (DESIGN_BLUEPRINT ch13 row · MASTER_PLAN_V3 §16, §30) — two diagrams
into assets/diagrams/:

  ch13_deductible_calculus  the CALCULUS approach (B.5.1): the expected per-loss
                            payment under an ordinary deductible is the AREA under
                            the survival curve to the RIGHT of d,
                            E[(X-d)+] = int_d^inf S(x) dx; the limited expected
                            value is the area to the LEFT of u. Real Growlithe #58
                            in the margin (the volcano-loss mascot).
  ch13_cases_approach       the CASES approach (B.5.2): the per-loss payment is a
                            PIECEWISE function of the loss X -- flat 0 below the
                            deductible d, a ramp of slope alpha through the covered
                            layer, flat at the capped payment above the maximum
                            covered loss u. Composite Growlithe #58 (front) +
                            Vulpix #37 (front) in the margins.

The chapter loss is X ~ Exp(theta = 10) (volcano damage to research gear, in
thousands of Poke-dollars); the full Cinnabar policy used in the cases figure has
deductible d = 4, maximum covered loss u = 12, coinsurance alpha = 0.8.

PRINT TARGET: bound book, every PNG rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is
ALSO distinguished by a hatch pattern / text label so figures survive grayscale.
Real sprites obey the IRON RULE: art lives in margins / corners / beside labels,
never over a curve, equation, axis, or number a reader must read. Sprite art is
REAL (assets/sprites/front/*.png) and is only ever COMPOSITED, never generated.

Run: python3 figures/src/gen_ch13.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sprite_util import front, place_sprite
from type_palette import chapter_accent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents). ch13 = Fire type, so the
# accent is the §17 fire color via chapter_accent(13).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
ACCENT = chapter_accent(13)  # fire #F08030
INK = "#333333"

PRINT_DPI = 300

# The chapter's exponential loss: X ~ Exp(theta), S(x) = e^{-x/theta}.
THETA = 10.0
D = 4.0
U = 12.0
ALPHA = 0.8


def S(x):
    return np.exp(-np.asarray(x, dtype=float) / THETA)


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
# 1. ch13_deductible_calculus — the survival-integral picture. (Concept 1)
#    E[(X-d)+] = area under S to the RIGHT of d; E[X^u] = area to the LEFT of u.
# --------------------------------------------------------------------------
def fig_deductible_calculus():
    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    _clean(ax)

    x = np.linspace(0, 45, 700)
    y = S(x)
    ax.plot(x, y, color=KANTO_RED, lw=2.8, zorder=6)

    # LEFT of d=4: the loss the trainer absorbs (the limited-value seed, shaded
    # grey/blue, light). RIGHT of d: the expected per-loss payment (orange).
    xl = np.linspace(0, D, 200)
    ax.fill_between(xl, S(xl), color=KANTO_BLUE, alpha=0.18, hatch="..",
                    edgecolor=KANTO_BLUE, lw=0.0, zorder=2)
    xr = np.linspace(D, 45, 500)
    ax.fill_between(xr, S(xr), color=ACCENT, alpha=0.42, hatch="//",
                    edgecolor=ACCENT, lw=0.0, zorder=3)

    # Deductible marker.
    ax.axvline(D, color=INK, lw=1.4, ls="--", zorder=5)
    ax.text(D, -0.045, "$d=4$", ha="center", va="top", color=INK, fontsize=11,
            fontweight="bold")

    # Label the orange payment area.
    payment = THETA * np.exp(-D / THETA)  # 10 e^{-0.4} ~= 6.703
    ax.annotate(
        r"$E[(X-d)_+]=\int_d^\infty S(x)\,dx$" "\n"
        r"$=\theta e^{-d/\theta}=10\,e^{-0.4}\approx 6.70$",
        xy=(12, S(12)), xytext=(20, 0.56), ha="center", fontsize=12, color=INK,
        arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.6),
        bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=ACCENT, lw=1.4),
        zorder=8)

    # Label the grey absorbed area.
    ax.text(1.6, 0.10, "trainer\nabsorbs", ha="center", va="center", fontsize=9.5,
            color=KANTO_BLUE, zorder=8)

    ax.set_title(
        "The calculus approach: expected payment is the survival AREA past the "
        "deductible\n"
        r"$X\sim\mathrm{Exp}(\theta=10)$, so $S(x)=e^{-x/\theta}$; "
        r"the whole area is $E[X]=\theta=10$",
        fontsize=12.5)
    ax.set_xlabel("loss size $x$ (thousands of Poké-dollars)", fontsize=10.5)
    ax.set_ylabel(r"survival $S(x)=P(X>x)$", fontsize=10.5)
    ax.set_xlim(0, 45)
    ax.set_ylim(0, 1.02)
    ax.set_xticks([0, D, 10, 20, 30, 40])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])

    # Real Growlithe sprite high-right, in the empty band where S has decayed to
    # near zero (clear of the curve and every label).
    place_sprite(ax, front(58), (38, 0.62), zoom=0.42, alpha=0.96, zorder=7)
    ax.text(38, 0.50, "#58 Growlithe", ha="center", fontsize=8, color=INK)
    fig.tight_layout()
    return save(fig, "ch13_deductible_calculus")


# --------------------------------------------------------------------------
# 2. ch13_cases_approach — the payment as a PIECEWISE function of the loss.
#    Flat 0 below d; ramp of slope alpha through the layer; flat at alpha(u-d)
#    above u. (Concept 2)
# --------------------------------------------------------------------------
def fig_cases_approach():
    fig, ax = plt.subplots(figsize=(11.5, 6.4))
    _clean(ax)

    xmax = 18.0
    # Reference 45-degree-ish line: what a "pay the whole loss" policy would pay.
    xs = np.linspace(0, xmax, 400)
    ax.plot(xs, xs, color=KANTO_GRAY, lw=1.4, ls=":", zorder=2,
            label="pay the full loss (no policy terms)")

    # The actual per-loss payment g(X) = alpha[(X^u) - (X^d)].
    def g(x):
        return ALPHA * (np.minimum(x, U) - np.minimum(x, D))

    yg = g(xs)
    ax.plot(xs, yg, color=KANTO_RED, lw=3.0, zorder=6,
            label=r"actual payment $\,g(X)=\alpha[(X\wedge u)-(X\wedge d)]$")

    # Shade the three CASES regions along the x-axis.
    ax.axvspan(0, D, color=KANTO_GRAY, alpha=0.12, zorder=1)
    ax.axvspan(D, U, color=ACCENT, alpha=0.16, zorder=1)
    ax.axvspan(U, xmax, color=KANTO_BLUE, alpha=0.10, zorder=1)

    # Case boundary markers.
    for xv, lab in [(D, "$d=4$"), (U, "$u=12$")]:
        ax.axvline(xv, color=INK, lw=1.1, ls="--", zorder=4)
        ax.text(xv, -0.55, lab, ha="center", va="top", color=INK, fontsize=11,
                fontweight="bold")

    cap = ALPHA * (U - D)  # 0.8 * 8 = 6.4
    ax.axhline(cap, color=KANTO_BLUE, lw=1.0, ls=":", zorder=3)
    ax.text(xmax - 0.2, cap + 0.15, r"capped payment $=\alpha(u-d)=0.8\cdot 8=6.4$",
            ha="right", va="bottom", color=KANTO_BLUE, fontsize=10)

    # Case labels under the three regions.
    ax.text(D / 2, 8.6, "CASE 1\n$x\\leq d$\npays $0$", ha="center", va="center",
            fontsize=9.5, color=KANTO_GRAY, zorder=8)
    ax.text((D + U) / 2, 8.6, "CASE 2\n$d<x\\leq u$\nramp, slope $\\alpha$",
            ha="center", va="center", fontsize=9.5, color=ACCENT, zorder=8)
    ax.text((U + xmax) / 2, 8.6, "CASE 3\n$x>u$\nflat at $\\alpha(u-d)$",
            ha="center", va="center", fontsize=9.5, color=KANTO_BLUE, zorder=8)

    ax.set_title(
        "The cases approach: the payment is a piecewise function of the loss\n"
        r"split the loss into three cases, integrate the density on each — "
        r"Cinnabar policy $d=4,\ u=12,\ \alpha=0.8$",
        fontsize=12.5)
    ax.set_xlabel("ground-up loss $x$ (thousands of Poké-dollars)", fontsize=10.5,
                  labelpad=14)
    ax.set_ylabel("policy payment", fontsize=10.5)
    ax.set_xlim(0, xmax)
    ax.set_ylim(0, 10.0)
    ax.set_xticks([0, D, U, xmax])
    ax.set_yticks([0, 2, cap, 8])
    ax.set_yticklabels(["0", "2", "6.4", "8"])
    ax.legend(loc="upper left", fontsize=9.5, frameon=True)

    # Real sprites in clear corners: Growlithe low-right (the covered loss),
    # Vulpix just above it, both well clear of the red payment curve (which is
    # flat at 6.4 out here) and every label.
    place_sprite(ax, front(58), (16.2, 2.2), zoom=0.38, alpha=0.96, zorder=7)
    ax.text(16.2, 1.2, "#58 Growlithe", ha="center", fontsize=7.5, color=INK)
    place_sprite(ax, front(37), (13.0, 2.2), zoom=0.38, alpha=0.96, zorder=7)
    ax.text(13.0, 1.2, "#37 Vulpix", ha="center", fontsize=7.5, color=INK)
    fig.tight_layout()
    return save(fig, "ch13_cases_approach")


REGISTRY = [
    fig_deductible_calculus,
    fig_cases_approach,
]


def main() -> None:
    print(f"Generating Chapter 13 (Continuous Deductibles & Review) figures -> "
          f"{OUT} at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
