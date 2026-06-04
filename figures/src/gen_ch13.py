#!/usr/bin/env python3
"""Generate the Chapter 13 (Covariance / variance-of-a-sum) math figure.

Beat 8 of the variance-of-a-linear-combination arc ends on a "Picture it"
figure whose <figure> alt text and caption promise a 3x3 grid that makes the
factor of 2 in

    Var(sum a_i X_i) = sum_i a_i^2 Var(X_i) + 2 sum_{i<j} a_i a_j Cov(X_i,X_j)

visible. The chapter referenced assets/diagrams/ch13_variance_grid.png, which
did not exist. This script renders exactly that filename:

  ch13_variance_grid   A 3x3 grid, rows and columns both labeled a1 X1,
                       a2 X2, a3 X3. The 3 diagonal cells (one color) hold
                       a_i^2 Var(X_i); the 6 off-diagonal cells (a second
                       color) hold a_i a_j Cov(X_i, X_j). The grid is
                       symmetric across the main diagonal, so each of the
                       three distinct covariance products appears in two
                       mirror-image cells -> the factor of 2.

PRINT TARGET: bound book, so the PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; the two cell classes
differ in fill color AND in hatch, so diagonal vs off-diagonal stays legible
in grayscale. Mirror-image covariance pairs are tied together with a faint
swap arrow and matched ("x2") tags so the doubling reads at a glance.

Run: python figures/src/gen_ch13.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import Rectangle, FancyArrowPatch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(HERE))
from sprite_util import front, place_sprite  # noqa: E402

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe).
KANTO_RED, KANTO_BLUE, KANTO_YEL = "#EE1515", "#3B4CCA", "#FFD733"
INK = "#333333"

# Light tints for cell fills (still distinct in grayscale via hatch).
DIAG_FILL = "#FCE3A6"   # warm yellow tint  -> variance cells
OFF_FILL = "#C9D0F2"    # cool blue tint    -> covariance cells
DIAG_EDGE = "#C9971C"
OFF_EDGE = "#3B4CCA"

PRINT_DPI = 300

LABELS = [r"$a_1 X_1$", r"$a_2 X_2$", r"$a_3 X_3$"]
N = 3


def save(fig, name: str) -> Path:
    path = OUT / f"{name}.png"
    fig.savefig(path, dpi=PRINT_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [fig] {path.relative_to(ROOT)}")
    return path


def variance_grid() -> Path:
    fig, ax = plt.subplots(figsize=(7.6, 7.6))
    ax.set_aspect("equal")
    ax.axis("off")

    # Grid geometry: cell (col c, row r) with row 0 drawn at the TOP so the
    # main diagonal runs top-left -> bottom-right, matching how a matrix reads.
    cell = 1.0
    x0, y0 = 0.0, 0.0  # bottom-left of the 3x3 block

    def cell_xy(r, c):
        # Returns the bottom-left corner of cell at matrix row r, col c.
        return x0 + c * cell, y0 + (N - 1 - r) * cell

    # Distinct covariance pairs -> a label index so mirror cells match.
    pair_tag = {(0, 1): "A", (0, 2): "B", (1, 2): "C"}

    for r in range(N):
        for c in range(N):
            bx, by = cell_xy(r, c)
            cx, cy = bx + cell / 2, by + cell / 2
            if r == c:
                ax.add_patch(Rectangle((bx, by), cell, cell, facecolor=DIAG_FILL,
                                       edgecolor=DIAG_EDGE, linewidth=1.6,
                                       hatch="///", zorder=1))
                ax.text(cx, cy, rf"$a_{{{r+1}}}^{{2}}\,\mathrm{{Var}}(X_{{{r+1}}})$",
                        ha="center", va="center", fontsize=12, color=INK, zorder=3,
                        path_effects=[pe.withStroke(linewidth=2.6, foreground="white")])
            else:
                i, j = (r, c) if r < c else (c, r)
                ax.add_patch(Rectangle((bx, by), cell, cell, facecolor=OFF_FILL,
                                       edgecolor=OFF_EDGE, linewidth=1.6,
                                       hatch="..", zorder=1))
                # Split the covariance label over two lines so it fits inside
                # the cell with margin to spare (the old single-line label
                # overflowed the cell width and ran into its neighbours). A
                # small white halo behind each line keeps it legible over the
                # dotted hatch.
                halo = [pe.withStroke(linewidth=2.6, foreground="white")]
                ax.text(cx, cy + 0.20, rf"$a_{{{i+1}}}a_{{{j+1}}}\,\mathrm{{Cov}}$",
                        ha="center", va="center", fontsize=10.5, color=INK,
                        zorder=3, path_effects=halo)
                ax.text(cx, cy - 0.07,
                        rf"$(X_{{{i+1}}},X_{{{j+1}}})$",
                        ha="center", va="center", fontsize=10.5, color=INK,
                        zorder=3, path_effects=halo)
                # Matched tag marking the two mirror cells of the same pair.
                ax.text(cx, cy - 0.34, f"pair {pair_tag[(i, j)]}",
                        ha="center", va="center", fontsize=8.5, style="italic",
                        color=OFF_EDGE, zorder=3, path_effects=halo)

    # Row / column header labels.
    for c in range(N):
        bx, _ = cell_xy(0, c)
        ax.text(bx + cell / 2, y0 + N * cell + 0.18, LABELS[c],
                ha="center", va="bottom", fontsize=13.5, fontweight="bold",
                color=INK)
    for r in range(N):
        _, by = cell_xy(r, 0)
        ax.text(x0 - 0.18, by + cell / 2, LABELS[r],
                ha="right", va="center", fontsize=13.5, fontweight="bold",
                color=INK)

    # --- Sprite decoration (margins only; never over a cell) -------------
    # The chapter's running team is Pikachu (X1), Charizard (X2), Bulbasaur
    # (X3); drop a tiny sprite above each column header so the abstract X_i
    # ties back to the actual climbers. They sit in the top margin, well
    # clear of every label, number, and grid cell.
    team = [25, 6, 1]  # Pikachu, Charizard, Bulbasaur
    for c, dex in enumerate(team):
        bx, _ = cell_xy(0, c)
        place_sprite(ax, front(dex), (bx + cell / 2, y0 + N * cell + 0.78),
                     zoom=0.42, alpha=0.95, zorder=4)

    # Faint diagonal line emphasizing the symmetry axis.
    ax.plot([x0, x0 + N * cell], [y0 + N * cell, y0], color=INK,
            lw=1.0, ls=(0, (4, 4)), alpha=0.5, zorder=2)

    # Swap arrows linking each mirror-image covariance pair across the diagonal.
    for (i, j) in pair_tag:
        bxi, byi = cell_xy(i, j)   # upper cell (row i, col j)
        bxj, byj = cell_xy(j, i)   # mirror cell (row j, col i)
        p1 = (bxi + cell / 2, byi + cell / 2)
        p2 = (bxj + cell / 2, byj + cell / 2)
        ax.add_patch(FancyArrowPatch(
            p1, p2, connectionstyle="arc3,rad=0.28",
            arrowstyle="<|-|>", mutation_scale=11,
            color=OFF_EDGE, lw=1.1, alpha=0.40, zorder=2))

    # Legend (two rows so the two entries never overlap).
    leg_y2 = y0 - 0.55   # upper legend row: diagonal
    leg_y1 = y0 - 1.05   # lower legend row: off-diagonal
    ax.add_patch(Rectangle((x0, leg_y2), 0.32, 0.32, facecolor=DIAG_FILL,
                           edgecolor=DIAG_EDGE, hatch="///", linewidth=1.4))
    ax.text(x0 + 0.45, leg_y2 + 0.16,
            r"diagonal: $a_i^{2}\,\mathrm{Var}(X_i)$  (one per variable)",
            ha="left", va="center", fontsize=11, color=INK)
    ax.add_patch(Rectangle((x0, leg_y1), 0.32, 0.32,
                           facecolor=OFF_FILL, edgecolor=OFF_EDGE,
                           hatch="..", linewidth=1.4))
    ax.text(x0 + 0.45, leg_y1 + 0.16,
            r"off-diagonal: $a_i a_j\,\mathrm{Cov}(X_i,X_j)$  (one per pair, appears twice)",
            ha="left", va="center", fontsize=11, color=INK)

    ax.set_title("Sum every cell of the grid", fontsize=16, pad=26)
    ax.text(x0 + N * cell / 2, y0 + N * cell + 1.30,
            r"each off-diagonal covariance appears twice $\Rightarrow$ the factor of $2$",
            ha="center", va="bottom", fontsize=11.5, style="italic", color=OFF_EDGE)

    ax.set_xlim(x0 - 1.65, x0 + N * cell + 0.55)
    ax.set_ylim(leg_y1 - 0.25, y0 + N * cell + 1.75)
    fig.tight_layout()
    return save(fig, "ch13_variance_grid")


def correlation_scatter() -> Path:
    """Three scatterplots illustrating positive / zero / negative covariance.

    Concept 1, Beat 8 references assets/diagrams/ch11_correlation_scatter.png.
    That PNG existed but was generated ad-hoc (no reproducible function) AND
    was missing the dashed mean crosshairs / four-quadrant shading that BOTH
    the chapter's alt text and figcaption explicitly describe ("Dashed
    crosshairs mark each variable's mean, dividing the plane into four
    quadrants; dots in the upper-right and lower-left quadrants contribute
    positive deviation-products..."). This function regenerates the figure to
    match the prose: each panel now draws the mean crosshairs and faintly
    shades the two "positive-product" quadrants so the covariance reasoning is
    visible, not just asserted.
    """
    rng = np.random.default_rng(13)
    n = 220
    panels = [
        (KANTO_RED, r"$\rho \approx +0.9$  (move together)", 0.9, "pos"),
        (KANTO_BLUE, r"$\rho \approx 0$  (no linear link)", 0.0, "zero"),
        ("#3DA35D", r"$\rho \approx -0.9$  (move opposite)", -0.9, "neg"),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(12.0, 4.4))

    for ax, (color, title, rho, kind) in zip(axes, panels):
        # Correlated bivariate normal with the target rho, standardized.
        z1 = rng.standard_normal(n)
        z2 = rng.standard_normal(n)
        x = z1
        y = rho * z1 + np.sqrt(max(1 - rho ** 2, 0.0)) * z2
        mx, my = x.mean(), y.mean()

        # Faint shading of the two quadrants whose deviation-products are
        # POSITIVE (upper-right and lower-left), centred on the means. Drawn
        # behind the dots so it never obscures a single data point.
        lim = 3.4
        ax.axhspan(my, my + lim, xmin=0.5, xmax=1.0, color=color, alpha=0.06, zorder=0)
        ax.axvspan(mx - lim, mx, ymin=0.0, ymax=0.5, color=color, alpha=0.06, zorder=0)
        # (upper-right and lower-left blocks)
        ax.add_patch(Rectangle((mx, my), lim, lim, color=color, alpha=0.06,
                               zorder=0, lw=0))
        ax.add_patch(Rectangle((mx - lim, my - lim), lim, lim, color=color,
                               alpha=0.06, zorder=0, lw=0))

        ax.scatter(x, y, s=11, color=color, alpha=0.7, zorder=2,
                   edgecolors="none")

        # Dashed mean crosshairs.
        ax.axhline(my, color=INK, lw=1.1, ls=(0, (5, 4)), alpha=0.7, zorder=1)
        ax.axvline(mx, color=INK, lw=1.1, ls=(0, (5, 4)), alpha=0.7, zorder=1)

        ax.set_title(title, fontsize=13, pad=10, color=INK)
        ax.set_xlabel("Pokemon A performance", fontsize=10)
        if ax is axes[0]:
            ax.set_ylabel("Pokemon B performance", fontsize=10)
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(False)
        ax.text(mx + 0.12, lim - 0.25, r"$\mu_A$", fontsize=9, color=INK,
                ha="left", va="top", alpha=0.8)
        ax.text(-lim + 0.18, my + 0.12, r"$\mu_B$", fontsize=9, color=INK,
                ha="left", va="bottom", alpha=0.8)

    # --- Sprite decoration (panel corners only; never over the cloud) -----
    # Pikachu + Charizard "surge together" -> positive panel; a placid
    # Slowpoke (#79) for the no-link panel; Charizard + a wilting Bulbasaur
    # for the move-opposite panel, mirroring the chapter's Charizard/Bulbasaur
    # negative-correlation story. Placed in the empty top-left / bottom-right
    # corners with alpha<1 so no data point is hidden.
    place_sprite(axes[0], front(25), (0.13, 0.87), xycoords="axes fraction",
                 zoom=0.34, alpha=0.9)
    place_sprite(axes[1], front(79), (0.13, 0.87), xycoords="axes fraction",
                 zoom=0.34, alpha=0.85)
    place_sprite(axes[2], front(6), (0.14, 0.87), xycoords="axes fraction",
                 zoom=0.34, alpha=0.9)
    place_sprite(axes[2], front(1), (0.87, 0.15), xycoords="axes fraction",
                 zoom=0.34, alpha=0.9)

    fig.suptitle("Correlation: how two teammates' performances move together",
                 fontsize=15, fontweight="bold", y=1.02)
    fig.tight_layout()
    return save(fig, "ch11_correlation_scatter")


def main() -> None:
    print(f"Generating Chapter 13 (Covariance) figures -> {OUT} at {PRINT_DPI} DPI")
    variance_grid()
    correlation_scatter()
    print("Done.")


if __name__ == "__main__":
    main()
