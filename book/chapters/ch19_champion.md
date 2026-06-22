<!--
  file: ch19_champion
  tier: finale (execution; no new theory)
  outcomes: all (1a-1g, 2a-2f, 3a-3i)
  tia: exam finale (not a TIA leaf)
  locale: Indigo Plateau — the Championship match (Ash vs Gary)
  maps_to: the whole journey, tested at once — exam strategy + three full mock exams
-->

# Champion's Challenge — Exam Strategy & Three Mock Exams {.type-dragon}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="The Kanto region map, every town and route cleared, the path running from Pallet Town all the way to the Indigo Plateau." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Kanto, end to end — eight badges earned, the whole region behind you. One chamber left: the Indigo Plateau, where everything you learned is tested at once.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "Friend and Foe Alike"**

The doors of the Indigo Plateau's championship stadium open with a sound like a held breath. You have eight badges on your belt, the Elite Four behind you, and the whole journey from Pallet Town packed into your Pokédex. And there, across the marble battlefield under the championship lights, with that infuriating half-smile, is **Gary**.

"Took you long enough, Ash." He tosses a Poké Ball and catches it. "Grandpa always said you were better at the *math* than the battling. Let's find out. No gym leader this time — no single type to study. I'm going to throw **thirty problems** at you, one after another, from everything you've ever learned. General probability, the distributions, the multivariate stuff, the loss models. Mixed. No warning which is which."

He checks an imaginary watch. "Three hours. **Six minutes a problem** if you want to finish. Get one wrong, you don't get to stop and sulk — you flag it and move on. And here's the part you'll hate: I'm not going to tell you the *topic*. You have to **recognize** it. The way a Champion reads an opponent's strategy from the first move."

Pikachu's cheeks spark. You feel the old jolt of doubt — not "do I know the formulas," but something harder. *Can you recognize which formula, instantly, under the clock, thirty times in a row, without a single panic?*

That is the whole game now. Not new theory. **Execution.** You crack your knuckles, open Actuary Mode one last time, and ask the only question that matters at the Plateau: **how do you turn everything you know into a 10, not a 6, when the clock is running and the archetype is hidden?**
:::

## Where You Are — 60-Second Retrieval

**Rank: Champion-ready · Badges: 8.** Every badge is pinned to your case — Cascade, Thunder, Boulder, Rainbow, Soul, Marsh, Volcano, and the Earth Badge you took from Giovanni in the Viridian Gym — and beyond them, the Elite Four cleared. You crossed the Plateau in the last chapters holding the final pieces: **order statistics** — the distribution of the *largest* or *smallest* of a sample, $F_{\max}(x)=[F(x)]^{n}$ and $F_{\min}(x)=1-[1-F(x)]^{n}$ — and the **Central Limit Theorem**, the promise that a sum or average of many independent pieces is approximately **normal**,

$$\bar X \;\overset{\text{approx}}{\sim}\; N\!\Big(\mu,\ \tfrac{\sigma^{2}}{n}\Big),\qquad S=\textstyle\sum X_i \;\overset{\text{approx}}{\sim}\; N\big(n\mu,\ n\sigma^{2}\big),$$

with the **continuity correction** (a $\pm 0.5$ nudge) whenever the thing you are approximating is *discrete*.

That CLT was the last new theorem in the book. This chapter teaches **no new mathematics at all** — every formula you need is already on your belt. What it teaches is the meta-skill of *using* all of it under a clock. Take sixty seconds and prove the journey still lives in your hands.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the whole journey**

Answer from memory; if any feels shaky, flip back before continuing.

1. Five independent scores are $\text{Unif}(0,1)$. What is $P(\max \le 0.8)$? *(Answer: $0.8^5 = 0.32768$.)*
2. A sum of $100$ i.i.d. pieces has mean-per-piece $3$ and variance-per-piece $4$. What are the mean and variance of the sum? *(Answer: $\mu_S=300$, $\text{Var}(S)=400$, so $\text{SD}=20$.)*
3. Approximating $P(X \le 25)$ for a *discrete* count by the normal, what number do you actually standardize at? *(Answer: $25.5$ — continuity correction.)*

All three instant? You're ready for the Plateau. Any hesitation? The retrieval *is* the lesson — go reclaim it, then come back.
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP081 "Friend and Foe Alike" + EP082 "Friends to the End"**

These two episodes are the Indigo League's climax. In **EP081 "Friend and Foe Alike,"** Ash advances into the Victory Tournament's later rounds at the Indigo Plateau, the stadium battles intensifying as the field narrows. In **EP082 "Friends to the End,"** Ash faces his rival **Ritchie** in the decisive match — the friend-and-foe theme made literal, a battle against someone who mirrors him. *Watch these alongside the chapter.* On screen the League is the whole journey tested at once, against a rival who is your equal — exactly our subject: thirty mixed problems, no topic labels, the clock running, an opponent who knows everything you know. (We cast that rival as **Gary** rather than Ritchie — the book's benchmark since Pallet Town — and the "thirty-problem mixed gauntlet" is an *in-world extension* framing the exam, not a scene from the episodes.)
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer, one last briefing</figcaption>
</figure>

Professor Oak's voice crackles through Actuary Mode as you face the championship battlefield.

"This is the only chapter, Ash, where I teach you nothing new. Every formula you need is already in Chapters 1–18. What separates a passing **6** from a perfect **10** is not knowledge — it is **execution**: pacing, recognizing an archetype on sight, deploying the right shortcut without hesitation, the discipline of a sanity check, and the refusal to ever leave a blank. The three mock exams that close this chapter are your dress rehearsal. The strategy below is the coaching that makes the rehearsal pay off. Treat *execution itself* as a skill you can drill — because it is."

By the end of this chapter you will be able to:

- **Budget** the three-hour, thirty-question sitting at **six minutes per question** and run the **two-pass strategy** — answer the recognized archetypes first, flag and return for the rest, never leaving a blank. *(Execution.)*
- **Master the calculator** — drive the TI-30XS MultiView reflexively on the handful of Exam-P key skills, banking minutes and killing rounding drift. *(Execution; §13/§18.)*
- **Recognize** each problem's archetype on sight from the *tell* in its stem, and **deploy** the matching shortcut — the gamma integral, the survival-function (Darth Vader) rule, MGF kernel-matching, exponential memorylessness, the Poisson identity $\mu=\sigma^2=\lambda$, the binomial$\to$Poisson approximation, and the continuity correction. *(Integrative, Topics 1–3.)*
- **Run** standing **sanity checks** on every answer — probabilities in $[0,1]$, variances $\ge 0$, $E[\text{payment}]\le E[\text{loss}]$, support consistency, a weighted average between its extremes. *(Execution.)*
- **Keep an error log** — classify every miss by root cause and retest it, so a recurring slip is fixed once, not re-made on exam day. *(Execution.)*
- **Sit and pass** three weight-matched mock exams under timed conditions, integrating every outcome from Topics 1–3 at once. *(All outcomes.)*

> *Exam-weight signpost.* This is the whole exam, mixed. The mocks are split the way the **live SOA Exam P** is: roughly **8 General Probability / 14 Univariate / 8 Multivariate** out of every 30. This is the **finale** — no single hard idea, but the load-bearing skill of *deploying all of them under time*, which is exactly what the real exam grades.

::: concept-gate
**CHAPTER TEST-OUT GATE — Are You Already Exam-Ready?**

This whole chapter is execution, so the test-out is execution. Set a **six-minute timer per problem** and work these four cold — different topic each, no labels, the way the real exam comes:

1. On Route 1, Spearow swoop in at an average rate of $3$ per minute (Poisson). Find $P(\text{at least }2\text{ in one minute})$.
2. A scanner flags a Ghost-type correctly $95\%$ of the time and false-flags a non-Ghost $10\%$ of the time; only $2\%$ of wild Pokémon are Ghost. It just flagged one. Find $P(\text{Ghost}\mid\text{flagged})$.
3. A density is $f(x)=\tfrac{1}{16}x\,e^{-x/4}$ for $x>0$. Find $E[X]$ **without** integrating by parts.
4. $S\sim\text{Binomial}(100,0.3)$. Using the normal approximation with continuity correction, find $P(S\le 25)$.

*(Answers: $1-4e^{-3}\approx 0.801$; $\approx 0.162$; recognize $\text{Gamma}(2,4)$ so $E[X]=\alpha\theta=8$; $\Phi(-0.98)\approx 0.163$.)*

Four for four, **inside six minutes each, recognizing the tool before computing**? You are ready — **skip straight to the three mock exams** and sit them timed. Any miss, any hesitation, or any answer that took you longer than the budget? The coaching below is built exactly for you. Each meta-skill has its own skip-gate too.
:::

---

Five meta-skills carry you from a 6 to a 10, in increasing subtlety. We teach them **in order**, each with its own "do you already own this?" skip-check, then the full lesson, then a Pokédex Entry you can carry into the exam:

1. **The six-minute budget & two-pass strategy** — *spend the clock where it earns points*
2. **Calculator mastery** — *drive the TI-30XS reflexively so the machine never costs you minutes*
3. **Archetype recognition & the shortcut catalog** — *name the tool from the tell, then collapse the work*
4. **Standing sanity checks** — *catch the impossible answer before you bubble it*
5. **The error-log method** — *turn every miss into a fix that sticks*

## Concept 1 — The Six-Minute Budget & Two-Pass Strategy

::: concept-gate
**DO YOU ALREADY OWN THIS? — Pacing**

You are $4$ minutes into a nasty double-integral, you cannot see the region, and $14$ problems remain untouched. What do you do *right now*?

If you answered **"mark a provisional guess, flag it, and move on — there's no penalty for a wrong answer, and a flagged problem I return to is worth more than a blank one I agonized over,"** you own pacing — **skip to Concept 2**. If your instinct was "push through, I never leave a problem unfinished," read on — that instinct will cost you the exam.
:::

**The one-sentence idea.** *You are paid only for the count of correct answers, not the order you solve them in — so spend the clock on points you can still earn, and never burn it on a problem that is beating you.*

**The arithmetic.** The exam is $180$ minutes for $30$ questions. Divide:

$$b = \frac{180\ \text{minutes}}{30\ \text{questions}} = 6\ \frac{\text{minutes}}{\text{question}}.$$

Six minutes is the *average* you can afford. But the exam is not built of average problems — some are ninety-second gifts, some are seven-minute monsters. Picture the thirty problems as thirty battles, each worth exactly **one point** whether it's a Caterpie or a Charizard. A grader does not award partial credit for "I was *so close* on the hard one." So the winning strategy is obvious once you see the points are flat: **bank time on the easy battles and spend it on the hard ones.** If a gift takes you two minutes, you have just *banked four minutes* to throw at a monster later. If a monster is eating minute after minute with no answer in sight, every extra minute you feed it is a minute stolen from two or three gifts still sitting unopened.

**The two passes.** **Pass 1:** go front to back; any problem whose archetype you recognize within about $30$ seconds, solve it now; any problem that is *not yielding* by about the four-minute mark, mark your best provisional answer, **flag it**, and move on. **Pass 2:** return to the flagged problems with all the time you banked from the gifts. A final sweep at the buzzer fills every remaining bubble with a guess.

**Surface and dismantle the trap.** The trap — the one that sinks more capable students than any formula error — is **"I don't leave a problem unfinished."** It feels like discipline. It is actually the most expensive habit on the exam. Sinking twelve minutes into one stubborn problem doesn't cost you one point; it costs you the **two or three later problems** you now have no time to even read. The second half of the trap is just as deadly: **leaving a blank.** Exam P has *no penalty for a wrong answer* — a blank scores zero, and so does a wrong guess, but a guess has a $\sim\!20\%$ chance (five choices) of being *right*. A guess therefore **strictly dominates** a blank. There is never, on this exam, a reason to leave a bubble empty.

**Picture it.** The clock is a literal progress bar; the two passes lay over it.

<figure>
<img src="../../assets/diagrams/ch19_pacing_strip.png" alt="A horizontal 180-minute exam timeline split into two passes over 30 question slots. The top band (Pass 1) sweeps left to right: recognized 'gift' questions are solved fast as short green blocks (~2 minutes, banking time); medium questions are solved at the 6-minute budget as blue blocks; stubborn 'monster' questions get a quick provisional guess and a red flag marker, banking time. The middle band (Pass 2) returns only to the flagged red monster slots, drawing on the time banked from the gifts, with thin connector arrows from each flag down to its revisit. A final yellow sliver labeled 'bubble every blank' fills any remaining empty answers. A Pikachu sprite paces the clock from the left margin." style="width:88%; max-width:720px; display:block; margin:1em auto;">
<figcaption>The two-pass clock: Pass 1 harvests the gifts and flags the monsters (banking time); Pass 2 spends the banked time on the flags; a final sweep guarantees no empty bubble. Each block is one question, worth exactly one point.</figcaption>
</figure>

**Consolidate.** You can now run an exam like a Champion runs a battle: triage on recognition, cap your spend per problem, bank time on the easy points, and finish with **zero blanks**. The single behaviour that earns this is *the willingness to walk away from a problem that is beating you.*

::: pokedex-entry
**POKÉDEX ENTRY №19·1 — The Six-Minute Budget & Two-Pass Strategy**

$$b = \frac{180\ \text{min}}{30\ \text{questions}} = 6\ \frac{\text{min}}{\text{question}}.$$

**Pass 1:** front to back; solve every recognized archetype, flag and provisionally answer anything not yielding by $\sim\!4$ minutes. **Pass 2:** return to the flags with banked time. **Always** bubble every question — a guess ($\sim\!20\%$ right) strictly beats a blank ($0\%$), because there is **no wrong-answer penalty**.

*In plain terms:* you are paid for the count correct, not the order. Bank time on the gifts; spend it on the monsters; never leave an empty bubble.

*Recognition cue:* the feeling of being **"stuck and frustrated"** *is itself* the signal to flag and move on — that feeling is protecting the clock for points you can still earn.
:::

## Concept 2 — Calculator Mastery (the TI-30XS MultiView)

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Calculator**

You need the mean and variance of a pmf with five outcomes, then a binomial coefficient $\binom{12}{6}$, then $e^{-3}$. Can you do all three on the TI-30XS *without retyping a single number*?

If you can enter the pmf in two lists and read $\bar x$ and $\sigma_x$ off **1-Var Stats**, fire $\binom{12}{6}$ from the [prb]{.kbd} menu in one press, and store $\lambda$ with [STO▸]{.kbd} so $e^{-\lambda}$ is one keystroke — **skip to Concept 3**. If any of those made you reach for longhand, read on; the machine is where minutes hide.
:::

**The one-sentence idea.** *The calculator is not a backup — it is a tool you drill until it is reflex, because Topic 2 (44–50% of the exam) is dominated by means, variances, $\binom{n}{k}$, and $e^x$ evaluations, and a fluent trainer reclaims minutes per sitting and eliminates rounding errors.*

The book teaches **one** machine, the **TI-30XS MultiView**, to mastery (the BA II Plus is allowed but not taught here). Bring **two** units to the exam — primary and backup — both **memory-cleared the night before**. Here are the key skills, each with the keystroke strip you should have in muscle memory by exam day.

**The flagship — 1-Var Stats for a pmf mean and variance.** Enter the outcomes in list `L1` and the probabilities (or frequencies) in `L2`, then run the statistics engine and read $\bar x$ (the mean) and $\sigma_x$ (whose **square** is the variance) straight off the screen:

[ [data]{.kbd} ]{.keystroke} enter `L1` = values, `L2` = probabilities, then [ [2nd]{.kbd} [stat]{.kbd} ]{.keystroke} → choose **1-Var Stats**, set `DATA:L1` and `FRQ:L2`, [ [enter]{.kbd} ]{.keystroke} → read $\bar x = E[X]$ and $\sigma_x$, so $\text{Var}(X)=\sigma_x^{2}$. *(Use $\sigma_x$, the population SD — **not** $s_x$, the sample SD.)*

**Combinations and permutations — one press.** For a binomial coefficient $\binom{12}{6}$, type the first count, open the probability menu, pick `nCr`, type the second count:

[ 12 [prb]{.kbd} nCr 6 [enter]{.kbd} ]{.keystroke} → $924$. For an ordered count use `nPr`; for a factorial, `!`.

**Exponentials for Poisson.** Store $-\lambda$ once and reuse it; the Poisson cdf then climbs by the recursion $p(k)=p(k-1)\cdot\lambda/k$:

[ [2nd]{.kbd} [e^x]{.kbd} [(-)]{.kbd} 3 [enter]{.kbd} ]{.keystroke} gives $e^{-3}$; store $e^{-\lambda}$ with [ [STO▸]{.kbd} [x]{.kbd} ]{.keystroke} so each Poisson term reuses it without retyping.

**Store-don't-retype, to kill rounding drift.** Bank every intermediate ($\sigma$, $X\wedge u$, $S(d)$, a standardized $z$) into a memory slot and **recall** it rather than retyping a rounded decimal:

[ ( value [−]{.kbd} [x]{.kbd} ) [÷]{.kbd} [y]{.kbd} [enter]{.kbd} ]{.keystroke} standardizes in one shot once $\mu$ is in `x` and $\sigma$ in `y`. A two-decimal intermediate can push a borderline answer into the wrong choice — and Exam P's answer options are often a hair apart *on purpose*.

::: trainers-tip
**TRAINER'S TIP — Clear the memory, bring a backup, read the last sentence first**

Clear both calculators' memory the **night before** so it's not a panic at the door (allowed display settings are not memory). A dead battery mid-exam is otherwise fatal — that's why you bring **two**. And on every stem, read the **last sentence first**: it tells you which number to chase, so you read the rest knowing what you're hunting.
:::

::: pokedex-entry
**POKÉDEX ENTRY №19·2 — TI-30XS MultiView Key Skills**

**1-Var Stats (flagship):** `L1`=values, `L2`=probs → [2nd]{.kbd}[stat]{.kbd} → 1-Var Stats, `FRQ:L2` → read $\bar x = E[X]$, $\text{Var}=\sigma_x^{2}$ (use $\sigma_x$, not $s_x$). **Counting:** `n` [prb]{.kbd} `nCr`/`nPr` `r`. **Poisson:** [2nd]{.kbd}[e^x]{.kbd}[(-)]{.kbd}$\lambda$, store with [STO▸]{.kbd}, recurse $p(k)=p(k-1)\lambda/k$. **Standardize:** store $\mu,\sigma$, then $(x-\mu)/\sigma$ in one expression.

*In plain terms:* the machine reclaims minutes and kills rounding drift — but only if it's reflex. Drill it on every problem in the mocks.

*Recognition cue:* whenever you're about to retype a rounded intermediate, **store it instead**; whenever you see a pmf mean/variance, reach for **1-Var Stats**, not longhand.
:::

## Concept 3 — Archetype Recognition & the Shortcut Catalog

::: concept-gate
**DO YOU ALREADY OWN THIS? — Recognition & Shortcuts**

A stem ends: *"…a density is $f(x)=\tfrac{1}{16}x\,e^{-x/4}$ on $x>0$; find $E[X]$."* Before computing, which tool, and which exact move?

If you instantly thought **"recognize the $\text{Gamma}(2,4)$ kernel — $E[X]=\alpha\theta=8$ — no integration by parts,"** you own this — **skip to Concept 4**. If you reached for the pencil and started $\int_0^\infty x\cdot\tfrac{1}{16}xe^{-x/4}\,dx$ for integration by parts, read on; that integral is a six-minute trap the gamma identity collapses to nine seconds.
:::

**The one-sentence idea.** *Exam speed is pattern-matching, not derivation: every problem carries a **tell** in its words, a fast scorer reads the tell and names the tool before the pencil moves, and a handful of identities then collapse the "hard" problems into one-liners.*

**Recognition first.** You already do this with Pokémon types — you see a Geodude and think "Water beats it" before the battle starts. A problem's archetype is its type. Two phrases do all the work in *"Spearow swoop in at an **average rate** of $3$ **per minute**; find $P(\text{at least }2)$."* **"Average rate per interval"** is the unmistakable signature of a **Poisson** count, so $N\sim\text{Poisson}(3)$; **"at least two"** is the signature of a **complement**, $1-P(0)-P(1)$. The two tells together hand you the solution *before you compute a single term*:

$$P(N\ge 2) = 1 - e^{-3} - 3e^{-3} = 1 - 4e^{-3} \approx 0.801.$$

**Surface and dismantle the trap.** The novice's instinct is to **start computing immediately** — to see "$P(\text{at least }2)$" and begin writing $P(2)+P(3)+\cdots$, a sum with no end; or, under panic, $1-P(1)$, *forgetting $P(0)$.* Both errors come from the same root: **pencil before recognition.** If you had named the archetype first — "Poisson, and 'at least' means complement of the *low* values" — you'd have known to subtract *both* $P(0)$ and $P(1)$. Recognition is not a luxury you do after the work; it is the move that *chooses* the work.

**The recognition map.** Every archetype has a tell. Memorize the left column; train the reflex to the right. (Chapter numbers are V3, where each tool was taught.)

| The stem says… | Reach for… | Taught in |
|---|---|---|
| "at least one" (independent trials) | complement $1-P(\text{none})=1-\prod(1-p_i)$ | ch01, ch05 |
| "given that," posterior, sensitivity/false-positive | Bayes' theorem / Bayes grid | ch02 |
| draws **without** replacement from a finite pool | hypergeometric | ch04 |
| "average rate," "per interval," count over time | Poisson, $\mu=\sigma^2=\lambda$ | ch05 |
| "time until," "memoryless," constant hazard | exponential | ch05 (geo) / ch11 (exp) |
| "number of trials until the $r$-th success" | (negative) binomial / geometric | ch05 |
| a given MGF $M_X(t)$ | kernel-match it / differentiate at $0$ | ch03 |
| $E[X]$ for $X\ge 0$ from the survival $S(x)$ | Darth Vader $\displaystyle\int_0^\infty S(x)\,dx$ | ch03 / ch10 |
| $\displaystyle\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx$ shape | gamma integral $=\Gamma(\alpha)\theta^{\alpha}$ | ch08 |
| deductible / limit / coinsurance | loss model $\alpha\big[(X\wedge u)-(X\wedge d)\big]$ | ch06 / ch13 |
| "strongest / weakest / $k$-th of $n$" | order statistics, $[F(x)]^n$ | ch17 |
| "approximately normal," large $n$, a sum/average | CLT ($+$ continuity correction if discrete) | ch12 |

The glyph $\wedge$ reads **"minimum with"** — $X\wedge u$ means $\min(X,u)$, the loss *capped* at $u$ — and $(X-d)_{+}$ reads **"$X$ minus $d$, floored at zero,"** the amount left after a deductible $d$.

**The recognition loop**, run on *every* stem: **(1)** read the **last sentence first** — it names the quantity asked. **(2)** scan for the **tell**. **(3)** name the **tool** (in your head) before the pencil moves.

**The shortcut catalog.** Once the tell names the tool, one of seven identities usually collapses the work. The slow path to the gate's density is $\E[X]=\tfrac{1}{16}\int_0^\infty x^2e^{-x/4}\,dx$ ground through **integration by parts twice**. The fast path *recognizes the shape*: the density is $\propto x^{2-1}e^{-x/4}$, the kernel of $\text{Gamma}(\alpha=2,\theta=4)$, whose mean is $\alpha\theta=8$ — nine seconds, no calculus. The seven moves:

- **Gamma integral** (polynomial $\times$ exponential → factorial): $\displaystyle\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx=\Gamma(\alpha)\,\theta^{\alpha}$, and $\int_0^\infty x^{n}e^{-x}\,dx=n!$.
- **Survival-function (Darth Vader) rule** for $X\ge 0$: $\displaystyle E[X]=\int_0^\infty S(x)\,dx$, or $\sum_{k\ge 0}P(X>k)$ for integer $X\ge 0$.
- **Exponential memorylessness** and the per-loss deductible mean: $E[X-d\mid X>d]=\theta$ and $E\big[(X-d)_{+}\big]=\theta\,e^{-d/\theta}$.
- **Poisson identity** and the **binomial$\to$Poisson** approximation: $\mu=\sigma^2=\lambda$, and $\text{Bin}(n,p)\approx\text{Pois}(np)$ for large $n$, small $p$.
- **MGF moments**: $M_X'(0)=E[X]$, $M_X''(0)=E[X^2]$.
- **Continuity correction**: $P(X\le k)\approx\Phi\!\big(\tfrac{k+0.5-\mu}{\sigma}\big)$ for a discrete $X$.

**Picture it.** The seven shortcuts, indexed by the tell that fires each — your Charizard's fast path against Gary's Blastoise brute force.

<figure>
<img src="../../assets/diagrams/ch19_shortcut_catalog.png" alt="A reference board of the seven exam shortcuts, framed as the final battle. Each tile shows a trigger tell on top and the identity that collapses the work below: 'polynomial times e^{-x/theta} integral' -> gamma integral Gamma(alpha)theta^alpha; 'E[X], X>=0, survival given' -> Darth Vader integral of S(x); 'exponential + already waited / deductible' -> memorylessness, theta and theta e^{-d/theta}; 'count over an interval' -> Poisson mu=sigma^2=lambda; 'rare event, many trials' -> binomial approximates Poisson; 'M_X(t) handed to you' -> differentiate at 0; 'discrete sum, normal approx' -> continuity correction k+0.5. A final tile asks: before you integrate by parts, ask gamma kernel? survival integral? memoryless exponential? Ash's Charizard sits in the lower-left margin labeled 'your shortcuts'; Gary's Blastoise in the upper-right margin labeled 'Gary's brute force.'" style="width:88%; max-width:720px; display:block; margin:1em auto;">
<figcaption>The shortcut catalog as a battle board: each tell (top of a tile) points to the identity (bottom) that collapses the work. Charizard's fast path beats Blastoise's brute force — the instant you're about to integrate by parts, ask whether one of the three usual suspects collapses it.</figcaption>
</figure>

**Consolidate.** You can now read any unlabeled stem, find its tell, name the right tool on sight, and reach for the identity that collapses it — the single motion that turns the Champion's "I won't tell you the topic" from a threat into a non-issue.

::: pokedex-entry
**POKÉDEX ENTRY №19·3 — Recognition & the Shortcut Catalog**

The loop: **read the last sentence → find the tell → name the tool → then compute.** Key tells: *"at least one"* → complement · *"given that / flagged"* → Bayes · *"average rate"* → Poisson · *"time until / memoryless"* → exponential · *"without replacement"* → hypergeometric · *given $M_X(t)$* → MGF · *deductible/limit* → loss model · *"strongest/$k$-th"* → order statistics · *"approximately normal, large $n$"* → CLT.

The seven shortcuts:
$$\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx=\Gamma(\alpha)\theta^{\alpha},\qquad E[X]=\int_0^\infty S(x)\,dx\ (X\ge 0),$$
$$E\big[(X-d)_{+}\big]=\theta e^{-d/\theta},\quad E[X-d\mid X>d]=\theta,\qquad \mu=\sigma^2=\lambda,$$
$$\text{Bin}(n,p)\approx\text{Pois}(np),\quad M_X'(0)=E[X],\ M_X''(0)=E[X^2],\quad P(X\le k)\approx\Phi\!\big(\tfrac{k+0.5-\mu}{\sigma}\big).$$

*Recognition cue:* the instant you're about to **integrate by parts**, stop and ask — *gamma kernel? survival integral? memoryless exponential?* One of the three usually collapses it.
:::

## Concept 4 — Standing Sanity Checks

::: concept-gate
**DO YOU ALREADY OWN THIS? — Sanity Checks**

Your final number is a variance of $-3$, or an expected *payment* of $\$8$ on an expected *loss* of $\$5$, or a probability of $1.4$. What does each tell you?

If you answered **"each is impossible, so I made an error — recheck before bubbling,"** you own the sanity checks — **skip to Concept 5**. If you'd have bubbled any of them, read on; most wrong multiple-choice answers are *impossible*, not merely incorrect.
:::

**The one-sentence idea.** *Most wrong answers are not just incorrect — they are **impossible**, and a two-second guardrail check on every final number catches them before they cost a point.*

You already know the *legal ranges* of every quantity in this book — probabilities live in $[0,1]$, variances are never negative, an insurance payment can't exceed the loss it covers. This concept makes *checking those ranges* a fixed last step. An expected payment of $8$ against an expected loss of $5$ violates a law of the model, not just the arithmetic; you don't need to know *where* the error is to know that there *is* one. The same logic disqualifies a variance of $-3$ (variances are $\ge 0$, being an average of squares) and a probability of $1.4$.

**Surface and dismantle the trap.** The trap is treating the computed number as **automatically trustworthy** — "I did the steps, so the answer is whatever came out." But the exam's distractor choices are *engineered* from the common errors, and many of those produce impossible values: forget a minus sign and your variance goes negative; swap a deductible for a limit and your payment exceeds the loss; misplace the complement and your probability tops $1$. The graders are *hoping* you bubble the impossible distractor without looking.

**The guardrails.** Each is a one-line invariant you check against your final number:

$$0\le P(\cdot)\le 1,\qquad \text{Var}(\cdot)\ge 0,\qquad \text{SD}=\sqrt{\text{Var}}\ge 0,\qquad E[\text{payment}]\le E[\text{loss}],$$
$$\mu_{\text{per payment}}\ \ge\ \mu_{\text{per loss}},\qquad \text{a weighted average lies between its smallest and largest input,}$$

plus **support consistency** (no mass outside the variable's stated range) and a **direction check** (a tail past the mean is below $0.5$). The general rule is one closing question, asked last, every time: **"Is this number inside the region its quantity is allowed to live in?"**

**Consolidate.** A guardrail scan is now the fixed last step of every problem, so an impossible answer never reaches a bubble. Combined with the budget, the calculator, recognition, and the catalog, this completes the execution skill set the exam grades.

::: pokedex-entry
**POKÉDEX ENTRY №19·4 — Standing Sanity Checks**

Run the relevant guardrail on every final number, before bubbling:
$$0\le P(\cdot)\le 1,\quad \text{Var}(\cdot)\ge 0,\quad E[\text{payment}]\le E[\text{loss}],\quad \mu_{\text{per payment}}\ge\mu_{\text{per loss}},$$
$$\text{(weighted average between its extremes)},\quad \text{(no mass outside support)},\quad \text{(tail past mean }<0.5).$$

*Recognition cue:* the instant you compute a final number, ask **"could a sane risk look like this?"** If not, you made a sign or formula error — recheck before bubbling.
:::

## Concept 5 — The Error-Log Method

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Error Log**

You miss three mock problems: one was a $\sigma$-vs-$\sigma^2$ slip, one a forgotten continuity correction, one you simply ran out of time on. What do you do with those three misses?

If you answered **"classify each by root cause, retest that exact archetype until it's automatic, and re-time the pacing miss — a logged error fixed once is an error not re-made on exam day,"** you own this — **skip to the Worked Examples**. If your plan was "feel bad and move on," read on; an unclassified miss is a miss you'll repeat.
:::

**The one-sentence idea.** *Every miss has a root cause; classify it, fix that cause, and retest the same archetype, so a recurring slip is eliminated once instead of re-made under pressure.*

After each mock, don't just score it — **log every miss** in three columns: the **problem** (and its archetype), the **root cause**, and the **fix + retest**. Root causes cluster into a short list:

- **Recognition miss** — named the wrong tool (or none). *Fix:* drill the recognition map (Concept 3) on that tell.
- **Formula slip** — right tool, wrong identity (divided by $\sigma^2$ not $\sigma$; used $\theta^2$ not $2\theta^2$). *Fix:* re-derive the identity once, then redo three of that type.
- **Computation/calculator error** — right setup, arithmetic or keystroke wrong. *Fix:* redo it on the TI-30XS with store-don't-retype.
- **Sanity miss** — bubbled an impossible value. *Fix:* add the guardrail as a fixed last step.
- **Pacing miss** — ran out of time. *Fix:* re-time with a hard six-minute cap and the two-pass rule.

The discipline is **retest, not just review**: after logging a continuity-correction miss, do three more continuity-correction problems the same day. A miss you merely *read about* recurs; a miss you *re-solve correctly three times* is gone. This is exactly the peer-review habit a reserving actuary uses so a single sign error never ships to a customer.

::: pokedex-entry
**POKÉDEX ENTRY №19·5 — The Error-Log Method**

After every mock, log each miss as **(problem + archetype) → (root cause) → (fix + retest)**. Root-cause categories: recognition · formula · computation/calculator · sanity · pacing. **Retest, don't just review** — redo three of the same archetype the same day.

*Recognition cue:* a miss is not a verdict, it's data. The same root cause appearing twice in your log is the highest-value thing you can fix before exam day.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/vs/blue.png" alt="Gary Oak, the rival, as the final opponent" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Gary Oak — the rival, your final benchmark at the Plateau</figcaption>
</figure>

Four examples model the *recognition-then-execution* loop on **unlabeled, mixed** problems — exactly the Champion's gauntlet. Watch how the archetype is named **first**, the shortcut deployed, the sanity check closing each one. They fade from fully narrated to exam speed.

### Worked Example 19.1 — A Hidden Poisson (full narration; recognition-first)

<figure style="margin:1.5em auto; max-width:130px; text-align:center;">
<img src="../../assets/sprites/front/21.png" alt="Spearow" style="width:96px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#021 Spearow</strong> — arrivals at an average rate ⇒ Poisson</figcaption>
</figure>

**ARCHETYPE:** *Poisson count, "at least" via complement.*

**Setup.** Gary leads with a flock count: "On Route 1, Spearow swoop in at an average rate of $3$ per minute, independently. In a given minute, what's the probability *at least two* swoop in?"

**Step 1 — Recognize (read the last sentence, find the tell).** The last sentence asks for $P(\text{at least }2)$. Two tells: **"average rate per minute"** ⇒ Poisson with $\lambda=3$; **"at least two"** ⇒ complement of the low values $\{0,1\}$. Tools named *before any computing.*

**Step 2 — Professor's Path (why the complement).** Directly, $P(N\ge 2)=\sum_{k\ge 2}P(N=k)$ is an infinite sum; but $\{N\ge 2\}$ is the complement of the finite set $\{0,1\}$, so $P(N\ge 2)=1-P(0)-P(1)$. For $\text{Poisson}(\lambda)$, $P(0)=e^{-3}$ and $P(1)=3e^{-3}$.

**Step 3 — Trainer's Path (fast).** $P(N\ge 2)=1-e^{-3}-3e^{-3}=1-4e^{-3}$. With $e^{-3}\approx 0.049787$ (one keystroke: [2nd]{.kbd}[e^x]{.kbd}[(-)]{.kbd}$3$): $1-4(0.049787)\approx \mathbf{0.801}$.

**Step 4 — Check & pitfall.** $0.801\in[0,1]$ ✓ (guardrail). **Pitfall:** computing $1-P(1)$ and forgetting $P(0)$ — "at least two" must complement *both* low values. *(Back-ref: Entries №19·3, №19·4.)*

### Worked Example 19.2 — A Disguised Bayes (partial guidance)

<figure style="margin:1.5em auto; max-width:130px; text-align:center;">
<img src="../../assets/sprites/front/92.png" alt="Gastly, a Ghost-type" style="width:96px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#092 Gastly</strong> — a rare Ghost the scanner flags: low base rate ⇒ Bayes</figcaption>
</figure>

**ARCHETYPE:** *Two-way Bayes / false-positive (low base rate).*

**Setup.** "A wild Pokémon is Ghost-type with probability $0.02$," Gary says. "Your Pokédex flags a true Ghost correctly $95\%$ of the time, but false-flags a non-Ghost as Ghost $10\%$ of the time. It just flagged this one. What's the probability it's *actually* a Ghost?"

**Identify.** Want $P(G\mid +)$, given $P(+\mid G)=0.95$ — the **bar is flipped**, so this is Bayes, not a lookup. Givens: prior $P(G)=0.02$, sensitivity $0.95$, false-positive $0.10$. *Your move: grid it.*

| Cause | Prior | $P(+\mid\cdot)$ | Joint |
|---|---|---|---|
| $G$ (Ghost) | $0.02$ | $0.95$ | $0.0190$ |
| $G^c$ (not) | $0.98$ | $0.10$ | $0.0980$ |
| **Total** | | | $0.1170$ |

$$P(G\mid +) = \frac{0.0190}{0.1170} \approx \mathbf{0.1624}.$$

**Check & pitfall.** Despite a "$95\%$-accurate" detector, the posterior is only $\approx 16\%$ — the base-rate effect: Ghosts are so rare ($2\%$) that the flood of false flags from the $98\%$ non-Ghosts swamps the true ones. **Pitfall:** the **prosecutor's fallacy** — quoting the $0.95$ sensitivity as the answer. *(Back-ref: Entry №19·3.)*

### Worked Example 19.3 — The Gamma Integral You Almost Did by Parts (light guidance)

**ARCHETYPE:** *gamma-family expectation via kernel recognition.*

**Setup.** Gary smirks: "Charizard's flame burns for $X$ minutes where $f(x)=\tfrac{1}{16}x\,e^{-x/4}$ for $x>0$. Find $E[X]$."

**Identify & solve.** The density $\propto x^{2-1}e^{-x/4}$ is a $\text{Gamma}(\alpha=2,\theta=4)$ kernel, so $E[X]=\alpha\theta=2\cdot 4=\mathbf{8}$. (Verify the constant: $\tfrac{1}{\Gamma(2)\,4^{2}}=\tfrac{1}{16}$ ✓.) The longer-but-no-parts route, via the gamma integral:
$$E[X]=\tfrac{1}{16}\int_0^\infty x^{3-1}e^{-x/4}\,dx = \tfrac{1}{16}\,\Gamma(3)\,4^{3} = \tfrac{1}{16}(2)(64) = 8.$$

**Check & pitfall.** $E[X]=8=\alpha\theta$ ✓. **Pitfall:** integrating $x\cdot xe^{-x/4}$ by parts under the clock when the gamma integral collapses it instantly. *(Back-ref: Entry №19·3.)*

### Worked Example 19.4 — A CLT That Needs the Continuity Correction (exam speed)

**ARCHETYPE:** *CLT normal approximation to a binomial, with continuity correction.*

**Setup.** "The League runs $100$ independent exhibition matches," Gary says. "Each has probability $0.3$ of an upset, independently. Approximate the probability of *at most $25$* upsets."

**Solve.** $S\sim\text{Binomial}(100,0.3)$: $\mu=np=30$, $\sigma^2=np(1-p)=21$, $\sigma=\sqrt{21}\approx 4.583$. Discrete ⇒ continuity correction at $25.5$:
$$P(S\le 25)\approx \Phi\!\left(\frac{25.5-30}{4.583}\right)=\Phi(-0.98)=1-\Phi(0.98)=1-0.8365\approx \mathbf{0.163}.$$

**Check & pitfall.** $0.163\in[0,1]$ ✓, and *below* $0.5$ since $25<\mu=30$ ✓ (direction check). **Pitfall:** skipping the $+0.5$ correction — without it you'd standardize at $25$, get $\Phi(-1.09)\approx 0.138$, and land in a different answer band. *(Back-ref: Entries №19·3, №19·4.)*

## Team Rocket's Trap

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Team Rocket — about to fail the pacing gate</figcaption>
</figure>

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

Jessie, James, and Meowth are sitting their *own* mock exam to "qualify" for a Rocket promotion. Twenty minutes in, James announces he's spent the whole time on Question 3 — a nasty double integral — because "we never leave a problem unfinished, that's not the Rocket way!" Meowth, panicking at the clock, starts *leaving the last five blank* rather than reading them: "No time, skip 'em, leave 'em empty." Jessie, meanwhile, refuses to flag anything: "Champions don't go *back.*" They finish $11$ of $30$, leave four blank, and bomb the time-management gate entirely.

**Where it fails:** all three broke the budget rule (Entry №19·1). James fed one monster twelve minutes that should have harvested three gifts. Meowth left blanks when a guess **strictly dominates** an empty bubble — there is *no penalty* for a wrong answer. Jessie's no-flagging pride threw away the entire two-pass advantage. **The fix:** cap any single problem at $\sim\!6$ minutes (flag and move), bubble *every* question even if it's a guess, and run two passes — gifts first, flags second. Pacing is a skill you drill, not a virtue you boast about.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

Working actuaries are judged on **accuracy under deadline**, exactly as you are on exam day. A pricing analyst handing a quote to an underwriter has minutes, not hours, and the very same guardrails apply: a loss cost can't be negative, a retention can't exceed the limit, an expected recovery can't beat the ceded premium — the same standing sanity checks (Entry №19·4) you run on every bubble.

The **two-pass strategy** is how analysts triage a model run: nail the cells you trust, flag the anomalies, circle back — never let one stubborn figure stall the whole deliverable. And the **error log** this chapter's mocks build (classify every miss by root cause, then retest it) is precisely the peer-review discipline a reserving actuary uses so a single sign error never ships to a customer.

*Series bridge:* this error-log-and-sanity-check habit carries straight into **CAS Exam 5** ratemaking and reserving, where one unchecked sign error can misprice an entire book of business.

*Transfer check:* strip the Pokémon out and the skill is identical — "thirty mixed actuarial problems, three hours, recognize the archetype, deploy the shortcut, sanity-check the answer, never blank." If you can run that loop with no Pikachu in sight, the skill has transferred — and that *is* Exam P.
:::

## The Gym Battle — Champion's Capstone

<figure style="margin:1.5em auto; max-width:130px; text-align:center;">
<img src="../../assets/sprites/front/6.png" alt="Charizard, Gary's measure of you" style="width:110px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#006 Charizard</strong> — the ace for the final, braided turn</figcaption>
</figure>

**Setup.** For the final turn, Gary stacks one integrative problem that braids three chapters into a single back-of-exam monster — exactly what the SOA buries near the end. "Aggregate claim cost," he calls it.

Over one tournament day, the **number** of injuries $N$ at the Pokémon Center is Poisson with mean $\lambda=4$. Each injury's **recovery cost** $X_i$ (thousands of Poké-dollars) is independent of $N$ and of each other, exponential with mean $\theta=5$. Let $T=\sum_{i=1}^{N}X_i$ be the day's **aggregate cost** (with $T=0$ if $N=0$). Gary wants three numbers: (1) $E[T]$, (2) $\text{Var}(T)$, and (3) by the normal approximation, $P(T>30)$.

**ARCHETYPE:** *compound Poisson aggregate — total expectation, total variance, then CLT.* Three tells, named first: Poisson frequency + exponential severity + "normal approximation of an aggregate."

**Step 1 — Identify and gather the severity moments.** $T$ is a compound distribution: a random number $N\sim\text{Poisson}(4)$ of i.i.d. severities $X_i\sim\text{Exponential}(5)$. For an exponential, $E[X]=\theta=5$ and $E[X^2]=2\theta^2=50$ (gamma-integral shortcut, Entry №19·3), so $\text{Var}(X)=50-25=25$.

**Step 2 — Professor's Path (the laws, then why they collapse).** By the **law of total expectation**, $E[T]=E[N]\,E[X]=4\cdot 5=\mathbf{20}$ (thousand). By the **law of total variance**, $\text{Var}(T)=E[N]\text{Var}(X)+\text{Var}(N)\,E[X]^2$. For a **Poisson** frequency $E[N]=\text{Var}(N)=\lambda$, which collapses it to $\text{Var}(T)=\lambda\,E[X^2]$. Both forms agree:
$$\text{Var}(T)=\underbrace{E[N]\text{Var}(X)}_{4(25)=100}+\underbrace{\text{Var}(N)E[X]^2}_{4(25)=100}=200 \;=\; \underbrace{\lambda\,E[X^2]}_{4(50)}=\mathbf{200}.$$
So $\text{SD}(T)=\sqrt{200}\approx 14.142$.

**Step 3 — Trainer's Path (the tail via CLT).** Approximate $T$ as $N(20,\,200)$. The aggregate is **continuous**, so **no** continuity correction:
$$P(T>30)\approx 1-\Phi\!\left(\frac{30-20}{14.142}\right)=1-\Phi(0.71)\approx 1-0.7611=\mathbf{0.239}.$$

**Step 4 — Check & the three pitfalls Gary built in.** Guardrails: $E[T]=20>0$ ✓; $\text{Var}(T)=200\ge 0$ ✓; $P(T>30)=0.239\in[0,1]$ and *below* $0.5$ since $30>\mu=20$ ✓ (direction check). The three traps: **(1)** using $\text{Var}(T)=\lambda\text{Var}(X)=100$, forgetting the frequency contribution; **(2)** applying a continuity correction to a *continuous* aggregate; **(3)** computing $E[X^2]=\theta^2=25$ instead of $2\theta^2=50$. Beat all three guardrails and the Champion is yours.

> "That," Gary says, the half-smile finally honest, "is how you read a problem you've never seen. You named all three tools before you touched the pencil. Grandpa was right about you." Pikachu's cheeks spark in triumph.

## The Gym Challenge — Three Mock Exams

::: problem-set
**THE CHAMPIONSHIP BRACKET — your final mission.** This is the real thing: three **30-question, 3-hour mock exams**, each weight-matched to the live Exam P syllabus (**≈8 General Probability / ≈14 Univariate / ≈8 Multivariate** per 30). Each mock is a **round of the tournament bracket** — each question an opponent. Work each mock **timed, in one sitting**, with only the provided normal table (Appendix C, **two-decimal $z$**) and a cleared TI-30XS. Score it against the **Scored Answer Key** that follows each mock (quick-answer table, then full worked solutions — never interleaved with the problems), then fill in the **Pacing Post-Mortem** template. Five options A–E, exactly one correct; **answer every question** (no guessing penalty). Markers: 🔴 Poké Ball = under-two-minute mechanics · 🟡 true SOA difficulty · 🔵 integrative / back-of-exam stretch.

**Readiness gates (all three must hold):** score **24/30** with correct method · Coaching Actuaries **Earned Level 7+** · steady **six-minute pacing**.

---

### ▶ MOCK A — Round One (M1.1–M1.30)

**General Probability (Topic 1).**

**M1.1.** 🔴 $P(\text{grass})=0.5$, $P(\text{bug})=0.3$, $P(\text{grass and bug})=0.2$. Find $P(\text{neither})$.  (A) 0.20 (B) 0.30 (C) 0.40 (D) 0.50 (E) 0.60

**M1.2.** 🟡 A wild Pokémon is Ghost with prior $0.02$; a scanner flags a true Ghost w.p. $0.95$ and false-flags a non-Ghost w.p. $0.10$. It flagged one. Find $P(\text{Ghost}\mid\text{flagged})$.  (A) 0.095 (B) 0.162 (C) 0.500 (D) 0.760 (E) 0.950

**M1.3.** 🔴 From $8$ caught Pokémon, how many distinct **ordered** line-ups of $3$?  (A) 56 (B) 112 (C) 168 (D) 336 (E) 512

**M1.4.** 🔴 Roll two fair dice. Find $P(\text{sum}=7\text{ or }11)$.  (A) 1/9 (B) 1/6 (C) 2/9 (D) 1/4 (E) 1/3

**M1.5.** 🔴 Three independent Poké Balls each catch w.p. $0.4$. Find $P(\text{at least one catch})$.  (A) 0.216 (B) 0.400 (C) 0.640 (D) 0.784 (E) 0.936

**M1.6.** 🟡 Route A holds $70\%$ of Pokémon ($10\%$ rare); Route B holds $30\%$ ($25\%$ rare). A captured one is rare. Find $P(\text{Route B})$.  (A) 0.30 (B) 0.42 (C) 0.52 (D) 0.58 (E) 0.75

**M1.7.** 🔴 $P(A)=0.6$, $P(B)=0.5$, $P(A\text{ or }B)=0.8$. Find $P(A\text{ and }B)$.  (A) 0.10 (B) 0.20 (C) 0.30 (D) 0.40 (E) 0.55

**M1.8.** 🟡 A tank holds $10$ Magikarp and $5$ Goldeen; net $4$ at once (no replacement). Find $P(\text{exactly }2\text{ Goldeen})$.  (A) 0.165 (B) 0.220 (C) 0.330 (D) 0.412 (E) 0.500

**Univariate RVs (Topic 2).**

**M1.9.** 🔴 Spearow arrive at average rate $3$/min (Poisson). Find $P(\text{at least }2)$ in one minute.  (A) 0.199 (B) 0.423 (C) 0.577 (D) 0.801 (E) 0.950

**M1.10.** 🟡 $f(x)=\tfrac{1}{16}xe^{-x/4}$, $x>0$. Find $E[X]$.  (A) 2 (B) 4 (C) 6 (D) 8 (E) 16

**M1.11.** 🔴 Each pull wins w.p. $0.2$. Find $P(\text{first win on the 4th pull})$.  (A) 0.0819 (B) 0.1024 (C) 0.1280 (D) 0.1600 (E) 0.2000

**M1.12.** 🔴 $X\sim N(50,\,64)$. Find $P(X>62)$.  (A) 0.0668 (B) 0.0934 (C) 0.1056 (D) 0.1587 (E) 0.3085

**M1.13.** 🟡 MGF $M(t)=e^{3t+2t^2}$. Find $\text{Var}$.  (A) 2 (B) 3 (C) 4 (D) 6 (E) 9

**M1.14.** 🟡 $X\sim\text{Exp}(\theta=4)$, deductible $d=2$. Find expected payment **per loss**.  (A) 1.21 (B) 2.00 (C) 2.43 (D) 3.30 (E) 4.00

**M1.15.** 🔴 $X\sim\text{Unif}(0,10)$. Find $\text{Var}(X)$.  (A) 2.89 (B) 5.00 (C) 8.33 (D) 10.0 (E) 25.0

**M1.16.** 🔴 Recovery $\sim\text{Exp}(\theta=10)$; already rested $4$ min. Find $P(\ge 6\text{ more min})$.  (A) 0.301 (B) 0.449 (C) 0.549 (D) 0.607 (E) 0.670

**M1.17.** 🟡 $100$ matches, each an upset w.p. $0.3$. Normal approx **with** continuity correction: $P(\le 25)$. Use $\Phi(0.98)=0.8365$.  (A) 0.115 (B) 0.137 (C) 0.163 (D) 0.211 (E) 0.250

**M1.18.** 🔵 $X\sim\text{Exp}(8)$, $d=2$, $u=10$, $\alpha=0.8$. Find expected payment **per loss**. ($e^{-0.25}=0.7788$, $e^{-1.25}=0.2865$.)  (A) 2.52 (B) 3.15 (C) 3.94 (D) 4.57 (E) 5.71

**M1.19.** 🔴 Daily visits $\sim\text{Poisson}(9)$. Find the SD.  (A) 1.5 (B) 3.0 (C) 4.5 (D) 9.0 (E) 81.0

**M1.20.** 🔴 $f(x)=cx^2$ on $0<x<3$. Find $c$.  (A) 1/27 (B) 1/9 (C) 1/3 (D) 2/9 (E) 1

**M1.21.** 🔴 Ditto copies form $1..6$, equally likely. Find $\text{Var}$.  (A) 2.50 (B) 2.92 (C) 3.50 (D) 5.83 (E) 17.5

**M1.22.** 🟡 Integer $X\ge 0$ with $P(X>0)=1$, $P(X>1)=0.6$, $P(X>2)=0.3$, $P(X>3)=0.1$. Find $E[X]$.  (A) 1.0 (B) 1.5 (C) 2.0 (D) 2.4 (E) 3.0

**Multivariate RVs (Topic 3).**

**M1.23.** 🔵 $f(x,y)=2$ on $0<x<y<1$. Find $P(Y<2X)$.  (A) 0.25 (B) 0.33 (C) 0.50 (D) 0.67 (E) 0.75

**M1.24.** 🟡 Five $\text{Unif}(0,1)$ strengths. Find $E[\text{strongest}]$.  (A) 0.50 (B) 0.625 (C) 0.75 (D) 0.833 (E) 0.90

**M1.25.** 🟡 $\text{Var}(X)=4$, $\text{Var}(Y)=9$, $\text{Corr}=0.5$. Find $\text{Var}(2X-Y)$.  (A) 7 (B) 13 (C) 19 (D) 25 (E) 37

**M1.26.** 🟡 $f(x)=x/8$ on $0<x<4$. Find $E[X\mid X>2]$.  (A) 2.67 (B) 3.00 (C) 3.11 (D) 3.33 (E) 3.50

**M1.27.** 🟡 $A\sim N(20,16)$, $B\sim N(30,9)$, independent. Find $P(A+B>60)$. Use $\Phi(2.0)=0.9772$.  (A) 0.0062 (B) 0.0228 (C) 0.0668 (D) 0.1587 (E) 0.3085

**M1.28.** 🔵 Three gadgets, exponential means $4,6,12$ hr; series (first failure). Find expected time to failure.  (A) 2.0 (B) 4.0 (C) 6.0 (D) 7.3 (E) 22.0

**M1.29.** 🔵 $N\sim\text{Poisson}(4)$, costs $X_i\sim\text{Exp}(5)$, $T=\sum X_i$. Find $\text{Var}(T)$.  (A) 100 (B) 140 (C) 200 (D) 250 (E) 400

**M1.30.** 🔵 $400$ policies, counts $\text{Poisson}(0.5)$ each; $M$ = total. Normal approx **with** continuity correction: $P(M\ge 210)$. Use $\Phi(0.67)=0.7486$.  (A) 0.159 (B) 0.211 (C) 0.251 (D) 0.309 (E) 0.401

#### Mock A — Scored Answers

**Quick-answer table** (score $1$ each; readiness gate $24/30$):

| # | Ans | # | Ans | # | Ans |
|---|---|---|---|---|---|
| M1.1 | C | M1.11 | B | M1.21 | B |
| M1.2 | B | M1.12 | A | M1.22 | C |
| M1.3 | D | M1.13 | C | M1.23 | C |
| M1.4 | C | M1.14 | C | M1.24 | D |
| M1.5 | D | M1.15 | C | M1.25 | B |
| M1.6 | C | M1.16 | C | M1.26 | C |
| M1.7 | C | M1.17 | C | M1.27 | B |
| M1.8 | C | M1.18 | B | M1.28 | A |
| M1.9 | D | M1.19 | B | M1.29 | C |
| M1.10 | D | M1.20 | B | M1.30 | C |

**Full worked solutions** (archetype-tagged, shortcut noted):

- **M1.1 (C, 0.40)** — *inclusion–exclusion + complement.* $P(\cup)=0.5+0.3-0.2=0.6$, so $P(\text{neither})=1-0.6=0.4$.
- **M1.2 (B, 0.162)** — *Bayes / false-positive.* $\dfrac{0.95(0.02)}{0.95(0.02)+0.10(0.98)}=\dfrac{0.0190}{0.1170}=0.162$. Low base rate keeps the posterior small.
- **M1.3 (D, 336)** — *permutation.* Ordered ⇒ $P(8,3)=8\cdot7\cdot6=336$ (one press: [prb]{.kbd} `nPr`).
- **M1.4 (C, 2/9)** — *equally-likely, disjoint union.* $(6+2)/36=8/36=2/9$.
- **M1.5 (D, 0.784)** — *at-least-one complement.* $1-(0.6)^3=1-0.216=0.784$.
- **M1.6 (C, 0.52)** — *total probability + Bayes.* $P(\text{rare})=0.7(0.10)+0.3(0.25)=0.145$; $P(B\mid\text{rare})=0.075/0.145=0.517$.
- **M1.7 (C, 0.30)** — *inclusion–exclusion solved for the intersection.* $0.6+0.5-0.8=0.3$.
- **M1.8 (C, 0.330)** — *hypergeometric.* $\binom{5}{2}\binom{10}{2}/\binom{15}{4}=450/1365=0.330$.
- **M1.9 (D, 0.801)** — *Poisson + complement.* $1-e^{-3}-3e^{-3}=1-4e^{-3}=0.801$.
- **M1.10 (D, 8)** — *gamma kernel.* $f\propto x^{2-1}e^{-x/4}$ ⇒ $\text{Gamma}(2,4)$, $E[X]=\alpha\theta=8$. No parts.
- **M1.11 (B, 0.1024)** — *geometric.* $(0.8)^3(0.2)=0.1024$.
- **M1.12 (A, 0.0668)** — *standardize.* $\sigma=8$, $z=(62-50)/8=1.5$; $1-\Phi(1.5)=1-0.9332=0.0668$. (Divide by $\sigma$, not $\sigma^2$.)
- **M1.13 (C, 4)** — *MGF kernel.* Normal MGF $e^{\mu t+\sigma^2t^2/2}$: $\sigma^2/2=2\Rightarrow\sigma^2=4$.
- **M1.14 (C, 2.43)** — *exponential deductible, memoryless.* $E[(X-d)_+]=\theta e^{-d/\theta}=4e^{-0.5}=2.43$.
- **M1.15 (C, 8.33)** — *uniform variance.* $(10-0)^2/12=8.33$.
- **M1.16 (C, 0.549)** — *exponential memorylessness.* $P(X>10\mid X>4)=P(X>6)=e^{-0.6}=0.549$.
- **M1.17 (C, 0.163)** — *CLT + continuity correction.* $\mu=30$, $\sigma=\sqrt{21}=4.583$; $P(\le25)\approx\Phi((25.5-30)/4.583)=\Phi(-0.98)=1-0.8365=0.163$.
- **M1.18 (B, 3.15)** — *full loss policy.* $E[X\wedge10]=8(1-e^{-1.25})=5.708$; $E[X\wedge2]=8(1-e^{-0.25})=1.770$; payment $=0.8(5.708-1.770)=3.15$.
- **M1.19 (B, 3.0)** — *Poisson identity.* $\sigma=\sqrt{\lambda}=\sqrt{9}=3$.
- **M1.20 (B, 1/9)** — *normalize.* $\int_0^3 x^2dx=9$, so $c=1/9$.
- **M1.21 (B, 2.92)** — *discrete uniform variance.* $(n^2-1)/12=35/12=2.92$.
- **M1.22 (C, 2.0)** — *survival method.* $E[X]=\sum_{k\ge0}P(X>k)=1+0.6+0.3+0.1=2.0$.
- **M1.23 (C, 0.5)** — *region integral.* Over $0<x<y<1$, the part with $y<2x$ splits at $x=\tfrac12$: $\tfrac14+\tfrac14=0.5$.
- **M1.24 (D, 0.833)** — *max order statistic.* $E[\max]=n/(n+1)=5/6=0.833$.
- **M1.25 (B, 13)** — *linear combination.* $\text{Cov}=0.5\sqrt{36}=3$; $4(4)+9-2(2)(3)=16+9-12=13$.
- **M1.26 (C, 3.11)** — *conditional expectation.* $P(X>2)=0.75$; $E[X;X>2]=56/24=2.333$; ratio $=3.11$.
- **M1.27 (B, 0.0228)** — *sum of normals.* $A+B\sim N(50,25)$, $z=2$; $1-0.9772=0.0228$.
- **M1.28 (A, 2.0)** — *min of exponentials.* Rate $\tfrac14+\tfrac16+\tfrac1{12}=\tfrac12$; $E[\min]=2$.
- **M1.29 (C, 200)** — *compound Poisson variance.* $\text{Var}(T)=\lambda E[X^2]=4(2\cdot25)=200$.
- **M1.30 (C, 0.251)** — *Poisson sum + CLT + continuity.* $M\sim\text{Poisson}(200)$, $\sigma=14.142$; $P(\ge210)\approx1-\Phi(0.67)=1-0.7486=0.251$.

#### Mock A — Pacing Post-Mortem (fill in after timed scoring)

| Metric | Your result | Target |
|---|---|---|
| Raw score | ___ / 30 | **24+** |
| Topic 1 correct | ___ / 8 | 6+ |
| Topic 2 correct | ___ / 14 | 11+ |
| Topic 3 correct | ___ / 8 | 6+ |
| Total time | ___ min | ≤ 180 |
| Problems left blank | ___ | **0** |
| # flagged on Pass 1 | ___ | (note for review) |

**Error log — one row per miss.** Root-cause categories: recognition · formula · computation/calculator · sanity · pacing.

| # missed | Archetype | Root cause | Fix + retest (3 of this type) |
|---|---|---|---|
| | | | |

---

### ▶ MOCK B — Round Two (M2.1–M2.30)

**General Probability (Topic 1).**

**M2.1.** 🔴 Five independent encounters, each shiny w.p. $0.1$. Find $P(\text{at least one shiny})$.  (A) 0.10 (B) 0.41 (C) 0.50 (D) 0.59 (E) 0.90

**M2.2.** 🔴 $P(A)=0.4$, $P(B)=0.5$, independent. Find $P(A\mid B)$.  (A) 0.20 (B) 0.40 (C) 0.50 (D) 0.80 (E) 0.90

**M2.3.** 🔴 How many unordered teams of $6$ from $12$?  (A) 720 (B) 924 (C) 1320 (D) 5040 (E) 665280

**M2.4.** 🟡 $2$ Great Balls (catch $0.6$) and $3$ Poké Balls (catch $0.3$); draw one at random and throw. Find $P(\text{catch})$.  (A) 0.30 (B) 0.42 (C) 0.45 (D) 0.50 (E) 0.60

**M2.5.** 🔵 Coin is fair (prior $0.7$) or two-headed (prior $0.3$). It flips heads. Find $P(\text{two-headed}\mid H)$.  (A) 0.30 (B) 0.46 (C) 0.50 (D) 0.65 (E) 0.70

**M2.6.** 🟡 $60\%$ own Fire, $50\%$ Water, $40\%$ Grass; $30\%$ FW, $20\%$ FG, $20\%$ WG, $10\%$ all three. Find $P(\text{at least one})$.  (A) 0.70 (B) 0.80 (C) 0.90 (D) 0.95 (E) 1.00

**M2.7.** 🟡 A $4$-digit code, digits $0$–$9$ with repetition. Find $P(\text{all four distinct})$.  (A) 0.360 (B) 0.504 (C) 0.600 (D) 0.720 (E) 0.840

**M2.8.** 🔴 $6$ independent throws, each success w.p. $0.5$. Find $P(\text{exactly }4)$.  (A) 0.094 (B) 0.234 (C) 0.312 (D) 0.375 (E) 0.500

**Univariate RVs (Topic 2).**

**M2.9.** 🟡 Each dig succeeds w.p. $0.4$. Find $P(\text{3rd success on the 5th dig})$.  (A) 0.138 (B) 0.166 (C) 0.230 (D) 0.346 (E) 0.400

**M2.10.** 🔴 $B\in\{0,1,2,3\}$ with pmf $0.4,0.3,0.2,0.1$. Find $\text{Var}(B)$.  (A) 0.50 (B) 0.80 (C) 1.00 (D) 1.05 (E) 1.20

**M2.11.** 🟡 $X\sim N(70,100)$. Find $P(60\le X\le 85)$. Use $\Phi(1.5)=0.9332$, $\Phi(1.0)=0.8413$.  (A) 0.6247 (B) 0.7745 (C) 0.8351 (D) 0.9332 (E) 0.9772

**M2.12.** 🟡 $200$ balls, each defective w.p. $0.01$. Poisson approx: $P(\le 1\text{ defect})$.  (A) 0.135 (B) 0.271 (C) 0.406 (D) 0.500 (E) 0.677

**M2.13.** 🔴 $X\sim\text{Exp}(\theta=3)$. Find $E[X^2]$.  (A) 3 (B) 6 (C) 9 (D) 12 (E) 18

**M2.14.** 🔵 $X\sim\text{Exp}(4)$, $d=2$, no limit, $Y=(X-2)_+$. Find $\text{Var}(Y)$.  (A) 5.89 (B) 9.70 (C) 13.52 (D) 16.00 (E) 19.41

**M2.15.** 🔴 $F(x)=1-e^{-x/5}$, $x\ge 0$. Find $P(X>10)$. ($e^{-2}=0.1353$.)  (A) 0.0498 (B) 0.1353 (C) 0.3679 (D) 0.6321 (E) 0.8647

**M2.16.** 🟡 $X\sim N(70,100)$; advance the top $10\%$. Find the cutoff. ($\Phi(1.28)=0.90$.)  (A) 72.8 (B) 80.0 (C) 82.8 (D) 84.5 (E) 90.0

**M2.17.** 🟡 Waits $\mu=8$, $\sigma=6$; over $100$ trainers find $P(\bar X<7)$. ($\Phi(1.67)=0.9525$.)  (A) 0.0475 (B) 0.0668 (C) 0.1587 (D) 0.4338 (E) 0.5000

**M2.18.** 🔴 $X\sim\text{Beta}(2,3)$. Find $E[X]$.  (A) 0.20 (B) 0.33 (C) 0.40 (D) 0.50 (E) 0.60

**M2.19.** 🔵 $X\sim\text{Gamma}(2,3)$. Find $P(X>6)$. ($e^{-2}=0.1353$.)  (A) 0.135 (B) 0.271 (C) 0.406 (D) 0.500 (E) 0.677

**M2.20.** 🔴 $M(t)=\exp(3(e^t-1))$. Find $E[N]$.  (A) 1 (B) 3 (C) 6 (D) 9 (E) 12

**M2.21.** 🟡 $E[X]=10$, $E[X\wedge 8]=6.2$. Find $E[(X-8)_+]$.  (A) 1.8 (B) 2.0 (C) 3.0 (D) 3.8 (E) 6.2

**M2.22.** 🔴 $X\sim\text{Unif}(0,2)$. Find $E[X^2]$.  (A) 1/3 (B) 1/2 (C) 2/3 (D) 4/3 (E) 2

**Multivariate RVs (Topic 3).**

**M2.23.** 🟡 $f(x,y)=x+y$ on the unit square. Find the marginal $f_X(x)$.  (A) $x$ (B) $x+1/2$ (C) $2x$ (D) $1/2$ (E) $x+1$

**M2.24.** 🟡 $E[X]=1$, $E[Y]=2$, $E[XY]=3$. Find $\text{Cov}(X,Y)$.  (A) -1 (B) 0 (C) 1 (D) 2 (E) 3

**M2.25.** 🔵 Bias $P\sim\text{Unif}(0,1)$; given $P=p$ a flip is heads w.p. $p$. A flip is heads. Find $E[P\mid H]$.  (A) 0.50 (B) 0.60 (C) 0.667 (D) 0.75 (E) 0.80

**M2.26.** 🔴 Independent $X,Y$: $\text{Var}(X)=5$, $\text{Var}(Y)=3$. Find $\text{Var}(X+2Y)$.  (A) 8 (B) 11 (C) 13 (D) 17 (E) 23

**M2.27.** 🔵 $N\sim\text{Poisson}(3)$; given $N=n$, strengths i.i.d. mean $2$, var $5$; $S$ = total. Find $\text{Var}(S)$.  (A) 12 (B) 15 (C) 27 (D) 33 (E) 45

**M2.28.** 🟡 Three independent $\text{Unif}(0,1)$. Find $P(\min>0.5)$.  (A) 0.0625 (B) 0.1250 (C) 0.2500 (D) 0.5000 (E) 0.8750

**M2.29.** 🟡 $f(x,y)=4xy$ on the unit square. Independent? And $f_X(x)$?  (A) dep; $2x$ (B) indep; $2x$ (C) indep; $x$ (D) dep; $4x$ (E) indep; $1$

**M2.30.** 🔵 $36$ matches, potions mean $4$, sd $3$; court stocked $162$. Treating the total as continuous, find $P(\text{total}>162)$. ($\Phi(1.0)=0.8413$.)  (A) 0.0228 (B) 0.0668 (C) 0.1587 (D) 0.3085 (E) 0.5000

#### Mock B — Scored Answers

**Quick-answer table:**

| # | Ans | # | Ans | # | Ans |
|---|---|---|---|---|---|
| M2.1 | B | M2.11 | B | M2.21 | D |
| M2.2 | B | M2.12 | C | M2.22 | D |
| M2.3 | B | M2.13 | E | M2.23 | B |
| M2.4 | B | M2.14 | C | M2.24 | C |
| M2.5 | B | M2.15 | B | M2.25 | C |
| M2.6 | C | M2.16 | C | M2.26 | D |
| M2.7 | B | M2.17 | A | M2.27 | C |
| M2.8 | B | M2.18 | C | M2.28 | B |
| M2.9 | A | M2.19 | C | M2.29 | B |
| M2.10 | C | M2.20 | B | M2.30 | C |

**Full worked solutions:**

- **M2.1 (B, 0.41)** — *at-least-one.* $1-(0.9)^5=0.410$.
- **M2.2 (B, 0.40)** — *independence.* $P(A\mid B)=P(A)=0.4$.
- **M2.3 (B, 924)** — *combination.* $\binom{12}{6}=924$.
- **M2.4 (B, 0.42)** — *total probability.* $(2/5)(0.6)+(3/5)(0.3)=0.42$.
- **M2.5 (B, 0.46)** — *Bayes.* $\dfrac{0.3(1)}{0.3(1)+0.7(0.5)}=0.30/0.65=0.46$.
- **M2.6 (C, 0.90)** — *3-event inclusion–exclusion.* $1.5-0.7+0.1=0.9$.
- **M2.7 (B, 0.504)** — *count distinct / total.* $(10\cdot9\cdot8\cdot7)/10^4=0.504$.
- **M2.8 (B, 0.234)** — *binomial.* $\binom{6}{4}(0.5)^6=15/64=0.234$.
- **M2.9 (A, 0.138)** — *negative binomial.* $\binom{4}{2}(0.4)^3(0.6)^2=0.138$.
- **M2.10 (C, 1.00)** — *Var from moments.* $E[B]=1.0$, $E[B^2]=2.0$, $\text{Var}=1.0$.
- **M2.11 (B, 0.7745)** — *interval.* $\Phi(1.5)-\Phi(-1)=0.9332-0.1587=0.7745$.
- **M2.12 (C, 0.406)** — *binomial→Poisson.* $\text{Pois}(2)$: $3e^{-2}=0.406$.
- **M2.13 (E, 18)** — *gamma integral.* Exponential $E[X^2]=2\theta^2=2(9)=18$. No parts.
- **M2.14 (C, 13.52)** — *deductible payment variance, memoryless.* $E[Y]=4e^{-0.5}=2.426$; $E[Y^2]=32e^{-0.5}=19.41$; $\text{Var}=19.41-5.886=13.52$.
- **M2.15 (B, 0.1353)** — *survival of exponential.* $S(10)=e^{-2}=0.1353$.
- **M2.16 (C, 82.8)** — *inverse normal.* $c=70+1.28(10)=82.8$.
- **M2.17 (A, 0.0475)** — *CLT mean.* $\text{sd}(\bar X)=0.6$, $z=-1.67$; $1-0.9525=0.0475$.
- **M2.18 (C, 0.40)** — *beta mean.* $\alpha/(\alpha+\beta)=2/5=0.4$.
- **M2.19 (C, 0.406)** — *gamma tail via Poisson-sum.* $e^{-2}(1+2)=3e^{-2}=0.406$.
- **M2.20 (B, 3)** — *MGF ⇒ Poisson(3).* $E[N]=\lambda=3$.
- **M2.21 (D, 3.8)** — *master identity.* $E[(X-8)_+]=E[X]-E[X\wedge8]=10-6.2=3.8$.
- **M2.22 (D, 4/3)** — *$E[g(X)]$.* $\int_0^2 x^2\tfrac12 dx=\tfrac12\cdot\tfrac83=\tfrac43$.
- **M2.23 (B, $x+\tfrac12$)** — *marginal.* $\int_0^1(x+y)dy=x+\tfrac12$.
- **M2.24 (C, 1)** — *covariance.* $E[XY]-E[X]E[Y]=3-2=1$.
- **M2.25 (C, 0.667)** — *continuous Bayes.* Posterior $\propto p$ ⇒ $\text{Beta}(2,1)$, mean $2/3$.
- **M2.26 (D, 17)** — *independent linear combo.* $5+4(3)=17$.
- **M2.27 (C, 27)** — *total variance, Poisson.* $3(5)+3(2^2)=15+12=27=\lambda E[\text{str}^2]$.
- **M2.28 (B, 0.125)** — *min order statistic.* $(0.5)^3=0.125$.
- **M2.29 (B, indep; $2x$)** — *factoring.* $4xy=(2x)(2y)$ over a rectangle ⇒ independent, $f_X=2x$.
- **M2.30 (C, 0.1587)** — *CLT sum.* mean $144$, sd $18$, $z=1$; $1-0.8413=0.1587$.

#### Mock B — Pacing Post-Mortem

| Metric | Your result | Target |
|---|---|---|
| Raw score | ___ / 30 | **24+** |
| Topic 1 / 2 / 3 correct | ___/8, ___/14, ___/8 | 6+, 11+, 6+ |
| Total time | ___ min | ≤ 180 |
| Problems left blank | ___ | **0** |

| # missed | Archetype | Root cause | Fix + retest |
|---|---|---|---|
| | | | |

---

### ▶ MOCK C — Final Round (M3.1–M3.30)

**General Probability (Topic 1).**

**M3.1.** 🔴 Spinner: $P(A)=0.35$, $P(B)=0.25$ (disjoint). Find $P(\text{neither})$.  (A) 0.10 (B) 0.25 (C) 0.40 (D) 0.50 (E) 0.60

**M3.2.** 🟡 Machine X makes $60\%$ ($2\%$ defective), Y makes $40\%$ ($5\%$ defective). A defective is found. Find $P(\text{Y})$.  (A) 0.375 (B) 0.500 (C) 0.625 (D) 0.700 (E) 0.800

**M3.3.** 🟡 Split $9$ into labeled squads of $3,3,3$. How many ways?  (A) 84 (B) 280 (C) 504 (D) 1680 (E) 362880

**M3.4.** 🔴 $4$ red, $6$ blue; draw $2$ without replacement. Find $P(\text{both red})$.  (A) 0.067 (B) 0.133 (C) 0.160 (D) 0.200 (E) 0.400

**M3.5.** 🔴 $4$ contests, each won w.p. $0.25$. Find $P(\text{at least one win})$.  (A) 0.316 (B) 0.500 (C) 0.684 (D) 0.750 (E) 0.938

**M3.6.** 🔴 $P(A)=0.3$, $P(B)=0.4$, $P(A\cap B)=0.12$. Independent, disjoint, or neither?  (A) disjoint (B) independent (C) neither (D) both (E) can't tell

**M3.7.** 🟡 Five distinct badges in a row at random. Find $P(\text{Boulder and Cascade adjacent})$.  (A) 0.20 (B) 0.30 (C) 0.40 (D) 0.50 (E) 0.60

**M3.8.** 🟡 $5$ throws, each success w.p. $0.4$. Find $P(\text{at least }4)$.  (A) 0.077 (B) 0.087 (C) 0.231 (D) 0.317 (E) 0.663

**Univariate RVs (Topic 2).**

**M3.9.** 🟡 Short ($0.6$): $\text{Exp}(\text{mean }3)$; long ($0.4$): $\text{Exp}(\text{mean }8)$. Find $E[\text{damage}]$.  (A) 3.0 (B) 4.4 (C) 5.0 (D) 5.5 (E) 8.0

**M3.10.** 🔴 $X\sim\text{Beta}(2,3)$. Find $\text{Var}(X)$.  (A) 0.01 (B) 0.04 (C) 0.06 (D) 0.10 (E) 0.24

**M3.11.** 🟡 Pidgey rate $2$/hr, Spearow $3$/hr (independent Poisson). Find $P(\text{exactly }4\text{ total})$. ($e^{-5}=0.006738$.)  (A) 0.140 (B) 0.156 (C) 0.175 (D) 0.195 (E) 0.210

**M3.12.** 🟡 $S(x)=e^{-x/4}$, $x\ge 0$. Find $E[X]$ by the survival method.  (A) 2 (B) 4 (C) 8 (D) 12 (E) 16

**M3.13.** 🔴 $X\sim N(70,100)$. By the empirical rule, $P(50\le X\le 90)$.  (A) 0.68 (B) 0.95 (C) 0.997 (D) 0.50 (E) 0.475

**M3.14.** 🔵 $X\sim\text{Exp}(5)$, $d=3$. Find expected payment **per payment**.  (A) 2.0 (B) 3.0 (C) 5.0 (D) 5.5 (E) 8.0

**M3.15.** 🟡 $M(t)=(1-2t)^{-3}$, $t<1/2$. Find $E[X]$.  (A) 2 (B) 3 (C) 5 (D) 6 (E) 9

**M3.16.** 🔵 Loss is $0$ w.p. $0.3$, else $\text{Unif}(0,10)$. Find $E[\text{loss}]$.  (A) 2.5 (B) 3.5 (C) 5.0 (D) 7.0 (E) 10.0

**M3.17.** 🟡 $X\sim\text{Bin}(144,0.5)$, $\mu=72$, $\sigma=6$. Normal approx **with** continuity correction: $P(X\ge 80)$. ($\Phi(1.25)=0.8944$.)  (A) 0.0668 (B) 0.0918 (C) 0.1056 (D) 0.1587 (E) 0.2266

**M3.18.** 🔴 $X\sim\text{Gamma}(4,2)$. Find $\text{Var}(X)$.  (A) 4 (B) 8 (C) 16 (D) 32 (E) 64

**M3.19.** 🔴 Each pull wins w.p. $0.25$; $X$ = pulls to the first win. Find $E[X]$.  (A) 0.25 (B) 1.33 (C) 3.0 (D) 4.0 (E) 5.0

**M3.20.** 🔴 $E[R]=5$, $\text{Var}(R)=4$. Find $\text{Var}(3R-2)$.  (A) 4 (B) 10 (C) 12 (D) 34 (E) 36

**M3.21.** 🟡 $X\sim\text{Exp}(10)$. Find the median. ($\ln 2=0.6931$.)  (A) 5.0 (B) 6.93 (C) 7.0 (D) 10.0 (E) 13.86

**M3.22.** 🔴 $X\sim\text{Unif}(2,10)$. Find $P(X>7)$.  (A) 0.250 (B) 0.300 (C) 0.375 (D) 0.500 (E) 0.700

**Multivariate RVs (Topic 3).**

**M3.23.** 🔴 $f(x,y)=1$ on the unit square. Find $P(X+Y<1)$.  (A) 0.25 (B) 0.50 (C) 0.667 (D) 0.75 (E) 1.00

**M3.24.** 🟡 $N\sim\text{Poisson}(3)$; given $N=n$, $E[S\mid N=n]=2n$. Find $E[S]$.  (A) 2 (B) 3 (C) 5 (D) 6 (E) 9

**M3.25.** 🔵 Rates $1/5$ and $1/10$; series system. Find expected time to failure.  (A) 2.5 (B) 3.33 (C) 5.0 (D) 7.5 (E) 15.0

**M3.26.** 🟡 $\text{Var}(X)=9$, $\text{Var}(Y)=16$, $\text{Cov}=-6$. Find $\text{Var}(X+Y)$.  (A) 7 (B) 13 (C) 19 (D) 25 (E) 37

**M3.27.** 🔵 $N\sim\text{Poisson}(4)$, $X_i\sim\text{Exp}(5)$. Find $E[T]$.  (A) 5 (B) 9 (C) 20 (D) 25 (E) 100

**M3.28.** 🔵 For that aggregate ($E[T]=20$, $\text{Var}(T)=200$, sd $14.142$), find $P(T>30)$. ($\Phi(0.71)=0.7611$; $T$ continuous.)  (A) 0.159 (B) 0.211 (C) 0.239 (D) 0.309 (E) 0.401

**M3.29.** 🟡 $\text{Cov}=4$, $\text{Var}(X)=16$, $\text{Var}(Y)=25$. Find $\text{Corr}(X,Y)$.  (A) 0.16 (B) 0.20 (C) 0.25 (D) 0.40 (E) 0.50

**M3.30.** 🟡 Five $\text{Unif}(0,1)$. Find $P(\max<0.8)$.  (A) 0.168 (B) 0.328 (C) 0.410 (D) 0.512 (E) 0.800

#### Mock C — Scored Answers

**Quick-answer table:**

| # | Ans | # | Ans | # | Ans |
|---|---|---|---|---|---|
| M3.1 | C | M3.11 | C | M3.21 | B |
| M3.2 | C | M3.12 | B | M3.22 | C |
| M3.3 | D | M3.13 | B | M3.23 | B |
| M3.4 | B | M3.14 | C | M3.24 | D |
| M3.5 | C | M3.15 | D | M3.25 | B |
| M3.6 | B | M3.16 | B | M3.26 | B |
| M3.7 | C | M3.17 | C | M3.27 | C |
| M3.8 | B | M3.18 | C | M3.28 | C |
| M3.9 | C | M3.19 | D | M3.29 | B |
| M3.10 | B | M3.20 | E | M3.30 | B |

**Full worked solutions:**

- **M3.1 (C, 0.40)** — *disjoint + complement.* $1-(0.35+0.25)=0.4$.
- **M3.2 (C, 0.625)** — *Bayes.* $\dfrac{0.4(0.05)}{0.6(0.02)+0.4(0.05)}=0.020/0.032=0.625$.
- **M3.3 (D, 1680)** — *multinomial.* $9!/(3!^3)=362880/216=1680$.
- **M3.4 (B, 0.133)** — *sequential without replacement.* $(4/10)(3/9)=0.133$.
- **M3.5 (C, 0.684)** — *at-least-one.* $1-(0.75)^4=0.684$.
- **M3.6 (B, independent)** — *test.* $P(A)P(B)=0.12=P(A\cap B)$; intersection $>0$ ⇒ not disjoint.
- **M3.7 (C, 0.40)** — *block trick.* $(4!\cdot2!)/5!=48/120=0.4$.
- **M3.8 (B, 0.087)** — *binomial upper tail.* $\binom{5}{4}(0.4)^4(0.6)+(0.4)^5=0.0768+0.0102=0.087$.
- **M3.9 (C, 5.0)** — *mixture mean.* $0.6(3)+0.4(8)=5.0$.
- **M3.10 (B, 0.04)** — *beta variance.* $6/(25\cdot6)=1/25=0.04$.
- **M3.11 (C, 0.175)** — *Poisson superposition.* $\text{Pois}(5)$: $e^{-5}5^4/4!=0.175$.
- **M3.12 (B, 4)** — *Darth Vader.* $\int_0^\infty e^{-x/4}dx=4$.
- **M3.13 (B, 0.95)** — *empirical rule.* $[50,90]=\mu\pm2\sigma\Rightarrow0.95$.
- **M3.14 (C, 5.0)** — *memoryless per-payment.* Given $X>d$, excess is fresh $\text{Exp}(5)$, mean $=\theta=5$.
- **M3.15 (D, 6)** — *MGF ⇒ Gamma$(3,2)$.* $E[X]=\alpha\theta=6$.
- **M3.16 (B, 3.5)** — *mixed.* $0.3(0)+0.7(5)=3.5$.
- **M3.17 (C, 0.1056)** — *continuity correction.* left edge $79.5$: $1-\Phi(1.25)=1-0.8944=0.1056$.
- **M3.18 (C, 16)** — *gamma variance.* $\alpha\theta^2=4(4)=16$.
- **M3.19 (D, 4)** — *geometric mean.* $1/p=1/0.25=4$.
- **M3.20 (E, 36)** — *linear transform.* $3^2(4)=36$.
- **M3.21 (B, 6.93)** — *exponential median.* $\theta\ln2=10(0.6931)=6.93$.
- **M3.22 (C, 0.375)** — *uniform.* $(10-7)/(10-2)=3/8=0.375$.
- **M3.23 (B, 0.5)** — *uniform on square.* triangle area $=1/2$.
- **M3.24 (D, 6)** — *total expectation.* $E[2N]=2(3)=6$.
- **M3.25 (B, 3.33)** — *min of exponentials.* rate $1/5+1/10=3/10$; $E=10/3=3.33$.
- **M3.26 (B, 13)** — *linear combo with covariance.* $9+16+2(-6)=13$.
- **M3.27 (C, 20)** — *compound mean.* $E[N]E[X]=4(5)=20$.
- **M3.28 (C, 0.239)** — *CLT tail (continuous, no cc).* $z=10/14.142=0.71$; $1-0.7611=0.239$.
- **M3.29 (B, 0.20)** — *correlation.* $4/(4\cdot5)=0.2$.
- **M3.30 (B, 0.328)** — *max order statistic.* $(0.8)^5=0.328$.

#### Mock C — Pacing Post-Mortem

| Metric | Your result | Target |
|---|---|---|
| Raw score | ___ / 30 | **24+** |
| Topic 1 / 2 / 3 correct | ___/8, ___/14, ___/8 | 6+, 11+, 6+ |
| Total time | ___ min | ≤ 180 |
| Problems left blank | ___ | **0** |

| # missed | Archetype | Root cause | Fix + retest |
|---|---|---|---|
| | | | |

**After all three mocks:** sweep your three error logs for the **same root cause appearing twice** — that recurring slip is the single highest-value fix before exam day. Clear it, then you are Champion-ready in fact, not just in title.
:::

## Badge Earned — Indigo League Champion

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/earth_badge.png" alt="The eight badges arrayed beneath the Indigo League Champion crest." style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Indigo League Champion — Exam P Ready!</strong> Rank: Champion-ready · 8 badges · 3 mocks cleared.</figcaption>
</figure>

You faced Gary across the championship battlefield, named every archetype before the pencil moved, and turned the whole journey into a single clean win. **Rank: Champion-ready (8 badges + the three mocks).** You earn the **Indigo League Champion** title — and declare yourself Exam-P ready — when you can, unaided:

**Mastery checklist — tick each before exam day:**

- ☐ **Pace** a 30-question mock in 3 hours at $\sim\!6$ minutes per question, running the two-pass strategy and **never leaving a blank**. *(Entry №19·1.)*
- ☐ **Drive the calculator** reflexively — 1-Var Stats for a pmf mean/variance, one-press $\binom{n}{k}$, stored $e^{-\lambda}$, store-don't-retype. *(Entry №19·2.)*
- ☐ **Recognize** a problem's archetype from the stem alone — no topic label — and **deploy** the matching shortcut on sight: gamma integral, Darth-Vader survival rule, MGF kernel-matching, exponential memorylessness, Poisson $\mu=\sigma^2=\lambda$, binomial$\to$Poisson, continuity correction. *(Entry №19·3.)*
- ☐ **Run** the standing sanity checks ($P\in[0,1]$, $\text{Var}\ge0$, $E[\text{payment}]\le E[\text{loss}]$, support consistency, tail-past-mean $<0.5$) so an impossible answer is never bubbled. *(Entry №19·4.)*
- ☐ **Keep an error log** — classify every miss by root cause and retest the archetype until the slip is gone. *(Entry №19·5.)*
- ☐ **Score** $24/30$ or better, with correct method and six-minute pacing, on **all three** mock exams; reach **Earned Level 7+**.

> **Gym rematch pointers.** Miss the pacing or score gate → redo a mock with a hard six-minute timer and the error log. Calculator costing you minutes → drill Concept 2 on every mock problem. Wrong tool named → drill the recognition map (Concept 3) until reflexive. Wrong identity → return to each shortcut's home chapter (gamma/MGF/survival → ch03/ch08/ch10, memorylessness/Poisson → ch05/ch11, loss models → ch06/ch13, CLT/continuity → ch12, order stats → ch17). Bubbled an impossible value → make the guardrail scan a fixed last step.

*The journey from Pallet Town is complete. Eight badges, the Elite Four, the Champion — all behind you. Walk into the real exam the way you walked into this chamber: you have seen every move before, you recognize the type on sight, and you do not let one number bully you. Go earn your 10.*

---

<!-- ===== CALLOUT BOX TEMPLATES (Pandoc fenced divs; styled by book/theme.css) =====
     ::: cold-open / now-playing / pokedex-entry / trainers-tip / team-rocket / kanto-realworld
     Concept gate ("Do you already own this?") and problem-set / answer-key also styled. -->

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
