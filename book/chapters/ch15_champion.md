<!--
  file: ch15_champion
  tier: B
  outcomes: all
  draft1_source: drafts/chapters_draft1/ch13_champions_challenge.md
  maps_to: The League — strategy + 3 mocks
-->

# Champion's Challenge — Exam Strategy & Mock Exams {.type-normal}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="The Kanto region map, every town and route now cleared, the path running from Pallet Town all the way to the Indigo Plateau." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Kanto, end to end — eight badges earned, the whole region behind you. One chamber left: the Indigo Plateau, where everything you learned is tested at once.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Champion Is Waiting"**

The doors of the Indigo Plateau's final chamber open with a sound like a held breath. You have eight badges on your belt, the Elite Four behind you, and the whole journey from Pallet Town packed into your Pokédex. And there, at the far end of the marble hall, leaning against the Champion's throne with that infuriating half-smile, is Gary.

"Took you long enough, Ash." He tosses a Poké Ball and catches it. "Grandpa always said you were better at the *math* than the battling. Let's find out. No gym leader this time — no single type to study. I'm going to throw **thirty problems** at you, one after another, from everything you've ever learned. General probability, the distributions, the multivariate stuff, the loss models. Mixed. No warning which is which."

He checks an imaginary watch. "Three hours. Six minutes a problem if you want to finish. Get one wrong, you don't get to stop and sulk — you flag it and move on. And here's the part you'll hate: I'm not going to tell you the *topic*. You have to **recognize** it. The way a Champion reads an opponent's strategy from the first move."

Pikachu's cheeks spark. You feel the old jolt of doubt — not "do I know the formulas," but something harder. *Can you recognize which formula, instantly, under the clock, thirty times in a row, without a single panic?*

That is the whole game now. Not new theory. **Execution.** You crack your knuckles, open Actuary Mode one last time, and ask the only question that matters at the Plateau: **how do you turn everything you know into a 10, not a 6, when the clock is running and the archetype is hidden?**
:::

## Where You Are — 60-Second Retrieval

You crossed the Indigo Plateau in the last chapter holding the final pieces: **order statistics** — the distribution of the *largest* or *smallest* of a sample, $F_{\max}(x)=[F(x)]^{n}$ and $F_{\min}(x)=1-[1-F(x)]^{n}$ — and the **Central Limit Theorem**, the promise that a sum or average of many independent pieces is approximately **normal**,

$$\bar X \;\overset{\text{approx}}{\sim}\; \Normal\!\Big(\mu,\ \tfrac{\sigma^{2}}{n}\Big),\qquad S=\textstyle\sum X_i \;\overset{\text{approx}}{\sim}\; \Normal\big(n\mu,\ n\sigma^{2}\big),$$

with the **continuity correction** (a $\pm 0.5$ nudge) whenever the thing you are approximating is *discrete*.

That CLT is the last new theorem in the book. This chapter teaches **no new mathematics at all** — every formula you need is already on your belt. What it teaches is the meta-skill of *using* all of it under a clock. Take sixty seconds and prove the last chapter still lives in your hands.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the last chapter**

Answer from memory; if any feels shaky, flip back before continuing.

1. Five independent scores are $\Unif(0,1)$. What is $P(\max \le 0.8)$? *(Answer: $0.8^5 = 0.32768$.)*
2. A sum of $100$ i.i.d. pieces has mean-per-piece $3$ and variance-per-piece $4$. What are the mean and variance of the sum? *(Answer: $\mu_S=300$, $\Var(S)=400$, so $\SD=20$.)*
3. Approximating $P(X \le 25)$ for a *discrete* count by the normal, what number do you actually standardize at? *(Answer: $25.5$ — continuity correction.)*

All three instant? You're ready for the Plateau. Any hesitation? The retrieval *is* the lesson — go reclaim it, then come back.
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer, one last briefing</figcaption>
</figure>

Professor Oak's voice crackles through Actuary Mode as you face the long marble hall.

"This is the only chapter, Ash, where I teach you nothing new. Every formula you need is already in Chapters 1–14. What separates a passing **6** from a perfect **10** is not knowledge — it is **execution**: pacing, recognizing an archetype on sight, deploying the right shortcut without hesitation, the discipline of a sanity check, and the refusal to ever leave a blank. The three mock exams that close this chapter are your dress rehearsal. The strategy below is the coaching that makes the rehearsal pay off. Treat *execution itself* as a skill you can drill — because it is."

By the end of this chapter you will be able to:

- **Budget** the three-hour, thirty-question sitting at six minutes per question and run the **two-pass strategy** — answer the recognized archetypes first, flag and return for the rest, never leaving a blank. *(Execution.)*
- **Recognize** each problem's archetype on sight from the *tell* in its stem, and **deploy** the matching shortcut — the gamma integral, the survival-function (Darth Vader) rule, MGF kernel-matching, exponential memorylessness, the Poisson identity $\mu=\sigma^2=\lambda$, the binomial$\to$Poisson approximation, and the continuity correction. *(Integrative, Topics 1–3.)*
- **Run** standing sanity checks on every answer — probabilities in $[0,1]$, variances $\ge 0$, $\E[\text{payment}]\le\E[\text{loss}]$, support consistency, a weighted average between its extremes. *(Execution.)*
- **Sit and pass** three weight-matched mock exams under timed conditions, integrating every outcome from Topics 1–3 at once. *(All outcomes.)*

> *Exam-weight signpost.* This is the whole exam, mixed. The mocks are split the way the **live SOA Exam P** is: roughly **8 General Probability / 14 Univariate / 8 Multivariate** out of every 30. This chapter is **Tier B** — no single hard idea, but the load-bearing skill of *deploying all of them under time*, which is exactly what the real exam grades.

::: concept-gate
**CHAPTER TEST-OUT GATE — Are You Already Exam-Ready?**

This whole chapter is execution, so the test-out is execution. Set a **six-minute timer per problem** and work these four cold — different topic each, no labels, the way the real exam comes:

1. On Route 1, Spearow swoop in at an average rate of $3$ per minute (Poisson). Find $P(\text{at least }2\text{ in one minute})$.
2. A scanner flags a Ghost-type correctly $95\%$ of the time and false-flags a non-Ghost $10\%$ of the time; only $2\%$ of wild Pokémon are Ghost. It just flagged one. Find $P(\text{Ghost}\given\text{flagged})$.
3. A density is $f(x)=\tfrac{1}{16}x\,e^{-x/4}$ for $x>0$. Find $\E[X]$ **without** integrating by parts.
4. $S\sim\Binom(100,0.3)$. Using the normal approximation with continuity correction, find $P(S\le 25)$.

*(Answers: $1-4e^{-3}\approx 0.801$; $\approx 0.162$; recognize $\GammaDist(2,4)$ so $\E[X]=\alpha\theta=8$; $\Phi(-0.982)\approx 0.163$.)*

Four for four, **inside six minutes each, recognizing the tool before computing**? You are ready — **skip straight to the three mock exams** and sit them timed. Any miss, any hesitation, or any answer that took you longer than the budget? The coaching below is built exactly for you. Each meta-skill has its own skip-gate too.
:::

---

Four meta-skills carry you from a 6 to a 10, in increasing subtlety. We teach them **in order**, each with its own "do you already own this?" skip-check, then the full nine-beat lesson, then a Pokédex Entry you can carry into the exam:

1. **The six-minute budget & two-pass strategy** — *spend the clock where it earns points*
2. **Archetype recognition** — *name the tool from the tell, before you compute*
3. **The shortcut catalog** — *the moves that turn six-minute problems into ninety-second ones*
4. **Standing sanity checks** — *catch the impossible answer before you bubble it*

## Concept 1 — The Six-Minute Budget & Two-Pass Strategy

::: concept-gate
**DO YOU ALREADY OWN THIS? — Pacing**

You are $4$ minutes into a nasty double-integral, you cannot see the region, and $14$ problems remain untouched. What do you do *right now*?

If you answered **"mark a provisional guess, flag it, and move on — there's no penalty for a wrong answer, and a flagged problem I return to is worth more than a blank one I agonized over,"** you own pacing — **skip to Concept 2**. If your instinct was "push through, I never leave a problem unfinished," read on — that instinct will cost you the exam.
:::

**Beat 1 — The one-sentence idea.** *You are paid only for the count of correct answers, not the order you solve them in — so spend the clock on points you can still earn, and never burn it on a problem that is beating you.*

**Beat 2 — Anchor + concrete instance.** You already know how to budget a fixed resource across competing claims — it is the same arithmetic as splitting a partition. Here the resource is **time**, and the partition is **the thirty problems.** The exam is $180$ minutes for $30$ questions. Divide:

$$\frac{180\ \text{minutes}}{30\ \text{questions}} = 6\ \frac{\text{minutes}}{\text{question}}.$$

Six minutes is the *average* you can afford. But the exam is not built of average problems — some are ninety-second gifts, some are seven-minute monsters.

**Beat 3 — Reason through it in plain words.** Picture the thirty problems as thirty Pokémon you must battle, each worth exactly **one point** whether it's a Caterpie or a Charizard. A grader does not award partial credit for "I was *so close* on the hard one." So the winning strategy is obvious once you see the points are flat: **bank time on the easy battles and spend it on the hard ones.** If a Caterpie problem takes you two minutes, you have just *banked four minutes* to throw at a Charizard later. If a Charizard problem is eating minute after minute with no answer in sight, every extra minute you feed it is a minute stolen from two or three gifts still sitting unopened further down the exam.

So you make two passes. **Pass 1:** go front to back; any problem whose archetype you recognize within about $30$ seconds, solve it now; any problem that is *not yielding* by about the four-minute mark, mark your best provisional answer, **flag it**, and move on. **Pass 2:** return to the flagged problems with all the time you banked from the gifts.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap — the one that sinks more capable students than any formula error — is **"I don't leave a problem unfinished."** It feels like discipline. It is actually the most expensive habit on the exam. Sinking twelve minutes into one stubborn problem doesn't cost you one point; it costs you the **two or three later problems** you now have no time to even read. And the second half of the trap is just as deadly: **leaving a blank.** Exam P has *no penalty for a wrong answer* — a blank scores zero, and so does a wrong guess, but a guess has a $\sim\!20\%$ chance (five choices) of being *right*. A guess therefore **strictly dominates** a blank. There is never, on this exam, a reason to leave a bubble empty.

**Beat 5 — Translate into notation, one glyph at a time.** Let $n=30$ be the question count and $T=180$ the minutes. The budget is the ratio

$$b = \frac{T}{n} = \frac{180}{30} = 6\ \text{min/question}.$$

Now let $t_i$ be the minutes you actually spend on problem $i$. The only hard constraint is that they sum to no more than the total:

$$\sum_{i=1}^{30} t_i \le 180.$$

The two-pass strategy is simply *choosing the $t_i$ wisely*: small $t_i$ on the gifts frees budget for large $t_i$ on the monsters, while a hard cap (flag at $t_i\approx 4$–$6$) stops any single problem from devouring the sum. The score you are maximizing is the count of correct answers,

$$\text{Score} = \sum_{i=1}^{30} \indicator{\text{problem } i \text{ answered correctly}},$$

where $\indicator{\cdot}$ (read "the indicator of") is $1$ when the bracketed statement is true and $0$ otherwise. Notice the score doesn't mention $t_i$ or the order at all — only correctness. That *is* the whole argument for the two-pass strategy.

**Beat 6 — Generalize: the rule that falls out.** Maximizing $\sum \indicator{\text{correct}}$ subject to $\sum t_i \le 180$ is a budget-allocation problem, and its solution is the greedy one: **spend each minute where it buys the highest probability of a point.** Early in the exam that's the recognized gifts (a near-certain point for ninety seconds); a problem that's stalled at four minutes has a *low* return on the next minute, so the next minute should go elsewhere. The two-pass loop is exactly this greedy rule made mechanical: gifts first, flag the stalls, return with banked time, fill every remaining bubble with a guess at the buzzer.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* thirty average problems — six minutes each, finish on the buzzer.
- *Twist (the realistic mix):* ten gifts at $2$ minutes ($20$ min) bank you $40$ minutes; spend them on the ten hardest, giving those nearly $10$ minutes apiece while the ten medium problems take their $6$. Same $180$ total, far more points.
- *Edge (you're running out of clock):* with two minutes left and four problems untouched, **stop solving and start bubbling** — four guesses average $\sim\!0.8$ expected points; one more solved problem is worth exactly $1$ but costs all your time and leaves three blanks. Guess them all.

**Beat 8 — Picture it.** The clock is a literal progress bar; the two passes lay over it.

<figure>
<img src="../../assets/diagrams/ch15_two_pass_timeline.png" alt="A horizontal 180-minute timeline split into two passes. Pass 1 sweeps left to right across all 30 question slots: recognized gifts are solved (short green blocks), stubborn problems get a quick provisional guess and a flag marker (short red blocks), banking time. Pass 2 returns only to the flagged red slots, now drawing on the banked time shown as a reservoir filling from the gifts. A final sliver at the right edge labeled 'bubble every blank' fills any remaining empty answers." style="width:80%; max-width:560px; display:block; margin:1em auto;">
<figcaption>The two-pass clock: Pass 1 harvests the gifts and flags the monsters (banking time); Pass 2 spends the banked time on the flags; a final sweep guarantees no empty bubble.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now run an exam like a Champion runs a battle: triage on recognition, cap your spend per problem, bank time on the easy points, and finish with **zero blanks**. The single behaviour that earns this badge is *the willingness to walk away from a problem that is beating you.*

::: pokedex-entry
**POKÉDEX ENTRY №15·1 — The Six-Minute Budget & Two-Pass Strategy**

$$b = \frac{180\ \text{min}}{30\ \text{questions}} = 6\ \frac{\text{min}}{\text{question}}.$$

**Pass 1:** front to back; solve every recognized archetype, flag and provisionally answer anything not yielding by $\sim\!4$ minutes. **Pass 2:** return to the flags with banked time. **Always** bubble every question — a guess ($\sim\!20\%$ right) strictly beats a blank ($0\%$), because there is **no wrong-answer penalty**.

*In plain terms:* you are paid for the count correct, not the order. Bank time on the gifts; spend it on the monsters; never leave an empty bubble.

*Recognition cue:* the feeling of being **"stuck and frustrated"** *is itself* the signal to flag and move on — that feeling is protecting the clock for points you can still earn.
:::

## Concept 2 — Archetype Recognition: Name the Tool From the Tell

::: concept-gate
**DO YOU ALREADY OWN THIS? — Recognition**

A stem ends: *"…find the probability of **at least one** success in $7$ independent attempts, each succeeding with probability $0.2$."* Before computing, which tool, and which exact move?

If you instantly thought **"complement — $1-(0.8)^7$ — because 'at least one' of independent trials is always $1-P(\text{none})$,"** you own recognition — **skip to Concept 3**. If you reached for the pencil before naming the tool, read on; speed on this exam *is* recognition, not arithmetic.
:::

**Beat 1 — The one-sentence idea.** *Exam speed is pattern-matching, not derivation: every problem carries a **tell** in its words, and a fast scorer reads the tell, names the tool, and only then picks up the pencil.*

**Beat 2 — Anchor + concrete instance.** You already do this with Pokémon types — you see a Geodude and think "Water beats it" before the battle starts, because the *type* dictates the move. A problem's archetype is its type. Here is one stem, read for its type:

> *"On Route 1, Spearow swoop in at an **average rate** of $3$ **per minute**, independently. In one minute, find $P(\text{at least }2)$."*

**Beat 3 — Reason through it in plain words.** Two phrases do all the work. **"Average rate per interval"** is the unmistakable signature of a **Poisson** count — events arriving at a constant rate $\lambda$ over an interval — so $N\sim\Poisson(3)$. And **"at least two"** is the signature of a **complement**: directly summing $P(2)+P(3)+\cdots$ runs forever, but $\{N\ge 2\}$ is just everything except $\{0,1\}$. The two tells together hand you the entire solution *before you compute a single term*:

$$P(N\ge 2) = 1 - P(0) - P(1) = 1 - e^{-3} - 3e^{-3} = 1 - 4e^{-3} \approx 0.801.$$

You recognized "Poisson" and "complement" in the time it took to read the sentence. The arithmetic was the easy part.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The novice's instinct is to **start computing immediately** — to see "$P(\text{at least }2)$" and begin writing $P(2)+P(3)+\cdots$, a sum with no end. Worse, under panic, to compute $P(N\ge 2)=1-P(1)$, *forgetting $P(0)$.* Both errors come from the same root: **pencil before recognition.** If you had named the archetype first — "Poisson, and 'at least' means complement of the *low* values" — you'd have known to subtract *both* $P(0)$ and $P(1)$, and you'd never have started an infinite sum. Recognition is not a luxury you do after the work; it is the move that *chooses* the work.

**Beat 5 — Translate into notation: the recognition map.** Every archetype has a glyph-level or word-level tell. Here is the map — memorize the left column, train the reflex to the right.

| The stem says… | Reach for… | From |
|---|---|---|
| "at least one" (independent trials) | complement $1-P(\text{none})=1-\prod(1-p_i)$ | Ch 5 |
| "given that," posterior, sensitivity/false-positive | Bayes' theorem / Bayes grid | Ch 5 |
| "average rate," "per interval," count over time | Poisson, $\mu=\sigma^2=\lambda$ | Ch 8 |
| "time until," "memoryless," constant hazard | Exponential | Ch 8 |
| "number of trials until the $r$-th success" | (Negative) Binomial / Geometric | Ch 8 |
| draws **without** replacement from a finite pool | Hypergeometric | Ch 8 |
| a given MGF $M_X(t)$ | kernel-match it / differentiate at $0$ | Ch 7 |
| $\E[X]$ for $X\ge 0$ from the survival $S(x)$ | Darth Vader $\displaystyle\int_0^\infty S(x)\,dx$ | Ch 7 |
| $\displaystyle\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx$ shape | gamma integral $=\Gamma(\alpha)\theta^{\alpha}$ | Ch 7 |
| deductible / limit / coinsurance | loss model $\alpha\big[(X\wedge u)-(X\wedge d)\big]$ | Ch 10 |
| "strongest / weakest / $k$-th of $n$" | order statistics, $[F(x)]^n$ | Ch 14 |
| "approximately normal," large $n$, a sum/average | CLT ($+$ continuity correction if discrete) | Ch 14 |

The symbol $\wedge$ here reads **"minimum with"** — $X\wedge u$ means $\min(X,u)$, the loss *capped* at the limit $u$ — and $(X-d)_{+}$ reads **"$X$ minus $d$, floored at zero,"** the amount left after a deductible $d$. Both are the loss-model glyphs from Chapter 10.

**Beat 6 — Generalize: the recognition loop.** The map compresses into a three-step reflex you run on *every* stem:

1. **Read the last sentence first** — it names the quantity asked ($\E[X]$? a probability? a variance?).
2. **Scan the stem for the tell** — the phrase or glyph that fixes the archetype.
3. **Name the tool out loud (in your head) before the pencil moves.**

The fast scorers haven't memorized more formulas than you; they've trained this loop until it is reflex.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* one clean tell — "average rate" $\Rightarrow$ Poisson.
- *Twist (disguise):* the tell is dressed up. "A wild Pokémon is Ghost-type with probability $0.02$; a scanner flags it correctly $95\%$ of the time and false-flags $10\%$ of non-Ghosts; it flagged one — is it a Ghost?" The words "flags correctly / false-flags / it flagged one, find the probability it *is*" are sensitivity, false-positive, and a *flipped bar* — pure **Bayes**, no matter the Pokémon skin.
- *General/edge (braided archetypes):* the back-of-exam problems stack two or three tells. "Daily injury **count** is Poisson; each injury's **cost** is exponential; find the variance of the **aggregate**" carries *three* tells (Poisson + exponential + compound/CLT) and you name all three before starting. (That's the Gym Battle.)

**Beat 8 — Picture it.** Recognition is a decision tree you descend from the tell.

<figure>
<img src="../../assets/diagrams/ch15_recognition_tree.png" alt="A decision tree for archetype recognition. The root asks 'what does the last sentence ask for?' branching to probability, expectation, or variance. Each branch then forks on the tell in the stem: 'average rate per interval' routes to Poisson, 'given that / flagged' routes to Bayes, 'time until / memoryless' routes to Exponential, 'deductible / limit' routes to the loss model, 'strongest / k-th' routes to order statistics, 'approximately normal / large n' routes to the CLT. Leaves name the tool and its one-line shortcut." style="width:82%; max-width:600px; display:block; margin:1em auto;">
<figcaption>The recognition tree: read what's asked, find the tell, land on the tool — all before the pencil moves. Train this until it's reflexive.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now read any unlabeled stem, find its tell, and name the right tool on sight — the single skill that turns the Champion's "I won't tell you the topic" from a threat into a non-issue.

::: pokedex-entry
**POKÉDEX ENTRY №15·2 — Archetype Recognition**

The recognition loop, run on every stem:

$$\textbf{(1) read the last sentence}\ \to\ \textbf{(2) find the tell}\ \to\ \textbf{(3) name the tool}\ \to\ \text{then compute.}$$

Key tells: *"at least one"* $\to$ complement · *"given that / flagged"* $\to$ Bayes · *"average rate"* $\to$ Poisson · *"time until / memoryless"* $\to$ exponential · *"without replacement"* $\to$ hypergeometric · *given $M_X(t)$* $\to$ MGF · *deductible/limit* $\to$ loss model · *"strongest/$k$-th"* $\to$ order statistics · *"approximately normal, large $n$"* $\to$ CLT.

*In plain terms:* exam speed is pattern-matching, not derivation. The left column of the recognition map is the thing to memorize; the reflex to the right column is the thing to drill.

*Recognition cue:* **read the last sentence first** — it names the quantity. Then the tool is chosen *before the pencil moves.*
:::

## Concept 3 — The Shortcut Catalog

::: concept-gate
**DO YOU ALREADY OWN THIS? — Shortcuts**

A density is $f(x)=\tfrac{1}{16}x\,e^{-x/4}$ on $x>0$ and you want $\E[X]$. What is the *fast* path?

If you thought **"recognize the $\GammaDist(2,4)$ kernel — $\E[X]=\alpha\theta=8$ — no integration by parts,"** you own the shortcuts — **skip to Concept 4**. If you started setting up $\int_0^\infty x\cdot\tfrac{1}{16}xe^{-x/4}\,dx$ for integration by parts, read on; that integral is a six-minute trap that the gamma identity collapses to nine seconds.
:::

**Beat 1 — The one-sentence idea.** *A handful of identities turn the exam's "hard" problems — the ones built to eat your clock through integration by parts — into one-line recognitions; knowing them is the difference between finishing and running out of time.*

**Beat 2 — Anchor + concrete instance.** You've already met each of these shortcuts in its home chapter; this concept *gathers* them so the recognition reflex from Concept 2 has somewhere to land. Take the gate's density, $f(x)=\tfrac{1}{16}xe^{-x/4}$.

**Beat 3 — Reason through it in plain words.** The slow path is to write $\E[X]=\int_0^\infty x\cdot\tfrac{1}{16}xe^{-x/4}\,dx = \tfrac{1}{16}\int_0^\infty x^{2}e^{-x/4}\,dx$ and grind through **integration by parts twice** — three or four minutes of bookkeeping with two chances to drop a sign. The fast path is to *recognize the shape*. The density is proportional to $x^{2-1}e^{-x/4}$, which is exactly the kernel of a $\GammaDist(\alpha=2,\ \theta=4)$. A gamma's mean is $\alpha\theta$, so

$$\E[X] = \alpha\theta = 2\cdot 4 = 8 \qquad\text{(nine seconds, no calculus).}$$

The very same recognition handles the raw integral too, via the **gamma integral identity** $\int_0^\infty x^{n-1}e^{-x/\theta}\,dx=\Gamma(n)\theta^{n}$:

$$\E[X]=\tfrac{1}{16}\int_0^\infty x^{3-1}e^{-x/4}\,dx = \tfrac{1}{16}\,\Gamma(3)\,4^{3} = \tfrac{1}{16}(2)(64) = 8.\ \checkmark$$

Same answer, no integration by parts in sight. *That* is what a shortcut buys you.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is **defaulting to brute force**: seeing an integral and reaching for integration by parts, or seeing $\E[X]$ for a positive variable and reaching for $\int x f(x)\,dx$ when $\int_0^\infty S(x)\,dx$ is far cleaner. Brute force isn't *wrong* — it gets the answer — but on a six-minute clock it's a luxury you cannot afford thirty times. The discipline is: **before you integrate by parts, ask "is this secretly a gamma kernel, a survival-function integral, or a memoryless exponential?"** One of the three almost always collapses the work.

**Beat 5 — Translate into notation: the seven shortcuts.** Each is an identity you match by *kernel* or by *tell*.

The **gamma integral** (turns a polynomial-times-exponential into a factorial):
$$\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx=\Gamma(\alpha)\,\theta^{\alpha},\qquad \int_0^\infty x^{n}e^{-x}\,dx=n!.$$

The **survival-function (Darth Vader) rule** for a non-negative variable:
$$\E[X]=\int_0^\infty S(x)\,dx\quad(X\ge 0),\qquad \E[X]=\sum_{k\ge 0}P(X>k)\quad(\text{integer }X\ge 0).$$

**Exponential memorylessness** (the past never matters) and the per-loss deductible mean:
$$\E[X-d\mid X>d]=\theta,\qquad \E\big[(X-d)_{+}\big]=\theta\,e^{-d/\theta}.$$

The **Poisson identity** and the **binomial$\to$Poisson** approximation:
$$\mu=\sigma^2=\lambda\ (\text{Poisson}),\qquad \Binom(n,p)\approx\Poisson(np)\quad(n\text{ large},\ p\text{ small}).$$

**MGF moments** (differentiate at zero) and the **continuity correction**:
$$M_X'(0)=\E[X],\quad M_X''(0)=\E[X^2],\qquad P(X\le k)\approx\Phi\!\Big(\tfrac{k+0.5-\mu}{\sigma}\Big)\ (\text{discrete }X).$$

**Beat 6 — Generalize: when each one fires.** They are organized by the tell that triggers them — which is exactly the recognition map of Concept 2 pointing *here*: a polynomial$\times$exponential integral $\to$ **gamma**; $\E[X]$ for $X\ge 0$ from a survival function $\to$ **Darth Vader**; an exponential with a deductible or "already waited" condition $\to$ **memorylessness**; a count over an interval $\to$ **Poisson identity**; a rare event in many trials $\to$ **binomial$\to$Poisson**; a problem that *hands you* $M_X(t)$ $\to$ **MGF moments**; a discrete sum approximated by the normal $\to$ **continuity correction.** Recognition (Concept 2) and the catalog (Concept 3) are the two halves of one motion: *the tell names the shortcut.*

**Beat 7 — Ramp the difficulty.**

- *Simplest:* a clean gamma kernel — read off $\alpha\theta$.
- *Twist:* the gamma integral hiding inside a *variance*. For $\Expo(\theta)$, $\E[X^2]=\int_0^\infty x^2 \tfrac1\theta e^{-x/\theta}dx = \tfrac1\theta\Gamma(3)\theta^3 = 2\theta^2$ — so $\Var=2\theta^2-\theta^2=\theta^2$, no parts.
- *Edge (two shortcuts at once):* a *gamma tail* with integer shape uses the **Poisson-sum identity**, $P(X>x)=e^{-x/\theta}\sum_{j=0}^{\alpha-1}\tfrac{(x/\theta)^j}{j!}$ — recognition of *both* gamma and Poisson in one move. (Mock C, C15.23.)

**Beat 8 — Picture it.** The seven shortcuts, indexed by the tell that fires them.

<figure>
<img src="../../assets/diagrams/ch15_shortcut_catalog.png" alt="A reference card grid of the seven exam shortcuts. Each tile shows the trigger tell on top and the identity below: 'polynomial times e^{-x/theta}' -> gamma integral Gamma(alpha)theta^alpha; 'E[X], X>=0, survival given' -> Darth Vader integral of S(x); 'exponential + already waited / deductible' -> memorylessness, theta and theta e^{-d/theta}; 'count over an interval' -> Poisson mu=sigma^2=lambda; 'rare event, many trials' -> binomial approximates Poisson; 'M_X(t) given' -> differentiate at 0; 'discrete sum, normal approx' -> continuity correction k+0.5." style="width:84%; max-width:620px; display:block; margin:1em auto;">
<figcaption>The shortcut catalog as a reference card: each tell (top of a tile) points to the identity (bottom) that collapses the work. This is where the recognition map of Concept 2 lands.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now meet a "hard" integral or moment and, instead of grinding, recognize which of seven identities collapses it — the move that turns the back half of the exam from a time sink into a sequence of one-liners.

::: pokedex-entry
**POKÉDEX ENTRY №15·3 — The Shortcut Catalog**

$$\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx=\Gamma(\alpha)\theta^{\alpha}\ \ (\text{gamma}),\qquad \E[X]=\int_0^\infty S(x)\,dx\ \ (\text{Darth Vader, }X\ge 0).$$
$$\E\big[(X-d)_{+}\big]=\theta e^{-d/\theta},\quad \E[X-d\mid X>d]=\theta\ \ (\text{memoryless}),\qquad \mu=\sigma^2=\lambda\ \ (\text{Poisson}).$$
$$\Binom(n,p)\approx\Poisson(np),\qquad M_X'(0)=\E[X],\ M_X''(0)=\E[X^2],\qquad P(X\le k)\approx\Phi\!\big(\tfrac{k+0.5-\mu}{\sigma}\big).$$

*In plain terms:* these seven are the moves the graders' "hard" problems are secretly testing. Knowing them is the difference between finishing and running out of clock.

*Recognition cue:* the instant you're about to **integrate by parts**, stop and ask — *gamma kernel? survival integral? memoryless exponential?* One of the three usually collapses it.
:::

## Concept 4 — Standing Sanity Checks

::: concept-gate
**DO YOU ALREADY OWN THIS? — Sanity Checks**

You finish a problem and your final number is a variance of $-3$, or an expected *payment* of $\$8$ on an expected *loss* of $\$5$, or a probability of $1.4$. What does each tell you?

If you answered **"each is impossible, so I made an error — recheck before bubbling; a negative variance, a payment above the loss, and a probability above one cannot occur,"** you own the sanity checks — **skip to the Worked Examples**. If you'd have bubbled any of them, read on; most wrong multiple-choice answers are *impossible*, not merely incorrect.
:::

**Beat 1 — The one-sentence idea.** *Most wrong answers are not just incorrect — they are **impossible**, and a two-second guardrail check on every final number catches them before they cost you a point.*

**Beat 2 — Anchor + concrete instance.** You already know the *legal ranges* of every quantity in this book — probabilities live in $[0,1]$, variances are never negative, an insurance payment can't exceed the loss it covers. This concept just makes *checking those ranges* a fixed last step. Suppose you finish a deductible problem and write $\E[\text{payment}]=8$ when the problem said $\E[\text{loss}]=5$.

**Beat 3 — Reason through it in plain words.** Stop — that answer is *impossible.* A payment is the loss minus a deductible (and possibly capped); it is always **less than or equal to** the loss. An expected payment of $8$ against an expected loss of $5$ violates a law of the model, not just the arithmetic. You don't need to know *where* the error is to know that there *is* one. The check costs two seconds; bubbling the impossible answer costs a point. The same logic disqualifies a variance of $-3$ (variances are $\ge 0$ by construction, being an average of squares) and a probability of $1.4$ (probabilities cap at $1$).

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is treating the computed number as **automatically trustworthy** — "I did the steps, so the answer is whatever came out." But the exam's distractor choices are *engineered* from the common errors, and many of those errors produce impossible values: forget a minus sign and your variance goes negative; swap a deductible for a limit and your payment exceeds the loss; misplace the complement and your probability tops $1$. The graders are *hoping* you bubble the impossible distractor without looking. The fix is a reflex: **the instant you compute a final number, ask "could a sane risk look like this?"** If not, you have a sign or formula error — find it before bubbling.

**Beat 5 — Translate into notation: the guardrails.** Each is a one-line invariant you check against your final number.

$$0\le P(\cdot)\le 1,\qquad \Var(\cdot)\ge 0,\qquad \SD=\sqrt{\Var}\ge 0,\qquad \E[\text{payment}]\le \E[\text{loss}].$$
$$\mu_{\text{per payment}}\ \ge\ \mu_{\text{per loss}},\qquad \text{a weighted average lies between its smallest and largest input.}$$

Plus **support consistency**: no probability mass may sit outside the variable's stated range — if $X\in[0,4]$, an answer that implies $P(X>4)>0$ is wrong.

**Beat 6 — Generalize: the closing checklist.** Every problem type has its guardrail, and they share one form — *a quantity that cannot legally leave a fixed region.* So the general rule is a single closing question applied to whatever you computed: **"Is this number inside the region its quantity is allowed to live in?"** Probability $\to [0,1]$; variance/SD $\to [0,\infty)$; per-payment mean $\ge$ per-loss mean; a law-of-total-probability or mixture answer $\to$ between its extremes; any value $\to$ inside the variable's support. One question, asked last, every time.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* a probability of $1.4$ — instantly impossible, recheck.
- *Twist (a plausible-but-wrong value):* a weighted average that lands *outside* its inputs. If three super-effective rates are $0.3,0.6,0.1$ and your "overall" comes out $0.7$, it's wrong — a weighted average must sit in $[0.1,0.6]$. The number *looks* fine; only the bound exposes it.
- *Edge (right range, still check the direction):* $P(T>30)$ for a variable with mean $20$ should be **below** $0.5$ (you're asking about the upper tail past the mean). If you get $0.76$, you likely computed $\Phi$ instead of $1-\Phi$ — a sign-of-the-tail slip the range check alone won't catch, but the *direction* check will.

**Beat 8 — Picture it.** Each quantity has a legal corridor; an answer outside it is a red flag.

<figure>
<img src="../../assets/diagrams/ch15_sanity_corridors.png" alt="A column of number lines, one per quantity, each shading its legal corridor and marking a sample impossible answer outside it. Probability: corridor [0,1], a red X at 1.4. Variance: corridor [0, infinity), a red X at -3. Per-payment vs per-loss mean: an arrow showing payment must sit at or below loss, a red X where payment 8 exceeds loss 5. Weighted average: a corridor between the smallest and largest input rate, a red X outside it. Each red X is captioned 'recheck before bubbling.'" style="width:80%; max-width:560px; display:block; margin:1em auto;">
<figcaption>Standing sanity corridors: every quantity has a region it cannot leave. An answer outside the corridor is a guaranteed error — recheck before you bubble.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now make a guardrail scan the fixed last step of every problem, so an impossible answer never reaches a bubble. Combined with the budget (Concept 1), recognition (Concept 2), and the catalog (Concept 3), this completes the execution skill set the exam actually grades.

::: pokedex-entry
**POKÉDEX ENTRY №15·4 — Standing Sanity Checks**

Run the relevant guardrail on every final number, before bubbling:

$$0\le P(\cdot)\le 1,\quad \Var(\cdot)\ge 0,\quad \E[\text{payment}]\le \E[\text{loss}],\quad \mu_{\text{per payment}}\ge\mu_{\text{per loss}},$$
$$\text{(weighted average between its extremes)},\quad \text{(no mass outside the support)},\quad \text{(tail past the mean }<0.5).$$

*In plain terms:* most wrong multiple-choice answers are *impossible*, not merely incorrect — a negative variance, a probability above one, a payment beating the loss. A two-second check eliminates them.

*Recognition cue:* the instant you compute a final number, ask **"could a sane risk look like this?"** If not, you made a sign or formula error — recheck before bubbling.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/blue.png" alt="Gary Oak, the Champion" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Gary Oak — the Champion, your final benchmark</figcaption>
</figure>

Four examples model the *recognition-then-execution* loop on **unlabeled, mixed** problems — exactly the Champion's gauntlet. Watch how the archetype is named **first**, the shortcut deployed, the sanity check closing each one. They fade from fully narrated to exam speed.

### Worked Example 15.1 — A Hidden Poisson (full narration; recognition-first)

**ARCHETYPE:** *Poisson count, "at least" via complement.*

**Setup (in-world).** Gary leads with a flock count: "On Route 1, Spearow swoop in at an average rate of $3$ per minute, independently. In a given minute, what's the probability *at least two* swoop in?"

**Step 1 — Recognize (read the last sentence, find the tell).** The last sentence asks for $P(\text{at least }2)$. Two tells: **"average rate per minute"** $\Rightarrow$ Poisson with $\lambda=3$; **"at least two"** $\Rightarrow$ complement of the low values $\{0,1\}$. Tools named — Poisson and complement — *before any computing.*

**Step 2 — Professor's Path (why the complement).** Directly, $P(N\ge 2)=\sum_{k\ge 2}P(N=k)$ is an infinite sum. But $\{N\ge 2\}$ is the complement of the finite set $\{0,1\}$, so
$$P(N\ge 2) = 1 - P(0) - P(1).$$
For $\Poisson(\lambda)$, $P(k)=e^{-\lambda}\lambda^{k}/k!$, so $P(0)=e^{-3}$ and $P(1)=3e^{-3}$.

**Step 3 — Trainer's Path (fast).**
$$P(N\ge 2) = 1 - e^{-3} - 3e^{-3} = 1 - 4e^{-3}.$$
With $e^{-3}\approx 0.049787$: $\;1 - 4(0.049787) = 1 - 0.19915 \approx \mathbf{0.8009}.$

**Step 4 — Check & pitfall.** $0.8009\in[0,1]$ ✓ (guardrail). **Pitfall:** computing $1-P(1)$ and forgetting $P(0)$ — "at least two" must complement *both* low values. *(Back-ref: Entries №15·2, №15·3.)*

### Worked Example 15.2 — A Disguised Bayes (partial guidance)

**ARCHETYPE:** *Two-way Bayes / false-positive (low base rate).*

**Setup (in-world).** "A wild Pokémon is Ghost-type with probability $0.02$," Gary says. "Your Pokédex flags a true Ghost correctly $95\%$ of the time, but false-flags a non-Ghost as Ghost $10\%$ of the time. It just flagged this one. What's the probability it's *actually* a Ghost?"

**Identify.** Want $P(G\given +)$, given $P(+\given G)=0.95$ — the **bar is flipped**, so this is Bayes, not a lookup. Givens: prior $P(G)=0.02$, sensitivity $P(+\given G)=0.95$, false-positive $P(+\given G^c)=0.10$. *Your move: grid it.*

| Cause | Prior | $P(+\given\cdot)$ | Joint |
|---|---|---|---|
| $G$ (Ghost) | $0.02$ | $0.95$ | $0.0190$ |
| $G^c$ (not) | $0.98$ | $0.10$ | $0.0980$ |
| **Total** | | | $0.1170$ |

$$P(G\given +) = \frac{0.0190}{0.1170} \approx \mathbf{0.1624}.$$

**Check & pitfall.** Despite a "$95\%$-accurate" detector, the posterior is only $\approx 16\%$ — the base-rate effect: Ghosts are so rare ($2\%$) that the flood of false flags from the $98\%$ non-Ghosts swamps the true ones. **Pitfall:** the **prosecutor's fallacy** — quoting the $0.95$ sensitivity as the answer. *(Back-ref: Entry №15·2.)*

### Worked Example 15.3 — The Gamma Integral You Almost Did by Parts (light guidance)

**ARCHETYPE:** *gamma-family expectation via kernel recognition.*

**Setup (in-world).** Gary smirks: "Charizard's flame burns for $X$ minutes where $f(x)=\tfrac{1}{16}x\,e^{-x/4}$ for $x>0$. Find $\E[X]$."

**Identify & solve.** The density $\propto x^{2-1}e^{-x/4}$ is a $\GammaDist(\alpha=2,\theta=4)$ kernel, so $\E[X]=\alpha\theta=2\cdot 4=\mathbf{8}$. (Verify the constant: $\tfrac{1}{\Gamma(2)\,4^{2}}=\tfrac{1}{16}$ ✓.) The longer-but-no-parts route, via the gamma integral:
$$\E[X]=\int_0^\infty x\cdot\tfrac{1}{16}x e^{-x/4}\,dx = \tfrac{1}{16}\int_0^\infty x^{3-1}e^{-x/4}\,dx = \tfrac{1}{16}\,\Gamma(3)\,4^{3} = \tfrac{1}{16}(2)(64) = 8.$$

**Check & pitfall.** $\E[X]=8=\alpha\theta$ ✓. **Pitfall:** integrating $x\cdot xe^{-x/4}$ by parts under the clock when the gamma integral $\int_0^\infty x^{n-1}e^{-x/\theta}dx=\Gamma(n)\theta^{n}$ collapses it instantly. *(Back-ref: Entry №15·3.)*

### Worked Example 15.4 — A CLT That Needs the Continuity Correction (exam speed)

**ARCHETYPE:** *CLT normal approximation to a binomial, with continuity correction.*

**Setup (in-world).** "The League runs $100$ independent exhibition matches," Gary says. "Each has probability $0.3$ of an upset, independently. Approximate the probability of *at most $25$* upsets."

**Solve.** $S\sim\Binom(100,0.3)$: $\mu=np=30$, $\sigma^2=np(1-p)=21$, $\sigma=\sqrt{21}\approx 4.583$. Discrete $\Rightarrow$ continuity correction at $25.5$:
$$P(S\le 25)\approx \Phi\!\left(\frac{25.5-30}{4.583}\right)=\Phi(-0.982)\approx \mathbf{0.163}.$$

**Check & pitfall.** $0.163\in[0,1]$ ✓, and *below* $0.5$ since $25<\mu=30$ ✓ (direction check). **Pitfall:** skipping the $+0.5$ correction — without it you'd standardize at $25$, get $\Phi(-1.091)\approx 0.138$, and land in a different answer band. *(Back-ref: Entries №15·2, №15·3.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — Make the calculator do the counting**

On the **TI-30XS MultiView**: for combinations/permutations type the first count, press `prb` $\to$ `nCr` (or `nPr`), then the second count — far faster and less error-prone than expanding factorials. For a pmf-weighted mean, enter the values in `L1`, probabilities in `L2`, then `2nd stat` $\to$ `1-Var Stats` reads $\bar{x}$ (the mean) and $\sigma$ straight off the lists.
:::

::: trainers-tip
**TRAINER'S TIP — Kill rounding drift with `STO→`**

Store intermediate results ($\sigma$, $X\wedge u$, $S(d)$) into variables `x`, `y`, `z` and **recall** them rather than retyping rounded decimals. A two-decimal intermediate can push a borderline answer into the wrong choice — and Exam P's answer choices are often a hair apart *on purpose*.
:::

::: trainers-tip
**TRAINER'S TIP — Bring a second cleared calculator, and read the last sentence first**

Bring a **second, cleared** calculator (TI-30XS *or* BA II Plus — both are allowed); a dead battery mid-exam is otherwise fatal. Clear the memory the **night before** so it's not a panic at the door. And on every stem, read the **last sentence first** — it tells you which number to chase, so you read the rest knowing what you're hunting.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

Jessie, James, and Meowth are sitting their *own* mock exam to "qualify" for a Rocket promotion. Twenty minutes in, James announces he's spent the whole time on Question 3 — a nasty double integral — because "we never leave a problem unfinished, that's not the Rocket way!" Meowth, panicking at the clock, starts *leaving the last five blank* rather than reading them: "No time, skip 'em, leave 'em empty." Jessie, meanwhile, refuses to flag anything: "Champions don't go *back.*" They finish $11$ of $30$, leave four blank, and bomb the time-management gate entirely.

**Where it fails:** all three broke the budget rule (Entry №15·1). James fed one monster twelve minutes that should have harvested three gifts. Meowth left blanks when a guess **strictly dominates** an empty bubble — there is *no penalty* for a wrong answer. Jessie's no-flagging pride threw away the entire two-pass advantage. **The fix:** cap any single problem at $\sim\!6$ minutes (flag and move), bubble *every* question even if it's a guess, and run two passes — gifts first, flags second. Pacing is a skill you drill, not a virtue you boast about.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

Working actuaries are judged on **accuracy under deadline**, exactly as you are on exam day. A pricing analyst handing a quote to an underwriter has minutes, not hours, and the very same guardrails apply: a loss cost can't be negative, a retention can't exceed the limit, an expected recovery can't beat the ceded premium — the same standing sanity checks (Entry №15·4) you run on every bubble.

The **two-pass strategy** is how analysts triage a model run: nail the cells you trust, flag the anomalies, circle back — never let one stubborn figure stall the whole deliverable. And the **error log** this chapter's mocks build (classify every miss by root cause, then retest it) is precisely the peer-review discipline a reserving actuary uses so a single sign error never ships to a customer.

*Series bridge:* this error-log-and-sanity-check habit carries straight into **CAS Exam 5** ratemaking and reserving, where one unchecked sign error can misprice an entire book of business.

*Transfer check:* strip the Pokémon out and the skill is identical — "thirty mixed actuarial problems, three hours, recognize the archetype, deploy the shortcut, sanity-check the answer, never blank." If you can run that loop with no Pikachu in sight, the skill has transferred — and that *is* Exam P.
:::

## The Gym Battle — Champion's Capstone

<figure style="margin:1.5em auto; max-width:130px; text-align:center;">
<img src="../../assets/sprites/front/6.png" alt="Charizard, Gary's ace" style="width:110px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#006 Charizard</strong> — the Champion's ace</figcaption>
</figure>

**Setup (in-world).** For the final turn, Gary sends out Charizard and stacks one integrative problem that braids three chapters into a single back-of-exam monster — exactly what the SOA buries near the end. "Aggregate claim cost," he calls it.

Over one tournament day, the **number** of injuries $N$ at the Pokémon Center is Poisson with mean $\lambda=4$. Each injury's **recovery cost** $X_i$ (thousands of Poké-dollars) is independent of $N$ and of each other, exponential with mean $\theta=5$. Let $T=\sum_{i=1}^{N}X_i$ be the day's **aggregate cost** (with $T=0$ if $N=0$). Gary wants three numbers: (1) $\E[T]$, (2) $\Var(T)$, and (3) by the normal approximation, $P(T>30)$.

**ARCHETYPE:** *compound Poisson aggregate — total expectation, total variance, then CLT.* Three tells, named first: Poisson frequency + exponential severity + "normal approximation of an aggregate."

**Step 1 — Identify and gather the severity moments.** $T$ is a compound distribution: a random number $N\sim\Poisson(4)$ of i.i.d. severities $X_i\sim\Expo(5)$. For an exponential, $\E[X]=\theta=5$ and $\E[X^2]=2\theta^2=50$ (gamma-integral shortcut, Entry №15·3), so $\Var(X)=50-25=25$.

**Step 2 — Professor's Path (the laws, then why they collapse).** By the **law of total expectation**, a compound mean is $\E[T]=\E[N]\,\E[X]$:
$$\E[T]=\lambda\,\E[X]=4\cdot 5=\mathbf{20}\ \text{(thousand)}.$$
By the **law of total variance**, the general compound variance is $\Var(T)=\E[N]\Var(X)+\Var(N)\,\E[X]^2$. For a **Poisson** frequency, $\E[N]=\Var(N)=\lambda$, which collapses it to the clean compound-Poisson result $\Var(T)=\lambda\,\E[X^2]$. Verify both forms agree:
$$\Var(T)=\underbrace{\E[N]\Var(X)}_{4(25)=100}+\underbrace{\Var(N)\E[X]^2}_{4(25)=100}=200 \;=\; \underbrace{\lambda\,\E[X^2]}_{4(50)}=\mathbf{200}.$$
The two halves — process variance from severity ($100$) and from frequency ($100$) — sum to $200$, confirming the $\lambda\,\E[X^2]$ shortcut. So $\SD(T)=\sqrt{200}\approx 14.142$.

**Step 3 — Trainer's Path (the tail via CLT).** Approximate $T$ as $\Normal(20,\,200)$. The aggregate is **continuous**, so **no** continuity correction:
$$P(T>30)\approx 1-\Phi\!\left(\frac{30-20}{14.142}\right)=1-\Phi(0.707)\approx 1-0.7602=\mathbf{0.240}.$$

**Step 4 — Check & the three pitfalls Gary built in.** Guardrails: $\E[T]=20>0$ ✓; $\Var(T)=200\ge 0$ ✓; $P(T>30)=0.24\in[0,1]$ and *below* $0.5$ since $30>\mu=20$ ✓ (direction check). The three traps this problem is engineered to catch: **(1)** using $\Var(T)=\lambda\Var(X)=100$, forgetting the frequency contribution — only valid if severity were constant; **(2)** applying a continuity correction to a *continuous* aggregate; **(3)** computing $\E[X^2]=\theta^2=25$ instead of $2\theta^2=50$ for an exponential. Beat all three guardrails and the Champion is yours.

> "That," Gary says, the half-smile finally honest, "is how you read a problem you've never seen. You named all three tools before you touched the pencil. Grandpa was right about you." Pikachu's cheeks spark in triumph.

<figure>
<img src="../../assets/badges/earth_badge.png" alt="All eight badges arrayed beneath the Indigo League Champion crest." style="width:150px; display:block; margin:1.5em auto;">
<figcaption class="badge-caption"><strong>Indigo League Champion — the journey complete.</strong></figcaption>
</figure>

## The Gym Challenge — Three Mock Exams

::: problem-set
**TEST-OUT INSTRUCTIONS.** This is the real thing: three **30-question, 3-hour mock exams**, each weight-matched to the live Exam P syllabus (≈8 General Probability / ≈14 Univariate / ≈8 Multivariate per 30). Work each mock **timed, in one sitting**, with only the provided normal table and a cleared calculator. Score it against the **Answer Key** below (problems first, full solutions after — never interleaved). **Readiness gate: 24/30 with correct method and six-minute pacing, on all three mocks.** Hit it and you are Exam-P ready; miss it and the diagnostic names the chapter waiting for you. Problems are numbered **C15.k** across all three mocks; markers: 🔴 Poké Ball = under-two-minute mechanics · 🟡 true SOA difficulty · 🔵 integrative / back-of-exam stretch.

### Route Trainers (recognition-speed mechanics)

**C15.1.** 🔴 *(Mock A — opening flock.)* On Route 1, Spearow arrive at an average rate of $\lambda=3$ per minute (Poisson, independent). In one minute, find $P(\text{at least }2)$.

**C15.2.** 🔴 *(Mock A — the Pokédex flag.)* A wild Pokémon is Ghost-type with prior $0.02$; the Pokédex flags a true Ghost with probability $0.95$ and false-flags a non-Ghost with probability $0.10$. It just flagged one. Find $P(\text{Ghost}\given\text{flagged})$.

**C15.3.** 🔴 *(Mock A — Charizard's flame.)* A Charizard's flame lasts $X$ minutes with density $f(x)=\tfrac{1}{16}xe^{-x/4}$, $x>0$. Find $\E[X]$.

**C15.4.** 🟡 *(Mock B — fishing without replacement.)* Misty's tank holds $10$ Magikarp and $5$ Goldeen. She nets $4$ fish at once (no replacement). Find $P(\text{exactly }2\text{ Goldeen})$.

**C15.5.** 🔴 *(Mock B — the slot streak.)* At the Celadon Game Corner each pull wins independently with probability $0.2$. Find $P(\text{first win on the 4th pull})$.

**C15.6.** 🔴 *(Mock B — Sabrina's reading.)* A psychic-power reading $X$ is $\Normal(\mu=50,\sigma^2=64)$. Find $P(X>62)$ using the provided $Z$-table.

**C15.7.** 🟡 *(Mock C — the warm-up quote.)* A fled Pokémon's gear cost $X\sim\Expo(\theta=4)$ (thousands). With ordinary deductible $d=2$, find the expected payment **per loss**.

**C15.8.** 🔴 *(Mock C — two dice on the Game Corner table.)* Roll two fair six-sided dice. Find $P(\text{sum}=7\text{ or sum}=11)$.

**C15.9.** 🔴 *(Mock C — uniform territory.)* A Pokémon's roaming distance $X$ is $\Unif(0,10)$ km. Find $\Var(X)$.

**C15.10.** 🔴 *(Mock A — MGF read-off.)* A random reward has MGF $M(t)=e^{3t+2t^2}$. Identify the distribution and find $\Var$.

**C15.11.** 🔴 *(Mock B — memoryless recovery.)* A fainted Pokémon's recovery time is $\Expo(\theta=10)$ minutes. Given it has already rested $4$ minutes, find $P(\text{at least }6\text{ more minutes needed})$.

**C15.12.** 🔴 *(Mock C — an ordered line-up.)* From $8$ caught Pokémon, how many distinct **ordered** battle line-ups of $3$ can Ash field?

### Gym Battles (true SOA difficulty)

**C15.13.** 🟡 *(Mock A — the upset count.)* The League runs $100$ independent exhibition matches, each an upset with probability $0.3$. Using the normal approximation **with continuity correction**, find $P(\text{at most }25\text{ upsets})$.

**C15.14.** 🟡 *(Mock A — full Safari policy.)* Loss $X\sim\Expo(\theta=8)$ (thousands), ordinary deductible $d=2$, maximum covered loss $u=10$, coinsurance $\alpha=0.8$. Find the expected payment **per loss**.

**C15.15.** 🟡 *(Mock A — the strongest challenger.)* Five independent challengers each have strength $X_i\sim\Unif(0,1)$. Find the expected strength of the **strongest**.

**C15.16.** 🟡 *(Mock A — joint over a triangle.)* $(X,Y)$ has joint density $f(x,y)=2$ on $\{0<x<y<1\}$. Find $P(Y<2X)$.

**C15.17.** 🔵 *(Mock B — Bayes with a continuous twist.)* A coin's bias $P$ is $\Unif(0,1)$. Given $P=p$, a flip is heads with probability $p$. A single flip is heads. Find $\E[P\given\text{heads}]$.

**C15.18.** 🟡 *(Mock B — variance of a deductible payment.)* Loss $X\sim\Expo(\theta=4)$, ordinary deductible $d=2$, no limit, $\alpha=1$. For the per-loss payment $Y=(X-2)_{+}$, find $\Var(Y)$.

**C15.19.** 🟡 *(Mock B — sum of independent normals.)* Two teammates' contributions are independent: $A\sim\Normal(20,16)$ and $B\sim\Normal(30,9)$. Find $P(A+B>60)$.

**C15.20.** 🟡 *(Mock B — conditional expectation.)* $X$ has density $f(x)=\tfrac{x}{8}$ on $0<x<4$. Find $\E[X\given X>2]$.

**C15.21.** 🟡 *(Mock B — covariance of a linear combination.)* For $X,Y$ with $\Var(X)=4$, $\Var(Y)=9$, $\Corr(X,Y)=0.5$, find $\Var(2X-Y)$.

**C15.22.** 🟡 *(Mock C — Poisson superposition.)* Pidgey arrive at rate $2$/hr and Spearow at rate $3$/hr, independent Poisson processes. Find $P(\text{exactly }4\text{ birds total in one hour})$.

**C15.23.** 🟡 *(Mock C — gamma tail via the Poisson-sum identity.)* $X\sim\GammaDist(\alpha=2,\theta=3)$. Find $P(X>6)$.

**C15.24.** 🔴 *(Mock C — the master identity.)* The warden tells you $\E[X]=10$ and $X\wedge 8$ has mean $6.2$ (thousands). Find $\E[(X-8)_{+}]$.

**C15.25.** 🟡 *(Mock C — total expectation, mixture.)* With probability $0.6$ a battle is "short," damage $\Expo(\text{mean }3)$; with probability $0.4$ it is "long," damage $\Expo(\text{mean }8)$. Find the overall expected damage.

**C15.26.** 🟡 *(Mock C — beta proportion.)* The fraction $X$ of a potion that is active ingredient is $\BetaDist(\alpha=2,\beta=3)$. Find $\E[X]$ and $\Var(X)$.

### Elite Challenge (integrative / back-of-exam stretch)

**C15.27.** 🔵 *(Mock A — the Champion's aggregate.)* Daily injuries $N\sim\Poisson(\lambda=4)$; each recovery cost $X_i\sim\Expo(\theta=5)$ (thousands), independent. For aggregate $T=\sum_{i=1}^N X_i$, find $\E[T]$, $\Var(T)$, and (normal approximation) $P(T>30)$.

**C15.28.** 🔵 *(Mock B — minimum of exponentials, reliability.)* A trainer's three independent gadgets have lifetimes $\Expo$ with means $4$, $6$, and $12$ hours. The system fails when the **first** gadget fails (series). Find the expected time to first failure.

**C15.29.** 🔵 *(Mock C — double expectation with total variance.)* The number of grunts $N\sim\Poisson(\lambda=3)$. Given $N=n$, each grunt's strength is i.i.d. with mean $2$ and variance $5$; let $S$ be the total strength. Find $\E[S]$ and $\Var(S)$.

**C15.30.** 🔵 *(Mock C — the final integrative turn.)* Claim counts per policy are $\Poisson(\lambda=0.5)$. A portfolio holds $400$ independent policies; let $M$ be the **total** number of claims. (a) Find $\E[M]$ and $\Var(M)$. (b) Using the normal approximation **with continuity correction**, find $P(M\ge 210)$.
:::

## Answer Key

::: answer-key
**Full worked solution for every problem, in C15.k order, each labeled with its archetype and the chapter / Pokédex Entry it draws on. A quick-answer table closes the section.**

**C15.1** — *Poisson, "at least" via complement (Ch 8; Entry №15·2).*
$$P(N\ge 2)=1-e^{-3}-3e^{-3}=1-4e^{-3}\approx 1-0.19915=\mathbf{0.8009}.$$

**C15.2** — *Two-way Bayes / false-positive (Ch 5; WE 15.2).*
$$P(G\given +)=\frac{0.95(0.02)}{0.95(0.02)+0.10(0.98)}=\frac{0.0190}{0.1170}\approx \mathbf{0.1624}.$$

**C15.3** — *gamma-kernel expectation (Ch 7; WE 15.3).* $f$ is $\GammaDist(2,4)$, so $\E[X]=\alpha\theta=2\cdot 4=\mathbf{8}.$

**C15.4** — *hypergeometric, without replacement (Ch 8; Entry №15·2).*
$$P=\frac{\binom{5}{2}\binom{10}{2}}{\binom{15}{4}}=\frac{10\cdot 45}{1365}=\frac{450}{1365}\approx \mathbf{0.3297}.$$

**C15.5** — *geometric wait-time (Ch 8).* First success on trial $4$: $(1-p)^3 p=(0.8)^3(0.2)=0.512(0.2)=\mathbf{0.1024}.$

**C15.6** — *normal standardization (Ch 7).* $Z=\tfrac{62-50}{8}=1.5$; $P(X>62)=1-\Phi(1.5)=1-0.9332=\mathbf{0.0668}.$

**C15.7** — *per-loss exponential deductible, memorylessness (Ch 10; Entry №15·3).* $\E[(X-2)_{+}]=\theta e^{-d/\theta}=4e^{-0.5}\approx \mathbf{2.426}$ thousand.

**C15.8** — *equally-likely outcomes, mutually-exclusive union (Ch 5).* Sum $7$: $6$ ways; sum $11$: $2$ ways; disjoint over $36$: $P=\tfrac{6+2}{36}=\tfrac{8}{36}\approx \mathbf{0.2222}.$

**C15.9** — *uniform variance (Ch 7).* $\Var(X)=\tfrac{(10-0)^2}{12}=\tfrac{100}{12}\approx \mathbf{8.333}.$

**C15.10** — *MGF kernel recognition (Ch 7; Entry №15·3).* $M(t)=e^{\mu t+\sigma^2 t^2/2}$ with $\mu=3$, $\sigma^2/2=2\Rightarrow\sigma^2=4$. Normal; $\Var=\mathbf{4}.$

**C15.11** — *exponential memorylessness (Ch 8; Entry №15·3).* $P(X>4+6\given X>4)=P(X>6)=e^{-6/10}=e^{-0.6}\approx \mathbf{0.5488}.$

**C15.12** — *ordered count, permutation (Ch 4).* $P(8,3)=8\cdot 7\cdot 6=\mathbf{336}.$

**C15.13** — *CLT binomial + continuity correction (Ch 14; WE 15.4).* $S\sim\Binom(100,0.3)$, $\mu=30$, $\sigma=\sqrt{21}\approx 4.583$. $P(S\le 25)\approx\Phi\!\big(\tfrac{25.5-30}{4.583}\big)=\Phi(-0.982)\approx \mathbf{0.163}.$

**C15.14** — *full loss policy, exponential (Ch 10).* $X\wedge 10$ has mean $8(1-e^{-1.25})\approx 5.708$; $X\wedge 2$ has mean $8(1-e^{-0.25})\approx 1.770$. $\E[Y_L]=0.8(5.708-1.770)=0.8(3.938)\approx \mathbf{3.151}$ thousand.

**C15.15** — *maximum order statistic, uniform (Ch 14).* For $\Unif(0,1)$, $\E[\max]=\tfrac{n}{n+1}=\tfrac{5}{6}\approx \mathbf{0.8333}.$ (Or $F_{\max}(x)=x^5$, density $5x^4$, $\E=\int_0^1 5x^5\,dx=5/6$.)

**C15.16** — *double integral over a region (Ch 11).* On $0<x<y<1$ with $f=2$, $P(Y<2X)$ is the part of the triangle with $y<2x$, i.e. $x<y<2x$ intersected with $y<1$. Split at $x=\tfrac12$:
$$\int_0^{1/2}\!\!\int_x^{2x}\!2\,dy\,dx+\int_{1/2}^{1}\!\!\int_x^{1}\!2\,dy\,dx=\int_0^{1/2}\!2x\,dx+\int_{1/2}^1\!2(1-x)\,dx=\tfrac14+\tfrac14=\mathbf{0.5}.$$

**C15.17** — *Bayesian posterior mean, beta update (Ch 5 / Ch 9).* Posterior $\propto p\cdot 1$ on $(0,1)$, i.e. $\BetaDist(2,1)$ with density $2p$. $\E[P\given H]=\int_0^1 p\cdot 2p\,dp=\tfrac{2}{3}\approx \mathbf{0.6667}.$

**C15.18** — *variance of a per-loss deductible payment, exponential (Ch 10).* $Y=0$ w.p. $1-e^{-0.5}$; given $Y>0$, $Y\sim\Expo(4)$ (memorylessness). $\E[Y]=4e^{-0.5}\approx 2.426$; $\E[Y^2]=e^{-0.5}\cdot 2\theta^2=32e^{-0.5}\approx 19.41$. $\Var(Y)=19.41-2.426^2\approx 19.41-5.89=\mathbf{13.52}.$

**C15.19** — *sum of independent normals (Ch 13).* $A+B\sim\Normal(50,25)$, $\sigma=5$. $P(A+B>60)=1-\Phi\!\big(\tfrac{60-50}{5}\big)=1-\Phi(2)=1-0.9772=\mathbf{0.0228}.$

**C15.20** — *conditional expectation from a density (Ch 11/12).* $P(X>2)=\int_2^4\tfrac{x}{8}\,dx=\tfrac{1}{16}(16-4)=0.75$. $\E[X;X>2]=\int_2^4 x\cdot\tfrac{x}{8}\,dx=\tfrac{1}{24}(64-8)=\tfrac{56}{24}\approx 2.333$. $\E[X\given X>2]=2.333/0.75\approx \mathbf{3.111}.$

**C15.21** — *variance of a linear combination (Ch 13).* $\Cov(X,Y)=0.5\sqrt{4\cdot 9}=3$. $\Var(2X-Y)=4\Var(X)+\Var(Y)-2(2)\Cov(X,Y)=16+9-12=\mathbf{13}.$

**C15.22** — *superposition of independent Poissons (Ch 8 / Ch 13).* Total $\sim\Poisson(2+3=5)$. $P(=4)=\tfrac{e^{-5}5^4}{4!}=\tfrac{e^{-5}(625)}{24}\approx \tfrac{0.0067379(625)}{24}\approx \mathbf{0.1755}.$

**C15.23** — *gamma tail via the Poisson-sum identity (Ch 7).* $X\sim\GammaDist(2,3)$ (integer shape): $P(X>6)=e^{-6/3}\big(1+\tfrac{6}{3}\big)=e^{-2}(3)=3e^{-2}\approx \mathbf{0.4060}.$

**C15.24** — *the master identity (Ch 10).* $\E[(X-8)_{+}]=\E[X]-\E[X\wedge 8]=10-6.2=\mathbf{3.8}$ thousand.

**C15.25** — *law of total expectation, mixture (Ch 12).* $\E[D]=0.6(3)+0.4(8)=1.8+3.2=\mathbf{5.0}.$

**C15.26** — *beta moments (Ch 9).* $\E[X]=\tfrac{\alpha}{\alpha+\beta}=\tfrac{2}{5}=\mathbf{0.4}$; $\Var(X)=\tfrac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}=\tfrac{6}{25\cdot 6}=\tfrac{1}{25}=\mathbf{0.04}.$

**C15.27** — *compound Poisson + CLT (Ch 12 + Ch 14; Gym Battle capstone).* $\E[T]=\lambda\E[X]=4(5)=\mathbf{20}$. $\Var(T)=\lambda\E[X^2]=4(50)=\mathbf{200}$, $\SD\approx 14.142$. $P(T>30)\approx 1-\Phi\!\big(\tfrac{30-20}{14.142}\big)=1-\Phi(0.707)\approx 1-0.7602=\mathbf{0.240}.$ (No continuity correction — $T$ is continuous.)

**C15.28** — *minimum of independent exponentials / series reliability (Ch 14).* Rates $\tfrac14,\tfrac16,\tfrac1{12}$; the minimum is $\Expo$ with total rate $\tfrac14+\tfrac16+\tfrac1{12}=\tfrac{3+2+1}{12}=\tfrac12$. $\E[\min]=1/r=\mathbf{2}$ hours.

**C15.29** — *double expectation + total variance, compound (Ch 12).* $\E[S]=\E[N]\cdot 2=3(2)=\mathbf{6}$. $\Var(S)=\E[N]\Var(\text{str})+\Var(N)\E[\text{str}]^2=3(5)+3(2^2)=15+12=\mathbf{27}$ (Poisson $N$, so $\E[N]=\Var(N)=3$; equals $\lambda\E[\text{str}^2]=3(5+4)=27$).

**C15.30** — *i.i.d. Poisson sum + CLT with continuity correction (Ch 8 + Ch 14; integrative).*
(a) $M\sim\Poisson(400\cdot 0.5=200)$, so $\E[M]=\mathbf{200}$, $\Var(M)=\mathbf{200}$, $\sigma=\sqrt{200}\approx 14.142$.
(b) Discrete, so correct at $209.5$: $P(M\ge 210)\approx 1-\Phi\!\big(\tfrac{209.5-200}{14.142}\big)=1-\Phi(0.672)\approx 1-0.7492=\mathbf{0.2508}.$

### Quick-Answer Table

| # | Answer | | # | Answer |
|---|---|---|---|---|
| C15.1 | $1-4e^{-3}\approx 0.8009$ | | C15.16 | $0.5$ |
| C15.2 | $\approx 0.1624$ | | C15.17 | $2/3\approx 0.6667$ |
| C15.3 | $8$ | | C15.18 | $\approx 13.52$ |
| C15.4 | $\approx 0.3297$ | | C15.19 | $0.0228$ |
| C15.5 | $0.1024$ | | C15.20 | $\approx 3.111$ |
| C15.6 | $0.0668$ | | C15.21 | $13$ |
| C15.7 | $4e^{-0.5}\approx 2.426$ | | C15.22 | $\approx 0.1755$ |
| C15.8 | $8/36\approx 0.2222$ | | C15.23 | $3e^{-2}\approx 0.4060$ |
| C15.9 | $100/12\approx 8.333$ | | C15.24 | $3.8$ |
| C15.10 | $\Var=4$ | | C15.25 | $5.0$ |
| C15.11 | $e^{-0.6}\approx 0.5488$ | | C15.26 | $\E=0.4,\ \Var=0.04$ |
| C15.12 | $336$ | | C15.27 | $20;\ 200;\ \approx 0.240$ |
| C15.13 | $\approx 0.163$ | | C15.28 | $2$ hours |
| C15.14 | $\approx 3.151$ | | C15.29 | $\E[S]=6,\ \Var(S)=27$ |
| C15.15 | $5/6\approx 0.8333$ | | C15.30 | $200,200;\ \approx 0.2508$ |
:::

## Badge Earned — Mastery Checklist

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/earth_badge.png" alt="All eight badges; Indigo League Champion crest." style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Indigo League Champion — Exam P Ready!</strong></figcaption>
</figure>

You earn the **Indigo League Champion** title — and declare yourself Exam-P ready — when you can, unaided:

1. **Pace** a 30-question mock in 3 hours at $\sim\!6$ minutes per question, running the two-pass strategy and **never leaving a blank**. *(Entry №15·1.)*
2. **Recognize** a problem's archetype from the stem alone — no topic label — and name the matching tool *before* computing. *(Entry №15·2.)*
3. **Deploy** each shortcut on sight: gamma integral, Darth Vader/survival rule, MGF kernel-matching, exponential memorylessness, Poisson $\mu=\sigma^2=\lambda$, binomial$\to$Poisson, continuity correction. *(Entry №15·3.)*
4. **Run** the standing sanity checks ($P\in[0,1]$, $\Var\ge 0$, $\E[\text{payment}]\le\E[\text{loss}]$, support consistency, tail-past-mean $<0.5$) so an impossible answer is never bubbled. *(Entry №15·4.)*
5. **Score** $24/30$ or better, with correct method and six-minute pacing, on **all three** mock exams.

> **Gym rematch (🧴 Potion).** Miss item 1 or 5 $\to$ the issue is pacing; redo a mock with a hard six-minute timer and an error log. Miss item 2 $\to$ drill the recognition map (Concept 2) until it's reflexive. Miss item 3 $\to$ return to each shortcut's home chapter (gamma/MGF/survival $\to$ Ch 7, memorylessness/Poisson $\to$ Ch 8, loss models $\to$ Ch 10, CLT/continuity $\to$ Ch 14). Miss item 4 $\to$ you're computing right but not *checking*; make the guardrail scan a fixed last step on every problem.

*The journey from Pallet Town is complete. Eight badges, the Elite Four, the Champion — all behind you. Walk into the real exam the way you walked into this chamber: you have seen every move before, you recognize the type on sight, and you do not let one number bully you. Go earn your 10.*

---

<!-- ===== CALLOUT BOX TEMPLATES (Pandoc fenced divs; styled by book/theme.css) =====
     ::: cold-open / pokedex-entry / trainers-tip / team-rocket / kanto-realworld
     Concept gate ("Do you already own this?") also uses a styled panel.
     Wrap the problem set in ::: problem-set and the key in ::: answer-key . -->
