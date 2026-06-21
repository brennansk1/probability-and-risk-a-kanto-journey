#!/usr/bin/env python3
"""Generate every Chapter 15 (Joint Moments & Covariance / Victory Road) figure.

Manifest (MASTER_PLAN_V3 §16) — three required diagrams, all into assets/diagrams/:
  ch15_covariance_scatter  deviation-product scatter: the four quadrants of Cov(X,Y)
  ch15_correlation_signs   three clouds labeled by rho (+, ~0, -) on the [-1,1] ruler
  ch15_linear_combo_var    the variance grid: diagonal variances + mirrored covariances

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is
ALSO distinguished by a hatch pattern / text label so figures survive grayscale
(color is never the sole channel). Sprites obey the IRON RULE: art in margins, never
over a curve, equation, axis, or number a reader must read. Chapter accent is the
Victory Road GROUND type (chapter_accent(15)).

Run: python figures/src/gen_ch15.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
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
GROUND = chapter_accent(15)  # Victory Road ground accent (#E0C068)
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
# 1. ch15_covariance_scatter — deviation-product quadrants of covariance.
#    One labeled panel: dots colored by the SIGN of their deviation-product,
#    with the four quadrants explicitly annotated (the engine of Cov).
# --------------------------------------------------------------------------
def fig_covariance_scatter():
    rng = np.random.default_rng(151)
    n = 220
    # A positively-linked team: Charizard surge X drives Pikachu surge Y.
    x = rng.normal(0, 1, n)
    y = 0.75 * x + rng.normal(0, 0.7, n)

    mx, my = x.mean(), y.mean()
    prod = (x - mx) * (y - my)

    fig, ax = plt.subplots(figsize=(8.4, 6.8))
    ax.set_title("Covariance is the average deviation-product\n"
                 "$\\mathrm{Cov}(X,Y)=\\mathbb{E}[(X-\\mu_X)(Y-\\mu_Y)]$",
                 fontsize=13.5)

    # mean crosshairs split the plane into four quadrants.
    ax.axvline(mx, color=INK, lw=1.4, ls="--", alpha=0.7, zorder=1)
    ax.axhline(my, color=INK, lw=1.4, ls="--", alpha=0.7, zorder=1)

    same = prod > 0   # upper-right & lower-left: deviations agree -> +
    opp = ~same
    ax.scatter(x[same], y[same], s=34, c=KANTO_GREEN, marker="o",
               edgecolors=INK, linewidths=0.4, alpha=0.85, zorder=3,
               label="same-sign deviations  (product $> 0$)")
    ax.scatter(x[opp], y[opp], s=34, c=KANTO_RED, marker="^",
               edgecolors=INK, linewidths=0.4, alpha=0.85, zorder=3,
               label="opposite-sign deviations  (product $< 0$)")

    xlo, xhi = x.min() - 0.6, x.max() + 0.6
    ylo, yhi = y.min() - 0.7, y.max() + 0.9
    ax.set_xlim(xlo, xhi)
    ax.set_ylim(ylo, yhi)

    # quadrant sign tags (in the corners, clear of the cloud's mass).
    tag = dict(fontsize=15, fontweight="bold", ha="center", va="center")
    ax.text(xhi - 0.35, yhi - 0.35, "$+$", color=KANTO_GREEN, **tag)
    ax.text(xlo + 0.35, ylo + 0.35, "$+$", color=KANTO_GREEN, **tag)
    ax.text(xlo + 0.35, yhi - 0.35, "$-$", color=KANTO_RED, **tag)
    ax.text(xhi - 0.35, ylo + 0.35, "$-$", color=KANTO_RED, **tag)

    ax.text(mx + 0.06, yhi - 0.05, "$\\mu_X$", color=INK, fontsize=10,
            ha="left", va="top")
    ax.text(xhi - 0.05, my + 0.06, "$\\mu_Y$", color=INK, fontsize=10,
            ha="right", va="bottom")

    ax.set_xlabel("Charizard surge $X$ (deviation from mean)", fontsize=11)
    ax.set_ylabel("Pikachu surge $Y$ (deviation from mean)", fontsize=11)
    ax.legend(loc="lower right", fontsize=8.6, framealpha=0.95)

    ax.text(0.5, -0.155,
            "Green dots (both deviations agree) push Cov UP; red dots pull it "
            "down.\nHere the up-slope wins: $\\mathrm{Cov}(X,Y)>0$ — the team "
            "surges together.",
            transform=ax.transAxes, ha="center", va="top", fontsize=10,
            color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc="#F5F0DC", ec=GROUND, lw=1.4))

    # decorative sprites in the top-left margin (the two teammates).
    place_sprite(ax, front(6), (xlo + 0.55, yhi - 0.55), zoom=0.22, alpha=0.9,
                 zorder=6)
    place_sprite(ax, front(25), (xlo + 1.25, yhi - 0.55), zoom=0.30, alpha=0.9,
                 zorder=6)

    fig.tight_layout()
    return save(fig, "ch15_covariance_scatter")


# --------------------------------------------------------------------------
# 2. ch15_correlation_signs — three clouds on the [-1,1] correlation ruler.
# --------------------------------------------------------------------------
def fig_correlation_signs():
    rng = np.random.default_rng(151)
    n = 150

    def cloud(rho):
        x = rng.normal(0, 1, n)
        z = rng.normal(0, 1, n)
        y = rho * x + np.sqrt(max(1e-9, 1 - rho ** 2)) * z
        return x, y

    panels = [
        (0.92, "$\\rho \\approx +0.9$", KANTO_GREEN, "o",
         "tight up-slope:\nmove together"),
        (0.0, "$\\rho \\approx 0$", KANTO_GRAY, "s",
         "round blob:\nno linear link"),
        (-0.92, "$\\rho \\approx -0.9$", KANTO_RED, "^",
         "tight down-slope:\nmove apart"),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(12.6, 5.0))
    fig.suptitle("Correlation $\\rho$ = covariance on a fixed $[-1,1]$ ruler "
                 "— how tightly the cloud hugs a line",
                 fontsize=13.5, y=1.02)

    for ax, (rho, lab, color, mk, note) in zip(axes, panels):
        x, y = cloud(rho)
        ax.scatter(x, y, s=26, c=color, marker=mk, edgecolors=INK,
                   linewidths=0.35, alpha=0.85, zorder=3)
        ax.axhline(0, color=INK, lw=0.9, ls="--", alpha=0.5)
        ax.axvline(0, color=INK, lw=0.9, ls="--", alpha=0.5)
        ax.set_xlim(-3.2, 3.2)
        ax.set_ylim(-3.2, 3.2)
        ax.set_xticks([])
        ax.set_yticks([])
        for s in ax.spines.values():
            s.set_edgecolor(INK)
            s.set_linewidth(1.0)
        ax.set_title(lab, fontsize=14, color=color, fontweight="bold")
        ax.text(0.5, -0.10, note, transform=ax.transAxes, ha="center",
                va="top", fontsize=9.5, color=INK)

    # the [-1,1] ruler strip beneath everything.
    fig.text(0.5, -0.10,
             "$-1$  (perfect decreasing line)   $\\cdots$   $0$  (no linear "
             "association)   $\\cdots$   $+1$  (perfect increasing line)",
             ha="center", fontsize=10.5, color=INK,
             bbox=dict(boxstyle="round,pad=0.35", fc="#F5F0DC", ec=GROUND,
                       lw=1.4))

    fig.tight_layout(rect=(0, 0.02, 1, 0.98))
    return save(fig, "ch15_correlation_signs")


# --------------------------------------------------------------------------
# 3. ch15_linear_combo_var — the variance grid (where the factor of 2 lives).
# --------------------------------------------------------------------------
def fig_linear_combo_var():
    fig, ax = plt.subplots(figsize=(8.8, 7.4))
    _blank(ax)
    ax.set_xlim(0, 10)
    ax.set_ylim(-1.0, 10.2)
    ax.set_title("$\\mathrm{Var}\\!\\left(\\sum a_iX_i\\right)$ = sum of every "
                 "cell\n"
                 "diagonal variances + each covariance counted TWICE",
                 fontsize=13.5)

    labels = ["$a_1X_1$", "$a_2X_2$", "$a_3X_3$"]
    n = 3
    x0, y0 = 1.6, 1.6
    cell = 2.3

    # header labels along top and left.
    for k in range(n):
        ax.text(x0 + cell / 2 + k * cell, y0 + n * cell + 0.32, labels[k],
                ha="center", va="bottom", fontsize=12, fontweight="bold",
                color=INK)
        ax.text(x0 - 0.32, y0 + cell / 2 + (n - 1 - k) * cell, labels[k],
                ha="right", va="center", fontsize=12, fontweight="bold",
                color=INK)

    # cells. Row r (top=0) is variable (n-1-r) on the vertical; col c is var c.
    diag_txt = [r"$a_1^2\,\mathrm{Var}(X_1)$",
                r"$a_2^2\,\mathrm{Var}(X_2)$",
                r"$a_3^2\,\mathrm{Var}(X_3)$"]
    cov_txt = {
        (0, 1): r"$a_1a_2\mathrm{Cov}_{12}$",
        (0, 2): r"$a_1a_3\mathrm{Cov}_{13}$",
        (1, 2): r"$a_2a_3\mathrm{Cov}_{23}$",
    }
    for r in range(n):       # visual row from top
        i = n - 1 - r        # variable index on vertical axis
        yy = y0 + r * cell
        for c in range(n):   # column variable index
            xx = x0 + c * cell
            if i == c:
                fc = GROUND
                txt = diag_txt[i]
                hatch = None
            else:
                fc = KANTO_BLUE
                a, b = min(i, c), max(i, c)
                txt = cov_txt[(a, b)]
                hatch = "//"
            ax.add_patch(Rectangle((xx, yy), cell, cell, facecolor=fc,
                                   edgecolor=INK, lw=1.4, alpha=0.78,
                                   hatch=hatch))
            ax.text(xx + cell / 2, yy + cell / 2, txt, ha="center",
                    va="center", fontsize=10.5, color=INK,
                    fontweight="bold" if i == c else "normal")

    # mirror arrows showing each off-diagonal pair appears twice.
    for (a, b) in [(0, 1), (0, 2), (1, 2)]:
        # cell (i=a,c=b) and its mirror (i=b,c=a)
        r1 = n - 1 - a
        cx1 = x0 + b * cell + cell / 2
        cy1 = y0 + r1 * cell + cell / 2
        r2 = n - 1 - b
        cx2 = x0 + a * cell + cell / 2
        cy2 = y0 + r2 * cell + cell / 2
        ax.add_patch(FancyArrowPatch((cx1, cy1), (cx2, cy2),
                     arrowstyle="<->", color=KANTO_RED, lw=1.4,
                     mutation_scale=11, alpha=0.55, zorder=2,
                     connectionstyle="arc3,rad=0.0"))

    # legend chips.
    ax.add_patch(Rectangle((0.4, -0.7), 0.5, 0.5, facecolor=GROUND,
                           edgecolor=INK, lw=1.2, alpha=0.78))
    ax.text(1.05, -0.45, "diagonal: $a_i^2\\,\\mathrm{Var}(X_i)$",
            ha="left", va="center", fontsize=9.5, color=INK)
    ax.add_patch(Rectangle((4.6, -0.7), 0.5, 0.5, facecolor=KANTO_BLUE,
                           edgecolor=INK, lw=1.2, alpha=0.78, hatch="//"))
    ax.text(5.25, -0.45,
            "off-diagonal pair (red arrow) "
            "$\\Rightarrow$ factor of $2$",
            ha="left", va="center", fontsize=9.5, color=INK)

    fig.tight_layout()
    return save(fig, "ch15_linear_combo_var")


REGISTRY = [
    fig_covariance_scatter,
    fig_correlation_signs,
    fig_linear_combo_var,
]


def main() -> None:
    print(f"Generating Chapter 15 (Joint Moments & Covariance) figures -> {OUT} "
          f"at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
