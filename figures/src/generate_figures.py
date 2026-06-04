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
    axR.annotate("overlap", xy=(5.15, 4.0), xytext=(5.15, 6.9),
                 ha="center", fontsize=10, color="#333333",
                 arrowprops=dict(arrowstyle="->", color="#333333"))
    axR.text(5.15, 1.35, r"$P(A\cap B)=P(A)\,P(B)$", ha="center", fontsize=13)
    axR.text(5.15, 0.55, "forced nonzero overlap  $\\Rightarrow$  may MULTIPLY",
             ha="center", fontsize=11, color="#444444")

    fig.suptitle("Mutually exclusive vs. independent — opposite situations, never the same",
                 fontsize=13, y=1.0)
    fig.tight_layout()
    save(fig, "ch03_me_vs_independent")
    return True

def fig_ch03_sample_space():     # ch03: the world S as a box of outcome chips
    import matplotlib.patches as mpatches
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.add_patch(mpatches.FancyBboxPatch((0.3, 0.3), 9.4, 5.4,
                 boxstyle="round,pad=0.02,rounding_size=0.25",
                 fill=False, edgecolor="#333333", linewidth=1.6))
    ax.text(0.65, 5.05, "$S$ — the sample space (every outcome, nothing missing)",
            fontsize=12.5, color="#333333")

    chips = [("Pidgey", KANTO_BLUE), ("Rattata", "#8D6E63"),
             ("Spearow", KANTO_RED), ("nothing", KANTO_GRAY)]
    x = 0.85
    for label, color in chips:
        w = 1.85
        ax.add_patch(mpatches.FancyBboxPatch((x, 1.6), w, 1.7,
                     boxstyle="round,pad=0.02,rounding_size=0.18",
                     facecolor=color, alpha=0.45,
                     edgecolor="#333333", linewidth=1.2))
        ax.text(x + w / 2, 2.45, label, ha="center", va="center", fontsize=12.5)
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
