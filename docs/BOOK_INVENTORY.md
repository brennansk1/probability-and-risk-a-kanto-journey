# Book Inventory — V3 build status board

Live status of the V3 build (*Probability & Risk: A Kanto Journey*). One row per chapter; updated as waves complete. Status legend: ☐ not started · ✍ authoring · 🔬 in QA (harness/blind/re-grade) · ✅ done (all four verification layers + DoD).

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
| 00 | Orientation | — | ☐ |
| 01 | Fundamentals of Probability | C/B | ☐ |
| 02 | Conditional Probability & Bayes | A | ✅ gold-standard exemplar — L1 harness 26/26 · L2 lint pass · L3 blind re-derivation (all correct) · **L4 tutor letter grade = A** (all 10 dims 9–10; NO concept compression — every concept fully derived) · A+ polish applied · clean build |
| 03 | Discrete RVs & Moments | A | ✅ **grade A** — harness clean · blind re-derivation (1 prose-drift caught & fixed) · 1-Var-Stats flagship · build clean |
| 04 | Combinatorics | B | ✅ **grade A** — blind re-derivation 40/40 clean · nCr/nPr keystrokes · build clean |
| 05 | Key Discrete Distributions | B | ✅ **grade A** — blind re-derivation 33/33 · series interlude fully taught · build clean |
| 06 | Deductibles & Limits (Discrete) | B | ✅ **grade A** — blind re-derivation clean · 3rd audit drill added to meet quota · build clean |
| 07 | Checkpoint A | — | ☐ |
| 08 | The Calculus Toolkit | C | ☐ |
| 09 | Densities & CDFs | B | ✅ **grade A** — blind re-derivation 19/19 · mixed distributions fully built · C9.16 statement fixed · build clean |
| 10 | Continuous Moments | B | ✅ **grade A** — blind re-derivation 30/30 · survival method derived via integral-swap · build clean |
| 11 | Key Continuous Distributions | B | ✅ **grade A** — blind re-derivation 30/30 · Pareto correctly enrichment · build clean |
| 12 | Normal & the CLT | A | ✅ **grade A** — harness 39/39 re-derived · CLT + continuity correction fully derived · build clean |
| 13 | Continuous Deductibles & Review | B | ☐ |
| 14 | Joint Distributions | A | ✅ **grade A** — harness 22/22 · blind re-derivation 22/22 + WEs · build clean · no compression |
| 15 | Joint Moments & Covariance | A | ✅ **grade A** — harness 22/22 · blind re-derivation 36/36 · build clean · no compression |
| 16 | Conditional & Double Expectation | A | ✅ **grade A** — harness 18/18 · blind re-derivation 30/30 · build clean · no compression |
| 17 | Order Statistics | B | ☐ |
| 18 | Checkpoint B | — | ☐ |
| 19 | Champion's Challenge (3 mocks) | — | ☐ |

## Conventions locked (from the ch02 exemplar — fold into `_TEMPLATE.md` + dossiers)
- **Calculator key-caps:** write `[2nd]{.kbd}` and sequences `[ ... ]{.keystroke}` as **bare markdown — never wrap them in backticks** (backticks make pandoc treat them as literal code). Pandoc `+bracketed_spans` renders `{.kbd}` as the semantic `<kbd>` element; CSS styles the `kbd` element (theme.css).
- **Answer section heading is `## Answers`** (linter aligned).
- **Figures:** inline `<figure><img src="../../assets/diagrams/chNN_*.png" alt="…">` for now (token system deferred); every figure needs alt text; `gen_chNN.py` must be runnable from `figures/src/`.
- **Per-chapter QA loop (proven):** author → `gen_chNN.py` + `bank.d/chNN.yaml` → `sims/verify_examples.py` (L1) → `check_format.py` (L2) → blind re-derivation agent (L3) → tutor re-grade agent (L4) → fix → pandoc build smoke-test.

## Appendices
☐ A formula sheet · ☐ B distribution Pokédex · ☐ C normal table · ☐ D TI-30XS field manual · ☐ E exam day · ☐ F cross-reference · ☐ G glossary · ☐ H answer keys · ☐ I risk primer
