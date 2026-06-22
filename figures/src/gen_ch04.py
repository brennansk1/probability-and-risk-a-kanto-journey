#!/usr/bin/env python3
"""Generate every Chapter 4 (Combinatorics / Viridian Forest -> Pewter / Brock) figure.

Manifest (MASTER_PLAN_V3 §16, DESIGN_BLUEPRINT ch04 row) — four diagrams into assets/diagrams/:
  ch04_perm_vs_comb     ordered slots (P(n,k)) vs the same pick with order discarded (C(n,k));
                        the k! collapse made literal. Composites Pidgey #16 in the margin.
  ch04_2x2_classifier   the ordered/unordered x with/without-replacement decision grid — the
                        pick-your-machine table as a labeled diagram (no sprite over a cell).
  ch04_binomial_flock   a flock of Pidgey #16 each a Bernoulli trial; the Binomial(n,p) pmf as
                        "choose which x of n succeed" -> C(n,x) p^x (1-p)^(n-x).
  ch04_hypergeo_forest  catch-WITHOUT-replacement from a forest cluster; composites real
                        Caterpie #10, Weedle #13, Metapod #11 over the success/failure split.

PRINT TARGET: bound book -> every PNG at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is ALSO
distinguished by a hatch / text label so figures survive grayscale (color never the sole channel).
Sprites obey the IRON RULE: real Pokemon art in margins/corners only, never over a bar, curve,
axis, equation, or number a reader must read.

Run: python3 figures/src/gen_ch04.py
"""
from __future__ import annotations

from math import comb, factorial, perm
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
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
ROCK = chapter_accent(4)  # §17 Rock accent (#B8A038) — banner/figure parity.
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


# --------------------------------------------------------------------------
# 1. ch04_perm_vs_comb — order matters (P) vs order discarded (C), the same
#    3-of-5 pick. The k! collapse is the whole story: P(5,3)=60 ordered cards
#    collapse to C(5,3)=10 unordered teams, each counted 3!=6 times.
#    Real Pidgey #16 sits in the top-margin, clear of every cell.
# --------------------------------------------------------------------------
def fig_perm_vs_comb():
    n, k = 5, 3
    P = perm(n, k)          # 60
    C = comb(n, k)          # 10
    kfac = factorial(k)     # 6

    fig, ax = plt.subplots(figsize=(11.5, 6.6))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.set_title(f"Permutation vs. combination — the same pick of {k} from {n}\n"
                 f"order matters: $P({n},{k})={P}$   vs.   order discarded: "
                 f"$\\binom{{{n}}}{{{k}}}={C}$",
                 fontsize=13)

    # --- LEFT: permutation = ordered slots with a shrinking menu ---
    ax.text(3.0, 8.05, "Order MATTERS  (permutation)", ha="center", fontsize=11.5,
            fontweight="bold", color=KANTO_BLUE)
    slot_labels = ["Lead", "Second", "Anchor"]
    menus = [5, 4, 3]
    for i, (lab, m) in enumerate(zip(slot_labels, menus)):
        x = 0.7 + i * 1.85
        ax.add_patch(FancyBboxPatch((x, 6.1), 1.5, 1.0,
                                    boxstyle="round,pad=0.04,rounding_size=0.10",
                                    fc="#EEF3FF", ec=KANTO_BLUE, lw=1.8, zorder=2))
        ax.text(x + 0.75, 6.6, lab, ha="center", va="center", fontsize=9.5,
                color=INK, zorder=3)
        ax.text(x + 0.75, 7.35, str(m), ha="center", va="center", fontsize=14,
                fontweight="bold", color=KANTO_BLUE, zorder=3)
        if i < 2:
            ax.text(x + 1.62, 6.6, "x", ha="center", va="center", fontsize=13,
                    color=INK)
    ax.text(3.05, 5.5, f"$5 \\times 4 \\times 3 = {P}$ ordered cards",
            ha="center", va="center", fontsize=12, color=KANTO_BLUE,
            fontweight="bold")
    ax.text(3.05, 4.95, "(the menu shrinks: each pick is gone)", ha="center",
            va="center", fontsize=8.6, color=INK, style="italic")

    # --- RIGHT: combination = one unordered team ---
    ax.text(9.0, 8.05, "Order DOESN'T  (combination)", ha="center", fontsize=11.5,
            fontweight="bold", color=KANTO_RED)
    ax.add_patch(FancyBboxPatch((7.35, 6.1), 3.3, 1.0,
                                boxstyle="round,pad=0.04,rounding_size=0.10",
                                fc="#FFEDED", ec=KANTO_RED, lw=1.8, zorder=2))
    ax.text(9.0, 6.6, "{ A,  B,  C }  — one team", ha="center", va="center",
            fontsize=10.5, color=INK, zorder=3)
    ax.text(9.0, 5.5, f"$\\binom{{5}}{{3}} = {C}$ teams", ha="center",
            va="center", fontsize=12, color=KANTO_RED, fontweight="bold")
    ax.text(9.0, 4.95, "(a set: reshuffling changes nothing)", ha="center",
            va="center", fontsize=8.6, color=INK, style="italic")

    # --- THE COLLAPSE: 3! ordered cards per team ---
    ax.add_patch(FancyBboxPatch((0.7, 1.3), 10.6, 3.0,
                                boxstyle="round,pad=0.05,rounding_size=0.12",
                                fc="#FFFDF2", ec=ROCK, lw=2.0, zorder=1))
    ax.text(6.0, 3.95, "Why divide by  $k!$ ?  —  each team is counted "
            f"${k}! = {kfac}$ times among the ordered cards",
            ha="center", va="center", fontsize=11, fontweight="bold", color=INK)
    orderings = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]
    for j, o in enumerate(orderings):
        x = 1.4 + j * 1.55
        ax.add_patch(Rectangle((x, 2.55), 1.15, 0.7, facecolor="#EEF3FF",
                               edgecolor=KANTO_BLUE, lw=1.2, zorder=2))
        ax.text(x + 0.575, 2.9, o, ha="center", va="center", fontsize=9.5,
                color=INK, family="monospace", zorder=3)
    ax.text(6.0, 1.85,
            f"$\\{{A,B,C\\}}$ is ONE team  →  $\\binom{{5}}{{3}}"
            f"=\\dfrac{{P(5,3)}}{{3!}}=\\dfrac{{{P}}}{{{kfac}}}={C}$",
            ha="center", va="center", fontsize=12.5, color=INK)

    # Pidgey in the very top margin — clear of every box and number (iron rule).
    place_sprite(ax, front(16), (0.93, 0.97), xycoords="axes fraction",
                 zoom=0.40, alpha=0.95, zorder=6)

    fig.tight_layout()
    return save(fig, "ch04_perm_vs_comb")


# --------------------------------------------------------------------------
# 2. ch04_2x2_classifier — the pick-your-machine grid: two questions
#    (order? replacement?) place any counting problem in one of four cells.
#    A labeled math diagram; no sprite over a cell.
# --------------------------------------------------------------------------
def fig_2x2_classifier():
    fig, ax = plt.subplots(figsize=(11.0, 7.2))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.set_title("Pick your machine — two questions classify every counting problem",
                 fontsize=13.5, fontweight="bold")

    # axis headers
    ax.text(4.6, 8.05, "Order MATTERS", ha="center", fontsize=11.5,
            fontweight="bold", color=KANTO_BLUE)
    ax.text(8.9, 8.05, "Order DOESN'T matter", ha="center", fontsize=11.5,
            fontweight="bold", color=KANTO_RED)
    ax.text(1.15, 6.05, "Without\nreplacement", ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=INK, rotation=90)
    ax.text(1.15, 2.75, "With\nreplacement", ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=INK, rotation=90)

    cells = [
        # (x, y, face, edge, title, formula, note)
        (2.4, 4.7, "#EEF3FF", KANTO_BLUE, "Permutation",
         "$P(n,k)=\\dfrac{n!}{(n-k)!}$", "arrange, line up, rank, seat"),
        (6.9, 4.7, "#FFEDED", KANTO_RED, "Combination",
         "$\\binom{n}{k}=\\dfrac{n!}{k!\\,(n-k)!}$",
         "choose a team / hand / sample"),
        (2.4, 1.4, "#F1EEFF", "#7B61FF", "Sequences w/ repeats",
         "$n^{\\,k}$", "PIN, lock, digit string"),
        (6.9, 1.4, "#EAF6EA", KANTO_GREEN, "Stars & bars (rare on P)",
         "$\\binom{n+k-1}{k}$", "multiset / unordered w/ repeats"),
    ]
    for x, y, fc, ec, title, formula, note in cells:
        ax.add_patch(FancyBboxPatch((x, y), 4.0, 2.7,
                                    boxstyle="round,pad=0.05,rounding_size=0.12",
                                    fc=fc, ec=ec, lw=2.0, zorder=2))
        ax.text(x + 2.0, y + 2.25, title, ha="center", va="center", fontsize=10.5,
                fontweight="bold", color=ec, zorder=3)
        ax.text(x + 2.0, y + 1.35, formula, ha="center", va="center", fontsize=13,
                color=INK, zorder=3)
        ax.text(x + 2.0, y + 0.45, note, ha="center", va="center", fontsize=8.4,
                color=INK, style="italic", zorder=3)

    # highlight the upper-right (the exam's home cell)
    ax.add_patch(FancyBboxPatch((6.78, 4.58), 4.24, 2.94,
                                boxstyle="round,pad=0.05,rounding_size=0.12",
                                fc="none", ec=KANTO_RED, lw=3.0, ls=(0, (4, 2)),
                                zorder=4))
    ax.text(8.9, 0.55, "~4 of 5 exam counting questions live in the "
            "unordered, without-replacement cell (a $\\binom{n}{k}$).",
            ha="center", va="center", fontsize=9.3, color=KANTO_RED,
            fontweight="bold")
    fig.tight_layout()
    return save(fig, "ch04_2x2_classifier")


# --------------------------------------------------------------------------
# 3. ch04_binomial_flock — n independent Pidgey, each a Bernoulli(p) trial;
#    the Binomial(n,p) pmf as "choose which x of n succeed". A flock of real
#    Pidgey #16 sits in the top margin (iron rule); the pmf bars carry the math.
# --------------------------------------------------------------------------
def fig_binomial_flock():
    n, p = 6, 0.5
    xs = list(range(n + 1))
    pmf = [comb(n, x) * p ** x * (1 - p) ** (n - x) for x in xs]
    mode = xs[pmf.index(max(pmf))]

    fig, ax = plt.subplots(figsize=(10.8, 6.4))
    ax.set_title("Binomial$(n,p)$ — count the SUCCESSES in $n$ fixed independent trials\n"
                 f"flock of $n={n}$ Pidgey, each flushes (success) w.p. $p={p}$",
                 fontsize=12.5)
    ax.bar(xs, pmf, width=0.62, color=ROCK, edgecolor=INK, lw=1.3, hatch="..",
           zorder=3)
    for x, pr in zip(xs, pmf):
        ax.text(x, pr + 0.008, f"{pr:.3f}", ha="center", va="bottom",
                fontsize=8.6, color=INK)
    ax.set_xlabel("$x$ = number of successes")
    ax.set_ylabel("$P(X=x)$")
    ax.set_xticks(xs)
    ax.set_ylim(0, 0.36)
    ax.grid(axis="y", alpha=0.4)

    ax.text(0.025, 0.96,
            "$P(X=x)=\\binom{n}{x}\\,p^{x}(1-p)^{\\,n-x}$\n"
            "$\\binom{n}{x}$: which $x$ of the $n$ flushed\n"
            "$E[X]=np$,  $\\mathrm{Var}(X)=np(1-p)$",
            transform=ax.transAxes, ha="left", va="top", fontsize=10.5,
            color=INK, bbox=dict(boxstyle="round,pad=0.4", fc="#FFF6D6",
                                 ec=KANTO_YEL, lw=1.5))
    ax.text(0.975, 0.96, f"$E[X]=np={n*p:.0f}$\n(mode here $={mode}$)",
            transform=ax.transAxes, ha="right", va="top", fontsize=9.5,
            color=KANTO_RED, fontweight="bold")

    # A small flock of real Pidgey across the very top margin (iron rule:
    # above every bar and number, in the figure's clear header band).
    for i, fx in enumerate([0.34, 0.46, 0.58, 0.70]):
        place_sprite(ax, front(16), (fx, 1.07), xycoords="axes fraction",
                     zoom=0.20, alpha=0.95, zorder=6)
    fig.tight_layout()
    return save(fig, "ch04_binomial_flock")


# --------------------------------------------------------------------------
# 4. ch04_hypergeo_forest — catch WITHOUT replacement from a forest cluster.
#    Split the cluster into successes / failures; choose from each. Composites
#    real Caterpie #10 (successes) and Weedle #13 / Metapod #11 (failures) in
#    the box headers (margins of each box; never over a count).
# --------------------------------------------------------------------------
def fig_hypergeo_forest():
    # Cluster: N=10, K=4 Caterpie (successes), N-K=6 (Weedle+Metapod) failures.
    # Grab k=3 without replacement; favourable = exactly x=2 Caterpie.
    N, K, k, x = 10, 4, 3, 2
    favourable = comb(K, x) * comb(N - K, k - x)   # 6 * 6 = 36
    total = comb(N, k)                              # 120
    prob = favourable / total                       # 0.30

    fig, ax = plt.subplots(figsize=(11.0, 6.8))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.set_title("Hypergeometric — draw WITHOUT replacement, count by type\n"
                 "cluster of $10$: $4$ Caterpie (success), $6$ others (failure); "
                 "grab $3$, want exactly $2$ Caterpie",
                 fontsize=12.5)

    # successes box (left)
    ax.add_patch(FancyBboxPatch((0.7, 4.4), 4.6, 3.0,
                                boxstyle="round,pad=0.05,rounding_size=0.12",
                                fc="#EAF6EA", ec=KANTO_GREEN, lw=2.0, zorder=2))
    ax.text(3.0, 6.95, "SUCCESSES: 4 Caterpie", ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=KANTO_GREEN, zorder=4)
    ax.text(3.0, 4.95, "choose  $\\binom{4}{2}=6$", ha="center", va="center",
            fontsize=12.5, color=INK, zorder=4)
    # Caterpie sprites inside the box header band (clear of the count below)
    for fx in [0.10, 0.18, 0.26, 0.34]:
        place_sprite(ax, front(10), (fx, 0.66), xycoords="axes fraction",
                     zoom=0.30, alpha=0.97, zorder=5)

    # failures box (right)
    ax.add_patch(FancyBboxPatch((6.7, 4.4), 4.6, 3.0,
                                boxstyle="round,pad=0.05,rounding_size=0.12",
                                fc="#FFEDED", ec=KANTO_RED, lw=2.0, zorder=2))
    ax.text(9.0, 6.95, "FAILURES: 6 others", ha="center", va="center",
            fontsize=10.5, fontweight="bold", color=KANTO_RED, zorder=4)
    ax.text(9.0, 4.95, "choose  $\\binom{6}{1}=6$", ha="center", va="center",
            fontsize=12.5, color=INK, zorder=4)
    # Weedle + Metapod sprites inside the failures box header band
    for fx, dex in [(0.60, 13), (0.68, 11), (0.76, 13), (0.84, 11)]:
        place_sprite(ax, front(dex), (fx, 0.66), xycoords="axes fraction",
                     zoom=0.30, alpha=0.97, zorder=5)

    # the AND multiply
    ax.text(6.0, 5.9, "x", ha="center", va="center", fontsize=18,
            fontweight="bold", color=INK, zorder=4)

    # result band
    ax.add_patch(FancyBboxPatch((0.7, 1.1), 10.6, 2.6,
                                boxstyle="round,pad=0.05,rounding_size=0.12",
                                fc="#FFFDF2", ec=ROCK, lw=2.0, zorder=2))
    ax.text(6.0, 3.05,
            f"favourable $= \\binom{{4}}{{2}}\\binom{{6}}{{1}} = 6\\cdot6 = "
            f"{favourable}$       over all hands $= \\binom{{10}}{{3}} = {total}$",
            ha="center", va="center", fontsize=11.5, color=INK, zorder=3)
    ax.text(6.0, 1.85,
            f"$P(\\text{{exactly }}2\\text{{ Caterpie}}) = "
            f"\\dfrac{{\\binom{{4}}{{2}}\\binom{{6}}{{1}}}}{{\\binom{{10}}{{3}}}} "
            f"= \\dfrac{{{favourable}}}{{{total}}} = {prob:.2f}$",
            ha="center", va="center", fontsize=13.5, color=KANTO_RED,
            fontweight="bold", zorder=3)
    fig.tight_layout()
    return save(fig, "ch04_hypergeo_forest")


REGISTRY = [
    fig_perm_vs_comb,
    fig_2x2_classifier,
    fig_binomial_flock,
    fig_hypergeo_forest,
]


def main() -> None:
    print(f"Generating Chapter 4 (Combinatorics) figures -> {OUT} "
          f"at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
