<!--
  V3 CHAPTER TEMPLATE — fill every section. Skeleton = MASTER_PLAN_V3 §6.
  GOLDEN RULES (from the ch02 exemplar, graded A):
   • NO CONCEPT COMPRESSION (§7): every concept runs the full nine-beat arc with a
     REAL derivation (never asserted). Length flexes to the concept; never trim to fit.
   • Calculator key-caps: write [2nd]{.kbd} and [ ... ]{.keystroke} as BARE markdown —
     NEVER inside backticks (backticks make pandoc render them as literal text).
   • WATCH-ALONGSIDE (§29): include a ::: now-playing box (Indigo-League episode tie-in)
     after Where You Are; weave the cold-open/beats to track that episode; label any
     embellishment as an in-world extension. Use the locked §29 episode map.
   • VISUAL IMMERSION 10/10 (§30, rubric dim 12 must be >=9): visuals are a primary
     immersion channel. HARD RULE: never generate/draw sprite/character/badge art —
     use REAL online assets only (assets/... from PokeAPI/pret/Showdown); you may only
     GENERATE math figures (which may composite real sprites). Embed, all inline
     <figure><img ... alt> with real alt text:
       - concept figures (>=1 per spatial/multi-step concept) via figures/src/gen_chNN.py;
       - CAST portraits at their beats (Oak @ Briefing; gym leader @ Gym Battle; Team Rocket
         @ Trap; Gary @ rival-trap) from assets/characters|vs/;
       - MASCOT sprites making the RV concrete from assets/sprites/front|official/
         (margins only, via place_sprite — IRON RULE: never over a curve/equation/axis);
       - the earned badge @ Badge Earned (assets/badges/); item glyphs where natural.
     A Tier-A chapter that renders as a wall of text with one figure FAILS.
   • Answer section heading is exactly "## Answers".
   • Drills = one escalating QUESTLINE (§28): commission -> Route legs -> Gym-Battle boss
     -> Elite post-game; quotas: audit >=3, rival_trap >=2, decision >=1; recycle the
     chapter's Team Rocket error into >=1 drill; every problem has actor/stakes/consequence
     and a self-contained verify: in problems/bank.d/chNN.yaml.
  metadata: file=chNN_slug · tier=A|B|C · outcomes=... · tia=... · locale=... · type=...
-->

# {Chapter Title} {.type-{type}}

::: cold-open
**▶ COLD OPEN — EPISODE: "{title}"**

{Second-person, present-tense scene that IS the chapter's core problem in disguise; ends on a question you can't yet answer.}
:::

## Where You Are — 60-Second Retrieval
{Retrieve the prior chapter's load-bearing idea; name the Trainer Rank + badges held; 3 instant-check questions.}

::: now-playing
**📺 NOW PLAYING — Indigo League {EP0xx "title"}**  {1–2 lines: what happens this episode + how it sets up the chapter's math; "watch before/after this chapter." Reference only on-screen events; label embellishments.}
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate
{Outcomes discharged (tag SOA ids) + exam-weight signpost + a Test-Out Gate (timed problems with answers).}

## Concept 1 — {name}
::: concept-gate
**DO YOU ALREADY OWN THIS? — {name}**  {micro skip-check + the discriminating wrong answer}
:::
{Nine beats: 1 one-sentence idea · 2 concrete instance · 3 reason in words · 4 dismantle the tempting wrong idea · 5 notation one glyph at a time (read aloud) · 6 DERIVE the formula · 7 ramp (simple→twist→general→edge) · 8 figure/table · 9 consolidate.}
::: pokedex-entry
**POKÉDEX ENTRY №01 — {name}**  {formula · plain meaning · recognition cue}
:::

<!-- repeat Concept blocks in difficulty order; one idea each; no compression -->

## Worked Examples — Faded Guidance
### Example 1 — {fully narrated: Professor's Path then Trainer's Path; identify→setup→solve→check}
### Example 2 — {partially guided}
<!-- more as needed -->

## Trainer's Tips
::: trainers-tip
**TRAINER'S TIP — {name}**  {exam craft; calculator path with [..]{.kbd}/[..]{.keystroke} if scheduled}
:::

## Team Rocket's Trap
::: team-rocket
**TEAM ROCKET'S TRAP**  {Jessie/James/Meowth commit the canonical error in-character; one-line fix}
:::

## From Kanto to the Real World
::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**  {named actuarial application + a "Series bridge" line}
:::

## The Gym Battle — {Badge} Capstone
{The chapter's hardest problem at exam difficulty, framed as the leader's challenge, solved completely.}

## The Gym Challenge — Problem Set
::: problem-set
{Route Trainers (mechanics) → Gym Battles (true SOA) → Elite Challenge (integrative). Each numbered CN.k, archetype-tagged; mirrors problems/bank.d/chNN.yaml.}
:::

## Answers
### Quick-Answer Table
{table: problem | answer | archetype}
{Full worked solutions, archetype-labeled, back-referenced to the Pokédex Entry + shortcut used.}

## Badge Earned — the {Badge} Badge
{3–6 can-do statements mapped 1-to-1 to the outcomes; "Gym Rematch" pointers back to sections.}
