# V3 Design Blueprint — TIA-ordered concept → figure → narrative integration
### The master spec everything conforms to. Pairs with MASTER_PLAN_V3.md (§1–§31).

> **Purpose.** One place that locks, for every chapter: the **TIA lesson sequence** (order + depth), the **figures** (and the real sprites each composites), the **narrative** (locale, watch-alongside episode, cast, questline), the **real-world bridge**, and the **length**. Authors build each chapter from its `docs/design/chNN.md` dossier, which is the per-chapter expansion of the row here. Nothing reorders, compresses, or pads the TIA flow (§31).

---

## Part 0 — The integration rules (how the four layers combine)

1. **TIA is the spine (§31).** Concepts appear in TIA's order at TIA's depth. The chapter↔TIA map is 1:1: ch01=A.1, ch02=A.2, ch03=A.3, ch04=A.4, ch05=A.5, ch06=A.6, ch07=A.7, ch08=B.0, ch09=B.1, ch10=B.2, ch11=B.3, ch12=B.4, ch13=B.5, ch14=C.1, ch15=C.2.1–2, ch16=C.2.3, ch17=C.3, ch18=C.4, ch19=exam finale; ch00=orientation.
2. **No compression, no padding (§7/§31).** A concept gets the length its TIA treatment needs — fully derived — and not a page more. Narrative motivates in a sentence; a figure appears because the concept needs it.
3. **Narrative wraps the concept (§3/§15).** The locale + the **watch-alongside episode (§29)** are chosen to fit the concept TIA places there. Cold open raises the question the concept answers; the questline (§28) is the drills; the cast hold their fixed jobs (§5).
4. **Visuals = real assets only (§30).** Generated **math figures** composite **real** Pokémon sprites; real sprite/cast/badge images embed at their beats. **Never generate sprite art.** Pull whatever real art a chapter needs from online.
5. **Real-world bridge (§ "From Kanto to the Real World").** Each chapter ends its teaching with the named actuarial use + a Series-bridge line.
6. **Ship gate (§25).** Each chapter loops author → harness → lint → blind re-derivation → tutor **grade-until-A** (now incl. dim 11 episode, dim 12 figures/real-sprites ≥9, dim 13 TIA-conformance ≥9).

---

## Part 1 — Per-chapter blueprint

Legend per row: **TIA leaves** · **Tier** · **SOA** · **📺 episode** · **locale/leader/badge/type** · **concept sequence (TIA order)** · **figures → real sprites composited** · **questline + cast** · **real-world bridge**.

### ACT I — DISCRETE ("The Countable Road")

**ch00 Orientation** — front matter · 📺 EP001 *Pokémon! I Choose You!* · Pallet Town / Oak / — / normal.
Concepts: how to use the book; the two-reader contract; exam facts; the Trainer's-Calculator primer (TI-30XS setup, STO▸, F◂▸D); Reading-the-Symbols. Figures: `ch00_journey_map` (Kanto map + route to Plateau, composites Pikachu #25), `ch00_calc_keypad` (TI-30XS schematic — math diagram, no sprite). Cast: Oak issues Pokédex + calculator. Length: short.

**ch01 Fundamentals** — A.1.1–A.1.5 · Tier C(sets)/B(incl–excl) · 1a,1d,1e · 📺 EP001+EP002 *Pokémon Emergency!* · Route 1 (Spearow swarm) / — / Trainer's License / flying.
Sequence: A.1.1 sample space & events & axioms → A.1.2 complements (& the "at least one" trick) → A.1.3 Venn diagrams → A.1.4 De Morgan → A.1.5 inclusion–exclusion (2- & 3-event).
Figures: `ch01_sample_space_box` (outcome chips; **Spearow #21, Pidgey #16, Rattata #19** in margin), `ch01_venn_two` (+ Pikachu #25 corner), `ch01_venn_three`, `ch01_incl_excl`, `ch01_complement_atleastone` (flock; Spearow #21). Embeds: Oak portrait @ Briefing; Team Rocket @ Trap; Gary @ rival-trap; Misty intro.
Questline: catalogue Route 1 for Oak → survive the Spearow swarm (boss) → post-game audit. Real-world: insurers avoid double-counting overlapping coverage via inclusion–exclusion.

**ch02 Conditional & Bayes** — A.2.1–A.2.4 · **Tier A** · 1c,1d,1e,1f,1g · 📺 EP007 *The Water Flowers of Cerulean City* · Cerulean / **Misty** / Cascade / water. *(GOLD-STANDARD EXEMPLAR — already A.)*
Sequence: A.2.1 conditional P(A|B) → multiplication rule → addition rule → A.2.2 independence (vs disjoint) → A.2.3 sequences/total probability → A.2.4 Bayes.
Figures: `ch02_bayes_grid`, `ch02_tree_sequential`, `ch02_total_prob`, `ch02_false_positive` (composite **Staryu #120 / Psyduck #54** suspects). Embeds: Misty @ Gym Battle; Oak; Team Rocket; Gary. Real-world: medical-test false positives, fraud detection.

**ch03 Discrete RVs & Moments** — A.3.1–A.3.8 · **Tier A** · 2a,2c,2d · 📺 EP014 *Electric Shock Showdown* + EP015 *Battle Aboard the St. Anne* · S.S. Anne→Vermilion / **Lt. Surge** / Thunder / electric.
Sequence: discrete RV & pmf/cdf/survival → A.3.1 mode → A.3.2 median/percentiles → A.3.3 expected value → A.3.4 tools for means → A.3.5 **survival-function (Darth-Vader) method** → A.3.6 variance definition → A.3.7 variance tools & Var(aX+b) → MGF → A.3.8 discrete uniform.
Figures: `ch03_pmf_cdf_survival` (sinking-ship survival; **Pikachu #25**), `ch03_darthvader_area`, `ch03_mean_median_mode`, `ch03_variance_spread`, `ch03_1var_stats_keypad` (TI-30XS 1-Var-Stats flow — math diagram). Discrete-uniform mascot **Ditto #132**. Embeds: Surge @ Gym Battle; Raichu #26 vs Pikachu #25. **Flagship calc skill: 1-Var Stats.** Real-world: expected claim counts.

**ch04 Combinatorics** — A.4.1–A.4.5 · Tier B · 1b,2d · 📺 EP003–EP005 (Viridian Forest → *Showdown in Pewter City*) · Viridian Forest/Pewter / **Brock** / Boulder / rock.
Sequence: A.4.1 permutations → A.4.2 combinations → ordered/unordered×replacement classifier → A.4.3 binomial → A.4.4 multinomial → A.4.5 hypergeometric.
Figures: `ch04_perm_vs_comb`, `ch04_2x2_classifier`, `ch04_binomial_flock` (**Pidgey #16** flock), `ch04_hypergeo_forest` (catch-without-replacement; **Caterpie #10, Weedle #13, Metapod #11**). Embeds: Brock @ Gym Battle (badge boulder); Geodude #74/Onix #95. Real-world: lottery/underwriting selection odds.

**ch05 Key Discrete Distributions** — A.5.0a–A.5.5 · Tier B · 2d · 📺 EP023–EP024 (Lavender) + EP026 *Pokémon Scent-sation!* · Lavender Tower/Celadon / **Erika** / Rainbow / ghost.
Sequence: A.5.0a geometric series → A.5.0b Taylor series for eˣ (series interlude) → A.5.1 geometric → A.5.2 memoryless → A.5.3 negative binomial → A.5.4 Poisson → A.5.5 sums of independent Poissons.
Figures: `ch05_geometric_series`, `ch05_taylor_exp`, `ch05_geometric_pmf` (slot/first-success; **Meowth #52**), `ch05_memoryless`, `ch05_negbin` (**Dugtrio #51**, wait-for-3rd), `ch05_poisson_window` (ghost swarm; **Gastly #92, Haunter #93**), `ch05_poisson_sums`. Embeds: Erika @ Gym Battle (rainbow); Gloom #44. Real-world: Poisson claim frequency; thinning/superposition.

**ch06 Deductibles & Limits (Discrete)** — A.6.1–A.6.3 · Tier B · 2e,2f · 📺 EP032 *The Ninja Poké-Showdown* (+ Safari EP035) · Fuchsia/Safari Zone / **Koga** / Soul / poison.
Sequence: A.6.1 deductibles (X−d)₊ → A.6.2 policy limits X∧u → coinsurance → E[X∧u]+E[(X−d)₊]=E[X] → per-loss vs per-payment → A.6.3 calculator approach.
Figures: `ch06_deductible_limit` (payment vs loss; **Safari Ball** item glyph), `ch06_payment_per_loss`, `ch06_safari_budget` (**Tauros #128, Kangaskhan #115**). Embeds: Koga @ Gym Battle (soul). Real-world: exactly how auto/health policies compute payment.

**ch07 Checkpoint A** — A.7 · — · 1*,2* · 📺 recap EP001–026 · route campfire / — / — / normal.
Concepts: spaced-retrieval over Act I; 12 mixed drills (League-qualifier mission). Figure: `ch07_act1_mindmap` (composites a few Act-I mascots). Length: ~2–4pp, no new theory.

### ACT II — CONTINUOUS ("The Smooth World")

**ch08 The Calculus Toolkit** — B.0.1–B.0.3 · Tier C (skippable) · prereq · 📺 EP013 *Mystery at the Lighthouse* · Bill's lighthouse / Oak·Bill / — / steel.
Sequence: B.0.1 differentiation (rules, optimization, L'Hôpital) → B.0.2 integration (u-sub, improper) → B.0.3 integration by parts (tabular) → the gamma integral ("Master Ball of integrals").
Figures: `ch08_deriv_rules`, `ch08_ibp_tabular`, `ch08_gamma_integral` (**Master Ball** item), `ch08_improper` (Bill's **Dragonite #149** cameo). Real-world: actuaries integrate loss densities daily; the gamma identity is a constant shortcut.

**ch09 Densities & CDFs** — B.1.1–B.1.3 · Tier B · 2a · 📺 EP022 *Abra and the Psychic Showdown* + EP024 · Saffron / **Sabrina** / Marsh / psychic.
Sequence: B.1.1 continuous overview (area = probability) → B.1.2 densities & CDFs (f=F′, normalizing constant) → B.1.3 mixed distributions.
Figures: `ch09_pdf_area` (**Kadabra #64** warps a bar chart into a curve), `ch09_cdf_from_pdf`, `ch09_mixed_dist`. Embeds: Sabrina @ Gym Battle (marsh); Haunter #93 (beats Sabrina). Real-world: loss-size densities.

**ch10 Continuous Moments** — B.2.1–B.2.3 · Tier B · 2c,2d · 📺 EP022–024 (Sabrina arc) · Saffron/Silph / Sabrina / — / psychic.
Sequence: B.2.1 moments of continuous (E[X]=∫xf) → B.2.2 moments of mixed → B.2.3 survival-function approach E[X]=∫₀^∞S(x)dx.
Figures: `ch10_continuous_moments`, `ch10_survival_integral` (**Mr. Mime #122**). Real-world: expected continuous loss.

**ch11 Key Continuous Distributions** — B.3.1–B.3.5 · Tier B · 2d · 📺 cross-Kanto travel · the smooth wilds / — / — / water.
Sequence: B.3.1 continuous uniform basics → B.3.2 uniform exam concepts → B.3.3 exponential (memoryless) → B.3.4 gamma/exponential/Poisson link → B.3.5 beta (+ Pareto enrichment).
Figures: `ch11_uniform` (**Porygon #137**), `ch11_exponential` (memoryless timer; **Electrode #101**), `ch11_gamma_shapes` (sum of exps; **Magneton #82**), `ch11_beta_shapes` (**Chansey #113**), `ch11_pareto_tail` (enrichment; **Snorlax #143**). Real-world: time-to-event & severity models.

**ch12 Normal & the CLT** — B.4.1–B.4.5 · **Tier A** · 2d,3i · 📺 EP077 *Round One – Begin!* (League crowd) · the Grand Gathering / — / — / normal.
Sequence: B.4.1 normal (pdf, standardize, 68-95-99.7) → B.4.2 interpolation (Z-table) → B.4.3 CLT (sum/mean) → B.4.4 continuity correction → B.4.5 lognormal (enrichment).
Figures: `ch12_normal_6895997` (bell; **Clefairy #35**), `ch12_standardize`, `ch12_clt_convergence` (many mixed sprites → bell), `ch12_continuity_correction`, `ch12_lognormal` (enrichment; **Gyarados #130**). Real-world: why pooling thousands of policies works.

**ch13 Continuous Deductibles & Review** — B.5.1–B.5.3 · Tier B · 2e,2f · 📺 EP056 *Volcanic Panic* (Cinnabar) · Cinnabar Lab / Oak·Blaine / — / fire.
Sequence: B.5.1 deductibles calculus approach → B.5.2 deductibles cases approach → B.5.3 review of other continuous ideas (Act-II checkpoint).
Figures: `ch13_deductible_calculus`, `ch13_cases_approach` (**Growlithe #58, Vulpix #37**). Real-world: continuous loss-and-payment pricing.

### ACT III — MULTIVARIATE ("The League")

**ch14 Joint Distributions** — C.1.1–C.1.2 · **Tier A** · 3a,3b · 📺 EP056 *Volcanic Panic* (Mansion logs = in-world extension) · Cinnabar Mansion / **Blaine** / Volcano / fire. *(authored — A; retrofit visuals)*
Sequence: C.1.1 joint pmf/pdf/cdf → double integrals over general regions → C.1.2 marginals → conditional distributions → independence (factor over rectangle).
Figures: `ch14_joint_grid`, `ch14_region_integral` (charred-ledger triangle; **Charmander #4/Charmeleon #5**), `ch14_marginal`, `ch14_conditional_slice`. Embeds: Blaine @ Gym Battle (volcano). Real-world: joint frequency–severity / copulas.

**ch15 Joint Moments & Covariance** — C.2.1–C.2.2 · **Tier A** · 3c,3e,3g,3h · 📺 EP075–076 (road to Plateau) · Victory Road / — / — / ground. *(authored — A; retrofit visuals)*
Sequence: C.2.1 joint moments E[XY] → C.2.2 covariance → correlation (−1≤ρ≤1) → variance of linear combinations (cross-terms) → independence vs ρ=0 → sums in-family (MGF).
Figures: `ch15_covariance_scatter`, `ch15_correlation_signs`, `ch15_linear_combo_var` (team as a sum; **Pikachu #25, Bulbasaur #1, Squirtle #7**). Embeds: Gary @ rival-trap (the SD-adder). Real-world: portfolio risk is covariance.

**ch16 Conditional & Double Expectation** — C.2.3 · **Tier A** · 3c,3d · 📺 EP063 *The Battle of the Badge* · Viridian Gym / **Giovanni** / Earth / ground. *(authored — A; retrofit visuals)*
Sequence: E[X|Y] as a random variable → law of total expectation → law of total variance (process vs parameter) → compound/mixture distributions.
Figures: `ch16_total_expectation_tree`, `ch16_total_variance_decomp`, `ch16_mixture` (**Rhyhorn #111, Nidoking #34**). Embeds: Giovanni @ Gym Battle (earth). Real-world: credibility (CAS MAS-II), compound claims.

**ch17 Order Statistics** — C.3.1–C.3.2 · Tier B · 3f · 📺 EP077–080 (League rounds) · Indigo Plateau / **Elite Four** / — / ice.
Sequence: C.3.1 order statistics (max/min CDFs) → k-th order statistic → min of independent exponentials → C.3.2 general order stats → reliability (series=min, parallel=max).
Figures: `ch17_order_max_min` (bracket; **Lapras #131**), `ch17_kth_order`, `ch17_reliability_series_parallel`. Embeds: Lorelei/Bruno/Agatha/Lance VS portraits. Real-world: reinsurance on the largest loss; reliability.

**ch18 Checkpoint B** — C.4 · — · 3* · 📺 EP077 · Plateau eve / — / — / normal.
Concepts: spaced-retrieval over Act III; 12 mixed drills. Figure: `ch18_act3_mindmap`. Length: ~2–4pp.

### FINALE

**ch19 Champion's Challenge** — exam finale (not TIA) · — · all · 📺 EP081 *Friend and Foe Alike* + EP082 *Friends to the End* · Indigo Plateau / **Gary** (rival) / Champion / dragon.
Concepts: 6-min pacing, two-pass strategy, calculator mastery, the shortcut catalog, error-log; **3 full weight-matched mock exams**. Figures: `ch19_pacing_strip`, `ch19_shortcut_catalog` (composite **Charizard #6, Pikachu #25** vs Gary's **Blastoise #9**). Real-world: exam-day execution.

---

## Part 2 — Real-asset (sprite) pull list for figures

Drive `assets/download_*.py` to ensure these real Gen-1 front sprites exist for figure compositing (all ∈ #1–151, already fetched): 1,4,5,6,7,9,10,11,13,16,17,19,21,25,26,34,35,37,43,44,50,51,52,54,58,60,63,64,65,74,77,81,82,92,93,94,95,100,101,111,113,115,118,120,121,122,126,128,130,131,132,137,143,149. VS portraits (`assets/vs/`): brock, misty, ltsurge, erika, koga, sabrina, blaine, giovanni, lorelei, bruno, agatha, lance, blue. Characters: oak, rocket. Badges: all 8 + trainer_license. Items: poke-ball, safari (→use poke-ball/great-ball), master-ball. **All real, already on disk; pull more from online only if a new beat needs it.**

---

## Part 3 — Execution order to the finished product (each chapter → QA grade A)

1. **Re-author the policy/standard into the dossiers:** generate `docs/design/chNN.md` for every chapter from the rows above (coverage manifest + concept order + figures+sprites + episode + questline + length).
2. **Retrofit the 4 completed chapters (ch01, ch02, ch14, ch15, ch16)** to §29 (now-playing box) + §30 (real-sprite figure compositing + real cast/badge embeds) — *no fabricated art* — then re-grade each to **A** on the full rubric (incl. dims 11/12/13).
3. **Generate the remaining chapters** in TIA-aware, hardest-first waves of 3, each through the full loop to **A**: ch03 → ch12 (resume Wave 2); then ch04, ch05, ch06; ch09, ch10, ch11; ch13, ch17, ch08; ch00, ch07, ch18; ch19 (+ mocks).
4. **Appendices A–I** (incl. the §29 Episode Companion viewing guide) once source chapters are stable.
5. **Chrome pass:** generate chapter banners + progress strips (real leader portrait + badge + map composited).
6. **Whole-book gate:** integrated harness green, lint green, full blind re-derivation, the tutor **grade-until-A on the assembled book**, render `make book` + `make workbook`, asset/copyright audit.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; private, non-commercial, non-distributed educational build; all sprite/anime assets are real assets sourced online, never generated.*
