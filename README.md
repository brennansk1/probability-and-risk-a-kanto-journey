# Probability & Risk: A Kanto Journey
### The Indigo League Edition — a narrative study companion for **SOA/CAS Exam P (Exam 1)**

A complete, 441-page teaching textbook that takes a reader from **the very beginning of college math** to a **perfect-score level of readiness for Exam P**, told as the story of Ash Ketchum — Trainer and actuary-in-training — crossing the Kanto region. Every probability concept is taught from the ground up; every problem is a task Ash must accomplish; and a parallel **real-world bridge** connects each idea to actual actuarial practice.

> **The promise (printed in the front matter):** *"You will never need an outside source to understand a concept in this book, and you will never be forced to read what you already know."*

This repository is the **full source** (Markdown + LaTeX math + committed figure code) plus the **built PDF**. It builds reproducibly to a print-and-bind-ready book.

📖 **The book:** [`Probability_and_Risk_A_Kanto_Journey.pdf`](Probability_and_Risk_A_Kanto_Journey.pdf) — 441 pages.

---

## What's inside

- **16 chapters + 2 spaced-retrieval checkpoints + 9 appendices**, covering the entire 2026 Exam P syllabus: General Probability (23–30%), Univariate Random Variables (44–50%), Multivariate Random Variables (23–30%).
- **302 problems**, every one with a full worked solution, an archetype tag, and a numeric answer **verified programmatically** (seed = 151).
- **64 instructional diagrams**, generated from committed matplotlib code (reproducible).
- A **two-reader design**: novices read linearly and learn from scratch; reviewers hit a *"Do you already own this?"* test-out gate at every chapter and concept and skip what they know.

### The teaching model (the "nine-beat" Concept Lesson Arc)

Every important concept is *taught*, not summarized, through a fixed nine-beat arc (see [`MASTER_PLAN_V2.md`](MASTER_PLAN_V2.md)):

> one-sentence plain idea → concrete numeric instance → reason it through in words → **surface and dismantle the tempting misconception** → translate into notation one glyph at a time → derive the formula from the instance → ramp the difficulty → picture/table → consolidate (the Pokédex Entry + recognition cue).

Notation is treated as **a language we teach, not a code we assume**: every symbol is introduced — named, read aloud, and motivated — before its first use, and logged in `notation_ledger.md`.

### The recurring elements (Pokémon-styled UI panels)

| Panel | Job |
|---|---|
| **Cold Open** | An anime episode that raises the chapter's question with real stakes |
| **Pokédex Entry** | The boxed theory/formula summary + recognition cue |
| **Trainer's Tip** | Pure exam craft — calculator keystrokes, pacing, shortcuts |
| **Team Rocket's Trap** | The canonical mistake, committed in-character, then fixed |
| **From Kanto to the Real World** | The concrete actuarial application (claim frequency, fraud detection, reserving, the CLT behind pooling) |
| **Concept Gate** | The "Do you already own this?" skip mechanic |

---

## Repository layout

```
.
├── Probability_and_Risk_A_Kanto_Journey.pdf   # the built book (441 pp)
├── MASTER_PLAN_V2.md      # governing teaching spec (nine-beat arc, two-reader, tiers)
├── DESIGN.md              # curriculum & production bible
├── FORMATTING.md          # build pipeline, callout boxes, print/bind spec
├── AUDIT.md               # the quality-gate charter (correctness, teaching, format)
├── notation_ledger.md     # every symbol, spoken name, first introduction
├── Makefile               # `make book` = full gated build
├── book/
│   ├── theme.css          # Kanto theme + styled boxes + print @page rules
│   ├── mathjax-preamble.md# global math macros
│   ├── frontmatter/       # title, how-to-use, skip diagnostic
│   ├── chapters/          # ch00..ch15 + 2 checkpoints
│   └── appendices/        # A–I
├── problems/
│   ├── bank.yaml + bank.d/# every problem as data (id, tier, outcomes, verify)
│   └── coverage.csv
├── syllabus/outcomes.yaml # SOA outcomes — source of truth for coverage
├── figures/src/           # committed matplotlib figure generators + Kanto mplstyle
├── sims/verify_examples.py# numeric verification harness (seed=151)
├── tools/                 # scaffold + the audit checkers + workflow scripts
└── assets/                # (gitignored) Pokémon art fetched at build time
```

---

## Building it

**Prerequisites:** `pandoc`, a PDF renderer (`weasyprint` **or** Google Chrome), Python 3 with the packages in `requirements.txt`.

```bash
pip install -r requirements.txt
make assets    # fetch Pokémon art from repos + generate all math figures
make book      # full gated build: verify → lint → figures → embed → PDF
```

`make book` runs every integrity gate before it compiles and **fails on any defect**:

| Gate | What it enforces |
|---|---|
| `make verify` | every numeric answer recomputed at seed=151 and matched |
| `make lint`   | LaTeX/render/structure audit **+** outcome & distribution coverage |
| `make figures`| all 64 diagrams regenerated from committed code |

**Current status:** ✅ verify **302/302** · ✅ format **0 errors / 0 warnings** · ✅ coverage **full** (25/24 outcomes, 18/12 distributions) · ✅ teaching-quality audited chapter-by-chapter against the gold-standard Bayes chapter · ✅ `make clean && make book` exits 0.

### Asset sourcing

All Pokémon imagery is **fetched at build time from open community repositories** — never hand-drawn or AI-generated:

- **Sprites / badges / type icons** → [`PokeAPI/sprites`](https://github.com/PokeAPI/sprites)
- **Characters / Kanto map** → [`pret/pokered`](https://github.com/pret/pokered) (Gen-1 disassembly)

Only the **mathematical** diagrams are generated locally (matplotlib), because no repo holds a plot for our exact problems. The raw `assets/` tree is gitignored and regenerated by `assets/download_sprites.py` + `assets/download_real_assets.py`.

---

## ⚖️ Legal & disclaimers

**This is an unofficial, non-commercial, educational fan work. It is not for sale.**

- **Pokémon** — Pokémon, the names of all Pokémon, characters, towns, gym badges, sprites, and related imagery are **™ and © Nintendo, Game Freak, and Creatures Inc. / The Pokémon Company.** This project is **not affiliated with, sponsored by, or endorsed by** any of them. All Pokémon trademarks and copyrights belong to their respective owners; they are used here **for educational and illustrative purposes only**, under a good-faith view of fair/educational use, with no claim of ownership and no intent to infringe.
- **Sprite & art assets** are sourced from the community repositories [`PokeAPI/sprites`](https://github.com/PokeAPI/sprites) and [`pret/pokered`](https://github.com/pret/pokered) and remain subject to **their** licenses and to the underlying Nintendo/Game Freak/Creatures rights. They are included for personal, educational study only and must not be used commercially.
- **SOA / CAS Exam P** — "Exam P," the syllabus, and official sample questions are the property of the **Society of Actuaries (SOA)** and **Casualty Actuarial Society (CAS)**. This book is **independent, unofficial study material**, not produced or endorsed by the SOA or CAS. No copyrighted exam questions are reproduced verbatim; problems are original or re-skinned and re-solved in original wording. **Always confirm current exam format, fees, and rules at [soa.org](https://www.soa.org) before sitting.**
- **Originality of content** — the prose, problems, solutions, and instructional diagrams are original to this project.
- **Licensing** — original textbook *text and problems*: **CC BY-NC-SA 4.0**. Original *code* (build system, figure generators, tooling): **MIT**. Third-party Pokémon assets: under their own licenses and the rights above (NOT relicensed).
- **Takedown** — this is a hobby/educational project. If you are a rights holder and have any concern, open an issue and the relevant material will be **removed promptly**.

*No copyright or trademark infringement is intended. This project exists to help people learn probability and pass an actuarial exam.*
