# Audit Charter — what "done to the desired level" means

The book's promise is a **perfect-score** Exam P companion that gets **printed and bound**. That sets the bar: a single wrong answer key, a mis-stated formula, or a problem that can't be solved as written is a defect a reader will trip on under exam pressure — and once it's bound, it's permanent. This document is the checklist the audit runs against. Each item lists **what** to check, **why** it matters, **how** to check it (the method), the **severity** if it fails, and whether it's **automatable** or needs **independent agent re-derivation**.

Guiding principle: the existing `make verify` gate is **self-consistency, not correctness** — the agent that wrote each problem also wrote its `verify:` expression, so a misunderstanding makes the answer and its check wrong together. Real correctness requires a *different* agent to re-derive the answer from the problem statement alone, never seeing the book's solution. That is the heart of Tier 0.

Severity scale: **BLOCKER** (wrong/unusable — must fix before print) · **MAJOR** (misleads or materially hurts study) · **MINOR** (polish, won't cause a wrong answer).

---

## Tier 0 — Mathematical correctness (the non-negotiable core)

| # | Check | Why | Method | Severity |
|---|---|---|---|---|
| 0.1 | **Every worked example re-derived independently** matches the book's stated answer. | A wrong worked example teaches the wrong method. | Independent agent solves from the prompt only, blind to the solution; compare. Disagreements re-checked a 2nd independent way. | BLOCKER |
| 0.2 | **Every Gym Challenge problem's answer** is independently reproducible. | 236 answers; any wrong one costs a mark and erodes trust. | Same blind re-derivation per problem in `problems/bank.d/*.yaml` + chapter text. | BLOCKER |
| 0.3 | **Answer key matches the worked solution** and the **quick-answer table** matches both. | Drift between the three is common and silent. | Cross-read: problem ↔ solution steps ↔ final-answer table ↔ `answer:` field. | BLOCKER |
| 0.4 | **Every formula in a Pokédex Entry is correct** (pmf/pdf, cdf, mean, variance, MGF, support). | A wrong reference formula propagates into many problems. | Check each against an authoritative table; verify dimensional/edge cases. | BLOCKER |
| 0.5 | **Appendix A (formula sheet) & B (distribution tables) are correct** and match the in-chapter entries. | Readers memorize these; errors here are maximally damaging. | Line-by-line check vs. SOA-accepted values; cross-check against chapters. | BLOCKER |
| 0.6 | **`verify:` expressions are independent and meaningful**, not circular restatements of the answer. | A check that just re-asserts the answer proves nothing. | Inspect each expression; ensure it encodes the computation, not the literal answer. | MAJOR |
| 0.7 | **Shortcuts (Trainer's Path) are valid**, not coincidentally right (gamma integral, Darth Vader, memoryless, MGF kernel, continuity correction). | A shortcut that works only on the example misleads. | Re-derive via the long method (Professor's Path) and confirm equivalence. | MAJOR |
| 0.8 | **Numerical hygiene**: probabilities in [0,1], variances ≥ 0, E[payment] ≤ E[loss], support consistent, rounding sane. | Cheap invariants catch whole classes of error. | Automatable assertion pass over stated answers. | MAJOR |

## Tier E — Explanatory completeness & teaching quality (co-equal with Tier 0)

**This is a teaching book, not a formula reference.** The promise is that a reader starting from beginning-college statistics is *taught* every concept — complex topics strategically broken down, every piece of notation explained, every important formula earned rather than asserted. A correct-but-unexplained formula fails the book's core purpose. The current first draft is reference-accurate but **under-taught** (e.g., the Darth Vader rule $\E[(X-d)_+]=\int_d^\infty S(x)\,dx$ is stated with a one-line gloss and no derivation/intuition; the master identity and the per-payment division by $S(d)$ are asserted, not built). Every item here is graded against the from-scratch learner.

| # | Check | Why | Method | Severity |
|---|---|---|---|---|
| E.1 | **Every symbol/notation is defined in plain words on first use** — $\wedge$, $(\cdot)_+$, $\Phi$, $\Gamma(\cdot)$, $\int_0^\infty$, the conditioning bar $\mid$, MGF, the Jacobian, $\sim$, order-stat subscripts. Nothing appears unexplained. | A reader who can't decode the notation can't learn the method. | Per chapter, list every symbol at first appearance; confirm a plain-language definition precedes/accompanies it. | BLOCKER |
| E.2 | **Every non-trivial formula is *earned*** — derived, or given a concrete intuition for *why* it is true — not merely asserted with a one-line gloss. Especially: Darth Vader rule, the master identity, per-payment ÷ $S(d)$, the variance shortcut, MGF→moments, CLT standardization, order-stat $[F(x)]^n$, Bayes, the gamma integral. | "Trust me" formulas don't transfer to new problems; understanding the *why* is what scores 9–10. | For each boxed formula, confirm a derivation or a worked intuition exists nearby (or a precise cross-ref to where it is derived). | BLOCKER |
| E.3 | **Complex topics are decomposed into a teaching sequence**: simplest case first, then add one complication at a time, then the general form (deductible alone → +limit → +coinsurance → +inflation; single RV → joint → conditional → double expectation). | Dumping the fully-assembled formula skips the learning. | Check each hard topic builds up incrementally rather than presenting the final form cold. | MAJOR |
| E.4 | **Worked examples show every step with line-by-line annotation** ("now standardize," "apply the gamma identity here") — no skipped algebra, no "it follows that." | The worked example is the model the reader imitates; gaps become the reader's gaps. | Re-read each example; flag any algebraic jump or unannotated step. | MAJOR |
| E.5 | **Concrete before abstract**: a numeric instance precedes or accompanies each general/symbolic formula. | Beginners anchor on numbers, then generalize. | Confirm each general result has a concrete companion. | MAJOR |
| E.6 | **"In plain terms" actually teaches meaning and use**, not a restatement of the symbols in words. | A gloss that just reads the formula aloud teaches nothing. | Judge each plain-terms line: does it add intuition? | MAJOR |
| E.7 | **No unexplained leaps**: every "clearly," "obviously," "it follows that," "by the X rule" is justified inline or precisely cross-referenced. | Each leap is a place a learner silently falls off. | Scan for hand-wave phrases; require justification or cross-ref. | MAJOR |
| E.8 | **Reading level matches the audience** (beginning-college stats); jargon is introduced before it is used. | Over-terse prose excludes the target reader. | Read for accessibility; flag unexplained jargon. | MINOR |
| E.9 | **Each genuinely hard concept has a supporting structural aid** where it helps (labeled diagram, table of cases, before/after, step list). | Visual/structural scaffolding carries hard ideas. | Confirm hard topics aren't pure prose+formula. | MINOR |
| E.10 | **Cumulative scaffolding holds across the book**: any tool a chapter *relies on* was actually taught (with its derivation/intuition) in its home chapter, not merely cited. | ch8 leaning on the Darth Vader rule only works if ch5 truly taught it. | Trace each cross-chapter reliance back to a real teaching moment. | MAJOR |

## Tier 1 — Exam fitness (does it actually prepare a top scorer?)

| # | Check | Why | Method | Severity |
|---|---|---|---|---|
| 1.1 | **Problem well-posedness**: enough info, unambiguous, exactly one defensible answer. | Ambiguous problems train bad habits and waste time. | Agent attempts to find a second valid interpretation; flag if found. | BLOCKER |
| 1.2 | **SOA-realism of phrasing & difficulty** (≥60% at true SOA level per `DESIGN.md`). | The exam is a specific genre; off-genre prep underperforms. | Compare phrasing/difficulty to SOA sample style; rate each problem. | MAJOR |
| 1.3 | **6-minute solvability** and **calculator feasibility** (TI-30XS / BA II Plus). | A problem needing 15 min or a computer isn't exam-valid. | Estimate solve path length; flag heavy/uncomputable ones. | MAJOR |
| 1.4 | **Syllabus scope**: in-scope distributions only; lognormal/Pareto/Weibull/chi-square appear **only** as flagged enrichment. | Out-of-scope drilling wastes study time. | Scan content vs. `syllabus/outcomes.yaml`; flag scope violations. | MAJOR |
| 1.5 | **Coverage depth**: each outcome has theory + ≥1 worked example + ≥ threshold problems; each in-scope distribution ≥ threshold. | The promise is *complete* coverage. | `tools/check_coverage.py` + manual confirm theory/example exist. | MAJOR |
| 1.6 | **Topic weighting** honored (General ~23–30%, Univariate ~44–50%, Multivariate ~23–30%). | Misweighted prep leaves the biggest block thin. | Tally problems/pages by topic; compare to weights. | MAJOR |
| 1.7 | **Ch13 mock exams** are 30Q / 3hr, weight-matched (~8/14/8), standalone, with scored keys. | The mocks are the readiness gate. | Verify counts, weight split, self-containment, answer keys. | MAJOR |
| 1.8 | **Notation matches SOA conventions** and is consistent book-wide (θ scale, geometric trials-vs-failures convention stated once and held, Φ for normal cdf, etc.). | Convention drift causes wrong answers on otherwise-known material. | Build a symbol/convention table; check each chapter against it. | MAJOR |

## Tier 2 — Pedagogy & narrative integrity

| # | Check | Why | Method | Severity |
|---|---|---|---|---|
| 2.1 | **Recognition cues are correct triggers** ("when you see ___, reach for this"). | Pattern-matching speed is the scoring lever; a wrong cue mis-fires. | Verify each cue actually discriminates the right tool. | MAJOR |
| 2.2 | **Team Rocket's Trap is the *actual* canonical mistake** for that topic, and "The fix:" is correct. | A fabricated trap fails to inoculate against the real error. | Confirm the error is the well-known one (e.g., per-loss vs per-payment, prosecutor's fallacy). | MAJOR |
| 2.3 | **Trainer's Tips are valid exam craft** (keystrokes correct, pacing real). | Bad calculator advice costs time/marks. | Check each keystroke sequence on the named calculator. | MAJOR |
| 2.4 | **Every problem has genuine narrative framing** (a task Ash must accomplish), no bare drills. | The book's pedagogical premise. | Scan problem statements for in-world context. | MINOR |
| 2.5 | **Voice/tense consistency**: 2nd-person present in narrative, 3rd-person in theory/real-world boxes; never break character outside marked boxes. | Tonal breaks read as unfinished. | Read for POV/tense slips. | MINOR |
| 2.6 | **Cast used per role** (Oak=formalizer, Pikachu=intuition, Misty/Brock=companions, Gary=benchmark one step ahead, Team Rocket=foil). | Misused cast dilutes the device. | Check each appearance against role. | MINOR |
| 2.7 | **Cross-chapter continuity**: badges accumulate correctly; seeded concepts pay off (hypergeometric ch3→ch6); no concept used before introduced. | Continuity errors confuse and break the dependency order. | Trace badge tally + forward/back references. | MAJOR |
| 2.8 | **Anime-beat mapping is recognizable but not required knowledge** (St. Anne, Spearow swarm, Game Corner, etc.). | The hook should help, never gate, understanding. | Confirm each beat is self-explained. | MINOR |
| 2.9 | **"From Kanto to the Real World" boxes name a concrete actuarial application** (claim frequency, reserving, credibility…), not vague. | These justify the career payoff and CAS bridge. | Check each box names a specific practice. | MINOR |

## Tier 3 — Structure, formatting & production (print-and-bind readiness)

| # | Check | Why | Method | Severity |
|---|---|---|---|---|
| 3.1 | **All 10 sections present, in order; problems-then-solutions** (never interleaved); one solution per problem ID. | The textbook contract; bound errors are permanent. | `tools/check_format.py` (already enforces) + spot read. | BLOCKER |
| 3.2 | **LaTeX renders**: balanced `$`/`$$`, matched `\left/\right`, all macros defined, no raw TeX in the PDF. | Broken math is unreadable. | `check_format.py` + visual scan of rendered PDF pages. | BLOCKER |
| 3.3 | **Sprites depict the correct Pokémon/character** the text names (Onix=#95, Koga portrait=Koga, badge matches gym, type icon matches leader). | A wrong sprite is an obvious, embarrassing, permanent error. | Cross-check each `<figure>` dex id/name/file vs. the surrounding text. | MAJOR |
| 3.4 | **Math figures match what the text describes** (the shaded region, the step graph's d and u, the Venn labels). | A figure that contradicts the prose misleads. | Read each figure against its caption and the passage. | MAJOR |
| 3.5 | **Appendices A–I are actually filled** (not stubs) and internally correct. | Half the reference layer lives here. | Check each appendix has real content. | MAJOR |
| 3.6 | **Badge checklist maps 1:1 to the chapter's learning outcomes.** | The mastery contract per chapter. | Compare checklist items to Oak's Briefing outcomes. | MINOR |
| 3.7 | **Cross-references resolve** (Appendix F manual/sample numbers, "see Chapter X", figure/table refs). | Dangling refs read as unfinished. | Resolve every reference. | MINOR |
| 3.8 | **Print geometry**: chapters start recto, nothing critical in the gutter, boxes/figures/tables not split awkwardly, no orphaned headings, TOC accurate, running heads correct, no stray blank pages. | Binding makes layout defects permanent. | Render PDF; inspect page breaks, gutter, TOC, headers. | MAJOR |
| 3.9 | **Image resolution for print** ≥300 DPI effective; sprites upscaled (nearest-neighbor), not blurry; fonts embedded. | Low-res art looks bad in print. | Check effective DPI at placed size; confirm font embedding. | MAJOR |
| 3.10 | **Reproducibility**: every math figure regenerable from committed code (`generate_figures.py`), seed=151, deterministic build. | Gitignored ad-hoc figures can be lost. | Confirm each referenced figure has generating code. | MINOR |
| 3.11 | **Legal**: trademark disclaimer + colophon present; provenance tags honest; no verbatim SOA/manual text. | Required for a fan/educational work. | Check disclaimer; spot-check provenance vs. phrasing. | MAJOR |

---

## How the audit workflow uses this

- **Tier 0 + 1.1** are run as **blind independent re-derivation**: a fresh agent (that did not write the chapter) solves each worked example and problem from the statement alone, then a second agent adversarially re-checks every disagreement before it's logged. This is the only way to catch correctness errors the self-written `verify:` gate cannot.
- **Tiers 1–2** are run as **expert read-throughs** per chapter against the specific checks above, producing structured findings (`{severity, kind, where, detail, fix}`).
- **Tier 3** is partly **automated** (`check_format.py`, `check_coverage.py`) and partly a **rendered-PDF visual pass**.
- Output: a per-chapter findings ledger + a consolidated defect list sorted by severity, with BLOCKERs gating "print-ready."

**Definition of print-ready:** zero open BLOCKERs, zero open MAJORs in Tier 0, and a written disposition (fixed / accepted / deferred) for every remaining MAJOR.
