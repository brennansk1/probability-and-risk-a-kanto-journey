<!--
  file: ch13_covariance
  tier: A
  outcomes: 3e,3g,3h
  draft1_source: drafts/chapters_draft1/ch11_victory_road.md
  maps_to: Victory Road — the team combines
-->

# Combining Forces {.type-normal}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with the route to Victory Road highlighted; every badge so far is collected and the path now climbs toward the Indigo Plateau." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 10 — every badge earned, you reach <strong>Victory Road</strong>, the gauntlet where the team stops being six separate Pokémon and becomes one <em>total</em>.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Climb Is a Sum"**

The cave mouth of Victory Road swallows the last of the afternoon light. No gym leader waits here, no badge — only a vertical gauntlet of boulders, strength puzzles, and wild Onix you must clear *as a team*, in one continuous push, before the Pokémon League registration window closes at dusk.

Oak's voice crackles through the Pokédex. "Ash — Victory Road isn't six battles. It's *one*. Your whole team feeds a single number: the total strength your team spends on the climb. I need that number. How strong is your team, all six combined — and, more importantly, how *reliable* is that total?"

You start adding. Pikachu's expected output, Charizard's, Bulbasaur's, the rest. The means add cleanly; that part you remember from the last chapter. Then Oak interrupts.

"Careful. Pikachu and Charizard feed off each other — when one surges, the other surges. And Bulbasaur *wilts* whenever Charizard overheats — when one is up, the other is down. Their efforts are *linked*. If you compute the spread of the team total as though everyone climbed alone, your estimate of whether the team holds together on this cliff will simply be wrong."

Pikachu's ears flatten. It senses the trap before you do: you were about to add up the variances and call it a day.

Misty leans in. "So the team's reliability isn't just the sum of each Pokémon's reliability?"

"No," Oak says. "When teammates move *together*, the total swings **more** than the parts suggest. When they move **against** each other, the total is **steadier** than the parts suggest. There is a cross-term hiding in there. Miss it, and your read on whether the team survives the climb is off — maybe dangerously."

You look up the dark slope. Six Pokémon, six variances, and a tangle of who-moves-with-whom. You can find the expected total easily. But the *spread* of that total — the thing that decides whether you reach the Plateau or collapse on a ledge — depends on something you have not yet named.

*How do you measure the way two teammates move together, and fold it into the reliability of the whole team?*
:::

## Where You Are — 60-Second Retrieval

You arrive at Victory Road carrying everything from the joint-distribution chapter and the double-expectation chapter. Two ideas from back there are the ground this chapter stands on.

First, **expectation is linear, always** — no conditions, no fine print:

$$\E[aX + bY + c] = a\,\E[X] + b\,\E[Y] + c.$$

Second, **variance is *not* linear** for a single scaled variable: a constant multiplier comes out **squared**,

$$\Var(aX) = a^2\,\Var(X), \qquad \SD(aX) = |a|\,\SD(X).$$

That squaring is the seed of everything ahead: means add gently, but spreads combine on the *squared* scale. This chapter's whole job is to discover the one extra term that appears when you add the spreads of two variables that are *linked*. Take sixty seconds and prove you still own the two facts above before reading on.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the last chapters**

Answer from memory; if any feels shaky, flip back before continuing.

1. $\E[X]=4$, $\E[Y]=10$. What is $\E[2X + 3Y]$? *(Answer: $2(4)+3(10)=38$.)*
2. $\Var(X)=9$. What is $\Var(5X)$? And $\SD(5X)$? *(Answer: $25\cdot9=225$; $\SD=5\cdot3=15$.)*
3. For a $0/1$ indicator $X$ with $P(X=1)=0.6$, what is $\E[X]$, and what is $\E[X^2]$? *(Answer: both $0.6$ — since $0^2=0$ and $1^2=1$, an indicator equals its own square.)*

All three instant? You're ready. Any hesitation? The retrieval *is* the lesson — go reclaim it, then come back.
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice steadies through the Pokédex's Actuary Mode as you stare up the slope.

"Victory Road is where individuals become a *portfolio*, Ash. Up to now you've studied one random variable at a time. From here on, the question is always about a **total** — a sum of many linked variables — and the entire game is getting its *spread* right. Master this and you can price the risk of an insurer's whole book of policies, not just one. This is the last Tier-A climb before the League."

By the end of this chapter you will be able to:

- **Compute covariance** $\Cov(X,Y) = \E[XY] - \E[X]\E[Y]$ for discrete and continuous pairs, and exploit its **bilinearity**. *(Outcome 3e.)*
- **Compute the correlation coefficient** $\rho$, interpret its sign and magnitude, and explain precisely why independence forces $\rho = 0$ while $\rho = 0$ does **not** force independence. *(Outcome 3e.)*
- **Find the variance of a sum or general linear combination** $\Var\!\big(\sum a_i X_i\big)$, including every $2a_i a_j \Cov(X_i,X_j)$ cross-term with the right sign. *(Outcome 3g.)*
- **Compute moments — mean and variance — of linear combinations** of random variables, including the independent and normal special cases. *(Outcome 3h.)*
- **Recognize sums of independent in-family distributions** (Normal+Normal, Poisson+Poisson, same-scale Gamma+Gamma, same-$p$ Binomial+Binomial) and combine them via the **MGF method**. *(Outcome 3h.)*

> *Exam-weight signpost.* Covariance, variance of sums, and sums of independent variables sit squarely in Exam P's **Multivariate** block (≈23–30% of the exam), and the variance-of-a-sum rule is one of the single most-tested computations on the test. This is a **Tier A** chapter — full treatment, full ramp.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own All of Victory Road?**

Already fluent? Prove it. Work these five, ~3 minutes each, *with correct method*:

1. $\E[X]=3$, $\E[Y]=5$, $\E[XY]=16$. Find $\Cov(X,Y)$.
2. $\SD(U)=5$, $\SD(V)=12$, $\rho=0.4$. Find $\Cov(U,V)$.
3. $\Var(X)=4$, $\Var(Y)=9$, $\Cov(X,Y)=2$. Find $\Var(X+Y)$ and $\Var(X-Y)$.
4. $X\sim\Normal(10,4)$ and $Y\sim\Normal(6,9)$ independent (variances given). Name the exact distribution of $X-Y$.
5. Independent $X\sim\Poisson(1.5)$ and $Y\sim\Poisson(2.5)$. Name the exact distribution of $X+Y$.

*(Answers: $1$; $24$; $\Var(X{+}Y)=17$, $\Var(X{-}Y)=9$; $\Normal(4,13)$; $\Poisson(4)$.)* Five for five with correct reasoning? **Skip to the Gym Challenge** and claim the medallion. Any miss or hesitation? The teaching below was built exactly for you — and each concept has its own skip-gate, so even a partial owner loses no time.
:::

---

Five ideas build on one another here, in increasing difficulty. We teach them **in order**, each with its own "do you already own this?" skip-check, then the full nine-beat lesson, then a Pokédex Entry you can carry into the exam:

1. **Covariance** — a single number for how two variables move together *(the foundation everything else uses)*
2. **Correlation** — covariance rescaled onto a fixed $-1$-to-$+1$ ruler
3. **Variance of a sum / linear combination** — the cross-term rule *(the load-bearing climb)*
4. **Independence vs. zero correlation** — and the one-way street between them
5. **Sums of independent in-family distributions** — pooling parameters with the MGF

## Concept 1 — Covariance: A Number for Moving Together

::: concept-gate
**DO YOU ALREADY OWN THIS? — Covariance**

Misty reports that her Staryu's spin-count $X$ and her Starmie's spin-count $Y$ satisfy $\E[X]=3$, $\E[Y]=5$, and $\E[XY]=16$. What is $\Cov(X,Y)$, and do the two spin *together* or *against* each other?

If you immediately answered **$\Cov(X,Y)=16-(3)(5)=1>0$, "together,"** you own covariance — **skip to Concept 2**. If $\E[XY]-\E[X]\E[Y]$ wasn't your first move, or the sign's meaning is fuzzy, this section is for you.
:::

**Beat 1 — The one-sentence idea.** *Covariance is the average of "how far above its mean $X$ is" times "how far above its mean $Y$ is" — one number that is positive when the two tend to rise and fall together, and negative when one rises as the other falls.*

**Beat 2 — Anchor + concrete instance.** You already know **variance**: the average squared distance of a *single* variable from its own mean, $\Var(X)=\E[(X-\mu_X)^2]$. Covariance is the natural next step — instead of multiplying $X$'s deviation by *itself*, multiply it by $Y$'s deviation. Here is the story, with real numbers small enough to do by hand.

On the first ledge, two things happen on each attempt: $X$ = the number of boulders Pikachu must Iron-Tail aside (either $0$ or $1$), and $Y$ = the number of wild Onix that emerge (either $0$ or $1$). The cave's RNG produces this joint table over many attempts:

| $p(x,y)$ | $y=0$ | $y=1$ |
|---|---|---|
| $x=0$ | $0.30$ | $0.10$ |
| $x=1$ | $0.20$ | $0.40$ |

*Do boulders and Onix tend to appear together?* Look at the table: the big $0.40$ sits in the "both $=1$" corner. That hints "together" — but we want a *number*.

**Beat 3 — Reason through it in plain words.** $X$ is high (equal to $1$) exactly when there are boulders; $Y$ is high exactly when Onix emerge. If boulders and Onix tend to show up on the *same* attempts, then whenever $X$ is above its average, $Y$ is *also* above its average — both deviations have the same sign, so their **product is positive**. Average those products over all attempts and you get a positive number: they move together. If instead Onix only showed up when there were *no* boulders, $X$ above average would pair with $Y$ below average — opposite signs, **negative product**, negative average. Covariance is exactly that average product of deviations.

Let's get the pieces. The marginal chance $X=1$ is $0.20+0.40=0.60$, so $\E[X]=0.60$. The chance $Y=1$ is $0.10+0.40=0.50$, so $\E[Y]=0.50$. Now $\E[XY]$: the product $XY$ is $1$ only in the both-equal-$1$ cell and $0$ everywhere else, so

$$\E[XY] = (1)(1)(0.40) = 0.40.$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** The seductive shortcut is to compute $\E[XY]$ by multiplying the two means:

$$\E[XY] \overset{?}{=} \E[X]\,\E[Y] = (0.60)(0.50) = 0.30. \qquad\textbf{(wrong, in general)}$$

But $\E[XY]=\E[X]\E[Y]$ holds **only when the two variables are unrelated** — it is the *thing covariance measures the failure of*. Here the true $\E[XY]=0.40$, not $0.30$. That **gap of $0.10$** between "what $\E[XY]$ actually is" and "what it would be if they ignored each other" is precisely the co-movement. Assuming $\E[XY]=\E[X]\E[Y]$ throws away the entire phenomenon we came here to measure.

**Beat 5 — Translate into notation, one glyph at a time.** Write $\mu_X$ (read "mew-sub-$X$") for $\E[X]$, the mean of $X$, and $\mu_Y$ for $\E[Y]$. The deviation "how far above its mean $X$ is" is $X-\mu_X$. The average product of deviations gets its own name, $\Cov$ (read "**covariance** of $X$ and $Y$"):

$$\Cov(X,Y) = \E\!\big[(X-\mu_X)(Y-\mu_Y)\big] \qquad \text{read aloud: "the average of $X$'s deviation times $Y$'s deviation."}$$

That definition is honest but slow. Expand the product inside and use linearity of expectation — every step justified, nothing skipped:

$$
\E\!\big[(X-\mu_X)(Y-\mu_Y)\big]
= \E\!\big[XY - \mu_Y X - \mu_X Y + \mu_X\mu_Y\big].
$$

Pull the constants $\mu_X,\mu_Y$ out (they are just numbers) and use $\E[X]=\mu_X$, $\E[Y]=\mu_Y$:

$$
= \E[XY] - \mu_Y\,\E[X] - \mu_X\,\E[Y] + \mu_X\mu_Y
= \E[XY] - \mu_Y\mu_X - \mu_X\mu_Y + \mu_X\mu_Y
= \E[XY] - \mu_X\mu_Y.
$$

Two of the three trailing terms cancel, leaving the **computational form**:

$$\Cov(X,Y) = \E[XY] - \E[X]\,\E[Y].$$

We did not assert this — we *derived* it from the definition. And it is exactly the gap from Beat 4.

**Beat 6 — Generalize: read the answer off the instance.** Plug in our numbers:

$$\boxed{\,\Cov(X,Y) = \E[XY] - \E[X]\,\E[Y] = 0.40 - (0.60)(0.50) = 0.40 - 0.30 = 0.10.\,}$$

A positive covariance: boulders and Onix *do* tend to appear together, just as the big corner cell suggested. The formula is the compression of "average the deviation products."

**Beat 7 — Ramp the difficulty.**

- *Simplest:* read $\E[XY]$, $\E[X]$, $\E[Y]$ off a small joint table, subtract — as above.
- *Twist (covariance with itself):* set $Y=X$. Then $\Cov(X,X)=\E[X^2]-\E[X]^2 = \Var(X)$. **Variance is just covariance of a variable with itself** — the two ideas were one idea all along. And $\Cov(X,Y)=\Cov(Y,X)$, since $XY=YX$; covariance doesn't care about order.
- *Twist (continuous):* for a continuous pair the only thing that changes is how you compute $\E[XY]$ — a double integral instead of a double sum:
$$\E[XY]=\iint xy\,f(x,y)\,dx\,dy, \qquad\text{then } \Cov(X,Y)=\E[XY]-\E[X]\E[Y].$$
The subtraction step is identical.
- *Constants drop out (the rule you'll lean on constantly):* shifting a variable by a constant moves its mean by the same amount, so the deviation $X-\mu_X$ is unchanged — a constant *shift* cannot affect co-movement. A constant *multiplier* factors straight out. Together:
$$\Cov(aX+b,\;cY+d) = ac\,\Cov(X,Y).$$
The $+b$ and $+d$ vanish; the $a$ and $c$ survive. (Derived in full in Worked Example 13.1's pitfall note.)

**Beat 8 — Picture it.** A figure makes "moving together" literal: each dot is one attempt, plotted at its $(X,Y)$. An up-sloping cloud means positive covariance; a down-sloping cloud, negative; a shapeless blob, near zero.

<figure>
<img src="../../assets/diagrams/ch11_correlation_scatter.png" alt="Three scatterplots of two Pokemon's per-climb outputs. Left: an up-sloping cloud where high X pairs with high Y (positive covariance). Middle: a circular shapeless cloud with no slope (covariance near zero). Right: a down-sloping cloud where high X pairs with low Y (negative covariance). Dashed crosshairs mark each variable's mean, dividing the plane into four quadrants; dots in the upper-right and lower-left quadrants contribute positive deviation-products, dots in the other two contribute negative." style="width:90%; max-width:560px; display:block; margin:1em auto;">
<figcaption>Covariance is the average of (deviation in $X$) × (deviation in $Y$). Dots in the upper-right and lower-left quadrants (both deviations same sign) push covariance up; the other two quadrants push it down. Left $\to$ positive, middle $\to$ ≈ zero, right $\to$ negative.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now turn any joint table or density — or just a given $\E[XY]$ — into one number that says whether two variables move together (positive), against (negative), or neither (zero), and you know that variance is the special case $\Cov(X,X)$.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Covariance**

$$\Cov(X,Y) = \E\!\big[(X-\mu_X)(Y-\mu_Y)\big] = \E[XY] - \E[X]\,\E[Y].$$

Special cases and rules:

$$\Cov(X,X) = \Var(X), \qquad \Cov(X,Y)=\Cov(Y,X), \qquad \Cov(aX+b,\;cY+d) = ac\,\Cov(X,Y).$$

*In plain terms:* the average of "$X$'s distance above its mean" times "$Y$'s distance above its mean." Positive ⇒ they tend to be high together (and low together); negative ⇒ one is high when the other is low; the size has units of $X$ times $Y$, so it is **not** yet on a fixed scale (Concept 2 fixes that).

*Why the computational form is faster:* $\E[XY]-\E[X]\E[Y]$ needs only three numbers; the definition needs the full deviation of every outcome.

*Recognition cue:* a problem hands you a **joint table**, a **joint density**, or the product moment $\E[XY]$ — or asks for the variance of a sum of *dependent* variables. Reach for $\Cov(X,Y)=\E[XY]-\E[X]\E[Y]$.
:::

## Concept 2 — Correlation: Covariance on a Fixed Ruler

::: concept-gate
**DO YOU ALREADY OWN THIS? — Correlation**

Brock measures Geodude's output $U$ ($\SD=5$) and Onix's output $V$ ($\SD=12$) and finds $\Cov(U,V)=24$. What is the correlation $\rho_{U,V}$?

If you answered **$\rho=\dfrac{24}{5\cdot 12}=0.4$** and can say *why $\rho$ has no units while covariance does*, **skip to Concept 3**. If covariance and correlation feel like the same thing, read on — the rescaling is the whole point.
:::

**Beat 1 — The one-sentence idea.** *Correlation is covariance divided by the two standard deviations, which strips away the units and pins the answer onto a fixed ruler from $-1$ to $+1$ — so you can read off the strength and direction of the linear link at a glance.*

**Beat 2 — Anchor + concrete instance.** Covariance (Concept 1) has a flaw: its size is meaningless on its own. A covariance of $24$ between two huge variables might be a *weak* link; between two tiny variables, a *strong* one. We need to standardize — exactly the trick you used to standardize a normal into a $Z$-score, but for co-movement.

Brock measures **Geodude's output $U$** with $\SD(U)=5$ and **Onix's output $V$** with $\SD(V)=12$, and finds their covariance is $\Cov(U,V)=24$. *Is that a strong link or a weak one?* The bare $24$ can't say.

**Beat 3 — Reason through it in plain words.** The largest covariance two variables *can* possibly have is the product of their standard deviations, $\SD(U)\SD(V)$ — that maximum is achieved only when one is an exact increasing linear function of the other. So divide the actual covariance by that maximum, and you get a pure fraction telling you *what share of the strongest-possible link* is present:

$$\frac{\Cov(U,V)}{\SD(U)\,\SD(V)} = \frac{24}{(5)(12)} = \frac{24}{60} = 0.4.$$

So this link is $40\%$ of the way to a perfect straight-line relationship, and positive. The units of $U$ and $V$ canceled top against bottom — the answer is a clean, unit-free number.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is to compare *covariances directly* across problems: "this pair has $\Cov=24$ and that pair has $\Cov=3$, so the first is eight times more strongly linked." **Wrong** — covariance carries the units of $X\times Y$, so re-scaling either variable (say, measuring output in different units) rescales the covariance without changing the relationship one bit. Only **correlation**, which divides those units out, lets you compare strengths across different pairs. Covariance tells you the *sign*; correlation tells you the *strength*.

**Beat 5 — Translate into notation, one glyph at a time.** The standardized covariance gets the Greek letter $\rho$ (read "**rho**"), and the name **correlation coefficient**:

$$\rho_{X,Y} = \Corr(X,Y) = \frac{\Cov(X,Y)}{\SD(X)\,\SD(Y)} = \frac{\Cov(X,Y)}{\sqrt{\Var(X)\,\Var(Y)}}, \qquad -1 \le \rho \le 1.$$

The subscript names the pair; $\Corr(X,Y)$ and $\rho_{X,Y}$ are the same thing read two ways. Because both the top (covariance) and the units in the bottom rescale identically when you stretch a variable, $\rho$ is **scale-free**:

$$\Corr(aX+b,\;cY+d) = \operatorname{sign}(ac)\,\rho_{X,Y}.$$

Stretching or shifting a variable cannot change the strength of its linear link; it can only flip the *sign* if a multiplier is negative.

**Beat 6 — Derive the bounds.** Why must $\rho$ live in $[-1,1]$? Consider the variance of the standardized sum $\dfrac{X-\mu_X}{\SD(X)} + \dfrac{Y-\mu_Y}{\SD(Y)}$. Each standardized piece has variance $1$, and (jumping ahead one concept) the variance of their sum is $1 + 1 + 2\rho = 2 + 2\rho$. A variance can never be negative, so $2+2\rho \ge 0$, giving $\rho \ge -1$. Repeat with a *difference* instead of a sum and you get $2 - 2\rho \ge 0$, i.e. $\rho \le 1$. The bounds aren't a convention — they fall straight out of "variance is never negative."

**Beat 7 — Ramp the difficulty.**

- *Simplest:* divide a given covariance by the two SDs — Brock's $0.4$.
- *Run it backward (the most common exam move):* you are *given* $\rho$ and the two SDs and asked to recover the covariance. Just multiply:
$$\Cov(X,Y) = \rho\,\SD(X)\,\SD(Y).$$
Many problems hide the covariance behind a stated correlation — this is how you unlock it.
- *Endpoints:* $\rho=+1$ means $Y$ is an exactly *increasing* linear function of $X$; $\rho=-1$, exactly *decreasing*; $\rho=0$ means *no linear* association (but, foreshadowing Concept 4, **not** necessarily "no relationship").

**Beat 8 — Picture it.** Reuse the three scatterplots from Concept 1, now labeled with $\rho$: a tight up-sloping line is $\rho\approx+0.9$; a round blob is $\rho\approx 0$; a tight down-sloping line is $\rho\approx -0.9$. Correlation is, visually, *how close the cloud hugs a straight line*, with sign for the slope.

**Beat 9 — Consolidate.** You can now convert covariance to a unit-free strength on the $[-1,1]$ ruler, read its sign and magnitude, and — crucially — recover a hidden covariance from a stated $\rho$ and two SDs.

::: pokedex-entry
**POKÉDEX ENTRY №02 — Correlation Coefficient**

$$\rho_{X,Y} = \Corr(X,Y) = \frac{\Cov(X,Y)}{\SD(X)\,\SD(Y)} = \frac{\Cov(X,Y)}{\sqrt{\Var(X)\,\Var(Y)}}, \qquad -1 \le \rho \le 1.$$

Recover covariance from a given correlation: $\;\Cov(X,Y) = \rho\,\SD(X)\,\SD(Y).$ Scale-free: $\Corr(aX+b,\,cY+d)=\operatorname{sign}(ac)\,\rho_{X,Y}$.

*In plain terms:* correlation is covariance rescaled to live in $[-1,1]$, measuring the **strength and direction** of the *linear* relationship without units. $+1$ = perfectly increasing line, $-1$ = perfectly decreasing line, $0$ = no linear link.

*Recognition cue:* the word **"correlation,"** a given $\rho$, or "how strongly are they related on a $-1$-to-$1$ scale." If you're *given* $\rho$ and two SDs, immediately recover $\Cov=\rho\,\SD_X\,\SD_Y$ — that is almost always the next step.
:::

## Concept 3 — Variance of a Sum: The Cross-Term Rule

*This is the load-bearing climb of the chapter — the single most-tested computation, and the one Oak warned you about in the cave. We give it the full Professor's-Path-first treatment.*

::: concept-gate
**DO YOU ALREADY OWN THIS? — Variance of a Sum**

Charizard's output $X$ has $\Var(X)=9$; Bulbasaur's $Y$ has $\Var(Y)=4$. They are **negatively** correlated, $\rho=-0.5$. Find $\Var(X+Y)$ and $\Var(X-Y)$.

If you answered **$\Var(X+Y)=7$ and $\Var(X-Y)=19$** — first converting $\rho$ to $\Cov=-0.5\cdot3\cdot2=-3$, then applying $\Var\pm 2\Cov$ — **skip to Concept 4**. If you got $13$ for both (forgetting the cross-term) or added the standard deviations, this is the most important section in the chapter for you.
:::

**Beat 1 — The one-sentence idea.** *The spread of a total is the sum of the individual spreads **plus** a cross-term for every pair — twice their covariance — so linked variables make the total either wilder (if they move together) or steadier (if they move apart).*

**Beat 2 — Anchor + concrete instance.** You know $\Var(aX)=a^2\Var(X)$ for *one* variable (the retrieval at the top). Now there are two, and the question is what extra appears. This is the cave problem made concrete.

**Charizard's output $X$** has $\Var(X)=9$; **Bulbasaur's output $Y$** has $\Var(Y)=4$. Because Bulbasaur wilts whenever Charizard overheats, they are **negatively** correlated with $\rho=-0.5$. Oak wants the variance of the combined push $T=X+Y$, and — for comparison — the variance of the "tag-out swing" $D=X-Y$.

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/front/6.png" alt="Charizard" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#006 Charizard — output $X$, $\Var(X)=9$</strong></figcaption>
</figure>

**Beat 3 — Reason through it in plain words.** First convert the correlation to a covariance (Entry №02): $\Cov(X,Y)=\rho\,\SD(X)\,\SD(Y)=(-0.5)(3)(2)=-3$. Now, *if the two were unrelated*, the spreads would just add: $9+4=13$. But they're **negatively** linked — when Charizard surges, Bulbasaur tends to sag, so the two partly *cancel* each other in the total. That cancellation makes the **sum steadier** than $13$. Conversely, in the *difference* $X-Y$, the negative link makes the two pull *apart* harder, so the **difference is wilder** than $13$. The cross-term has to carry that information, and it does: it's $2\Cov$ for a sum, $-2\Cov$ for a difference.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two traps live here, and they are the most punished errors on the topic.

*Trap 1 — "variances just add."*
$$\Var(X+Y) \overset{?}{=} \Var(X)+\Var(Y) = 13. \qquad\textbf{(wrong unless uncorrelated)}$$
That is right *only* when $\Cov=0$. Here $\Cov=-3$, so the truth is $13 + 2(-3) = 7$ — the negative link shrinks the spread. Dropping the cross-term silently assumes independence you were never given.

*Trap 2 — "add the standard deviations."* Some reach for $\SD(X)+\SD(Y)=3+2=5$, then square to $25$. **Standard deviations never add.** Variances combine (plus the cross-term); you take the square root only at the very end. Adding SDs has no theoretical basis at all.

**Beat 5 — Translate into notation, one glyph at a time.** We want $\Var(X+Y)$, read "the variance of the sum." Start from the one true definition — variance is covariance with itself (Entry №01, Beat 7) — and let covariance's **bilinearity** do the work. Bilinearity just means covariance distributes over sums, like multiplying out $(a+b)(c+d)$:

$$\Cov(X+Y,\;X+Y) = \Cov(X,X) + \Cov(X,Y) + \Cov(Y,X) + \Cov(Y,Y).$$

Read it as "FOIL for covariance": every term on the left pairs with every term on the right.

**Beat 6 — Derive the formula.** Now translate each piece back. $\Cov(X+Y,X+Y)$ *is* $\Var(X+Y)$. On the right, $\Cov(X,X)=\Var(X)$, $\Cov(Y,Y)=\Var(Y)$, and the two middle terms are equal ($\Cov(X,Y)=\Cov(Y,X)$), so they combine into $2\Cov(X,Y)$:

$$\boxed{\,\Var(X+Y) = \Var(X) + \Var(Y) + 2\,\Cov(X,Y).\,}$$

For the difference, replace $Y$ with $-Y$; since $\Cov(X,-Y)=-\Cov(X,Y)$ and $\Var(-Y)=\Var(Y)$, only the cross-term flips sign:

$$\Var(X-Y) = \Var(X) + \Var(Y) - 2\,\Cov(X,Y).$$

**The individual variances still *add* in a difference** — only the cross-term changes sign. This is the single most-missed detail on the topic; burn it in.

Now finish the concrete case:

$$\Var(T)=\Var(X+Y)=9+4+2(-3)=7, \qquad \Var(D)=\Var(X-Y)=9+4-2(-3)=19.$$

Exactly the intuition from Beat 3: the negative link makes the **sum steadier** ($7<13$) and the **difference wilder** ($19>13$).

**Beat 7 — Ramp the difficulty.**

- *Simplest:* two variables, $\Var(X)+\Var(Y)\pm 2\Cov$, as above.
- *Weighted combination:* coefficients $a,b$ come out **squared** on the variances and as the product $ab$ (times $2$) on the cross-term:
$$\Var(aX+bY)=a^2\Var(X)+b^2\Var(Y)+2ab\,\Cov(X,Y).$$
- *General $n$-variable form (the one to memorize):* one squared-weight term per variable, plus one cross-term per *pair*:
$$\Var\!\Big(\sum_{i=1}^{n} a_i X_i\Big) = \sum_{i=1}^{n} a_i^2\,\Var(X_i) \;+\; 2\!\!\sum_{1\le i<j\le n}\!\! a_i a_j\,\Cov(X_i,X_j).$$
The $i<j$ under the second sum means "each unordered pair once"; the factor of $2$ accounts for $\Cov(X_i,X_j)$ and $\Cov(X_j,X_i)$ being equal. For $n=3$ there are three pairs: $(1,2),(1,3),(2,3)$.
- *Edge / sanity:* if **all** pairs are uncorrelated, every cross-term vanishes and variance adds cleanly — $\Var(\sum a_iX_i)=\sum a_i^2\Var(X_i)$. That clean rule is the *special case*, not the default.

**Beat 8 — Picture it: the variance grid.** Lay the variables along both axes of a grid. The formula is "sum every cell." The $n$ diagonal cells are the variances; the off-diagonal cells are the covariances, and because the grid is symmetric, each covariance appears **twice** — that's where the factor of $2$ comes from.

<figure>
<img src="../../assets/diagrams/ch13_variance_grid.png" alt="A 3-by-3 grid with rows and columns both labeled a1X1, a2X2, a3X3. The three diagonal cells are shaded one color and hold a1^2 Var(X1), a2^2 Var(X2), a3^2 Var(X3). The six off-diagonal cells are shaded a second color and hold the products a_i a_j Cov(X_i, X_j); the grid is symmetric across the diagonal, so each of the three distinct covariance products appears in two mirror-image cells, visually explaining the factor of 2 in the variance-of-a-sum formula." style="width:78%; max-width:520px; display:block; margin:1em auto;">
<figcaption>$\Var(\sum a_iX_i)$ is the sum of every cell in this grid: $n$ diagonal variance cells plus pairs of mirror-image covariance cells. Each distinct covariance appears twice — that is the factor of $2$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now find the variance of any sum, difference, or weighted blend of random variables, getting every cross-term and its sign right — and you will never again add standard deviations or silently drop a covariance.

::: pokedex-entry
**POKÉDEX ENTRY №03 — Variance of a Sum / Linear Combination**

Two variables:
$$\Var(X+Y) = \Var(X) + \Var(Y) + 2\,\Cov(X,Y), \qquad \Var(X-Y) = \Var(X) + \Var(Y) - 2\,\Cov(X,Y).$$

General linear combination:
$$\Var\!\Big(\sum_{i=1}^{n} a_i X_i\Big) = \sum_{i=1}^{n} a_i^2\,\Var(X_i) + 2\!\!\sum_{1\le i<j\le n}\!\! a_i a_j\,\Cov(X_i,X_j).$$

Mean (always clean, no covariance term ever): $\;\E\!\big[\sum a_i X_i + b\big] = \sum a_i\,\E[X_i] + b.$

*In plain terms:* the spread of a total is **not** just the sum of spreads — there's a cross-term per pair. Positive covariance inflates the total's variance; negative covariance shrinks it. A difference still **adds** the variances; only the cross-term flips sign. Weights enter **squared** on variances, as $2a_ia_j$ on cross-terms.

*Recognition cue:* any **sum, difference, or weighted blend** of random variables whose variance you need. Write the cross-terms first, then ask "are these independent?" — only then do you get to delete them.
:::

## Concept 4 — Independence vs. Zero Correlation (the One-Way Street)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Independence and Correlation**

$X$ is uniform on $\{-1,0,1\}$ (each with probability $\tfrac13$) and $Y=X^2$. Is $\Cov(X,Y)=0$? Are $X$ and $Y$ independent?

If you answered **"$\Cov=0$, yet they are *not* independent"** — and can explain why correlation misses the link — **skip to Concept 5**. If "$\rho=0$" made you say "independent," this section dismantles exactly that error.
:::

**Beat 1 — The one-sentence idea.** *Independence always forces correlation to zero, but zero correlation does not force independence — because correlation only detects **linear** co-movement and is blind to curved relationships.*

**Beat 2 — Anchor + concrete instance.** From Concept 3 you saw that uncorrelated variables let variance add cleanly. The natural assumption is "uncorrelated = unrelated = independent." It's half-right, and the wrong half is a classic exam trap.

Let $X$ be uniform on $\{-1,0,1\}$, each value with probability $\tfrac13$, and let $Y=X^2$. So $Y=1$ when $X=\pm1$ and $Y=0$ when $X=0$. *These are about as dependent as two variables get — $Y$ is a deterministic function of $X$.* Yet watch what correlation says.

**Beat 3 — Reason through it in plain words.** $X$ is symmetric about $0$, so $\E[X]=\tfrac13(-1+0+1)=0$. Now $\E[XY]=\E[X\cdot X^2]=\E[X^3]=\tfrac13\big((-1)^3+0^3+1^3\big)=\tfrac13(-1+0+1)=0$. Therefore

$$\Cov(X,Y)=\E[XY]-\E[X]\E[Y]=0-(0)\E[Y]=0, \quad\text{so}\quad \rho=0.$$

Zero correlation. But independence would require $P(X=0,\,Y=1)=P(X=0)\,P(Y=1)$. The left side is **$0$** (if $X=0$ then $Y=0\ne1$), while the right side is $P(X=0)\,P(Y=1)=\tfrac13\cdot\tfrac23=\tfrac29\ne0$. They are **not** independent — in fact knowing $X$ tells you $Y$ exactly. Correlation simply couldn't see it: the relationship is a symmetric parabola, perfectly *curved*, with no straight-line tilt for $\rho$ to detect.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap:

$$\rho = 0 \overset{?}{\Longrightarrow} X,Y \text{ independent}. \qquad\textbf{(wrong)}$$

Correlation is a *linear* detector. A relationship that goes up then down (like $Y=X^2$) has no net tilt, so $\rho=0$ — yet the variables are tightly linked. The implication runs **one way only**:

$$X \perp Y \;\Longrightarrow\; \Cov(X,Y)=0 \;\Longrightarrow\; \rho=0, \qquad\text{but } \rho=0 \;\not\Longrightarrow\; X\perp Y.$$

(The symbol $\perp$, read "is independent of," means knowing one tells you nothing about the other.) The *forward* direction is true and useful; the *converse* is the trap.

**Beat 5 — Translate into notation, and prove the forward direction.** Why does independence force $\Cov=0$? Because independence is exactly the statement that the joint factors, which makes $\E[XY]=\E[X]\E[Y]$:

$$\E[XY]=\iint xy\,f(x,y)\,dx\,dy = \iint xy\,f_X(x)f_Y(y)\,dx\,dy = \Big(\int x f_X(x)dx\Big)\Big(\int y f_Y(y)dy\Big)=\E[X]\E[Y].$$

(The middle step used independence: $f(x,y)=f_X(x)f_Y(y)$.) Then $\Cov(X,Y)=\E[XY]-\E[X]\E[Y]=0$. So independence ⇒ zero covariance ⇒ zero correlation, always.

**Beat 6 — Why the converse fails (the structural reason).** Covariance is built from the product moment $\E[XY]$, which weights the relationship by $x\cdot y$ — a *linear* quantity in each variable. Any dependence whose "ups" and "downs" cancel under that linear weighting (like a function symmetric about $X$'s mean) leaves $\E[XY]=\E[X]\E[Y]$ untouched. Independence is a statement about *every* joint probability; correlation is a statement about *one linear average*. The first is far stronger, so it implies the second — never the reverse.

**Beat 7 — Ramp the difficulty.**

- *Simplest (forward):* told "independent," instantly set every covariance term to $0$ and let variances add cleanly. This is a *license to delete*.
- *The canonical counterexample:* $Y=X^2$ with $X$ symmetric about $0$ — memorize it; it is the standard exam illustration that $\rho=0\not\Rightarrow$ independence.
- *Edge:* the **normal** family is the famous exception where the implication *does* go both ways — for *jointly normal* $X,Y$, $\rho=0$ **does** imply independence. (That equivalence is special to joint normality; never assume it elsewhere.)

**Beat 8 — Picture it.** Reuse the middle scatterplot from Concept 1 — a round, sloping-nowhere blob — and overlay the $Y=X^2$ parabola: a perfect upside-down-free curve through $(-1,1),(0,0),(1,1)$. Both have $\rho=0$; one is genuinely unrelated, the other is a deterministic curve. Correlation can't tell them apart.

**Beat 9 — Consolidate.** You can now use independence as a license to delete every covariance term, *and* you will never run that street backward — $\rho=0$ alone never licenses "independent."

::: pokedex-entry
**POKÉDEX ENTRY №04 — Independence vs. Zero Correlation (the one-way street)**

$$X \perp Y \;\Longrightarrow\; \Cov(X,Y)=0 \;\Longrightarrow\; \rho=0, \qquad\text{but } \rho=0 \;\not\Longrightarrow\; X\perp Y.$$

*In plain terms:* independent variables are *always* uncorrelated (because $\E[XY]=\E[X]\E[Y]$). But uncorrelated variables can still be dependent — $\rho$ only sees *linear* association, so a purely curved link (e.g. $Y=X^2$ with $X$ symmetric about $0$) hides from it. Exception: *jointly normal* variables, for which $\rho=0$ **does** give independence.

*Recognition cue:* "$X$ and $Y$ are independent" ⇒ delete every covariance term on sight. "Does $\rho=0$ imply independence?" ⇒ **no**, and the answer is the $Y=X^2$ counterexample.
:::

## Concept 5 — Sums That Stay in the Family (the MGF Method)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Sums of Independent In-Family Variables**

Independent $X\sim\Poisson(3)$ and $Y\sim\Poisson(2)$. Name the exact distribution of $X+Y$. And independent $X\sim\Normal(\mu_X,\sigma_X^2)$, $Y\sim\Normal(\mu_Y,\sigma_Y^2)$: name the distribution of $X-Y$.

If you answered **$\Poisson(5)$** and **$\Normal(\mu_X-\mu_Y,\;\sigma_X^2+\sigma_Y^2)$** (means subtract, variances *add*), **skip to the Worked Examples**. If you reached for a convolution sum, read on — pooling parameters is far faster.
:::

**Beat 1 — The one-sentence idea.** *When you add **independent** members of certain families, the sum is a member of the **same** family with the parameters simply pooled — so you replace a hard convolution with one parameter addition.*

**Beat 2 — Anchor + concrete instance.** You met the **moment generating function** $M_X(t)=\E[e^{tX}]$ earlier as the "DNA" that uniquely identifies a distribution. Here it does one spectacular trick: the MGF of a sum of *independent* variables is the *product* of their MGFs. That product often collapses into a recognizable family's MGF.

In the deepest chamber, **Zubat** appear independently at rate $\lambda_Z=3$ per minute and **Golbat** at rate $\lambda_G=2$ per minute, each $\Poisson$. You need the chance that *fewer than 3 bats total* appear in a given minute so you can slip past. *What is the distribution of the total $X_Z+X_G$?*

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/41.png" alt="Zubat" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#041 Zubat — arrivals $\sim\Poisson(3)$</strong></figcaption>
</figure>

**Beat 3 — Reason through it in plain words.** Both bat species arrive as Poisson processes, independently. Intuitively, "bats per minute, from any species" should *also* be Poisson, with a rate that is just the two rates added: $3+2=5$. Pooling independent Poisson streams pools their rates. So $X_Z+X_G\sim\Poisson(5)$, and you finish with a single one-variable Poisson calculation instead of summing over every $(x_Z,x_G)$ pair that totals each value.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The brute-force temptation is **convolution**: to get $P(X_Z+X_G=k)$, sum $P(X_Z=j)P(X_G=k-j)$ over all $j$. That's correct but slow and error-prone, and it hides the clean answer. The *other* trap is over-applying the shortcut: pooling only works for **independent** variables, and only **within the same family with compatible parameters** — Gammas need a common scale, Binomials and NegBinomials a common $p$. Pool incompatible parameters and you get nonsense.

**Beat 5 — Translate into notation, one glyph at a time.** The MGF of $X$ is $M_X(t)=\E[e^{tX}]$ (read "the moment generating function of $X$"). For **independent** $X_1,\dots,X_n$, the MGF of the sum factors:

$$M_{X_1+\cdots+X_n}(t) = \E\!\big[e^{t(X_1+\cdots+X_n)}\big] = \E\!\big[e^{tX_1}\cdots e^{tX_n}\big] = \prod_{i=1}^{n} M_{X_i}(t),$$

where the last step used independence to split the expectation of a product into a product of expectations. The $\prod$ (read "the product over $i$") just means "multiply these together."

**Beat 6 — Derive the Poisson pooling from the MGF.** The MGF of a $\Poisson(\lambda)$ is $M(t)=e^{\lambda(e^t-1)}$. By independence,

$$M_{X_Z+X_G}(t) = e^{3(e^t-1)}\cdot e^{2(e^t-1)} = e^{(3+2)(e^t-1)} = e^{5(e^t-1)},$$

which is *exactly* the MGF of a $\Poisson(5)$. Because an MGF uniquely determines a distribution (its uniqueness property), $X_Z+X_G\sim\Poisson(5)$ — no convolution needed. The same argument, run on each family's MGF, gives the whole table below.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* pool two independent Poisson rates ⇒ $\Poisson(\sum\lambda_i)$, then one tail calculation.
- *Normal (the workhorse):* independent normals are closed under **any** linear combination, not just sums. In particular a *difference* of independent normals is normal:
$$X-Y \sim \Normal\!\big(\mu_X-\mu_Y,\;\sigma_X^2+\sigma_Y^2\big).$$
**Means subtract; variances ADD** — the same "a difference still adds variances" lesson from Concept 3.
- *Watch the requirements:* Gammas pool shapes *only* with a shared scale $\theta$; Binomials and NegBinomials pool *only* with a shared $p$. The full menu:

| Family | Independent components | Sum |
|---|---|---|
| Normal | $X_i \sim \Normal(\mu_i,\sigma_i^2)$ | $\sum X_i \sim \Normal\!\big(\sum\mu_i,\ \sum\sigma_i^2\big)$ |
| Poisson | $X_i \sim \Poisson(\lambda_i)$ | $\sum X_i \sim \Poisson\!\big(\sum\lambda_i\big)$ |
| Gamma (same scale $\theta$) | $X_i \sim \GammaDist(\alpha_i,\theta)$ | $\sum X_i \sim \GammaDist\!\big(\sum\alpha_i,\ \theta\big)$ |
| Binomial (same $p$) | $X_i \sim \Binom(n_i,p)$ | $\sum X_i \sim \Binom\!\big(\sum n_i,\ p\big)$ |
| Neg. Binomial (same $p$) | $X_i \sim \NegBin(r_i,p)$ | $\sum X_i \sim \NegBin\!\big(\sum r_i,\ p\big)$ |

**Beat 8 — Picture it.** Two thin Poisson bar-charts ($\lambda=3$ and $\lambda=2$) feed an arrow into one wider Poisson bar-chart ($\lambda=5$): the pooled stream is recognizably the same shape, just shifted right and spread to match $\lambda=5$. The picture says "same family, pooled parameter."

**Beat 9 — Consolidate.** You can now spot an independent in-family sum, pool the parameters in one step, and finish with a single one-variable distribution calculation — and you know the exact compatibility requirements that license the move.

::: pokedex-entry
**POKÉDEX ENTRY №05 — Sums That Stay in the Family (MGF method)**

For **independent** $X_1,\dots,X_n$: $\;M_{X_1+\cdots+X_n}(t) = \prod_{i=1}^{n} M_{X_i}(t).$ By MGF uniqueness, several families are closed under independent sums (pool the parameters):

$$\Normal:\ \textstyle\sum\Normal(\mu_i,\sigma_i^2)=\Normal(\sum\mu_i,\sum\sigma_i^2); \quad \Poisson:\ \textstyle\sum\Poisson(\lambda_i)=\Poisson(\sum\lambda_i);$$
$$\GammaDist\text{ (same }\theta):\ \textstyle\sum\GammaDist(\alpha_i,\theta)=\GammaDist(\sum\alpha_i,\theta); \quad \Binom/\NegBin\text{ (same }p):\ \text{add the }n_i\text{ or }r_i.$$

Normals close under **any** linear combination: $X-Y\sim\Normal(\mu_X-\mu_Y,\ \sigma_X^2+\sigma_Y^2)$ — means subtract, **variances add**.

*In plain terms:* adding independent members of these families gives back the same family with pooled parameters — replace a convolution with one parameter addition.

*Recognition cue:* "$X,Y$ independent [Normals / Poissons / same-scale Gammas / same-$p$ Binomials]; find $P(X+Y>c)$." Pool first, then do a single one-variable calculation. **Check compatibility:** Gammas need a common scale; Binomials/NegBinomials a common $p$.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Oak walks the first one; Gary models the capstone at full speed.</figcaption>
</figure>

Four examples, fading from fully narrated to exam-speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because the variance-of-a-sum rule is the hard, load-bearing idea.

### Worked Example 13.1 — Boulders and Onix (full narration; understanding-first)

**ARCHETYPE:** *Covariance and correlation from a joint pmf table; constants-drop-out rule.*

**Setup.** The Concept-1 table again, now as a clean exam item. $X$ = boulders cleared, $Y$ = Onix met:

| $p(x,y)$ | $y=0$ | $y=1$ |
|---|---|---|
| $x=0$ | $0.30$ | $0.10$ |
| $x=1$ | $0.20$ | $0.40$ |

Find $\Cov(X,Y)$ and the correlation $\rho$.

**Step 1 — Identify (which tools, and why).** Both $X,Y$ are $0/1$ indicators. We need $\Cov(X,Y)=\E[XY]-\E[X]\E[Y]$ (Entry №01), then divide by the two SDs for $\rho$ (Entry №02). Indicators have a gift: $\E[X^2]=\E[X]$, which makes the variances trivial.

**Step 2 — Professor's Path (the why).** Get the marginals first. The chance $X=1$ is the whole bottom row, $0.20+0.40=0.60$, so $\E[X]=0.60$; the chance $Y=1$ is the right column, $0.10+0.40=0.50$, so $\E[Y]=0.50$. For an indicator, $X^2=X$, so $\E[X^2]=\E[X]=0.60$ and

$$\Var(X)=\E[X^2]-\E[X]^2=0.60-0.36=0.24, \qquad \Var(Y)=0.50-0.25=0.25.$$

Now the product moment. $XY=1$ *only* in the both-equal-$1$ cell (probability $0.40$); every other cell has $X=0$ or $Y=0$, killing the product. So $\E[XY]=0.40$, and

$$\Cov(X,Y)=\E[XY]-\E[X]\E[Y]=0.40-(0.60)(0.50)=0.40-0.30=0.10.$$

**Step 3 — Trainer's Path (the fast how).** Marginals $0.60,0.50$; only the corner cell feeds $\E[XY]=0.40$; subtract: $\Cov=0.10$. Then

$$\rho=\frac{\Cov}{\SD(X)\SD(Y)}=\frac{0.10}{\sqrt{0.24}\,\sqrt{0.25}}=\frac{0.10}{(0.4899)(0.5)}=\frac{0.10}{0.24495}\approx 0.408.$$

**Step 4 — Check & the constants-drop-out note.** $\rho\approx0.41$ sits safely inside $[-1,1]$ ✓, and it's positive — boulders and Onix do tend to co-occur, matching the fat corner cell. **Pitfall:** computing $\E[XY]$ as a sum over *all four* cells and forgetting that any cell with a $0$ contributes nothing — for two indicators, only the both-$1$ cell matters. *Quick proof of the constants rule promised in Concept 1:* $\Cov(aX+b,cY+d)=\E[(aX+b)(cY+d)]-\E[aX+b]\E[cY+d]$; expand both, and every term containing $b$ or $d$ cancels between the two halves, leaving $ac(\E[XY]-\E[X]\E[Y])=ac\,\Cov(X,Y)$. *(Back-ref: Entries №01, №02.)*

### Worked Example 13.2 — The Variance of the Team Total (partial guidance)

**ARCHETYPE:** *Variance of a sum / difference from a given correlation.*

**Setup.** Charizard's output $X$ has $\Var(X)=9$; Bulbasaur's $Y$ has $\Var(Y)=4$; they are negatively correlated with $\rho=-0.5$. Find $\Var(T)$ for $T=X+Y$ and $\Var(D)$ for $D=X-Y$.

**Identify.** The correlation hides the covariance; recover it with $\Cov=\rho\,\SD(X)\,\SD(Y)$ (Entry №02), then apply the cross-term rule (Entry №03).

**Solve.** With $\SD(X)=3$, $\SD(Y)=2$:

$$\Cov(X,Y)=\rho\,\SD(X)\,\SD(Y)=(-0.5)(3)(2)=-3.$$

$$\Var(T)=\Var(X)+\Var(Y)+2\Cov(X,Y)=9+4+2(-3)=7.$$

$$\Var(D)=\Var(X)+\Var(Y)-2\Cov(X,Y)=9+4-2(-3)=19.$$

**Check & pitfall.** Negative covariance makes the **sum steadier** ($7<13$) and the **difference wilder** ($19>13$) — the diversification intuition exactly. Two classic traps: (1) mishandling the sign in the difference — it is $-2\Cov$, and $\Cov$ is *itself* negative, so the term becomes $+6$; (2) adding standard deviations instead of variances. You never add SDs. *(Back-ref: Entry №03.)*

### Worked Example 13.3 — Weighted Blend on the Final Ledge (light guidance)

**ARCHETYPE:** *Variance of a general weighted linear combination.*

**Setup.** For the last stretch you send three Pokémon with effort weights $2X_1$, $3X_2$, $X_3$. You know $\Var(X_1)=1$, $\Var(X_2)=2$, $\Var(X_3)=3$, the only nonzero covariance is $\Cov(X_1,X_2)=0.5$, and $X_3$ is independent of the others. Find $\Var(2X_1+3X_2+X_3)$.

**Solve.** Weights $a_1=2,a_2=3,a_3=1$. Squared-weight (diagonal) terms:

$$a_1^2\Var(X_1)+a_2^2\Var(X_2)+a_3^2\Var(X_3)=4(1)+9(2)+1(3)=4+18+3=25.$$

Cross-terms: only the $(1,2)$ pair is nonzero ($X_3$ independent ⇒ its two covariances vanish):

$$2\,a_1a_2\,\Cov(X_1,X_2)=2(2)(3)(0.5)=6.$$

$$\Var(2X_1+3X_2+X_3)=25+6=31.$$

**Check & pitfall.** **Pitfall:** applying the weight to the covariance only once. The cross-term is $2a_ia_j\Cov$ — *both* weights **and** the factor of $2$ must appear: $2\cdot2\cdot3\cdot0.5=6$, not $0.5$ or $3$. *(Back-ref: Entry №03.)*

### Worked Example 13.4 — Two Independent Bat Swarms (exam speed)

**ARCHETYPE:** *Sum of independent Poissons; pool the rates, then a tail.*

**Setup.** Zubat $\sim\Poisson(3)$ and Golbat $\sim\Poisson(2)$, independent. Find $P(\text{fewer than 3 bats total in a minute})$.

**Solve.** Pool: $N=X_Z+X_G\sim\Poisson(5)$. "Fewer than 3" means $N\le 2$:

$$P(N\le 2)=e^{-5}\!\left(1+5+\frac{5^2}{2}\right)=e^{-5}(1+5+12.5)=18.5\,e^{-5}\approx 18.5(0.0067379)\approx 0.1247.$$

**Professor's Path (why pooling is legal).** $M_{\Poisson(\lambda)}(t)=e^{\lambda(e^t-1)}$, so by independence $M_{X_Z+X_G}(t)=e^{3(e^t-1)}e^{2(e^t-1)}=e^{5(e^t-1)}$, the MGF of $\Poisson(5)$. Uniqueness ⇒ the sum *is* $\Poisson(5)$; no convolution needed.

**Check & pitfall.** $P\approx0.125$ is a sensible probability ✓. **Pitfall:** reading "fewer than 3" as $N\le3$ — it is $N\le2$. *(Back-ref: Entry №05.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — three reflexes that buy whole minutes**

1. **Given $\rho$, recover covariance instantly:** $\Cov=\rho\,\sigma_X\sigma_Y$. Most problems hide the covariance behind a stated correlation and two SDs — this is your first move.
2. **Independence is a license to delete:** the instant you read "independent," cross out *every* covariance term — but never touch the squared-variance terms.
3. **In-family pooling beats convolution:** Normal / Poisson / same-scale-Gamma / same-$p$-Binomial sums collapse to one distribution. Spot the family *before* you integrate or sum anything.
:::

::: trainers-tip
**TRAINER'S TIP — calculator hygiene**

On the TI-30XS, write any "$X-Y$" variance as $\Var X+\Var Y-2\Cov$ *before* keying numbers — the sign on the cross-term is the single most common slip on this topic. For a Poisson tail like $P(N\le2)$ with $\lambda=5$, bank $e^{-5}$ with `STO→` first, then evaluate `e^{-5}·(1+5+5²/2)` in one entry so you never re-key a rounded constant.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

<figure style="margin:1.25em auto; max-width:150px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">Jessie, James &amp; Meowth — the misconception, embodied</figcaption>
</figure>

Jessie and James rig two trap-nets across the cave. Net A has output spread $\SD=6$; Net B has $\SD=8$. "When both nets fire together," Meowth declares, "the total spread is just six plus eight — *fourteen!* We'll overwhelm the twerp's whole team!" James paints "$14$" on the launcher. They fire. The nets snap *correlated* — both surge at once — and the combined recoil blows the launcher apart, dropping all of Team Rocket down a chute. "We're blasting off again!"

**Where it fails:** Meowth added **standard deviations** instead of variances, and ignored covariance entirely. Even if the nets were *independent*, the true spread would be $\sqrt{6^2+8^2}=\sqrt{100}=10$, not $14$. With **positive** covariance (the nets surge together) it is *larger* still — but **never** the naive sum of SDs.

**The fix:** standard deviations never add; **variances** add (plus $2\Cov$). Combine on the *variance* scale, then take the square root at the very end.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

Portfolio risk *is* covariance. An insurer holding thousands of policies cares about the variance of the **total** loss, and that total's variance is dominated by the cross-terms:

$$\Var\!\Big(\sum_i L_i\Big)=\sum_i\Var(L_i)+2\!\sum_{i<j}\Cov(L_i,L_j).$$

**Diversification** — the entire reason insurance and reinsurance work — is the deliberate engineering of *low or negative* covariance between risks, so the pooled total is far steadier than any single policy. A reinsurer pricing a catastrophe treaty must estimate how strongly regional hurricane losses move together; underestimate that covariance and you under-reserve and risk insolvency. Capital-requirement formulas (Solvency II, the NAIC RBC correlation matrix) are literally covariance matrices applied to lines of business.

There is a humbling limit, too. If $n$ identical risks each have variance $\sigma^2$ and a *common positive* pairwise covariance $c$, the **average** loss has variance $\dfrac{\sigma^2}{n}+\dfrac{n-1}{n}c\to c$ as $n\to\infty$. Independent risks ($c=0$) average away to nothing; *correlated* risks leave an irreducible **systematic floor** $c$, no matter how large the book. That is exactly why insurers can diversify idiosyncratic claim noise but **cannot** diversify away a single hurricane hitting every policy at once (Problem C13.16 builds this).

*Series bridge:* this covariance-of-totals machinery is the foundation of portfolio risk theory and the correlation aggregation in CAS Exam 5 / MAS-II capital modeling.

*Transfer check (no Pokémon in it):* "Two loss lines have variances $100$ and $225$ and correlation $-0.3$; find the variance of their total." $\Cov=-0.3\sqrt{100}\sqrt{225}=-45$, so $\Var=100+225+2(-45)=235$ — a $90$-unit diversification benefit over the naive $325$. If you can do that, the skill has transferred.
:::

## The Gym Battle — Victory Road Capstone

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/blue.png" alt="Gary, your rival" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Gary models the expert path at exam speed — no gym leader guards Victory Road; the mountain is the opponent.</figcaption>
</figure>

*This is the chapter's hardest single problem: it pulls in covariance from a correlation matrix, the full linear-combination variance rule, a normal-approximation tail, a variance-of-a-difference, and a sum-in-family finish — exactly the integrative item the exam loves.*

**Setup.** Dusk is an hour off. Oak needs the full risk profile of your three-Pokémon vanguard before you commit to the final shaft. Let $X_1,X_2,X_3$ be the strength outputs of Pikachu, Charizard, and Bulbasaur, with

$$\E[X_1]=10,\ \E[X_2]=14,\ \E[X_3]=8, \qquad \Var(X_1)=4,\ \Var(X_2)=9,\ \Var(X_3)=5,$$

and pairwise correlations $\rho_{12}=0.5$, $\rho_{13}=-0.2$, $\rho_{23}=0$. The vanguard's total push is $T=X_1+X_2+X_3$.

(a) Find $\E[T]$ and $\Var(T)$.
(b) The shaft clears only if total push exceeds $40$. Assuming $T$ is approximately normal, estimate $P(T>40)$.
(c) A relief Pidgeot is sent if the *gap* $G=X_2-X_3$ has standard deviation under $4$. Does it qualify?
(d) After the climb, two **independent** scouting flights each report Spearow sightings as $\Poisson(2.5)$. Find the probability the two flights report $5$ or more sightings combined.

**ARCHETYPE:** *full linear-combination variance from a correlation matrix + normal-approx tail + variance of a difference + sum-in-family.*

**Identify.** (a) Mean is linear; variance needs all three cross-terms via $\Cov_{ij}=\rho_{ij}\sigma_i\sigma_j$. (b) Standardize $T$. (c) Variance of a difference. (d) Pool two independent Poissons.

**Trainer's Path.**

*Convert correlations to covariances* with $\sigma_1=2,\sigma_2=3,\sigma_3=\sqrt5$:

$$\Cov_{12}=0.5(2)(3)=3,\quad \Cov_{13}=-0.2(2)\sqrt5=-0.4\sqrt5\approx-0.8944,\quad \Cov_{23}=0.$$

**(a)** Mean: $\E[T]=10+14+8=32$. Variance (all weights $=1$, so just sum variances plus twice the three covariances):

$$\Var(T)=\underbrace{4+9+5}_{18}+2\big(\Cov_{12}+\Cov_{13}+\Cov_{23}\big)=18+2(3-0.8944+0)=18+4.2111=22.211,$$

so $\SD(T)=\sqrt{22.211}\approx 4.713$.

**(b)** Standardize and read the normal tail:

$$z=\frac{40-32}{4.713}=\frac{8}{4.713}\approx 1.70, \qquad P(T>40)=P(Z>1.70)\approx 1-0.9554=0.0446\approx 4.5\%.$$

**(c)** Gap variance (a difference, so $-2\Cov_{23}$, and $\Cov_{23}=0$):

$$\Var(G)=\Var(X_2)+\Var(X_3)-2\Cov_{23}=9+5-0=14, \qquad \SD(G)=\sqrt{14}\approx 3.742.$$

Since $3.742<4$, the relief Pidgeot is **not** dispatched — the gap is steady enough.

**(d)** Two independent $\Poisson(2.5)$ pool to $\Poisson(5)$. Want $P(N\ge5)=1-P(N\le4)$:

$$P(N\le4)=e^{-5}\!\left(1+5+\tfrac{25}{2}+\tfrac{125}{6}+\tfrac{625}{24}\right)=e^{-5}(1+5+12.5+20.8333+26.0417)=65.375\,e^{-5}\approx 0.4405,$$
$$P(N\ge5)\approx 1-0.4405=0.5595.$$

**Professor's Path (the matrix view of (a)).** Writing $\mathbf a=(1,1,1)^{\!\top}$ and $\Sigma$ the covariance matrix, $\Var(T)=\mathbf a^{\!\top}\Sigma\,\mathbf a=\sum_i\Var(X_i)+2\sum_{i<j}\Cov_{ij}$ — the same arithmetic, but the matrix form scales to all six teammates and is exactly how a capital model aggregates correlated lines.

**Check & pitfall.** Every variance is positive; every probability is in $[0,1]$. Sanity: the net covariance is *positive* ($+4.21$), so $\SD(T)\approx4.71$ must exceed the independent value $\sqrt{18}\approx4.24$ — and it does ✓. The headline pitfall: forgetting the $\rho_{13}=-0.2$ term is **negative**, partly offsetting the positive $\rho_{12}$ term — drop its sign and you overstate $\Var(T)$.

> Gary smirks. "Mean's the easy part. The whole exam lives in that cross-term — and you nailed the sign. See you at the Plateau, Ash."

## The Gym Challenge — Problem Set

::: problem-set
**TEST-OUT INSTRUCTIONS.** Work this set timed (~6 min per Gym Battle problem, less for Route Trainers), then check the **Answer Key** below. Hit the mastery bar (**80%+ with correct method**) and you may move on. Problems are listed first; full worked solutions follow afterward (never interleaved). Markers: 🔴 Poké Ball = routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (mechanics)

**C13.1.** 🔴 On the entrance ledge, Pikachu's output $X$ has $\Var(X)=4$ and Charizard's $Y$ has $\Var(Y)=9$. They are **independent**. Find $\Var(X+Y)$.

**C13.2.** 🔴 Same two climbers as C13.1 ($\Var(X)=4$, $\Var(Y)=9$), but now their efforts move together with $\Cov(X,Y)=2$. Find $\Var(X+Y)$ and $\Var(X-Y)$.

**C13.3.** 🔴 Brock measures Geodude's output $U$ ($\SD=5$) and Onix's output $V$ ($\SD=12$) with correlation $\rho=0.4$. Convert this to the covariance $\Cov(U,V)$.

**C13.4.** 🔴 Misty reports $\E[X]=3$, $\E[Y]=5$, $\E[XY]=16$ for her two Pokémon's spin-counts. Find $\Cov(X,Y)$ and state whether they move together or apart.

**C13.5.** 🟡 A relay sends Pokémon up with weights $a=3$ on output $X$ and $b=-2$ on output $Y$, where $\Var(X)=2$, $\Var(Y)=5$, and $X,Y$ are independent. Find $\Var(3X-2Y)$.

**C13.6.** 🟡 Two independent normal climbers: $X\sim\Normal(10,4)$ and $Y\sim\Normal(6,9)$ (variances given). Identify the exact distribution of $X-Y$, including its mean and variance.

**C13.7.** 🔴 Wild Rattata appear in two independent corridors as $\Poisson(1.5)$ and $\Poisson(2.5)$. Identify the exact distribution of the total count and state its mean and variance.

### Gym Battles (true SOA difficulty)

**C13.8.** 🟡 The cave RNG gives the joint pmf of $(X,Y)$ — boulders cleared and Onix met — as $p(0,0)=0.2$, $p(1,0)=0.2$, $p(0,1)=0.1$, $p(1,1)=0.3$, $p(2,1)=0.2$. Compute $\Cov(X,Y)$ and the correlation $\rho$.

**C13.9.** 🟡 A vanguard of three has $\Var(X_1)=2$, $\Var(X_2)=3$, $\Var(X_3)=4$, with $\Cov(X_1,X_2)=1$, $\Cov(X_1,X_3)=-1$, and $X_2,X_3$ uncorrelated. Find $\Var(X_1+X_2+X_3)$.

**C13.10.** 🟡 With the same variances and covariances as C13.9, the load-weighted team total is $W=X_1+2X_2+3X_3$. Find $\Var(W)$.

**C13.11.** 🔵 A continuous pair has joint density $f(x,y)=x+y$ on the unit square $0\le x\le1,\ 0\le y\le1$. Find $\Cov(X,Y)$. (You may use $\E[X]=\E[Y]=\tfrac{7}{12}$.)

**C13.12.** 🔵 Let $X$ be uniform on $\{-1,0,1\}$ (each with probability $\tfrac13$) and $Y=X^2$. Show $\Cov(X,Y)=0$, yet $X$ and $Y$ are **not** independent. (The canonical uncorrelated-but-dependent trap.)

**C13.13.** 🟡 Charizard's output $X\sim\Normal(14,9)$ and Bulbasaur's $Y\sim\Normal(8,5)$ are independent. The shaft clears if combined output $X+Y$ exceeds $25$. Find $P(X+Y>25)$.

**C13.14.** 🔴 Two independent climbers' times are $\GammaDist(2,\theta)$ and $\GammaDist(3,\theta)$ with common scale $\theta=4$. Identify the exact distribution of the total time and give its mean and variance.

**C13.15.** 🟡 A portfolio of two routes has losses $L_1,L_2$ with $\Var(L_1)=100$, $\Var(L_2)=225$, and correlation $\rho=-0.3$. Compare $\Var(L_1+L_2)$ against the naive independent value $\Var(L_1)+\Var(L_2)$, and state the diversification benefit (reduction in variance).

### Elite Challenge (integrative / stretch)

**C13.16.** 🔵 Six teammates each have output variance $\sigma^2=4$, and **every** distinct pair has the same covariance $c=1$. Let $T=\sum_{i=1}^6 X_i$. Derive $\Var(T)$ in terms of $\sigma^2$ and $c$ using the count of pairs, then evaluate it. Also find the correlation between any single $X_i$ and the total $T$.

**C13.17.** 🔵 A compound climb: you make $N$ pushes where $N\sim\Poisson(3)$, and each push expends independent strength $S_i$ with $\E[S]=2$, $\Var(S)=1$, independent of $N$. The total expended is $T=\sum_{i=1}^N S_i$. Using $\E[T]=\E[N]\E[S]$ and $\Var(T)=\E[N]\Var(S)+\Var(N)\E[S]^2$, find $\E[T]$ and $\Var(T)$.

**C13.18.** 🔵 Define $X_1,X_2,X_3$ as in the Gym Battle capstone ($\sigma_1=2,\sigma_2=3,\sigma_3=\sqrt5$; $\rho_{12}=0.5,\rho_{13}=-0.2,\rho_{23}=0$). Oak wants the covariance between the *front-pair total* $A=X_1+X_2$ and the *rear-pair total* $B=X_2+X_3$ (note $X_2$ appears in both). Use bilinearity to find $\Cov(A,B)$.
:::

## Answer Key

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

**C13.1** — *Variance of an independent sum (Entry №03).* Independent ⇒ $\Cov=0$, so $\Var(X+Y)=\Var(X)+\Var(Y)=4+9=\boxed{13}$.

**C13.2** — *Variance of a sum/difference with covariance (Entry №03).*
$$\Var(X+Y)=4+9+2(2)=\boxed{17}, \qquad \Var(X-Y)=4+9-2(2)=\boxed{9}.$$
Positive covariance inflates the sum, deflates the difference.

**C13.3** — *Recover covariance from correlation (Entry №02).* $\Cov(U,V)=\rho\,\SD(U)\,\SD(V)=0.4(5)(12)=\boxed{24}.$

**C13.4** — *Covariance from $\E[XY]$ (Entry №01).* $\Cov(X,Y)=\E[XY]-\E[X]\E[Y]=16-(3)(5)=\boxed{1}>0$, so they **move together**.

**C13.5** — *Variance of a weighted independent combination (Entry №03).* Independent ⇒ no cross-term; weights enter squared (sign vanishes):
$$\Var(3X-2Y)=3^2\Var(X)+(-2)^2\Var(Y)=9(2)+4(5)=18+20=\boxed{38}.$$

**C13.6** — *Difference of independent normals (Entry №05).* Normals close under linear combinations: $X-Y\sim\Normal(10-6,\ 4+9)=\boxed{\Normal(4,13)}$. Means subtract, variances **add**.

**C13.7** — *Sum of independent Poissons (Entry №05).* Pool the rates: total $\sim\Poisson(1.5+2.5)=\boxed{\Poisson(4)}$, with $\E=\Var=4$ (Poisson mean = variance).

**C13.8** — *Covariance and correlation from a joint pmf (Entries №01, №02).*
$X$ marginal: $P(0)=0.2+0.1=0.3$, $P(1)=0.2+0.3=0.5$, $P(2)=0.2$. So $\E[X]=0(0.3)+1(0.5)+2(0.2)=0.9$, $\E[X^2]=0+0.5+4(0.2)=1.3$, $\Var(X)=1.3-0.81=0.49$.
$Y$ marginal (indicator): $P(1)=0.1+0.3+0.2=0.6$, so $\E[Y]=0.6$, $\Var(Y)=0.6-0.36=0.24$.
$\E[XY]$ (nonzero only when both $\ge1$): $(1,1)\!:1(0.3)=0.3$; $(2,1)\!:2(0.2)=0.4$, so $\E[XY]=0.7$.
$$\Cov=0.7-(0.9)(0.6)=0.7-0.54=\boxed{0.16}, \qquad \rho=\frac{0.16}{\sqrt{0.49}\sqrt{0.24}}=\frac{0.16}{(0.7)(0.4899)}\approx\boxed{0.467}.$$

**C13.9** — *Variance of a sum of three with cross-terms (Entry №03).*
$$\Var(X_1+X_2+X_3)=2+3+4+2(\Cov_{12}+\Cov_{13}+\Cov_{23})=9+2(1-1+0)=\boxed{9}.$$

**C13.10** — *Variance of a weighted three-variable combination (Entry №03).* Weights $a_1=1,a_2=2,a_3=3$.
Diagonal: $1^2(2)+2^2(3)+3^2(4)=2+12+36=50$.
Cross: $2[(1)(2)(1)+(1)(3)(-1)+(2)(3)(0)]=2[2-3+0]=-2$.
$$\Var(W)=50-2=\boxed{48}.$$

**C13.11** — *Continuous covariance (Entry №01).*
$$\E[XY]=\int_0^1\!\!\int_0^1 xy(x+y)\,dx\,dy=\int_0^1\!\!\int_0^1 (x^2y+xy^2)\,dx\,dy.$$
Inner over $x$: $\tfrac{y}{3}+\tfrac{y^2}{2}$. Outer over $y$: $\tfrac13\cdot\tfrac12+\tfrac12\cdot\tfrac13=\tfrac16+\tfrac16=\tfrac13$.
$$\Cov=\E[XY]-\E[X]\E[Y]=\tfrac13-\left(\tfrac{7}{12}\right)^2=\tfrac13-\tfrac{49}{144}=\tfrac{48-49}{144}=\boxed{-\tfrac{1}{144}}\approx-0.00694.$$

**C13.12** — *Uncorrelated-but-dependent counterexample (Entry №04).*
$\E[X]=0$ by symmetry. $\E[XY]=\E[X\cdot X^2]=\E[X^3]=\tfrac13\big((-1)^3+0+1^3\big)=0$. So $\Cov(X,Y)=0-0=\boxed{0}$.
Not independent: $P(X=0,Y=1)=0$, but $P(X=0)P(Y=1)=\tfrac13\cdot\tfrac23=\tfrac29\ne0$. (Knowing $X=0$ forces $Y=0$.) Hence $\rho=0$ does **not** imply independence.

**C13.13** — *Sum of independent normals + tail (Entry №05).*
$X+Y\sim\Normal(14+8,\ 9+5)=\Normal(22,14)$, $\SD=\sqrt{14}\approx3.742$.
$$z=\frac{25-22}{3.742}\approx0.80, \qquad P(X+Y>25)=P(Z>0.80)\approx1-0.7881=\boxed{0.2119}.$$

**C13.14** — *Sum of same-scale Gammas (Entry №05).* Common scale $\theta=4$ ⇒ shapes add: total $\sim\GammaDist(2+3,4)=\boxed{\GammaDist(5,4)}$. Mean $=\alpha\theta=5(4)=20$; variance $=\alpha\theta^2=5(16)=80$.

**C13.15** — *Diversification via negative covariance (Entry №03 / real-world box).*
$\Cov(L_1,L_2)=\rho\,\SD_1\SD_2=(-0.3)(10)(15)=-45$.
$$\Var(L_1+L_2)=100+225+2(-45)=325-90=\boxed{235}.$$
Naive independent value $=325$. Diversification benefit $=325-235=\boxed{90}$ reduction in variance (a $27.7\%$ cut), purely from the negative correlation.

**C13.16** — *Equicorrelated sum, count of pairs (Entry №03).*
General: $\Var(T)=n\sigma^2+2\binom{n}{2}c=n\sigma^2+n(n-1)c$. With $n=6,\sigma^2=4,c=1$:
$$\Var(T)=6(4)+6(5)(1)=24+30=\boxed{54}.$$
Correlation of $X_i$ with $T$: $\Cov(X_i,T)=\Var(X_i)+\sum_{j\ne i}\Cov(X_i,X_j)=4+5(1)=9$, so
$$\rho_{X_i,T}=\frac{9}{\sqrt{4}\sqrt{54}}=\frac{9}{2(7.348)}\approx\boxed{0.612}.$$

**C13.17** — *Compound-distribution moments (bridges the double-expectation chapter; Entry №03).*
$\E[T]=\E[N]\E[S]=3(2)=\boxed{6}$.
For $N\sim\Poisson(3)$: $\E[N]=\Var(N)=3$.
$$\Var(T)=\E[N]\Var(S)+\Var(N)\E[S]^2=3(1)+3(2)^2=3+12=\boxed{15}.$$
(Poisson check: $\Var(T)=\lambda\,\E[S^2]=3(\Var S+\E[S]^2)=3(1+4)=15$ ✓.)

**C13.18** — *Covariance of two overlapping sums via bilinearity (Entry №01).*
$\Cov_{12}=0.5(2)(3)=3$, $\Cov_{13}=-0.2(2)\sqrt5\approx-0.8944$, $\Cov_{23}=0$, $\Var(X_2)=9$.
By bilinearity, $\Cov(A,B)=\Cov(X_1+X_2,\;X_2+X_3)=\Cov(X_1,X_2)+\Cov(X_1,X_3)+\Cov(X_2,X_2)+\Cov(X_2,X_3)$
$$=3+(-0.8944)+9+0=\boxed{11.106}.$$
The shared $X_2$ contributes its full variance $9$ — overlap creates strong positive covariance between the two sums.

### Quick-Answer Table

| # | Answer | | # | Answer |
|---|---|---|---|---|
| C13.1 | $13$ | | C13.10 | $48$ |
| C13.2 | $\Var(X{+}Y)=17$, $\Var(X{-}Y)=9$ | | C13.11 | $-\tfrac{1}{144}\approx-0.00694$ |
| C13.3 | $\Cov=24$ | | C13.12 | $\Cov=0$, dependent |
| C13.4 | $\Cov=1$ (together) | | C13.13 | $\approx0.212$ |
| C13.5 | $38$ | | C13.14 | $\GammaDist(5,4)$, $\E=20,\Var=80$ |
| C13.6 | $\Normal(4,13)$ | | C13.15 | $\Var=235$; benefit $90$ |
| C13.7 | $\Poisson(4)$, $\E=\Var=4$ | | C13.16 | $\Var(T)=54$, $\rho\approx0.612$ |
| C13.8 | $\Cov=0.16$, $\rho\approx0.467$ | | C13.17 | $\E[T]=6$, $\Var(T)=15$ |
| C13.9 | $9$ | | C13.18 | $\Cov(A,B)\approx11.106$ |
:::

## Badge Earned — Mastery Checklist

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/earth_badge.png" alt="Victory Road medallion" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Victory Road Cleared — checkpoint medallion!</strong></figcaption>
</figure>

You earn the **Victory Road Cleared** medallion when you can, unaided:

1. **Compute covariance** $\Cov(X,Y)=\E[XY]-\E[X]\E[Y]$ from a joint pmf or density, and convert a given correlation $\rho$ into a covariance with $\Cov=\rho\,\sigma_X\sigma_Y$ — and back. *(Outcome 3e.)*
2. **State and use the independence/correlation one-way street:** independence $\Rightarrow\rho=0$, but $\rho=0\not\Rightarrow$ independence, with the $Y=X^2$ counterexample at hand. *(Outcome 3e.)*
3. **Find the variance of any linear combination** $\Var(\sum a_iX_i)=\sum a_i^2\Var(X_i)+2\sum_{i<j}a_ia_j\Cov(X_i,X_j)$, getting every cross-term and sign right — including $\Var(X-Y)=\Var X+\Var Y-2\Cov$. *(Outcome 3g.)*
4. **Compute means and variances of linear combinations** in the independent and normal special cases without hesitation. *(Outcome 3h.)*
5. **Recognize and collapse sums of independent in-family distributions** (Normal, Poisson, same-scale Gamma, same-$p$ Binomial) via the MGF/parameter-pooling rule, then finish a single one-variable tail calculation. *(Outcome 3h.)*

> **Gym rematch pointers (🧴 Potion).** Miss item 1 → re-read Concepts 1–2 and Worked Example 13.1. Miss item 2 → Concept 4 and C13.12. Miss item 3 → redo Worked Examples 13.2–13.3 and Gym Battle (a). Miss item 4 → Gym Battle (b)–(c). Miss item 5 → re-drill Concept 5, Worked Example 13.4, and C13.6, C13.7, C13.13, C13.14.

*Onward — the climb is cleared. Ahead lie order statistics and the Central Limit Theorem, where these sums of independent variables finally reveal the bell curve that every total secretly approaches.*

---

<!-- ===== CALLOUT BOX TEMPLATES (Pandoc fenced divs; styled by book/theme.css) =====
     ::: cold-open / pokedex-entry / trainers-tip / team-rocket / kanto-realworld
     Concept gate ("Do you already own this?") also uses a styled panel.
     Wrap the problem set in ::: problem-set and the key in ::: answer-key . -->
