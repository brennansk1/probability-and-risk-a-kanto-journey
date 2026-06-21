#!/usr/bin/env python3
"""Generate every Chapter 12 (Normal & the Central Limit Theorem / the Grand
Gathering / Indigo League crowd / Normal type) figure.

Manifest (DESIGN_BLUEPRINT ch12 row · MASTER_PLAN_V3 §16, §30) — five diagrams
into assets/diagrams/:
  ch12_normal_6895997        the bell + the 68-95-99.7 rule (Clefairy #35)
  ch12_standardize           shifting/scaling any normal to the standard Z
  ch12_clt_convergence       many mixed real sprites averaging into a bell
  ch12_continuity_correction the staircase pmf overlaid by the smooth normal,
                             showing WHY the +/-0.5 half-step is added
  ch12_lognormal             ENRICHMENT: e^(normal) -> right-skewed (Gyarados #130)

PRINT TARGET: bound book, every PNG rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is
ALSO distinguished by a hatch pattern / text label so figures survive grayscale.
Real sprites obey the IRON RULE: art lives in margins / atop bars / beside labels,
never over a curve, equation, axis, or number a reader must read. Sprite art is
REAL (assets/sprites/front/*.png) and is only ever COMPOSITED, never generated.

Run: python3 figures/src/gen_ch12.py
"""
from __future__ import annotations

from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from cycler import cycler
from scipy import stats

from sprite_util import front, place_sprite
from type_palette import chapter_accent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents). ch12 = Normal type, so the
# accent is the §17 normal color via chapter_accent(12).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
ACCENT = chapter_accent(12)  # normal #A8A878
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


def _clean(ax):
    ax.set_facecolor("white")
    ax.grid(False)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def _blank(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_facecolor("white")
    ax.grid(False)


# --------------------------------------------------------------------------
# 1. ch12_normal_6895997 — the bell + the 68-95-99.7 rule. (Concept 1)
# --------------------------------------------------------------------------
def fig_normal_6895997():
    fig, ax = plt.subplots(figsize=(11, 6.2))
    _clean(ax)
    x = np.linspace(-4, 4, 800)
    y = stats.norm.pdf(x)
    ax.plot(x, y, color=INK, lw=2.4, zorder=5)

    # Nested 1/2/3-sigma bands, each its own hatch so grayscale survives.
    bands = [
        (1, KANTO_GREEN, "....", "68%"),
        (2, KANTO_YEL, "//", "95%"),
        (3, KANTO_RED, "xx", "99.7%"),
    ]
    # Paint widest first so narrower bands sit on top.
    for k, color, hatch, _ in reversed(bands):
        xb = np.linspace(-k, k, 400)
        ax.fill_between(xb, stats.norm.pdf(xb), color=color, alpha=0.30,
                        hatch=hatch, edgecolor=color, lw=0.0, zorder=2)

    # sigma gridlines + axis ticks at mu +/- k*sigma.
    for k in range(-3, 4):
        ax.axvline(k, color=KANTO_GRAY, lw=0.8, ls=":", zorder=1)
    ax.set_xticks(range(-3, 4))
    ax.set_xticklabels([r"$\mu-3\sigma$", r"$\mu-2\sigma$", r"$\mu-\sigma$",
                        r"$\mu$", r"$\mu+\sigma$", r"$\mu+2\sigma$",
                        r"$\mu+3\sigma$"], fontsize=9)
    ax.set_yticks([])
    ax.set_ylim(0, 0.46)
    ax.set_xlim(-4, 4)

    # The three coverage call-outs, stacked, none over the curve apex.
    ax.annotate("68% within $\\pm 1\\sigma$", xy=(0, 0.12), xytext=(0, 0.135),
                ha="center", fontsize=11, color="#2e7d32", fontweight="bold")
    ax.annotate("95% within $\\pm 2\\sigma$", xy=(1.5, 0.04),
                xytext=(2.05, 0.255), ha="center", fontsize=10.5,
                color="#9a7d00", fontweight="bold",
                arrowprops=dict(arrowstyle="->", color="#9a7d00", lw=1.4))
    ax.annotate("99.7% within $\\pm 3\\sigma$", xy=(-2.5, 0.012),
                xytext=(-2.4, 0.30), ha="center", fontsize=10.5,
                color=KANTO_RED, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.4))

    ax.set_title("The bell and the 68-95-99.7 rule\n"
                 r"$X\sim N(\mu,\sigma^2)$: area within $k$ standard deviations of the mean",
                 fontsize=13.5)
    ax.set_xlabel("value of $X$ (in standard deviations from the mean)",
                  fontsize=10)

    # Real Clefairy sprite decorates the upper-left margin (clear of curve/labels).
    place_sprite(ax, front(35), (-3.5, 0.40), zoom=0.42, alpha=0.95, zorder=6)
    ax.text(-3.5, 0.335, "#35 Clefairy", ha="center", fontsize=8,
            color=INK)
    fig.tight_layout()
    return save(fig, "ch12_normal_6895997")


# --------------------------------------------------------------------------
# 2. ch12_standardize — shift then scale any normal to the standard Z. (Concept 1)
# --------------------------------------------------------------------------
def fig_standardize():
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.4))
    mu, sigma = 50.0, 8.0

    # left: the raw N(50, 8^2)
    axL = axes[0]
    _clean(axL)
    x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 600)
    axL.plot(x, stats.norm.pdf(x, mu, sigma), color=KANTO_BLUE, lw=2.4)
    # shade X <= 62 (a worked point: z = (62-50)/8 = 1.5)
    xs = np.linspace(mu - 4 * sigma, 62, 400)
    axL.fill_between(xs, stats.norm.pdf(xs, mu, sigma), color=KANTO_BLUE,
                     alpha=0.28, hatch="//", edgecolor=KANTO_BLUE, lw=0.0)
    axL.axvline(62, color=KANTO_RED, lw=1.6, ls="--")
    axL.axvline(mu, color=KANTO_GRAY, lw=1.0, ls=":")
    axL.text(62, stats.norm.pdf(62, mu, sigma) + 0.004, "$x=62$", ha="center",
             color=KANTO_RED, fontsize=10, fontweight="bold")
    axL.set_title(r"Raw score: $X\sim N(\mu=50,\ \sigma=8)$", fontsize=12)
    axL.set_xlabel("battle-points $X$", fontsize=10)
    axL.set_yticks([])
    axL.set_xticks([mu - 2 * sigma, mu, 62, mu + 2 * sigma])

    # right: the standard N(0,1)
    axR = axes[1]
    _clean(axR)
    z = np.linspace(-4, 4, 600)
    axR.plot(z, stats.norm.pdf(z), color=ACCENT, lw=2.6)
    zs = np.linspace(-4, 1.5, 400)
    axR.fill_between(zs, stats.norm.pdf(zs), color=ACCENT, alpha=0.40,
                     hatch="//", edgecolor=ACCENT, lw=0.0)
    axR.axvline(1.5, color=KANTO_RED, lw=1.6, ls="--")
    axR.axvline(0, color=KANTO_GRAY, lw=1.0, ls=":")
    axR.text(1.5, stats.norm.pdf(1.5) + 0.012, "$z=1.5$", ha="center",
             color=KANTO_RED, fontsize=10, fontweight="bold")
    axR.set_title(r"Standardized: $Z=\dfrac{X-\mu}{\sigma}\sim N(0,1)$",
                  fontsize=12)
    axR.set_xlabel("standard units $Z$", fontsize=10)
    axR.set_yticks([])
    axR.set_xticks(range(-3, 4))

    # The transformation arrow + the same-area message, between panels.
    fig.text(0.5, 0.52, r"$z=\dfrac{62-50}{8}=1.5$", ha="center",
             fontsize=13, color=INK, fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.3", fc="#FFF6D6", ec=KANTO_YEL,
                       lw=1.4))
    fig.text(0.5, 0.40, "same shaded\narea", ha="center", fontsize=9,
             color=KANTO_GREEN, fontweight="bold", style="italic")
    arrow = FancyArrowPatch((0.455, 0.46), (0.545, 0.46),
                            transform=fig.transFigure,
                            arrowstyle="-|>", mutation_scale=22,
                            color=KANTO_GREEN, lw=2.2)
    fig.patches.append(arrow)

    fig.suptitle("Standardizing: slide by $\\mu$, squeeze by $\\sigma$ - "
                 "the shaded probability never changes", fontsize=13.5,
                 y=1.02)
    # Clefairy in left margin of left panel.
    place_sprite(axL, front(35), (mu - 3.4 * sigma, stats.norm.pdf(mu, mu, sigma)
                                  * 0.92), zoom=0.34, alpha=0.95, zorder=6)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    return save(fig, "ch12_standardize")


# --------------------------------------------------------------------------
# 3. ch12_clt_convergence — averaging many non-normal results -> a bell. (Concept 3)
# --------------------------------------------------------------------------
def fig_clt_convergence():
    fig, axes = plt.subplots(1, 3, figsize=(13.5, 5.0), sharey=False)
    rng = np.random.default_rng(151)

    # A deliberately NON-normal parent: a right-skewed (exponential-ish) score.
    def draw_means(n, reps=60000):
        s = rng.exponential(scale=1.0, size=(reps, n))
        return s.mean(axis=1)

    panels = [(1, "n = 1 trainer\n(one skewed score)"),
              (5, "n = 5 trainers\n(average of 5)"),
              (30, "n = 30 trainers\n(average of 30)")]
    # mixed real sprites floating above each panel = "many trainers pooling"
    dex_sets = [[25], [1, 7, 25], [1, 4, 7, 25, 35, 130]]

    for ax, (n, label), dexes in zip(axes, panels, dex_sets):
        _clean(ax)
        m = draw_means(n)
        ax.hist(m, bins=60, density=True, color=ACCENT, alpha=0.55,
                edgecolor=ACCENT, hatch="..", lw=0.0)
        # overlay the CLT-predicted normal: mean 1, sd = 1/sqrt(n).
        xx = np.linspace(m.min(), m.max(), 400)
        ax.plot(xx, stats.norm.pdf(xx, 1.0, 1.0 / np.sqrt(n)),
                color=KANTO_RED, lw=2.4, zorder=5,
                label="CLT normal" if n == 1 else None)
        ax.set_title(label, fontsize=11)
        ax.set_yticks([])
        ax.set_xlabel("sample mean $\\bar X$", fontsize=9.5)
        # real sprites in the top margin, never over the histogram body.
        ytop = ax.get_ylim()[1]
        ax.set_ylim(0, ytop * 1.22)
        xs_positions = np.linspace(*ax.get_xlim(), len(dexes) + 2)[1:-1]
        for sx, d in zip(xs_positions, dexes):
            place_sprite(ax, front(d), (sx, ytop * 1.10), zoom=0.22,
                         alpha=0.9, zorder=6)

    axes[0].legend(loc="upper right", fontsize=9, frameon=True)
    fig.suptitle("The Central Limit Theorem: average enough independent results "
                 "and the bell appears\n"
                 r"even a skewed parent: $\bar X \approx N\!\left(\mu,\ \sigma^2/n\right)$ "
                 "- the spread shrinks like $1/\\sqrt{n}$",
                 fontsize=13, y=1.04)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    return save(fig, "ch12_clt_convergence")


# --------------------------------------------------------------------------
# 4. ch12_continuity_correction — discrete staircase vs smooth normal. (Concept 4)
# --------------------------------------------------------------------------
def fig_continuity_correction():
    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    _clean(ax)
    # Binomial n=100, p=0.5 (a discrete SUM of 100 results), normal-approximated.
    n, p = 100, 0.5
    mu, sigma = n * p, np.sqrt(n * p * (1 - p))  # 50, 5
    ks = np.arange(38, 63)
    pmf = stats.binom.pmf(ks, n, p)

    # Draw the discrete pmf as unit-width bars centered on each integer.
    for k, pk in zip(ks, pmf):
        focus = (54 <= k <= 56)
        ax.add_patch(Rectangle((k - 0.5, 0), 1.0, pk,
                               facecolor=KANTO_BLUE if not focus else KANTO_YEL,
                               edgecolor=INK, lw=0.8,
                               alpha=0.85 if focus else 0.40,
                               hatch="xx" if focus else None, zorder=2))

    # The smooth normal curve on top.
    xx = np.linspace(36, 64, 600)
    ax.plot(xx, stats.norm.pdf(xx, mu, sigma), color=KANTO_RED, lw=2.6,
            zorder=5)

    # Highlight the P(X = 54,55,56) target = bars 53.5 .. 56.5 under the curve.
    lo, hi = 53.5, 56.5
    xb = np.linspace(lo, hi, 200)
    ax.fill_between(xb, stats.norm.pdf(xb, mu, sigma), color=KANTO_RED,
                    alpha=0.22, zorder=3)
    for b, lab in [(lo, "53.5"), (hi, "56.5")]:
        ax.axvline(b, color=KANTO_RED, lw=1.4, ls="--", zorder=4)
        ax.text(b, -0.004, lab, ha="center", va="top", color=KANTO_RED,
                fontsize=10, fontweight="bold")

    ax.annotate("the discrete bars for 54, 55, 56\nspan the half-steps "
                "53.5 to 56.5",
                xy=(55, stats.norm.pdf(55, mu, sigma) * 0.5),
                xytext=(59.5, 0.075), ha="center", fontsize=10, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3),
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_RED,
                          lw=1.2))

    ax.set_title("Continuity correction: a discrete bar has WIDTH 1, so it "
                 "reaches a half-step past its center\n"
                 r"$P(54\leq X\leq 56)\approx P(53.5< Y< 56.5)$ with "
                 r"$Y\sim N(np,\ np(1-p))$",
                 fontsize=12.5)
    ax.set_xlabel("number of wins $X$ out of 100 (discrete) "
                  "vs. normal approximation $Y$", fontsize=10)
    ax.set_yticks([])
    ax.set_xlim(37, 64)
    ax.set_ylim(0, 0.092)
    ax.set_xticks([40, 45, 50, 53.5, 56.5, 60])
    ax.set_xticklabels(["40", "45", r"$\mu=50$", "53.5", "56.5", "60"],
                       fontsize=9)
    place_sprite(ax, front(35), (40.5, 0.083), zoom=0.34, alpha=0.95, zorder=6)
    fig.tight_layout()
    return save(fig, "ch12_continuity_correction")


# --------------------------------------------------------------------------
# 5. ch12_lognormal — ENRICHMENT: exp(normal) is right-skewed. (Concept 5)
# --------------------------------------------------------------------------
def fig_lognormal():
    fig, ax = plt.subplots(figsize=(11, 6.0))
    _clean(ax)
    # If ln(L) ~ N(mu, sigma^2), L is lognormal: positive, right-skewed.
    mu, sigma = 0.0, 0.6
    x = np.linspace(0.001, 7, 800)
    y = stats.lognorm.pdf(x, s=sigma, scale=np.exp(mu))
    ax.plot(x, y, color=ACCENT, lw=2.8, zorder=5)
    ax.fill_between(x, y, color=ACCENT, alpha=0.30, hatch="..",
                    edgecolor=ACCENT, lw=0.0, zorder=2)

    # mark mean, median, mode to show skew ordering (mode<median<mean).
    median = np.exp(mu)                      # 1.0
    mean = np.exp(mu + sigma ** 2 / 2)       # ~1.197
    mode = np.exp(mu - sigma ** 2)           # ~0.698
    for val, lab, col, dy in [(mode, "mode", KANTO_GREEN, 0.04),
                              (median, "median", KANTO_BLUE, 0.10),
                              (mean, "mean", KANTO_RED, 0.16)]:
        ax.axvline(val, color=col, lw=1.6, ls="--", zorder=4)
        ax.text(val, stats.lognorm.pdf(median, s=sigma, scale=np.exp(mu)) + dy,
                lab, ha="center", color=col, fontsize=10, fontweight="bold")

    ax.annotate("long right tail:\na few enormous losses",
                xy=(4.5, stats.lognorm.pdf(4.5, s=sigma, scale=np.exp(mu))),
                xytext=(5.0, 0.45), ha="center", fontsize=10, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.3))

    ax.set_title("ENRICHMENT - the lognormal: exponentiate a normal and the "
                 "bell becomes a right-skewed loss curve\n"
                 r"$\ln L\sim N(\mu,\sigma^2)\ \Rightarrow\ L$ is lognormal "
                 "(positive, skewed: mode $<$ median $<$ mean)",
                 fontsize=12.5)
    ax.set_xlabel("claim size / damage $L > 0$", fontsize=10)
    ax.set_yticks([])
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 0.78)
    # Gyarados decorates the tail margin (the rare, enormous outcome).
    place_sprite(ax, front(130), (5.9, 0.62), zoom=0.42, alpha=0.95, zorder=6)
    ax.text(5.9, 0.50, "#130 Gyarados", ha="center", fontsize=8, color=INK)
    fig.tight_layout()
    return save(fig, "ch12_lognormal")


REGISTRY = [
    fig_normal_6895997,
    fig_standardize,
    fig_clt_convergence,
    fig_continuity_correction,
    fig_lognormal,
]


def main() -> None:
    print(f"Generating Chapter 12 (Normal & CLT) figures -> {OUT} "
          f"at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
