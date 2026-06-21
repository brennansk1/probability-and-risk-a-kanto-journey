#!/usr/bin/env python3
"""Generate every Chapter 3 (Discrete RVs & Moments / S.S. Anne -> Vermilion / Lt. Surge) figure.

Manifest (MASTER_PLAN_V3 §16, DESIGN_BLUEPRINT ch03 row) — five diagrams into assets/diagrams/:
  ch03_pmf_cdf_survival   pmf / cdf / survival of the sinking-ship RV; composites Pikachu #25
  ch03_darthvader_area    E[X] = sum of S(k): the survival "staircase" whose area is the mean
  ch03_mean_median_mode   one skewed pmf marked with its mode, median, and mean (they differ)
  ch03_variance_spread    two pmfs, same mean, different spread (variance as spread)
  ch03_1var_stats_keypad  TI-30XS MultiView 1-Var-Stats workflow schematic (math diagram, no sprite)

PRINT TARGET: bound book -> every PNG at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is ALSO
distinguished by a hatch / text label so figures survive grayscale (color never the sole channel).
Sprites obey the IRON RULE: real Pokemon art in margins/corners only, never over a bar, curve,
axis, equation, or number a reader must read.

Run: python3 figures/src/gen_ch03.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from cycler import cycler

from sprite_util import front, place_sprite
from type_palette import chapter_accent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
ELECTRIC = chapter_accent(3)  # §17 Electric accent (#F8D030) — banner/figure parity.
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


def _blank(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_facecolor("white")
    ax.grid(False)


# The shared "decks holding" random variable used in figs 1 and 2.
#   X = number of intact decks when the S.S. Anne finally goes under, X in {0,1,2,3,4}.
#   pmf p(k): 0.10, 0.20, 0.30, 0.25, 0.15  (sums to 1).
#   E[X] = 0*.10 + 1*.20 + 2*.30 + 3*.25 + 4*.15 = 0 + .20 + .60 + .75 + .60 = 2.15.
SHIP_K = [0, 1, 2, 3, 4]
SHIP_PMF = [0.10, 0.20, 0.30, 0.25, 0.15]
SHIP_EX = sum(k * p for k, p in zip(SHIP_K, SHIP_PMF))  # 2.15


def _cdf(pmf):
    out, run = [], 0.0
    for p in pmf:
        run += p
        out.append(run)
    return out


def _survival(pmf):
    # S(k) = P(X > k) = 1 - F(k).
    return [1.0 - c for c in _cdf(pmf)]


# --------------------------------------------------------------------------
# 1. ch03_pmf_cdf_survival — three stacked panels of the same discrete RV.
#    Real Pikachu #25 composited into the top-left margin (iron rule).
# --------------------------------------------------------------------------
def fig_pmf_cdf_survival():
    cdf = _cdf(SHIP_PMF)
    surv = _survival(SHIP_PMF)

    fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.8))
    fig.suptitle("One random variable, three views — $X$ = intact decks when the "
                 "S.S. Anne goes under", fontsize=13.5, fontweight="bold", y=1.02)

    # --- pmf ---
    ax = axes[0]
    ax.bar(SHIP_K, SHIP_PMF, width=0.62, color=ELECTRIC, edgecolor=INK,
           lw=1.3, hatch="..", zorder=3)
    for k, p in zip(SHIP_K, SHIP_PMF):
        ax.text(k, p + 0.012, f"{p:.2f}", ha="center", va="bottom",
                fontsize=9, color=INK)
    ax.set_title("pmf  $p(k)=P(X=k)$", fontsize=11.5)
    ax.set_xlabel("$k$ (intact decks)")
    ax.set_ylabel("$p(k)$")
    ax.set_xticks(SHIP_K)
    ax.set_ylim(0, 0.40)
    ax.grid(axis="y", alpha=0.4)
    # Pikachu in the upper-left margin — clear of every bar/number.
    place_sprite(ax, front(25), (0.10, 0.86), xycoords="axes fraction",
                 zoom=0.42, alpha=0.95, zorder=6)

    # --- cdf (right-continuous step) ---
    ax = axes[1]
    xs = [-0.6] + SHIP_K + [4.6]
    ys = [0.0] + cdf + [1.0]
    ax.step(xs, ys, where="post", color=KANTO_BLUE, lw=2.4, zorder=3)
    for k, c in zip(SHIP_K, cdf):
        ax.plot(k, c, "o", color=KANTO_BLUE, ms=6, zorder=4)
    ax.set_title("cdf  $F(k)=P(X\\leq k)$", fontsize=11.5)
    ax.set_xlabel("$k$")
    ax.set_ylabel("$F(k)$")
    ax.set_xticks(SHIP_K)
    ax.set_ylim(0, 1.05)
    ax.grid(alpha=0.4)
    ax.text(0.04, 0.92, "climbs to 1\n(non-decreasing)", transform=ax.transAxes,
            fontsize=8.5, color=KANTO_BLUE, va="top")

    # --- survival (right-continuous step) ---
    ax = axes[2]
    ys = [1.0] + surv + [0.0]
    ax.step(xs, ys, where="post", color=KANTO_RED, lw=2.4, zorder=3)
    for k, s in zip(SHIP_K, surv):
        ax.plot(k, s, "o", color=KANTO_RED, ms=6, zorder=4)
    ax.set_title("survival  $S(k)=P(X>k)=1-F(k)$", fontsize=11.5)
    ax.set_xlabel("$k$")
    ax.set_ylabel("$S(k)$")
    ax.set_xticks(SHIP_K)
    ax.set_ylim(0, 1.05)
    ax.grid(alpha=0.4)
    ax.text(0.50, 0.92, '"ship survives\npast deck $k$"', transform=ax.transAxes,
            fontsize=8.5, color=KANTO_RED, va="top")

    fig.tight_layout()
    return save(fig, "ch03_pmf_cdf_survival")


# --------------------------------------------------------------------------
# 2. ch03_darthvader_area — E[X] = sum_{k>=0} S(k) as the area under the
#    survival staircase. Each unit-wide bar of height S(k) is one term.
# --------------------------------------------------------------------------
def fig_darthvader_area():
    surv = _survival(SHIP_PMF)            # S(0..4); S(4)=0
    terms = surv[:-1]                     # S(0),S(1),S(2),S(3) -> the nonzero terms
    fig, ax = plt.subplots(figsize=(10.5, 6.0))
    ax.set_title("The Darth-Vader rule:  $E[X]=\\sum_{k=0}^{\\infty} S(k)$  "
                 "= area under the survival staircase", fontsize=13)

    # Each shaded bar spans [k, k+1) with height S(k): its area IS the term S(k).
    labels = ["S(0)", "S(1)", "S(2)", "S(3)"]
    hatches = ["..", "//", "xx", "\\\\"]
    running = 0.0
    for k, (s, lab, h) in enumerate(zip(terms, labels, hatches)):
        ax.add_patch(Rectangle((k, 0), 1.0, s, facecolor=KANTO_RED,
                               edgecolor=INK, lw=1.3, alpha=0.55, hatch=h,
                               zorder=2))
        ax.text(k + 0.5, s + 0.02, f"${lab}={s:.2f}$", ha="center", va="bottom",
                fontsize=10, color=INK)
        running += s

    # Overlay the survival step for context.
    xs = [0, 0, 1, 1, 2, 2, 3, 3, 4]
    ys = [1.0, surv[0], surv[0], surv[1], surv[1], surv[2], surv[2], surv[3], surv[3]]
    ax.step([0, 1, 2, 3, 4], surv[:-1] + [0], where="post", color=KANTO_RED,
            lw=2.4, zorder=4)

    ax.set_xlim(-0.3, 5.2)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("$k$")
    ax.set_ylabel("$S(k)=P(X>k)$")
    ax.set_xticks([0, 1, 2, 3, 4])
    ax.grid(alpha=0.35)

    ax.text(2.55, 0.78,
            "Add the bar areas (each width $1$):\n"
            f"$E[X]={terms[0]:.2f}+{terms[1]:.2f}+{terms[2]:.2f}+{terms[3]:.2f}"
            f"={running:.2f}$",
            ha="left", va="top", fontsize=11.5, color=INK,
            bbox=dict(boxstyle="round,pad=0.4", fc="#FFF6D6", ec=KANTO_YEL, lw=1.5))
    ax.text(2.55, 0.55,
            "Same answer as $\\sum k\\,p(k)=2.15$ — two roads to the mean.",
            ha="left", va="top", fontsize=9.5, color=KANTO_GREEN, style="italic")

    fig.tight_layout()
    return save(fig, "ch03_darthvader_area")


# --------------------------------------------------------------------------
# 3. ch03_mean_median_mode — a right-skewed pmf with mode, median, mean marked
#    in distinct positions so the reader sees the three centers disagree.
# --------------------------------------------------------------------------
def fig_mean_median_mode():
    # Battles-won-per-day RV, right-skewed, chosen so mode < median < mean (all
    # distinct so the reader literally sees the three centers disagree):
    #   k:    0     1     2     3     4     5
    #   p:  0.40  0.25  0.15  0.10  0.06  0.04   (sum 1)
    #   mode = 0 (tallest bar); median = 1 (first cdf >= 0.5); mean = 1.29.
    k = [0, 1, 2, 3, 4, 5]
    p = [0.40, 0.25, 0.15, 0.10, 0.06, 0.04]
    mode = k[p.index(max(p))]                   # 0
    mean = sum(ki * pi for ki, pi in zip(k, p))
    # median: smallest k with cdf >= 0.5
    cdf = _cdf(p)
    median = next(ki for ki, c in zip(k, cdf) if c >= 0.5)

    fig, ax = plt.subplots(figsize=(10.5, 6.0))
    ax.set_title("Three different 'centers' of a skewed pmf\n"
                 "$X$ = battles won per day at Vermilion", fontsize=13)
    ax.bar(k, p, width=0.6, color=ELECTRIC, edgecolor=INK, lw=1.3, hatch="..",
           zorder=2)
    for ki, pi in zip(k, p):
        ax.text(ki, pi + 0.008, f"{pi:.2f}", ha="center", va="bottom",
                fontsize=8.5, color=INK)
    ax.set_xlabel("$k$ (battles won)")
    ax.set_ylabel("$p(k)$")
    ax.set_xticks(k)
    ax.set_ylim(0, 0.46)
    ax.grid(axis="y", alpha=0.4)

    # markers as vertical lines, each a different style + a labeled flag.
    ax.axvline(mode, color=KANTO_GREEN, lw=2.2, ls="-", zorder=3)
    ax.axvline(median, color=KANTO_BLUE, lw=2.2, ls="--", zorder=3)
    ax.axvline(mean, color=KANTO_RED, lw=2.2, ls=":", zorder=3)

    ax.text(mode + 0.06, 0.435, f"mode $={mode}$", ha="left", va="top",
            fontsize=9.5, color=KANTO_GREEN, fontweight="bold")
    ax.text(median + 0.06, 0.30, f"median $={median}$", ha="left", va="top",
            fontsize=9.5, color=KANTO_BLUE, fontweight="bold")
    ax.text(mean + 0.06, 0.20, f"mean $={mean:.2f}$", ha="left", va="top",
            fontsize=9.5, color=KANTO_RED, fontweight="bold")

    ax.text(0.97, 0.62,
            "Right-skew pushes the\nmean above the median,\n"
            "above the mode:\n"
            "mode $<$ median $<$ mean",
            transform=ax.transAxes, ha="right", va="top", fontsize=10,
            color=INK, bbox=dict(boxstyle="round,pad=0.35", fc="#EEF3FF",
                                 ec=KANTO_BLUE, lw=1.3))
    fig.tight_layout()
    return save(fig, "ch03_mean_median_mode")


# --------------------------------------------------------------------------
# 4. ch03_variance_spread — two pmfs, SAME mean, different variance.
# --------------------------------------------------------------------------
def fig_variance_spread():
    # Both centered at mean 2. Tight: concentrated near 2. Wide: spread to the ends.
    k = [0, 1, 2, 3, 4]
    tight = [0.05, 0.20, 0.50, 0.20, 0.05]   # mean 2, small var
    wide = [0.25, 0.10, 0.30, 0.10, 0.25]    # mean 2, large var
    mt = sum(ki * pi for ki, pi in zip(k, tight))
    mw = sum(ki * pi for ki, pi in zip(k, wide))
    vt = sum((ki - mt) ** 2 * pi for ki, pi in zip(k, tight))
    vw = sum((ki - mw) ** 2 * pi for ki, pi in zip(k, wide))

    fig, axes = plt.subplots(1, 2, figsize=(12, 5.2), sharey=True)
    fig.suptitle("Same mean, different spread — variance measures the spread",
                 fontsize=13.5, fontweight="bold", y=1.00)

    for ax, pmf, var, title, col, hatch in [
        (axes[0], tight, vt, "Reliable: low variance", KANTO_BLUE, "//"),
        (axes[1], wide, vw, "Erratic: high variance", KANTO_RED, "xx"),
    ]:
        ax.bar(k, pmf, width=0.6, color=col, edgecolor=INK, lw=1.3,
               alpha=0.85, hatch=hatch, zorder=2)
        for ki, pi in zip(k, pmf):
            ax.text(ki, pi + 0.01, f"{pi:.2f}", ha="center", va="bottom",
                    fontsize=8.5, color=INK)
        ax.axvline(2, color=KANTO_GREEN, lw=2.2, ls=":", zorder=3)
        ax.text(2, 0.55, "mean $=2$", ha="center", color=KANTO_GREEN,
                fontsize=9.5, fontweight="bold")
        ax.set_title(title, fontsize=11.5)
        ax.set_xlabel("$k$")
        ax.set_xticks(k)
        ax.set_ylim(0, 0.60)
        ax.grid(axis="y", alpha=0.4)
        ax.text(0.5, 0.80, f"$\\mathrm{{Var}}(X)={var:.2f}$",
                transform=ax.transAxes, ha="center", fontsize=12,
                color=col, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=col, lw=1.4))
    axes[0].set_ylabel("$p(k)$")
    fig.tight_layout()
    return save(fig, "ch03_variance_spread")


# --------------------------------------------------------------------------
# 5. ch03_1var_stats_keypad — the TI-30XS MultiView 1-Var-Stats flow.
#    A labeled SCHEMATIC (math diagram), NO sprite. Mirrors the flagship calc skill.
# --------------------------------------------------------------------------
def fig_1var_stats_keypad():
    fig, ax = plt.subplots(figsize=(11.5, 6.6))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.set_title("Flagship workflow: 1-Var Stats on the TI-30XS MultiView\n"
                 "read $\\bar x=E[X]$ and $\\sigma x$ (so Var $=\\sigma x^2$) straight off the screen",
                 fontsize=13)

    def keycap(x, y, label, w=1.15, h=0.62, fc="#2b2b2b", tc="white"):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                    boxstyle="round,pad=0.02,rounding_size=0.10",
                                    fc=fc, ec=INK, lw=1.3, zorder=3))
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                fontsize=9.5, color=tc, fontweight="bold", zorder=4)

    def step(x, y, n, text, w=5.0, h=1.5):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                    boxstyle="round,pad=0.05,rounding_size=0.12",
                                    fc="#FFFDF2", ec=ELECTRIC, lw=1.8, zorder=2))
        ax.add_patch(plt.Circle((x + 0.42, y + h - 0.42), 0.30,
                                fc=ELECTRIC, ec=INK, lw=1.2, zorder=3))
        ax.text(x + 0.42, y + h - 0.42, str(n), ha="center", va="center",
                fontsize=11, fontweight="bold", color=INK, zorder=4)
        ax.text(x + 0.95, y + h - 0.42, text[0], ha="left", va="center",
                fontsize=10.5, fontweight="bold", color=INK, zorder=4)
        for i, line in enumerate(text[1:]):
            ax.text(x + 0.30, y + h - 1.02 - i * 0.42, line, ha="left",
                    va="center", fontsize=9.0, color=INK, zorder=4)

    # Step 1 — enter the data lists.
    step(0.4, 7.0, 1, ["Enter the pmf into two lists",
                       "L1 = the values  k",
                       "L2 = the probabilities  p(k)"])
    keycap(5.9, 7.55, "data", fc=ELECTRIC, tc=INK)
    ax.text(7.2, 7.86, "opens the list editor", fontsize=9, color=INK, va="center")
    # tiny list table
    ax.text(7.2, 7.30, "L1: 0  1  2  3  4", fontsize=8.6, color=INK,
            family="monospace", va="center")
    ax.text(7.2, 7.02, "L2: .10 .20 .30 .25 .15", fontsize=8.6, color=INK,
            family="monospace", va="center")

    # Step 2 — launch 1-Var Stats.
    step(0.4, 5.1, 2, ["Launch the statistics engine",
                       "choose 1-Var Stats",
                       "set DATA: L1   FRQ: L2   (probabilities as frequencies)"])
    keycap(5.9, 5.62, "2nd", fc=ELECTRIC, tc=INK)
    keycap(7.15, 5.62, "stat", fc=ELECTRIC, tc=INK)
    ax.text(8.5, 5.93, "= 1-Var Stats menu", fontsize=9, color=INK, va="center")
    ax.text(5.9, 5.30, "DATA: L1   FRQ: L2   then CALC",
            fontsize=8.8, color=INK, family="monospace", va="center")

    # Step 3 — read the screen.
    step(0.4, 3.2, 3, ["Read the results screen",
                       "$\\bar x$  = the mean  $E[X]$",
                       "$\\sigma x$ = population SD  (square it for the variance)"])

    # the calculator "screen" readout on the right.
    ax.add_patch(FancyBboxPatch((6.2, 2.9), 5.2, 2.0,
                                boxstyle="round,pad=0.05,rounding_size=0.10",
                                fc="#C7E6C7", ec=INK, lw=1.6, zorder=2))
    ax.text(6.5, 4.55, "1-Var Stats", fontsize=10, family="monospace",
            color=INK, va="center")
    ax.text(6.5, 4.18, r"$\bar x$ = 2.15", fontsize=11, family="monospace",
            color=KANTO_RED, fontweight="bold", va="center")
    ax.text(6.5, 3.80, r"$\Sigma x$ = ...", fontsize=9.5, family="monospace",
            color=INK, va="center")
    ax.text(6.5, 3.42, r"$\sigma x$ = 1.195...", fontsize=11, family="monospace",
            color=KANTO_BLUE, fontweight="bold", va="center")
    ax.text(6.5, 3.08, r"n = 1", fontsize=9.0, family="monospace", color=INK,
            va="center")

    # Step 4 — the takeaway.
    ax.add_patch(FancyBboxPatch((0.4, 1.2), 11.0, 1.4,
                                boxstyle="round,pad=0.05,rounding_size=0.12",
                                fc="#FFF6D6", ec=KANTO_YEL, lw=1.8, zorder=2))
    ax.text(6.0, 2.18,
            r"$E[X]=\bar x = 2.15$       "
            r"$\mathrm{Var}(X)=\sigma x^{2}=(1.195\ldots)^2 \approx 1.43$",
            ha="center", va="center", fontsize=12, color=INK, fontweight="bold")
    ax.text(6.0, 1.58,
            "Always use  $\\sigma x$  (population SD, the FRQ-weighted one), "
            "NOT  $sx$  (the sample SD).",
            ha="center", va="center", fontsize=9.5, color=KANTO_RED,
            style="italic")

    # connecting arrows down the left column.
    for y0, y1 in [(7.0, 6.6), (5.1, 4.7), (3.2, 2.6)]:
        ax.annotate("", xy=(2.9, y1), xytext=(2.9, y0),
                    arrowprops=dict(arrowstyle="->", color=ELECTRIC, lw=2.2))

    fig.tight_layout()
    return save(fig, "ch03_1var_stats_keypad")


REGISTRY = [
    fig_pmf_cdf_survival,
    fig_darthvader_area,
    fig_mean_median_mode,
    fig_variance_spread,
    fig_1var_stats_keypad,
]


def main() -> None:
    print(f"Generating Chapter 3 (Discrete RVs & Moments) figures -> {OUT} "
          f"at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
