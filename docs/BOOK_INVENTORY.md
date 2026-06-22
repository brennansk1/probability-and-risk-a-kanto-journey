# Book Inventory — V3 build status board

Live status of the V3 build (*Probability & Risk: A Kanto Journey*). One row per chapter; updated as waves complete. Status legend: ☐ not started · ✍ authoring · 🔬 in QA (harness/blind/re-grade) · ✅ done (all four verification layers + DoD).

## Final assembly — ✅ COMPLETE (whole-book grade A)
- ✅ All 20 chapters + 9 appendices + episode-guide front matter authored to grade A.
- ✅ **Harness 450/450** (seed 151) · **check_format PASS** · **check_coverage PASS (full coverage)**.
- ✅ **Episode stills** (real Indigo League frames, 6-shot panel-picked) embedded in 19/20 now-playing boxes — ch07 intentionally text-only (recap); source episodes streamed and deleted locally (stills gitignored).
- ✅ **Real Kanto region map** (labeled FRLG-style) replaces the 32×32 stub, with a **per-chapter "you are here" pin** on every opener (ch11 keeps the un-pinned full map by design).
- ✅ **Whole-book independent tutor grade: A** — A− on first pass, four defects fixed (EP059 source-of-truth, badge earning-order normalization, ch16 alt-text, appendix-F wording), re-confirmed clean A.
- ✅ **Final PDFs rendered** (Chrome headless for MathJax; `build/output/`, gitignored): **book = 477 pp / 35 MB**, **workbook = 550 pp / 37 MB**, 0 "could not fetch". Workbook injects 409 work-space grids (146 lg / 145 md / 118 sm).
- Render note: PDFs **must** be rendered with Chrome headless, not WeasyPrint — WeasyPrint cannot run the MathJax JS, so equations would ship as raw TeX. Makefile FRONT corrected to the V3 set (episode-guide only; ch00 carries orientation).

## Foundation
- ✅ Pipeline ported to repo root (Makefile, tools, book chrome, figures helpers, sims, syllabus, assets)
- ✅ V3 deltas: pandoc `+bracketed_spans`; `.kbd`/`.keystroke`/`.enrichment`/`.dex-profile` CSS
- ☐ Token-embed rewrite of `embed_visuals.py` (deferred; ch02 uses proven inline `<figure>` for now)
- ☐ `figures/manifest.yaml`, `book/ranks.yaml`, `figures/src/type_palette.py`
- ☐ `outcomes.yaml` remap to V3 chapter numbers
- ☐ Scaffold remaining chapters/appendices/frontmatter

## Chapters
| Ch | Title | Tier | Status |
|---|---|---|---|
| 00 | Orientation | — | ✅ **grade A** — exam facts accurate · calculator + symbols primers correct · 4 calc drills verify |
| 01 | Fundamentals of Probability | C/B | ☐ |
| 02 | Conditional Probability & Bayes | A | ✅ gold-standard exemplar — L1 harness 26/26 · L2 lint pass · L3 blind re-derivation (all correct) · **L4 tutor letter grade = A** (all 10 dims 9–10; NO concept compression — every concept fully derived) · A+ polish applied · clean build |
| 03 | Discrete RVs & Moments | A | ✅ **grade A** — harness clean · blind re-derivation (1 prose-drift caught & fixed) · 1-Var-Stats flagship · build clean |
| 04 | Combinatorics | B | ✅ **grade A** — blind re-derivation 40/40 clean · nCr/nPr keystrokes · build clean |
| 05 | Key Discrete Distributions | B | ✅ **grade A** — blind re-derivation 33/33 · series interlude fully taught · build clean |
| 06 | Deductibles & Limits (Discrete) | B | ✅ **grade A** — blind re-derivation clean · 3rd audit drill added to meet quota · build clean |
| 07 | Checkpoint A | — | ✅ **grade A** — 12/12 mixed drills · full Act-I coverage · mind-map + pass gate |
| 08 | The Calculus Toolkit | C | ✅ **grade A** — 18/18 re-derived · gamma integral derived · C8.14 table fixed · build clean |
| 09 | Densities & CDFs | B | ✅ **grade A** — blind re-derivation 19/19 · mixed distributions fully built · C9.16 statement fixed · build clean |
| 10 | Continuous Moments | B | ✅ **grade A** — blind re-derivation 30/30 · survival method derived via integral-swap · build clean |
| 11 | Key Continuous Distributions | B | ✅ **grade A** — blind re-derivation 30/30 · Pareto correctly enrichment · build clean |
| 12 | Normal & the CLT | A | ✅ **grade A** — harness 39/39 re-derived · CLT + continuity correction fully derived · build clean |
| 13 | Continuous Deductibles & Review | B | ✅ **grade A** — 26/26 re-derived · calculus + cases approaches · build clean |
| 14 | Joint Distributions | A | ✅ **grade A** — harness 22/22 · blind re-derivation 22/22 + WEs · build clean · no compression |
| 15 | Joint Moments & Covariance | A | ✅ **grade A** — harness 22/22 · blind re-derivation 36/36 · build clean · no compression |
| 16 | Conditional & Double Expectation | A | ✅ **grade A** — harness 18/18 · blind re-derivation 30/30 · build clean · no compression |
| 17 | Order Statistics | B | ✅ **grade A** — all re-derived · max/min/k-th/reliability derived · Elite Four · build clean |
| 18 | Checkpoint B | — | ✅ **grade A** — 12/12 mixed drills · full Act-III coverage · now-playing box added |
| 19 | Champion's Challenge (3 mocks) | — | ✅ **grade A** — 90/90 harness · 18/18 blind sample · 3 mocks weight-matched 8/14/8 · M3.13 duplicate option fixed |

## Conventions locked (from the ch02 exemplar — fold into `_TEMPLATE.md` + dossiers)
- **Calculator key-caps:** write `[2nd]{.kbd}` and sequences `[ ... ]{.keystroke}` as **bare markdown — never wrap them in backticks** (backticks make pandoc treat them as literal code). Pandoc `+bracketed_spans` renders `{.kbd}` as the semantic `<kbd>` element; CSS styles the `kbd` element (theme.css).
- **Answer section heading is `## Answers`** (linter aligned).
- **Figures:** inline `<figure><img src="../../assets/diagrams/chNN_*.png" alt="…">` for now (token system deferred); every figure needs alt text; `gen_chNN.py` must be runnable from `figures/src/`.
- **Per-chapter QA loop (proven):** author → `gen_chNN.py` + `bank.d/chNN.yaml` → `sims/verify_examples.py` (L1) → `check_format.py` (L2) → blind re-derivation agent (L3) → tutor re-grade agent (L4) → fix → pandoc build smoke-test.

## Appendices
☐ A formula sheet · ☐ B distribution Pokédex · ☐ C normal table · ☐ D TI-30XS field manual · ☐ E exam day · ☐ F cross-reference · ☐ G glossary · ☐ H answer keys · ☐ I risk primer
