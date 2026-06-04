export const meta = {
  name: 'sprint-bayes-gold-standard',
  description: 'Phase 1: rebuild the Bayes chapter (ch04) to the v2 nine-beat masterful teaching standard, with multi-lens audit and integrity gates',
  whenToUse: 'The v2 Phase-1 sprint: produce the gold-standard reference chapter the model is rolled out from.',
  phases: [
    { title: 'Blueprint',  detail: 'concept inventory + tiers + nine-beat plan + notation ledger + figures + problems' },
    { title: 'Build',      detail: 'author the full chapter (prose+problems) and generate its figures, in parallel' },
    { title: 'Audit',      detail: 'four independent lenses: teaching, notation/LaTeX, blind correctness, immersion/visual/real-world' },
    { title: 'Revise',     detail: 'apply all findings to the chapter + problem file' },
    { title: 'Gate',       detail: 'run lint + verify; report the masterful-checklist verdict' },
  ],
}

const CH = 'book/chapters/ch04_cerulean_city.md'   // the Bayes chapter (v2 "Ch 5")
const PROBS = 'problems/bank.d/ch4.yaml'
const N = 4                                        // problem-id prefix C4.k

const SPEC = `
GOVERNING SPECS — read before doing anything:
- MASTER_PLAN_V2.md   (the teaching model: two-reader contract, the nine-beat Concept Lesson Arc,
                       depth tiers, notation-as-language, the visual/UX layer Part 12, the narrative
                       immersion + real-world weave Part 13, the Part 9 "is this masterful?" checklist,
                       and the Cold-Read + Skip ultimate gates).
- AUDIT.md            (Tier 0 correctness, Tier E teaching completeness, Tiers 1-3).
- DESIGN.md           (curriculum, chapter architecture, production bible).
- FORMATTING.md       (Markdown→Pandoc→PDF pipeline; the 5 fenced-div callout boxes ::: ; MathJax \$...\$
                       with macros from book/mathjax-preamble.md; sprites as <figure> HTML; print/bind).
This is the Bayes chapter (Cerulean City / Misty): conditional probability, independence,
multiplication & addition rules, law of total probability, Bayes' theorem. It is TIER A — the
proving-ground chapter. Assume the reader knows NOTHING beyond arithmetic.
`.trim()

const BLUEPRINT_SCHEMA = {
  type: 'object',
  properties: {
    concepts: { type: 'array', items: { type: 'object', properties: {
      name: { type: 'string' },
      tier: { type: 'string', enum: ['A', 'B', 'C'] },
      outcomes: { type: 'array', items: { type: 'string' } },
      one_sentence_idea: { type: 'string' },
      concrete_instance: { type: 'string', description: 'the in-world numeric story that teaches it' },
      tempting_misconception: { type: 'string' },
      new_notation: { type: 'array', items: { type: 'string' }, description: 'glyphs introduced here, each with spoken name' },
      figure: { type: 'string', description: 'filename in assets/diagrams/ or "none"' },
    }, required: ['name', 'tier', 'one_sentence_idea', 'concrete_instance', 'tempting_misconception'] } },
    figures: { type: 'array', items: { type: 'object', properties: {
      filename: { type: 'string' }, describes: { type: 'string' },
    }, required: ['filename', 'describes'] } },
    problem_plan: { type: 'object', properties: {
      route_trainers: { type: 'integer' }, gym_battles: { type: 'integer' }, elite_challenge: { type: 'integer' },
    } },
    narrative_beats: { type: 'array', items: { type: 'string' } },
  },
  required: ['concepts', 'figures', 'problem_plan'],
}

const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['pass', 'revise'] },
    issues: { type: 'array', items: { type: 'object', properties: {
      severity: { type: 'string', enum: ['blocker', 'major', 'minor'] },
      checklist_item: { type: 'string', description: 'which Part-9 / AUDIT.md item' },
      where: { type: 'string' },
      detail: { type: 'string' },
      fix: { type: 'string' },
    }, required: ['severity', 'where', 'detail', 'fix'] } },
  },
  required: ['verdict', 'issues'],
}

// ---------------------------------------------------------------------------
phase('Blueprint')
const blueprint = await agent(
  `${SPEC}

Produce the BLUEPRINT for rebuilding the Bayes chapter to the v2 standard. Inventory every concept in
difficulty order, assign each a tier (A/B/C), and for each Tier-A/B concept give: the one-sentence idea
(Beat 1), the concrete in-world numeric instance that will teach it (Beat 2), the tempting misconception
to dismantle (Beat 4), and the new notation introduced (Beat 5, each glyph with its spoken name).
List the figures needed (Bayes table grid, probability tree, etc.) as filenames under assets/diagrams/.
Plan the problem counts to budget (~18-22, ~40/45/15 split). List the Cerulean/Misty narrative beats.
Return the structured blueprint.`,
  { label: 'blueprint', phase: 'Blueprint', schema: BLUEPRINT_SCHEMA }
)

// ---------------------------------------------------------------------------
phase('Build')
const [authorSummary] = await parallel([
  // Author the full chapter
  () => agent(
    `${SPEC}

BLUEPRINT: ${JSON.stringify(blueprint)}

Rewrite ${CH} COMPLETELY as a masterful teaching chapter. This replaces the Draft-1 version.

Hard requirements (graded against MASTER_PLAN_V2 Part 9 + the Cold-Read & Skip gates):
- Teaching-first skeleton (Part 3): Cold Open → "Where you are" + 60-second retrieval → Oak's Briefing
  with the chapter Test-Out gate → then FOR EACH concept in difficulty order: a "Do you already own this?"
  skip micro-check, then the full nine-beat Concept Lesson Arc, then the Pokédex Entry + Recognition Cue.
  Then faded worked examples (full→partial→independent; Tier-A first example is understanding-first /
  Professor's Path before Trainer's Path) → Trainer's Tips → Team Rocket's Trap → FROM KANTO TO THE REAL
  WORLD → the Gym Battle capstone → the Gym Challenge problem set → Answer Key → Badge Earned checklist.
- Assume NOTHING: every symbol introduced one glyph at a time, named and read aloud, by translating an
  English sentence into the symbol (Part 4). Concrete numbers BEFORE general notation, always.
- Derive every result (total probability, Bayes) from the concrete case — never assert it.
- Surface and dismantle the canonical misconception IN THE LESSON (the prosecutor's fallacy:
  P(clue|guilty) vs P(guilty|clue)); Team Rocket then re-commits it.
- Use the five fenced-div boxes (::: pokedex-entry / trainers-tip / team-rocket / kanto-realworld /
  cold-open). All math in \$...\$/\$\$...\$\$ using preamble macros; COMPLEX math in DISPLAY mode (\$\$),
  multi-step derivations aligned; never cramped inline fractions. Reference figures by the blueprint
  filenames as centered <figure> blocks with alt text. Iron Rule: math never over a sprite.
- TEXTBOOK-FORMAT the end matter: wrap the problem set in "::: problem-set" and the key in
  "::: answer-key" fenced divs; number problems C${N}.k; problems list first, full worked solutions after
  (never interleaved); each solution shows every step in display math with an archetype tag and a
  back-reference.
- Write all problems to ${PROBS} (overwrite) with full schema incl. a numeric \`verify:\` expression that
  uses the provided names (math, st) NOT __import__.
- Remove the "status: stub" marker.
Return a 1-paragraph summary of the concepts taught and how the nine-beat arc was applied.`,
    { label: 'author', phase: 'Build' }
  ),
  // Generate the chapter's figures from committed code (Part 8 reproducibility, Part 12 matplotlib theme)
  () => agent(
    `${SPEC}

BLUEPRINT figures: ${JSON.stringify(blueprint.figures)}

Write a committed matplotlib script figures/src/gen_ch04.py that generates each figure in the blueprint
(Bayes-table grid, probability tree, base-rate / false-positive visual) into assets/diagrams/ at 300 DPI
using figures/src/kanto_theme.mplstyle and the Kanto palette (red #EE1515, blue #3B4CCA, yellow #FFD733,
green #4DAD5B). Instructional clarity first: clean labels, legible at print size, color-blind-safe, and
readable in grayscale (use labels+patterns, not color alone). Run it and confirm the PNGs exist.
Return the list of files written.`,
    { label: 'figures', phase: 'Build' }
  ),
])

// ---------------------------------------------------------------------------
phase('Audit')
const audits = await parallel([
  // 1) Teaching quality (Part 9 teaching + Cold-Read test)
  () => agent(
    `${SPEC}\n\nAudit ${CH} for TEACHING QUALITY against MASTER_PLAN_V2 Part 9 (teaching) + Tier E of AUDIT.md.
    Check, skeptically, as if you knew none of this: does every Tier-A/B concept run all nine beats in order?
    one-sentence idea before any symbol? concrete instance before general notation? each result DERIVED not
    asserted? the misconception surfaced and dismantled in-lesson? difficulty ramp present? depth ∝
    difficulty×weight? Apply the COLD-READ TEST: could a true beginner learn each concept from this alone?
    And the SKIP TEST: is there a working test-out gate at chapter and concept level? Report findings.`,
    { label: 'audit:teaching', phase: 'Audit', schema: FINDINGS_SCHEMA }
  ),
  // 2) Notation + LaTeX + render
  () => agent(
    `${SPEC}\n\nAudit ${CH} for NOTATION-AS-LANGUAGE (Part 4) and LaTeX/RENDER quality. Run
    \`python3 tools/check_format.py\`. Verify: every symbol is introduced (named + read aloud + motivated)
    BEFORE its first use; no symbol used before introduction; complex expressions are in DISPLAY math (not
    cramped inline); multi-step derivations are aligned; no broken macros / stray \$ / raw TeX; the five box
    classes are used correctly and balanced; every <figure> references an existing asset with alt text.
    Flag any "say-it-aloud" gloss missing on a hard expression. Report findings.`,
    { label: 'audit:notation', phase: 'Audit', schema: FINDINGS_SCHEMA }
  ),
  // 3) Blind correctness (independent re-derivation)
  () => agent(
    `${SPEC}\n\nAudit ${CH} and ${PROBS} for CORRECTNESS by INDEPENDENT BLIND RE-DERIVATION. For each worked
    example and each problem, solve it yourself from the statement ALONE, WITHOUT reading the book's solution,
    then compare to the book's stated answer. Run \`python3 sims/verify_examples.py\` and
    \`python3 tools/check_coverage.py\`. Flag every disagreement with your own derivation and the correct
    answer. Also check invariants (probabilities in [0,1]; posterior + complement = 1; Bayes table rows
    normalize). Report findings (a disagreement is severity blocker).`,
    { label: 'audit:correctness', phase: 'Audit', schema: FINDINGS_SCHEMA }
  ),
  // 4) Immersion + visual + real-world
  () => agent(
    `${SPEC}\n\nAudit ${CH} for the NARRATIVE-IMMERSION (Part 13) and VISUAL/UX (Part 12) layers. Apply the
    Immersion Test (does it feel like progressing through Kanto with real stakes; are problems Ash's tasks?),
    the Transfer Test (can the reader state the real-world actuarial use — fraud detection / medical-test
    pricing — and solve a de-skinned version?), the fidelity rule (is the Cerulean mystery a faithful model
    of conditioning/Bayes?), and the Iron Rule (no math over sprites; equations on calm backgrounds). Check
    the FROM KANTO TO THE REAL WORLD box appears AFTER in-world understanding and names a concrete
    application. Report findings.`,
    { label: 'audit:immersion', phase: 'Audit', schema: FINDINGS_SCHEMA }
  ),
])

const allIssues = audits.filter(Boolean).flatMap(a => a.issues || [])
const blockers = allIssues.filter(i => i.severity === 'blocker')
const majors = allIssues.filter(i => i.severity === 'major')
log(`Audit: ${blockers.length} blockers, ${majors.length} majors, ${allIssues.length - blockers.length - majors.length} minor.`)

// ---------------------------------------------------------------------------
phase('Revise')
const reviseSummary = (allIssues.length === 0)
  ? 'No findings to apply.'
  : await agent(
      `${SPEC}\n\nApply fixes to ${CH} (and ${PROBS} if needed) for these audit findings, hardest first.
      Findings: ${JSON.stringify(allIssues)}
      Author summary: ${authorSummary}
      Fix every blocker and major; address minors where cheap. Preserve the nine-beat structure, the boxes,
      the textbook problem/solution formatting, and the verified answers. Keep the Iron Rule. After fixing,
      briefly confirm each blocker/major is resolved.`,
      { label: 'revise', phase: 'Revise' }
    )

// ---------------------------------------------------------------------------
phase('Gate')
const gate = await agent(
  `Run the integrity gates and report the final verdict for ${CH}:
  - \`python3 tools/check_format.py\`  (render/notation/structure; must PASS)
  - \`python3 sims/verify_examples.py\` (numeric answers; must PASS)
  - \`python3 tools/check_coverage.py\` (coverage; gaps OK, structural errors not)
  Then give a one-paragraph masterful-checklist verdict: are the Cold-Read and Skip gates met, and is this
  chapter ready to be the gold-standard reference? List any remaining blockers/majors by name.
  Return your report as text.`,
  { label: 'gate', phase: 'Gate' }
)

return {
  blueprint_concepts: (blueprint.concepts || []).map(c => ({ name: c.name, tier: c.tier })),
  audit: { blockers: blockers.length, majors: majors.length, total: allIssues.length },
  revised: reviseSummary !== 'No findings to apply.',
  gate_report: gate,
}
