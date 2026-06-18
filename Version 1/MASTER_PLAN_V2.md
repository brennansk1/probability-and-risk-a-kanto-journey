# Making *A Kanto Journey* a Masterful Teaching Textbook
## Master Design Plan — v2 (Beginning-of-College → Perfect Exam P Score)

> **Governing spec.** This document supersedes the teaching approach of Draft 1 and governs all chapter (re)writes. `DESIGN.md` (curriculum/production), `FORMATTING.md` (build/assets), and `AUDIT.md` (quality gates) remain in force; where they conflict with this file on *teaching method*, this file wins.

> **Designer's preface.** Most math textbooks fail for one reason: the author forgot what it felt like not to know. They write the *summary* an expert would want, not the *path* a learner needs. Governing rule: **assume the reader knows nothing, but never waste the reader's time.** Teach every idea from the ground up; let anyone who already owns an idea prove it in sixty seconds and move on. No gaps for the novice; no condescension for the capable.

---

## Part 1 — Two-reader contract
- **Floor:** assume nothing beyond arithmetic. Do NOT assume fluent algebra, summation/integral notation, set theory, or probability vocabulary.
- **Ceiling:** able to score 9–10 on Exam P.
- **The Novice** reads linearly and learns from scratch. **The Reviewer** tests out at a "Do you already own this?" gate at the top of every chapter and every major concept; pass the stated bar → skip; fail/hesitate → full teaching is right there.
- **Front-matter promise:** *"You will never need an outside source to understand a concept in this book, and you will never be forced to read what you already know."*

## Part 2 — Design doctrine (enforceable rules)
1. **Defeat the Expert Blind Spot (prime directive).** At every step that could confuse a first-timer, ask inline "why would someone seeing this for the first time get stuck here?" and answer it. A step is shown or cut — never "obvious."
2. **One new thing at a time.** Never introduce a new concept, new notation, and a hard computation together. When the idea is new, the numbers are easy.
3. **Concrete → Pictorial → Symbolic, in that order.** Symbols are the last step, never the first.
4. **Notation is a language we teach, not a code we assume.** (Part 4.)
5. **The formula is the destination, not the starting gun.** Derive every result from something already understood.
6. **Surface the wrong idea before the right one.** State and dismantle the tempting misconception inside the lesson.
7. **Depth ∝ difficulty × exam weight.** Uniform spacing is a defect. (Part 5.)
8. **Learn by retrieving.** Open each chapter with a 60-second retrieval of the prior chapter's load-bearing idea.
9. **Worked examples fade into independence.** First example fully narrated; next partially guided; capstone at full speed.
10. **Warm, plain, direct voice.** Write to a smart friend who hasn't seen this yet; preempt confusion; never a ten-dollar word where a one-dollar word is clearer.

## Part 3 — The Concept Lesson Arc (nine beats — replaces "summarizing")
Every Tier-A/B concept is built on this arc; the reference layer survives only at the end as the payoff.
1. **One-sentence idea (advance organizer)** — the whole concept in one plain sentence, before any symbol.
2. **Anchor + concrete instance** — tie to prior learning, then a specific numeric story from Ash's journey.
3. **Reason through the concrete case in words** — plain reasoning, no general notation yet.
4. **Surface and dismantle the tempting wrong idea** — show why it fails on the concrete case.
5. **Translate into notation, one glyph at a time** — introduce symbols by translating the plain sentence into symbols, each named and read aloud.
6. **Generalize: derive the formula from the instance** — the formula is the compression of what was just done.
7. **Ramp the difficulty** — simplest → twist that breaks easy intuition → general → edge/boundary cases.
8. **Picture or table** — a figure/grid for anything spatial or multi-step (dual-coding: words *and* image).
9. **Consolidate** — "here is what you can now do," then the **Pokédex Entry** (summary) + **Recognition Cue** (speed trigger).

**Teaching-first chapter skeleton:**
```
1. Cold Open (Episode — narrative motivation)
2. "Where you are" + 60-second retrieval of last chapter's key idea
3. Oak's Briefing (learning outcomes + Test-Out gate)
4. FOR EACH CONCEPT, in difficulty order:
     • "Do you already own this?" micro-check (skip path)
     • The Concept Lesson Arc (9 beats)              ← the teaching
     • Pokédex Entry (summary) + Recognition Cue (speed)
5. Worked Examples — faded guidance (full → partial → independent)
6. Trainer's Tips (exam craft)
7. Team Rocket's Trap (misconception, also mined in-lesson)
8. FROM KANTO TO THE REAL WORLD
9. The Gym Battle (capstone, expert-modeled)
10. The Gym Challenge (problem set — three tiers, to budget)
11. Answer Key (full worked solutions)
12. Badge Earned (mastery checklist mapped to outcomes)
```

## Part 4 — Notation taught as a language
- **"Reading the Symbols" primer (Ch 0 / front matter):** teaches how to read aloud Σ, ∫, ∈, | (given), P(·), E[·], subscripts, variable vs. realized value.
- **First-use law:** the first time any symbol appears it gets Beat-5 treatment (named + read aloud + motivated by translating English → symbol). Build check flags any symbol used before introduction.
- **Notation Ledger (`notation_ledger.md`):** every symbol, spoken name, plain meaning, first-introduction location. Powers the check and the appendix.
- **Spoken-form reuse** and **margin "say-it-aloud" glosses:** e.g. `E[(X−d)₊]` → *"the average amount paid after the deductible, never less than zero."*

## Part 5 — Depth calibration
| Tier | Definition | Treatment | Space |
|---|---|---|---|
| **A — load-bearing & hard** | high weight *and* hard | full 9-beat arc, full ramp, ≥1 figure, ≥3 faded worked examples | 4–7 pp |
| **B — important** | high weight *or* moderately hard | full arc, lighter ramp, ≥2 worked examples | 2–4 pp |
| **C — easy/mechanical** | low difficulty | abbreviated: one-sentence idea + concrete instance + notation + entry | 0.5–1.5 pp |

**Tier A:** Bayes & total probability · pmf/pdf/cdf/survival web · expectation & survival-function method · insurance loss-vs-payment model · joint/marginal/conditional & double integrals · conditional & double expectation & total variance · covariance & variance of linear combinations · CLT with continuity correction.
**Tier B:** combinatorics · each distribution's derivation & when-it-arises · transformations · order statistics · MGFs.
**Tier C:** set algebra & axioms · discrete uniform · basic counting · calculus/algebra toolkit (thorough but fully skippable in pieces).

## Part 6 — Expanded chapter map (16 chapters + 2 checkpoints)
Ch 0 Orientation · Ch 1 Toolkit I (numbers/variables/functions/notation) · Ch 2 Toolkit II (series & calculus) · Ch 3 Space of Possible Outcomes · Ch 4 Counting · **Ch 5 Reasoning From Evidence (Bayes) — Tier A proving ground** · *Checkpoint A* · Ch 6 Variables of Fortune (RV language) · Ch 7 Center & Spread (expectation/variance/MGF/Darth Vader) · Ch 8 Discrete Distributions · Ch 9 Continuous Distributions & Transformations · Ch 10 Pricing the Risk · *Checkpoint B* · Ch 11 Joint Distributions · Ch 12 Conditional & Double Expectation · Ch 13 Covariance & Sums · Ch 14 Order Statistics & CLT · Ch 15 Champion's Challenge (strategy + 3 mocks).
> Renumbering to this map is a later phase; the current repo keeps `chNN_*` names. The Bayes chapter is `book/chapters/ch04_cerulean_city.md`.

## Part 7 — Worked examples & problems
- **Faded guidance per concept:** ex1 fully narrated (every micro-step *and why chosen*); ex2 partially guided; Gym Battle expert-modeled at exam speed.
- **Understanding-first for hard ideas:** the first example of a Tier-A concept leads with **Professor's Path** (rigorous *why*) before **Trainer's Path** (fast *how*).
- **Problem bank 280–320 total**, weighted to exam weight; three tiers (Route Trainers → Gym Battles → Elite Challenge); every problem keeps a full worked solution, archetype tag, and back-reference.
- **Three full mock exams** (30 Q, ~8 General/14 Univariate/8 Multivariate).

## Part 8 — Integrity gates (run before any release)
1. **Programmatic answer verification** (`sims/verify_examples.py`, seed=151): every example/problem recomputed (closed-form or Monte Carlo) and asserted against the printed answer. Build fails on mismatch.
2. **Render audit:** no stray `$`, `\(`, `\)`, unescaped commands, broken fractions; proof every page at print resolution.
3. **Notation-before-introduction check** wired into the build.
4. **Self-correction policy:** intentional "watch this derail" moments framed as such or removed — never ambiguous with a real error.
5. **Copyright/asset audit:** instructional figures original/committed; sprite flourishes kept out of distributed/printed PDF or replaced with originals; disclaimer intact.
6. **Coverage guarantee:** every SOA outcome ≥8 problems; every in-scope distribution ≥6; mocks match weight split.

## Part 9 — The "Is this masterful?" checklist (a chapter isn't done until all hold)
**Teaching quality:** every Tier-A/B concept runs all nine beats in order · one-sentence idea before any symbol · concrete numeric instance before general notation · each new symbol introduced before use & logged in ledger · a natural misconception surfaced and dismantled in-lesson · each result derived (not asserted) · concrete→pictorial→symbolic respected, ≥1 figure/table per spatial or multi-step idea · difficulty ramp present · depth ∝ difficulty×weight · every potentially-confusing step answers "why would a first-timer get stuck here?"
**Practice:** worked examples fade full→partial→independent, hard concepts understanding-first · problem count meets budget & weight split with full solutions.
**Integrity:** all answers pass the harness; zero render artifacts; no ambiguous self-corrections; assets clean.
**Dual-use & readiness:** test-out gate at chapter and concept level · all mapped outcomes covered with teaching + ≥1 worked example · exam-weight signposted · mastery checklist maps one-to-one.
**The two ultimate gates (both must be yes):**
- **Cold-Read Test:** a reader who knew *none* of this could learn it from this section alone, no outside source.
- **Skip Test:** a reader who already knew it can prove mastery at the gate and move on without reading.

## Part 10 — Execution sequence
- **Phase 0 — Lock the model** (this document).
- **Phase 1 — Prove it on Chapter 5 (Bayes)** end-to-end in the full nine-beat style as the gold-standard reference. *(THIS SPRINT.)*
- **Phase 2 — Integrity harness** runs continuously.
- **Phase 3 — Roll hardest-first:** Tier-A chapters (6,7,10,11,12,13,14), then Tier-B (4,8,9), then foundations (0,1,2,3) and checkpoints.
- **Phase 4 — Final pass:** green verification build, page-by-page render proof, asset audit, "Reading the Symbols," notation appendix, exam-weight signposting, print-ready export.

## Part 11 — Preserve (do not regress)
Narrative-to-math fidelity · two-path worked examples · archetype tags · Team Rocket misconception traps (now also mined in-lesson) · the design system & colored boxes · the dual-use promise.

## Part 12 — Visual & UX (a Pokémon game that happens to be a math textbook)
**Strict separation of layers:** the Pokémon visual language owns the *frame, navigation, emotion*; mathematical typography owns the *content*; they never fight for the same pixel.
**Iron Rule of the math layer (non-negotiable):** wherever a concept/equation/derivation/solution lives, clarity wins absolutely — equations in clean high-contrast type on calm backgrounds, never over a sprite/map/texture; generous whitespace, single reading column, display math centered and unobstructed; no decoration may reduce the contrast/size/spacing an equation needs. If a flourish competes with a formula, the flourish is cut.
**Where the game layer lives (each element has a pedagogical job):** town/route headers (place & mood) · Kanto map progress strip (a literal progress bar) · gym-leader portrait + type badge (names the chapter's "boss"/difficulty) · Pokémon sprites in problem setups (make the random variable concrete) · badge icons (mastery tracker) · Poké Ball/item glyphs (wayfinding: Master Ball = highest-leverage shortcut, Poké Ball = routine method, Potion = gym-rematch pointer) · Pokédex "Actuary Mode" frame (the device that poses each problem) · type-color accents (color *means* something: theory/tip/trap/real-world).
**Box system as UI panels:** Pokédex Entry (blue device-screen) · Trainer's Tip (yellow item-callout) · Team Rocket's Trap (red "transmission intercepted") · FROM KANTO TO THE REAL WORLD (green field-journal) · Cold Open (cinematic banner + light narrative) · Concept gate "Do you already own this?" (Poké Center "heal or proceed" panel).
**Typography:** two type families — a display face for titles/banners/badges/chrome only; a clean classical text+math face for all body prose and equations (ornamented = navigation/flavor; plain = content). Math set with proper `\dfrac`, aligned multi-line derivations, sized delimiters — never inline-slashed fractions or collapsed exponents. Color must survive grayscale printing — every panel also has an icon and a label, color is never the only signal.
**The test for this layer:** *Could the reader cover every sprite, map, and badge with their hand and still learn the math perfectly?* (must be yes) *And does the page feel like Kanto?* (must be yes).

## Part 13 — Narrative immersion that teaches
**Three things held at once:** diegetic immersion, pedagogical rigor, real-world bridge.
**Spine:** you are Ash, actuary-in-training (2nd person, present tense); the Pokédex "Actuary Mode" poses every problem; season-long goal (8 badges = syllabus, Indigo Plateau = the exam); recurring cast with fixed teaching jobs (Oak formalizes, rival models the expert path, companions pose sub-problems, Team Rocket embodies the misconception); stakes escalate with difficulty.
**Integration mechanics:** (1) the world raises the question first (Cold Open → Beat 1); (2) the concrete instance is a real story beat with the situation's actual numbers; (3) **fidelity rule** — only use a Pokémon situation when it *behaves the way the math behaves*; a charming-but-wrong analogy is cut; (4) misconceptions happen to characters (Team Rocket's wrong method fails in-story); (5) problems are tasks, not exercises; (6) the capstone is the boss fight.
**Real-world bridge:** the green field-journal box appears *after* the concept is understood in-world; concrete named applications only (Poisson → claim frequency; deductibles → how auto/health policies are priced; Bayes → fraud detection & medical-test pricing; CLT → why pooling works); a "Series bridge" line where relevant; tone steps slightly out of character (Ash reflecting).
**Guardrails:** story may add a sentence, never hide a step; no story without a job; whimsy in the frame, precision in the core; immersion dialed to the concept's tier.
**Dual test (both must be yes):** **Immersion Test** (it feels like progressing through Kanto with real stakes) and **Transfer Test** (the reader can state the real-world actuarial use and solve a de-skinned exam problem with no Pokémon in it).

---
*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; educational, non-commercial work; exam details verified against the SOA Exam P syllabus (2026).*
