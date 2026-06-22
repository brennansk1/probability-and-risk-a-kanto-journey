#!/usr/bin/env python3
"""Generate every Chapter 8 (The Calculus Toolkit / Bill's lighthouse /
training montage / Steel type / the "HM: Calculus") figure.

Manifest (DESIGN_BLUEPRINT ch08 row · MASTER_PLAN_V3 §16, §19, §30) — four
diagrams into assets/diagrams/. This is a Tier-C prerequisite chapter (TIA
B.0.1-B.0.3): differentiation -> integration -> integration by parts -> the
gamma integral. Each tool gets a tight, complete figure.

  ch08_deriv_rules    the mode of f(x) = (1/4) x e^{-x/2}: the slope goes flat
                      (f'=0) at the crest x=2; inset shows exponential beating
                      polynomial so x^2 e^{-x/3} -> 0. (B.0.1)
  ch08_ibp_tabular    the tabular integration-by-parts table for
                      integral x^3 e^{-x/2} dx: derivatives of x^3 down the left,
                      antiderivatives of e^{-x/2} down the right, alternating
                      +/- diagonal products. (B.0.3)
  ch08_gamma_integral the Master Ball of integrals: the gamma integrand
                      x^{alpha-1} e^{-x} for alpha=1..4, each shaded area a
                      factorial Gamma(alpha)=(alpha-1)!. Composites the REAL
                      Master Ball item sprite (assets/items/master-ball.png). (gamma)
  ch08_improper       the improper integral over [0, infinity): the full area
                      under (1/theta) e^{-x/theta} is 1 (normalization); the tail
                      from t rightward is the survival S(t)=e^{-t/theta}; a sliding
                      wall b recedes to infinity. Composites Bill's lighthouse
                      Dragonite (#149). (B.0.2)

PRINT TARGET: bound book, every PNG rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is
ALSO distinguished by a hatch pattern / text label so figures survive grayscale.
Real sprites/items obey the IRON RULE: art lives in margins / beside labels, never
over a curve, equation, axis, or number a reader must read. Item and sprite art is
REAL (assets/items/*.png, assets/sprites/front/*.png) and is only ever COMPOSITED,
never generated.

Run: python3 figures/src/gen_ch08.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from cycler import cycler

from sprite_util import front, item, place_sprite
from type_palette import chapter_accent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents). ch08 = Steel type (the HM /
# machine toolkit), so the accent is chapter_accent(8) = steel #B8B8D0.
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
ACCENT = chapter_accent(8)  # steel #B8B8D0
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
# 1. ch08_deriv_rules — the mode (f'=0) + exponential-beats-polynomial. (B.0.1)
# --------------------------------------------------------------------------
def fig_deriv_rules():
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.6),
                             gridspec_kw={"width_ratios": [1.55, 1.0]})

    # Left: f(x) = (1/4) x e^{-x/2} climbing, cresting at x=2, then decaying;
    # a flat dashed tangent marks where f'=0 (the mode).
    axL = axes[0]
    _clean(axL)
    x = np.linspace(0, 14, 700)
    f = 0.25 * x * np.exp(-x / 2)
    axL.plot(x, f, color=KANTO_BLUE, lw=2.8, zorder=5)
    axL.fill_between(x, f, color=ACCENT, alpha=0.28, zorder=2)

    mode = 2.0
    fmode = 0.25 * mode * np.exp(-mode / 2)
    # The horizontal tangent at the crest (slope zero).
    axL.plot([mode - 2.2, mode + 2.2], [fmode, fmode], color=KANTO_RED, lw=2.0,
             ls="--", zorder=6)
    axL.plot([mode, mode], [0, fmode], color=KANTO_GRAY, lw=1.0, ls=":", zorder=3)
    axL.scatter([mode], [fmode], color=KANTO_RED, s=55, zorder=7)
    axL.annotate(r"crest: $f'(x)=0$ at $x=2$" "\n" r"(the mode)",
                 xy=(mode, fmode), xytext=(5.2, fmode + 0.018), ha="left",
                 fontsize=11, color=INK,
                 arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.4),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_RED,
                           lw=1.2))
    axL.text(0.9, 0.205,
             r"$f'(x)=\frac{1}{4} e^{-x/2}\left(1-\frac{x}{2}\right)$",
             ha="left", va="center", fontsize=11, color=KANTO_BLUE)
    axL.set_title(r"A density peaks where the slope goes flat: $f(x)=\frac{1}{4} x\,e^{-x/2}$",
                  fontsize=12.5)
    axL.set_xlabel("$x$", fontsize=10)
    axL.set_yticks([])
    axL.set_xticks([0, 2, 4, 6, 8, 10, 12, 14])
    axL.set_xlim(0, 14)
    axL.set_ylim(0, 0.24)

    # Right: exponential beats polynomial — x^2 (rising) vs e^{x/3} (rising
    # faster); their ratio collapses to 0.
    axR = axes[1]
    _clean(axR)
    xr = np.linspace(0, 18, 500)
    axR.plot(xr, xr ** 2, color=KANTO_YEL, lw=2.6, zorder=4,
             label=r"$x^2$ (polynomial)")
    axR.plot(xr, np.exp(xr / 3), color=KANTO_GREEN, lw=2.6, zorder=5,
             label=r"$e^{x/3}$ (exponential)")
    axR.annotate(r"$\dfrac{x^2}{e^{x/3}}\to 0$" "\n" r"exp beats poly",
                 xy=(13, np.exp(13 / 3)), xytext=(2.2, 230), ha="left",
                 fontsize=10.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=KANTO_GREEN, lw=1.4),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_GREEN,
                           lw=1.2))
    axR.set_title("Exponential outruns polynomial", fontsize=12)
    axR.set_xlabel("$x$", fontsize=10)
    axR.set_yticks([])
    axR.set_xlim(0, 18)
    axR.set_ylim(0, 320)
    axR.legend(loc="upper left", fontsize=9.5, frameon=True)

    fig.suptitle("Differentiation: find the peak with $f'=0$, and let exponential "
                 "decay win the tail", fontsize=13.5, y=1.02)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    return save(fig, "ch08_deriv_rules")


# --------------------------------------------------------------------------
# 2. ch08_ibp_tabular — tabular integration by parts. (B.0.3)
# --------------------------------------------------------------------------
def fig_ibp_tabular():
    fig, ax = plt.subplots(figsize=(11, 6.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")

    ax.text(5, 9.5, r"Tabular integration by parts:  "
                    r"$\int x^3\,e^{-x/2}\,dx$",
            ha="center", va="center", fontsize=15, color=INK, fontweight="bold")

    # Two columns: D (differentiate x^3 to zero) and I (integrate e^{-x/2}).
    xD, xI = 3.0, 7.0
    ax.text(xD, 8.5, r"$D$:  differentiate $x^3$", ha="center", fontsize=12,
            color=KANTO_RED, fontweight="bold")
    ax.text(xI, 8.5, r"$I$:  integrate $e^{-x/2}$", ha="center", fontsize=12,
            color=KANTO_BLUE, fontweight="bold")

    # Rows: derivatives of x^3 (left) and antiderivatives of e^{-x/2} (right).
    Dcol = [r"$x^3$", r"$3x^2$", r"$6x$", r"$6$", r"$0$"]
    Icol = [r"$e^{-x/2}$", r"$-2e^{-x/2}$", r"$4e^{-x/2}$", r"$-8e^{-x/2}$",
            r"$16e^{-x/2}$"]
    signs = ["$+$", "$-$", "$+$", "$-$"]   # alternating diagonal-product signs
    ys = [7.7, 6.4, 5.1, 3.8, 2.5]

    for y, d, i in zip(ys, Dcol, Icol):
        ax.text(xD, y, d, ha="center", va="center", fontsize=14, color=INK,
                bbox=dict(boxstyle="round,pad=0.30", fc="#FBEAEA",
                          ec=KANTO_RED, lw=1.2))
        ax.text(xI, y, i, ha="center", va="center", fontsize=13, color=INK,
                bbox=dict(boxstyle="round,pad=0.30", fc="#E8ECFB",
                          ec=KANTO_BLUE, lw=1.2))

    # Diagonal arrows pairing D-row k with I-row k+1, labeled with the sign.
    for k, sgn in enumerate(signs):
        y0, y1 = ys[k], ys[k + 1]
        ax.add_patch(FancyArrowPatch((xD + 0.95, y0 - 0.18),
                                     (xI - 0.95, y1 + 0.18),
                                     arrowstyle="->", mutation_scale=16,
                                     color=KANTO_GRAY, lw=1.5, zorder=2))
        ax.text((xD + xI) / 2, (y0 + y1) / 2 + 0.42, sgn, ha="center",
                va="center", fontsize=13, color=KANTO_GREEN, fontweight="bold")

    # The assembled answer along the bottom.
    ax.text(5, 1.25,
            r"$\int x^3 e^{-x/2}dx = -2x^3e^{-x/2}-12x^2e^{-x/2}"
            r"-48x\,e^{-x/2}-96\,e^{-x/2}+C$",
            ha="center", va="center", fontsize=11.5, color=INK,
            bbox=dict(boxstyle="round,pad=0.4", fc="#EAF6EC", ec=KANTO_GREEN,
                      lw=1.4))
    ax.text(5, 0.45,
            r"Each term $=$ (sign)$\times$($D$-entry)$\times$(next $I$-entry); "
            r"stop when $D$ hits $0$.",
            ha="center", va="center", fontsize=10, color=KANTO_GRAY)

    fig.tight_layout()
    return save(fig, "ch08_ibp_tabular")


# --------------------------------------------------------------------------
# 3. ch08_gamma_integral — the Master Ball of integrals. (the gamma identity)
# --------------------------------------------------------------------------
def fig_gamma_integral():
    fig, ax = plt.subplots(figsize=(11, 6.2))
    _clean(ax)
    x = np.linspace(0, 16, 700)
    # The gamma integrand x^{alpha-1} e^{-x}; its total area is Gamma(alpha)=(alpha-1)!.
    cases = [
        (1, KANTO_GRAY, "..", r"$\alpha=1:\ \int_0^\infty e^{-x}dx=\Gamma(1)=0!=1$"),
        (2, KANTO_GREEN, "\\\\", r"$\alpha=2:\ \int_0^\infty x\,e^{-x}dx=\Gamma(2)=1!=1$"),
        (3, KANTO_BLUE, "//", r"$\alpha=3:\ \int_0^\infty x^2e^{-x}dx=\Gamma(3)=2!=2$"),
        (4, KANTO_RED, "xx", r"$\alpha=4:\ \int_0^\infty x^3e^{-x}dx=\Gamma(4)=3!=6$"),
    ]
    for a, color, hatch, lab in cases:
        y = x ** (a - 1) * np.exp(-x)
        ax.plot(x, y, color=color, lw=2.6, zorder=5, label=lab)
        ax.fill_between(x, y, color=color, alpha=0.13, hatch=hatch,
                        edgecolor=color, lw=0.0, zorder=2)

    ax.text(8.4, 1.02,
            r"$\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx="
            r"\Gamma(\alpha)\,\theta^{\alpha}$",
            ha="center", va="center", fontsize=13.5, color=INK, zorder=7,
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=KANTO_RED,
                      lw=1.6))
    ax.text(8.4, 0.72, r"the whole area under each curve is a factorial",
            ha="center", va="center", fontsize=10, color=KANTO_GRAY)

    ax.set_title("The Master Ball of integrals: power $\\times$ decaying "
                 "exponential collapses to a factorial\n"
                 r"integrand $x^{\alpha-1}e^{-x}$ ($\theta=1$); the shaded area "
                 r"is $\Gamma(\alpha)=(\alpha-1)!$",
                 fontsize=12.5)
    ax.set_xlabel("$x$", fontsize=10)
    ax.set_yticks([])
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 1.25)
    ax.legend(loc="upper right", fontsize=10, frameon=True)

    # The REAL Master Ball item sprite in a clear margin (mid-left, above the
    # decayed tails of all four curves) — the "catch any gamma integral" emblem.
    place_sprite(ax, item("master-ball"), (12.2, 0.52), zoom=1.9, alpha=0.97,
                 zorder=6)
    ax.text(12.2, 0.30, "Master Ball", ha="center", fontsize=8.5, color=INK)
    fig.tight_layout()
    return save(fig, "ch08_gamma_integral")


# --------------------------------------------------------------------------
# 4. ch08_improper — improper integral over [0, infinity): area=1 + survival tail. (B.0.2)
# --------------------------------------------------------------------------
def fig_improper():
    fig, ax = plt.subplots(figsize=(11.5, 6.0))
    _clean(ax)
    theta = 7.0
    x = np.linspace(0, 45, 700)
    f = (1.0 / theta) * np.exp(-x / theta)
    ax.plot(x, f, color=KANTO_BLUE, lw=2.8, zorder=6)

    # Full area under the density = 1 (normalization), shaded light.
    ax.fill_between(x, f, color=ACCENT, alpha=0.30, zorder=2)
    ax.text(2.2, 0.092,
            r"$\int_0^\infty \frac{1}{\theta} e^{-x/\theta}dx = 1$" "\n"
            "(total area $=1$:" "\n" "a valid density)",
            ha="left", va="center", fontsize=10.5, color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_BLUE,
                      lw=1.0))

    # The survival tail from t rightward, hatched.
    t = 10.0
    xt = np.linspace(t, 45, 400)
    ax.fill_between(xt, (1.0 / theta) * np.exp(-xt / theta), color=KANTO_BLUE,
                    alpha=0.32, hatch="//", edgecolor=KANTO_BLUE, lw=0.0,
                    zorder=3)
    ax.axvline(t, color=KANTO_RED, lw=1.6, ls="--", zorder=4)
    ax.text(t + 0.5, 0.052,
            r"$S(t)=\int_t^\infty\! f = e^{-t/\theta}$",
            ha="left", va="center", fontsize=11, color=KANTO_BLUE)
    ax.text(t, -0.006, "$t$", ha="center", va="top", color=KANTO_RED,
            fontsize=11, fontweight="bold")

    # The sliding wall b -> infinity (the limit definition of the improper integral).
    b = 34.0
    ax.axvline(b, color=KANTO_GRAY, lw=1.4, ls=":", zorder=4)
    ax.annotate(r"wall $b\to\infty$;  tail $e^{-b/\theta}\to 0$",
                xy=(b, (1.0 / theta) * np.exp(-b / theta)), xytext=(20, 0.085),
                ha="left", fontsize=10, color=INK,
                arrowprops=dict(arrowstyle="->", color=KANTO_GRAY, lw=1.4),
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_GRAY,
                          lw=1.0))

    ax.set_title("Improper integral over $[0,\\infty)$: integrate to a wall $b$, "
                 "then slide $b$ to infinity\n"
                 r"the full area is $1$ (normalization); the tail from $t$ "
                 r"rightward is the survival $S(t)$",
                 fontsize=12.5)
    ax.set_xlabel("$x$", fontsize=10)
    ax.set_yticks([])
    ax.set_xticks([0, 7, 14, 21, 28, 35, 42])
    ax.set_xlim(0, 45)
    ax.set_ylim(0, 0.16)

    # Bill's lighthouse Dragonite (#149) — the giant the lighthouse beam summons
    # from the deep — sits in a clear upper-right margin, well clear of the curve.
    place_sprite(ax, front(149), (39.5, 0.125), zoom=0.42, alpha=0.96, zorder=7)
    ax.text(39.5, 0.094, "#149 Dragonite", ha="center", fontsize=8, color=INK)
    fig.tight_layout()
    return save(fig, "ch08_improper")


REGISTRY = [
    fig_deriv_rules,
    fig_ibp_tabular,
    fig_gamma_integral,
    fig_improper,
]


def main() -> None:
    print(f"Generating Chapter 8 (The Calculus Toolkit) figures -> "
          f"{OUT} at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
