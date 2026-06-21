#!/usr/bin/env python3
"""Generate every programmatic figure for the textbook (matplotlib, Kanto theme).

PRINT TARGET: the book is printed and bound, so all raster output is >=300 DPI.
Figures are written to assets/diagrams/ (so embed_visuals.diagram()/dist_card()
can reference them). No copyrighted sprites are drawn here — only original plots,
diagrams, and distribution "trading cards".

This file is a scaffold: it sets up the theme, palette, output dir, and DPI, and
registers the figures each chapter needs. The workflow's figure stage fills in the
plotting bodies. Run: python figures/src/generate_figures.py
"""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")

# Kanto color cycle (set here, not in the .mplstyle: matplotlib's style parser
# treats '#' in hex literals as a comment and rejects the prop_cycle line).
from cycler import cycler  # noqa: E402
plt.rcParams["axes.prop_cycle"] = cycler(color=[
    KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN,
    "#FF7043", "#7B61FF", "#00BCD4", "#FF4081", "#8D6E63", "#78909C", "#E040FB", "#FFAB40",
])

PRINT_DPI = 300  # bound book: keep all figures crisp at trim size


def save(fig, name: str) -> None:
    path = OUT / f"{name}.png"
    fig.savefig(path, dpi=PRINT_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [fig] {path.relative_to(ROOT)}")


# --------------------------------------------------------------------------
# Figure registry — one entry per required figure (DESIGN.md 4.3).
# The workflow fills each body; calling main() renders whatever is implemented.
# --------------------------------------------------------------------------
def fig_kanto_progress_strip():  # chapter-head progress map
    ...

def fig_ch02_venn():             # General Probability: 2/3-event Venn
    ...

def fig_ch03_me_vs_independent():  # ch03: two-panel ME-vs-independent contrast
    import matplotlib.patches as mpatches
    from sprite_util import front, place_sprite
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(11, 5.2))

    def frame(ax, title):
        ax.add_patch(mpatches.Rectangle((0, 0), 10, 8, fill=False,
                     edgecolor="#333333", linewidth=1.4))
        ax.text(0.35, 7.45, "$S$", fontsize=15, color="#333333")
        ax.set_title(title, fontsize=14, pad=12)
        ax.set_xlim(-0.4, 10.4); ax.set_ylim(-0.4, 8.4)
        ax.set_aspect("equal"); ax.axis("off"); ax.grid(False)

    # LEFT: mutually exclusive — two non-touching circles.
    frame(axL, "Mutually exclusive")
    axL.add_patch(mpatches.Circle((3.0, 4.0), 1.7, facecolor=KANTO_BLUE,
                  alpha=0.45, edgecolor="#333333", linewidth=1.2))
    axL.add_patch(mpatches.Circle((7.0, 4.0), 1.7, facecolor=KANTO_RED,
                  alpha=0.45, edgecolor="#333333", linewidth=1.2))
    axL.text(3.0, 4.0, "$A$", ha="center", va="center", fontsize=15)
    axL.text(7.0, 4.0, "$B$", ha="center", va="center", fontsize=15)
    axL.text(5.0, 1.35, r"$P(A\cap B)=0$", ha="center", fontsize=13)
    axL.text(5.0, 0.55, "no overlap  $\\Rightarrow$  may ADD",
             ha="center", fontsize=11, color="#444444")

    # RIGHT: independent — two overlapping circles, overlap = P(A)P(B).
    frame(axR, "Independent")
    axR.add_patch(mpatches.Circle((4.3, 4.0), 1.9, facecolor=KANTO_BLUE,
                  alpha=0.40, edgecolor="#333333", linewidth=1.2))
    axR.add_patch(mpatches.Circle((6.0, 4.0), 1.9, facecolor=KANTO_RED,
                  alpha=0.40, edgecolor="#333333", linewidth=1.2))
    axR.text(3.4, 4.0, "$A$", ha="center", va="center", fontsize=15)
    axR.text(6.9, 4.0, "$B$", ha="center", va="center", fontsize=15)
    # "overlap" label: point at the lens edge, not driving across the math.
    axR.annotate("overlap", xy=(5.15, 5.6), xytext=(5.15, 7.0),
                 ha="center", fontsize=10, color="#333333",
                 arrowprops=dict(arrowstyle="->", color="#333333"))
    axR.text(5.15, 1.35, r"$P(A\cap B)=P(A)\,P(B)$", ha="center", fontsize=13)
    axR.text(5.15, 0.55, "forced nonzero overlap  $\\Rightarrow$  may MULTIPLY",
             ha="center", fontsize=11, color="#444444")

    # Sprites: Pikachu's two snare traps from Concept 5 / Team Rocket's Trap.
    # Tucked in upper corners of each S box — never over a circle or equation.
    place_sprite(axL, front(25), (9.1, 7.0), zoom=0.42, alpha=0.95)  # Pikachu
    place_sprite(axR, front(25), (9.1, 7.0), zoom=0.42, alpha=0.95)

    fig.suptitle("Mutually exclusive vs. independent — opposite situations, never the same",
                 fontsize=13, y=1.0)
    fig.tight_layout()
    save(fig, "ch03_me_vs_independent")
    return True

def fig_ch03_sample_space():     # ch03: the world S as a box of outcome chips
    import matplotlib.patches as mpatches
    from sprite_util import front, place_sprite
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.add_patch(mpatches.FancyBboxPatch((0.3, 0.3), 9.4, 5.4,
                 boxstyle="round,pad=0.02,rounding_size=0.25",
                 fill=False, edgecolor="#333333", linewidth=1.6))
    ax.text(0.65, 5.05, "$S$ — the sample space (every outcome, nothing missing)",
            fontsize=12.5, color="#333333")

    # (label, color, dex sprite to perch atop the chip; None = the boring chip)
    chips = [("Pidgey", KANTO_BLUE, 16), ("Rattata", "#8D6E63", 19),
             ("Spearow", KANTO_RED, 21), ("nothing", KANTO_GRAY, None)]
    x = 0.85
    for label, color, dex in chips:
        w = 1.85
        ax.add_patch(mpatches.FancyBboxPatch((x, 1.6), w, 1.7,
                     boxstyle="round,pad=0.02,rounding_size=0.18",
                     facecolor=color, alpha=0.45,
                     edgecolor="#333333", linewidth=1.2))
        ax.text(x + w / 2, 2.25, label, ha="center", va="center", fontsize=12.5)
        # Perch a small species sprite above each chip (decorative; the label
        # below carries all the meaning, so the figure reads fine in grayscale).
        if dex is not None:
            place_sprite(ax, front(dex), (x + w / 2, 4.05), zoom=0.42, alpha=0.95)
        x += w + 0.30

    # spotlight the easy-to-forget "nothing" chip
    ax.annotate("don't drop the\nboring outcome",
                xy=(x - 0.30 - 1.85 / 2, 1.6), xytext=(x - 0.30 - 1.85 / 2, 0.55),
                ha="center", fontsize=10.5, color="#EE1515",
                arrowprops=dict(arrowstyle="->", color="#EE1515", linewidth=1.4))

    ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.set_aspect("auto"); ax.axis("off"); ax.grid(False)
    fig.tight_layout()
    save(fig, "ch03_sample_space")
    return True

def fig_ch03_venn_two():         # ch03 Concept 3: two-event Venn for De Morgan / "neither"
    """Two events in S: 'or', 'and', and the 'neither' region outside both,
    which De Morgan names (A∪B)^c = A^c ∩ B^c. Matches the Concept-3 caption."""
    import matplotlib.patches as mpatches
    from sprite_util import front, place_sprite
    fig, ax = plt.subplots(figsize=(8.4, 5.8))
    ax.add_patch(mpatches.Rectangle((0, 0), 12, 9, fill=False,
                 edgecolor="#333333", linewidth=1.6))
    ax.text(0.55, 8.15, "$S$", fontsize=17, color="#333333")

    # Two overlapping circles.
    ax.add_patch(mpatches.Circle((4.8, 4.5), 2.9, facecolor=KANTO_BLUE,
                 alpha=0.42, edgecolor="#333333", linewidth=1.3))
    ax.add_patch(mpatches.Circle((7.6, 4.5), 2.9, facecolor=KANTO_YEL,
                 alpha=0.55, edgecolor="#333333", linewidth=1.3))

    # Region labels.
    ax.text(3.5, 4.5, "$A$ only", ha="center", va="center", fontsize=13.5)
    ax.text(6.2, 4.5, r"$A\cap B$", ha="center", va="center", fontsize=13.5)
    ax.text(8.9, 4.5, "$B$ only", ha="center", va="center", fontsize=13.5)

    # The "neither" region — the whole point of this Concept-3 figure.
    ax.text(1.7, 1.05, r"$(A\cup B)^c = A^c\cap B^c$",
            ha="left", va="center", fontsize=13, color="#EE1515")
    ax.text(1.7, 0.45, "the “neither” region — outside both circles",
            ha="left", va="center", fontsize=10.5, color="#444444")
    ax.annotate("", xy=(0.9, 7.7), xytext=(2.1, 1.4),
                arrowprops=dict(arrowstyle="->", color="#EE1515", linewidth=1.3,
                                connectionstyle="arc3,rad=-0.2"))

    # Sprites: G = Pidgey (event A), W = Spearow (event B) per the Concept-3 text.
    # Perched near each circle's outer label, well clear of the math.
    place_sprite(ax, front(16), (2.9, 6.7), zoom=0.42, alpha=0.95)  # Pidgey -> A
    place_sprite(ax, front(21), (9.5, 6.7), zoom=0.42, alpha=0.95)  # Spearow -> B

    ax.set_xlim(0, 12); ax.set_ylim(0, 9)
    ax.set_aspect("equal"); ax.axis("off"); ax.grid(False)
    fig.tight_layout()
    save(fig, "ch03_venn_two")
    return True

def fig_ch03_venn_three():       # ch03 Concept 4: three-event Venn with +/- IE bookkeeping
    """Three-event diagram with all seven cells, annotated with the
    inclusion-exclusion sign each contributes: +singles, -pairs, +triple."""
    import matplotlib.patches as mpatches
    from sprite_util import front, place_sprite
    fig, ax = plt.subplots(figsize=(8.2, 8.2))
    ax.add_patch(mpatches.Rectangle((0, 0), 12, 12, fill=False,
                 edgecolor="#333333", linewidth=1.6))
    ax.text(0.55, 11.1, "$S$", fontsize=17, color="#333333")

    r = 3.0
    cA = (4.6, 7.4)   # A  (upper-left)
    cB = (7.4, 7.4)   # B  (upper-right)
    cC = (6.0, 5.1)   # C  (lower-center)
    ax.add_patch(mpatches.Circle(cA, r, facecolor=KANTO_RED,
                 alpha=0.34, edgecolor="#333333", linewidth=1.2))
    ax.add_patch(mpatches.Circle(cB, r, facecolor=KANTO_BLUE,
                 alpha=0.34, edgecolor="#333333", linewidth=1.2))
    ax.add_patch(mpatches.Circle(cC, r, facecolor=KANTO_GREEN,
                 alpha=0.34, edgecolor="#333333", linewidth=1.2))

    # Circle name labels (placed in the far lobes, clear of all cell labels).
    ax.text(2.9, 9.1, "$A$", ha="center", va="center", fontsize=15, color="#B71C1C")
    ax.text(9.1, 9.1, "$B$", ha="center", va="center", fontsize=15, color="#1A237E")
    ax.text(6.0, 2.5, "$C$", ha="center", va="center", fontsize=15, color="#1B5E20")

    grey = "#333333"
    # Seven cells, each tagged with the IE sign it carries.
    # +singles
    ax.text(3.5, 7.7, "$+A$\nonly", ha="center", va="center", fontsize=11, color=grey)
    ax.text(8.5, 7.7, "$+B$\nonly", ha="center", va="center", fontsize=11, color=grey)
    ax.text(6.0, 3.9, "$+C$\nonly", ha="center", va="center", fontsize=11, color=grey)
    # -pairs (pairwise-only lenses)
    ax.text(6.0, 8.45, r"$-(A\cap B)$", ha="center", va="center", fontsize=10.5, color="#C62828")
    ax.text(4.2, 5.65, r"$-(A\cap C)$", ha="center", va="center", fontsize=10.5, color="#C62828")
    ax.text(7.8, 5.65, r"$-(B\cap C)$", ha="center", va="center", fontsize=10.5, color="#C62828")
    # +triple (center)
    ax.text(6.0, 6.55, r"$+(A\cap B\cap C)$", ha="center", va="center",
            fontsize=10, color="#1B5E20")

    # The bookkeeping rule, spelled out below the diagram.
    ax.text(6.0, 0.75, "$+$singles $\\;-\\;$pairs $\\;+\\;$triple "
            "$\\;\\Rightarrow\\;$ every cell counted exactly once",
            ha="center", va="center", fontsize=11, color="#444444")

    # Sprites: the three surveyed species, in the outer lobes beside the names.
    place_sprite(ax, front(16), (2.9, 8.2), zoom=0.36, alpha=0.92)  # Pidgey -> A
    place_sprite(ax, front(19), (9.1, 8.2), zoom=0.36, alpha=0.92)  # Rattata -> B
    place_sprite(ax, front(21), (6.0, 1.6), zoom=0.36, alpha=0.92)  # Spearow -> C

    ax.set_xlim(0, 12); ax.set_ylim(0, 12)
    ax.set_aspect("equal"); ax.axis("off"); ax.grid(False)
    fig.tight_layout()
    save(fig, "ch03_venn_three")
    return True

def fig_ch04_bayes_grid():       # Bayes-table / tree
    ...

def card_distribution(name: str):  # distribution "trading card" (Ch 6-7, App B)
    ...

def fig_ch07_normal_tails():     # normal curve, shaded tails
    ...

def fig_ch08_payment_step():     # payment-vs-loss step graph (deductible/limit)
    ...

def fig_ch09_joint_region():     # joint-density region sketch
    ...

def fig_ch12_clt():              # CLT convergence stills
    ...


REGISTRY = [
    fig_kanto_progress_strip, fig_ch02_venn, fig_ch03_sample_space,
    fig_ch03_venn_two, fig_ch03_venn_three,
    fig_ch03_me_vs_independent, fig_ch04_bayes_grid,
    fig_ch07_normal_tails, fig_ch08_payment_step, fig_ch09_joint_region, fig_ch12_clt,
]


def main() -> None:
    print(f"Generating figures -> {OUT} at {PRINT_DPI} DPI")
    done = 0
    for fn in REGISTRY:
        try:
            result = fn()
        except NotImplementedError:
            result = None
        if result is not None:
            done += 1
    print(f"Done. {done}/{len(REGISTRY)} figures implemented "
          f"({len(REGISTRY)-done} are scaffold stubs for the workflow to fill).")


if __name__ == "__main__":
    main()
