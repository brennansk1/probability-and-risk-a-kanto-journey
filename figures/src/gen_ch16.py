#!/usr/bin/env python3
"""Generate every Chapter 16 (Conditional & Double Expectation / Viridian Gym /
Giovanni unmasked) figure.

Manifest (MASTER_PLAN_V3 §16) — three required diagrams, all into assets/diagrams/:
  ch16_total_expectation_tree   Concept 2, Beat 8: a one-stage fan tree, leaf =
                                P(Y=y) x E[X|Y=y]; the three products
                                20, 21, 24 sum to E[X] = 65.
  ch16_total_variance_decomp    Concept 3, Beat 8: a two-row table (means /
                                variances) under the weights 0.5/0.3/0.2; Term 2
                                = Var(means) = 925, Term 1 = weighted-avg of
                                variances = 111.7; a stacked bar shows the
                                between-squad term dominating the 1036.7 total.
  ch16_mixture                  Concept 4, Beat 8: the conditional slices that a
                                hidden layer Y mixes into one unconditional
                                distribution of X, AND the compound-sum split of
                                Var(S) into size-noise lambda*sigma^2 = 2700 and
                                count-noise lambda*mu^2 = 7500 -> 10200.

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element
is ALSO distinguished by a hatch pattern / text label so figures survive grayscale
(color is never the sole channel). Sprites obey the IRON RULE: art in margins,
never over a curve, equation, axis, or number a reader must read. This is a
Ground-type chapter (Giovanni), so the figure accent leans on the §17 Ground
color via chapter_accent(16).

Run: python figures/src/gen_ch16.py
"""
from __future__ import annotations

from math import factorial
from pathlib import Path

import numpy as np
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
GROUND = chapter_accent(16)  # §17 Ground accent (banner/accent parity): #E0C068
INK = "#333333"

plt.rcParams["axes.prop_cycle"] = cycler(color=[
    KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN,
    "#FF7043", "#7B61FF", "#00BCD4", "#FF4081", "#8D6E63", "#78909C"])

PRINT_DPI = 300

# The three Giovanni squads: probability, conditional mean, conditional variance.
# dex matches the chapter story: Diglett-line scouts (#50), Nidoking-line regulars
# (#34), Rhydon-line elites (#112). Sprites are decorative only.
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
# 1. ch16_total_expectation_tree — total expectation as a one-stage fan tree.
#    Concept 2, Beat 8.
# --------------------------------------------------------------------------
def fig_total_expectation_tree():
    fig, ax = plt.subplots(figsize=(8.8, 6.6))
    fig.suptitle(r"Total expectation: each leaf is $P(Y{=}y)\times"
                 r"\mathrm{E}[X\mid Y{=}y]$" + "\n"
                 r"Giovanni's hidden squad $\to$ expected strength",
                 y=1.00, fontsize=13)
    ax.set_facecolor("white")
    ax.grid(False)
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    root = (1.0, 7.4)
    ax.plot(*root, marker="o", ms=16, color=GROUND,
            markeredgecolor=INK, markeredgewidth=1.4, zorder=4)
    ax.text(root[0], root[1] + 0.7, "before the\nball is thrown",
            ha="center", va="bottom", fontsize=10.5, color=INK)

    leaf_y = [8.9, 6.3, 3.7]
    leaf_x = 5.2
    products = []
    for sq, ly in zip(SQUADS, leaf_y):
        prod = sq["p"] * sq["mean"]
        products.append(prod)
        ax.annotate("", xy=(leaf_x - 0.55, ly), xytext=(root[0] + 0.25, root[1]),
                    arrowprops=dict(arrowstyle="-|>", color=sq["color"], lw=2.4))
        mx, my = (root[0] + leaf_x) / 2 - 0.2, (root[1] + ly) / 2
        ax.text(mx, my, rf"$P(Y{{=}}{sq['y']}){{=}}{sq['p']}$", ha="center",
                va="center", fontsize=10.5, color=sq["color"], fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.22", fc="white",
                          ec=sq["color"], lw=1.2))
        box = FancyBboxPatch((leaf_x - 0.5, ly - 0.55), 2.7, 1.1,
                             boxstyle="round,pad=0.04", fc=sq["color"],
                             alpha=0.30, ec=INK, lw=1.3, hatch=sq["hatch"])
        ax.add_patch(box)
        ax.text(leaf_x + 1.0, ly,
                rf"{sq['label']}" + "\n" +
                rf"$\mathrm{{E}}[X\mid Y{{=}}{sq['y']}]={sq['mean']}$",
                ha="center", va="center", fontsize=10.5, color=INK,
                fontweight="bold")
        place_sprite(ax, front(sq["dex"]), (leaf_x - 0.18, ly),
                     zoom=0.40, alpha=0.95)
        ax.annotate("", xy=(8.7, ly), xytext=(leaf_x + 2.3, ly),
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))
        ax.text(8.95, ly, rf"$= {prod:.0f}$", ha="left", va="center",
                fontsize=12, color=INK, fontweight="bold")

    ax.plot([9.25, 9.25], [3.7, 8.9], color=INK, lw=1.4)
    ax.annotate("", xy=(9.25, 1.8), xytext=(9.25, 3.5),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))
    total = sum(products)
    ax.text(9.25, 1.35,
            rf"$\mathrm{{E}}[X]={products[0]:.0f}+{products[1]:.0f}"
            rf"+{products[2]:.0f}={total:.0f}$",
            ha="center", va="top", fontsize=13.5, color=KANTO_RED,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.35", fc="#FFE0E0", ec=KANTO_RED,
                      lw=1.6))

    fig.tight_layout()
    return save(fig, "ch16_total_expectation_tree")


# --------------------------------------------------------------------------
# 2. ch16_total_variance_decomp — two-row table + stacked total-variance bar.
#    Concept 3, Beat 8.
# --------------------------------------------------------------------------
def fig_total_variance_decomp():
    fig, (axT, axB) = plt.subplots(
        1, 2, figsize=(12.2, 5.6), gridspec_kw={"width_ratios": [1.9, 1]})
    fig.suptitle(r"Total variance $=$ expected within-squad variance $+$ "
                 r"variance of the squad means", y=1.00, fontsize=13)

    # ---- LEFT: the two-row table.
    axT.set_facecolor("white")
    axT.grid(False)
    axT.axis("off")
    axT.set_xlim(0, 11.2)
    axT.set_ylim(0, 10.4)

    col_x = [3.4, 5.6, 7.8]
    row_mean_y = 7.0
    row_var_y = 4.6
    cell_w, cell_h = 1.9, 1.2

    axT.text(0.9, 8.6, "weight $P(Y)$", ha="left", va="center", fontsize=11,
             color=INK, fontweight="bold")
    for sq, cx in zip(SQUADS, col_x):
        place_sprite(axT, front(sq["dex"]), (cx, 9.55), zoom=0.34, alpha=0.95)
        axT.text(cx, 9.0, sq["label"], ha="center", va="center", fontsize=10.5,
                 color=sq["color"], fontweight="bold")
        axT.text(cx, 8.6, rf"${sq['p']}$", ha="center", va="center",
                 fontsize=12, color=INK, fontweight="bold")

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

    axT.annotate(r"$\mathrm{Var}(\text{row 1})$" + "\n" + r"Term 2 $= 925$",
                 xy=(col_x[-1] + cell_w / 2, row_mean_y),
                 xytext=(10.0, row_mean_y + 0.55),
                 arrowprops=dict(arrowstyle="-|>", color=KANTO_RED, lw=1.6),
                 fontsize=10.5, color=KANTO_RED, ha="center", va="center",
                 fontweight="bold",
                 bbox=dict(boxstyle="round,pad=0.28", fc="#FFE0E0",
                           ec=KANTO_RED, lw=1.4))
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
    term1 = 111.7
    term2 = 925.0
    total = term1 + term2
    bar_x = 0.5
    axB.bar(bar_x, term1, width=0.5, color=KANTO_BLUE, alpha=0.45,
            hatch="..", edgecolor=INK, lw=1.2,
            label=r"Term 1 (process): $\mathrm{E}[\mathrm{Var}(X\mid Y)]=111.7$")
    axB.bar(bar_x, term2, width=0.5, bottom=term1, color=KANTO_RED, alpha=0.45,
            hatch="xx", edgecolor=INK, lw=1.2,
            label=r"Term 2 (parameter): $\mathrm{Var}(\mathrm{E}[X\mid Y])=925$")
    axB.annotate("within-squad\nnoise (process, 111.7)",
                 xy=(bar_x + 0.25, term1 / 2),
                 xytext=(bar_x + 0.30, term1 + 175),
                 arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2),
                 ha="left", va="center", fontsize=8.6, color=INK,
                 fontweight="bold")
    axB.text(bar_x, term1 + term2 / 2, "which-squad\nspread\n(parameter,\ndominates)",
             ha="center", va="center", fontsize=9.5, color=INK,
             fontweight="bold")
    axB.text(bar_x, total + 35, rf"$\mathrm{{Var}}(X)={total:.1f}$",
             ha="center", va="bottom", fontsize=12.5, color=INK,
             fontweight="bold")
    axB.set_xlim(0, 1.35)
    axB.set_ylim(0, total * 1.18)
    axB.set_xticks([])
    axB.set_ylabel("variance")
    axB.set_title("Add, don't average", fontsize=12)
    axB.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), fontsize=8.2)

    fig.tight_layout()
    return save(fig, "ch16_total_variance_decomp")


# --------------------------------------------------------------------------
# 3. ch16_mixture — LEFT: the hidden layer mixing slices into one unconditional
#    distribution. RIGHT: the compound-sum Var(S) split (Concept 4, Beat 8).
# --------------------------------------------------------------------------
def fig_mixture():
    fig, (axL, axR) = plt.subplots(
        1, 2, figsize=(12.6, 5.8), gridspec_kw={"width_ratios": [1.7, 1]})
    fig.suptitle(r"A mixture: a hidden layer $Y$ blends slices into one $X$; "
                 r"a compound sum splits its variance", y=1.00, fontsize=13)

    # ---- LEFT: three component slices (dashed) + their probability-weighted
    #      mixture (solid). This is the compound/mixture distribution picture.
    axL.set_facecolor("white")
    axL.grid(False)
    for s in ("top", "right", "left"):
        axL.spines[s].set_visible(False)
    axL.set_yticks([])

    xs = np.linspace(0, 180, 900)
    mixture = np.zeros_like(xs)
    for sq in SQUADS:
        comp = np.exp(-0.5 * ((xs - sq["mean"]) / sq["sd"]) ** 2)
        comp = comp / (sq["sd"] * np.sqrt(2 * np.pi))  # proper normal density
        axL.plot(xs, comp * sq["p"], color=sq["color"], lw=1.8, ls="--",
                 alpha=0.9,
                 label=rf"{sq['label']} component $\times\,{sq['p']}$")
        mixture += sq["p"] * comp
    axL.plot(xs, mixture, color=INK, lw=2.6,
             label="mixture $f_X(x)$ (unconditional)")
    axL.fill_between(xs, 0, mixture, color=GROUND, alpha=0.22)

    # mark the unconditional mean E[X] = 65.
    axL.axvline(65, color=KANTO_GREEN, lw=1.6, ls=":")
    axL.text(65, mixture.max() * 1.04, r"$\mathrm{E}[X]=65$", ha="center",
             va="bottom", fontsize=10.5, color=KANTO_GREEN, fontweight="bold")
    axL.set_xlim(0, 180)
    axL.set_ylim(0, mixture.max() * 1.20)
    axL.set_xlabel("$x$  (Pokémon strength)")
    axL.set_xticks([40, 70, 120])
    axL.set_title("One distribution, three hidden components", fontsize=11.5)
    axL.legend(loc="upper right", fontsize=8.2)
    # decorative Giovanni-squad elite sprite in the top-left margin.
    place_sprite(axL, front(112), (12, mixture.max() * 1.06), zoom=0.34,
                 alpha=0.9)

    # ---- RIGHT: compound-sum Var(S) split into size-noise + count-noise.
    axR.set_facecolor("white")
    axR.grid(False)
    for s in ("top", "right"):
        axR.spines[s].set_visible(False)
    size_noise = 3 * 900       # E[N] sigma^2 = lambda sigma^2
    count_noise = 3 * 50 ** 2  # Var(N) mu^2  = lambda mu^2
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
    axR.set_title(r"Compound $S=\sum_1^N X_i$:" + "\n"
                  r"$\mathrm{Var}(S)=\mathrm{E}[N]\sigma^2+\mathrm{Var}(N)\mu^2$",
                  fontsize=10.5)
    axR.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), fontsize=8.6)

    fig.tight_layout()
    return save(fig, "ch16_mixture")


REGISTRY = [
    fig_total_expectation_tree,
    fig_total_variance_decomp,
    fig_mixture,
]


def main() -> None:
    print(f"Generating Chapter 16 (Conditional & Double Expectation) figures -> "
          f"{OUT} at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
