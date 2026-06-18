export const meta = {
  name: 'workbook-autosize',
  description: 'Auto-size the dot-grid work area for every problem from its solution complexity, then QA the white-space formatting and rebuild',
  whenToUse: 'After the deterministic workbook build works; gives true per-problem sizing + a formatting QA pass.',
  phases: [
    { title: 'Size',    detail: 'per chapter: judge each problem\'s work-space size from its worked solution' },
    { title: 'Build',   detail: 'merge sizes, rebuild workbook + textbook' },
    { title: 'QA',      detail: 'per chapter: render workbook pages, verify clean white space, patch sizes' },
    { title: 'Rebuild', detail: 'merge QA patches, final workbook build' },
  ],
}

// chapters that contain a ::: problem-set (file -> CN prefix number)
const CH = [
  ['ch00_orientation',0],['ch01_toolkit_numbers',1],['ch02_toolkit_calculus',2],
  ['ch03_outcomes',3],['ch04_counting',4],['ch05_bayes',5],['ch05x_checkpoint_a',5],
  ['ch06_random_variables',6],['ch07_center_spread',7],['ch08_discrete',8],
  ['ch09_continuous',9],['ch10_pricing',10],['ch10x_checkpoint_b',10],['ch11_joint',11],
  ['ch12_double_expectation',12],['ch13_covariance',13],['ch14_order_clt',14],['ch15_champion',15],
]

const SIZING = `
Size key (height of the dot-grid work area to leave for handwriting the FULL solution):
  sm = 3.5cm  (~6 dot-rows): a one-step answer — a single formula plug-in, a definition, a quick lookup.
  md = 7cm    (~13 rows): a few steps — set up, substitute, simplify (most Gym-Battle mechanics).
  lg = 12cm   (~22 rows): multi-step — a derivation, an integral with setup, a Bayes table, a deductible/variance computation.
  xl = 19cm   (~full page): integrative / Elite-tier / any mock-exam question / anything needing a diagram (Venn, tree, region) plus work.
Judge each problem by the LENGTH AND COMPLEXITY OF ITS OWN WORKED SOLUTION in the Answer Key (read it!),
not by tier alone. A "Route Trainer" with a real computation may deserve md; an Elite proof deserves xl.
`.trim()

// ---- Size: one agent per chapter, writes workbook/sizes/<num>.json ----
phase('Size')
await parallel(CH.map(([file, num]) => () => agent(
  `Open book/chapters/${file}.md. It has a ::: problem-set (problems C${num}.k) and a ::: answer-key
  (full worked solutions). For EVERY problem in the problem-set, read its matching worked solution and
  decide how much blank work space a student needs to solve it by hand.
  ${SIZING}
  Write a JSON object mapping every problem id to its size to workbook/sizes/ch${String(num).padStart(2,'0')}_${file}.json,
  e.g. {"C${num}.1":"sm","C${num}.2":"lg", ...}. Cover every problem in this chapter's problem-set. Mock-exam
  questions (ch15) are all lg or xl. Return the count you sized.`,
  { label: `size:${file.slice(0,5)}`, phase: 'Size' })))

// ---- Build: merge + rebuild ----
phase('Build')
await agent(
  `Merge every workbook/sizes/*.json file into a single workbook/workspace_sizes.json (one flat object of
  all problem-id -> size entries; later files override earlier on collision). Use python3. Then run
  \`make workbook\` and \`make book\`. Confirm both PDFs build and report build/output/*.pdf page counts and
  that \`python3 tools/check_format.py\` still PASSES. Return the summary.`,
  { label: 'build', phase: 'Build' })

// ---- QA: per chapter, render workbook pages, verify white-space formatting ----
phase('QA')
const qa = await parallel(CH.map(([file, num]) => () => agent(
  `QA the WORKBOOK white-space formatting for ${file} (C${num}.k problems) in
  build/output/kanto_journey_workbook.pdf. Find this chapter's "The Gym Challenge" pages (search the PDF text
  for a distinctive problem statement) and visually inspect 2-3 of them with the Read tool. Verify:
  - every problem is immediately followed by a labelled "Work — C${num}.k" dot-grid area (no problem missing space),
  - the space SIZE fits the problem's difficulty (not cramped for hard ones, not a wasteful full page for a one-liner),
  - clean formatting: no problem orphaned from its work area across a page break, no huge empty gaps, the dot grid renders.
  If any work area is mis-sized, EDIT workbook/sizes/ch${String(num).padStart(2,'0')}_${file}.json to fix just those
  ids (sm/md/lg/xl). Return PATCHED if you changed sizes, else OK, with a one-line note.`,
  { label: `qa:${file.slice(0,5)}`, phase: 'QA' })))

const patched = qa.filter(r => r && /PATCHED/i.test(r)).length

// ---- Rebuild only if QA patched sizes ----
phase('Rebuild')
if (patched > 0) {
  await agent(
    `QA adjusted ${patched} chapters' work-space sizes. Re-merge workbook/sizes/*.json into
    workbook/workspace_sizes.json and run \`make workbook\`. Confirm the PDF rebuilt and report the page count.`,
    { label: 'rebuild', phase: 'Rebuild' })
} else {
  log('QA found no size changes needed; workbook is final.')
}

return { chapters_sized: CH.length, qa_patched: patched }
