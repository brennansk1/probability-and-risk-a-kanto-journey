<!--
  file: ch00_orientation
  tier: front-matter
  outcomes: orientation
  tia: front matter (precedes A.1.1)
  locale: Pallet Town (Oak's lab)
  type: normal
  maps_to: Pallet Town — Oak issues the Pokedex (Actuary Mode) + the TI-30XS; the dual quest begins
  episode: EP001 "Pokemon! I Choose You!"
-->

# Orientation — The Dual Quest, the Gear, and How to Read the Journey {.type-normal}

<figure>
<img src="../../assets/diagrams/ch00_journey_map.png" alt="The eight-badge road from Pallet Town to the Indigo Plateau drawn as a horizontal progress bar. Ten labeled stops run left to right: Pallet Town (you are here), Cerulean/Misty (Cascade, ch02), S.S. Anne/Lt. Surge (Thunder, ch03), Pewter/Brock (Boulder, ch04), Celadon/Erika (Rainbow, ch05), Fuchsia/Koga (Soul, ch06), Saffron/Sabrina (Marsh, ch09), Cinnabar/Blaine (Volcano, ch14), Viridian/Giovanni (Earth, ch16), and the Indigo Plateau marked EXAM P (ch19). A real Pikachu sprite stands at the start labeled 'your partner.'" style="width:88%; max-width:760px; display:block; margin:1em auto;">
<figcaption>The whole book on one map: eight badges are eight chunks of the Exam P syllabus, and the Indigo Plateau at the road's end <em>is</em> the exam. You start at Pallet Town with a Trainer Rank of Rookie and zero badges. (Stops are ordered to the math, not to canon — see "The Journey Convention" below.)</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "I Choose You!"**

It is the night before you leave Pallet Town. You are ten years old, you cannot sleep, and tomorrow you walk out the door to begin a journey every trainer in Kanto dreams of: catch and raise Pokémon, challenge the eight Gym Leaders, earn their badges, and climb the road north to the **Indigo Plateau** — the championship.

But Professor Oak's lab is still lit. When you knock, the old Professor is waiting, and he tells you the journey is not the one you think. "Anyone can collect badges, Ash," he says. "I am sending you after something harder. You will become a Pokémon Master — *and* you will become an **actuary**: someone who can put an honest number on the risks a trainer faces. A wild encounter, a coin-flip slot machine, a sinking ship, a deductible on a Safari Ball — all of it is *probability*, and probability can be *measured*."

He hands you two things. The first is the **Pokédex** — but this one has a new setting, **Actuary Mode**, that does not just scan Pokémon: it poses you problems, the same kind the Society of Actuaries asks on **Exam P**, the probability exam that stands at the far end of the map like a final, invisible Gym Leader. The second is a small, sturdy calculator — a **TI-30XS MultiView** — "standard-issue gear," Oak says, "as essential as your Poké Balls. Learn to drive it before you need it."

You flip the field guide — *this book* — open to a page deep in the journey, and a line of symbols stares back:

$$\E[X] \;=\; \sum_{k} k\,P(X = k).$$

You don't recognize a single piece of it. But Oak only smiles. "You will read that aloud as easily as a sentence — soon. Tonight you don't learn probability. Tonight you learn **how to use the guide**, **how to read the symbols**, and **how to hold the calculator.** Then you sleep, and tomorrow the road begins."

*This chapter is that night. It is not a lesson with a badge at the end — it is the orientation that makes every lesson after it land.*
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP001 "Pokémon! I Choose You!"**

<figure><img src="../../assets/stills/ch00_now_playing.jpg" alt="Pikachu — the partner Ash receives in Indigo League EP001." style="width:58%; max-width:420px; display:block; margin:0.4em auto;"><figcaption style="font-size:0.8em; color:#555;">EP001 — meet your partner; the journey begins.</figcaption></figure>

The very first episode. Ash oversleeps on the morning of his journey, races to Professor Oak's lab, and — the starters already taken — receives an unruly **Pikachu** who wants nothing to do with him or its Poké Ball. By the episode's end, attacked by a flock of Spearow, Ash shields Pikachu with his own body, and Pikachu chooses to fight for him: the bond that carries the whole series is forged. *Our cold-open borrows that same lab-doorstep moment* — Oak handing over the Pokédex — and extends it: in this telling the Pokédex carries "Actuary Mode" and Oak issues a calculator too (an in-world extension for the book's dual quest, not an on-screen line). **Watch EP001 before you start** — it is the launch of the journey you are about to read.
:::

## Where You Are — the Only Thing This Book Assumes

Every *other* chapter opens by having you retrieve the load-bearing idea from the chapter before — learning sticks when you pull it back out of memory yourself. This is the **first** thing in the book, so there is nothing behind you to retrieve. Instead, here is the one thing this book genuinely assumes you bring: **comfortable grade-school arithmetic.** Not algebra, not calculus, not "math-class trauma." Just arithmetic. Everything else is built from the ground up where it is needed (calculus gets its own toolkit chapter at the start of Act II).

::: trainers-tip
**60-SECOND READINESS CHECK — the only prerequisite**

Do these in your head or on scratch paper. If all four feel routine, you have everything you need to set out.

1. What is $\dfrac{3}{4}$ as a decimal? *(Answer: $0.75$.)*
2. What is $0.2 \times 0.5$? *(Answer: $0.10$.)*
3. What is $\dfrac{12}{30}$ reduced, and as a decimal? *(Answer: $\dfrac{2}{5} = 0.4$.)*
4. What is $1 - 0.35$? *(Answer: $0.65$.)*

All four routine? You are ready — and more ready than you think. Any of them shaky? Don't worry and don't skip: this book fills every gap out loud, and a half hour with the calculator you're about to meet restores the arithmetic. That is a promise — and the rest of this chapter is how the book keeps it.
:::

## Oak's Briefing — The Dual Quest & the Two Promises

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer, who issues your Pokédex and calculator and guides every definition.</figcaption>
</figure>

Oak sits you down at the lab door. "Before you carry the guide onto the road, let me tell you what it is and how it works."

**The premise — you are Ash, and the quest is double.** You leave Pallet Town to become a Pokémon Master, but Oak's charge is to *also* become an actuary. The two quests share one map:

- **Eight badges = the syllabus.** Each Gym you clear corresponds to a chunk of Exam P. Earn all eight and you have covered the whole exam, concept for concept. The journey map above shows them.
- **The Indigo Plateau = the exam.** The championship at the road's end *is* Exam P. The finale (`ch19`) is the sitting itself.
- **The Pokédex poses the problems.** Its **Actuary Mode** is the voice that hands you each chapter's problem — scan a Pokémon, get a risk question. Every worked example and drill is the Pokédex doing its job.

"Now," Oak says, "the guide makes you **two promises** — they sound like opposites until you see how they fit."

> **Promise 1 — No gaps.** *You will never need an outside source to understand a concept in this book.* Every idea is built from the ground up; every symbol is named the first time it appears. Assume you know nothing beyond arithmetic, and the book fills in the rest — out loud, step by step, never "it is obvious that."

> **Promise 2 — No wasted time.** *You will never be forced to read what you already know.* The moment a concept begins, there is a short **skip-gate** — a quick check. Pass it and you jump straight to the practice and the badge. Hesitate, and the full teaching is right there, built for you.

"Those two promises," Oak says, "are why the guide works for the trainer who has never seen probability *and* the one reviewing for a perfect score — at the same time. Nobody is bored; nobody is lost."

By the end of this orientation you will be able to:

- **Navigate** the book — its colored boxes, its skip-gates, its nine-beat lessons, its tiered problem sets — so you always know where the help is. *(Orientation.)*
- **State the exam facts** — the shape of Exam P, what it provides, and what it does not — so the target is concrete from day one. *(Orientation.)*
- **Drive the TI-30XS MultiView** for setup — modes, clear-before-each-problem, the seven memory slots and `STO▸`, the fraction toggle `F◂▸D`, and order of operations. *(The Trainer's-Calculator primer.)*
- **Read aloud** the core notation this book uses — variables vs. values, the bar $\mid$ ("given"), the sum $\sum$ and its cousin $\int$, set membership $\in$, and operators like $P(\cdot)$ and $\E[\cdot]$. *(The Reading-the-Symbols primer.)*

> *Where this sits.* This is **front matter**, worth **zero** exam points directly — yet it is the highest-leverage half hour in the book, because every later chapter is written in this notation and solved on this calculator. Spend it once now, slowly.

::: concept-gate
**ORIENTATION TEST-OUT — Are You Already Oriented?**

Three quick checks. If all three are instant and correct, you may **skip to the Trainer Rank ladder** and start Chapter 1 — but most readers gain real time from the calculator primer below even if they know the rest.

1. **Read this line aloud, in plain English:** $\displaystyle P\!\left(X = 3 \mid N = 5\right) = \sum_{i=1}^{4} p_i.$
   *(Target: "the probability that the variable $X$ equals 3, given that $N$ equals 5, equals the sum, as $i$ runs from 1 to 4, of $p_i$.")*
2. **Name the job of each book box:** a blue **Pokédex Entry**, a yellow **Trainer's Tip**, a red **Team Rocket's Trap**, a green **From Kanto to the Real World**, a purple **Now Playing**, a grey **Beyond the Syllabus** (enrichment), and a **Concept Gate**.
3. **On the TI-30XS, what does `[STO▸]` do, and why use it?** *(Target: it stores a computed value into a memory slot so you re-use it instead of re-typing — which kills rounding drift.)*

All three instant? You're oriented. Any hesitation? The sections below were written for you — and each is independent, so read only the ones you need.
:::

---

This chapter has four short parts, none of them a probability lesson:

1. **How to use the book** — the panels, the gates, the nine-beat arc, the questline.
2. **The exam facts** — what Exam P actually is.
3. **The journey convention + the Trainer Rank ladder** — how progress works.
4. **The Trainer's Calculator** — TI-30XS setup — and **Reading the Symbols** — the notation primer.

## Part 1 — How to Use This Book

This book is a Pokémon journey that happens to be a probability textbook. Like any game, it has a small set of repeating panels, each with one job. Learn them once and you will always know — at a glance — whether the box in front of you is teaching, warning, summarizing, or letting you skip.

**The Iron Rule first.** Wherever real mathematics lives — a formula, a derivation, a solution — it is printed in clean, high-contrast type on a calm background, never crowded by a sprite or a map. The Pokémon art owns the *frame and the feeling*; the math owns the *content*; they never fight for the same space. A test you can apply to any page: *cover every sprite, badge, and map with your hand — can you still learn the math perfectly?* The answer here is always yes.

**The box legend** (each box carries an icon and a label, so its meaning survives grayscale printing):

::: pokedex-entry
**POKÉDEX ENTRY — the blue device screen.** The *keeper* box. When a concept is fully taught, its formula, its one-line "what it means," and a *recognition cue* ("when you see ___, reach for this") are sealed here. These are what you carry into the exam. Want a chapter's compressed summary? Read its Pokédex Entries.
:::

::: trainers-tip
**TRAINER'S TIP — the yellow item callout.** Exam craft: a calculator keystroke, a pacing trick, a fast way to recognize a problem's type. The teaching tells you *why*; the Trainer's Tip tells you *how to be fast*. Calculator skills live here, with key-caps like [2nd]{.kbd} [prb]{.kbd}.
:::

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap (the red box).** Jessie, James, and Meowth attempt the problem and confidently make the *single most tempting wrong move* — the mistake the exam is built to catch. Their scheme fails, the error is named, you get a one-line guardrail. The error they make is the error you were about to make.
:::

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD — the green field journal.** After a concept is understood in-world, this box shows the *real* actuarial job it does: Bayes prices medical tests; deductibles set your auto premium; the Central Limit Theorem is why insurance pooling works. It is the bridge to the career the exam unlocks — and a transfer check that the same problem with *no Pokémon in it* is one you can now solve.
:::

::: now-playing
**📺 NOW PLAYING — the purple watch-alongside box.** This book is built so you can watch the *Indigo League* anime alongside it. Each chapter's Now-Playing box names the episode(s) its story tracks, what happens in them, and a "watch before/after" cue. The show is the hook; the math is the cargo; the real world is the payoff. (Where the book extends canon, it says so — never claiming a scene is on screen when it isn't.)
:::

::: enrichment
**BEYOND THE SYLLABUS — the grey enrichment box.** Occasionally a topic (Pareto tails, the lognormal) is taught because the full course covers it, but it sits *off* the Exam P syllabus. These boxes are clearly labeled "for the curious / future exams," are **never** behind a gate, never on a mastery checklist, and never required. Read them if you want depth; skip them with a clear conscience if you want focus.
:::

::: concept-gate
**CONCEPT GATE — "Do you already own this?" (the Poké Center heal-or-proceed panel).** At the top of every chapter and every major concept. A short, honest check. Pass it *with the right method* and you skip ahead. Hesitate, and the full lesson is immediately below. This panel is how the book keeps Promise 2.
:::

**The two gates, as a habit.** The **Chapter Test-Out Gate** (top of each chapter) lets a fluent reviewer skip an *entire* chapter. The **Concept Gate** (top of each concept) lets a partial owner skip *just the pieces they already have*. You can fail the chapter gate, pass three of five concept gates, and read only the two concepts you actually need. That is the whole point.

**The nine-beat lesson arc.** When a concept *isn't* skipped, the book teaches it the same careful way every time — never "here's the formula, good luck." Each lesson walks nine short beats: (1) the idea in one plain sentence, before any symbol; (2) a concrete instance from the journey, with real numbers; (3) reasoning through it in plain words; (4) surfacing and dismantling the *tempting wrong idea*; (5) translating into notation **one glyph at a time**; (6) deriving the formula from the instance; (7) ramping the difficulty (simple → twist → general → edge); (8) a picture or table; (9) consolidating into a Pokédex Entry. You don't memorize this list — you'll feel the rhythm by Act I's end. Just know the help is always there, in that order, and the formula is the *destination*, never the starting gun.

**The problem set is a questline, not a worksheet.** Each chapter's problems form **one connected mission**. A *commissioner* (a Gym Leader, Oak, Nurse Joy, the Safari Warden) opens with a goal and a stake; the **Route Trainers** tier is the early legs (scouting, cataloguing, skirmishes), lightly scaffolded; the **Gym Battle** tier is the literal **boss fight** — the chapter's hardest problem at full exam speed; the **Elite Challenge** tier is the optional post-game. Clearing the questline *earns the badge*. Some problems carry recurring cast: **Team Rocket** mis-records a value for you to *audit* and correct; **Gary** claims an answer for you to *check*. Every problem has a full worked solution in the **Answer Key** that follows — problems first, all solutions after, never interleaved, so you can struggle honestly before you peek.

That is the furniture. Now the facts, the progress system, and the gear.

## Part 2 — The Exam Facts

Oak pulls up the target on the Pokédex screen. "Know exactly what waits at the Plateau, Ash. A trainer who knows the rules of the battle never panics in it."

**Exam P at a glance:**

| What | The fact |
|---|---|
| **Length** | **3 hours.** |
| **Questions** | **30** multiple-choice, five options (A–E), exactly one correct. |
| **Scoring** | Scored **0–10**; a **6 or higher passes.** (Roughly 60% correct is the usual landmark.) |
| **Guessing** | **No penalty for a wrong answer.** Never leave a question blank — a guess can only help. |
| **Provided** | A **standard normal distribution table** is given on screen. You do **not** memorize it. |
| **Calculator** | The **TI-30XS MultiView** (the machine this book teaches) is permitted. Bring **two**, both memory-cleared. |
| **Format** | Computer-based (CBT) at a Prometric center; you may write on provided scratch paper. |

::: trainers-tip
**TRAINER'S TIP — the two facts that change how you sit the exam**

(1) **No penalty for guessing** means your last act on every question is to *select an answer*, even a blind one — 30 answered beats 28 answered and 2 blank, always. (2) **Six minutes per question** on average (180 minutes ÷ 30). That budget is why the calculator fluency in Part 4 matters: every keystroke you save is a question you don't run out of time on. The finale chapter (`ch19`) drills both under timed mock exams.
:::

**Where the points live.** Exam P weights its three topics — and so does this book's problem count:

- **General Probability** — about **23–30%** (Act I's openings: sets, conditional probability, Bayes).
- **Univariate Random Variables** — about **44–50%**, the single largest slice (most of Acts I and II: distributions, moments, deductibles, the Normal).
- **Multivariate Random Variables** — about **23–30%** (Act III: joint distributions, covariance, conditional expectation, order statistics).

You don't act on these percentages now; they're the reason later chapters spend the most pages where the exam spends the most points.

## Part 3 — The Journey Convention & the Trainer Rank Ladder

**The journey convention — badges sequenced to the math.** This book follows the *Indigo League* anime's characters, locales, and major arcs faithfully, but it **orders the Gym challenges to honor the mathematical dependency chain, not the show's catch-order.** Conditional probability has to come before counting (you reason from evidence before you enumerate), so you meet **Misty's** Cerulean gym *before* **Brock's** Pewter gym — the reverse of canon. Ash backtracks constantly in the show, so this reads naturally; the journey map at the top of this chapter shows the book's order. We state the convention once, here, and never apologize for it again: **when the math needs a concept, that's where its Gym appears.**

One more licensed deviation, stated up front: in the anime Ash *loses* at the Indigo League. Here the League **is** the exam — and because you will have done the work, the finale is written as a **win** (a 9–10, not a coin-flip pass).

**The Trainer Rank ladder — progress you can feel.** Badges are not just a checklist; they raise a cumulative **Trainer Rank** that every chapter opener reports (in its "Where You Are" line) so you always know how far you've come:

| Badges held | Trainer Rank |
|---|---|
| 0–2 | **Rookie Trainer** |
| 3–4 | **Junior Trainer** |
| 5–6 | **Ace Trainer** |
| 7 | **Veteran Trainer** |
| 8 + mock exams cleared | **Champion-ready** |

You begin, tonight, at the very bottom of the ladder:

> **Rank: Rookie Trainer · Badges: 0.**

Each chapter you clear earns a badge, ticks the rank, and lights another node on the journey map. By the time you reach the Plateau — Champion-ready, eight badges, mocks cleared — Exam P is just the last battle of a road you've already walked.

## Part 4 — The Trainer's Calculator (TI-30XS MultiView)

<figure>
<img src="../../assets/diagrams/ch00_calc_keypad.png" alt="A labeled schematic of the TI-30XS MultiView calculator. The body shows a green two-line display reading E[X] = x-bar = 2.15, above a grid of keys. Seven keys are highlighted and called out in a legend on the right: [2nd] (the gateway key), [prb] (nCr / nPr / factorial, ch04), [data] (the list editor for entering a pmf into L1, L2, ch03), [2nd][stat] (1-Var Stats, reading x-bar = E[X] and sigma-x where Var = sigma-x squared), [STO arrow] (store don't retype, seven memories), [F<>D] (toggle a fraction to its decimal), and [2nd][ln] = e^x (Poisson and exponential in one keystroke). A note explains setup: set the display mode, store with STO, clear scratch memory with [2nd][clear var], and bring two memory-cleared units to the exam." style="width:88%; max-width:720px; display:block; margin:1em auto;">
<figcaption>Your standard-issue gear. This book teaches <strong>one</strong> calculator — the TI-30XS MultiView — to fluency. The seven spotlighted keys are the ones Exam P leans on; each gets a full just-in-time lesson in the chapter where the math first needs it. Tonight, just the setup.</figcaption>
</figure>

Oak hands you the calculator. "One machine, Ash, learned cold — that beats two machines learned half-way. Master this one and you'll reclaim minutes on the exam and stop making rounding mistakes. Tonight, only the basics: how to set it up, how to *clear* it, and the one habit that saves more points than any other."

This book teaches the TI-30XS MultiView and only it — its MathPrint display, one-press `nCr`/`nPr`, and a data-list **1-Var Stats** engine make it the best-suited permitted machine for Exam P. Each skill is dropped exactly where it's first needed (a key-cap strip in a Trainer's Tip): the `[prb]{.kbd}` menu in `ch04` for binomial coefficients, the flagship **1-Var Stats** workflow in `ch03` for means and variances, `[2nd]{.kbd}[ln]{.kbd}` $=e^x$ in `ch05` for Poisson, and standardization with stored $\mu,\sigma$ in `ch12`. The full field manual is **Appendix D**. Here is the setup that comes first.

**Notation note.** Calculator keys are written as bare key-caps — [2nd]{.kbd}, [prb]{.kbd}, [data]{.kbd}, [STO▸]{.kbd}, [F◂▸D]{.kbd}, [enter]{.kbd} — little boxes, distinct from math type and from code. A sequence is just key-caps in a row: [2nd]{.kbd} [stat]{.kbd}.

### Setup skill 1 — Modes & the display

Press [mode]{.kbd} once to see the display settings. For Exam P, the defaults are fine: **MathPrint** (so fractions, exponents, and roots show the way they're written), **Float** decimal display (full precision, not a fixed 2 places), and **Degree** is irrelevant to probability. The point of checking [mode]{.kbd} is simply to *know where it is* — set it once and forget it.

### Setup skill 2 — The gateway key [2nd]{.kbd}

Almost every key has a **second function** printed in small type *above* it. The [2nd]{.kbd} key is how you reach it: press [2nd]{.kbd}, then the key, and you get the label above instead of on it. The most important examples this book uses constantly:

- [2nd]{.kbd} [ln]{.kbd} gives $e^x$ (the key's printed second function).
- [2nd]{.kbd} [stat]{.kbd} (the second function over [data]{.kbd}/stat) opens the **statistics** menu.
- [2nd]{.kbd} [clear var]{.kbd} wipes stored variables.

If a keystroke ever gives a result you didn't expect, the usual cause is a missing or stray [2nd]{.kbd}. Glance at whether you wanted the printed-*on* function or the printed-*above* one.

### Setup skill 3 — Clear before every problem

This is a discipline, not a feature. **Before each new problem, clear the slate** so a leftover number never contaminates a fresh calculation:

- [clear]{.kbd} wipes the current entry line.
- [2nd]{.kbd} [clear var]{.kbd} clears the stored memory variables (do this between problems that store different values).

::: trainers-tip
**TRAINER'S TIP — clear-before-each-problem**

The single cheapest error-prevention habit on the exam: between problems, press [clear]{.kbd} and, if you stored anything, [2nd]{.kbd} [clear var]{.kbd}. A stale value left in memory is invisible until it silently corrupts your next answer. Make the clear a reflex, like recalling a Pokémon before the next battle.
:::

### Setup skill 4 — The seven memory slots & [STO▸]{.kbd} (store, don't retype)

The TI-30XS holds **seven memory variables** — $x, y, z, t, a, b, c$. To save a computed value into one, press [STO▸]{.kbd} then the variable key. To use it later, just type that variable; it stands in for the full stored number.

*Why it matters more than it looks.* When a multi-step problem produces an ugly intermediate — say $E[X]=2.15384\ldots$ — you have two choices. You can write down a rounded "$2.15$" and re-type it later (introducing **rounding drift** that can push your answer into the wrong multiple-choice bucket), or you can press [STO▸]{.kbd} [x]{.kbd} and carry the *full-precision* value forward untouched. Always do the second. **Store, don't retype** — it is the habit that most reliably separates a right answer from a "close, but not option C."

A worked feel for it: compute $(0.2)(0.5)+(0.7)(0.05)$, press [STO▸]{.kbd} [a]{.kbd} to bank the full result, and now [a]{.kbd} *is* that number in every later keystroke — no copying, no rounding, no drift.

### Setup skill 5 — The fraction toggle [F◂▸D]{.kbd}

Press [F◂▸D]{.kbd} to flip the displayed answer between its **fraction** and **decimal** forms. Get $\tfrac{3}{8}$ from a computation and want $0.375$? One press. Probabilities are often cleaner to *enter* as fractions and cleaner to *report* as decimals — this key moves between them instantly.

### Setup skill 6 — Order of operations

The TI-30XS obeys standard order of operations (it is an algebraic-entry machine), so it evaluates `2 + 3 × 4` as $2+12=14$, **not** $20$. The lesson: **parenthesize anything you mean to group**, especially a numerator or denominator. To compute $\dfrac{x-\mu}{\sigma}$, type `( x − μ ) ÷ σ` — without the parentheses the machine divides only $\mu$ by $\sigma$ and ruins the answer. When in doubt, add the brackets; they never hurt.

::: pokedex-entry
**POKÉDEX ENTRY №00.0 — TI-30XS Setup Checklist**

- **[mode]{.kbd}** once: MathPrint, Float. Set and forget.
- **[2nd]{.kbd}** reaches each key's small *above-the-key* function ($e^x$, stat, clear var).
- **Clear before every problem:** [clear]{.kbd}, and [2nd]{.kbd} [clear var]{.kbd} for stored memory.
- **[STO▸]{.kbd} + a variable** ($x,y,z,t,a,b,c$): *store, don't retype* — carry full precision, kill rounding drift.
- **[F◂▸D]{.kbd}** toggles a fraction ↔ its decimal.
- **Order of operations** is standard: **parenthesize numerators and denominators.**

*Recognition cue:* an ugly intermediate value → [STO▸]{.kbd} it. A grouped expression → wrap it in parentheses. A new problem → clear first.
:::

## Part 5 — Reading the Symbols

"One last thing tonight," Oak says. "The guide speaks in symbols. They look like a locked door, but every symbol is a *word* — a plain-English word you already know. Learn to say each one aloud and the door was never locked." Here are the glyphs you'll meet first; each gets its *full* nine-beat lesson the first time it does real work (variables and $\sum$ in `ch01`, the bar $\mid$ in `ch02`, $\int$ in `ch08`). Tonight, learn only the word each one says.

**Variables vs. their values — capital is the slot, lowercase is what fills it.** A **capital** letter ($X$, $Y$, $N$) names a **random variable**: an uncertain quantity, a labeled empty slot. Its matching **lowercase** ($x$, $y$, $n$) is **one particular value** the slot might take. So $P(X = x)$ reads "the probability that the variable $X$ takes the value $x$." Capital = the question; lowercase = this run's answer. *(This is not the "solve-for-$x$" letter of school algebra, which hides one fixed number — a random variable has a whole range of values it could take, each with some chance.)*

**Subscripts — one name for a numbered family.** A small mark *below* the line is a **label**, never math: $L_4$ is "the fourth $L$," never $L\times4$ and never $L^4$ (powers sit *above* the line). An index letter generalizes it: $L_i$ is "the $i$-th one." When you see $p_k$, hear "the $k$-th probability."

**The summation sign $\sum$ — a long-handled plus sign.** $\sum$ (capital sigma, **S for Sum**) means only **"add these up."** Read the start *below* it, the stop *above* it, the term to its right, then write out the additions:
$$\sum_{i=1}^{n} a_i \;:=\; a_1 + a_2 + \cdots + a_n.$$
If you can do $5+8+3$, you can do every summation in this book. (Its multiplying cousin $\prod$ — capital pi — works identically with $\times$.)

**Function & operator notation $P(\cdot)$, $\E[\cdot]$ — a name, then its input.** A **name** immediately followed by a bracket means "apply this named operation to what's inside" — read "[name] of [input]." So $P(A)$ is "the probability of $A$" (a number in $[0,1]$), $\E[X]$ is "the expected value — the average — of $X$," $f(x)$ is "$f$ of $x$." It is **never** multiplication: there is no number "$P$" to multiply by. (Tell them apart by what's in front: a *number* before a bracket multiplies, $3(x)=3x$; a *named operation* before a bracket is applied.)

**The "given" bar $\mid$ — the words "given that."** Inside a probability, the vertical bar splits the bracket in two: everything to its **right** is the world you now assume happened; everything to its **left** is what you're finding *inside* that world. So $P(A \mid B)$ is "the probability of $A$ **given that** $B$ happened." The bar is **not symmetric** — $P(A\mid B)\neq P(B\mid A)$ in general; whatever you are *told* goes on the right. (Confusing the two sides is the costliest notation slip on the whole exam; Chapter 2 builds Bayes' theorem precisely to convert one into the other.)

**Set membership $\in$ — "is in / belongs to."** $x \in A$ reads "$x$ is in $A$." With curly braces (a set), $3 \in \{1,2,3,4,5\}$ reads "$3$ is in the set one-through-five" (true). You meet it properly when Chapter 1 names the space of possible outcomes.

**The integral sign $\int$ — "the continuous sum."** The tall stretched-$S$ is the exact cousin of $\sum$: where $\sum$ adds a *list* of separate terms, $\int$ adds a *smooth, unbroken* quantity. $\int_a^b f(x)\,dx$ reads "the integral from $a$ to $b$ of $f(x)$" — the area under $f$ between $a$ and $b$ — with the trailing $dx$ a quiet "with respect to $x$." You won't need it until Act II (`ch08` builds it from scratch); for now, when you see the stretched-$S$, hear **"the continuous sum of."**

::: trainers-tip
**TRAINER'S TIP — read every symbol *aloud***

When a line of math looks like a wall, don't stare — *narrate it.* Point at each glyph and say its English word: "$P$ of … $X$ equals … given that … the sum of …." A formula you can read aloud as a sentence is a formula you can use. Silent staring is where people freeze; reading aloud is where they unfreeze. And remember the two position rules: *below* the line is a subscript (a label), *above* the line is an exponent (a power); a *named operation* hugging a bracket applies, a *number* hugging a bracket multiplies.
:::

::: pokedex-entry
**POKÉDEX ENTRY №00.1 — The Symbol Glossary You Leave Pallet Town With**

| Symbol | Read aloud | Means |
|---|---|---|
| $X$ vs. $x$ | "the variable $X$" / "a value $x$" | capital = uncertain quantity; lowercase = a value it takes |
| $L_i$ | "$L$ sub $i$" | the $i$-th member of a family (a label, never $\times$ or a power) |
| $\sum$ | "the sum of" | add the listed terms (start below, stop above, term right) |
| $P(\cdot),\ \E[\cdot]$ | "the probability of" / "the expected value of" | a named operation applied to its input (never multiplication) |
| $\mid$ | "given that" | right of the bar = assumed world; left = what you're finding |
| $\in$ | "is in / belongs to" | the left thing is a member of the right collection |
| $\int$ | "the continuous sum of" | the smooth cousin of $\sum$ (area under a curve) |

*Recognition cue:* every glyph is a word. Stuck on a line? Say each word in order, left to right, and the sentence appears.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

Why open an exam-prep book with the journey, the gear, and the symbols — before a single probability? Because all three are exactly what a working actuary uses every day, and none of them is the "hard part."

A practicing actuary reads $\E[(X-d)_+]$ off a pricing memo and instantly hears *"the average the insurer pays on a loss $X$ after a deductible $d$."* They read $P(\text{default}\mid\text{downgrade})$ and hear *"the chance a bond defaults given it was just downgraded."* They drive a calculator reflexively and never lose a digit to rounding. And they manage a long campaign — many exams, over years — by knowing exactly what each sitting demands and pacing toward it. The notation, the tool, and the map: fluency in these is what separates the candidates who clear Exam P from those who freeze, far more often than any single theorem does.

*Series bridge:* the same notation runs through every later actuarial exam (FM, FAM, the CAS volumes); the same single-calculator discipline pays off every time you sit one; and the same "the syllabus is a map you walk" mindset carries you through the whole credentialing journey. Learn to read the map once, here in Pallet Town, and you read it for the rest of the road.
:::

## Badge Earned — Trainer's License Stamp

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/trainer_license.png" alt="Trainer's License stamp — a Poke Ball seal marking the start of the journey" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Trainer's License stamped — the journey begins!</strong> Rank: Rookie Trainer · Badges: 0.</figcaption>
</figure>

This isn't a Gym Badge — the first of those waits in Cerulean, a chapter or two up the road. It's your **Trainer's License**: proof you can read both maps and hold your gear before you set foot on Route 1. You've earned it when you can, unaided:

- ☐ **Navigate the book** — name what each box does (Pokédex Entry, Trainer's Tip, Team Rocket's Trap, Real-World, Now Playing, Enrichment, Concept Gate) and use the chapter and concept test-out gates to skip only what you truly own.
- ☐ **State the exam facts** — 3 hours · 30 questions · scored 0–10, a 6 passes · normal table provided · TI-30XS permitted · no penalty for guessing.
- ☐ **Know the journey** — eight badges are the syllabus, the Indigo Plateau is the exam, the badges are sequenced to the math (not canon), and the Trainer Rank ladder climbs Rookie → Champion-ready. You begin at **Rookie · 0 badges**.
- ☐ **Set up the calculator** — modes, the [2nd]{.kbd} gateway, clear-before-each-problem, [STO▸]{.kbd} (store don't retype), [F◂▸D]{.kbd}, and parenthesizing for order of operations.
- ☐ **Read the symbols** — variable vs. value, subscripts, $\sum$, $P(\cdot)$/$\E[\cdot]$, the bar $\mid$ ("given," not symmetric), $\in$, and $\int$ — each as a plain-English word.

> **Gym rematch pointers (🧴 Potion).** Fuzzy on the boxes or gates → re-skim Part 1. Unsure of the target → Part 2's exam-facts table. Hazy on rank or badge order → Part 3. Calculator setup shaky → Part 4 + Pokédex Entry №00.0, and remember Appendix D is the full field manual. A symbol still looks like a wall → Part 5, read it aloud, and trust that its *full* lesson arrives the first time it does real work.

*Onward to Route 1 and beyond — where you meet Pikachu for real, reason your first wild encounter, and start collecting the eight badges that are Exam P in disguise. Rank: Rookie Trainer · Badges: 0. The road north begins.*

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
