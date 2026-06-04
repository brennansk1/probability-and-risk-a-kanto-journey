export const meta = {
  name: 'v2-figures',
  description: 'Generate the remaining missing math figures (committed matplotlib scripts) for ch00/02/04/06/07/08/10',
  whenToUse: 'Final production gap: 32 instructional diagrams referenced by chapters but never generated.',
  phases: [{ title: 'Figures', detail: 'one agent per chapter generates its referenced diagrams' }],
}

const CHAPTERS = [
  'ch00_orientation', 'ch02_toolkit_calculus', 'ch04_counting',
  'ch06_random_variables', 'ch07_center_spread', 'ch08_discrete', 'ch10_pricing',
]

phase('Figures')
const results = await parallel(CHAPTERS.map(file => () => agent(
  `Generate the missing MATH figures for book/chapters/${file}.md.

  Step 1: list the diagrams it references and which are missing —
    grep -oE 'assets/diagrams/[a-zA-Z0-9_]+\\.png' book/chapters/${file}.md | sort -u
    then check which do NOT exist under assets/diagrams/.
  Step 2: for EACH missing file, read its <figure> caption and the surrounding passage so the plot
    actually depicts what the text describes (e.g. a function machine, a summation's anatomy, a pmf bar
    chart, a pdf area, a cdf staircase, a payment-vs-loss step graph, a survival-area integral, etc.).
  Step 3: write ONE committed script figures/src/gen_${file.slice(0,4)}.py that produces EXACTLY those
    filenames into assets/diagrams/. Use matplotlib with figures/src/kanto_theme.mplstyle, 300 DPI, the
    Kanto palette (red #EE1515, blue #3B4CCA, yellow #FFD733, green #4DAD5B), clean legible labels,
    color-blind-safe and readable in grayscale (use labels/patterns, not color alone). These are
    INSTRUCTIONAL diagrams — clarity over decoration; NO Pokemon art (sprites are repo-sourced separately).
  Step 4: run the script and confirm every referenced PNG now exists (ls them).
  Return the list of files written.`,
  { label: `fig:${file.slice(0,4)}`, phase: 'Figures' })))

log(`Figure agents returned: ${results.filter(Boolean).length}/${CHAPTERS.length}`)
return { done: results.filter(Boolean).length }
