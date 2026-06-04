<!--
  file: ch07_center_spread
  tier: A
  outcomes: 2b,2c,2d
  draft1_source: drafts/chapters_draft1/ch05_vermilion_city.md
  maps_to: Vermilion, Lt. Surge — expectation/variance/MGF/Darth Vader
-->

# Center & Spread {.type-electric}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with the journey now at Vermilion City on the southern coast; Cerulean and the Nugget Bridge lie to the north." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 10 — you have crossed the Nugget Bridge and reached <strong>Vermilion City</strong>, the harbor town, the docked S.S. Anne, and Lt. Surge's Electric gym: the home of the <em>Thunder Badge</em>.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "A Number Left to Chance"**

The S.S. Anne rolls beneath you, a floating city of trainers swapping Pokémon and trading battle stories. You came aboard to trade your Butterfree — but Team Rocket has other plans. Somewhere below the waterline a charge has cracked the hull, and the captain's voice crackles over the speakers: *"Flooding detected. Evacuate."*

You sprint for the upper deck, Pikachu on your shoulder, and run straight into a problem you cannot blink away. The first mate is holding a clipboard. "Hull's failing at *random*," he shouts over the alarm. "Engineering can't tell me *when* the lower decks go under — only the **distribution** of the time until they flood. I need the expected minutes we've got. Give me one number and I can time the lifeboats."

He shoves the clipboard at you. On it: a falling curve labeled $S(t) = P(T > t)$ — "the probability the hull is still holding at time $t$." No average printed. No table. Just a function of $t$ and a line sliding toward zero.

Pikachu's cheeks spark. You realize you have never actually *defined* the thing the first mate wants. Back in Cerulean you learned to combine the probabilities of *events*. But here the unknown isn't an event — it's a **number whose value is left to chance**: the minutes until the flood. What is its *average*? How wildly does it *swing*? And could you really pull the expected escape time straight out of that survival curve — without ever writing down a density?

The deck tilts. The first mate is waiting. **How do you find the average of a number you cannot predict — and how do you measure how far it strays from that average?**
:::

## Where You Are — 60-Second Retrieval

You're holding the **Cascade Badge** from Cerulean, and the **Boulder Badge** before it. In the last chapter you learned to read evidence *backward* — Bayes, total probability, conditioning. The load-bearing idea you must carry forward is the one underneath all of it: a **random variable** $X$ is *a number whose value is settled only when chance resolves*, and a probability gets attached to each value it can take.

In the chapter just before this one you met that object's anatomy: its **pmf** $p(x)=P(X=x)$ (for a discrete $X$, the probability sitting on each value), its **pdf** $f(x)$ (for a continuous $X$, how thickly probability is smeared along the line), and the rule that both must be nonnegative and total to $1$. *This* chapter takes that object and asks the two questions every actuary asks of any uncertain quantity: **where is its center, and how far does it spread?** Take sixty seconds and prove you still own the setup before reading on.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the last chapter**

Answer from memory; if any feels shaky, flip back before continuing.

1. A discrete $X$ has $p(1)=0.2,\ p(2)=0.5,\ p(3)=0.3$. Is this a valid pmf, and what is $P(X\ge 2)$? *(Answer: yes — nonnegative, sums to $1$; $P(X\ge2)=0.8$.)*
2. A density is $f(x)=2x$ on $0\le x\le 1$. What is $P(X>\tfrac12)$? *(Answer: $\int_{1/2}^{1}2x\,dx = 1-\tfrac14=\tfrac34$.)*
3. What does "$\int_a^b f(x)\,dx$" *mean* in words? *(Answer: the probability $X$ lands between $a$ and $b$ — the area under the density over that stretch.)*

All three instant? You're ready. Any hesitation? The retrieval *is* the lesson — go reclaim it, then come back. Everything below is "what do you *do* with $p(x)$ and $f(x)$ once you have them."
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice comes through the Pokédex's Actuary Mode as you climb toward the deck. "Ash — every price an actuary ever quotes is built from two numbers: the **average** of an uncertain quantity and its **spread** around that average. A premium is an average loss plus a margin for the spread. Master *center and spread* here, in Vermilion, and the named distributions waiting in the next towns become bookkeeping — each one is just a particular shape with a known mean and variance. This is a **Tier A** chapter. Take it slowly; the whole univariate block stands on it."

By the end of this chapter you will be able to:

- **Compute** the expectation $\E[X]$ and $\E[g(X)]$ of a random variable, and use **linearity** $\E[aX+b]=a\E[X]+b$. *(Outcome 2b.)*
- **Compute** the variance via $\Var(X)=\E[X^2]-(\E[X])^2$, the standard deviation, the coefficient of variation, and apply $\Var(aX+b)=a^2\Var(X)$. *(Outcome 2c.)*
- **Derive** moments from a **moment generating function** by differentiation, and recognize an MGF's kernel to read off a distribution. *(Outcome 2d.)*
- **Deploy** the survival-function ("Darth Vader") rule $\E[X]=\int_0^\infty S(x)\,dx$ for a nonnegative $X$, and its discrete analog.

> *Exam-weight signpost.* Expectation, variance, and the MGF are tested on **nearly every** Exam P sitting and feed directly into the insurance-pricing and distribution chapters. The Darth Vader rule is a recurring time-saver. This chapter earns the full treatment.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own All of Vermilion?**

Already fluent? Prove it. Work these four, ~5 minutes each, *with correct method*:

1. A density is $f(x)=\tfrac{3}{8}x^2$ on $0\le x\le 2$. Find $\E[X]$ and $\Var(X)$.
2. $\E[X]=10$, $\Var(X)=9$. Let $Y=3X-2$. Find $\E[Y]$, $\Var(Y)$, $\SD(Y)$.
3. $M_X(t)=(1-3t)^{-4}$ for $t<\tfrac13$. Find $\E[X]$ and $\Var(X)$.
4. A nonnegative $T$ has survival function $S(t)=e^{-t/10}$, $t\ge0$. Find $\E[T]$ *without* recovering the density.

*(Answers: $\E[X]=1.5,\ \Var(X)=0.15$; $\E[Y]=28,\ \Var(Y)=81,\ \SD(Y)=9$; $\E[X]=12,\ \Var(X)=36$; $\E[T]=10$.)* Four for four with the right reasoning? **Skip to the Gym Challenge** and claim the badge. Any miss or hesitation? The teaching below was built exactly for you — and each concept has its own skip-gate, so even a partial owner loses no time.
:::

---

Five ideas build on one another here, in increasing difficulty. We teach them **in order**, each with its own "do you already own this?" skip-check, then the full nine-beat lesson, then a Pokédex Entry you can carry into the exam:

1. **Expectation** — the center of an uncertain number *(the foundation everything else uses)*
2. **$\E[g(X)]$ and linearity** — averaging a *function* of $X$, and the one shortcut that's always legal
3. **Variance and standard deviation** — measuring the spread, and the computational shortcut
4. **The moment generating function** — one function that hands you every moment
5. **The survival-function (Darth Vader) rule** — the mean straight off the survival curve

## Concept 1 — Expectation: The Center of an Uncertain Number

::: concept-gate
**DO YOU ALREADY OWN THIS? — Expectation**

A prize wheel pays \$1, \$2, or \$4 with probabilities $0.5$, $0.3$, $0.2$. Over thousands of spins, what is the *average* payout per spin?

If you immediately answered **\$1.90** (via $1(0.5)+2(0.3)+4(0.2)=0.5+0.6+0.8$, *not* the plain average $\tfrac{1+2+4}{3}\approx2.33$), you own expectation — **skip to Concept 2**. If you reached for the plain average, or you're unsure why each value is weighted by its probability, this section is for you.
:::

**Beat 1 — The one-sentence idea.** *The expectation of $X$ is its long-run average: every value it can take, weighted by how likely that value is.*

**Beat 2 — Anchor + concrete instance.** A random variable is a number left to chance. "Where is it centered?" is the most basic question you can ask about it — and the answer is *not* the plain average of its possible values, because some values happen far more often than others.

Here is the story, with real numbers. A vending machine on the S.S. Anne promenade pays out a small prize $X$ in Poké-dollars each time you buy a Fresh Water. Engineering's log says $X$ takes the value **\$1 half the time, \$2 thirty percent of the time, and \$5 twenty percent of the time**:

$$p(1)=0.5,\qquad p(2)=0.3,\qquad p(5)=0.2.$$

*Over thousands of purchases, what does a prize cost the machine on average?*

**Beat 3 — Reason through it in plain words.** Imagine **1000 purchases.** By the probabilities, about **500** pay \$1, **300** pay \$2, and **200** pay \$5. The total paid out is

$$500(\$1) + 300(\$2) + 200(\$5) = \$500 + \$600 + \$1000 = \$2100,$$

so the average per purchase is $\$2100 / 1000 = \$2.10$. Notice what happened: dividing each *count* by $1000$ turns it back into a *probability* ($\tfrac{500}{1000}=0.5$, and so on), so the average is exactly the **probability-weighted sum**:

$$\E[X] = 1(0.5) + 2(0.3) + 5(0.2) = 0.5 + 0.6 + 1.0 = 2.10.$$

> **⚠ Watch this derail (intentional).** A tempting mental slip is to mis-multiply the last term as $5(0.2)=1.0$ → "$0.5+0.6+0.5=1.6$" or to drop it to $0.5+0.6=1.1$. If your weighted sum and your count-version (\$2.10) ever *disagree*, the method is fine — it's mental arithmetic. The fix is always the same: re-add termwise, and trust the count picture. Here every term checks: $5\times0.2=1.0$ exactly, so the answer is \$2.10. *(We surface this on purpose; it is the exact slip the exam punishes.)*

**Beat 4 — Surface and dismantle the tempting wrong idea.** The natural mistake is the **plain average** of the three prize values:

$$\frac{1 + 2 + 5}{3} = 2.67. \qquad\textbf{(wrong — ignores the weights)}$$

That would be right *only if* all three prizes were equally likely. They aren't — \$1 comes up half the time, \$5 only a fifth. The plain average secretly assigns weight $\tfrac13$ to each value; the true mean weights each value by *its own* probability. Whenever the outcomes aren't equally likely, the plain average throws away the very information the distribution gives you. **The mean is a probability-weighted average, never a plain one.**

**Beat 5 — Translate into notation, one glyph at a time.** We want "the average value of $X$." We write it $\E[X]$:

$$\E[X] \qquad\text{read aloud: ``the expectation of } X\text{,'' or ``the expected value of } X\text{.''}$$

The letter $\E$ is an *operator* — it eats a random variable and returns a single ordinary number (its center). Inside, the recipe "value times its probability, added up over all values" uses the summation sign you met in the last chapter:

$$\sum_{x} \qquad\text{read aloud: ``the sum over all values } x \text{ of'' } (\text{just: add these up}).$$

So for our discrete prize,

$$\E[X] = \sum_x x\,p(x) = 1(0.5)+2(0.3)+5(0.2) = 2.10.$$

For a **continuous** $X$ there is no list of values to add — probability is *smeared* with density $f(x)$, so the sum becomes an integral, the continuous cousin of $\sum$. The symbol $\int$ reads **"the integral of,"** and you should hear it as *"add up, over a continuum"*:

$$\E[X] = \int_{-\infty}^{\infty} x\,f(x)\,dx \qquad\text{read aloud: ``the integral of } x \text{ times its density, over all } x\text{.''}$$

Each tiny slice $f(x)\,dx$ is "the probability $X$ sits near $x$," and $x$ times that slice is its contribution to the average — exactly the discrete recipe with the sum replaced by an integral.

**Beat 6 — Generalize: derive the formula from the instance.** We did not invent the formula; we *compressed* the count-reasoning. "Average over many trials" $=$ "$\sum$ (value $\times$ fraction of trials at that value)," and "fraction of trials at value $x$" *is* $p(x)$ in the long run. Replace each count-fraction with its probability and you have

$$\boxed{\;\E[X] = \sum_x x\,p(x)\ \ (\text{discrete}),\qquad \E[X] = \int_{-\infty}^{\infty} x\,f(x)\,dx\ \ (\text{continuous}).\;}$$

The discrete and continuous formulas are *one idea* — value weighted by probability, totaled — wearing two notations.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the discrete vending machine, $\E[X]=2.10$.
- *Continuous twist:* the time-to-flood $T$ has density $f(t)=\tfrac{1}{10}e^{-t/10}$ on $t\ge0$. Then
$$\E[T]=\int_0^\infty t\cdot\tfrac{1}{10}e^{-t/10}\,dt = 10 \text{ minutes}$$
(using the gamma identity $\int_0^\infty t\,e^{-t/\theta}\,dt=\theta^2$ with $\theta=10$). Same recipe — value times density, integrated.
- *Symmetry shortcut:* if the density is symmetric about a point $c$ (mirror image on each side), the mean *is* $c$ — no integral needed. A density $f(x)=\tfrac34 x(2-x)$ on $[0,2]$ is symmetric about $x=1$, so $\E[X]=1$ on sight.
- *Edge:* a mean can be **infinite**. If the tail of $f$ is heavy enough that $\int x f(x)\,dx$ diverges, $\E[X]$ does not exist — a warning you will meet again with heavy-tailed losses.

**Beat 8 — Picture it.** Expectation is the **balance point** of the distribution: pile the probability on a seesaw and $\E[X]$ is where it balances.

<figure>
<img src="../../assets/diagrams/ch07_expectation_balance.png" alt="A horizontal axis acting as a seesaw. For the discrete prize, three weighted blocks sit at x=1 (height 0.5), x=2 (height 0.3), and x=5 (height 0.2); a triangular fulcrum sits at x=2.10, the balance point. Beside it, a continuous density curve with its fulcrum under the mean, showing E[X] as the center of mass." style="width:80%; max-width:560px; display:block; margin:1em auto;">
<figcaption>Expectation is the center of mass: the fulcrum that balances the probability. The lone \$5 prize, though rare, sits far out and tugs the balance point to $2.10$ — well above the most common value, \$1.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now take any pmf or pdf and find the center of the distribution — the long-run average — by weighting each value by its probability and totaling. That single number is the first thing every pricing problem needs.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Expectation (the Mean)**

$$\E[X] = \sum_x x\,p(x)\ \ (\text{discrete}),\qquad \E[X] = \int_{-\infty}^{\infty} x\,f(x)\,dx\ \ (\text{continuous}).$$

*In plain terms:* the mean is the probability-weighted average — each value times its probability, totaled. It is the balance point (center of mass) of the distribution, **not** the plain average of the possible values.

*Recognition cue:* the words **"average," "expected," "mean," "fair value," "long-run."** Weight each value by its probability and add (or integrate). A rare extreme value still pulls the mean toward itself.
:::

## Concept 2 — $\E[g(X)]$ and Linearity

::: concept-gate
**DO YOU ALREADY OWN THIS? — Functions of $X$ and Linearity**

A jolt $X$ (hundreds of volts) is equally likely $1$ or $3$, so $\E[X]=2$. A "charged" attack does $X^2$ hundred volts. Is the average charged damage $\E[X^2]$ equal to $\E[X]^2 = 4$?

If you answered **"no — $\E[X^2]=\tfrac12(1)+\tfrac12(9)=5\ne4$, you weight $g(x)$ by the same probabilities"** and you know $\E[3X-2]=3\E[X]-2=4$, **skip to Concept 3**. If you were tempted to square the mean, read on — this is the single most-punished slip in the chapter.
:::

**Beat 1 — The one-sentence idea.** *To average a function $g(X)$, weight each $g(x)$ by the same probability $X$ assigns to $x$ — and for the special case $g(x)=ax+b$, you may pull the constants straight out.*

**Beat 2 — Anchor + concrete instance.** Concept 1 averaged $X$ itself. But pricing rarely wants $X$ raw — it wants a *transformed* quantity: a squared value, a scaled-and-shifted payout, a deductible applied. So we need to average $g(X)$, a function of the random number.

Lt. Surge's Raichu delivers a jolt $X$ (hundreds of volts) that is **equally likely to be $1$ or $3$**: $p(1)=p(3)=\tfrac12$, so $\E[X]=\tfrac12(1)+\tfrac12(3)=2$. A *charged* attack does $g(X)=X^2$ hundred volts, and the gym's payout converter pays $h(X)=3X-2$ Poké-dollars. *What is the average charged damage $\E[X^2]$, and the average payout $\E[3X-2]$?*

**Beat 3 — Reason through it in plain words.** The charged attack is $X^2$. When $X=1$ it does $1^2=1$; when $X=3$ it does $3^2=9$. These two values still happen with probability $\tfrac12$ each, so average them with *those same weights*:

$$\E[X^2] = \tfrac12(1) + \tfrac12(9) = 0.5 + 4.5 = 5.$$

For the payout $3X-2$: when $X=1$ it pays $3(1)-2=1$; when $X=3$ it pays $3(3)-2=7$; average $\tfrac12(1)+\tfrac12(7)=4$. Notice that $4 = 3(2)-2 = 3\E[X]-2$ — for this *linear* transform, you could have pulled the $3$ and the $-2$ straight out.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is to first average $X$ and *then* plug into $g$:

$$\E[X^2] \overset{?}{=} \big(\E[X]\big)^2 = 2^2 = 4. \qquad\textbf{(wrong)}$$

But the true value is $5$, not $4$. Squaring is *bending* the number line — it stretches the big values ($3\to9$) much more than the small ones ($1\to1$) — so averaging *after* you bend is not the same as bending the average. In general

$$\E[g(X)] \ne g(\E[X]) \quad\text{for a nonlinear } g.$$

This is **Jensen's trap**, and the gap here, $5-4=1$, is no accident — it is exactly the variance you'll meet in the next concept. The *only* $g$ for which you may safely "plug in the mean" is a **linear** one, $g(x)=ax+b$, where the bending is just a uniform stretch-and-shift.

**Beat 5 — Translate into notation, one glyph at a time.** The rule for averaging *any* function is the **Law of the Unconscious Statistician** (LOTUS) — so named because you can compute $\E[g(X)]$ without ever finding the distribution of $g(X)$, "unconsciously" reusing $X$'s own probabilities:

$$\E[g(X)] = \sum_x g(x)\,p(x)\quad\text{or}\quad \int_{-\infty}^{\infty} g(x)\,f(x)\,dx.$$

Read it: *"average $g(x)$, weighting by the probability $X$ puts on $x$."* For the linear special case $g(x)=ax+b$ (here $a,b$ are plain constants), this collapses to **linearity of expectation**:

$$\E[aX+b] = a\,\E[X] + b \qquad\text{read aloud: ``the average of a scaled, shifted } X \text{ is the scaled, shifted average.''}$$

More generally $\E[g_1(X)+g_2(X)] = \E[g_1(X)] + \E[g_2(X)]$ — **expectation splits across sums and pulls out constants, always.**

**Beat 6 — Generalize: derive linearity from LOTUS.** Linearity is not a separate axiom — it falls out of LOTUS with $g(x)=ax+b$. Split the sum and pull the constants:

$$\E[aX+b] = \sum_x (ax+b)\,p(x) = a\underbrace{\sum_x x\,p(x)}_{\E[X]} + b\underbrace{\sum_x p(x)}_{=\,1} = a\,\E[X] + b.$$

The last step used $\sum_x p(x)=1$ (a valid pmf totals to one). The constant $a$ slides out of the sum because it multiplies every term; the $+b$ contributes $b$ times the total probability, which is $b$. The same two moves with an integral give the continuous version. **That is why linearity is always legal and squaring is not: only $ax+b$ survives the pull-out cleanly.**

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $\E[X^2]=5$ via LOTUS, as above.
- *Linear twist:* $\E[3X-2]=3(2)-2=4$ — constants out, no LOTUS sum needed.
- *Continuous LOTUS:* for $X$ with density $f$, the average of $\sqrt{X}$ is $\int_0^\infty \sqrt{x}\,f(x)\,dx$ — you weight $\sqrt{x}$, never take $\sqrt{\E[X]}$.
- *Edge (the trap, sharpened):* $\E[1/X]\ne 1/\E[X]$, $\E[e^X]\ne e^{\E[X]}$ — any time $g$ curves, you must average *after* applying $g$. The MGF in Concept 4 is literally $\E[e^{tX}]$, computed the LOTUS way.

**Beat 8 — Picture it.** The figure shows *why* bending-then-averaging differs from averaging-then-bending for a curved $g$.

<figure>
<img src="../../assets/diagrams/ch07_jensen_lotus.png" alt="A parabola y=x^2 over the x-axis. The two equally likely inputs x=1 and x=3 are marked; their outputs 1 and 9 sit on the curve. The average of the outputs, 5, is marked on the y-axis. Separately, the mean input x=2 maps to 4 on the curve. A bracket shows the gap of 1 between 5 (E[X^2], averaging after bending) and 4 (g(E[X]), bending the average), labeled 'this gap is the variance'." style="width:80%; max-width:560px; display:block; margin:1em auto;">
<figcaption>Why $\E[g(X)]\ne g(\E[X])$ for a curved $g$: average the <em>outputs</em> $1$ and $9$ to get $5$ (correct), versus map the mean input $2$ to $4$ (the trap). The gap, $5-4=1$, is exactly $\Var(X)$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now average any function of $X$ by weighting $g(x)$ with $X$'s probabilities (LOTUS), pull constants through a linear transform (linearity), and you will never again square the mean when you meant to mean the square.

::: pokedex-entry
**POKÉDEX ENTRY №02 — $\E[g(X)]$ (LOTUS) and Linearity**

$$\E[g(X)] = \sum_x g(x)\,p(x)\quad\text{or}\quad \int_{-\infty}^{\infty} g(x)\,f(x)\,dx.$$
$$\E[aX+b] = a\,\E[X]+b,\qquad \E[g_1(X)+g_2(X)]=\E[g_1(X)]+\E[g_2(X)].$$

*In plain terms:* to average a function of $X$, weight $g(x)$ by $X$'s own probabilities — do **not** plug the mean into $g$. The single exception is a linear $g$, where constants pull straight out.

*Recognition cue:* a transformed quantity — $X^2$, $\sqrt X$, a payout $aX+b$, $e^{tX}$. Weight $g(x)$, never $g(\E[X])$. For $aX+b$, scale and shift the mean directly.
:::

## Concept 3 — Variance and Standard Deviation

::: concept-gate
**DO YOU ALREADY OWN THIS? — Variance**

$X$ is equally likely $1$ or $3$. You already have $\E[X]=2$ and $\E[X^2]=5$. What is $\Var(X)$, and what is $\Var(3X-2)$?

If you answered **$\Var(X)=5-2^2=1$** and **$\Var(3X-2)=3^2\cdot1=9$** (the $-2$ doesn't matter), **skip to Concept 4**. If you computed $\Var$ as $\E[X^2]=5$ without subtracting $\E[X]^2$, or you let the $+b$ change the variance, read on.
:::

**Beat 1 — The one-sentence idea.** *Variance is the average squared distance from the mean — it measures how far the values typically stray from the center.*

**Beat 2 — Anchor + concrete instance.** Concept 1 found the center; but two distributions can share a center and feel completely different — one tightly clustered, one wildly scattered. *Spread* is the second number every price needs. We measure it by asking: on average, how far is $X$ from its own mean?

Stay with Surge's jolt: $X$ is equally likely $1$ or $3$, $\E[X]=2$. *How far does the jolt typically stray from $2$?*

**Beat 3 — Reason through it in plain words.** The deviations from the mean are $1-2=-1$ and $3-2=+1$. If we just *averaged* the deviations we'd get $\tfrac12(-1)+\tfrac12(+1)=0$ — the positives and negatives cancel, every time, by the very definition of the mean. Useless. So **square** each deviation first (killing the sign), then average:

$$\Var(X) = \tfrac12(-1)^2 + \tfrac12(+1)^2 = \tfrac12(1) + \tfrac12(1) = 1.$$

The jolt sits, on average, a squared-distance of $1$ from its center. Taking the square root undoes the squaring and returns to volt-units: the **standard deviation** is $\sqrt{1}=1$ (i.e. $100$ volts).

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two traps live here. First, the one above: averaging the *signed* deviations gives $0$ always — you must square first. Second, and far more common on the exam: computing $\E[X^2]$ and **stopping there**, forgetting to subtract:

$$\Var(X) \overset{?}{=} \E[X^2] = 5. \qquad\textbf{(wrong — forgot the }-(\E[X])^2\text{)}$$

The true variance is $1$, not $5$. The quantity $\E[X^2]=5$ is the average *squared value*, measured from **zero**; variance measures spread from the **mean**, so you must remove the part of $\E[X^2]$ that is just "the mean being far from zero." That correction is exactly $(\E[X])^2 = 4$, leaving $5-4=1$. Forgetting the $-(\E[X])^2$ is the single most frequent variance error; **the second moment is not the variance.**

**Beat 5 — Translate into notation, one glyph at a time.** Name the mean $\mu$ (Greek "mu," the standard symbol for $\E[X]$). Variance is the *expected squared deviation*:

$$\Var(X) = \E\!\big[(X-\mu)^2\big] \qquad\text{read aloud: ``the average of the squared distance from the mean.''}$$

This is just LOTUS (Entry №02) with $g(x)=(x-\mu)^2$. The **standard deviation** is its square root, written $\SD(X)$ or $\sigma$ ("sigma"):

$$\SD(X) = \sigma = \sqrt{\Var(X)}.$$

A scale-free version, handy for comparing spreads of quantities with very different sizes, is the **coefficient of variation** — the standard deviation as a *fraction* of the mean:

$$\mathrm{CV} = \frac{\SD(X)}{\E[X]} = \frac{\sigma}{\mu}.$$

**Beat 6 — Generalize: derive the computational shortcut.** Computing $\E[(X-\mu)^2]$ directly is clumsy. Expand the square *inside* the expectation and use linearity (Entry №02), remembering $\mu=\E[X]$ is a constant:

$$\Var(X) = \E\!\big[(X-\mu)^2\big] = \E\!\big[X^2 - 2\mu X + \mu^2\big] = \E[X^2] - 2\mu\,\E[X] + \mu^2.$$

Now $\E[X]=\mu$, so the middle term is $-2\mu\cdot\mu=-2\mu^2$, and the last is $+\mu^2$:

$$\Var(X) = \E[X^2] - 2\mu^2 + \mu^2 = \E[X^2] - \mu^2.$$

$$\boxed{\;\Var(X) = \E[X^2] - (\E[X])^2.\;}$$

This **"mean of the square minus square of the mean"** shortcut is almost always faster than the definition, and it is *why* you compute $\E[X^2]$ in nearly every spread problem.

How does spread behave under a linear rescale $aX+b$? Shifting by $b$ slides every value *and* the mean by the same $b$, so distances from the mean are unchanged — $b$ can't affect spread. Scaling by $a$ multiplies every distance by $a$, and since variance is a *squared* distance, it multiplies by $a^2$:

$$\boxed{\;\Var(aX+b) = a^2\,\Var(X),\qquad \SD(aX+b) = |a|\,\SD(X).\;}$$

The $+b$ vanished; the $a$ came out **squared** for variance, as $|a|$ for the standard deviation.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $\Var(X)=\E[X^2]-(\E[X])^2 = 5-4 = 1$.
- *Continuous:* for a density, compute $\E[X^2]=\int x^2 f(x)\,dx$, then subtract $(\E[X])^2$. (Worked Example 7.2 does this end to end.)
- *Rescaling twist:* the casino converts a prize via $Y=3X-2$. The $-2$ is irrelevant to spread; $\Var(Y)=3^2\Var(X)=9\Var(X)$. If $\Var(X)=9$, then $\Var(Y)=81$ and $\SD(Y)=9\cdot\SD(X)$.
- *Edge:* variance is *always* $\ge 0$ (it's an average of squares). If you ever compute a negative variance, you subtracted in the wrong order — it's $\E[X^2]-\mu^2$, never $\mu^2-\E[X^2]$. A variance of exactly $0$ means $X$ is a constant.

**Beat 8 — Picture it.** Same center, different spread:

<figure>
<img src="../../assets/diagrams/ch07_variance_spread.png" alt="Two distributions sharing the same mean of 2 drawn on a common axis. One is tightly clustered around 2 (small variance); the other is widely scattered with mass pushed out toward the extremes (large variance). Under each, the squared deviations from the mean are shaded, and the average shaded area is labeled Var(X). A side note shows a shift by b sliding the whole picture without changing the shaded spread, and a scale by a stretching it so the spread grows by a-squared." style="width:80%; max-width:560px; display:block; margin:1em auto;">
<figcaption>Variance is the average shaded (squared-deviation) area about the mean. Shifting by $b$ slides the picture — spread unchanged; scaling by $a$ stretches it — spread grows by $a^2$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now measure spread: compute $\E[X^2]$, subtract $(\E[X])^2$ for the variance, square-root for the standard deviation, divide by the mean for the coefficient of variation, and rescale spread under $aX+b$ with the $a^2$ rule.

::: pokedex-entry
**POKÉDEX ENTRY №03 — Variance, SD, and CV**

$$\Var(X) = \E\!\big[(X-\mu)^2\big] = \E[X^2] - (\E[X])^2,\qquad \SD(X) = \sqrt{\Var(X)}.$$
$$\mathrm{CV} = \frac{\SD(X)}{\E[X]},\qquad \Var(aX+b) = a^2\Var(X),\qquad \SD(aX+b)=|a|\,\SD(X).$$

*In plain terms:* variance is the average squared distance from the mean; the shortcut "mean of the square minus square of the mean" is almost always faster. A shift $b$ never changes spread; a scale $a$ multiplies variance by $a^2$.

*Recognition cue:* any request for **spread, volatility, standard deviation, or risk**. Compute $\E[X^2]$ first; the $-(\E[X])^2$ correction is the step people forget. A constant added to $X$ never changes the variance.
:::

## Concept 4 — The Moment Generating Function

::: concept-gate
**DO YOU ALREADY OWN THIS? — MGF**

A random variable has MGF $M_X(t)=(1-3t)^{-4}$ for $t<\tfrac13$. Find $\E[X]$ and $\Var(X)$ — by *either* differentiating at $0$ or recognizing the kernel.

If you answered **$\E[X]=12$, $\Var(X)=36$** (Gamma with $\alpha=4,\theta=3$: mean $\alpha\theta$, variance $\alpha\theta^2$; or $M'(0)=12$, $M''(0)=180$, $180-144=36$), **skip to Concept 5**. If "$M_X(t)=\E[e^{tX}]$" is unfamiliar or you can't get moments out of it, read on.
:::

**Beat 1 — The one-sentence idea.** *The moment generating function is one function that, once you have it, hands you every moment of $X$ by differentiating at zero — and its shape uniquely fingerprints the distribution.*

**Beat 2 — Anchor + concrete instance.** So far each moment ($\E[X]$, $\E[X^2]$, …) was a separate integral. The MGF packs *all* of them into a single object: it is just $\E[e^{tX}]$, computed by LOTUS (Entry №02) with $g(x)=e^{tx}$. Differentiating it peels off the moments one at a time.

The ship's generator outputs a surge $X$ whose MGF engineering hands you is

$$M_X(t)=\frac{1}{(1-3t)^4},\qquad t<\tfrac13.$$

*They need the mean and variance of the surge to size a breaker.*

**Beat 3 — Reason through it in plain words (why differentiating works).** Why should derivatives at $0$ give moments? Write $e^{tX}$ as its power series — the same $e^u = 1 + u + \tfrac{u^2}{2!}+\cdots$ you know, with $u=tX$:

$$e^{tX} = 1 + tX + \frac{(tX)^2}{2!} + \frac{(tX)^3}{3!} + \cdots$$

Take the expectation of both sides (linearity lets you average term by term):

$$M_X(t) = \E[e^{tX}] = 1 + t\,\E[X] + \frac{t^2}{2!}\E[X^2] + \frac{t^3}{3!}\E[X^3] + \cdots$$

Now read off coefficients: the coefficient of $t$ is $\E[X]$, the coefficient of $t^2$ is $\tfrac{1}{2!}\E[X^2]$, and so on. Differentiating once and setting $t=0$ plucks out the $t$-coefficient ($\E[X]$); differentiating twice plucks out $\E[X^2]$. The MGF is a *moment vending machine* — each derivative at $0$ dispenses the next moment.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is to read the parameters off the *wrong slot*. A Gamma MGF has the form $(1-\theta t)^{-\alpha}$. Faced with $(1-3t)^{-4}$, the tempting misread is

$$\theta \overset{?}{=} \tfrac13,\ \alpha \overset{?}{=} -4 \qquad\textbf{(wrong)}$$

— confusing "the number multiplying $t$ inside" with "$1/$that," and dropping the sign of the exponent. Pin the form down once and read carefully: write the family as $(1-\theta t)^{-\alpha}$, so $\theta$ is **the coefficient of $t$** ($\theta=3$) and $\alpha$ is the **positive** exponent ($\alpha=4$). Mis-slotting flips the mean from $12$ to something absurd. **Always normalize to the standard kernel before reading parameters.**

**Beat 5 — Translate into notation, one glyph at a time.** The definition:

$$M_X(t) = \E\!\big[e^{tX}\big] \qquad\text{read aloud: ``the expected value of } e \text{ to the } tX\text{.''}$$

The variable $t$ is a *dummy dial* — not a probability, just a knob we turn near $0$. The notation $M_X^{(n)}(0)$ means "the $n$-th derivative of $M_X$, evaluated at $t=0$," and the moment-extraction rule is

$$\E[X] = M_X'(0),\qquad \E[X^2] = M_X''(0),\qquad \E[X^n] = M_X^{(n)}(0).$$

Two structural facts make MGFs powerful: **uniqueness** — if two random variables have the same MGF, they have the same distribution (so recognizing a kernel *identifies* the variable) — and the **sum rule** for independent $X,Y$:

$$M_{X+Y}(t) = M_X(t)\,M_Y(t),\qquad M_{aX+b}(t) = e^{bt}M_X(at).$$

**Beat 6 — Generalize: derive the mean and variance for our surge.** Differentiate $M_X(t)=(1-3t)^{-4}$ using the chain rule (the inside $1-3t$ has derivative $-3$):

$$M_X'(t) = -4(1-3t)^{-5}\cdot(-3) = 12(1-3t)^{-5}\ \Rightarrow\ \E[X]=M_X'(0)=12.$$
$$M_X''(t) = 12\cdot(-5)(1-3t)^{-6}\cdot(-3) = 180(1-3t)^{-6}\ \Rightarrow\ \E[X^2]=M_X''(0)=180.$$

Then by Entry №03,

$$\Var(X) = \E[X^2] - (\E[X])^2 = 180 - 12^2 = 180 - 144 = 36.$$

**Kernel shortcut (same answer, no calculus):** $(1-\theta t)^{-\alpha}$ is the Gamma family, for which $\E[X]=\alpha\theta$ and $\Var(X)=\alpha\theta^2$. With $\alpha=4,\theta=3$: mean $=4\cdot3=12$, variance $=4\cdot9=36$. One read, by uniqueness.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* differentiate $(1-3t)^{-4}$ once for the mean.
- *Kernel recognition (faster):* match $(1-\theta t)^{-\alpha}$ to Gamma; read $\alpha,\theta$ and use $\alpha\theta,\ \alpha\theta^2$.
- *Other kernels:* $e^{\lambda(e^t-1)}$ is **Poisson$(\lambda)$** (mean $=$ variance $=\lambda$); $(1-p+pe^t)^n$ is **Binomial$(n,p)$**; $e^{\mu t+\sigma^2 t^2/2}$ is **Normal$(\mu,\sigma^2)$**. Memorize the kernels and skip differentiation.
- *Edge (higher moments / shifts):* a Normal MGF gives $\E[X^3]$ in one differentiation-free move via $\E[X^3]=\mu^3+3\mu\sigma^2$; and $M_{aX+b}(t)=e^{bt}M_X(at)$ rescales a known MGF without re-deriving.

**Beat 8 — Table it.** A reference grid of kernels turns recognition into a lookup:

<figure>
<img src="../../assets/diagrams/ch07_mgf_kernels.png" alt="A reference table of moment generating function kernels. Rows: Gamma with MGF (1 - theta t)^(-alpha), mean alpha-theta, variance alpha-theta-squared; Poisson with MGF exp(lambda(e^t - 1)), mean and variance both lambda; Binomial with MGF (1 - p + p e^t)^n, mean np, variance np(1-p); Normal with MGF exp(mu t + sigma-squared t-squared over 2), mean mu, variance sigma-squared; Exponential with MGF (1 - theta t)^(-1), mean theta, variance theta-squared. A column on the right shows the 'read it off' parameter slot for each." style="width:85%; max-width:600px; display:block; margin:1em auto;">
<figcaption>The MGF kernel table: match the algebraic shape, read the parameters off the labeled slots, and the mean/variance follow with no calculus. Uniqueness guarantees the match is the distribution.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now extract any moment from an MGF by differentiating at $0$, recognize the common kernels to read parameters and identify the distribution by uniqueness, and rescale or combine MGFs for shifts and independent sums.

::: pokedex-entry
**POKÉDEX ENTRY №04 — Moment Generating Function**

$$M_X(t) = \E\!\big[e^{tX}\big],\qquad \E[X^n] = M_X^{(n)}(0).$$
**Uniqueness:** the MGF determines the distribution. **Independent sums:** $M_{X+Y}(t)=M_X(t)M_Y(t)$. **Linear:** $M_{aX+b}(t)=e^{bt}M_X(at)$.

Common kernels: $(1-\theta t)^{-\alpha}\!\to$ Gamma$(\alpha,\theta)$; $e^{\lambda(e^t-1)}\!\to$ Poisson$(\lambda)$; $(1-p+pe^t)^n\!\to$ Binomial$(n,p)$; $e^{\mu t+\sigma^2t^2/2}\!\to$ Normal$(\mu,\sigma^2)$.

*In plain terms:* a generator that, once known, dispenses every moment by differentiation at zero — and whose shape uniquely fingerprints the distribution.

*Recognition cue:* **"given the MGF," an $e^{tX}$ expectation, or a factored MGF matching a known family.** Read off parameters from the kernel, or differentiate at $0$.
:::

## Concept 5 — The Survival-Function (Darth Vader) Rule

::: concept-gate
**DO YOU ALREADY OWN THIS? — Darth Vader Rule**

A nonnegative time $T$ has survival function $S(t)=P(T>t)=e^{-t/8}$ for $t\ge0$. Find $\E[T]$ **without** recovering the density $f$.

If you answered **$8$** (via $\E[T]=\int_0^\infty S(t)\,dt = \int_0^\infty e^{-t/8}\,dt = 8$) and you know this needs $T\ge0$, **skip to the Worked Examples**. If you reached to differentiate $S$ into $f$ first, read on — there's a shortcut that deletes two error-prone steps.
:::

**Beat 1 — The one-sentence idea.** *For a nonnegative random variable, the mean is simply the area under its survival curve — no density required.*

**Beat 2 — Anchor + concrete instance.** Recall from the previous chapter the **survival function** $S(x)=P(X>x)=1-F(x)$ — "the chance you're still above $x$." Often a problem hands you $S$ (or only the cdf $F$) and asks for the mean. The obvious route is to recover the density $f=F'$ and integrate $xf$. The Darth Vader rule skips that entirely.

Back on the deck, the first mate's clipboard gives the time-to-flood $T$ (minutes, $T\ge0$) through its survival function

$$S(t)=P(T>t)=e^{-t/10},\qquad t\ge0.$$

*He needs the expected minutes before flooding — straight off the curve.*

**Beat 3 — Reason through it in plain words (why the area is the mean).** Picture the lifetime $T$ as "how long the hull *survives*." For each moment $t$, the hull is still alive past $t$ with probability $S(t)=P(T>t)$. The total expected lifetime is built by adding up, over every moment, the chance the hull is *still going* at that moment — because each unit of time contributes to the average only while the hull survives it. Summing "probability still alive at $t$" over all $t$ gives the expected lifetime. Concretely:

$$\E[T] = \int_0^\infty S(t)\,dt = \int_0^\infty e^{-t/10}\,dt = \big[-10\,e^{-t/10}\big]_0^\infty = 0 - (-10) = 10 \text{ minutes.}$$

Hand the first mate **10 minutes.**

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is forgetting the rule's one requirement — **$X\ge 0$** — and applying it to a variable that can go negative:

$$\E[X] \overset{?}{=} \int_0^\infty S(x)\,dx \quad\text{even when } X<0 \text{ is possible.} \qquad\textbf{(wrong — drops the negative tail)}$$

The clean identity $\E[X]=\int_0^\infty S(x)\,dx$ holds *only* for nonnegative $X$. If $X$ can be negative, the area-under-$S$ picture misses the part of the distribution below zero, and you must add a correction term $-\int_{-\infty}^0 F(x)\,dx$. The good news: almost every actuarial quantity — a time, a loss, a claim size — *is* nonnegative, so the simple rule applies. **Check $X\ge0$ before you reach for it.**

**Beat 5 — Translate into notation, one glyph at a time.** The rule, named (the "Darth Vader rule" because the shaded area under the falling survival curve resembles the silhouette):

$$\boxed{\;\E[X] = \int_0^\infty S(x)\,dx = \int_0^\infty P(X>x)\,dx,\qquad X\ge0.\;}$$

For higher moments there's a matching form, $\E[X^k]=\int_0^\infty k\,x^{k-1}S(x)\,dx$. And for a **discrete** nonnegative $X\in\{0,1,2,\dots\}$, the integral becomes a sum:

$$\E[X] = \sum_{k=0}^{\infty} P(X>k) = \sum_{k=1}^{\infty} P(X\ge k).$$

**Beat 6 — Generalize: derive it (why area under $S$ equals the mean).** Start from the definition $\E[X]=\int_0^\infty x f(x)\,dx$ for $X\ge0$, and rewrite the value $x$ as an integral of $1$: $x = \int_0^x 1\,dt$. Substitute and swap the order of integration (the region is $0\le t\le x<\infty$):

$$\E[X] = \int_0^\infty\!\!\left(\int_0^x 1\,dt\right) f(x)\,dx = \int_0^\infty\!\!\left(\int_t^\infty f(x)\,dx\right) dt = \int_0^\infty P(X>t)\,dt = \int_0^\infty S(t)\,dt.$$

The inner integral $\int_t^\infty f(x)\,dx$ is exactly $P(X>t)=S(t)$. So the rule is not magic — it is the ordinary mean with the order of a double integral flipped. The discrete version is the same swap with a sum.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $S(t)=e^{-t/10}$ gives $\E[T]=10$ by direct integration.
- *Bounded support twist:* if $X$ lives on $[0,2]$ with $S(x)=1-\tfrac{x^3}{8}$, integrate $S$ **only over $[0,2]$** (where $S>0$): $\int_0^2 (1-\tfrac{x^3}{8})\,dx = 2 - \tfrac{16}{32} = \tfrac32$. Running the integral to $\infty$ would add a spurious tail.
- *Heavy tail:* $S(x)=\big(\tfrac{2}{2+x}\big)^3$ (a Pareto-type tail) gives $\E[X]=\int_0^\infty \big(\tfrac{2}{2+x}\big)^3 dx = 1$ — finite only because the tail decays fast enough.
- *Discrete edge:* $N\in\{0,1,2,3\}$ with $P(N>0)=0.6,\,P(N>1)=0.35,\,P(N>2)=0.15$ gives $\E[N]=0.6+0.35+0.15=1.10$ by the survival-sum.

**Beat 8 — Picture it.** The rule made visual: the mean *is* the shaded area beneath the survival curve.

<figure>
<img src="../../assets/diagrams/ch07_survival_darthvader.png" alt="A falling survival curve S(x)=P(X>x) starting at height 1 when x=0 and decaying toward 0 as x grows, drawn over the nonnegative x-axis. The entire region between the curve and the axis is shaded and labeled 'area = E[X]'. A caption notes the requirement X >= 0." style="width:72%; max-width:520px; display:block; margin:1em auto;">
<figcaption>The Darth Vader rule: for $X\ge0$, the shaded area under the survival curve $S(x)=P(X>x)$ <em>is</em> $\E[X]$. No density needed — integrate the curve you were handed.</figcaption>
</figure>

**Beat 9 — Consolidate.** When a problem gives you $S(x)$ (or only $F$) and asks for a mean of a nonnegative variable, you can integrate the survival curve directly — skipping the density entirely — and you know to stop the integral at the top of a bounded support.

::: pokedex-entry
**POKÉDEX ENTRY №05 — The Survival-Function (Darth Vader) Rule**

For a **nonnegative** $X\ge0$:
$$\E[X] = \int_0^\infty S(x)\,dx = \int_0^\infty P(X>x)\,dx,\qquad \E[X^k]=\int_0^\infty k\,x^{k-1}S(x)\,dx.$$
Discrete analog for $X\in\{0,1,2,\dots\}$:
$$\E[X] = \sum_{k=0}^{\infty} P(X>k) = \sum_{k=1}^{\infty} P(X\ge k).$$

*In plain terms:* the area under "still alive past $x$" is the expected lifetime. Skip recovering the density — integrate $S$.

*Recognition cue:* you're handed $S(x)$ (or only the cdf) and asked for a mean, and $X\ge0$. **Integrate the survival curve directly.** For bounded $X$, integrate only over the support.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/surge.png" alt="Lt. Surge" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Lt. Surge — the Lightning American, your center-and-spread drillmaster</figcaption>
</figure>

Four examples, fading from fully narrated to exam-speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because the normalize-then-mean-then-variance workflow is the load-bearing skill of the chapter.

### Worked Example 7.1 — Lt. Surge's Variable Shock (full narration; understanding-first)

**ARCHETYPE:** *Normalize a density, then mean and variance of a continuous RV.*

**Setup.** Lt. Surge's Raichu delivers a shock whose magnitude $X$ (hundreds of volts) has density $f(x)=c\,x(2-x)$ on $0\le x\le2$ (and $0$ elsewhere). Surge dares you: "Find the average jolt and how wildly it swings before you step on my mat." Find $c$, $\E[X]$, and $\Var(X)$.

<figure style="margin:1.25em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/26.png" alt="Raichu" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;"><strong>#026 Raichu</strong></figcaption>
</figure>

**Step 1 — Identify (which entries, in which order?).** A density with an unknown constant $c$ out front $\to$ first enforce "valid density" ($\int f=1$, from the previous chapter) to find $c$. Then Entry №01 for $\E[X]$, Entry №02's LOTUS for $\E[X^2]$, and Entry №03 for the variance. Three entries, in sequence.

**Step 2 — Professor's Path (the why).** *Normalize first* — a density is only legitimate once it totals to $1$, and until $c$ is pinned down no expectation means anything:

$$\int_0^2 c\,x(2-x)\,dx = c\!\left[x^2 - \tfrac{x^3}{3}\right]_0^2 = c\!\left(4 - \tfrac{8}{3}\right) = c\cdot\tfrac{4}{3} = 1 \ \Rightarrow\ c=\tfrac{3}{4}.$$

Now the **mean** (Entry №01), value times density, integrated:

$$\E[X] = \tfrac34\int_0^2 x^2(2-x)\,dx = \tfrac34\!\left[\tfrac{2x^3}{3} - \tfrac{x^4}{4}\right]_0^2 = \tfrac34\!\left(\tfrac{16}{3} - 4\right) = \tfrac34\cdot\tfrac{4}{3} = 1.$$

The density $x(2-x)$ is symmetric about $x=1$, so $\E[X]=1$ was foreseeable — a good consistency check. Now the **second moment** via LOTUS (Entry №02) with $g(x)=x^2$:

$$\E[X^2] = \tfrac34\int_0^2 x^3(2-x)\,dx = \tfrac34\!\left[\tfrac{x^4}{2} - \tfrac{x^5}{5}\right]_0^2 = \tfrac34\!\left(8 - \tfrac{32}{5}\right) = \tfrac34\cdot\tfrac{8}{5} = \tfrac{6}{5} = 1.2.$$

Finally the **variance** (Entry №03), mean of the square minus square of the mean:

$$\Var(X) = \E[X^2] - (\E[X])^2 = 1.2 - 1^2 = 0.2.$$

**Step 3 — Trainer's Path (the fast how).** Symmetry $\Rightarrow \E[X]=1$ on sight; you only need $\E[X^2]=\tfrac65$, then $\Var = \tfrac65 - 1 = \tfrac15 = 0.2$. So the average jolt is **100 volts**, with $\SD=\sqrt{0.2}\approx0.447$ (about 45 volts).

**Step 4 — Check & pitfall.** $c=\tfrac34>0$ and $f\ge0$ on $[0,2]$: valid. The mean landing exactly at the midpoint $1$ confirms the symmetry. **Pitfall:** reporting $\E[X^2]=1.2$ *as* the variance — forgetting the $-(\E[X])^2=-1$ correction — would overstate the spread sixfold. *(Back-ref: Entries №01–№03.)*

### Worked Example 7.2 — Reading the Generator (partial guidance)

**ARCHETYPE:** *Moments by differentiating an MGF, with kernel-recognition cross-check.*

**Setup.** The ship's generator outputs a surge $X$ with MGF $M_X(t)=(1-3t)^{-4}$ for $t<\tfrac13$. Engineering needs the **mean and variance** to size a breaker.

**Identify.** Given the MGF $\to$ Entry №04: differentiate at $0$, *or* recognize the kernel. *Your move: do it both ways and confirm they agree.*

**Trainer's Path (kernel recognition).** $(1-\theta t)^{-\alpha}$ is Gamma. Match: the coefficient of $t$ inside is $\theta=3$; the positive exponent is $\alpha=4$. For Gamma, $\E[X]=\alpha\theta=12$ and $\Var(X)=\alpha\theta^2 = 4\cdot9 = 36$. One read.

**Professor's Path (differentiate).**
$$M_X'(t) = 12(1-3t)^{-5}\ \Rightarrow\ \E[X]=M_X'(0)=12,$$
$$M_X''(t) = 180(1-3t)^{-6}\ \Rightarrow\ \E[X^2]=M_X''(0)=180,$$
$$\Var(X) = 180 - 12^2 = 180 - 144 = 36.$$

**Check & pitfall.** Both paths give mean $12$, variance $36$; $\Var=36\ge0$ ✓. **Pitfall:** misreading the kernel as $\theta=\tfrac13$ (the reciprocal) instead of $\theta=3$ — always write the family as $(1-\theta t)^{-\alpha}$ so $\theta$ is the number multiplying $t$. *(Back-ref: Entry №04.)*

### Worked Example 7.3 — Timing the Lifeboats (light guidance)

**ARCHETYPE:** *Mean from a survival function (Darth Vader rule), nonnegative RV — two ways.*

**Setup.** The time-to-flood $T$ (minutes, $T\ge0$) has survival function $S(t)=e^{-t/10}$. Find $\E[T]$ both by the Darth Vader rule and by recovering the density, to prove they match.

**Darth Vader (Entry №05).** $T\ge0$ and only $S$ is given, so integrate the curve:
$$\E[T] = \int_0^\infty e^{-t/10}\,dt = \big[-10e^{-t/10}\big]_0^\infty = 10.$$

**Density route (cross-check).** $F(t)=1-e^{-t/10}$, so $f(t)=F'(t)=\tfrac{1}{10}e^{-t/10}$, and $\E[T]=\int_0^\infty t\cdot\tfrac1{10}e^{-t/10}\,dt = \tfrac1{10}\cdot10^2 = 10$ (gamma identity $\int_0^\infty t e^{-t/\theta}dt=\theta^2$).

**Check & pitfall.** $S(t)=e^{-t/10}$ is an Exponential with mean $\theta=10$, so $\E[T]=10$ is the known answer ✓. The Darth Vader route skipped the density step. **Pitfall:** the rule needs $T\ge0$; for a variable that could dip below zero you'd add the negative-tail correction. *(Back-ref: Entry №05.)*

### Worked Example 7.4 — The Casino Conversion (exam speed)

**ARCHETYPE:** *Linear rescaling of mean and variance.*

**Setup.** A prize wheel pays $X$ with $\E[X]=10$, $\Var(X)=9$. The casino converts every prize via $Y=3X-2$. Find $\E[Y]$, $\Var(Y)$, $\SD(Y)$.

$$\E[Y] = 3\E[X]-2 = 3(10)-2 = 28,\qquad \Var(Y) = 3^2\Var(X) = 9\cdot9 = 81,\qquad \SD(Y)=\sqrt{81}=9.$$

**Check & pitfall.** The $-2$ shifted the mean but left the variance untouched; the $3$ entered the variance **squared** ✓. **Pitfall:** writing $\Var(Y)=3\cdot9=27$ (forgetting to square the scale) or letting the $-2$ change the variance. *(Back-ref: Entries №01, №03.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — Variance keystrokes**

On the TI-30XS, store $\E[X]$ with **STO→ $x$** *before* squaring, then compute $\E[X^2] - x^2$ from memory. This kills the rounding error that turns a clean $0.200$ into $0.199$ and costs you the matching multiple-choice option. Always compute $\E[X^2]$ first, then subtract — never report the second moment as the variance.
:::

::: trainers-tip
**TRAINER'S TIP — MGF in one glance**

If an MGF is a power of $(1-\theta t)$, it's **Gamma**: the exponent is $\alpha$, the number times $t$ is $\theta$, so mean $=\alpha\theta$ and variance $=\alpha\theta^2$ with zero calculus. If it's $e^{\lambda(e^t-1)}$ it's **Poisson$(\lambda)$**; $(1-p+pe^t)^n$ is **Binomial**; $e^{\mu t+\sigma^2t^2/2}$ is **Normal**. Memorize the four kernels and you skip differentiation entirely.
:::

::: trainers-tip
**TRAINER'S TIP — When you see a survival function, don't hunt for $f$**

Given $S(x)$ and asked for $\E[X]$ with $X\ge0$: integrate $S$ directly. Recovering the density first is two extra, error-prone steps the Darth Vader rule deletes. For a *bounded* $X$, integrate $S$ only over the support — never out to $\infty$.
:::

::: trainers-tip
**TRAINER'S TIP — Re-add when two routes disagree**

If a count-based average and a probability-weighted sum disagree (as in Concept 1's deliberate derail), the *method* is fine — it's mental arithmetic. Re-add termwise and trust the probability-weighted definition. A mis-multiplied last term is the classic culprit.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

Jessie schemes to "fairly price" the ransom for a captured Magikarp. The black-market multiplier squares the resale value, so the payout is $X^2$. "Easy!" she crows. "The average value is $\E[X]=4$, so the average *squared* value is just $\E[X^2]=4^2=16$. We demand sixteen!" James nods. Meowth tallies the loot.

They set the ransom at $16$ — and the buyer, who knows $X$ actually swings between $2$ and $6$, walks away laughing. Because the *true* second moment is

$$\E[X^2] = (\E[X])^2 + \Var(X) = 16 + \Var(X) > 16.$$

Team Rocket left the **variance** on the table and **under**priced their own scheme. Again.

**Where it fails:** Jessie computed $g(\E[X])$ instead of $\E[g(X)]$ for the nonlinear $g(x)=x^2$ — **Jensen's trap** (Concept 2). For a nonlinear $g$, average $g(x)$ against the probabilities, or use $\E[X^2]=\Var(X)+(\E[X])^2$; the two answers differ by *exactly* the variance. The only $g$ you may "plug the mean into" is a linear one.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

This chapter is the arithmetic of **every premium ever quoted.** An insurer's pure premium for a risk is its **expected loss** $\E[X]$ — the center you computed in Concept 1 — and the **risk load** (the margin that keeps the insurer solvent) scales with the **spread**, $\SD(X)$ or $\Var(X)$, from Concept 3. A policy that is cheap on average but wildly volatile is *more* expensive to write than its mean suggests; that is why variance, not just the mean, sits in the price.

The **survival function** is the single most important object in life and health actuarial work: $S(x)$ is the probability a life (or a machine, or a policy) lasts past age/time $x$, and the Darth Vader rule $\E[X]=\int_0^\infty S(x)\,dx$ is exactly how an actuary computes a **complete expectation of life** or an **expected claim duration** from a survival curve alone. P&C reserving uses the same identity to turn a loss-size survival function straight into an **expected severity**. And the **coefficient of variation** you met in Concept 3 is the standard "relative risk" yardstick insurers use to compare the volatility of lines with very different mean claim sizes.

*Series bridge:* the survival function and complete-expectation machinery are the backbone of the CAS/SOA life-contingencies exams (FAM-L / ALTAM); the MGF reappears as the engine for sums of independent risks and the Central Limit Theorem later in this very book.

*Transfer check:* could you solve this with **no Pokémon in it**? "A loss $X$ has survival function $S(x)=e^{-x/10}$ for $x\ge0$; find the expected loss." Same rule, same $\E[X]=10$. If you can do that, the skill has transferred.
:::

## The Gym Battle — Thunder Badge Capstone

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/types/electric.png" alt="Electric type icon" style="width:90px; display:block; margin:0 auto;">
<figcaption style="font-size:0.85em;">Lt. Surge's Electric Gym — the Thunder Badge challenge</figcaption>
</figure>

**Surge's Challenge.** Lt. Surge slams his hand on the gym's voltage panel. "You want the Thunder Badge? Then read my Raichu like a meter, kid." The damage $X$ (hundreds of volts) his Raichu deals per turn has density

$$f(x)=\tfrac{3}{8}x^2,\qquad 0\le x\le2,$$

and $0$ elsewhere. Surge demands, all in one breath: (a) confirm it's a valid density; (b) the cdf $F(x)$ and survival function $S(x)$; (c) the expected damage $\E[X]$ — **twice**, once by $\int x f$ and once by the Darth Vader rule, to prove you trust it; (d) $\Var(X)$ and the coefficient of variation; (e) the median damage; (f) the expected damage of a *charged* attack worth $g(X)=X^2$; and (g) a moment check — confirm the $\E[X^2]$ you used in (d) equals $\int x^2 f$.

**ARCHETYPE:** *Full single-RV workout — verify, cdf & survival, dual-method mean, variance & CV, median, $\E[g(X)]$.*

**Identify.** Entries №01–№05 in sequence; this is the chapter's whole toolkit in one battle.

**Step 1 — (a) Valid?** $f\ge0$ on $[0,2]$, and
$$\int_0^2 \tfrac38 x^2\,dx = \tfrac38\cdot\tfrac{x^3}{3}\Big|_0^2 = \tfrac18\cdot8 = 1.\ \checkmark$$

**Step 2 — (b) cdf & survival.** For $0\le x\le2$,
$$F(x)=\int_0^x \tfrac38 u^2\,du = \tfrac{x^3}{8},\qquad S(x)=1-\tfrac{x^3}{8},$$
with $F=0$ below $0$ and $F=1$ above $2$.

**Step 3 — (c) Mean, two ways.** Direct (Entry №01):
$$\E[X]=\int_0^2 x\cdot\tfrac38 x^2\,dx = \tfrac38\cdot\tfrac{x^4}{4}\Big|_0^2 = \tfrac{3}{32}\cdot16 = \tfrac32 = 1.5.$$
Darth Vader (Entry №05; $X\ge0$ but bounded, so integrate $S$ only over $[0,2]$):
$$\E[X]=\int_0^2 S(x)\,dx = \int_0^2\!\Big(1-\tfrac{x^3}{8}\Big)dx = \Big[x-\tfrac{x^4}{32}\Big]_0^2 = 2-\tfrac{16}{32} = 2-\tfrac12 = \tfrac32.\ \checkmark$$

**Step 4 — (d) Variance & CV.** Second moment by LOTUS:
$$\E[X^2]=\int_0^2 x^2\cdot\tfrac38 x^2\,dx = \tfrac38\cdot\tfrac{x^5}{5}\Big|_0^2 = \tfrac{3}{40}\cdot32 = \tfrac{12}{5} = 2.4,$$
$$\Var(X)=2.4-1.5^2 = 2.4-2.25 = 0.15,\qquad \SD=\sqrt{0.15}\approx0.387,\qquad \mathrm{CV}=\frac{0.387}{1.5}\approx0.258.$$

**Step 5 — (e) Median.** Solve $F(m)=\tfrac12$: $\tfrac{m^3}{8}=\tfrac12 \Rightarrow m^3=4 \Rightarrow m=4^{1/3}\approx1.587$.

**Step 6 — (f) Charged attack $\E[X^2]$.** This *is* part (d)'s second moment: $\E[g(X)]=\E[X^2]=2.4$. Note $g(\E[X])=1.5^2=2.25\ne2.4$ — the gap is the variance, exactly Team Rocket's trap.

**Step 7 — (g) Moment check.** The $\E[X^2]=2.4$ used in the variance is the same integral $\int_0^2 x^2 f\,dx$ computed in (d). Consistent. $\checkmark$

**Professor's Path (median, exact).** $m=4^{1/3}=2^{2/3}\approx1.587$, and $F(1.587)=1.587^3/8=0.5$ confirms it. Since the median $1.587$ exceeds the mean $1.5$, the rising density $f\propto x^2$ is **left-skewed** (mass piled toward the high end, tail trailing left) — the median-above-mean ordering is itself a sanity flag.

**Check & verdict.** Every probability in $[0,1]$, $\Var=0.15\ge0$, the two mean computations agree, and median $>$ mean matches the rising density's left skew. **Pitfall:** integrating $S$ over $[0,\infty)$ instead of stopping at $2$ would add a spurious tail; for bounded $X$, the Darth Vader integral runs only over where $S>0$.

> Surge grins and tosses you the badge. "You didn't just crunch one number — you read the whole meter. The Thunder Badge is yours."

## The Gym Challenge — Problem Set

::: problem-set
**TEST-OUT INSTRUCTIONS.** Work this set timed (~6 min/problem), then check the **Answer Key** below. Hit the mastery bar (**80%+ with correct method**) and you may move on. Miss it, and the chapter is waiting. Problems are listed first; full worked solutions follow afterward (never interleaved). Markers: 🔴 Poké Ball = routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (mechanics)

**C7.1.** 🔴 A dockworker's headcount $X$ of Pidgey on the S.S. Anne mast has pmf $p(x)=kx$ for $x=1,2,3,4$ and $0$ otherwise. Find $k$, then state $P(X\ge3)$.

**C7.2.** 🔴 The time $X$ (hours) a Geodude naps has density $f(x)=c(1-x)$ for $0\le x\le1$. Find $c$ and $\E[X]$.

**C7.3.** 🔴 A vending machine's payout $X$ (Poké-dollars) is discrete uniform on $\{1,2,3,4,5,6\}$. Compute $\E[X]$ and $\Var(X)$.

**C7.4.** 🔴 Misty's Staryu recovers in $T$ minutes with survival function $S(t)=e^{-t/8}$, $t\ge0$. Using the Darth Vader rule, find $\E[T]$, then $P(T>8)$.

**C7.5.** 🟡 A prize wheel pays $X$ with $\E[X]=10$, $\Var(X)=9$. The casino converts every prize via $Y=3X-2$. Find $\E[Y]$, $\Var(Y)$, $\SD(Y)$.

**C7.6.** 🟡 A Voltorb's stored charge has MGF $M_X(t)=e^{4(e^t-1)}$. Identify the family and state $\E[X]$ and $\Var(X)$ from the kernel.

**C7.7.** 🔴 A continuous loss $X$ has cdf $F(x)=1-\dfrac{16}{(x+4)^2}$ for $x\ge0$. Find the median.

**C7.18.** 🟡 A Magnemite squadron's number of hits $X$ has MGF $M_X(t)=(0.4e^t+0.6)^{10}$. Identify the family and state $\E[X]$ and $\Var(X)$ from the kernel.

### Gym Battles (true SOA difficulty)

**C7.8.** 🟡 Surge's backup capacitor discharges energy $X$ (hundreds of volts) with density $f(x)=\tfrac12 x$ for $0\le x\le2$. Report (i) $\E[X]$, (ii) $\Var(X)$, (iii) the coefficient of variation.

**C7.9.** 🟡 A salvage drone's repair cost $X$ (thousands of Poké-dollars) has density $f(x)=\dfrac{3}{x^4}$ for $x\ge1$. Find $\E[X]$, then $\E[X^2]$ and $\Var(X)$, and explain in one line why a finite-variance assumption matters here.

**C7.10.** 🟡 A rigged slot machine's net payout $X$ has MGF $M_X(t)=\dfrac{0.3\,e^t}{1-0.7\,e^t}$ for $e^t<\tfrac{1}{0.7}$. Recognize the family, then compute $\E[X]$ and confirm against the family's mean.

**C7.11.** 🟡 A flooded compartment's depth $X$ (meters) has density $f(x)=\tfrac{3}{16}(4-x^2)$ for $0\le x\le2$. Verify it integrates to $1$, then find $\E[X]$ and $P(X>1)$.

**C7.12.** 🔵 A Pikachu's Thunderbolt damage $X$ is Exponential with mean $6$. The scoreboard awards $g(X)=\sqrt{X}$. Using $\E[\sqrt X]=\tfrac16\int_0^\infty x^{1/2}e^{-x/6}\,dx$ and $\int_0^\infty x^{1/2}e^{-x/\theta}dx=\Gamma(\tfrac32)\theta^{3/2}$ with $\Gamma(\tfrac32)=\tfrac{\sqrt\pi}{2}$, find $\E[\sqrt X]$.

**C7.13.** 🟡 A claim severity $X$ has survival function $S(x)=\left(\dfrac{2}{2+x}\right)^3$ for $x\ge0$. Use the Darth Vader rule to find $\E[X]$.

**C7.14.** 🔵 A discrete loss $N$ takes values $0,1,2,3$ with $P(N>0)=0.6$, $P(N>1)=0.35$, $P(N>2)=0.15$, $P(N>3)=0$. Use the discrete survival-sum to find $\E[N]$, then find $\Var(N)$.

**C7.15.** 🔵 Surge's super-charged Raichu deals damage $X$ with density $f(x)=cx^2(3-x)$ on $0\le x\le3$. Find $c$, the mode, and the mean, and state whether the distribution is left- or right-skewed via the mean–mode comparison.

**C7.19.** 🟡 A Magmar's cooldown time $X$ (minutes) has MGF $M_X(t)=(1-5t)^{-1}$ for $t<\tfrac15$. Without naming the family, differentiate to obtain $\E[X]$ and $\E[X^2]$, then give $\Var(X)$.

**C7.20.** 🟡 Three independent flame bursts each have duration $X_i\sim$ Exponential with mean $4$, MGF $M(t)=(1-4t)^{-1}$. Let $S=X_1+X_2+X_3$. Find $M_S(t)$, identify the family of $S$, and state $\E[S]$ and $\Var(S)$.

### Elite Challenge (integrative / stretch)

**C7.16.** 🔵 A reactor's output $X$ has MGF $M_X(t)=\exp(2t+8t^2)$. Identify the distribution (the Normal kernel $e^{\mu t+\sigma^2t^2/2}$), state $\mu$ and $\sigma^2$, then compute $\E[X^3]$. *(Hint: $\E[X^3]=\mu^3+3\mu\sigma^2$.)*

**C7.17.** 🔵 The time-to-flood is $T$ minutes with density $f(t)=\dfrac{t}{50}e^{-t^2/100}$ for $t\ge0$ (a Rayleigh-type model). (i) Find $S(t)$. (ii) Use the Darth Vader rule with $u=t^2/100$ to find $\E[T]$ in terms of $\Gamma(\tfrac12)=\sqrt\pi$. (iii) Find the median and compare it to the mean.

**C7.21.** 🔵 The number of trials $X$ to land the $4$th capture has MGF $M_X(t)=\left[\dfrac{0.25\,e^t}{1-0.75\,e^t}\right]^4$ for $e^t<\tfrac{1}{0.75}$. Recognize the family and parameters, then compute $\E[X]$.
:::

## Answer Key

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

**C7.1** — *Normalize a pmf (prior-chapter validity + Entry №01 setup).* Require $\sum_{x=1}^4 kx = k(1+2+3+4) = 10k = 1$, so $k=0.1$. Then $P(X\ge3)=p(3)+p(4)=0.3+0.4=0.7$.

**C7.2** — *Normalize a density, then mean (Entry №01).* $\int_0^1 c(1-x)\,dx = c\big[x-\tfrac{x^2}{2}\big]_0^1 = c\cdot\tfrac12 = 1 \Rightarrow c=2$. Then $\E[X]=\int_0^1 x\cdot2(1-x)\,dx = 2\big[\tfrac{x^2}{2}-\tfrac{x^3}{3}\big]_0^1 = 2\cdot\tfrac16 = \tfrac13$.

**C7.3** — *Discrete-uniform mean and variance (Entries №01, №03).* For uniform on $1..n$, $\E[X]=\tfrac{n+1}{2}=\tfrac72=3.5$ and $\Var(X)=\tfrac{n^2-1}{12}=\tfrac{35}{12}\approx2.917$.

**C7.4** — *Darth Vader rule + survival probability (Entry №05).* $\E[T]=\int_0^\infty e^{-t/8}\,dt = 8$. $P(T>8)=S(8)=e^{-1}\approx0.368$.

**C7.5** — *Linear rescaling of mean and variance (Entries №01, №03).* $\E[Y]=3(10)-2=28$. $\Var(Y)=3^2\cdot9=81$. $\SD(Y)=\sqrt{81}=9$.

**C7.6** — *MGF kernel recognition, Poisson (Entry №04).* $M_X(t)=e^{\lambda(e^t-1)}$ with $\lambda=4$ is Poisson; mean $=\lambda=4$, variance $=\lambda=4$.

**C7.7** — *Median from a cdf (prior-chapter percentile).* Set $F(m)=1-\tfrac{16}{(m+4)^2}=\tfrac12 \Rightarrow \tfrac{16}{(m+4)^2}=\tfrac12 \Rightarrow (m+4)^2=32 \Rightarrow m+4=4\sqrt2 \Rightarrow m=4\sqrt2-4\approx1.657$.

**C7.18** — *Binomial MGF kernel recognition (Entry №04).* $M_X(t)=(pe^t+(1-p))^n$ is Binomial$(n,p)$ with $n=10$, $p=0.4$. Hence $\E[X]=np=4$ and $\Var(X)=np(1-p)=10(0.4)(0.6)=2.4$.

**C7.8** — *Full continuous mean/variance/CV (Entries №01, №03).* $\E[X]=\int_0^2 x\cdot\tfrac12 x\,dx = \tfrac12\cdot\tfrac{x^3}{3}\big|_0^2 = \tfrac12\cdot\tfrac83 = \tfrac43\approx1.333$. $\E[X^2]=\int_0^2 x^2\cdot\tfrac12 x\,dx = \tfrac12\cdot\tfrac{x^4}{4}\big|_0^2 = \tfrac12\cdot4 = 2$. $\Var(X)=2-(\tfrac43)^2 = 2-\tfrac{16}{9} = \tfrac29\approx0.222$. $\mathrm{CV}=\dfrac{\sqrt{2/9}}{4/3} = \dfrac{\sqrt2/3}{4/3} = \dfrac{\sqrt2}{4}\approx0.354$.

**C7.9** — *Moments of a power-law density (Entries №01, №03).* $\E[X]=\int_1^\infty x\cdot3x^{-4}\,dx = 3\int_1^\infty x^{-3}\,dx = 3\cdot\tfrac12 = \tfrac32$. $\E[X^2]=3\int_1^\infty x^{-2}\,dx = 3\cdot1 = 3$. $\Var(X)=3-(\tfrac32)^2 = 3-2.25 = 0.75$. The second moment converges only because the tail exponent exceeds the moment order; one degree heavier and $\Var$ would be infinite, breaking any variance-based pricing.

**C7.10** — *MGF kernel recognition, geometric (Entry №04).* $M_X(t)=\dfrac{pe^t}{1-(1-p)e^t}$ with $p=0.3$ is the geometric (support $1,2,\dots$). Differentiate: with $q=0.7$, $M_X'(t)=\dfrac{0.3e^t}{(1-0.7e^t)^2}$; at $t=0$, $M_X'(0)=\dfrac{0.3}{(0.3)^2}=\dfrac{1}{0.3}=\tfrac{10}{3}\approx3.333=\tfrac1p$.

**C7.11** — *Verify density, mean, tail probability (Entries №01).* $\int_0^2\tfrac{3}{16}(4-x^2)\,dx = \tfrac{3}{16}\big[4x-\tfrac{x^3}{3}\big]_0^2 = \tfrac{3}{16}(8-\tfrac83) = \tfrac{3}{16}\cdot\tfrac{16}{3} = 1\ \checkmark$. $\E[X]=\tfrac{3}{16}\int_0^2 x(4-x^2)\,dx = \tfrac{3}{16}\big[2x^2-\tfrac{x^4}{4}\big]_0^2 = \tfrac{3}{16}(8-4) = \tfrac34 = 0.75$. $P(X>1)=\tfrac{3}{16}\int_1^2(4-x^2)\,dx = \tfrac{3}{16}\big[4x-\tfrac{x^3}{3}\big]_1^2 = \tfrac{3}{16}\big(\tfrac{16}{3}-\tfrac{11}{3}\big) = \tfrac{3}{16}\cdot\tfrac53 = \tfrac{5}{16}\approx0.3125$.

**C7.12** — *$\E[g(X)]$ via the gamma identity (Entry №02; Ch.1 gamma).* $\E[\sqrt X]=\tfrac16\int_0^\infty x^{1/2}e^{-x/6}\,dx = \tfrac16\,\Gamma(\tfrac32)\,6^{3/2} = \tfrac16\cdot\tfrac{\sqrt\pi}{2}\cdot6\sqrt6 = \tfrac{\sqrt\pi}{2}\sqrt6 = \tfrac{\sqrt{6\pi}}{2}\approx2.171$.

**C7.13** — *Darth Vader rule on a Pareto tail (Entry №05).* $\E[X]=\int_0^\infty\!\big(\tfrac{2}{2+x}\big)^3 dx$. Let $u=2+x$: $=\int_2^\infty 8u^{-3}\,du = 8\big[-\tfrac12 u^{-2}\big]_2^\infty = 8\cdot\tfrac12\cdot\tfrac14 = 1$.

**C7.14** — *Discrete Darth Vader sum + variance (Entries №05, №03).* $\E[N]=\sum_{k\ge0}P(N>k)=0.6+0.35+0.15+0=1.10$. Recover the pmf: $P(N=0)=1-0.6=0.4$, $P(N=1)=0.6-0.35=0.25$, $P(N=2)=0.35-0.15=0.20$, $P(N=3)=0.15$. $\E[N^2]=0+1(0.25)+4(0.20)+9(0.15)=0.25+0.80+1.35=2.40$. $\Var(N)=2.40-1.10^2=2.40-1.21=1.19$.

**C7.15** — *Normalize, mode, mean, skew (Entries №01, №03; mode via calculus).* Normalize: $\int_0^3 cx^2(3-x)\,dx = c\big[x^3-\tfrac{x^4}{4}\big]_0^3 = c(27-\tfrac{81}{4}) = c\cdot\tfrac{27}{4} = 1 \Rightarrow c=\tfrac{4}{27}$. Mode: maximize $3x^2-x^3$; $6x-3x^2=3x(2-x)=0 \Rightarrow x=2$ (interior max). Mean: $\E[X]=\tfrac{4}{27}\int_0^3 x^3(3-x)\,dx = \tfrac{4}{27}\big[\tfrac{3x^4}{4}-\tfrac{x^5}{5}\big]_0^3 = \tfrac{4}{27}\big(\tfrac{243}{4}-\tfrac{243}{5}\big) = \tfrac{4}{27}\cdot\tfrac{243}{20} = 1.8$. Since mean $1.8<$ mode $2$, the distribution is **left-skewed**.

**C7.19** — *Moments by differentiating an MGF (Entry №04).* $M_X'(t)=5(1-5t)^{-2}\Rightarrow\E[X]=M_X'(0)=5$. $M_X''(t)=50(1-5t)^{-3}\Rightarrow\E[X^2]=M_X''(0)=50$. $\Var(X)=50-5^2=25$. (This is Exponential with mean $\theta=5$, where $\Var=\theta^2=25$.)

**C7.20** — *MGF of a sum equals the product of MGFs (Entry №04).* For independent $X_i$, $M_S(t)=\big[(1-4t)^{-1}\big]^3=(1-4t)^{-3}$, the Gamma$(\alpha=3,\theta=4)$ kernel. Thus $\E[S]=\alpha\theta=12$ and $\Var(S)=\alpha\theta^2=3(16)=48$.

**C7.16** — *Normal MGF kernel + higher moment (Entry №04).* $M_X(t)=e^{\mu t+\sigma^2t^2/2}$ matches $2t+8t^2$, so $\mu=2$ and $\tfrac{\sigma^2}{2}=8 \Rightarrow \sigma^2=16$. For a Normal, $\E[X^3]=\mu^3+3\mu\sigma^2 = 8 + 3(2)(16) = 8+96 = 104$.

**C7.17** — *Survival function, Darth Vader with substitution, median (Entries №05).* (i) $S(t)=\int_t^\infty \tfrac{u}{50}e^{-u^2/100}\,du$; with $w=u^2/100$, $dw=\tfrac{u}{50}\,du$, so $S(t)=\int_{t^2/100}^\infty e^{-w}\,dw = e^{-t^2/100}$. (ii) $\E[T]=\int_0^\infty e^{-t^2/100}\,dt$; sub $u=t^2/100 \Rightarrow t=10\sqrt u,\ dt=5u^{-1/2}\,du$, giving $\E[T]=\int_0^\infty 5u^{-1/2}e^{-u}\,du = 5\Gamma(\tfrac12) = 5\sqrt\pi\approx8.862$. (iii) Median: $e^{-m^2/100}=\tfrac12 \Rightarrow m^2=100\ln2 \Rightarrow m=10\sqrt{\ln2}\approx8.326$. Mean $8.862>$ median $8.326$, so the model is right-skewed.

**C7.21** — *Negative-binomial MGF kernel (Entry №04).* The kernel $\big[\tfrac{pe^t}{1-(1-p)e^t}\big]^r$ counts trials-until-$r$-successes with $r=4$, $p=0.25$. Its mean is $\E[X]=\dfrac{r}{p}=\dfrac{4}{0.25}=16$.

### Quick-Answer Table

| # | Answer | | # | Answer |
|---|---|---|---|---|
| C7.1 | $k=0.1$, $P(X\ge3)=0.7$ | | C7.10 | Geometric; $\E=10/3\approx3.333$ |
| C7.2 | $c=2$, $\E[X]=1/3$ | | C7.11 | $\E=0.75$, $P(X>1)=5/16\approx0.3125$ |
| C7.3 | $\E=3.5$, $\Var=35/12\approx2.917$ | | C7.12 | $\sqrt{6\pi}/2\approx2.171$ |
| C7.4 | $\E[T]=8$, $P(T>8)\approx0.368$ | | C7.13 | $\E[X]=1$ |
| C7.5 | $\E=28$, $\Var=81$, $\SD=9$ | | C7.14 | $\E[N]=1.1$, $\Var=1.19$ |
| C7.6 | Poisson; $\E=\Var=4$ | | C7.15 | $c=4/27$, mode $2$, mean $1.8$, left-skew |
| C7.7 | $m=4\sqrt2-4\approx1.657$ | | C7.16 | Normal$(2,16)$; $\E[X^3]=104$ |
| C7.8 | $\E=4/3$, $\Var=2/9$, CV$\approx0.354$ | | C7.17 | $S=e^{-t^2/100}$, $\E[T]=5\sqrt\pi\approx8.86$, median $\approx8.33$ |
| C7.9 | $\E=1.5$, $\E[X^2]=3$, $\Var=0.75$ | | C7.18 | Binomial$(10,0.4)$; $\E=4$, $\Var=2.4$ |
| C7.19 | $\E=5$, $\E[X^2]=50$, $\Var=25$ | | C7.20 | Gamma$(3,4)$; $\E=12$, $\Var=48$ |
| C7.21 | NegBin$(r{=}4,p{=}0.25)$; $\E=16$ | | | |
:::

## Badge Earned — Mastery Checklist

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/thunder_badge.png" alt="Thunder Badge" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Thunder Badge earned!</strong></figcaption>
</figure>

You earn the **Thunder Badge** when you can, unaided:

1. **Compute** $\E[X]$ for a discrete or continuous $X$ as the probability-weighted average, and $\E[g(X)]$ via LOTUS, applying linearity $\E[aX+b]=a\E[X]+b$ — and knowing $\E[g(X)]\ne g(\E[X])$ for nonlinear $g$. *(Outcome 2b.)*
2. **Compute** $\Var(X)=\E[X^2]-(\E[X])^2$, $\SD$, and the coefficient of variation, and apply $\Var(aX+b)=a^2\Var(X)$. *(Outcome 2c.)*
3. **Extract** mean and variance from a moment generating function — by differentiation at $0$ *and* by kernel recognition (Gamma, Poisson, Binomial, Normal). *(Outcome 2d.)*
4. **Deploy** the Darth Vader rule $\E[X]=\int_0^\infty S(x)\,dx$ (and its discrete sum) on sight of a survival function with $X\ge0$, integrating only over the support when $X$ is bounded.

> **Gym rematch pointers (🧴 Potion).** Miss item 1 $\to$ re-read Concepts 1–2 + WE 7.1. Miss item 2 $\to$ Concept 3 + WE 7.1 / C7.8. Miss item 3 $\to$ Concept 4 + WE 7.2 / C7.6, C7.10. Miss item 4 $\to$ Concept 5 + WE 7.3 + C7.13, C7.14.

*Onward — where these single numbers become whole named families: the discrete distributions waiting in Celadon.*
