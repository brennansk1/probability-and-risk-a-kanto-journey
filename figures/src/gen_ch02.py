#!/usr/bin/env python3
"""Generate every Chapter 2 (Conditional Probability & Bayes / Cerulean / Misty) figure.

Manifest (MASTER_PLAN_V3 §16) — four required diagrams, all into assets/diagrams/:
  ch02_bayes_grid       the detective's grid (prior x likelihood -> posterior), Sick-Staryu
  ch02_tree_sequential  the without-replacement multiplication tree (Brock's bag)
  ch02_total_prob       Misty's lead fan: law of total probability (weighted leaves)
  ch02_false_positive   base-rate / false-positive area visual (Sick-Staryu test)

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is
ALSO distinguished by a hatch pattern / text label so figures survive grayscale
(color is never the sole channel). Sprites obey the IRON RULE: art in margins, never
over a curve, equation, axis, or number a reader must read.

Run: python figures/src/gen_ch02.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch, FancyBboxPatch, Patch
from cycler import cycler

from sprite_util import front, item, place_sprite

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents) — Water-type chapter, so the
# accent leans on KANTO_BLUE (Water #6890F0 in the §17 type map, here the deeper
# Kanto blue for ink contrast).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
WATER = "#6890F0"  # §17 Water accent (banner/accent parity)
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
    """Strip a panel down to a clean drawing surface (no grid/ticks/spines)."""
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_facecolor("white")
    ax.grid(False)


# --------------------------------------------------------------------------
# 1. ch02_bayes_grid — the detective's grid (prior x likelihood -> posterior).
#    Sick-Staryu Brineflux test (Concept 6 / Worked Example 1).
# --------------------------------------------------------------------------
def fig_bayes_grid():
    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.6)
    ax.set_title("The detective's grid: multiply across, normalize down\n"
                 "Did the Staryu actually catch Brineflux?", fontsize=13.5)

    cols = ["Cause", "Prior", "Likelihood\n$P(+\\mid\\cdot)$",
            "Joint\n$=$ Prior $\\times$ Like.", "Posterior\n$=$ Joint $/$ total"]
    # Sick-Staryu numbers (Concept 6 / WE 1):
    #   Sick:    prior 0.02, P(+|D)=0.95 -> joint 0.0190
    #   Healthy: prior 0.98, P(+|Dc)=0.08 -> joint 0.0784
    #   total P(+) = 0.0974; posteriors 0.195 / 0.805.
    rows = [
        ("Sick", 0.02, 0.95, 0.0190, KANTO_RED, "xx"),
        ("Healthy", 0.98, 0.08, 0.0784, WATER, "//"),
    ]
    total_joint = sum(r[3] for r in rows)

    x_edges = [0.3, 2.5, 4.3, 6.3, 8.7, 11.7]
    y_top = 6.0
    hh = 1.05   # header height
    rh = 1.35   # data row height

    for j, c in enumerate(cols):
        ax.add_patch(Rectangle((x_edges[j], y_top), x_edges[j + 1] - x_edges[j],
                               hh, facecolor=KANTO_GRAY, edgecolor=INK,
                               lw=1.3, alpha=0.9))
        ax.text((x_edges[j] + x_edges[j + 1]) / 2, y_top + hh / 2, c,
                ha="center", va="center", fontsize=9.5, color="white",
                fontweight="bold")

    y_sick = y_top - rh + rh / 2
    for i, (name, prior, like, joint, color, hatch) in enumerate(rows):
        y = y_top - (i + 1) * rh
        post = joint / total_joint
        vals = [name, f"{prior:.2f}", f"{like:.2f}", f"{joint:.4f}",
                f"{post:.3f}"]
        for j, v in enumerate(vals):
            fc = color if j == 0 else "white"
            ax.add_patch(Rectangle((x_edges[j], y),
                                   x_edges[j + 1] - x_edges[j], rh,
                                   facecolor=fc, edgecolor=INK, lw=1.2,
                                   alpha=0.9 if j == 0 else 1.0,
                                   hatch=hatch if j == 0 else None))
            ax.text((x_edges[j] + x_edges[j + 1]) / 2, y + rh / 2, v,
                    ha="center", va="center", fontsize=11.5,
                    color="white" if j == 0 else INK,
                    fontweight="bold" if j in (0, 4) else "normal")

    # "multiply across" arrow in the header gap, never crossing the numbers.
    ax.annotate("", xy=(x_edges[3] + 0.05, y_top - 0.12),
                xytext=(x_edges[1] + 0.2, y_top - 0.12),
                arrowprops=dict(arrowstyle="->", color=KANTO_GREEN, lw=2.0))
    ax.text((x_edges[1] + x_edges[3]) / 2, y_top + 0.06, "multiply across",
            ha="center", va="bottom", fontsize=9, color=KANTO_GREEN,
            fontweight="bold")

    # joint-column total = P(evidence) band.
    y_tot = y_top - 2 * rh - hh
    ax.add_patch(Rectangle((x_edges[3], y_tot), x_edges[4] - x_edges[3], hh,
                           facecolor=KANTO_YEL, edgecolor=INK, lw=1.3, alpha=0.6,
                           hatch=".."))
    ax.text((x_edges[3] + x_edges[4]) / 2, y_tot + hh / 2,
            f"$P(+)={total_joint:.4f}$", ha="center", va="center",
            fontsize=11, color=INK, fontweight="bold")
    ax.annotate("", xy=((x_edges[3] + x_edges[4]) / 2, y_tot + hh + 0.02),
                xytext=((x_edges[3] + x_edges[4]) / 2, y_top - 2 * rh - 0.02),
                arrowprops=dict(arrowstyle="-", color=KANTO_YEL, lw=2.2))
    ax.text((x_edges[3] + x_edges[4]) / 2, y_tot - 0.28,
            "sum the joint column", ha="center", fontsize=9, color=INK,
            style="italic")

    # divide -> posterior arrow in the right margin (clear of numbers).
    ax.annotate("", xy=((x_edges[4] + x_edges[5]) / 2, y_top - 2 * rh - 0.05),
                xytext=((x_edges[4] + x_edges[5]) / 2, y_tot + hh + 0.02),
                arrowprops=dict(arrowstyle="->", color=KANTO_GREEN, lw=1.8))
    ax.text(x_edges[5] - 0.05, (y_tot + y_top - 2 * rh) / 2 + 0.1,
            "each joint\n$\\div\\,P(+)$", ha="right", va="center",
            fontsize=8.5, color=KANTO_GREEN, fontweight="bold")

    psum = sum(r[3] for r in rows) / total_joint
    p_sick = rows[0][3] / total_joint
    p_heal = rows[1][3] / total_joint
    ax.text(6.0, 0.35,
            f"Self-check: posteriors sum to {psum:.0f}   "
            f"({p_sick:.3f} + {p_heal:.3f} = 1.000)  "
            r"$\Rightarrow$ a positive scan is still only $\approx 19.5\%$ sick",
            ha="center", fontsize=10, color=KANTO_GREEN, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="#E8F5E9", ec=KANTO_GREEN,
                      lw=1.4))

    # decorative Staryu in the Sick cell's top-left corner (clear of the
    # centered "Sick" label).
    place_sprite(ax, front(120), (x_edges[0] + 0.32, y_sick + rh * 0.32),
                 zoom=0.26, alpha=0.9, zorder=6)

    fig.tight_layout()
    return save(fig, "ch02_bayes_grid")


# --------------------------------------------------------------------------
# 2. ch02_tree_sequential — without-replacement multiplication tree (Brock's bag).
# --------------------------------------------------------------------------
def fig_tree_sequential():
    fig, ax = plt.subplots(figsize=(11, 6.4))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.set_title("Multiplication rule as a tree: 2 draws, no replacement\n"
                 "7 Poke Balls, 3 Great Balls", fontsize=14)

    root = (1.0, 4.5)

    def node(x, y, label, color, hatch):
        ax.add_patch(Circle((x, y), 0.42, facecolor=color, edgecolor=INK,
                            lw=1.4, alpha=0.9, hatch=hatch, zorder=3))
        ax.text(x, y, label, ha="center", va="center", fontsize=10,
                fontweight="bold", color=INK, zorder=4)

    def edge(p0, p1, label, color):
        ax.annotate("", xy=p1, xytext=p0,
                    arrowprops=dict(arrowstyle="-", color=color, lw=2.2))
        mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2
        ax.text(mx, my, label, ha="center", va="center", fontsize=10,
                color=INK, bbox=dict(boxstyle="round,pad=0.18", fc="white",
                                     ec=color, lw=1.2))

    node(*root, "start", KANTO_GRAY, "")

    p_pos = (4.2, 6.6)   # first = Poke
    g_pos = (4.2, 2.4)   # first = Great
    edge(root, p_pos, "$7/10$", KANTO_RED)
    edge(root, g_pos, "$3/10$", KANTO_BLUE)
    node(*p_pos, "Poke", KANTO_RED, "..")
    node(*g_pos, "Great", KANTO_BLUE, "oo")

    leaves = [
        (p_pos, (8.4, 7.7), "$6/9$", KANTO_RED, "..", "Poke",
         r"$\frac{7}{10}\cdot\frac{6}{9}=\frac{42}{90}$"),
        (p_pos, (8.4, 5.6), "$3/9$", KANTO_BLUE, "oo", "Great",
         r"$\frac{7}{10}\cdot\frac{3}{9}=\frac{21}{90}$"),
        (g_pos, (8.4, 3.3), "$7/9$", KANTO_RED, "..", "Poke",
         r"$\frac{3}{10}\cdot\frac{7}{9}=\frac{21}{90}$"),
        (g_pos, (8.4, 1.2), "$2/9$", KANTO_BLUE, "oo", "Great",
         r"$\frac{3}{10}\cdot\frac{2}{9}=\frac{6}{90}$"),
    ]
    for parent, pos, frac, color, hatch, lab, path in leaves:
        edge(parent, pos, frac, color)
        node(*pos, lab, color, hatch)
        ax.text(pos[0] + 0.65, pos[1], path, ha="left", va="center",
                fontsize=11, color=INK)

    # left-margin legend with item sprites.
    place_sprite(ax, item("poke-ball"), (0.55, 7.9), zoom=0.45, alpha=0.95)
    ax.text(1.05, 7.9, "= Poke Ball", ha="left", va="center", fontsize=9,
            color=INK)
    place_sprite(ax, item("great-ball"), (0.55, 7.2), zoom=0.45, alpha=0.95)
    ax.text(1.05, 7.2, "= Great Ball", ha="left", va="center", fontsize=9,
            color=INK)

    ax.text(6.0, 0.2,
            "Each leaf = product along its path; the four leaves sum to "
            r"$90/90=1$",
            ha="center", fontsize=10, style="italic", color=INK)
    fig.tight_layout()
    return save(fig, "ch02_tree_sequential")


# --------------------------------------------------------------------------
# 3. ch02_total_prob — Misty's lead fan: law of total probability.
# --------------------------------------------------------------------------
def fig_total_prob():
    fig, ax = plt.subplots(figsize=(10.5, 6.0))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_title("Law of total probability: sum the weighted leaves\n"
                 "Misty's lead -> chance her opener is super-effective",
                 fontsize=13.5)

    root = (1.2, 4.0)
    ax.add_patch(Circle((root[0], root[1]), 0.42, facecolor=KANTO_GRAY,
                        edgecolor=INK, lw=1.4, zorder=3))
    ax.text(root[0], root[1], "lead", ha="center", va="center", fontsize=9,
            fontweight="bold", color=INK, zorder=4)

    # (name, prior, super-effective rate, y, color, hatch, dex)
    branches = [
        ("Staryu", 0.5, 0.30, 6.3, KANTO_BLUE, "//", 120),
        ("Starmie", 0.3, 0.60, 4.0, KANTO_RED, "xx", 121),
        ("Psyduck", 0.2, 0.10, 1.7, KANTO_YEL, "..", 54),
    ]
    total = 0.0
    for name, prior, like, y, color, hatch, dex in branches:
        tip = (5.6, y)
        ax.annotate("", xy=tip, xytext=(root[0] + 0.4, root[1]),
                    arrowprops=dict(arrowstyle="-", color=color, lw=2.4))
        ax.text((root[0] + tip[0]) / 2, (root[1] + y) / 2 + 0.25,
                f"$P=${prior}", ha="center", fontsize=10, color=INK,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec=color, lw=1))
        ax.add_patch(Circle((tip[0], y), 0.45, facecolor=color, edgecolor=INK,
                            lw=1.4, alpha=0.85, hatch=hatch, zorder=3))
        ax.text(tip[0], y, name, ha="center", va="center", fontsize=8.5,
                fontweight="bold", color=INK, zorder=4)
        # species sprite in the white gap, nudged off its own branch line.
        sx = 4.3
        sy = y - 0.62 if abs(y - root[1]) < 0.5 else (
            y - 0.30 if y > root[1] else y + 0.30)
        place_sprite(ax, front(dex), (sx, sy), zoom=0.32, alpha=0.92, zorder=4)
        contrib = prior * like
        total += contrib
        ax.text(tip[0] + 0.7, y,
                f"super-eff. rate $={like}$\n"
                f"weight $= {prior}\\times{like} = {contrib:.2f}$",
                ha="left", va="center", fontsize=10, color=INK)

    ax.text(6.0, 0.4,
            f"$P(\\text{{super-effective}}) = 0.15+0.18+0.02 = {total:.2f}$",
            ha="center", fontsize=13, fontweight="bold", color=KANTO_GREEN,
            bbox=dict(boxstyle="round,pad=0.35", fc="#E8F5E9",
                      ec=KANTO_GREEN, lw=1.5))
    fig.tight_layout()
    return save(fig, "ch02_total_prob")


# --------------------------------------------------------------------------
# 4. ch02_false_positive — base-rate / false-positive area visual.
# --------------------------------------------------------------------------
def fig_false_positive():
    fig, ax = plt.subplots(figsize=(10.5, 6.4))
    _blank(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.0, 9.2)
    ax.set_title("Why a positive scan can still mean 'probably healthy'\n"
                 "Base rate 2% sick, 95% sensitivity, 8% false-positive rate",
                 fontsize=13)

    # 10,000 Water Pokemon: 200 sick, 9,800 healthy. Widths are NOT to base-rate
    # scale (2% is unreadably thin); we use a legible split and label the true
    # population counts explicitly.
    sick_w = 1.6
    heal_w = 8.4
    H = 7.5
    y0 = 0.6

    # Sick block (200): true positives 95% -> 190, false negatives 5% -> 10.
    tp_h = 0.95 * H
    ax.add_patch(Rectangle((0, y0), sick_w, tp_h, facecolor=KANTO_RED,
                           edgecolor=INK, lw=1.2, alpha=0.85, hatch="xx"))
    ax.add_patch(Rectangle((0, y0 + tp_h), sick_w, H - tp_h, facecolor=KANTO_RED,
                           edgecolor=INK, lw=1.2, alpha=0.22))

    # Healthy block (9,800): false positives 8% -> 784, true negatives -> 9,016.
    fp_h = 0.08 * H
    ax.add_patch(Rectangle((sick_w, y0), heal_w, fp_h, facecolor=WATER,
                           edgecolor=INK, lw=1.2, alpha=0.85, hatch="//"))
    ax.add_patch(Rectangle((sick_w, y0 + fp_h), heal_w, H - fp_h,
                           facecolor=WATER, edgecolor=INK, lw=1.2, alpha=0.16))

    ax.text(sick_w / 2, y0 + tp_h / 2, "190\nTrue\npos.", ha="center",
            va="center", fontsize=9.5, color="white", fontweight="bold")
    ax.text(sick_w / 2, y0 + tp_h + (H - tp_h) / 2, "10\nmiss", ha="center",
            va="center", fontsize=7.5, color=INK)
    ax.text(sick_w + heal_w / 2, y0 + fp_h / 2,
            "784  False positives", ha="center", va="center", fontsize=11,
            color="white", fontweight="bold")
    ax.text(sick_w + heal_w / 2, y0 + fp_h + (H - fp_h) / 2,
            "9,016  True negatives", ha="center", va="center", fontsize=11,
            color=INK)

    ax.text(sick_w / 2, y0 + H + 0.25, "SICK\n200", ha="center", fontsize=10,
            color=KANTO_RED, fontweight="bold")
    ax.text(sick_w + heal_w / 2, y0 + H + 0.25, "HEALTHY  9,800", ha="center",
            fontsize=10, color=KANTO_BLUE, fontweight="bold")

    # punchline.
    ax.text(5.0, -0.7,
            "Among the $190+784=974$ positives, only 190 are truly sick:  "
            r"$P(\text{sick}\mid +)=\frac{190}{974}\approx 0.195$",
            ha="center", fontsize=11.5, color=INK, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.35", fc="#FFF6D6", ec=KANTO_YEL,
                      lw=1.5))

    # decorative Staryu in the top-right margin (the scanned patient).
    place_sprite(ax, front(120), (9.4, 8.7), zoom=0.3, alpha=0.9, zorder=6)

    fig.tight_layout()
    return save(fig, "ch02_false_positive")


REGISTRY = [
    fig_bayes_grid,
    fig_tree_sequential,
    fig_total_prob,
    fig_false_positive,
]


def main() -> None:
    print(f"Generating Chapter 2 (Conditional & Bayes) figures -> {OUT} "
          f"at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
