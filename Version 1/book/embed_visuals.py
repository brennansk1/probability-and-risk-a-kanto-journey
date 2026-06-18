"""Insert image references into the chapter markdown files (idempotent).

Adapted from the sister project (Causal Inference: A Pokemon Approach).
Each insertion is guarded by a unique HTML-comment marker, so re-running is a
no-op. Image paths are relative from a chapter file (book/chapters/*.md) so they
resolve at Pandoc time with --resource-path.

For a PRINTED/BOUND build: prefer original silhouettes over copyrighted sprites,
and ensure raster assets are >=300 DPI (see assets/upscale_assets.py). See
FORMATTING.md sec. 9 and the print notes in README.md.

Usage:
    python book/embed_visuals.py
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "book" / "chapters"

# Asset root relative to a chapter file (book/chapters/foo.md -> ../../assets)
A = "../../assets"


def insert_after(text: str, anchor: str, block: str, marker: str) -> str:
    if marker in text:
        return text
    out, inserted = [], False
    for line in text.splitlines(keepends=True):
        out.append(line)
        if not inserted and anchor in line:
            out.extend(["\n", f"<!-- {marker} -->\n", block.rstrip() + "\n\n"])
            inserted = True
    if not inserted:
        out.extend(["\n", f"<!-- {marker} -->\n", block.rstrip() + "\n"])
    return "".join(out)


# --------------------------------------------------------------------------
# Figure-builder helpers (HTML <figure> blocks)
# --------------------------------------------------------------------------
def figure(src: str, caption: str, width: str = "60%") -> str:
    return (
        f'<figure>\n'
        f'<img src="{src}" alt="{caption}" '
        f'style="width:{width}; max-width:520px; display:block; margin:1em auto;">\n'
        f'<figcaption>{caption}</figcaption>\n'
        f'</figure>\n'
    )


def diagram(name: str, caption: str, width: str = "80%") -> str:
    """A generated matplotlib figure from assets/diagrams/."""
    return figure(f"{A}/diagrams/{name}.png", caption, width)


def dist_card(name: str, caption: str = "", width: str = "70%") -> str:
    """A distribution 'trading card' (generated) reused in Ch 6-7 and Appendix B."""
    return figure(f"{A}/diagrams/card_{name}.png", caption or f"{name.title()} distribution", width)


def pokemon(dex_id: int, name: str, width: int = 140) -> str:
    return (
        f'<figure style="margin:1.5em auto; max-width:{width+20}px; text-align:center;">\n'
        f'<img src="{A}/sprites/front/{dex_id}.png" alt="{name}" '
        f'style="width:{width}px; display:block; margin:0 auto; image-rendering: pixelated;">\n'
        f'<figcaption style="font-size:0.85em;"><strong>#{dex_id:03d} {name}</strong></figcaption>\n'
        f'</figure>\n'
    )


def pokemon_row(entries, width: int = 110, caption: str = "") -> str:
    items = "".join(
        f'<figure style="margin:0; text-align:center;">\n'
        f'<img src="{A}/sprites/front/{dex_id}.png" alt="{name}" '
        f'style="width:{width}px; display:block; margin:0 auto; image-rendering: pixelated;">\n'
        f'<figcaption style="font-size:0.8em;">#{dex_id:03d} {name}</figcaption>\n'
        f'</figure>\n'
        for dex_id, name in entries
    )
    cap = (f'<p style="text-align:center; font-size:0.85em; color:#666; '
           f'font-style:italic; margin:0.25em 0 1em;">{caption}</p>\n') if caption else ""
    return (
        f'<div style="display:flex; gap:18px; flex-wrap:wrap; justify-content:center; '
        f'align-items:flex-end; margin:1.25em auto;">\n{items}</div>\n{cap}'
    )


def badge(name: str, display: str) -> str:
    return (
        f'<figure style="text-align:center; margin:1.5em auto;">\n'
        f'<img src="{A}/badges/{name}_badge.png" alt="{display} Badge" '
        f'style="width:140px; display:block; margin:0 auto;">\n'
        f'<figcaption class="badge-caption"><strong>{display} Badge earned!</strong></figcaption>\n'
        f'</figure>\n'
    )


_CHAR_EXT = {"nurse_joy": "webp"}


def character(name: str, display: str) -> str:
    # Centered block (floats overlap text in WeasyPrint/Chrome PDF output).
    ext = _CHAR_EXT.get(name, "png")
    rendering = "" if ext != "png" else " image-rendering: pixelated;"
    return (
        f'<figure style="margin:1.5em auto; max-width:160px; text-align:center;">\n'
        f'<img src="{A}/characters/{name}.{ext}" alt="{display}" '
        f'style="width:140px; display:block; margin:0 auto;{rendering}">\n'
        f'<figcaption style="font-size:0.85em;">{display}</figcaption>\n'
        f'</figure>\n'
    )


def type_icon(type_name: str, display=None, width: int = 90) -> str:
    label = display or f"{type_name.title()}-type"
    return (
        f'<figure style="margin:1em auto; max-width:{width+20}px; text-align:center;">\n'
        f'<img src="{A}/sprites/types/{type_name}.png" alt="{label}" '
        f'style="width:{width}px; display:block; margin:0 auto;">\n'
        f'<figcaption style="font-size:0.85em;">{label}</figcaption>\n'
        f'</figure>\n'
    )


# --------------------------------------------------------------------------
# Per-chapter insertions. Add edit_chNN() functions as chapters are written;
# the workflow's figure stage appends to this registry.
# --------------------------------------------------------------------------
INSERTIONS: dict = {
    # "ch08_fuchsia_safari.md": [
    #     ("# Chapter 8", character("koga", "Koga, Fuchsia Gym Leader"), "FIG-CH08-KOGA"),
    #     ("## The Gym Battle", badge("soul", "Soul"), "FIG-CH08-BADGE"),
    # ],
}


def main() -> None:
    if not INSERTIONS:
        print("No insertions registered yet. Populate INSERTIONS as chapters are written.")
        return
    for fname, edits in INSERTIONS.items():
        f = CHAPTERS / fname
        if not f.exists():
            print(f"  [skip] {fname} (not found)")
            continue
        text = f.read_text()
        for anchor, block, marker in edits:
            text = insert_after(text, anchor, block, marker)
        f.write_text(text)
        print(f"  [ok]  {fname}")


if __name__ == "__main__":
    main()
