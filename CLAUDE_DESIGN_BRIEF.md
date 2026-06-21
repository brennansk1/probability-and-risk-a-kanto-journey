# Claude Design Brief — Refine the Textbook Formatting
### *Probability & Risk: A Kanto Journey* (V3) — the visual/typography/layout layer

> **Read this, then refine the styling layer to a professional, immersive, print-perfect standard.** You own the *frame* (typography, color, boxes, page geometry, chrome). You do **not** touch lesson content, math, problem numbers, or `verify:` expressions. Curriculum/format spec lives in `MASTER_PLAN_V3.md` (§6 Format, §13 Calculator key-caps, §14 Asset upgrade, §17 distributions, §19 enrichment, §22 CSS deltas, §27 embedding). The current implementation to refine/port from is `Version 1/book/theme.css` + `Version 1/book/workbook.css`.

---

## 1. The aesthetic target

A Pokémon Game-Boy-era **game** that happens to be a rigorous actuarial textbook. Two layers, strictly separated:

- **Game layer** owns the *frame, navigation, emotion*: chapter banners, the Kanto map progress strip, gym-leader VS portraits, badges, Pokédex "Actuary Mode" device panels, type-color accents, the pixel display font.
- **Math layer** owns the *content*: body prose and every equation, in clean high-contrast type on calm backgrounds.

**They never fight for the same pixel.** The whole brief succeeds or fails on one test.

---

## 2. The Iron Rule (non-negotiable, the acceptance test)

> **Cover every sprite, badge, banner, and map with your hand — every equation, number, and derivation must still be perfectly legible and correctly spaced. And uncovered, the page must still feel like Kanto.**

Corollaries:
- Equations are **never** set over a sprite, map, texture, or tint that reduces contrast. Display math is centered, single-column, generously spaced, with sized delimiters and real `\dfrac` (never inline-slashed fractions or collapsed exponents).
- **Color is never the only signal.** Every colored panel also carries an **icon + a text label**, so it survives grayscale printing and color-blind readers. Verify by desaturating a page.
- Decoration that competes with a formula is **cut**, not compromised.

---

## 3. Constraints

- **Static, print-first.** Output is a bound **reader PDF** (`make book`) and a **workbook PDF** (`make workbook`) via Pandoc → HTML → WeasyPrint/Chrome. **No animation, no JavaScript, no web-only effects.** Everything must render identically in print.
- **Self-contained build.** Pandoc runs `--standalone --embed-resources` (assets base64-inlined). Styling is plain CSS in `theme.css`/`workbook.css` + inline styles emitted by `book/embed_visuals.py`. MathJax is configured in `mathjax-config.html` / `mathjax-preamble.md`.
- **US Letter, print-and-bind**: mirrored margins with a binding gutter, running heads, page numbers, sensible page-break control.
- **Grayscale-survivable + color-blind-safe** as above.
- **Don't break the linters.** `tools/check_format.py` asserts required headings and box classes exist; keep class names stable (see §5) unless you also update the plan/linter notes.

---

## 4. Files you own

| File | Role |
|---|---|
| `book/theme.css` | Reader styling — typography, color tokens, box panels, figures, `@page` print rules, chapter chrome. **Primary deliverable.** |
| `book/workbook.css` | Workbook-only overrides — dot-grid working-space blocks, symmetric margins. |
| `book/mathjax-config.html`, `book/mathjax-preamble.md` | Math rendering config + macros — tune sizing/spacing only; don't redefine notation. |
| `book/embed_visuals.py` | Emits inline-styled `<figure>`/panel HTML for tokens (`{{fig:…}}`, `{{dex:…}}`, `{{badge:…}}`, `{{vs:…}}`, `{{banner:…}}`, `{{progress:…}}`, `{{keycap:…}}`). Keep markup classed so `theme.css` controls the look. |
| `figures/src/gen_dex.py`, `gen_calc.py`, `type_palette.py` | Pokédex-profile + keypad compositors + the 18-type→color map (keep the map in sync with the CSS `:root` tokens). |

Start from `Version 1/book/theme.css` (Kanto palette, `@page` rules, Press Start 2P running heads, the box classes) and `workbook.css` (the `.workspace` dot-grid) — refine and extend, don't rebuild from scratch.

---

## 5. Refinement checklist (prioritized)

**A. Typography system.** Two families, jobs separated:
- *Display face* (Press Start 2P, `book/fonts/PressStart2P-Regular.ttf`, OFL) for titles, banners, badges, chrome **only** — never body or math (it's unreadable at length).
- *Clean classical text+math face* for all body prose and equations. Establish a modular type scale, comfortable measure (~65–75 chars), generous leading, clear heading hierarchy (chapter → section → concept → beat). Math inline-size matches surrounding text; display math has breathing room.

**B. The box / UI-panel system.** Each fenced-div class becomes a distinct game-UI panel — each with **color + icon + label**:
- `.cold-open` — cinematic episode banner (light narrative).
- `.pokedex-entry` — blue "device screen" (the formula/summary readout).
- `.trainers-tip` — yellow item-callout (exam craft).
- `.team-rocket` — red "transmission intercepted" (the misconception trap).
- `.kanto-realworld` — green field-journal (real-world actuarial bridge).
- `.concept-gate` — Poké Center "heal or proceed" skip-check.
- `.problem-set` / `.answer-key` — the questline drills + solutions (keep `.problem-set` class exactly — the workbook Lua filter keys on it).
- `.archetype-tag` — small problem-archetype chip.
Refine borders, tints, corner treatments, icon chips, and spacing so they read as a consistent device family — calm enough that the math inside is never harmed.

**C. The "Pokédex Actuary Mode" frame.** A consistent device-screen treatment (corner brackets, a small Pokédex icon chip, a subtle screen tint) around `.pokedex-entry` and problem statements — **pure CSS**, crisp at print resolution.

**D. Calculator key-caps (`.kbd` / `.keystroke`).** Style `[2nd]{.kbd}`-style spans as little physical key-caps (rounded, beveled, monospace), and `.keystroke` as a horizontal "press this, then this" strip. Must be visually distinct from inline `code`.

**E. Distribution Pokédex profiles (`.dex-profile`).** Frame the generated scan-readout (mascot art + stat block + recognition cue) like a Pokédex screen; ensure the stat-block math stays crisp.

**F. Chapter chrome.** Style the `{{banner:chNN}}` VS-banner (gym-leader portrait + type color + chapter title + badge) and the `{{progress:chNN}}` strip (Kanto map with current town marked, earned badges lit / unearned greyed, **Trainer Rank** label, Exam-Readiness %). These open every chapter — make them feel like entering a new town.

**G. Type-color theming.** Drive chapter accents from the 18-type → hex map (§17 of the plan) exposed as `:root` CSS custom properties; each chapter's accent tints its banner + figure-accent without touching body/math contrast. Keep `figures/src/type_palette.py` and the CSS tokens identical (the audit checks parity).

**H. Enrichment (`.enrichment`).** A clearly-labeled "Beyond the Syllabus" panel, visually *quieter* than core content (so it never competes with exam material).

**I. Print `@page` rules.** US Letter; mirrored inner/outer margins with a binding gutter; running heads (chapter short-title verso, section recto) in the display face; page numbers; `page-break-inside: avoid` on figures, panels, and worked examples; avoid orphan headings and stranded captions.

**J. Figures & captions.** Centered, sized sensibly, captions in a smaller italic; `image-rendering: pixelated` preserved for pixel sprites; never let a figure crowd an adjacent equation.

**K. Workbook edition.** Refine `.workspace` dot-grid blocks (`.ws-sm/md/lg/xl`) — clean 5mm dot grid, right amount of space per tier (route < gym < elite), symmetric margins (no binding gutter), and ensure injected grids never split awkwardly across pages.

---

## 6. Deliverables

1. A refined **`book/theme.css`** and **`book/workbook.css`** implementing §5.
2. Synced **`:root` type-color tokens** ↔ `figures/src/type_palette.py`.
3. A one-page **style-guide / kitchen-sink sample** (a small markdown file exercising every panel, the key-caps, a dex-profile, a banner, a progress strip, display + inline math, a table, a problem + answer) so the look can be proofed in isolation.
4. A short **`docs/design/STYLE_NOTES.md`** recording the type scale, color tokens, panel anatomy, and any decisions, so chapter authors stay consistent.

---

## 7. How to preview & verify

- `make html` → open the styled single-file HTML; proof the sample (§6.3) and one real chapter.
- `make book` and `make workbook` → render the PDFs; **0 "could not fetch" warnings**; check the bind gutter, running heads, and that no panel/figure/equation splits badly across a page.
- **Grayscale test:** desaturate a rendered page — every panel still distinguishable by icon + label; all math legible.
- **Iron-Rule test (§2):** hand-cover all art — math perfect; uncover — feels like Kanto.
- Keep `tools/check_format.py` green (required headings + box classes intact).

---

## 8. Acceptance criteria (done = all true)

- Passes the **Iron-Rule test** and the **grayscale test**.
- Every box class in §5.B reads as a coherent device-panel family; none harms the math it contains.
- Reader + workbook PDFs render clean at print resolution; correct US-Letter geometry, gutters, running heads, and page-break behavior.
- Type scale, color tokens, and panel anatomy are documented in `docs/design/STYLE_NOTES.md` and consistent across the sample.
- No animation/JS; everything is static and print-faithful.

*Scope: formatting/visual layer only. Content, math, and verification belong to the authoring waves (MASTER_PLAN_V3 §25–§28). Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; private, non-commercial build.*
