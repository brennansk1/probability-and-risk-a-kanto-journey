#!/usr/bin/env python3
"""Generate the Chapter 0 (Orientation / notation-reading) MATH figures.

Chapter 0 teaches how to *read* the five core notational glyphs, and each
"Beat 8 -- Picture it" panel references a diagram under assets/diagrams/ that
did not yet exist. This script renders EXACTLY those five filenames. They are
notation-anatomy diagrams (callouts on symbols), not data plots, so axes,
grids and ticks are switched off and everything is laid out on a clean canvas.

  ch00_variable_vs_value   Two panels: capital L = "the slot / name of the
                           uncertain level" (ball still spinning) vs L = 3 =
                           "one value that filled the slot this run", joined by
                           a "the encounter happens" arrow.

  ch00_subscripts_team     A six-slot party menu, each slot labeled L_1..L_6
                           with values 5,8,3,12,7,6; slot 4 highlighted with a
                           "L_4 = 12: the level of the fourth Pokemon" callout.

  ch00_summation_anatomy   A large sum_{i=1}^{n} L_i with four callout arrows
                           (sigma = "the sum of"; i=1 = START; n = STOP;
                           L_i = TERM) and the worked expansion 5+8+3+12 = 28.

  ch00_function_machine    The "named machine": event A in -> box P -> a single
                           number 0.4 on a 0..1 dial out, with three parallel
                           examples f(x), P(A), E[X].

  ch00_given_bar           P(A | B) with the bar highlighted; right of bar =
                           "the given world", left = "the question"; plus a
                           small inset Venn (B circle, A-and-B sliver) showing
                           "crop the world down to B, then look at A inside".

PRINT TARGET: bound book -> 300 DPI.
INSTRUCTIONAL CLARITY: Kanto palette, color-blind-safe and grayscale-legible.
Meaning never rests on color alone -- every colored region also carries a text
label, and the two cell/role classes differ in hatch as well as hue.

Run: python figures/src/gen_ch00.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import (
    Circle,
    FancyArrowPatch,
    FancyBboxPatch,
    Rectangle,
    Wedge,
)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe).
KANTO_RED = "#EE1515"
KANTO_BLUE = "#3B4CCA"
KANTO_YEL = "#FFD733"
KANTO_GRN = "#4DAD5B"
INK = "#333333"
MUTE = "#888888"

# Light tints (kept distinct in grayscale via hatch + text labels).
RED_FILL = "#FBD3D3"
BLUE_FILL = "#D2D7F2"
YEL_FILL = "#FCEFB8"
GRN_FILL = "#D6ECDA"

PRINT_DPI = 300


def save(fig, name: str) -> Path:
    path = OUT / f"{name}.png"
    fig.savefig(path, dpi=PRINT_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [fig] {path.relative_to(ROOT)}")
    return path


def clean(ax, xlim=(0, 10), ylim=(0, 10)):
    """Turn an axes into a blank schematic canvas."""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_facecolor("white")


def callout(ax, xy, xytext, text, color, ha="center", fs=11, lw=1.6,
            connectionstyle="arc3,rad=0.0", wrap=True):
    ax.annotate(
        text, xy=xy, xytext=xytext, ha=ha, va="center", fontsize=fs,
        color=INK, wrap=wrap,
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                        connectionstyle=connectionstyle,
                        shrinkA=4, shrinkB=6),
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec=color, lw=1.4),
    )


# ---------------------------------------------------------------------------
# 1. ch00_variable_vs_value -- the slot vs the value that fills it.
# ---------------------------------------------------------------------------
def fig_variable_vs_value():
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    clean(ax, xlim=(0, 19), ylim=(0, 10))

    def pokeball(cx, cy, r, closed):
        # Top red half / bottom white, black band, center button.
        top = Wedge((cx, cy), r, 0, 180, fc=KANTO_RED, ec=INK, lw=1.6, zorder=3)
        bot = Wedge((cx, cy), r, 180, 360, fc="white", ec=INK, lw=1.6, zorder=3)
        ax.add_patch(top)
        ax.add_patch(bot)
        ax.add_patch(Rectangle((cx - r, cy - 0.10 * r), 2 * r, 0.20 * r,
                               fc=INK, ec=INK, zorder=4))
        ax.add_patch(Circle((cx, cy), 0.30 * r, fc="white", ec=INK, lw=1.6,
                            zorder=5))
        ax.add_patch(Circle((cx, cy), 0.13 * r,
                            fc=(KANTO_GRN if closed else "white"),
                            ec=INK, lw=1.4, zorder=6))

    # ---- LEFT PANEL: the slot (still uncertain) ----
    ax.add_patch(FancyBboxPatch((0.5, 1.0), 8.2, 8.0,
                                boxstyle="round,pad=0.15", fc=YEL_FILL,
                                ec=KANTO_BLUE, lw=1.8, zorder=1))
    # motion arcs to suggest spinning / undecided
    cx, cy, r = 4.6, 6.4, 1.5
    for dx in (-1.0, 1.0):
        ax.add_patch(FancyArrowPatch((cx + dx * (r + 0.5), cy + 0.6),
                                     (cx + dx * (r + 0.5), cy - 0.6),
                                     connectionstyle="arc3,rad=" +
                                     ("0.5" if dx > 0 else "-0.5"),
                                     arrowstyle="-|>", color=MUTE, lw=1.4,
                                     zorder=2))
    pokeball(cx, cy, r, closed=False)
    ax.text(4.6, 3.45, r"$L$", fontsize=46, ha="center", va="center",
            color=KANTO_BLUE, fontweight="bold")
    ax.text(4.6, 2.05, "the NAME of the uncertain level\n(the slot — not yet decided)",
            fontsize=11.5, ha="center", va="center", color=INK)

    # ---- RIGHT PANEL: one value that filled it ----
    ax.add_patch(FancyBboxPatch((10.3, 1.0), 8.2, 8.0,
                                boxstyle="round,pad=0.15", fc=GRN_FILL,
                                ec=KANTO_GRN, lw=1.8, zorder=1))
    pokeball(13.6, 6.4, 1.5, closed=True)
    ax.text(16.4, 6.4, "Lv. 3", fontsize=15, ha="center", va="center",
            color=INK, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=INK, lw=1.2))
    ax.text(14.4, 3.45, r"$L = 3$", fontsize=34, ha="center", va="center",
            color=KANTO_GRN, fontweight="bold")
    ax.text(14.4, 2.05, "ONE value that filled the slot\nthis run (a particular value)",
            fontsize=11.5, ha="center", va="center", color=INK)

    # ---- connecting arrow ----
    ax.add_patch(FancyArrowPatch((8.85, 5.0), (10.15, 5.0),
                                 arrowstyle="-|>", color=KANTO_RED, lw=2.6,
                                 zorder=7))
    ax.text(9.5, 5.75, "the encounter\nhappens", fontsize=10.5, ha="center",
            va="center", color=KANTO_RED, fontweight="bold")

    ax.text(9.5, 9.55, "Capital = the slot     vs.     lowercase value = what fills it",
            fontsize=13, ha="center", va="center", color=INK, fontweight="bold")
    return save(fig, "ch00_variable_vs_value")


# ---------------------------------------------------------------------------
# 2. ch00_subscripts_team -- the six-slot party, L_1..L_6.
# ---------------------------------------------------------------------------
def fig_subscripts_team():
    fig, ax = plt.subplots(figsize=(9.5, 5.8))
    clean(ax, xlim=(0, 19), ylim=(0, 12))

    values = [5, 8, 3, 12, 7, 6]
    # 2 columns x 3 rows party menu.
    cols = [1.0, 10.0]
    rows = [7.6, 4.6, 1.6]  # top to bottom (top row clears the title band)
    positions = []
    for r_i, ry in enumerate(rows):
        for c_i, cx in enumerate(cols):
            positions.append((cx, ry, r_i * 2 + c_i))  # slot index 0..5

    ax.text(9.5, 11.3, "Your party — a numbered family of levels",
            fontsize=13, ha="center", va="center", color=INK, fontweight="bold")

    for (x, y, idx) in positions:
        highlight = (idx == 3)  # slot 4 (1-based)
        face = YEL_FILL if highlight else "#FFFFFF"
        edge = KANTO_RED if highlight else INK
        lw = 2.6 if highlight else 1.4
        ax.add_patch(FancyBboxPatch((x, y, ), 8.0, 2.4,
                                    boxstyle="round,pad=0.06", fc=face,
                                    ec=edge, lw=lw, zorder=2))
        # mini pokeball icon (monochrome, no species art)
        bcx, bcy = x + 1.0, y + 1.2
        ax.add_patch(Wedge((bcx, bcy), 0.55, 0, 180, fc=KANTO_RED, ec=INK,
                           lw=1.2, zorder=3))
        ax.add_patch(Wedge((bcx, bcy), 0.55, 180, 360, fc="white", ec=INK,
                           lw=1.2, zorder=3))
        ax.add_patch(Rectangle((bcx - 0.55, bcy - 0.06), 1.10, 0.12, fc=INK,
                               zorder=4))
        ax.add_patch(Circle((bcx, bcy), 0.17, fc="white", ec=INK, lw=1.0,
                            zorder=5))
        # subscript label and value
        ax.text(x + 2.3, y + 1.55, rf"$L_{{{idx+1}}}$", fontsize=24,
                ha="left", va="center", color=INK, fontweight="bold")
        ax.text(x + 2.3, y + 0.65, f"= {values[idx]}", fontsize=15,
                ha="left", va="center", color=INK)
        # slot number badge
        ax.add_patch(Circle((x + 7.3, y + 1.85), 0.32,
                            fc=(KANTO_RED if highlight else MUTE), ec=INK,
                            lw=1.0, zorder=4))
        ax.text(x + 7.3, y + 1.85, str(idx + 1), fontsize=11, ha="center",
                va="center", color="white", fontweight="bold", zorder=5)

    # callout to slot 4 (cols[1], rows[1]); note sits below the menu, clear of
    # every slot box, and arcs up into the highlighted slot from beneath.
    hx, hy = cols[1], rows[1]
    callout(ax, xy=(hx + 0.05, hy + 0.05), xytext=(9.4, 0.55),
            text=r"$L_4 = 12$:  the level of the FOURTH Pokémon"
                 "\n" r"(never $L\times4$, never $L^4$)",
            color=KANTO_RED, ha="center", fs=11.5,
            connectionstyle="arc3,rad=0.25")
    return save(fig, "ch00_subscripts_team")


# ---------------------------------------------------------------------------
# 3. ch00_summation_anatomy -- the four parts of sum_{i=1}^{n} L_i.
# ---------------------------------------------------------------------------
def fig_summation_anatomy():
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    clean(ax, xlim=(0, 19), ylim=(0, 11))

    # Big expression, drawn from its parts so we can point at each.
    cx = 8.0
    ax.text(cx, 6.4, r"$\sum$", fontsize=96, ha="center", va="center",
            color=KANTO_BLUE, fontweight="bold")
    ax.text(cx, 8.7, r"$n$", fontsize=30, ha="center", va="center", color=INK)
    ax.text(cx, 4.05, r"$i = 1$", fontsize=24, ha="center", va="center",
            color=INK)
    ax.text(cx + 2.4, 6.4, r"$L_i$", fontsize=44, ha="center", va="center",
            color=INK, fontweight="bold")

    # Four callouts.
    # sigma
    callout(ax, xy=(cx - 0.9, 6.6), xytext=(2.4, 8.7),
            text="capital sigma — S for SUM\nreads: “the sum of”",
            color=KANTO_BLUE, fs=10.5, connectionstyle="arc3,rad=0.25")
    # n on top = STOP
    callout(ax, xy=(cx + 0.55, 8.8), xytext=(13.2, 9.6),
            text="STOP: keep going\nuntil $i$ reaches $n$",
            color=KANTO_RED, fs=10.5, connectionstyle="arc3,rad=-0.2")
    # i=1 below = START
    callout(ax, xy=(cx - 0.2, 3.7), xytext=(2.5, 2.5),
            text="START: the index $i$\nbegins at 1",
            color=KANTO_GRN, fs=10.5, connectionstyle="arc3,rad=-0.25")
    # term L_i
    callout(ax, xy=(cx + 2.9, 6.5), xytext=(15.3, 7.7),
            text="TERM: what you\nadd each time\n($i$ plugged in)",
            color="#C9971C", fs=10.5, connectionstyle="arc3,rad=0.2")

    # Worked expansion banner.
    ax.add_patch(FancyBboxPatch((1.2, 0.35), 16.6, 1.55,
                                boxstyle="round,pad=0.1", fc=YEL_FILL,
                                ec=INK, lw=1.4, zorder=1))
    ax.text(9.5, 1.12,
            r"$\sum_{i=1}^{4} L_i \;=\; L_1+L_2+L_3+L_4 \;=\; 5+8+3+12 \;=\; 28$",
            fontsize=17, ha="center", va="center", color=INK)
    return save(fig, "ch00_summation_anatomy")


# ---------------------------------------------------------------------------
# 4. ch00_function_machine -- name + bracketed input -> a number out.
# ---------------------------------------------------------------------------
def fig_function_machine():
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    clean(ax, xlim=(0, 19), ylim=(0, 11))

    ax.text(9.5, 10.4, 'A named operation: input in, one number out — not multiplication',
            fontsize=12.5, ha="center", va="center", color=INK, fontweight="bold")

    # input chip: event A
    ax.add_patch(FancyBboxPatch((0.6, 6.0), 3.0, 1.8,
                                boxstyle="round,pad=0.1", fc=BLUE_FILL,
                                ec=KANTO_BLUE, lw=1.8, zorder=2))
    ax.text(2.1, 6.9, r"event $A$", fontsize=15, ha="center", va="center",
            color=INK, fontweight="bold")
    ax.text(2.1, 5.35, "the input\n(a thing that might happen)", fontsize=9.5,
            ha="center", va="center", color=INK)

    # arrow in
    ax.add_patch(FancyArrowPatch((3.75, 6.9), (5.55, 6.9), arrowstyle="-|>",
                                 color=INK, lw=2.4, zorder=3))

    # the machine box: P
    ax.add_patch(FancyBboxPatch((5.7, 5.7), 3.5, 2.5,
                                boxstyle="round,pad=0.12", fc=YEL_FILL,
                                ec=KANTO_RED, lw=2.2, zorder=2))
    ax.text(7.45, 7.35, r"$P(\,\cdot\,)$", fontsize=26, ha="center",
            va="center", color=INK, fontweight="bold")
    ax.text(7.45, 6.25, "the probability\noperation", fontsize=10, ha="center",
            va="center", color=INK)

    # arrow out
    ax.add_patch(FancyArrowPatch((9.35, 6.9), (11.15, 6.9), arrowstyle="-|>",
                                 color=INK, lw=2.4, zorder=3))

    # output dial 0..1
    dial_c = (13.4, 6.9)
    dr = 1.6
    ax.add_patch(Wedge(dial_c, dr, 0, 180, fc="white", ec=INK, lw=1.8,
                       zorder=2))
    ax.add_patch(Wedge(dial_c, dr, 0, 180, width=0.001, fc="none"))
    # tick labels 0 and 1
    ax.text(dial_c[0] - dr - 0.25, dial_c[1] - 0.05, "0", fontsize=12,
            ha="right", va="center", color=INK)
    ax.text(dial_c[0] + dr + 0.25, dial_c[1] - 0.05, "1", fontsize=12,
            ha="left", va="center", color=INK)
    # needle pointing to 0.4 -> angle from 180 (0) to 0 (1); 0.4 -> 180-0.4*180=108deg
    import math
    ang = math.radians(180 - 0.4 * 180)
    nx = dial_c[0] + (dr - 0.2) * math.cos(ang)
    ny = dial_c[1] + (dr - 0.2) * math.sin(ang)
    ax.add_patch(FancyArrowPatch(dial_c, (nx, ny), arrowstyle="-|>",
                                 color=KANTO_RED, lw=2.6, zorder=4))
    ax.add_patch(Circle(dial_c, 0.12, fc=INK, zorder=5))
    ax.text(dial_c[0], dial_c[1] - 1.05, "0.4", fontsize=18, ha="center",
            va="center", color=KANTO_RED, fontweight="bold")
    ax.text(dial_c[0], dial_c[1] + 1.95, "one number in [0, 1]", fontsize=10,
            ha="center", va="center", color=INK)

    # Three parallel examples.
    ax.add_patch(FancyBboxPatch((1.0, 0.5), 16.8, 3.1,
                                boxstyle="round,pad=0.12", fc="#F4F4EC",
                                ec=MUTE, lw=1.2, zorder=1))
    ex = [
        (r"$f(x)$", "“$f$ of $x$”", "returns a number", KANTO_BLUE),
        (r"$P(A)$", "“probability of $A$”", "a number in [0, 1]", KANTO_RED),
        (r"$\mathbb{E}[X]$", "“expected value of $X$”", "the long-run average",
         KANTO_GRN),
    ]
    xs = [4.0, 9.4, 14.8]
    for (sym, rd, ret, col), x in zip(ex, xs):
        ax.text(x, 2.95, sym, fontsize=22, ha="center", va="center",
                color=col, fontweight="bold")
        ax.text(x, 1.95, rd, fontsize=11, ha="center", va="center", color=INK)
        ax.text(x, 1.15, ret, fontsize=9.5, ha="center", va="center",
                color=MUTE)
    return save(fig, "ch00_function_machine")


# ---------------------------------------------------------------------------
# 5. ch00_given_bar -- P(A | B): question | given world, plus inset Venn.
# ---------------------------------------------------------------------------
def fig_given_bar():
    fig, ax = plt.subplots(figsize=(9.5, 5.8))
    clean(ax, xlim=(0, 19), ylim=(0, 11))

    # Build P( A | B ) from parts so each piece can be pointed at.
    yexp = 7.6
    ax.text(3.3, yexp, r"$P($", fontsize=58, ha="center", va="center",
            color=INK, fontweight="bold")
    ax.text(5.9, yexp, r"$A$", fontsize=54, ha="center", va="center",
            color=KANTO_GRN, fontweight="bold")
    ax.text(8.1, yexp, r"$\mid$", fontsize=64, ha="center", va="center",
            color=KANTO_RED, fontweight="bold")
    ax.text(10.3, yexp, r"$B$", fontsize=54, ha="center", va="center",
            color=KANTO_BLUE, fontweight="bold")
    ax.text(12.6, yexp, r"$)$", fontsize=58, ha="center", va="center",
            color=INK, fontweight="bold")

    # highlight ring on the bar
    ax.add_patch(Circle((8.1, yexp), 0.95, fc="none", ec=KANTO_RED, lw=2.2,
                        ls="--", zorder=4))
    ax.text(8.1, 9.55, 'the bar reads:\n“given that”', fontsize=11,
            ha="center", va="center", color=KANTO_RED, fontweight="bold")
    ax.add_patch(FancyArrowPatch((8.1, 9.0), (8.1, yexp + 1.0),
                                 arrowstyle="-|>", color=KANTO_RED, lw=1.8,
                                 zorder=4))

    # bracket + label under LEFT (question)
    ax.plot([5.0, 6.8], [6.2, 6.2], color=KANTO_GRN, lw=2.2)
    ax.plot([5.0, 5.0], [6.2, 6.45], color=KANTO_GRN, lw=2.2)
    ax.plot([6.8, 6.8], [6.2, 6.45], color=KANTO_GRN, lw=2.2)
    ax.text(5.9, 5.05, "THE QUESTION\nfind the chance of this,\ninside that world",
            fontsize=10.5, ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc=GRN_FILL, ec=KANTO_GRN,
                      lw=1.4))

    # bracket + label under RIGHT (given world)
    ax.plot([9.4, 11.2], [6.2, 6.2], color=KANTO_BLUE, lw=2.2)
    ax.plot([9.4, 9.4], [6.2, 6.45], color=KANTO_BLUE, lw=2.2)
    ax.plot([11.2, 11.2], [6.2, 6.45], color=KANTO_BLUE, lw=2.2)
    ax.text(10.3, 5.05, "THE GIVEN WORLD\nassume this happened —\neverything to the right",
            fontsize=10.5, ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc=BLUE_FILL, ec=KANTO_BLUE,
                      lw=1.4))

    # ---- inset Venn: crop world to B, look at A inside ----
    inx, iny = 15.6, 6.6
    # dimmed full sample space
    ax.add_patch(FancyBboxPatch((13.1, 2.2), 5.6, 5.0,
                                boxstyle="round,pad=0.05", fc="#EDEDED",
                                ec=MUTE, lw=1.2, zorder=1))
    ax.text(13.45, 6.85, "sample space\n(dimmed)", fontsize=8.5, ha="left",
            va="top", color=MUTE, zorder=2)
    # circle B (the given world, in focus)
    bcirc = Circle((inx, iny - 0.7), 1.85, fc=BLUE_FILL, ec=KANTO_BLUE,
                   lw=2.0, alpha=0.9, zorder=2)
    ax.add_patch(bcirc)
    ax.text(inx + 0.55, iny - 1.85, r"$B$", fontsize=18, ha="center",
            va="center", color=KANTO_BLUE, fontweight="bold", zorder=4)
    # sliver A-and-B highlighted: circle A overlapping, only show overlap accent
    acirc = Circle((inx - 1.1, iny - 0.1), 1.25, fc=GRN_FILL, ec=KANTO_GRN,
                   lw=2.0, alpha=0.85, zorder=3)
    ax.add_patch(acirc)
    ax.text(inx - 1.45, iny + 0.75, r"$A$", fontsize=16, ha="center",
            va="center", color=KANTO_GRN, fontweight="bold", zorder=4)
    ax.text(inx - 0.45, iny - 0.35, r"$A\cap B$", fontsize=10, ha="center",
            va="center", color=INK, fontweight="bold", zorder=5)
    ax.text(15.9, 2.55,
            "condition = crop the world down to $B$,\nthen look at $A$ inside",
            fontsize=8.8, ha="center", va="bottom", color=INK, zorder=4)

    ax.text(6.5, 2.6, "The bar is NOT symmetric:\n$P(A\\mid B)\\neq P(B\\mid A)$ in general.",
            fontsize=11, ha="center", va="center", color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc=YEL_FILL, ec="#C9971C",
                      lw=1.4))
    return save(fig, "ch00_given_bar")


def main():
    print("Generating Chapter 0 orientation figures @ 300 DPI:")
    fig_variable_vs_value()
    fig_subscripts_team()
    fig_summation_anatomy()
    fig_function_machine()
    fig_given_bar()
    print("Done.")


if __name__ == "__main__":
    main()
