export const meta = {
  name: 'v2-complete-book',
  description: 'Execute the entire MASTER_PLAN_V2: build Bayes as the gold standard, roll the nine-beat teaching model across every chapter, then the full finalize pass',
  whenToUse: 'The single comprehensive run that completes all tasks in MASTER_PLAN_V2 (Phases 1-4).',
  phases: [
    { title: 'Reference',  detail: 'build the Bayes chapter (ch05) to gold standard — the exemplar' },
    { title: 'Roll',       detail: 'rebuild every other chapter + checkpoint to the v2 standard, hardest-first' },
    { title: 'Finalize',   detail: 'notation ledger + primer, appendices, coverage top-up, integrity gates' },
  ],
}

const SPEC = `
GOVERNING SPECS (read before acting): MASTER_PLAN_V2.md (the teaching model — two-reader contract,
the nine-beat Concept Lesson Arc, depth tiers, notation-as-language Part 4, visual/UX Part 12,
narrative+real-world Part 13, the Part 9 "is this masterful?" checklist, the Cold-Read + Skip gates),
AUDIT.md (Tier 0 correctness, Tier E teaching, Tiers 1-3), DESIGN.md, FORMATTING.md.
Pipeline is Markdown→Pandoc→PDF: \$...\$ math with macros from book/mathjax-preamble.md; the styled
fenced-div boxes ::: pokedex-entry / trainers-tip / team-rocket / kanto-realworld / cold-open /
concept-gate ; the end matter wrapped in ::: problem-set then ::: answer-key (problems first, full
worked solutions after, never interleaved); sprites/figures as centered <figure> HTML with alt text;
Iron Rule — math never over a sprite; complex math in DISPLAY mode, never cramped inline.
`.trim()

const BUILD_RULES = (ch) => `
Rewrite book/chapters/${ch.file} COMPLETELY to the masterful v2 standard (replaces the stub).
- Mine the Draft-1 source ${ch.draft1 ? `drafts/chapters_draft1/${ch.draft1}.md and its problems in drafts/bank_draft1/` : '(none — new chapter)'} for CORRECT math, numbers, and problems to preserve — but REWRITE the teaching from scratch to the nine-beat arc; do not inherit Draft-1's "formula + one-line gloss" style.
- Read book/chapters/ch05_bayes.md as the GOLD-STANDARD EXEMPLAR for voice, depth, box usage, and formatting; match its quality.
- Teaching-first skeleton: Cold Open → "Where you are" 60-second retrieval → Oak's Briefing + Test-Out gate → for EACH concept (difficulty order): a ::: concept-gate skip micro-check, then the full nine-beat arc, then Pokédex Entry + Recognition Cue → faded worked examples (full→partial→independent; Tier-A first example understanding-first) → Trainer's Tips → Team Rocket's Trap → From Kanto to the Real World → Gym Battle capstone → Gym Challenge (::: problem-set, tiered, numbered ${ch.num}.k) → Answer Key (::: answer-key, one full worked solution per problem, after all problems) → Badge Earned checklist.
- Assume NOTHING: every symbol introduced one glyph at a time (named + read aloud + motivated) before use; concrete numbers before general notation; derive every result; surface & dismantle the canonical misconception in-lesson.
- Depth ∝ tier ${ch.tier}. Write problems to problems/bank.d/${ch.bank}.yaml (overwrite) with full schema incl. a numeric verify: expression using provided names (math, st), not __import__.
- Remove the "status: stub" marker.`

const FINDINGS = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['pass', 'revise'] },
    issues: { type: 'array', items: { type: 'object', properties: {
      severity: { type: 'string', enum: ['blocker', 'major', 'minor'] },
      where: { type: 'string' }, detail: { type: 'string' }, fix: { type: 'string' },
    }, required: ['severity', 'where', 'detail', 'fix'] } },
  },
  required: ['verdict', 'issues'],
}

// ---- chapter registry (hardest-first within Roll) ----
const A = (file, num, bank, topic, draft1) => ({ file, num, bank, topic, draft1, tier: 'A', kind: 'chapter' })
const B = (file, num, bank, topic, draft1) => ({ file, num, bank, topic, draft1, tier: 'B', kind: 'chapter' })
const C = (file, num, bank, topic, draft1) => ({ file, num, bank, topic, draft1, tier: 'C', kind: 'chapter' })
const CK = (file, num, bank, topic) => ({ file, num, bank, topic, draft1: '', tier: 'C', kind: 'checkpoint' })

const BAYES = A('ch05_bayes', 'C5', 'ch05', 'Conditional probability, independence, total probability, Bayes', 'ch04_cerulean_city')

const ROLL = [
  // Tier A first (the chapters that decide the score)
  A('ch06_random_variables', 'C6', 'ch06', 'Random variables; pmf/pdf/cdf/survival', 'ch05_vermilion_city'),
  A('ch07_center_spread', 'C7', 'ch07', 'Expectation, variance, moments, MGF, Darth Vader rule', 'ch05_vermilion_city'),
  A('ch10_pricing', 'C10', 'ch10', 'Deductibles, limits, coinsurance, inflation; loss vs payment', 'ch08_fuchsia_safari'),
  A('ch11_joint', 'C11', 'ch11', 'Joint/marginal/conditional distributions; double integrals', 'ch09_cinnabar_island'),
  A('ch12_double_expectation', 'C12', 'ch12', 'Conditional & double expectation; total variance', 'ch10_viridian_gym'),
  A('ch13_covariance', 'C13', 'ch13', 'Covariance, correlation, linear combinations, sums', 'ch11_victory_road'),
  A('ch14_order_clt', 'C14', 'ch14', 'Order statistics; CLT with continuity correction', 'ch12_indigo_plateau'),
  // Tier B
  B('ch04_counting', 'C4', 'ch04', 'Combinatorics', 'ch03_pewter_city'),
  B('ch08_discrete', 'C8', 'ch08', 'Discrete distributions', 'ch06_celadon_city'),
  B('ch09_continuous', 'C9', 'ch09', 'Continuous distributions & transformations', 'ch07_saffron_city'),
  B('ch02_toolkit_calculus', 'C2', 'ch02', 'Series & calculus for probability; gamma identity', 'ch01_trainer_school'),
  B('ch15_champion', 'C15', 'ch15', 'Exam strategy, shortcut catalog, 3 mock exams', 'ch13_champions_challenge'),
  // Tier C foundations
  C('ch00_orientation', 'C0', 'ch00', 'How to use the book; how to read the math', ''),
  C('ch01_toolkit_numbers', 'C1', 'ch01', 'Numbers, variables, functions, notation', 'ch01_trainer_school'),
  C('ch03_outcomes', 'C3', 'ch03', 'Sample spaces, events, axioms, inclusion-exclusion', 'ch02_route_1'),
  // checkpoints
  CK('ch05x_checkpoint_a', 'CA', 'ch05x', 'Spaced-retrieval review of Topic 1 (General Probability)'),
  CK('ch10x_checkpoint_b', 'CB', 'ch10x', 'Spaced-retrieval review of Topic 2 (Univariate)'),
]

// audit lenses chosen by tier (depth ∝ difficulty)
function auditLenses(ch) {
  const teaching = `${SPEC}\n\nAudit book/chapters/${ch.file} for TEACHING QUALITY vs MASTER_PLAN_V2 Part 9 + Tier E. As if you knew none of this: do Tier-A/B concepts run all nine beats in order? one-sentence idea before any symbol? concrete before notation? every result DERIVED not asserted? misconception dismantled in-lesson? difficulty ramp? Apply the COLD-READ and SKIP tests. Report findings.`
  const correctness = `${SPEC}\n\nAudit book/chapters/${ch.file} and problems/bank.d/${ch.bank}.yaml for CORRECTNESS by INDEPENDENT BLIND RE-DERIVATION: solve each worked example and problem from the statement alone, WITHOUT reading the book's solution, then compare. Run \`python3 sims/verify_examples.py\` and \`python3 tools/check_coverage.py\`. Check invariants. A disagreement is a blocker. Report findings.`
  const formatNotation = `${SPEC}\n\nAudit book/chapters/${ch.file} for NOTATION (Part 4: every symbol introduced before use, named + read aloud), LaTeX/RENDER (run \`python3 tools/check_format.py\`; complex math in display; no broken macros/stray \$; boxes balanced & known classes; problem-set then answer-key), and the Iron Rule (math never over sprites). Report findings.`
  const immersion = `${SPEC}\n\nAudit book/chapters/${ch.file} for IMMERSION (Part 13: feels like Kanto, problems are Ash's tasks, fidelity rule) and the TRANSFER test (real-world actuarial use named; de-skinnable). Report findings.`
  if (ch.tier === 'A') return [['teaching', teaching], ['correctness', correctness], ['format', formatNotation], ['immersion', immersion]]
  if (ch.tier === 'B') return [['teaching', teaching], ['correctness', correctness], ['format', formatNotation]]
  return [['correctness', correctness], ['format', formatNotation]]   // C / checkpoints
}

// build one chapter end-to-end; returns {file, blockers, majors}
async function buildChapter(ch, isRef) {
  const ph = (s) => isRef ? 'Reference' : 'Roll'
  // Blueprint (chapters only; checkpoints skip straight to author)
  if (ch.kind === 'chapter') {
    await agent(`${SPEC}\n\nProduce a teaching BLUEPRINT for book/chapters/${ch.file} (${ch.topic}, tier ${ch.tier}): concepts in difficulty order with tiers, and for each the one-sentence idea, the concrete in-world instance, the misconception to dismantle, the new notation (glyph + spoken name), figures needed (assets/diagrams/${ch.file.slice(0,4)}*.png), and the problem budget. Then STOP — return the blueprint as text for the author to use.`,
      { label: `blueprint:${ch.num}`, phase: ph() })
  }
  // Author
  const authorPrompt = ch.kind === 'checkpoint'
    ? `${SPEC}\n\nWrite book/chapters/${ch.file} as a CHECKPOINT (no new content): a short spaced-retrieval review of "${ch.topic}" — retrieval prompts that force recall, then ~6-10 mixed problems drawing across those chapters, then a full Answer Key (::: problem-set then ::: answer-key). Add its problems to problems/bank.d/${ch.bank}.yaml with verify: expressions. Keep the Kanto frame light (Rocket Hideout / review montage). Remove the stub marker.`
    : `${SPEC}\n\n${BUILD_RULES(ch)}`
  const authorSummary = await agent(authorPrompt, { label: `author:${ch.num}`, phase: ph() })

  // Figures (generate any plots the chapter references, from committed code)
  await agent(`${SPEC}\n\nFor book/chapters/${ch.file}: find every <figure> that references assets/diagrams/*.png, and ensure each exists. For any missing MATH figure (no Pokemon art — only repo sprites are art), write/extend a committed matplotlib script figures/src/gen_${ch.file.slice(0,4)}.py using figures/src/kanto_theme.mplstyle at 300 DPI (legible in grayscale), run it to create the PNGs. Confirm all referenced figures now exist. Return the list.`,
    { label: `figures:${ch.num}`, phase: ph() })

  // Audit (lenses by tier), then revise
  const lenses = auditLenses(ch)
  const findings = await parallel(lenses.map(([name, prompt]) => () =>
    agent(prompt, { label: `audit:${ch.num}:${name}`, phase: ph(), schema: FINDINGS })))
  const issues = findings.filter(Boolean).flatMap(f => f.issues || [])
  const blockers = issues.filter(i => i.severity === 'blocker').length
  const majors = issues.filter(i => i.severity === 'major').length
  if (issues.length) {
    await agent(`${SPEC}\n\nApply fixes to book/chapters/${ch.file} (and problems/bank.d/${ch.bank}.yaml if needed) for these findings, blockers & majors first. Preserve the nine-beat structure, boxes, textbook problem/solution formatting, and verified answers.\nFindings: ${JSON.stringify(issues)}\nAuthor summary: ${authorSummary}\nConfirm each blocker/major resolved.`,
      { label: `revise:${ch.num}`, phase: ph() })
  }
  return { file: ch.file, tier: ch.tier, blockers, majors }
}

// =========================================================================
phase('Reference')
log('Building the Bayes chapter (ch05) as the gold-standard exemplar...')
const refResult = await buildChapter(BAYES, true)

// =========================================================================
phase('Roll')
log(`Rolling the model across ${ROLL.length} chapters/checkpoints, hardest-first...`)
const rollResults = await parallel(ROLL.map(ch => () => buildChapter(ch, false)))

// =========================================================================
phase('Finalize')
const finalize = await parallel([
  // Notation ledger + Reading-the-Symbols primer + notation appendix
  () => agent(`${SPEC}\n\nBuild notation_ledger.md: every symbol used in the book, its spoken name, plain meaning, and the chapter/section of first introduction (scan book/chapters/*.md). Then ensure book/chapters/ch00_orientation.md contains the "Reading the Symbols" primer (how to read Σ, ∫, ∈, | given, P(·), E[·], subscripts, variable vs realized value) and fill book/appendices/appendix_g_glossary.md as the notation appendix cross-linked to first appearances. Remove stubs you complete.`,
    { label: 'finalize:notation', phase: 'Finalize' }),
  // Reference appendices A,B,C,D + I
  () => agent(`${SPEC}\n\nFill the reference appendices (remove their stubs): appendix_a_formula_sheet (master formula sheet + shortcut catalog), appendix_b_distribution_tables (every in-scope distribution: support, pmf/pdf, cdf, mean, variance, MGF, recognition cue; enrichment flagged), appendix_c_normal_table (the provided Z-table + symmetry techniques), appendix_d_calculator_guide (TI-30XS & BA II Plus keystrokes), appendix_i_risk_primer (Risk & Insurance study-note primer for Ch10). All math in display where complex; verify formulas against the chapters.`,
    { label: 'finalize:appendices', phase: 'Finalize' }),
  // Exam appendices E,F,H + coverage top-up
  () => agent(`${SPEC}\n\nFill appendix_e_exam_day (logistics & psychology), appendix_f_cross_reference (chapter↔ACTEX/Broverman/Finan + SOA sample numbers), appendix_h_answer_keys (pointer/consolidation). Then run \`python3 tools/check_coverage.py\` and TOP UP problems so every SOA outcome has >=8 problems and every in-scope distribution >=6 (add problems to the relevant problems/bank.d/*.yaml with verify: expressions). Remove stubs you complete.`,
    { label: 'finalize:coverage', phase: 'Finalize' }),
])

phase('Finalize')
const gate = await agent(`Run the integrity gates and report the final whole-book verdict:
  - \`python3 tools/check_format.py\`   (render/notation/structure — must PASS)
  - \`python3 sims/verify_examples.py\`  (numeric answers — must PASS)
  - \`python3 tools/check_coverage.py\`  (coverage — structural errors must be 0; report gaps)
Then a one-paragraph verdict vs MASTER_PLAN_V2 Part 9: are the Cold-Read & Skip gates met book-wide, is the verification green, does the coverage guarantee hold? List remaining blockers/majors by chapter. Return as text.`,
  { label: 'finalize:gate', phase: 'Finalize' })

return {
  reference: refResult,
  roll: rollResults.filter(Boolean),
  needsWork: [refResult, ...rollResults.filter(Boolean)].filter(r => r.blockers > 0 || r.majors > 0),
  gate,
}
