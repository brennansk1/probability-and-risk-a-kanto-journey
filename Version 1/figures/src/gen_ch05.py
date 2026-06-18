#!/usr/bin/env python3
"""Generate every Chapter 4 (Bayes / Cerulean City / Misty) figure.

Covers the seven BLUEPRINT diagrams plus a base-rate / false-positive visual:
  ch04_conditioning_shrink   "shrinking the world" renormalization
  ch04_probability_tree      Brock's without-replacement multiplication tree
  ch04_union_venn            inclusion-exclusion Venn (+ disjoint inset)
  ch04_independence_grid     independent vs dependent contingency grids
  ch04_total_prob_tree       Misty's lead fan: law of total probability
  ch04_bayes_table           the detective's grid (prior x likelihood -> posterior)
  ch04_sequential_update     before/after posterior bars (phantom thief)
  ch04_base_rate             base-rate / false-positive area visual (Sick-Staryu test)

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette, and every color-coded
element is ALSO distinguished by a hatch pattern / text label, so the figures
remain readable in grayscale (color is never the only channel of information).

Run: python figures/src/gen_ch04.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyArrowPatch, FancyBboxPatch
from cycler import cycler

from sprite_util import front, item, place_sprite

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
# 1. Conditioning: "shrinking the world" (renormalize by dividing by P(B)).
# --------------------------------------------------------------------------
def fig_conditioning_shrink():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5.4))
    fig.suptitle("Conditioning = shrinking the world down to $B$", y=0.995)

    # LEFT: full sample space S, B shaded, A-and-B sliver highlighted.
    _blank(axL)
    axL.set_xlim(0, 10)
    axL.set_ylim(0, 8.6)
    axL.add_patch(Rectangle((0, 0), 10, 8, fill=True, facecolor=KANTO_BG,
                            edgecolor=INK, lw=1.6))
    axL.text(0.3, 7.6, "$S$: all 60 trainers", fontsize=11.5, va="top",
             fontweight="bold", color=INK)
    # B = Water-type subset: 24 of 60. A-and-B (locals) = 9 of the 24.
    axL.add_patch(Rectangle((4.6, 1.0), 4.8, 4.6, facecolor=KANTO_BLUE,
                            edgecolor=INK, lw=1.4, alpha=0.55, hatch="//"))
    axL.text(7.6, 5.85, "$B$ = Water-type (24)", ha="center", fontsize=10.5,
             color=INK, fontweight="bold")
    # A-and-B sliver: 9/24 of B's width -> 4.8 * 9/24 = 1.8 wide.
    axL.add_patch(Rectangle((4.6, 1.0), 1.8, 4.6, facecolor=KANTO_RED,
                            edgecolor=INK, lw=1.4, alpha=0.85, hatch="xx"))
    axL.text(5.5, 3.3, "9", ha="center", va="center", fontsize=13,
             color="white", fontweight="bold")
    axL.text(8.0, 3.3, "15", ha="center", va="center", fontsize=12, color=INK)
    axL.text(5.5, 0.55, "$A\\cap B$ = locals (9)", ha="center", fontsize=10,
             color=INK)
    axL.text(2.2, 3.3, "36 not\nWater-type", ha="center", va="center",
             fontsize=9.5, color=INK, style="italic")
    axL.set_title("The whole world $S$ — locals are $9/60$", fontsize=12)

    # arrow between panels
    arr = FancyArrowPatch((0.485, 0.52), (0.515, 0.52),
                          transform=fig.transFigure, mutation_scale=26,
                          lw=2.4, color=KANTO_GREEN)
    fig.patches.append(arr)
    fig.text(0.5, 0.46, "re-crop &\nrenormalize\n$\\div\\,P(B)$",
             ha="center", va="top", fontsize=9.5, color=INK, fontweight="bold")

    # RIGHT: B fills the frame; A-within-B is the answer.
    _blank(axR)
    axR.set_xlim(0, 10)
    axR.set_ylim(0, 8.6)
    axR.add_patch(Rectangle((0, 0), 10, 8, facecolor=KANTO_BLUE,
                            edgecolor=INK, lw=1.8, alpha=0.55, hatch="//"))
    # A-within-B: 9 of 24 -> 10 * 9/24 = 3.75 wide.
    axR.add_patch(Rectangle((0, 0), 3.75, 8, facecolor=KANTO_RED,
                            edgecolor=INK, lw=1.6, alpha=0.85, hatch="xx"))
    axR.text(1.875, 4.0, "9\nlocals", ha="center", va="center",
             fontsize=13, color="white", fontweight="bold")
    axR.text(6.875, 4.0, "15\nnot local", ha="center", va="center",
             fontsize=12, color=INK)
    # title placed ABOVE the frame so it never sits on the red region.
    axR.text(5.0, 8.35, "Now $B$ (24) is the entire world", ha="center",
             va="bottom", fontsize=11.5, fontweight="bold", color=INK)
    axR.set_title(r"$P(A\mid B)=\frac{P(A\cap B)}{P(B)}=\frac{9}{24}=0.375$",
                  fontsize=13)

    # decorative: a Staryu in the lower-right margin (a Water-type owner's mon).
    place_sprite(axR, front(120), (9.4, 0.7), zoom=0.34, alpha=0.9, zorder=6)

    fig.tight_layout(rect=(0, 0, 1, 0.94))
    return save(fig, "ch04_conditioning_shrink")


# --------------------------------------------------------------------------
# 2. Probability tree: Brock's without-replacement draw (multiplication rule).
# --------------------------------------------------------------------------
def fig_probability_tree():
    fig, ax = plt.subplots(figsize=(11, 6.4))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.set_title("Multiplication rule: Brock draws 2 balls (no replacement)\n"
                 "7 Poke Balls, 3 Great Balls", fontsize=14)

    root = (1.0, 4.5)

    def node(x, y, label, color, hatch):
        ax.add_patch(Circle((x, y), 0.42, facecolor=color, edgecolor=INK,
                            lw=1.4, alpha=0.9, hatch=hatch, zorder=3))
        ax.text(x, y, label, ha="center", va="center", fontsize=10,
                fontweight="bold", color=INK, zorder=4)

    def edge(p0, p1, label, color, dy=0.0):
        ax.annotate("", xy=p1, xytext=p0,
                    arrowprops=dict(arrowstyle="-", color=color, lw=2.2))
        mx, my = (p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2 + dy
        ax.text(mx, my, label, ha="center", va="center", fontsize=10,
                color=INK, bbox=dict(boxstyle="round,pad=0.18", fc="white",
                                     ec=color, lw=1.2))

    node(*root, "start", KANTO_GRAY, "")

    # stage-1 nodes
    p_pos = (4.2, 6.6)   # first = Poke
    g_pos = (4.2, 2.4)   # first = Great
    edge(root, p_pos, "$7/10$", KANTO_RED)
    edge(root, g_pos, "$3/10$", KANTO_BLUE)
    node(*p_pos, "Poke", KANTO_RED, "..")
    node(*g_pos, "Great", KANTO_BLUE, "oo")

    # stage-2 leaves with multiplied path probabilities.
    leaves = [
        (p_pos, (8.4, 7.7), "$6/9$", KANTO_RED, "..", "Poke",
         "PP", r"$\frac{7}{10}\cdot\frac{6}{9}=\frac{42}{90}$"),
        (p_pos, (8.4, 5.6), "$3/9$", KANTO_BLUE, "oo", "Great",
         "PG", r"$\frac{7}{10}\cdot\frac{3}{9}=\frac{21}{90}$"),
        (g_pos, (8.4, 3.3), "$7/9$", KANTO_RED, "..", "Poke",
         "GP", r"$\frac{3}{10}\cdot\frac{7}{9}=\frac{21}{90}$"),
        (g_pos, (8.4, 1.2), "$2/9$", KANTO_BLUE, "oo", "Great",
         "GG", r"$\frac{3}{10}\cdot\frac{2}{9}=\frac{6}{90}$"),
    ]
    for parent, pos, frac, color, hatch, lab, _tag, path in leaves:
        edge(parent, pos, frac, color)
        node(*pos, lab, color, hatch)
        ax.text(pos[0] + 0.65, pos[1], path, ha="left", va="center",
                fontsize=11, color=INK)

    # decorative items in the left margin: a Poke Ball and a Great Ball legend.
    place_sprite(ax, item("poke-ball"), (0.55, 7.9), zoom=0.45, alpha=0.95)
    ax.text(1.05, 7.9, "= Poke Ball", ha="left", va="center", fontsize=9,
            color=INK)
    place_sprite(ax, item("great-ball"), (0.55, 7.2), zoom=0.45, alpha=0.95)
    ax.text(1.05, 7.2, "= Great Ball", ha="left", va="center", fontsize=9,
            color=INK)

    ax.text(6.0, 0.2,
            "Each leaf = product along its path  (multiply the branch probabilities)",
            ha="center", fontsize=10, style="italic", color=INK)
    fig.tight_layout()
    return save(fig, "ch04_probability_tree")


# --------------------------------------------------------------------------
# 3. Union Venn: inclusion-exclusion (+ disjoint inset).
# --------------------------------------------------------------------------
def fig_union_venn():
    fig, ax = plt.subplots(figsize=(10, 6.2))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_title("Addition rule: subtract the double-counted overlap\n"
                 r"$P(A\cup B)=P(A)+P(B)-P(A\cap B)$", fontsize=14)

    # main two-circle Venn over 100 Route-24 logs.
    cA = Circle((4.3, 4.3), 2.3, facecolor=KANTO_BLUE, edgecolor=INK, lw=1.6,
                alpha=0.45, hatch="//")
    cB = Circle((6.3, 4.3), 2.3, facecolor=KANTO_YEL, edgecolor=INK, lw=1.6,
                alpha=0.55, hatch="\\\\")
    ax.add_patch(cA)
    ax.add_patch(cB)
    # overlap emphasis (drawn as a lens via a small red ellipse-ish marker label)
    ax.add_patch(Circle((5.3, 4.3), 0.95, facecolor=KANTO_RED, edgecolor=INK,
                        lw=1.4, alpha=0.7, hatch="xx", zorder=2))

    ax.text(3.1, 6.7, "$A$ = Water-type\n($=40$)", ha="center", fontsize=11,
            color=INK, fontweight="bold")
    ax.text(7.6, 6.7, "$B$ = tall-grass\n($=30$)", ha="center", fontsize=11,
            color=INK, fontweight="bold")
    # A-only = 40 - 12 = 28; B-only = 30 - 12 = 18; overlap = 12.
    ax.text(3.4, 4.3, "28", ha="center", va="center", fontsize=13, color=INK)
    ax.text(7.2, 4.3, "18", ha="center", va="center", fontsize=13, color=INK)
    ax.text(5.3, 4.55, "12", ha="center", va="center", fontsize=13,
            color="white", fontweight="bold")
    # overlap callout placed BELOW the Venn, clear of the red lens.
    ax.text(5.3, 1.35, "overlap counted\nTWICE $\\to$ subtract once",
            ha="center", va="top", fontsize=9.5, color=KANTO_RED,
            fontweight="bold")
    ax.annotate("", xy=(5.3, 3.35), xytext=(5.3, 1.55),
                arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.6))
    # union total, stated explicitly.
    ax.text(5.3, 7.55, r"$P(A\cup B)=\frac{40+30-12}{100}=0.58$", ha="center",
            fontsize=11, color=INK)

    # disjoint (mutually exclusive) inset.
    ax.add_patch(FancyBboxPatch((8.9, 0.5), 3.0, 3.0,
                                boxstyle="round,pad=0.05",
                                fc="white", ec=KANTO_GRAY, lw=1.3, zorder=1))
    ax.add_patch(Circle((9.85, 2.0), 0.7, facecolor=KANTO_BLUE, edgecolor=INK,
                        lw=1.2, alpha=0.45, hatch="//", zorder=2))
    ax.add_patch(Circle((11.0, 2.0), 0.7, facecolor=KANTO_YEL, edgecolor=INK,
                        lw=1.2, alpha=0.55, hatch="\\\\", zorder=2))
    ax.text(10.4, 3.2, "disjoint case", ha="center", fontsize=9.5,
            color=INK, fontweight="bold")
    ax.text(10.4, 0.75, "no overlap:\n$P(A\\cap B)=0$", ha="center", va="bottom",
            fontsize=8.5, color=INK)

    # decorative mons in the circle corners (clear of all counts/labels):
    # a Magikarp (Water-type) low-left in A, an Oddish (grass) low-right in B.
    place_sprite(ax, front(129), (3.0, 3.0), zoom=0.34, alpha=0.85, zorder=4)
    place_sprite(ax, front(43), (7.6, 3.0), zoom=0.34, alpha=0.85, zorder=4)

    fig.tight_layout()
    return save(fig, "ch04_union_venn")


# --------------------------------------------------------------------------
# 4. Independence grid: independent vs dependent contingency areas.
# --------------------------------------------------------------------------
def fig_independence_grid():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5.6))
    fig.suptitle("Independence: joint cell = product of margins?", y=0.99)

    def draw_grid(ax, joint, title, verdict, vcolor):
        _blank(ax)
        ax.set_xlim(-0.15, 1.25)
        ax.set_ylim(-0.25, 1.2)
        pA = 0.6   # P(A) column width
        pB = 0.5   # P(B) row height
        # four cells of the 2x2 (areas = probabilities).
        ax.add_patch(Rectangle((0, 0), pA, pB, facecolor=KANTO_BLUE,
                               edgecolor=INK, lw=1.3, alpha=0.5, hatch="//"))
        ax.add_patch(Rectangle((pA, 0), 1 - pA, pB, facecolor=KANTO_BG,
                               edgecolor=INK, lw=1.3))
        ax.add_patch(Rectangle((0, pB), pA, 1 - pB, facecolor=KANTO_BG,
                               edgecolor=INK, lw=1.3))
        ax.add_patch(Rectangle((pA, pB), 1 - pA, 1 - pB, facecolor=KANTO_BG,
                               edgecolor=INK, lw=1.3))
        # draw the realized joint as a red overlay rectangle inside the cell.
        jh = joint / pA  # height so width*height = joint within column width pA
        ax.add_patch(Rectangle((0, 0), pA, jh, facecolor=KANTO_RED,
                               edgecolor=INK, lw=1.6, alpha=0.8, hatch="xx",
                               zorder=3))
        ax.text(pA / 2, jh / 2, f"$P(A\\cap B)$\n$={joint:.2f}$", ha="center",
                va="center", fontsize=10, color="white", fontweight="bold",
                zorder=4)
        # margin labels.
        ax.text(pA / 2, -0.13, "$P(A)=0.6$", ha="center", fontsize=10, color=INK)
        ax.text(-0.13, pB / 2, "$P(B)=0.5$", ha="center", va="center",
                rotation=90, fontsize=10, color=INK)
        ax.text(0.5, 1.10, title, ha="center", fontsize=12, fontweight="bold",
                color=INK)
        prod = 0.6 * 0.5
        ax.text(0.5, -0.24,
                f"product $0.6\\times0.5={prod:.2f}$   {verdict}",
                ha="center", fontsize=10.5, color=vcolor, fontweight="bold")

    draw_grid(axL, 0.30, "Independent", "= 0.30  MATCH", KANTO_GREEN)
    draw_grid(axR, 0.18, "Dependent", r"$\neq$ 0.18  MISMATCH", KANTO_RED)

    # spinner counterexample callout box.
    fig.text(0.5, 0.015,
             "Callout: pairwise independent  $\\neq$  mutually independent "
             "(the 4-sector spinner: each pair multiplies, but the triple does not).",
             ha="center", fontsize=9.5, color=INK,
             bbox=dict(boxstyle="round,pad=0.4", fc="#FFF6D6",
                       ec=KANTO_YEL, lw=1.4))
    fig.tight_layout(rect=(0, 0.06, 1, 0.95))
    return save(fig, "ch04_independence_grid")


# --------------------------------------------------------------------------
# 5. Total probability fan: Misty's lead (weighted sum of leaves).
# --------------------------------------------------------------------------
def fig_total_prob_tree():
    fig, ax = plt.subplots(figsize=(10.5, 6.0))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_title("Law of total probability: sum the weighted leaves\n"
                 "Misty's lead Pokemon -> chance you land a super-effective hit",
                 fontsize=13.5)

    root = (1.2, 4.0)
    ax.add_patch(Circle((root[0], root[1]), 0.42, facecolor=KANTO_GRAY,
                        edgecolor=INK, lw=1.4, zorder=3))
    ax.text(root[0], root[1], "lead", ha="center", va="center", fontsize=9,
            fontweight="bold", color=INK, zorder=4)

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
        # Small species sprite tucked into the white gap just left of its leaf
        # node. The middle branch runs horizontally through y, so its edge line
        # would pass straight through the sprite -- nudge that one down to clear
        # the line. The diagonal branches already clear it, so nudge them toward
        # their own line's "inside" to sit in clean white space.
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
    return save(fig, "ch04_total_prob_tree")


# --------------------------------------------------------------------------
# 6. Bayes table: the detective's grid (prior x likelihood -> posterior).
# --------------------------------------------------------------------------
def fig_bayes_table():
    fig, ax = plt.subplots(figsize=(11.5, 6.0))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.4)
    ax.set_title("The detective's grid: multiply across, normalize down\n"
                 "Did the Staryu actually catch Brineflux?", fontsize=13.5)

    cols = ["Cause", "Prior", "Likelihood\n$P(+\\mid\\cdot)$",
            "Joint\n$=$ Prior $\\times$ Like.", "Posterior\n$=$ Joint $/$ total"]
    # Chapter numbers (Sick-Staryu, Beat 8 / WE 5.1):
    #   Sick:    prior 0.02, P(+|D)=0.95 -> joint 0.0190
    #   Healthy: prior 0.98, P(+|Dc)=0.08 -> joint 0.0784
    #   total P(+) = 0.0974; posteriors 0.195 / 0.805.
    rows = [
        ("Sick", 0.02, 0.95, 0.0190, KANTO_RED, "xx"),
        ("Healthy", 0.98, 0.08, 0.0784, KANTO_BLUE, "//"),
    ]
    total_joint = sum(r[3] for r in rows)

    x_edges = [0.3, 2.5, 4.3, 6.3, 8.7, 11.7]
    y_top = 6.0
    hh = 1.05   # header height
    rh = 1.35   # data row height

    # header row
    for j, c in enumerate(cols):
        ax.add_patch(Rectangle((x_edges[j], y_top), x_edges[j + 1] - x_edges[j],
                               hh, facecolor=KANTO_GRAY, edgecolor=INK,
                               lw=1.3, alpha=0.9))
        ax.text((x_edges[j] + x_edges[j + 1]) / 2, y_top + hh / 2, c,
                ha="center", va="center", fontsize=9.5, color="white",
                fontweight="bold")

    post_centers = []
    for i, (name, prior, like, joint, color, hatch) in enumerate(rows):
        y = y_top - (i + 1) * rh
        post = joint / total_joint
        post_centers.append((y + rh / 2, post))
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

    # "multiply across" arrow ABOVE the Sick row (in the header gap), so it
    # never crosses the prior/likelihood numbers.
    y_sick = y_top - rh + rh / 2
    ax.annotate("", xy=(x_edges[3] + 0.05, y_top - 0.12),
                xytext=(x_edges[1] + 0.2, y_top - 0.12),
                arrowprops=dict(arrowstyle="->", color=KANTO_GREEN, lw=2.0))
    ax.text((x_edges[1] + x_edges[3]) / 2, y_top + 0.06, "multiply across",
            ha="center", va="bottom", fontsize=9, color=KANTO_GREEN,
            fontweight="bold")

    # joint-column total = P(evidence), in a band just below the two rows.
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

    # divide -> posterior: a curved arrow from the P(+) band up to the
    # posterior column, placed in the right margin (clear of all numbers).
    ax.annotate("", xy=(x_edges[4] - 0.08, y_tot + hh / 2),
                xytext=(x_edges[4] + 0.05, y_tot + hh / 2),
                arrowprops=dict(arrowstyle="-", color=KANTO_GREEN, lw=0))
    ax.annotate("", xy=((x_edges[4] + x_edges[5]) / 2, y_top - 2 * rh - 0.05),
                xytext=((x_edges[4] + x_edges[5]) / 2, y_tot + hh + 0.02),
                arrowprops=dict(arrowstyle="->", color=KANTO_GREEN, lw=1.8,
                                connectionstyle="arc3,rad=0"))
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
    # "Sick" label, which is centered in the cell).
    place_sprite(ax, front(120), (x_edges[0] + 0.32, y_sick + rh * 0.32),
                 zoom=0.26, alpha=0.9, zorder=6)

    fig.tight_layout()
    return save(fig, "ch04_bayes_table")


# --------------------------------------------------------------------------
# 7. Sequential update: phantom-thief posteriors after 1 vs 2 nights.
# --------------------------------------------------------------------------
def fig_sequential_update():
    fig, ax = plt.subplots(figsize=(9.5, 5.8))
    causes = ["Traveler", "Local", "Rocket"]
    after1 = [0.458, 0.027, 0.515]
    after2 = [0.060, 0.0004, 0.940]
    colors = [KANTO_BLUE, KANTO_YEL, KANTO_RED]
    hatches = ["//", "..", "xx"]

    x = range(len(causes))
    w = 0.38
    for i, (c, h) in enumerate(zip(colors, hatches)):
        ax.bar(i - w / 2, after1[i], w, color=c, edgecolor=INK, lw=1.3,
               hatch=h, label="after 1 night" if i == 0 else None)
        ax.bar(i + w / 2, after2[i], w, color=c, edgecolor=INK, lw=1.3,
               hatch=h, alpha=0.55,
               label="after 2 nights" if i == 0 else None)
        ax.text(i - w / 2, after1[i] + 0.02, f"{after1[i]:.3f}", ha="center",
                fontsize=9, color=INK)
        ax.text(i + w / 2, after2[i] + 0.02,
                f"{after2[i]:.3f}" if after2[i] >= 0.001 else "~0.000",
                ha="center", fontsize=9, color=INK)

    ax.set_xticks(list(x))
    ax.set_xticklabels(causes, fontsize=12, fontweight="bold")
    ax.set_ylabel("Posterior probability")
    ax.set_ylim(0, 1.05)
    ax.set_title("Sequential updating: consistent evidence sharpens belief\n"
                 "Who is the phantom thief? (solid = 1 night, faded = 2 nights)",
                 fontsize=13)

    # manual legend keyed on shade, not hue (grayscale-safe).
    from matplotlib.patches import Patch
    handles = [
        Patch(facecolor=KANTO_GRAY, edgecolor=INK, label="after 1 night"),
        Patch(facecolor=KANTO_GRAY, edgecolor=INK, alpha=0.55,
              label="after 2 nights"),
    ]
    ax.legend(handles=handles, loc="upper left")
    ax.annotate("evidence piles\non Rocket", xy=(2 + w / 2, 0.94),
                xytext=(1.35, 0.74), fontsize=10, color=KANTO_RED,
                fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.8))

    # decorative: a stolen Poke Ball icon hovering over the short Local group
    # (plenty of headroom there; clear of every bar and value label).
    place_sprite(ax, item("poke-ball"), (1.0, 0.32), zoom=0.5, alpha=0.85,
                 zorder=6)
    ax.text(1.0, 0.46, "the stolen\nitem bag", ha="center", va="bottom",
            fontsize=8, color=INK, style="italic")

    fig.tight_layout()
    return save(fig, "ch04_sequential_update")


# --------------------------------------------------------------------------
# 8. Base-rate / false-positive area visual (Sick-Staryu test).
# --------------------------------------------------------------------------
def fig_base_rate():
    fig, ax = plt.subplots(figsize=(10.5, 6.4))
    _blank(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.0, 9.2)
    ax.set_title("Why a positive scan can still mean 'probably healthy'\n"
                 "Base rate 2% sick, 95% sensitivity, 8% false-positive rate",
                 fontsize=13)

    # 10,000 Water Pokemon (Beat 3): 200 sick, 9,800 healthy.
    # Widths are NOT to base-rate scale (2% is too thin to read); we instead
    # use a readable split and label the true population counts explicitly.
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
    ax.add_patch(Rectangle((sick_w, y0), heal_w, fp_h, facecolor=KANTO_BLUE,
                           edgecolor=INK, lw=1.2, alpha=0.8, hatch="//"))
    ax.add_patch(Rectangle((sick_w, y0 + fp_h), heal_w, H - fp_h,
                           facecolor=KANTO_BLUE, edgecolor=INK, lw=1.2,
                           alpha=0.16))

    # counts (out of 10,000).
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

    # bracket the two shaded "positive" bands.
    ax.annotate("", xy=(sick_w + heal_w + 0.05, y0),
                xytext=(sick_w + heal_w + 0.05, y0 + fp_h),
                arrowprops=dict(arrowstyle="-", color=INK, lw=1.0))

    # punchline: among positives, P(sick | +).
    ax.text(5.0, -0.7,
            "Among the $190+784=974$ positives, only 190 are truly sick:  "
            r"$P(\text{sick}\mid +)=\frac{190}{974}\approx 0.195$",
            ha="center", fontsize=11.5, color=INK, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.35", fc="#FFF6D6", ec=KANTO_YEL,
                      lw=1.5))

    # decorative Staryu in the top-right margin (the scanned patient).
    place_sprite(ax, front(120), (9.4, 8.7), zoom=0.3, alpha=0.9, zorder=6)

    fig.tight_layout()
    return save(fig, "ch04_base_rate")


REGISTRY = [
    fig_conditioning_shrink,
    fig_probability_tree,
    fig_union_venn,
    fig_independence_grid,
    fig_total_prob_tree,
    fig_bayes_table,
    fig_sequential_update,
    fig_base_rate,
]


def main() -> None:
    print(f"Generating Chapter 5 (Bayes) figures -> {OUT} at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
