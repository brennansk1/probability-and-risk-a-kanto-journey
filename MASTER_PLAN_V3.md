# Probability & Risk: A Kanto Journey — V3 Master Plan
### Rebuilding the textbook around the TIA handouts + SOA syllabus, with a full Gen-1 narrative map

> **Status:** living planning doc. It governs the V3 re-write; v1's `DESIGN.md` / `FORMATTING.md` / `AUDIT.md` (in `Version 1/`) are ported and remain in force on production/format except where this file resequences the curriculum.

---

## 1. Context & intent

The repo holds a Pokémon-themed SOA **Exam P** textbook with a masterful teaching engine. The whole v1 book is archived in `Version 1/` to make room for a redesign around two authoritative documents placed at the root:

1. **`2026-09-p-syllabus.pdf`** — the official SOA Exam P syllabus. Governs **scope + weighting**: General Probability **23–30%**, Univariate RVs **44–50%**, Multivariate RVs **23–30%**; 23 lettered learning outcomes (1a–1g, 2a–2f, 3a–3i).
2. **`P-Single-file-Handouts.pdf`** — TIA's *Exam P Lesson Handouts* (David Revelle, PhD), 361 pp. Its table of contents is the **canonical teaching order**: **A. Discrete → B. Continuous → C. Multivariate**, each split into fine-grained lessons.

**Roles:** TIA = course structure & sequence. SOA = weighting + outcome checklist. v1 = quality bar, narrative engine, and prose to adapt.

**Locked decisions:**
- **Full fresh re-write** at v1's quality, TIA as the structural base, *all* topics covered.
- **Defer calculus** (TIA-style): Act I uses only algebra + inline series; a full Calculus Toolkit opens Act II (TIA `B.0`).
- **Match TIA subsection granularity** (~20 chapters, three acts).
- **Rich, immersive Gen-1 narrative**, faithful to the first-series anime; **same chapter format** as v1; every concept taught in an easy-to-understand way.

---

## 2. The structural pivots (TIA order vs. v1 order)

| Pivot | v1 did | TIA / V3 does |
|---|---|---|
| Calculus | Front as Ch 1–2 | **Deferred** to the start of Act II (`B.0`); discrete act = algebra + inline series |
| Discrete vs. continuous | Interleaved | **Fully separated** into Act A then Act B |
| Moments | After counting + RV language | **Before** named distributions; taught discrete-first (`A.3`), re-extended continuous (`B.2`) |
| Series (geometric, Taylor eˣ) | Front toolkit | **Inline interlude** right where geometric/Poisson need it (`A.5.0`) |
| Deductibles/limits | One "Pricing" chapter | **Twice** — discrete (`A.6`) then continuous (`B.5`) |
| CLT | Bundled w/ order stats | **With the Normal**, in the continuous act (`B.4`) |
| Order statistics | Bundled w/ CLT | **Alone** in the multivariate act (`C.3`) |
| MV moments | Double-exp before covariance | Covariance **first** (`C.2.2`), then conditional/double exp (`C.2.3`) |

---

## 3. The narrative spine — three acts = three movements of the Kanto journey

The book *is* the first-generation anime arc (Indigo League): you are **Ash Ketchum**, ten years old, leaving Pallet Town, bonding with **Pikachu**, dogged by **Team Rocket**, measured against your rival **Gary**, collecting **eight badges** on the road to the **Indigo Plateau** — except in this telling Professor Oak sets you a *dual* quest: become a Pokémon Master **and** an actuary who can price the risks trainers face. The Pokédex's **"Actuary Mode"** poses every problem.

The math's three-topic shape maps cleanly onto the journey's three natural movements:

- **ACT I — DISCRETE PROBABILITY · "The Countable Road."** Pallet Town to the Game Corner. The early journey, where everything is *countable*: which Pokémon steps out of the grass, how many Spearow, win or lose a slot pull. Algebra and counting are all you need. (SOA Topic 1 + the discrete half of Topic 2.)
- **ACT II — CONTINUOUS PROBABILITY · "The Smooth World."** You acquire the **HMs / field tools** (calculus) and enter Sabrina's Saffron, where reality warps into smooth, infinite-valued quantities — time, distance, measurement. (Rest of Topic 2.)
- **ACT III — MULTIVARIATE PROBABILITY · "The League."** Cinnabar, the Viridian Gym, Victory Road, the Indigo Plateau. Variables now move *together*: a team's performance is a sum of correlated parts; the strongest and weakest competitors are extremes; the championship is the exam. (Topic 3.)

**Emotional throughline (faithful to the anime's heart):** the unbreakable Ash–Pikachu bond (forged on Route 1); failure-as-growth; the rival always one step ahead; Team Rocket's schemes that fail in *instructive* ways; the slow accumulation of badges. **One licensed deviation:** in canon Ash loses at the Indigo League — here the League *is* the exam, and because you did the work, the finale is a win (a 9–10, not a coin-flip pass). The book "hits the iconic beats but deviates freely whenever Ash needs his actuarial skills."

**Journey & badge-order note.** The book follows the anime's characters, locations, and major arcs, but **sequences the badge challenges to honor the actuarial dependency chain** (e.g., Misty's reasoning-from-evidence gym is met before Brock's counting gym, because conditional probability precedes combinatorics in TIA). Ash backtracks constantly in canon, so this reads naturally; we state the convention once in the front matter.

---

## 4. Full chapter-by-chapter narrative + concept map

Files live in `book/chapters/`; the Makefile globs `ch*.md` lexicographically, so the zero-padded prefix **is** the reading order. Each chapter below gives: canon location/beat · the cold-open hook · the concept it motivates (and the **fidelity check** — the analogy is used only because the Pokémon situation *behaves the way the math behaves*) · gym leader/badge · Team Rocket's trap (the canonical misconception) · the real-world bridge · TIA source + SOA outcomes.

### Front matter (`book/frontmatter/`)
- `how-to-use.md` — the two-reader contract, the nine-beat arc, the box legend, exam facts, the badge tracker, the journey/badge-order convention.
- `diagnostic.md` — global skip diagnostic.
- `reading-the-symbols.md` — notation-as-language primer (Σ, ∫, ∈, | "given", P(·), E[·], variable vs. realized value).

---

### ACT I — DISCRETE PROBABILITY · "The Countable Road"

**`ch00_orientation.md` — Pallet Town, the night before.**
*Beat:* Ash can't sleep; in Oak's lab the Professor reveals the dual quest and hands over the Pokédex with "Actuary Mode." The Kanto map on the wall is literally the syllabus progress bar.
*Job:* orientation, how-to-use, exam facts (3 hr · 30 Q · scored 0–10 · normal table provided · TI-30XS). *TIA: front matter · SOA: —*

**`ch01_fundamentals.md` — Route 1: the Spearow swarm.**
*Beat:* Pikachu refuses the Poké Ball (the sample space is bigger than your assumptions). On Route 1 a flock of Spearow descends; you can't track every bird, so you reason about *events* — "at least one Spearow reaches Pikachu." A storm, a Thunderbolt, Ho-Oh's rainbow on the horizon (foreshadowing the perfect score). You wreck **Misty's** bike fishing Pikachu from the river; she joins.
*Concept:* sample space, events, axioms, unions/intersections, complements, Venn, De Morgan, inclusion–exclusion. *Fidelity:* "at least one of a flock" is exactly `1 − P(none)`.
*Boss:* none — Trainer's License. *Team Rocket's trap:* "mutually exclusive means independent" (their cage logic fails). *Real world:* insurers avoid double-counting overlapping coverages with inclusion–exclusion. *TIA: A.1.1–A.1.5 · SOA: 1a, 1d, 1e*

**`ch02_conditional.md` — Viridian City → Cerulean City: reasoning from evidence.**
*Beat:* Officer Jenny suspects Ash stole Pikachu; a saboteur has hit the Pokémon Center. Wet footprints are *evidence* — you update belief from base rates (who's common) and likelihood (who leaves prints). At Cerulean, **Misty's** gym is the proving ground.
*Concept:* conditional probability, independence, sequences of events, Bayes' theorem, law of total probability — the detective's grid. *Fidelity:* a culprit's identity is a hypothesis updated by evidence — textbook Bayes.
*Boss:* **Misty — Cascade Badge.** *Cast:* Oak builds the grid; Pikachu flags base-rate neglect. *Team Rocket's trap:* the prosecutor's fallacy — confusing `P(evidence|guilty)` with `P(guilty|evidence)`. *Real world:* medical-test false positives, fraud detection. *TIA: A.2.1–A.2.4 · SOA: 1c, 1e, 1f, 1g*

**`ch03_discrete_moments.md` — The S.S. Anne (docking at Vermilion).**
*Beat:* a luxury cruise too crowded to track passenger-by-passenger — you can only describe it by *distribution*. Then Team Rocket sinks the ship: a survival function made literal ("the ship survives past time x"). At Vermilion, **Lt. Surge** measures raw power (magnitude = mean) and reliability (spread = variance); Pikachu refuses the Thunder Stone (choosing its own distribution).
*Concept:* discrete RV, pmf/cdf/survival; mode, median, percentiles; expected value, tools for means, the **survival-function ("Darth Vader") method**; variance definition + tools; discrete uniform. *Fidelity:* `E[X] = Σ S(k)` *is* "how long the ship survives."
*Boss:* **Lt. Surge — Thunder Badge.** *Team Rocket's trap:* reporting the mode as if it were the mean. *Real world:* expected claim counts; why insurers price the average, not the typical case. *TIA: A.3.1–A.3.8 · SOA: 2a, 2c, 2d*

**`ch04_combinatorics.md` — Viridian Forest & Pewter City: counting the uncountable.**
*Beat:* Viridian Forest teems with more bugs and trainers than anyone can enumerate; you learn to count *by rule*. **Brock's** rock-solid logic test for the Boulder Badge is a counting gauntlet.
*Concept:* permutations, combinations, the **binomial**, multinomial, and **hypergeometric** distributions; the ordered/unordered × with/without-replacement classifier. *Fidelity:* drawing a team from a roster without replacement *is* hypergeometric.
*Boss:* **Brock — Boulder Badge.** *Team Rocket's trap:* counting ordered when order doesn't matter (double-counting arrangements). *Real world:* lottery/underwriting selection odds. *TIA: A.4.1–A.4.5 · SOA: 1b, 2d*

**`ch05_discrete_distributions.md` — Lavender Town & the Celadon Game Corner.**
*Beat:* in the Pokémon Tower, **Gastly/Haunter** appear in random counts (Poisson over a window); at the Game Corner the slot machine is a Bernoulli factory and "how many pulls until the first jackpot?" is geometric. A short **series interlude** ("summing an endless swarm of Caterpie" = geometric series; `Σλᵏ/k! = eλ` = the Taylor series for eˣ) gives you the only algebra these distributions need. Team Rocket runs the Game Corner (canon: their hideout is beneath it).
*Concept:* geometric series + Taylor for eˣ, then geometric, **memoryless property**, negative binomial, **Poisson**, sums of independent Poissons. *Fidelity:* memorylessness = the slot has no memory of past pulls.
*Boss:* **Erika — Rainbow Badge** (Celadon, grass = growth/distributions). *Team Rocket's trap:* gambler's fallacy ("we're due") — the geometric is memoryless. *Real world:* Poisson claim frequency; thinning/superposition. *TIA: A.5.0a–A.5.5 · SOA: 2d*

**`ch06_deductibles_discrete.md` — Fuchsia City & the Safari Zone.**
*Beat:* the Safari Zone hands every trainer a *fixed number* of Safari Balls and capped attempts — a deductible-and-limit world by design. The Warden hires you to price coverage against the cost of escaped Pokémon.
*Concept:* ordinary deductible `(X−d)₊`, policy limit `X∧u`, coinsurance, the calculator approach; `E[X∧u] + E[(X−d)₊]` relationships in the discrete setting. *Fidelity:* "you pay the first d yourself, the policy caps at u" *is* the Safari Zone's ball budget.
*Boss:* **Koga — Soul Badge** (poison/ninja). *Team Rocket's trap:* applying the deductible after the limit instead of before. *Real world:* exactly how auto/health policies compute payment. *TIA: A.6.1–A.6.3 · SOA: 2e, 2f*

**`ch07_checkpoint_discrete.md` — a Route campfire / minor tournament.**
*Beat:* a rest stop before the wilds change character; a small trainer tournament forces mixed retrieval of everything discrete. No new theory.
*Job:* spaced-retrieval checkpoint over Act I. *TIA: A.7.1 · SOA: 1*, 2**

---

### ACT II — CONTINUOUS PROBABILITY · "The Smooth World"

**`ch08_calculus.md` — Acquiring the HMs (a training montage with Oak / Bill's lighthouse).**
*Beat:* counting won't work where outcomes are continuous (time to faint, distance fled, measured weight). Oak issues the **field tools**: integration is "the net that sums infinitely many tiny outcomes"; the gamma identity is "the Master Ball of integrals — it catches the hard ones in one line."
*Concept:* differentiation (product/quotient/chain, optimization, L'Hôpital), integration (u-sub, by parts/tabular, improper integrals over [0,∞)), the **gamma integral** `∫₀^∞ x^{α−1}e^{−x/θ}dx = Γ(α)θ^α`. *Boss:* none — "HM acquired." *TIA: B.0.1–B.0.3 · SOA: prerequisite*

**`ch09_densities_cdfs.md` — Saffron City: Sabrina warps reality.**
*Beat:* **Sabrina's** psychic power makes reality *smooth and continuous* — no more discrete chips, now a density spread over a continuum. (Canon: Haunter beats Sabrina by making her laugh.)
*Concept:* continuous distributions overview, **densities & CDFs**, normalizing constants, mixed distributions. *Fidelity:* probability as area under a curve, not a sum of bars.
*Boss:* **Sabrina — Marsh Badge.** *Team Rocket's trap:* reading `f(x)` as a probability instead of a density (`f(x) > 1` panic). *Real world:* loss-size densities. *TIA: B.1.1–B.1.3 · SOA: 2a*

**`ch10_continuous_moments.md` — Saffron / Silph Co.**
*Beat:* measuring Sabrina's warped quantities — the same center/spread questions as the S.S. Anne, now with integrals.
*Concept:* moments of continuous distributions, moments of mixed distributions, the **survival-function approach** for continuous `E[X] = ∫₀^∞ S(x)dx`. *TIA: B.2.1–B.2.3 · SOA: 2c, 2d*

**`ch11_continuous_distributions.md` — the smooth wilds between cities.**
*Concept:* continuous **uniform** (basics + exam concepts), **exponential** (time-to-event, memoryless), **gamma** (sum of exponentials; the exponential/gamma/Poisson link), **beta** (proportions); **Pareto** as flagged enrichment. *Fidelity:* the exponential's memorylessness mirrors the geometric's — the continuous twin. *TIA: B.3.1–B.3.5 · SOA: 2d*

**`ch12_normal_clt.md` — a vast trainer gathering (P1 Grand Prix / League qualifier).**
*Beat:* thousands of trainers' results, individually unpredictable, aggregate into a predictable **bell**. The on-screen normal table is your only outside aid.
*Concept:* the **normal distribution** (68–95–99.7, standardization, table + interpolation), the **Central Limit Theorem**, **continuity correction**; **lognormal** as enrichment. *Fidelity:* pooling many i.i.d. results → normal is *why* leagues and insurers are predictable at scale.
*Team Rocket's trap:* forgetting continuity correction on a discrete sum. *Real world:* why pooling thousands of policies works. *TIA: B.4.1–B.4.5 · SOA: 2d, 3i*

**`ch13_continuous_deductibles.md` — Cinnabar Lab: pricing the volcano.**
*Beat:* the research station on a live volcano needs continuous-loss coverage; you re-derive the Safari-Zone deductible math with calculus.
*Concept:* deductibles **calculus approach**, deductibles **cases approach**, review of other continuous ideas (Act II checkpoint + the continuous loss-and-payment model). *TIA: B.5.1–B.5.3 · SOA: 2e, 2f*

---

### ACT III — MULTIVARIATE PROBABILITY · "The League"

**`ch14_joint.md` — Cinnabar Island: the Pokémon Mansion research logs.**
*Beat:* **Blaine's** mansion diaries (the Mewtwo experiment) record paired quantities together — power *and* stability, moving as one. Two variables, one joint law.
*Concept:* joint pmf/pdf/cdf, **double integrals over non-rectangular regions** (the hardest skill: inner limits), marginals by integrating/summing out, conditional distributions, independence via factoring over a rectangular support. *Fidelity:* two co-recorded measurements *are* a joint distribution.
*Boss:* **Blaine — Volcano Badge.** *Team Rocket's trap:* integrating over a rectangle when the support is a triangle. *Real world:* joint frequency–severity modeling. *TIA: C.1.1–C.1.2 · SOA: 3a, 3b*

**`ch15_joint_moments_cov.md` — Victory Road: the team as a combination.**
*Beat:* Victory Road's gauntlet forces your six Pokémon to perform as one unit — the team's strength is a **sum of correlated parts**, and ignoring the correlation dangerously misstates the risk.
*Concept:* joint moments `E[XY]`, **covariance**, **correlation** (−1≤ρ≤1; independence ⇒ ρ=0, not conversely), `Var(X+Y)` and general **linear combinations** `Var(ΣaᵢXᵢ)`; sums of independent in-family RVs (Normal+Normal, etc.). *Fidelity:* team synergy/anti-synergy = positive/negative covariance.
*Team Rocket's trap:* adding variances of correlated variables as if independent. *Real world:* portfolio risk is all covariance. *TIA: C.2.1–C.2.2 · SOA: 3c, 3d, 3e, 3g, 3h*

**`ch16_conditional_moments.md` — Viridian Gym: Giovanni unmasked.**
*Beat:* the eighth gym leader's true nature is hidden inside another role — **Giovanni**, secretly the Team Rocket boss. `E[X|Y]` is exactly that: the answer depends on the realized value of a hidden `Y`.
*Concept:* conditional expectation `E[X|Y]`, **law of total expectation** `E[X]=E[E[X|Y]]`, **law of total variance** `Var(X)=E[Var(X|Y)]+Var(E[X|Y])` (process vs. parameter variance → a credibility-theory bridge), compound/mixture distributions. *Fidelity:* a mixture's mean is an average of conditional means.
*Boss:* **Giovanni — Earth Badge.** *Team Rocket's trap:* using `E[X|Y]` as a number instead of a function of `Y`. *Real world:* credibility (CAS MAS-II), compound claims. *TIA: C.2.3 · SOA: 3c, 3d*

**`ch17_order_statistics.md` — Indigo Plateau: the Elite Four bracket.**
*Beat:* the field gathers; you care about *extremes* — the strongest and weakest competitors — and the order of a sorted draw.
*Concept:* order statistics of independent RVs: `F_max=[F]^n`, `F_min=1−[S]^n`, the k-th order statistic, min of independent exponentials, system reliability (series = min, parallel = max). *Fidelity:* "who wins the bracket" = the maximum order statistic.
*Boss:* **the Elite Four.** *Team Rocket's trap:* treating the max's CDF as `n·F` instead of `F^n`. *Real world:* reinsurance on the largest loss; reliability. *TIA: C.3.1–C.3.2 · SOA: 3f*

**`ch18_checkpoint_multivariate.md` — the night before the championship.**
*Beat:* final camp at the Plateau; mixed retrieval of the whole multivariate act. *Job:* spaced-retrieval checkpoint. *TIA: C.4.1 · SOA: 3**

---

### FINALE

**`ch19_champion.md` — The Championship match = the exam.**
*Beat:* Ash vs. **Gary** (the rival/benchmark) under the lights of the Indigo Plateau — which is the Prometric center in disguise. No new theory: this is execution.
*Job:* 6-minute pacing, two-pass strategy, calculator mastery, the consolidated **shortcut catalog** (gamma integral, Darth Vader, kernel recognition, memorylessness, Poisson mean=variance, binomial→Poisson, continuity correction), sanity checks, the error-log method, and **three full weight-matched mock exams** (~8 General / ~14 Univariate / ~8 Multivariate) with scored keys and pacing post-mortems. Readiness gates: 24/30, Earned Level 7+, six-minute pacing. *SOA: all*

### Appendices (`book/appendices/`, keep A–I)
A formula sheet · B distribution Pokédex (Field Guide) · C **normal table** (syllabus-provided) · D calculator guide · E exam-day · **F cross-reference — rewritten to map each chapter to its TIA section + commercial manuals (Ross, Wackerly, Hassett, etc.)** · G glossary (Kanto term ↔ formal term) · H answer keys · I Risk-and-Insurance primer.

---

## 5. The cast and their fixed pedagogical jobs (unchanged from v1)

- **Ash (you)** — second-person, present-tense protagonist; the actuary-in-training.
- **Professor Oak** — the formalizer; delivers rigorous definitions/axioms and runs the diagnostics ("the Professor's Path").
- **Pikachu** — the intuition check; reacts when reasoning "feels" off, foreshadowing a trap before it's named.
- **Misty & Brock** — companions who pose sub-problems from their expertise (Misty: water/luck/distributions; Brock: rock-solid counting/logic).
- **Gary Oak** — the benchmark/expert path ("the Trainer's Path"), always a step ahead; reappears at act boundaries and at the finale.
- **Team Rocket (Jessie, James, Meowth)** — the blunder-foil; every chapter they attempt the problem and commit its canonical misconception, which is then diagnosed in one line.
- **The eight gym leaders** — each is a chapter's "boss"; the badge is the mastery token (badge tracker = the appendix checklist).

---

## 6. Format — identical to v1 (non-negotiable)

Every chapter keeps v1's exact skeleton and the box system; only the order and content are new.

**Standard chapter skeleton (every chapter):**
1. **Cold Open (Episode)** — a second-person anime scene that is the chapter's core problem in disguise, ending on a question you can't yet answer.
2. **"Where You Are" + 60-second retrieval** of the prior chapter's load-bearing idea.
3. **Oak's Briefing** — the SOA outcomes discharged (tagged), the exam-weight signpost, and the **chapter Test-Out Gate**.
4. **For each concept, in difficulty order:** a "Do you already own this?" micro-gate → the **nine-beat Concept Lesson Arc** → a **Pokédex Entry** (summary) + **Recognition Cue**.
5. **Worked Examples — faded guidance:** Example 1 fully narrated (Professor's Path then Trainer's Path), Example 2 partially guided, the **Gym Battle** capstone at full exam speed.
6. **Trainer's Tip** (exam craft only).
7. **Team Rocket's Trap** (the canonical misconception, in-character, then the one-line fix).
8. **From Kanto to the Real World** (named actuarial application + a "Series bridge" to later exams).
9. **The Gym Challenge** (problem set, three tiers: **Route Trainers** → **Gym Battles** → **Elite Challenge**, counts scaled to syllabus weight).
10. **Full Answer Key** (complete worked solutions, archetype-tagged, back-referenced).
11. **Badge Earned** — a mastery checklist mapped one-to-one to the learning outcomes, with "Gym Rematch" pointers.

**The nine-beat Concept Lesson Arc (every Tier-A/B concept):** one-sentence idea → concrete instance → reason in words → surface & dismantle the tempting wrong idea → translate to notation one glyph at a time → derive the formula from the instance → ramp (simple → twist → general → edge) → picture/table → consolidate (Pokédex Entry + cue).

**Box system (UI panels, color + icon + label so they survive grayscale):** Pokédex Entry (blue device-screen) · Trainer's Tip (yellow item-callout) · Team Rocket's Trap (red "transmission intercepted") · From Kanto to the Real World (green field-journal) · Cold Open (cinematic banner) · Concept Gate (Poké Center "heal or proceed").

**Visual/UX iron rule:** the game layer owns the *frame, navigation, emotion*; math typography owns the *content*; they never fight for the same pixel. Equations always in clean high-contrast type on calm backgrounds, never over a sprite/map. *Test: cover every sprite with your hand and the math still teaches perfectly — and the page still feels like Kanto.*

**Markdown conventions (reuse exactly):** Pandoc fenced divs `::: class :::` for every box; `$…$` / `$$…$$` math; `<figure><img><figcaption>` for art; per-chapter metadata HTML comment (tier, outcomes, TIA source, locale); problems numbered `C{ch}.{n}`.

---

## 7. Teaching commitment — rich immersion *and* easy to understand

The two are not in tension; v1's doctrine delivers both, and V3 holds the same bar:
- **Two-reader contract:** assume nothing beyond arithmetic for the novice; let the reviewer prove mastery at a gate in 60 seconds and skip. *"You will never need an outside source to understand a concept here, and you will never be forced to read what you already know."*
- **One new thing at a time** (new idea ⇒ easy numbers); **concrete → pictorial → symbolic**; **derive, never assert**; **surface the misconception before the right idea**; **notation taught as a language** (first-use law + `notation_ledger.md`).
- **Depth ∝ difficulty × exam weight** (Tier A/B/C). Tier A for V3: Bayes · survival-function expectation · joint/marginal/conditional & region integrals · covariance & linear combinations · conditional/double expectation & total variance · CLT + continuity correction · insurance loss-vs-payment.
- **NO CONCEPT COMPRESSION (overriding rule).** Page/length budgets in this plan are *descriptive estimates, never caps*. A concept gets **however many pages it needs to be taught completely** — full nine-beat arc, full derivation, full ramp, every confusing step addressed. **The narrative and pacing wrap around the concept, not the other way around:** never trim, rush, or merge a concept's teaching to hit a length target or fit a story beat. If a concept needs 8 pages, it gets 8 pages and the story stretches to carry it. Where a length estimate and complete teaching conflict, completeness wins every time.
- **Fidelity rule for immersion:** a Pokémon situation is used *only* when it behaves the way the math behaves; a charming-but-wrong analogy is cut. Story adds a sentence, never hides a step.
- **Two ultimate gates per chapter:** the **Cold-Read Test** (a true novice can learn it here, no outside source) and the **Skip Test** (a reviewer can prove mastery at the gate and move on).

---

## 8. Coverage matrices (the master checklists — keep green)

**SOA outcome → chapter** (all 23 covered):
- 1a → ch01 · 1b → ch04 · 1c → ch02 · 1d → ch01 · 1e → ch01/ch02 · 1f → ch02 · 1g → ch02
- 2a → ch03 (disc) / ch09 (cont) · 2b → ch03/ch09/ch14 · 2c → ch03/ch10 · 2d → ch03/ch04/ch05/ch10/ch11/ch12 · 2e → ch06/ch13 · 2f → ch06/ch13
- 3a → ch14 · 3b → ch14 · 3c → ch15/ch16 · 3d → ch15/ch16 · 3e → ch15 · 3f → ch17 · 3g → ch15 · 3h → ch15 · 3i → ch12

**TIA leaf lesson → chapter:** every leaf from `A.1.1` through `C.4.1` maps to a chapter section (Act A → ch01–07, Act B → ch08–13, Act C → ch14–18). This matrix is enforced by `check_coverage.py`.

---

## 9. Infrastructure — reuse v1's pipeline wholesale

The build system is structure-agnostic (chapters auto-globbed by filename), so **port it unchanged** from `Version 1/` to the root and only author new content:
- `Makefile`, `requirements.txt` — copy as-is (`assets → figures → embed → verify → lint → pdf/book/workbook`).
- `tools/` — `check_format.py` (update `REQUIRED_HEADINGS` if a skeleton heading is renamed), `check_coverage.py` (point at the new outcomes + 20-chapter bank), `scaffold_v2.py` (generate the 20 empty chapters from §4), `workbook.lua`.
- `book/` chrome — `theme.css`, `workbook.css`, `mathjax-preamble.md`, `mathjax-config.html`, `frontmatter/title.html`, `fonts/`, `embed_visuals.py` — copy as-is.
- `figures/src/` — keep `generate_figures.py`, `sprite_util.py`, `kanto_theme.mplstyle`, `assets/download_*.py`; **rewrite `gen_chXX.py` per the new chapter list**.
- `problems/bank.d/` — one YAML per new chapter (`ch01.yaml`…`ch19.yaml`), same schema; re-tag to new chapter numbers + TIA sections; keep the seed-151 `sims/verify_examples.py` gate. Target ~280–320 problems, weight-matched; every outcome ≥8, every in-scope distribution ≥6.
- `syllabus/outcomes.yaml` — ensure all 23 outcomes with `min_per_outcome`.
- **`Version 1/` is the archive + prose source** — adapt overlapping concept prose into the new positions/skins; do not delete.

---

## 10. Authoring sequence (execution phases)

1. **Port infrastructure** to the root so the empty tree builds.
2. **Port/rewrite governing docs** (`DESIGN.md`, `FORMATTING.md`, `AUDIT.md`) to the V3 structure; reset `notation_ledger.md`; add both coverage matrices.
3. **Scaffold all 20 chapters + appendices** from §4 (`scaffold_v2.py`).
4. **Author a gold-standard reference chapter first** — `ch02_conditional.md` (Bayes, Tier-A) — to lock the V3 voice and format, exactly as v1's Phase 1.
5. **Roll out act by act, hardest-first within each act**; build the problem bank chapter-by-chapter alongside.
6. **Integrity + render pass:** `make verify`, `make lint`, full `make book` + `make workbook`, page-by-page render proof, asset/copyright audit.

---

## 11. Verification

- `make verify` → every example/problem recomputes to its printed answer (seed=151); build fails on mismatch.
- `make lint` → `check_format.py` (no stray `$`, balanced LaTeX, required headings, sprite rules) + `check_coverage.py` (every outcome ≥ min; every in-scope distribution covered).
- **Coverage matrices green** (§8): every TIA leaf lesson and SOA outcome maps to authored content.
- `make book` / `make workbook` render cleanly; spot-proof one chapter per act at print resolution.
- **Per chapter:** Cold-Read Test and Skip Test both pass.

---

## 12. Resolved threads (now fully specified in §15–§28)

All prior open threads are locked below — this plan is implementation-ready:

- Gym-leader ↔ chapter assignments, types, and journey throughline → **§15**.
- Per-chapter concept tiers, figure manifest, and problem budget → **§16**.
- Distribution roster, Pokédex-profile mascots & stat blocks, per-type color map → **§17**.
- TI-30XS calculator skill schedule & keypad spotlight keys → **§18**.
- Pareto/lognormal enrichment policy & checkpoint design → **§19**.
- Notation ledger seed & MathJax macros → **§20**.
- Target directory tree & file inventory → **§21**.
- Concrete infrastructure changes (Makefile, pandoc, scaffold, schemas, CSS) → **§22**.
- Front-matter & appendix content specs → **§23**.
- Mock-exam blueprint → **§24**.
- Definition of Done + execution roadmap → **§25**.
- Build discipline — four-layer verification, the wave engine, dossiers & inventory → **§26**.
- Figure-embedding architecture — token system + manifest + no-mutation build copy → **§27**.
- True progression & immersion — drill archetypes, the chapter questline, the Trainer Rank ladder → **§28**.
- Watch-Alongside TV-show tie-in — the locked episode map + `now-playing` boxes + viewing-guide appendix → **§29**.
- Visual immersion — sprites + figures to 10/10 (per-chapter visual manifest; rubric dim 12) → **§30**.

---

## 13. Calculator integration — the TI-30XS MultiView, taught to mastery

**Decision:** the book teaches **one** calculator, the **TI-30XS MultiView** (the SOA-allowed machine best suited to Exam P — MathPrint display, one-press `nCr`/`nPr`, and the data-list 1-Var-Stats engine). The BA II Plus is **not** taught; its guidebook stays archived as a reference only. Single-calculator fluency is the highest-leverage, lowest-risk exam strategy. Source of truth for keystrokes: `30XSMV_Guidebook_EN.pdf` (Statistics p23, Probability p29, Data Editor p32).

**Why this raises the pass rate:** Topic 2 (Univariate, 44–50% of the exam) is dominated by mean/variance of a pmf and by `nCr`/`e^x`/`ln` evaluations. A trainer who can drive the TI-30XS reflexively reclaims minutes per sitting and eliminates rounding errors. The flagship technique is the **data-list 1-Var Stats** workflow: enter outcomes in `L1`, probabilities (or frequencies) in `L2`, run `2nd → stat → 1-Var Stats`, and read `x̄` (the mean) and `σx` (whose square is the variance) directly — solving a huge share of Topic-2 questions in seconds.

**Design (reuses v1's proven scaffolding, now single-calculator + visual):**

1. **"Trainer's Calculator" primer (front matter / `ch00`).** Oak issues the TI-30XS MultiView as standard-issue gear alongside the Pokédex. Teaches setup once: modes/MathPrint, **clear-before-each-problem**, the **7 memory slots + `STO▸`** (store-don't-retype to kill rounding drift), fraction toggle `F◂▸D`, order of operations, answer toggle / `ans`.
2. **Just-in-time skill drops** — each calculator skill is introduced inside a **Trainer's Tip** exactly where the math first needs it, paired with a recognition cue and a key-cap keystroke strip:
   - `ch04` combinatorics → `prb` menu: `nCr`, `nPr`, `!` (binomial coefficients).
   - `ch03` discrete moments → the **1-Var Stats pmf workflow** (flagship, full worked treatment) + `STO▸` for `E[X]`.
   - `ch05` discrete distributions → `e^x` for Poisson; **Poisson-cdf recursion** with stored `e^{−λ}` and `p(k)=p(k−1)·λ/k`.
   - `ch08` calculus → `!` for the gamma integral; `e^x` evaluation at limits.
   - `ch11`/`ch12` continuous & normal → `e^{−x/θ}` survival in one keystroke; `STO▸` standardization `z=(x−μ)/σ`; continuity correction `±0.5` *before* standardizing.
3. **Appendix D rebuilt as a single-calculator field manual** — "The Trainer's Calculator: TI-30XS MultiView Field Manual," organized by operation (every Exam-P keystroke), with a **labeled keypad diagram** spotlighting the ~8 critical keys (`2nd`, `prb`, `data`, `stat`, `STO▸`, `F◂▸D`, `e^x`, `ln`), the `prb` menu, the data editor, and the 1-Var-Stats screen flow. Ends with a clean **single-calculator tear-out quick-reference card** (no more parity columns).
4. **Key-cap visual styling (new).** A `.kbd` CSS class renders keystrokes as little key-cap boxes so calculator notation is visually distinct from code; sequences render as a horizontal "keystroke strip." Authoring convention: pandoc **bracketed spans** — `[2nd]{.kbd}` `[prb]{.kbd}` — so add `+bracketed_spans` to the `PANDOC_FLAGS` `--from`. A `keycap()` / keystroke helper in `embed_visuals.py` emits the same markup for generated inserts. The keypad diagram is an original labeled schematic via a new `figures/src/gen_calc.py`.
5. **Calculator drills in the bank + mocks.** Add an optional `calc_skill:` field to the problem YAML; tag problems that train a specific technique (1-Var Stats variance, `nCr` binomial, `e^x` Poisson). The `ch19` mock exams enforce 6-minute pacing *with* the calculator in hand.
6. **Exam-day protocol (Appendix E), single-calculator:** bring **two** TI-30XS MultiView units (primary + backup), both **memory-cleared** the night before; allowed display settings are not memory; the cleared-memory rule and backup-unit rule stated plainly.

*No box-type proliferation:* all in-chapter calculator content lives in the existing **Trainer's Tip** box (now with key-cap visuals) and the **Pokédex keystroke entries**, per v1's "no box without a job" doctrine.

---

## 14. Figure & asset upgrade — richer, more immersive, all static (PDF + workbook)

**Decision:** stay **print-first and fully static** (300 DPI PNG, no animation/interactivity), but go lavish on real assets now that the **private repo** removes distribution concerns. Build on the existing modular pipeline — `embed_visuals.py` helpers, `figures/src/sprite_util.place_sprite()`, the `gen_chXX.py` generators, the PokeAPI + `pret/pokered` download scripts, and `kanto_theme.mplstyle`.

1. **Build out every required figure.** The nine-beat arc mandates a figure for any spatial/multi-step idea (Beat 8). Define a **per-chapter figure manifest** (in this doc) and a `gen_chXX.py` per new chapter; the format audit fails if a manifest figure is missing.
2. **Richer real assets (download freely).** Use **high-res official artwork** (`official()`) for chapter headers and **gym-leader boss portraits**; add new categories via new `assets/download_*.py` scripts (same idempotent/retry pattern): VS gym-leader portraits, Gen-1 **town/route backgrounds** (pret/pokered tilesets) for act/chapter banners, the **high-res FireRed Kanto region map** for the progress strip, a wider **item-icon** set, and overworld NPC sprites. In a private repo these may be committed *or* kept gitignored and fetched by `make assets` (recommended, to keep the repo light).
3. **Per-chapter type theming.** Each chapter already carries a Pokémon type (`{.type-water}` etc.). Drive a single **type→color map** (18 types) that tints both the **chapter banner** (gym-leader VS portrait + type color + the chapter's badge) and that chapter's matplotlib **figure accent** (a per-chapter accent over the shared `kanto_theme`).
4. **Distribution Pokédex profiles (flagship immersive asset).** Make `dex_profile()` real: every in-scope distribution gets a **Pokédex scan readout** — the TV-show device screen Ash sees when he catalogues a Pokémon. Each profile shows the behavior-matched mascot's official art (Poisson ↔ a random swarm; Exponential ↔ a Voltorb timer; Geometric ↔ keep trying until success), the show-style **Pokédex category** flavor line (e.g., Poisson = "the Swarm-Count Pokémon"), a **stat block** (support, pmf/pdf, mean, variance, MGF), the discrete/continuous "type," and the **recognition cue**. Rendered as a static composite (PIL/matplotlib layout) styled like the Pokédex UI. Each renders at the distribution's **Pokédex Entry** and all collect in **Appendix B** as the in-book **Pokédex / Field Guide**. *(No trading-card / TCG framing — this is the anime's catalogue device.)*
5. **Badge & map progress chrome.** A `progress_strip(chapter)` generator emits a small composite at each chapter open — the Kanto map with a marker at the current town and the **earned badges lit, unearned greyed** — making the syllabus-as-journey literal. Reuses the existing `badge()` assets.
6. **Tasteful sprite compositing in math figures.** Expand `place_sprite()` usage under the **iron rule** (art in margins, never over a curve/equation/axis): a mascot beside every pmf/pdf chart; Poké Ball / type-icon set markers in Venn diagrams; the sinking **S.S. Anne** in the survival-function figure; the **Safari-Zone ball budget** in deductible figures.
7. **"Pokédex Actuary Mode" frame (CSS, not raster).** Upgrade the box styling in `theme.css` with device-UI flourishes (corner brackets, an icon chip, a screen tint) around Pokédex Entries and problem statements — pure CSS so it stays crisp and print-perfect.
8. **New `embed_visuals.py` helpers:** real `dex_profile()`, `progress_strip()`, `vs_banner(leader, type, badge)` (chapter header), `boss_portrait()`, plus the `keycap()` keystroke helper from §13 — all idempotent-marker guarded.
9. **Fidelity & audit.** Everything 300 DPI; nearest-neighbor upscaling for pixel art; color-blind-safe (labels + hatching) and grayscale-survivable (icon + label, never color alone). Extend the asset audit to verify every referenced asset exists and every chapter has its manifest figures + progress strip + distribution Pokédex profiles. Keep the copyright disclaimer; note the build is private and non-distributed.

---

## 15. Locked journey throughline — chapter ↔ locale ↔ leader ↔ type ↔ badge

The book follows the anime's beats but **resequences badge challenges to honor the math-dependency chain** (stated once in front matter). Each chapter's **accent type** drives its banner color (§17 map) and figure accent; the **badge** is the mastery token shown earned at chapter close. Elite Four/Champion close Act III.

| Ch | Locale (cold-open) | Leader / boss | Accent type | Badge earned |
|---|---|---|---|---|
| 00 | Pallet Town (Oak's lab) | Professor Oak | Normal | Trainer's License |
| 01 | Route 1 (Spearow swarm) | — (tutorial route) | Flying | — |
| 02 | Viridian→Cerulean (the mystery) | **Misty** | Water | Cascade |
| 03 | S.S. Anne → Vermilion | **Lt. Surge** | Electric | Thunder |
| 04 | Viridian Forest → Pewter | **Brock** | Rock | Boulder |
| 05 | Lavender Tower → Celadon | **Erika** (Gastly motif) | Ghost | Rainbow |
| 06 | Fuchsia / Safari Zone | **Koga** | Poison | Soul |
| 07 | Route campfire (checkpoint) | — | Normal | (review) |
| 08 | Bill's lighthouse (HM training) | Oak / Bill | Steel | HM: Calculus |
| 09 | Saffron (Sabrina warps reality) | **Sabrina** | Psychic | Marsh |
| 10 | Saffron / Silph Co. | Sabrina (cont.) | Psychic | (Marsh cont.) |
| 11 | The smooth wilds | — | Water | — |
| 12 | The Grand Gathering (CLT) | — | Normal | — |
| 13 | Cinnabar Lab (volcano cover) | Oak / Blaine | Fire | — |
| 14 | Cinnabar Mansion logs | **Blaine** | Fire | Volcano |
| 15 | Victory Road | — (team gauntlet) | Ground | — |
| 16 | Viridian Gym (Giovanni) | **Giovanni** | Ground | Earth |
| 17 | Indigo Plateau (bracket) | **Elite Four** | Ice | (all 8 + Plateau) |
| 18 | Plateau eve (checkpoint) | — | Normal | (review) |
| 19 | Championship match = the exam | **Gary** (rival) | Dragon | Champion |

---

## 16. Per-chapter concept tiers, figure manifest & problem budget

Tier drives depth (A = full 9-beat + ramp + ≥3 faded examples; B = full arc, ≥2 examples; C = abbreviated). **These are floors, not ceilings — see the no-concept-compression rule (§7): a concept expands to whatever length fully teaches it; the page count is never a cap.** Figures listed are the `assets/diagrams/{name}.png` outputs of each `gen_chXX.py`; each is referenced via `diagram()`/`dex_profile()` (§22). Problem budget targets ~**330 teaching problems + 90 mock = ~420 total**, weight-matched (General ≈25% · Univariate ≈47% · Multivariate ≈28%); enforced minimums: every SOA outcome ≥8 problems, every in-scope distribution ≥6. Each teaching chapter's count also includes its **archetype quota** (≥3 audit, ≥2 rival_trap, ≥1 decision — §28) and its drills form one escalating **questline** (commission → legs → Gym-Battle boss → optional post-game).

| Ch | Tier(s) | Figures (`gen_chXX.py` outputs) | Problems |
|---|---|---|---|
| 00 | — | `kanto_progress_blank`, `book_map_legend` | 4 (calc setup) |
| 01 | C (set algebra), B (incl–excl) | `ch01_sample_space_box`, `ch01_venn_two`, `ch01_venn_three`, `ch01_incl_excl`, `ch01_me_vs_indep` | 20 |
| 02 | **A** | `ch02_bayes_grid`, `ch02_tree_sequential`, `ch02_total_prob`, `ch02_false_positive` | 26 |
| 03 | **A** | `ch03_pmf_cdf_survival`, `ch03_darthvader_area`, `ch03_mean_median_mode`, `ch03_variance_spread`, `dex_discrete_uniform` | 22 |
| 04 | B | `ch04_perm_vs_comb`, `ch04_2x2_classifier`, `dex_binomial`, `dex_multinomial`, `dex_hypergeometric` | 20 |
| 05 | B | `ch05_geometric_series`, `ch05_poisson_window`, `ch05_memoryless`, `dex_geometric`, `dex_negbinom`, `dex_poisson` | 24 |
| 06 | B | `ch06_deductible_limit`, `ch06_payment_per_loss`, `ch06_safari_budget` | 16 |
| 07 | (mixed) | `ch07_act1_mindmap` | 12 |
| 08 | C (skippable) | `ch08_deriv_rules`, `ch08_ibp_tabular`, `ch08_gamma_integral`, `ch08_improper` | 12 |
| 09 | B | `ch09_pdf_area`, `ch09_cdf_from_pdf`, `ch09_mixed_dist` | 16 |
| 10 | B | `ch10_continuous_moments`, `ch10_survival_integral` | 14 |
| 11 | B | `ch11_uniform`, `ch11_exponential`, `ch11_gamma_shapes`, `ch11_beta_shapes`, `dex_uniform_c`, `dex_exponential`, `dex_gamma`, `dex_beta`, `dex_pareto` | 22 |
| 12 | **A** | `ch12_normal_6895997`, `ch12_standardize`, `ch12_clt_convergence`, `ch12_continuity_correction`, `dex_normal`, `dex_lognormal` | 22 |
| 13 | B | `ch13_deductible_calculus`, `ch13_cases_approach` | 16 |
| 14 | **A** | `ch14_joint_grid`, `ch14_region_integral`, `ch14_marginal`, `ch14_conditional_slice` | 22 |
| 15 | **A** | `ch15_covariance_scatter`, `ch15_correlation_signs`, `ch15_linear_combo_var` | 20 |
| 16 | **A** | `ch16_total_expectation_tree`, `ch16_total_variance_decomp`, `ch16_mixture` | 18 |
| 17 | B | `ch17_order_max_min`, `ch17_kth_order`, `ch17_reliability_series_parallel` | 16 |
| 18 | (mixed) | `ch18_act3_mindmap` | 12 |
| 19 | — | `ch19_pacing_strip`, `ch19_shortcut_catalog` | 90 (3 mocks) |

Plus chapter-chrome figures auto-generated for **all** chapters by `progress_strip()` and `vs_banner()` (§14): `ch{NN}_progress`, `ch{NN}_banner`.

---

## 17. Distribution roster, Pokédex-profile mascots & the type→color map

**In-scope distributions** (taught to mastery), with the locked **Gen-1 mascot** whose behavior matches the math (fidelity rule), its home chapter, and the key stat block. Each renders as a Pokédex scan profile (§14) at the distribution's Pokédex Entry and collects in the Appendix B Field Guide.

| Distribution | Mascot (fidelity) | Ch | Support | Mean | Variance |
|---|---|---|---|---|---|
| Bernoulli(p) | Voltorb (one shock: 0/1) | 04 | {0,1} | p | pq |
| Binomial(n,p) | Pidgey flock (count of n) | 04 | 0…n | np | npq |
| Multinomial | Eevee (k evolution outcomes) | 04 | vectors | npᵢ | npᵢ(1−pᵢ) |
| Hypergeometric(N,K,n) | Magikarp pond (draw w/o replacement) | 04 | — | nK/N | nK/N·(N−K)/N·(N−n)/(N−1) |
| Geometric(p) | Meowth (keep trying until 1st success) | 05 | 1,2,… | 1/p | q/p² |
| Negative binomial(r,p) | Dugtrio (wait for r-th) | 05 | r,r+1,… | r/p | rq/p² |
| Poisson(λ) | Gastly swarm (random count/window) | 05 | 0,1,… | λ | λ |
| Discrete uniform{1..n} | Ditto (any form, equally likely) | 03 | 1…n | (n+1)/2 | (n²−1)/12 |
| Continuous uniform(a,b) | Porygon (flat, digital) | 11 | [a,b] | (a+b)/2 | (b−a)²/12 |
| Exponential(θ) | Electrode (memoryless timer) | 11 | [0,∞) | θ | θ² |
| Gamma(α,θ) | Magneton (sum of α units) | 11 | [0,∞) | αθ | αθ² |
| Beta(a,b) | Chansey (a proportion of luck) | 11 | [0,1] | a/(a+b) | ab/[(a+b)²(a+b+1)] |
| Normal(μ,σ²) | Clefairy (Mt. Moon bell) | 12 | ℝ | μ | σ² |

**Enrichment-only (flagged, never gated — taught because TIA does, but marked "off-syllabus"):**

| Distribution | Mascot | Ch | Note |
|---|---|---|---|
| Pareto | Snorlax (rare but enormous → heavy tail) | 11 | enrichment box |
| Lognormal | Gyarados (Magikarp's multiplicative growth) | 12 | enrichment box |

**Type → color map** (drives `.type-*` CSS banners + matplotlib accents; full 18 for completeness, Gen-1 leaders use the first eight):

`Normal #A8A878` · `Fire #F08030` · `Water #6890F0` · `Electric #F8D030` · `Grass #78C850` · `Ice #98D8D8` · `Fighting #C03028` · `Poison #A040A0` · `Ground #E0C068` · `Flying #A890F0` · `Psychic #F85888` · `Bug #A8B820` · `Rock #B8A038` · `Ghost #705898` · `Dragon #7038F8` · `Dark #705848` · `Steel #B8B8D0` · `Fairy #EE99AC`.

Single source of truth: `figures/src/type_palette.py` (Python dict) + `:root` CSS custom properties in `book/theme.css` (kept in sync; the audit checks parity).

---

## 18. TI-30XS MultiView — skill schedule & keypad spotlight

**Keypad diagram spotlight keys** (highlighted in the `gen_calc.py` schematic, Appendix D): `[2nd]`, `[prb]` (→ nCr / nPr / !), `[data]`, `[2nd][stat]` (1-Var Stats), `[STO▸]` + recall `[2nd][recall]`, `[F◂▸D]`, `[e^x]` (`[2nd][ln]`), `[ln]`, `[x²]`, `[^]`, `[(-)]`, `[2nd][clear var]`.

**Skill schedule** (each introduced once, where first needed, in a Trainer's Tip with a `.keystroke` strip; reinforced later):

| Ch | Calculator skill | Canonical keystroke |
|---|---|---|
| 00 | Setup, clear, store-don't-retype | `[mode]` … ; `[STO▸][x]` ; `[2nd][clear var]` |
| 01 | Complement arithmetic | `1 [−] 0.8 [^] 12 [enter]` |
| 04 | Binomial coefficient | `12 [prb] →nCr 6 [enter]` |
| 04 | Permutations / factorial | `[prb] →nPr` ; `n [prb] →!` |
| 03 | **1-Var Stats pmf** (flagship) | `[data]` L1=values, L2=probs ; `[2nd][stat] 1-Var ; FRQ:L2` → read `x̄`, `σx` (var = σx²) |
| 05 | Poisson via stored eᵏ + recursion | `[2nd][e^x][(-)]λ [STO▸][a]` ; `p(k)=p(k−1)·λ/k` |
| 08 | Gamma factorial, eˣ at limits | `[prb] →!` ; `[2nd][e^x]` |
| 11 | Exponential survival | `[2nd][e^x][(-)] x [÷] θ [enter]` |
| 12 | Standardize with stored μ,σ | `( x [−] μ ) [÷] σ` with `[STO▸]` |
| 12 | Continuity correction | apply `±0.5` **before** standardizing |

Problems tagged `calc_skill:` drill these; `ch19` mocks run them under 6-minute pacing.

---

## 19. Enrichment policy & checkpoint design

**Enrichment (Pareto, lognormal, and any TIA-taught-but-off-syllabus margin):** taught in a clearly labeled `::: enrichment` box (new class, §22) headed *"Beyond the Syllabus — for the curious / future exams."* Never behind a test-out gate, never in the mastery checklist, never counted toward outcome coverage; one worked example max, no problem-bank minimum. This honors TIA's completeness without diluting exam focus.

**Checkpoints (`ch07` after Act I, `ch18` after Act III; the Act II checkpoint is folded into `ch13`'s review):** ~2–4 pp each, **no new theory**. Structure: a one-page concept mind-map figure → 60-second retrieval grid of the act's load-bearing ideas → 12 **mixed** problems at exam difficulty drawn across the act (full solutions, archetype-tagged) → a "you're ready when…" gate. Light narrative wrapper only (a campfire / pre-final-night beat); no gym battle. Mock-style mixing here is the spaced-retrieval payoff.

---

## 20. Notation ledger seed & MathJax macros

`notation_ledger.md` is reset and seeded with the core symbols; the build's notation-before-introduction check reads it. MathJax macros live in `book/mathjax-preamble.md` (first Pandoc input).

**Seed symbols** (symbol · spoken · meaning · first intro): `S` "the sample space" (ch01) · `∅` "the empty set" (ch01) · `∈ ⊆` "is in / is a subset of" (ch01) · `∪ ∩ Aᶜ` "union / intersection / complement" (ch01) · `P(A)` "probability of A" (ch01) · `P(A∣B)` "probability of A given B" (ch02) · `~` "is distributed as" (ch04) · `p(k)` "pmf" (ch03) · `F(x)` "cdf" (ch03) · `S(x)` "survival function" (ch03) · `E[X]` "expected value" (ch03) · `Var(X)` "variance" (ch03) · `M_X(t)` "moment generating function" (ch03) · `f(x)` "density" (ch09) · `Γ(α)` "gamma function" (ch08) · `(X−d)₊` "payment after deductible" (ch06) · `X∧u` "loss capped at u" (ch06) · `Cov, Corr, ρ` (ch15) · `E[X∣Y]` "conditional expectation" (ch16) · `x̄, σx` "calculator mean / population sd" (ch03 calc).

**Macros (port from v1, confirm present):** `\E`, `\Var`, `\SD`, `\Cov`, `\Corr`, `\given` ( `\,|\, `), and distribution operators `\Bin \Pois \Geo \NB \HG \Unif \Exp \Gam \Bet \Norm`.

---

## 21. Target directory tree (built fresh at repo root; `Version 1/` stays archived)

```
/ (repo root, private)
├── MASTER_PLAN_V3.md  DESIGN.md  FORMATTING.md  AUDIT.md  README.md  LICENSE.md
├── Makefile  requirements.txt  notation_ledger.md  .gitignore
├── 2026-09-p-syllabus.pdf  P-Single-file-Handouts.pdf  30XSMV_Guidebook_EN.pdf
├── book/
│   ├── frontmatter/  (title.html, how-to-use.md, diagnostic.md, reading-the-symbols.md, trainers-calculator.md)
│   ├── chapters/     (ch00…ch19 — 20 files per §4/§15)
│   ├── appendices/   (appendix_a…i per §23)
│   ├── theme.css  workbook.css  mathjax-preamble.md  mathjax-config.html  embed_visuals.py  fonts/
├── figures/src/  (generate_figures.py, sprite_util.py, kanto_theme.mplstyle, type_palette.py, gen_calc.py, gen_ch00…gen_ch19.py, gen_dex.py)
├── problems/bank.d/  (ch00…ch19.yaml)   problems/schema.md
├── sims/verify_examples.py
├── syllabus/outcomes.yaml
├── tools/  (check_format.py, check_coverage.py, scaffold_v2.py, workbook.lua)
├── workbook/  (workspace_sizes.json)
├── assets/  (download_*.py, upscale_assets.py ; built subdirs gitignored: sprites/, official/, badges/, characters/, items/, maps/, backgrounds/, vs/, diagrams/, dex/)
└── build/  (HTML + PDF outputs, gitignored)
```

---

## 22. Concrete infrastructure changes (delta from the ported v1 pipeline)

- **`Makefile`** — extend `PANDOC_FLAGS --from=` with `+bracketed_spans` (enables `[2nd]{.kbd}`). Add `gen_dex.py` and `gen_calc.py` to the `figures` target. No new top-level targets.
- **`tools/check_format.py`** — set `REQUIRED_HEADINGS` to the §6 skeleton: `Cold Open`, `Where You Are`, `Oak's Briefing`, `Gym Challenge`, `Answers`, `Badge Earned`. Add checks: every `.kbd` span non-empty; every `dex_profile` name in the §17 roster; `.type-*` class matches a §17 type.
- **`tools/check_coverage.py`** — read `syllabus/outcomes.yaml`; assert each of the 23 outcomes ≥8 problems, each in-scope distribution ≥6, mocks match the weight split; enrichment distributions exempt. **Also enforce the §28 per-chapter archetype quotas** (audit ≥3, rival_trap ≥2, decision ≥1) and **validate each chapter's dossier coverage manifest** is fully satisfied.
- **`problems/bank.d/*.yaml`** — extend schema with optional `tia_section:`, `calc_skill:`, and the §28 immersion fields `actor:`, `stakes:`, `consequence:`, `archetype:` (enum: `audit | rival_trap | decision | standard`), `quest_step:` (mission ordering), `depends_on:` (threaded prior problem — value also restated as a given). Keep `id, chapter, tier, outcomes, distributions, provenance, difficulty, narrative_hook, statement, solution, answer, shortcut_used, verify`. Tier vocabulary: `route_trainer | gym_battle | elite_challenge | mock`.
- **`book/embed_visuals.py`** — **token-resolution rewrite (§27):** parse `{{fig:…}}`/`{{dex:…}}`/`{{badge:…}}`/`{{sprite:…}}`/`{{vs:…}}`/`{{banner:…}}`/`{{progress:…}}`/`{{keycap:…}}` against `figures/manifest.yaml`, resolve via helpers `dex_profile`, `progress_strip(chapter)`, `vs_banner(leader,type,badge)`, `boss_portrait(leader)`, `keycap`/`keystroke`, and write into **`build/` working copies** (never mutate `book/`). `progress_strip`/`vs_banner` read `book/ranks.yaml`.
- **New files:** `figures/manifest.yaml` (slug→generator/chapter/caption/alt), `book/ranks.yaml` (badge-count→rank), `docs/design/chNN.md` dossiers (each with a coverage manifest), `docs/BOOK_INVENTORY.md`, `book/chapters/_TEMPLATE.md`.
- **`book/theme.css`** — add classes: `.kbd`, `.keystroke` (§13 key-caps), `.dex-profile`, `.vs-banner`, `.enrichment` (§19), `.type-{18}` (§17), and the Pokédex-frame device flourishes (§14.7) on `.pokedex-entry`/problem blocks; add the 18 type colors as `:root` custom properties.
- **`figures/src/`** — new `type_palette.py` (the §17 dict), `gen_calc.py` (keypad schematic), `gen_dex.py` (the Pokédex-profile compositor), and `gen_ch00…gen_ch19.py` per §16.
- **`assets/`** — new `download_backgrounds.py` (pret/pokered town/route tiles), `download_vs.py` (gym-leader VS portraits), and an extended item set; all idempotent/retry, gitignored output, pulled by `make assets`.

---

## 23. Front-matter & appendix content specs

**Front matter:** `how-to-use.md` (two-reader contract, nine-beat arc, box legend incl. `.kbd`/`.enrichment`, exam facts, badge tracker, journey/badge-order convention) · `diagnostic.md` (global skip diagnostic) · `reading-the-symbols.md` (the §20 primer) · `trainers-calculator.md` (the §18 TI-30XS primer).

**Appendices (A–I):**
- **A — Master formula sheet:** every §17 stat block + the shortcut catalog (gamma integral, Darth-Vader survival, MGF kernel recognition, memorylessness, Poisson mean=variance, binomial→Poisson, continuity correction). One-page fold-out.
- **B — Distribution Pokédex (Field Guide):** all §17 Pokédex profiles, in-scope then enrichment, with recognition cues.
- **C — Normal table:** the SOA-provided Φ(z) table + symmetry/inverse techniques (matches on-screen exhibit).
- **D — TI-30XS MultiView Field Manual:** §18 keypad diagram, by-operation keystrokes, the `prb`/`data`/`stat` flows, the 1-Var-Stats pmf walkthrough, tear-out quick-reference card.
- **E — Exam day:** logistics, CBT interface, cleared-memory rule, two-TI-30XS backup rule, two-pass plan, nerves.
- **F — Cross-reference:** each chapter → its TIA section (A.1.1…C.4.1) + commercial-manual chapters (Ross, Wackerly, Hassett, ASM/Finan) + SOA sample-question numbers.
- **G — Glossary:** Kanto term ↔ formal term (e.g., "Darth-Vader rule" ↔ survival-function expectation).
- **H — Answer keys:** consolidated full solutions, archetype-labeled, back-referenced to the Pokédex Entry + shortcut used.
- **I — Risk & Insurance primer:** the SOA-assumed background for the loss/payment outcomes (supports ch06/ch13).

---

## 24. Mock-exam blueprint (`ch19`)

Three full exams, each **30 questions / 3 hours / scored 0–10 (6 passes)**, weight-matched: **~8 General · ~14 Univariate · ~8 Multivariate**, archetype-balanced so each spans the act's load-bearing skills. Five choices A–E, one correct; no penalty for guessing (answer every question). Each exam ships with: a scored key, full worked solutions (archetype-tagged, calculator path noted), and a **pacing post-mortem** template (per-question time, error-log root-cause categories). Readiness gates restated: **24/30**, Coaching Actuaries **Earned Level 7+**, steady **6-minute** pacing. Mock questions live in `problems/bank.d/ch19.yaml` with `tier: mock`.

---

## 25. Definition of Done & execution roadmap

**Per-concept DoD:** all nine beats present in order; one-sentence idea before any symbol; concrete instance before general notation; each new symbol introduced + logged in the ledger; a misconception surfaced and dismantled; the result derived, not asserted; ≥1 figure for any spatial/multi-step idea; difficulty ramp present.

**Per-chapter DoD:** all 11 skeleton parts (§6); tier-correct depth (§16); every mapped SOA outcome taught + ≥1 worked example; all §16 figures built and embedded; calculator skill (if scheduled, §18) present with a `.kbd` strip; problem budget met with full solutions and passing `verify:`; Badge-Earned checklist maps 1-to-1 to outcomes; **Cold-Read Test** and **Skip Test** both pass; **no concept compression** — the re-grade confirms every concept is taught to completion, nothing rushed or truncated to save space. **Plus (§26/§28):** passes **blind adversarial re-derivation** (Layer 3); drills form a coherent **questline** (commission → legs → Gym-Battle boss → optional post-game) that pays off the cold-open; the **archetype quotas** and **dossier coverage manifest** are both met; ≥1 drill recycles the chapter's canonical error; the cast micro-arc is present; chained problems are self-contained for `verify:`; the progress strip shows correct rank/badges/readiness.

**Global DoD:** both coverage matrices (§8) green; `make verify` (seed 151) and `make lint` clean (incl. token/manifest + grid-count assertions, §27); `make book` + `make workbook` render without artifacts (0 "could not fetch"); asset audit passes (every referenced asset exists; every chapter has banner + progress strip + manifest figures + Pokédex profiles); a **full blind re-derivation across all chapters** with zero unresolved discrepancies; the **independent Exam-P tutor re-grade** (Layer 4) gives a **letter grade of A** on the comprehensive rubric — the QA loop (fix → re-grade) repeats until an A is earned; nothing ships below an A; copyright disclaimer intact.

**The grade-until-A gate (Layer 4, mandatory).** After a chapter is fully generated, a fresh independent Exam-P **tutor agent** (no authoring context) grades it on a comprehensive rubric and assigns a **letter grade**. Rubric dimensions (each scored, with evidence): (1) mathematical correctness & rigor; (2) **teaching completeness — every concept fully developed with NO compression** (full nine-beat, full derivation, full ramp; flag any rushed/truncated/over-merged concept); (3) notation taught before use; (4) pacing & one-lesson focus; (5) structure/format adherence (§6); (6) immersion in openers AND drills + the questline (§28); (7) calculator integration (§13); (8) Cold-Read Test; (9) Skip Test; (10) exam-readiness (would these problems + teaching produce a 9–10 scorer); (11) **watch-alongside fidelity** (§29) — an accurate `now-playing` episode tie-in whose cold-open/beats track the cited Indigo-League episode(s), embellishments labeled, so reading reinforces watching; (12) **visual immersion** (§30) — rich real-asset visuals: math figures that composite real Pokémon sprites + real sprite/cast/badge images embedded at their beats, all iron-rule compliant, with **no fabricated/generated sprite art** (real online assets only); (13) **TIA conformance** (§31) — concepts appear in TIA teaching order at the depth TIA requires; narrative + figures are integrated into that flow, never padding or reordering it. The tutor returns a letter grade + a prioritized defect list. **An A requires dimension 12 (figure immersion) ≥ 9, dimension 11 (episode tie-in) present and accurate, and dimension 13 (TIA conformance) ≥ 9.** **If below A, fix every item and re-grade; loop until A.** Only then is the chapter ✅ in `BOOK_INVENTORY.md`. The same gate runs once more on the full assembled book before release.

**Execution roadmap (ordered):**
1. **Port infrastructure** (§21/§22): copy v1 pipeline to root, apply the deltas, confirm an empty tree runs `make html`.
2. **Governing docs:** finalize this plan; port/rewrite `DESIGN.md`, `FORMATTING.md`, `AUDIT.md` to V3; seed `notation_ledger.md` (§20); write `syllabus/outcomes.yaml`; create `type_palette.py`.
3. **Scaffold** all 20 chapters + 4 front-matter + 9 appendices via `scaffold_v2.py` (§6 skeleton).
4. **Asset base:** run `make assets` (sprites, official art, badges, VS portraits, backgrounds, map); build `gen_calc.py` keypad + `gen_dex.py` for all §17 Pokédex profiles.
5. **Dossiers:** write `docs/design/chNN.md` for the wave's chapters (coverage manifest + worked examples + canonical error + cast micro-arc + questline + figure slugs).
6. **Gold-standard chapter:** author `ch02_conditional.md` end-to-end (Tier A) to lock voice/format; pass the full DoD incl. Layer-3 blind re-derivation before scaling.
7. **Roll out by act, hardest-first, via the §26 wave engine** (waves of ~3: author in parallel from dossiers → orchestrator's integrated harness self-gate → blind-verify each → fix + whole-book stale-value grep → mark done in `BOOK_INVENTORY.md`): Act I (`ch01,03,04,05,06` then `00,07`) → Act II (`ch08–13`) → Act III (`ch14–17` then `18`) → finale (`ch19` + mocks). Build each chapter's `gen_chXX.py` figures and `bank.d/chXX.yaml` alongside the prose.
8. **Appendices** (§23) once their source chapters are stable.
9. **Integrity + render pass:** green `make verify`/`lint`, full `book`+`workbook`, page-by-page proof at print resolution, final asset/copyright audit, **full blind re-derivation across all chapters, then the Layer-4 independent re-grade** until the reviewer says ship it.

---

## 26. Build discipline — the Replication Playbook applied to V3

The sibling FM book's method is adopted wholesale: **a theme is a skin over a verified skeleton, and the two are kept strictly separate.** V3 already has the skeleton pieces (Markdown chapters, a `verify:`-carrying bank, code-generated figures, `outcomes.yaml`); this section adds the *discipline* that made the FM book trustworthy.

**Four-layer verification (every chapter passes all four):**

| Layer | Mechanism | Catches |
|---|---|---|
| 1. **Harness** | `sims/verify_examples.py`, fixed **seed 151** — recomputes every `verify:` from scratch | wrong final answers in the bank; runs every build, 100% must pass |
| 2. **Structural lint** | `check_format.py` + `check_coverage.py` | missing sections, coverage gaps, weighting, malformed structure |
| 3. **Blind adversarial re-derivation** | a **fresh agent per chapter, no authoring context**, re-derives every worked example/problem and reports mismatches | **prose-vs-bank drift** — the harness verifies the *bank*; chapter *prose* re-types numbers by hand and drifts. Where most real defects hide. **Non-negotiable, every chapter, every wave.** |
| 4. **Independent re-grade** | a fresh reviewer in a **subject-tutor persona** grades the finished chapter on a fixed rubric | pedagogy, pacing, immersion, "would I teach from this" |

**The lesson stated loudly:** *harness-pass ≠ chapter-correct.* The harness checks the bank; only blind re-derivation (Layer 3) catches a stale intermediate or a wrong boxed answer in the prose. Budget for it on every chapter.

**The wave engine (authoring loop):** (1) **Select** the next ~3 chapters, **hardest-first** (weight × difficulty); (2) **Author** in parallel — one agent per chapter from its **dossier** (`docs/design/chNN.md`) against `_TEMPLATE.md` + the gold-standard exemplar; (3) **Self-gate** on the orchestrator's **own integrated harness run** after all writes land — *never* trust parallel agents' reports about each other; (4) **Blind-verify** each chapter (Layer 3); (5) **Fix**, re-run the harness, and **grep the whole book for any changed value** (stale copies hide in gates, tables, appendices, cross-refs); (6) **Mark done** in `docs/BOOK_INVENTORY.md`; reschedule.

**New docs:** `docs/design/chNN.md` **dossiers** (derived-vs-memorized, each worked example, the canonical error, the calculator path, the cast micro-arc, the figure slugs, the drill-archetype quota, the **coverage manifest**); `docs/BOOK_INVENTORY.md` (live status board); `book/chapters/_TEMPLATE.md` (the §6 skeleton); `AUDIT.md` (the four-layer definitions). Gold-standard exemplar = **`ch02_conditional.md`**, taken to a genuine 10 before any wave scales.

**Failure modes to design around:** trusting cross-agent reports; verifying figures by grepping built HTML (filenames vanish under `--embed-resources`); the workbook silently injecting zero workspace on a class mismatch; forgetting a token-bearing directory in the embed scope; left-in author scaffolding; stale values after a fix.

---

## 27. Figure & asset embedding architecture (decided after exploration)

**Finding.** V1 chapters carry **hardcoded inline `<figure>` HTML** (bloats prose, not lintable) alongside an **empty marker-insertion `embed_visuals.py`** (central `INSERTIONS` dict, idempotent markers, **mutates `book/chapters/*.md` in place, no backup, fragile substring anchors**). Pandoc flags are already correct (`--standalone --embed-resources --resource-path=…`); the workbook Lua keys on `::: problem-set`, which **matches** the chapters today.

**Decision — adopt a token system (FM-proven), with a manifest and a no-mutation build copy.** Cleanest, most lintable, most immersion-friendly choice for a 20-chapter rewrite:

1. **Author figures as tokens in prose**, never raw HTML: `{{fig:ch03_pmf_cdf_survival}}` · `{{dex:poisson}}` (Pokédex profile, §17) · `{{badge:cascade}}` · `{{sprite:gastly}}` · `{{vs:misty}}` (gym-leader banner) · `{{banner:ch02}}` · `{{progress:ch05}}` (rank/badge strip, §28) · `{{keycap:2nd,prb,nCr}}` (calculator strip, §13).
2. **`embed_visuals.py` resolves each token** to the §14.8 helper's `<figure>/<img>` (`diagram`, `dex_profile`, `badge`, `vs_banner`, `progress_strip`, `keycap`, …); Pandoc `--embed-resources` base64-inlines it.
3. **Single source of truth: `figures/manifest.yaml`** — every slug → `{generator, chapter, caption, alt}`. `check_format.py` asserts every `{{…}}` token resolves to a manifest entry, every entry is referenced ≥1×, **all slugs match `^[a-z0-9_]+$`** (reject uppercase loudly — the silent-skip bug), and `alt` is present.
4. **No source mutation.** The embed step writes into **`build/` working copies**, leaving `book/` pristine (cleaner than tar-backup→restore, same guarantee).
5. **Embed scope = every token-bearing directory:** `frontmatter/`, `chapters/`, `appendices/`.
6. **Verify embedding by build log, not grep:** success = `0` "could not fetch" warnings + token/manifest lint green (base64 hides filenames in the HTML).
7. **Workbook integrity:** `check_format.py` asserts the Lua class string (`problem-set`) matches the chapters' div class; the build asserts **injected-grid count == problem count**.
8. **Best-embed-for-immersion:** Beat-8 mandates a figure for any spatial/multi-step idea; `{{banner:chNN}}` + `{{progress:chNN}}` auto-open every chapter; `place_sprite()` compositing stays under the **iron rule** (margins only). (Cross-ref §14, §16.)

---

## 28. True progression & immersion (decided after exploration)

**Diagnosis (honest scores from the bank audit):** chapter **openers 9/10**, practice **drills 4/10**, **progression ~4–6/10**. `narrative_hook` is cosmetic (a place/action, never an actor + stake; never enters the `statement`); Team Rocket's canonical error lives only in prose, never as a drill; Gary never poses a trap; badges are per-chapter with no cumulative rank. **The theme is cosmetic on the drills — exactly the FM failure mode. Fix from the start; retrofitting ~330 stems later is a whole extra pass.**

### Fix A — push immersion *into the drills*
- **Schema additions** (`problems/bank.d/*.yaml`): `actor:`, `stakes:`, `consequence:` (2–3 clauses: who cares, what changes), and `archetype:` (enum). **Numbers, `answer`, `verify:` unchanged** — only the task shape the reader sees changes.
- **Three high-immersion archetypes, per-chapter quotas enforced by `check_coverage.py`:**
  - **`audit` / catch-the-error (≥3):** "Team Rocket (or a predecessor) recorded the value as X and declared it safe — find the true value and name the error." **Recycles each chapter's Team Rocket's Trap into drills.**
  - **`rival_trap` (≥2):** "Gary claims the answer is X — is he right? If not, what's his error and the true value?"
  - **`decision` (≥1):** two options where the **story shape and the math are the same object** (with- vs. without-replacement; pool risk vs. go alone).
- **Recurring-cast micro-arc per chapter:** a 3–4-problem thread with one character pursuing one goal, referenced back. Fixed drill cast jobs (§5): **Team Rocket = audit foil**, **Gary = rival trap**, **gym leaders / Oak / Joy / Jenny / Warden = commissioners who set the stake.**

### Fix B — make progression *real* (a ladder, not just per-chapter badges)
- **Trainer Rank ladder** (cumulative): Rookie (0–2 badges) → Junior (3–4) → Ace (5–6) → Veteran (7) → **Champion-ready** (8 + mocks). Source: `book/ranks.yaml`.
- **Badge gallery + map progress strip** (`{{progress:chNN}}`, §14.5): earned badges lit, unearned greyed, current town marked, rank label, cumulative **Exam-Readiness %** (outcomes mastered + checkpoint scores). At every chapter open and the finale.
- **Checkpoint gating made real** (`ch07`, `ch18`, `ch13` fold): an explicit pass bar and a *spaced-retrieval* fail path ("not yet — review chX, retry in 2 days").
- **Spine continuity:** each cold-open pays off the prior badge and plants the next; "Where You Are" names the **rank + badges held**; `ch19` tallies total problems, badges, readiness as the payoff.

### Fix C — the chapter **questline**: problems as a connected, escalating mission
Each chapter's problem set is **one story mission you progress through**, so the reader feels like they're *doing tasks in the journey*, not grinding exercises.
- **Mission arc (beginning → middle → boss → post-game):** a **commissioner** opens with a goal + stake; the **Route-Trainer** tier are the early legs (scouting/cataloguing/skirmishes); the **Gym Battle** tier is the literal **boss fight** (the chapter's hardest problem at exam difficulty); the **Elite Challenge** tier is the optional post-game. Clearing the questline *earns the badge* and ticks the **Trainer Rank**.
- **Threaded continuity:** problems share a running scenario and, where natural, **chain** ("the encounter rate λ you found scouting Route 8 now sets the ambush odds…"). **Verification safety:** every chained problem **also restates the needed prior value as a given**, so its `verify:` stays self-contained — a wrong upstream answer never cascade-blocks the harness or the reader.
- **Difficulty = story escalation, with faded guidance:** route → gym → elite map to scout → gym battle → league; early legs lightly **scaffolded**, the boss and post-game full-independence — the set itself *feels like growing competence*.
- **Progress beats inside the set:** short interstitial lines mark advancement ("Boulder Badge in reach — one battle left"); the questline pays off the cold-open.
- **Multi-chapter questlines at the seams:** checkpoints (`ch07`, `ch18`) are **League-qualifier** missions interleaving the act's archetypes; the `ch19` mocks are the **tournament bracket** (each mock a round, each question an opponent).

### Coverage guarantee — immersion **wraps** the checklist, never replaces it
The questline is a **narrative ordering over a required coverage manifest**, not a substitute. Each dossier (`docs/design/chNN.md`) carries a **coverage manifest** — every SOA outcome, in-scope distribution, calculator skill, and archetype the chapter must hit — and the questline threads through all of them in story order. `check_coverage.py` enforces the manifest independently; a charming questline that drops a required skill **fails the build**. The skeleton (coverage) stays rigid; the skin (mission) is what you experience.

### Infra deltas for §28
- Problem schema gains `actor/stakes/consequence/archetype`, plus optional `quest_step:` (mission ordering) and `depends_on:` (the threaded prior problem — value also restated as a given). `check_coverage.py` enforces the archetype quotas (audit ≥3, rival_trap ≥2, decision ≥1) **on top of** outcome/distribution/calc-skill minimums, and validates the dossier coverage manifest.
- `progress_strip()` / `vs_banner()` read `book/ranks.yaml` to render rank + badge gallery; questline interstitial beats render from the bank's `quest_step` ordering.
- **DoD additions (§25):** each chapter's drills form a coherent questline (commission → legs → Gym-Battle boss → optional post-game) that pays off the cold-open; archetype quotas + dossier coverage manifest both met; ≥1 drill recycles the chapter's canonical error; the cast micro-arc is present; chained problems are self-contained for `verify:`; the progress strip shows correct rank/badges/readiness.

---

## 29. Watch-Alongside — the TV-show tie-in (a core immersion pillar)

**Vision:** the book is built so a learner can **watch the Pokémon *Indigo League* anime alongside reading** — each chapter's cold-open and story beats track specific episode(s), so watching and reading reinforce each other and interest stays high. The real-world actuarial bridge (§ "From Kanto to the Real World") is kept; the show is the hook, the math is the cargo, the real world is the payoff.

**Mechanism — a per-chapter `::: now-playing` box** (placed right after the Cold Open / "Where You Are"): a **real still from the tied episode** (`assets/stills/`, extracted locally per §30), then *"📺 NOW PLAYING — Indigo League EP0xx '<title>'"*, 1–2 lines on what happens in that episode and how it sets up the chapter's math, and a "watch this before/after the chapter" cue. **Fidelity rule:** reference only events that actually occur in the cited episode; where the book extends canon (e.g., the Pokémon-Mansion paired logs in ch14, the Safari-Zone deductible job in ch06), **label it an in-world extension**, never claim it's on screen.

**The locked episode map** (verified against Serebii/Bulbapedia):

| Ch | Locale | Watch-Alongside (Indigo League) |
|---|---|---|
| 00 | Pallet Town | EP001 *Pokémon! I Choose You!* |
| 01 | Route 1 (Spearow swarm) | EP001 + EP002 *Pokémon Emergency!* |
| 02 | Cerulean / Misty | EP007 *The Water Flowers of Cerulean City* |
| 03 | S.S. Anne → Vermilion / Surge | EP014 *Electric Shock Showdown* + EP015 *Battle Aboard the St. Anne* |
| 04 | Viridian Forest / Pewter / Brock | EP003 *Ash Catches a Pokémon* · EP004 *Challenge of the Samurai* · EP005 *Showdown in Pewter City* |
| 05 | Lavender Tower / Celadon / Erika | EP023 *The Tower of Terror* · EP024 *Haunter Versus Kadabra* · EP026 *Pokémon Scent-sation!* |
| 06 | Fuchsia / Safari / Koga | EP032 *The Ninja Poké-Showdown* (+ Safari Zone EP035 *The Legend of Dratini*) |
| 07 | Checkpoint A | recap — rewatch EP001–026 highlights |
| 08 | Bill's lighthouse (calculus) | EP013 *Mystery at the Lighthouse* |
| 09 | Saffron / Sabrina | EP022 *Abra and the Psychic Showdown* + EP024 *Haunter Versus Kadabra* |
| 10 | Saffron / Silph Co. | EP022–024 (Sabrina arc) |
| 11 | the smooth wilds | cross-Kanto travel episodes (no single gym) |
| 12 | the Grand Gathering (CLT) | EP077 *Round One – Begin!* (the League crowd = the bell of thousands) |
| 13 | Cinnabar Lab | EP059 *Volcanic Panic* (Cinnabar arc) |
| 14 | Cinnabar Mansion / Blaine | EP059 *Volcanic Panic* (Blaine/Volcano; Mansion logs = in-world extension) |
| 15 | Victory Road | the road to the Plateau (~EP075–076) |
| 16 | Viridian Gym / Giovanni | EP063 *The Battle of the Badge* |
| 17 | Indigo Plateau / Elite Four | EP077–080 (League rounds) |
| 18 | Checkpoint B | EP077 |
| 19 | Champion = the exam | EP081 *Friend and Foe Alike* + EP082 *Friends to the End* (Ash vs Ritchie) |

**Appendix add:** an **Episode Companion (Viewing Guide)** — the full chapter↔episode order so the reader can binge the season alongside the book, with each entry noting the concept that episode motivates.

---

## 30. Visual immersion — real online sprites + generated figures (a core immersion pillar)

**The one hard guardrail:** **never generate or draw sprite / character / badge / Pokémon art.** That art must always be a **real asset downloaded from online** (PokeAPI · pret/pokered · Pokémon Showdown, via `assets/download_*.py`). The author *generates* only **math figures** (matplotlib diagrams) — and those figures may **composite real sprites** into themselves. (Reason: fabricated sprite art can't match the real thing.)

**Three visual channels, all using REAL assets, used richly:**
1. **Generated concept figures** — matplotlib math diagrams (`figures/src/gen_chNN.py`), `chapter_accent(ch)` tint, color-blind-safe (labels + hatching), 300 DPI; ≥1 per spatial/multi-step concept (§16). They **composite real Pokémon sprites** via `sprite_util.place_sprite()` (margins/corners only — **IRON RULE:** never over a curve, equation, axis, or label) so the random variable is *visible* inside its own figure.
2. **Real online assets embedded at their beats** — Pokémon sprites, gym-leader/cast portraits, the earned badge, item glyphs — as inline `<figure><img src="../../assets/{sprites,characters,vs,badges,items}/…" alt="…">` (pixel art uses `image-rendering:pixelated`). Oak at Oak's Briefing; the leader at the Gym Battle; Team Rocket at the Trap; Gary at a rival-trap drill; the chapter's mascots beside the relevant Pokédex Entry; the badge at "Badge Earned."

3. **Real TV-show episode stills (watch-alongside frames)** — frames extracted **locally** from the user's own Season-1 video files via `assets/extract_stills.py` (ffmpeg → `assets/stills/chNN_*.png`). A still is the *actual on-screen moment* the chapter ties to (§29). **Use stills for scene/narrative beats** — the `now-playing` box, the cold-open scene, the chapter banner, the Gym-Battle moment — where a real frame beats a static sprite; **keep clean sprites for figure compositing** (a busy frame harms a diagram). Per beat, pick whichever is more immersive; a still may *replace* a VS portrait at the banner/gym beat when it reads better. Stills are **real frames, never generated**; curate by extracting candidate frames around the target timestamp and selecting the best (downscale/compress for build size; alt text; iron rule).

**Pull as much real art from online as the chapters can use** — more Pokémon, VS portraits, backgrounds, items — whenever a beat benefits; the build embeds them (base64). The chapter banner + §28 progress strip are generated figures compositing the **real** leader portrait/episode still + badge + map.

**Sourcing & rights:** stills are extracted **only** from local video files the user supplies (never downloaded from streaming/unauthorized sources); like all sprite/anime assets they are real, used in a **private, non-distributed** educational build, never generated.

**Conformance (see §31):** every figure and embedded asset exists because a concept or beat needs it, placed where TIA puts that concept — rich, never padding the TIA flow.

**Grading:** rubric dimension **12** (§25), **must score ≥9 for an A** — judged on real-asset richness (figures compositing real sprites + real sprite/cast/badge embeds at beats) and iron-rule compliance. A Tier-A chapter whose concepts are under-illustrated fails; **any generated/fake sprite or character art fails outright** — all such art must be real online assets.

---

## 31. TIA conformance — the master integration rule (overrides on conflict)

The **TIA *Exam P Lesson Handouts* define the teaching order and the depth/length of every concept.** Everything else — narrative, episodes, figures, drills, immersion — is **integrated into** that spine, never the reverse:

- **Order:** concepts appear in TIA's sequence (A.1.1 → C.4.1, mapped to chapters in §4/§16). Narrative locale/episode is chosen to *fit* the concept that TIA places there — not the other way around.
- **Length:** each concept gets the depth TIA gives it — **complete (no compression, §7) but not padded.** Narrative adds a sentence to motivate, never a page that delays the math; a figure exists because the concept needs it. If a flourish would lengthen a concept beyond what TIA's treatment needs, it is cut.
- **Masterful integration:** the test is that a reader following the TIA course could use this book as the *same course, dramatized* — same concepts, same order, same rigor, now narrated and illustrated. The TIA→chapter→concept→figure→narrative blueprint lives in `docs/DESIGN_BLUEPRINT.md` and each `docs/design/chNN.md` dossier.
- **Grading:** rubric dimension **13** (§25); an A requires ≥9. A chapter that reorders, compresses, or pads relative to TIA fails this dimension regardless of how good the story is.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; educational, non-commercial work; exam details verified against the SOA Exam P syllabus (September 2026). All anime/sprite assets are used for a private, non-distributed educational build.*
