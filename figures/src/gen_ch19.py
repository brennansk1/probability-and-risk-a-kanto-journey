#!/usr/bin/env python3
"""Generate every Chapter 19 (Champion's Challenge / Indigo Plateau / the exam /
Dragon type) figure.

Manifest (DESIGN_BLUEPRINT ch19 row · MASTER_PLAN_V3 §16, §24, §30) — two
diagrams into assets/diagrams/:
  ch19_pacing_strip      the 6-minutes-per-question exam timeline: the two-pass
                         strategy laid over a 180-minute bar (Pikachu #25 paces it)
  ch19_shortcut_catalog  the shortcut menu as a battle board — Ash's Charizard #6
                         (the shortcuts) facing Gary's Blastoise #9 (brute force)

PRINT TARGET: bound book, every PNG rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is
ALSO distinguished by a hatch pattern / text label so figures survive grayscale.
Real sprites obey the IRON RULE: art lives in margins / corners / beside labels,
never over a curve, equation, axis, or number a reader must read. Sprite art is
REAL (assets/sprites/front/*.png) and is only ever COMPOSITED, never generated.

Run: python3 figures/src/gen_ch19.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
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
DRAGON = chapter_accent(19)  # Championship dragon accent (#7038F8)
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


def _clean(ax):
    ax.set_facecolor("white")
    ax.grid(False)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)


# --------------------------------------------------------------------------
# 1. ch19_pacing_strip — the 6-min/question two-pass timeline. (Concept 1)
# --------------------------------------------------------------------------
def fig_pacing_strip():
    """A 180-minute exam clock with the two-pass strategy laid over 30 slots.

    Top band = Pass 1 (front-to-back): recognized 'gift' questions solved fast
    (short green blocks), stubborn 'monster' questions flagged with a quick
    provisional guess (short red blocks) -- banking time. Bottom band = Pass 2,
    returning only to the flagged slots with the banked time, then a final
    'bubble every blank' sliver guarantees no empty answer. The 6-min average
    line is the budget reference; Pikachu paces the clock from the margin.
    """
    fig, ax = plt.subplots(figsize=(12.5, 6.2))
    _clean(ax)

    T = 180.0          # total minutes
    n = 30             # questions
    budget = T / n     # = 6 min/question (the reference average)

    # ---- The full 180-minute clock bar (the resource) ----
    ax.add_patch(Rectangle((0, 3.05), T, 0.7, facecolor=DRAGON, alpha=0.10,
                           edgecolor=DRAGON, lw=1.6, zorder=1))
    ax.text(T / 2, 3.92, "THE CLOCK — 180 minutes, 30 questions, "
            r"$\dfrac{180}{30}=6$ min/question",
            ha="center", va="bottom", fontsize=12.5, color=INK, fontweight="bold")
    # minute ticks every 30 min
    for m in range(0, int(T) + 1, 30):
        ax.plot([m, m], [3.02, 3.08], color=KANTO_GRAY, lw=1.0, zorder=2)
        ax.text(m, 2.94, f"{m}", ha="center", va="top", fontsize=8.5,
                color=KANTO_GRAY)

    # A realistic mix of per-question times that still sums to <= 180: some gifts
    # (2 min, solved), some monsters (flagged at ~4 then revisited), the rest ~6.
    # gift=solved-now (green); monster=flagged-now / solved-on-pass-2 (red);
    # medium=solved-now at the budget (blue).
    # 10 gifts @2, 10 medium @6, 10 monsters: 2 (flag) on pass1 + ~5 on pass2.
    # Pass-1 spend: 10*2 + 10*6 + 10*2 = 100 min. Pass-2 spend: 10*~5 = 50 min.
    # Total 150 min -> 30 min banked buffer + the final bubble sweep.

    # ---- Pass 1 band (top): front-to-back triage ----
    y1 = 2.05
    x = 0.0
    # interleave a believable order: gift, medium, monster, repeating
    order = (["gift", "medium", "monster"] * 10)[:30]
    pass1_dur = {"gift": 2.0, "medium": 6.0, "monster": 2.0}
    colors = {"gift": KANTO_GREEN, "medium": KANTO_BLUE, "monster": KANTO_RED}
    hatch = {"gift": "..", "medium": "", "monster": "xx"}
    flagged = []  # x-centers of flagged monsters (for the pass-2 callbacks)
    for kind in order:
        d = pass1_dur[kind]
        ax.add_patch(Rectangle((x, y1), d, 0.62, facecolor=colors[kind],
                               alpha=0.55 if kind != "medium" else 0.42,
                               edgecolor=colors[kind], lw=1.0,
                               hatch=hatch[kind], zorder=3))
        if kind == "monster":
            # a flag marker on the provisional guess
            ax.plot([x + d / 2], [y1 + 0.78], marker="v", ms=7,
                    color=KANTO_RED, zorder=5)
            flagged.append(x + d / 2)
        x += d
    pass1_end = x
    ax.text(-3, y1 + 0.31, "PASS 1", ha="right", va="center", fontsize=11,
            color=INK, fontweight="bold")
    ax.text(pass1_end / 2, y1 - 0.18,
            "front-to-back: solve every recognized gift; flag + provisional-guess "
            "any monster not yielding by ~4 min",
            ha="center", va="top", fontsize=9.5, color=INK)

    # ---- Pass 2 band (middle): return to the flags with banked time ----
    y2 = 0.95
    xp = pass1_end
    for fx in flagged:
        d = 5.0
        ax.add_patch(Rectangle((xp, y2), d, 0.62, facecolor=KANTO_RED,
                               alpha=0.30, edgecolor=KANTO_RED, lw=1.2,
                               hatch="xx", zorder=3))
        # a thin connector from the flag (pass 1) to its revisit (pass 2)
        ax.add_patch(FancyArrowPatch((fx, y1 - 0.02), (xp + d / 2, y2 + 0.64),
                                     arrowstyle="-|>", mutation_scale=9,
                                     color=KANTO_RED, lw=0.8, alpha=0.45,
                                     connectionstyle="arc3,rad=-0.15", zorder=2))
        xp += d
    pass2_end = xp
    ax.text(-3, y2 + 0.31, "PASS 2", ha="right", va="center", fontsize=11,
            color=INK, fontweight="bold")
    ax.text((pass1_end + pass2_end) / 2, y2 - 0.18,
            "return to the flagged monsters with the time banked from the gifts",
            ha="center", va="top", fontsize=9.5, color=INK)

    # ---- Final sweep: bubble every blank (a guess beats a blank) ----
    sweep_lo, sweep_hi = pass2_end, T
    ax.add_patch(Rectangle((sweep_lo, y2), sweep_hi - sweep_lo, 0.62,
                           facecolor=KANTO_YEL, alpha=0.55, edgecolor=KANTO_YEL,
                           lw=1.2, hatch="//", zorder=3))
    ax.text((sweep_lo + sweep_hi) / 2, y2 + 0.31, "bubble\nevery blank",
            ha="center", va="center", fontsize=8.0, color=INK, zorder=6)

    # ---- The 6-min budget reference line across the question slots ----
    ax.text(2, y1 + 1.45,
            r"each block = one question (worth exactly 1 point); gifts bank time, "
            r"monsters spend it — never leave a blank ($\sim$20% beats 0%)",
            ha="left", va="center", fontsize=9.5, color=DRAGON, style="italic")

    # legend
    handles = [
        Rectangle((0, 0), 1, 1, facecolor=KANTO_GREEN, alpha=0.55, hatch="..",
                  edgecolor=KANTO_GREEN, label="gift solved (~2 min) -> banks time"),
        Rectangle((0, 0), 1, 1, facecolor=KANTO_BLUE, alpha=0.42,
                  edgecolor=KANTO_BLUE, label="medium solved at budget (~6 min)"),
        Rectangle((0, 0), 1, 1, facecolor=KANTO_RED, alpha=0.45, hatch="xx",
                  edgecolor=KANTO_RED, label="monster: flag + guess, revisit on pass 2"),
        Rectangle((0, 0), 1, 1, facecolor=KANTO_YEL, alpha=0.55, hatch="//",
                  edgecolor=KANTO_YEL, label="final sweep: bubble every blank"),
    ]
    ax.legend(handles=handles, loc="lower center", ncol=2, fontsize=9,
              frameon=True, bbox_to_anchor=(0.5, -0.02))

    ax.set_title("The two-pass clock — spend the budget where it earns points",
                 fontsize=13.5, pad=14)
    ax.set_xlim(-14, T + 4)
    ax.set_ylim(0.2, 4.4)
    ax.set_xticks([])
    ax.set_yticks([])

    # Real Pikachu sprite paces the clock from the top-left margin (clear of bars).
    place_sprite(ax, front(25), (-9, 3.55), zoom=0.42, alpha=0.97, zorder=7)
    ax.text(-9, 3.05, "#25 Pikachu", ha="center", fontsize=8, color=INK)
    fig.tight_layout()
    return save(fig, "ch19_pacing_strip")


# --------------------------------------------------------------------------
# 2. ch19_shortcut_catalog — the shortcut menu as a battle board. (Concept 3)
# --------------------------------------------------------------------------
def fig_shortcut_catalog():
    """The seven exam shortcuts as a reference board, framed as the final battle:
    Ash's Charizard (the fast shortcut path) vs Gary's Blastoise (brute force).

    Each tile = a trigger 'tell' (top) -> the identity that collapses the work
    (bottom). The two real sprites sit in the outer margins (corners), never over
    a tile's math. This is where the Concept-2 recognition map lands.
    """
    fig, ax = plt.subplots(figsize=(12.5, 8.2))
    _clean(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.set_xticks([])
    ax.set_yticks([])

    ax.text(6, 8.62, "THE SHORTCUT CATALOG", ha="center", va="center",
            fontsize=15.5, color=INK, fontweight="bold")
    ax.text(6, 8.18, "read the tell (top) -> deploy the identity (bottom); "
            "the move that turns a 6-minute problem into a 90-second one",
            ha="center", va="center", fontsize=10, color=DRAGON, style="italic")

    # Seven shortcut tiles laid out in a 2-wide x 4-tall grid (last cell = the
    # 'before you brute-force, ask' banner). Each tile: tell (top), identity
    # (bottom, in a math-friendly mono-ish style via mathtext).
    tiles = [
        (r"poly $\times\,e^{-x/\theta}$ integral",
         r"gamma: $\int_0^\infty x^{\alpha-1}e^{-x/\theta}dx=\Gamma(\alpha)\theta^{\alpha}$",
         KANTO_RED),
        (r"$E[X]$, $X\geq 0$, survival given",
         r"Darth Vader: $E[X]=\int_0^\infty S(x)\,dx$",
         KANTO_BLUE),
        (r"exponential + 'already waited' / deductible",
         r"memoryless: $E[X-d\,|\,X>d]=\theta$, $E[(X-d)_+]=\theta e^{-d/\theta}$",
         KANTO_GREEN),
        (r"count over an interval",
         r"Poisson: $\mu=\sigma^2=\lambda$",
         "#FF7043"),
        (r"rare event, many trials",
         r"binomial $\to$ Poisson: $\mathrm{Bin}(n,p)\approx\mathrm{Pois}(np)$",
         "#7B61FF"),
        (r"$M_X(t)$ handed to you",
         r"MGF: $M_X'(0)=E[X]$, $M_X''(0)=E[X^2]$",
         "#00BCD4"),
        (r"discrete sum, normal approx",
         r"continuity: $P(X\leq k)\approx\Phi(\frac{k+0.5-\mu}{\sigma})$",
         "#B8A038"),
    ]

    # grid geometry: 2 columns, rows from top to bottom
    col_x = [1.55, 6.55]
    tile_w, tile_h = 4.0, 1.62
    row_y = [6.15, 4.25, 2.35, 0.45]   # 4 rows (last row right cell = banner)
    positions = [
        (col_x[0], row_y[0]), (col_x[1], row_y[0]),
        (col_x[0], row_y[1]), (col_x[1], row_y[1]),
        (col_x[0], row_y[2]), (col_x[1], row_y[2]),
        (col_x[0], row_y[3]),
    ]
    for (tx, ty), (tell, ident, c) in zip(positions, tiles):
        ax.add_patch(Rectangle((tx, ty), tile_w, tile_h, facecolor=c, alpha=0.10,
                               edgecolor=c, lw=1.8, zorder=2))
        # tell strip
        ax.add_patch(Rectangle((tx, ty + tile_h - 0.46), tile_w, 0.46,
                               facecolor=c, alpha=0.22, edgecolor="none",
                               zorder=3))
        ax.text(tx + tile_w / 2, ty + tile_h - 0.23, tell, ha="center",
                va="center", fontsize=9.2, color=INK, fontweight="bold",
                zorder=4)
        ax.text(tx + tile_w / 2, ty + (tile_h - 0.46) / 2, ident, ha="center",
                va="center", fontsize=10.0, color=INK, zorder=4)

    # The 8th cell (bottom-right): the trigger banner.
    bx, by = col_x[1], row_y[3]
    ax.add_patch(Rectangle((bx, by), tile_w, tile_h, facecolor=DRAGON,
                           alpha=0.12, edgecolor=DRAGON, lw=1.8, zorder=2))
    ax.text(bx + tile_w / 2, by + tile_h / 2,
            "Before you integrate by parts, ask:\n"
            "gamma kernel?  survival integral?\n"
            "memoryless exponential?\n"
            "One of the three usually collapses it.",
            ha="center", va="center", fontsize=9.4, color=INK, zorder=4)

    # Battle framing: Ash's Charizard (shortcuts) lower-left corner; Gary's
    # Blastoise (brute force) upper-right corner -- both in clear margins.
    place_sprite(ax, front(6), (0.62, 0.95), zoom=0.46, alpha=0.97, zorder=6)
    ax.text(0.62, 0.30, "#6 Charizard\n(your shortcuts)", ha="center",
            fontsize=7.6, color=INK)
    place_sprite(ax, front(9), (11.4, 7.7), zoom=0.46, alpha=0.97, zorder=6)
    ax.text(11.4, 7.05, "#9 Blastoise\n(Gary's brute force)", ha="center",
            fontsize=7.6, color=INK)

    fig.tight_layout()
    return save(fig, "ch19_shortcut_catalog")


REGISTRY = [
    fig_pacing_strip,
    fig_shortcut_catalog,
]


def main() -> None:
    print(f"Generating Chapter 19 (Champion's Challenge) figures -> "
          f"{OUT} at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
