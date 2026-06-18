#!/usr/bin/env python3
"""Generate every Chapter 15 (Champion / exam-execution) math figure.

Chapter 15's "Picture it" beats reference four diagrams under
assets/diagrams/ that did not exist yet. This script renders one
purpose-built PNG per figure so each picture matches its alt text and
caption exactly:

  ch15_two_pass_timeline   Concept 1, Beat 8: the 180-minute clock as a
                           two-pass timeline. Pass 1 sweeps all 30 slots
                           (gifts solved = green, monsters flagged with a
                           quick provisional guess = red, banking time);
                           Pass 2 returns only to the flagged slots using
                           the banked reservoir; a final sliver bubbles
                           every blank.
  ch15_recognition_tree    Concept 2, Beat 8: a decision tree rooted at
                           "what does the last sentence ask for?"
                           (probability / expectation / variance), each
                           branch forking on the stem's tell to a leaf that
                           names the tool + its one-line shortcut.
  ch15_shortcut_catalog    Concept 3, Beat 8: a reference-card grid of the
                           seven exam shortcuts, each tile = trigger tell on
                           top, identity below.
  ch15_sanity_corridors    Concept 4, Beat 8: a column of number lines, one
                           per quantity, shading the legal corridor and
                           marking a sample impossible answer with a red X
                           captioned "recheck before bubbling."

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded
element ALSO carries a hatch / glyph / label so the figures stay legible in
grayscale.

Run: python figures/src/gen_ch15.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Rectangle
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


# --------------------------------------------------------------------------
# 1. Concept 1, Beat 8: the two-pass 180-minute timeline.
# --------------------------------------------------------------------------
def fig_two_pass_timeline():
    fig, (axP1, axP2) = plt.subplots(
        2, 1, figsize=(11.2, 6.0),
        gridspec_kw={"height_ratios": [1, 1], "hspace": 0.55})
    fig.suptitle("The two-pass clock: harvest the gifts, flag the monsters, "
                 "spend the banked time", y=1.02, fontsize=15)

    # A reproducible mix of 30 question slots: gifts (solved green),
    # monsters (quick provisional guess + flag, red). True = gift.
    rng = np.random.default_rng(15)
    n = 30
    is_gift = rng.random(n) < 0.6   # ~60% recognized gifts on pass 1
    is_gift[0] = True
    is_gift[1] = True
    is_gift[-1] = False             # ensure at least one flag near the end

    slot_w = 1.0
    gap = 0.18

    def _draw_slots(ax, mode):
        """mode='pass1' draws all 30; 'pass2' greys the gifts, highlights flags."""
        for i in range(n):
            x = i * (slot_w + gap)
            gift = is_gift[i]
            if mode == "pass1":
                color = KANTO_GREEN if gift else KANTO_RED
                hatch = "//" if gift else "xx"
                alpha = 0.85
            else:  # pass2: gifts already banked (faded), flags are the work
                if gift:
                    color, hatch, alpha = KANTO_GRAY, "..", 0.25
                else:
                    color, hatch, alpha = KANTO_RED, "xx", 0.9
            ax.add_patch(Rectangle((x, 0), slot_w, 1.0, facecolor=color,
                                   edgecolor=INK, lw=0.9, alpha=alpha,
                                   hatch=hatch))
            if mode == "pass1" and not gift:
                # flag marker on the monsters
                ax.text(x + slot_w / 2, 1.18, "⚑", ha="center",
                        va="bottom", fontsize=11, color=KANTO_RED,
                        fontweight="bold")
        ax.set_xlim(-0.6, n * (slot_w + gap) + 2.6)
        ax.set_ylim(-0.5, 1.9)
        ax.set_aspect("auto")
        ax.grid(False)
        ax.set_yticks([])
        ax.set_xticks([])
        for s in ax.spines.values():
            s.set_visible(False)

    total = n * (slot_w + gap)

    # ---- PASS 1 ----
    _draw_slots(axP1, "pass1")
    axP1.annotate("", xy=(total + 0.2, -0.32), xytext=(-0.4, -0.32),
                  arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.6))
    axP1.text(-0.4, -0.30, "0 min", ha="left", va="top", fontsize=9,
              color=INK)
    axP1.text(total + 0.2, -0.30, "180 min", ha="right", va="top",
              fontsize=9, color=INK)
    axP1.text(total / 2, -0.30, "front → back, all 30 slots",
              ha="center", va="top", fontsize=10, color=INK)
    axP1.set_title("PASS 1  —  solve gifts, flag + provisionally guess "
                   "monsters (banking time)", fontsize=12, loc="left",
                   color=INK, pad=18)

    # legend chips for pass 1
    axP1.add_patch(Rectangle((total + 0.4, 1.15), 0.7, 0.5,
                   facecolor=KANTO_GREEN, edgecolor=INK, lw=0.8, hatch="//"))
    axP1.text(total + 1.25, 1.40, "gift solved", va="center", fontsize=9.5,
              color=INK)
    axP1.add_patch(Rectangle((total + 0.4, 0.4), 0.7, 0.5,
                   facecolor=KANTO_RED, edgecolor=INK, lw=0.8, hatch="xx"))
    axP1.text(total + 1.25, 0.65, "flagged ⚑", va="center", fontsize=9.5,
              color=INK)

    # --- decorative sprite (margin only): Charizard = the "monster" problem,
    # placed in the right margin beside the legend, clear of every slot/label.
    # Illustrative only; the timeline teaches identically with it removed.
    place_sprite(axP1, front(6), (total + 1.95, -0.05), zoom=0.4, alpha=0.92,
                 zorder=2)

    # banked-time reservoir cue under pass 1
    axP1.annotate("gifts bank time ↓",
                  xy=(total / 2, -0.05), xytext=(total / 2, 1.55),
                  ha="center", fontsize=9.5, color=KANTO_GREEN,
                  fontweight="bold",
                  arrowprops=dict(arrowstyle="-|>", color=KANTO_GREEN, lw=1.2))

    # ---- PASS 2 ----
    _draw_slots(axP2, "pass2")
    # banked reservoir: a green bar feeding the flagged slots
    res_y = 1.30
    axP2.add_patch(FancyBboxPatch((-0.4, res_y), total * 0.62, 0.42,
                   boxstyle="round,pad=0.02", facecolor=KANTO_GREEN,
                   edgecolor=INK, lw=1.0, alpha=0.55, hatch="//"))
    axP2.text(total * 0.31 - 0.4, res_y + 0.21, "banked time reservoir",
              ha="center", va="center", fontsize=9.5, color=INK,
              fontweight="bold")
    # arrow: reservoir spends on the flagged (red) slots
    flag_idx = [i for i in range(n) if not is_gift[i]]
    target = flag_idx[len(flag_idx) // 2]
    tx = target * (slot_w + gap) + slot_w / 2
    axP2.add_patch(FancyArrowPatch((total * 0.20, res_y), (tx, 1.05),
                   mutation_scale=16, lw=2.0, color=KANTO_GREEN))
    axP2.set_title("PASS 2  —  return only to the flags, spend the "
                   "banked time", fontsize=12, loc="left", color=INK, pad=18)

    # final sliver: bubble every blank
    sliver_x = total + 0.2
    axP2.add_patch(Rectangle((sliver_x, 0), 0.55, 1.0, facecolor=KANTO_YEL,
                   edgecolor=INK, lw=1.0, hatch=".."))
    axP2.annotate("bubble\nevery blank", xy=(sliver_x + 0.28, 0.5),
                  xytext=(sliver_x + 1.1, 1.45), ha="left", va="center",
                  fontsize=9.5, color=INK, fontweight="bold",
                  arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.2),
                  bbox=dict(boxstyle="round,pad=0.3", fc="#FFF6D6",
                            ec=KANTO_YEL, lw=1.2))
    axP2.text(-0.4, -0.30, "final sweep at the buzzer — zero blanks",
              ha="left", va="top", fontsize=9.5, color=INK)

    # --- decorative item (margin only): a Poké Ball beside the "bubble every
    # blank" sliver — every question gets a ball thrown at it. Off the data.
    place_sprite(axP2, item("poke-ball"), (sliver_x + 1.35, 0.35), zoom=0.85,
                 alpha=0.95, zorder=2)

    return save(fig, "ch15_two_pass_timeline")


# --------------------------------------------------------------------------
# 2. Concept 2, Beat 8: the archetype-recognition decision tree.
# --------------------------------------------------------------------------
def fig_recognition_tree():
    fig, ax = plt.subplots(figsize=(13.0, 8.4))
    fig.suptitle("The recognition tree: what is asked → find the tell "
                 "→ name the tool", y=0.985, fontsize=16)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis("off")

    def chip_node(x, y, w, h, text, accent, hatch, fs=10, weight="normal"):
        """Light-fill node with a thick accent border + a small hatched color
        chip on the left edge: color-coded for sighted readers, hatch+border
        for grayscale, and text always on a pale fill so it stays legible."""
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                     boxstyle="round,pad=0.03", facecolor="white",
                     edgecolor=accent, lw=2.0))
        chip_w = 0.30
        ax.add_patch(Rectangle((x - w / 2 + 0.04, y - h / 2 + 0.04),
                     chip_w, h - 0.08, facecolor=accent, edgecolor=INK,
                     lw=0.8, alpha=0.9, hatch=hatch))
        ax.text(x + chip_w / 2, y, text, ha="center", va="center",
                fontsize=fs, color=INK, fontweight=weight)

    # Root.
    ax.add_patch(FancyBboxPatch((6.0 - 2.3, 9.05 - 0.48), 4.6, 0.96,
                 boxstyle="round,pad=0.03", facecolor="#FFF6D6",
                 edgecolor=KANTO_YEL, lw=2.2, hatch=".."))
    ax.text(6.0, 9.05, "ROOT: what does the\nlast sentence ASK FOR?",
            ha="center", va="center", fontsize=11.5, color=INK,
            fontweight="bold")

    # Tier-1: the three quantities asked.
    q = [(2.2, 7.5, "a PROBABILITY"),
         (6.0, 7.5, "an EXPECTATION  $\\mathbb{E}[X]$"),
         (9.8, 7.5, "a VARIANCE")]
    for (x, y, t) in q:
        chip_node(x, y, 3.2, 0.74, t, KANTO_BLUE, "//", fs=10, weight="bold")
        ax.annotate("", xy=(x, y + 0.40), xytext=(6.0, 8.52),
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))

    # Leaves: (parent_x, leaf_x, leaf_y, tell, tool + shortcut)
    rows_y = (5.55, 4.05, 2.55)
    leaves = [
        # under PROBABILITY
        (2.2, 2.2, rows_y[0], "“given that / flagged”",
         "BAYES\n$P(A\\mid B)$, flipped bar"),
        (2.2, 2.2, rows_y[1], "“at least one”",
         "COMPLEMENT\n$1-P(\\text{none})$"),
        (2.2, 2.2, rows_y[2], "“approx. normal, large $n$”",
         "CLT\n$+$ continuity correction"),
        # under EXPECTATION
        (6.0, 6.0, rows_y[0], "“average rate per interval”",
         "POISSON\n$\\mu=\\sigma^2=\\lambda$"),
        (6.0, 6.0, rows_y[1], "“time until / memoryless”",
         "EXPONENTIAL\n$\\mathbb{E}[X-d\\mid X>d]=\\theta$"),
        (6.0, 6.0, rows_y[2], "“deductible / limit”",
         "LOSS MODEL\n$\\alpha[(X\\wedge u)-(X\\wedge d)]$"),
        # under VARIANCE
        (9.8, 9.8, rows_y[0], "“strongest / $k$-th of $n$”",
         "ORDER STATS\n$[F(x)]^n$"),
        (9.8, 9.8, rows_y[1], "polynomial $\\times\\,e^{-x/\\theta}$",
         "GAMMA KERNEL\n$\\Gamma(\\alpha)\\theta^{\\alpha}$"),
        (9.8, 9.8, rows_y[2], "given $M_X(t)$",
         "MGF MOMENTS\n$M_X''(0)=\\mathbb{E}[X^2]$"),
    ]
    for (px, lx, ly, tell, tool) in leaves:
        # connector from the tier-1 node down the spine, then to this leaf
        ax.annotate("", xy=(lx, ly + 0.74), xytext=(px, 7.13),
                    arrowprops=dict(arrowstyle="-", color=KANTO_GRAY, lw=1.0))
        # the tell rides on the edge
        ax.text(lx, ly + 0.74, tell, ha="center", va="center", fontsize=8.0,
                color="#B01010", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.20", fc="white",
                          ec=KANTO_YEL, lw=1.0))
        chip_node(lx, ly, 3.3, 0.92, tool, KANTO_GREEN, "xx", fs=8.6,
                  weight="bold")

    ax.text(6.0, 1.25,
            "Land on the tool — and its one-line shortcut — "
            "before the pencil moves.",
            ha="center", va="center", fontsize=11, color=INK,
            style="italic")

    # --- decorative sprites (empty bottom corners only): Gastly tags the
    # "given that / flagged" Ghost-scanner tell (→ Bayes); Spearow tags the
    # "average rate per interval" flock tell (→ Poisson). Off every node/edge.
    place_sprite(ax, front(92), (1.15, 0.55), zoom=0.45, alpha=0.9, zorder=2)
    place_sprite(ax, front(21), (10.9, 0.55), zoom=0.45, alpha=0.9, zorder=2)

    return save(fig, "ch15_recognition_tree")


# --------------------------------------------------------------------------
# 3. Concept 3, Beat 8: the seven-shortcut reference-card grid.
# --------------------------------------------------------------------------
def fig_shortcut_catalog():
    fig, ax = plt.subplots(figsize=(11.6, 7.2))
    fig.suptitle("The shortcut catalog: each tell (top) points to the "
                 "identity (bottom) that collapses the work",
                 y=0.995, fontsize=14)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # (tell, identity) for the seven shortcuts.
    cards = [
        ("polynomial $\\times\\,e^{-x/\\theta}$",
         "GAMMA INTEGRAL\n$\\int_0^\\infty x^{\\alpha-1}"
         "e^{-x/\\theta}dx=\\Gamma(\\alpha)\\theta^{\\alpha}$"),
        ("$\\mathbb{E}[X]$, $X\\geq 0$, survival given",
         "DARTH VADER\n$\\mathbb{E}[X]=\\int_0^\\infty S(x)\\,dx$"),
        ("exponential $+$ already waited / deductible",
         "MEMORYLESSNESS\n$\\mathbb{E}[X-d\\mid X>d]=\\theta,\\ "
         "\\mathbb{E}[(X-d)_+]=\\theta e^{-d/\\theta}$"),
        ("count over an interval",
         "POISSON\n$\\mu=\\sigma^2=\\lambda$"),
        ("rare event, many trials",
         "BINOMIAL $\\to$ POISSON\n$\\mathrm{Bin}(n,p)\\approx"
         "\\mathrm{Poi}(np)$"),
        ("$M_X(t)$ given",
         "MGF MOMENTS\n$M_X'(0)=\\mathbb{E}[X],\\ "
         "M_X''(0)=\\mathbb{E}[X^2]$"),
        ("discrete sum, normal approx",
         "CONTINUITY CORRECTION\n$P(X\\leq k)\\approx"
         "\\Phi\\left(\\frac{k+0.5-\\mu}{\\sigma}\\right)$"),
    ]

    cols, rows = 3, 3
    margin = 0.35
    cw = (12 - margin * (cols + 1)) / cols
    ch = (8.2 - margin * (rows + 1)) / rows
    y_top = 8.2

    tile_colors = [KANTO_GREEN, KANTO_BLUE, KANTO_RED, KANTO_YEL,
                   "#00BCD4", "#7B61FF", "#FF7043"]
    tile_hatch = ["xx", "//", "\\\\", "..", "//", "xx", "\\\\"]

    for idx, (tell, ident) in enumerate(cards):
        r = idx // cols
        c = idx % cols
        x0 = margin + c * (cw + margin)
        y0 = y_top - (r + 1) * ch - r * margin
        ax.add_patch(FancyBboxPatch((x0, y0), cw, ch,
                     boxstyle="round,pad=0.05", facecolor="white",
                     edgecolor=INK, lw=1.4))
        # tell band on top (color + hatch for grayscale legibility)
        band_h = ch * 0.30
        ax.add_patch(Rectangle((x0, y0 + ch - band_h), cw, band_h,
                     facecolor=tile_colors[idx], edgecolor=INK, lw=1.0,
                     alpha=0.55, hatch=tile_hatch[idx]))
        ax.text(x0 + cw / 2, y0 + ch - band_h / 2, tell, ha="center",
                va="center", fontsize=8.6, color=INK, fontweight="bold")
        # identity below
        ax.text(x0 + cw / 2, y0 + (ch - band_h) / 2, ident, ha="center",
                va="center", fontsize=8.8, color=INK)

    # eighth slot: the closing reminder.
    r, c = 2, 1
    x0 = margin + c * (cw + margin)
    y0 = y_top - (r + 1) * ch - r * margin
    ax.add_patch(FancyBboxPatch((x0, y0), cw, ch,
                 boxstyle="round,pad=0.05", facecolor="#FFF6D6",
                 edgecolor=KANTO_YEL, lw=1.6, hatch=".."))
    ax.text(x0 + cw / 2, y0 + ch / 2,
            "Before you integrate\nby parts, ask:\ngamma? survival?\nmemoryless?",
            ha="center", va="center", fontsize=9.5, color=INK,
            fontweight="bold", style="italic")

    # --- decorative sprite (empty 9th grid cell only): Charizard, whose flame
    # is the worked gamma-kernel example (WE 15.3). Fills the blank tile, sits
    # over no identity or tell. Purely illustrative.
    r9, c9 = 2, 2
    x9 = margin + c9 * (cw + margin)
    y9 = y_top - (r9 + 1) * ch - r9 * margin
    place_sprite(ax, front(6), (x9 + cw / 2, y9 + ch / 2), zoom=0.62,
                 alpha=0.95, zorder=2)
    ax.text(x9 + cw / 2, y9 + 0.12, "gamma kernel = Charizard's flame",
            ha="center", va="bottom", fontsize=7.6, color=KANTO_GRAY,
            style="italic")

    return save(fig, "ch15_shortcut_catalog")


# --------------------------------------------------------------------------
# 4. Concept 4, Beat 8: standing sanity corridors with impossible answers.
# --------------------------------------------------------------------------
def fig_sanity_corridors():
    fig, axes = plt.subplots(4, 1, figsize=(10.4, 7.4),
                             gridspec_kw={"hspace": 0.95})
    fig.suptitle("Standing sanity corridors: every quantity has a region it "
                 "cannot legally leave", y=0.99, fontsize=14)

    def base(ax, lo, hi, title):
        ax.set_xlim(lo, hi)
        ax.set_ylim(-1, 1)
        ax.grid(False)
        ax.set_yticks([])
        for s in ("left", "right", "top"):
            ax.spines[s].set_visible(False)
        ax.spines["bottom"].set_position(("data", 0))
        ax.spines["bottom"].set_color(INK)
        ax.spines["bottom"].set_linewidth(1.4)
        ax.set_title(title, fontsize=11, loc="left", color=INK, pad=4)

    def corridor(ax, a, b, color, hatch, label):
        ax.axvspan(a, b, ymin=0.30, ymax=0.70, facecolor=color, alpha=0.40,
                   hatch=hatch, edgecolor=INK, lw=1.0)
        ax.text((a + b) / 2, 0.62, label, ha="center", va="bottom",
                fontsize=9, color=INK, fontweight="bold")

    def red_x(ax, x, caption):
        ax.plot(x, 0, marker="X", markersize=15, color=KANTO_RED,
                markeredgecolor=INK, markeredgewidth=1.0, zorder=5)
        ax.annotate(caption, xy=(x, 0), xytext=(x, -0.78), ha="center",
                    va="top", fontsize=8.4, color=KANTO_RED,
                    fontweight="bold",
                    arrowprops=dict(arrowstyle="-|>", color=KANTO_RED,
                                    lw=1.1))

    # (a) Probability in [0,1]; impossible 1.4.
    ax = axes[0]
    base(ax, -0.4, 1.7, "Probability  —  legal corridor $[0,1]$")
    corridor(ax, 0, 1, KANTO_GREEN, "//", "$0\\leq P\\leq 1$")
    ax.set_xticks([0, 0.5, 1])  # 1.4 omitted: the red X already marks it
    red_x(ax, 1.4, "$P=1.4$\nrecheck before bubbling")

    # (b) Variance in [0, inf); impossible -3.
    ax = axes[1]
    base(ax, -4.5, 6.0, "Variance  —  legal corridor $[0,\\infty)$")
    corridor(ax, 0, 6.0, KANTO_BLUE, "\\\\", "$\\mathrm{Var}\\geq 0$")
    ax.annotate("", xy=(6.0, 0), xytext=(5.4, 0),
                arrowprops=dict(arrowstyle="-|>", color=KANTO_BLUE, lw=1.4))
    ax.set_xticks([-3, 0, 3, 6])
    red_x(ax, -3, "$\\mathrm{Var}=-3$\nrecheck before bubbling")

    # (c) Per-payment vs per-loss mean: payment must be <= loss.
    ax = axes[2]
    base(ax, -0.5, 10.0,
         "Expected payment vs expected loss  —  payment $\\leq$ loss")
    corridor(ax, 0, 5, KANTO_GREEN, "//",
             "payment lives in $[0,\\ \\mathbb{E}[\\text{loss}]]$")
    ax.axvline(5, ymin=0.20, ymax=0.80, color=INK, lw=1.4, ls="--")
    ax.text(5, 0.80, "$\\mathbb{E}[\\text{loss}]=5$", ha="center", va="bottom",
            fontsize=8.6, color=INK)
    ax.annotate("", xy=(5.0, -0.30), xytext=(0.2, -0.30),
                arrowprops=dict(arrowstyle="-|>", color=KANTO_GREEN, lw=1.3))
    ax.set_xticks([0, 5, 8])
    # decorative item (empty gap between the loss line and the impossible X):
    # a Potion = the payment/recovery this corridor bounds. Off the data.
    place_sprite(ax, item("potion"), (6.4, 0.5), zoom=0.7, alpha=0.95,
                 xycoords="data", zorder=3)
    red_x(ax, 8, "$\\mathbb{E}[\\text{pay}]=8>5$\nrecheck before bubbling")

    # (d) Weighted average between smallest and largest input.
    ax = axes[3]
    base(ax, -0.05, 0.85,
         "Weighted average  —  must lie between its smallest and "
         "largest input")
    corridor(ax, 0.1, 0.6, KANTO_YEL, "..",
             "inputs $\\{0.1,\\,0.3,\\,0.6\\}\\Rightarrow$ avg $\\in[0.1,0.6]$")
    for v in (0.1, 0.3, 0.6):
        ax.plot(v, 0, marker="o", markersize=7, color=KANTO_BLUE,
                markeredgecolor=INK, markeredgewidth=0.8, zorder=4)
    ax.set_xticks([0.1, 0.3, 0.6, 0.7])
    red_x(ax, 0.7, "avg $=0.7$ (outside)\nrecheck before bubbling")

    return save(fig, "ch15_sanity_corridors")


REGISTRY = [
    fig_two_pass_timeline,
    fig_recognition_tree,
    fig_shortcut_catalog,
    fig_sanity_corridors,
]


def main() -> None:
    print(f"Generating Chapter 15 (Champion) figures -> {OUT} at "
          f"{PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
