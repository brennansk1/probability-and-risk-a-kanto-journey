<!--
  file: ch03_discrete_moments
  tier: A
  outcomes: 2a,2c,2d
  tia: A.3
  locale: S.S. Anne -> Vermilion
  type: electric
  maps_to: The S.S. Anne (docking at Vermilion), Lt. Surge -- power=mean, reliability=variance; Thunder Badge
-->

# Power and Reliability {.type-electric}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with the sea route from Cerulean down to Vermilion City highlighted; Vermilion, home of the Thunder Badge and the docked S.S. Anne, is marked as the current destination." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 10 — you have left Cerulean, crossed to the coast, and boarded the <strong>S.S. Anne</strong> at Vermilion harbor: home of the Thunder Badge and the city where raw power meets reliability.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Ship That Could Only Be Described by Its Distribution"**

You step off the gangway onto the **S.S. Anne** and the noise hits you like a wave — a luxury cruise so packed with trainers that you couldn't count them if you tried. The captain, harried, grabs your sleeve. "You're the one with the Actuary Pokédex? Good. I have a problem no head-count can solve."

He waves at the throng. "I can't tell you *who* is aboard. But I can tell you the **shape** of the crowd. In any given cabin, the number of Pokémon a trainer is carrying is **1, 2, 3, 4, or 5** — and from years of ticket data I know exactly how often each happens." He hands you a slip:

| Pokémon carried, $k$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Share of trainers | $0.20$ | $0.25$ | $0.30$ | $0.15$ | $0.10$ |

"The galley needs to provision. I need the **average** party size to order food, and I need to know how *wildly it swings* cabin to cabin so I don't run short. One number for the center, one number for the spread."

Before you can answer, the floor lurches. Klaxons. **Team Rocket** has scuttled the hull — the S.S. Anne is taking on water and will go down. A new clipboard is thrust at you: the **time until each deck floods**, measured in minutes, deck by deck. The captain, white-faced: "How long does this ship *survive*? On average — how many minutes before she's under?"

Pikachu's cheeks crackle. You realize you have never actually *defined* the thing the captain keeps asking for. Back in Cerulean you combined the probabilities of *events*. But the unknown here isn't an event — it's a **number whose value is left to chance**: the party size in a random cabin, the minutes until a deck goes under. What is its *average*? How far does it *swing*? And could you really read the ship's expected survival time straight off a "still-afloat" curve — without ever writing down a probability for each individual minute?

*You don't yet know how. How do you boil a whole random quantity down to a number for its center and a number for its spread?*
:::

## Where You Are — 60-Second Retrieval

**Rank: Rookie · Badges: 1 (Cascade).** You earned the **Cascade Badge** in Cerulean by learning to *reason from evidence* — conditioning, the multiplication rule, the law of total probability, and Bayes. The load-bearing idea you carry onto the ship: a **probability** is a number in $[0,1]$, and a set of disjoint outcomes that covers everything must have probabilities that **sum to one**. You also met the **complement** $P(A^c) = 1 - P(A)$ and the **summation sign** $\sum$ ("add these up") inside the law of total probability.

Those two facts — *probabilities sum to one*, and $\sum$ *just means add* — are the entire foundation of this chapter. A **distribution** is nothing but a complete list of disjoint outcomes with probabilities that sum to one, and every quantity we compute (mean, variance, MGF) is a **weighted sum** over that list. Take sixty seconds and prove you still own these before reading on.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the last chapter**

Answer from memory; if any feels shaky, flip back before continuing.

1. A spinner lands on A, B, or C with $P(A)=0.5$, $P(B)=0.3$. What must $P(C)$ be, and why? *(Answer: $0.2$ — the three disjoint outcomes must sum to $1$.)*
2. If $P(\text{rain}) = 0.3$, what is $P(\text{no rain})$? *(Answer: $1 - 0.3 = 0.7$, the complement.)*
3. Read aloud and evaluate: $\sum_{k=1}^{3} k$. *(Answer: "the sum over $k$ from 1 to 3 of $k$" $= 1+2+3 = 6$.)*

All three instant? You're ready. Any hesitation? The retrieval *is* the lesson — go reclaim it, then come back.
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice crackles through the Actuary Pokédex as the deck tilts beneath you.

"The captain has handed you a **random variable**, Ash — a number whose value depends on chance. This is the gateway to the whole second topic of the exam, and it is *enormous*: random variables and their summaries are nearly half of Exam P. Everything here — the average, the swing, the moment generating function, even the survival time of this sinking ship — is built from one humble idea you already own: *probabilities sum to one*. Lt. Surge, the Vermilion gym leader, judges every trainer on exactly two numbers: **raw power** and **reliability**. Power is the *mean*. Reliability is the *variance*. Master those two, plus the machinery that produces them, and the Thunder Badge is yours. Take it slowly; this is the spine of Topic 2."

By the end of this chapter you will be able to:

- **Recognize and validate a discrete random variable** — read and build its probability mass function (pmf), cumulative distribution function (cdf), and **survival function**, and check that a candidate distribution is valid. *(Outcome 2a.)*
- **Locate the center** — compute the **expected value** $\E[X]$ of a pmf and of $g(X)$, and find the **mode, median, and percentiles** (knowing the mean is none of these). *(Outcome 2a, plus standard descriptive measures.)*
- **Read the mean off a survival curve** — deploy the survival-function ("Darth Vader") method $\E[X] = \sum_{k\ge 0} S(k)$ for a nonnegative integer $X$. *(Outcome 2a/2c.)*
- **Measure the spread** — compute **variance, standard deviation, and the coefficient of variation**, use the "mean of the square minus square of the mean" shortcut, and rescale spread under $aX+b$ with $\Var(aX+b)=a^2\Var(X)$. *(Outcome 2c.)*
- **Generate every moment at once** — define and use the **moment generating function** $M_X(t)=\E[e^{tX}]$ to extract moments and identify distributions. *(Outcome 2d.)*
- **Apply the discrete uniform distribution** — the "equally likely" model, its mean $(n+1)/2$ and variance $(n^2-1)/12$. *(Outcome 2a.)*

> *Exam-weight signpost.* Univariate random variables are **44–50% of Exam P** — the single largest topic — and the mean/variance of a pmf is its most-tested skill. This is a **Tier A** chapter: it earns the full treatment, and every named distribution in the rest of Act I and all of Act II is just this machinery with a specific pmf plugged in.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own the S.S. Anne?**

Already fluent? Prove it. Work these five, ~3 minutes each, *with correct method*:

1. $X$ takes values $0,1,2$ with $P(0)=0.5$, $P(1)=0.3$, $P(2)=0.2$. Find $\E[X]$ and $\Var(X)$.
2. For that same $X$, write the cdf $F(1)$ and the survival value $S(1)=P(X>1)$.
3. A nonnegative integer $N$ has $P(N>0)=0.6$, $P(N>1)=0.35$, $P(N>2)=0.15$, $P(N>3)=0$. Find $\E[N]$ **without** a value-times-probability sum.
4. $\Var(X)=4$. Find $\Var(3X-7)$ and $\SD(3X-7)$.
5. $M_X(t) = 0.4 + 0.6e^t$. Find $\E[X]$.

*(Answers: $\E[X]=0.7$, $\Var(X)=0.61$; $F(1)=0.8$, $S(1)=0.2$; $\E[N]=1.10$; $\Var=36$, $\SD=6$; $\E[X]=0.6$.)* Five for five with the right reasoning? **Skip to the Gym Challenge** and claim the badge. Any miss or hesitation? The teaching below was built exactly for you — read on. Each concept has its own skip-gate too, so even a partial owner loses no time.
:::

---

Eight ideas build on one another here, in increasing difficulty. We teach them **in order**, each with its own "do you already own this?" skip-check, then the full nine-beat lesson, then a Pokédex Entry you can carry into the exam:

1. **The discrete random variable and its pmf** — a number left to chance, and its probability list *(the foundation)*
2. **The cdf and the survival function** — "at most $x$" and "more than $x$"
3. **Mode, median, and percentiles** — the typical, the middle, and the cut-points
4. **Expected value** — the long-run average, and the tools that compute it
5. **The survival-function (Darth Vader) method** — the mean read straight off the survival curve
6. **Variance, SD, and CV** — measuring the swing, and $\Var(aX+b)$
7. **The moment generating function** — one function that dispenses every moment
8. **The discrete uniform distribution** — the "equally likely" model

## Concept 1 — The Discrete Random Variable and Its pmf

::: concept-gate
**DO YOU ALREADY OWN THIS? — pmf**

A "distribution" for $X\in\{1,2,3\}$ is proposed: $P(1)=0.5$, $P(2)=0.3$, $P(3)=0.3$. Is it a valid pmf? And for the valid version where the last is $0.2$, what is $P(X\le 2)$?

If you instantly answered **"not valid — the three add to $1.1 > 1$"** and **$P(X\le 2)=0.8$**, you own this — **skip to Concept 2**. If you didn't check the sum, or weren't sure how to combine $P(1)$ and $P(2)$, this section is for you.
:::

**Beat 1 — The one-sentence idea.** *A discrete random variable is a number whose value is decided by chance, and its probability mass function (pmf) is just the complete list of values it can take, each tagged with the probability it lands there.*

**Beat 2 — Anchor + concrete instance.** Back on the captain's slip is exactly this object. Let $X$ = "the number of Pokémon a randomly chosen trainer is carrying." Before you pick a trainer, $X$ has no fixed value — it's $1$, $2$, $3$, $4$, or $5$, each with a known chance:

| $k$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $p(k) = P(X=k)$ | $0.20$ | $0.25$ | $0.30$ | $0.15$ | $0.10$ |

This table *is* the pmf of $X$. It answers every "what's the chance $X$ equals this exact value?" question at a glance.

**Beat 3 — Reason through it in plain words.** Two things make this a legitimate description of chance, and they're the same two from the retrieval. First, **no probability can be negative** — there's no such thing as a $-0.1$ chance. Second, because the five values are *disjoint* (a trainer carries exactly one count) and *exhaustive* (every trainer carries one of these counts), their probabilities must **cover all of the certainty there is** — they sum to exactly $1$:

$$0.20 + 0.25 + 0.30 + 0.15 + 0.10 = 1.00. \checkmark$$

If they summed to less than $1$, some outcome would be missing; more than $1$, and you'd be double-counting certainty. A pmf is *valid* exactly when both checks pass.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is to accept any table of "probabilities" without checking the sum. Consider the proposed pmf

$$p(1)=0.5,\quad p(2)=0.3,\quad p(3)=0.3. \qquad\textbf{(invalid)}$$

Each entry is individually in $[0,1]$, so it *looks* fine — but $0.5+0.3+0.3 = 1.1 > 1$. That extra $0.1$ of "certainty" has nowhere to live; the table is not a distribution at all. **A pmf is not just nonnegative numbers — it is nonnegative numbers that sum to one.** The matching trap on the low side: a table summing to $0.9$ is *also* invalid (it's missing $0.1$ of probability). Always run the sum.

**Beat 5 — Translate into notation, one glyph at a time.** We write the pmf as a function of the value $k$:

$$p(k) = P(X = k) \qquad \text{read aloud: ``}p\text{ of }k\text{ is the probability that }X\text{ equals }k\text{.''}$$

The capital $X$ is the **random variable** (the quantity before it's observed); a lowercase $k$ (or $x$) is a **particular value** it might take. The two validity conditions, in symbols:

$$p(k) \ge 0 \text{ for every } k, \qquad \sum_{k} p(k) = 1.$$

The $\sum_k$ reads **"add up $p(k)$ over every value $k$ in the support."** The **support** is just the set of values with positive probability — here $\{1,2,3,4,5\}$.

**Beat 6 — Generalize: derive the "find the missing probability" move.** Because the entries must sum to $1$, *any one* of them can be recovered from the rest — this is the most common pmf manipulation on the exam. Suppose a pmf is given as

$$p(k) = c\,k \quad \text{for } k = 1,2,3,4,$$

with an unknown constant $c$. Don't guess $c$ — *force the sum to one*. The total is $c(1+2+3+4) = 10c$, and setting $10c = 1$ gives $c = \tfrac{1}{10}$. The normalization condition isn't a rule to memorize; it's the equation that *pins down* any free constant in a pmf.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* read $P(X=3)=0.30$ straight off the table.
- *Twist (combine values):* "carries **at most** $2$" is $P(X\le 2) = p(1)+p(2) = 0.10 + 0.25 = 0.35$ — disjoint values, so add (Concept 2 formalizes this as the cdf).
- *General (solve for a constant):* the $p(k)=ck$ example above — normalize to find $c$.
- *Edge (a formula pmf):* a pmf can be given as a rule, e.g. $p(k) = (0.5)^k$ for $k=1,2,3,\dots$ The same two checks apply: each term is nonnegative, and $\sum_{k=1}^\infty (0.5)^k = 1$ (a geometric series you'll meet fully in Chapter 5). The support being infinite changes nothing about the validity test.

**Beat 8 — Picture it.** A pmf is naturally a **bar chart**: one bar per value, its height the probability, all heights summing to $1$. (We draw it together with the cdf and survival function in Concept 2's figure, so you can see how the three views of the same distribution relate.)

**Beat 9 — Consolidate.** You can now read a pmf, *validate* it with the two checks (nonnegative, sums to one), recover a missing entry or a free constant by forcing the sum to one, and combine disjoint values by adding their probabilities. Every distribution in this book is a pmf (or its continuous cousin) — this is the object everything else acts on.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Discrete Random Variable & pmf**

A **discrete random variable** $X$ takes values in a countable set (the *support*). Its **probability mass function** is
$$p(k) = P(X = k), \qquad \text{valid iff } p(k)\ge 0 \text{ for all } k \text{ and } \sum_k p(k) = 1.$$

*In plain terms:* the complete list of values with the probability of each. The two validity checks are *nonnegative* and *sums to one* — the second also pins down any unknown constant.

*Recognition cue:* a **table or formula giving $P(X=k)$**, or the words "the number of …" attached to a chance experiment. First move on any pmf: **confirm it sums to one** (or use that to solve for the missing piece).
:::

## Concept 2 — The cdf and the Survival Function

::: concept-gate
**DO YOU ALREADY OWN THIS? — cdf & survival**

For the cabin pmf ($p(1)=0.10,\,p(2)=0.25,\,p(3)=0.30,\,p(4)=0.20,\,p(5)=0.15$), find $F(3)=P(X\le 3)$ and $S(3)=P(X>3)$.

If you answered **$F(3)=0.65$** and **$S(3)=0.35$** (and saw that $F(3)+S(3)=1$), **skip to Concept 3**. If you weren't sure whether $S(3)$ should include $X=3$, read on — the strict-vs-not boundary is the whole game.
:::

**Beat 1 — The one-sentence idea.** *The cdf accumulates probability up to and including a value ("at most $x$"); the survival function is its mirror, the probability of landing strictly above ("more than $x$").*

**Beat 2 — Anchor + concrete instance.** The pmf answers "*equals* $k$." But the captain — and the exam — usually ask "*at most* $k$" or "*more than* $k$." Take the cabin distribution. "A trainer carries **at most 3** Pokémon" pools the disjoint values $1, 2, 3$:

$$P(X \le 3) = p(1) + p(2) + p(3) = 0.10 + 0.25 + 0.30 = 0.65.$$

"A trainer carries **more than 3**" pools the rest:

$$P(X > 3) = p(4) + p(5) = 0.20 + 0.15 = 0.35.$$

**Beat 3 — Reason through it in plain words.** These two questions partition the whole crowd: every trainer carries *either* at most $3$ *or* more than $3$, never both, never neither. So the two probabilities must add to all the certainty there is:

$$0.65 + 0.35 = 1.$$

That means the "more than" probability is just $1$ minus the "at most" probability — the **complement** from Cerulean, wearing new clothes. Knowing the cdf, you get the survival function for free, and vice versa.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The single most punished slip here is the **boundary**: is $X=3$ counted in "$P(X>3)$" or not? It is **not**.

$$P(X > 3) = p(4)+p(5) = 0.35, \qquad\text{but}\qquad P(X \ge 3) = p(3)+p(4)+p(5) = 0.65. \quad\textbf{(different!)}$$

The strict inequality "$>$" *excludes* the endpoint; "$\ge$" *includes* it. For a discrete variable these genuinely differ by the lump $p(3)=0.30$. Likewise $P(X<3) = 0.35$ but $P(X\le 3)=0.65$. **Always pin down whether the endpoint is in or out** — read the words "at most / fewer than / more than / at least" carefully, and remember $S$ is defined with a *strict* "$>$."

**Beat 5 — Translate into notation, one glyph at a time.** The **cumulative distribution function** (cdf):

$$F(x) = P(X \le x) \qquad \text{read aloud: ``}F\text{ of }x\text{ is the probability }X\text{ is at most }x\text{.''}$$

The **survival function** $S$ — "the probability you *survive past* $x$," the chance the random value is still above $x$:

$$S(x) = P(X > x) = 1 - F(x) \qquad \text{read aloud: ``the probability }X\text{ exceeds }x\text{.''}$$

The name is literal on a sinking ship: if $X$ is the minute the ship goes under, then $S(x) = P(X>x)$ is **the probability the ship is still afloat after $x$ minutes** — it *survives past* time $x$. The cdf $F$ is built from the pmf by accumulating:

$$F(x) = \sum_{k \le x} p(k) \qquad \text{(add every mass at or below } x\text{).}$$

**Beat 6 — Generalize: derive the staircase shape of a discrete cdf.** Build $F$ for the cabin distribution by accumulating left to right:

$$F(1)=0.10,\quad F(2)=0.35,\quad F(3)=0.65,\quad F(4)=0.85,\quad F(5)=1.00.$$

Between integers nothing accumulates, so $F$ is **flat**, then it **jumps** by exactly $p(k)$ at each value $k$. For instance $F$ jumps from $0.35$ to $0.65$ at $k=3$ — a jump of $0.30 = p(3)$. This gives the universal facts about *any* cdf, which we *derive* rather than assert: $F$ is **non-decreasing** (you only ever add nonnegative mass), it starts at $0$ (below the smallest value, nothing has accumulated) and ends at $1$ (above the largest, everything has), and for a discrete variable it is a **right-continuous staircase** whose jump at $k$ recovers the pmf, $p(k) = F(k) - F(k^-)$.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* read $F(3)=0.65$ by accumulating, $S(3)=1-0.65=0.35$.
- *Twist (recover a pmf from a cdf):* given only $F(4)=0.85$ and $F(5)=1.00$, the mass at $5$ is the jump $p(5) = F(5)-F(4) = 0.15$.
- *Twist (a between-values range):* $P(2 < X \le 4) = F(4) - F(2) = 0.85 - 0.35 = 0.50$ — the cdf differences out an interval. Mind the endpoints: this is "$X$ is $3$ or $4$."
- *Edge (boundary discipline):* $P(X \ge 4) = S(3) = 1 - F(3) = 0.35$, **not** $S(4)$. "At least $4$" means "more than $3$." Translating "$\ge a$" into "$> a-1$" for integer $X$ prevents the off-by-one.

**Beat 8 — Picture it: three views of one distribution.** The pmf (bars), the cdf (rising staircase), and the survival function (falling staircase) are three pictures of the *same* random variable. The cdf climbs from $0$ to $1$; the survival curve is its upside-down mirror, falling from $1$ to $0$; at every value they sum to $1$.

<figure>
<img src="../../assets/diagrams/ch03_pmf_cdf_survival.png" alt="Three stacked panels for the cabin distribution over values 1 to 5 with probabilities 0.10, 0.25, 0.30, 0.20, 0.15. Top panel: the pmf as five bars whose heights are the probabilities, summing to 1. Middle panel: the cdf as a rising right-continuous staircase reaching 0.10, 0.35, 0.65, 0.85, 1.00, with each jump labeled as the corresponding pmf mass. Bottom panel: the survival function S(x)=P(X>x) as a falling staircase from 1 down to 0, the mirror image of the cdf; a note shows F(x)+S(x)=1 at every x." style="width:72%; max-width:520px; display:block; margin:1em auto;">
<figcaption>One distribution, three views: the pmf bars sum to $1$; the cdf accumulates them into a rising staircase; the survival function is the falling mirror, $S(x)=1-F(x)$. The jump in $F$ at each value $k$ <em>is</em> the pmf mass $p(k)$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now build the cdf from a pmf by accumulating, get the survival function as $1-F$, recover the pmf as a jump in the cdf, difference out any interval, and — crucially — keep the strict-vs-non-strict boundary straight. The survival function is about to do something remarkable in Concept 5: hand you the mean directly.

::: pokedex-entry
**POKÉDEX ENTRY №02 — cdf and Survival Function**

$$F(x) = P(X\le x) = \sum_{k\le x} p(k), \qquad S(x) = P(X > x) = 1 - F(x).$$

Any cdf is **non-decreasing**, runs from $0$ to $1$, and (discrete) is a right-continuous staircase whose jump at $k$ is $p(k)=F(k)-F(k^-)$.

*In plain terms:* $F$ accumulates "at most $x$"; $S$ is the leftover "more than $x$." They always sum to $1$.

*Recognition cue:* the words **"at most / at least / more than / fewer than," or a survival/reliability question** ("still working after time $x$"). Translate to $F$ or $S$, mind the strict-vs-non-strict endpoint, and use $S=1-F$ to switch between them.
:::

## Concept 3 — Mode, Median, and Percentiles

::: concept-gate
**DO YOU ALREADY OWN THIS? — Mode, Median, Percentiles**

For the cabin pmf ($0.10,0.25,0.30,0.20,0.15$ at $1$–$5$), find the **mode** and the **median**.

If you answered **mode $=3$** (the most likely value) and **median $=3$** (the smallest $k$ with $F(k)\ge 0.5$), **skip to Concept 4**. If you'd have averaged the values, or confused these with the mean, read on.
:::

**Beat 1 — The one-sentence idea.** *The mode is the most likely single value, the median is the middle (half the probability lies at or below it), and a percentile is the cut-point with a given fraction of probability below it — none of these is the mean.*

**Beat 2 — Anchor + concrete instance.** The captain wants "the typical cabin." But "typical" can mean three different things, and on the exam they're three separate questions. Take the cabin distribution.

- The **mode** is the value with the biggest bar: $p(3)=0.30$ is the tallest, so the mode is $\mathbf{3}$ — *the single most common* party size.
- The **median** is the value where the running total $F$ first reaches half. Accumulate: $F(1)=0.10$, $F(2)=0.35$, $F(3)=0.65$. The first time $F(k)\ge 0.5$ is at $k=\mathbf{3}$ — so half the trainers carry $3$ or fewer.

**Beat 3 — Reason through it in plain words.** The **mode** answers "if I had to bet on *one exact* value, which?" — just find the tallest bar. The **median** answers "what value splits the crowd in half?" — walk up the cdf until you cross $0.5$; the first value that does is the median. A **percentile** generalizes the median: the $p$-th percentile is the smallest value whose cumulative probability reaches $p/100$. The median is exactly the $50$th percentile.

**Beat 4 — Surface and dismantle the tempting wrong idea.** *(This is the chapter's signature trap — Team Rocket will fall straight into it.)* The deadly mistake is to report the **mode as if it were the mean**. They are different questions and usually different numbers. The mode is "the most likely value"; the mean (next concept) is the "probability-weighted average," which we'll compute as $2.95$ for this very distribution. The mode is $3$; the mean is $2.95$; the median is $3$. **Three different summaries, three different jobs.** Reporting "most cabins carry $3$, so the average is $3$" overstates the average here — and on a skewed distribution the gap can be enormous. Insurers price the *mean* claim, not the *typical* claim, precisely because these diverge. Never substitute one for another.

**Beat 5 — Translate into notation, one glyph at a time.** The **mode** is the maximizer of the pmf:

$$\text{mode} = \arg\max_k\, p(k) \qquad \text{read aloud: ``the value }k\text{ that makes }p(k)\text{ largest.''}$$

The **median** $m$ (discrete convention) is the smallest value with at least half the probability at or below it:

$$m = \min\{\,k : F(k) \ge 0.5\,\} \qquad \text{read aloud: ``the smallest }k\text{ whose cdf reaches one-half.''}$$

The **$100p$-th percentile** $\pi_p$ replaces $0.5$ with $p$:

$$\pi_p = \min\{\,k : F(k) \ge p\,\}.$$

**Beat 6 — Generalize: derive the median rule, and the edge case it hides.** Why "smallest $k$ with $F(k)\ge 0.5$"? The median should split mass so that *at least half* lies at or below it and *at least half* at or above it. Walking up the staircase $F$, the first rung that reaches $0.5$ is the first value for which "at most $k$" already accounts for half the crowd — that's the split point. The hidden edge case: if $F(k) = 0.5$ *exactly* at some value (the cdf lands *on* the line), the median is conventionally taken as that $k$ (any value between it and the next is technically a valid median; the exam uses the smallest). For our distribution $F$ jumps past $0.5$ at $k=3$ (from $0.35$ to $0.65$), so the median is unambiguously $3$.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* mode $=3$ (tallest bar); median $=3$ (first $F\ge 0.5$).
- *Twist (the 90th percentile):* $\pi_{0.90} = \min\{k: F(k)\ge 0.90\}$. With $F(4)=0.85$ and $F(5)=1.00$, the first to reach $0.90$ is $k=5$ — the 90th percentile is $5$.
- *Twist (multi-modal):* if two values tie for the tallest bar, the distribution has **two modes** (bimodal) — both are reported. The mode need not be unique.
- *Edge (cdf lands on the line):* if $F(2)=0.50$ exactly, the median is $2$ by the "smallest $k$" convention; be ready for the rare exam item that puts the cdf right on $0.5$.

**Beat 8 — Picture it.** On the pmf bar chart, the **mode** is the tallest bar; on the cdf staircase, the **median** is where the rising stair first crosses the $0.5$ line and a **percentile** is where it first crosses its target height. The **mean** (dashed) sits at the balance point of the bars — often *between* the integer values, which is exactly why it usually differs from the mode and median.

<figure>
<img src="../../assets/diagrams/ch03_mean_median_mode.png" alt="The cabin pmf drawn as five bars at values 1 to 5 with heights 0.10, 0.25, 0.30, 0.20, 0.15. The tallest bar at 3 is labeled MODE = 3. A solid vertical line at 3 is labeled MEDIAN = 3 (first cdf value reaching one-half). A dashed vertical line at 2.95 is labeled MEAN = 2.95 and sits slightly left of 3 at the balance point of the bars. A small caption stresses that the three summaries answer three different questions and need not coincide." style="width:74%; max-width:540px; display:block; margin:1em auto;">
<figcaption>Three summaries of one distribution. Mode (tallest bar) $=3$; median (cdf first crosses $0.5$) $=3$; mean (balance point) $=2.95$. They answer different questions and need not coincide — reporting the mode as the mean is the chapter's classic error.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now find the mode (tallest bar), the median (first $F\ge 0.5$), and any percentile (first $F\ge p$), and you will never again report one of these as if it were the mean. Next we compute the mean itself.

::: pokedex-entry
**POKÉDEX ENTRY №03 — Mode, Median, Percentiles**

$$\text{mode} = \arg\max_k p(k), \quad \text{median} = \min\{k: F(k)\ge 0.5\}, \quad \pi_p = \min\{k: F(k)\ge p\}.$$

*In plain terms:* mode $=$ most likely value (tallest bar); median $=$ middle (first cdf rung at half); percentile $=$ cut-point (first cdf rung at $p$). The **mean is none of these** — it's the weighted average (next concept).

*Recognition cue:* "most likely / typical value" $\to$ **mode**; "the middle / 50th percentile" $\to$ **median**; "the value below which $p\%$ fall" $\to$ **percentile**. Build the cdf and read off the cut-point.
:::

## Concept 4 — Expected Value: the Long-Run Average

::: concept-gate
**DO YOU ALREADY OWN THIS? — Expected Value**

A trainer carries $X$ Pokémon with $p(1)=0.10,\,p(2)=0.25,\,p(3)=0.30,\,p(4)=0.20,\,p(5)=0.15$. Find $\E[X]$, and find $\E[X^2]$.

If you got **$\E[X]=2.95$** and **$\E[X^2]=9.85$** (each a probability-weighted sum), **skip to Concept 5**. If you averaged $1$ through $5$ to get $3$, or weren't sure how to weight $X^2$, read on.
:::

**Beat 1 — The one-sentence idea.** *The expected value is the probability-weighted average of the values — what you'd get per trial, on average, over the long run.*

**Beat 2 — Anchor + concrete instance.** The captain needs *one number* for the center to provision the galley. The naive move is to average $1,2,3,4,5$ to get $3$ — but that pretends every party size is equally likely, and they aren't ($3$ is three times as common as $1$). The honest average weights each value by how often it occurs:

$$\E[X] = 1(0.10) + 2(0.25) + 3(0.30) + 4(0.20) + 5(0.15).$$

Term by term: $0.10 + 0.50 + 0.90 + 0.80 + 0.75 = \mathbf{2.95}$. So the *average* party is $2.95$ Pokémon — even though no single trainer carries $2.95$, and the most common count is $3$.

**Beat 3 — Reason through it in plain words.** Imagine $1000$ trainers drawn from this distribution. About $100$ carry $1$, $250$ carry $2$, $300$ carry $3$, $200$ carry $4$, $150$ carry $5$. The total Pokémon is $100(1)+250(2)+300(3)+200(4)+150(5) = 2950$, and dividing by $1000$ trainers gives $2.95$ per trainer. The expected value is exactly this long-run average, with the *fractions* (the pmf) standing in for the counts. It is the **balance point** of the distribution — the spot where the bar chart would teeter level on a fingertip.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is the **unweighted average**:

$$\frac{1+2+3+4+5}{5} = 3. \qquad\textbf{(wrong — ignores the probabilities)}$$

That answer is only correct if all five values are *equally likely* (the discrete uniform of Concept 8). Here they're not — the heavier weight on $2$ and $3$ pulls the mean down to $2.95$. **The expected value weights by probability; it is not the average of the possible values.** (And, from Concept 3: it is not the mode $3$ either, even though they're close here.)

**Beat 5 — Translate into notation, one glyph at a time.** The expected value (also "mean," also $\mu$):

$$\E[X] = \sum_k k\,p(k) \qquad \text{read aloud: ``the sum, over every value }k\text{, of }k\text{ times its probability.''}$$

We write $\mu = \E[X]$ for short. To average a *function* of $X$ — say $X^2$, or a payout $g(X)$ — you weight the function values, not the raw $k$. This is the **law of the unconscious statistician (LOTUS)**:

$$\E[g(X)] = \sum_k g(k)\,p(k) \qquad \text{read aloud: ``weight each }g(k)\text{ by the probability of }k\text{.''}$$

It's "unconscious" because you *don't* need the distribution of $g(X)$ — you reuse the pmf of $X$ and just transform the values.

**Beat 6 — Generalize: derive $\E[X^2]$ and the linearity rule.** Apply LOTUS with $g(k)=k^2$ to get the **second moment**, which we'll need for variance:

$$\E[X^2] = \sum_k k^2 p(k) = 1(0.10) + 4(0.25) + 9(0.30) + 16(0.20) + 25(0.15) = 0.10+1.00+2.70+3.20+3.75 = 9.85.$$

Note carefully: $\E[X^2] = 9.85 \neq (\E[X])^2 = 2.95^2 = 8.7025$. **Squaring and averaging do not commute** — the gap between them is the variance (Concept 6). One more rule falls out of the sum's structure: pulling constants through and splitting sums gives **linearity of expectation**,

$$\E[aX + b] = a\,\E[X] + b,$$

because $\sum_k (ak+b)p(k) = a\sum_k k\,p(k) + b\sum_k p(k) = a\E[X] + b\cdot 1$. The center shifts by $b$ and scales by $a$, exactly as you'd expect of an average.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $\E[X] = \sum k\,p(k) = 2.95$.
- *Twist (a function/payout):* if the galley charges $\$2$ per Pokémon plus a $\$1$ cover, the cost is $g(X)=2X+1$ and $\E[2X+1] = 2(2.95)+1 = 6.90$ by linearity — no new sum needed.
- *General (LOTUS on a nonlinear $g$):* $\E[X^2]$ above; you must weight the *squared* values, you cannot square the mean.
- *Edge (infinite support):* for $p(k)=(0.5)^k$ on $k=1,2,\dots$, $\E[X]=\sum_k k(0.5)^k = 2$ (a series summed in Chapter 5). The formula is identical; the support is just infinite.

**Beat 8 — Picture it / tool it.** The mean is the **balance point** of the pmf bars (shown dashed in the Concept 3 figure at $2.95$). But the highest-leverage skill in this chapter is *computing* it fast and error-free — and the TI-30XS MultiView has a built-in engine that does the whole $\sum k\,p(k)$ and $\sum k^2 p(k)$ in one pass. That is the flagship Trainer's Tip below; learn it cold.

**Beat 9 — Consolidate.** You can now compute $\E[X]$ as a probability-weighted sum, average any function $g(X)$ via LOTUS (in particular $\E[X^2]$), and rescale a mean with linearity $\E[aX+b]=a\E[X]+b$. The mean is the *center*; the next two concepts give you a second way to find it (survival sum) and a way to measure how far the values *swing* from it (variance).

::: pokedex-entry
**POKÉDEX ENTRY №04 — Expected Value**

$$\E[X] = \sum_k k\,p(k) = \mu, \qquad \E[g(X)] = \sum_k g(k)\,p(k)\ \text{(LOTUS)}, \qquad \E[aX+b] = a\E[X]+b.$$

*In plain terms:* the probability-weighted average of the values — the long-run mean and the balance point. To average $g(X)$, weight the transformed values $g(k)$; to average $X^2$, weight the squares ($\E[X^2]\neq(\E[X])^2$).

*Recognition cue:* "**average / expected / mean / long-run / per-trial**" value, or a **payout** $g(X)$. Multiply each value (or $g$-value) by its probability and add. On the calculator, drive **1-Var Stats**.
:::

## Concept 5 — The Survival-Function (Darth Vader) Method

::: concept-gate
**DO YOU ALREADY OWN THIS? — Survival Sum for the Mean**

A nonnegative integer $N$ has $P(N>0)=0.6$, $P(N>1)=0.35$, $P(N>2)=0.15$, $P(N>3)=0$. Find $\E[N]$ **without** a $\sum k\,p(k)$ sum.

If you answered **$\E[N] = 0.6+0.35+0.15 = 1.10$** (the sum of the survival values), **skip to Concept 6**. If you reached for the pmf first, this section hands you a genuine shortcut.
:::

**Beat 1 — The one-sentence idea.** *For a nonnegative integer random variable, the mean is simply the sum of the survival probabilities $S(0)+S(1)+S(2)+\cdots$ — no value-times-probability sum required.*

**Beat 2 — Anchor + concrete instance.** Now the *second* clipboard: Team Rocket has sunk the ship, and you're handed $N$ = the number of full minutes the S.S. Anne stays afloat, a nonnegative integer. Often a problem gives you the **survival function** $S(k)=P(N>k)$ — "still afloat after $k$ minutes" — directly, not the pmf. The obvious route is to recover each $p(k)$ as a difference of survival values and then sum $k\,p(k)$. The Darth Vader method skips that entirely. With $S(0)=0.6$, $S(1)=0.35$, $S(2)=0.15$, $S(3)=0$:

$$\E[N] = S(0)+S(1)+S(2)+S(3) = 0.6+0.35+0.15+0 = 1.10 \text{ minutes}.$$

The ship survives, on average, $1.10$ minutes — read straight off the "still afloat" curve.

**Beat 3 — Reason through it in plain words.** Why on earth should *adding up survival probabilities* give the mean? Picture the ship's lifetime as a stack of one-minute "tickets." The ship earns a ticket for surviving past minute $0$ (probability $S(0)$), another for surviving past minute $1$ (probability $S(1)$), and so on. Its total lifetime $N$ is just *how many of these tickets it collects*. The **average number of tickets** is the sum of the chances of collecting each one — and the chance of collecting the $k$-th ticket is exactly $S(k)$. Adding the per-ticket survival chances *is* averaging the lifetime.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two traps. First, the **off-by-one start**: the sum begins at $S(0)$, not $S(1)$. $S(0)=P(N>0)=P(N\ge 1)$ is the chance the ship lasts *at least one* minute — it absolutely counts. Dropping it undercounts the mean. Second, **using $F$ instead of $S$**: the mean is $\sum S(k)$, *not* $\sum F(k)$ (the cdf grows without bound as you sum it — that can't be a mean). Remember: you sum the **survival** ("still going") values, starting at $k=0$.

$$\E[N] = \sum_{k=0}^{\infty} S(k), \qquad\textbf{not}\qquad \sum_{k=1}^\infty S(k)\ \text{and not}\ \sum F(k).$$

**Beat 5 — Translate into notation, one glyph at a time.** The rule (named the "Darth Vader rule" because the shaded region under the falling survival staircase has the look of a dark silhouette):

$$\E[N] = \sum_{k=0}^{\infty} S(k) = \sum_{k=0}^\infty P(N > k) \qquad \text{read aloud: ``add the probability of surviving past each }k\text{, from }0\text{ up.''}$$

Each term $S(k)=P(N>k)$ is the height of the survival staircase at $k$; the sum is the **total area** under that staircase. (The continuous twin you'll meet in Chapter 10 replaces the sum with an integral, $\E[X]=\int_0^\infty S(x)\,dx$, the same area idea.)

**Beat 6 — Derive it from the definition (this is the load-bearing derivation).** Start from the ordinary definition $\E[N]=\sum_{k\ge 1} k\,p(k)$ for a nonnegative integer $N$, and rewrite each integer $k$ as a sum of $1$'s — $k = \underbrace{1+1+\cdots+1}_{k\text{ terms}} = \sum_{j=0}^{k-1} 1$:

$$\E[N] = \sum_{k=1}^{\infty} k\,p(k) = \sum_{k=1}^{\infty} \left(\sum_{j=0}^{k-1} 1\right) p(k) = \sum_{k=1}^{\infty}\sum_{j=0}^{k-1} p(k).$$

Now **swap the order of summation**. The pair $(k,j)$ ranges over all $j\ge 0$ with $k > j$. So fix $j$ first and let $k$ run over every value strictly greater than $j$:

$$\E[N] = \sum_{j=0}^{\infty}\sum_{k=j+1}^{\infty} p(k) = \sum_{j=0}^{\infty} P(N > j) = \sum_{j=0}^{\infty} S(j).$$

The inner sum $\sum_{k>j} p(k)$ is *by definition* $P(N>j)=S(j)$. We didn't assert the rule — we *built* it by counting each value $k$ once for every integer below it, then re-bundling by those integers. Sanity-check on the cabin distribution: $\E[X]$ by survival should match $2.95$. With $S(0)=1,\,S(1)=0.9,\,S(2)=0.65,\,S(3)=0.35,\,S(4)=0.15,\,S(5)=0$: $1+0.9+0.65+0.35+0.15 = 3.05$? Careful — the cabin $X$ starts at $1$, not $0$, so $S(0)=P(X>0)=1$; the sum $1+0.9+0.65+0.35+0.15=3.05$ would be the mean if the support included $0$. For a variable supported on $\{1,\dots,5\}$ the convention sums $S(0)+\cdots = 1+0.9+0.65+0.35+0.15$; this equals $\E[X]=2.95$ only after noting $X\ge 1$ contributes a guaranteed $+1$... we keep it clean by using the method only on its native case (support starting at $0$, as with claim **counts**). *(See the Trainer's Tip for the safe statement.)*

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the sinking-ship $N$, $\E[N]=0.6+0.35+0.15=1.10$.
- *Twist (given the cdf instead):* if you're handed $F$, convert first: $S(k)=1-F(k)$, then sum. E.g. $F(0)=0.4,F(1)=0.65,F(2)=0.85,F(3)=1$ gives $S=0.6,0.35,0.15,0$ and $\E[N]=1.10$ again.
- *General (a claim count):* the method shines for distributions naturally supported on $\{0,1,2,\dots\}$ — the number of claims, accidents, or arrivals — which is its bread-and-butter exam use.
- *Edge (must be nonnegative):* the rule needs $N\ge 0$. For a variable that can be negative it does not apply as stated.

**Beat 8 — Picture it.** The mean is the **total area under the survival staircase** — every one-minute "ticket" stacked up.

<figure>
<img src="../../assets/diagrams/ch03_darthvader_area.png" alt="A falling survival staircase S(k)=P(N>k) for a nonnegative integer N, plotted over k = 0, 1, 2, 3. The heights are S(0)=0.6, S(1)=0.35, S(2)=0.15, S(3)=0, drawn as a descending step function over the nonnegative axis. The entire region between the staircase and the axis is shaded and divided into unit-width columns labeled with their heights 0.6, 0.35, 0.15; a label reads 'area = sum of S(k) = E[N] = 1.10'. A small sinking-ship motif sits in the top-right margin, clear of the steps. The requirement N >= 0 is noted." style="width:72%; max-width:520px; display:block; margin:1em auto;">
<figcaption>The Darth Vader method made visual: for a nonnegative integer $N$, the shaded area under the survival staircase $S(k)=P(N>k)$ <em>is</em> $\E[N]$. Each unit-width column has height $S(k)$; summing them ($0.6+0.35+0.15=1.10$) gives the mean — no pmf needed.</figcaption>
</figure>

**Beat 9 — Consolidate.** When a problem hands you a survival function (or a cdf) for a nonnegative integer variable and asks for the mean, you can sum the survival values directly — $\E[N]=\sum_{k\ge 0}S(k)$ — skipping the pmf. You derived it (swap-the-sum), you can picture it (area under the staircase), and you know the two traps (start at $0$, sum $S$ not $F$).

::: pokedex-entry
**POKÉDEX ENTRY №05 — The Survival-Function (Darth Vader) Method**

For a **nonnegative integer** $X$:
$$\E[X] = \sum_{k=0}^{\infty} S(k) = \sum_{k=0}^{\infty} P(X > k) = \sum_{k=0}^\infty \big(1 - F(k)\big).$$

*In plain terms:* the mean is the area under the survival staircase — add the "still going" probabilities from $k=0$ up. No pmf required.

*Recognition cue:* you're handed $S(x)$ **or only the cdf $F$**, the variable is a **nonnegative count**, and you're asked for a mean. Sum the survival values (start at $0$; sum $S$, not $F$). Continuous twin (Ch. 10): $\E[X]=\int_0^\infty S(x)\,dx$.
:::

## Concept 6 — Variance, Standard Deviation, and the Coefficient of Variation

::: concept-gate
**DO YOU ALREADY OWN THIS? — Variance**

For the cabin $X$ you found $\E[X]=2.95$ and $\E[X^2]=9.85$. Find $\Var(X)$ and $\SD(X)$. Then find $\Var(3X-7)$.

If you answered **$\Var(X)=9.85 - 2.95^2 = 1.1475$**, **$\SD(X)\approx 1.071$**, and **$\Var(3X-7)=9(1.1475)=10.3275$**, **skip to Concept 7**. If you forgot to subtract $(\E[X])^2$, or kept the $-7$, read on — those are the two famous slips.
:::

**Beat 1 — The one-sentence idea.** *Variance is the average squared distance of the values from the mean — one number for how widely the random quantity swings — and the standard deviation is its square root, back in the original units.*

**Beat 2 — Anchor + concrete instance.** Lt. Surge, watching from the dock, growls: "Power isn't everything. I want to know if your numbers are *reliable* — do they hold steady, or swing all over?" That's the captain's second question too: how wildly does party size vary cabin to cabin? The center is $\mu=2.95$; the spread asks how far values typically fall from $2.95$. We measure it by averaging the **squared** deviations:

$$\Var(X) = \E\big[(X-\mu)^2\big] = \sum_k (k-2.95)^2\,p(k).$$

But there's a far faster route (Beat 6): $\Var(X) = \E[X^2] - (\E[X])^2 = 9.85 - 2.95^2 = 9.85 - 8.7025 = \mathbf{1.1475}$.

**Beat 3 — Reason through it in plain words.** Why *squared* distances? Raw deviations $X-\mu$ average to **zero** by construction (the positives and negatives cancel — that's what makes $\mu$ the balance point), so they're useless as a spread measure. Squaring kills the signs so deviations can't cancel, and it punishes far-out values more than near ones — a value twice as far contributes four times as much. The **standard deviation** $\SD(X)=\sqrt{\Var(X)}=\sqrt{1.1475}\approx 1.071$ undoes the squaring to land back in "Pokémon" units: a typical cabin sits about $1.07$ Pokémon away from the average.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two famous slips, both recycled into the drills.

First — *the one Team Rocket commits* — **forgetting $-(\E[X])^2$**. Writing $\Var(X) \overset{?}{=} \E[X^2] = 9.85$ vastly overstates the spread. Variance is "mean of the square **minus** square of the mean"; the subtraction is not optional. (Equivalently: $\E[X^2]$ measures spread *around zero*, not around the mean; the $-(\E[X])^2$ re-centers it.)

Second, **a negative variance**. If you ever get one, you subtracted backwards. It is always $\E[X^2]-\mu^2$, **never** $\mu^2 - \E[X^2]$ — variance is an average of squares, so it can never be negative. (A variance of exactly $0$ means $X$ is a constant.)

**Beat 5 — Translate into notation, one glyph at a time.** Variance, its shortcut, and the standard deviation:

$$\Var(X) = \E\big[(X-\mu)^2\big] = \E[X^2] - (\E[X])^2, \qquad \SD(X) = \sqrt{\Var(X)} = \sigma.$$

We write $\sigma^2 = \Var(X)$ and $\sigma=\SD(X)$. The **coefficient of variation** expresses spread *relative* to the mean — a unitless "how big is the swing compared to the center?":

$$\mathrm{CV} = \frac{\SD(X)}{\E[X]} = \frac{\sigma}{\mu} \qquad \text{read aloud: ``standard deviation as a fraction of the mean.''}$$

For the cabin distribution, $\mathrm{CV} = 1.071/2.95 \approx 0.363$.

**Beat 6 — Derive the shortcut and the rescaling rule.** Expand the squared deviation and push expectation through (linearity, Entry №04):

$$\Var(X) = \E[(X-\mu)^2] = \E[X^2 - 2\mu X + \mu^2] = \E[X^2] - 2\mu\,\E[X] + \mu^2.$$

Since $\E[X]=\mu$, the middle term is $-2\mu\cdot\mu = -2\mu^2$ and the last is $+\mu^2$, leaving

$$\boxed{\;\Var(X) = \E[X^2] - \mu^2 = \E[X^2] - (\E[X])^2.\;}$$

Now the behavior under a linear rescale $aX+b$. Shifting by $b$ slides every value *and* the mean by the same $b$, so distances from the mean are unchanged — $b$ cannot affect spread. Scaling by $a$ multiplies every deviation by $a$, and since variance squares deviations, it multiplies by $a^2$:

$$\boxed{\;\Var(aX+b) = a^2\,\Var(X), \qquad \SD(aX+b) = |a|\,\SD(X).\;}$$

The $+b$ vanishes; the $a$ comes out **squared** for variance, as $|a|$ for the standard deviation. So $\Var(3X-7) = 3^2(1.1475) = 10.3275$ — the $-7$ does nothing.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $\Var(X) = \E[X^2]-(\E[X])^2 = 9.85 - 8.7025 = 1.1475$.
- *Twist (rescale):* the galley cost $Y=2X+1$ has $\Var(Y) = 4\,\Var(X) = 4.59$; the $+1$ cover charge never touches the spread.
- *Twist (CV compares risks):* a process with $\mu=100,\sigma=10$ ($\mathrm{CV}=0.10$) is *relatively* steadier than one with $\mu=4,\sigma=1$ ($\mathrm{CV}=0.25$), even though the second's raw $\sigma$ is smaller — CV is how actuaries compare volatility across different scales.
- *Edge (sign discipline):* a negative variance is impossible; if you see one, you did $\mu^2 - \E[X^2]$ by mistake. $\Var=0$ $\Leftrightarrow$ $X$ is constant.

**Beat 8 — Picture it.** Two distributions can share the same center yet differ wildly in spread.

<figure>
<img src="../../assets/diagrams/ch03_variance_spread.png" alt="Two discrete distributions sharing the same mean of 3 drawn on a common value axis. The left one is tightly clustered around 3 with most mass on 2, 3, 4 (small variance); the right one is widely scattered with substantial mass pushed out to 1 and 5 (large variance). Under each, the squared deviations from the mean are shaded, and the average shaded area is labeled Var(X). A side note shows that shifting by b slides the whole picture without changing the shaded spread, while scaling by a stretches it so the spread grows by a-squared." style="width:80%; max-width:560px; display:block; margin:1em auto;">
<figcaption>Variance is the average shaded (squared-deviation) area about the mean. Same center, different spread. Shifting by $b$ slides the picture — spread unchanged; scaling by $a$ stretches it — variance grows by $a^2$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now measure spread: compute $\E[X^2]$, subtract $(\E[X])^2$ for the variance, square-root for the standard deviation, divide by the mean for the CV, and rescale spread under $aX+b$ with the $a^2$ rule. Together with $\E[X]$, you've answered Lt. Surge's two questions — power (mean) and reliability (variance).

::: pokedex-entry
**POKÉDEX ENTRY №06 — Variance, SD, and CV**

$$\Var(X) = \E\big[(X-\mu)^2\big] = \E[X^2] - (\E[X])^2, \qquad \SD(X) = \sqrt{\Var(X)} = \sigma.$$
$$\mathrm{CV} = \frac{\SD(X)}{\E[X]}, \qquad \Var(aX+b) = a^2\Var(X), \qquad \SD(aX+b) = |a|\,\SD(X).$$

*In plain terms:* variance is the average squared distance from the mean; the shortcut "mean of the square minus square of the mean" is almost always faster. A shift $b$ never changes spread; a scale $a$ multiplies variance by $a^2$.

*Recognition cue:* any request for **spread, volatility, standard deviation, reliability, or risk**. Compute $\E[X^2]$ first; the $-(\E[X])^2$ correction is the step people forget. A constant added to $X$ never changes the variance.
:::

## Concept 7 — The Moment Generating Function

::: concept-gate
**DO YOU ALREADY OWN THIS? — MGF**

A random variable has $M_X(t) = 0.2 + 0.5e^t + 0.3e^{2t}$. Find $\E[X]$ and $\E[X^2]$ — by differentiating at $0$ *or* by reading the distribution off the MGF.

If you answered **$\E[X]=1.1$, $\E[X^2]=1.7$** (the MGF is the distribution $P(0)=0.2,P(1)=0.5,P(2)=0.3$, so $\E[X]=0.5+0.6=1.1$, $\E[X^2]=0.5+1.2=1.7$; or $M'(0)=1.1$, $M''(0)=1.7$), **skip to Concept 8**. If "$M_X(t)=\E[e^{tX}]$" is unfamiliar or you can't get moments out of it, read on.
:::

**Beat 1 — The one-sentence idea.** *The moment generating function is one function that, once you have it, hands you every moment of $X$ by differentiating at zero — and its shape uniquely fingerprints the distribution.*

**Beat 2 — Anchor + concrete instance.** So far each moment ($\E[X]$, then $\E[X^2]$) was a separate weighted sum. The MGF packs *all* of them into a single object: it is just $\E[e^{tX}]$, computed by LOTUS (Entry №04) with $g(k)=e^{tk}$. Differentiating it peels off the moments one at a time. Take the small electric-cell distribution Lt. Surge uses to spec a battery — $X$ cells fire, with $P(X=0)=0.2$, $P(X=1)=0.5$, $P(X=2)=0.3$. Its MGF is

$$M_X(t) = \E[e^{tX}] = 0.2\,e^{0t} + 0.5\,e^{1t} + 0.3\,e^{2t} = 0.2 + 0.5e^t + 0.3e^{2t}.$$

*Surge needs the mean and variance to size the breaker.*

**Beat 3 — Reason through it in plain words (why differentiating works).** Why should derivatives at $0$ give moments? Write $e^{tX}$ as its power series — the same $e^u = 1 + u + \tfrac{u^2}{2!} + \cdots$, with $u=tX$:

$$e^{tX} = 1 + tX + \frac{(tX)^2}{2!} + \frac{(tX)^3}{3!} + \cdots$$

Take the expectation of both sides (linearity lets you average term by term):

$$M_X(t) = \E[e^{tX}] = 1 + t\,\E[X] + \frac{t^2}{2!}\E[X^2] + \frac{t^3}{3!}\E[X^3] + \cdots$$

Now read off coefficients: the coefficient of $t$ is $\E[X]$, the coefficient of $t^2$ is $\tfrac{1}{2!}\E[X^2]$, and so on. Differentiating once and setting $t=0$ plucks out the $t$-coefficient ($\E[X]$); differentiating twice plucks out $\E[X^2]$. The MGF is a **moment vending machine** — each derivative at $0$ dispenses the next moment.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is to evaluate the *plain* MGF at $0$ and call it a moment. Note $M_X(0) = \E[e^0] = \E[1] = 1$ for **every** distribution — it carries no information about $X$ and is a built-in sanity check, *not* the mean. The mean is the **first derivative** at $0$:

$$\E[X] = M_X'(0), \qquad\textbf{not}\qquad M_X(0)=1. $$

A second slip: confusing $M_X''(0) = \E[X^2]$ (the *second moment*) with the variance. You still must subtract: $\Var(X) = M_X''(0) - [M_X'(0)]^2$.

**Beat 5 — Translate into notation, one glyph at a time.** The definition:

$$M_X(t) = \E\big[e^{tX}\big] \qquad \text{read aloud: ``the expected value of }e\text{ to the }tX\text{.''}$$

The variable $t$ is a *dummy dial* — not a probability, just a knob we turn near $0$. The notation $M_X^{(n)}(0)$ means "the $n$-th derivative of $M_X$, evaluated at $t=0$," and the moment-extraction rule is

$$\E[X] = M_X'(0), \qquad \E[X^2] = M_X''(0), \qquad \E[X^n] = M_X^{(n)}(0).$$

Two structural facts make MGFs powerful: **uniqueness** — if two random variables have the same MGF, they have the same distribution (so recognizing a kernel *identifies* the variable) — and the rules for sums and rescales of independent variables:

$$M_{X+Y}(t) = M_X(t)\,M_Y(t) \ (\text{independent}), \qquad M_{aX+b}(t) = e^{bt}M_X(at).$$

**Beat 6 — Derive the mean and variance for our cell distribution.** Differentiate $M_X(t)=0.2 + 0.5e^t + 0.3e^{2t}$ (recall $\tfrac{d}{dt}e^{ct} = c\,e^{ct}$):

$$M_X'(t) = 0.5e^t + 0.6e^{2t} \ \Rightarrow\ \E[X] = M_X'(0) = 0.5 + 0.6 = 1.1.$$
$$M_X''(t) = 0.5e^t + 1.2e^{2t} \ \Rightarrow\ \E[X^2] = M_X''(0) = 0.5 + 1.2 = 1.7.$$

Then by Entry №06,

$$\Var(X) = \E[X^2] - (\E[X])^2 = 1.7 - 1.1^2 = 1.7 - 1.21 = 0.49.$$

**Cross-check (read the distribution off the MGF):** a discrete MGF is literally $\sum_k p(k)e^{kt}$, so the coefficient of $e^{kt}$ *is* $p(k)$. Here $p(0)=0.2,p(1)=0.5,p(2)=0.3$ — exactly the cell distribution — and $\E[X]=0(0.2)+1(0.5)+2(0.3)=1.1$, $\E[X^2]=0+0.5+4(0.3)=1.7$, matching. Two routes, one answer, by uniqueness.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* differentiate once for the mean, $M_X'(0)=1.1$.
- *Twist (read off the pmf):* a finite discrete MGF wears its pmf on its sleeve — the coefficient of $e^{kt}$ is $p(k)$. No calculus needed.
- *Kernel recognition (looking ahead):* certain algebraic shapes are signatures of named families you'll meet next — $(0.4 + 0.6e^t)$ is a single Bernoulli, $(0.4+0.6e^t)^n$ is **Binomial$(n,0.6)$**, $e^{\lambda(e^t-1)}$ is **Poisson$(\lambda)$** (mean $=$ variance $=\lambda$). Match the shape, read the parameters, skip the differentiation.
- *Edge (rescale a known MGF):* $M_{aX+b}(t)=e^{bt}M_X(at)$ lets you get the MGF of $2X+1$ without re-deriving — multiply by $e^{t}$ and replace $t$ with $2t$.

**Beat 8 — Table it.** A reference grid of kernels turns recognition into a lookup (filled out fully in Chapters 4–5 as each family arrives):

| MGF kernel | Family | Mean | Variance |
|---|---|---|---|
| $\sum_k p(k)e^{kt}$ | any discrete (read $p(k)$ off $e^{kt}$) | $\sum k\,p(k)$ | $\E[X^2]-\mu^2$ |
| $(1-p+pe^t)^n$ | Binomial$(n,p)$ | $np$ | $np(1-p)$ |
| $e^{\lambda(e^t-1)}$ | Poisson$(\lambda)$ | $\lambda$ | $\lambda$ |

**Beat 9 — Consolidate.** You can now extract any moment from an MGF by differentiating at $0$ ($\E[X]=M'(0)$, $\E[X^2]=M''(0)$, then $\Var=M''(0)-[M'(0)]^2$), read a discrete pmf straight off the $e^{kt}$ coefficients, recognize common kernels to identify a distribution by uniqueness, and rescale or combine MGFs for shifts and independent sums.

::: pokedex-entry
**POKÉDEX ENTRY №07 — Moment Generating Function**

$$M_X(t) = \E\big[e^{tX}\big] = \sum_k e^{kt}p(k), \qquad \E[X^n] = M_X^{(n)}(0), \qquad M_X(0)=1 \text{ (always)}.$$
**Uniqueness:** the MGF determines the distribution. **Independent sums:** $M_{X+Y}(t)=M_X(t)M_Y(t)$. **Linear:** $M_{aX+b}(t)=e^{bt}M_X(at)$.

*In plain terms:* a generator that, once known, dispenses every moment by differentiation at zero — and whose shape uniquely fingerprints the distribution. For a discrete $X$, the coefficient of $e^{kt}$ is $p(k)$.

*Recognition cue:* **"given the MGF," an $e^{tX}$ expectation, or a factored MGF matching a known family.** Differentiate at $0$ for moments (then subtract for variance), or read parameters off the kernel.
:::

## Concept 8 — The Discrete Uniform Distribution

::: concept-gate
**DO YOU ALREADY OWN THIS? — Discrete Uniform**

A fair die-like spinner lands on $1,2,\dots,8$ equally likely. Find $\E[X]$ and $\Var(X)$.

If you answered **$\E[X]=\tfrac{8+1}{2}=4.5$** and **$\Var(X)=\tfrac{8^2-1}{12}=5.25$**, **skip to the Worked Examples**. If you'd have summed by hand (fine, but slow) or didn't know the closed forms, read on.
:::

**Beat 1 — The one-sentence idea.** *The discrete uniform distribution models "$n$ equally likely outcomes" — every value $1,2,\dots,n$ has the same probability $1/n$ — and its mean and variance have clean closed forms.*

**Beat 2 — Anchor + concrete instance.** Pikachu refuses the Thunder Stone Lt. Surge offers — choosing to stay Pikachu rather than evolve, on its own terms. Its mascot here is **Ditto**: any of $n$ equally likely forms, none favored. Concretely, model a fair $6$-sided outcome $X\in\{1,2,3,4,5,6\}$, each with probability $\tfrac16$. This is the *one* case where the unweighted average (the trap of Concept 4) is actually correct — because the weights really are all equal.

**Beat 3 — Reason through it in plain words.** With every value equally likely, the center is just the **midpoint** of the range — for $\{1,\dots,6\}$, that's $\tfrac{1+6}{2}=3.5$. The spread depends only on *how wide* the range is: values spread over $\{1,\dots,6\}$ swing more than values crammed into $\{1,2,3\}$. Both summaries turn out to depend only on $n$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is mis-reading the **support and its size**. If the values are $\{1,2,\dots,n\}$ the mean is $\tfrac{n+1}{2}$ — but if the values are $\{0,1,\dots,n\}$ that's $n+1$ outcomes and the mean is $\tfrac{n}{2}$. And **uniform does not mean "mean $=$ any old midpoint"** unless the spacing is the consecutive integers $1,2,\dots,n$. Always confirm the support is $\{1,\dots,n\}$ before applying the closed forms. (A spinner labelled $\{2,4,6,8\}$ is uniform on $4$ values but the integer formulas don't apply directly — shift/scale it first.)

**Beat 5 — Translate into notation, one glyph at a time.** Write $X \sim \Unif\{1,\dots,n\}$ ("$X$ is **distributed as** discrete uniform on $1$ through $n$"; the $\sim$ reads "is distributed as"). Its pmf, mean, and variance:

$$p(k) = \frac{1}{n} \text{ for } k=1,\dots,n, \qquad \E[X] = \frac{n+1}{2}, \qquad \Var(X) = \frac{n^2-1}{12}.$$

**Beat 6 — Derive both closed forms.** For the **mean**, use the famous sum of the first $n$ integers, $\sum_{k=1}^n k = \tfrac{n(n+1)}{2}$:

$$\E[X] = \sum_{k=1}^n k\cdot\frac1n = \frac1n\cdot\frac{n(n+1)}{2} = \frac{n+1}{2}.$$

For the **variance**, use $\sum_{k=1}^n k^2 = \tfrac{n(n+1)(2n+1)}{6}$ to get the second moment, then subtract the squared mean:

$$\E[X^2] = \frac1n\sum_{k=1}^n k^2 = \frac1n\cdot\frac{n(n+1)(2n+1)}{6} = \frac{(n+1)(2n+1)}{6}.$$

$$\Var(X) = \E[X^2] - (\E[X])^2 = \frac{(n+1)(2n+1)}{6} - \left(\frac{n+1}{2}\right)^2.$$

Factor out $\tfrac{n+1}{12}$: $\Var(X) = \tfrac{n+1}{12}\big[2(2n+1) - 3(n+1)\big] = \tfrac{n+1}{12}(4n+2-3n-3) = \tfrac{n+1}{12}(n-1) = \dfrac{n^2-1}{12}.$ Both forms are *derived*, not memorized — though once derived, memorize them.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* fair six-sided $X$: $\E[X]=\tfrac{7}{2}=3.5$, $\Var(X)=\tfrac{35}{12}\approx 2.917$.
- *Twist (a function of a uniform):* a payout $3X$ on a fair die has mean $3(3.5)=10.5$ and variance $9\cdot\tfrac{35}{12}=26.25$ (linearity + the $a^2$ rule, Entries №04/06).
- *General (any $n$):* the spinner on $\{1,\dots,8\}$: mean $4.5$, variance $\tfrac{63}{12}=5.25$.
- *Edge (shifted support):* $\{0,1,\dots,n\}$ has $n+1$ equally likely values, mean $\tfrac n2$, variance $\tfrac{(n+1)^2-1}{12}=\tfrac{n^2+2n}{12}$ — re-derive, don't blindly reuse.

**Beat 8 — Stat block.** The discrete uniform as a Field-Guide entry (mascot: Ditto — any form, equally likely):

::: pokedex-entry
**POKÉDEX SCAN — Discrete Uniform $\{1,\dots,n\}$ · "the Equally-Likely Pokémon" (Ditto)**

| Field | Value |
|---|---|
| **Type** | Discrete |
| **Support** | $k \in \{1, 2, \dots, n\}$ |
| **pmf** | $p(k) = \dfrac{1}{n}$ |
| **Mean** | $\E[X] = \dfrac{n+1}{2}$ |
| **Variance** | $\Var(X) = \dfrac{n^2 - 1}{12}$ |
| **MGF** | $M_X(t) = \dfrac{1}{n}\displaystyle\sum_{k=1}^{n} e^{kt}$ |

*Fidelity:* like Ditto's equally likely transformations, no outcome is favored — every value carries the same mass $1/n$.

*Recognition cue:* **"equally likely," "a fair die / random integer from $1$ to $n$," "each outcome has the same chance."** Apply $\tfrac{n+1}{2}$ and $\tfrac{n^2-1}{12}$ — after confirming the support is $\{1,\dots,n\}$.
:::

**Beat 9 — Consolidate.** You can now recognize the equally-likely model, apply its closed-form mean $\tfrac{n+1}{2}$ and variance $\tfrac{n^2-1}{12}$ (and derive them when the support shifts), and you know it's the one case where the unweighted average is the right mean.

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/surge.png" alt="Lt. Surge, the Vermilion Gym Leader" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Lt. Surge — Vermilion Gym Leader, judge of power (mean) and reliability (variance)</figcaption>
</figure>

Four examples, fading from fully narrated to exam-speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*, on the calculator), because the mean/variance of a pmf is the load-bearing skill of this entire topic.

### Worked Example 1 — The Cabin Census (full narration; understanding-first)

**ARCHETYPE:** *Mean and variance of a pmf — the flagship Topic-2 skill.*

**Setup.** This is the captain's question, solved cleanly. The number of Pokémon a random trainer carries has pmf $p(1)=0.10,\,p(2)=0.25,\,p(3)=0.30,\,p(4)=0.20,\,p(5)=0.15$. Find $\E[X]$, $\Var(X)$, and $\SD(X)$.

**Step 1 — Identify (what's being asked).** Center and spread of a discrete pmf $\to$ compute $\E[X]$ and $\E[X^2]$, then $\Var=\E[X^2]-(\E[X])^2$. First, *validate*: $0.10+0.25+0.30+0.20+0.15 = 1.00$ ✓, all nonnegative ✓ — a valid pmf.

**Step 2 — Professor's Path (the why).** The mean is the probability-weighted average (Entry №04):

$$\E[X] = \sum_k k\,p(k) = 1(0.10)+2(0.25)+3(0.30)+4(0.20)+5(0.15) = 0.10+0.50+0.90+0.80+0.75 = 2.95.$$

The second moment weights the *squares* (LOTUS):

$$\E[X^2] = \sum_k k^2 p(k) = 1(0.10)+4(0.25)+9(0.30)+16(0.20)+25(0.15) = 0.10+1.00+2.70+3.20+3.75 = 9.85.$$

Variance is mean-of-square minus square-of-mean (Entry №06):

$$\Var(X) = \E[X^2]-(\E[X])^2 = 9.85 - 2.95^2 = 9.85 - 8.7025 = 1.1475, \qquad \SD(X) = \sqrt{1.1475} \approx 1.0712.$$

**Step 3 — Trainer's Path (the fast how: 1-Var Stats).** Don't hand-sum under time pressure — use the calculator's statistics engine. Enter the values in list **L1** and the probabilities in **L2**, then run **1-Var Stats** reading L2 as the frequency list. The machine returns $\bar{x}=2.95$ (the mean) and $\sigma x = 1.0712$ (whose **square** is the variance, $\sigma x^2 = 1.1475$). Full key-caps in the flagship Trainer's Tip below.

**Step 4 — Check & pitfall.** Sanity: $\E[X]=2.95$ lies inside the support $[1,5]$ ✓ and near the mode $3$ ✓; $\Var(X)=1.1475 > 0$ ✓. **Pitfall:** reporting $\Var(X)=\E[X^2]=9.85$ — forgetting the $-(\E[X])^2$; or reporting the unweighted average $3$ as the mean. *(Back-ref: Entries №04, №06.)*

### Worked Example 2 — How Long Does the Ship Survive? (partial guidance)

**ARCHETYPE:** *Mean of a nonnegative count via the survival-function (Darth Vader) method.*

**Setup.** As the S.S. Anne floods, the number of whole minutes $N$ it stays afloat has survival function $S(0)=0.6$, $S(1)=0.35$, $S(2)=0.15$, $S(3)=0$. Find $\E[N]$ two ways and confirm they agree.

<figure style="margin:1.25em auto; max-width:150px; text-align:center;">
<img src="../../assets/items/escape-rope.png" alt="An Escape Rope item icon, evoking the evacuation of the sinking ship" style="width:90px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">The clock is running — how many minutes, on average?</figcaption>
</figure>

**Identify.** Nonnegative integer count, survival function handed to you $\to$ Darth Vader method: $\E[N]=\sum_{k\ge 0}S(k)$ (Entry №05). *Your move: add the survival values.*

**Survival sum (fast):**
$$\E[N] = S(0)+S(1)+S(2)+S(3) = 0.6 + 0.35 + 0.15 + 0 = 1.10 \text{ minutes}.$$

**Cross-check via the pmf.** Recover each mass as a drop in survival: $p(0)=S(-1)-S(0)$... cleaner to use $p(k)=S(k-1)-S(k)$ with $S(-1)=1$: $p(0)=1-0.6=0.4$, $p(1)=0.6-0.35=0.25$, $p(2)=0.35-0.15=0.20$, $p(3)=0.15-0=0.15$. Then
$$\E[N] = 0(0.4)+1(0.25)+2(0.20)+3(0.15) = 0+0.25+0.40+0.45 = 1.10. \checkmark$$

**Check & pitfall.** Both routes give $1.10$ ✓, and $\sum p(k)=0.4+0.25+0.20+0.15=1$ ✓. **Pitfall:** starting the survival sum at $S(1)$ (dropping $S(0)=0.6$ undercounts to $0.50$), or summing $F$ instead of $S$. *(Back-ref: Entries №02, №05.)*

### Worked Example 3 — Reading the Battery MGF (light guidance)

**ARCHETYPE:** *Moments from a moment generating function.*

**Setup.** Lt. Surge's battery fires $X$ cells with $M_X(t) = 0.2 + 0.5e^t + 0.3e^{2t}$. Find $\E[X]$, $\Var(X)$, and the mode.

**Differentiate at $0$ (Entry №07).**
$$M_X'(t) = 0.5e^t + 0.6e^{2t} \Rightarrow \E[X]=M_X'(0)=1.1; \qquad M_X''(t)=0.5e^t+1.2e^{2t} \Rightarrow \E[X^2]=M_X''(0)=1.7.$$
$$\Var(X) = 1.7 - 1.1^2 = 1.7 - 1.21 = 0.49.$$

**Read the pmf off the kernel.** Coefficients of $e^{kt}$ give $p(0)=0.2,p(1)=0.5,p(2)=0.3$, so the **mode** is the most likely value, $k=1$ ($p(1)=0.5$ is largest).

**Check & pitfall.** $M_X(0)=0.2+0.5+0.3=1$ ✓ (every MGF must). **Pitfall:** quoting $M_X(0)=1$ as the mean (it's always $1$), or forgetting to subtract $(\E[X])^2$ when going from $M''(0)$ to the variance. *(Back-ref: Entries №03, №06, №07.)*

### Worked Example 4 — The Fair Spinner (exam speed)

**ARCHETYPE:** *Discrete uniform — closed-form mean and variance.*

**Setup.** A prize spinner lands on $\{1,2,\dots,10\}$ equally likely. Find $\E[X]$, $\Var(X)$, and $\E[2X+3]$.

$$\E[X] = \frac{n+1}{2} = \frac{11}{2} = 5.5, \qquad \Var(X) = \frac{n^2-1}{12} = \frac{99}{12} = 8.25.$$
$$\E[2X+3] = 2\E[X]+3 = 2(5.5)+3 = 14 \quad(\text{linearity, Entry №04}).$$

**Check & pitfall.** Mean $5.5$ is the midpoint of $1$–$10$ ✓; variance $8.25>0$ ✓. **Pitfall:** using $\tfrac{n+1}{2}$ when the support is actually $\{0,\dots,n\}$ or non-consecutive — confirm the support is $\{1,\dots,n\}$ first. *(Back-ref: Entry on the Discrete Uniform.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — THE FLAGSHIP: 1-Var Stats cracks any pmf mean & variance**

This single workflow solves a huge share of Topic-2 questions in seconds and kills rounding errors. You enter the **values** in list L1 and the **probabilities** (or frequencies) in L2, then let the calculator compute $\sum k\,p(k)$ and $\sum k^2 p(k)$ for you. On the TI-30XS MultiView, for Worked Example 1's cabin pmf:

**1. Open the data editor and clear it.** Press [data]{.kbd} [data]{.kbd} (the second press offers *Clear L1*) — or [data]{.kbd} then arrow to *CLR ALL* — to wipe old lists.

**2. Type the values into L1, the probabilities into L2.** With the cursor in the L1 column:
[ 1 [enter]{.kbd} 2 [enter]{.kbd} 3 [enter]{.kbd} 4 [enter]{.kbd} 5 [enter]{.kbd} ]{.keystroke}
then arrow to the **L2** column and enter the matching probabilities:
[ 0.10 [enter]{.kbd} 0.25 [enter]{.kbd} 0.30 [enter]{.kbd} 0.20 [enter]{.kbd} 0.15 [enter]{.kbd} ]{.keystroke}

**3. Run 1-Var Stats.** Press [2nd]{.kbd} [data]{.kbd} (this is the **[stat]** function). Choose **1-Var Stats**. Set **DATA: L1** and, crucially, **FRQ: L2** (frequency = the probability list) — this is what tells the machine to *weight* each value by its probability. Press [enter]{.kbd} to calculate.

**4. Read the screen.** Scroll the results:
- $\bar{x} = 2.95$ — this is $\E[X]$, the **mean**.
- $\sigma x = 1.0712$ — the **population** standard deviation. Its **square is the variance:** $\sigma x^2 = 1.1475$. Square it on the home screen with [x²]{.kbd}: [ 1.0712 [x²]{.kbd} [enter]{.kbd} ]{.keystroke} $\to 1.1475$.
- $\sum x$ and $\sum x^2$ are also shown if you'd rather grab the raw moments.

**The one trap that voids the answer:** read **$\sigma x$, never $sx$.** The TI also reports $sx$ — the *sample* SD that divides by $n-1$. For a probability distribution you want the **population** value $\sigma x$ (lowercase sigma); $sx$ gives a wrong variance. When your probabilities sum to exactly $1$, $\sigma x$ is correct and $sx$ is meaningless. **Mean $=\bar x$; variance $=(\sigma x)^2$ — every time.**
:::

::: trainers-tip
**TRAINER'S TIP — Store the mean, don't retype it**

When a follow-up asks for $\E[2X+3]$ or $\Var(X)$ from $\E[X]$ and $\E[X^2]$, bank the mean once with [STO▸]{.kbd} so rounding never drifts. After 1-Var Stats, store $\bar x$: on the home screen [ 2.95 [STO▸]{.kbd} [x]{.kbd} [enter]{.kbd} ]{.keystroke}, then compute the variance from the stored value, e.g. [ 9.85 [−]{.kbd} [x]{.kbd} [x²]{.kbd} [enter]{.kbd} ]{.keystroke} $\to 1.1475$. Store-don't-retype is the same discipline you used for the Bayes denominator in Cerulean.
:::

::: trainers-tip
**TRAINER'S TIP — The survival sum starts at zero**

For a nonnegative integer count, $\E[X]=\sum_{k=0}^\infty S(k)$ — the first term is $S(0)=P(X>0)$, and dropping it is the most common Darth-Vader error. If you're handed the cdf instead, convert termwise with $S(k)=1-F(k)$ before summing. And summing $S$, not $F$: the cdf marches toward $1$ and its sum diverges, which can never be a mean.
:::

::: trainers-tip
**TRAINER'S TIP — Variance: square the mean, don't square the SD by accident**

The shortcut is $\Var(X)=\E[X^2]-(\E[X])^2$. Compute $\E[X^2]$ first (weight the *squared* values), then subtract the *square* of the mean — not the mean of the squares twice. Quick sanity gates: variance is **never negative**; the SD is always **smaller than the range**; and a $+b$ shift changes the mean but **never** the variance.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

From the lifeboat, Meowth has swiped the captain's cabin slip and is doing the galley's job for them. "Lookit dis — three Pokémon is da most common cabin, taller bar than all da others! So da *average* cabin is three Pokémon. Order food for three per trainer, easy money!"

Jessie nods. "Obviously. The biggest bar *is* the average. Provision for three."

James squints at the slip. "But… there's a whole pile of cabins carrying only one or two. Wouldn't all those drag the average *down* a little below three…?"

Meowth waves him off. "Three's da winner, three's da average! Same t'ing!" — and orders exactly enough food for three-per-trainer.

**Where it fails:** Meowth reported the **mode** ($3$, the most likely value) as if it were the **mean** (the probability-weighted average). They are *different questions*: the mean here is $\E[X]=1(0.10)+2(0.25)+3(0.30)+4(0.20)+5(0.15) = 2.95$, dragged *below* $3$ by exactly the light-cabin mass James noticed. Provisioning for $3.0$ per trainer over-orders by $0.05$ per trainer — a real waste at cruise scale. The mode is the tallest bar; the mean is the balance point; on a skewed distribution they can differ by a lot. **Compute the weighted average — never substitute the mode for the mean.** (An audit drill, C3.7, makes you catch this exact error.)
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

This is the literal math of **pricing insurance claims** — and the reason insurers price the *average*, not the *typical* case.

An insurer covering a block of policies cares about the **expected claim count** and **expected claim cost** per policy — the $\E[X]$ you computed for the cabins — because over thousands of policies the *average* is what the premiums must cover. The most *common* outcome is often **zero claims** (the mode), but pricing to the mode would set premiums at zero and bankrupt the company; the mean, pulled up by the rare large claims, is the honest price. Meowth's "the biggest bar is the average" error is exactly the mistake that sinks a naive pricer.

The **variance** is just as load-bearing: it sets the **risk loading** (the cushion above expected cost) and the capital an insurer must hold so a bad year doesn't ruin it. Lt. Surge's two numbers — power (mean) and reliability (variance) — are precisely the two an actuary reports for any risk. The **coefficient of variation** lets them compare the relative volatility of a small auto book against a large homeowners book on equal footing. And the **survival function** is the native language of **lifetime and reliability models**: $S(x)=P(\text{still alive / still working after } x)$ underlies life insurance, pensions, and warranty pricing — and the Darth-Vader rule $\E[X]=\sum S(k)$ is how you read an expected lifetime straight off a survival table.

*Series bridge:* the moment generating function you met here is the workhorse of later exams — it proves the **Central Limit Theorem** (Ch. 12), identifies sums of independent risks (FM / LTAM), and underlies the **collective risk model** (CAS Exam 5 / STAM). And the discrete-uniform, expectation, and variance machinery is the foundation every named distribution in Chapters 4–5 is built on.

*Transfer check:* could you solve this with **no Pokémon in it**? "A random variable takes values $1$–$5$ with probabilities $0.10,0.25,0.30,0.20,0.15$; find its mean, variance, and the most likely value." Same numbers, same $2.95$, $1.1475$, mode $3$. If you can do that, the skill has transferred.
:::

## The Gym Battle — Thunder Badge Capstone

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/types/electric.png" alt="Electric type icon" style="width:90px; display:block; margin:0 auto;">
<figcaption style="font-size:0.85em;">Lt. Surge's Electric Gym — the Thunder Badge challenge</figcaption>
</figure>

**Lt. Surge's Challenge.** "Enough drills, soldier," Surge barks, planting himself between you and the badge. "Here's a real spec sheet. My Raichu's Thunderbolt deals damage $X$ in one of four amounts, and I've logged how often each lands." He slaps down the table — but tears off the last probability.

| Damage $k$ | $20$ | $40$ | $60$ | $80$ |
|---|---|---|---|---|
| $p(k) = P(X=k)$ | $0.15$ | $0.35$ | $c$ | $0.20$ |

"Tell me four things, the way an actuary would: the missing probability $c$; the **expected damage** (my power); the **variance and standard deviation** of the damage (my reliability); and — because my breaker is rated per *boosted* shot — the mean and variance of the **boosted damage** $Y = 1.5X + 10$. Get all four right and the Thunder Badge is yours."

**ARCHETYPE:** *Full pmf workflow — normalize, mean, variance/SD, and linear-transform mean & variance.*

**Step 1 — Normalize to find $c$ (Entry №01).** A valid pmf sums to $1$:
$$0.15 + 0.35 + c + 0.20 = 1 \;\Rightarrow\; c = 1 - 0.70 = 0.30.$$
So $p(20)=0.15,\,p(40)=0.35,\,p(60)=0.30,\,p(80)=0.20$.

**Step 2 — Expected damage, the mean (Entry №04 / 1-Var Stats).**
$$\E[X] = 20(0.15)+40(0.35)+60(0.30)+80(0.20) = 3 + 14 + 18 + 16 = 51.$$
*(Calculator: L1 $=20,40,60,80$; L2 $=0.15,0.35,0.30,0.20$; 1-Var Stats with FRQ$=$L2 returns $\bar x = 51$.)*

**Step 3 — Variance and SD (Entry №06).** Second moment first:
$$\E[X^2] = 400(0.15)+1600(0.35)+3600(0.30)+6400(0.20) = 60 + 560 + 1080 + 1280 = 2980.$$
$$\Var(X) = \E[X^2]-(\E[X])^2 = 2980 - 51^2 = 2980 - 2601 = 379, \qquad \SD(X) = \sqrt{379} \approx 19.47.$$
*(Calculator cross-check: $\sigma x \approx 19.47$, and $\sigma x^2 = 379$.)*

**Step 4 — The boosted shot $Y = 1.5X + 10$ (linearity + the $a^2$ rule).**
$$\E[Y] = 1.5\,\E[X] + 10 = 1.5(51) + 10 = 76.5 + 10 = 86.5.$$
$$\Var(Y) = 1.5^2\,\Var(X) = 2.25(379) = 852.75, \qquad \SD(Y) = 1.5\,\SD(X) \approx 29.20.$$
The $+10$ boost shifts the mean but **does nothing** to the variance; the $\times 1.5$ scales the mean by $1.5$ and the variance by $1.5^2=2.25$.

**Step 5 — Check & the pitfalls Surge is testing.** Sanity: $c=0.30\in[0,1]$ and the pmf now sums to $1$ ✓; $\E[X]=51$ lies inside $[20,80]$ ✓; $\Var(X)=379>0$ ✓. The traps Surge planted: (a) forgetting to **normalize** for $c$; (b) reporting $\E[X^2]=2980$ as the variance instead of subtracting $51^2$; (c) keeping the $+10$ in the variance of $Y$ (it must vanish). Avoid all three and the spec sheet checks out.

> "Power *and* reliability — and you handled the rescale without flinching," Surge says, grinning, and presses the Thunder Badge into your palm. "That's a soldier's work. The badge is yours."

*(A trainer who only reported the mode — $40$, the tallest bar — would have handed Surge the wrong "power" entirely; see audit drill C3.7.)*

## The Gym Challenge — Problem Set

::: problem-set
**THE S.S. ANNE LOGBOOK — your questline.** The captain has commissioned you as the ship's actuary. This problem set is one escalating mission: the **Route Trainer** legs are dockside fieldwork (validating manifests, reading cabin tables, quick survival checks); the **Gym Battle** tier is the boss fight (Lt. Surge's full spec sheet at exam difficulty); the **Elite Challenge** tier is optional post-game once the badge is yours. Work it timed (~6 min/problem, faster with 1-Var Stats), then check the **Answers** below. Hit the mastery bar (**80%+ with correct method**) to clear the questline and claim the Thunder Badge. Problems are listed first; full worked solutions follow afterward (never interleaved). Markers: 🔴 routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (the early legs — validating & reading the manifest)

**C3.1.** 🔴 *(The captain's first task: validate a cabin manifest before trusting it.)* A proposed pmf for $X\in\{0,1,2,3\}$ is $p(0)=0.1,\,p(1)=0.3,\,p(2)=0.4,\,p(3)=c$. Find $c$ that makes it a valid pmf, then compute $P(X\le 1)$.

**C3.2.** 🔴 *(Reading the galley's party-size table.)* A trainer carries $X$ Pokémon with $p(1)=0.2,\,p(2)=0.5,\,p(3)=0.3$. Find $\E[X]$.

**C3.3.** 🔴 *(Spread of the same party-size table — for provisioning slack.)* For the $X$ in C3.2 ($p(1)=0.2,p(2)=0.5,p(3)=0.3$), find $\E[X^2]$ and $\Var(X)$.

**C3.4.** 🔴 *(CALC SKILL — drive the 1-Var Stats engine on a deck-occupancy table.)* A deck holds $X$ trainers, $X\in\{2,3,4,5\}$ with probabilities $0.1,0.4,0.3,0.2$. Using the calculator's 1-Var Stats (values in L1, probabilities in L2), find the mean $\bar x$ and the variance $\sigma x^2$.

**C3.5.** 🟡 *(Building the cdf from a manifest, then reading a range.)* $X\in\{1,2,3,4\}$ with pmf $0.2,0.3,0.4,0.1$. Find the cdf value $F(2)$ and $P(2 < X \le 4)$.

**C3.6.** 🟡 *(Survival check on a flooding deck.)* A deck stays dry for $N$ whole minutes, a nonnegative integer, with survival values $S(0)=0.7,\,S(1)=0.4,\,S(2)=0.1,\,S(3)=0$. Find $\E[N]$ by the survival-function method.

**C3.7.** 🟡 *(AUDIT — Team Rocket "provisioned for the mode.")* The cabin pmf is $p(1)=0.10,\,p(2)=0.25,\,p(3)=0.30,\,p(4)=0.20,\,p(5)=0.15$. Meowth reports "the most common cabin is $3$, so the average party size is $3$." Find the true $\E[X]$ and name Meowth's error.

**C3.8.** 🔴 *(A fair prize spinner on the promenade deck.)* A spinner lands on $\{1,2,\dots,6\}$ equally likely. Find $\E[X]$ and $\Var(X)$.

> *Questline beat: the dockside fieldwork is done. The captain points you to the gym. Lt. Surge is the boss.*

### Gym Battles (the boss fight — true SOA difficulty)

**C3.9.** 🟡 *(Surge's tear-off spec sheet — normalize, then summarize.)* $X\in\{10,20,30,40\}$ with $p(10)=0.2,\,p(20)=c,\,p(30)=0.3,\,p(40)=0.1$. Find $c$, then $\E[X]$ and $\Var(X)$.

**C3.10.** 🟡 *(Sizing the breaker for a boosted shot — a linear transform.)* For a damage $X$ with $\E[X]=51$ and $\Var(X)=379$ (given), find $\E[Y]$ and $\Var(Y)$ for the boosted shot $Y = 1.5X + 10$.

**C3.11.** 🟡 *(Reading moments off a battery's MGF.)* A cell count $X$ has $M_X(t) = 0.3 + 0.4e^{t} + 0.3e^{2t}$. Find $\E[X]$ and $\Var(X)$.

**C3.12.** 🔵 *(RIVAL TRAP — Gary reads variance straight off $\E[X^2]$.)* For $X$ with $p(0)=0.5,\,p(1)=0.3,\,p(2)=0.2$, Gary computes $\E[X^2]=1.1$ and declares "so the variance is $1.1$." Find the true $\Var(X)$ and name Gary's error.

**C3.13.** 🟡 *(Median and percentile of a deck-damage table — for a guarantee clause.)* $X\in\{1,2,3,4,5\}$ with pmf $0.1,0.2,0.4,0.2,0.1$. Find the median and the $90$th percentile.

**C3.14.** 🔵 *(AUDIT — Meowth's "survival sum" forgot the first term.)* A claim count $N$ has $S(0)=0.5,\,S(1)=0.3,\,S(2)=0.1,\,S(3)=0$. Meowth sums "$0.3+0.1=0.4$" and reports $\E[N]=0.4$. Find the true $\E[N]$ and name his error.

**C3.15.** 🟡 *(A payout that is a function of damage — LOTUS.)* Damage $X\in\{1,2,3\}$ with pmf $0.5,0.3,0.2$. A repair cost is $g(X)=X^2 + 2$. Find $\E[g(X)]$.

**C3.16.** 🔵 *(Coefficient of variation — comparing two reactors' reliability.)* Reactor A's output has $\mu=50,\sigma=5$; Reactor B's has $\mu=8,\sigma=1.2$. Compute each CV and state which is *relatively* more reliable.

**C3.17.** 🟡 *(Mode, median, and mean of one table — three different jobs.)* $X\in\{1,2,3,4\}$ with pmf $0.4,0.1,0.1,0.4$. Find the mode, the median, and the mean, and note whether they coincide.

**C3.18.** 🔵 *(RIVAL TRAP — Gary applies the discrete-uniform formula to the wrong support.)* A spinner lands on $\{0,1,2,\dots,9\}$ equally likely. Gary says "$n=9$ so the mean is $(9+1)/2 = 5$." Find the true $\E[X]$ and name his error.

> *Questline beat: the badge is yours. The post-game below is optional — but it's where the sharpest actuaries play.*

### Elite Challenge (post-game — integrative / stretch)

**C3.19.** 🔵 *(DECISION — flat fee vs. per-Pokémon billing on the same crowd.)* The cabin pmf is $p(1)=0.10,p(2)=0.25,p(3)=0.30,p(4)=0.20,p(5)=0.15$ (so $\E[X]=2.95$). The galley can bill **Option A:** a flat $\$8$ per cabin, or **Option B:** $\$3$ per Pokémon. Compute the expected revenue per cabin under each, and say which yields more on average.

**C3.20.** 🔵 *(Variance via the survival/pmf bridge — a full count summary.)* A claim count $N$ has $S(0)=0.6,\,S(1)=0.3,\,S(2)=0.1,\,S(3)=0$. Find $\E[N]$ (survival method) and $\Var(N)$ (recover the pmf, then $\E[N^2]-(\E[N])^2$).

**C3.21.** 🔵 *(Identify a distribution from its MGF, then summarize.)* A surge count has $M_X(t) = \tfrac{1}{4}\big(e^{t}+e^{2t}+e^{3t}+e^{4t}\big)$. Identify the distribution by name, and give $\E[X]$ and $\Var(X)$ using its closed forms.

**C3.22.** 🔵 *(DECISION — guarantee at the mean or at a percentile?)* Deck-clearing time $X\in\{1,2,3,4,5\}$ minutes has pmf $0.1,0.2,0.4,0.2,0.1$. The captain can promise evacuation "by the **mean** time" or "by the **80th percentile** time." Compute both times and state which promise is safer (covers more evacuations) and why the two differ.
:::

## Answers

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

**C3.1** — *(standard) Normalize a pmf, then accumulate (Entry №01, №02).* Sum to one: $0.1+0.3+0.4+c=1 \Rightarrow c=0.2$. Then $P(X\le 1) = p(0)+p(1) = 0.1+0.3 = 0.40$.

**C3.2** — *(standard) Expected value of a pmf (Entry №04).*
$$\E[X] = 1(0.2)+2(0.5)+3(0.3) = 0.2+1.0+0.9 = 2.1.$$

**C3.3** — *(standard) Second moment and variance (Entries №04, №06).*
$$\E[X^2] = 1(0.2)+4(0.5)+9(0.3) = 0.2+2.0+2.7 = 4.9, \qquad \Var(X) = 4.9 - 2.1^2 = 4.9 - 4.41 = 0.49.$$

**C3.4** — *(standard; calc skill) 1-Var Stats on L1/L2 (Entries №04, №06).* L1 $=2,3,4,5$; L2 $=0.1,0.4,0.3,0.2$. By hand to confirm the calculator: $\E[X] = 2(0.1)+3(0.4)+4(0.3)+5(0.2) = 0.2+1.2+1.2+1.0 = 3.6$; $\E[X^2] = 4(0.1)+9(0.4)+16(0.3)+25(0.2) = 0.4+3.6+4.8+5.0 = 13.8$; $\Var(X) = 13.8 - 3.6^2 = 13.8 - 12.96 = 0.84$. The machine returns $\bar x = 3.6$, $\sigma x^2 = 0.84$.

**C3.5** — *(standard) cdf and an interval (Entry №02).* $F(2) = p(1)+p(2) = 0.2+0.3 = 0.50$. $P(2<X\le 4) = F(4)-F(2) = 1.00 - 0.50 = 0.50$ (i.e. $p(3)+p(4) = 0.4+0.1 = 0.50$ ✓).

**C3.6** — *(standard) Survival-function (Darth Vader) method (Entry №05).*
$$\E[N] = S(0)+S(1)+S(2)+S(3) = 0.7+0.4+0.1+0 = 1.2.$$

**C3.7** — *(audit) Mode-vs-mean — the chapter's Team Rocket error (Entries №03, №04).*
$$\E[X] = 1(0.10)+2(0.25)+3(0.30)+4(0.20)+5(0.15) = 0.10+0.50+0.90+0.80+0.75 = 2.95.$$
**Meowth's error:** he reported the **mode** ($3$, the tallest bar) as the **mean**. They answer different questions; the light-cabin mass drags the true mean to $2.95$, *below* the mode. Never substitute the mode for the mean.

**C3.8** — *(standard) Discrete uniform closed forms (Discrete Uniform entry).* $n=6$: $\E[X] = \tfrac{6+1}{2} = 3.5$; $\Var(X) = \tfrac{6^2-1}{12} = \tfrac{35}{12} \approx 2.9167$.

**C3.9** — *(standard) Normalize, then mean & variance (Entries №01, №04, №06).* $c = 1 - (0.2+0.3+0.1) = 0.4$. $\E[X] = 10(0.2)+20(0.4)+30(0.3)+40(0.1) = 2+8+9+4 = 23$. $\E[X^2] = 100(0.2)+400(0.4)+900(0.3)+1600(0.1) = 20+160+270+160 = 610$. $\Var(X) = 610 - 23^2 = 610 - 529 = 81$ (so $\SD = 9$).

**C3.10** — *(standard) Linear transform of mean & variance (Entries №04, №06).* $\E[Y] = 1.5(51)+10 = 76.5+10 = 86.5$. $\Var(Y) = 1.5^2(379) = 2.25(379) = 852.75$. The $+10$ leaves the variance untouched.

**C3.11** — *(standard) Moments from an MGF (Entry №07).* $M_X'(t) = 0.4e^t + 0.6e^{2t} \Rightarrow \E[X] = 0.4+0.6 = 1.0$. $M_X''(t) = 0.4e^t + 1.2e^{2t} \Rightarrow \E[X^2] = 0.4+1.2 = 1.6$. $\Var(X) = 1.6 - 1.0^2 = 0.6$. *(Cross-check: pmf $p(0)=0.3,p(1)=0.4,p(2)=0.3$ from the $e^{kt}$ coefficients gives the same.)*

**C3.12** — *(rival_trap) Variance needs $-(\E[X])^2$ (Entry №06).* $\E[X] = 0(0.5)+1(0.3)+2(0.2) = 0.7$. $\E[X^2] = 0+0.3+4(0.2) = 1.1$. True $\Var(X) = 1.1 - 0.7^2 = 1.1 - 0.49 = 0.61$. **Gary is wrong:** he quoted the *second moment* $\E[X^2]=1.1$ as the variance, forgetting to subtract $(\E[X])^2 = 0.49$. (This is also the error Team Rocket commits in Beat 4.)

**C3.13** — *(standard) Median and percentile from the cdf (Entry №03).* cdf: $F(1)=0.1,F(2)=0.3,F(3)=0.7,F(4)=0.9,F(5)=1.0$. Median $= \min\{k:F(k)\ge 0.5\} = 3$. $90$th percentile $= \min\{k:F(k)\ge 0.90\} = 4$ ($F(4)=0.90$).

**C3.14** — *(audit) Survival sum starts at $S(0)$ (Entry №05).* True $\E[N] = S(0)+S(1)+S(2)+S(3) = 0.5+0.3+0.1+0 = 0.9$. **Meowth's error:** he dropped the first term $S(0)=0.5$, summing only from $S(1)$. $S(0)=P(N>0)$ counts and must be included; his $0.4$ undercounts the mean.

**C3.15** — *(standard) LOTUS on a nonlinear function (Entry №04).* $\E[g(X)] = \sum g(k)p(k)$ with $g(k)=k^2+2$: $g(1)=3,g(2)=6,g(3)=11$. $\E[g(X)] = 3(0.5)+6(0.3)+11(0.2) = 1.5+1.8+2.2 = 5.5$. *(Equivalently $\E[X^2]+2 = 3.5+2 = 5.5$.)*

**C3.16** — *(standard) Coefficient of variation comparison (Entry №06).* $\mathrm{CV}_A = 5/50 = 0.10$; $\mathrm{CV}_B = 1.2/8 = 0.15$. Reactor **A** is *relatively* more reliable (smaller CV) — even though both have spread, A's swing is a smaller fraction of its mean.

**C3.17** — *(standard) Mode, median, mean of one table (Entries №03, №04).* Mode: two tallest bars tie at $0.4$, so **bimodal**, modes $1$ and $4$. cdf $F(1)=0.4,F(2)=0.5,F(3)=0.6,F(4)=1.0$; median $= \min\{k:F\ge 0.5\} = 2$. Mean $= 1(0.4)+2(0.1)+3(0.1)+4(0.4) = 0.4+0.2+0.3+1.6 = 2.5$. They do **not** coincide — three different summaries.

**C3.18** — *(rival_trap) Discrete uniform on the wrong support (Discrete Uniform entry).* The support is $\{0,1,\dots,9\}$ — that's $10$ equally likely values, *not* $\{1,\dots,9\}$. True $\E[X] = \tfrac{0+9}{2} = 4.5$ (the midpoint of $0$ to $9$). **Gary's error:** he plugged $n=9$ into $\tfrac{n+1}{2}$, but the formula $\tfrac{n+1}{2}$ is for support $\{1,\dots,n\}$. With a $0$-start, the mean is the midpoint $\tfrac{0+9}{2}=4.5$, not $5$.

**C3.19** — *(decision) Expected revenue, two billing options (Entry №04).* Option A: flat $\$8$ per cabin $\Rightarrow$ expected revenue $= \$8$. Option B: $\$3$ per Pokémon $\Rightarrow$ expected revenue $= 3\,\E[X] = 3(2.95) = \$8.85$. **Option B yields more on average** ($8.85 > 8$); the per-Pokémon plan wins because the average party exceeds $8/3 \approx 2.67$. Same crowd, two framings, one expectation calculation.

**C3.20** — *(standard) Survival mean + variance via recovered pmf (Entries №05, №06).* Survival mean: $\E[N] = 0.6+0.3+0.1+0 = 1.0$. Recover pmf with $p(k)=S(k-1)-S(k)$, $S(-1)=1$: $p(0)=1-0.6=0.4$, $p(1)=0.6-0.3=0.3$, $p(2)=0.3-0.1=0.2$, $p(3)=0.1-0=0.1$. $\E[N^2] = 0+1(0.3)+4(0.2)+9(0.1) = 0.3+0.8+0.9 = 2.0$. $\Var(N) = 2.0 - 1.0^2 = 1.0$.

**C3.21** — *(standard) Identify a distribution from its MGF (Entry №07, Discrete Uniform entry).* $M_X(t) = \tfrac14(e^t+e^{2t}+e^{3t}+e^{4t}) = \sum_{k=1}^4 \tfrac14 e^{kt}$, so $p(k)=\tfrac14$ for $k=1,2,3,4$: this is **discrete uniform on $\{1,2,3,4\}$**. $\E[X] = \tfrac{4+1}{2} = 2.5$; $\Var(X) = \tfrac{4^2-1}{12} = \tfrac{15}{12} = 1.25$.

**C3.22** — *(decision) Mean time vs. percentile time (Entries №03, №04).* cdf: $F(1)=0.1,F(2)=0.3,F(3)=0.7,F(4)=0.9,F(5)=1.0$. Mean $= 1(0.1)+2(0.2)+3(0.4)+4(0.2)+5(0.1) = 0.1+0.4+1.2+0.8+0.5 = 3.0$ min. $80$th percentile $= \min\{k:F(k)\ge 0.80\} = 4$ min ($F(4)=0.90$). The **80th-percentile promise (4 min) is safer**: by the mean time of $3$ min only $F(3)=70\%$ of decks are cleared, whereas by $4$ min $90\%$ are. They differ because the mean is a balance point pulled by the whole distribution, while a percentile guarantees a *coverage fraction* — and for evacuation safety you want coverage, not the average.

### Quick-Answer Table

| # | Answer | | # | Answer |
|---|---|---|---|---|
| C3.1 | $c=0.2$; $P(X\le1)=0.40$ | | C3.12 | $\Var=0.61$ (Gary wrong) |
| C3.2 | $\E[X]=2.1$ | | C3.13 | median $3$; 90th pct $4$ |
| C3.3 | $\E[X^2]=4.9$; $\Var=0.49$ | | C3.14 | $\E[N]=0.9$ (dropped $S(0)$) |
| C3.4 | $\bar x=3.6$; $\sigma x^2=0.84$ | | C3.15 | $\E[g(X)]=5.5$ |
| C3.5 | $F(2)=0.50$; $P=0.50$ | | C3.16 | $\mathrm{CV}_A=0.10<\mathrm{CV}_B=0.15$ |
| C3.6 | $\E[N]=1.2$ | | C3.17 | modes $1,4$; median $2$; mean $2.5$ |
| C3.7 | $\E[X]=2.95$ (not mode $3$) | | C3.18 | $\E[X]=4.5$ (Gary wrong) |
| C3.8 | $\E[X]=3.5$; $\Var=35/12$ | | C3.19 | A $\$8$, B $\$8.85$; B wins |
| C3.9 | $c=0.4$; $\E[X]=23$; $\Var=81$ | | C3.20 | $\E[N]=1.0$; $\Var=1.0$ |
| C3.10 | $\E[Y]=86.5$; $\Var=852.75$ | | C3.21 | $\Unif\{1,..,4\}$; $\E=2.5$; $\Var=1.25$ |
| C3.11 | $\E[X]=1.0$; $\Var=0.6$ | | C3.22 | mean $3$; 80th pct $4$; pct safer |
:::

## Badge Earned — the Thunder Badge

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/thunder_badge.png" alt="The Thunder Badge, an eight-pointed orange star-shaped gym badge" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Thunder Badge earned!</strong> Rank: Rookie → 2 badges.</figcaption>
</figure>

You handed Lt. Surge the spec sheet done right — power, reliability, and the boosted-shot rescale — and he pressed the Thunder Badge into your palm. The S.S. Anne's survivors are safe ashore, the galley provisioned by the *mean* and not the mode. **Rank: Rookie (2 badges).** Two down, six to go on the road to the Indigo Plateau.

**Mastery checklist — tick each before you move on (mapped 1-to-1 to the SOA outcomes):**

- ☐ **(2a — pmf/cdf/survival)** I can read and **validate** a pmf (nonnegative, sums to one), build its **cdf** by accumulating, get the **survival function** $S=1-F$, mind the strict-vs-non-strict boundary, and recover a pmf mass as a cdf jump. *(Rematch: Concepts 1–2, WE 1–2, C3.1, C3.5.)*
- ☐ **(2a — center & shape)** I can compute the **expected value** $\E[X]=\sum k\,p(k)$ and $\E[g(X)]$ (LOTUS), and find the **mode, median, and percentiles** — and I never report the mode as the mean. *(Rematch: Concepts 3–4, the Trap, C3.2, C3.7, C3.13, C3.17.)*
- ☐ **(2a/2c — survival method)** I can read a mean off a survival function with the **Darth Vader** sum $\E[X]=\sum_{k\ge0}S(k)$ for a nonnegative count, starting at $S(0)$. *(Rematch: Concept 5, WE 2, C3.6, C3.14, C3.20.)*
- ☐ **(2c — spread)** I can compute **variance, SD, and CV**, use $\Var(X)=\E[X^2]-(\E[X])^2$, and rescale with $\Var(aX+b)=a^2\Var(X)$. *(Rematch: Concept 6, the Gym Battle, C3.3, C3.10, C3.12, C3.16.)*
- ☐ **(2d — MGF)** I can use $M_X(t)=\E[e^{tX}]$ to extract moments ($\E[X^n]=M^{(n)}(0)$), read a discrete pmf off the $e^{kt}$ coefficients, and identify a distribution by uniqueness. *(Rematch: Concept 7, WE 3, C3.11, C3.21.)*
- ☐ **(2a — discrete uniform)** I can apply the **discrete uniform** with $\E[X]=\tfrac{n+1}{2}$, $\Var(X)=\tfrac{n^2-1}{12}$, after confirming the support is $\{1,\dots,n\}$. *(Rematch: Concept 8, WE 4, C3.8, C3.18, C3.21.)*
- ☐ **(calculator)** I can drive **1-Var Stats** (L1 values, L2 probabilities, FRQ$=$L2) to read $\bar x$ (mean) and $\sigma x$ (variance $=\sigma x^2$), and I read $\sigma x$, never $sx$. *(Rematch: flagship Trainer's Tip, WE 1, C3.4.)*

**Gym Rematch pointers.** Reported the mode as the mean? Re-read Concept 3 Beat 4 and the Trap, then redo C3.7. Forgot $-(\E[X])^2$? Concept 6 Beat 4, then C3.12. Dropped $S(0)$ in a survival sum? Concept 5 Beat 4, then C3.14. Mis-applied the uniform formula? Concept 8 Beat 4, then C3.18.

> Next stop: **Viridian Forest and Pewter City**, where the swarm is too vast to list and you'll learn to *count by rule* — permutations, combinations, and the first named distributions (binomial, hypergeometric). Pack the mean and variance machinery: every distribution there is this chapter with a specific pmf plugged in.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
