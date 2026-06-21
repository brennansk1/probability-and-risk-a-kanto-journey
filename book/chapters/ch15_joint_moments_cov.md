<!--
  file: ch15_joint_moments_cov
  tier: A
  outcomes: 3e,3g,3h
  tia: C.5
  locale: Victory Road
  type: ground
  maps_to: Victory Road — the team as a combination (the six become one total)
  content_base: Version 1/book/chapters/ch13_covariance.md (re-skinned + lifted to V3 ch02 gold standard)
-->

# Combining Forces {.type-ground}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with the route to Victory Road highlighted; every gym badge so far is collected and the path now climbs from Viridian toward the Indigo Plateau, with Victory Road marked as the current leg." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 10 — every badge earned, you reach <strong>Victory Road</strong>, the gauntlet where the team stops being six separate Pokémon and becomes one <em>total</em>.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Climb Is a Sum"**

The cave mouth of Victory Road swallows the last of the afternoon light. No gym leader waits here, no badge to win — only a vertical gauntlet of boulders, strength puzzles, and wild Onix you must clear *as a team*, in one continuous push, before the Pokémon League registration window closes at dusk.

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

**Rank: Veteran Trainer · Badges: 7.** Seven badges earned; only Giovanni's Earth Badge remains. The road from Viridian now climbs into Victory Road, the last leg before the Indigo Plateau. You arrive carrying everything from the joint-distribution chapters and the chapter on expectation. Two ideas from back there are the ground this chapter stands on.

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

"Victory Road is where individuals become a *portfolio*, Ash. Up to now you've studied one random variable at a time, and at most their joint behavior. From here on, the question is always about a **total** — a sum of many linked variables — and the entire game is getting its *spread* right. Master this and you can price the risk of an insurer's whole book of policies, not just one. This is the last Tier-A climb before the League."

By the end of this chapter you will be able to:

- **Compute joint moments** $\E[XY]$ and, more generally, $\E[g(X,Y)]$ over a joint pmf or density, and use them as the raw material for everything that follows. *(Outcome 3e.)*
- **Compute covariance** $\Cov(X,Y) = \E[XY] - \E[X]\E[Y]$ for discrete and continuous pairs, and exploit its **bilinearity**. *(Outcome 3e.)*
- **Compute the correlation coefficient** $\rho$, interpret its sign and magnitude, and explain precisely why independence forces $\rho = 0$ while $\rho = 0$ does **not** force independence. *(Outcome 3e.)*
- **Find the variance of a sum or general linear combination** $\Var\!\big(\sum a_i X_i\big)$, including every $2a_i a_j \Cov(X_i,X_j)$ cross-term with the right sign. *(Outcome 3g.)*
- **Compute moments — mean and variance — of linear combinations** of random variables, including the independent and normal special cases, and combine **sums of independent in-family distributions** (Normal+Normal, Poisson+Poisson, same-scale Gamma+Gamma, same-$p$ Binomial+Binomial) via the **MGF method**. *(Outcomes 3g, 3h.)*

> *Exam-weight signpost.* Covariance, variance of sums, and sums of independent variables sit squarely in Exam P's **Multivariate** block (≈23–30% of the exam), and the variance-of-a-sum rule is one of the single most-tested computations on the test. This is a **Tier A** chapter — full treatment, full ramp.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own All of Victory Road?**

Already fluent? Prove it. Work these five, ~3 minutes each, *with correct method*:

1. $\E[X]=3$, $\E[Y]=5$, $\E[XY]=16$. Find $\Cov(X,Y)$.
2. $\SD(U)=5$, $\SD(V)=12$, $\rho=0.4$. Find $\Cov(U,V)$.
3. $\Var(X)=4$, $\Var(Y)=9$, $\Cov(X,Y)=2$. Find $\Var(X+Y)$ and $\Var(X-Y)$.
4. $X\sim\Normal(10,4)$ and $Y\sim\Normal(6,9)$ independent (variances given). Name the exact distribution of $X-Y$.
5. Independent $X\sim\Poisson(1.5)$ and $Y\sim\Poisson(2.5)$. Name the exact distribution of $X+Y$.

*(Answers: $1$; $24$; $\Var(X{+}Y)=17$, $\Var(X{-}Y)=9$; $\Normal(4,13)$; $\Poisson(4)$.)* Five for five with correct reasoning? **Skip to the Gym Battle** and claim the medallion. Any miss or hesitation? The teaching below was built exactly for you — and each concept has its own skip-gate, so even a partial owner loses no time.
:::

---

Six ideas build on one another here, in increasing difficulty. We teach them **in order**, each with its own "do you already own this?" skip-check, then the full nine-beat lesson, then a Pokédex Entry you can carry into the exam:

1. **Joint moments** $\E[XY]$ and $\E[g(X,Y)]$ — the raw material *(everything else is built from these)*
2. **Covariance** — a single number for how two variables move together
3. **Correlation** — covariance rescaled onto a fixed $-1$-to-$+1$ ruler
4. **Variance of a sum / linear combination** — the cross-term rule *(the load-bearing climb)*
5. **Independence vs. zero correlation** — and the one-way street between them
6. **Sums that stay in the family** — pooling parameters with the MGF

## Concept 1 — Joint Moments: $\E[XY]$ and $\E[g(X,Y)]$

::: concept-gate
**DO YOU ALREADY OWN THIS? — Joint Moments**

On a ledge, $X$ = boulders Pikachu clears (either $0$ or $1$) and $Y$ = Onix that emerge (either $0$ or $1$), with joint pmf $p(1,1)=0.40$ and the product $XY$ equal to $1$ only there. What is $\E[XY]$? And if instead the cave asks for $\E[(X+Y)^2]$, do you know the *recipe* (sum $g(x,y)$ weighted by $p(x,y)$ over every cell)?

If you answered **$\E[XY]=0.40$** and can state "$\E[g(X,Y)]=\sum_x\sum_y g(x,y)\,p(x,y)$ (or the double integral)," **skip to Concept 2**. If "average a function of *two* variables" is hazy, this section builds it.
:::

**Beat 1 — The one-sentence idea.** *To average any quantity that depends on two variables, you sweep over every joint outcome, plug it into the quantity, weight by that outcome's probability, and add — exactly like a one-variable expected value, but over a grid (or a region) instead of a line.*

**Beat 2 — Anchor + concrete instance.** You already know the one-variable expected value: $\E[g(X)]=\sum_x g(x)\,p_X(x)$ — average $g$ over $X$'s outcomes, weighted by their probabilities. A joint moment is the same act, with the single sum replaced by a double sum over the *pairs* $(x,y)$, weighted by the **joint** pmf $p(x,y)$. Here is the story, with numbers small enough to do by hand.

On the first ledge, two things happen on each attempt: $X$ = the number of boulders Pikachu must Iron-Tail aside (either $0$ or $1$), and $Y$ = the number of wild Onix that emerge (either $0$ or $1$). The cave's RNG produces this joint table over many attempts:

| $p(x,y)$ | $y=0$ | $y=1$ |
|---|---|---|
| $x=0$ | $0.30$ | $0.10$ |
| $x=1$ | $0.20$ | $0.40$ |

The single number we will need over and over is the **product moment** $\E[XY]$ — the average of $X$ times $Y$. *What is it?*

**Beat 3 — Reason through it in plain words.** Walk every cell and ask "what is $x\cdot y$ here, and how likely is this cell?" In three of the four cells either $x=0$ or $y=0$, so the product $xy$ is $0$ and the cell contributes nothing no matter how likely it is. Only the both-equal-$1$ cell has $xy=1$, and it carries probability $0.40$. So the average product is

$$\E[XY] = \sum_x\sum_y xy\,p(x,y) = (0)(0.30)+(0)(0.10)+(0)(0.20)+(1)(1)(0.40) = 0.40.$$

The whole double sum collapsed to one surviving term — a recurring gift when $X$ and $Y$ are $0/1$ indicators.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The seductive shortcut is to compute $\E[XY]$ by multiplying the two means:

$$\E[XY] \overset{?}{=} \E[X]\,\E[Y] = (0.60)(0.50) = 0.30. \qquad\textbf{(wrong, in general)}$$

*(The marginals: $\E[X]=P(X{=}1)=0.20+0.40=0.60$ and $\E[Y]=P(Y{=}1)=0.10+0.40=0.50$.)* But $\E[XY]=\E[X]\E[Y]$ holds **only when the two variables are unrelated** — it is the very thing the *next* concept measures the failure of. Here the true $\E[XY]=0.40$, not $0.30$. Computing the joint moment from the **joint table**, not from the product of marginals, is the entire point of having a joint distribution at all.

**Beat 5 — Translate into notation, one glyph at a time.** Write $\E[XY]$ (read "the expected value of $X$ times $Y$") for the product moment. More generally, for *any* function $g$ of the two variables, the **joint moment** of $g$ is

$$\E\!\big[g(X,Y)\big] = \sum_x\sum_y g(x,y)\,p(x,y) \qquad\text{(discrete)},$$

read aloud as "sum, over every pair $(x,y)$, of $g$ at that pair times the probability of that pair." The double $\sum_x\sum_y$ just means "sweep the whole grid." For a **continuous** pair with joint density $f(x,y)$, the two sums become two integrals:

$$\E\!\big[g(X,Y)\big] = \iint g(x,y)\,f(x,y)\,dx\,dy \qquad\text{(continuous)}.$$

The product moment is the special case $g(x,y)=xy$. Other useful choices: $g=x$ recovers $\E[X]$ (a marginal mean), $g=(x+y)^2$ gives $\E[(X+Y)^2]$, and $g=\max(x,y)$ gives the expected larger of the two.

**Beat 6 — Generalize: read the recipe off the instance.** Nothing was special about $g=xy$. The pattern is always the same three moves — **(i)** for each joint outcome compute $g$, **(ii)** multiply by that outcome's joint probability (or density), **(iii)** add them all up:

$$\boxed{\,\E\!\big[g(X,Y)\big] = \sum_x\sum_y g(x,y)\,p(x,y) \;\text{ or }\; \iint g(x,y)\,f(x,y)\,dx\,dy.\,}$$

This is not a new rule to memorize so much as the *definition* of expectation, extended from one variable to a pair. Every covariance, variance-of-a-sum, and correlation in this chapter is just this recipe with a cleverly chosen $g$.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $\E[XY]$ off a small joint table — sweep the cells, as above.
- *A different $g$:* $\E[(X+Y)^2]$. You could expand and use $\E[X^2]+2\E[XY]+\E[Y^2]$, or sweep the grid directly with $g(x,y)=(x+y)^2$. Both give the same number; the grid sweep never goes wrong.
- *Continuous:* for $f(x,y)$ on a region, $\E[XY]=\iint xy\,f\,dx\,dy$ — a double integral, but the *recipe* is identical to the discrete sum.
- *Edge (the factoring gift):* if (and only if) $X,Y$ are **independent**, the joint moment of a product *factors*: $\E[g(X)h(Y)]=\E[g(X)]\,\E[h(Y)]$. In particular $\E[XY]=\E[X]\E[Y]$. We prove this in Concept 5; for now, never *assume* it.

**Beat 8 — Picture it.** A joint pmf is a grid of probability masses; computing $\E[g(X,Y)]$ means stamping each cell with its $g$-value, multiplying cell-by-cell by the mass, and totalling. For the product moment specifically, the cells where either coordinate is $0$ are "dead" — they stamp a $0$ — so for two indicators only the both-$1$ corner is alive. The scatter figure in the next concept makes the *signed* version of this sweep visible.

**Beat 9 — Consolidate.** You can now average any function of two variables — most importantly the product $XY$ — straight off a joint table or density. That single skill is the raw material for covariance, correlation, and the variance of a sum, which are the rest of this chapter.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Joint Moments**

$$\E\!\big[g(X,Y)\big] = \sum_x\sum_y g(x,y)\,p(x,y) \quad\text{or}\quad \iint g(x,y)\,f(x,y)\,dx\,dy.$$

The **product moment** is the case $g(x,y)=xy$: $\;\E[XY]=\sum_x\sum_y xy\,p(x,y)$ (or the double integral).

*In plain terms:* average a function of two variables by sweeping every joint outcome, weighting by the joint probability/density, and adding. It is ordinary expectation lifted from a line to a grid (or region).

*Recognition cue:* anytime a problem hands you a **joint table** or **joint density** and asks for the average of *something built from both* variables — $\E[XY]$, $\E[(X+Y)^2]$, $\E[\max(X,Y)]$ — sweep the grid with that $g$. Do **not** factor $\E[XY]$ into $\E[X]\E[Y]$ unless independence is given.
:::

## Concept 2 — Covariance: A Number for Moving Together

::: concept-gate
**DO YOU ALREADY OWN THIS? — Covariance**

Misty reports that her Staryu's spin-count $X$ and her Starmie's spin-count $Y$ satisfy $\E[X]=3$, $\E[Y]=5$, and $\E[XY]=16$. What is $\Cov(X,Y)$, and do the two spin *together* or *against* each other?

If you immediately answered **$\Cov(X,Y)=16-(3)(5)=1>0$, "together,"** you own covariance — **skip to Concept 3**. If $\E[XY]-\E[X]\E[Y]$ wasn't your first move, or the sign's meaning is fuzzy, this section is for you.
:::

**Beat 1 — The one-sentence idea.** *Covariance is the average of "how far above its mean $X$ is" times "how far above its mean $Y$ is" — one number that is positive when the two tend to rise and fall together, and negative when one rises as the other falls.*

**Beat 2 — Anchor + concrete instance.** You already know **variance**: the average squared distance of a *single* variable from its own mean, $\Var(X)=\E[(X-\mu_X)^2]$. Covariance is the natural next step — instead of multiplying $X$'s deviation by *itself*, multiply it by $Y$'s deviation, then average with the joint-moment recipe from Concept 1.

Use the same ledge table, $X$ = boulders cleared, $Y$ = Onix met:

| $p(x,y)$ | $y=0$ | $y=1$ |
|---|---|---|
| $x=0$ | $0.30$ | $0.10$ |
| $x=1$ | $0.20$ | $0.40$ |

*Do boulders and Onix tend to appear together?* Look at the table: the big $0.40$ sits in the "both $=1$" corner. That hints "together" — but we want a *number*.

**Beat 3 — Reason through it in plain words.** $X$ is high (equal to $1$) exactly when there are boulders; $Y$ is high exactly when Onix emerge. If boulders and Onix tend to show up on the *same* attempts, then whenever $X$ is above its average, $Y$ is *also* above its average — both deviations have the same sign, so their **product is positive**. Average those products over all attempts and you get a positive number: they move together. If instead Onix only showed up when there were *no* boulders, $X$ above average would pair with $Y$ below average — opposite signs, **negative product**, negative average. Covariance is exactly that average product of deviations.

We already have the pieces from Concept 1: $\E[X]=0.60$, $\E[Y]=0.50$, and the product moment $\E[XY]=0.40$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The seductive shortcut is again to set $\E[XY]=\E[X]\E[Y]=0.30$. But the true $\E[XY]=0.40$. That **gap of $0.10$** between "what $\E[XY]$ actually is" and "what it would be if they ignored each other" is precisely the co-movement — and it *is* the covariance. Assuming $\E[XY]=\E[X]\E[Y]$ throws away the entire phenomenon we came here to measure.

**Beat 5 — Translate into notation, one glyph at a time.** Write $\mu_X$ (read "mew-sub-$X$") for $\E[X]$ and $\mu_Y$ for $\E[Y]$. The deviation "how far above its mean $X$ is" is $X-\mu_X$. The average product of deviations gets its own name, $\Cov$ (read "**covariance** of $X$ and $Y$"):

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
- *Constants drop out (the rule you'll lean on constantly):* shifting a variable by a constant moves its mean by the same amount, so the deviation $X-\mu_X$ is unchanged — a constant *shift* cannot affect co-movement. A constant *multiplier* factors straight out. Together,
$$\Cov(aX+b,\;cY+d) = ac\,\Cov(X,Y).$$
The $+b$ and $+d$ vanish; the $a$ and $c$ survive. (Derived in full in Worked Example 15.1's pitfall note.)

**Beat 8 — Picture it.** A figure makes "moving together" literal: each dot is one attempt, plotted at its $(X,Y)$, and the mean-crosshairs split the plane into four quadrants. Dots where both deviations agree in sign (upper-right, lower-left) contribute a *positive* product; the other two quadrants contribute negative. Covariance is the average over all dots — so a cloud that tilts up has positive covariance.

<figure>
<img src="../../assets/diagrams/ch15_covariance_scatter.png" alt="A scatterplot of two Pokemon's per-climb surges, X (Charizard) horizontal and Y (Pikachu) vertical, each plotted as its deviation from its own mean. Dashed crosshairs at the two means divide the plane into four quadrants, tagged with plus signs in the upper-right and lower-left (where both deviations share a sign, so their product is positive) and minus signs in the upper-left and lower-right. Green circles mark dots whose deviation-product is positive, red triangles mark dots whose product is negative; the cloud tilts upward, so green same-sign dots dominate and the covariance is positive." style="width:80%; max-width:540px; display:block; margin:1em auto;">
<figcaption>Covariance is the average of (deviation in $X$) × (deviation in $Y$). Same-sign dots (upper-right and lower-left, green) push covariance up; opposite-sign dots (red) pull it down. Here the up-slope wins: $\Cov(X,Y)>0$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now turn any joint table or density — or just a given $\E[XY]$ — into one number that says whether two variables move together (positive), against (negative), or neither (zero), and you know that variance is the special case $\Cov(X,X)$.

::: pokedex-entry
**POKÉDEX ENTRY №02 — Covariance**

$$\Cov(X,Y) = \E\!\big[(X-\mu_X)(Y-\mu_Y)\big] = \E[XY] - \E[X]\,\E[Y].$$

Special cases and rules:

$$\Cov(X,X) = \Var(X), \qquad \Cov(X,Y)=\Cov(Y,X), \qquad \Cov(aX+b,\;cY+d) = ac\,\Cov(X,Y).$$

*In plain terms:* the average of "$X$'s distance above its mean" times "$Y$'s distance above its mean." Positive ⇒ they tend to be high together (and low together); negative ⇒ one is high when the other is low; the size has units of $X$ times $Y$, so it is **not** yet on a fixed scale (Concept 3 fixes that).

*Why the computational form is faster:* $\E[XY]-\E[X]\E[Y]$ needs only three numbers; the definition needs the full deviation of every outcome.

*Recognition cue:* a problem hands you a **joint table**, a **joint density**, or the product moment $\E[XY]$ — or asks for the variance of a sum of *dependent* variables. Reach for $\Cov(X,Y)=\E[XY]-\E[X]\E[Y]$.
:::

## Concept 3 — Correlation: Covariance on a Fixed Ruler

::: concept-gate
**DO YOU ALREADY OWN THIS? — Correlation**

Brock measures Geodude's output $U$ ($\SD=5$) and Onix's output $V$ ($\SD=12$) and finds $\Cov(U,V)=24$. What is the correlation $\rho_{U,V}$?

If you answered **$\rho=\dfrac{24}{5\cdot 12}=0.4$** and can say *why $\rho$ has no units while covariance does*, **skip to Concept 4**. If covariance and correlation feel like the same thing, read on — the rescaling is the whole point.
:::

**Beat 1 — The one-sentence idea.** *Correlation is covariance divided by the two standard deviations, which strips away the units and pins the answer onto a fixed ruler from $-1$ to $+1$ — so you can read off the strength and direction of the linear link at a glance.*

**Beat 2 — Anchor + concrete instance.** Covariance (Concept 2) has a flaw: its size is meaningless on its own. A covariance of $24$ between two huge variables might be a *weak* link; between two tiny variables, a *strong* one. We need to standardize — exactly the trick you used to standardize a normal into a $Z$-score, but for co-movement.

Brock measures **Geodude's output $U$** with $\SD(U)=5$ and **Onix's output $V$** with $\SD(V)=12$, and finds their covariance is $\Cov(U,V)=24$. *Is that a strong link or a weak one?* The bare $24$ can't say.

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/95.png" alt="Onix, a Rock/Ground-type Pokémon" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#095 Onix — output $V$, $\SD(V)=12$</strong></figcaption>
</figure>

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
- *Endpoints:* $\rho=+1$ means $Y$ is an exactly *increasing* linear function of $X$; $\rho=-1$, exactly *decreasing*; $\rho=0$ means *no linear* association (but, foreshadowing Concept 5, **not** necessarily "no relationship").

**Beat 8 — Picture it.** Three scatterplots, now labeled with $\rho$: a tight up-sloping line is $\rho\approx+0.9$; a round blob is $\rho\approx 0$; a tight down-sloping line is $\rho\approx -0.9$. Correlation is, visually, *how close the cloud hugs a straight line*, with sign for the slope.

<figure>
<img src="../../assets/diagrams/ch15_correlation_signs.png" alt="Three side-by-side scatterplots labeled by correlation. Left: a tight upward-sloping cloud of green circles, labeled rho about plus 0.9, captioned 'tight up-slope: move together'. Middle: a round shapeless blob of gray squares, labeled rho about 0, captioned 'round blob: no linear link'. Right: a tight downward-sloping cloud of red triangles, labeled rho about minus 0.9, captioned 'tight down-slope: move apart'. A ruler strip beneath reads minus 1 (perfect decreasing line), 0 (no linear association), plus 1 (perfect increasing line)." style="width:92%; max-width:640px; display:block; margin:1em auto;">
<figcaption>Correlation places covariance on a fixed $[-1,1]$ ruler. $+1$ = perfectly increasing line, $-1$ = perfectly decreasing line, $0$ = no linear association. Magnitude is how tightly the cloud hugs a line; sign is the slope's direction.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now convert covariance to a unit-free strength on the $[-1,1]$ ruler, read its sign and magnitude, and — crucially — recover a hidden covariance from a stated $\rho$ and two SDs.

::: pokedex-entry
**POKÉDEX ENTRY №03 — Correlation Coefficient**

$$\rho_{X,Y} = \Corr(X,Y) = \frac{\Cov(X,Y)}{\SD(X)\,\SD(Y)} = \frac{\Cov(X,Y)}{\sqrt{\Var(X)\,\Var(Y)}}, \qquad -1 \le \rho \le 1.$$

Recover covariance from a given correlation: $\;\Cov(X,Y) = \rho\,\SD(X)\,\SD(Y).$ Scale-free: $\Corr(aX+b,\,cY+d)=\operatorname{sign}(ac)\,\rho_{X,Y}$.

*In plain terms:* correlation is covariance rescaled to live in $[-1,1]$, measuring the **strength and direction** of the *linear* relationship without units. $+1$ = perfectly increasing line, $-1$ = perfectly decreasing line, $0$ = no linear link.

*Recognition cue:* the word **"correlation,"** a given $\rho$, or "how strongly are they related on a $-1$-to-$1$ scale." If you're *given* $\rho$ and two SDs, immediately recover $\Cov=\rho\,\SD_X\,\SD_Y$ — that is almost always the next step.
:::

## Concept 4 — Variance of a Sum: The Cross-Term Rule

*This is the load-bearing climb of the chapter — the single most-tested computation, and the one Oak warned you about in the cave. We give it the full Professor's-Path-first treatment.*

::: concept-gate
**DO YOU ALREADY OWN THIS? — Variance of a Sum**

Charizard's output $X$ has $\Var(X)=9$; Bulbasaur's $Y$ has $\Var(Y)=4$. They are **negatively** correlated, $\rho=-0.5$. Find $\Var(X+Y)$ and $\Var(X-Y)$.

If you answered **$\Var(X+Y)=7$ and $\Var(X-Y)=19$** — first converting $\rho$ to $\Cov=-0.5\cdot3\cdot2=-3$, then applying $\Var\pm 2\Cov$ — **skip to Concept 5**. If you got $13$ for both (forgetting the cross-term) or added the standard deviations, this is the most important section in the chapter for you.
:::

**Beat 1 — The one-sentence idea.** *The spread of a total is the sum of the individual spreads **plus** a cross-term for every pair — twice their covariance — so linked variables make the total either wilder (if they move together) or steadier (if they move apart).*

**Beat 2 — Anchor + concrete instance.** You know $\Var(aX)=a^2\Var(X)$ for *one* variable (the retrieval at the top). Now there are two, and the question is what extra appears. This is the cave problem made concrete.

**Charizard's output $X$** has $\Var(X)=9$; **Bulbasaur's output $Y$** has $\Var(Y)=4$. Because Bulbasaur wilts whenever Charizard overheats, they are **negatively** correlated with $\rho=-0.5$. Oak wants the variance of the combined push $T=X+Y$, and — for comparison — the variance of the "tag-out swing" $D=X-Y$.

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/front/6.png" alt="Charizard, a Fire/Flying-type Pokémon" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#006 Charizard — output $X$, $\Var(X)=9$</strong></figcaption>
</figure>

**Beat 3 — Reason through it in plain words.** First convert the correlation to a covariance (Entry №03): $\Cov(X,Y)=\rho\,\SD(X)\,\SD(Y)=(-0.5)(3)(2)=-3$. Now, *if the two were unrelated*, the spreads would just add: $9+4=13$. But they're **negatively** linked — when Charizard surges, Bulbasaur tends to sag, so the two partly *cancel* each other in the total. That cancellation makes the **sum steadier** than $13$. Conversely, in the *difference* $X-Y$, the negative link makes the two pull *apart* harder, so the **difference is wilder** than $13$. The cross-term has to carry that information, and it does: it's $2\Cov$ for a sum, $-2\Cov$ for a difference.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two traps live here, and they are the most punished errors on the topic.

*Trap 1 — "variances just add."*
$$\Var(X+Y) \overset{?}{=} \Var(X)+\Var(Y) = 13. \qquad\textbf{(wrong unless uncorrelated)}$$
That is right *only* when $\Cov=0$. Here $\Cov=-3$, so the truth is $13 + 2(-3) = 7$ — the negative link shrinks the spread. Dropping the cross-term silently assumes independence you were never given.

*Trap 2 — "add the standard deviations."* Some reach for $\SD(X)+\SD(Y)=3+2=5$, then square to $25$. **Standard deviations never add.** Variances combine (plus the cross-term); you take the square root only at the very end. Adding SDs has no theoretical basis at all. *(This is exactly the error Team Rocket commits below — and it blows up their launcher.)*

**Beat 5 — Translate into notation, one glyph at a time.** We want $\Var(X+Y)$, read "the variance of the sum." Start from the one true definition — variance is covariance with itself (Entry №02, Beat 7) — and let covariance's **bilinearity** do the work. Bilinearity just means covariance distributes over sums, like multiplying out $(a+b)(c+d)$:

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
<img src="../../assets/diagrams/ch15_linear_combo_var.png" alt="A 3-by-3 grid with rows and columns both labeled a1X1, a2X2, a3X3. The three diagonal cells are shaded the Victory Road ground color and hold a1^2 Var(X1), a2^2 Var(X2), a3^2 Var(X3). The six off-diagonal cells are shaded blue with a hatch pattern and hold the products a_i a_j Cov(X_i, X_j); red double-headed arrows connect each off-diagonal cell to its mirror image across the diagonal, showing that each of the three distinct covariance products appears in two cells, which is the source of the factor of 2 in the variance-of-a-sum formula." style="width:78%; max-width:520px; display:block; margin:1em auto;">
<figcaption>$\Var(\sum a_iX_i)$ is the sum of every cell in this grid: $n$ diagonal variance cells plus pairs of mirror-image covariance cells. Each distinct covariance appears twice — that is the factor of $2$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now find the variance of any sum, difference, or weighted blend of random variables, getting every cross-term and its sign right — and you will never again add standard deviations or silently drop a covariance.

::: pokedex-entry
**POKÉDEX ENTRY №04 — Variance of a Sum / Linear Combination**

Two variables:
$$\Var(X+Y) = \Var(X) + \Var(Y) + 2\,\Cov(X,Y), \qquad \Var(X-Y) = \Var(X) + \Var(Y) - 2\,\Cov(X,Y).$$

General linear combination:
$$\Var\!\Big(\sum_{i=1}^{n} a_i X_i\Big) = \sum_{i=1}^{n} a_i^2\,\Var(X_i) + 2\!\!\sum_{1\le i<j\le n}\!\! a_i a_j\,\Cov(X_i,X_j).$$

Mean (always clean, no covariance term ever): $\;\E\!\big[\sum a_i X_i + b\big] = \sum a_i\,\E[X_i] + b.$

*In plain terms:* the spread of a total is **not** just the sum of spreads — there's a cross-term per pair. Positive covariance inflates the total's variance; negative covariance shrinks it. A difference still **adds** the variances; only the cross-term flips sign. Weights enter **squared** on variances, as $2a_ia_j$ on cross-terms.

*Recognition cue:* any **sum, difference, or weighted blend** of random variables whose variance you need. Write the cross-terms first, then ask "are these independent?" — only then do you get to delete them.
:::

## Concept 5 — Independence vs. Zero Correlation (the One-Way Street)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Independence and Correlation**

$X$ is uniform on $\{-1,0,1\}$ (each with probability $\tfrac13$) and $Y=X^2$. Is $\Cov(X,Y)=0$? Are $X$ and $Y$ independent?

If you answered **"$\Cov=0$, yet they are *not* independent"** — and can explain why correlation misses the link — **skip to Concept 6**. If "$\rho=0$" made you say "independent," this section dismantles exactly that error.
:::

**Beat 1 — The one-sentence idea.** *Independence always forces correlation to zero, but zero correlation does not force independence — because correlation only detects **linear** co-movement and is blind to curved relationships.*

**Beat 2 — Anchor + concrete instance.** From Concept 4 you saw that uncorrelated variables let variance add cleanly. The natural assumption is "uncorrelated = unrelated = independent." It's half-right, and the wrong half is a classic exam trap.

Let $X$ be uniform on $\{-1,0,1\}$, each value with probability $\tfrac13$, and let $Y=X^2$. So $Y=1$ when $X=\pm1$ and $Y=0$ when $X=0$. *These are about as dependent as two variables get — $Y$ is a deterministic function of $X$.* Yet watch what correlation says.

**Beat 3 — Reason through it in plain words.** $X$ is symmetric about $0$, so $\E[X]=\tfrac13(-1+0+1)=0$. Now $\E[XY]=\E[X\cdot X^2]=\E[X^3]=\tfrac13\big((-1)^3+0^3+1^3\big)=\tfrac13(-1+0+1)=0$. Therefore

$$\Cov(X,Y)=\E[XY]-\E[X]\E[Y]=0-(0)\E[Y]=0, \quad\text{so}\quad \rho=0.$$

Zero correlation. But independence would require $P(X=0,\,Y=1)=P(X=0)\,P(Y=1)$. The left side is **$0$** (if $X=0$ then $Y=0\ne1$), while the right side is $P(X=0)\,P(Y=1)=\tfrac13\cdot\tfrac23=\tfrac29\ne0$. They are **not** independent — in fact knowing $X$ tells you $Y$ exactly. Correlation simply couldn't see it: the relationship is a symmetric parabola, perfectly *curved*, with no straight-line tilt for $\rho$ to detect.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap:

$$\rho = 0 \overset{?}{\Longrightarrow} X,Y \text{ independent}. \qquad\textbf{(wrong)}$$

Correlation is a *linear* detector. A relationship that goes up then down (like $Y=X^2$) has no net tilt, so $\rho=0$ — yet the variables are tightly linked. The implication runs **one way only**:

$$X \perp Y \;\Longrightarrow\; \Cov(X,Y)=0 \;\Longrightarrow\; \rho=0, \qquad\text{but } \rho=0 \;\not\Longrightarrow\; X\perp Y.$$

(The symbol $\perp$, read "is independent of," means knowing one tells you nothing about the other.) The *forward* direction is true and useful; the *converse* is the trap.

**Beat 5 — Translate into notation, and prove the forward direction.** Why does independence force $\Cov=0$? Because independence is exactly the statement that the joint factors, which makes the product moment factor (the "gift" promised in Concept 1):

$$\E[XY]=\iint xy\,f(x,y)\,dx\,dy = \iint xy\,f_X(x)f_Y(y)\,dx\,dy = \Big(\int x f_X(x)dx\Big)\Big(\int y f_Y(y)dy\Big)=\E[X]\E[Y].$$

(The middle step used independence: $f(x,y)=f_X(x)f_Y(y)$.) Then $\Cov(X,Y)=\E[XY]-\E[X]\E[Y]=0$. So independence ⇒ zero covariance ⇒ zero correlation, always.

**Beat 6 — Why the converse fails (the structural reason).** Covariance is built from the product moment $\E[XY]$, which weights the relationship by $x\cdot y$ — a *linear* quantity in each variable. Any dependence whose "ups" and "downs" cancel under that linear weighting (like a function symmetric about $X$'s mean) leaves $\E[XY]=\E[X]\E[Y]$ untouched. Independence is a statement about *every* joint probability; correlation is a statement about *one linear average*. The first is far stronger, so it implies the second — never the reverse.

**Beat 7 — Ramp the difficulty.**

- *Simplest (forward):* told "independent," instantly set every covariance term to $0$ and let variances add cleanly. This is a *license to delete*.
- *The canonical counterexample:* $Y=X^2$ with $X$ symmetric about $0$ — memorize it; it is the standard exam illustration that $\rho=0\not\Rightarrow$ independence.
- *Edge:* the **normal** family is the famous exception where the implication *does* go both ways — for *jointly normal* $X,Y$, $\rho=0$ **does** imply independence. (That equivalence is special to joint normality; never assume it elsewhere.)

**Beat 8 — Picture it.** Reuse the middle scatterplot from Concept 3 — a round, sloping-nowhere blob — and overlay the $Y=X^2$ parabola through $(-1,1),(0,0),(1,1)$. Both have $\rho=0$; one is genuinely unrelated, the other is a deterministic curve. Correlation can't tell them apart.

**Beat 9 — Consolidate.** You can now use independence as a license to delete every covariance term, *and* you will never run that street backward — $\rho=0$ alone never licenses "independent."

::: pokedex-entry
**POKÉDEX ENTRY №05 — Independence vs. Zero Correlation (the one-way street)**

$$X \perp Y \;\Longrightarrow\; \Cov(X,Y)=0 \;\Longrightarrow\; \rho=0, \qquad\text{but } \rho=0 \;\not\Longrightarrow\; X\perp Y.$$

*In plain terms:* independent variables are *always* uncorrelated (because $\E[XY]=\E[X]\E[Y]$). But uncorrelated variables can still be dependent — $\rho$ only sees *linear* association, so a purely curved link (e.g. $Y=X^2$ with $X$ symmetric about $0$) hides from it. Exception: *jointly normal* variables, for which $\rho=0$ **does** give independence.

*Recognition cue:* "$X$ and $Y$ are independent" ⇒ delete every covariance term on sight. "Does $\rho=0$ imply independence?" ⇒ **no**, and the answer is the $Y=X^2$ counterexample.
:::

## Concept 6 — Sums That Stay in the Family (the MGF Method)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Sums of Independent In-Family Variables**

Independent $X\sim\Poisson(3)$ and $Y\sim\Poisson(2)$. Name the exact distribution of $X+Y$. And independent $X\sim\Normal(\mu_X,\sigma_X^2)$, $Y\sim\Normal(\mu_Y,\sigma_Y^2)$: name the distribution of $X-Y$.

If you answered **$\Poisson(5)$** and **$\Normal(\mu_X-\mu_Y,\;\sigma_X^2+\sigma_Y^2)$** (means subtract, variances *add*), **skip to the Worked Examples**. If you reached for a convolution sum, read on — pooling parameters is far faster.
:::

**Beat 1 — The one-sentence idea.** *When you add **independent** members of certain families, the sum is a member of the **same** family with the parameters simply pooled — so you replace a hard convolution with one parameter addition.*

**Beat 2 — Anchor + concrete instance.** You met the **moment generating function** $M_X(t)=\E[e^{tX}]$ earlier as the "DNA" that uniquely identifies a distribution. Here it does one spectacular trick: the MGF of a sum of *independent* variables is the *product* of their MGFs — which is the joint-moment factoring rule from Concept 5 applied to $g(X)=e^{tX}$. That product often collapses into a recognizable family's MGF.

In the deepest chamber, **Zubat** appear independently at rate $\lambda_Z=3$ per minute and **Golbat** at rate $\lambda_G=2$ per minute, each $\Poisson$. You need the chance that *fewer than 3 bats total* appear in a given minute so you can slip past. *What is the distribution of the total $X_Z+X_G$?*

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/41.png" alt="Zubat, a Poison/Flying-type Pokémon" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
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
**Means subtract; variances ADD** — the same "a difference still adds variances" lesson from Concept 4.
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
**POKÉDEX ENTRY №06 — Sums That Stay in the Family (MGF method)**

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

Five examples, fading from fully narrated to exam-speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because the variance-of-a-sum rule is the hard, load-bearing idea.

### Worked Example 15.1 — Boulders and Onix (full narration; understanding-first)

<figure style="margin:1.25em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/95.png" alt="Onix, the rock-snake Pokémon" style="width:120px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#095 Onix — the rock-snake whose appearances $Y$ track the boulders $X$</strong></figcaption>
</figure>

**ARCHETYPE:** *Joint moments → covariance and correlation from a joint pmf table; constants-drop-out rule.*

**Setup.** The Concept-1/2 table again, now as a clean exam item. $X$ = boulders cleared, $Y$ = Onix met:

| $p(x,y)$ | $y=0$ | $y=1$ |
|---|---|---|
| $x=0$ | $0.30$ | $0.10$ |
| $x=1$ | $0.20$ | $0.40$ |

Find $\Cov(X,Y)$ and the correlation $\rho$.

**Step 1 — Identify (which tools, and why).** Both $X,Y$ are $0/1$ indicators. We need the product moment $\E[XY]$ (Entry №01), then $\Cov(X,Y)=\E[XY]-\E[X]\E[Y]$ (Entry №02), then divide by the two SDs for $\rho$ (Entry №03). Indicators have a gift: $\E[X^2]=\E[X]$, which makes the variances trivial.

**Step 2 — Professor's Path (the why).** Get the marginals first. The chance $X=1$ is the whole bottom row, $0.20+0.40=0.60$, so $\E[X]=0.60$; the chance $Y=1$ is the right column, $0.10+0.40=0.50$, so $\E[Y]=0.50$. For an indicator, $X^2=X$, so $\E[X^2]=\E[X]=0.60$ and

$$\Var(X)=\E[X^2]-\E[X]^2=0.60-0.36=0.24, \qquad \Var(Y)=0.50-0.25=0.25.$$

Now the product moment (sweep the grid, Entry №01). $XY=1$ *only* in the both-equal-$1$ cell (probability $0.40$); every other cell has $X=0$ or $Y=0$, killing the product. So $\E[XY]=0.40$, and

$$\Cov(X,Y)=\E[XY]-\E[X]\E[Y]=0.40-(0.60)(0.50)=0.40-0.30=0.10.$$

**Step 3 — Trainer's Path (the fast how).** Marginals $0.60,0.50$; only the corner cell feeds $\E[XY]=0.40$; subtract: $\Cov=0.10$. Then

$$\rho=\frac{\Cov}{\SD(X)\SD(Y)}=\frac{0.10}{\sqrt{0.24}\,\sqrt{0.25}}=\frac{0.10}{(0.4899)(0.5)}=\frac{0.10}{0.24495}\approx 0.408.$$

**Step 4 — Check & the constants-drop-out note.** $\rho\approx0.41$ sits safely inside $[-1,1]$ ✓, and it's positive — boulders and Onix do tend to co-occur, matching the fat corner cell. **Pitfall:** computing $\E[XY]$ as a sum over *all four* cells and forgetting that any cell with a $0$ contributes nothing — for two indicators, only the both-$1$ cell matters. *Quick proof of the constants rule promised in Concept 2:* $\Cov(aX+b,cY+d)=\E[(aX+b)(cY+d)]-\E[aX+b]\E[cY+d]$; expand both, and every term containing $b$ or $d$ cancels between the two halves, leaving $ac(\E[XY]-\E[X]\E[Y])=ac\,\Cov(X,Y)$. *(Back-ref: Entries №01, №02, №03.)*

### Worked Example 15.2 — The Variance of the Team Total (partial guidance)

**ARCHETYPE:** *Variance of a sum / difference from a given correlation.*

**Setup.** Charizard's output $X$ has $\Var(X)=9$; Bulbasaur's $Y$ has $\Var(Y)=4$; they are negatively correlated with $\rho=-0.5$. Find $\Var(T)$ for $T=X+Y$ and $\Var(D)$ for $D=X-Y$.

**Identify.** The correlation hides the covariance; recover it with $\Cov=\rho\,\SD(X)\,\SD(Y)$ (Entry №03), then apply the cross-term rule (Entry №04).

**Solve.** With $\SD(X)=3$, $\SD(Y)=2$:

$$\Cov(X,Y)=\rho\,\SD(X)\,\SD(Y)=(-0.5)(3)(2)=-3.$$

$$\Var(T)=\Var(X)+\Var(Y)+2\Cov(X,Y)=9+4+2(-3)=7.$$

$$\Var(D)=\Var(X)+\Var(Y)-2\Cov(X,Y)=9+4-2(-3)=19.$$

**Check & pitfall.** Negative covariance makes the **sum steadier** ($7<13$) and the **difference wilder** ($19>13$) — the diversification intuition exactly. Two classic traps: (1) mishandling the sign in the difference — it is $-2\Cov$, and $\Cov$ is *itself* negative, so the term becomes $+6$; (2) adding standard deviations instead of variances. You never add SDs. *(Back-ref: Entry №04.)*

### Worked Example 15.3 — Weighted Blend on the Final Ledge (light guidance)

**ARCHETYPE:** *Variance of a general weighted linear combination.*

**Setup.** For the last stretch you send three Pokémon with effort weights $2X_1$, $3X_2$, $X_3$. You know $\Var(X_1)=1$, $\Var(X_2)=2$, $\Var(X_3)=3$, the only nonzero covariance is $\Cov(X_1,X_2)=0.5$, and $X_3$ is independent of the others. Find $\Var(2X_1+3X_2+X_3)$.

**Solve.** Weights $a_1=2,a_2=3,a_3=1$. Squared-weight (diagonal) terms:

$$a_1^2\Var(X_1)+a_2^2\Var(X_2)+a_3^2\Var(X_3)=4(1)+9(2)+1(3)=4+18+3=25.$$

Cross-terms: only the $(1,2)$ pair is nonzero ($X_3$ independent ⇒ its two covariances vanish):

$$2\,a_1a_2\,\Cov(X_1,X_2)=2(2)(3)(0.5)=6.$$

$$\Var(2X_1+3X_2+X_3)=25+6=31.$$

**Check & pitfall.** **Pitfall:** applying the weight to the covariance only once. The cross-term is $2a_ia_j\Cov$ — *both* weights **and** the factor of $2$ must appear: $2\cdot2\cdot3\cdot0.5=6$, not $0.5$ or $3$. *(Back-ref: Entry №04.)*

### Worked Example 15.4 — A Joint Moment of the Total (partial guidance)

**ARCHETYPE:** *Joint moment $\E[g(X,Y)]$ via $\E[(X+Y)^2]=\Var(X+Y)+\E[X+Y]^2$.*

**Setup.** Two teammates have $\E[X]=3$, $\E[Y]=5$, $\Var(X)=4$, $\Var(Y)=9$, and $\Cov(X,Y)=2$. Find the second moment of the team total, $\E[(X+Y)^2]$.

**Identify.** $\E[(X+Y)^2]$ is a joint moment with $g(x,y)=(x+y)^2$ (Entry №01). The fast route uses the identity $\E[W^2]=\Var(W)+\E[W]^2$ on $W=X+Y$ — so we need $\Var(X+Y)$ (Entry №04) and $\E[X+Y]$ (linearity).

**Solve.** Mean of the total: $\E[X+Y]=3+5=8$. Variance of the total (positive covariance inflates it):

$$\Var(X+Y)=\Var(X)+\Var(Y)+2\Cov(X,Y)=4+9+2(2)=17.$$

Then

$$\E[(X+Y)^2]=\Var(X+Y)+\E[X+Y]^2=17+8^2=17+64=81.$$

**Check & pitfall.** Equivalently, expand: $\E[(X+Y)^2]=\E[X^2]+2\E[XY]+\E[Y^2]$, with $\E[X^2]=\Var X+\E[X]^2=4+9=13$, $\E[Y^2]=9+25=34$, and $\E[XY]=\Cov+\E[X]\E[Y]=2+15=17$, giving $13+2(17)+34=81$ ✓. **Pitfall:** writing $\E[(X+Y)^2]=\E[X+Y]^2=64$ — forgetting that the second moment exceeds the squared mean by exactly the variance. *(Back-ref: Entries №01, №04.)*

### Worked Example 15.5 — Two Independent Bat Swarms (exam speed)

**ARCHETYPE:** *Sum of independent Poissons; pool the rates, then a tail.*

**Setup.** Zubat $\sim\Poisson(3)$ and Golbat $\sim\Poisson(2)$, independent. Find $P(\text{fewer than 3 bats total in a minute})$.

**Solve.** Pool: $N=X_Z+X_G\sim\Poisson(5)$. "Fewer than 3" means $N\le 2$:

$$P(N\le 2)=e^{-5}\!\left(1+5+\frac{5^2}{2}\right)=e^{-5}(1+5+12.5)=18.5\,e^{-5}\approx 18.5(0.0067379)\approx 0.1247.$$

**Professor's Path (why pooling is legal).** $M_{\Poisson(\lambda)}(t)=e^{\lambda(e^t-1)}$, so by independence $M_{X_Z+X_G}(t)=e^{3(e^t-1)}e^{2(e^t-1)}=e^{5(e^t-1)}$, the MGF of $\Poisson(5)$. Uniqueness ⇒ the sum *is* $\Poisson(5)$; no convolution needed.

**Check & pitfall.** $P\approx0.125$ is a sensible probability ✓. **Pitfall:** reading "fewer than 3" as $N\le3$ — it is $N\le2$. *(Back-ref: Entry №06.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — three reflexes that buy whole minutes**

1. **Given $\rho$, recover covariance instantly:** $\Cov=\rho\,\sigma_X\sigma_Y$. Most problems hide the covariance behind a stated correlation and two SDs — this is your first move.
2. **Independence is a license to delete:** the instant you read "independent," cross out *every* covariance term — but never touch the squared-variance terms.
3. **In-family pooling beats convolution:** Normal / Poisson / same-scale-Gamma / same-$p$-Binomial sums collapse to one distribution. Spot the family *before* you integrate or sum anything.
:::

::: trainers-tip
**TRAINER'S TIP — calculator hygiene**

On the TI-30XS MultiView, write any "$X-Y$" variance as $\Var X+\Var Y-2\Cov$ *before* keying numbers — the sign on the cross-term is the single most common slip on this topic. For a Poisson tail like $P(N\le2)$ with $\lambda=5$, bank $e^{-5}$ first with [ 5 [+/−]{.kbd} [2nd]{.kbd} [e^x]{.kbd} [STO▸]{.kbd} [x]{.kbd} [enter]{.kbd} ]{.keystroke}, then evaluate the bracket in one entry — [ [x]{.kbd} [×]{.kbd} ( 1 [+]{.kbd} 5 [+]{.kbd} 5 [x²]{.kbd} [÷]{.kbd} 2 ) [enter]{.kbd} ]{.keystroke} — so you never re-key a rounded constant.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

<figure style="margin:1.25em auto; max-width:150px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket — Jessie, James, and Meowth" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">Jessie, James &amp; Meowth — the misconception, embodied</figcaption>
</figure>

Jessie and James rig two trap-nets across the cave. Net A has output spread $\SD=6$; Net B has $\SD=8$. "When both nets fire together," Meowth declares, "the total spread is just six plus eight — *fourteen!* We'll overwhelm the twerp's whole team!" James paints "$14$" on the launcher. They fire. The nets snap *correlated* — both surge at once — and the combined recoil blows the launcher apart, dropping all of Team Rocket down a chute. "We're blasting off again!"

**Where it fails:** Meowth added **standard deviations** instead of variances, and ignored covariance entirely. Even if the nets were *independent*, the true spread would be $\sqrt{6^2+8^2}=\sqrt{100}=10$, not $14$. With **positive** covariance (the nets surge together) it is *larger* still — but **never** the naive sum of SDs.

**The fix:** standard deviations never add; **variances** add (plus $2\Cov$). Combine on the *variance* scale, then take the square root at the very end. *(You'll audit this exact blunder in Problem C15.21.)*
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

Portfolio risk *is* covariance. An insurer holding thousands of policies cares about the variance of the **total** loss, and that total's variance is dominated by the cross-terms:

$$\Var\!\Big(\sum_i L_i\Big)=\sum_i\Var(L_i)+2\!\sum_{i<j}\Cov(L_i,L_j).$$

**Diversification** — the entire reason insurance and reinsurance work — is the deliberate engineering of *low or negative* covariance between risks, so the pooled total is far steadier than any single policy. A reinsurer pricing a catastrophe treaty must estimate how strongly regional hurricane losses move together; underestimate that covariance and you under-reserve and risk insolvency. Capital-requirement formulas (Solvency II, the NAIC RBC correlation matrix) are literally covariance matrices applied to lines of business.

There is a humbling limit, too. If $n$ identical risks each have variance $\sigma^2$ and a *common positive* pairwise covariance $c$, the **average** loss has variance $\dfrac{\sigma^2}{n}+\dfrac{n-1}{n}c\to c$ as $n\to\infty$. Independent risks ($c=0$) average away to nothing; *correlated* risks leave an irreducible **systematic floor** $c$, no matter how large the book. That is exactly why insurers can diversify idiosyncratic claim noise but **cannot** diversify away a single hurricane hitting every policy at once (Problem C15.16 builds this).

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
**THE VICTORY ROAD CLIMB — your questline.** Oak has handed you the commission: deliver the full risk profile of your team before the registration window closes at dusk. This problem set is one continuous ascent — the **Route Trainer** legs are the lower ledges (mechanics on single pairs and small sums); the **Gym Battle** tier is the mid-mountain boss stretch (true SOA difficulty); the **Elite Challenge** tier is the summit push (integrative) once the medallion is yours. Work it timed (~6 min per Gym Battle problem, less for Route Trainers), then check the **Answer Key** below. Hit the mastery bar (**80%+ with correct method**) to clear the climb and earn the Victory Road medallion. Problems are listed first; full worked solutions follow afterward (never interleaved). Markers: 🔴 routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (the lower ledges — mechanics)

**C15.1.** 🔴 *(Logging the combined push on the entrance ledge.)* Pikachu's strength output $X$ has $\Var(X)=4$ and Charizard's $Y$ has $\Var(Y)=9$. They are **independent**. Find $\Var(X+Y)$.

**C15.2.** 🔴 *(The same two climbers now feed off each other.)* With $\Var(X)=4$, $\Var(Y)=9$ as in C15.1, now $\Cov(X,Y)=2$. Find $\Var(X+Y)$ and $\Var(X-Y)$.

**C15.3.** 🔴 *(Brock converts a Geodude/Onix correlation into a covariance.)* Brock measures Geodude's output $U$ ($\SD=5$) and Onix's output $V$ ($\SD=12$) with correlation $\rho=0.4$. Find $\Cov(U,V)$.

**C15.4.** 🔴 *(Misty's Staryu and Starmie spin-counts.)* Misty reports $\E[X]=3$, $\E[Y]=5$, $\E[XY]=16$. Find $\Cov(X,Y)$ and state whether the two move together or apart.

**C15.5.** 🟡 *(A relay with effort weights on two independent outputs.)* A relay uses weight $a=3$ on output $X$ and $b=-2$ on output $Y$, where $\Var(X)=2$, $\Var(Y)=5$, and $X,Y$ are independent. Find $\Var(3X-2Y)$.

**C15.6.** 🟡 *(Two independent normal climbers; the distribution of their gap.)* $X\sim\Normal(10,4)$ and $Y\sim\Normal(6,9)$ (variances given) are independent. Identify the exact distribution of $X-Y$, including its mean and variance.

**C15.7.** 🔴 *(Wild Rattata in two independent corridors.)* Rattata appear independently as $\Poisson(1.5)$ and $\Poisson(2.5)$. Identify the exact distribution of the total count and state its mean and variance.

**C15.20.** 🟡 *(DECISION — pick the steadier pairing for the final rope team.)* You must rope two of your Pokémon together for the cliff. Each candidate output has $\Var=9$ and $\Var=4$. Pairing A links Charizard+Bulbasaur with $\rho=-0.5$; Pairing B links Charizard+Geodude with $\rho=+0.5$. The rope holds best when the *combined* output is **steadiest** (smallest $\Var(X+Y)$). Compute $\Var(X+Y)$ for each pairing and decide which rope team to send.

> *Questline beat: the lower ledges are cleared. Oak radios the risk profile up the mountain — the boss stretch is next.*

### Gym Battles (the boss stretch — true SOA difficulty)

**C15.8.** 🟡 *(Cave RNG joint pmf of boulders cleared and Onix met.)* The joint pmf of $(X,Y)$ is $p(0,0)=0.2$, $p(1,0)=0.2$, $p(0,1)=0.1$, $p(1,1)=0.3$, $p(2,1)=0.2$. Compute $\Cov(X,Y)$ and the correlation $\rho$.

**C15.9.** 🟡 *(Three-Pokémon vanguard with mixed-sign covariances.)* Your three-Pokémon vanguard pushes a jammed boulder gate first; if the total push swings too wide the gate slams back on them. Their outputs $X_1,X_2,X_3$ have $\Var(X_1)=2$, $\Var(X_2)=3$, $\Var(X_3)=4$; $\Cov(X_1,X_2)=1$, $\Cov(X_1,X_3)=-1$, and $X_2,X_3$ uncorrelated. Oak needs the spread of the combined push before he sends them in: find $\Var(X_1+X_2+X_3)$.

**C15.10.** 🟡 *(Load-weighted team total.)* With the variances and covariances of C15.9, the load-weighted total is $W=X_1+2X_2+3X_3$. Find $\Var(W)$.

**C15.11.** 🔵 *(Two linked cave attributes with a continuous density.)* Two linked cave attributes — a ledge's grip $X$ and its loose-rock risk $Y$ — follow the joint density $f(x,y)=x+y$ on the unit square $0\le x\le1,\ 0\le y\le1$, and Oak needs to know whether better grip tends to come with more loose rock before the team commits. Find $\Cov(X,Y)$. (You may use $\E[X]=\E[Y]=\tfrac{7}{12}$.)

**C15.12.** 🔵 *(RIVAL TRAP — Gary reads $\rho=0$ as "independent.")* Let $X$ be uniform on $\{-1,0,1\}$ (each prob $\tfrac13$) and $Y=X^2$. Gary glances at the data and announces, "$\rho=0$, so $X$ and $Y$ are independent — send them on separate ropes." Show $\Cov(X,Y)=0$, show $X$ and $Y$ are **not** independent, and name Gary's error.

**C15.13.** 🟡 *(Shaft clears only if combined output exceeds 25.)* Charizard's output $X\sim\Normal(14,9)$ and Bulbasaur's $Y\sim\Normal(8,5)$ are independent. Find $P(X+Y>25)$.

**C15.14.** 🔴 *(Two independent gamma climb-times sharing a scale.)* Independent times $\GammaDist(2,\theta)$ and $\GammaDist(3,\theta)$ with common scale $\theta=4$. Identify the distribution of the total time and give its mean and variance.

**C15.15.** 🟡 *(AUDIT — a recon note claims a diversification benefit; verify it.)* A two-route loss portfolio has $\Var(L_1)=100$, $\Var(L_2)=225$, and correlation $\rho=-0.3$. A scout's note claims "the total variance is just $100+225=325$." Compute the **true** $\Var(L_1+L_2)$, state the diversification benefit (variance reduction) over the note's value, and name the scout's error.

**C15.21.** 🟡 *(AUDIT — recycles Team Rocket's launcher blunder.)* Team Rocket's salvaged log reads: "Net A spread $\SD=6$, Net B spread $\SD=8$, both fired together; combined spread $=6+8=14$." Assuming the two nets are **independent**, compute the **correct** combined standard deviation, and name precisely where the log went wrong.

**C15.22.** 🟡 *(AUDIT — a binomial pooling claim to check.)* Two independent scouting sweeps record successful sightings as $\Binom(4,0.3)$ and $\Binom(6,0.3)$. A note asserts the combined count is $\Binom(10,0.6)$. Identify the **correct** distribution of the total, give its mean and variance, and name the note's error.

> *Questline beat: the medallion is yours. The summit push below is optional — but it's where the real climbers test themselves.*

### Elite Challenge (the summit push — integrative / stretch)

**C15.16.** 🔵 *(Six teammates with a common pairwise covariance climb together.)* Each of six teammates has output variance $\sigma^2=4$, and **every** distinct pair has covariance $c=1$. Let $T=\sum_{i=1}^6 X_i$. Derive $\Var(T)$ in terms of $\sigma^2$ and $c$ via the count of pairs, then evaluate it. Also find the correlation $\Corr(X_i,T)$ between any single $X_i$ and the total.

**C15.17.** 🔵 *(A random number of pushes, each expending random strength.)* You make $N\sim\Poisson(3)$ pushes, each expending independent strength $S_i$ with $\E[S]=2$, $\Var(S)=1$, independent of $N$. The total expended is $T=\sum_{i=1}^N S_i$. Using $\E[T]=\E[N]\E[S]$ and $\Var(T)=\E[N]\Var(S)+\Var(N)\E[S]^2$, find $\E[T]$ and $\Var(T)$.

**C15.18.** 🔵 *(Front-pair total and rear-pair total share $X_2$.)* Oak splits the vanguard into a front pair and a rear pair to cross two ledges at once, but the same climber $X_2$ is roped into both pairs — so if one pair lurches, the shared climber drags the other. With $X_1,X_2,X_3$ as in the Gym Battle capstone ($\sigma_1=2,\sigma_2=3,\sigma_3=\sqrt5$; $\rho_{12}=0.5,\rho_{13}=-0.2,\rho_{23}=0$), Oak wants the covariance between the *front-pair total* $A=X_1+X_2$ and the *rear-pair total* $B=X_2+X_3$. Use bilinearity to find $\Cov(A,B)$ so he knows how tightly the two pairs move together.

**C15.19.** 🔵 *(Joint moment of the total.)* Two teammates have $\E[X]=3$, $\E[Y]=5$, $\Var(X)=4$, $\Var(Y)=9$, $\Cov(X,Y)=2$. Find the second moment of the team total $\E[(X+Y)^2]$ and the product moment $\E[XY]$.
:::

## Answers

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

**C15.1** — *(standard) Variance of an independent sum (Entry №04).* Independent ⇒ $\Cov=0$, so $\Var(X+Y)=\Var(X)+\Var(Y)=4+9=\boxed{13}$.

**C15.2** — *(standard) Variance of a sum/difference with covariance (Entry №04).*
$$\Var(X+Y)=4+9+2(2)=\boxed{17}, \qquad \Var(X-Y)=4+9-2(2)=\boxed{9}.$$
Positive covariance inflates the sum, deflates the difference; the variances always **add**.

**C15.3** — *(standard) Recover covariance from correlation (Entry №03).* $\Cov(U,V)=\rho\,\SD(U)\,\SD(V)=0.4(5)(12)=\boxed{24}.$

**C15.4** — *(standard) Covariance from $\E[XY]$ (Entries №01, №02).* $\Cov(X,Y)=\E[XY]-\E[X]\E[Y]=16-(3)(5)=\boxed{1}>0$, so they **move together**.

**C15.5** — *(standard) Variance of a weighted independent combination (Entry №04).* Independent ⇒ no cross-term; weights enter squared (sign vanishes):
$$\Var(3X-2Y)=3^2\Var(X)+(-2)^2\Var(Y)=9(2)+4(5)=18+20=\boxed{38}.$$

**C15.6** — *(standard) Difference of independent normals (Entry №06).* Normals close under linear combinations: $X-Y\sim\Normal(10-6,\ 4+9)=\boxed{\Normal(4,13)}$. Means subtract, variances **add**.

**C15.7** — *(standard) Sum of independent Poissons (Entry №06).* Pool the rates: total $\sim\Poisson(1.5+2.5)=\boxed{\Poisson(4)}$, with $\E=\Var=4$ (Poisson mean = variance).

**C15.20** — *(decision) Variance of a sum, two correlation regimes (Entry №04).* $\Cov=\rho\,\SD_X\SD_Y$ with $\SD_X=3,\SD_Y=2$.
$$\text{Pairing A } (\rho=-0.5):\ \Var(X+Y)=9+4+2(-0.5)(3)(2)=13-6=7.$$
$$\text{Pairing B } (\rho=+0.5):\ \Var(X+Y)=9+4+2(+0.5)(3)(2)=13+6=19.$$
**Send Pairing A** (Charizard+Bulbasaur): the **negative** correlation makes the combined output far steadier ($7<19$). Negative covariance is the rope team's friend — the same diversification idea that drives insurance.

**C15.8** — *(standard) Covariance and correlation from a joint pmf (Entries №01, №02, №03).*
$X$ marginal: $P(0)=0.2+0.1=0.3$, $P(1)=0.2+0.3=0.5$, $P(2)=0.2$. So $\E[X]=0(0.3)+1(0.5)+2(0.2)=0.9$, $\E[X^2]=0+0.5+4(0.2)=1.3$, $\Var(X)=1.3-0.81=0.49$.
$Y$ marginal (indicator): $P(1)=0.1+0.3+0.2=0.6$, so $\E[Y]=0.6$, $\Var(Y)=0.6-0.36=0.24$.
$\E[XY]$ (nonzero only when both $\ge1$): $(1,1)\!:1(0.3)=0.3$; $(2,1)\!:2(0.2)=0.4$, so $\E[XY]=0.7$.
$$\Cov=0.7-(0.9)(0.6)=0.7-0.54=\boxed{0.16}, \qquad \rho=\frac{0.16}{\sqrt{0.49}\sqrt{0.24}}=\frac{0.16}{(0.7)(0.4899)}\approx\boxed{0.467}.$$

**C15.9** — *(standard) Variance of a sum of three with mixed-sign cross-terms (Entry №04).*
$$\Var(X_1+X_2+X_3)=2+3+4+2(\Cov_{12}+\Cov_{13}+\Cov_{23})=9+2(1-1+0)=\boxed{9}.$$

**C15.10** — *(standard) Variance of a weighted three-variable combination (Entry №04).* Weights $a_1=1,a_2=2,a_3=3$.
Diagonal: $1^2(2)+2^2(3)+3^2(4)=2+12+36=50$.
Cross: $2[(1)(2)(1)+(1)(3)(-1)+(2)(3)(0)]=2[2-3+0]=-2$.
$$\Var(W)=50-2=\boxed{48}.$$

**C15.11** — *(standard) Continuous covariance via a joint moment (Entries №01, №02).*
$$\E[XY]=\int_0^1\!\!\int_0^1 xy(x+y)\,dx\,dy=\int_0^1\!\!\int_0^1 (x^2y+xy^2)\,dx\,dy.$$
Inner over $x$: $\tfrac{y}{3}+\tfrac{y^2}{2}$. Outer over $y$: $\tfrac13\cdot\tfrac12+\tfrac12\cdot\tfrac13=\tfrac16+\tfrac16=\tfrac13$.
$$\Cov=\E[XY]-\E[X]\E[Y]=\tfrac13-\left(\tfrac{7}{12}\right)^2=\tfrac13-\tfrac{49}{144}=\tfrac{48-49}{144}=\boxed{-\tfrac{1}{144}}\approx-0.00694.$$

**C15.12** — *(rival_trap) Uncorrelated-but-dependent counterexample (Entry №05).*
$\E[X]=0$ by symmetry. $\E[XY]=\E[X\cdot X^2]=\E[X^3]=\tfrac13\big((-1)^3+0+1^3\big)=0$. So $\Cov(X,Y)=0-0=\boxed{0}$, hence $\rho=0$.
Not independent: $P(X=0,Y=1)=0$, but $P(X=0)P(Y=1)=\tfrac13\cdot\tfrac23=\tfrac29\ne0$ (knowing $X=0$ forces $Y=0$). **Gary's error:** he ran the one-way street **backward**. Independence $\Rightarrow\rho=0$, but $\rho=0\not\Rightarrow$ independence — correlation sees only *linear* association, and $Y=X^2$ is purely curved.

**C15.13** — *(standard) Sum of independent normals + tail (Entry №06).*
$X+Y\sim\Normal(14+8,\ 9+5)=\Normal(22,14)$, $\SD=\sqrt{14}\approx3.742$.
$$z=\frac{25-22}{3.742}\approx0.80, \qquad P(X+Y>25)=P(Z>0.80)\approx1-0.7881=\boxed{0.2119}.$$

**C15.14** — *(standard) Sum of same-scale Gammas (Entry №06).* Common scale $\theta=4$ ⇒ shapes add: total $\sim\GammaDist(2+3,4)=\boxed{\GammaDist(5,4)}$. Mean $=\alpha\theta=5(4)=20$; variance $=\alpha\theta^2=5(16)=80$.

**C15.15** — *(audit) Diversification via negative covariance (Entry №04).*
$\Cov(L_1,L_2)=\rho\,\SD_1\SD_2=(-0.3)(10)(15)=-45$.
$$\Var(L_1+L_2)=100+225+2(-45)=325-90=\boxed{235}.$$
The note's value $325$ omits the cross-term entirely. Diversification benefit $=325-235=\boxed{90}$ reduction in variance (a $27.7\%$ cut), purely from the negative correlation. **Scout's error:** treating the routes as uncorrelated (dropping $2\Cov$) when they are negatively correlated — variances do **not** "just add" unless $\Cov=0$.

**C15.21** — *(audit) Standard deviations never add — Team Rocket's launcher (Entry №04).* The correct combination is on the **variance** scale:
$$\Var = 6^2 + 8^2 = 36 + 64 = 100, \qquad \SD = \sqrt{100} = \boxed{10}.$$
**Where the log went wrong:** it added standard deviations ($6+8=14$). SDs never add; **variances** add (plus $2\Cov$ if linked), and you take the square root only at the very end. Even independent, the true spread is $10$, not $14$ — and with positive covariance it would be larger still, but never the naive SD sum.

**C15.22** — *(audit) Binomial pooling requires a common $p$ and adds the $n_i$ (Entry №06).* Both sweeps share $p=0.3$, so the total is
$$\boxed{\Binom(4+6,\ 0.3)=\Binom(10,0.3)}, \qquad \E=np=10(0.3)=3, \quad \Var=np(1-p)=10(0.3)(0.7)=2.1.$$
**Note's error:** it added the $p$'s ($0.3+0.3=0.6$). Same-$p$ binomials add the **$n$'s**, not the $p$'s; the success probability is unchanged by pooling.

**C15.16** — *(standard) Equicorrelated sum, count of pairs (Entry №04).*
General: $\Var(T)=n\sigma^2+2\binom{n}{2}c=n\sigma^2+n(n-1)c$. With $n=6,\sigma^2=4,c=1$:
$$\Var(T)=6(4)+6(5)(1)=24+30=\boxed{54}.$$
Correlation of $X_i$ with $T$: $\Cov(X_i,T)=\Var(X_i)+\sum_{j\ne i}\Cov(X_i,X_j)=4+5(1)=9$, so
$$\Corr(X_i,T)=\frac{9}{\sqrt{4}\sqrt{54}}=\frac{9}{2(7.348)}\approx\boxed{0.612}.$$

**C15.17** — *(standard) Compound-distribution moments (Entry №04).*
$\E[T]=\E[N]\E[S]=3(2)=\boxed{6}$.
For $N\sim\Poisson(3)$: $\E[N]=\Var(N)=3$.
$$\Var(T)=\E[N]\Var(S)+\Var(N)\E[S]^2=3(1)+3(2)^2=3+12=\boxed{15}.$$
(Poisson check: $\Var(T)=\lambda\,\E[S^2]=3(\Var S+\E[S]^2)=3(1+4)=15$ ✓.)

**C15.18** — *(standard) Covariance of two overlapping sums via bilinearity (Entry №02).*
$\Cov_{12}=0.5(2)(3)=3$, $\Cov_{13}=-0.2(2)\sqrt5\approx-0.8944$, $\Cov_{23}=0$, $\Var(X_2)=9$.
By bilinearity, $\Cov(A,B)=\Cov(X_1+X_2,\;X_2+X_3)=\Cov(X_1,X_2)+\Cov(X_1,X_3)+\Cov(X_2,X_2)+\Cov(X_2,X_3)$
$$=3+(-0.8944)+9+0=\boxed{11.106}.$$
The shared $X_2$ contributes its full variance $9$ — overlap creates strong positive covariance between the two sums.

**C15.19** — *(standard) Joint moment of the total (Entries №01, №04).*
Product moment: $\E[XY]=\Cov(X,Y)+\E[X]\E[Y]=2+(3)(5)=\boxed{17}$.
Second moment of the total via $\E[W^2]=\Var(W)+\E[W]^2$ with $W=X+Y$:
$$\Var(X+Y)=4+9+2(2)=17, \quad \E[X+Y]=8, \quad \E[(X+Y)^2]=17+8^2=\boxed{81}.$$
(Check by expansion: $\E[X^2]+2\E[XY]+\E[Y^2]=13+2(17)+34=81$ ✓.)

### Quick-Answer Table

| # | Answer | | # | Answer |
|---|---|---|---|---|
| C15.1 | $13$ | | C15.12 | $\Cov=0$, dependent (Gary wrong) |
| C15.2 | $\Var(X{+}Y)=17$, $\Var(X{-}Y)=9$ | | C15.13 | $\approx0.212$ |
| C15.3 | $\Cov=24$ | | C15.14 | $\GammaDist(5,4)$, $\E=20,\Var=80$ |
| C15.4 | $\Cov=1$ (together) | | C15.15 | $\Var=235$; benefit $90$ |
| C15.5 | $38$ | | C15.16 | $\Var(T)=54$, $\rho\approx0.612$ |
| C15.6 | $\Normal(4,13)$ | | C15.17 | $\E[T]=6$, $\Var(T)=15$ |
| C15.7 | $\Poisson(4)$, $\E=\Var=4$ | | C15.18 | $\Cov(A,B)\approx11.106$ |
| C15.8 | $\Cov=0.16$, $\rho\approx0.467$ | | C15.19 | $\E[XY]=17$, $\E[(X{+}Y)^2]=81$ |
| C15.9 | $9$ | | C15.20 | A $=7$, B $=19$; send A |
| C15.10 | $48$ | | C15.21 | $\SD=10$ (not $14$) |
| C15.11 | $-\tfrac{1}{144}\approx-0.00694$ | | C15.22 | $\Binom(10,0.3)$, $\E=3,\Var=2.1$ |
:::

## Badge Earned — the Victory Road Medallion

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with Victory Road cleared and the Indigo Plateau ahead" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Victory Road — the Indigo Plateau in sight.</strong> The team climbed as one total; seven badges in hand, only Giovanni's Earth Badge left to earn.</figcaption>
</figure>

You handed Oak the honest risk profile, the team held together on the cliff, and you cleared Victory Road before dusk — the Indigo Plateau is now in sight. You earn the **Victory Road Cleared** medallion when you can, unaided:

**Mastery checklist — tick each before you move on (mapped 1-to-1 to the SOA outcomes):**

- ☐ **(3e)** I can compute a **joint moment** $\E[XY]$ or $\E[g(X,Y)]$ off a joint table or density, turn it into **covariance** $\Cov(X,Y)=\E[XY]-\E[X]\E[Y]$, and convert a given correlation $\rho$ into a covariance with $\Cov=\rho\,\sigma_X\sigma_Y$ — and back. *(Rematch: Concepts 1–3, WE 15.1, Problems C15.3, C15.4, C15.8, C15.11, C15.19.)*
- ☐ **(3e)** I can state and use the **independence/correlation one-way street**: independence $\Rightarrow\rho=0$, but $\rho=0\not\Rightarrow$ independence, with the $Y=X^2$ counterexample at hand. *(Rematch: Concept 5, Problem C15.12.)*
- ☐ **(3g)** I can find the **variance of any linear combination** $\Var(\sum a_iX_i)=\sum a_i^2\Var(X_i)+2\sum_{i<j}a_ia_j\Cov(X_i,X_j)$, getting every cross-term and sign right — including $\Var(X-Y)=\Var X+\Var Y-2\Cov$ — and I never add standard deviations. *(Rematch: Concept 4, WE 15.2–15.3, Gym Battle (a), Problems C15.9, C15.10, C15.15, C15.20, C15.21.)*
- ☐ **(3h)** I can compute **means and variances of linear combinations** in the independent and normal special cases, and recognize and collapse **sums of independent in-family distributions** (Normal, Poisson, same-scale Gamma, same-$p$ Binomial) via the MGF/parameter-pooling rule, then finish a single one-variable calculation. *(Rematch: Concept 6, WE 15.5, Gym Battle (b)–(d), Problems C15.6, C15.7, C15.13, C15.14, C15.22.)*

> **Gym rematch pointers (🧴 Potion).** Missed a covariance-from-a-table? Re-run WE 15.1, then C15.8, C15.11. Forgot the cross-term or added SDs? Concept 4, Beat 4, then C15.2, C15.20, C15.21. Read $\rho=0$ as independence? Concept 5, then C15.12. Tripped on in-family pooling? Concept 6, WE 15.5, then C15.6, C15.7, C15.14, C15.22.

*Onward — the climb is cleared. Ahead lie order statistics and the Central Limit Theorem, where these sums of independent variables finally reveal the bell curve that every total secretly approaches.*

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
