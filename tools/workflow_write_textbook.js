export const meta = {
  name: 'write-kanto-exam-p',
  description: 'Write "Probability & Risk: A Kanto Journey" chapter-by-chapter, then audit and inspect formatting',
  whenToUse: 'After the scaffold is approved, to draft the textbook prose + problems and gate it through correctness, coverage, and formatting audits.',
  phases: [
    { title: 'Write',          detail: 'one agent per chapter fills the 10-part skeleton + problems' },
    { title: 'Audit',          detail: 'adversarial correctness / pedagogy / coverage review per chapter' },
    { title: 'FormatInspect',  detail: 'LaTeX, sprite/figure, callout-box, and structure inspection' },
  ],
}

// ---------------------------------------------------------------------------
// Chapters to write. `only` (via args) lets you run a subset, e.g. args:[8,5].
// ch08 (Safari Zone / loss models) is the gold-standard reference — write it first.
// ---------------------------------------------------------------------------
const ALL = [
  { n: 8,  file: 'ch08_fuchsia_safari.md',     topic: 'Loss models: deductibles, limits, coinsurance (2e-2f)',  weight: 'highest' },
  { n: 1,  file: 'ch01_trainer_school.md',     topic: 'Prerequisite calculus/series/gamma integral',           weight: 'low' },
  { n: 5,  file: 'ch05_vermilion_city.md',     topic: 'Random variables, expectation, moments, MGF (2a-2d)',   weight: 'high' },
  { n: 2,  file: 'ch02_route_1.md',            topic: 'Sample spaces, axioms, inclusion-exclusion (1a)',        weight: 'med' },
  { n: 3,  file: 'ch03_pewter_city.md',        topic: 'Combinatorics (1b)',                                     weight: 'med' },
  { n: 4,  file: 'ch04_cerulean_city.md',      topic: 'Conditional probability, Bayes (1c-1g)',                 weight: 'med' },
  { n: 6,  file: 'ch06_celadon_city.md',       topic: 'Discrete distributions (2d2)',                           weight: 'high' },
  { n: 7,  file: 'ch07_saffron_city.md',       topic: 'Continuous distributions + transforms (2d3)',            weight: 'high' },
  { n: 9,  file: 'ch09_cinnabar_island.md',    topic: 'Joint/marginal/conditional distributions (3a-3b)',       weight: 'med' },
  { n: 10, file: 'ch10_viridian_gym.md',       topic: 'Conditional + double expectation, total variance (3c-3d)', weight: 'med' },
  { n: 11, file: 'ch11_victory_road.md',       topic: 'Covariance, correlation, sums (3e,3g,3h)',               weight: 'med' },
  { n: 12, file: 'ch12_indigo_plateau.md',     topic: 'Order statistics, CLT (3f,3i)',                          weight: 'med' },
  { n: 13, file: 'ch13_champions_challenge.md', topic: 'Exam strategy + 3 weight-matched mock exams',           weight: 'high' },
]

const CHAPTERS = (Array.isArray(args) && args.length)
  ? ALL.filter(c => args.includes(c.n))
  : ALL

const SPEC_NOTE = `
Read DESIGN.md (charter, 10-part chapter architecture, production bible) and
FORMATTING.md (the five Pokemon-styled callout boxes authored as Pandoc fenced
divs :::, MathJax $...$ math with macros from book/mathjax-preamble.md, sprites
inserted as <figure> HTML via book/embed_visuals.py, print/bind constraints).
Match the existing stub's heading structure exactly. Pokemon art is referenced,
never drawn; only mathematical figures are generated.
`.trim()

const FINDING_SCHEMA = {
  type: 'object',
  properties: {
    issues: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          severity: { type: 'string', enum: ['blocker', 'major', 'minor'] },
          kind:     { type: 'string', enum: ['math-error', 'coverage-gap', 'pedagogy', 'latex', 'sprite-figure', 'box-style', 'structure', 'other'] },
          where:    { type: 'string' },
          detail:   { type: 'string' },
          fix:      { type: 'string' },
        },
        required: ['severity', 'kind', 'where', 'detail'],
      },
    },
    verdict: { type: 'string', enum: ['pass', 'revise'] },
  },
  required: ['issues', 'verdict'],
}

// ---------------------------------------------------------------------------
// Pipeline: each chapter flows Write -> Audit -> FormatInspect independently.
// ---------------------------------------------------------------------------
const results = await pipeline(
  CHAPTERS,

  // Stage 1 — WRITE
  (c) => agent(
    `You are writing Chapter ${c.n} of an Exam P study textbook.
${SPEC_NOTE}

Open book/chapters/${c.file} and replace the stub with a COMPLETE chapter on:
${c.topic} (syllabus weight: ${c.weight}).

Requirements:
- Fill all 10 sections: Cold Open, Oak's Briefing (tagged SOA outcomes), Pokedex
  Entries (formula + plain meaning + recognition cue), 3-5 Worked Examples (six-part
  skeleton, archetype tags, Trainer's Path / Professor's Path), Trainer's Tips,
  Team Rocket's Trap (+ "The fix:"), the Gym Battle capstone, then the two end-of-chapter
  sections below, then Badge Earned checklist.

- LIKE A REAL TEXTBOOK, the chapter ends with a PROBLEMS LIST followed by a SOLUTIONS
  LIST — never interleaved:
  * "The Gym Challenge (Problem Set)" = the full PROBLEMS LIST. Every problem has genuine
    in-world NARRATIVE FRAMING (a task Ash/you must accomplish for a story reason, with the
    numbers embedded in the scene) — no bare decontextualized drills. Number each problem
    C${c.n}.k and tier them: Route Trainers (mechanics) -> Gym Battles (true SOA difficulty)
    -> Elite Challenge (integrative). State ONLY the problems here (no solutions).
  * "Answer Key" = the SOLUTIONS LIST, AFTER all problems, in the same C${c.n}.k order:
    a complete worked solution for EVERY problem (not just final answers), each labeled with
    its archetype and back-referenced to the Pokedex Entry used, ending with a quick-answer
    table. Every problem in the list has exactly one matching solution.
- Use the five fenced-div callout boxes appropriately.
- All math in $...$/$$...$$ using the preamble macros. No unbalanced delimiters.
- Write every problem to problems/bank.d/ch${c.n}.yaml (a NEW file you own; top-level
  key \`problems:\`) with full schema (id C${c.n}.n, tier, archetype, outcomes,
  distributions, provenance, difficulty, statement, solution, answer, and a numeric
  \`verify:\` expression where possible). Do NOT touch problems/bank.yaml or other
  chapters' files — they are written concurrently.
- Insert sprite/badge/figure references AS <figure> HTML directly into your own
  chapter file (use the exact HTML format from book/embed_visuals.py helpers:
  sprites image-rendering:pixelated, centered block figures, alt text). Reference only
  assets that exist under assets/ (sprites 1-151, badges, types, characters, map) or a
  generated math figure in assets/diagrams/. Do NOT edit the shared embed_visuals.py.
- Remove the "status: stub" marker when done.

Return a one-paragraph summary of what you wrote and which outcomes it covers.`,
    { label: `write:ch${c.n}`, phase: 'Write' }
  ),

  // Stage 2 — AUDIT (adversarial correctness + pedagogy + coverage)
  (writeSummary, c) => agent(
    `Adversarially audit Chapter ${c.n} (book/chapters/${c.file}) just written.
Author's summary: ${writeSummary}

Check, skeptically:
- MATH: every worked example and answer key is numerically correct. Run
  \`python3 sims/verify_examples.py\` and \`python3 tools/check_coverage.py\`.
- COVERAGE: the chapter's mapped SOA outcomes each have a Pokedex Entry and >=1
  worked example; problems hit the tier counts (DESIGN.md 4.1).
- PEDAGOGY: recognition cues present; archetype tags on examples; Trainer's Tips and
  the Team Rocket trap are correct and instructive; difficulty matches true SOA.
Report findings with the schema. verdict 'revise' if any blocker/major remains.`,
    { label: `audit:ch${c.n}`, phase: 'Audit', schema: FINDING_SCHEMA }
  ),

  // Stage 3 — FORMAT INSPECTION (LaTeX, sprites/figures, boxes, structure)
  (audit, c) => agent(
    `Inspect Chapter ${c.n} (book/chapters/${c.file}) for FORMATTING issues only.
Prior audit verdict: ${audit?.verdict}; issues: ${JSON.stringify(audit?.issues || [])}

Run \`python3 tools/check_format.py\` and also inspect by hand for:
- LaTeX: balanced $ and $$, matched \\left/\\right, macros defined in the preamble,
  no raw/garbled TeX, display math renders.
- Sprites/figures: every <figure> in the chapter references an asset that exists under
  assets/ (sprites 1-151, badges, types, characters, map) or a generated math figure in
  assets/diagrams/; alt text present; centered block figures (no floats); no hand-drawn
  Pokemon. (Figures live inline in the chapter file, not in embed_visuals.py.)
- Callout boxes: only the five known classes, fenced divs balanced (:::).
- Structure: all 10 sections present in order; the chapter ends with the PROBLEMS LIST
  (Gym Challenge) and THEN the SOLUTIONS LIST (Answer Key) — solutions after, never
  interleaved; every problem C${c.n}.k in the problem set has exactly one matching worked
  solution in the key; print/bind friendliness (no oversized inline HTML that breaks
  pagination).
Apply safe fixes directly. Return findings with the schema (verdict 'pass' when clean).`,
    { label: `format:ch${c.n}`, phase: 'FormatInspect', schema: FINDING_SCHEMA }
  ),
)

// ---------------------------------------------------------------------------
// Roll-up
// ---------------------------------------------------------------------------
const rollup = CHAPTERS.map((c, i) => ({
  chapter: c.n,
  file: c.file,
  audit: results[i]?.verdict ?? 'unknown',
  formatIssues: (results[i]?.issues || []).filter(x => x.severity !== 'minor').length,
}))

const needsWork = rollup.filter(r => r.audit !== 'pass' || r.formatIssues > 0)
log(`Done. ${CHAPTERS.length} chapters processed; ${needsWork.length} need follow-up.`)

return { rollup, needsWork }
