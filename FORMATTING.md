# Formatting & Asset Pipeline — How This Book Is Built

This document records the exact, **already-proven** formatting and asset machinery used by the sister project *Causal Inference: A Pokémon Approach* (Kanto Region Edition), located at
`/Users/brennankelley/Desktop/Projects/Causal Inference Textbook/Kanto`.
We are reusing that pipeline wholesale for *Probability & Risk: A Kanto Journey*. Everything below is transcribed from that working repo so a writer can reproduce it without reopening the source.

**The pipeline in one line:** chapters are authored as **Markdown** with `$…$` LaTeX math and raw inline HTML `<figure>` blocks for images; a Python script (`embed_visuals.py`) injects those figure blocks idempotently; **Pandoc** converts Markdown → a single self-contained HTML file with **MathJax**; a **CSS stylesheet** (`textbook.css`) styles everything for print; and **WeasyPrint or headless Chrome** renders that HTML → the final PDF. A `Makefile` orchestrates it.

---

## 1. The toolchain (Markdown → Pandoc → HTML/CSS → PDF)

The canonical source is **Markdown**, not LaTeX. Math is written with dollar-sign delimiters and rendered by **MathJax** at the HTML step. Styling is **CSS** (print stylesheet with `@page` rules), not a LaTeX class. Two PDF rendering paths exist:

1. **Pandoc → LaTeX (xelatex)** — a traditional `--pdf-engine=xelatex` path with a `template.tex`. Present but secondary.
2. **Pandoc → self-contained HTML → WeasyPrint / Chrome headless** — the **primary, working** path that produced the shipped 8 MB illustrated PDF. This is the one we adopt.

### Required tools

- `pandoc` (≥ 2.11, with `--citeproc`)
- A TeX distribution with `xelatex` (only for the secondary LaTeX path)
- `weasyprint` **or** Google Chrome (the Makefile falls back to Chrome headless if WeasyPrint's native libs are missing)
- Python 3 with `matplotlib`, `requests`, `tqdm` (for figure generation and sprite downloads)

### The exact Pandoc invocation (primary HTML-for-PDF path)

```
pandoc \
  --from=markdown+smart+tex_math_dollars+footnotes \
  --standalone --embed-resources \
  --css=textbook.css \
  --mathjax \
  --toc --toc-depth=2 \
  --resource-path=.:../../textbook/chapters:../../assets \
  --include-before-body=title.html \
  --metadata title="..." \
  -o output/book_for_pdf.html  ch01.md ch02.md ... appendix_*.md
```

Key flags to carry over:

- `--embed-resources` (a.k.a. `--self-contained`) — inlines every image and the CSS into one HTML file so the PDF renderer needs no external paths. **This is why the figure `src` paths must resolve at Pandoc time.**
- `--mathjax` — math is rendered client-side; WeasyPrint/Chrome then rasterizes it.
- `--resource-path=.:../../textbook/chapters:../../assets` — lets relative image paths like `../../assets/sprites/front/25.png` resolve from either the chapter dir or the build dir.
- `tex_math_dollars` — enables `$…$` / `$$…$$` math in Markdown.

### HTML → PDF conversion (from the Makefile)

```sh
if command -v weasyprint >/dev/null 2>&1; then
    weasyprint book_for_pdf.html book.pdf
elif [ -x "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" ]; then
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
        --headless --disable-gpu --no-pdf-header-footer \
        --virtual-time-budget=30000 \
        --print-to-pdf="$PWD/book.pdf" \
        "file://$PWD/book_for_pdf.html"
fi
```

The `--virtual-time-budget=30000` gives MathJax 30 s to typeset before Chrome prints.

---

## 2. How LaTeX / math is written

Math lives **inline in the Markdown** using standard delimiters — no separate `.tex` files for content:

- Inline: `$\tau_i = Y_i(1) - Y_i(0)$`
- Display: `$$\tau = E[Y_i(1) - Y_i(0)] = E[Y_i(1)] - E[Y_i(0)]$$`
- Multi-line aligned environments work because MathJax supports them, e.g. `\underbrace{...}_{\text{...}}`, `\perp\!\!\!\perp` for independence, `\mid` for the conditional bar.

Example transcribed from `ch02_pewter_city.md`:

```markdown
$$Y_i = D_i \cdot Y_i(1) + (1 - D_i) \cdot Y_i(0)$$

where $D_i \in \{0, 1\}$ is the treatment indicator.
```

**Implication for our book:** all the Exam P math (gamma integrals, `$E[X\wedge u]$`, `$(X-d)_+$`, MGFs, `$\Phi(z)$`) is written directly in the chapter Markdown with `$…$`. The `macros.tex` shorthands described in `DESIGN.md` §4.1 can be supplied to MathJax via a small `\newcommand` block in a per-file or global preamble if we want `\E`, `\Var`, etc.; otherwise write them out longhand. (MathJax accepts `\newcommand` definitions placed inside a `$$…$$` block at the top of the first chapter.)

---

## 3. How sprites & images are inserted

Images are **raw HTML `<figure>` blocks embedded in the Markdown**, generated and injected by a Python script — they are *not* Markdown `![]()` syntax. This gives precise control over width, centering, captions, and pixel-art rendering.

### The injector: `embed_visuals.py`

A single idempotent script writes figure blocks into each chapter file. Its design (worth copying exactly):

- **Idempotent via unique HTML-comment markers.** Each insertion is guarded by a marker like `<!-- FIG-CH02-ONIX -->`. Re-running the script is a no-op if the marker is already present:

  ```python
  def insert_after(text, anchor, block, marker):
      if marker in text:
          return text          # already inserted — skip
      # ...find the first line containing `anchor`, insert block after it
  ```

- **`anchor`** is a substring of an existing line (usually a heading like `"# Chapter 2:"` or `"## 5.3"`). The block is inserted immediately after the first matching line; if no match, it appends at end.

- **Relative asset root** is `A = "../../assets"`, written so paths resolve from `textbook/chapters/*.md`.

### The figure-builder helpers (transcribe these)

```python
A = "../../assets"

def figure(src, caption, width="60%"):
    return (
        f'<figure>\n'
        f'<img src="{src}" alt="{caption}" '
        f'style="width:{width}; max-width:520px; display:block; margin:1em auto;">\n'
        f'<figcaption>{caption}</figcaption>\n'
        f'</figure>\n'
    )

def pokemon(dex_id, name, width=140):
    """Centered single sprite, captioned with Pokédex number. Pixel-art rendering."""
    return (
        f'<figure style="margin:1.5em auto; max-width:{width+20}px; text-align:center;">\n'
        f'<img src="{A}/sprites/front/{dex_id}.png" alt="{name}" '
        f'style="width:{width}px; display:block; margin:0 auto; image-rendering: pixelated;">\n'
        f'<figcaption style="font-size:0.85em;"><strong>#{dex_id:03d} {name}</strong></figcaption>\n'
        f'</figure>\n'
    )

def pokemon_row(entries, width=110, caption=""):
    """Horizontal flex row of sprites. `entries` = list of (dex_id, name)."""
    items = "".join(
        f'<figure style="margin:0; text-align:center;">\n'
        f'<img src="{A}/sprites/front/{dex_id}.png" alt="{name}" '
        f'style="width:{width}px; display:block; margin:0 auto; image-rendering: pixelated;">\n'
        f'<figcaption style="font-size:0.8em;">#{dex_id:03d} {name}</figcaption>\n'
        f'</figure>\n'
        for dex_id, name in entries
    )
    return (
        f'<div style="display:flex; gap:18px; flex-wrap:wrap; '
        f'justify-content:center; align-items:flex-end; margin:1.25em auto;">\n'
        f'{items}</div>\n'
    )

def badge(name, display):
    return (
        f'<figure style="text-align:center; margin:1.5em auto;">\n'
        f'<img src="{A}/badges/{name}_badge.png" alt="{display} Badge" '
        f'style="width:140px; display:block; margin:0 auto;">\n'
        f'<figcaption><strong>{display} Badge earned!</strong></figcaption>\n'
        f'</figure>\n'
    )

def character(name, display, side="right"):
    """Character portrait, centered block (floats overlap text in WeasyPrint, so don't float)."""
    ext = {"nurse_joy": "webp"}.get(name, "png")
    rendering = "" if ext != "png" else " image-rendering: pixelated;"
    return (
        f'<figure style="margin:1.5em auto; max-width:160px; text-align:center;">\n'
        f'<img src="{A}/characters/{name}.{ext}" alt="{display}" '
        f'style="width:140px; display:block; margin:0 auto;{rendering}">\n'
        f'<figcaption style="font-size:0.85em;">{display}</figcaption>\n'
        f'</figure>\n'
    )

def type_icon(type_name, display=None, width=90):
    label = display or f"{type_name.title()}-type"
    return (
        f'<figure style="margin:1em auto; max-width:{width+20}px; text-align:center;">\n'
        f'<img src="{A}/sprites/types/{type_name}.png" alt="{label}" '
        f'style="width:{width}px; display:block; margin:0 auto;">\n'
        f'<figcaption style="font-size:0.85em;">{label}</figcaption>\n'
        f'</figure>\n'
    )
```

### Two lessons baked into the source (don't relearn them)

1. **`image-rendering: pixelated`** on the Gen-1 sprites keeps the pixel art crisp when scaled up. Smooth art (e.g. the `.webp` Nurse Joy portrait) deliberately omits it.
2. **No floated figures.** The `character()` helper keeps a `side` argument for backward-compat but ignores it: *"floated figures overlap adjacent text in weasyprint/Chrome PDF output, so character portraits render as centered block figures instead."* Use centered block `<figure>`s everywhere.

### A rendered example (from `ch02_pewter_city.md` after injection)

```html
<!-- FIG-CH02-ONIX -->
<figure style="margin:1.5em auto; max-width:180px; text-align:center;">
<img src="../../assets/sprites/front/95.png" alt="Onix"
     style="width:160px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#095 Onix</strong></figcaption>
</figure>
```

---

## 4. Where the assets come from (download scripts)

Assets live under `assets/` and are fetched by scripts, not committed art:

```
assets/
├── sprites/front/{1..151}.png   # Gen-1 front sprites, named by Pokédex number
├── sprites/types/{type}.png     # type icons (rock, electric, grass, …)
├── sprites/icons/
├── characters/{name}.png|.webp  # Oak, Brock, Misty, gym leaders, rival, rocket
├── badges/{name}_badge.png      # boulder, cascade, thunder, rainbow, soul, marsh, volcano, earth
├── maps/kanto_map.png
├── diagrams/*.png               # matplotlib-generated figures
├── kanto_theme.mplstyle         # matplotlib style (see §6)
├── download_sprites.py
├── download_real_assets.py
├── generate_diagrams.py
└── upscale_assets.py
```

### `download_sprites.py` (the mechanism)

Pulls all 151 Kanto front sprites from the **PokeAPI sprite GitHub repo**, saved as `assets/sprites/front/{id}.png`. Idempotent (skips non-empty existing files), polite (retries, timeout, custom User-Agent):

```python
SPRITE_URL = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
KANTO_RANGE = range(1, 152)   # 1–151 inclusive
OUTPUT_DIR  = SCRIPT_DIR / "sprites" / "front"
# for each id: GET with 3 retries / 30s timeout, write bytes, skip if already present
```

**Legal note carried from `DESIGN.md` §4.3:** sprites are fetched at build time for personal/non-commercial use and the `assets/` tree is `.gitignore`d. The distributed PDF for our book should prefer original stylized silhouettes; keep the trademark disclaimer on the title page and colophon.

---

## 5. How the styled callout boxes work

This is the most important part to get right for *our* book, because the design calls for five distinct box types (Pokédex Entry, Trainer's Tip, Team Rocket's Trap, FROM KANTO TO THE REAL WORLD, Cold Open).

In the sister project, callouts are written as **Markdown blockquotes** (`>`), and `textbook.css` styles every blockquote with a green left rule and tinted background:

```css
blockquote {
    border-left: 4px solid #4DAD5B;   /* Kanto green */
    background: #f0f8f0;
    padding: 10px 16px;
    margin: 12pt 0;
    font-style: italic;
    color: #2c4a2c;
    page-break-inside: avoid;          /* don't split a box across pages */
}
```

A box in Markdown therefore looks like:

```markdown
> **Definition 2.1 (Random Assignment).** Treatment $D_i$ is randomly assigned if
>
> $$(Y_i(0), Y_i(1)) \perp\!\!\!\perp D_i$$
>
> meaning the joint distribution of potential outcomes is the same in both groups.
```

and `> **Professor Oak Explains: …**`, `> **Blue's Mistake: …**` are used as named-box variants — all sharing the single blockquote style.

### What we must ADD: a Pokémon-styled five-box system

The sister project uses *one* plain blockquote for every callout. That is too generic for this book. Our `DESIGN.md` §4.3 mandates **five distinct, color-coded boxes**, and we want each to *look like a piece of the Pokémon world*, not a generic textbook sidebar. Author every box as a Pandoc **fenced div** (`:::`), which becomes `<div class="…">`, then style the classes to evoke real Pokémon UI.

Authoring form (clean Markdown, no inline HTML in the prose):

```markdown
::: pokedex-entry
**POKÉDEX ENTRY №023 — The Exponential Distribution**

$$f(x) = \tfrac{1}{\theta} e^{-x/\theta}, \quad x > 0$$

*In plain terms:* the waiting time until the next random event…

*Recognition cue:* when you see "time until," "memoryless," or a constant hazard — reach for this.
:::
```

The design intent for each box (the "feels like Pokémon" layer):

| Class | In-world identity | Visual motif |
|---|---|---|
| `.pokedex-entry` | The Pokédex device reading out a data entry | Red top bar with a glowing blue "lens" dot (the Pokédex camera), rounded screen, monospace/pixel header, faint scan-line tint on the screen body |
| `.trainers-tip` | A Trainer's field note / TM disc | Yellow Poké Ball–button corner, lightbulb-free "TIP" tab, warm parchment tint |
| `.team-rocket` | A Team Rocket transmission (the blunder-foil) | Black header band with the white **R** insignia, red alert tint, "TRANSMISSION INTERCEPTED" eyebrow |
| `.kanto-realworld` | A field dispatch from the real actuarial world | Dark-green rule + green tint, a small ⬛ marker, "FROM KANTO TO THE REAL WORLD" pill header (this is the colored box the brief explicitly requested) |
| `.cold-open` | The anime "episode" teaser | Light-gray italic block, a film-strip / "▶ EPISODE" eyebrow, larger leading |

CSS (extends `textbook.css`; full version lives in `book/theme.css` in the scaffold). The Poké Ball and Pokédex motifs are built from pure CSS gradients/borders so **no copyrighted art is embedded**:

```css
/* ---- shared callout shell ---- */
.pokedex-entry, .trainers-tip, .team-rocket, .kanto-realworld, .cold-open {
    margin: 14pt 0; padding: 0; page-break-inside: avoid;
    border-radius: 10px; overflow: hidden;
    box-shadow: 0 2px 0 rgba(0,0,0,0.12);
    position: relative;
}
.pokedex-entry > :first-child, .trainers-tip > :first-child,
.team-rocket > :first-child, .kanto-realworld > :first-child,
.cold-open > :first-child {                 /* the header line */
    margin: 0; padding: 7px 14px;
    font-family: 'Press Start 2P', 'Courier New', monospace;  /* pixel header */
    font-size: 9pt; letter-spacing: 0.5px; color: #fff;
}
.pokedex-entry > :not(:first-child), .trainers-tip > :not(:first-child),
.team-rocket > :not(:first-child), .kanto-realworld > :not(:first-child),
.cold-open > :not(:first-child) { padding: 4px 16px; }

/* ---- POKÉDEX ENTRY: the device screen ---- */
.pokedex-entry { border: 3px solid #EE1515; background: #f3f9ff; }
.pokedex-entry > :first-child {
    background: #EE1515;
    /* the blue camera lens + three indicator lights, drawn with gradients */
    background-image:
        radial-gradient(circle at 18px 50%, #7FD7FF 0 7px, #3B4CCA 7px 9px, transparent 9px),
        radial-gradient(circle at 40px 42%, #ff5a5a 0 2.5px, transparent 2.5px),
        radial-gradient(circle at 50px 42%, #FFD733 0 2.5px, transparent 2.5px),
        radial-gradient(circle at 60px 42%, #4DAD5B 0 2.5px, transparent 2.5px);
    padding-left: 78px;
}
.pokedex-entry > :not(:first-child) {        /* faint scan-lines on the "screen" */
    background-image: repeating-linear-gradient(
        to bottom, rgba(59,76,202,0.04) 0 2px, transparent 2px 4px);
}

/* ---- TRAINER'S TIP: field note ---- */
.trainers-tip { border: 2px solid #E6B800; background: #fffbe6; }
.trainers-tip > :first-child {
    background: #FFD733; color: #5a4a00;
    /* yellow Poké Ball button on the right */
    background-image: radial-gradient(circle at calc(100% - 16px) 50%,
        #fff 0 4px, #333 4px 5.5px, #FFD733 5.5px 11px, #333 11px 12.5px, transparent 12.5px);
}

/* ---- TEAM ROCKET'S TRAP: intercepted transmission ---- */
.team-rocket { border: 2px solid #EE1515; background: #fdeeee; }
.team-rocket > :first-child {
    background: #111;
    /* white "R" insignia on the left */
    background-image: radial-gradient(circle at 16px 50%, #fff 0 9px, transparent 9px);
    padding-left: 36px;
}
.team-rocket > :first-child::before { content: "R"; position: absolute;
    left: 11px; top: 7px; color: #EE1515; font-weight: 900; font-size: 11pt; }

/* ---- FROM KANTO TO THE REAL WORLD: actuarial dispatch ---- */
.kanto-realworld { border: 2px solid #2e7d32; border-left-width: 8px; background: #eef7ef; }
.kanto-realworld > :first-child { background: #2e7d32; }

/* ---- COLD OPEN: the episode teaser ---- */
.cold-open { border: 1px dashed #aaa; background: #f5f5f5; font-style: italic; }
.cold-open > :first-child { background: #888; font-style: normal; }
.cold-open > :not(:first-child) { line-height: 1.7; }
```

The **pixel header font** (`Press Start 2P`) is the single biggest "this is Pokémon" cue. Self-host it (Google Fonts, OFL-licensed) and `@font-face` it so WeasyPrint/Chrome embeds it — see §6. Body text stays Georgia serif for readability; only box headers, the running header, and badge captions use the pixel font.

> **Fallback:** if a CSS motif (lens dots, R-insignia) renders poorly in WeasyPrint, degrade to a flat colored header band + the eyebrow text. Chrome-headless honors all of the above; WeasyPrint occasionally simplifies multi-layer `radial-gradient`s. Test both via `make weasy`.

Alternative (`tcolorbox`) only applies if we ever switch to the LaTeX path (`DESIGN.md` §4.4); for the adopted Markdown→HTML→PDF pipeline, the fenced-div + CSS approach above is the answer.

---

## 6. The theme: colors & matplotlib style

### Palette (single source of truth — use everywhere)

| Name | Hex |
|---|---|
| Kanto Red | `#EE1515` |
| Kanto Blue | `#3B4CCA` |
| Kanto Yellow | `#FFD733` |
| Kanto Green | `#4DAD5B` |
| Kanto Gray | `#888888` |
| Background | `#FAFAF5` |

These appear in `textbook.css` (headings red, links/subheads blue, callout rules green), in `title.md` (title red, subtitle blue), and in `kanto_theme.mplstyle` (figure palette).

### `kanto_theme.mplstyle` (copy verbatim for figure generation)

```ini
figure.figsize: 10, 6
figure.dpi: 150
figure.facecolor: white
font.family: sans-serif
font.sans-serif: DejaVu Sans, Arial, Helvetica, sans-serif
font.size: 12
axes.facecolor: "#FAFAF5"
axes.edgecolor: "#333333"
axes.grid: True
axes.titlesize: 16
axes.titleweight: bold
axes.prop_cycle: cycler('color', ['#EE1515', '#3B4CCA', '#FFD733', '#4DAD5B', '#FF7043', '#7B61FF', '#00BCD4', '#FF4081', '#8D6E63', '#78909C', '#E040FB', '#FFAB40'])
grid.color: "#E0E0E0"
grid.linestyle: --
grid.alpha: 0.7
lines.linewidth: 2.0
savefig.dpi: 200
savefig.bbox: tight
savefig.facecolor: white
```

Load it in any figure script with `plt.style.use("kanto_theme.mplstyle")`.

### Pokémon-flavored typography & chrome (the "feels like Kanto" layer)

Beyond the palette, a handful of cheap CSS touches make the whole book read as Pokémon without any licensed art:

- **Pixel display font for chrome.** Self-host **Press Start 2P** (OFL) and use it *only* for chapter numbers, box headers, badge captions, and the running header — never body text:

  ```css
  @font-face { font-family: 'Press Start 2P';
      src: url('fonts/PressStart2P-Regular.ttf') format('truetype'); }
  h1 .chapter-num, .badge-caption, .running-head { font-family: 'Press Start 2P', monospace; }
  ```

- **Type-colored chapter accents.** Each gym chapter is themed to its leader's type. Define the official type colors and tint the chapter's `h1` rule + first box accordingly:

  ```css
  :root {
      --t-rock:#B6A136; --t-water:#6390F0; --t-electric:#F7D02C; --t-grass:#7AC74C;
      --t-poison:#A33EA1; --t-psychic:#F95587; --t-fire:#EE8130; --t-ground:#E2BF65;
      --t-normal:#A8A77A; --t-ghost:#735797;
  }
  h1.type-water  { border-bottom-color: var(--t-water);  color: var(--t-water);  }
  h1.type-electric { border-bottom-color: var(--t-electric); color:#b58f00; }
  /* …one per gym; set via a class on the chapter heading. */
  ```

  Chapter → type mapping follows the gym leaders: Brock=Rock, Misty=Water, Surge=Electric, Erika=Grass, Sabrina=Psychic, Koga=Poison, Blaine=Fire, Giovanni=Ground. (Ch 1/2 Normal; Ch 5 Electric, etc. — see `DESIGN.md` Part 1.)

- **Poké Ball list bullets.** Replace default `ul` bullets with a tiny CSS Poké Ball:

  ```css
  ul.pokeball { list-style: none; padding-left: 1.4em; }
  ul.pokeball > li::before {
      content: ""; display: inline-block; width: 0.7em; height: 0.7em;
      margin-left: -1.2em; margin-right: 0.5em; vertical-align: middle;
      border: 1.5px solid #222; border-radius: 50%;
      background: linear-gradient(to bottom, #EE1515 0 45%, #222 45% 55%, #fff 55% 100%);
  }
  ```

- **Section dividers as a Poké Ball line.** Style `hr` as a centered Poké Ball flanked by rules (use a small inline SVG-in-CSS or the gradient trick) instead of a plain line.

- **Badge-earned banner.** The end-of-chapter badge figure (from `embed_visuals.badge()`) sits above a pixel-font "‹BADGE› BADGE EARNED!" caption; the eight-badge montage closes the final content chapter.

- **Running header = "Route to a 10."** Reuse the `string-set: chapter-title` mechanism but format the header in the pixel font with a tiny Poké Ball glyph, reinforcing the journey framing on every page.

### CSS structure highlights (inherited from `textbook.css`)

- `@page { size: A4; margin: 2.5cm …; @bottom-center { content: counter(page); } @top-center { content: string(chapter-title); } }` — page numbers + running chapter title in the header.
- `@page :first { … content:""; }` — no header/footer on the title page.
- `h1 { color:#EE1515; border-bottom:3px solid #EE1515; page-break-before:always; string-set: chapter-title content(); }` — each chapter starts on a new page and sets the running header. (We add the type-color classes above on top of this.)
- `h2 { color:#3B4CCA; border-bottom:1px solid #ccc; page-break-after:avoid; }`
- Tables: red header row (`th { background:#EE1515; color:white; }`), zebra striping on even rows. For distribution tables we additionally allow a "trading card" variant (rounded border, type-colored header) reused in Appendix B.
- `figure, pre, blockquote, table, .pokedex-entry, .trainers-tip, .team-rocket, .kanto-realworld { page-break-inside: avoid; }` — keeps boxes/figures/tables from splitting across pages.
- Body font is Georgia serif, justified, hyphenated; pixel font reserved for chrome only.

### Title page (`title.md` / `title.html`)

A `--include-before-body` HTML block with inline styles: 52pt red title, 30pt blue subtitle, italic gray tagline, a red `<hr>`, and a small-print colophon carrying the CC BY-NC-SA license line and the Nintendo/Game Freak/Creatures trademark disclaimer. Copy this structure and reskin the text for Exam P.

---

## 7. The Makefile targets (what to run)

From the sister repo's `textbook/build/Makefile`:

| Target | Effect |
|---|---|
| `make pdf` | Pandoc → LaTeX (xelatex) PDF (secondary path) |
| `make html` | Single self-contained HTML page (water.css, MathJax) |
| `make weasy` | **Primary**: styled HTML (`textbook.css`) → WeasyPrint/Chrome PDF |
| `make release-pdf` | Build the weasy PDF and copy to the repo's top-level release location |
| `make clean` | Remove `output/` |

Chapters are auto-collected in order: `CHAPTERS := $(sort $(wildcard ../../textbook/chapters/ch*.md))` and appendices `appendix_*.md`. **So naming files `ch01_*.md … ch13_*.md` is all that's needed for ordering** — no manual file list.

---

## 8. The workflow, end to end (what a writer does)

1. Write/edit a chapter in `textbook/chapters/chNN_name.md` — prose + `$…$` math + `>`/`:::` callout boxes.
2. (Once per chapter) add figure insertions to `embed_visuals.py` (anchor + marker + helper call), then `python embed_visuals.py` to inject the `<figure>` HTML idempotently.
3. Generate any new diagrams: `python assets/generate_diagrams.py` (uses `kanto_theme.mplstyle`).
4. Ensure sprites exist: `python assets/download_sprites.py` (skips existing).
5. `make weasy` → review `output/*_weasy.pdf`.
6. When happy, `make release-pdf`.

---

## 9. Differences for *Probability & Risk: A Kanto Journey*

Carry over the entire pipeline above, with these project-specific changes:

- **Five color-coded callout classes** (§5 option 1) instead of the single green blockquote — this satisfies the design's distinct-box requirement.
- **Math is heavier** (integrals, MGFs, `$E[X\wedge u]$`): add a global MathJax `\newcommand` preamble (`\E`, `\Var`, `\SD`, `\Cov`, `\Corr`, `\dplus`, `\limexp`, distribution shorthands) at the top of `ch01`, or via a Pandoc `header-includes`.
- **13 chapters + appendices A–I** instead of 8 + 4 — same `chNN_*.md` / `appendix_*.md` naming so the Makefile globs them in order.
- **`sims/` verification gate** (`seed=151`): a step the sister project did not enforce — we add a `make verify` target that runs the example-checking notebook/scripts and fails the build on a numeric mismatch (see `DESIGN.md` §4.4, §4.8).
- **All Pokémon art is fetched from repos** (PokeAPI/sprites for sprites/badges/types, pret/pokered for characters + map) via `assets/download_sprites.py` and `assets/download_real_assets.py` — nothing hand-drawn or AI-generated. Only the *mathematical* figures are matplotlib-generated. `assets/` is `.gitignore`d; fetch on build.
- **This build is printed & bound.** See §10 for the print spec (trim, gutter, recto chapter starts, 300 DPI, font embedding).

---

## 10. Print & bind specification

The output is a physically **printed and bound** study book, so the PDF is print-grade, not screen-only:

- **Trim size:** US Letter 8.5×11 in (set in `book/theme.css` `@page { size: 8.5in 11in }`). Switch to 6×9 or A4 by editing that one rule.
- **Binding gutter:** mirrored margins via `@page :left` / `@page :right` — inner (spine-side) margin 1.1 in, outer 0.8 in, top/bottom 1 in. This keeps text out of the spine on a perfect-bound or coil book.
- **Recto chapter starts:** `h1 { break-before: right }` so every chapter opens on a right-hand page (the renderer inserts a blank verso when needed). Screen view falls back to a plain page break.
- **Page furniture:** page number on the outer bottom corner, running chapter title (pixel font) on the outer top; both suppressed on the title page.
- **Resolution:** all generated figures render at **300 DPI** (`generate_figures.py`, `PRINT_DPI=300`). Repo sprites are low-res (≈96 px); run `assets/upscale_assets.py` (nearest-neighbor) so the pixel art stays sharp rather than blurry when scaled for print.
- **Fonts embedded:** self-host `Press Start 2P` (`book/fonts/`) and rely on Georgia/serif system fonts; WeasyPrint and Chrome both embed fonts in the PDF so the printer needs nothing installed.
- **Ink discipline:** box header bands use solid color but are short; avoid full-page dark fills. The Team Rocket black header is intentionally a thin band.
- **Optional pre-press:** for a commercial printer wanting bleed/crop marks, add `bleed: 3mm; marks: crop;` to `@page` and extend full-bleed images past the trim. Not needed for the inset-figure layout we use.
- **Color:** palette is RGB; most print-on-demand (Lulu, Mixam, local) accept RGB PDF and convert. If a shop requires CMYK, post-process with Ghostscript (`-sColorConversionStrategy=CMYK`).

**Recommended render path for print:** Chrome headless honors `break-before: right` and the mirrored-margin `@page` rules most faithfully; WeasyPrint is close but occasionally simplifies multi-layer gradients (the box motifs). Build both via `make pdf` and pick the cleaner proof.
