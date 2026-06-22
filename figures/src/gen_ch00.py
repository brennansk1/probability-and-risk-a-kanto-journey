#!/usr/bin/env python3
"""Generate every Chapter 0 (Orientation / Pallet Town / Professor Oak) figure.

Manifest (MASTER_PLAN_V3 §16/§18, DESIGN_BLUEPRINT ch00 row) — two diagrams into
assets/diagrams/:
  ch00_journey_map     the Kanto route Pallet Town -> Indigo Plateau drawn as the
                       SYLLABUS PROGRESS BAR (eight badges = the syllabus, the Plateau
                       = the exam). Composites the REAL Pikachu front sprite (#25) as the
                       trainer marker at the start (iron rule: in the margin, never over a
                       label). The 32x32 town-map tile is too small to read, so the route is
                       drawn as a clean schematic strip; the real sprite supplies the Kanto art.
  ch00_calc_keypad     a labeled TI-30XS MultiView keypad SCHEMATIC (a math/diagram figure,
                       NO Pokemon sprite) spotlighting the Exam-P keys the book drives:
                       [2nd], [prb], [data], [stat], [STO>], [F<>D], [e^x]. (§18 spotlight set.)

PRINT TARGET: bound book -> every PNG at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is ALSO
distinguished by a hatch / text label so figures survive grayscale (color never the sole channel).
Sprites obey the IRON RULE: real Pokemon art in margins/corners only, never over a label,
number, or key a reader must read. The keypad figure carries NO sprite (it is a pure schematic).

Run: python3 figures/src/gen_ch00.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
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
NORMAL = chapter_accent(0)  # §17 Normal accent (#A8A878) — Pallet Town / ch00 banner parity.
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
# 1. ch00_journey_map — the eight-badge road from Pallet Town to the Indigo
#    Plateau, drawn as the syllabus progress bar. Each gym stop is a badge =
#    a slice of the syllabus; the Plateau at the end is Exam P. The REAL
#    Pikachu sprite stands at the start (iron rule: margin, clear of labels).
# --------------------------------------------------------------------------
def fig_journey_map():
    # Stops along the math-sequenced road (NOT canon badge order — §3/§15):
    #   the eight gym leaders, in the order the book meets them, then the Plateau.
    stops = [
        ("Pallet\nTown", "you are\nhere", NORMAL),
        ("Cerulean\nMisty", "Cascade\nch02", KANTO_BLUE),
        ("S.S. Anne\nLt. Surge", "Thunder\nch03", KANTO_YEL),
        ("Pewter\nBrock", "Boulder\nch04", "#B8A038"),
        ("Celadon\nErika", "Rainbow\nch05", "#705898"),
        ("Fuchsia\nKoga", "Soul\nch06", "#A040A0"),
        ("Saffron\nSabrina", "Marsh\nch09", "#F85888"),
        ("Cinnabar\nBlaine", "Volcano\nch14", "#F08030"),
        ("Viridian\nGiovanni", "Earth\nch16", "#E0C068"),
        ("Indigo\nPlateau", "EXAM P\nch19", KANTO_RED),
    ]
    n = len(stops)
    fig, ax = plt.subplots(figsize=(13.5, 5.4))
    _blank(ax)
    ax.set_xlim(-0.6, n - 0.4)
    ax.set_ylim(0, 4)
    ax.set_title("The journey IS the syllabus: Pallet Town to the Indigo Plateau\n"
                 "eight badges = eight chunks of Exam P; the Plateau = the exam itself "
                 "(stops ordered to the math, not to canon)",
                 fontsize=13, fontweight="bold")

    y = 2.0
    # The road: a thick progress-bar spine.
    ax.plot([0, n - 1], [y, y], color=KANTO_GRAY, lw=10, solid_capstyle="round",
            zorder=1, alpha=0.45)
    # Only the very first leg is "travelled" (you start at Pallet) — the rest greyed.
    ax.plot([0, 0.5], [y, y], color=NORMAL, lw=10, solid_capstyle="round", zorder=2)

    for i, (place, badge, col) in enumerate(stops):
        is_start = (i == 0)
        is_exam = (i == n - 1)
        # node
        r = 0.30 if not is_exam else 0.36
        ax.add_patch(Circle((i, y), r, fc=col, ec=INK, lw=1.6,
                            alpha=0.95 if (is_start or is_exam) else 0.85, zorder=4))
        if is_exam:
            ax.text(i, y, "P", ha="center", va="center", fontsize=14,
                    fontweight="bold", color="white", zorder=5)
        # place label above, badge/chapter tag below (alternate to avoid crowding)
        ax.text(i, y + 0.55, place, ha="center", va="bottom", fontsize=9,
                color=INK, fontweight="bold", zorder=5)
        tag_col = KANTO_RED if is_exam else (KANTO_GREEN if is_start else INK)
        ax.text(i, y - 0.55, badge, ha="center", va="top", fontsize=8.2,
                color=tag_col, zorder=5,
                fontweight="bold" if (is_start or is_exam) else "normal")

    # Real Pikachu marker at the start, in the margin ABOVE the road — iron rule:
    # clear of every label and node.
    place_sprite(ax, front(25), (0.0, 3.4), zoom=0.5, zorder=6)
    ax.text(0.0, 3.86, "your partner", ha="center", va="bottom", fontsize=8,
            color=INK, style="italic")

    # Legend strip.
    ax.text(n / 2 - 0.5, 0.55,
            "Earn a badge by clearing a chapter's Gym Challenge; your Trainer Rank "
            "climbs as the badges add up.\nReach the Plateau Champion-ready and Exam P "
            "is just the final battle.",
            ha="center", va="center", fontsize=9.5, color=INK,
            bbox=dict(boxstyle="round,pad=0.4", fc="#FFF6D6", ec=KANTO_YEL, lw=1.5))

    fig.tight_layout()
    return save(fig, "ch00_journey_map")


# --------------------------------------------------------------------------
# 2. ch00_calc_keypad — a labeled TI-30XS MultiView keypad SCHEMATIC. A math
#    diagram: NO Pokemon sprite. Spotlights the Exam-P keys the book drives
#    (§18): [2nd], [prb], [data], [stat], [STO>], [F<>D], [e^x].
# --------------------------------------------------------------------------
def fig_calc_keypad():
    fig, ax = plt.subplots(figsize=(11.0, 8.4))
    _blank(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12.2)
    ax.set_title("Your standard-issue gear: the TI-30XS MultiView\n"
                 "the seven keys (spotlighted) that win Exam P",
                 fontsize=14, fontweight="bold")

    # ---- calculator body ----
    ax.add_patch(FancyBboxPatch((0.6, 0.5), 8.8, 11.0,
                                boxstyle="round,pad=0.05,rounding_size=0.35",
                                fc="#22252b", ec=INK, lw=2.2, zorder=1))
    # ---- display ----
    ax.add_patch(FancyBboxPatch((1.2, 9.2), 7.6, 1.9,
                                boxstyle="round,pad=0.05,rounding_size=0.12",
                                fc="#9fb89a", ec="#3a4a36", lw=2.0, zorder=2))
    ax.text(1.5, 10.55, "MathPrint  TI-30XS", fontsize=9, family="monospace",
            color="#2a3a26", va="center")
    ax.text(1.5, 9.95, r"E[X] = $\bar{x}$", fontsize=13, family="monospace",
            color="#1c2a19", va="center", fontweight="bold")
    ax.text(5.2, 9.95, r"2.15", fontsize=13, family="monospace",
            color="#1c2a19", va="center", fontweight="bold")
    ax.text(1.5, 9.45, "the screen shows what you type, two lines",
            fontsize=7.6, family="monospace", color="#3a4a36", va="center", style="italic")

    # ---- key grid ----
    # rows counted from the TOP of the key area downward.
    SPOT = NORMAL  # spotlight fill (normal-type accent for ch00)
    DARK = "#3a3f47"

    # layout grid geometry
    x0, y0 = 1.2, 8.4      # top-left of first key
    kw, kh = 1.32, 0.78    # key width/height
    gx, gy = 0.20, 0.30    # gaps

    def key(c, r, label, badge=None, small=False):
        """Draw a key. `badge=(n, color)` marks a spotlighted key: colored border +
        a small numbered chip in its corner, keyed to the matching legend row below."""
        x = x0 + c * (kw + gx)
        y = y0 - r * (kh + gy)
        spotlight = badge is not None
        fc = SPOT if spotlight else DARK
        tc = INK if spotlight else "#e8e8ea"
        ec = badge[1] if spotlight else "#15171b"
        ax.add_patch(FancyBboxPatch((x, y), kw, kh,
                                    boxstyle="round,pad=0.02,rounding_size=0.10",
                                    fc=fc, ec=ec, lw=2.6 if spotlight else 1.3,
                                    zorder=3 + (1 if spotlight else 0)))
        ax.text(x + kw / 2, y + kh / 2, label, ha="center", va="center",
                fontsize=8.0 if small else 9.2,
                color=tc, fontweight="bold", zorder=5)
        if spotlight:
            n, col = badge
            bx, by = x + kw - 0.16, y + kh - 0.16      # top-right corner chip
            ax.add_patch(Circle((bx, by), 0.20, fc=col, ec="white", lw=1.4, zorder=7))
            ax.text(bx, by, str(n), ha="center", va="center",
                    fontsize=8.5, color="white", fontweight="bold", zorder=8)

    # spotlight set, numbered in reading order (matches the legend below)
    BLUE, GREEN, RED, CYAN, ORANGE, GOLD, PURPLE = (
        KANTO_BLUE, KANTO_GREEN, KANTO_RED, "#00BCD4", "#FF7043", "#B8860B", "#7B61FF")

    # Row 0 — 2nd(1), mode, delete, clear, on
    key(0, 0, "2nd", badge=(1, BLUE))
    key(1, 0, "mode"); key(2, 0, "delete"); key(3, 0, "clear"); key(4, 0, "on")
    # Row 1 — prb(2), data(3), x^2, ^, STO>(4)
    key(0, 1, "prb", badge=(2, GREEN))
    key(1, 1, "data", badge=(3, RED))
    key(2, 1, "x²"); key(3, 1, "^")
    key(4, 1, "STO▸", badge=(4, CYAN))
    # Row 2 — F<>D(5), ln, e^x via 2nd-ln(6), (, )
    key(0, 2, "F◂▸D", badge=(5, ORANGE), small=True)
    key(1, 2, "ln")
    key(2, 2, "[2nd] ln\n= eˣ", badge=(6, GOLD), small=True)
    key(3, 2, "("); key(4, 2, ")")
    # Row 3 — stat via 2nd(7), (-), /, x, -
    key(0, 3, "[2nd]\n= stat", badge=(7, PURPLE), small=True)
    key(1, 3, "(-)"); key(2, 3, "÷"); key(3, 3, "×"); key(4, 3, "−")
    # Row 4 — number pad sample + enter
    key(0, 4, "7"); key(1, 4, "8"); key(2, 4, "9")
    key(3, 4, "."); key(4, 4, "enter")

    # ---- numbered legend down the right margin (no connector lines: the corner
    #      chip on each key carries the number, so nothing crosses the keypad) ----
    notes = [
        (1, BLUE,   "[2nd] — the gateway key: turns a key into its small label above it"),
        (2, GREEN,  "[prb] — nCr / nPr / !  (binomial coefficients, ch04)"),
        (3, RED,    "[data] — the list editor: type the pmf into L1, L2 (ch03)"),
        (4, CYAN,   "[STO▸] — store, don't retype: kill rounding drift (7 memories)"),
        (5, ORANGE, "[F◂▸D] — toggle a fraction ↔ its decimal"),
        (6, GOLD,   "[2nd][ln] = eˣ — Poisson / exponential in one keystroke (ch05+)"),
        (7, PURPLE, "[2nd][stat] — 1-Var Stats: read x̄ = E[X], σx (Var = σx²)"),
    ]
    ax.set_xlim(0, 16.6)
    lx, ly, dy = 10.0, 8.55, 1.0
    for (n, col, text) in notes:
        ax.add_patch(Circle((lx, ly), 0.21, fc=col, ec="white", lw=1.4, zorder=4))
        ax.text(lx, ly, str(n), ha="center", va="center", fontsize=8.5,
                color="white", fontweight="bold", zorder=5)
        ax.text(lx + 0.42, ly, text, ha="left", va="center", fontsize=9.6,
                color=INK, zorder=4)
        ly -= dy

    ax.text(13.3, 0.85,
            "Setup once, then clear before every problem:\n"
            "[mode] set the display · store with [STO▸] · wipe scratch memory with\n"
            "[2nd][clear var]. Your two calculators leave for the exam memory-cleared.",
            ha="center", va="center", fontsize=9.0, color=INK,
            bbox=dict(boxstyle="round,pad=0.45", fc="#FFF6D6", ec=KANTO_YEL, lw=1.5))

    fig.tight_layout()
    return save(fig, "ch00_calc_keypad")


REGISTRY = [
    fig_journey_map,
    fig_calc_keypad,
]


def main() -> None:
    print(f"Generating Chapter 0 (Orientation) figures -> {OUT} at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
