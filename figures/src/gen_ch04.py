#!/usr/bin/env python3
"""Generate every Chapter 4 (Counting / Combinatorics / Brock's forest) figure.

Covers the five BLUEPRINT diagrams referenced by book/chapters/ch04_counting.md:
  ch04count_stage_tree            multiplication principle as a 3-stage tree (3x2x4=24)
  ch04count_permutation_slots     ordered slots with a shrinking menu (8x7x6=336)
  ch04count_combination_collapse  k! ordered cards collapse to one team (P(12,6)/6!=924)
  ch04count_multinomial_repeats   identical-E orderings collapse (8!/2!=20160)
  ch04count_hypergeom_split       success/failure pile split (6*6/120=0.30)

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
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch, FancyArrowPatch
from cycler import cycler

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
# 1. Multiplication principle as a 3-stage tree: 3 x 2 x 4 = 24 leaves.
# --------------------------------------------------------------------------
def fig_stage_tree():
    fig, ax = plt.subplots(figsize=(12, 7.2))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.set_title("Multiplication principle as a tree: count the leaves\n"
                 "$3$ main trails $\\times\\ 2$ sub-trails $\\times\\ 4$ clearings "
                 "$= 24$ routes", fontsize=14)

    # x positions of the four columns: root, stage1 (3), stage2 (6), leaves (24).
    x_root, x1, x2, x3 = 0.7, 3.2, 6.0, 9.2
    y_lo, y_hi = 0.6, 9.4

    def ys(n):
        # evenly spaced vertical centers across the drawing band.
        if n == 1:
            return [(y_lo + y_hi) / 2]
        step = (y_hi - y_lo) / n
        return [y_lo + step * (i + 0.5) for i in range(n)]

    y_root = (y_lo + y_hi) / 2
    y1 = ys(3)            # 3 main trails
    y2 = ys(6)            # each splits into 2 -> 6 sub-trails
    y3 = ys(24)           # each into 4 -> 24 clearings

    def line(p0, p1, color, lw=1.6, alpha=1.0):
        ax.plot([p0[0], p1[0]], [p0[1], p1[1]], color=color, lw=lw,
                alpha=alpha, zorder=1, solid_capstyle="round")

    # root node
    ax.add_patch(Circle((x_root, y_root), 0.30, facecolor=KANTO_GRAY,
                        edgecolor=INK, lw=1.4, zorder=3))
    ax.text(x_root, y_root, "in", ha="center", va="center", fontsize=8,
            fontweight="bold", color="white", zorder=4)

    # stage 1: 3 main-trail nodes (red, hatch "..")
    for yy in y1:
        line((x_root, y_root), (x1, yy), KANTO_RED, lw=2.2)
        ax.add_patch(Circle((x1, yy), 0.26, facecolor=KANTO_RED, edgecolor=INK,
                            lw=1.2, alpha=0.9, hatch="..", zorder=3))

    # stage 2: each main trail -> 2 sub-trails (blue, hatch "//")
    for i, yy in enumerate(y1):
        for j in range(2):
            child = y2[2 * i + j]
            line((x1, yy), (x2, child), KANTO_BLUE, lw=1.6)
            ax.add_patch(Circle((x2, child), 0.20, facecolor=KANTO_BLUE,
                                edgecolor=INK, lw=1.0, alpha=0.9, hatch="//",
                                zorder=3))

    # stage 3: each sub-trail -> 4 clearings = 24 leaves (yellow, hatch "xx")
    for i, yy in enumerate(y2):
        for j in range(4):
            leaf = y3[4 * i + j]
            line((x2, yy), (x3, leaf), KANTO_YEL, lw=0.9, alpha=0.9)
            ax.add_patch(Circle((x3, leaf), 0.085, facecolor=KANTO_YEL,
                                edgecolor=INK, lw=0.6, zorder=3))

    # column headers / menu sizes.
    head_y = 9.75
    for x, n, lab, col, first in [(x1, 3, "main trails", KANTO_RED, True),
                                  (x2, 2, "sub-trails", KANTO_BLUE, False),
                                  (x3, 4, "clearings", KANTO_YEL, False)]:
        # leftmost column reads as just "3"; later columns as "x 2", "x 4".
        label = f"${n}$" if first else f"$\\times\\,{n}$"
        ax.text(x, head_y, label, ha="center", fontsize=13,
                fontweight="bold", color=col)
        ax.text(x, head_y - 0.45, lab, ha="center", fontsize=9, color=INK)

    # running-count annotations down the right edge.
    ax.text(x3 + 0.55, y_root, "$3\\times2\\times4$\n$=\\mathbf{24}$ leaves",
            ha="left", va="center", fontsize=13, color=KANTO_GREEN,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.35", fc="#E8F5E9", ec=KANTO_GREEN,
                      lw=1.5))
    ax.text(6.0, 0.18,
            'each node fans into the NEXT stage\'s full menu  ("for each")',
            ha="center", fontsize=9.5, style="italic", color=INK)

    fig.tight_layout()
    return save(fig, "ch04count_stage_tree")


# --------------------------------------------------------------------------
# 2. Permutation slots: ordered slots with a shrinking menu, 8 x 7 x 6 = 336.
# --------------------------------------------------------------------------
def fig_permutation_slots():
    fig, ax = plt.subplots(figsize=(11, 5.6))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.set_title("A permutation as ordered slots with a shrinking menu\n"
                 "$P(8,3) = 8 \\times 7 \\times 6 = 336$", fontsize=14)

    slots = [("Lead", 8, KANTO_RED, "xx"),
             ("Second", 7, KANTO_BLUE, "//"),
             ("Anchor", 6, KANTO_YEL, "..")]
    sw = 2.4   # slot width
    gap = 0.9
    x0 = 1.6
    y0 = 3.0
    sh = 2.0   # slot height

    centers = []
    for i, (name, menu, col, hatch) in enumerate(slots):
        x = x0 + i * (sw + gap)
        cx = x + sw / 2
        centers.append(cx)
        # menu size above the slot.
        ax.text(cx, y0 + sh + 1.0, f"${menu}$", ha="center", va="center",
                fontsize=22, fontweight="bold", color=col)
        ax.text(cx, y0 + sh + 0.35, "choices left", ha="center", fontsize=8.5,
                color=INK)
        # the slot box.
        ax.add_patch(FancyBboxPatch((x, y0), sw, sh,
                                    boxstyle="round,pad=0.02",
                                    facecolor=col, edgecolor=INK, lw=1.6,
                                    alpha=0.30, hatch=hatch, zorder=2))
        ax.text(cx, y0 + sh / 2, name, ha="center", va="center", fontsize=13,
                fontweight="bold", color=INK, zorder=3)
        # multiplication sign between slots.
        if i < len(slots) - 1:
            ax.text(x + sw + gap / 2, y0 + sh / 2, r"$\times$", ha="center",
                    va="center", fontsize=22, color=INK)

    # product below.
    ax.text((centers[0] + centers[-1]) / 2, 1.6,
            "$8 \\times 7 \\times 6 = \\mathbf{336}$ ordered line-ups",
            ha="center", fontsize=15, fontweight="bold", color=KANTO_GREEN,
            bbox=dict(boxstyle="round,pad=0.35", fc="#E8F5E9", ec=KANTO_GREEN,
                      lw=1.5))

    # cancelled-tail note: the 5 unused Pokemon = (n-k)! = 5!.
    ax.text(centers[-1] + 2.4, y0 + sh / 2,
            "5 unused Pokemon\nform the cancelled\n"
            "$(n-k)! = 5!$ tail",
            ha="center", va="center", fontsize=10, color=KANTO_GRAY,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_GRAY,
                      lw=1.3, ls="--"))
    ax.text(0.4, 0.5,
            r"directly: $P(8,3)=\frac{8!}{(8-3)!}=\frac{8!}{5!}=336$",
            ha="left", fontsize=11, color=INK)

    fig.tight_layout()
    return save(fig, "ch04count_permutation_slots")


# --------------------------------------------------------------------------
# 3. Combination collapse: 6! ordered cards collapse to 1 team; P(12,6)/6!=924.
# --------------------------------------------------------------------------
def fig_combination_collapse():
    fig, ax = plt.subplots(figsize=(11.5, 6.6))
    _blank(ax)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 9)
    ax.set_title("A combination collapses orderings\n"
                 "$6! = 720$ ordered cards of one roster $=$ a single team",
                 fontsize=14)

    roster = ["A", "B", "C", "D", "E", "F"]
    # six ordered registration cards, each a different sequence of the SAME six.
    orderings = [
        ["A", "B", "C", "D", "E", "F"],
        ["B", "A", "C", "E", "D", "F"],
        ["C", "B", "A", "F", "E", "D"],
        ["F", "E", "D", "C", "B", "A"],
        ["D", "C", "F", "A", "B", "E"],
        ["E", "F", "B", "D", "A", "C"],
    ]
    card_w, card_h = 3.4, 0.66
    x_card = 0.5
    y_top = 8.0
    dy = 1.18
    cellw = card_w / 6

    for r, seq in enumerate(orderings):
        y = y_top - r * dy
        ax.add_patch(FancyBboxPatch((x_card, y - card_h / 2), card_w, card_h,
                                    boxstyle="round,pad=0.02",
                                    facecolor="white", edgecolor=KANTO_BLUE,
                                    lw=1.3, zorder=2))
        for c, item in enumerate(seq):
            cx = x_card + cellw * (c + 0.5)
            ax.text(cx, y, item, ha="center", va="center", fontsize=9,
                    color=INK, zorder=3)
            if c < 5:
                ax.plot([x_card + cellw * (c + 1)] * 2,
                        [y - card_h / 2 + 0.06, y + card_h / 2 - 0.06],
                        color="#CCCCCC", lw=0.6, zorder=2)
    ax.text(x_card + card_w / 2, y_top + 0.75,
            "$720$ ordered cards\n(only 6 of them shown)", ha="center",
            fontsize=9.5, color=INK, style="italic")

    # big brace + arrow pointing right to one unordered team.
    arr = FancyArrowPatch((x_card + card_w + 0.5, 4.3),
                          (8.4, 4.3), mutation_scale=26, lw=2.4,
                          color=KANTO_GREEN, zorder=4)
    ax.add_patch(arr)
    ax.text((x_card + card_w + 0.5 + 8.4) / 2, 4.85,
            "all describe\nONE team", ha="center", fontsize=9.5,
            color=KANTO_GREEN, fontweight="bold")
    ax.text((x_card + card_w + 0.5 + 8.4) / 2, 3.55, r"$\div\,6!$",
            ha="center", fontsize=12, color=KANTO_GREEN, fontweight="bold")

    # single unordered team set drawn once (a set in braces).
    tx, ty, tw, th = 8.7, 3.4, 3.6, 1.8
    ax.add_patch(FancyBboxPatch((tx, ty), tw, th, boxstyle="round,pad=0.05",
                                facecolor=KANTO_YEL, edgecolor=INK, lw=1.8,
                                alpha=0.35, hatch="..", zorder=2))
    ax.text(tx + tw / 2, ty + th * 0.66,
            "{ " + ",  ".join(roster) + " }", ha="center", va="center",
            fontsize=12, fontweight="bold", color=INK, zorder=3)
    ax.text(tx + tw / 2, ty + th * 0.26, "one unordered team",
            ha="center", va="center", fontsize=10, color=INK, zorder=3)

    # bottom line: the division identity.
    ax.text(6.5, 0.55,
            r"$\binom{12}{6}=\frac{P(12,6)}{6!}=\frac{665280}{720}"
            r"=\mathbf{924}$ teams",
            ha="center", fontsize=14, fontweight="bold", color=KANTO_GREEN,
            bbox=dict(boxstyle="round,pad=0.35", fc="#E8F5E9", ec=KANTO_GREEN,
                      lw=1.5))
    fig.tight_layout()
    return save(fig, "ch04count_combination_collapse")


# --------------------------------------------------------------------------
# 4. Multinomial repeats: identical-E orderings collapse; 8!/2! = 20160.
# --------------------------------------------------------------------------
def fig_multinomial_repeats():
    fig, ax = plt.subplots(figsize=(11, 6.2))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.5)
    ax.set_title("Repeats collapse arrangements\n"
                 "the $2!$ orderings of the identical E's are ONE visible word",
                 fontsize=14)

    word = list("CATERPIE")
    e_idx = [3, 7]  # positions of the two E's in CATERPIE
    cw = 1.05       # cell width
    x0 = 1.7

    def draw_word(y, e_labels):
        """Draw CATERPIE; the two E's tinted red, labelled with e_labels."""
        for i, ch in enumerate(word):
            x = x0 + i * cw
            is_e = i in e_idx
            fc = KANTO_RED if is_e else KANTO_BG
            ax.add_patch(Rectangle((x, y), cw * 0.9, 0.9,
                                   facecolor=fc, edgecolor=INK, lw=1.3,
                                   alpha=0.85 if is_e else 1.0,
                                   hatch="xx" if is_e else None, zorder=2))
            ax.text(x + cw * 0.45, y + 0.45, ch, ha="center", va="center",
                    fontsize=15, fontweight="bold",
                    color="white" if is_e else INK, zorder=3)
            if is_e:
                lab = e_labels[0] if i == e_idx[0] else e_labels[1]
                ax.text(x + cw * 0.45, y - 0.28, lab, ha="center", va="center",
                        fontsize=10, color=KANTO_RED, fontweight="bold")

    # two rows: same word with the two E positions' labels swapped.
    draw_word(6.0, ("$E_1$", "$E_2$"))
    draw_word(4.0, ("$E_2$", "$E_1$"))

    # equals sign between the two rows -> they LOOK identical.
    ax.text(x0 - 0.9, 5.0, "$=$", ha="center", va="center", fontsize=26,
            color=INK)
    ax.text(x0 + 8 * cw + 0.35, 5.0, "look\nidentical", ha="left", va="center",
            fontsize=10, color=INK, style="italic")

    # brace + arrow: the pair collapses to one visible word.
    arr = FancyArrowPatch((6.0, 3.4), (6.0, 2.4), mutation_scale=22, lw=2.4,
                          color=KANTO_GREEN)
    ax.add_patch(arr)
    ax.text(6.7, 2.9, "collapse the\n$2!$ E-orderings", ha="left", va="center",
            fontsize=9.5, color=KANTO_GREEN, fontweight="bold")

    # one visible CATERPIE (plain).
    for i, ch in enumerate(word):
        x = x0 + i * cw
        ax.add_patch(Rectangle((x, 1.2), cw * 0.9, 0.9, facecolor=KANTO_YEL,
                               edgecolor=INK, lw=1.3, alpha=0.45, hatch="..",
                               zorder=2))
        ax.text(x + cw * 0.45, 1.65, ch, ha="center", va="center",
                fontsize=15, fontweight="bold", color=INK, zorder=3)

    ax.text(6.0, 0.35,
            r"$\frac{8!}{2!} = \mathbf{20{,}160}$ distinguishable words",
            ha="center", fontsize=14, fontweight="bold", color=KANTO_GREEN,
            bbox=dict(boxstyle="round,pad=0.3", fc="#E8F5E9", ec=KANTO_GREEN,
                      lw=1.5))
    fig.tight_layout()
    return save(fig, "ch04count_multinomial_repeats")


# --------------------------------------------------------------------------
# 5. Hypergeometric split: success/failure piles; (6*6)/120 = 0.30.
# --------------------------------------------------------------------------
def fig_hypergeom_split():
    fig, ax = plt.subplots(figsize=(11.5, 6.6))
    _blank(ax)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 9)
    ax.set_title("Combinatorial probability: choose from each pile, over all hands\n"
                 "cluster of $10$: $4$ Caterpie (success), $6$ Weedle (failure); "
                 "draw $3$", fontsize=13.5)

    # ----- LEFT: successes box (4 Caterpie), choose 2 (circled). -----
    sx, sy, sw, sh = 0.5, 5.0, 3.4, 3.0
    ax.add_patch(FancyBboxPatch((sx, sy), sw, sh, boxstyle="round,pad=0.04",
                                facecolor=KANTO_RED, edgecolor=INK, lw=1.6,
                                alpha=0.22, hatch="xx", zorder=1))
    ax.text(sx + sw / 2, sy + sh + 0.3, "SUCCESSES: 4 Caterpie", ha="center",
            fontsize=10.5, fontweight="bold", color=KANTO_RED)
    succ_pos = [(sx + 0.9, sy + 1.9), (sx + 2.4, sy + 1.9),
                (sx + 0.9, sy + 0.9), (sx + 2.4, sy + 0.9)]
    for i, (px, py) in enumerate(succ_pos):
        chosen = i < 2
        ax.add_patch(Circle((px, py), 0.42, facecolor=KANTO_RED, edgecolor=INK,
                            lw=1.3, alpha=0.85 if chosen else 0.35,
                            hatch="xx" if chosen else None, zorder=3))
        ax.text(px, py, "C", ha="center", va="center", fontsize=11,
                fontweight="bold", color="white" if chosen else INK, zorder=4)
        if chosen:
            ax.add_patch(Circle((px, py), 0.56, fill=False, edgecolor=KANTO_GREEN,
                                lw=2.2, zorder=4))
    ax.text(sx + sw / 2, sy - 0.35,
            r"choose $\binom{4}{2}=6$", ha="center", fontsize=12,
            color=INK, fontweight="bold")

    # ----- RIGHT: failures box (6 Weedle), choose 1 (circled). -----
    fx, fy, fw, fh = 4.7, 5.0, 4.6, 3.0
    ax.add_patch(FancyBboxPatch((fx, fy), fw, fh, boxstyle="round,pad=0.04",
                                facecolor=KANTO_BLUE, edgecolor=INK, lw=1.6,
                                alpha=0.22, hatch="//", zorder=1))
    ax.text(fx + fw / 2, fy + fh + 0.3, "FAILURES: 6 Weedle", ha="center",
            fontsize=10.5, fontweight="bold", color=KANTO_BLUE)
    fail_pos = [(fx + 0.9, fy + 2.0), (fx + 2.3, fy + 2.0), (fx + 3.7, fy + 2.0),
                (fx + 0.9, fy + 0.8), (fx + 2.3, fy + 0.8), (fx + 3.7, fy + 0.8)]
    for i, (px, py) in enumerate(fail_pos):
        chosen = i < 1
        ax.add_patch(Circle((px, py), 0.42, facecolor=KANTO_BLUE, edgecolor=INK,
                            lw=1.3, alpha=0.85 if chosen else 0.35,
                            hatch="//" if chosen else None, zorder=3))
        ax.text(px, py, "W", ha="center", va="center", fontsize=11,
                fontweight="bold", color="white" if chosen else INK, zorder=4)
        if chosen:
            ax.add_patch(Circle((px, py), 0.56, fill=False, edgecolor=KANTO_GREEN,
                                lw=2.2, zorder=4))
    ax.text(fx + fw / 2, fy - 0.35,
            r"choose $\binom{6}{1}=6$", ha="center", fontsize=12,
            color=INK, fontweight="bold")

    # times sign between the two boxes.
    ax.text(4.35, 6.5, r"$\times$", ha="center", va="center", fontsize=24,
            color=INK)

    # numerator (favorable) over denominator (all hands).
    ax.text(10.9, 6.9, "$6 \\times 6 = 36$\nfavorable hands", ha="center",
            va="center", fontsize=12, color=INK, fontweight="bold")
    ax.plot([9.6, 12.2], [5.6, 5.6], color=INK, lw=2.0)
    ax.add_patch(FancyBboxPatch((9.55, 4.0), 2.7, 1.2,
                                boxstyle="round,pad=0.03",
                                facecolor=KANTO_GRAY, edgecolor=INK, lw=1.3,
                                alpha=0.22, zorder=1))
    ax.text(10.9, 4.6, r"all $\binom{10}{3}=120$" + "\nhands", ha="center",
            va="center", fontsize=11, color=INK, fontweight="bold")

    # final probability.
    ax.text(6.5, 2.0,
            r"$P(\text{exactly 2 Caterpie}) = \frac{\binom{4}{2}\binom{6}{1}}"
            r"{\binom{10}{3}} = \frac{36}{120} = \mathbf{0.30}$",
            ha="center", fontsize=15, fontweight="bold", color=KANTO_GREEN,
            bbox=dict(boxstyle="round,pad=0.4", fc="#E8F5E9", ec=KANTO_GREEN,
                      lw=1.6))
    fig.tight_layout()
    return save(fig, "ch04count_hypergeom_split")


REGISTRY = [
    fig_stage_tree,
    fig_permutation_slots,
    fig_combination_collapse,
    fig_multinomial_repeats,
    fig_hypergeom_split,
]


def main() -> None:
    print(f"Generating Chapter 4 (Counting) figures -> {OUT} at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
