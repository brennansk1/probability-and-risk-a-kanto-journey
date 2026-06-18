#!/usr/bin/env python3
"""Generate the Chapter 2 (Calculus toolkit) math figures.

Chapter 2 ("DO YOU ALREADY OWN THIS?" calculus refresher) references five
diagrams in its "Beat 8 — Picture it" panels. None existed under
assets/diagrams/. This script renders EXACTLY those filenames:

  ch02_geometric_sum   A bar chart of the geometric terms 3, 1.2, 0.48, ...
                       (a=3, r=0.4) plus a cumulative staircase whose top
                       climbs toward the dashed ceiling a/(1-r) = 5 and never
                       crosses it. The shrinking gap-to-5 is annotated.

  ch02_mode_tangent    The density f(x) = (1/4) x e^{-x/2} rising from the
                       origin, cresting at the mode x=2, then decaying, with a
                       flat dashed tangent (f'=0) at the crest. An inset shows
                       x^2 and e^{x/3} and their ratio collapsing to 0
                       (exponential beats polynomial).

  ch02_improper_area   The density c e^{-x/7} (c=1/7) over [0, infinity). Full
                       area = 1 (normalization); the tail from t rightward is
                       the survival function S(t); a movable wall b shows the
                       upper limit sliding to infinity as the tail e^{-b/theta}
                       vanishes.

  gamma_integrand      The gamma integrand x^{alpha-1} e^{-x} for
                       alpha = 1,2,3,4, each curve's whole area labeled
                       Gamma(alpha) = (alpha-1)! = 1, 1, 2, 6.

  ch02_reverse_order   The region between y=sqrt(x) and y=1 over 0<=x<=1, i.e.
                       0<=x<=y^2 under 0<=y<=1. Vertical strips (dy first ->
                       impossible int e^{y^3}dy) and horizontal strips
                       (dx first -> easy, 0..y^2) overlaid; the easy
                       horizontal description is highlighted.

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color distinction
is reinforced with a label, hatch, or line style so the figures stay legible in
grayscale. No Pokemon art (sprites are sourced separately).

Run: python figures/src/gen_ch02.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

from sprite_util import front, item, place_sprite

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN = "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B"
INK = "#333333"

PRINT_DPI = 300


def save(fig, name: str) -> Path:
    path = OUT / f"{name}.png"
    fig.savefig(path, dpi=PRINT_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [fig] {path.relative_to(ROOT)}")
    return path


# ---------------------------------------------------------------------------
# 1. ch02_geometric_sum  — bars of the terms + cumulative staircase -> ceiling 5
# ---------------------------------------------------------------------------
def fig_geometric_sum() -> None:
    a, r = 3.0, 0.4
    n = 7
    k = np.arange(n)
    terms = a * r ** k          # 3, 1.2, 0.48, ...
    partial = np.cumsum(terms)  # 3, 4.2, 4.68, ... -> 5
    ceiling = a / (1 - r)       # = 5

    fig, ax = plt.subplots(figsize=(8.2, 5.2))

    # Cumulative staircase: each bar STACKED on the running total.
    bottoms = np.concatenate(([0.0], partial[:-1]))
    bars = ax.bar(
        k, terms, bottom=bottoms, width=0.62,
        color=KANTO_BLUE, edgecolor=INK, linewidth=1.1, alpha=0.88,
        label="term $a r^k$ (stacked)", zorder=3,
    )
    # Hatch the first bar so the "term" idea reads even in grayscale.
    for b in bars:
        b.set_hatch("")

    # Running-total markers connected as a staircase line (top of each bar).
    step_x = np.repeat(k, 2)[1:]            # 0,1,1,2,2,...,n-1
    step_x = np.append(step_x, n - 0.4)
    step_y = np.repeat(partial, 2)[:-1]     # hold each total until next bar
    step_y = np.insert(step_y, 0, 0.0)
    ax.plot(step_x - 0.31, step_y, color=KANTO_RED, linewidth=2.2, zorder=4,
            label="running total $S_n$")
    ax.plot(k, partial, "o", color=KANTO_RED, markersize=7,
            markeredgecolor=INK, zorder=5)

    # Ceiling.
    ax.axhline(ceiling, color=INK, linestyle="--", linewidth=1.8, zorder=2)
    ax.text(n - 0.4, ceiling + 0.12,
            r"ceiling $\frac{a}{1-r}=\frac{3}{0.6}=5$",
            ha="right", va="bottom", fontsize=12, color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc=KANTO_YEL, ec=INK, alpha=0.9))

    # Annotate the shrinking gap to 5 at the first interior point only
    # (later gaps are too thin to label without crowding the crest).
    # Place the arrow just LEFT of the bar/curve so it never sits on the red line.
    ki = 1
    gap = ceiling - partial[ki]
    ax.annotate(
        "", xy=(ki - 0.33, ceiling), xytext=(ki - 0.33, partial[ki]),
        arrowprops=dict(arrowstyle="<->", color=KANTO_GREEN, lw=1.8))
    ax.text(ki - 0.42, (ceiling + partial[ki]) / 2,
            f"gap\n{gap:.2g}", color="#2F6E3C", fontsize=9.5,
            va="center", ha="right", fontweight="bold")
    ax.text(5.45, 2.2,
            "each step the\ngap shrinks by\n$r=0.4$",
            ha="center", va="center", fontsize=10.5, color="#2F6E3C",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_GREEN))

    # Term-value labels: only the first three bars are tall enough to label
    # cleanly inside; later bars are too thin and would collide with the red
    # running-total line, so we leave them unlabeled.
    for ki in range(3):
        ax.text(ki, bottoms[ki] + terms[ki] / 2,
                f"{terms[ki]:.3g}".rstrip("0").rstrip("."),
                ha="center", va="center", fontsize=9, color="white",
                fontweight="bold", zorder=6)

    # Caterpie swarm: a small sprite atop the first (largest) bar, in the empty
    # upper-left margin. Illustrative only — sits on no curve, number, or axis.
    place_sprite(ax, front(10), (0.0, 3.0), zoom=0.34,
                 box_alignment=(0.5, 0.0), alpha=0.95, zorder=6)

    ax.set_xlabel("term index $k$")
    ax.set_ylabel("value")
    ax.set_title(r"Geometric series $\sum a r^k$ creeps up to the wall $a/(1-r)$")
    ax.set_xticks(k)
    ax.set_ylim(0, 5.9)
    ax.set_xlim(-0.7, n - 0.1)
    ax.legend(loc="lower right")
    save(fig, "ch02_geometric_sum")


# ---------------------------------------------------------------------------
# 2. ch02_mode_tangent — density peak (f'=0) + inset: exp beats polynomial
# ---------------------------------------------------------------------------
def fig_mode_tangent() -> None:
    x = np.linspace(0, 12, 600)
    f = 0.25 * x * np.exp(-x / 2)   # mode at x=2
    mode = 2.0
    fmode = 0.25 * mode * np.exp(-mode / 2)

    fig, ax = plt.subplots(figsize=(8.2, 5.4))

    ax.plot(x, f, color=KANTO_BLUE, linewidth=2.6,
            label=r"$f(x)=\frac{1}{4} x e^{-x/2}$")
    ax.fill_between(x, 0, f, color=KANTO_BLUE, alpha=0.10)

    # Flat tangent at the crest.
    ax.plot([mode - 1.7, mode + 1.7], [fmode, fmode],
            color=KANTO_RED, linestyle="--", linewidth=2.0,
            label=r"tangent at mode: $f'=0$")
    ax.plot([mode], [fmode], "o", color=KANTO_RED, markersize=9,
            markeredgecolor=INK, zorder=5)
    ax.axvline(mode, color=INK, linestyle=":", linewidth=1.0, ymax=fmode / 0.22)
    ax.annotate(r"mode $x=2$", xy=(mode, fmode), xytext=(4.6, fmode + 0.018),
                fontsize=12, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(boxstyle="round,pad=0.3", fc=KANTO_YEL, ec=INK, alpha=0.9))

    ax.set_xlabel("$x$")
    ax.set_ylabel("$f(x)$")
    ax.set_title(r"The mode is where the slope goes flat ($f'=0$)")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 0.22)
    ax.legend(loc="upper right")

    # Inset: x^2 vs e^{x/3}, and their ratio -> 0.
    axin = fig.add_axes([0.52, 0.40, 0.34, 0.34])
    xi = np.linspace(0, 18, 400)
    poly = xi ** 2
    expo = np.exp(xi / 3)
    axin.plot(xi, poly, color=KANTO_GREEN, linewidth=2.0, label=r"$x^2$")
    axin.plot(xi, expo, color=KANTO_RED, linewidth=2.0, linestyle="--",
              label=r"$e^{x/3}$")
    axin.set_ylim(0, 145)            # extra headroom so the title clears the curves
    axin.set_xlim(0, 18)
    axin.set_title(r"$\dfrac{x^2}{e^{x/3}}\to 0$", fontsize=10, pad=8)
    axin.tick_params(labelsize=7)
    axin.legend(loc="upper left", fontsize=7.5, framealpha=0.95)
    axin.text(11.5, 40, "exponential\nwins", fontsize=7.5, color=KANTO_RED,
              ha="center", fontweight="bold")

    # Pikachu watches from the charging cradle (cold open). Tucked into the
    # lower-right margin, on no curve or axis the reader must read.
    place_sprite(ax, front(25), (11.4, 0.022), zoom=0.40,
                 box_alignment=(1.0, 0.0), alpha=0.95, zorder=6)
    save(fig, "ch02_mode_tangent")


# ---------------------------------------------------------------------------
# 3. ch02_improper_area — total area=1, survival tail S(t), wall b -> infinity
# ---------------------------------------------------------------------------
def fig_improper_area() -> None:
    theta = 7.0
    c = 1.0 / theta
    x = np.linspace(0, 40, 800)
    f = c * np.exp(-x / theta)
    t = 9.0
    b = 28.0  # the movable wall

    fig, ax = plt.subplots(figsize=(8.4, 5.2))

    # Full area = 1 (normalization), shaded under the whole curve up to wall b.
    xfull = x[x <= b]
    ax.fill_between(xfull, 0, c * np.exp(-xfull / theta),
                    color=KANTO_BLUE, alpha=0.16, zorder=1)
    # Survival tail from t to b, hatched + colored so it reads in grayscale.
    xtail = x[(x >= t) & (x <= b)]
    ax.fill_between(xtail, 0, c * np.exp(-xtail / theta),
                    facecolor=KANTO_RED, alpha=0.30, hatch="//",
                    edgecolor=KANTO_RED, linewidth=0.0, zorder=2,
                    label=r"survival tail $S(t)=\int_t^\infty f$")

    ax.plot(x, f, color=KANTO_BLUE, linewidth=2.6, zorder=4,
            label=r"$f(x)=c\,e^{-x/7},\ c=\frac{1}{7}$")

    # Full-area label.
    ax.annotate(r"total area $=1$" "\n" r"(fixes $c$)",
                xy=(3.0, 0.5 * c * np.exp(-3.0 / theta)),
                xytext=(8.5, 0.115), fontsize=11.5, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2),
                bbox=dict(boxstyle="round,pad=0.3", fc=KANTO_YEL, ec=INK, alpha=0.9))

    # Marker line at t.
    ax.axvline(t, color=KANTO_RED, linestyle=":", linewidth=1.6, zorder=3)
    ax.text(t, -0.012, "$t$", color=KANTO_RED, ha="center", va="top",
            fontsize=13, fontweight="bold")
    ax.text(15.5, 0.035, r"$S(t)=e^{-t/\theta}$" "\n" r"$S(0)=1,\ S(\infty)=0$",
            color=KANTO_RED, fontsize=11, ha="center",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_RED))

    # Movable wall b sliding to infinity.
    ax.axvline(b, color=KANTO_GREEN, linestyle="--", linewidth=2.0, zorder=3)
    ax.annotate("", xy=(b + 7, 0.082), xytext=(b, 0.082),
                arrowprops=dict(arrowstyle="->", color="#2F6E3C", lw=2.0))
    ax.text(b - 0.5, 0.122, r"wall $b\to\infty$" "\n" r"tail $e^{-b/\theta}\to 0$",
            color="#2F6E3C", ha="center", va="top", fontsize=10,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=KANTO_GREEN, alpha=0.9))

    ax.set_xlabel("$x$")
    ax.set_ylabel("$f(x)$")
    ax.set_title(r"Improper integral over $[0,\infty)$: area $=1$, tail $=S(t)$")
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 0.165)
    ax.legend(loc="upper right")

    # A Potion in the dead-flat far tail (recovery-time density of a fainted
    # Pokemon). Empty region, well clear of curve, axes, and every label.
    place_sprite(ax, item("potion"), (36.0, 0.052), zoom=0.85, alpha=0.92,
                 box_alignment=(0.5, 0.5), zorder=6)
    save(fig, "ch02_improper_area")


# ---------------------------------------------------------------------------
# 4. gamma_integrand — x^{alpha-1} e^{-x} for alpha=1..4, area = (alpha-1)!
# ---------------------------------------------------------------------------
def fig_gamma_integrand() -> None:
    x = np.linspace(0, 14, 700)
    alphas = [1, 2, 3, 4]
    colors = [KANTO_RED, KANTO_BLUE, KANTO_GREEN, "#9B59B6"]
    styles = ["-", "--", "-.", ":"]
    factorials = {1: 1, 2: 1, 3: 2, 4: 6}  # (alpha-1)!

    fig, ax = plt.subplots(figsize=(8.2, 5.2))

    for a, col, st in zip(alphas, colors, styles):
        y = x ** (a - 1) * np.exp(-x)
        ax.plot(x, y, color=col, linestyle=st, linewidth=2.4,
                label=(r"$\alpha=%d:\ \int_0^\infty x^{%d}e^{-x}dx="
                       r"\Gamma(%d)=%d!=%d$" % (a, a - 1, a, a - 1, factorials[a])))
        # Light fill under each curve to convey "the area IS the factorial".
        ax.fill_between(x, 0, y, color=col, alpha=0.07)

    ax.set_xlabel("$x$")
    ax.set_ylabel(r"$x^{\alpha-1}e^{-x}$")
    ax.set_title(r"Gamma integrand: total area $=\Gamma(\alpha)=(\alpha-1)!$")
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 1.05)
    ax.legend(loc="upper right", fontsize=10)

    # The Master Ball: this identity IS the Master Ball of integrals. Drop a
    # small one in the empty lower-right corner, below every (decayed) curve.
    # Sits on no curve, label, or axis tick.
    place_sprite(ax, item("master-ball"), (12.3, 0.18), zoom=0.85, alpha=0.92,
                 box_alignment=(0.5, 0.5), zorder=6)
    save(fig, "gamma_integrand")


# ---------------------------------------------------------------------------
# 5. ch02_reverse_order — region under y=1 above y=sqrt(x); two slicing schemes
# ---------------------------------------------------------------------------
def fig_reverse_order() -> None:
    # Region R: between curve y = sqrt(x) (below) and y = 1 (top), 0<=x<=1.
    # Equivalently 0 <= x <= y^2 for 0 <= y <= 1.
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 5.2))

    xx = np.linspace(0, 1, 300)
    ycurve = np.sqrt(xx)  # boundary y = sqrt(x)  <=>  x = y^2

    for ax in axes:
        # Shade R: above y=sqrt(x), below y=1.
        ax.fill_between(xx, ycurve, 1.0, color=KANTO_YEL, alpha=0.35, zorder=1)
        ax.plot(xx, ycurve, color=INK, linewidth=2.0, zorder=4,
                label=r"$y=\sqrt{x}\ \Leftrightarrow\ x=y^2$")
        ax.axhline(1.0, color=INK, linewidth=1.4, linestyle="-", zorder=4)
        ax.set_xlim(-0.05, 1.12)
        ax.set_ylim(-0.05, 1.18)
        ax.set_xlabel("$x$")
        ax.set_ylabel("$y$")
        ax.set_aspect("equal", adjustable="box")

    # ----- LEFT: vertical strips (dy first) -> impossible -----
    axL = axes[0]
    for xs in np.linspace(0.06, 0.96, 10):
        axL.plot([xs, xs], [np.sqrt(xs), 1.0], color=KANTO_RED,
                 linewidth=1.4, alpha=0.8, zorder=3)
    axL.set_title("Vertical strips  ($dy$ first)")
    axL.text(0.5, 0.46,
             r"$\int_0^1\int_{\sqrt{x}}^{1} e^{y^3}\,dy\,dx$" "\n"
             r"inner $\int e^{y^3}dy$" "\n" r"has no elementary form",
             ha="center", va="center", fontsize=10.5, color=KANTO_RED,
             bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=KANTO_RED))
    axL.text(0.52, 1.08, r"IMPOSSIBLE $\times$", color=KANTO_RED,
             fontsize=12, ha="center", fontweight="bold")
    axL.legend(loc="lower right", fontsize=9)

    # ----- RIGHT: horizontal strips (dx first) -> easy -----
    axR = axes[1]
    for ys in np.linspace(0.06, 0.96, 10):
        axR.plot([0.0, ys ** 2], [ys, ys], color=KANTO_GREEN,
                 linewidth=1.6, alpha=0.9, zorder=3)
    axR.set_title("Horizontal strips  ($dx$ first)")
    # Highlight the inner description 0 .. y^2.
    yb = 0.6
    axR.annotate("", xy=(yb ** 2, yb), xytext=(0.0, yb),
                 arrowprops=dict(arrowstyle="<->", color="#2F6E3C", lw=2.4))
    axR.text(yb ** 2 / 2, yb + 0.05, r"$0\leq x\leq y^2$", color="#2F6E3C",
             ha="center", va="bottom", fontsize=11, fontweight="bold")
    axR.text(0.56, 0.32,
             r"$\int_0^1\int_{0}^{y^2} e^{y^3}\,dx\,dy$" "\n"
             r"$=\int_0^1 y^2 e^{y^3}dy=\frac{1}{3}(e-1)$",
             ha="center", va="center", fontsize=10.5, color="#2F6E3C",
             bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=KANTO_GREEN))
    axR.text(0.52, 1.08, r"EASY $\checkmark$", color="#2F6E3C",
             fontsize=12, ha="center", fontweight="bold")

    fig.suptitle("Same region $R$, sliced two ways — reverse the order, re-slice the picture",
                 fontsize=14, fontweight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    save(fig, "ch02_reverse_order")


def main() -> None:
    print("Generating Chapter 2 figures...")
    fig_geometric_sum()
    fig_mode_tangent()
    fig_improper_area()
    fig_gamma_integrand()
    fig_reverse_order()
    print("Done.")


if __name__ == "__main__":
    main()
