#!/usr/bin/env python3
"""Generate every Chapter 5 (Key Discrete Distributions / Lavender Tower -> Celadon /
Erika) figure.

Manifest (MASTER_PLAN_V3 §16, DESIGN_BLUEPRINT ch05 row) — seven diagrams into
assets/diagrams/:
  ch05_geometric_series   the geometric-series toolkit: partial sums marching to 1/(1-r)
  ch05_taylor_exp         Taylor series for e^x: partial sums sandwiching the curve
  ch05_geometric_pmf      first-success wait, geometric decay; composites Meowth #52
  ch05_memoryless         the survival tail re-anchored: the past evaporates
  ch05_negbin            negative-binomial pmf (wait-for-3rd); composites Dugtrio #51
  ch05_poisson_window     two Poisson windows (1 min lambda=3, 5 min lambda=15);
                          composites Gastly #92 + Haunter #93
  ch05_poisson_sums       superposition: independent Poisson streams add their rates

PRINT TARGET: bound book -> every PNG at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is
ALSO distinguished by a hatch / line-style / text label so figures survive grayscale
(color is never the sole channel). Sprites obey the IRON RULE: real Pokemon art in
margins/corners only, never over a bar, curve, axis, equation, or number a reader
must read.

Run: python3 figures/src/gen_ch05.py
"""
from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, FancyArrowPatch
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
GHOST = chapter_accent(5)  # §17 Ghost accent (#705898) — banner/figure parity.
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
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)
    ax.set_facecolor("white")
    ax.grid(False)


# --------------------------------------------------------------------------
# 1. ch05_geometric_series — the toolkit interlude (A.5.0a).
#    Partial sums of sum r^k (r=0.6) climb a staircase that converges to 1/(1-r).
# --------------------------------------------------------------------------
def fig_geometric_series():
    r = 0.6
    n_terms = 8
    terms = [r ** k for k in range(n_terms)]
    partials = []
    run = 0.0
    for t in terms:
        run += t
        partials.append(run)
    limit = 1.0 / (1.0 - r)  # 2.5

    fig, ax = plt.subplots(figsize=(10.5, 6.0))
    ax.set_title("The geometric series: partial sums march to a finite limit\n"
                 r"$\sum_{k=0}^{\infty} r^{k}=\dfrac{1}{1-r}$  "
                 f"(here $r={r}$, limit $={limit:.2f}$)", fontsize=13)

    xs = list(range(1, n_terms + 1))
    # The limit line (dashed, labeled).
    ax.axhline(limit, color=KANTO_RED, lw=2.0, ls="--", zorder=2)
    ax.text(n_terms + 0.05, limit, r"$\dfrac{1}{1-r}=2.5$", color=KANTO_RED,
            fontsize=12, va="center", ha="left", fontweight="bold")

    # Bars = each new term r^k added; staircase line = the partial sum.
    ax.bar(xs, terms, width=0.5, color=GHOST, edgecolor=INK, lw=1.2,
           hatch="..", alpha=0.85, zorder=3, label=r"new term $r^{k}$")
    ax.plot(xs, partials, "-o", color=KANTO_BLUE, lw=2.4, ms=7, zorder=4,
            label="partial sum $S_n$")
    for x, s in zip(xs, partials):
        ax.text(x, s + 0.06, f"{s:.2f}", ha="center", va="bottom",
                fontsize=8.6, color=KANTO_BLUE)

    ax.set_xlabel("number of terms summed,  $n$")
    ax.set_ylabel("value")
    ax.set_xticks(xs)
    ax.set_xticklabels([f"$k\\!\\leq\\!{n-1}$" for n in xs])
    ax.set_ylim(0, limit + 0.55)
    ax.set_xlim(0.4, n_terms + 1.4)
    ax.grid(axis="y", alpha=0.35)
    ax.legend(loc="center right", fontsize=10, framealpha=0.95)

    ax.text(0.03, 0.95,
            r"each term is $r$ times the one before;" "\n"
            r"because $|r|<1$ they shrink fast enough" "\n"
            r"that the running total never exceeds $\frac{1}{1-r}$.",
            transform=ax.transAxes, ha="left", va="top", fontsize=9.5,
            color=INK, bbox=dict(boxstyle="round,pad=0.35", fc="#EFE8FA",
                                 ec=GHOST, lw=1.3))
    fig.tight_layout()
    return save(fig, "ch05_geometric_series")


# --------------------------------------------------------------------------
# 2. ch05_taylor_exp — Taylor series for e^x (A.5.0b).
#    Partial sums 1, 1+x, 1+x+x^2/2, ... converging to e^x on a window.
# --------------------------------------------------------------------------
def fig_taylor_exp():
    xs = [i / 40.0 for i in range(-80, 81)]  # x in [-2, 2]
    true = [math.exp(x) for x in xs]

    def partial(x, n):  # sum_{k=0}^{n} x^k / k!
        return sum(x ** k / math.factorial(k) for k in range(n + 1))

    orders = [1, 2, 3, 5]
    styles = ["--", "-.", ":", (0, (5, 1))]
    cols = [KANTO_BLUE, KANTO_GREEN, "#FF7043", GHOST]

    fig, ax = plt.subplots(figsize=(10.5, 6.0))
    ax.set_title("Taylor series for $e^{x}$: add terms, the polynomial hugs the curve\n"
                 r"$e^{x}=\sum_{k=0}^{\infty}\dfrac{x^{k}}{k!}"
                 r"=1+x+\dfrac{x^{2}}{2!}+\dfrac{x^{3}}{3!}+\cdots$", fontsize=12.5)

    ax.plot(xs, true, color=KANTO_RED, lw=3.0, zorder=5, label="$e^{x}$ (true)")
    for n, sty, col in zip(orders, styles, cols):
        ys = [partial(x, n) for x in xs]
        ax.plot(xs, ys, ls=sty, color=col, lw=2.0, zorder=4,
                label=f"up to $x^{{{n}}}$")

    ax.set_xlabel("$x$")
    ax.set_ylabel("value")
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.2, 7.6)
    ax.axhline(0, color=KANTO_GRAY, lw=0.9)
    ax.axvline(0, color=KANTO_GRAY, lw=0.9)
    ax.grid(alpha=0.3)
    ax.legend(loc="upper left", fontsize=9.5, framealpha=0.95)

    ax.text(0.97, 0.06,
            r"set $x=\lambda$: $\sum_k \lambda^k/k! = e^{\lambda}$" "\n"
            r"is exactly why the Poisson masses sum to 1.",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=9.5,
            color=INK, bbox=dict(boxstyle="round,pad=0.35", fc="#FFF6D6",
                                 ec=KANTO_YEL, lw=1.3))
    fig.tight_layout()
    return save(fig, "ch05_taylor_exp")


# --------------------------------------------------------------------------
# 3. ch05_geometric_pmf — first-success wait. Geometric(0.15) decay, trials
#    convention. Real Meowth #52 (the slot-pulling cat) in the upper-right margin.
#    Right tail past k=5 shaded: P(X>5)=q^5.
# --------------------------------------------------------------------------
def fig_geometric_pmf():
    p = 0.15
    q = 1 - p
    kmax = 14
    ks = list(range(1, kmax + 1))
    pmf = [q ** (k - 1) * p for k in ks]

    fig, ax = plt.subplots(figsize=(10.5, 6.0))
    ax.set_title("Geometric$(0.15)$: waiting for the first success\n"
                 r"$p(k)=q^{\,k-1}p$ — each bar is $q=0.85$ times the previous",
                 fontsize=12.5)

    for k, pk in zip(ks, pmf):
        col = KANTO_RED if k > 5 else GHOST
        hatch = "xx" if k > 5 else ".."
        ax.bar(k, pk, width=0.62, color=col, edgecolor=INK, lw=1.1,
               hatch=hatch, alpha=0.88, zorder=3)
    for k, pk in zip(ks[:6], pmf[:6]):
        ax.text(k, pk + 0.004, f"{pk:.3f}", ha="center", va="bottom",
                fontsize=8.0, color=INK)

    ax.set_xlabel("$k$ (throw of the first success)")
    ax.set_ylabel("$p(k)$")
    ax.set_xticks(ks)
    ax.set_ylim(0, 0.175)
    ax.set_xlim(0.3, kmax + 0.7)
    ax.grid(axis="y", alpha=0.35)

    surv5 = q ** 5
    ax.text(0.97, 0.78,
            "shaded right tail $k>5$:\n"
            r"$P(X>5)=q^{5}=" f"{surv5:.4f}$" "\n"
            "(all first 5 throws fail)",
            transform=ax.transAxes, ha="right", va="top", fontsize=9.8,
            color=KANTO_RED, bbox=dict(boxstyle="round,pad=0.35", fc="#FDEAEA",
                                       ec=KANTO_RED, lw=1.3))
    # Meowth #52 in the upper-right margin — clear of all bars/labels.
    place_sprite(ax, front(52), (0.86, 0.95), xycoords="axes fraction",
                 zoom=0.42, alpha=0.97, zorder=6)
    fig.tight_layout()
    return save(fig, "ch05_geometric_pmf")


# --------------------------------------------------------------------------
# 4. ch05_memoryless — the survival tail re-anchored. Show that, given you've
#    already failed m times, the remaining wait has the SAME shape as a fresh start.
# --------------------------------------------------------------------------
def fig_memoryless():
    p = 0.15
    q = 1 - p
    m = 3  # already failed 3 times
    n_extra = list(range(0, 9))
    fresh = [q ** n for n in n_extra]                 # P(X > n) fresh
    cond = [q ** n for n in n_extra]                  # P(X > m+n | X > m) — identical!

    fig, axes = plt.subplots(1, 2, figsize=(12.2, 5.4), sharey=True)
    fig.suptitle("Memorylessness: a wait that has already failed $m$ times is as "
                 "fresh as a brand-new wait",
                 fontsize=13, fontweight="bold", y=1.01)

    # Left: a brand-new wait, survival vs. extra trials n.
    ax = axes[0]
    ax.bar(n_extra, fresh, width=0.6, color=KANTO_BLUE, edgecolor=INK, lw=1.1,
           hatch="//", alpha=0.85, zorder=3)
    ax.set_title("Fresh start:  $P(X>n)=q^{\\,n}$", fontsize=11.5)
    ax.set_xlabel("extra trials  $n$")
    ax.set_ylabel("survival probability")
    ax.set_xticks(n_extra)
    ax.set_ylim(0, 1.05)
    ax.grid(axis="y", alpha=0.35)

    # Right: conditioned on already failing m=3, survival of the REMAINING wait.
    ax = axes[1]
    ax.bar(n_extra, cond, width=0.6, color=KANTO_RED, edgecolor=INK, lw=1.1,
           hatch="xx", alpha=0.85, zorder=3)
    ax.set_title(f"Already failed $m={m}$:  "
                 r"$P(X>m+n\mid X>m)=q^{\,n}$", fontsize=11.5)
    ax.set_xlabel("further extra trials  $n$")
    ax.set_xticks(n_extra)
    ax.set_ylim(0, 1.05)
    ax.grid(axis="y", alpha=0.35)

    fig.text(0.5, -0.02,
             r"$P(X>m+n\mid X>m)=\dfrac{q^{m+n}}{q^{m}}=q^{n}=P(X>n)$"
             "   — the two charts are identical: the past evaporates.",
             ha="center", va="top", fontsize=11, color=INK,
             bbox=dict(boxstyle="round,pad=0.4", fc="#EFE8FA", ec=GHOST, lw=1.4))
    fig.tight_layout()
    return save(fig, "ch05_memoryless")


# --------------------------------------------------------------------------
# 5. ch05_negbin — negative binomial (failures convention), r=3, p=0.4.
#    Rises off k=0, peaks, decays. Real Dugtrio #51 (three heads = wait-for-3)
#    in the upper-right margin.
# --------------------------------------------------------------------------
def fig_negbin():
    r, p = 3, 0.4
    q = 1 - p
    kmax = 14
    ks = list(range(0, kmax + 1))
    pmf = [math.comb(k + r - 1, k) * p ** r * q ** k for k in ks]
    mean = r * q / p  # 4.5

    fig, ax = plt.subplots(figsize=(10.5, 6.0))
    ax.set_title("Negative Binomial$(r=3,\\ p=0.4)$: waiting for the $3$rd success\n"
                 r"$p(k)=\binom{k+r-1}{k}p^{r}q^{k}$ (failures before the $3$rd win)",
                 fontsize=12.5)

    bars = ax.bar(ks, pmf, width=0.66, color=GHOST, edgecolor=INK, lw=1.1,
                  hatch="..", alpha=0.88, zorder=3)
    # Highlight k=2 (the worked value 0.1382).
    bars[2].set_facecolor(KANTO_RED)
    bars[2].set_alpha(0.9)
    bars[2].set_hatch("xx")
    for k in (0, 1, 2, 3, 4):
        ax.text(k, pmf[k] + 0.003, f"{pmf[k]:.3f}", ha="center", va="bottom",
                fontsize=8.0, color=INK)

    ax.axvline(mean, color=KANTO_BLUE, lw=2.2, ls="--", zorder=4)
    ax.text(mean + 0.15, 0.155, f"mean $=rq/p={mean:.1f}$", color=KANTO_BLUE,
            fontsize=10, va="top", ha="left", fontweight="bold")

    ax.set_xlabel("$k$ (losses before the $3$rd win)")
    ax.set_ylabel("$p(k)$")
    ax.set_xticks(ks)
    ax.set_ylim(0, 0.175)
    ax.set_xlim(-0.6, kmax + 0.6)
    ax.grid(axis="y", alpha=0.35)

    ax.text(0.62, 0.93,
            r"unlike the geometric (tallest at $k=0$)," "\n"
            r"it $rises$ off $0$: you rarely collect $3$" "\n"
            r"wins with zero losses. Highlighted $k=2$:" "\n"
            r"$\binom{4}{2}(0.4)^3(0.6)^2=0.1382$.",
            transform=ax.transAxes, ha="left", va="top", fontsize=9.3,
            color=INK, bbox=dict(boxstyle="round,pad=0.35", fc="#FDEAEA",
                                 ec=KANTO_RED, lw=1.2))
    # Dugtrio #51 (three heads — wait for the 3rd) in the upper-right margin.
    place_sprite(ax, front(51), (0.93, 0.55), xycoords="axes fraction",
                 zoom=0.40, alpha=0.97, zorder=6)
    fig.tight_layout()
    return save(fig, "ch05_negbin")


# --------------------------------------------------------------------------
# 6. ch05_poisson_window — two Poisson windows. Left: 1 minute, lambda=3.
#    Right: 5 minutes, lambda=15 (the rescaling lesson), left tail k<=9 shaded
#    (the "lull", P=0.0699). Real Gastly #92 + Haunter #93 in margins.
# --------------------------------------------------------------------------
def fig_poisson_window():
    def pois(lam, k):
        return math.exp(-lam) * lam ** k / math.factorial(k)

    fig, axes = plt.subplots(1, 2, figsize=(13.0, 5.6))
    fig.suptitle("Poisson counts have no upper limit — and $\\lambda$ scales with the window",
                 fontsize=13, fontweight="bold", y=1.01)

    # Left: lambda = 3 (one minute).
    lam = 3
    ks = list(range(0, 13))
    pmf = [pois(lam, k) for k in ks]
    ax = axes[0]
    ax.bar(ks, pmf, width=0.7, color=GHOST, edgecolor=INK, lw=1.0, hatch="..",
           alpha=0.88, zorder=3)
    ax.axvline(lam, color=KANTO_BLUE, lw=2.0, ls="--", zorder=4)
    ax.text(lam + 0.2, max(pmf) * 0.96, r"$\lambda=3$", color=KANTO_BLUE,
            fontsize=10.5, fontweight="bold", va="top")
    ax.set_title("One minute:  $\\lambda=3$", fontsize=11.5)
    ax.set_xlabel("$k$ (Gastly in the window)")
    ax.set_ylabel("$p(k)$")
    ax.set_xticks(ks)
    ax.set_ylim(0, 0.26)
    ax.grid(axis="y", alpha=0.35)
    place_sprite(ax, front(92), (0.86, 0.86), xycoords="axes fraction",
                 zoom=0.40, alpha=0.97, zorder=6)

    # Right: lambda = 15 (five minutes), shade the left tail k<=9.
    lam = 15
    ks = list(range(0, 31))
    pmf = [pois(lam, k) for k in ks]
    ax = axes[1]
    for k, pk in zip(ks, pmf):
        shaded = k <= 9
        ax.bar(k, pk, width=0.8,
               color=KANTO_RED if shaded else GHOST,
               edgecolor=INK, lw=0.7,
               hatch="xx" if shaded else "..",
               alpha=0.88, zorder=3)
    ax.axvline(lam, color=KANTO_BLUE, lw=2.0, ls="--", zorder=4)
    ax.text(lam + 0.3, max(pmf) * 0.96, r"$\lambda=15$", color=KANTO_BLUE,
            fontsize=10.5, fontweight="bold", va="top")
    ax.set_title("Five minutes:  $\\lambda=5\\times3=15$", fontsize=11.5)
    ax.set_xlabel("$k$ (Gastly in the window)")
    ax.set_ylabel("$p(k)$")
    ax.set_xticks(range(0, 31, 3))
    ax.set_ylim(0, 0.115)
    ax.grid(axis="y", alpha=0.35)

    tail = sum(pois(lam, k) for k in range(0, 10))
    ax.text(0.97, 0.80,
            "shaded left tail $k\\leq 9$:\n"
            f"$P(Y<10)={tail:.4f}$\n"
            "a genuine lull (rate is per\nminute — rescale to the window!)",
            transform=ax.transAxes, ha="right", va="top", fontsize=9.3,
            color=KANTO_RED, bbox=dict(boxstyle="round,pad=0.35", fc="#FDEAEA",
                                       ec=KANTO_RED, lw=1.2))
    place_sprite(ax, front(93), (0.90, 0.40), xycoords="axes fraction",
                 zoom=0.34, alpha=0.97, zorder=6)
    fig.tight_layout()
    return save(fig, "ch05_poisson_sums_helper_noop") if False else save(
        fig, "ch05_poisson_window")


# --------------------------------------------------------------------------
# 7. ch05_poisson_sums — superposition. Two independent Poisson streams (Gastly
#    lambda=3, Haunter lambda=1) combine into one Poisson(4): rates simply ADD.
# --------------------------------------------------------------------------
def fig_poisson_sums():
    fig, ax = plt.subplots(figsize=(11.0, 6.2))
    _blank(ax)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.set_title("Superposition: independent Poisson streams ADD their rates\n"
                 r"$\mathrm{Pois}(\lambda_1)+\mathrm{Pois}(\lambda_2)"
                 r"=\mathrm{Pois}(\lambda_1+\lambda_2)$", fontsize=13)

    def stream_box(x, y, w, h, title, lam, sprite_dex, fc):
        ax.add_patch(FancyBboxPatch((x, y), w, h,
                                    boxstyle="round,pad=0.05,rounding_size=0.12",
                                    fc=fc, ec=INK, lw=1.6, zorder=2))
        ax.text(x + w / 2, y + h - 0.42, title, ha="center", va="center",
                fontsize=11.5, fontweight="bold", color=INK, zorder=4)
        ax.text(x + w / 2, y + h - 0.95, f"rate $\\lambda={lam}$/min",
                ha="center", va="center", fontsize=11, color=INK, zorder=4)
        place_sprite(ax, front(sprite_dex), (x + w / 2, y + 0.62),
                     xycoords="data", zoom=0.5, alpha=0.97, zorder=5)

    # Two input streams (left).
    stream_box(0.5, 5.1, 3.6, 2.9, "Gastly stream", 3, 92, "#EFE8FA")
    stream_box(0.5, 1.1, 3.6, 2.9, "Haunter stream", 1, 93, "#E7ECFB")

    # Combined stream (right).
    ax.add_patch(FancyBboxPatch((7.4, 3.1), 4.2, 3.0,
                                boxstyle="round,pad=0.05,rounding_size=0.12",
                                fc="#FFF6D6", ec=KANTO_YEL, lw=2.2, zorder=2))
    ax.text(9.5, 5.55, "Total ghosts", ha="center", va="center",
            fontsize=12.5, fontweight="bold", color=INK, zorder=4)
    ax.text(9.5, 4.85, r"$\mathrm{Pois}(3+1)=\mathrm{Pois}(4)$",
            ha="center", va="center", fontsize=13, color=KANTO_RED,
            fontweight="bold", zorder=4)
    ax.text(9.5, 4.20, "rate $\\lambda=4$/min,  mean $=$ var $=4$",
            ha="center", va="center", fontsize=10, color=INK, zorder=4)
    ax.text(9.5, 3.55, "over 2 min: $\\mathrm{Pois}(8)$",
            ha="center", va="center", fontsize=10, color=INK, style="italic",
            zorder=4)

    # Arrows merging into the combined box.
    for y0 in (6.55, 2.55):
        ax.add_patch(FancyArrowPatch((4.2, y0), (7.3, 4.6),
                                     arrowstyle="-|>", mutation_scale=20,
                                     color=GHOST, lw=2.4, zorder=3,
                                     connectionstyle="arc3,rad=0.12"))

    ax.text(6.0, 0.5,
            "Just sum the rates — no convolution needed. (The MGF proof: "
            r"$M(t)=e^{\lambda_1(e^t-1)}e^{\lambda_2(e^t-1)}"
            r"=e^{(\lambda_1+\lambda_2)(e^t-1)}$.)",
            ha="center", va="center", fontsize=9.5, color=INK, style="italic",
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec=KANTO_GRAY, lw=1.0))
    fig.tight_layout()
    return save(fig, "ch05_poisson_sums")


REGISTRY = [
    fig_geometric_series,
    fig_taylor_exp,
    fig_geometric_pmf,
    fig_memoryless,
    fig_negbin,
    fig_poisson_window,
    fig_poisson_sums,
]


def main() -> None:
    print(f"Generating Chapter 5 (Key Discrete Distributions) figures -> {OUT} "
          f"at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
