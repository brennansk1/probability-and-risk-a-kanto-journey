#!/usr/bin/env python3
"""Post-process generated diagram PNGs for print + embedding.

The figure generators (figures/src/gen_ch*.py) save at 300 DPI, which for the
large physical canvases yields ~3000-4000 px PNGs. In the book those diagrams
display at <= ~600 px wide, so the native resolution is 5x more than print
needs: it bloats the embedded HTML and balloons the Chrome-rendered PDF (each
oversized bitmap is re-embedded at display size).

This step caps every diagram at MAX_PX on its longest side (still ~280 DPI at a
6" display — crisp for print and zoom) and re-encodes to an optimized 256-colour
palette PNG (diagrams are flat-colour line art, so quantisation is invisible,
especially under the display downscale). Net effect on this book: diagrams drop
from ~30 MB to ~7 MB, the workbook PDF from ~74 MB to ~29 MB, with no visible
quality loss.

Idempotent: re-running on already-optimised files is a no-op-ish (re-quantises
at the same size). Run automatically by `make figures`.

Usage: python3 tools/optimize_figures.py
"""
from __future__ import annotations

import glob
import os
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
DIAGRAMS = ROOT / "assets" / "diagrams"
MAX_PX = 1700          # longest-side cap
PALETTE_COLORS = 256


def optimize(path: str) -> tuple[int, int]:
    before = os.path.getsize(path)
    im = Image.open(path).convert("RGBA")
    w, h = im.size
    if max(w, h) > MAX_PX:
        s = MAX_PX / max(w, h)
        im = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    # flatten any transparency onto white, then quantise to a compact palette
    bg = Image.new("RGB", im.size, (255, 255, 255))
    bg.paste(im, mask=im.split()[3])
    q = bg.quantize(colors=PALETTE_COLORS, method=Image.FASTOCTREE, dither=Image.Dither.NONE)
    q.save(path, optimize=True)
    return before, os.path.getsize(path)


def main() -> None:
    files = sorted(glob.glob(str(DIAGRAMS / "*.png")))
    if not files:
        print("optimize_figures: no diagrams found (run `make figures` first)")
        return
    before = after = 0
    for p in files:
        b, a = optimize(p)
        before += b
        after += a
    print(f"optimize_figures: {len(files)} diagrams  {before/1e6:.1f}MB -> {after/1e6:.1f}MB "
          f"(cap {MAX_PX}px, {PALETTE_COLORS}-colour palette)")


if __name__ == "__main__":
    main()
