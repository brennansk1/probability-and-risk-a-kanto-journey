export const meta = {
  name: 'figures-audit-and-sprites',
  description: 'Per-chapter: audit every figure for correctness/clarity, integrate Pokémon sprites/items into figures where they teach, add sprites to prose gaps; then rebuild both PDFs and QA',
  whenToUse: 'Figure-quality audit + sprite enrichment pass over the whole book.',
  phases: [
    { title: 'Enrich', detail: 'per chapter: fix figures + composite sprites/items + add prose sprites' },
    { title: 'Build',  detail: 'regenerate all figures, rebuild textbook + workbook, gates' },
    { title: 'QA',     detail: 'render samples, verify figures correct and sprites integrated cleanly' },
  ],
}

const IRON = `
THE IRON RULE: art decorates, it NEVER obscures the math. Place sprites in margins, atop bars,
beside labels, or in region corners — never over a curve, equation, number, or axis the reader must
read. Keep them small (zoom ~0.3-0.6 for front sprites) and use alpha<1 where they sit near data.
Sprites are illustrative, not load-bearing: the figure must still teach perfectly in grayscale with
every sprite removed.`.trim()

const ASSETS = `
Available art (import helpers from figures/src/sprite_util.py — front(dex), official(dex), item(name),
place_sprite(ax, path, xy, zoom=, xycoords=, alpha=)):
- front(1..151): 96px Gen-1 pixel sprites — best for in-figure use (Pidgey=16/17/18, Pikachu=25, Rattata=19,
  Gastly=92, Magikarp=129, Caterpie=10, Oddish=43, Onix=95, Chansey=113, Kangaskhan=115, Scyther=123, ...).
- item(name): poke-ball, great-ball, ultra-ball, master-ball, safari-ball, premier-ball, potion,
  super-potion, hyper-potion, max-potion, full-restore, revive, rare-candy, antidote, thunder-stone, ...
- official(1..151): high-res official artwork (for large/header placements only).
Pick species/items that fit the chapter's narrative (e.g. Safari Zone -> safari-ball on ch10's loss graph;
the haunted tower -> Gastly on ch08's Poisson pmf; Koga -> antidote/poison mons).`.trim()

// chapter -> {gen: generator script or "" if none, prefix for figure refs}
const CH = [
  { f:'ch00_orientation',        gen:'figures/src/gen_ch00.py' },
  { f:'ch01_toolkit_numbers',    gen:'' },                         // no figures: prose sprites only
  { f:'ch02_toolkit_calculus',   gen:'figures/src/gen_ch02.py' },
  { f:'ch03_outcomes',           gen:'figures/src/generate_figures.py' }, // edit only fig_ch03_* funcs
  { f:'ch04_counting',           gen:'figures/src/gen_ch04.py' },
  { f:'ch05_bayes',              gen:'figures/src/gen_ch05.py' },
  { f:'ch05x_checkpoint_a',      gen:'' },
  { f:'ch06_random_variables',   gen:'figures/src/gen_ch06.py' },
  { f:'ch07_center_spread',      gen:'figures/src/gen_ch07.py' },
  { f:'ch08_discrete',           gen:'figures/src/gen_ch08.py' },
  { f:'ch09_continuous',         gen:'figures/src/gen_ch09.py' },
  { f:'ch10_pricing',            gen:'figures/src/gen_ch10.py' },
  { f:'ch10x_checkpoint_b',      gen:'' },
  { f:'ch11_joint',              gen:'figures/src/gen_ch11.py' },
  { f:'ch12_double_expectation', gen:'figures/src/gen_ch12.py' },
  { f:'ch13_covariance',         gen:'figures/src/gen_ch13.py' },
  { f:'ch14_order_clt',          gen:'figures/src/gen_ch14.py' },
  { f:'ch15_champion',           gen:'figures/src/gen_ch15.py' },
]

phase('Enrich')
const enrich = await parallel(CH.map(ch => () => agent(
  `You own ONE chapter: book/chapters/${ch.f}.md${ch.gen ? ` and its figure generator ${ch.gen}` : ' (this chapter has no generated figures)'}.
Do three things, then regenerate.

${ch.gen ? `(A) AUDIT EVERY FIGURE this chapter references. For each <figure> in ${ch.f}.md that points to
assets/diagrams/*.png: VIEW the PNG (Read tool) and read its caption + the surrounding passage. Verify it
is CORRECT (matches the math and the caption), CLEAR (labels legible, nothing cut off or overlapping,
axes/units right), and print-quality (300 DPI, readable in grayscale). Fix any defects in ${ch.gen}.
If a referenced figure has NO function in ${ch.gen} (e.g. it was generated ad-hoc and isn't reproducible),
ADD a function that regenerates it. ${ch.f.startsWith('ch03') ? 'Edit ONLY the fig_ch03_* functions in this shared file.' : ''}

(B) INTEGRATE SPRITES/ITEMS into this chapter's figures where it genuinely helps comprehension or ties the
math to the story — e.g. a species sprite atop a pmf bar, mons inside Venn circles, an item on a loss/payment
graph. ${IRON}
${ASSETS}
` : ''}
(C) ADD PROSE SPRITES to ${ch.f}.md where there are gaps: if the chapter has no header sprite/character, add
one; beside worked examples / problems that NAME a specific Pokémon or item, add a small centered <figure>
(use the exact <figure> HTML style already used elsewhere in the book: front sprite path
../../assets/sprites/front/<dex>.png, image-rendering:pixelated, alt text, caption). Items live at
../../assets/items/<name>.png. Don't overdo it — one tasteful sprite per major example, never over math.

${ch.gen ? `Finally run \`python3 ${ch.gen}\` and confirm it completes and the PNGs are written.` : ''}
Return a short summary: figures audited, defects fixed, sprites/items added (figures + prose).`,
  { label: ch.f.slice(0,5), phase: 'Enrich' })))

log(`Enrich done: ${enrich.filter(Boolean).length}/${CH.length} chapters.`)

phase('Build')
await agent(
  `Regenerate and rebuild everything, reporting results:
  1. \`make figures\` — regenerate all diagrams (must complete with no Python error; if a gen script errors,
     read it and fix the error, e.g. unsupported mathtext like \\tfrac/\\dfrac/\\! -> use \\frac and drop \\!).
  2. \`python3 tools/check_format.py\` — every referenced figure must exist; 0 errors.
  3. \`make book\` (textbook) and \`make workbook\` — both PDFs must build.
  Report: figures count, format result, and both PDF page counts.`,
  { label: 'build', phase: 'Build' })

phase('QA')
const qa = await parallel(CH.filter(c => c.gen).map(ch => () => agent(
  `QA chapter ${ch.f} in build/output/kanto_journey.pdf. Find 1-2 of its figure pages (search the PDF text
  for a figure caption) and VIEW them. Confirm: figures render correctly, integrated sprites/items look clean
  and DON'T obscure any math (Iron Rule), captions still match. If a sprite overlaps data or a figure looks
  wrong, fix ${ch.gen} and re-run it. Return OK or FIXED with a one-line note.`,
  { label: `qa:${ch.f.slice(0,5)}`, phase: 'QA' })))

const fixed = qa.filter(r => r && /FIXED/i.test(r)).length
if (fixed > 0) {
  await agent(`QA fixed ${fixed} chapters' figures. Re-run \`make figures\`, then \`make book\` and
    \`make workbook\`. Confirm both rebuild and report page counts.`, { label: 'rebuild', phase: 'QA' })
} else {
  log('QA: no figure fixes needed after enrichment.')
}

return { chapters: CH.length, enriched: enrich.filter(Boolean).length, qa_fixed: fixed }
