#!/usr/bin/env python3
"""Generate every Chapter 14 (Order Statistics & the CLT / Indigo Plateau) math figure.

Chapter 14's five nine-beat arcs each close on a "Picture it" beat whose <figure>
references one purpose-built diagram. None of these existed yet; this script
renders EXACTLY the five filenames the chapter points at, so picture and caption
agree:

  ch14_max_density            Concept 1, Beat 8: densities of max of n i.i.d.
                              Unif(0,1) for n=1,3,8 (= n x^{n-1}), mass piling
                              toward 1, with the mean n/(n+1) marked.
  ch14_min_exponential_race   Concept 2, Beat 8: three exponential clocks with
                              rates 1/4,1/6,1/12 as timeline arrows with ring
                              markers; the earliest (minimum) flagged; an inset
                              survival plot showing the combined min clock as one
                              steeper exponential of rate 1/2.
  ch14_series_parallel        Concept 3, Beat 8: series circuit (lifetime = min,
                              R = prod S = 0.729) vs parallel circuit (lifetime =
                              max, R = 1 - prod F = 0.999), plus a sorted-dots
                              strip with X_(2) circled.
  ch14_clt_convergence        Concept 4, Beat 8: histograms of the sample mean of
                              n i.i.d. Unif(0,1) for n=1,2,5,30 with a normal
                              curve overlaid, narrowing as variance ~ sigma^2/n.
  ch14_continuity_correction  Concept 5, Beat 8: Binom(400,0.4) bar histogram +
                              normal curve centered at 160, bars >=180 shaded,
                              dashed line at 179.5 marking the left edge of the
                              180 bar.

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element
ALSO carries a linestyle / hatch / direct label, so the figures stay legible in
grayscale.

Run: python figures/src/gen_ch14.py
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle, FancyBboxPatch
from cycler import cycler

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
# Concept 1 -- Density of the maximum of n i.i.d. Unif(0,1): f_max = n x^{n-1}.
# --------------------------------------------------------------------------
def fig_max_density() -> Path:
    fig, ax = plt.subplots(figsize=(8, 5))
    x = np.linspace(0, 1, 600)

    # (n, color, linestyle) -- linestyle distinguishes curves in grayscale.
    specs = [
        (1, KANTO_GRAY, "-",  "n = 1  (flat:  1)"),
        (3, KANTO_BLUE, "--", "n = 3  (3x^2)"),
        (8, KANTO_RED,  "-.", "n = 8  (8x^7)"),
    ]
    for n, color, ls, label in specs:
        y = n * x ** (n - 1)
        ax.plot(x, y, color=color, ls=ls, lw=2.6, label=label, zorder=3)
        mean = n / (n + 1)
        ax.axvline(mean, color=color, ls=":", lw=1.4, alpha=0.8, zorder=2)
        ax.annotate(
            rf"$\frac{{{n}}}{{{n + 1}}}$",
            xy=(mean, 0), xytext=(mean, -0.55 - 0.35 * (n == 8)),
            ha="center", va="top", color=color, fontsize=12,
            annotation_clip=False,
        )

    ax.text(0.50, -1.15, r"mean $\frac{n}{n+1}$ creeps toward 1 $\rightarrow$",
            ha="center", va="top", color=INK, fontsize=11, clip_on=False)

    ax.set_xlim(0, 1.02)
    ax.set_ylim(0, 8.4)
    ax.set_xlabel("x")
    ax.set_ylabel(r"$f_{\max}(x) = n\,x^{\,n-1}$")
    ax.set_title("Density of the maximum of n i.i.d. Uniform(0,1)")
    ax.legend(loc="upper left", framealpha=0.95)
    fig.subplots_adjust(bottom=0.22)
    return save(fig, "ch14_max_density")


# --------------------------------------------------------------------------
# Concept 2 -- The exponential race: min of independent exponentials.
# --------------------------------------------------------------------------
def fig_min_exponential_race() -> Path:
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.set_facecolor("white")
    ax.grid(False)
    for s in ax.spines.values():
        s.set_visible(False)

    # Three clocks: rates 1/4, 1/6, 1/12 -> means 4, 6, 12.
    # Illustrative ring times (a representative race outcome); min flagged.
    clocks = [
        (r"Clock A:  rate $\frac{1}{4}$  (mean 4)",  KANTO_RED,   "//",  2.3),
        (r"Clock B:  rate $\frac{1}{6}$  (mean 6)",  KANTO_BLUE,  "\\\\", 5.1),
        (r"Clock C:  rate $\frac{1}{12}$ (mean 12)", KANTO_GREEN, "xx",  9.4),
    ]
    t_max = 12.5
    ys = [2.4, 1.5, 0.6]
    earliest = min(c[3] for c in clocks)

    for (label, color, hatch, ring), y in zip(clocks, ys):
        ax.add_patch(FancyArrowPatch(
            (0, y), (t_max, y), arrowstyle="-|>", mutation_scale=16,
            color=INK, lw=1.6, zorder=2))
        # ring-time marker
        ax.add_patch(Circle((ring, y), 0.13, facecolor=color,
                            edgecolor=INK, lw=1.2, hatch=hatch, zorder=4))
        ax.text(ring, y + 0.22, f"ring @ {ring:g}", ha="center", va="bottom",
                color=color, fontsize=9.5)
        ax.text(-0.3, y, label, ha="right", va="center", color=INK, fontsize=10)

    # Vertical line at the minimum (earliest ring).
    ax.axvline(earliest, color=KANTO_RED, ls="--", lw=2.0, zorder=1)
    ax.text(earliest, 3.05, f"minimum = first ring @ {earliest:g}",
            ha="center", va="bottom", color=KANTO_RED, fontsize=11,
            fontweight="bold")

    ax.set_xlim(-3.6, t_max + 0.4)
    ax.set_ylim(0.0, 3.5)
    ax.set_yticks([])
    ax.set_xlabel("time (minutes)")
    ax.set_xticks(range(0, 13, 2))
    ax.tick_params(axis="x", length=4)
    ax.spines["bottom"].set_visible(True)
    ax.spines["bottom"].set_position(("data", 0.15))
    ax.spines["bottom"].set_color(INK)
    ax.set_title("The exponential race: the first clock to ring",
                 loc="left", pad=14)

    # Inset: survival curves + combined min clock (rate 1/2, steeper).
    inset = fig.add_axes([0.62, 0.50, 0.30, 0.32])
    tt = np.linspace(0, 12, 400)
    inset.plot(tt, np.exp(-tt / 4), color=KANTO_RED, ls="-",
               lw=1.6, label="A")
    inset.plot(tt, np.exp(-tt / 6), color=KANTO_BLUE, ls="--", lw=1.6, label="B")
    inset.plot(tt, np.exp(-tt / 12), color=KANTO_GREEN, ls="-.", lw=1.6, label="C")
    inset.plot(tt, np.exp(-tt / 2), color=INK, ls=":", lw=2.6,
               label=r"min: rate $\frac{1}{2}$")
    inset.set_title(r"survival $S(t)$ -- rates add", fontsize=9.5)
    inset.set_xlabel("t", fontsize=8)
    inset.tick_params(labelsize=7)
    inset.legend(fontsize=6.8, loc="upper right", framealpha=0.9)
    inset.set_xlim(0, 12)
    inset.set_ylim(0, 1.02)

    return save(fig, "ch14_min_exponential_race")


# --------------------------------------------------------------------------
# Concept 3 -- Series vs parallel reliability + k-th order statistic strip.
# --------------------------------------------------------------------------
def fig_series_parallel() -> Path:
    fig = plt.figure(figsize=(9.2, 6.0))
    gs = fig.add_gridspec(2, 2, height_ratios=[3, 1], hspace=0.35, wspace=0.22)
    ax_s = fig.add_subplot(gs[0, 0])
    ax_p = fig.add_subplot(gs[0, 1])
    ax_k = fig.add_subplot(gs[1, :])

    def comp_box(ax, cx, cy, color, hatch):
        ax.add_patch(FancyBboxPatch(
            (cx - 0.32, cy - 0.18), 0.64, 0.36,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            facecolor=color, edgecolor=INK, lw=1.6, hatch=hatch, alpha=0.9))

    colors = [KANTO_RED, KANTO_BLUE, KANTO_GREEN]
    hatches = ["//", "\\\\", "xx"]

    # --- Series (single line): lifetime = min ---
    ax_s.set_title("Series  (chain)", fontsize=13, fontweight="bold")
    ys = 0.55
    ax_s.plot([-0.2, 0.18], [ys, ys], color=INK, lw=1.6)
    centers = [0.5, 1.5, 2.5]
    for cx, color, hatch in zip(centers, colors, hatches):
        comp_box(ax_s, cx, ys, color, hatch)
    ax_s.plot([0.82, 1.18], [ys, ys], color=INK, lw=1.6)
    ax_s.plot([1.82, 2.18], [ys, ys], color=INK, lw=1.6)
    ax_s.plot([2.82, 3.2], [ys, ys], color=INK, lw=1.6)
    ax_s.text(1.5, 0.05, "lifetime = min   (weakest link)",
              ha="center", va="center", fontsize=10.5, color=INK)
    ax_s.text(1.5, -0.18,
              r"$R = \prod_i S_i = 0.9^3 = 0.729$",
              ha="center", va="center", fontsize=11.5, color=KANTO_RED)
    ax_s.set_xlim(-0.4, 3.4)
    ax_s.set_ylim(-0.35, 1.0)

    # --- Parallel (three branches): lifetime = max ---
    ax_p.set_title("Parallel  (backups)", fontsize=13, fontweight="bold")
    branch_y = [0.85, 0.55, 0.25]
    for by, color, hatch in zip(branch_y, colors, hatches):
        ax_p.plot([0.1, 0.55], [0.55, by], color=INK, lw=1.4)
        comp_box(ax_p, 1.0, by, color, hatch)
        ax_p.plot([1.45, 1.9], [by, 0.55], color=INK, lw=1.4)
    ax_p.plot([-0.15, 0.1], [0.55, 0.55], color=INK, lw=1.6)
    ax_p.plot([1.9, 2.15], [0.55, 0.55], color=INK, lw=1.6)
    ax_p.text(1.0, -0.02, "lifetime = max   (last backup)",
              ha="center", va="center", fontsize=10.5, color=INK)
    ax_p.text(1.0, -0.25,
              r"$R = 1 - \prod_i F_i = 1 - 0.1^3 = 0.999$",
              ha="center", va="center", fontsize=11.5, color=KANTO_BLUE)
    ax_p.set_xlim(-0.35, 2.35)
    ax_p.set_ylim(-0.42, 1.1)

    for ax in (ax_s, ax_p):
        ax.set_aspect("equal")
        ax.axis("off")

    # --- Sorted-dots strip on [0,1] with X_(2) circled ---
    ax_k.set_title(r"Order statistics: the $k$-th sorted value  "
                   r"($X_{(2)}$ = 2nd smallest)", fontsize=11.5)
    ax_k.annotate("", xy=(1.05, 0), xytext=(-0.05, 0),
                  arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.6))
    dots = [0.14, 0.33, 0.61, 0.88]   # already sorted
    labels = [r"$X_{(1)}$", r"$X_{(2)}$", r"$X_{(3)}$", r"$X_{(4)}$"]
    for i, (d, lab) in enumerate(zip(dots, labels)):
        ax_k.add_patch(Circle((d, 0), 0.022, facecolor=KANTO_GRAY,
                              edgecolor=INK, lw=1.0, zorder=3))
        ax_k.annotate(lab, xy=(d, 0), xytext=(d, 0.14), ha="center",
                      va="bottom", fontsize=10, color=INK)
    # circle the second-from-left
    ax_k.add_patch(Circle((dots[1], 0), 0.05, facecolor="none",
                          edgecolor=KANTO_RED, lw=2.4, zorder=4))
    ax_k.text(1.02, -0.16, "x", ha="center", va="top", fontsize=10, color=INK)
    ax_k.text(0.0, -0.16, "0", ha="center", va="top", fontsize=10, color=INK)
    ax_k.text(1.0, -0.16, "1", ha="center", va="top", fontsize=10, color=INK)
    ax_k.set_xlim(-0.08, 1.12)
    ax_k.set_ylim(-0.28, 0.30)
    ax_k.axis("off")

    return save(fig, "ch14_series_parallel")


# --------------------------------------------------------------------------
# Concept 4 -- CLT convergence: sample mean of n i.i.d. Unif(0,1).
# --------------------------------------------------------------------------
def fig_clt_convergence() -> Path:
    rng = np.random.default_rng(7)
    ns = [1, 2, 5, 30]
    fig, axes = plt.subplots(2, 2, figsize=(9, 6.2))
    axes = axes.ravel()
    reps = 200_000
    bins = np.linspace(0, 1, 46)
    centers = 0.5 * (bins[:-1] + bins[1:])

    for ax, n in zip(axes, ns):
        means = rng.random((reps, n)).mean(axis=1)
        ax.hist(means, bins=bins, density=True, color=KANTO_BLUE,
                edgecolor="white", alpha=0.85, zorder=2,
                label=f"sample mean, n = {n}")
        # Overlaid normal: mean 1/2, variance (1/12)/n.
        mu, var = 0.5, (1 / 12) / n
        sd = math.sqrt(var)
        nx = np.linspace(0, 1, 400)
        ny = np.exp(-0.5 * ((nx - mu) / sd) ** 2) / (sd * math.sqrt(2 * math.pi))
        ax.plot(nx, ny, color=KANTO_RED, lw=2.4, zorder=3, label="normal curve")
        ax.set_title(f"n = {n}", fontsize=12, fontweight="bold")
        ax.set_xlim(0, 1)
        ax.set_xlabel(r"$\bar X_n$", fontsize=11)
        ax.legend(fontsize=8.5, loc="upper right", framealpha=0.92)

    fig.suptitle(r"The CLT in action: sample mean of Uniform(0,1) "
                 r"goes normal (and narrows like $\sigma^2/n$)",
                 fontsize=13, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    return save(fig, "ch14_clt_convergence")


# --------------------------------------------------------------------------
# Concept 5 -- Continuity correction on Binom(400, 0.4).
# --------------------------------------------------------------------------
def fig_continuity_correction() -> Path:
    n, p = 400, 0.4
    mu = n * p                       # 160
    sigma = math.sqrt(n * p * (1 - p))  # sqrt(96) ~ 9.798

    # Exact binomial pmf via log-gamma for numerical stability.
    ks = np.arange(120, 205)
    log_pmf = (
        np.array([math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
                  for k in ks])
        + ks * math.log(p) + (n - ks) * math.log(1 - p)
    )
    pmf = np.exp(log_pmf)

    fig, ax = plt.subplots(figsize=(9, 5.2))
    shaded = ks >= 180
    ax.bar(ks[~shaded], pmf[~shaded], width=1.0, color=KANTO_GRAY,
           edgecolor="white", lw=0.4, alpha=0.7, zorder=2,
           label="Binomial(400, 0.4) bars")
    ax.bar(ks[shaded], pmf[shaded], width=1.0, color=KANTO_BLUE,
           edgecolor="white", lw=0.4, alpha=0.9, zorder=2, hatch="//",
           label=r"bars with $X \geq 180$")

    # Overlaid normal curve centered at mu.
    xx = np.linspace(ks.min(), ks.max(), 600)
    yy = np.exp(-0.5 * ((xx - mu) / sigma) ** 2) / (sigma * math.sqrt(2 * math.pi))
    ax.plot(xx, yy, color=KANTO_RED, lw=2.4, zorder=4,
            label=r"normal $\mathcal{N}(160,\,96)$")

    # Dashed line at 179.5 -- left edge of the 180 bar.
    ax.axvline(179.5, color=INK, ls="--", lw=2.0, zorder=5)
    ax.annotate(r"corrected boundary $179.5$" + "\n(left edge of the 180 bar)",
                xy=(179.5, 0.0125), xytext=(150, 0.030),
                ha="center", fontsize=10, color=INK,
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))
    ax.axvline(mu, color=KANTO_GREEN, ls=":", lw=1.6, zorder=3)
    ax.text(mu, 0.0415, r"$\mu = 160$", ha="center", va="bottom",
            color=KANTO_GREEN, fontsize=10)

    ax.set_xlim(135, 200)
    ax.set_ylim(0, 0.044)
    ax.set_xlabel("number of wins  X")
    ax.set_ylabel("probability")
    ax.set_title("Continuity correction: include the whole 180 bar")
    ax.legend(loc="upper right", framealpha=0.95)
    return save(fig, "ch14_continuity_correction")


def main() -> None:
    print("Generating Chapter 14 figures (order statistics & CLT):")
    fig_max_density()
    fig_min_exponential_race()
    fig_series_parallel()
    fig_clt_convergence()
    fig_continuity_correction()
    print("Done.")


if __name__ == "__main__":
    main()
