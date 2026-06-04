#!/usr/bin/env python3
"""Generate every Chapter 10 (Pricing / Loss Models) math figure.

Each of Chapter 10's nine-beat concept arcs closes on a "Picture it" beat whose
<figure> points at one purpose-built diagram. None existed yet; this script
renders EXACTLY the four filenames the chapter references, so picture and caption
agree:

  ch10_deductible_survival   Concept 1, Beat 8: the survival curve S(x)=e^{-x/4}
                             for Expo(4). A vertical line at d=2 splits the area:
                             the part LEFT of d (loss the trainer absorbs) vs the
                             shaded part RIGHT of d = E[(X-d)_+] = 4 e^{-1/2}
                             ~= 2.426. Whole area = E[X] = 4.
  ch10_limit_survival        Concept 2, Beat 8: the survival curve for Unif(0,10),
                             a straight ramp from (0,1) to (10,0). A vertical line
                             at u=8 splits the area: left region (0..8) shaded =
                             E[X wedge 8] = 4.8 (limited expected value); the small
                             triangular right region (8..10) = E[(X-8)_+] (excess).
                             Areas sum to E[X] = 5.
  ch10_payment_vs_loss       Concept 3, Beat 8: payment-vs-ground-up-loss step
                             graph. Flat 0 from X=0 to d=2; ramp of slope
                             alpha=0.8 from d=2 to u=10; flat cap at
                             alpha(u-d)=6.4 beyond u.
  ch10_perloss_vs_perpayment Concept 4, Beat 8: two stacked horizontal bars of the
                             same fled Pokemon. PER LOSS keeps the grey zero block
                             plus the paying flees -> averages low at 2.426.
                             PER PAYMENT deletes the zero block -> averages 4.
                             Arrow labelled "divide by S(d)=P(X>d)" connects them.

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element
ALSO carries a hatch / linestyle / direct label, so figures stay legible in
grayscale.

Run: python figures/src/gen_ch10.py
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
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
    KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN])

PRINT_DPI = 300


def save(fig, name: str) -> Path:
    path = OUT / f"{name}.png"
    fig.savefig(path, dpi=PRINT_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [fig] {path.relative_to(ROOT)}")
    return path


# --------------------------------------------------------------------------
# Concept 1, Beat 8 -- E[(X-d)_+] as the survival-curve area right of d.
# X ~ Expo(4): S(x) = e^{-x/4}; d = 2; right area = 4 e^{-1/2} ~= 2.426.
# --------------------------------------------------------------------------
def fig_deductible_survival() -> Path:
    fig, ax = plt.subplots(figsize=(8, 5))
    d = 2.0
    xmax = 20.0
    x = np.linspace(0, xmax, 800)
    S = np.exp(-x / 4.0)

    # Shade the RIGHT area (expected per-loss payment) with the red hatch.
    xr = x[x >= d]
    Sr = np.exp(-xr / 4.0)
    ax.fill_between(xr, 0, Sr, facecolor=KANTO_RED, alpha=0.30,
                    hatch="////", edgecolor=KANTO_RED, linewidth=0.0,
                    label=r"area right of $d$  =  $\mathrm{E}[(X-d)_+] = 4e^{-1/2}\approx 2.426$")
    # Shade the LEFT area (loss the trainer absorbs) in light grey dots.
    xl = x[x <= d]
    Sl = np.exp(-xl / 4.0)
    ax.fill_between(xl, 0, Sl, facecolor=KANTO_GRAY, alpha=0.30,
                    hatch="..", edgecolor=KANTO_GRAY, linewidth=0.0,
                    label="area left of $d$ (trainer absorbs)")

    ax.plot(x, S, color=KANTO_BLUE, linewidth=2.4,
            label=r"survival curve  $S(x)=e^{-x/4}$")

    # Vertical line at the deductible.
    ax.axvline(d, color=INK, linestyle="--", linewidth=1.6)
    ax.annotate(r"deductible $d=2$", xy=(d, 1.02), xytext=(d + 0.6, 1.04),
                fontsize=11, color=INK, va="bottom")

    # Whole-area note: integral from 0 to inf = E[X] = 4.
    ax.annotate(r"whole area under $S$  =  $\mathrm{E}[X]=4$",
                xy=(6.5, 0.30), fontsize=11, color=INK)

    ax.set_xlim(0, xmax)
    ax.set_ylim(0, 1.12)
    ax.set_xlabel("loss $x$ (thousands of Pokedollars)")
    ax.set_ylabel(r"$S(x)=P(X>x)$")
    ax.set_title("Deductible: expected payment is the survival area right of $d$")
    ax.legend(loc="upper right")
    return save(fig, "ch10_deductible_survival")


# --------------------------------------------------------------------------
# Concept 2, Beat 8 -- master identity as one picture.
# X ~ Unif(0,10): S(x) = 1 - x/10; u = 8.
# left area (0..8) = E[X wedge 8] = 4.8 ; right triangle (8..10) = E[(X-8)_+] ;
# total = E[X] = 5.
# --------------------------------------------------------------------------
def fig_limit_survival() -> Path:
    fig, ax = plt.subplots(figsize=(8, 5))
    u = 8.0
    x = np.linspace(0, 10, 400)
    S = 1.0 - x / 10.0

    xl = x[x <= u]
    Sl = 1.0 - xl / 10.0
    ax.fill_between(xl, 0, Sl, facecolor=KANTO_GREEN, alpha=0.30,
                    hatch="\\\\", edgecolor=KANTO_GREEN, linewidth=0.0,
                    label=r"left area  =  $\mathrm{E}[X\wedge 8] = 4.8$")
    xr = x[x >= u]
    Sr = 1.0 - xr / 10.0
    ax.fill_between(xr, 0, Sr, facecolor=KANTO_RED, alpha=0.35,
                    hatch="////", edgecolor=KANTO_RED, linewidth=0.0,
                    label=r"right area  =  $\mathrm{E}[(X-8)_+]$ (excess)")

    ax.plot(x, S, color=KANTO_BLUE, linewidth=2.4,
            label=r"survival curve  $S(x)=1-x/10$")

    ax.axvline(u, color=INK, linestyle="--", linewidth=1.6)
    ax.annotate(r"limit $u=8$", xy=(u, 1.02), xytext=(u - 2.6, 1.04),
                fontsize=11, color=INK, va="bottom")

    ax.annotate("left + right  =  $\\mathrm{E}[X]=5$",
                xy=(0.4, 0.18), fontsize=11, color=INK)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1.12)
    ax.set_xlabel("loss $x$ (thousands of Pokedollars)")
    ax.set_ylabel(r"$S(x)=P(X>x)$")
    ax.set_title("The master identity in one picture: $\\mathrm{E}[X\\wedge u]+\\mathrm{E}[(X-u)_+]=\\mathrm{E}[X]$")
    ax.legend(loc="upper right")
    return save(fig, "ch10_limit_survival")


# --------------------------------------------------------------------------
# Concept 3, Beat 8 -- payment vs ground-up loss step/ramp graph.
# d = 2, u = 10, alpha = 0.8; cap = alpha(u-d) = 6.4.
# --------------------------------------------------------------------------
def fig_payment_vs_loss() -> Path:
    fig, ax = plt.subplots(figsize=(8, 5))
    d, u, alpha = 2.0, 10.0, 0.8
    cap = alpha * (u - d)  # 6.4
    xmax = 14.0

    # Three regimes.
    x0 = np.array([0.0, d])
    y0 = np.array([0.0, 0.0])
    x1 = np.array([d, u])
    y1 = alpha * (x1 - d)
    x2 = np.array([u, xmax])
    y2 = np.array([cap, cap])

    ax.plot(x0, y0, color=KANTO_GRAY, linewidth=3.0, solid_capstyle="round",
            label="below $d$: payment $=0$")
    ax.plot(x1, y1, color=KANTO_BLUE, linewidth=3.0, solid_capstyle="round",
            label=r"layer: ramp of slope $\alpha=0.8$")
    ax.plot(x2, y2, color=KANTO_RED, linewidth=3.0, solid_capstyle="round",
            label=r"above $u$: capped at $\alpha(u-d)=6.4$")

    # Guides.
    ax.axvline(d, color=INK, linestyle=":", linewidth=1.2, alpha=0.8)
    ax.axvline(u, color=INK, linestyle=":", linewidth=1.2, alpha=0.8)
    ax.axhline(cap, color=INK, linestyle=":", linewidth=1.0, alpha=0.6)

    ax.annotate("$d=2$", xy=(d, -0.02), xytext=(d, -0.65),
                ha="center", fontsize=11, color=INK)
    ax.annotate("$u=10$", xy=(u, -0.02), xytext=(u, -0.65),
                ha="center", fontsize=11, color=INK)
    ax.annotate(r"cap $=\alpha(u-d)=6.4$", xy=(u, cap),
                xytext=(u + 0.3, cap - 1.0), fontsize=11, color=KANTO_RED)

    # Corner markers.
    ax.plot([d], [0.0], "o", color=KANTO_BLUE, markersize=7, zorder=5)
    ax.plot([u], [cap], "o", color=KANTO_RED, markersize=7, zorder=5)

    ax.set_xlim(0, xmax)
    ax.set_ylim(-0.8, 7.5)
    ax.set_xlabel("ground-up loss $X$ (thousands)")
    ax.set_ylabel("policy payment $Y_L$ (thousands)")
    ax.set_title(r"Payment vs. loss: $Y_L=\alpha[(X\wedge u)-(X\wedge d)]$")
    ax.legend(loc="upper left")
    return save(fig, "ch10_payment_vs_loss")


# --------------------------------------------------------------------------
# Concept 4, Beat 8 -- per loss vs per payment as two stacked bars.
# Per loss: zero block (losses below d) + paying flees -> avg 2.426.
# Per payment: delete zero block, average only paying flees -> avg 4.
# Connect with "divide by S(d)=P(X>d)" arrow. For Expo(4), d=2: S(d)=e^{-1/2}=0.6065.
# --------------------------------------------------------------------------
def fig_perloss_vs_perpayment() -> Path:
    fig, ax = plt.subplots(figsize=(8, 5))

    Sd = math.exp(-0.5)            # ~0.6065 = fraction of flees that pay
    zero_frac = 1.0 - Sd          # ~0.3935 = fraction paying 0
    total_w = 10.0                # bar drawn 0..10 in axis units
    pay_w = total_w * Sd          # paying portion width
    zero_w = total_w * zero_frac  # zero-payment portion width

    bar_h = 1.4
    y_top = 5.0     # PER LOSS bar baseline
    y_bot = 0.6     # PER PAYMENT bar baseline

    # --- TOP bar: PER LOSS = zero block (grey) + paying flees (blue) ---
    ax.add_patch(Rectangle((0, y_top), zero_w, bar_h, facecolor=KANTO_GRAY,
                           alpha=0.45, hatch="..", edgecolor=INK, linewidth=1.0))
    ax.add_patch(Rectangle((zero_w, y_top), pay_w, bar_h, facecolor=KANTO_BLUE,
                           alpha=0.40, hatch="////", edgecolor=INK, linewidth=1.0))
    ax.text(zero_w / 2, y_top + bar_h / 2, "zero-payment\nflees ($X\\leq d$)",
            ha="center", va="center", fontsize=10, color=INK)
    ax.text(zero_w + pay_w / 2, y_top + bar_h / 2, "paying flees",
            ha="center", va="center", fontsize=10, color=INK)
    ax.text(-0.3, y_top + bar_h / 2, "PER LOSS", ha="right", va="center",
            fontsize=12, fontweight="bold", color=INK)
    # average marker over the WHOLE top bar (pulled low) -- placed to the
    # LEFT of centre so it never collides with the per-payment label below.
    ax.annotate(r"average $=2.426$" + "\n(over all flees)",
                xy=(total_w * 0.5, y_top - 0.05),
                xytext=(total_w * 0.30, y_top - 1.2), ha="center",
                fontsize=10, color=KANTO_RED,
                arrowprops=dict(arrowstyle="-|>", color=KANTO_RED, lw=1.6))

    # --- BOTTOM bar: PER PAYMENT = paying flees only (zero block deleted) ---
    ax.add_patch(Rectangle((0, y_bot), pay_w, bar_h, facecolor=KANTO_BLUE,
                           alpha=0.40, hatch="////", edgecolor=INK, linewidth=1.0))
    # ghost where the deleted zero block used to be.
    ax.add_patch(Rectangle((pay_w, y_bot), zero_w, bar_h, facecolor="none",
                           edgecolor=KANTO_GRAY, linewidth=1.0, linestyle="--"))
    ax.text(pay_w + zero_w / 2, y_bot + bar_h / 2, "zeros\ndeleted",
            ha="center", va="center", fontsize=9, color=KANTO_GRAY, style="italic")
    ax.text(pay_w / 2, y_bot + bar_h / 2, "paying flees only",
            ha="center", va="center", fontsize=10, color=INK)
    ax.text(-0.3, y_bot + bar_h / 2, "PER PAYMENT", ha="right", va="center",
            fontsize=12, fontweight="bold", color=INK)
    ax.annotate(r"average $=4$" + "\n(over paid claims)",
                xy=(pay_w * 0.65, y_bot + bar_h + 0.05),
                xytext=(pay_w * 0.78, y_bot + bar_h + 1.05), ha="center",
                fontsize=10, color=KANTO_GREEN,
                arrowprops=dict(arrowstyle="-|>", color=KANTO_GREEN, lw=1.6))

    # --- connecting arrow: divide by S(d) ---
    arr = FancyArrowPatch((total_w + 0.7, y_top + bar_h / 2),
                          (total_w + 0.7, y_bot + bar_h / 2),
                          arrowstyle="-|>", mutation_scale=20,
                          color=KANTO_RED, lw=2.0)
    ax.add_patch(arr)
    ax.text(total_w + 1.0, (y_top + y_bot + bar_h) / 2,
            r"divide by" + "\n" + r"$S(d)=P(X>d)$",
            ha="left", va="center", fontsize=10, color=KANTO_RED)

    ax.set_xlim(-2.8, total_w + 4.2)
    ax.set_ylim(-0.4, y_top + bar_h + 0.8)
    ax.axis("off")
    ax.set_title("Per loss vs. per payment: delete the zeros, average rises")
    return save(fig, "ch10_perloss_vs_perpayment")


def main() -> None:
    print("Generating Chapter 10 figures ->", OUT)
    fig_deductible_survival()
    fig_limit_survival()
    fig_payment_vs_loss()
    fig_perloss_vs_perpayment()
    print("Done.")


if __name__ == "__main__":
    main()
