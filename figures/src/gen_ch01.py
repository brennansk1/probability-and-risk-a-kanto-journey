#!/usr/bin/env python3
"""Generate every Chapter 1 (Fundamentals of Probability / Route 1 / Spearow swarm) figure.

Manifest (MASTER_PLAN_V3 §16) — five concept diagrams, all into assets/diagrams/:
  ch01_sample_space_box  the world S as a box of outcome chips (don't drop "nothing")
  ch01_venn_two          two-circle Venn: or / and / neither (+ De Morgan)
  ch01_venn_three        three-circle Venn: the seven cells of inclusion-exclusion
  ch01_incl_excl         inclusion-exclusion bookkeeping: +singles -pairs +triple
  ch01_me_vs_indep       mutually exclusive (no overlap) vs independent (forced overlap)

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is
ALSO distinguished by a hatch pattern / text label so figures survive grayscale
(color is never the sole channel). Sprites obey the IRON RULE: art in margins, never
over a curve, equation, axis, or number a reader must read.

Run: python3 figures/src/gen_ch01.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, FancyBboxPatch

from sprite_util import front, item, place_sprite
from type_palette import chapter_accent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents). Chapter 1 is a FLYING-type
# tutorial route, so the figure accent leans on the §17 Flying color.
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
FLYING = chapter_accent(1)  # §17 Flying accent (banner/accent parity)
INK = "#333333"

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
# 1. ch01_sample_space_box — the world S as a box of outcome chips.
#    Concept 1: every outcome must be in the box, even the boring "nothing".
# --------------------------------------------------------------------------
def fig_sample_space_box():
    fig, ax = plt.subplots(figsize=(10.5, 5.0))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.set_title("The sample space $S$: every outcome that could happen\n"
                 "one wild Route 1 encounter", fontsize=13.5)

    # The box S.
    ax.add_patch(FancyBboxPatch((0.4, 1.0), 11.2, 3.6,
                                boxstyle="round,pad=0.02,rounding_size=0.25",
                                facecolor=KANTO_BG, edgecolor=INK, lw=2.0))
    ax.text(6.0, 4.25, "$S$ — the sample space (every outcome, nothing missing)",
            ha="center", va="center", fontsize=11, fontweight="bold", color=INK)

    # Four outcome chips: Pidgey, Rattata, Spearow, nothing.
    # Each chip: a thick colored border (grayscale-survivable channel #1) + a
    # text label (channel #2) + the sprite kept clear in a white body so the art
    # never fights the math (the IRON RULE). No body hatch — it would obscure the
    # sprite; the border weight/color carries the distinction instead.
    chips = [
        ("Pidgey", 16, KANTO_GREEN),
        ("Rattata", 19, KANTO_BLUE),
        ("Spearow", 21, KANTO_RED),
        ("nothing", None, KANTO_GRAY),
    ]
    cw, ch = 2.3, 1.7
    x0 = 0.85
    gap = (11.2 - 0.9 - 4 * cw) / 3
    for i, (label, dex, color) in enumerate(chips):
        x = x0 + i * (cw + gap)
        y = 1.5
        ax.add_patch(FancyBboxPatch((x, y), cw, ch,
                                    boxstyle="round,pad=0.02,rounding_size=0.12",
                                    facecolor="white", edgecolor=color, lw=2.6))
        ax.text(x + cw / 2, y + 0.28, label, ha="center", va="center",
                fontsize=11, fontweight="bold", color=INK)
        if dex is not None:
            place_sprite(ax, front(dex), (x + cw / 2, y + 1.12), zoom=0.40,
                         alpha=1.0, zorder=6)
        else:
            ax.text(x + cw / 2, y + 1.12, "(no\nencounter)", ha="center",
                    va="center", fontsize=8.5, style="italic", color=KANTO_GRAY)

    # Warning arrow at the easy-to-forget "nothing" chip.
    x_nothing = x0 + 3 * (cw + gap) + cw / 2
    ax.annotate("", xy=(x_nothing, 1.45), xytext=(x_nothing, 0.55),
                arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=2.2))
    ax.text(x_nothing, 0.25, "don't drop the boring outcome!", ha="center",
            va="center", fontsize=9, color=KANTO_RED, fontweight="bold")

    ax.text(6.0, 5.55,
            "An $\\mathit{event}$ is any subset of $S$, e.g. "
            r'"a bird appears" $=\{$Pidgey, Spearow$\}$',
            ha="center", va="center", fontsize=10, color=INK, style="italic")
    fig.tight_layout()
    return save(fig, "ch01_sample_space_box")


# --------------------------------------------------------------------------
# 2. ch01_venn_two — two-circle Venn: or / and / neither, plus De Morgan.
# --------------------------------------------------------------------------
def fig_venn_two():
    fig, ax = plt.subplots(figsize=(8.8, 6.2))
    _blank(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.set_title("Two events in $S$: \"or\", \"and\", \"neither\"",
                 fontsize=13.5)

    # Rectangle S.
    ax.add_patch(Rectangle((0.5, 0.8), 9.0, 6.2, facecolor=KANTO_BG,
                           edgecolor=INK, lw=2.0))
    ax.text(9.25, 6.7, "$S$", ha="right", va="top", fontsize=14,
            fontweight="bold", color=INK)

    # Two overlapping circles.
    cA = (4.0, 3.9)
    cB = (6.0, 3.9)
    r = 2.1
    ax.add_patch(Circle(cA, r, facecolor=KANTO_BLUE, edgecolor=INK, lw=1.8,
                        alpha=0.30, hatch="//"))
    ax.add_patch(Circle(cB, r, facecolor=KANTO_RED, edgecolor=INK, lw=1.8,
                        alpha=0.30, hatch="xx"))

    ax.text(2.9, 5.3, "$A$", ha="center", fontsize=15, fontweight="bold",
            color=KANTO_BLUE)
    ax.text(7.1, 5.3, "$B$", ha="center", fontsize=15, fontweight="bold",
            color=KANTO_RED)

    # Region labels (kept off any sprite, plain math type).
    ax.text(3.1, 3.9, "$A$ only", ha="center", va="center", fontsize=10,
            color=INK)
    ax.text(6.9, 3.9, "$B$ only", ha="center", va="center", fontsize=10,
            color=INK)
    ax.text(5.0, 3.9, "$A\\cap B$\n(\"and\")", ha="center", va="center",
            fontsize=9.5, color=INK, fontweight="bold")
    ax.text(5.0, 1.4, "$(A\\cup B)^c = A^c\\cap B^c$  (\"neither\")",
            ha="center", va="center", fontsize=10, color=INK, fontweight="bold")

    ax.text(5.0, 0.1,
            r'"or" $=A\cup B$ (both circles) $\cdot$ "and" $=A\cap B$ (overlap)'
            r' $\cdot$ "neither" $=$ outside both',
            ha="center", va="center", fontsize=9.5, style="italic", color=INK)
    fig.tight_layout()
    return save(fig, "ch01_venn_two")


# --------------------------------------------------------------------------
# 3. ch01_venn_three — three-circle Venn: the seven cells.
# --------------------------------------------------------------------------
def fig_venn_three():
    fig, ax = plt.subplots(figsize=(8.4, 7.4))
    _blank(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Three events: the seven cells of inclusion-exclusion",
                 fontsize=13.5)

    ax.add_patch(Rectangle((0.4, 0.6), 9.2, 8.6, facecolor=KANTO_BG,
                           edgecolor=INK, lw=2.0))
    ax.text(9.35, 8.9, "$S$", ha="right", va="top", fontsize=14,
            fontweight="bold", color=INK)

    r = 2.5
    cA = (3.7, 5.9)
    cB = (6.3, 5.9)
    cC = (5.0, 3.6)
    ax.add_patch(Circle(cA, r, facecolor=KANTO_BLUE, edgecolor=INK, lw=1.6,
                        alpha=0.26, hatch="//"))
    ax.add_patch(Circle(cB, r, facecolor=KANTO_RED, edgecolor=INK, lw=1.6,
                        alpha=0.26, hatch="xx"))
    ax.add_patch(Circle(cC, r, facecolor=KANTO_YEL, edgecolor=INK, lw=1.6,
                        alpha=0.30, hatch=".."))

    ax.text(2.4, 7.6, "$A$", fontsize=15, fontweight="bold", color=KANTO_BLUE)
    ax.text(7.6, 7.6, "$B$", fontsize=15, fontweight="bold", color=KANTO_RED)
    ax.text(5.0, 1.6, "$C$", fontsize=15, fontweight="bold", color="#B8860B",
            ha="center")

    # Seven cells.
    ax.text(2.7, 6.4, "$A$\nonly", ha="center", va="center", fontsize=8.5,
            color=INK)
    ax.text(7.3, 6.4, "$B$\nonly", ha="center", va="center", fontsize=8.5,
            color=INK)
    ax.text(5.0, 2.7, "$C$\nonly", ha="center", va="center", fontsize=8.5,
            color=INK)
    ax.text(5.0, 6.9, "$A\\cap B$", ha="center", va="center", fontsize=8,
            color=INK)
    ax.text(3.3, 4.5, "$A\\cap C$", ha="center", va="center", fontsize=8,
            color=INK)
    ax.text(6.7, 4.5, "$B\\cap C$", ha="center", va="center", fontsize=8,
            color=INK)
    ax.text(5.0, 5.0, "$A\\cap B\\cap C$", ha="center", va="center",
            fontsize=7.8, color=INK, fontweight="bold")

    ax.text(5.0, 0.15,
            "$+$singles $-$pairs $+$triple counts every cell exactly once",
            ha="center", va="center", fontsize=9.5, style="italic", color=INK)
    fig.tight_layout()
    return save(fig, "ch01_venn_three")


# --------------------------------------------------------------------------
# 4. ch01_incl_excl — inclusion-exclusion bookkeeping with the Route 24 counts.
# --------------------------------------------------------------------------
def fig_incl_excl():
    fig, ax = plt.subplots(figsize=(10.5, 5.6))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.set_title("Inclusion-exclusion: subtract the overlap you counted twice\n"
                 "100 Route 24 logs: 40 Water, 30 grass, 12 both",
                 fontsize=13)

    # Two overlapping circles with counts (areas not to scale; counts labelled).
    cA = (4.3, 4.0)
    cB = (6.4, 4.0)
    r = 2.0
    ax.add_patch(Circle(cA, r, facecolor=KANTO_BLUE, edgecolor=INK, lw=1.8,
                        alpha=0.30, hatch="//"))
    ax.add_patch(Circle(cB, r, facecolor=KANTO_GREEN, edgecolor=INK, lw=1.8,
                        alpha=0.30, hatch=".."))
    ax.text(3.1, 5.6, "Water (40)", ha="center", fontsize=11,
            fontweight="bold", color=KANTO_BLUE)
    ax.text(7.6, 5.6, "grass (30)", ha="center", fontsize=11,
            fontweight="bold", color="#2E7D32")

    ax.text(3.4, 4.0, "28", ha="center", va="center", fontsize=12, color=INK)
    ax.text(7.3, 4.0, "18", ha="center", va="center", fontsize=12, color=INK)
    ax.text(5.35, 4.0, "12\nboth", ha="center", va="center", fontsize=10,
            color=INK, fontweight="bold")

    # The arithmetic, off to the right of the circles.
    ax.text(9.0, 5.0, r"$40 + 30 - 12$", ha="left", va="center", fontsize=14,
            color=INK)
    ax.text(9.0, 4.0, r"$= 58$", ha="left", va="center", fontsize=14,
            color=INK, fontweight="bold")
    ax.text(9.0, 3.0,
            r"$P(W\cup G)=\dfrac{58}{100}=0.58$",
            ha="left", va="center", fontsize=12, color=KANTO_GREEN,
            fontweight="bold")

    ax.text(6.0, 1.1,
            r"$P(A\cup B)=P(A)+P(B)-P(A\cap B)$"
            "\n"
            "add both piles, then remove the 12 counted in both",
            ha="center", va="center", fontsize=11, color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc="#E8F5E9", ec=KANTO_GREEN,
                      lw=1.4))
    fig.tight_layout()
    return save(fig, "ch01_incl_excl")


# --------------------------------------------------------------------------
# 5. ch01_me_vs_indep — mutually exclusive vs independent (the trap).
# --------------------------------------------------------------------------
def fig_me_vs_indep():
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11.5, 5.6))
    for ax in (axL, axR):
        _blank(ax)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 9)

    # LEFT: mutually exclusive — circles don't touch.
    axL.set_title("Mutually exclusive\n$P(A\\cap B)=0$  (you may ADD)",
                  fontsize=12)
    axL.add_patch(Rectangle((0.5, 0.8), 9.0, 6.8, facecolor=KANTO_BG,
                            edgecolor=INK, lw=1.8))
    axL.add_patch(Circle((3.0, 4.2), 1.7, facecolor=KANTO_BLUE, edgecolor=INK,
                         lw=1.8, alpha=0.32, hatch="//"))
    axL.add_patch(Circle((6.9, 4.2), 1.7, facecolor=KANTO_RED, edgecolor=INK,
                         lw=1.8, alpha=0.32, hatch="xx"))
    axL.text(3.0, 4.2, "$A$", ha="center", va="center", fontsize=15,
             fontweight="bold", color=KANTO_BLUE)
    axL.text(6.9, 4.2, "$B$", ha="center", va="center", fontsize=15,
             fontweight="bold", color=KANTO_RED)
    axL.text(5.0, 1.6, "no overlap", ha="center", va="center", fontsize=10,
             style="italic", color=INK)
    axL.text(5.0, 0.0,
             "if $A$ happens, $B$ is impossible\n$\\Rightarrow$ maximally "
             "DEPENDENT",
             ha="center", va="center", fontsize=9.5, color=KANTO_RED,
             fontweight="bold")

    # RIGHT: independent — overlap forced to P(A)P(B).
    axR.set_title("Independent\n$P(A\\cap B)=P(A)\\,P(B)$  (you may MULTIPLY)",
                  fontsize=12)
    axR.add_patch(Rectangle((0.5, 0.8), 9.0, 6.8, facecolor=KANTO_BG,
                            edgecolor=INK, lw=1.8))
    axR.add_patch(Circle((4.0, 4.2), 1.9, facecolor=KANTO_BLUE, edgecolor=INK,
                         lw=1.8, alpha=0.30, hatch="//"))
    axR.add_patch(Circle((6.0, 4.2), 1.9, facecolor=KANTO_RED, edgecolor=INK,
                         lw=1.8, alpha=0.30, hatch="xx"))
    axR.text(3.0, 5.4, "$A$", ha="center", va="center", fontsize=15,
             fontweight="bold", color=KANTO_BLUE)
    axR.text(7.0, 5.4, "$B$", ha="center", va="center", fontsize=15,
             fontweight="bold", color=KANTO_RED)
    axR.text(5.0, 4.2, "$P(A)P(B)$", ha="center", va="center", fontsize=8.5,
             color=INK, fontweight="bold")
    axR.text(5.0, 1.6, "overlap FORCED nonzero", ha="center", va="center",
             fontsize=10, style="italic", color=INK)
    axR.text(5.0, 0.0,
             "knowing $A$ leaves $B$ unchanged\n$\\Rightarrow$ overlap is a "
             "specific size, not zero",
             ha="center", va="center", fontsize=9.5, color=KANTO_GREEN,
             fontweight="bold")

    fig.suptitle("Two opposite situations — never the same", fontsize=13.5,
                 y=1.02)
    fig.tight_layout()
    return save(fig, "ch01_me_vs_indep")


REGISTRY = [
    fig_sample_space_box,
    fig_venn_two,
    fig_venn_three,
    fig_incl_excl,
    fig_me_vs_indep,
]


def main() -> None:
    print(f"Generating Chapter 1 (Fundamentals / Route 1) figures -> {OUT} "
          f"at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
