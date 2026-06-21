#!/usr/bin/env python3
"""Generate every Chapter 12 (Normal & the Central Limit Theorem) figure.

Manifest (MASTER_PLAN_V3 §16) — four required diagrams, all into assets/diagrams/:
  ch12_normal_6895997        the 68-95-99.7 rule on the standard bell
  ch12_standardize           sliding/scaling any N(mu,sigma^2) onto the one Z table
  ch12_clt_convergence       sample mean of Unif(0,1) draws -> normal as n grows
  ch12_continuity_correction binomial bars + overlaid normal, the +-0.5 half-unit fix

LOCALE: a vast trainer gathering / League qualifier (the §15 normal/no-badge chapter).
ACCENT: type_palette.chapter_accent(12) -> Normal #A8A878.

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe; every color-coded element is ALSO
distinguished by a hatch / text label so figures survive grayscale (color is never
the sole channel). Sprites obey the IRON RULE: art in margins, never over a curve,
equation, axis, or number a reader must read.

Run: python figures/src/gen_ch12.py
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
NORMAL = chapter_accent(12)  # §17 Normal accent (banner/accent parity) = #A8A878
INK = "#333333"

plt.rcParams["axes.prop_cycle"] = cycler(color=[
    KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN,
    "#FF7043", "#7B61FF", "#00BCD4", "#FF4081", "#8D6E63", "#78909C"])

PRINT_DPI = 300

# A reproducible RNG (seed 151 = the Kanto Pokedex count) for the CLT panel.
RNG = np.random.default_rng(151)


def save(fig, name: str) -> Path:
    path = OUT / f"{name}.png"
    fig.savefig(path, dpi=PRINT_DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  [fig] {path.relative_to(ROOT)}")
    return path


def _blank(ax):
    """Strip a panel to a clean drawing surface (no grid/ticks/spines)."""
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_facecolor("white")
    ax.grid(False)


def _std_normal(x):
    return np.exp(-x ** 2 / 2.0) / np.sqrt(2 * np.pi)


# --------------------------------------------------------------------------
# 1. ch12_normal_6895997 — the 68-95-99.7 rule on the standard bell.
# --------------------------------------------------------------------------
def fig_6895997():
    fig, ax = plt.subplots(figsize=(11, 6.2))
    ax.set_facecolor("white")
    x = np.linspace(-4, 4, 1000)
    y = _std_normal(x)
    ax.plot(x, y, color=INK, lw=2.2, zorder=5)

    # Nested bands: within 3 sigma (lightest), 2 sigma, 1 sigma (darkest).
    bands = [
        (3, "#E8E4D0", "99.7%", "..", 0.7),
        (2, "#CFC79A", "95%", "//", 0.85),
        (1, NORMAL, "68%", "xx", 0.9),
    ]
    for k, fc, lab, hatch, a in bands:
        xb = np.linspace(-k, k, 400)
        ax.fill_between(xb, _std_normal(xb), color=fc, alpha=a, hatch=hatch,
                        edgecolor="white", lw=0.0, zorder=2)

    # sigma gridlines + labels.
    for k in (-3, -2, -1, 0, 1, 2, 3):
        ax.plot([k, k], [0, _std_normal(k)], color=INK, lw=0.9, ls=":",
                alpha=0.7, zorder=4)
    ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
    ax.set_xticklabels([r"$\mu-3\sigma$", r"$\mu-2\sigma$", r"$\mu-\sigma$",
                        r"$\mu$", r"$\mu+\sigma$", r"$\mu+2\sigma$",
                        r"$\mu+3\sigma$"], fontsize=10)
    ax.set_yticks([])
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)

    # Percent callouts inside each band, stacked so they never overlap the curve.
    ax.text(0, 0.165, "68%", ha="center", fontsize=13, fontweight="bold",
            color=INK)
    ax.text(0, 0.055, "95%", ha="center", fontsize=12, fontweight="bold",
            color=INK)
    ax.annotate("99.7%", xy=(2.55, 0.012), xytext=(3.3, 0.10),
                fontsize=11, fontweight="bold", color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.2))

    ax.set_title("The 68-95-99.7 rule: how much mass lives within "
                 r"$1,2,3$ standard deviations", fontsize=13)
    ax.set_xlim(-4.2, 4.2)
    ax.set_ylim(0, 0.46)

    # decorative Clefairy (Mt. Moon bell mascot) in the top-left margin.
    place_sprite(ax, front(35), (-3.6, 0.40), zoom=0.30, alpha=0.92, zorder=6)
    ax.text(0, 0.43, "every normal, relabeled to the same bell",
            ha="center", fontsize=9.5, style="italic", color=KANTO_GRAY)
    fig.tight_layout()
    return save(fig, "ch12_normal_6895997")


# --------------------------------------------------------------------------
# 2. ch12_standardize — slide-and-scale any N(mu,sigma^2) onto the Z table.
# --------------------------------------------------------------------------
def fig_standardize():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 5.4))

    # LEFT: a raw N(50, 8^2) with x = 62 marked, right tail shaded.
    mu, sig = 50.0, 8.0
    xs = np.linspace(mu - 4 * sig, mu + 4 * sig, 800)
    ys = _std_normal((xs - mu) / sig) / sig
    ax1.plot(xs, ys, color=KANTO_BLUE, lw=2.2)
    tail = xs >= 62
    ax1.fill_between(xs[tail], ys[tail], color=KANTO_BLUE, alpha=0.45,
                     hatch="//", edgecolor="white")
    ax1.axvline(62, color=INK, lw=1.0, ls=":")
    ax1.axvline(mu, color=INK, lw=0.8, ls="--", alpha=0.6)
    ax1.set_title(r"raw scale: $X\sim\mathcal{N}(50,\,8^2)$", fontsize=12)
    ax1.set_xticks([mu - sig, mu, 62, mu + 2 * sig])
    ax1.set_xticklabels(["42", "50", "62", "66"], fontsize=9)
    ax1.set_yticks([])
    ax1.text(70, ys.max() * 0.45, r"$P(X>62)$", fontsize=11, color=KANTO_BLUE,
             fontweight="bold")
    for s in ("top", "right", "left"):
        ax1.spines[s].set_visible(False)

    # CENTER arrow between panels.
    fig.text(0.5, 0.55, r"$Z=\dfrac{X-\mu}{\sigma}=\dfrac{62-50}{8}=1.5$",
             ha="center", fontsize=12.5, color=KANTO_GREEN, fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.3", fc="#E8F5E9", ec=KANTO_GREEN,
                       lw=1.4))
    fig.text(0.5, 0.44, "subtract the mean,\nthen divide by the SD",
             ha="center", fontsize=8.5, style="italic", color=KANTO_GRAY)

    # RIGHT: the standard N(0,1) with z = 1.5 marked, same tail.
    zs = np.linspace(-4, 4, 800)
    zy = _std_normal(zs)
    ax2.plot(zs, zy, color=INK, lw=2.2)
    ztail = zs >= 1.5
    ax2.fill_between(zs[ztail], zy[ztail], color=NORMAL, alpha=0.85, hatch="//",
                     edgecolor="white")
    ax2.axvline(1.5, color=INK, lw=1.0, ls=":")
    ax2.axvline(0, color=INK, lw=0.8, ls="--", alpha=0.6)
    ax2.set_title(r"standard scale: $Z\sim\mathcal{N}(0,1)$", fontsize=12)
    ax2.set_xticks([-1, 0, 1.5, 2])
    ax2.set_xticklabels(["-1", "0", "1.5", "2"], fontsize=9)
    ax2.set_yticks([])
    ax2.annotate(r"$1-\Phi(1.5)$" "\n" r"$=1-0.9332$" "\n" r"$=0.0668$",
                 xy=(1.9, 0.03), xytext=(2.4, 0.18), fontsize=10,
                 color=INK, fontweight="bold",
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.1))
    for s in ("top", "right", "left"):
        ax2.spines[s].set_visible(False)

    fig.suptitle("Standardizing: every normal probability is one $\\Phi$ "
                 "table lookup", fontsize=13.5, y=1.00)
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    return save(fig, "ch12_standardize")


# --------------------------------------------------------------------------
# 3. ch12_clt_convergence — sample mean of Unif(0,1) goes normal as n grows.
# --------------------------------------------------------------------------
def fig_clt_convergence():
    fig, axes = plt.subplots(1, 4, figsize=(14, 3.8), sharey=False)
    ns = [1, 2, 5, 30]
    reps = 60000
    for ax, n in zip(axes, ns):
        means = RNG.uniform(0, 1, size=(reps, n)).mean(axis=1)
        ax.hist(means, bins=45, range=(0, 1), density=True, color=NORMAL,
                edgecolor="white", lw=0.3, alpha=0.9)
        # overlay the CLT normal: mean 0.5, var (1/12)/n.
        mu, var = 0.5, (1 / 12) / n
        sd = np.sqrt(var)
        gx = np.linspace(0, 1, 400)
        gy = _std_normal((gx - mu) / sd) / sd
        ax.plot(gx, gy, color=KANTO_RED, lw=2.0)
        ax.set_title(f"$n={n}$", fontsize=12)
        ax.set_xticks([0, 0.5, 1])
        ax.set_yticks([])
        for s in ("top", "right", "left"):
            ax.spines[s].set_visible(False)
    axes[0].text(0.5, 0.5, "flat\n(uniform)", ha="center", va="center",
                 fontsize=8.5, color=INK, transform=axes[0].transAxes)
    axes[-1].text(0.97, 0.95, "normal\ncurve", ha="right", va="top",
                  fontsize=8.5, color=KANTO_RED, fontweight="bold",
                  transform=axes[-1].transAxes)
    fig.suptitle("The Central Limit Theorem: the sample mean of "
                 r"$\mathrm{Unif}(0,1)$ draws goes bell-shaped (and narrows) "
                 "as $n$ grows", fontsize=13, y=1.04)
    fig.tight_layout()
    return save(fig, "ch12_clt_convergence")


# --------------------------------------------------------------------------
# 4. ch12_continuity_correction — binomial bars + overlaid normal, the +-0.5 fix.
# --------------------------------------------------------------------------
def fig_continuity_correction():
    from scipy.stats import binom

    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    ax.set_facecolor("white")
    n, p = 400, 0.4
    mu, sig = n * p, np.sqrt(n * p * (1 - p))  # 160, sqrt(96) ~ 9.80

    ks = np.arange(135, 190)
    pmf = binom.pmf(ks, n, p)
    # bars below 180 = light; bars at/above 180 = shaded (the event).
    for k, pk in zip(ks, pmf):
        shaded = k >= 180
        ax.add_patch(Rectangle((k - 0.5, 0), 1.0, pk,
                               facecolor=KANTO_RED if shaded else NORMAL,
                               edgecolor="white", lw=0.5,
                               alpha=0.9 if shaded else 0.55,
                               hatch="xx" if shaded else None, zorder=2))

    # overlaid normal approximation.
    gx = np.linspace(135, 190, 600)
    gy = _std_normal((gx - mu) / sig) / sig
    ax.plot(gx, gy, color=INK, lw=2.2, zorder=5)

    # the corrected boundary at 179.5 (left edge of the 180 bar).
    ax.axvline(179.5, color=KANTO_GREEN, lw=2.0, ls="--", zorder=6)
    ax.annotate("correct boundary\n179.5  (left edge\nof the 180 bar)",
                xy=(179.5, 0.018), xytext=(165, 0.030), fontsize=9.5,
                color=KANTO_GREEN, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=KANTO_GREEN, lw=1.4))
    ax.axvline(180, color=KANTO_GRAY, lw=1.2, ls=":", zorder=6)
    ax.annotate("naive 180\nslices the bar\nin half", xy=(180, 0.006),
                xytext=(183.5, 0.022), fontsize=8.5, color=KANTO_GRAY,
                arrowprops=dict(arrowstyle="->", color=KANTO_GRAY, lw=1.1))

    ax.set_title(r"Continuity correction: $X\sim\mathrm{Bin}(400,0.4)$, "
                 r"$P(X\geq 180)$ starts the normal area at $179.5$",
                 fontsize=12.5)
    ax.set_xlabel("number of wins $k$", fontsize=10)
    ax.set_xlim(150, 190)
    ax.set_ylim(0, 0.046)
    ax.set_yticks([])
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)

    ax.text(170, 0.041,
            r"$z=\dfrac{179.5-160}{\sqrt{96}}\approx 1.99,\quad "
            r"P(X\geq 180)\approx 1-\Phi(1.99)=0.0233$",
            ha="center", fontsize=11, color=INK, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="#E8F5E9", ec=KANTO_GREEN,
                      lw=1.4))
    fig.tight_layout()
    return save(fig, "ch12_continuity_correction")


REGISTRY = [
    fig_6895997,
    fig_standardize,
    fig_clt_convergence,
    fig_continuity_correction,
]


def main() -> None:
    print(f"Generating Chapter 12 (Normal & CLT) figures -> {OUT} "
          f"at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
