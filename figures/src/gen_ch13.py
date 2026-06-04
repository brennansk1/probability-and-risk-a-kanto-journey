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

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

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
                        ha="center", va="center", fontsize=13, color=INK, zorder=3)
            else:
                i, j = (r, c) if r < c else (c, r)
                ax.add_patch(Rectangle((bx, by), cell, cell, facecolor=OFF_FILL,
                                       edgecolor=OFF_EDGE, linewidth=1.6,
                                       hatch="..", zorder=1))
                ax.text(cx, cy + 0.10,
                        rf"$a_{{{i+1}}}a_{{{j+1}}}\,\mathrm{{Cov}}(X_{{{i+1}}},X_{{{j+1}}})$",
                        ha="center", va="center", fontsize=11.5, color=INK, zorder=3)
                # Matched tag marking the two mirror cells of the same pair.
                ax.text(cx, cy - 0.27, f"pair {pair_tag[(i, j)]}",
                        ha="center", va="center", fontsize=9.5, style="italic",
                        color=OFF_EDGE, zorder=3)

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
            arrowstyle="<|-|>", mutation_scale=12,
            color=OFF_EDGE, lw=1.3, alpha=0.55, zorder=2))

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
    ax.text(x0 + N * cell / 2, y0 + N * cell + 0.62,
            r"each off-diagonal covariance appears twice $\Rightarrow$ the factor of $2$",
            ha="center", va="bottom", fontsize=11.5, style="italic", color=OFF_EDGE)

    ax.set_xlim(x0 - 1.65, x0 + N * cell + 0.55)
    ax.set_ylim(leg_y1 - 0.25, y0 + N * cell + 1.05)
    fig.tight_layout()
    return save(fig, "ch13_variance_grid")


def main() -> None:
    print(f"Generating Chapter 13 (Covariance) figures -> {OUT} at {PRINT_DPI} DPI")
    variance_grid()
    print("Done.")


if __name__ == "__main__":
    main()
