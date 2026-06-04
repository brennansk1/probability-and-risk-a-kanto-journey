#!/usr/bin/env python3
"""Generate every Chapter 6 (Random Variables / S.S. Anne) math figure.

Chapter 6 introduces the "RV web" — pmf, pdf, cdf, survival, percentile — and
closes each concept on a "Picture it" beat whose <figure> references one
purpose-built diagram. None of these existed yet; this script renders EXACTLY
the six filenames the chapter points at, so picture and caption agree:

  ch06_discrete_vs_continuous   Concept 1, Beat 8: two panels. DISCRETE: spikes
                                at 0,1,2,3 of height 0.1,0.4,0.3,0.2 summing to 1.
                                CONTINUOUS: a smooth shaded density whose AREA
                                (not height) is the probability, total area 1.
  ch06_pmf_bars                 Concept 2, Beat 8: pmf bar chart over 0,1,2,3 with
                                heights 0.1,0.4,0.3,0.2; bars x=2,3 shaded to show
                                P(X>=2)=0.5; note all heights sum to 1.
  ch06_pdf_area                 Concept 3, Beat 8: density line f(x)=2(1-x) on
                                [0,1]; region [0,0.5] shaded with area 3/4 =
                                P(X<=1/2); note f(0)=2>1 height is a density;
                                whole area = 1.
  ch06_cdf_staircase_smooth     Concept 4, Beat 8: two panels. DISCRETE: a
                                right-continuous staircase jumping 0.1,0.4,0.3,0.2
                                at 0,1,2,3 with filled/open dots. CONTINUOUS: the
                                smooth cdf F(x)=1-e^{-x/4} with F(2)~=0.393 marked.
  ch06_cdf_survival_percentile  Concept 5, Beat 8: cdf F(t)=1-e^{-t/8} rising and
                                survival S(t)=e^{-t/8} falling, crossing at 0.5;
                                median read off at t=8 ln 2 ~= 5.55.
  ch06_rv_web                   Concept 5 closer: hub-and-spoke "RV web" with cdf
                                as the hub connecting pmf/pdf, survival, percentile
                                via labeled arrows (accumulate / differentiate /
                                S=1-F / invert).

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element
ALSO carries a linestyle / hatch / direct label, so the figures stay legible in
grayscale. No Pokemon art.

Run: python figures/src/gen_ch06.py
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

from sprite_util import front, item, place_sprite

# --- paths / theme -----------------------------------------------------------
HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
STYLE = HERE / "kanto_theme.mplstyle"
OUT = REPO / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(STYLE))

# Kanto palette (color-blind-safe usage: always paired with label/linestyle/hatch)
RED = "#EE1515"
BLUE = "#3B4CCA"
YELLOW = "#FFD733"
GREEN = "#4DAD5B"
INK = "#333333"

DPI = 300

# pmf used throughout the discrete examples
PMF_X = np.array([0, 1, 2, 3])
PMF_P = np.array([0.1, 0.4, 0.3, 0.2])


def save(fig, name):
    path = OUT / name
    fig.savefig(path, dpi=DPI)
    plt.close(fig)
    print(f"wrote {path}")


# -----------------------------------------------------------------------------
# 1. discrete vs continuous
# -----------------------------------------------------------------------------
def fig_discrete_vs_continuous():
    fig, (axd, axc) = plt.subplots(1, 2, figsize=(11, 5))

    # DISCRETE: spikes
    axd.set_title("DISCRETE", color=BLUE)
    axd.vlines(PMF_X, 0, PMF_P, color=BLUE, linewidth=4, zorder=3)
    axd.scatter(PMF_X, PMF_P, color=BLUE, s=70, zorder=4, edgecolor=INK)
    for x, p in zip(PMF_X, PMF_P):
        axd.annotate(f"{p:g}", (x, p), textcoords="offset points",
                     xytext=(0, 8), ha="center", fontsize=11, color=INK)
    axd.axhline(0, color=INK, linewidth=1.0)
    axd.set_xlim(-0.6, 3.6)
    axd.set_ylim(0, 0.52)
    axd.set_xticks(PMF_X)
    axd.set_xlabel("value $x$")
    axd.set_ylabel("probability $P(X=x)$")
    axd.text(0.5, 0.97, "spikes sum to $1$", transform=axd.transAxes,
             ha="center", va="top", fontsize=11, style="italic", color=INK,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#CCCCCC"))

    # CONTINUOUS: smooth density, area is the probability
    axc.set_title("CONTINUOUS", color=RED)
    x = np.linspace(0, 6, 400)
    # a smooth unimodal density (gamma-ish), normalized over the window
    f = (x ** 2) * np.exp(-x)
    f = f / np.trapz(f, x)
    axc.plot(x, f, color=RED, linewidth=2.5, label="density $f(x)$")
    # shade a sub-interval as "the probability"
    mask = (x >= 1.2) & (x <= 3.0)
    axc.fill_between(x[mask], f[mask], color=RED, alpha=0.30, hatch="///",
                     edgecolor=RED, label="$P(a\\leq X\\leq b)$ = area")
    axc.axhline(0, color=INK, linewidth=1.0)
    axc.set_xlim(0, 6)
    axc.set_ylim(0, f.max() * 1.25)
    axc.set_xlabel("value $x$")
    axc.set_ylabel("density $f(x)$")
    axc.annotate("area, not height,\nis the probability",
                 xy=(2.0, 0.12), xytext=(3.3, 0.27),
                 fontsize=10.5, color=INK, ha="left",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    axc.text(0.5, 0.97, "total area $=1$", transform=axc.transAxes,
             ha="center", va="top", fontsize=11, style="italic", color=INK,
             bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#CCCCCC"))
    axc.legend(loc="upper right", fontsize=9.5)

    # --- decorative sprites (margins only; never over data) -----------------
    # discrete: a small Pidgey sits in the upper-left margin (count = "how many")
    place_sprite(axd, front(16), (0.10, 0.86), xycoords="axes fraction",
                 zoom=0.42, alpha=0.95)
    # continuous: a Magikarp rides the lower-right margin, clear of curve/area
    place_sprite(axc, front(129), (0.88, 0.32), xycoords="axes fraction",
                 zoom=0.38, alpha=0.9)

    fig.suptitle("Two ways probability lives on the line",
                 fontsize=15, fontweight="bold", y=1.02)
    fig.tight_layout()
    save(fig, "ch06_discrete_vs_continuous.png")


# -----------------------------------------------------------------------------
# 2. pmf bars  (P(X>=2) = 0.5 shaded)
# -----------------------------------------------------------------------------
def fig_pmf_bars():
    fig, ax = plt.subplots(figsize=(8, 5.2))
    colors = [BLUE if x < 2 else RED for x in PMF_X]
    hatches = ["" if x < 2 else "///" for x in PMF_X]
    bars = ax.bar(PMF_X, PMF_P, width=0.55, color=colors, edgecolor=INK,
                  linewidth=1.2)
    for b, h in zip(bars, hatches):
        b.set_hatch(h)
    for x, p in zip(PMF_X, PMF_P):
        ax.annotate(f"{p:g}", (x, p), textcoords="offset points",
                    xytext=(0, 6), ha="center", fontsize=12, color=INK)

    ax.set_xticks(PMF_X)
    ax.set_xlabel("flooded compartments $x$")
    ax.set_ylabel("probability $P(X=x)$")
    ax.set_ylim(0, 0.5)
    ax.set_xlim(-0.6, 3.6)
    ax.set_title("The flooded-compartment pmf")

    # legend explaining shading
    from matplotlib.patches import Patch
    handles = [
        Patch(facecolor=BLUE, edgecolor=INK, label="$x<2$"),
        Patch(facecolor=RED, edgecolor=INK, hatch="///",
              label="$P(X\\geq 2)=0.3+0.2=0.5$"),
    ]
    ax.legend(handles=handles, loc="upper right")
    # note relocated to the empty gutter over x=0 (clear of every bar)
    ax.text(0.0, 0.44, "all four heights\nsum to $1$",
            ha="center", va="center", fontsize=10.5, style="italic", color=INK,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="#CCCCCC"))

    # decorative: a small Pidgey perches atop the tallest bar (margin, no data)
    place_sprite(ax, front(16), (1, 0.40 + 0.045), zoom=0.40, alpha=0.95)

    fig.tight_layout()
    save(fig, "ch06_pmf_bars.png")


# -----------------------------------------------------------------------------
# 3. pdf area  f(x)=2(1-x) on [0,1], shade [0,0.5] = 3/4
# -----------------------------------------------------------------------------
def fig_pdf_area():
    fig, ax = plt.subplots(figsize=(8, 5.2))
    x = np.linspace(0, 1, 200)
    f = 2 * (1 - x)
    ax.plot(x, f, color=RED, linewidth=2.6, label="$f(x)=2(1-x)$")

    mask = x <= 0.5
    ax.fill_between(x[mask], f[mask], color=RED, alpha=0.30, hatch="///",
                    edgecolor=RED)
    ax.axhline(0, color=INK, linewidth=1.0)
    ax.axhline(1, color=INK, linewidth=0.8, linestyle=":")
    # "height = 1" reference, kept inside the right edge (ha=right)
    ax.text(0.985, 1.05, "height $=1$ ", va="bottom", ha="right",
            fontsize=9.5, color=INK)

    # area label (points into the shaded region, below the line)
    ax.annotate("$P(X\\leq\\frac{1}{2})=$ shaded area $=\\frac{3}{4}$",
                xy=(0.22, 0.85), xytext=(0.34, 1.45),
                fontsize=12, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    # height-is-density note (points at f(0)=2; text well clear to the right)
    ax.annotate("height is a density,\nnot a probability\n($f(0)=2>1$)",
                xy=(0.0, 2.0), xytext=(0.30, 2.10),
                fontsize=10.5, color=INK, ha="left", va="top",
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    # whole-area = 1 note (in the unshaded lower-right triangle, clear of curve)
    ax.text(0.70, 0.28, "whole area\nunder line $=1$", fontsize=10.5,
            color=INK, ha="center", style="italic")

    ax.set_xlim(0, 1.04)
    ax.set_ylim(0, 2.35)
    ax.set_xlabel("depth fraction $x$")
    ax.set_ylabel("density $f(x)$")
    ax.set_title("The depth density: probability is shaded area")
    # legend lower-left, clear of every annotation
    ax.legend(loc="lower left", bbox_to_anchor=(0.015, 0.02))

    # decorative: a Magikarp drifts in the lower-right margin (water depth motif)
    place_sprite(ax, front(129), (0.90, 0.13), xycoords="axes fraction",
                 zoom=0.36, alpha=0.9)

    fig.tight_layout()
    save(fig, "ch06_pdf_area.png")


# -----------------------------------------------------------------------------
# 4. cdf staircase (discrete) vs smooth cdf (continuous)
# -----------------------------------------------------------------------------
def fig_cdf_staircase_smooth():
    fig, (axd, axc) = plt.subplots(1, 2, figsize=(11, 5))

    # DISCRETE staircase, right-continuous
    axd.set_title("DISCRETE: staircase", color=BLUE)
    cum = np.cumsum(PMF_P)  # 0.1,0.5,0.8,1.0
    F_before = np.concatenate(([0.0], cum))  # value just left of each jump point
    # horizontal segments
    edges = [-1] + list(PMF_X) + [4]
    levels = [0.0] + list(cum)
    for i in range(len(levels)):
        x0 = edges[i]
        x1 = edges[i + 1]
        axd.hlines(levels[i], x0, x1, color=BLUE, linewidth=2.6, zorder=2)
    # dots: filled at top of jump (included), open at bottom (right-continuous)
    for j, x in enumerate(PMF_X):
        top = cum[j]
        bottom = F_before[j]
        axd.plot(x, top, "o", color=BLUE, markersize=8, zorder=5)        # included
        axd.plot(x, bottom, "o", mfc="white", mec=BLUE, mew=1.8,
                 markersize=8, zorder=5)                                  # excluded
    axd.set_xlim(-1, 4)
    axd.set_ylim(0, 1.08)
    axd.set_xticks(PMF_X)
    axd.set_xlabel("value $x$")
    axd.set_ylabel("$F(x)=P(X\\leq x)$")
    axd.text(0.04, 0.96, "right-continuous:\nfilled dot included,\nopen dot excluded",
             transform=axd.transAxes, ha="left", va="top", fontsize=9.5,
             color=INK, bbox=dict(boxstyle="round,pad=0.3", fc="white",
                                  ec="#CCCCCC"))

    # CONTINUOUS smooth cdf F(x)=1-e^{-x/4}, F(2)~=0.393
    axc.set_title("CONTINUOUS: smooth climb", color=RED)
    x = np.linspace(0, 20, 400)
    F = 1 - np.exp(-x / 4)
    axc.plot(x, F, color=RED, linewidth=2.6, label="$F(x)=1-e^{-x/4}$")
    axc.axhline(1, color=INK, linewidth=0.8, linestyle=":")
    axc.text(20, 1.0, " asymptote $1$", va="center", ha="right",
             fontsize=9.5, color=INK)
    F2 = 1 - math.exp(-2 / 4)
    axc.plot([2, 2], [0, F2], color=INK, linestyle="--", linewidth=1.2)
    axc.plot([0, 2], [F2, F2], color=INK, linestyle="--", linewidth=1.2)
    axc.plot(2, F2, "o", color=RED, markersize=8, zorder=5)
    axc.annotate(f"$F(2)\\approx{F2:.3f}$", xy=(2, F2), xytext=(5.5, F2 - 0.12),
                 fontsize=11, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    axc.set_xlim(0, 20)
    axc.set_ylim(0, 1.08)
    axc.set_xlabel("value $x$")
    axc.set_ylabel("$F(x)=P(X\\leq x)$")
    axc.text(0.5, 0.04, "slope is the density", transform=axc.transAxes,
             ha="center", va="bottom", fontsize=10, style="italic", color=INK)

    # --- decorative sprites (lower-right margins, clear of curves) ----------
    place_sprite(axd, front(16), (0.88, 0.20), xycoords="axes fraction",
                 zoom=0.40, alpha=0.95)   # discrete: Pidgey count
    place_sprite(axc, front(120), (0.86, 0.20), xycoords="axes fraction",
                 zoom=0.40, alpha=0.9)    # continuous: Staryu recovery time

    fig.suptitle("The cdf accumulates probability from $0$ to $1$",
                 fontsize=15, fontweight="bold", y=1.02)
    fig.tight_layout()
    save(fig, "ch06_cdf_staircase_smooth.png")


# -----------------------------------------------------------------------------
# 5. cdf + survival + median percentile read
# -----------------------------------------------------------------------------
def fig_cdf_survival_percentile():
    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    t = np.linspace(0, 30, 500)
    F = 1 - np.exp(-t / 8)
    S = np.exp(-t / 8)
    ax.plot(t, F, color=BLUE, linewidth=2.6, label="cdf $F(t)=1-e^{-t/8}$ (rising)")
    ax.plot(t, S, color=RED, linewidth=2.6, linestyle="--",
            label="survival $S(t)=e^{-t/8}$ (falling)")

    # median read
    med = 8 * math.log(2)  # ~5.545
    ax.axhline(0.5, color=INK, linestyle=":", linewidth=1.2)
    ax.plot([med, med], [0, 0.5], color=INK, linestyle=":", linewidth=1.2)
    ax.plot(med, 0.5, "o", color=YELLOW, markeredgecolor=INK, markersize=10,
            zorder=6)
    ax.annotate(f"median: $F=0.5$ at\n$t=8\\ln 2\\approx{med:.2f}$ min",
                xy=(med, 0.5), xytext=(11, 0.62), fontsize=11, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    # vertical gap = 1 annotation
    tg = 12.0
    Fg = 1 - math.exp(-tg / 8)
    Sg = math.exp(-tg / 8)
    ax.annotate("", xy=(tg, Fg), xytext=(tg, Sg),
                arrowprops=dict(arrowstyle="<->", color=GREEN, lw=2.0))
    ax.text(tg + 0.5, (Fg + Sg) / 2,
            "$F(t)+S(t)=1$\nat every $t$", color=INK, fontsize=10.5,
            va="center")

    ax.set_xlim(0, 30)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("recovery time $t$ (minutes)")
    ax.set_ylabel("probability")
    ax.set_title("Cdf and survival are mirror images summing to $1$")
    ax.legend(loc="center right")

    # decorative: Staryu in the upper-left margin (its recovery time is T)
    place_sprite(ax, front(120), (0.085, 0.86), xycoords="axes fraction",
                 zoom=0.42, alpha=0.95)

    fig.tight_layout()
    save(fig, "ch06_cdf_survival_percentile.png")


# -----------------------------------------------------------------------------
# 6. the RV web (hub-and-spoke)
# -----------------------------------------------------------------------------
def fig_rv_web():
    fig, ax = plt.subplots(figsize=(9, 7))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.grid(False)

    nodes = {
        "pmfpdf": (2.0, 8.0, "pmf / pdf", BLUE),
        "cdf": (5.0, 5.0, "cdf  $F$\n(hub)", YELLOW),
        "survival": (8.2, 7.6, "survival\n$S$", RED),
        "percentile": (8.2, 2.4, "percentile\n$\\pi_p$", GREEN),
    }

    def draw_node(key, big=False):
        x, y, label, color = nodes[key]
        w = 2.4 if big else 2.0
        h = 1.5 if big else 1.2
        box = FancyBboxPatch((x - w / 2, y - h / 2), w, h,
                             boxstyle="round,pad=0.1,rounding_size=0.25",
                             linewidth=1.6, edgecolor=INK, facecolor=color,
                             alpha=0.9 if key == "cdf" else 0.30, zorder=3)
        ax.add_patch(box)
        ax.text(x, y, label, ha="center", va="center", fontsize=12.5,
                fontweight="bold", color=INK, zorder=4)

    for k in nodes:
        draw_node(k, big=(k == "cdf"))

    def arrow(p0, p1, color, rad=0.0):
        a = FancyArrowPatch(p0, p1, connectionstyle=f"arc3,rad={rad}",
                            arrowstyle="-|>", mutation_scale=20,
                            color=color, linewidth=2.0, zorder=2)
        ax.add_patch(a)

    def label(x, y, text, color, fontsize=11):
        # white-backed label so it stays legible and never reads as struck-through
        ax.text(x, y, text, color=color, fontsize=fontsize, ha="center",
                va="center", zorder=6,
                bbox=dict(boxstyle="round,pad=0.25", fc="white",
                          ec=color, alpha=0.95, linewidth=1.0))

    cx, cy = nodes["cdf"][0], nodes["cdf"][1]
    px, py = nodes["pmfpdf"][0], nodes["pmfpdf"][1]
    sx, sy = nodes["survival"][0], nodes["survival"][1]
    qx, qy = nodes["percentile"][0], nodes["percentile"][1]

    # pmf/pdf <-> cdf: two well-separated curved arrows so labels sit clear of both
    # accumulate (down, left lane)
    arrow((px + 0.2, py - 0.8), (cx - 1.5, cy + 0.9), BLUE, rad=0.35)
    label(1.85, 6.35, "accumulate\n(sum / integrate)", BLUE, fontsize=9.5)
    # differentiate (up, right lane)
    arrow((cx - 1.0, cy + 1.0), (px + 1.2, py - 0.9), INK, rad=0.35)
    label(4.25, 6.95, "differentiate", INK, fontsize=9.5)

    # cdf -> survival
    arrow((cx + 1.35, cy + 0.5), (sx - 1.25, sy - 0.7), RED, rad=-0.18)
    label(6.75, 6.55, "$S=1-F$", RED)

    # cdf -> percentile
    arrow((cx + 1.35, cy - 0.5), (qx - 1.25, qy + 0.7), GREEN, rad=0.18)
    label(6.75, 3.45, "invert:\nsolve $F=p$", GREEN)

    # decorative items in empty corners (illustrative; never over arrows/labels)
    place_sprite(ax, item("poke-ball"), (0.9, 8.9), zoom=0.85, alpha=0.9)
    place_sprite(ax, item("potion"), (1.0, 1.6), zoom=0.85, alpha=0.9)

    ax.set_title("The RV Web", fontsize=17, fontweight="bold")
    ax.text(5.0, 0.4, "the cdf $F$ is the hub: reach every other object from it",
            ha="center", fontsize=10.5, style="italic", color=INK)
    fig.tight_layout()
    save(fig, "ch06_rv_web.png")


def main():
    fig_discrete_vs_continuous()
    fig_pmf_bars()
    fig_pdf_area()
    fig_cdf_staircase_smooth()
    fig_cdf_survival_percentile()
    fig_rv_web()


if __name__ == "__main__":
    main()
