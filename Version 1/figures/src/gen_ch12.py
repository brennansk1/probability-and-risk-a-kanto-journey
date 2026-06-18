#!/usr/bin/env python3
"""Generate the Chapter 12 (Double Expectation / Viridian / Giovanni) math figures.

The chapter's nine-beat arcs each end on a "Picture it" beat whose <figure> needs
a purpose-built diagram. Two of the chapter's math PNGs already exist
(ch12_clt_convergence, ch12_order_stats); the four produced here back the
"Picture it" beats of the four core concepts and did NOT exist yet:

  ch12_conditional_slices       Concept 1, Beat 8: three stacked conditional
                                slices of X (centers 40, 70, 120 with widening
                                spread), and a separate E[X|Y] axis showing the
                                conditional mean as its OWN random variable
                                landing on 40/70/120 w.p. 0.5/0.3/0.2.
  ch12_total_expectation_tree   Concept 2, Beat 8: a one-stage fan tree, leaf =
                                P(Y=y) x E[X|Y=y]; the three products
                                20, 21, 24 sum to E[X] = 65.
  ch12_total_variance_table     Concept 3, Beat 8: a two-row table (means /
                                variances) under the weights 0.5/0.3/0.2; Term 2
                                = Var(means) = 925, Term 1 = weighted-avg of
                                variances = 111.7; a stacked bar shows the
                                between-squad term dominating the 1036.7 total.
  ch12_compound_tree            Concept 4, Beat 8: a random count N (Poisson)
                                branching into 0,1,2,3,... with that many i.i.d.
                                damage blocks stacked into S; a stacked bar
                                splits Var(S) into size-noise lambda*sigma^2 =
                                2700 and count-noise lambda*mu^2 = 7500 -> 10200.

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element
ALSO carries a label / hatch / distinct shape, so the figures stay legible in
grayscale.

Run: python figures/src/gen_ch12.py
"""
from __future__ import annotations

from math import factorial
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle, FancyBboxPatch
from cycler import cycler

from sprite_util import front, place_sprite

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

# The three Giovanni squads: probability, conditional mean, conditional variance.
# dex matches the Gym-Battle tier story: scouts (Diglett #50), regulars
# (Nidoking #34), elites (Rhydon #112). Sprites are decorative only.
SQUADS = [
    {"y": 1, "p": 0.5, "mean": 40, "var": 25,  "sd": 5,  "color": KANTO_BLUE,
     "hatch": "//",  "label": "Squad 1", "dex": 50},
    {"y": 2, "p": 0.3, "mean": 70, "var": 64,  "sd": 8,  "color": KANTO_GREEN,
     "hatch": "..",  "label": "Squad 2", "dex": 34},
    {"y": 3, "p": 0.2, "mean": 120, "var": 400, "sd": 20, "color": KANTO_RED,
     "hatch": "xx",  "label": "Squad 3", "dex": 112},
]


def save(fig, name: str) -> Path:
    path = OUT / f"{name}.png"
    fig.savefig(path, dpi=PRINT_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [fig] {path.relative_to(ROOT)}")
    return path


# --------------------------------------------------------------------------
# 1. Concept 1, Beat 8: three conditional slices + E[X|Y] as a random variable.
# --------------------------------------------------------------------------
def fig_conditional_slices():
    fig, (axL, axR) = plt.subplots(
        1, 2, figsize=(11.5, 5.6), gridspec_kw={"width_ratios": [1.7, 1]})
    fig.suptitle(r"Conditioning selects a slice; its center $\mathrm{E}[X\mid Y]$"
                 r" is itself random", y=1.00)

    # LEFT: three stacked conditional densities of X, one per squad.
    axL.set_facecolor("white")
    axL.grid(False)
    for s in ("top", "right", "left"):
        axL.spines[s].set_visible(False)
    axL.set_yticks([])

    xs = np.linspace(0, 170, 700)
    # vertical offset per slice so the bumps stack without overlapping.
    offsets = [0.0, 1.0, 2.0]
    peak = 0.85  # height of the tallest bump in offset units

    for sq, off in zip(SQUADS, offsets):
        pdf = np.exp(-0.5 * ((xs - sq["mean"]) / sq["sd"]) ** 2)
        pdf = pdf / pdf.max() * peak                      # normalize bump height
        axL.fill_between(xs, off, off + pdf, color=sq["color"], alpha=0.45,
                         hatch=sq["hatch"], edgecolor=INK, lw=1.0)
        axL.plot(xs, off + pdf, color=sq["color"], lw=2.0)
        axL.axhline(off, color=INK, lw=0.8)
        # vertical tick at the center g(y) = E[X|Y=y]
        axL.plot([sq["mean"], sq["mean"]], [off, off + peak], color=INK,
                 lw=1.8, ls="--")
        axL.plot(sq["mean"], off + peak, marker="v", color=INK, ms=8)
        # center label sits just left of the peak marker, hugging its own bump
        # so it never collides with the slice stacked above it.
        axL.text(sq["mean"] - 6, off + peak + 0.06,
                 rf"$g({sq['y']})={sq['mean']}$", ha="right", va="bottom",
                 fontsize=11, color=INK, fontweight="bold")
        # label and sprite both live in the far-left margin (x < ~22, left of
        # every bump's rising flank), stacked so neither crosses a curve.
        axL.text(20, off + peak * 0.30,
                 rf"$X\mid Y={sq['y']}$" + f"\n(w.p. {sq['p']})",
                 ha="left", va="center", fontsize=10, color=sq["color"],
                 fontweight="bold")
        place_sprite(axL, front(sq["dex"]), (8, off + peak * 0.32),
                     zoom=0.40, alpha=0.95)

    axL.set_xlim(0, 175)
    axL.set_ylim(-0.1, offsets[-1] + peak + 0.55)
    axL.set_xlabel("$x$  (Pokémon strength)")
    axL.set_title("Three conditional slices of $X$", fontsize=12.5)
    axL.set_xticks([40, 70, 120])

    # RIGHT: the conditional mean E[X|Y] plotted as its own random variable.
    axR.set_facecolor("white")
    axR.grid(False)
    for s in ("top", "right"):
        axR.spines[s].set_visible(False)
    axR.set_xticks([])
    axR.set_xlim(-0.6, 1.5)
    axR.set_ylim(0, 175)
    axR.set_ylabel(r"$\mathrm{E}[X\mid Y]$", fontsize=13)
    axR.set_title("A random variable\nwith 3 values", fontsize=12.5)

    for sq in SQUADS:
        # marker size encodes probability so it reads in grayscale too.
        axR.plot(0, sq["mean"], marker="o", ms=10 + 34 * sq["p"],
                 color=sq["color"], markeredgecolor=INK, markeredgewidth=1.2,
                 zorder=3)
        axR.plot([-0.55, 0], [sq["mean"], sq["mean"]], color=sq["color"],
                 lw=1.2, ls=":")
        axR.text(0.18, sq["mean"],
                 rf"${sq['mean']}$  (w.p. ${sq['p']}$)", va="center",
                 ha="left", fontsize=11, color=INK, fontweight="bold")
    axR.set_yticks([40, 70, 120])

    fig.tight_layout()
    return save(fig, "ch12_conditional_slices")


# --------------------------------------------------------------------------
# 2. Concept 2, Beat 8: total expectation as a one-stage fan tree.
# --------------------------------------------------------------------------
def fig_total_expectation_tree():
    fig, ax = plt.subplots(figsize=(8.6, 6.4))
    fig.suptitle(r"Total expectation: each leaf is $P(Y{=}y)\times"
                 r"\mathrm{E}[X\mid Y{=}y]$", y=0.99)
    ax.set_facecolor("white")
    ax.grid(False)
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    root = (1.0, 7.6)
    ax.plot(*root, marker="o", ms=16, color=KANTO_YEL,
            markeredgecolor=INK, markeredgewidth=1.4, zorder=4)
    ax.text(root[0], root[1] + 0.7, "before the\nball is thrown",
            ha="center", va="bottom", fontsize=10.5, color=INK)

    leaf_y = [9.0, 6.4, 3.8]
    leaf_x = 5.2
    products = []
    for sq, ly in zip(SQUADS, leaf_y):
        prod = sq["p"] * sq["mean"]
        products.append(prod)
        # branch
        ax.annotate("", xy=(leaf_x - 0.55, ly), xytext=(root[0] + 0.25, root[1]),
                    arrowprops=dict(arrowstyle="-|>", color=sq["color"], lw=2.4))
        # probability label on the branch
        mx, my = (root[0] + leaf_x) / 2 - 0.2, (root[1] + ly) / 2
        ax.text(mx, my, rf"$P(Y{{=}}{sq['y']}){{=}}{sq['p']}$", ha="center",
                va="center", fontsize=10.5, color=sq["color"], fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.22", fc="white",
                          ec=sq["color"], lw=1.2))
        # leaf box: squad label + conditional mean
        box = FancyBboxPatch((leaf_x - 0.5, ly - 0.55), 2.7, 1.1,
                             boxstyle="round,pad=0.04", fc=sq["color"],
                             alpha=0.30, ec=INK, lw=1.3, hatch=sq["hatch"])
        ax.add_patch(box)
        ax.text(leaf_x + 1.0, ly,
                rf"{sq['label']}" + "\n" +
                rf"$\mathrm{{E}}[X\mid Y{{=}}{sq['y']}]={sq['mean']}$",
                ha="center", va="center", fontsize=10.5, color=INK,
                fontweight="bold")
        # decorative species sprite in the leaf box's left corner.
        place_sprite(ax, front(sq["dex"]), (leaf_x - 0.18, ly),
                     zoom=0.40, alpha=0.95)
        # product on the branch -> sent to the summation column
        ax.annotate("", xy=(8.7, ly), xytext=(leaf_x + 2.3, ly),
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))
        ax.text(8.95, ly, rf"$= {prod:.0f}$", ha="left", va="center",
                fontsize=12, color=INK, fontweight="bold")

    # summation bracket at the bottom
    ax.plot([9.25, 9.25], [3.8, 9.0], color=INK, lw=1.4)
    ax.annotate("", xy=(9.25, 1.9), xytext=(9.25, 3.6),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))
    total = sum(products)
    ax.text(9.25, 1.45,
            rf"$\mathrm{{E}}[X]={products[0]:.0f}+{products[1]:.0f}"
            rf"+{products[2]:.0f}={total:.0f}$",
            ha="center", va="top", fontsize=13.5, color=KANTO_RED,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.35", fc="#FFE0E0", ec=KANTO_RED,
                      lw=1.6))

    fig.tight_layout()
    return save(fig, "ch12_total_expectation_tree")


# --------------------------------------------------------------------------
# 3. Concept 3, Beat 8: two-row table + stacked total-variance bar.
# --------------------------------------------------------------------------
def fig_total_variance_table():
    fig, (axT, axB) = plt.subplots(
        1, 2, figsize=(12.2, 5.6), gridspec_kw={"width_ratios": [1.9, 1]})
    fig.suptitle(r"Total variance $=$ weighted-avg of variances $+$ variance of"
                 r" means", y=1.00)

    # ---- LEFT: the two-row table.
    axT.set_facecolor("white")
    axT.grid(False)
    axT.axis("off")
    axT.set_xlim(0, 11.2)
    axT.set_ylim(0, 10.4)

    col_x = [3.4, 5.6, 7.8]          # one column per squad
    row_mean_y = 7.0
    row_var_y = 4.6
    cell_w, cell_h = 1.9, 1.2

    # header: weights
    axT.text(0.9, 8.6, "weight $P(Y)$", ha="left", va="center", fontsize=11,
             color=INK, fontweight="bold")
    for sq, cx in zip(SQUADS, col_x):
        # decorative species sprite above each column header.
        place_sprite(axT, front(sq["dex"]), (cx, 9.55), zoom=0.34, alpha=0.95)
        axT.text(cx, 9.0, sq["label"], ha="center", va="center", fontsize=10.5,
                 color=sq["color"], fontweight="bold")
        axT.text(cx, 8.6, rf"${sq['p']}$", ha="center", va="center",
                 fontsize=12, color=INK, fontweight="bold")

    # row labels
    axT.text(0.9, row_mean_y, r"cond. mean" + "\n" + r"$\mathrm{E}[X\mid Y{=}y]$",
             ha="left", va="center", fontsize=10.5, color=INK, fontweight="bold")
    axT.text(0.9, row_var_y, r"cond. var" + "\n" + r"$\mathrm{Var}(X\mid Y{=}y)$",
             ha="left", va="center", fontsize=10.5, color=INK, fontweight="bold")

    for sq, cx in zip(SQUADS, col_x):
        for val, ry in ((sq["mean"], row_mean_y), (sq["var"], row_var_y)):
            axT.add_patch(Rectangle((cx - cell_w / 2, ry - cell_h / 2),
                                    cell_w, cell_h, facecolor=sq["color"],
                                    alpha=0.28, edgecolor=INK, lw=1.2,
                                    hatch=sq["hatch"]))
            axT.text(cx, ry, rf"${val}$", ha="center", va="center",
                     fontsize=13, color=INK, fontweight="bold")

    # arrow: variance of row 1 -> Term 2 (box parked far right, below the
    # header row so it never overlaps the Squad-3 weight label).
    axT.annotate(r"$\mathrm{Var}(\text{row 1})$" + "\n" + r"Term 2 $= 925$",
                 xy=(col_x[-1] + cell_w / 2, row_mean_y),
                 xytext=(10.0, row_mean_y + 0.55),
                 arrowprops=dict(arrowstyle="-|>", color=KANTO_RED, lw=1.6),
                 fontsize=10.5, color=KANTO_RED, ha="center", va="center",
                 fontweight="bold",
                 bbox=dict(boxstyle="round,pad=0.28", fc="#FFE0E0",
                           ec=KANTO_RED, lw=1.4))
    # arrow: weighted average of row 2 -> Term 1
    axT.annotate(r"wtd avg of row 2" + "\n" + r"Term 1 $= 111.7$",
                 xy=(col_x[-1] + cell_w / 2, row_var_y),
                 xytext=(10.0, row_var_y - 0.55),
                 arrowprops=dict(arrowstyle="-|>", color=KANTO_BLUE, lw=1.6),
                 fontsize=10.5, color=KANTO_BLUE, ha="center", va="center",
                 fontweight="bold",
                 bbox=dict(boxstyle="round,pad=0.28", fc="#E0E6FF",
                           ec=KANTO_BLUE, lw=1.4))

    # ---- RIGHT: stacked total-variance bar.
    axB.set_facecolor("white")
    axB.grid(False)
    for s in ("top", "right"):
        axB.spines[s].set_visible(False)
    term1 = 111.7    # E[Var(X|Y)] within-squad noise
    term2 = 925.0    # Var(E[X|Y]) which-squad spread
    total = term1 + term2
    bar_x = 0.5
    axB.bar(bar_x, term1, width=0.5, color=KANTO_BLUE, alpha=0.45,
            hatch="..", edgecolor=INK, lw=1.2,
            label=r"Term 1: $\mathrm{E}[\mathrm{Var}(X\mid Y)]=111.7$")
    axB.bar(bar_x, term2, width=0.5, bottom=term1, color=KANTO_RED, alpha=0.45,
            hatch="xx", edgecolor=INK, lw=1.2,
            label=r"Term 2: $\mathrm{Var}(\mathrm{E}[X\mid Y])=925$")
    # the within-squad segment is tiny; label it with an external callout to
    # the RIGHT (clear space) so the text is never clipped by the small bar.
    axB.annotate("within-squad\nnoise (111.7)",
                 xy=(bar_x + 0.25, term1 / 2),
                 xytext=(bar_x + 0.30, term1 + 175),
                 arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2),
                 ha="left", va="center", fontsize=8.6, color=INK,
                 fontweight="bold")
    axB.text(bar_x, term1 + term2 / 2, "which-squad\nspread\n(dominates)",
             ha="center", va="center", fontsize=10, color=INK,
             fontweight="bold")
    axB.text(bar_x, total + 35, rf"$\mathrm{{Var}}(X)={total:.1f}$",
             ha="center", va="bottom", fontsize=12.5, color=INK,
             fontweight="bold")
    axB.set_xlim(0, 1.35)
    axB.set_ylim(0, total * 1.18)
    axB.set_xticks([])
    axB.set_ylabel("variance")
    axB.set_title("Add, don't average", fontsize=12)
    axB.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), fontsize=8.6)

    fig.tight_layout()
    return save(fig, "ch12_total_variance_table")


# --------------------------------------------------------------------------
# 4. Concept 4, Beat 8: compound sum tree + Var(S) split into the two terms.
# --------------------------------------------------------------------------
def fig_compound_tree():
    fig, (axL, axR) = plt.subplots(
        1, 2, figsize=(12.4, 5.8), gridspec_kw={"width_ratios": [1.9, 1]})
    fig.suptitle(r"Compound sum $S=\sum_{i=1}^{N}X_i$: a random count of random"
                 r" sizes", y=1.00)

    # ---- LEFT: random count N branches into 0,1,2,3 with i.i.d. blocks below.
    axL.set_facecolor("white")
    axL.grid(False)
    axL.axis("off")
    axL.set_xlim(0, 10)
    axL.set_ylim(0, 10)

    root = (5.0, 9.3)
    axL.plot(*root, marker="o", ms=15, color=KANTO_YEL,
             markeredgecolor=INK, markeredgewidth=1.4, zorder=4)
    axL.text(root[0], root[1] + 0.45,
             r"count $N\sim\mathrm{Poisson}(\lambda{=}3)$",
             ha="center", va="bottom", fontsize=11, color=INK, fontweight="bold")
    # decorative Rhydon (#112) in the top-left margin — it lands the Horn Drills.
    place_sprite(axL, front(112), (1.0, 9.0), zoom=0.5, alpha=0.95)

    # Poisson(3) weights for n = 0,1,2,3 ; "..." for the tail.
    counts = [0, 1, 2, 3]
    lam = 3.0
    weights = [np.exp(-lam) * lam ** n / factorial(n) for n in counts]
    branch_x = [1.3, 3.6, 5.9, 8.2]
    head_y = 7.6
    block_w, block_h, block_gap = 0.9, 0.42, 0.12

    for n, bx, w in zip(counts, branch_x, weights):
        axL.annotate("", xy=(bx, head_y + 0.25), xytext=(root[0], root[1] - 0.2),
                     arrowprops=dict(arrowstyle="-|>", color=KANTO_GRAY, lw=1.6))
        # N=n label with its Poisson weight
        axL.text(bx, head_y + 0.02, rf"$N{{=}}{n}$",
                 ha="center", va="top", fontsize=11, color=INK,
                 fontweight="bold")
        axL.text(bx, head_y - 0.42, f"(w.p. {w:.2f})", ha="center", va="top",
                 fontsize=8.6, color=KANTO_GRAY)
        # stack n i.i.d. damage blocks beneath this branch
        top = head_y - 1.05
        for i in range(n):
            by = top - i * (block_h + block_gap)
            axL.add_patch(Rectangle((bx - block_w / 2, by - block_h),
                                    block_w, block_h, facecolor=KANTO_BLUE,
                                    alpha=0.40, edgecolor=INK, lw=1.0,
                                    hatch="//"))
            axL.text(bx, by - block_h / 2, rf"$X_{i+1}$", ha="center",
                     va="center", fontsize=8.6, color=INK)
        if n == 0:
            axL.text(bx, top - 0.3, r"$S=0$", ha="center", va="center",
                     fontsize=9.5, color=INK)
    # the random tail
    axL.text(branch_x[-1] + 1.3, head_y - 0.2, r"$\cdots$", ha="center",
             va="center", fontsize=18, color=KANTO_GRAY)
    axL.text(5.0, 0.7,
             r"$S=X_1+\cdots+X_N$,  each $X_i$ i.i.d. "
             r"($\mu{=}50,\ \sigma^2{=}900$)",
             ha="center", va="center", fontsize=10.5, color=INK,
             fontweight="bold")

    # ---- RIGHT: Var(S) split into size-noise + count-noise.
    axR.set_facecolor("white")
    axR.grid(False)
    for s in ("top", "right"):
        axR.spines[s].set_visible(False)
    size_noise = 3 * 900     # lambda * sigma^2 = E[N] sigma^2
    count_noise = 3 * 50**2  # lambda * mu^2     = Var(N) mu^2
    total = size_noise + count_noise
    bar_x = 0.5
    axR.bar(bar_x, size_noise, width=0.5, color=KANTO_BLUE, alpha=0.45,
            hatch="//", edgecolor=INK, lw=1.2,
            label=r"size noise $\mathrm{E}[N]\sigma^2=2700$")
    axR.bar(bar_x, count_noise, width=0.5, bottom=size_noise, color=KANTO_RED,
            alpha=0.45, hatch="xx", edgecolor=INK, lw=1.2,
            label=r"count noise $\mathrm{Var}(N)\mu^2=7500$")
    axR.text(bar_x, size_noise / 2, "how big\neach hit is", ha="center",
             va="center", fontsize=9.5, color=INK, fontweight="bold")
    axR.text(bar_x, size_noise + count_noise / 2,
             "how many\nhits land\n(dominates)", ha="center", va="center",
             fontsize=9.5, color=INK, fontweight="bold")
    axR.text(bar_x, total + 350, rf"$\mathrm{{Var}}(S)={total:,}$",
             ha="center", va="bottom", fontsize=12.5, color=INK,
             fontweight="bold")
    axR.set_xlim(0, 1.0)
    axR.set_ylim(0, total * 1.18)
    axR.set_xticks([])
    axR.set_ylabel("variance of total damage")
    axR.set_title(r"$\mathrm{Var}(S)=\mathrm{E}[N]\sigma^2+\mathrm{Var}(N)\mu^2$",
                  fontsize=11.5)
    axR.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), fontsize=9)

    fig.tight_layout()
    return save(fig, "ch12_compound_tree")


REGISTRY = [
    fig_conditional_slices,
    fig_total_expectation_tree,
    fig_total_variance_table,
    fig_compound_tree,
]


def main() -> None:
    print(f"Generating Chapter 12 (Double Expectation) figures -> {OUT} "
          f"at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
