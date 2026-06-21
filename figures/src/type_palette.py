"""Single source of truth for Pokemon type colors (V3 §17) and per-chapter accents.

Keep the 18 TYPE hex values in sync with the `:root` custom properties in
book/theme.css (the asset audit checks parity). gen_chNN.py figures import
CHAPTER_ACCENT[nn] to tint that chapter's figure accent; the chapter banner
uses the same color.
"""

# 18 canonical type colors.
TYPE_COLOR = {
    "normal":   "#A8A878",
    "fire":     "#F08030",
    "water":    "#6890F0",
    "electric": "#F8D030",
    "grass":    "#78C850",
    "ice":      "#98D8D8",
    "fighting": "#C03028",
    "poison":   "#A040A0",
    "ground":   "#E0C068",
    "flying":   "#A890F0",
    "psychic":  "#F85888",
    "bug":      "#A8B820",
    "rock":     "#B8A038",
    "ghost":    "#705898",
    "dragon":   "#7038F8",
    "dark":     "#705848",
    "steel":    "#B8B8D0",
    "fairy":    "#EE99AC",
}

# Per-chapter accent type (V3 §15 journey throughline). Chapter index -> type name.
CHAPTER_TYPE = {
    0:  "normal",    # Pallet Town
    1:  "flying",    # Route 1 — Spearow swarm
    2:  "water",     # Cerulean / Misty
    3:  "electric",  # S.S. Anne -> Vermilion / Lt. Surge
    4:  "rock",      # Viridian Forest / Pewter / Brock
    5:  "ghost",     # Lavender Tower (Gastly) / Celadon / Erika
    6:  "poison",    # Fuchsia / Safari Zone / Koga
    7:  "normal",    # Checkpoint A
    8:  "steel",     # Calculus toolkit (HMs / machines)
    9:  "psychic",   # Saffron / Sabrina
    10: "psychic",   # Saffron / Silph Co.
    11: "water",     # the smooth continuous wilds
    12: "normal",    # the Normal distribution + CLT
    13: "fire",      # Cinnabar Lab / volcano
    14: "fire",      # Cinnabar Mansion / Blaine
    15: "ground",    # Victory Road
    16: "ground",    # Viridian Gym / Giovanni
    17: "ice",       # Indigo Plateau / Elite Four
    18: "normal",    # Checkpoint B
    19: "dragon",    # Championship = the exam
}


def chapter_accent(ch: int) -> str:
    """Hex accent color for chapter `ch` (falls back to normal)."""
    return TYPE_COLOR[CHAPTER_TYPE.get(ch, "normal")]
