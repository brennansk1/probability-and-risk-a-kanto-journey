#!/usr/bin/env python3
"""Generate every Chapter 9 (Continuous Distributions / Saffron City) math figure.

Chapter 9 builds the five in-scope continuous families plus single-variable
transformations through nine-beat arcs. Each "Picture it" beat references one
purpose-built diagram. Previously the chapter reused three unrelated files
(ch07_normal_tails, ch09_joint_region, gamma_integrand), three of which were
semantically WRONG for their captions. This script renders EXACTLY the seven
filenames the revised chapter points at, so every picture matches its caption
and alt text:

  ch09_density_cdf        Concept 0, Beat 8: a generic smooth density with the
                          band (a,b) shaded = P(a<X<b); a second panel shows the
                          cdf F(x) as accumulated-area-from-the-left.

  ch09_uniform_rectangle  Concept 1, Beat 8: a FLAT density of height 1/(b-a) on
                          [2,10]; the sub-rectangle over (4,7) is shaded, area =
                          length ratio 3/8.

  ch09_exponential_decay  Concept 2, Beat 8: a decaying exponential density;
                          right tail beyond x shaded = S(x)=e^{-x/theta}; an inset
                          re-anchors the identical decaying shape at s
                          (memorylessness).

  ch09_gamma_family       Concept 3, Beat 8: right-skewed gamma densities; the
                          hump moves right / grows more symmetric as alpha rises;
                          alpha=1 is the pure-decay exponential.

  ch09_beta_family        Concept 4, Beat 8: several beta densities on [0,1] —
                          alpha<beta leans toward 0, alpha=beta symmetric,
                          alpha=beta=1 the flat Unif(0,1).

  ch09_normal_standardize Concept 5, Beat 8: the standard-normal bell; right tail
                          beyond z=1.5 shaded = 1-Phi(1.5); a band from z=-1 to
                          z=2 read as a difference of two Phi values.

  ch09_transform_sliver   Concept 6, Beat 8: two stacked densities linked by a
                          monotone map; a thin sliver of X-area maps to a sliver
                          of Y-area, rescaled by the Jacobian so areas match.

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element
ALSO carries a hatch / linestyle / direct label, so the figures stay legible in
grayscale.

Run: python figures/src/gen_ch09.py
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch  # noqa: F401

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
KANTO_PURPLE = "#7B61FF"  # Saffron / psychic accent
INK = "#333333"
DPI = 300


# ---------------------------------------------------------------------------
def fig_density_cdf():
    """Two panels: density with P(a<X<b) shaded, and the matching cdf F."""
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(12, 5.0))

    # a smooth, slightly skewed density (a gamma-ish hump) on [0, 10]
    x = np.linspace(0, 10, 800)
    f = (x ** 2) * np.exp(-x / 1.6)
    f /= np.trapz(f, x)  # normalize to area 1
    a, b = 2.0, 4.5

    axL.plot(x, f, color=KANTO_BLUE, lw=2.4, zorder=4)
    band = (x >= a) & (x <= b)
    axL.fill_between(x[band], f[band], color=KANTO_PURPLE, alpha=0.45,
                     hatch="//", edgecolor=INK, lw=0, zorder=3)
    axL.annotate(r"$P(a<X<b)=\int_a^b f\,dx$", xy=(3.0, 0.08),
                 xytext=(4.6, 0.20), fontsize=12.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
    axL.text(8.2, 0.05, r"total area $=1$", fontsize=11.5, color=KANTO_GRAY)
    for v, lab in ((a, "a"), (b, "b")):
        axL.axvline(v, color=INK, ls=":", lw=1.3, zorder=2)
        axL.text(v, -0.018, f"${lab}$", ha="center", va="top", fontsize=12,
                 color=INK)
    axL.set_xlabel(r"$x$")
    axL.set_ylabel(r"density  $f(x)$")
    axL.set_title("Probability is area under the density")
    axL.set_ylim(0, max(f) * 1.25)
    axL.grid(axis="x", visible=False)

    # cdf = running integral
    F = np.array([np.trapz(f[: i + 1], x[: i + 1]) for i in range(len(x))])
    axR.plot(x, F, color=KANTO_GREEN, lw=2.4, zorder=4)
    xc = 4.5
    Fc = np.interp(xc, x, F)
    axR.fill_between(x[x <= xc], F[x <= xc], color=KANTO_GREEN, alpha=0.18,
                     zorder=2)
    axR.plot([xc, xc], [0, Fc], color=INK, ls=":", lw=1.3, zorder=3)
    axR.plot([0, xc], [Fc, Fc], color=INK, ls=":", lw=1.3, zorder=3)
    axR.annotate(r"$F(x)=P(X\leq x)$" + "\n(area swept from the left)",
                 xy=(xc, Fc), xytext=(5.2, 0.45), fontsize=12, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
    axR.text(xc, -0.04, r"$x$", ha="center", va="top", fontsize=12, color=INK)
    axR.axhline(1.0, color=KANTO_GRAY, ls="--", lw=1.1)
    axR.text(0.3, 1.02, r"levels off at $1$", fontsize=11, color=KANTO_GRAY)
    axR.set_xlabel(r"$x$")
    axR.set_ylabel(r"cdf  $F(x)$")
    axR.set_title("The cdf accumulates that area")
    axR.set_ylim(0, 1.12)
    axR.grid(axis="x", visible=False)

    fig.suptitle("Density vs. cdf — two views of the same continuous law",
                 fontsize=15, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    out = OUT / "ch09_density_cdf.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
def fig_uniform_rectangle():
    """Flat density 1/(b-a) on [2,10]; sub-rectangle over (4,7) shaded = 3/8."""
    a, b = 2.0, 10.0
    h = 1.0 / (b - a)
    lo, hi = 4.0, 7.0

    fig, ax = plt.subplots(figsize=(10, 4.6))

    # whole rectangle
    ax.fill_between([a, b], [h, h], color=KANTO_BLUE, alpha=0.18, zorder=2)
    ax.plot([a, a, b, b], [0, h, h, 0], color=KANTO_BLUE, lw=2.4, zorder=4)
    # shaded band
    ax.fill_between([lo, hi], [h, h], color=KANTO_PURPLE, alpha=0.5,
                    hatch="//", edgecolor=INK, lw=0, zorder=3)

    ax.annotate(r"height $=\frac{1}{b-a}=\frac{1}{8}$", xy=(b, h),
                xytext=(7.4, h * 1.55), fontsize=12.5, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))
    ax.annotate(r"$P(4<X<7)=\frac{7-4}{10-2}=\frac{3}{8}$", xy=(5.5, h / 2),
                xytext=(5.0, h * 1.9), fontsize=13, color=KANTO_PURPLE,
                ha="center",
                arrowprops=dict(arrowstyle="->", color=KANTO_PURPLE, lw=1.5))

    for v in (a, lo, hi, b):
        ax.axvline(v, color=INK, ls=":", lw=1.0, ymax=0.66, zorder=1)
    ax.set_xticks([a, lo, hi, b])
    ax.set_xticklabels([r"$a=2$", "4", "7", r"$b=10$"])
    ax.set_yticks([0, h])
    ax.set_yticklabels(["0", r"$\frac{1}{8}$"])
    ax.set_xlabel(r"$x$  (Porygon's coordinate on the corridor)")
    ax.set_ylabel(r"density  $f(x)$")
    ax.set_title(r"Uniform$(2,10)$ — a flat rectangle; probability is a length ratio")
    ax.set_xlim(0.5, 11.5)
    ax.set_ylim(0, h * 2.25)
    ax.grid(False)

    fig.tight_layout()
    out = OUT / "ch09_uniform_rectangle.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
def fig_exponential_decay():
    """Decaying density, right tail beyond x shaded = S(x); inset re-anchors at s."""
    theta = 6.0
    x = np.linspace(0, 30, 800)
    f = (1.0 / theta) * np.exp(-x / theta)
    cut = 10.0

    fig, ax = plt.subplots(figsize=(10, 5.6))

    ax.plot(x, f, color=KANTO_RED, lw=2.4, zorder=4)
    tail = x >= cut
    ax.fill_between(x[tail], f[tail], color=KANTO_RED, alpha=0.35,
                    hatch="\\\\", edgecolor=INK, lw=0, zorder=3)
    ax.axvline(cut, color=INK, ls=":", lw=1.3, zorder=2)
    ax.annotate(r"right tail $=S(x)=e^{-x/\theta}$", xy=(15, 0.012),
                xytext=(15.5, 0.06), fontsize=12.5, color=KANTO_RED,
                arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.5))
    ax.text(cut, -0.006, r"$x$", ha="center", va="top", fontsize=12, color=INK)
    ax.set_xlabel(r"$t$  (waiting time, minutes)")
    ax.set_ylabel(r"density  $f(t)=\frac{1}{\theta}e^{-t/\theta}$")
    ax.set_title(r"Exponential$(\theta=6)$ — constant relative decay")
    ax.set_ylim(0, (1.0 / theta) * 1.12)
    ax.set_xlim(0, 30)
    ax.grid(axis="x", visible=False)

    # inset: re-anchor the identical shape at s -> memorylessness
    axin = ax.inset_axes([0.52, 0.42, 0.44, 0.5])
    s = 8.0
    xr = np.linspace(s, s + 22, 400)
    fr = (1.0 / theta) * np.exp(-(xr - s) / theta)  # fresh exponential from s
    axin.plot(xr, fr, color=KANTO_PURPLE, lw=2.0)
    axin.axvline(s, color=INK, ls=":", lw=1.1)
    axin.text(s, (1.0 / theta) * 1.02, r"$s$", ha="center", va="bottom",
              fontsize=10, color=INK)
    axin.set_title("re-anchored at $s$:\nthe identical shape", fontsize=9.5)
    axin.set_xticks([])
    axin.set_yticks([])
    axin.set_facecolor("#FFFFFF")

    fig.tight_layout()
    out = OUT / "ch09_exponential_decay.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
def gamma_pdf(x, alpha, theta):
    return (x ** (alpha - 1) * np.exp(-x / theta)
            / (math.gamma(alpha) * theta ** alpha))


def fig_gamma_family():
    """Right-skewed gamma densities; hump moves right with alpha; alpha=1 = expo."""
    theta = 2.0
    x = np.linspace(0.0001, 22, 900)
    fig, ax = plt.subplots(figsize=(10, 5.6))

    specs = [
        (1, KANTO_RED, "-", r"$\alpha=1$  (exponential — pure decay)"),
        (2, KANTO_YEL, "--", r"$\alpha=2$"),
        (3, KANTO_BLUE, "-.", r"$\alpha=3$  (gate opens on 3rd tick)"),
        (5, KANTO_GREEN, ":", r"$\alpha=5$  (taller, more symmetric)"),
    ]
    for alpha, c, ls, lab in specs:
        ax.plot(x, gamma_pdf(x, alpha, theta), color=c, lw=2.4, ls=ls,
                label=lab, zorder=4)
        # mark the hump (mode = (alpha-1)*theta for alpha>1)
        if alpha > 1:
            mode = (alpha - 1) * theta
            ax.plot(mode, gamma_pdf(mode, alpha, theta), "o", color=c,
                    markersize=6, zorder=5)

    ax.annotate("hump slides right and\ngrows more symmetric as $\\alpha$ rises",
                xy=(8, gamma_pdf(8, 5, theta)), xytext=(11, 0.18),
                fontsize=11.5, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3))
    ax.set_xlabel(r"$x$  (total waiting time)")
    ax.set_ylabel(r"density  $f(x)$")
    ax.set_title(r"Gamma$(\alpha,\ \theta=2)$ — a sum of $\alpha$ exponential waits")
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 0.5)
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper right")

    fig.tight_layout()
    out = OUT / "ch09_gamma_family.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
def beta_pdf(x, a, b):
    C = math.gamma(a + b) / (math.gamma(a) * math.gamma(b))
    return C * x ** (a - 1) * (1 - x) ** (b - 1)


def fig_beta_family():
    """Beta densities on [0,1]: lean-left, symmetric, and the flat uniform."""
    x = np.linspace(0.0001, 0.9999, 800)
    fig, ax = plt.subplots(figsize=(10, 5.6))

    specs = [
        (2, 3, KANTO_BLUE, "-", r"$\alpha=2,\ \beta=3$  (leans toward $0$, mean $0.4$)"),
        (3, 3, KANTO_GREEN, "--", r"$\alpha=\beta=3$  (symmetric, mean $0.5$)"),
        (1, 1, KANTO_RED, "-.", r"$\alpha=\beta=1$  (flat — Uniform$(0,1)$)"),
        (5, 2, KANTO_PURPLE, ":", r"$\alpha=5,\ \beta=2$  (leans toward $1$)"),
    ]
    for a, b, c, ls, lab in specs:
        ax.plot(x, beta_pdf(x, a, b), color=c, lw=2.4, ls=ls, label=lab,
                zorder=4)

    ax.axvline(0.5, color=KANTO_GRAY, ls=":", lw=1.1)
    ax.text(0.5, 2.55, r"$0.5$", ha="center", color=KANTO_GRAY, fontsize=10)
    ax.set_xlabel(r"$x$  (a random proportion)")
    ax.set_ylabel(r"density  $f(x)$")
    ax.set_title(r"Beta$(\alpha,\beta)$ — flexible shapes, all trapped on $[0,1]$")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 2.7)
    ax.grid(axis="x", visible=False)
    ax.legend(loc="upper center", fontsize=10)

    fig.tight_layout()
    out = OUT / "ch09_beta_family.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
def fig_normal_standardize():
    """Standard normal: right tail beyond z=1.5 shaded; band z=-1..2 as a difference."""
    z = np.linspace(-4, 4, 800)
    phi = np.exp(-z ** 2 / 2) / math.sqrt(2 * math.pi)

    fig, (axL, axR) = plt.subplots(1, 2, figsize=(12, 5.0), sharey=True)

    # Left: right tail beyond z = 1.5
    axL.plot(z, phi, color=KANTO_BLUE, lw=2.4, zorder=4)
    tail = z >= 1.5
    axL.fill_between(z[tail], phi[tail], color=KANTO_RED, alpha=0.45,
                     hatch="//", edgecolor=INK, lw=0, zorder=3)
    axL.axvline(1.5, color=INK, ls=":", lw=1.3)
    axL.annotate(r"$P(Z>1.5)=1-\Phi(1.5)=0.0668$", xy=(2.0, 0.02),
                 xytext=(0.1, 0.30), fontsize=11.5, color=KANTO_RED,
                 arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.4))
    axL.text(1.5, -0.02, r"$z=1.5$", ha="center", va="top", fontsize=11,
             color=INK)
    axL.set_xlabel(r"$z$")
    axL.set_ylabel(r"density  $\varphi(z)$")
    axL.set_title("A right tail is $1-\\Phi(z)$")
    axL.set_ylim(0, 0.46)
    axL.grid(axis="x", visible=False)

    # Right: band z = -1 .. 2 as Phi(2) - Phi(-1)
    axR.plot(z, phi, color=KANTO_BLUE, lw=2.4, zorder=4)
    band = (z >= -1) & (z <= 2)
    axR.fill_between(z[band], phi[band], color=KANTO_GREEN, alpha=0.35,
                     hatch="\\\\", edgecolor=INK, lw=0, zorder=3)
    for v in (-1, 2):
        axR.axvline(v, color=INK, ls=":", lw=1.3)
    axR.annotate(r"$\Phi(2)-\Phi(-1)=0.8185$", xy=(0.3, 0.18),
                 xytext=(-3.7, 0.33), fontsize=11.5, color="#2c6e36",
                 arrowprops=dict(arrowstyle="->", color="#2c6e36", lw=1.4))
    axR.text(-1, -0.02, r"$z=-1$", ha="center", va="top", fontsize=11,
             color=INK)
    axR.text(2, -0.02, r"$z=2$", ha="center", va="top", fontsize=11, color=INK)
    axR.set_xlabel(r"$z$")
    axR.set_title("A band is $\\Phi(z_2)-\\Phi(z_1)$")
    axR.grid(axis="x", visible=False)

    fig.suptitle(r"Standardize, then read the $\Phi$ table (left-area)",
                 fontsize=15, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    out = OUT / "ch09_normal_standardize.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
def fig_transform_sliver():
    """Two stacked densities linked by a monotone map; equal-area slivers (Jacobian)."""
    # X ~ Unif(0,1), Y = -4 ln X  ->  Y ~ Expo(4). Monotone-decreasing map.
    fig = plt.figure(figsize=(9.5, 8.5))
    gs = fig.add_gridspec(2, 2, width_ratios=[1, 2.4], height_ratios=[2.4, 1],
                          wspace=0.08, hspace=0.08)

    ax_map = fig.add_subplot(gs[0, 1])   # the transformation curve y = g(x)
    ax_fy = fig.add_subplot(gs[0, 0], sharey=ax_map)  # Y density (vertical)
    ax_fx = fig.add_subplot(gs[1, 1], sharex=ax_map)  # X density (horizontal)

    x = np.linspace(0.001, 1, 500)
    y = -4 * np.log(x)               # monotone decreasing
    YMAX = 16

    # --- transformation curve ---
    ax_map.plot(x, y, color=KANTO_PURPLE, lw=2.6, zorder=4)
    # a thin sliver in x maps to a sliver in y
    x0, dx = 0.30, 0.05
    y_hi = -4 * np.log(x0)
    y_lo = -4 * np.log(x0 + dx)
    ax_map.axvspan(x0, x0 + dx, color=KANTO_BLUE, alpha=0.30, zorder=2)
    ax_map.axhspan(y_lo, y_hi, color=KANTO_RED, alpha=0.30, zorder=2)
    ax_map.annotate("a thin $x$-sliver maps\nto a $y$-sliver", xy=(x0, y_hi),
                    xytext=(0.42, 11), fontsize=10.5, color=INK,
                    arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))
    ax_map.set_title(r"monotone map  $y=g(x)=-4\ln x$", fontsize=12)
    ax_map.set_ylim(0, YMAX)
    ax_map.set_xlim(0, 1)
    ax_map.tick_params(labelleft=False, labelbottom=False)
    ax_map.grid(False)

    # --- X density (Unif(0,1)): flat height 1, drawn below, sliver highlighted ---
    fx = np.ones_like(x)
    ax_fx.plot(x, fx, color=KANTO_BLUE, lw=2.4)
    ax_fx.fill_between([x0, x0 + dx], [1, 1], color=KANTO_BLUE, alpha=0.5,
                       hatch="//", edgecolor=INK, lw=0)
    ax_fx.set_ylim(1.5, 0)  # inverted so the density hangs under the map
    ax_fx.set_xlabel(r"$x$  ($X\sim$ Uniform$(0,1)$, height $1$)")
    ax_fx.set_ylabel(r"$f_X$")
    ax_fx.grid(False)

    # --- Y density (Expo(4)): drawn at left, rotated, sliver highlighted ---
    yy = np.linspace(0.001, YMAX, 400)
    fy = 0.25 * np.exp(-yy / 4)
    ax_fy.plot(fy, yy, color=KANTO_RED, lw=2.4)
    ys = (yy >= y_lo) & (yy <= y_hi)
    ax_fy.fill_betweenx(yy[ys], fy[ys], color=KANTO_RED, alpha=0.5,
                        hatch="\\\\", edgecolor=INK, lw=0)
    ax_fy.set_xlim(0.27, 0)  # inverted so density opens toward the map
    ax_fy.set_ylabel(r"$y$  ($Y=-4\ln X\sim$ Exponential$(4)$)")
    ax_fy.set_xlabel(r"$f_Y$")
    ax_fy.grid(False)

    fig.suptitle("Probability is conserved: the Jacobian rescales each sliver\n"
                 r"$f_Y(y)=f_X(x)\,\left|dx/dy\right|$ keeps the two slivers' areas equal",
                 fontsize=13, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    out = OUT / "ch09_transform_sliver.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
def main():
    written = [
        fig_density_cdf(),
        fig_uniform_rectangle(),
        fig_exponential_decay(),
        fig_gamma_family(),
        fig_beta_family(),
        fig_normal_standardize(),
        fig_transform_sliver(),
    ]
    for w in written:
        print(w)


if __name__ == "__main__":
    main()
