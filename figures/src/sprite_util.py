"""Helpers to composite Pokémon art into matplotlib figures.

Use these so sprites are placed consistently and stay crisp. THE IRON RULE: art
decorates, it never obscures the math — place sprites in margins, atop bars, beside
labels or inside region corners, never over a curve, equation, or axis a reader must
read. Keep zoom small and, where it competes with data, alpha < 1.

  from sprite_util import front, official, item, place_sprite
  place_sprite(ax, front(25), (x, y), zoom=0.45)      # Pikachu pixel sprite at data (x,y)
  place_sprite(ax, item("safari-ball"), (0.9, 0.1), xycoords="axes fraction", zoom=1.1)
"""
from __future__ import annotations
from pathlib import Path
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

ASSETS = Path(__file__).resolve().parent.parent.parent / "assets"


def front(dex: int) -> Path:
    """96px Gen-1 pixel sprite (small, iconic — best for in-figure use)."""
    return ASSETS / "sprites" / "front" / f"{dex}.png"


def official(dex: int) -> Path:
    """High-res official artwork (~475px — for big/header placements)."""
    return ASSETS / "sprites" / "official" / f"{dex}.png"


def item(name: str) -> Path:
    """Item sprite, e.g. 'poke-ball', 'safari-ball', 'master-ball', 'potion'."""
    return ASSETS / "items" / f"{name}.png"


def place_sprite(ax, path, xy, zoom=0.5, xycoords="data",
                 box_alignment=(0.5, 0.5), alpha=1.0, zorder=5, pixelated=True):
    """Drop a sprite onto `ax` at `xy`. Returns the AnnotationBbox (None if missing)."""
    p = Path(path)
    if not p.exists():
        return None
    img = mpimg.imread(str(p))
    oi = OffsetImage(img, zoom=zoom,
                     interpolation="nearest" if pixelated else "antialiased")
    if alpha < 1.0:
        try:
            oi.get_children()[0].set_alpha(alpha)
        except Exception:
            pass
    ab = AnnotationBbox(oi, xy, frameon=False, xycoords=xycoords,
                        box_alignment=box_alignment, pad=0, zorder=zorder)
    ax.add_artist(ab)
    return ab
