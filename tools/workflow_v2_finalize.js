export const meta = {
  name: 'v2-finalize-repair',
  description: 'Complete the cut-off Finalize phase: generate missing figures, extract missing problem YAML, write all appendices + notation ledger, top up coverage, run gates',
  whenToUse: 'Continuation after the comprehensive run was halted by the session limit.',
  phases: [
    { title: 'Repair',   detail: 'missing figures + missing problem YAML + Bayes majors' },
    { title: 'Finalize', detail: 'appendices A-I + notation ledger + Reading-the-Symbols primer' },
    { title: 'Coverage', detail: 'top up problems to the coverage guarantee' },
    { title: 'Gate',     detail: 'run check_format / verify_examples / check_coverage + verdict' },
  ],
}

const SPEC = `
GOVERNING SPECS: MASTER_PLAN_V2.md (teaching model, Part 9 checklist), AUDIT.md, DESIGN.md, FORMATTING.md.
Math is \$...\$ with macros from book/mathjax-preamble.md (NOTE: use \\mid for "given", not \\middle).
Boxes are ::: fenced divs; end matter is ::: problem-set then ::: answer-key. Pokemon art is repo-sourced;
only MATH figures are generated (matplotlib, figures/src/kanto_theme.mplstyle, 300 DPI, legible in grayscale).
Verify expressions must use provided names (math, st), never __import__.
`.trim()

// chapters with <figure> refs to PNGs that were never generated
const FIG_CH = ['ch12_double_expectation', 'ch13_covariance', 'ch14_order_clt', 'ch15_champion']
// chapters whose problem sets exist in prose but were never written to bank.d/*.yaml
const PROB_CH = [
  { file: 'ch01_toolkit_numbers', bank: 'ch01' },
  { file: 'ch02_toolkit_calculus', bank: 'ch02' },
  { file: 'ch06_random_variables', bank: 'ch06' },
  { file: 'ch09_continuous', bank: 'ch09' },
  { file: 'ch15_champion', bank: 'ch15' },
]

// =========================================================================
phase('Repair')
const repair = await parallel([
  // generate every missing math figure these chapters reference
  ...FIG_CH.map(file => () => agent(
    `${SPEC}\n\nbook/chapters/${file}.md references several assets/diagrams/*.png that do NOT exist yet
    (run: grep -oE 'assets/diagrams/[a-zA-Z0-9_]+\\.png' book/chapters/${file}.md | sort -u, then check which are
    missing under assets/diagrams/). For each MISSING figure, read the surrounding text + caption to learn what it
    must show, then write/extend a committed script figures/src/gen_${file.slice(0,4)}.py (matplotlib, use
    figures/src/kanto_theme.mplstyle, 300 DPI, color-blind-safe + readable in grayscale, clean labels) that
    produces EXACTLY those filenames. Run it. Confirm every referenced PNG now exists. Return the file list.`,
    { label: `figures:${file.slice(0,4)}`, phase: 'Repair' })),

  // extract each missing chapter's problems + solutions into its bank.d yaml
  ...PROB_CH.map(c => () => agent(
    `${SPEC}\n\nbook/chapters/${c.file}.md has a full problem set (::: problem-set, numbered C*.k) and Answer Key
    (::: answer-key) in prose, but problems/bank.d/${c.bank}.yaml is MISSING. Create it: for every problem in the
    chapter, add an entry with the full schema (id, chapter, tier, archetype, outcomes, distributions, provenance,
    difficulty, narrative_hook, statement, solution, answer, and a numeric verify: expression using math/st). The
    statement/solution/answer MUST match what the chapter already prints (do not invent new answers). Return the
    count written.`,
    { label: `problems:${c.bank}`, phase: 'Repair' })),

  // resolve the 2 residual majors on the Bayes reference chapter
  () => agent(
    `${SPEC}\n\nRe-audit book/chapters/ch05_bayes.md (the gold-standard reference) against MASTER_PLAN_V2 Part 9
    and Tier E: nine-beat completeness, every symbol introduced before use, every result derived not asserted,
    misconception dismantled in-lesson, Cold-Read & Skip gates, display math for complex expressions. Fix any
    blocker/major directly in the file (and problems/bank.d/ch05.yaml if needed). Run python3 tools/check_format.py
    afterward. Report what you changed.`,
    { label: 'revise:ch05', phase: 'Repair' }),
])
log(`Repair done: ${repair.filter(Boolean).length}/${repair.length} agents returned.`)

// =========================================================================
phase('Finalize')
await parallel([
  // notation ledger + Ch0 primer + notation appendix (G)
  () => agent(
    `${SPEC}\n\nBuild notation_ledger.md: scan book/chapters/*.md for every mathematical symbol; record its spoken
    name, plain meaning, and the chapter of first introduction. Ensure book/chapters/ch00_orientation.md contains a
    "Reading the Symbols" primer (how to read aloud Σ, ∫, ∈, | (given), P(·), E[·], subscripts, variable vs realized
    value). Fill book/appendices/appendix_g_glossary.md as the notation + glossary appendix (Kanto term ↔ formal
    term), cross-referenced to first appearances. Remove the stub markers from files you complete.`,
    { label: 'finalize:notation', phase: 'Finalize' }),
  // reference appendices A, B, C
  () => agent(
    `${SPEC}\n\nFill these appendices (remove their stub markers); verify all formulas against the chapters, display
    math where complex:
    - appendix_a_formula_sheet.md: one-page master formula sheet + the shortcut catalog (gamma integral, Darth Vader
      survival rule, MGF kernel recognition, memorylessness, continuity correction).
    - appendix_b_distribution_tables.md: every in-scope distribution (Bernoulli, binomial, geometric, negative
      binomial, hypergeometric, Poisson, discrete uniform; uniform, exponential, gamma, beta, normal) with support,
      pmf/pdf, cdf, mean, variance, MGF, recognition cue; enrichment families flagged.
    - appendix_c_normal_table.md: the provided standard-normal table + symmetry techniques.`,
    { label: 'finalize:appx-abc', phase: 'Finalize' }),
  // reference appendices D, E, F, H, I
  () => agent(
    `${SPEC}\n\nFill these appendices (remove their stub markers):
    - appendix_d_calculator_guide.md: TI-30XS MultiView & BA II Plus keystrokes for every recurring computation.
    - appendix_e_exam_day.md: logistics & psychology (registration, CBT interface, cleared calculator, two-pass plan).
    - appendix_f_cross_reference.md: chapter ↔ ACTEX/Broverman & Finan sections + SOA sample-question numbers.
    - appendix_h_answer_keys.md: consolidation/pointer to the per-chapter keys.
    - appendix_i_risk_primer.md: the "Risk and Insurance" study-note primer needed for Ch10 (Pricing the Risk).`,
    { label: 'finalize:appx-defhi', phase: 'Finalize' }),
])

// =========================================================================
phase('Coverage')
await agent(
  `${SPEC}\n\nRun python3 tools/check_coverage.py. TOP UP problems so every SOA outcome has >=8 problems and every
  in-scope distribution has >=6 (current gaps include beta, bernoulli, gamma, geometric, negative_binomial). Add
  new, narratively-framed problems WITH full worked solutions to the appropriate problems/bank.d/*.yaml (full schema
  + numeric verify: using math/st), and also add them to the corresponding chapter's ::: problem-set and
  ::: answer-key so prose and bank stay in sync. Re-run check_coverage until structural errors are 0 and gaps are
  closed (or report any that remain). Return the final coverage summary.`,
  { label: 'coverage:topup', phase: 'Coverage' })

// =========================================================================
phase('Gate')
const gate = await agent(
  `Run and report the final whole-book integrity gates:
  - python3 tools/check_format.py    (must PASS — no missing figures, no LaTeX/box errors)
  - python3 sims/verify_examples.py   (must PASS — every numeric answer)
  - python3 tools/check_coverage.py   (0 structural errors; report any remaining gaps)
  Then give a one-paragraph verdict vs MASTER_PLAN_V2 Part 9 (Cold-Read & Skip gates, verification green, coverage
  guarantee). List any remaining issues by chapter. Return as text.`,
  { label: 'gate', phase: 'Gate' })

return { repair_agents: repair.filter(Boolean).length, gate }
