#!/usr/bin/env python3
"""Download EXTRA Pokémon art from PokeAPI/sprites for richer figures.

Adds three asset classes the book wasn't using:
  - items/         item sprites (Poké Balls, Potions, etc.) for UI glyphs + loss/Safari figures
  - sprites/official/  high-res official artwork (for chapter headers / cast at print DPI)
  - (dream-world SVGs are available too but skipped — SVG compositing needs extra deps)

Source: https://github.com/PokeAPI/sprites  (community sprite aggregation; see README/LICENSE).
All assets are for personal, educational, non-commercial use; not relicensed. Idempotent
(skips existing non-empty files), so safe to re-run.

Usage: python assets/download_extra_assets.py
"""
from __future__ import annotations
from pathlib import Path
import sys, time

try:
    import requests
except ImportError:
    sys.exit("requests required: pip install requests")

ROOT = Path(__file__).resolve().parent
RAW = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites"
HEADERS = {"User-Agent": "kanto-exam-p-textbook/1.0"}
KANTO = range(1, 152)

# Items relevant to the book: the UI wayfinding glyphs + loss/Safari/poison themes.
ITEMS = [
    "poke-ball", "great-ball", "ultra-ball", "master-ball", "safari-ball", "premier-ball",
    "potion", "super-potion", "hyper-potion", "max-potion", "full-restore", "revive",
    "rare-candy", "antidote", "full-heal", "escape-rope", "exp-share", "amulet-coin",
    "thunder-stone", "fire-stone", "water-stone", "leaf-stone", "moon-stone",
]


def fetch(url: str, dest: Path) -> str:
    if dest.exists() and dest.stat().st_size > 0:
        return "skip"
    for attempt in range(3):
        try:
            r = requests.get(url, timeout=30, headers=HEADERS)
            if r.status_code == 404:
                return "404"
            r.raise_for_status()
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(r.content)
            return "ok"
        except requests.RequestException:
            time.sleep(1.5)
    return "fail"


def main() -> None:
    items_dir = ROOT / "items"
    art_dir = ROOT / "sprites" / "official"

    print("[1/2] Item sprites …")
    got = miss = 0
    for name in ITEMS:
        st = fetch(f"{RAW}/items/{name}.png", items_dir / f"{name}.png")
        if st in ("ok", "skip"): got += 1
        else: miss += 1; print(f"   {st}: {name}")
    print(f"   items: {got}/{len(ITEMS)} available")

    print("[2/2] High-res official artwork (1–151) …")
    got = 0
    for i in KANTO:
        st = fetch(f"{RAW}/pokemon/other/official-artwork/{i}.png", art_dir / f"{i}.png")
        if st in ("ok", "skip"): got += 1
    print(f"   official artwork: {got}/151")
    print("Done.")


if __name__ == "__main__":
    main()
