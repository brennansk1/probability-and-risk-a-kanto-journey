#!/usr/bin/env python3
"""Generate every Chapter 6 (Deductibles & Limits, DISCRETE / Fuchsia & the Safari Zone /
Koga) figure.

Manifest (MASTER_PLAN_V3 §16/§30, DESIGN_BLUEPRINT ch06 row) — three diagrams into
assets/diagrams/:
  ch06_deductible_limit   payment-vs-loss STEP picture: the per-loss payment under a
                          deductible d and a maximum covered loss u, drawn as the layer
                          between d and u. Composites the real Safari Ball item glyph.
  ch06_payment_per_loss   the per-loss vs per-payment distinction: the lump of probability
                          at payment 0 (losses that never clear the deductible) vs the
                          conditional distribution among actual payments. Composites the
                          real Poke Ball item glyph.
  ch06_safari_budget      the master identity E[X^u] + E[(X-d)+] split of the loss into
                          "what the limit keeps" and "the excess", as a stacked
                          survival-bar budget. Composites real Tauros #128 + Kangaskhan #115.

This is the DISCRETE deductible chapter (A.6.1-A.6.3); the continuous calculus version is
ch13. Every loss here is a non-negative integer RV with a given pmf, so all expectations
are finite sums (no integrals) and every figure reads off a table.

PRINT TARGET: bound book -> every PNG at 300 DPI.
INSTRUCTIONAL CLARITY: color-blind-safe Kanto palette; every color-coded element is ALSO
distinguished by a hatch / text label so figures survive grayscale (color never the sole
channel). Real Pokemon / item art obeys the IRON RULE: margins/corners only, never over a
bar, step, axis, equation, or number a reader must read.

Run: python3 figures/src/gen_ch06.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from cycler import cycler

from sprite_util import front, item, place_sprite
from type_palette import chapter_accent

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = ROOT / "assets" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

plt.style.use(str(HERE / "kanto_theme.mplstyle"))

# Kanto palette (color-blind-safe trio + accents).
KANTO_RED, KANTO_BLUE, KANTO_YEL, KANTO_GREEN, KANTO_GRAY, KANTO_BG = (
    "#EE1515", "#3B4CCA", "#FFD733", "#4DAD5B", "#888888", "#FAFAF5")
POISON = chapter_accent(6)  # §17 Poison accent (#A040A0) — banner/figure parity.
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


# ---------------------------------------------------------------------------
# The shared Safari-Zone loss random variable used across the chapter & figures.
#   X = gear-loss (thousands of Poke-dollars) when a Safari Pokemon flees,
#   X in {0,1,2,3,4,5}, pmf below (sums to 1).
#   E[X]              = 1.56
#   S(j) = P(X>j)     = 0.70, 0.45, 0.25, 0.12, 0.04, 0
#   deductible d=2 :  E[(X-2)+] = 0.41 = S(2)+S(3)+S(4) = 0.25+0.12+0.04
#   limit      u=3 :  E[X^3]    = 1.40 = S(0)+S(1)+S(2) = 0.70+0.45+0.25
#   identity      :  E[X^u] + E[(X-u)+] = E[X]  for every u.
# ---------------------------------------------------------------------------
LOSS_K = [0, 1, 2, 3, 4, 5]
LOSS_PMF = [0.30, 0.25, 0.20, 0.13, 0.08, 0.04]
DEDUCT = 2
LIMIT = 3


def _survival(pmf, support):
    return [sum(pi for ki, pi in zip(support, pmf) if ki > j) for j in support]


SURV = _survival(LOSS_PMF, LOSS_K)            # S(0..5)
EX = sum(k * p for k, p in zip(LOSS_K, LOSS_PMF))  # 1.56


def _payment(x, d, u):
    """Per-loss payment under deductible d then maximum covered loss u: the layer
    of the loss between d and u, i.e. (x ^ u) - (x ^ d) = ((x-d)+ capped so the
    loss above u is not covered)."""
    return min(x, u) - min(x, d)


# ===========================================================================
# 1. ch06_deductible_limit — payment vs loss, as a STEP function.
#    For each loss level k, plot the per-loss payment g(k) = (k^u) - (k^d):
#    flat 0 up to the deductible, rises 1-for-1 through the covered layer, flat
#    at (u - d) once the loss clears the maximum covered loss. Real Safari Ball
#    composited in the top-left margin (iron rule).
# ===========================================================================
def fig_deductible_limit():
    d, u = DEDUCT, LIMIT
    xs = list(range(0, 7))
    pay = [_payment(x, d, u) for x in xs]          # 0,0,0,1,1,1,1

    fig, ax = plt.subplots(figsize=(10.6, 6.2))
    ax.set_title("Payment vs. loss — a deductible knocks off the bottom, a limit caps the top\n"
                 f"per-loss payment $g(X)=(X\\wedge {u})-(X\\wedge {d})$  "
                 f"(Safari gear-loss, $d={d}$, $u={u}$)", fontsize=12.5)

    # the 45-degree "if the policy paid the whole loss" reference line.
    ax.plot([0, 6], [0, 6], ls="--", lw=1.6, color=KANTO_GRAY, zorder=2,
            label="if policy paid the full loss  ($y=x$)")

    # the actual per-loss payment as a step (where='post' = right-continuous in k).
    ax.step(xs + [6.0], pay + [pay[-1]], where="post", lw=2.8, color=POISON,
            zorder=4, label="per-loss payment  $g(k)$")
    ax.plot(xs, pay, "o", color=POISON, ms=7, zorder=5)

    # shaded covered layer band between d and u.
    ax.axvspan(d, u, color=KANTO_GREEN, alpha=0.12, zorder=1)
    ax.axvline(d, color=KANTO_BLUE, lw=1.8, ls=":", zorder=3)
    ax.axvline(u, color=KANTO_RED, lw=1.8, ls=":", zorder=3)

    ax.text(d, 4.55, f"deductible $d={d}$\n(trainer eats this)", ha="center",
            va="bottom", fontsize=9.5, color=KANTO_BLUE, fontweight="bold")
    ax.text(u, 5.55, f"max covered loss $u={u}$", ha="center", va="bottom",
            fontsize=9.5, color=KANTO_RED, fontweight="bold")
    ax.text((d + u) / 2, 0.55, "covered\nlayer", ha="center", va="center",
            fontsize=9.5, color=KANTO_GREEN, fontweight="bold")
    ax.annotate("pays $0$ until the\nloss clears $d$", xy=(0.7, 0.04),
                xytext=(0.15, 2.4), fontsize=9, color=POISON,
                arrowprops=dict(arrowstyle="->", color=POISON, lw=1.6))
    ax.annotate(f"flat at $u-d={u - d}$:\nexcess over $u$ not covered",
                xy=(5.0, u - d), xytext=(4.0, 3.0), fontsize=9, color=POISON,
                arrowprops=dict(arrowstyle="->", color=POISON, lw=1.6))

    ax.set_xlim(-0.3, 6.2)
    ax.set_ylim(0, 6.2)
    ax.set_xlabel("loss  $X$  (thousands)")
    ax.set_ylabel("per-loss payment")
    ax.set_xticks(xs)
    ax.set_yticks(range(0, 7))
    ax.grid(alpha=0.35)
    ax.legend(loc="upper left", bbox_to_anchor=(0.005, 0.86), fontsize=8.6,
              framealpha=0.95)

    # Safari Ball in the upper-left margin — clear of every step/line/number.
    place_sprite(ax, item("safari-ball"), (0.065, 0.955),
                 xycoords="axes fraction", zoom=1.5, zorder=6)

    fig.tight_layout()
    return save(fig, "ch06_deductible_limit")


# ===========================================================================
# 2. ch06_payment_per_loss — per-loss vs per-payment.
#    LEFT: the per-loss payment pmf with its big lump at 0 (every flee that never
#    clears the deductible records a 0 payment). RIGHT: the per-payment pmf — the
#    SAME distribution with the zeros dropped and renormalized by P(X>d). The two
#    means differ by exactly the factor S(d). Real Poke Ball in the top-right margin.
# ===========================================================================
def fig_payment_per_loss():
    d = DEDUCT
    # per-loss payment values g(k) = (k - d)+ (no limit here: focus is the zero lump)
    pay_vals = [max(k - d, 0) for k in LOSS_K]     # 0,0,0,1,2,3
    # per-loss payment pmf: collapse equal payment values.
    perloss = {}
    for v, p in zip(pay_vals, LOSS_PMF):
        perloss[v] = perloss.get(v, 0.0) + p
    Sd = SURV[d]                                    # P(X>d)=S(2)=0.25
    # per-payment pmf: drop the 0 payments, renormalize by P(X>d).
    perpay = {v: p / Sd for v, p in perloss.items() if v > 0}

    fig, axes = plt.subplots(1, 2, figsize=(12.4, 5.4), sharey=False)
    fig.suptitle("Two different averages of the SAME policy: per loss vs. per payment "
                 f"(deductible $d={d}$)", fontsize=13, fontweight="bold", y=1.01)

    Eperloss = sum(v * p for v, p in perloss.items())
    Eperpay = sum(v * p for v, p in perpay.items())

    # --- LEFT: per-loss (counts the zeros) ---
    ax = axes[0]
    vs = sorted(perloss)
    ps = [perloss[v] for v in vs]
    bars = ax.bar(vs, ps, width=0.6, color=POISON, edgecolor=INK, lw=1.3,
                  hatch="..", zorder=3)
    # highlight the zero lump.
    bars[0].set_facecolor(KANTO_GRAY)
    bars[0].set_alpha(0.85)
    for v, p in zip(vs, ps):
        ax.text(v, p + 0.012, f"{p:.2f}", ha="center", va="bottom", fontsize=9,
                color=INK)
    ax.annotate("lump at $0$: every loss\n$\\leq d$ records a $0$ payment\n"
                f"$P(\\text{{pay}}=0)=F(d)={1 - Sd:.2f}$",
                xy=(0, perloss[0]), xytext=(0.55, 0.50), fontsize=8.8,
                color=KANTO_GRAY, fontweight="bold",
                arrowprops=dict(arrowstyle="->", color=KANTO_GRAY, lw=1.6))
    ax.set_title("PER LOSS  $Y_L=(X-d)_+$\ncounts every flee, zeros included",
                 fontsize=10.8)
    ax.set_xlabel("payment")
    ax.set_ylabel("probability")
    ax.set_xticks(vs)
    ax.set_ylim(0, 0.85)
    ax.grid(axis="y", alpha=0.4)
    ax.text(0.97, 0.80, f"$E[Y_L]={Eperloss:.2f}$", transform=ax.transAxes,
            ha="right", va="top", fontsize=12, color=POISON, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=POISON, lw=1.4))

    # --- RIGHT: per-payment (zeros dropped, renormalized) ---
    ax = axes[1]
    vs2 = sorted(perpay)
    ps2 = [perpay[v] for v in vs2]
    ax.bar(vs2, ps2, width=0.6, color=KANTO_BLUE, edgecolor=INK, lw=1.3,
           hatch="//", zorder=3)
    for v, p in zip(vs2, ps2):
        ax.text(v, p + 0.012, f"{p:.2f}", ha="center", va="bottom", fontsize=9,
                color=INK)
    ax.set_title("PER PAYMENT  $(X-d\\mid X>d)$\nonly the flees that actually pay",
                 fontsize=10.8)
    ax.set_xlabel("payment")
    ax.set_ylabel("probability")
    ax.set_xticks([0] + vs2)
    ax.set_xlim(-0.6, max(vs2) + 0.6)
    ax.set_ylim(0, 0.85)
    ax.grid(axis="y", alpha=0.4)
    ax.text(0.97, 0.80, f"$E[Y_P]={Eperpay:.2f}$", transform=ax.transAxes,
            ha="right", va="top", fontsize=12, color=KANTO_BLUE,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=KANTO_BLUE,
                      lw=1.4))
    ax.text(0.5, 0.55,
            f"divide out the zeros:\n"
            f"$E[Y_P]=\\dfrac{{E[Y_L]}}{{P(X>d)}}=\\dfrac{{{Eperloss:.2f}}}{{{Sd:.2f}}}"
            f"={Eperpay:.2f}$",
            transform=ax.transAxes, ha="center", va="center", fontsize=9.6,
            color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc="#EEF3FF", ec=KANTO_BLUE,
                      lw=1.2))
    # Poke Ball in the top-right margin of the right panel.
    place_sprite(ax, item("poke-ball"), (0.93, 0.955),
                 xycoords="axes fraction", zoom=1.5, zorder=6)

    fig.tight_layout()
    return save(fig, "ch06_payment_per_loss")


# ===========================================================================
# 3. ch06_safari_budget — the master identity, as a survival-bar budget.
#    The mean E[X] is the sum of the survival bars S(0..). A cut at u splits that
#    total area into the "limit keeps" part (bars left of u  ->  E[X^u]) and the
#    "excess" part (bars at/after u  ->  E[(X-u)+]). The two add back to E[X].
#    Real Tauros #128 + Kangaskhan #115 in the margins (the Safari Zone marquee).
# ===========================================================================
def fig_safari_budget():
    u = LIMIT
    surv = SURV[:]                                  # S(0..5); S(5)=0
    terms = surv[:-1]                               # nonzero terms S(0..4)
    Exu = sum(terms[:u])                            # E[X^u] = S(0)+...+S(u-1)
    Eexcess = sum(terms[u:])                        # E[(X-u)+] = S(u)+S(u+1)+...

    fig, ax = plt.subplots(figsize=(10.8, 6.2))
    ax.set_title("The Warden's budget identity:  "
                 "$E[X\\wedge u]+E[(X-u)_+]=E[X]$\n"
                 f"each survival bar $S(k)$ is one Poke-dollar of expected loss "
                 f"(cut at the limit $u={u}$)", fontsize=12)

    labels = [f"S({k})" for k in range(len(terms))]
    for k, (s, lab) in enumerate(zip(terms, labels)):
        kept = k < u
        fc = KANTO_GREEN if kept else KANTO_RED
        hatch = "//" if kept else "xx"
        ax.add_patch(Rectangle((k, 0), 1.0, s, facecolor=fc, edgecolor=INK,
                               lw=1.3, alpha=0.55, hatch=hatch, zorder=2))
        ax.text(k + 0.5, s + 0.02, f"${lab}={s:.2f}$", ha="center", va="bottom",
                fontsize=9.5, color=INK)

    # the survival step for context.
    ax.step(list(range(len(terms))) + [len(terms)], terms + [0.0],
            where="post", color=INK, lw=2.0, alpha=0.8, zorder=4)
    ax.axvline(u, color=INK, lw=2.0, ls=":", zorder=5)
    ax.text(u, 0.93, f"limit $u={u}$", ha="center", va="bottom", fontsize=10,
            color=INK, fontweight="bold")

    ax.text(u / 2.0, 0.74,
            "kept by the limit\n"
            f"$E[X\\wedge {u}]={Exu:.2f}$",
            ha="center", va="center", fontsize=10.5, color=KANTO_GREEN,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="#E7F6EA", ec=KANTO_GREEN,
                      lw=1.4))
    ax.text(u + 1.4, 0.40,
            "excess over $u$\n"
            f"$E[(X-{u})_+]={Eexcess:.2f}$",
            ha="center", va="center", fontsize=10.5, color=KANTO_RED,
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", fc="#FCEAEA", ec=KANTO_RED,
                      lw=1.4))
    ax.text(0.5, 0.965,
            f"green $+$ red $={Exu:.2f}+{Eexcess:.2f}={EX:.2f}=E[X]$ — "
            "the whole loss, split in two.",
            transform=ax.transAxes, ha="center", va="top", fontsize=10.2,
            color=INK,
            bbox=dict(boxstyle="round,pad=0.35", fc="#FFF6D6", ec=KANTO_YEL,
                      lw=1.5))

    ax.set_xlim(-0.3, 6.4)
    ax.set_ylim(0, 1.02)
    ax.set_xlabel("$k$  (loss level, thousands)")
    ax.set_ylabel("$S(k)=P(X>k)$")
    ax.set_xticks(range(0, 6))
    ax.grid(alpha=0.3)

    # The Safari Zone marquee species in the right margin (iron rule: clear of bars).
    place_sprite(ax, front(128), (0.90, 0.74), xycoords="axes fraction",
                 zoom=0.40, alpha=0.95, zorder=6)   # Tauros
    place_sprite(ax, front(115), (0.90, 0.50), xycoords="axes fraction",
                 zoom=0.40, alpha=0.95, zorder=6)   # Kangaskhan

    fig.tight_layout()
    return save(fig, "ch06_safari_budget")


REGISTRY = [
    fig_deductible_limit,
    fig_payment_per_loss,
    fig_safari_budget,
]


def main() -> None:
    print(f"Generating Chapter 6 (Deductibles & Limits, discrete) figures -> {OUT} "
          f"at {PRINT_DPI} DPI")
    written = [fn() for fn in REGISTRY]
    print(f"Done. {len(written)} figures written.")


if __name__ == "__main__":
    main()
