#!/usr/bin/env python3
"""Generate every Chapter 7 (Center & Spread / Expectation, Variance, MGF) math figure.

Chapter 7's five concept arcs each close on a "Picture it" / "Table it" beat whose
<figure> references one purpose-built diagram. None of these existed yet; this
script renders EXACTLY the five filenames the chapter points at, so picture and
caption agree:

  ch07_expectation_balance   Concept 1, Beat 8: expectation as center of mass.
                             A discrete seesaw with weighted blocks at x=1 (0.5),
                             x=2 (0.3), x=5 (0.2) balanced on a fulcrum at the mean
                             2.10; beside it a continuous density balanced on a
                             fulcrum under its mean.
  ch07_jensen_lotus          Concept 2, Beat 8: y = x^2 with equally likely inputs
                             x=1, x=3 mapping to outputs 1 and 9; average of outputs
                             = 5 = E[X^2] (correct) vs mapping the mean input 2 to
                             4 = g(E[X]) (the trap). Bracket shows the gap 5-4 = 1
                             = Var(X).
  ch07_variance_spread       Concept 3, Beat 8: two distributions, SAME mean 2,
                             different spread (tight vs wide), squared-deviation
                             shading = Var(X); side note on shift-by-b (slides, no
                             change) and scale-by-a (stretches, spread x a^2).
  ch07_mgf_kernels           Concept 4, Beat 8: reference table of MGF kernels
                             (Gamma, Poisson, Binomial, Normal, Exponential) with
                             mean, variance, and the "read it off" parameter slot.
  ch07_survival_darthvader   Concept 5, Beat 8: a falling survival curve
                             S(x) = P(X>x) from 1 toward 0, entire area shaded and
                             labeled area = E[X]; note X >= 0.

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element
ALSO carries a linestyle / hatch / direct label, so the figures stay legible in
grayscale.

Run: python figures/src/gen_ch07.py
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch, Polygon, FancyBboxPatch
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
# Concept 1 -- Expectation is the balance point (center of mass).
#   Discrete prize: x=1 (p=0.5), x=2 (p=0.3), x=5 (p=0.2), mean = 2.10.
#   Continuous: a right-skewed density balanced on a fulcrum under its mean.
# --------------------------------------------------------------------------
def fig_expectation_balance() -> Path:
    fig, (axd, axc) = plt.subplots(1, 2, figsize=(11, 5))

    # ---- Left: discrete seesaw --------------------------------------------
    xs = [1.0, 2.0, 5.0]
    ps = [0.5, 0.3, 0.2]
    mean = sum(x * p for x, p in zip(xs, ps))  # 2.10
    cols = [KANTO_BLUE, KANTO_GREEN, KANTO_RED]
    hatches = ["//", "..", "xx"]

    beam_y = 0.0
    axd.axhline(beam_y, color=INK, lw=2.5, zorder=3)  # the seesaw beam

    bar_w = 0.34
    for x, p, c, h in zip(xs, ps, cols, hatches):
        axd.add_patch(Rectangle((x - bar_w / 2, beam_y), bar_w, p,
                                facecolor=c, edgecolor=INK, hatch=h,
                                lw=1.3, alpha=0.92, zorder=4))
        axd.text(x, p + 0.03, f"p = {p}", ha="center", va="bottom",
                 fontsize=10, color=INK)
        axd.text(x, -0.055, f"$x={int(x)}$", ha="center", va="top",
                 fontsize=11, color=INK)

    # Fulcrum (triangle) at the balance point = mean.
    tri_h = 0.16
    axd.add_patch(Polygon([(mean, beam_y), (mean - 0.22, beam_y - tri_h),
                           (mean + 0.22, beam_y - tri_h)],
                          closed=True, facecolor=KANTO_YEL,
                          edgecolor=INK, lw=1.5, zorder=5))
    axd.annotate(f"balance point\n$E[X] = {mean:.2f}$",
                 xy=(mean, beam_y - tri_h), xytext=(mean + 1.2, 0.32),
                 ha="left", va="center", fontsize=11, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))

    axd.set_xlim(0, 6.2)
    axd.set_ylim(-0.42, 0.62)
    axd.set_title("Discrete prize: weighted blocks on a seesaw")
    axd.set_xlabel("prize value  $x$  (dollars)")
    axd.set_yticks([])
    axd.grid(False)

    # ---- Right: continuous density balanced under its mean ----------------
    x = np.linspace(0, 6, 600)
    # Skewed density (gamma-like) so the mean sits right of the peak.
    k, theta = 2.0, 1.0
    dens = (x ** (k - 1) * np.exp(-x / theta)) / (math.gamma(k) * theta ** k)
    cmean = k * theta  # = 2.0

    axc.plot(x, dens, color=KANTO_RED, lw=2.4, ls="-",
             label="density  $f(x)$", zorder=4)
    axc.fill_between(x, 0, dens, color=KANTO_RED, alpha=0.16, zorder=2)
    axc.axhline(0, color=INK, lw=2.5, zorder=3)

    axc.add_patch(Polygon([(cmean, 0), (cmean - 0.22, -0.045),
                           (cmean + 0.22, -0.045)],
                          closed=True, facecolor=KANTO_YEL,
                          edgecolor=INK, lw=1.5, zorder=5))
    axc.annotate(f"$E[X] = {cmean:.1f}$\n(center of mass)",
                 xy=(cmean, -0.045), xytext=(cmean + 1.3, 0.22),
                 ha="left", va="center", fontsize=11, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
    # Mark the peak (mode) to contrast with the mean.
    peak_x = x[np.argmax(dens)]
    axc.axvline(peak_x, color=KANTO_BLUE, lw=1.5, ls=":")
    axc.text(peak_x - 0.1, dens.max() * 0.92, "peak\n(mode)", ha="right",
             va="top", fontsize=9.5, color=KANTO_BLUE)

    axc.set_xlim(0, 6.2)
    axc.set_ylim(-0.12, dens.max() * 1.25)
    axc.set_title("Continuous density: balanced under the mean")
    axc.set_xlabel("value  $x$")
    axc.set_yticks([])
    axc.legend(loc="upper right")
    axc.grid(False)

    fig.suptitle("Expectation = the fulcrum that balances the probability",
                 fontsize=15, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return save(fig, "ch07_expectation_balance")


# --------------------------------------------------------------------------
# Concept 2 -- Jensen / LOTUS: averaging after bending vs bending the average.
#   g(x) = x^2; inputs 1 and 3 (each prob 1/2); E[X]=2.
#   E[X^2] = (1+9)/2 = 5 (average the OUTPUTS) vs g(E[X]) = 4 (map the mean).
#   Gap 5 - 4 = 1 = Var(X).
# --------------------------------------------------------------------------
def fig_jensen_lotus() -> Path:
    fig, ax = plt.subplots(figsize=(8.5, 6.2))

    x = np.linspace(0, 3.8, 400)
    ax.plot(x, x ** 2, color=INK, lw=2.4, label="$g(x) = x^2$", zorder=3)

    x1, x2, mu = 1.0, 3.0, 2.0
    y1, y2 = x1 ** 2, x2 ** 2          # 1, 9
    avg_out = (y1 + y2) / 2            # 5  = E[X^2]
    g_of_mu = mu ** 2                  # 4  = g(E[X])

    # Chord connecting the two output points -- its midpoint is the average output.
    ax.plot([x1, x2], [y1, y2], color=KANTO_BLUE, lw=2.0, ls="--",
            label="chord (averages the outputs)", zorder=4)

    # Input points on the axis.
    for xv in (x1, x2):
        ax.plot(xv, 0, "o", color=KANTO_GREEN, ms=9, zorder=5)
        ax.plot([xv, xv], [0, xv ** 2], color=KANTO_GREEN, lw=1.2, ls=":",
                zorder=2)
        ax.text(xv, -0.55, f"$x={int(xv)}$", ha="center", va="top",
                fontsize=11, color=INK)
    # Output points on the curve.
    for xv, yv in ((x1, y1), (x2, y2)):
        ax.plot(xv, yv, "o", color=INK, ms=8, zorder=6)
        ax.text(xv - 0.08, yv, f"  {int(yv)}", ha="right" if xv == x2 else "left",
                va="center", fontsize=10, color=INK)

    # E[X^2] = 5 : average of outputs (midpoint of chord), on the y-axis.
    ax.plot(mu, avg_out, "s", color=KANTO_RED, ms=11, zorder=7)
    ax.plot([0, mu], [avg_out, avg_out], color=KANTO_RED, lw=1.4, ls="--",
            zorder=3)
    ax.text(0.06, avg_out, "$E[X^2]=5$\n(average AFTER bending)", ha="left",
            va="bottom", fontsize=10.5, color=KANTO_RED, fontweight="bold")

    # g(E[X]) = 4 : map the mean input through g, on the curve.
    ax.plot(mu, g_of_mu, "D", color=KANTO_BLUE, ms=11, zorder=7)
    ax.plot([mu, mu], [0, g_of_mu], color=KANTO_BLUE, lw=1.2, ls=":", zorder=2)
    ax.plot([0, mu], [g_of_mu, g_of_mu], color=KANTO_BLUE, lw=1.4, ls=":",
            zorder=3)
    ax.text(mu + 0.07, -0.55, "$E[X]=2$", ha="left", va="top", fontsize=11,
            color=KANTO_BLUE)
    ax.text(0.06, g_of_mu - 0.15, "$g(E[X])=4$\n(bend the average — the trap)",
            ha="left", va="top", fontsize=10.5, color=KANTO_BLUE)

    # Gap bracket between 5 and 4 = Var(X).
    bx = mu + 0.55
    ax.annotate("", xy=(bx, avg_out), xytext=(bx, g_of_mu),
                arrowprops=dict(arrowstyle="<->", color=KANTO_GREEN, lw=2.0))
    ax.text(bx + 0.12, (avg_out + g_of_mu) / 2,
            "gap $= 5-4 = 1$\n$=\\mathrm{Var}(X)$", ha="left", va="center",
            fontsize=11, color=KANTO_GREEN, fontweight="bold")

    ax.set_xlim(0, 3.95)
    ax.set_ylim(-1.4, 10.5)
    ax.set_xlabel("input  $x$")
    ax.set_ylabel("output  $g(x)$")
    ax.set_title("Why $E[g(X)] \\neq g(E[X])$ when $g$ curves")
    ax.legend(loc="upper left")
    fig.tight_layout()
    return save(fig, "ch07_jensen_lotus")


# --------------------------------------------------------------------------
# Concept 3 -- Variance: same mean (2), different spread; squared-deviation
#   shading = Var(X). Side note: shift by b slides (spread unchanged);
#   scale by a stretches (spread x a^2).
# --------------------------------------------------------------------------
def fig_variance_spread() -> Path:
    fig = plt.figure(figsize=(11.5, 6.0))
    gs = fig.add_gridspec(2, 2, width_ratios=[2.1, 1.0], hspace=0.45,
                          wspace=0.28)
    ax_t = fig.add_subplot(gs[0, 0])
    ax_w = fig.add_subplot(gs[1, 0])
    ax_s = fig.add_subplot(gs[:, 1])

    mu = 2.0
    x = np.linspace(-3, 7, 800)

    def normal(xx, m, s):
        return np.exp(-0.5 * ((xx - m) / s) ** 2) / (s * math.sqrt(2 * math.pi))

    # Squared-deviation weight (x-mu)^2, scaled to overlay nicely.
    sq = (x - mu) ** 2

    for ax, sigma, title, col, hatch in (
        (ax_t, 0.7, "Small variance — tightly clustered (Var $= 0.49$)",
         KANTO_BLUE, "//"),
        (ax_w, 1.7, "Large variance — widely scattered (Var $= 2.89$)",
         KANTO_RED, "xx"),
    ):
        dens = normal(x, mu, sigma)
        # Density-weighted squared deviation: this is the integrand of Var(X).
        integrand = sq * dens
        ax.plot(x, dens, color=col, lw=2.3, label="density  $f(x)$", zorder=4)
        ax.fill_between(x, 0, integrand, color=col, alpha=0.30, hatch=hatch,
                        edgecolor=col, lw=0.0,
                        label="$(x-\\mu)^2 f(x)$  shaded", zorder=2)
        ax.axvline(mu, color=INK, lw=1.6, ls="--", zorder=3)
        ax.text(mu + 0.08, dens.max() * 0.96, "$\\mu = 2$", ha="left",
                va="top", fontsize=10.5, color=INK)
        var = sigma ** 2
        ax.text(0.985, 0.62,
                f"avg shaded area\n$= \\mathrm{{Var}}(X) = {var:.2f}$",
                transform=ax.transAxes, ha="right", va="top", fontsize=10,
                color=col, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=col,
                          alpha=0.9))
        ax.set_title(title, fontsize=12)
        ax.set_xlim(-3, 7)
        ax.set_ylim(0, max(dens.max(), integrand.max()) * 1.18)
        ax.set_yticks([])
        ax.legend(loc="upper left", fontsize=9)
    ax_w.set_xlabel("value  $x$")

    # ---- Side note: shift vs scale ----------------------------------------
    ax_s.set_title("Rescaling spread", fontsize=12)
    sigma0 = 1.0
    base = normal(x, mu, sigma0)
    # original
    ax_s.plot(x, base + 1.55, color=INK, lw=1.8, label="$X$")
    # shift by b: slides right, same width
    shifted = normal(x, mu + 2.0, sigma0)
    ax_s.plot(x, shifted + 0.85, color=KANTO_GREEN, lw=1.8, ls="--",
              label="$X+b$  (slides; spread same)")
    ax_s.annotate("", xy=(mu + 2.0, 1.18), xytext=(mu, 1.18),
                  arrowprops=dict(arrowstyle="->", color=KANTO_GREEN, lw=1.6))
    ax_s.text(mu + 1.0, 1.30, "$+b$", ha="center", va="bottom", fontsize=10,
              color=KANTO_GREEN)
    # scale by a: wider, spread x a^2
    scaled = normal(x, mu, sigma0 * 1.9)
    ax_s.plot(x, scaled + 0.05, color=KANTO_RED, lw=1.8, ls="-.",
              label="$aX$  (stretches; spread $\\times a^2$)")
    ax_s.annotate("", xy=(mu + 1.9, 0.30), xytext=(mu - 1.9, 0.30),
                  arrowprops=dict(arrowstyle="<->", color=KANTO_RED, lw=1.6))
    ax_s.text(mu, 0.36, "stretch", ha="center", va="bottom", fontsize=9.5,
              color=KANTO_RED)
    ax_s.set_xlim(-3, 7)
    ax_s.set_ylim(0, 2.5)
    ax_s.set_yticks([])
    ax_s.set_xlabel("value")
    ax_s.legend(loc="upper center", fontsize=8.3, bbox_to_anchor=(0.5, -0.12))

    fig.suptitle("Variance = average squared deviation about the mean",
                 fontsize=15, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return save(fig, "ch07_variance_spread")


# --------------------------------------------------------------------------
# Concept 4 -- MGF kernel reference table.
# --------------------------------------------------------------------------
def fig_mgf_kernels() -> Path:
    fig, ax = plt.subplots(figsize=(11.5, 6.0))
    ax.set_axis_off()

    cols_x = [0.02, 0.20, 0.50, 0.66, 0.83]
    headers = ["Family", "MGF kernel  $M_X(t)$", "Mean", "Variance",
               '"Read it off" slot']

    rows = [
        ("Gamma", r"$(1-\theta t)^{-\alpha}$", r"$\alpha\theta$",
         r"$\alpha\theta^{2}$", r"shape $\alpha$, scale $\theta$", KANTO_RED),
        ("Poisson", r"$e^{\lambda(e^{t}-1)}$", r"$\lambda$", r"$\lambda$",
         r"rate $\lambda$  (mean = var)", KANTO_BLUE),
        ("Binomial", r"$(1-p+pe^{t})^{n}$", r"$np$", r"$np(1-p)$",
         r"trials $n$, success $p$", KANTO_GREEN),
        ("Normal", r"$e^{\,\mu t+\sigma^{2}t^{2}/2}$", r"$\mu$",
         r"$\sigma^{2}$", r"$\mu$ linear, $\sigma^{2}$ quadratic", "#7B61FF"),
        ("Exponential", r"$(1-\theta t)^{-1}$", r"$\theta$", r"$\theta^{2}$",
         r"scale $\theta$  (Gamma, $\alpha=1$)", "#FF7043"),
    ]

    n = len(rows)
    top = 0.86
    bottom = 0.07
    row_h = (top - bottom) / n
    header_y = top + 0.045

    # Header row.
    ax.add_patch(FancyBboxPatch((0.0, top - 0.002), 1.0, header_y - top + 0.05,
                                boxstyle="round,pad=0.005",
                                transform=ax.transAxes, facecolor=INK,
                                edgecolor=INK, zorder=1))
    for cx, h in zip(cols_x, headers):
        ax.text(cx, header_y + 0.022, h, transform=ax.transAxes, ha="left",
                va="center", fontsize=11.5, color="white", fontweight="bold")

    # Data rows (zebra striping + a colored family tab).
    for i, (fam, mgf, mean, var, slot, col) in enumerate(rows):
        y0 = top - (i + 1) * row_h
        yc = y0 + row_h / 2
        if i % 2 == 0:
            ax.add_patch(Rectangle((0.0, y0), 1.0, row_h,
                                   transform=ax.transAxes, facecolor=KANTO_BG,
                                   edgecolor="none", zorder=0))
        # colored family tab on the left edge
        ax.add_patch(Rectangle((0.0, y0 + 0.01), 0.012, row_h - 0.02,
                               transform=ax.transAxes, facecolor=col,
                               edgecolor="none", zorder=2))
        ax.text(cols_x[0], yc, fam, transform=ax.transAxes, ha="left",
                va="center", fontsize=12, color=col, fontweight="bold")
        ax.text(cols_x[1], yc, mgf, transform=ax.transAxes, ha="left",
                va="center", fontsize=13.5, color=INK)
        ax.text(cols_x[2], yc, mean, transform=ax.transAxes, ha="left",
                va="center", fontsize=12.5, color=INK)
        ax.text(cols_x[3], yc, var, transform=ax.transAxes, ha="left",
                va="center", fontsize=12.5, color=INK)
        ax.text(cols_x[4], yc, slot, transform=ax.transAxes, ha="left",
                va="center", fontsize=10, color=INK)
        # row separator
        ax.axhline(y0, xmin=0.0, xmax=1.0, color="#D8D8D8", lw=0.8, zorder=1)

    # Column separators.
    for cx in cols_x[1:]:
        ax.plot([cx - 0.015, cx - 0.015], [bottom, top + 0.05],
                transform=ax.transAxes, color="#D8D8D8", lw=0.8, zorder=1)

    ax.text(0.5, 0.005,
            "Match the algebraic shape $\\rightarrow$ read parameters off the "
            "slot $\\rightarrow$ mean / variance follow, no calculus. "
            "Uniqueness guarantees the match.",
            transform=ax.transAxes, ha="center", va="top", fontsize=9.5,
            color="#555555", style="italic")

    ax.set_title("MGF kernel lookup table — recognize the shape, read the moments",
                 fontsize=15, pad=14)
    fig.tight_layout()
    return save(fig, "ch07_mgf_kernels")


# --------------------------------------------------------------------------
# Concept 5 -- Darth Vader rule: for X >= 0, area under S(x)=P(X>x) = E[X].
# --------------------------------------------------------------------------
def fig_survival_darthvader() -> Path:
    fig, ax = plt.subplots(figsize=(8.5, 5.2))

    theta = 10.0
    x = np.linspace(0, 45, 700)
    S = np.exp(-x / theta)  # exponential survival; area = theta = E[X]

    ax.fill_between(x, 0, S, color=KANTO_YEL, alpha=0.45, hatch="..",
                    edgecolor=KANTO_RED, lw=0.0, zorder=2,
                    label="shaded area $=\\int_0^\\infty S(x)\\,dx = E[X]$")
    ax.plot(x, S, color=KANTO_RED, lw=2.6, ls="-",
            label="survival  $S(x) = P(X>x)$", zorder=4)

    # Start height 1 at x = 0.
    ax.plot(0, 1, "o", color=KANTO_RED, ms=9, zorder=5)
    ax.annotate("$S(0) = 1$", xy=(0, 1), xytext=(3.0, 1.04), ha="left",
                va="center", fontsize=11, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    # Label the area = E[X] in the body of the shading.
    ax.text(8.5, 0.42, "area $= E[X]$", ha="center", va="center",
            fontsize=15, color=INK, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=KANTO_RED,
                      alpha=0.92))

    # Decay-toward-0 note.
    ax.annotate("decays toward $0$", xy=(38, math.exp(-38 / theta)),
                xytext=(28, 0.34), ha="left", va="center", fontsize=10.5,
                color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    ax.axhline(0, color=INK, lw=1.6, zorder=3)
    ax.set_xlim(0, 45)
    ax.set_ylim(0, 1.12)
    ax.set_xlabel("value  $x \\geq 0$")
    ax.set_ylabel("$P(X > x)$")
    ax.set_title("The Darth Vader rule: $E[X] = $ area under the survival curve")
    ax.text(0.985, 0.04, "requires  $X \\geq 0$", transform=ax.transAxes,
            ha="right", va="bottom", fontsize=10, color="#555555",
            style="italic",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#CCCCCC"))
    ax.legend(loc="upper right")
    fig.tight_layout()
    return save(fig, "ch07_survival_darthvader")


def main() -> None:
    print("Generating Chapter 7 figures ...")
    fig_expectation_balance()
    fig_jensen_lotus()
    fig_variance_spread()
    fig_mgf_kernels()
    fig_survival_darthvader()
    print("Done.")


if __name__ == "__main__":
    main()
