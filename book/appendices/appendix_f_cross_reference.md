<!--
  file: appendix_f_cross_reference
  kind: appendix
  letter: F
  title: Cross-Reference — lining this book up with TIA, the SOA syllabus, and commercial manuals
  purpose: let a reader studying in parallel with commercial resources map each V3 chapter to its TIA leaf section(s), the SOA outcome(s) it discharges, the syllabus topic & weight, and the corresponding chapter-level topic in widely used Exam P resources; original tabulation only — names and chapter numbers, never reproduced content
  sources: docs/DESIGN_BLUEPRINT.md Part 0 §1 + Part 1 (binding TIA map), MASTER_PLAN_V3 Part 1 TIA/SOA tags, syllabus/outcomes.yaml (outcome→chapter map)
  plan: MASTER_PLAN_V3 §23
-->

# Appendix F — Cross-Reference {.type-normal}

> **What this is.** A set of lookup tables for the reader studying this book *alongside* a commercial resource — a TIA seminar, a study manual, or a probability textbook. It lines up each chapter of *Probability & Risk: A Kanto Journey* (ch00–ch19) with (1) the **TIA lesson handout** sections it follows, (2) the **SOA Exam P syllabus topic and weight** it serves, and (3) the **chapter-level topic** you would turn to in the standard manuals and texts. Everything here is an **original tabulation**: it cites only section *names* and *numbers* and general topic *labels* — it reproduces no part of any manual, seminar, or textbook. Use it as a switchboard, not as a substitute for those resources.
>
> **How to read it.** This book's spine *is* TIA's lesson order — the chapter↔TIA map is 1:1 (ch01 = lesson group A.1, … ch17 = C.3), so Table F.1 is the master key; the other tables hang off it. "TIA leaf" means the finest-grained handout subsection (e.g. A.2.4 *Bayes' theorem*), in TIA's own numbering. "SOA outcome" uses the syllabus's letter codes (1a … 3i) as tracked in this book's `outcomes.yaml`.

---

## F.1 This book → TIA lesson handouts → SOA outcomes

Each V3 chapter maps to a contiguous block of TIA leaf sections (the handouts' own A/B/C numbering) and discharges the SOA learning outcome(s) shown. Outcome codes are the primary assignments from this book's `syllabus/outcomes.yaml`; checkpoint and finale chapters re-test the outcomes of the act they close rather than introducing new ones.

| Ch | Chapter title | TIA leaf section(s) | SOA outcome(s) discharged |
|----|---------------|---------------------|---------------------------|
| 00 | Orientation | *front matter* (precedes A.1.1) | — (orientation; calculator + symbols primer) |
| 01 | Fundamentals of Probability | A.1.1 – A.1.5 | 1a, 1d, 1e |
| 02 | Conditional Probability & Bayes | A.2.1 – A.2.4 | 1c, 1e, 1f, 1g |
| 03 | Discrete RVs & Moments | A.3.1 – A.3.8 | 2a, 2c, 2d |
| 04 | Combinatorics | A.4.1 – A.4.5 | 1b, 2d |
| 05 | Key Discrete Distributions | A.5.0a – A.5.5 | 2d |
| 06 | Deductibles & Limits (Discrete) | A.6.1 – A.6.3 | 2e, 2f |
| 07 | Checkpoint A | A.7.1 | *Act-I retrieval:* 1*, 2* |
| 08 | The Calculus Toolkit | B.0.1 – B.0.3 | *prerequisite* (no SOA outcome) |
| 09 | Densities & CDFs | B.1.1 – B.1.3 | 2a |
| 10 | Continuous Moments | B.2.1 – B.2.3 | 2c, 2d |
| 11 | Key Continuous Distributions | B.3.1 – B.3.5 | 2d |
| 12 | Normal & the CLT | B.4.1 – B.4.5 | 2d, 3i |
| 13 | Continuous Deductibles & Review | B.5.1 – B.5.3 | 2e, 2f |
| 14 | Joint Distributions | C.1.1 – C.1.2 | 3a, 3b |
| 15 | Joint Moments & Covariance | C.2.1 – C.2.2 | 3e, 3g, 3h |
| 16 | Conditional & Double Expectation | C.2.3 | 3c, 3d |
| 17 | Order Statistics | C.3.1 – C.3.2 | 3f |
| 18 | Checkpoint B | C.4.1 | *Act-III retrieval:* 3* |
| 19 | Champion's Challenge (3 mock exams) | *exam finale* (not a TIA leaf) | all (1a–1g, 2a–2f, 3a–3i) |

> *Note on the multivariate leaves.* TIA's C.2 group runs C.2.1–C.2.2 (joint moments, covariance/correlation, variance of linear combinations) into C.2.3 (conditional & double expectation). This book splits that block across **ch15** (C.2.1–C.2.2) and **ch16** (C.2.3) so the law of total expectation/variance gets its own chapter; the SOA codes follow the split (3e/3g/3h vs. 3c/3d).

---

## F.2 This book → SOA Exam P syllabus topics & weights

The Exam P syllabus has three topics with the score weights below. The chapters that *primarily* serve each topic are listed; several chapters bridge two topics (combinatorics underpins both counting and discrete distributions; the CLT lives with the Normal but serves multivariate sums), shown in the bridge column.

| SOA topic | Syllabus weight | Core chapters | Bridge / shared chapters |
|-----------|-----------------|---------------|--------------------------|
| **1 — General Probability** | 23–30% | 01 (sets, axioms, inclusion–exclusion), 02 (conditional, total probability, Bayes), 04 (combinatorics) | 07 (Checkpoint A retrieval) |
| **2 — Univariate Random Variables** | 44–50% | 03 (discrete RVs & moments), 05 (discrete distributions), 06 (discrete deductibles), 09 (densities & CDFs), 10 (continuous moments), 11 (continuous distributions), 12 (Normal), 13 (continuous deductibles) | 04 (named-distribution counting), 07 (Checkpoint A) |
| **3 — Multivariate Random Variables** | 23–30% | 14 (joint distributions), 15 (joint moments & covariance), 16 (conditional & double expectation), 17 (order statistics) | 12 (CLT — outcome 3i), 18 (Checkpoint B) |

Spanning chapters (not topic-specific): **ch00** (orientation), **ch08** (calculus prerequisite — discharges no SOA outcome but underwrites all of Topic 2 and Topic 3), and **ch19** (three full mock exams, weight-matched to the topic split below).

> **Mock-exam weighting (ch19).** Each 30-question mock follows the syllabus weights: **≈ 8 General Probability · ≈ 14 Univariate · ≈ 8 Multivariate**.

---

## F.3 This book → standard commercial study manuals & texts

For each chapter, the table names the *corresponding topic* you would look up in widely used Exam P resources — the **ASM** manual (Weishaus), **ACTEX**, **Coaching Actuaries / Adapt**, **Finan's** free study guide, and two probability texts: **Ross**, *A First Course in Probability*, and **Wackerly et al.**, *Mathematical Statistics with Applications*. These are **general topic labels** ("conditional probability & Bayes," "joint distributions") for navigation only — consult each resource's own table of contents for its exact section numbers, which differ by edition.

| Ch | This book's focus | Topic to look up in ASM / ACTEX / Adapt / Finan | Ross (topic) | Wackerly (topic) |
|----|-------------------|--------------------------------------------------|--------------|------------------|
| 00 | Orientation, calculator, notation | front matter / "how to use" / calculator setup | preface, axioms preview | introduction & probability overview |
| 01 | Sets, axioms, Venn, inclusion–exclusion | set theory & axioms of probability; inclusion–exclusion | combinatorial analysis & axioms of probability | probability & set notation; axioms |
| 02 | Conditional probability, total probability, Bayes | conditional probability & Bayes' theorem | conditional probability & independence | conditional probability, independence & Bayes' rule |
| 03 | Discrete RVs, expectation, variance, MGF | discrete random variables; moments; MGFs | discrete random variables & expectation | discrete random variables & their distributions |
| 04 | Permutations, combinations, multinomial, hypergeometric | combinatorics & counting | combinatorial analysis | combinatorial methods & counting |
| 05 | Geometric, neg-binomial, Poisson | named discrete distributions | special discrete distributions | discrete distributions (geometric, neg-binomial, Poisson) |
| 06 | Deductibles, limits, coinsurance (discrete) | insurance payment models / coverage modifications | *(not a Ross topic — actuarial coverage)* | *(not a Wackerly topic — actuarial coverage)* |
| 07 | Checkpoint A (Act-I review) | General-Probability review set | *(review)* | *(review)* |
| 08 | Calculus toolkit (derivatives, integrals, gamma integral) | calculus review / prerequisites | *(assumed prerequisite)* | *(assumed prerequisite)* |
| 09 | Densities, CDFs, mixed distributions | continuous random variables; pdf/cdf | continuous random variables | continuous random variables & probability densities |
| 10 | Continuous moments; survival-function method | expectation of continuous RVs; moments | expectation of continuous RVs | expected values of continuous RVs |
| 11 | Uniform, exponential, gamma, beta | named continuous distributions | special continuous distributions | continuous distributions (uniform, exponential, gamma, beta) |
| 12 | Normal, standardization, CLT, continuity correction | normal distribution & the Central Limit Theorem | the normal distribution & the CLT | the normal distribution & the Central Limit Theorem |
| 13 | Deductibles & limits (continuous); review | coverage modifications (continuous) | *(not a Ross topic — actuarial coverage)* | *(not a Wackerly topic — actuarial coverage)* |
| 14 | Joint pmf/pdf/cdf, marginals, conditionals, independence | joint distributions; marginal & conditional | jointly distributed random variables | multivariate / bivariate distributions; marginal & conditional |
| 15 | E[XY], covariance, correlation, variance of sums | covariance & correlation; linear combinations | covariance, variance of sums & correlation | covariance & expectation of functions; correlation |
| 16 | Conditional & double expectation; total variance; compound | conditional expectation; double expectation; variance | conditional expectation & its uses | conditional expectations |
| 17 | Order statistics; min/max; reliability | order statistics | order statistics | order statistics |
| 18 | Checkpoint B (Act-III review) | Multivariate review set | *(review)* | *(review)* |
| 19 | Three full mock exams; pacing; shortcuts | full-length practice exams | *(end-of-text problem sets)* | *(supplementary exercises)* |

> *Edition caveat.* Section numbers in every one of these resources shift between editions and printings; this table deliberately points only at *topics*. When two resources file a topic differently — e.g. some manuals fold order statistics into the multivariate chapter, others give it its own — follow the topic label, not a number.

---

## F.4 Official SOA sample questions

The SOA publishes a free, regularly updated set of **Exam P sample questions and solutions** on its website (search "SOA Exam P sample questions"). They are the single best gauge of exam-level difficulty and phrasing, and every serious candidate should work them. This book is built to map cleanly onto that set: solve the samples *by topic* and route each one back to the chapter that teaches it.

| If the sample question is about… | Study from chapter(s) |
|-----------------------------------|------------------------|
| Sets, Venn diagrams, inclusion–exclusion, axioms | 01 |
| Conditional probability, total probability, Bayes' theorem | 02 |
| Counting, permutations/combinations, hypergeometric | 04 |
| Discrete random variables, expectation, variance, MGFs | 03, 05 |
| Named discrete distributions (binomial, geometric, neg-binomial, Poisson) | 04, 05 |
| Deductibles, policy limits, coinsurance (discrete loss) | 06 |
| Continuous densities, CDFs, mixed distributions | 09 |
| Continuous expectation & moments; survival-function method | 10 |
| Named continuous distributions (uniform, exponential, gamma, beta) | 11 |
| Normal probabilities, standardization, the CLT, continuity correction | 12 |
| Deductibles & limits on a continuous loss | 13 |
| Joint distributions, marginals, conditionals, independence | 14 |
| Covariance, correlation, variance of linear combinations | 15 |
| Conditional & double expectation; total variance; compound distributions | 16 |
| Order statistics; min/max; reliability | 17 |
| Mixed full-length practice under timing | 19 (three mock exams) |

> **Suggested workflow.** Finish an act, take the matching checkpoint (ch07 / ch18), then pull the SOA samples on that act's topics and time yourself. Anything you miss routes straight back through the table above. Save the official set's hardest mixed run for *after* ch19, as a final dress rehearsal against the real thing.

*The SOA sample questions are the property of the Society of Actuaries; this appendix points to them and does not reproduce them. Commercial manuals, seminars, and textbooks named here are the property of their respective publishers; only their names and general topic structure are referenced.*
