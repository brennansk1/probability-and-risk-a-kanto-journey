export const meta = {
  name: 'v2-teaching-audit',
  description: 'Independent teaching-quality audit of every chapter vs MASTER_PLAN_V2 Part 9 (Cold-Read + Skip gates), then auto-revise chapters that fall short, then re-gate',
  whenToUse: 'The honest pass the comprehensive run missed (its schema audits failed silently). Text outputs — no StructuredOutput.',
  phases: [
    { title: 'Audit',  detail: 'one grader per chapter against the Part-9 teaching checklist' },
    { title: 'Revise', detail: 'fix chapters graded below the masterful bar' },
    { title: 'Gate',   detail: 're-run integrity gates + verdict' },
  ],
}

const SPEC = `
GOVERNING SPEC: MASTER_PLAN_V2.md. Audit TEACHING QUALITY (Part 2 doctrine, Part 3 nine-beat Concept
Lesson Arc, Part 4 notation-as-language, Part 5 depth tiers, Part 9 checklist + the two ultimate gates).
ch05_bayes is the GOLD-STANDARD reference — judge other chapters against its quality. Reference, do not
re-audit it. ch00 is orientation and chNNx are checkpoints (review template) — grade them on their own terms.
`.trim()

// chapter file, tier, topic
const CH = [
  ['ch00_orientation', 'C', 'orientation + Reading the Symbols primer'],
  ['ch01_toolkit_numbers', 'C', 'numbers/variables/functions/notation'],
  ['ch02_toolkit_calculus', 'B', 'series & calculus; gamma identity'],
  ['ch03_outcomes', 'C', 'sample spaces, axioms, inclusion-exclusion'],
  ['ch04_counting', 'B', 'combinatorics'],
  ['ch06_random_variables', 'A', 'pmf/pdf/cdf/survival'],
  ['ch07_center_spread', 'A', 'expectation/variance/MGF/Darth Vader'],
  ['ch08_discrete', 'B', 'discrete distributions'],
  ['ch09_continuous', 'A', 'continuous distributions & transforms'],
  ['ch10_pricing', 'A', 'deductibles/limits/coinsurance; loss vs payment'],
  ['ch11_joint', 'A', 'joint/marginal/conditional; double integrals'],
  ['ch12_double_expectation', 'A', 'conditional & double expectation; total variance'],
  ['ch13_covariance', 'A', 'covariance/correlation/sums'],
  ['ch14_order_clt', 'A', 'order statistics; CLT'],
  ['ch15_champion', 'B', 'exam strategy + 3 mock exams'],
  ['ch05x_checkpoint_a', 'C', 'Topic-1 spaced-retrieval review'],
  ['ch10x_checkpoint_b', 'C', 'Topic-2 spaced-retrieval review'],
]

// Audit -> Revise as a per-chapter pipeline (a chapter revises as soon as its grade lands).
const results = await pipeline(
  CH,
  // Stage 1: grade
  ([file, tier, topic]) => agent(
    `${SPEC}

Grade book/chapters/${file}.md (tier ${tier} — ${topic}) for TEACHING QUALITY as if you knew none of it.
Compare against book/chapters/ch05_bayes.md (the gold standard). Go through the Part-9 teaching checklist
item by item for each major concept:
- nine beats present and IN ORDER (one-sentence idea → concrete instance → reason in words → dismantle the
  tempting wrong idea → notation one glyph at a time → derive the formula → ramp → picture/table → consolidate)?
- one-sentence plain idea BEFORE any symbol? concrete numeric instance BEFORE general notation?
- every new symbol introduced (named + read aloud + motivated) before first use?
- every result DERIVED from prior knowledge, not asserted?
- a natural misconception surfaced AND dismantled in-lesson?
- difficulty ramp (simplest → twist → general → edge)? depth proportional to tier?
- worked examples fade full→partial→independent; Tier-A first example understanding-first?
- the COLD-READ TEST (a true beginner could learn each concept here, no outside source) — PASS/FAIL?
- the SKIP TEST (a working test-out gate at chapter and concept level) — PASS/FAIL?
(For ch00/checkpoints, grade on their own purpose.)

Return a text report that ENDS with a final line EXACTLY in this form:
GRADE: <masterful|revise> | COLDREAD: <pass|fail> | SKIP: <pass|fail>
followed by a bulleted FIXES list (specific, file-located) if anything is below the Bayes bar.`,
    { label: `audit:${file.slice(0,5)}`, phase: 'Audit' }),

  // Stage 2: revise iff graded 'revise' or a gate failed
  (report, [file, tier]) => {
    const verdict = (report.match(/GRADE:\s*(\w+)/i) || [])[1]?.toLowerCase()
    const coldread = (report.match(/COLDREAD:\s*(\w+)/i) || [])[1]?.toLowerCase()
    const skip = (report.match(/SKIP:\s*(\w+)/i) || [])[1]?.toLowerCase()
    const needsFix = verdict === 'revise' || coldread === 'fail' || skip === 'fail'
    if (!needsFix) return { file, status: 'masterful' }
    return agent(
      `${SPEC}

Revise book/chapters/${file}.md to meet the masterful bar (match ch05_bayes quality). Apply the FIXES from
this teaching audit, hardest first. Preserve correctness (answers already verified at seed=151 — do not
change numeric answers), the boxes, the ::: problem-set / ::: answer-key formatting, and all figures.
Where a concept is asserted, ADD the derivation; where a symbol is used before introduction, introduce it
first; where a beat is missing, add it; ensure the Cold-Read and Skip gates pass.

AUDIT REPORT:
${report}

After editing, run python3 tools/check_format.py and confirm no new errors. Briefly confirm Cold-Read and
Skip now pass.`,
      { label: `revise:${file.slice(0,5)}`, phase: 'Revise' }
    ).then(() => ({ file, status: 'revised' }))
  },
)

// ---- Gate ----
phase('Gate')
const gate = await agent(
  `Run the integrity gates and report the final verdict:
   - python3 tools/check_format.py     (must PASS)
   - python3 sims/verify_examples.py    (must PASS — answers unchanged)
   - python3 tools/check_coverage.py    (must PASS)
  Then a one-paragraph teaching-readiness verdict. Return as text.`,
  { label: 'gate', phase: 'Gate' })

const masterful = results.filter(r => r && r.status === 'masterful').map(r => r.file)
const revised = results.filter(r => r && r.status === 'revised').map(r => r.file)
return { masterful, revised, gate }
