#!/usr/bin/env python3
"""Generate every Chapter 8 (Named Discrete Distributions / Celadon City) math figure.

Chapter 8 builds the named discrete laws (binomial, geometric, Poisson) through
nine-beat arcs whose "Picture it" beat each references one purpose-built pmf
diagram. None existed yet; this script renders EXACTLY the three filenames the
chapter points at, so picture and caption agree:

  ch08_binomial_pmf   Concept 2, Beat 8: bar chart of Binom(10, 0.2). Bars rise
                      from k=0 (~0.107), peak at k=2 (0.3020), fall toward k=10.
                      Dashed vertical line marks the mean np=2; the k=2 bar is
                      highlighted to match the worked value 0.3020.

  ch08_geometric_pmf  Concept 3, Beat 8: bar chart of Geom(0.15), trials
                      convention. Tallest bar at k=1 (0.15); each subsequent bar
                      is q=0.85 times the previous one (0.15, 0.1275, 0.1084,...).
                      The right tail past k=5 is shaded; its mass is q^5=0.4437.

  ch08_poisson_pmf    Concept 4, Beat 8: two side-by-side Poisson pmfs. Left:
                      lambda=3 (one minute), peaking near k=3 with a long thin
                      right tail. Right: lambda=15 (five minutes), a broad hump
                      near 15 with bars k=0..9 shaded as the left tail
                      P(Y<10)=0.0699. Both have no upper bound on k.

PRINT TARGET: bound book, so every PNG is rendered at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element
ALSO carries a hatch / linestyle / direct label, so the figures stay legible in
grayscale.

Run: python figures/src/gen_ch08.py
"""
from __future__ import annotations

import math
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe + accents).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
INK = "#333333"
DPI = 300


# ---------------------------------------------------------------------------
def binom_pmf(k, n, p):
    return math.comb(n, k) * p**k * (1 - p) ** (n - k)


def fig_bernoulli_pmf():
    """Bernoulli(0.2): two bars, P(0)=0.8 and P(1)=0.2 — the atom of counting."""
    p = 0.2
    ks = [0, 1]
    probs = [1 - p, p]

    fig, ax = plt.subplots(figsize=(5.4, 4.4))
    colors = [KANTO_GRAY, KANTO_BLUE]
    bars = ax.bar(ks, probs, width=0.5, color=colors, edgecolor=INK,
                  linewidth=1.2, zorder=3)
    for k, pr in zip(ks, probs):
        ax.text(k, pr + 0.015, f"{pr:.1f}", ha="center", va="bottom",
                fontsize=13, color=INK)

    ax.set_xticks([0, 1])
    ax.set_xticklabels([r"$0$  (loss, $q=0.8$)", r"$1$  (win, $p=0.2$)"])
    ax.set_ylabel(r"$P(X = k)$")
    ax.set_title(r"Bernoulli$(0.2)$ — a single yes/no trial")
    ax.set_ylim(0, 0.92)
    ax.set_xlim(-0.6, 1.6)
    ax.grid(axis="x", visible=False)

    fig.tight_layout()
    out = OUT / "ch08_bernoulli_pmf.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    return out


def fig_binomial_pmf():
    """Binom(10, 0.2): peak at k=2 (0.3020), mean np=2 dashed line, k=2 bar lit."""
    n, p = 10, 0.2
    ks = np.arange(0, n + 1)
    probs = np.array([binom_pmf(int(k), n, p) for k in ks])

    fig, ax = plt.subplots(figsize=(9, 5.5))

    colors = [KANTO_BLUE] * (n + 1)
    hatches = [""] * (n + 1)
    colors[2] = KANTO_RED          # highlight the worked k=2 bar
    hatches[2] = "//"
    bars = ax.bar(ks, probs, width=0.72, color=colors, edgecolor=INK,
                  linewidth=1.1, zorder=3)
    for b, h in zip(bars, hatches):
        if h:
            b.set_hatch(h)

    # mean line
    ax.axvline(n * p, color=INK, linestyle="--", linewidth=1.8, zorder=4)
    ax.annotate(r"mean $np = 2$", xy=(2, 0.315), xytext=(4.2, 0.30),
                fontsize=12, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))

    # value labels on the leading bars
    for k in (0, 1, 2, 3):
        ax.text(k, probs[k] + 0.008, f"{probs[k]:.3f}", ha="center",
                va="bottom", fontsize=10.5, color=INK)

    # callout for the highlighted bar
    ax.annotate(r"$p(2)=\binom{10}{2}(0.2)^2(0.8)^8 = 0.3020$",
                xy=(2, 0.302), xytext=(4.6, 0.235),
                fontsize=12, color=KANTO_RED,
                arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.5))

    ax.set_xticks(ks)
    ax.set_xlabel(r"$k$  (number of wins out of $n=10$)")
    ax.set_ylabel(r"$P(X = k)$")
    ax.set_title(r"Binomial$(10,\ 0.2)$ pmf — count clusters around the mean")
    ax.set_ylim(0, 0.345)
    ax.set_xlim(-0.6, 10.6)
    ax.grid(axis="x", visible=False)

    fig.tight_layout()
    out = OUT / "ch08_binomial_pmf.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
def fig_geometric_pmf():
    """Geom(0.15) trials convention: geometric decay, right tail k>5 shaded = q^5."""
    p, q = 0.15, 0.85
    ks = np.arange(1, 21)
    probs = q ** (ks - 1) * p

    fig, ax = plt.subplots(figsize=(9, 5.5))

    tail_mask = ks > 5
    colors = np.where(tail_mask, KANTO_YEL, KANTO_GREEN)
    bars = ax.bar(ks, probs, width=0.72, color=list(colors), edgecolor=INK,
                  linewidth=1.1, zorder=3)
    # hatch the shaded tail so it reads in grayscale
    for b, t in zip(bars, tail_mask):
        if t:
            b.set_hatch("xx")

    # decay annotation: each bar is q x previous
    ax.annotate(r"each bar $= q \times$ previous, $q = 0.85$",
                xy=(2, probs[1]), xytext=(5.0, 0.122),
                fontsize=12, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))

    # value labels on leading bars
    for i, k in enumerate(ks[:3]):
        ax.text(k, probs[i] + 0.0035, f"{probs[i]:.4f}", ha="center",
                va="bottom", fontsize=10.5, color=INK)

    # bracket / shaded-tail label for survival q^5
    ax.annotate(r"right tail $k>5$:  $P(X>5)=q^5 = 0.4437$",
                xy=(8.5, 0.012), xytext=(7.0, 0.085),
                fontsize=12, color="#8a6d00",
                arrowprops=dict(arrowstyle="->", color="#8a6d00", lw=1.5))

    # boundary marker between "first 5 passes" and the survival tail
    ax.axvline(5.5, color=INK, linestyle=":", linewidth=1.6, zorder=4)

    ax.set_xticks(ks[::1])
    ax.set_xlabel(r"$k$  (pass on which the first success occurs)")
    ax.set_ylabel(r"$P(X = k) = q^{\,k-1}p$")
    ax.set_title(r"Geometric$(0.15)$ pmf (trials convention) — geometric decay")
    ax.set_ylim(0, 0.168)
    ax.set_xlim(0.4, 20.6)
    ax.grid(axis="x", visible=False)

    # legend by patch (color + hatch), not color alone
    from matplotlib.patches import Patch
    legend = [
        Patch(facecolor=KANTO_GREEN, edgecolor=INK, label=r"$k \leq 5$  (success arrives early)"),
        Patch(facecolor=KANTO_YEL, edgecolor=INK, hatch="xx",
              label=r"$k > 5$  (survival tail, mass $q^5$)"),
    ]
    ax.legend(handles=legend, loc="upper right")

    fig.tight_layout()
    out = OUT / "ch08_geometric_pmf.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
def negbin_pmf(k, r, p):
    """P(X=k) for X = failures before the r-th success, NB(r, p)."""
    return math.comb(k + r - 1, k) * p**r * (1 - p) ** k


def fig_negbin_pmf():
    """NegBinom(r=3, p=0.4), failures convention: rise-then-decay, k=2 bar lit (0.1382)."""
    r, p = 3, 0.4
    ks = np.arange(0, 16)
    probs = np.array([negbin_pmf(int(k), r, p) for k in ks])

    fig, ax = plt.subplots(figsize=(9, 5.5))

    colors = [KANTO_GREEN] * len(ks)
    hatches = [""] * len(ks)
    colors[2] = KANTO_RED          # highlight the worked k=2 bar (third win on round 5)
    hatches[2] = "//"
    bars = ax.bar(ks, probs, width=0.74, color=colors, edgecolor=INK,
                  linewidth=1.1, zorder=3)
    for b, h in zip(bars, hatches):
        if h:
            b.set_hatch(h)

    # mean line: E[X] = rq/p = 4.5
    mean = r * (1 - p) / p
    ax.axvline(mean, color=INK, linestyle="--", linewidth=1.8, zorder=4)
    ax.annotate(r"mean $=\frac{rq}{p} = 4.5$", xy=(mean, 0.165), xytext=(6.6, 0.155),
                fontsize=12, color=INK,
                arrowprops=dict(arrowstyle="->", color=INK, lw=1.4))

    # value labels on the leading bars (skip k=2; its value rides in the red callout)
    for k in (0, 1, 3):
        ax.text(k, probs[k] + 0.004, f"{probs[k]:.4f}", ha="center",
                va="bottom", fontsize=10.5, color=INK)

    # callout for the highlighted bar
    ax.annotate(r"$p(2)=\binom{4}{2}(0.4)^3(0.6)^2 = 0.1382$",
                xy=(2, probs[2]), xytext=(4.4, 0.118),
                fontsize=12, color=KANTO_RED,
                arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.5))

    # note the rise: unlike the geometric (r=1), the NB pmf bumps up before decaying
    ax.annotate("rises off $k=0$ then decays\n(unlike the geometric's pure decay)",
                xy=(0, probs[0]), xytext=(7.4, 0.075),
                fontsize=10.5, color=KANTO_GRAY,
                arrowprops=dict(arrowstyle="->", color=KANTO_GRAY, lw=1.2))

    ax.set_xticks(ks)
    ax.set_xlabel(r"$k$  (losses before the $r=3$rd success)")
    ax.set_ylabel(r"$P(X = k) = \binom{k+r-1}{k}p^{r}q^{k}$")
    ax.set_title(r"Negative Binomial$(r=3,\ p=0.4)$ pmf — rise, then geometric-like tail")
    ax.set_ylim(0, 0.185)
    ax.set_xlim(-0.6, 15.6)
    ax.grid(axis="x", visible=False)

    fig.tight_layout()
    out = OUT / "ch08_negbin_pmf.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
def fig_hypergeom_split():
    """Structural diagram: choose k from K successes and n-k from N-K failures, over C(N,n)."""
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.2)
    ax.axis("off")

    from matplotlib.patches import FancyBboxPatch, Circle

    # --- The pool: N=12, K=4 Gloom (rare), 8 fillers --------------------------
    ax.text(5, 5.9, r"The pool: $N = 12$", ha="center",
            fontsize=13, fontweight="bold", color=INK)

    # draw 12 tokens: 4 rare (red, hatched) + 8 filler (green)
    def token(cx, cy, rare):
        c = Circle((cx, cy), 0.28,
                   facecolor=(KANTO_RED if rare else KANTO_GREEN),
                   edgecolor=INK, linewidth=1.2, zorder=3,
                   hatch=("//" if rare else ""))
        ax.add_patch(c)

    # K=4 rare on the left block, 8 filler on the right block
    rare_xy = [(0.9, 5.0), (1.6, 5.0), (0.9, 4.3), (1.6, 4.3)]
    fill_xy = [(3.2 + 0.7 * (i % 4), 5.0 - 0.7 * (i // 4)) for i in range(8)]
    for (x, y) in rare_xy:
        token(x, y, True)
    for (x, y) in fill_xy:
        token(x, y, False)
    ax.text(1.25, 5.55, r"$K = 4$ rare", ha="center", fontsize=11, color=KANTO_RED)
    ax.text(4.6, 5.55, r"$N - K = 8$ filler", ha="center", fontsize=11, color=KANTO_GREEN)

    # --- The draw: n=3, of which k=2 rare ------------------------------------
    box = FancyBboxPatch((0.6, 1.4), 8.8, 1.9,
                         boxstyle="round,pad=0.05,rounding_size=0.15",
                         facecolor=KANTO_BG, edgecolor=INK, linewidth=1.4, zorder=1)
    ax.add_patch(box)
    ax.text(5, 3.55, r"Draw $n = 3$ without replacement, want $k = 2$ rare",
            ha="center", fontsize=12.5, fontweight="bold", color=INK)

    # the chosen 2 rare
    token(1.6, 2.4, True)
    token(2.4, 2.4, True)
    ax.text(2.0, 1.75, r"$\binom{K}{k}=\binom{4}{2}=6$ ways", ha="center",
            fontsize=11.5, color=KANTO_RED)

    # the chosen 1 filler
    token(6.4, 2.4, False)
    ax.text(6.9, 1.75, r"$\binom{N-K}{n-k}=\binom{8}{1}=8$ ways", ha="center",
            fontsize=11.5, color=KANTO_GREEN)

    ax.text(4.4, 2.4, r"$\times$", ha="center", va="center",
            fontsize=20, color=INK)

    # --- The formula bar ------------------------------------------------------
    ax.text(5, 0.6,
            r"$P(X=2)=\frac{\binom{4}{2}\binom{8}{1}}{\binom{12}{3}}"
            r"=\frac{6\cdot 8}{220}=\frac{48}{220}$",
            ha="center", fontsize=14, color=INK)

    fig.tight_layout()
    out = OUT / "ch08_hypergeom_split.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
def poisson_pmf(k, lam):
    return math.exp(-lam) * lam**k / math.factorial(k)


def fig_poisson_pmf():
    """Two Poisson pmfs: lambda=3 (one min) and lambda=15 (five min, left tail k<=9)."""
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(12, 5.3))

    # --- Left: lambda = 3, one minute -------------------------------------
    lamL = 3
    ksL = np.arange(0, 13)
    pL = np.array([poisson_pmf(int(k), lamL) for k in ksL])
    axL.bar(ksL, pL, width=0.74, color=KANTO_BLUE, edgecolor=INK,
            linewidth=1.0, zorder=3)
    axL.axvline(lamL, color=INK, linestyle="--", linewidth=1.7, zorder=4)
    axL.annotate(r"mean $=\lambda = 3$", xy=(3, 0.235), xytext=(5.2, 0.215),
                 fontsize=11.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.3))
    axL.annotate("long thin right tail\n(no upper bound)", xy=(9, 0.012),
                 xytext=(6.2, 0.10), fontsize=10.5, color=KANTO_GRAY,
                 arrowprops=dict(arrowstyle="->", color=KANTO_GRAY, lw=1.2))
    axL.set_xticks(ksL[::2])
    axL.set_xlabel(r"$k$  (ghosts in one minute)")
    axL.set_ylabel(r"$P(X = k)$")
    axL.set_title(r"Poisson$(\lambda = 3)$ — one minute")
    axL.set_ylim(0, 0.26)
    axL.grid(axis="x", visible=False)

    # --- Right: lambda = 15, five minutes; shade left tail k<=9 -----------
    lamR = 15
    ksR = np.arange(0, 33)
    pR = np.array([poisson_pmf(int(k), lamR) for k in ksR])
    tail = ksR <= 9
    colors = np.where(tail, KANTO_RED, KANTO_BLUE)
    bars = axR.bar(ksR, pR, width=0.74, color=list(colors), edgecolor=INK,
                   linewidth=1.0, zorder=3)
    for b, t in zip(bars, tail):
        if t:
            b.set_hatch("//")
    axR.axvline(lamR, color=INK, linestyle="--", linewidth=1.7, zorder=4)
    axR.annotate(r"mean $=\lambda = 15$", xy=(15, 0.108), xytext=(19, 0.095),
                 fontsize=11.5, color=INK,
                 arrowprops=dict(arrowstyle="->", color=INK, lw=1.3))
    axR.annotate(r"left tail $k\leq 9$:  $P(Y<10)=0.0699$",
                 xy=(7, 0.020), xytext=(0.5, 0.064),
                 fontsize=11, color=KANTO_RED,
                 arrowprops=dict(arrowstyle="->", color=KANTO_RED, lw=1.4))
    axR.set_xticks(ksR[::4])
    axR.set_xlabel(r"$k$  (ghosts in five minutes)")
    axR.set_ylabel(r"$P(Y = k)$")
    axR.set_title(r"Poisson$(\lambda = 15)$ — five minutes")
    axR.set_ylim(0, 0.118)
    axR.grid(axis="x", visible=False)

    from matplotlib.patches import Patch
    axR.legend(handles=[
        Patch(facecolor=KANTO_RED, edgecolor=INK, hatch="//",
              label=r"$k \leq 9$  (the lull, $0.0699$)"),
        Patch(facecolor=KANTO_BLUE, edgecolor=INK, label=r"$k \geq 10$"),
    ], loc="upper right")

    fig.suptitle("Poisson counts have no upper limit — rescale $\\lambda$ to the window",
                 fontsize=15, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    out = OUT / "ch08_poisson_pmf.png"
    fig.savefig(out, dpi=DPI)
    plt.close(fig)
    return out


# ---------------------------------------------------------------------------
def main():
    written = [fig_bernoulli_pmf(), fig_binomial_pmf(), fig_geometric_pmf(),
               fig_negbin_pmf(), fig_hypergeom_split(), fig_poisson_pmf()]
    for w in written:
        print(w)


if __name__ == "__main__":
    main()
