<!--
  file: ch03_discrete_moments
  tier: A
  outcomes: 2a,2c,2d
  tia: A.3
  locale: S.S. Anne -> Vermilion
  type: electric
  maps_to: S.S. Anne cruise + Vermilion Gym, Lt. Surge -- magnitude (mean) & reliability (variance)
-->

# Describing a Whole Population by Its Distribution {.type-electric}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with the sea route to Vermilion City highlighted; Vermilion, home of the Thunder Badge, is marked as the current destination after Cerulean." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 10 — you have left Cerulean with the Cascade Badge, boarded the luxury liner <em>S.S. Anne</em>, and are sailing for Vermilion City: home of Lt. Surge and the Thunder Badge.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "Battle Aboard the St. Anne"**

The **S.S. Anne** is enormous. Thousands of trainers crowd her decks for the cruise to Vermilion — far too many to track one by one. You couldn't write down what *each* passenger is doing if you tried. Yet the ship's purser keeps a single tidy ledger, and from it she can answer almost any question: *how many badges does a typical passenger hold? what's the most common number? how spread out are they?*

She isn't listing people. She's listing a **distribution** — for each possible value, what *fraction* of passengers have it. One small table stands in for the whole crowd.

Then the lights flicker. **Team Rocket** has rigged the hull, and the great ship begins to list. As alarms wail, a grim new question takes over: *how long will she stay afloat?* The captain's damage report reads like the purser's ledger turned sideways — for each moment, the chance the **ship is still above water past that moment.** "She'll likely go under around the third deck," the captain mutters, "but I want the *average*, not the typical case. Tell me the **expected** number of decks that hold."

You realize the crowd and the sinking are the *same* mathematics. A passenger's badge count and the ship's failing decks are both **random variables** — quantities whose value you can't know in advance, only describe by *how probability is spread across the possibilities*. And the captain's question — the **average**, weighted across every possibility, not the most likely single outcome — is a number you don't yet know how to compute.

*How do you collapse an entire distribution into one honest number — its center — and then say how widely it scatters around that center?*
:::

## Where You Are — 60-Second Retrieval

**Rank: Rookie Trainer · Badges: 1 (Cascade).** You earned the **Cascade Badge** at Cerulean by running clues *backward* with Bayes' theorem. The load-bearing idea you carry onto the ship is **conditional weighting**: in the law of total probability you computed an overall rate by *weighting each case's value by how likely that case is* — $P(A)=\sum_i P(B_i)\,P(A\mid B_i)$, a **weighted average of conditional rates.** Hold onto that phrase. The **expected value** in this chapter is *exactly* a weighted average — now of the *values a quantity takes*, weighted by their probabilities. Cerulean taught you to weight outcomes; Vermilion teaches you to weight *numbers*.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the last chapter**

Answer from memory; if any feels shaky, flip back before continuing.

1. A day is rainy w.p. $0.3$; the gym floods w.p. $0.5$ on rainy days, $0.05$ on dry days. What is $P(\text{flood})$? *(Answer: $(0.3)(0.5)+(0.7)(0.05)=0.185$ — a weighted average of the two flood rates.)*
2. Why is $0.185$ guaranteed to land between $0.05$ and $0.5$? *(Answer: a weighted average always sits between its smallest and largest input.)*
3. Probabilities of a complete list of disjoint outcomes must sum to what? *(Answer: $1$.)*

All three instant? You're ready — the "weighted average" reflex and the "probabilities sum to 1" reflex are the whole foundation of moments. Any hesitation? Reclaim it first.
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP014 "Electric Shock Showdown" + EP015 "Battle Aboard the St. Anne"**

In **EP015** Ash and friends board the glamorous cruise liner *S.S. Anne*, a floating crowd of trainers swapping and battling Pokémon — until Team Rocket's scheme leaves the ship listing and the heroes scrambling to escape as she founders (our cold-open dramatizes this sinking; the "expected decks that hold" framing is an in-world extension for the math, not an on-screen line). In **EP014** Ash reaches **Vermilion City** and challenges **Lt. Surge** for the **Thunder Badge** — and famously *loses the first bout* before adapting his strategy and winning the rematch: a perfect picture of this chapter's twin themes, raw **magnitude** (mean power) versus **reliability** (low variance). *Watch EP015 then EP014 right before this chapter* — the crowd, the sinking, and the electric gym are the three scenes the math lives in.
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice crackles through the Pokédex's Actuary Mode as the deck tilts under your feet.

"Ash — you can no longer reason about *one* outcome at a time. On a ship of thousands, and across a distribution of possibilities, you must describe the *whole* with a handful of summary numbers: where it's **centered** and how far it **spreads.** These are an actuary's daily bread. The expected number of claims, the variance of a loss — every premium ever priced rests on the two ideas you're about to build. This is a **Tier A** chapter; take it one summary number at a time."

By the end of this chapter you will be able to:

- **Describe** a discrete random variable with its **pmf, cdf, and survival function**, and read probabilities off any of the three. *(Outcome 2a.)*
- **Locate the center** three different ways — **mode, median/percentiles, and the mean (expected value)** — and know when they disagree. *(Outcomes 2a, 2c.)*
- **Compute expected values** of $X$ and of functions $g(X)$ and linear transforms $aX+b$, including the **survival-function ("Darth-Vader") method** $E[X]=\sum_{k\ge0}S(k)$. *(Outcome 2c.)*
- **Measure spread** with the **variance and standard deviation**, via the definition *and* the computational formula $\Var(X)=E[X^2]-(E[X])^2$, and apply $\Var(aX+b)=a^2\Var(X)$. *(Outcome 2c.)*
- **Recognize and use** the **moment generating function** $M_X(t)=E[e^{tX}]$ to extract moments, and the **discrete uniform** distribution as the simplest worked case. *(Outcomes 2c, 2d.)*

> *Exam-weight signpost.* Univariate random variables are the **single largest slice of Exam P (44–50%)**, and mean/variance computations sit at the center of it. The **1-Var Stats calculator workflow** you learn here (the chapter's flagship technique) will reclaim minutes on exam day. This is a **Tier A** chapter — full treatment, reused in every distribution chapter that follows.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own All of Vermilion?**

Already fluent? Prove it. Work these five, ~3 minutes each, *with correct method*. Use the pmf $p(0)=0.1,\ p(1)=0.2,\ p(2)=0.3,\ p(3)=0.25,\ p(4)=0.15$ for the first three.

1. Find the **mode** and the **median** of $X$.
2. Find $E[X]$ — and then re-find it as $\sum_{k\ge0}S(k)$.
3. Find $\Var(X)$ and the standard deviation.
4. If $Y=3X+2$, find $E[Y]$ and $\Var(Y)$.
5. $X$ is discrete uniform on $\{1,2,\dots,10\}$. Find $E[X]$ and $\Var(X)$.

*(Answers: mode $2$, median $2$; $E[X]=2.15$ both ways; $\Var=1.4275,\ \sigma\approx1.195$; $E[Y]=8.45,\ \Var(Y)=12.8475$; $E[X]=5.5,\ \Var(X)=8.25$.)* Five for five with the right reasoning? **Skip to the Gym Challenge** and claim the badge. Any miss or hesitation? The teaching below was built for you — and each concept has its own skip-gate, so even a partial owner loses no time.
:::

---

We build nine ideas, in TIA's order and increasing difficulty. We start with the *language* of a random variable, then locate its **center** three ways, then compute the **mean** and its shortcuts, then measure **spread**, then meet the **MGF** and the simplest named distribution. Each gets a "do you already own this?" skip-check, the full nine-beat lesson, and a Pokédex Entry.

0. **The random variable & its pmf / cdf / survival** — the language everything else speaks
1. **The mode** — the most likely single value *(A.3.1)*
2. **The median & percentiles** — the middle, and any cut-point *(A.3.2)*
3. **Expected value** — the weighted-average center, the mean *(A.3.3)*
4. **Tools for means** — $E[g(X)]$, linearity, $E[aX+b]$ *(A.3.4)*
5. **The survival-function (Darth-Vader) method** — the mean as area under $S$ *(A.3.5)*
6. **Variance — the definition** — average squared distance from the mean *(A.3.6)*
7. **Variance tools & $\Var(aX+b)$** — the computational formula and transforms *(A.3.7)*
8. **The moment generating function** — and the **discrete uniform** distribution *(A.3.8)*

## Concept 0 — The Random Variable and Its pmf, cdf, and Survival Function

::: concept-gate
**DO YOU ALREADY OWN THIS? — RV language**

For the ship's RV $X$ = intact decks, with $p(0)=0.1,\ p(1)=0.2,\ p(2)=0.3,\ p(3)=0.25,\ p(4)=0.15$, find $F(2)=P(X\le 2)$ and $S(2)=P(X>2)$.

If you instantly wrote **$F(2)=0.6$** and **$S(2)=0.4$** (and know $F(2)+S(2)=1$), **skip to Concept 1**. If "survival function" or the relationship $S=1-F$ is fuzzy, this section is for you.
:::

**Beat 1 — The one-sentence idea.** *A discrete random variable is a numerical quantity whose value is uncertain, and you describe it completely by listing how much probability sits on each possible value.*

**Beat 2 — Anchor + concrete instance.** As the S.S. Anne lists, let $X$ = **the number of decks that are still intact when she finally goes under.** $X$ can be $0,1,2,3,$ or $4$. From the captain's damage model, the chances are:

| $k$ (intact decks) | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $p(k)=P(X=k)$ | $0.10$ | $0.20$ | $0.30$ | $0.25$ | $0.15$ |

This list — value $\to$ probability — is the **probability mass function (pmf)**. Notice it does the same job the purser's badge ledger did for the crowd: one compact table standing in for an entire random situation.

**Beat 3 — Reason through it in plain words.** Two sanity facts make a list a *legal* pmf: every entry is a probability, so $0\le p(k)\le 1$; and the values are an exhaustive, disjoint list of what can happen, so the entries **sum to 1**: $0.10+0.20+0.30+0.25+0.15=1$. ✓ If a list doesn't sum to 1, it isn't a pmf — you've either missed a value or mis-copied one.

Often you don't want $P(X=k)$ but "$X$ is *at most* $k$" or "*more than* $k$." Accumulate the pmf from the left and you get the **cumulative distribution function (cdf)** $F(k)=P(X\le k)$; subtract from 1 and you get the **survival function** $S(k)=P(X>k)$ — literally "the ship survives past deck $k$."

**Beat 4 — Surface and dismantle the tempting wrong idea.** The classic slip is an **off-by-one on the inequality**: confusing $P(X\le k)$ with $P(X<k)$, or $P(X>k)$ with $P(X\ge k)$. For a discrete RV these differ by exactly the mass $p(k)$ sitting *on* $k$:

$$P(X<k)=F(k)-p(k), \qquad P(X\ge k)=S(k)+p(k)=1-F(k-1).$$

The point $k$ itself is *included* in $F(k)=P(X\le k)$ and *excluded* from $S(k)=P(X>k)$. Always ask: "is the endpoint in or out?" (This matters far less for continuous variables in Act II — but for discrete RVs the lone point carries real probability, so the boundary is never free.)

**Beat 5 — Translate into notation, one glyph at a time.** A capital letter is the **random variable** (the uncertain quantity); a lowercase letter is a **particular value** it might take:

$$X \quad\text{(the RV)}, \qquad k \quad\text{(a value)}, \qquad P(X=k)=p(k) \quad\text{(``the chance } X \text{ equals } k\text{'').}$$

The **cdf** accumulates, the **survival** is its complement:

$$F(k)=P(X\le k)=\sum_{j\le k}p(j), \qquad S(k)=P(X>k)=1-F(k).$$

Read $F$ aloud as "the chance $X$ is **at most** $k$," and $S$ as "the chance $X$ is **more than** $k$." The two always add to one because $X$ is *either* $\le k$ *or* $>k$, never both.

**Beat 6 — Build the three views from the instance.** Accumulate the ship's pmf:

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ |
|---|---|---|---|---|---|
| $p(k)$ | $0.10$ | $0.20$ | $0.30$ | $0.25$ | $0.15$ |
| $F(k)=P(X\le k)$ | $0.10$ | $0.30$ | $0.60$ | $0.85$ | $1.00$ |
| $S(k)=P(X>k)$ | $0.90$ | $0.70$ | $0.40$ | $0.15$ | $0.00$ |

$F$ climbs from the first probability up to $1$; $S$ falls from just-under-1 down to $0$. Each column satisfies $F(k)+S(k)=1$. The cdf is a **right-continuous staircase** — it jumps by $p(k)$ at each value and is flat between, so it is non-decreasing and ends at $1$.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* read $p(2)=0.30$ straight off the table.
- *Twist (range probabilities):* $P(1\le X\le 3)=F(3)-F(0)=0.85-0.10=0.75$ — subtract the cdf *just below* the lower end, not at it. Equivalently add $p(1)+p(2)+p(3)=0.20+0.30+0.25=0.75$. ✓
- *General:* any "more than / at least / between" question is an inequality you answer with $F$ or $S$ — never re-sum the pmf if a cdf value is handy.
- *Edge:* $S(4)=0$ and $F(4)=1$ — past the largest value, survival is impossible and the cdf is maxed.

**Beat 8 — Picture it.** The same RV wears three faces — bars for the pmf, a rising staircase for the cdf, a falling staircase for the survival.

<figure>
<img src="../../assets/diagrams/ch03_pmf_cdf_survival.png" alt="Three side-by-side panels of the same discrete random variable X = intact decks of the S.S. Anne. Left: a bar chart of the pmf with bars 0.10, 0.20, 0.30, 0.25, 0.15 over k = 0..4, with a small Pikachu sprite in the upper-left margin. Middle: the cdf as a rising right-continuous staircase climbing 0.10, 0.30, 0.60, 0.85, 1.00. Right: the survival function as a falling staircase 0.90, 0.70, 0.40, 0.15, 0.00. Each k satisfies F(k) + S(k) = 1." style="width:92%; max-width:760px; display:block; margin:1em auto;">
<figcaption>One random variable, three views: the pmf (mass on each value), the cdf $F(k)=P(X\le k)$ (rising to 1), and the survival $S(k)=P(X>k)=1-F(k)$ (falling to 0).</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now describe any discrete RV by its pmf, accumulate it into a cdf, complement it into a survival function, and answer any "$=$, $<$, $\le$, $>$, $\ge$, between" question by choosing the right one — watching the endpoint every time.

::: pokedex-entry
**POKÉDEX ENTRY №07 — Discrete RV: pmf, cdf, survival**

$$p(k)=P(X=k)\ \ge 0,\quad \sum_k p(k)=1; \qquad F(k)=P(X\le k)=\sum_{j\le k}p(j); \qquad S(k)=P(X>k)=1-F(k).$$

*In plain terms:* the pmf is the mass on each value; the cdf accumulates it; the survival is what's left. They carry the same information in three shapes.

*Recognition cue:* a **table of values and probabilities**, or words like "**at most / more than / at least / between**." Match the inequality to $F$ or $S$ and mind whether the endpoint is in or out ($P(X<k)=F(k)-p(k)$).
:::

## Concept 1 — The Mode (A.3.1)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Mode**

For the ship's pmf ($p(0)=0.1,\,p(1)=0.2,\,p(2)=0.3,\,p(3)=0.25,\,p(4)=0.15$), what is the **mode**?

If you instantly said **$2$** (the value with the *largest probability*, not the largest value), **skip to Concept 2**. If you said $4$, or you're unsure whether the mode can be a tie, read on.
:::

**Beat 1 — The one-sentence idea.** *The mode is the value the random variable is **most likely** to take — the tallest bar of the pmf.*

**Beat 2 — Anchor + concrete instance.** Scan the ship's pmf for the biggest probability. The entries are $0.10,\,0.20,\,\mathbf{0.30},\,0.25,\,0.15$. The largest is $0.30$, sitting on $k=2$. So the **mode is $2$ intact decks** — the single most likely way the ship goes under.

**Beat 3 — Reason through it in plain words.** "Most likely" is a statement about *probability*, not about *size*. You are not looking for the biggest *value* of $X$; you are looking for the value where the *bar is tallest*. Here $k=4$ is the biggest value but only the *fourth*-most likely. The mode answers "what would you bet on for a single trial?" — the typical case.

**Beat 4 — Surface and dismantle the tempting wrong idea.** *(This is Team Rocket's trap for the chapter.)* The seductive error is to **report the mode as if it were the average** — "the most common outcome is the expected outcome." It is not. The mode is the *peak*; the mean is the *balance point*, and for a skewed distribution they can be far apart. A casino that priced its payouts off the *most common* result instead of the *average* result would go bankrupt. Reporting "the typical case" when asked for "the expected case" is the single most common error in this chapter — keep the mode and the mean in separate boxes.

**Beat 5 — Translate into notation, one glyph at a time.** The mode is the **argmax** of the pmf — the value $k$ that maximizes $p(k)$:

$$\text{mode} = \arg\max_k\, p(k) \qquad \text{read aloud: ``the } k \text{ at which } p(k) \text{ is largest.''}$$

"$\arg\max$" returns the *input* that maximizes the function, not the maximum value itself: $\max_k p(k)=0.30$ but $\arg\max_k p(k)=2$.

**Beat 6 — The rule (no derivation: the mode is defined, not derived).** Unlike the mean and variance, the mode isn't computed from a formula — it is *read off* the pmf as the location of the largest mass. The only content is the tie rule: if two (or more) values share the top probability, the distribution is **bimodal** (or multimodal) and *all* of them are modes. There is nothing to derive beyond "find the tallest bar(s)."

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the ship, mode $=2$.
- *Twist (tie):* if the pmf were $0.30,\,0.30,\,0.20,\,0.10,\,0.10$ on $\{0,1,2,3,4\}$, *both* $0$ and $1$ are modes — bimodal.
- *General (formula-defined pmf):* for a Binomial$(n,p)$ later, the mode is near $(n+1)p$; for now, just compare the masses you're given.
- *Edge:* a uniform pmf (every value equally likely) has **every** value as a mode — "no single peak."

**Beat 8 — Picture it.** On the pmf bar chart, the mode is simply the tallest bar — your eye finds it before your pencil does. (See the combined center figure in Concept 3, Beat 8, where mode, median, and mean are marked together so you can watch them disagree.)

**Beat 9 — Consolidate.** You can now find the mode of any discrete RV by locating the largest mass, handle ties as multimodality, and — crucially — you will never again report the mode when the question asks for the mean.

::: pokedex-entry
**POKÉDEX ENTRY №08 — The Mode**

$$\text{mode}=\arg\max_k p(k) \quad\text{(the value(s) with the largest probability).}$$

*In plain terms:* the most likely single value — the tallest bar. Ties give a multimodal distribution (all tied values are modes).

*Recognition cue:* "**most likely / most common / typical** value." Read it off the pmf; do **not** confuse it with the mean (the average).
:::

## Concept 2 — The Median and Percentiles (A.3.2)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Median & percentiles**

For the ship's pmf, find the **median** and the **$25^{\text{th}}$ percentile** of $X$.

If you said **median $=2$** (first $k$ with $F(k)\ge 0.5$) and **$25^{\text{th}}$ percentile $=1$** (first $k$ with $F(k)\ge 0.25$), **skip to Concept 3**. If percentiles for a *discrete* RV feel slippery, read on.
:::

**Beat 1 — The one-sentence idea.** *The median is the middle value — the smallest value at which the accumulated probability first reaches one half; a percentile generalizes this to any cut-point $p$.*

**Beat 2 — Anchor + concrete instance.** Walk up the ship's cdf until you first hit $0.5$. The cdf reads $F(0)=0.10,\,F(1)=0.30,\,F(2)=\mathbf{0.60},\,F(3)=0.85,\,F(4)=1.00$. The first value where $F(k)\ge 0.5$ is $k=2$. So the **median is $2$ intact decks**: at least half the probability is at or below $2$.

**Beat 3 — Reason through it in plain words.** The median splits the probability so that *half is at or below it.* You don't average anything; you **climb the cdf staircase** and stop the instant you've accumulated $50\%$. Because the cdf jumps in discrete steps, the "halfway" line usually lands *inside* a jump — and the convention is to take the value at the **top** of that jump, i.e. the smallest $k$ with $F(k)\ge 0.5$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two traps. First, **don't interpolate** the way you would for a continuous variable or a sorted data list: for a discrete RV with a given pmf, the median is a *value the RV can take*, found from the cdf — not "halfway between two values." Second, **the median is not the mean.** Here median $=2$ but (as you'll see) the mean is $2.15$; for skewed distributions they differ, and reporting one for the other loses money. (When a jump lands *exactly* on $0.5$ — i.e. $F(k)=0.5$ exactly — any value in $[k,k+1]$ technically qualifies and conventions vary; the exam-safe choice is the smallest such $k$.)

**Beat 5 — Translate into notation, one glyph at a time.** The $100p^{\text{th}}$ **percentile** $\pi_p$ is the smallest value whose cdf reaches $p$:

$$\pi_p=\min\{\,k : F(k)\ge p\,\} \qquad \text{read aloud: ``the smallest } k \text{ whose cumulative probability is at least } p\text{.''}$$

The **median** is the $50^{\text{th}}$ percentile, $\pi_{0.5}$. **Quartiles** are $\pi_{0.25}$ and $\pi_{0.75}$.

**Beat 6 — Apply the definition.** Read percentiles straight off the cdf row.

- *Median* ($p=0.5$): first $F(k)\ge0.5$ is $F(2)=0.60$, so $\pi_{0.5}=2$.
- *$25^{\text{th}}$ percentile* ($p=0.25$): first $F(k)\ge0.25$ is $F(1)=0.30$, so $\pi_{0.25}=1$. (Note $F(0)=0.10<0.25$, so $0$ does *not* qualify.)
- *$75^{\text{th}}$ percentile* ($p=0.75$): first $F(k)\ge0.75$ is $F(3)=0.85$, so $\pi_{0.75}=3$.

No formula — just "climb the staircase to the cut-line."

**Beat 7 — Ramp the difficulty.**

- *Simplest:* median of the ship, $2$.
- *Twist (exact landing):* if $F(k)$ equalled $0.5$ exactly at some $k$, take that smallest $k$ (exam convention).
- *General (any percentile):* the $90^{\text{th}}$ percentile is the first $k$ with $F(k)\ge 0.9$; for the ship that's $F(4)=1.00\Rightarrow \pi_{0.9}=4$.
- *Edge:* the median is robust to extreme tails — adding a tiny chance of a huge value barely moves it, whereas it *does* move the mean. That robustness is exactly why insurers report both.

**Beat 8 — Picture it.** On the rising cdf staircase, draw a horizontal line at height $p$; the percentile is the $k$-value where the staircase first rises to or above that line. (The combined center figure in Concept 3 marks the median against the mode and mean.)

**Beat 9 — Consolidate.** You can now find the median and any percentile of a discrete RV by climbing its cdf to the cut-line, handle the exact-landing convention, and explain why the median (robust) and the mean (pulled by tails) differ.

::: pokedex-entry
**POKÉDEX ENTRY №09 — Median & Percentiles**

$$\pi_p=\min\{k:F(k)\ge p\}, \qquad \text{median}=\pi_{0.5}.$$

*In plain terms:* climb the cdf staircase until the accumulated probability first reaches $p$; that value is the percentile. The median is the half-way cut.

*Recognition cue:* "**middle / median / $k^{\text{th}}$ percentile / quartile**." Build the cdf, then read the first value past the cut-line. It is **robust** to tails (unlike the mean).
:::

## Concept 3 — Expected Value: The Weighted-Average Center (A.3.3)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Expected value**

The captain wants the **expected** number of intact decks for the ship's pmf. Compute $E[X]$.

If you wrote **$E[X]=\sum_k k\,p(k)=2.15$** (and you know why it's *not* the mode $2$ and *not* a plain average of $0\!-\!4$), **skip to Concept 4**. If you reached for the mode or the simple average $\tfrac{0+1+2+3+4}{5}=2$, read on.
:::

**Beat 1 — The one-sentence idea.** *The expected value is the long-run average outcome — each possible value weighted by how likely it is — the balance point of the distribution.*

**Beat 2 — Anchor + concrete instance.** This is the law-of-total-probability reflex from Cerulean, now applied to *numbers*: weight each value by its probability and add. For the ship,

$$E[X]=0(0.10)+1(0.20)+2(0.30)+3(0.25)+4(0.15).$$

**Beat 3 — Reason through it in plain words.** Imagine the ship sinks $1{,}000$ times under the same damage model. About $100$ times $0$ decks hold, $200$ times $1$ deck holds, $300$ times $2$, $250$ times $3$, $150$ times $4$. The *total* decks-that-held across all $1{,}000$ sinkings is $0(100)+1(200)+2(300)+3(250)+4(150)=2{,}150$, so the **average per sinking** is $2{,}150/1{,}000=2.15$. The expected value *is* that long-run average — and you get it directly by using the probabilities as weights instead of imagining $1{,}000$ trials.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two tempting wrong centers:

- The **mode** ($2$): "the most common outcome." But the captain asked for the *average*, which the heavier upper tail ($k=3,4$) pulls above the peak.
- The **plain average of the values** $\tfrac{0+1+2+3+4}{5}=2$: this secretly assumes every value is *equally likely*. They aren't — $k=2$ carries three times the mass of $k=0$. You must weight by $p(k)$.

The correct $E[X]=2.15$ is *above* both, because probability is shifted toward the larger values. **The mean is a weighted average, never a count-them-up average.**

**Beat 5 — Translate into notation, one glyph at a time.** The expected value (a.k.a. the **mean**, written $\mu$) sums *value times probability*:

$$E[X]=\sum_k k\,p(k)=\mu \qquad \text{read aloud: ``the sum, over every value } k\text{, of } k \text{ times its probability.''}$$

Each term $k\,p(k)$ is "this value, scaled by how much it counts." The $\sum$ just says "add those products." The result is one number — the distribution's center of mass.

**Beat 6 — Derive it from the instance.** The long-run-average argument *is* the derivation. Over $N$ trials, value $k$ occurs about $N\,p(k)$ times, contributing $k\cdot N\,p(k)$ to the total. Sum over $k$ and divide by $N$:

$$\text{average}=\frac{\sum_k k\,(N\,p(k))}{N}=\sum_k k\,p(k)=E[X].$$

The $N$'s cancel — exactly the way the counts cancelled in conditioning back at Cerulean. So $E[X]=\sum_k k\,p(k)$ isn't asserted; it *is* the limiting average. For the ship:

$$E[X]=0(0.10)+1(0.20)+2(0.30)+3(0.25)+4(0.15)=0+0.20+0.60+0.75+0.60=2.15.\ \checkmark$$

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the ship, $E[X]=2.15$.
- *Twist (skew shifts the mean):* compare to the right-skewed "battles won" RV in the figure below, where the mean sits well above the mode.
- *General:* for any pmf, multiply each value by its probability and sum — even infinitely many values, provided the sum converges (you'll meet that with the geometric and Poisson in ch05).
- *Sanity boundary:* the mean must lie between the smallest and largest possible value, $0\le 2.15\le 4$. ✓ A "mean" outside the support is an arithmetic error.

**Beat 8 — Picture it: three centers, side by side.** Mode, median, and mean answer *different* questions and, for a skewed pmf, give *different* numbers.

<figure>
<img src="../../assets/diagrams/ch03_mean_median_mode.png" alt="A right-skewed pmf for X = battles won per day at Vermilion, with bars 0.40, 0.25, 0.15, 0.10, 0.06, 0.04 over k = 0..5. Three vertical markers: a solid green line at the mode = 0 (the tallest bar), a dashed blue line at the median = 1, and a dotted red line at the mean = 1.29. A callout notes that right-skew pushes mode < median < mean." style="width:78%; max-width:560px; display:block; margin:1em auto;">
<figcaption>For a right-skewed pmf the three centers disagree: <strong>mode</strong> (tallest bar) $<$ <strong>median</strong> (cdf cut-line) $<$ <strong>mean</strong> (balance point, pulled rightward by the tail).</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now compute the expected value of any discrete RV as the probability-weighted sum of its values, explain why it differs from the mode and the median, and sanity-bound it within the support.

::: pokedex-entry
**POKÉDEX ENTRY №10 — Expected Value (the Mean)**

$$E[X]=\sum_k k\,p(k)=\mu.$$

*In plain terms:* the long-run average — each value weighted by its probability; the distribution's balance point. It lies between the smallest and largest possible value.

*Recognition cue:* "**expected / average / mean / on average / in the long run / per**." Weight by probability and sum; never report the mode or an unweighted average.
:::

## Concept 4 — Tools for Means: $E[g(X)]$, Linearity, and $E[aX+b]$ (A.3.4)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Mean tools**

For the ship's RV ($E[X]=2.15$), suppose each intact deck is worth $\$3$M in salvage plus a $\$2$M fixed survey fee, so payout $Y=3X+2$. Find $E[Y]$. Also find $E[X^2]$.

If you wrote **$E[Y]=3(2.15)+2=8.45$** *without* re-summing, and **$E[X^2]=\sum k^2p(k)=6.05$**, **skip to Concept 5**. If you re-built a whole new pmf for $Y$, read on — there's a far faster way.
:::

**Beat 1 — The one-sentence idea.** *To average a **function** of $X$, weight the function's values by the same probabilities; and because expectation is just a weighted sum, it passes straight through constants and addition — $E[aX+b]=aE[X]+b$.*

**Beat 2 — Anchor + concrete instance.** The salvage payout is $Y=3X+2$ ($\$3$M per intact deck, plus a $\$2$M flat fee). You *could* build $Y$'s pmf from scratch — but you don't have to. Two tools handle every such question: the **law of the unconscious statistician** (for any function $g$) and **linearity** (for the special case $aX+b$).

**Beat 3 — Reason through it in plain words.** To average $g(X)$, you don't need $g(X)$'s own pmf — you already know how often each $X$-value occurs, and each one *determines* a $g$-value. So weight $g(k)$ by the *same* $p(k)$ and sum. And when $g$ is linear, $g(X)=aX+b$, scaling every value by $a$ scales the average by $a$, and adding $b$ to every value adds $b$ to the average. A constant fee shifts the mean by exactly the fee; a per-unit rate scales the mean by exactly the rate.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The dangerous reflex is to push the function *inside* the expectation: writing $E[X^2]=(E[X])^2$, or $E[g(X)]=g(E[X])$. **This is false for nonlinear $g$.** Here $(E[X])^2=2.15^2=4.6225$, but $E[X^2]=6.05$ — not equal. (The gap between them is exactly the variance, as Concept 7 will reveal.) Expectation moves freely through *linear* operations only; for squares, exponentials, reciprocals, you must average the function's values, not plug the mean into the function. *(Pushing $E$ through a square is the variance-version of Team Rocket's trap — watch for it.)*

**Beat 5 — Translate into notation, one glyph at a time.** For any function $g$, the **law of the unconscious statistician (LOTUS)**:

$$E[g(X)]=\sum_k g(k)\,p(k) \qquad \text{read aloud: ``average the values of } g\text{, weighted by } p(k)\text{.''}$$

And **linearity of expectation** for constants $a,b$:

$$E[aX+b]=a\,E[X]+b, \qquad E[a]=a \quad(\text{a constant averages to itself}).$$

**Beat 6 — Derive both from the definition.** LOTUS is immediate: $g(X)$ takes value $g(k)$ exactly when $X=k$, which has probability $p(k)$, so $E[g(X)]=\sum_k g(k)p(k)$. Linearity then drops out by choosing $g(k)=ak+b$ and splitting the sum:

$$E[aX+b]=\sum_k (ak+b)\,p(k)=a\underbrace{\sum_k k\,p(k)}_{E[X]}+b\underbrace{\sum_k p(k)}_{=\,1}=a\,E[X]+b.$$

The second sum is $1$ because a pmf sums to one — that's why the constant survives as a plain $+b$.

Apply it. The salvage payout:

$$E[Y]=E[3X+2]=3E[X]+2=3(2.15)+2=8.45 \ (\$\text{M}).$$

And the **second moment** $E[X^2]$ via LOTUS with $g(k)=k^2$:

$$E[X^2]=\sum_k k^2 p(k)=0(0.10)+1(0.20)+4(0.30)+9(0.25)+16(0.15)=0+0.20+1.20+2.25+2.40=6.05.$$

(You'll need exactly this $E[X^2]=6.05$ for the variance in Concept 7.)

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $E[3X+2]=8.45$ by linearity (no new pmf).
- *Twist (nonlinear $g$):* $E[X^2]=6.05$ by LOTUS — and note $E[X^2]\ne (E[X])^2=4.6225$.
- *General:* any $g$ — a payout schedule, a squared loss, $e^{tX}$ (the MGF in Concept 8) — uses the same $\sum g(k)p(k)$.
- *Edge:* $E[aX+b]=aE[X]+b$ holds for **any** RV, dependent or not — linearity never requires independence. (Contrast variance, Concept 7, where $a$ gets *squared* and a cross-term can appear for sums.)

**Beat 8 — Picture it.** Linearity is a relabeling of the same bars: stretch the $k$-axis by $a$ and shift it by $b$, and the balance point moves the same way — the picture of "$3X+2$ scales and slides the distribution." (No new figure needed; it's the Concept-3 pmf with a stretched, shifted axis.)

**Beat 9 — Consolidate.** You can now average any function of $X$ with LOTUS, pull constants and sums straight through expectation with linearity, compute $E[X^2]$ for the variance to come, and you will never again write $E[X^2]=(E[X])^2$.

::: pokedex-entry
**POKÉDEX ENTRY №11 — Tools for Means (LOTUS & Linearity)**

$$E[g(X)]=\sum_k g(k)\,p(k); \qquad E[aX+b]=a\,E[X]+b.$$

*In plain terms:* average a function by weighting its values; expectation passes through scaling and shifting. But for **nonlinear** $g$, $E[g(X)]\ne g(E[X])$ — average the function, don't plug in the mean.

*Recognition cue:* a **payout/cost as a function of $X$**, or a **rescaled** quantity ($aX+b$). Linear $\to$ use $aE[X]+b$; nonlinear (squares, $e^{tX}$) $\to$ LOTUS sum.
:::

## Concept 5 — The Survival-Function (Darth-Vader) Method (A.3.5)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Darth-Vader rule**

For the ship ($S(0)=0.90,\,S(1)=0.70,\,S(2)=0.40,\,S(3)=0.15$), find $E[X]$ by summing the survival function.

If you wrote **$E[X]=\sum_{k\ge0}S(k)=0.90+0.70+0.40+0.15=2.15$** and got the *same* $2.15$ as $\sum k\,p(k)$, **skip to Concept 6**. If you've never seen the mean computed from the survival function, this elegant shortcut is for you.
:::

**Beat 1 — The one-sentence idea.** *For a **non-negative integer** random variable, the mean equals the sum of its survival function — add up the chances of "more than $0$," "more than $1$," "more than $2$," …*

**Beat 2 — Anchor + concrete instance.** The captain's damage report is *already* in survival form ("chance the ship holds past deck $k$"). Rather than convert back to a pmf, sum the survival column directly:

$$E[X]=S(0)+S(1)+S(2)+S(3)=0.90+0.70+0.40+0.15=2.15.$$

Same answer, fewer multiplications — no $k\cdot p(k)$ products at all.

**Beat 3 — Reason through it in plain words.** Here's the picture that makes it obvious. Think of $X$ as a stack of unit "blocks." $X\ge 1$ contributes a block whenever the ship survives past deck $0$ — probability $S(0)$. $X\ge 2$ contributes another whenever it survives past deck $1$ — probability $S(1)$. And so on. The *expected number of blocks* is just the sum of the chances each block is present: $E[X]=S(0)+S(1)+S(2)+\cdots$. You're counting the same expected total a different way — by layers instead of by values.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two guardrails. First, the method needs $X$ to be a **non-negative** integer RV ($X\in\{0,1,2,\dots\}$); it does **not** apply as-is to a variable that can go negative. Second, sum the **survival** $S(k)=P(X>k)$, *not* the cdf $F(k)$ — and start at $k=0$. A common slip is to sum $P(X\ge k)$ from $k=1$ instead; that also works (it's the same list shifted), but mixing the two conventions double-counts or drops a term. Pick one form — we use $\sum_{k\ge 0}P(X>k)$ — and stick to it.

**Beat 5 — Translate into notation, one glyph at a time.** For a non-negative integer RV:

$$E[X]=\sum_{k=0}^{\infty} S(k)=\sum_{k=0}^{\infty}P(X>k) \qquad \text{read aloud: ``sum the chances of exceeding } 0,1,2,\dots\text{''}$$

(The nickname: imagine stacking the probability "layers" like Vader's cape — hence the *Darth-Vader rule*. The continuous twin, $E[X]=\int_0^\infty S(x)\,dx$, returns in ch10.)

**Beat 6 — Derive it from the definition.** Start from $E[X]=\sum_{k\ge0} k\,p(k)$ and rewrite each $k$ as a count of the integers below it, $k=\sum_{j=0}^{k-1}1$. Swapping the order of summation (a tidy interchange of two sums):

$$E[X]=\sum_{k=0}^{\infty} k\,p(k)=\sum_{k=0}^{\infty}\ \sum_{j=0}^{k-1} p(k)=\sum_{j=0}^{\infty}\ \sum_{k=j+1}^{\infty} p(k)=\sum_{j=0}^{\infty} P(X>j)=\sum_{j=0}^{\infty}S(j).$$

The inner sum $\sum_{k>j}p(k)$ is exactly $P(X>j)=S(j)$. So the survival sum *is* the mean — derived, not asserted.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the ship, $E[X]=0.90+0.70+0.40+0.15=2.15$. ✓ (matches $\sum k\,p(k)$).
- *Twist (when it shines):* if you're *handed* the survival function (or a cdf) and never the pmf, this is the fast path — no conversion needed.
- *General:* works for any non-negative integer RV with a convergent mean (geometric, Poisson — ch05).
- *Edge:* $S(k)\to 0$ as $k$ grows (here $S(4)=0$), so the infinite sum has only finitely many nonzero terms for a bounded RV; for unbounded RVs the tail must shrink fast enough to converge.

**Beat 8 — Picture it.** Plot the survival function as a falling staircase. Each step is a unit-wide rectangle of height $S(k)$; its **area** is the term $S(k)$. The total shaded area under the staircase *is* $E[X]$ — the discrete echo of "area under the survival curve."

<figure>
<img src="../../assets/diagrams/ch03_darthvader_area.png" alt="The survival function of the ship RV drawn as a falling staircase, with four shaded unit-width rectangles of heights S(0)=0.90, S(1)=0.70, S(2)=0.40, S(3)=0.15. A callout adds the bar areas: E[X] = 0.90 + 0.70 + 0.40 + 0.15 = 2.15, noting this equals the sum-k-p(k) answer of 2.15 -- two roads to the mean." style="width:78%; max-width:560px; display:block; margin:1em auto;">
<figcaption>The Darth-Vader rule made visual: $E[X]=\sum_{k\ge0}S(k)$ is the <strong>area</strong> under the survival staircase — each unit-wide bar of height $S(k)$ contributes one term. The areas sum to $2.15$, the same mean as $\sum k\,p(k)$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now compute the mean of a non-negative integer RV by summing its survival function — a one-line shortcut whenever you're handed $S$ or $F$ instead of the pmf — and you know it agrees exactly with $\sum k\,p(k)$.

::: pokedex-entry
**POKÉDEX ENTRY №12 — Survival-Function (Darth-Vader) Method**

For a non-negative integer RV,
$$E[X]=\sum_{k=0}^{\infty} S(k)=\sum_{k=0}^{\infty}P(X>k).$$

*In plain terms:* the mean is the area under the survival staircase — add the chances of exceeding $0,1,2,\dots$. The continuous twin is $E[X]=\int_0^\infty S(x)\,dx$ (ch10).

*Recognition cue:* you're **given the survival function or cdf** (not the pmf), or the problem is naturally phrased as "lasts longer than $k$." Sum $S$ directly — no $k\,p(k)$ products.
:::

## Concept 6 — Variance: The Definition (A.3.6)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Variance (definition)**

Using the ship's RV ($\mu=2.15$), set up the variance as $E[(X-\mu)^2]$. What does each piece mean?

If you can write **$\Var(X)=\sum_k (k-2.15)^2\,p(k)$** and say "it's the average *squared* distance from the mean," **skip to Concept 7** for the fast formula. If "why squared?" is unclear, read on.
:::

**Beat 1 — The one-sentence idea.** *Variance is the average **squared** distance of the random variable from its mean — a single number for how widely the distribution scatters around its center.*

**Beat 2 — Anchor + concrete instance.** Lt. Surge cares about two things in a Pokémon: raw power (the **mean**) and *reliability* — does it perform consistently, or wildly? Two Pokémon can have the *same* average output yet feel completely different in battle: one steady, one erratic. Variance is the number that tells them apart. For the ship, the mean is $\mu=2.15$; variance asks how far the actual $X$ typically lands from $2.15$.

**Beat 3 — Reason through it in plain words.** Measure each value's distance from the mean, $k-\mu$. If you just *averaged* those distances you'd get **zero** — the mean is the balance point, so positive and negative deviations cancel by design. To stop the cancellation you **square** each deviation (making it non-negative), then average the squares, weighting by probability. Big deviations get *disproportionately* large squares, so variance is especially sensitive to far-flung values — exactly the "erratic" behavior Surge wants to penalize.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Why not average the *raw* deviations, or their *absolute* values? Raw deviations sum to zero (useless: $E[X-\mu]=E[X]-\mu=0$ always). Absolute values avoid the cancellation but are algebraically clumsy — $|X-\mu|$ doesn't expand or combine cleanly across sums. **Squaring** both kills the cancellation *and* keeps the algebra clean (it expands, and it gives the tidy computational formula of Concept 7). The price is units: variance is in *squared* units, which is why we also take its square root.

**Beat 5 — Translate into notation, one glyph at a time.** The variance is the expected squared deviation; its square root is the **standard deviation** $\sigma$, back in the original units:

$$\Var(X)=E\big[(X-\mu)^2\big]=\sigma^2, \qquad \SD(X)=\sigma=\sqrt{\Var(X)}.$$

Read $\Var$ aloud as "the average of $(X \text{ minus its mean})$ squared." The symbol $\sigma^2$ (sigma-squared) *is* the variance; $\sigma$ is the standard deviation.

**Beat 6 — Compute from the definition.** Average the squared deviations of the ship RV, weighting by $p(k)$, with $\mu=2.15$:

$$\begin{aligned}
\Var(X)&=\sum_k (k-2.15)^2\,p(k)\\
&=(0-2.15)^2(0.10)+(1-2.15)^2(0.20)+(2-2.15)^2(0.30)\\
&\quad+(3-2.15)^2(0.25)+(4-2.15)^2(0.15)\\
&=(4.6225)(0.10)+(1.3225)(0.20)+(0.0225)(0.30)+(0.7225)(0.25)+(3.4225)(0.15)\\
&=0.46225+0.26450+0.00675+0.180625+0.513375=1.4275.
\end{aligned}$$

So $\Var(X)=1.4275$ and $\sigma=\sqrt{1.4275}\approx 1.195$ intact decks. (Concept 7's shortcut will reproduce this in two terms instead of five.)

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the definition sum above, $\Var=1.4275$.
- *Twist (same mean, different spread):* see the figure — two pmfs both centered at $2$, one tight ($\Var=0.80$), one erratic ($\Var=2.20$). Mean alone can't tell them apart; variance can.
- *General:* the definition $\sum(k-\mu)^2 p(k)$ works for any discrete RV — but it's tedious, which motivates the next concept.
- *Edge:* $\Var(X)\ge 0$ always (a sum of non-negative terms), and $\Var(X)=0$ **iff** $X$ is a constant (no spread at all).

**Beat 8 — Picture it.** Spread, not center, is the story.

<figure>
<img src="../../assets/diagrams/ch03_variance_spread.png" alt="Two side-by-side pmfs over k = 0..4, both with mean 2 marked by a green dotted line. Left ('Reliable: low variance'): mass concentrated at the center, 0.05, 0.20, 0.50, 0.20, 0.05, with Var(X) = 0.80. Right ('Erratic: high variance'): mass pushed to the ends, 0.25, 0.10, 0.30, 0.10, 0.25, with Var(X) = 2.20." style="width:82%; max-width:620px; display:block; margin:1em auto;">
<figcaption>Same mean ($2$), different variance: the tight distribution is <strong>reliable</strong> ($\Var=0.80$); the end-loaded one is <strong>erratic</strong> ($\Var=2.20$). Variance is the number that distinguishes them — exactly what Lt. Surge tests.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now define and compute variance as the probability-weighted average of squared deviations, explain why we square, read the standard deviation as the same idea in original units, and see that mean alone is blind to spread.

::: pokedex-entry
**POKÉDEX ENTRY №13 — Variance (Definition)**

$$\Var(X)=E\big[(X-\mu)^2\big]=\sum_k (k-\mu)^2 p(k)=\sigma^2, \qquad \SD(X)=\sigma=\sqrt{\Var(X)}.$$

*In plain terms:* the average squared distance from the mean — the spread. We square so deviations don't cancel and the algebra stays clean. $\Var\ge 0$, and $=0$ only for a constant.

*Recognition cue:* "**spread / variability / consistency / risk / how far from average / standard deviation**." Center is the mean; spread is the variance.
:::

## Concept 7 — Variance Tools and $\Var(aX+b)$ (A.3.7)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Variance tools**

For the ship ($E[X]=2.15$, $E[X^2]=6.05$), find $\Var(X)$ with the computational formula. Then find $\Var(3X+2)$.

If you wrote **$\Var(X)=6.05-2.15^2=1.4275$** and **$\Var(3X+2)=9(1.4275)=12.8475$** (the $+2$ vanishes, the $3$ gets *squared*), **skip to Concept 8**. If you'd have re-summed squared deviations, or kept the $+2$, read on.
:::

**Beat 1 — The one-sentence idea.** *Variance is fastest as "the second moment minus the squared mean," $\Var(X)=E[X^2]-(E[X])^2$; and under a linear transform the shift drops out while the scale is **squared**, $\Var(aX+b)=a^2\Var(X)$.*

**Beat 2 — Anchor + concrete instance.** You already computed both moments in Concept 4: $E[X]=2.15$ and $E[X^2]=6.05$. The computational formula turns those two numbers straight into the variance — no deviation table needed:

$$\Var(X)=E[X^2]-(E[X])^2=6.05-2.15^2=6.05-4.6225=1.4275.$$

Same $1.4275$ as the five-term definition sum — in one subtraction.

**Beat 3 — Reason through it in plain words.** The computational formula says: "average of the squares, minus the square of the average." Those two are equal *only* when $X$ is constant; their **gap is the variance.** (This is the precise reason $E[X^2]\ne (E[X])^2$ from Concept 4 — the difference isn't an error, it's exactly $\sigma^2$.) For the transform: adding a constant $b$ slides every value (and the mean) by the same amount, so *distances from the mean don't change* — variance ignores shifts. Scaling by $a$ stretches every distance by $a$, and since variance is built from *squared* distances, it stretches by $a^2$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Three classic slips:

- **Dropping the $(E[X])^2$ term:** writing $\Var(X)=E[X^2]=6.05$. Wrong — you must subtract the squared mean ($1.4275$, not $6.05$). *(This is the variance form of Team Rocket's trap.)*
- **Forgetting to square $a$:** writing $\Var(3X+2)=3\Var(X)$. Wrong — the scale is *squared*: $9\Var(X)$.
- **Keeping the $+b$:** writing $\Var(3X+2)=9\Var(X)+2$. Wrong — a constant shift adds *zero* variance.

**Beat 5 — Translate into notation, one glyph at a time.** The computational ("shortcut") formula and the linear-transform rule:

$$\Var(X)=E[X^2]-\big(E[X]\big)^2; \qquad \Var(aX+b)=a^2\,\Var(X), \qquad \SD(aX+b)=|a|\,\SD(X).$$

Read the transform aloud: "scaling by $a$ multiplies the variance by $a$-squared; adding $b$ changes nothing." Note the SD uses $|a|$ (a standard deviation is never negative).

**Beat 6 — Derive both.** *Computational formula:* expand the squared deviation and use linearity (Concept 4):

$$\Var(X)=E[(X-\mu)^2]=E[X^2-2\mu X+\mu^2]=E[X^2]-2\mu\,E[X]+\mu^2=E[X^2]-2\mu^2+\mu^2=E[X^2]-\mu^2.$$

(We used $E[X]=\mu$ and that $\mu$ is a constant.) *Transform rule:* let $Y=aX+b$, so $E[Y]=a\mu+b$ and

$$\Var(aX+b)=E\big[(aX+b-(a\mu+b))^2\big]=E\big[(a(X-\mu))^2\big]=a^2E[(X-\mu)^2]=a^2\Var(X).$$

The $b$'s cancel inside the square — that's *why* shifts don't matter — and the $a$ comes out squared.

Apply it to the salvage payout $Y=3X+2$:

$$\Var(Y)=3^2\,\Var(X)=9(1.4275)=12.8475, \qquad \SD(Y)=3\,\sigma=3(1.195)\approx 3.586\ (\$\text{M}).$$

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $\Var(X)=6.05-4.6225=1.4275$ from the two moments.
- *Twist (transform):* $\Var(3X+2)=9\Var(X)=12.8475$; the $+2$ vanishes.
- *General:* compute $E[X]$ and $E[X^2]$ once (or read $\bar x,\sigma x$ off the calculator), then *every* variance and transform follows.
- *Edge / sanity:* always $E[X^2]\ge (E[X])^2$ (so variance $\ge0$); if your subtraction goes negative, you mis-computed a moment. And $\Var(-X)=(-1)^2\Var(X)=\Var(X)$ — negating doesn't change spread.

**Beat 8 — Picture it: the flagship calculator workflow.** All of this — $E[X]=\bar x$ and $\Var(X)=\sigma x^2$ — falls out of one screen on the TI-30XS MultiView's **1-Var Stats** engine. Enter the values in L1 and the probabilities in L2, run 1-Var Stats with FRQ:L2, and read the mean and population SD directly.

<figure>
<img src="../../assets/diagrams/ch03_1var_stats_keypad.png" alt="A schematic of the TI-30XS MultiView 1-Var-Stats workflow in three numbered steps. Step 1: press the data key to open the list editor and enter L1 = 0 1 2 3 4, L2 = .10 .20 .30 .25 .15. Step 2: press 2nd then stat to launch the statistics menu, choose 1-Var Stats, set DATA:L1 and FRQ:L2, then CALC. Step 3: read the results screen showing x-bar = 2.15 and sigma-x = 1.195. A summary banner concludes E[X] = x-bar = 2.15 and Var(X) = sigma-x squared = (1.195)^2 ~ 1.43, with a warning to use sigma-x (population SD) not sx (sample SD)." style="width:88%; max-width:720px; display:block; margin:1em auto;">
<figcaption>The flagship technique: <strong>1-Var Stats</strong> reads $E[X]=\bar x$ and $\sigma x$ (so $\Var=\sigma x^2$) straight off one screen. Use $\sigma x$ (population SD), never $sx$ (sample SD).</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now get the variance in one subtraction from the two moments, transform it correctly under $aX+b$ (square the scale, ignore the shift), and read both the mean and variance off the calculator's 1-Var Stats screen.

::: pokedex-entry
**POKÉDEX ENTRY №14 — Variance Tools & Transforms**

$$\Var(X)=E[X^2]-\big(E[X]\big)^2; \qquad \Var(aX+b)=a^2\Var(X); \qquad \SD(aX+b)=|a|\,\SD(X).$$

*In plain terms:* variance is "mean of the square minus square of the mean." A shift adds no variance; a scale multiplies it by the scale **squared**.

*Recognition cue:* asked for a variance from a pmf $\to$ compute $E[X]$, $E[X^2]$, subtract. A **rescaled** RV $\to$ $a^2\Var(X)$. Never drop the $(E[X])^2$ term; never forget to square $a$.
:::

## Concept 8 — The Moment Generating Function & the Discrete Uniform (A.3.8)

::: concept-gate
**DO YOU ALREADY OWN THIS? — MGF & discrete uniform**

(a) If $M_X(t)=E[e^{tX}]$, how do you get $E[X]$ and $E[X^2]$ from it? (b) For $X$ discrete uniform on $\{1,\dots,n\}$, state $E[X]$ and $\Var(X)$.

If you said **(a) differentiate and set $t=0$: $E[X]=M_X'(0)$, $E[X^2]=M_X''(0)$**, and **(b) $E[X]=\frac{n+1}{2},\ \Var(X)=\frac{n^2-1}{12}$**, **skip to the Worked Examples**. Otherwise, read on.
:::

**Beat 1 — The one-sentence idea.** *The moment generating function packs **all** the moments of $X$ into one function; differentiating it at $t=0$ "pops out" the mean, the second moment, and beyond — and the discrete uniform is the simplest distribution to see every tool at work.*

**Beat 2 — Anchor + concrete instance.** Suppose Lt. Surge's gym has $n$ identical training pads numbered $1$ to $n$ and you step onto one **uniformly at random** — every pad equally likely. That's the **discrete uniform** on $\{1,2,\dots,n\}$, the cleanest possible pmf ($p(k)=1/n$ for each $k$). Its mascot is **Ditto**, which takes any form with equal ease — every value equally likely. We'll use it to exercise the mean and variance tools, and the MGF to extract moments.

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/front/132.png" alt="Ditto, the Transform Pokemon, mascot of the discrete uniform distribution" style="width:120px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#132 Ditto — the discrete-uniform mascot</strong> (any form, equally likely)</figcaption>
</figure>

**Beat 3 — Reason through it in plain words.** Why an MGF? Computing $E[X]$, $E[X^2]$, $E[X^3]$, … one LOTUS sum at a time is tedious. The MGF is a single object — the expected value of $e^{tX}$ — whose **derivatives at $t=0$** hand you the moments in order, because the Taylor series of $e^{tX}$ has $X^k$ sitting in its $k$-th term. It's a moment vending machine: differentiate $n$ times, set $t=0$, collect the $n$-th moment. (It has a second superpower — sums of independent RVs *multiply* their MGFs — which we'll cash in for the Poisson and Normal later.)

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is **forgetting to evaluate at $t=0$** — or confusing the MGF *value* with a moment. $M_X(t)$ itself is not a moment; the *derivative at zero* is. Always $M_X(0)=E[e^0]=E[1]=1$ (a free sanity check: every MGF passes through $1$ at $t=0$). The moments come from the **slopes** there: $M_X'(0)$, $M_X''(0)$, and so on.

**Beat 5 — Translate into notation, one glyph at a time.** The MGF and the moment-extraction rule:

$$M_X(t)=E\big[e^{tX}\big]=\sum_k e^{tk}\,p(k); \qquad E[X^r]=M_X^{(r)}(0)=\left.\frac{d^r}{dt^r}M_X(t)\right|_{t=0}.$$

Read it aloud: "the $r$-th moment is the $r$-th derivative of the MGF, evaluated at $t=0$." In particular $E[X]=M_X'(0)$ and $E[X^2]=M_X''(0)$, so $\Var(X)=M_X''(0)-\big(M_X'(0)\big)^2$.

**Beat 6 — Derive the moment-extraction, then the discrete-uniform moments.** *Why differentiation works:* expand $e^{tX}=\sum_{r\ge0}\frac{(tX)^r}{r!}$ and take expectations term by term:

$$M_X(t)=E[e^{tX}]=\sum_{r=0}^\infty \frac{t^r}{r!}E[X^r]=1+tE[X]+\tfrac{t^2}{2}E[X^2]+\cdots.$$

This is a power series in $t$ whose coefficient of $t^r$ is $E[X^r]/r!$; differentiating $r$ times and setting $t=0$ isolates exactly $E[X^r]$.

*Discrete-uniform moments* (the cleanest case — derive by direct LOTUS, using the standard sums $\sum_{k=1}^n k=\frac{n(n+1)}{2}$ and $\sum_{k=1}^n k^2=\frac{n(n+1)(2n+1)}{6}$):

$$E[X]=\sum_{k=1}^n k\cdot\frac1n=\frac1n\cdot\frac{n(n+1)}2=\frac{n+1}{2}.$$

$$\begin{aligned}
E[X^2]&=\frac1n\cdot\frac{n(n+1)(2n+1)}6=\frac{(n+1)(2n+1)}6,\\
\Var(X)&=E[X^2]-\big(E[X]\big)^2=\frac{(n+1)(2n+1)}6-\frac{(n+1)^2}4=\frac{n^2-1}{12}.
\end{aligned}$$

(The last step is routine algebra over a common denominator of $12$.) So a discrete uniform on $\{1,\dots,n\}$ has mean $\frac{n+1}2$ and variance $\frac{n^2-1}{12}$.

**Beat 7 — Ramp the difficulty.**

- *Simplest (a die-like uniform):* $n=6$ gives $E[X]=\frac{7}{2}=3.5$ and $\Var(X)=\frac{35}{12}\approx2.917$.
- *Twist (MGF check on $n=6$):* $M_X(t)=\frac16\sum_{k=1}^{6}e^{tk}$; differentiating and setting $t=0$ returns $M_X'(0)=\frac16(1+2+\cdots+6)=3.5=E[X]$. ✓
- *General uniform on $\{1,\dots,n\}$:* mean $\frac{n+1}{2}$, variance $\frac{n^2-1}{12}$ — the formulas above.
- *Edge:* a uniform on $\{a,a+1,\dots,b\}$ ($m=b-a+1$ values) is a shifted copy: $E[X]=\frac{a+b}{2}$ and $\Var(X)=\frac{m^2-1}{12}$ — the shift moves the mean but, by Concept 7, leaves the variance to depend only on the *count* of values.

**Beat 8 — Picture it.** The discrete uniform is a *flat* pmf — every bar the same height $1/n$ — so it has no single mode (every value is a mode), its mean and median both sit at the center $\frac{n+1}{2}$, and its spread $\frac{n^2-1}{12}$ grows with the range. (Flat bars; see the Pokédex Entry stat block.)

**Beat 9 — Consolidate.** You can now extract any moment by differentiating the MGF at $t=0$ (with the free check $M_X(0)=1$), and you own the discrete uniform's mean $\frac{n+1}{2}$ and variance $\frac{n^2-1}{12}$ as a fully worked example of every tool in the chapter.

::: pokedex-entry
**POKÉDEX ENTRY №15 — MGF & the Discrete Uniform**

**MGF:** $\displaystyle M_X(t)=E[e^{tX}]$, with $E[X^r]=M_X^{(r)}(0)$; in particular $E[X]=M_X'(0)$, $E[X^2]=M_X''(0)$, and $M_X(0)=1$ always.

**Discrete uniform on $\{1,\dots,n\}$** (mascot: Ditto #132): $p(k)=\frac1n$; $\ E[X]=\dfrac{n+1}{2}$; $\ \Var(X)=\dfrac{n^2-1}{12}$.

*In plain terms:* the MGF is a moment vending machine — differentiate at $0$. The discrete uniform spreads probability evenly across $n$ values: center at $\frac{n+1}{2}$, spread $\frac{n^2-1}{12}$.

*Recognition cue:* "**MGF / generate the moments / $M_X(t)$**" $\to$ differentiate at $0$. "**Equally likely / chosen at random from $\{1,\dots,n\}$**" $\to$ discrete uniform; quote the formulas.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:170px; text-align:center;">
<img src="../../assets/vs/ltsurge.png" alt="Lt. Surge, the Vermilion City Gym Leader" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Lt. Surge — Vermilion Gym Leader, your moments mentor</figcaption>
</figure>

Four examples, fading from fully narrated to exam speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how, on the calculator*), because the mean/variance workflow is the load-bearing skill of the whole univariate act.

### Worked Example 1 — The Captain's Damage Report (full narration; understanding-first)

**ARCHETYPE:** *Full center + spread of a discrete RV from its pmf — the bread-and-butter Topic-2 item.*

**Setup.** The S.S. Anne's intact-deck RV has pmf $p(0)=0.10,\ p(1)=0.20,\ p(2)=0.30,\ p(3)=0.25,\ p(4)=0.15$. Find the mode, the median, $E[X]$, $\Var(X)$, and $\sigma$. Then the salvage payout is $Y=3X+2$ ($\$$M); find $E[Y]$ and $\Var(Y)$.

**Step 1 — Identify (what's the question really asking?).** "Mode/median" = center by *peak* and by *cut-line*; "$E[X]$/$\Var$" = center by *balance* and *spread*; "$Y=3X+2$" = a *linear transform*, so use linearity, not a new pmf.

**Step 2 — Professor's Path (the why).**
*Mode:* largest mass is $p(2)=0.30\Rightarrow$ **mode $=2$.**
*Median:* cdf is $0.10,0.30,\mathbf{0.60},0.85,1.00$; first $\ge0.5$ is at $k=2\Rightarrow$ **median $=2$.**
*Mean (weighted average of values):*
$$E[X]=0(0.10)+1(0.20)+2(0.30)+3(0.25)+4(0.15)=2.15.$$
*Second moment (LOTUS with $g=k^2$):*
$$E[X^2]=0+1(0.20)+4(0.30)+9(0.25)+16(0.15)=6.05.$$
*Variance (computational formula):*
$$\Var(X)=E[X^2]-(E[X])^2=6.05-2.15^2=6.05-4.6225=1.4275,\quad \sigma=\sqrt{1.4275}\approx1.195.$$
*Transform (linearity + $a^2$ rule):*
$$E[Y]=3E[X]+2=3(2.15)+2=8.45,\qquad \Var(Y)=3^2\Var(X)=9(1.4275)=12.8475.$$

**Step 3 — Trainer's Path (the fast how: 1-Var Stats).** Don't hand-sum on the exam. On the TI-30XS MultiView, press [data]{.kbd} and type the values into **L1** and the probabilities into **L2**:

[ L1: 0  1  2  3  4   ·   L2: .10  .20  .30  .25  .15 ]{.keystroke}

Then launch the stats engine and tell it the probabilities are the frequencies: [ [2nd]{.kbd} [stat]{.kbd} → 1-Var Stats · DATA: L1 · FRQ: L2 · CALC ]{.keystroke}. The screen shows $\bar x = 2.15$ (that's $E[X]$) and $\sigma x \approx 1.195$ (population SD). Square it for the variance — [ [x²]{.kbd} ]{.kbd} — giving $\Var(X)=\sigma x^2\approx 1.4275$. (Use $\sigma x$, **never** $sx$, the sample SD.) For the payout, no re-entry: [ 3 [×]{.kbd} 2.15 [+]{.kbd} 2 [enter]{.kbd} ]{.keystroke} $=8.45$ and [ 9 [×]{.kbd} 1.4275 [enter]{.kbd} ]{.keystroke} $=12.8475$.

**Step 4 — Check & pitfall.** Mean $2.15$ lies in $[0,4]$ ✓; it sits *above* the mode/median ($2$), consistent with the upper-tail mass at $k=3,4$. $E[X^2]=6.05\ge(E[X])^2=4.6225$, so $\Var=1.4275\ge0$ ✓. **Pitfalls:** reporting the mode $2$ as the mean; writing $\Var=E[X^2]=6.05$ (dropping the $-(E[X])^2$); writing $\Var(Y)=3\Var(X)$ or $9\Var(X)+2$. *(Back-ref: Entries №08–№14.)*

### Worked Example 2 — Tokens at the S.S. Anne Casino (partial guidance)

**ARCHETYPE:** *Mean two ways (pmf sum **and** survival sum) + a payout transform.*

**Setup.** A token machine on the cruise pays $T$ tokens, $T\in\{0,1,2,3\}$ with $p=0.4,0.3,0.2,0.1$. (a) Find $E[T]$ by $\sum k\,p(k)$ **and** by the survival method. (b) Each token redeems for $\$5$, minus a $\$1$ play fee, so winnings $W=5T-1$; find $E[W]$ and $\Var(W)$.

**Identify.** "Mean two ways" = direct sum vs. Darth-Vader; "$W=5T-1$" = linear transform.

**(a) Direct:** $E[T]=0(0.4)+1(0.3)+2(0.2)+3(0.1)=0.3+0.4+0.3=1.0.$
**Survival:** $S(0)=P(T>0)=0.6,\ S(1)=0.3,\ S(2)=0.1$, so $E[T]=0.6+0.3+0.1=1.0.$ ✓ *Same mean, two roads* (Entry №12).

**(b)** First the spread of $T$: $E[T^2]=0+1(0.3)+4(0.2)+9(0.1)=2.0$, so $\Var(T)=2.0-1.0^2=1.0$. Then by linearity and the $a^2$ rule:
$$E[W]=5E[T]-1=5(1.0)-1=4.0,\qquad \Var(W)=5^2\Var(T)=25(1.0)=25.0.$$

**Check & pitfall.** The two mean methods agree at $1.0$ ✓; $E[W]=4.0$ is plausible (about four dollars net per play). **Pitfall:** the $-1$ fee changes the mean but adds **zero** variance ($\Var(W)=25$, not $25-1$). *(Back-ref: Entries №11, №12, №14.)*

### Worked Example 3 — Mean Straight From the Survival Function (light guidance)

**ARCHETYPE:** *Darth-Vader method when only the cdf/survival is given.*

**Setup.** A Magnemite's number of consecutive shocks before overheating, $X\in\{0,1,2,3,4\}$, is described *only* by its cdf: $F(0)=0.10,\,F(1)=0.35,\,F(2)=0.65,\,F(3)=0.90,\,F(4)=1.00$. Find $E[X]$ without reconstructing the pmf.

Convert to survival, $S(k)=1-F(k)$: $S(0)=0.90,\,S(1)=0.65,\,S(2)=0.35,\,S(3)=0.10,\,S(4)=0$. Sum the survival (Entry №12):
$$E[X]=\sum_{k\ge0}S(k)=0.90+0.65+0.35+0.10=2.0.$$

**Check & pitfall.** Cross-check via the pmf if you like: $p(k)$ are the cdf jumps $0.10,0.25,0.30,0.25,0.10$, and $\sum k\,p(k)=0+0.25+0.60+0.75+0.40=2.0$ ✓. **Pitfall:** summing $F$ instead of $S$, or starting the sum at $k=1$. *(Back-ref: Entry №12.)*

### Worked Example 4 — A Random Training Pad (exam speed)

**ARCHETYPE:** *Discrete uniform — quote the formulas.*

<figure style="margin:1.25em auto; max-width:130px; text-align:center;">
<img src="../../assets/sprites/front/132.png" alt="Ditto, the discrete-uniform mascot" style="width:110px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">#132 Ditto — any pad, equally likely</figcaption>
</figure>

**Setup.** Lt. Surge has $10$ training pads numbered $1$–$10$; you step onto one uniformly at random. Let $X$ be the pad number. Find $E[X]$ and $\Var(X)$.

Discrete uniform on $\{1,\dots,n\}$ with $n=10$ (Entry №15):
$$E[X]=\frac{n+1}{2}=\frac{11}{2}=5.5,\qquad \Var(X)=\frac{n^2-1}{12}=\frac{99}{12}=8.25.$$

**Check & pitfall.** $5.5$ is the midpoint of $1$–$10$ ✓. **Pitfall:** using $\frac{n}{2}=5$ for the mean (off by a half) or $\frac{n^2}{12}$ for the variance (forgetting the $-1$). *(Back-ref: Entry №15.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — Drive 1-Var Stats for every mean/variance from a pmf (flagship skill)**

Any "find $E[X]$ and $\Var(X)$ from this table" problem is a calculator problem. Put values in **L1**, probabilities in **L2**, run [ [2nd]{.kbd} [stat]{.kbd} → 1-Var Stats · FRQ: L2 ]{.keystroke}, and read $\bar x=E[X]$ and $\sigma x$. Then $\Var(X)=\sigma x^2$ — square it with [x²]{.kbd}. **Always use $\sigma x$ (population SD), never $sx$ (sample SD)** — $sx$ divides by $n-1$ and gives the wrong answer for a probability distribution. Clear the lists between problems with [2nd]{.kbd} [data]{.kbd} → ClrL1/L2 so old values never leak in. This single workflow solves a huge share of Topic-2 (44–50% of the exam) in seconds.
:::

::: trainers-tip
**TRAINER'S TIP — Variance shortcut, and the two ways it bites**

Compute variance as $E[X^2]-(E[X])^2$, never the five-term deviation sum under time pressure. Two recurring errors: (1) **forgetting the $-(E[X])^2$** (you reported the raw second moment); (2) on $\Var(aX+b)$, **forgetting to square $a$** or **keeping the $+b$**. Memorize the shape: *shift adds nothing, scale squares.* If a "variance" ever comes out negative, you mis-typed a moment — $E[X^2]\ge(E[X])^2$ always.
:::

::: trainers-tip
**TRAINER'S TIP — When you're handed $S$ or $F$, sum the survival**

If a problem gives you the **survival function or cdf** for a non-negative integer RV and asks for the mean, don't rebuild the pmf — go straight to $E[X]=\sum_{k\ge0}S(k)$ (convert $S=1-F$ first if needed). It's fewer operations and fewer chances to slip. Just keep one convention: sum $P(X>k)$ starting at $k=0$.
:::

::: trainers-tip
**TRAINER'S TIP — Three centers answer three questions**

Don't compute the mean when the problem says "**most likely**" (that's the mode) or "**middle / median**" (climb the cdf). And don't quote the mode when it asks for "**expected / average**." For skewed distributions all three differ — read the verb in the question and pick the matching center.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

<figure style="margin:1em auto; max-width:150px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket — Jessie, James, and Meowth" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
</figure>

Aboard the S.S. Anne, Meowth has swiped the casino's payout sheet. "Easy money! Da machine pays out **four tokens** more often than any other amount — dat's da most common result! So da *average* payout's gotta be four tokens a pull. We rig it, we rake it in!"

Jessie grins. "Four tokens a play. We'll be rich by Vermilion."

James squints at the sheet. "But Jessie… the *big* payouts are rare, and there's a fat chance of **zero**. Doesn't the average get dragged *down* by all those zeros…?"

Meowth waves a paw. "Bah! Most common *is* average! Everybody knows dat!" — and bets the team's entire budget on a four-token average.

**Where it fails:** Meowth reported the **mode** as if it were the **mean.** The most *common* value is not the *average* value. With the real pmf — wins $W\in\{0,1,2,3,4\}$ at probabilities $0.10,0.15,0.20,0.25,0.30$ — the mode is indeed $4$, but the mean is
$$E[W]=0(0.10)+1(0.15)+2(0.20)+3(0.25)+4(0.30)=2.5,$$
not $4$. The cluster of low and zero payouts pulls the average well below the peak. Betting on a "$4$-token average" overpays by a full $60\%$. The fix is one line: *the mean is $\sum k\,p(k)$, a weighted average — never the tallest bar.* (You'll catch Meowth red-handed in Problem C3.8.)
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

This is the literal arithmetic of **pricing insurance.**

An insurer covering a block of policies cannot predict any *single* policyholder's claims — just like the purser can't track one passenger. Instead it models the **claim count** $N$ as a random variable and prices off its **expected value** $E[N]$: the *pure premium* per policy is the expected cost, $E[N]\times$(expected cost per claim). Charging the **mode** (the most common claim count — often *zero*!) instead of the **mean** would collapse the company on the first bad year — Meowth's exact mistake, with real money. The **variance** $\Var(N)$ then drives the **risk load** and the capital the insurer must hold: a book with the same expected claims but higher variance is riskier and must be priced and reserved more conservatively — precisely Lt. Surge's "magnitude *and* reliability."

The **survival function** is just as practical: actuaries routinely compute expected lifetimes and expected time-to-event as $E[X]=\sum S(k)$ (discrete) or $\int_0^\infty S(x)\,dx$ (continuous, ch10) — the foundation of life contingencies. And the **MGF** is the workhorse for combining independent risks, because the MGF of a sum is the *product* of MGFs (cashed in for the Poisson and Normal in later chapters).

*Series bridge:* expected value and variance are the first two **moments** — the start of a ladder (skewness, kurtosis) that runs through all of probability, and $E[N]$, $\Var(N)$ feed directly into **aggregate loss models** and **credibility** on the later CAS/SOA exams (STAM, MAS-I). Every premium you will ever compute begins with $E[X]$ and $\Var(X)$.

*Transfer check:* could you solve this with no Pokémon in it? "A random variable takes values $0,1,2,3,4$ with probabilities $0.10,0.20,0.30,0.25,0.15$; find its mean and variance." Same $2.15$ and $1.4275$. If you can do that, the skill has transferred.
:::

## The Gym Battle — Thunder Badge Capstone

<figure style="display:flex; gap:18px; flex-wrap:wrap; justify-content:center; align-items:flex-end; margin:1.5em auto;">
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/26.png" alt="Raichu, Lt. Surge's powerful Electric-type Pokemon" style="width:120px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;"><strong>#26 Raichu</strong> — Surge's heavy hitter</figcaption>
</figure>
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/25.png" alt="Pikachu, Ash's Electric-type Pokemon" style="width:110px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;"><strong>#25 Pikachu</strong> — Ash's reliable partner</figcaption>
</figure>
</figure>

**Lt. Surge's Challenge.** "So you beat the water girl," Surge booms, "but power is what wins at Vermilion. My **Raichu** hits *harder* than your runt Pikachu — bigger average damage. Why would you ever pick the little guy?" He drops two damage sheets on the table.

- **Raichu's** damage per turn $R\in\{0,2,4,6\}$ with probabilities $0.10,0.20,0.30,0.40$.
- **Pikachu's** damage per turn $P\in\{2,3,4,5\}$ with probabilities $0.20,0.30,0.30,0.20$.

"Compute the expected damage of each. Then — because *you* claim reliability beats raw power — compute the **variance** of each, and tell me which Pokémon you'd send into a must-not-whiff battle. Convince me, Trainer."

**ARCHETYPE:** *Compare two discrete RVs on mean **and** variance; interpret magnitude vs. reliability for a decision.*

**Step 1 — Identify.** Two pmfs; need $E$ and $\Var$ of each (the full toolkit), then a *decision* that weighs center against spread.

**Step 2 — Trainer's Path: 1-Var Stats each.** Enter Raichu's values/probs in L1/L2, run 1-Var Stats:
$$\begin{aligned}
E[R]&=0(0.10)+2(0.20)+4(0.30)+6(0.40)=0+0.4+1.2+2.4=4.0,\\
E[R^2]&=0+4(0.20)+16(0.30)+36(0.40)=20.0,\quad \Var(R)=20.0-4.0^2=4.0.
\end{aligned}$$
Now Pikachu:
$$\begin{aligned}
E[P]&=2(0.20)+3(0.30)+4(0.30)+5(0.20)=0.4+0.9+1.2+1.0=3.5,\\
E[P^2]&=4(0.20)+9(0.30)+16(0.30)+25(0.20)=13.3,\quad \Var(P)=13.3-3.5^2=1.05.
\end{aligned}$$

| | Mean $E$ | Variance $\Var$ | SD $\sigma$ |
|---|---|---|---|
| **Raichu** $R$ | $4.0$ | $4.0$ | $2.0$ |
| **Pikachu** $P$ | $3.5$ | $1.05$ | $\approx1.02$ |

**Step 3 — Professor's Path (why the decision goes to Pikachu).** Surge is right that **Raichu has the higher mean** ($4.0$ vs. $3.5$) — more *average* damage. But Raichu is **erratic**: its variance ($4.0$) is nearly *four times* Pikachu's ($1.05$), and crucially Raichu whiffs entirely ($R=0$) a full $10\%$ of the time, while Pikachu *never deals less than $2$.* In a "must-not-whiff" battle — where a single zero-damage turn loses you the match — the **floor** matters more than the average. Pikachu's tight distribution guarantees steady output; Raichu trades a half-point of average for a real chance of a catastrophic zero. **Reliability (low variance) beats raw magnitude when downside risk is fatal** — exactly the lesson Ash learns when he out-thinks Surge's Raichu instead of out-muscling it.

**Step 4 — Check, verdict & the pitfall Surge is testing.** Both means lie inside their supports ($4.0\in[0,6]$, $3.5\in[2,5]$) ✓; both $E[X^2]\ge(E[X])^2$ so both variances are positive ✓. **Verdict:** send **Pikachu** into the must-not-whiff battle — its far smaller variance and higher floor make it the safer bet despite the lower mean. The pitfall Surge is probing is *judging a risk by its mean alone* — the same blindness that makes the mode-as-mean error dangerous. Center and spread are *two* numbers, and a real decision needs both.

> "...Huh," Surge grunts, studying your variance column. "The little guy never drops below two. Maybe there's more to a battle than big numbers. The Thunder Badge is yours, Trainer."

*(If the battle instead rewarded the single biggest hit — a "highest-damage-wins" format — the calculus flips toward Raichu's heavier upper tail. Center vs. spread is always a* judgment *about what the stakes reward — see Problem C3.21.)*

## The Gym Challenge — Problem Set

::: problem-set
**THE S.S. ANNE LEDGER & THE VERMILION GYM — your questline.** Lt. Surge has set you a single escalating mission: first the **Route Trainer** legs (reading the ship's ledger and warming up your moment tools on the cruise to Vermilion), then the **Gym Battle** tier (the boss fight — full mean/variance/decision problems at exam difficulty), then the optional **Elite Challenge** post-game. Work it timed (~6 min/problem), then check the **Answers** below. Hit the mastery bar (**80%+ with correct method**) to clear the questline and claim the Thunder Badge. Problems are listed first; full worked solutions follow afterward. Markers: 🔴 routine method · 🟡 routine-with-a-twist · 🔵 stretch.

Several problems share the ship's ledger RV $X$ = intact decks, pmf $p(0)=0.10,\,p(1)=0.20,\,p(2)=0.30,\,p(3)=0.25,\,p(4)=0.15$ (so $F$ and $S$ are as tabulated in Concept 0). Each problem restates whatever it needs, so you can work them in any order.

### Route Trainers (the early legs — reading the ledger, warming up)

**C3.1.** 🔴 *(The purser asks for the single most likely badge count among passengers.)* Passenger badge counts $B\in\{0,1,2,3\}$ have pmf $0.50,0.30,0.15,0.05$. Find the **mode** and the **median** of $B$.

**C3.2.** 🔴 *(How many Thunder Shocks does Pikachu land in a warm-up bout?)* $N\in\{1,2,3\}$ with pmf $0.5,0.3,0.2$. Find $E[N]$.

**C3.3.** 🔴 *(Read the captain's survival report directly.)* A lifeboat's time-to-launch $X\in\{0,1,2,3\}$ (minutes) has survival values $S(0)=0.8,\,S(1)=0.5,\,S(2)=0.2,\,S(3)=0.05$. Find $E[X]$ by the survival method.

**C3.4.** 🟡 *(Variance warm-up on the ledger.)* Using the ship's RV $X$ ($E[X]=2.15$, $E[X^2]=6.05$ — both given), find $\Var(X)$ and $\sigma$.

**C3.5.** 🟡 *(Rescale the salvage estimate.)* A surveyor values each intact deck at $\$4$M plus a flat $\$5$M fee: $Y=4X+5$. Given $E[X]=2.15$ and $\Var(X)=1.4275$, find $E[Y]$ and $\Var(Y)$.

**C3.6.** 🔴 *(Step onto a random training pad.)* $X$ is discrete uniform on $\{1,2,\dots,8\}$. Find $E[X]$ and $\Var(X)$.

**C3.7.** 🟡 *(The first-class deck percentile.)* For the ship's RV $X$ (cdf $0.10,0.30,0.60,0.85,1.00$ on $0$–$4$), find the $25^{\text{th}}$ and $75^{\text{th}}$ percentiles.

**C3.26.** 🔴 *(DECISION — two identical-mean machines, pick the steadier.)* Machine A pays $X_A\in\{0,4\}$ each w.p. $0.5$; Machine B pays $X_B\in\{1,3\}$ each w.p. $0.5$. Both have the same mean — find it — then find each variance and say which machine a risk-averse player should choose.

> *Questline beat: the ledger reads clean and your tools are warm. Surge is waiting at the gym. The boss fights begin.*

### Gym Battles (the boss fight — true SOA difficulty)

**C3.8.** 🟡 *(AUDIT — Team Rocket's rigged casino sheet.)* The token machine's winnings $W\in\{0,1,2,3,4\}$ have pmf $0.10,0.15,0.20,0.25,0.30$. Meowth's note declares "the average payout is **4 tokens** — that's the most common result." Find the true $E[W]$ and name Meowth's error.

**C3.9.** 🟡 *(Full center + spread of a salvage RV.)* Salvage value $V\in\{0,10,20,30,40\}$ (in $\$$M) has pmf $0.15,0.25,0.30,0.20,0.10$. Find $E[V]$, $\Var(V)$, and $\sigma$.

**C3.10.** 🟡 *(Mean from a cdf via survival.)* A generator's run-length $X\in\{0,1,2,3,4\}$ has cdf $F=0.10,0.35,0.65,0.90,1.00$. Find $E[X]$ by the Darth-Vader method.

**C3.11.** 🔵 *(MGF — extract the moments.)* A small RV has MGF $M_X(t)=0.2+0.5e^{t}+0.3e^{2t}$. Find $E[X]$ and $\Var(X)$ by differentiating at $t=0$, and identify the pmf.

**C3.12.** 🟡 *(A random gym pad, shifted.)* $X$ is discrete uniform on $\{2,3,\dots,9\}$ (eight consecutive values). Find $E[X]$ and $\Var(X)$.

**C3.13.** 🔵 *(RIVAL TRAP — Gary brags about his Eevee's average.)* Gary's Eevee deals damage $D\in\{1,2,6\}$ with pmf $0.5,0.3,0.2$; your Pokémon deals a steady $D=3$ every turn (a constant). Gary says "my Eevee's *expected* damage is higher, so it's the better attacker — obviously." Find $E[D]$ for the Eevee, compare to your $3$, and say whether Gary's reasoning (mean alone) settles it — bring variance into your answer.

**C3.14.** 🟡 *(LOTUS — a nonlinear payout.)* For the ship's RV $X$ ($p=0.10,0.20,0.30,0.25,0.15$ on $0$–$4$), a bonus pays $g(X)=X^2$ thousand. Find $E[g(X)]=E[X^2]$, and note why it is **not** $(E[X])^2$.

**C3.15.** 🟡 *(Mode, median, mean all at once — and they differ.)* $X\in\{0,1,2,3,4,5\}$ has pmf $0.40,0.25,0.15,0.10,0.06,0.04$. Find the mode, median, and mean, and confirm mode $<$ median $<$ mean.

**C3.16.** 🔵 *(AUDIT — a dropped variance term.)* A trainer's recorded notes give $E[X]=3$ and $E[X^2]=10$ for a damage RV, then state "so $\Var(X)=10$." Find the true variance and name the error.

**C3.17.** 🟡 *(Transform then compare.)* For $N$ = Thunder Shocks with pmf $0.5,0.3,0.2$ on $\{1,2,3\}$ (so $E[N]=1.7$, $\Var(N)=0.61$ — both given), let total energy $Y=2N+5$. Find $E[Y]$ and $\Var(Y)$.

**C3.18.** 🔵 *(MGF sanity + mean.)* An RV has $M_X(t)=e^{2(e^t-1)}$ (a Poisson, previewed). You are told $M_X'(0)=2$. Without expanding the whole thing, state $E[X]$ and confirm $M_X(0)=1$.

**C3.24.** 🟡 *(AUDIT — Team Rocket drops a survival term.)* An escape time $X\in\{0,1,2,3\}$ has survival $S(0)=0.8,\,S(1)=0.5,\,S(2)=0.2,\,S(3)=0$. Jessie sums "$S(1)+S(2)+S(3)=0.7$" and calls that the expected time. Find the true $E[X]$ and name Jessie's error.

> *Questline beat: the Thunder Badge is yours. The post-game below is optional — the integrative challenges where the league players sharpen up.*

### Elite Challenge (post-game — integrative / stretch)

**C3.19.** 🔵 *(Survival + transform together.)* A non-negative integer RV $X$ has survival $S(0)=0.7,\,S(1)=0.4,\,S(2)=0.2,\,S(3)=0.05,\,S(4)=0$. (a) Find $E[X]$. (b) If $Y=10X$, find $E[Y]$. (c) Given additionally $E[X^2]=3.05$, find $\Var(Y)$.

**C3.20.** 🔵 *(Discrete uniform, derived from scratch.)* For $X$ discrete uniform on $\{1,\dots,n\}$, derive $E[X]=\frac{n+1}{2}$ and $\Var(X)=\frac{n^2-1}{12}$ using $\sum k=\frac{n(n+1)}{2}$ and $\sum k^2=\frac{n(n+1)(2n+1)}{6}$. Then evaluate at $n=6$ (a fair die).

**C3.21.** 🔵 *(DECISION — magnitude vs. reliability, the format decides.)* Recall the Gym Battle: Raichu $R\in\{0,2,4,6\}$ ($p=0.10,0.20,0.30,0.40$) and Pikachu $P\in\{2,3,4,5\}$ ($p=0.20,0.30,0.30,0.20$). Given $E[R]=4.0,\Var(R)=4.0$ and $E[P]=3.5,\Var(P)=1.05$ (all restated), decide: (a) in a must-not-whiff battle (a single $0$ loses), which do you send? (b) In a "highest single hit wins" format, which gives the better shot at a $6$? Justify each with the right summary.

**C3.23.** 🔵 *(RIVAL TRAP — Gary forgets to square the scale.)* A damage stat $X$ has $\Var(X)=5$. Gary triples it for a power-up, $Y=3X$, and says "the variance just triples too, so $\Var(Y)=15$." Find the true $\Var(Y)$ and name Gary's error.
:::

## Answers

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

### Quick-Answer Table

| # | Answer | Archetype | | # | Answer | Archetype |
|---|---|---|---|---|---|---|
| C3.1 | mode $0$, median $0$ | standard | | C3.12 | $5.5;\ 5.25$ | standard |
| C3.2 | $1.7$ | standard | | C3.13 | Eevee $E[D]=2.3<3$; Gary wrong | rival_trap |
| C3.3 | $1.55$ | standard | | C3.14 | $6.05\ne 4.6225$ | standard |
| C3.4 | $1.4275;\ \sigma\approx1.195$ | standard | | C3.15 | mode $0$, median $1$, mean $1.29$ | standard |
| C3.5 | $E=13.6,\ \Var=22.84$ | standard | | C3.16 | $\Var=1$ (not $10$) | audit |
| C3.6 | $4.5;\ 5.25$ | standard | | C3.17 | $E=8.4,\ \Var=2.44$ | standard |
| C3.7 | $\pi_{0.25}=1,\ \pi_{0.75}=3$ | standard | | C3.18 | $E[X]=2,\ M_X(0)=1$ | standard |
| C3.8 | $E[W]=2.5$ (not $4$) | audit | | C3.19 | $1.35;\ 13.5;\ 122.75$ | standard |
| C3.9 | $E=18.5,\ \Var=142.75,\ \sigma\approx11.95$ | standard | | C3.20 | $\tfrac{n+1}2,\tfrac{n^2-1}{12}$; $3.5,\ \tfrac{35}{12}$ | standard |
| C3.10 | $2.0$ | standard | | C3.21 | (a) Pikachu; (b) Raichu | decision |
| C3.23 | $\Var(Y)=45$ (Gary forgot the square) | rival_trap | | | | |
| C3.24 | $E[X]=1.5$ (Jessie dropped $S(0)$) | audit | | | | |
| C3.11 | $E=1.1,\ \Var=0.49$; $p=.2,.5,.3$ | standard | | C3.26 | mean $2$; $\Var_A=4>\Var_B=1$; pick B | decision |

**C3.1** — *(standard) Mode = peak, median = cdf cut-line (Entries №08, №09).* Largest mass is $p(0)=0.50\Rightarrow$ **mode $=0$.** cdf $=0.50,0.80,0.95,1.00$; first $\ge0.5$ is $F(0)=0.50\Rightarrow$ **median $=0$.**

**C3.2** — *(standard) Expected value (Entry №10).* $E[N]=1(0.5)+2(0.3)+3(0.2)=0.5+0.6+0.6=1.7.$

**C3.3** — *(standard) Survival-function method (Entry №12).* $E[X]=S(0)+S(1)+S(2)+S(3)=0.8+0.5+0.2+0.05=1.55.$

**C3.4** — *(standard) Variance computational formula (Entry №14).* $\Var(X)=E[X^2]-(E[X])^2=6.05-2.15^2=6.05-4.6225=1.4275$; $\sigma=\sqrt{1.4275}\approx1.195.$

**C3.5** — *(standard) Linear transform (Entry №14).* $E[Y]=4E[X]+5=4(2.15)+5=13.6$; $\Var(Y)=4^2\Var(X)=16(1.4275)=22.84.$ (The $+5$ adds no variance.)

**C3.6** — *(standard) Discrete uniform (Entry №15).* $n=8$: $E[X]=\frac{n+1}{2}=4.5$; $\Var(X)=\frac{n^2-1}{12}=\frac{63}{12}=5.25.$

**C3.7** — *(standard) Percentiles from the cdf (Entry №09).* cdf $=0.10,0.30,0.60,0.85,1.00$. First $\ge0.25$ is $F(1)=0.30\Rightarrow \pi_{0.25}=1$. First $\ge0.75$ is $F(3)=0.85\Rightarrow \pi_{0.75}=3.$

**C3.8** — *(audit) Mode-as-mean error (Entries №08, №10).* True mean: $E[W]=0(0.10)+1(0.15)+2(0.20)+3(0.25)+4(0.30)=0+0.15+0.40+0.75+1.20=2.5.$ **Meowth's error:** he reported the **mode** ($4$, the largest mass) as the **mean.** The mean is the probability-weighted average $2.5$, dragged down by the low/zero payouts — not the tallest bar.

**C3.9** — *(standard) Full center + spread (Entries №10, №14).* $E[V]=0(0.15)+10(0.25)+20(0.30)+30(0.20)+40(0.10)=0+2.5+6.0+6.0+4.0=18.5.$ $E[V^2]=0+100(0.25)+400(0.30)+900(0.20)+1600(0.10)=25+120+180+160=485.$ $\Var(V)=485-18.5^2=485-342.25=142.75$; $\sigma\approx11.95.$

**C3.10** — *(standard) Darth-Vader from a cdf (Entry №12).* $S(k)=1-F(k)=0.90,0.65,0.35,0.10,0$. $E[X]=0.90+0.65+0.35+0.10=2.0.$

**C3.11** — *(standard) MGF differentiation (Entry №15).* $M_X(t)=0.2+0.5e^t+0.3e^{2t}$, so the pmf reads off the coefficients: $p(0)=0.2,\ p(1)=0.5,\ p(2)=0.3.$ $M_X'(t)=0.5e^t+0.6e^{2t}\Rightarrow E[X]=M_X'(0)=0.5+0.6=1.1.$ $M_X''(t)=0.5e^t+1.2e^{2t}\Rightarrow E[X^2]=M_X''(0)=0.5+1.2=1.7.$ $\Var(X)=1.7-1.1^2=1.7-1.21=0.49.$ (Check directly: $\sum k p(k)=0.5+0.6=1.1$ ✓.)

**C3.12** — *(standard) Shifted discrete uniform (Entry №15).* Eight consecutive values $\{2,\dots,9\}$: mean is the midpoint $\frac{2+9}{2}=5.5$; variance depends only on the count $m=8$, $\Var=\frac{m^2-1}{12}=\frac{63}{12}=5.25.$ (A shift moves the mean, not the variance — Entry №14.)

**C3.13** — *(rival_trap) Mean alone doesn't settle a decision (Entries №10, №13).* Eevee: $E[D]=1(0.5)+2(0.3)+6(0.2)=0.5+0.6+1.2=2.3.$ Your steady $3$ has $E=3$ and $\Var=0$. **Gary is wrong twice:** (1) factually, the Eevee's mean $2.3$ is *below* your $3$, so it isn't even the higher average; (2) methodologically, "higher mean $\Rightarrow$ better" ignores spread — your constant $3$ has *zero* variance (perfectly reliable), while the Eevee swings from $1$ to $6$ ($\Var=3.61$). On both counts the steady attacker wins.

**C3.14** — *(standard) LOTUS, nonlinear $g$ (Entry №11).* $E[X^2]=\sum k^2 p(k)=0+1(0.20)+4(0.30)+9(0.25)+16(0.15)=0.20+1.20+2.25+2.40=6.05.$ This is **not** $(E[X])^2=2.15^2=4.6225$ — you must average the squares, not square the average. (Their gap, $1.4275$, is exactly the variance.)

**C3.15** — *(standard) Three centers disagree (Entries №08, №09, №10).* Mode $=0$ (mass $0.40$, the peak). cdf $=0.40,0.65,0.80,0.90,0.96,1.00$; first $\ge0.5$ is $F(1)=0.65\Rightarrow$ median $=1$. Mean $=0(0.40)+1(0.25)+2(0.15)+3(0.10)+4(0.06)+5(0.04)=0+0.25+0.30+0.30+0.24+0.20=1.29.$ So mode $0<$ median $1<$ mean $1.29$ — right-skew. ✓

**C3.16** — *(audit) Dropped $(E[X])^2$ term (Entry №14).* $\Var(X)=E[X^2]-(E[X])^2=10-3^2=10-9=1.$ The note reported the **raw second moment** $E[X^2]=10$ as the variance — forgetting to subtract $(E[X])^2$. True $\Var=1$.

**C3.17** — *(standard) Linear transform of a known mean/variance (Entry №14).* $E[Y]=2E[N]+5=2(1.7)+5=8.4$; $\Var(Y)=2^2\Var(N)=4(0.61)=2.44.$ (The $+5$ contributes no variance.)

**C3.18** — *(standard) MGF mean + sanity check (Entry №15).* $E[X]=M_X'(0)=2$ (given). Every MGF satisfies $M_X(0)=E[e^0]=1$; here $M_X(0)=e^{2(e^0-1)}=e^{2(1-1)}=e^0=1$ ✓.

**C3.24** — *(audit) Off-by-one in the survival method (Entry №12).* The survival sum starts at $k=0$: $E[X]=S(0)+S(1)+S(2)+S(3)=0.8+0.5+0.2+0=1.5$. **Jessie's error:** she dropped the $S(0)$ term, summing only from $k=1$ to get $0.7$. Always start the survival sum at $k=0$.

**C3.19** — *(standard) Survival + transform together (Entries №12, №14).* (a) $E[X]=S(0)+S(1)+S(2)+S(3)=0.7+0.4+0.2+0.05=1.35.$ (b) $E[Y]=10E[X]=13.5.$ (c) $\Var(X)=E[X^2]-(E[X])^2=3.05-1.35^2=3.05-1.8225=1.2275$; $\Var(Y)=10^2\Var(X)=100(1.2275)=122.75.$

**C3.20** — *(standard) Discrete-uniform derivation (Entry №15).* $E[X]=\frac1n\sum_{k=1}^n k=\frac1n\cdot\frac{n(n+1)}{2}=\frac{n+1}{2}.$ $E[X^2]=\frac1n\sum_{k=1}^n k^2=\frac1n\cdot\frac{n(n+1)(2n+1)}{6}=\frac{(n+1)(2n+1)}{6}.$ Then $\Var(X)=\frac{(n+1)(2n+1)}{6}-\frac{(n+1)^2}{4}=\frac{(n+1)\big[2(2n+1)-3(n+1)\big]}{12}=\frac{(n+1)(n-1)}{12}=\frac{n^2-1}{12}.$ At $n=6$: $E[X]=\frac{7}{2}=3.5$, $\Var(X)=\frac{35}{12}\approx2.917.$

**C3.21** — *(decision) Magnitude vs. reliability, format-dependent (Entries №13, №14).* (a) **Must-not-whiff:** send **Pikachu.** Raichu deals $0$ with probability $0.10$ (an instant loss) and has four times the variance ($4.0$ vs. $1.05$); Pikachu never drops below $2$. Low variance / high floor wins when a single zero is fatal. (b) **Highest single hit:** send **Raichu** — only Raichu can reach $6$ (probability $0.40$), while Pikachu caps at $5$. The heavy upper tail that *hurts* reliability *helps* a max-hit format. The right summary depends on what the stakes reward: floor (variance) vs. ceiling (upper tail).

**C3.26** — *(decision) Equal means, choose by variance (Entries №10, №14).* Both means: $E[X_A]=\frac{0+4}{2}=2$ and $E[X_B]=\frac{1+3}{2}=2$ — identical. Variances: $\Var(X_A)=E[X_A^2]-4=\frac{0+16}{2}-4=8-4=4$; $\Var(X_B)=\frac{1+9}{2}-4=5-4=1$. A **risk-averse player chooses Machine B** — same expected payout, one-quarter the variance (steadier). Same mean, different risk — exactly the magnitude-vs-reliability theme.

**C3.23** — *(rival_trap) Forgetting to square the scale (Entry №14).* $\Var(3X)=3^2\Var(X)=9(5)=45$, not $15$. **Gary's error:** a scale factor $a$ multiplies the variance by $a^2$, not by $a$ — he tripled when he should have multiplied by nine.
:::

## Badge Earned — the Thunder Badge

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/thunder_badge.png" alt="The Thunder Badge, a yellow eight-pointed star gym badge" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Thunder Badge earned!</strong> Rank: Rookie Trainer · 2 badges.</figcaption>
</figure>

You convinced Lt. Surge that a battle is *two* numbers — magnitude and reliability — not one, and he pressed the **Thunder Badge** into your hand. **Rank: Rookie Trainer · 2 badges** (Cascade + Thunder). Two down, six to go on the road to the Indigo Plateau.

**Mastery checklist — tick each before you move on (mapped 1-to-1 to the SOA outcomes):**

- ☐ **(2a)** I can describe a discrete RV with its **pmf, cdf, and survival function**, convert among them ($S=1-F$), and answer any $=,<,\le,>,\ge,$ between question while watching the endpoint. *(Rematch: Concept 0, WE 3, Problems C3.3, C3.7, C3.10.)*
- ☐ **(2a/2c)** I can locate the **mode, median/percentiles, and mean**, and explain when (and why) the three disagree. *(Rematch: Concepts 1–3, WE 1, Problems C3.1, C3.8, C3.15.)*
- ☐ **(2c)** I can compute $E[X]$, $E[g(X)]$ (LOTUS), and $E[aX+b]$ (linearity), **including the survival-function (Darth-Vader) method** $E[X]=\sum_{k\ge0}S(k)$. *(Rematch: Concepts 3–5, WE 2–3, Problems C3.2, C3.5, C3.14.)*
- ☐ **(2c)** I can compute **variance** by definition and by $E[X^2]-(E[X])^2$, take the SD, and apply $\Var(aX+b)=a^2\Var(X)$ — never dropping the squared-mean term or forgetting to square the scale. *(Rematch: Concepts 6–7, WE 1, Problems C3.4, C3.9, C3.16, C3.17.)*
- ☐ **(2c/2d)** I can extract moments from the **MGF** ($E[X^r]=M_X^{(r)}(0)$) and quote the **discrete uniform** mean $\frac{n+1}{2}$ and variance $\frac{n^2-1}{12}$. *(Rematch: Concept 8, WE 4, Problems C3.6, C3.11, C3.12, C3.18, C3.20.)*
- ☐ **Flagship calculator:** I can drive **1-Var Stats** (L1 values, L2 probabilities, FRQ:L2) to read $\bar x=E[X]$ and $\sigma x$ (so $\Var=\sigma x^2$), and I always use $\sigma x$, never $sx$. *(Rematch: WE 1 Trainer's Path, the Gym Battle.)*

**Gym Rematch pointers.** Reported a mode as a mean? Concept 1 Beat 4 and the Team Rocket Trap, then C3.8. Dropped the $(E[X])^2$ term? Concept 7 Beat 4, then C3.16. Forgot to square the scale on a transform? Concept 7 Beat 6, then C3.5, C3.17. Summed the cdf instead of the survival? Concept 5 Beat 4, then C3.3, C3.10.

> Next stop: **Viridian Forest and Pewter City**, where the wild things are too many to list and you'll learn to **count by rule** — permutations, combinations, and the binomial — on the way to Brock's Boulder Badge. Pack your moment tools; every distribution you meet there comes with a mean and a variance.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
