<!--
  file: ch12_normal_clt
  tier: A
  outcomes: 2d,3i
  tia: B.4
  locale: The Grand Gathering (P1 Grand Prix / League qualifier)
  type: normal
  maps_to: a vast trainer gathering — thousands of unpredictable results aggregate into a predictable bell; no badge
-->

# The Bell of the Gathering — Normal & the Central Limit Theorem {.type-normal}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with the journey now between Saffron and Cinnabar; a great stadium icon marks the League qualifier gathering, the staging ground before the final cities." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 10 — you have crossed the smooth wilds and arrived at the <strong>Grand Gathering</strong>: a League qualifier where thousands of trainers' results pile up into a single, predictable <em>bell</em>. No gym, no badge — just the most universal curve in all of probability, and the theorem that explains why it is everywhere.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "Ten Thousand Trainers"**

You step into the qualifier grounds and the scale stops you cold. This is not a gym, not a single duel — it is a *gathering*. Thousands of trainers have come to register for the road to the Indigo Plateau, and the central scoreboard is trying to summarize them all at once.

A single trainer's result is hopeless to predict. One battles like a champion; the next freezes; a third gets a lucky type matchup. Pikachu watches one nervous rookie fumble a Poké Ball and shrugs — *who could call that?* Each individual score is its own little coin-flip of nerves, luck, and skill.

And yet. The scoreboard's master display does something uncanny. As the results stream in — one, then a hundred, then ten thousand — the cloud of individual scores collects itself into a smooth, symmetric **bell**: tall in the middle, where most trainers land, tailing off gently to the rare prodigies and the rare disasters. The chaos of ten thousand unpredictable trainers has become a single, *predictable* shape.

"That's the curve Oak keeps muttering about," Misty says. "Heights, measurement errors, the sum of many small shocks — they all end up looking like that. He calls it the *normal*."

A registrar leans over. "We pay out a participation purse on every match. We can't predict one purse. But we budgeted for the *total* of all of them — and we need to know the chance we blow the budget. Also: the banner for the day goes to anyone who wins **at least 180** of their 400 skirmish rounds. How many trainers clear that bar?"

She slides a single laminated card across the desk: a **standard normal table**. "This is the only outside help you get. No formula sheet, no calculator memory — just this table and your head."

Pikachu's cheeks spark. The total purse is a *sum* of thousands of random pieces. The banner count is a whole number of *wins*. Both are piles of randomness — and both, somehow, the scoreboard is about to predict with one bell-shaped curve and one laminated card. *But how does adding up thousands of unpredictable things produce something you can predict — and how do you turn that card into an answer?*
:::

## Where You Are — 60-Second Retrieval

**Rank: seasoned traveler · six badges in hand** (Cascade, Thunder, Boulder, Rainbow, Soul, Marsh). You have crossed the smooth, continuous world: in Saffron you learned that for a continuous variable, **probability is area under a density curve**, and you met the **normal bell** and the move that tames it — **standardization** $Z=(X-\mu)/\sigma$. Just before this you summed exponential waits into gammas and learned the rule that **means add and, for independent pieces, variances add**.

This chapter stands on exactly those two foundations: the normal density (probability = area, read through one table) and the add-up-the-pieces arithmetic of sums. Take sixty seconds and prove you still own them before reading on.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the road behind you**

Answer from memory; if any feels shaky, flip back before continuing.

1. For a continuous $X$, how do you get $P(a<X<b)$ from the density $f$? *(Answer: integrate — it's the area $\int_a^b f$.)*
2. If $X_1,\dots,X_n$ are independent with the *same* variance $\sigma^2$, what is $\Var(X_1+\cdots+X_n)$? *(Answer: $n\sigma^2$ — variances of independent pieces add.)*
3. The standard-normal cdf $\Phi(z)$ gives which area — left of $z$ or right of $z$? *(Answer: the **left** area, $P(Z\le z)$.)*

All three instant? You're ready for the bell. Any hesitation? The retrieval *is* the lesson — go reclaim it, then come back.
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice crackles through the Pokédex's Actuary Mode as you stare at the self-assembling bell.

"Ash — this gathering teaches the two ideas that make actuarial science *possible at scale.* The first is the **normal distribution**: the one curve so universal that the exam hands you its table, because almost every aggregate quantity ends up shaped like it. The second is the reason *why* — the **Central Limit Theorem**: add up many independent random pieces and the total goes bell-shaped no matter what the pieces looked like. Learn to standardize, read the table, and apply the CLT — including the half-unit **continuity correction** for whole-number counts — and you can price a pool of thousands of policies with nothing but that laminated card. This is a **Tier A** topic, and it is on nearly every sitting. Take it slowly."

By the end of this chapter you will be able to:

- **State and use the normal density** $X\sim\Normal(\mu,\sigma^2)$ — recognize its parameters, sketch the bell, and apply the **68–95–99.7** rule. *(Outcome 2d.)*
- **Standardize** any normal via $Z=(X-\mu)/\sigma$ and read tails, bands, and inverse percentiles off the $\Phi$ table, using symmetry $\Phi(-z)=1-\Phi(z)$ and **linear interpolation** between table rows. *(Outcome 2d.)*
- **Apply the Central Limit Theorem**: attach the right mean and spread to a **sum** ($n\mu,\ \sqrt n\,\sigma$) or a **mean** ($\mu,\ \sigma/\sqrt n$), standardize, and read the probability off the table. *(Outcome 3i.)*
- **Deploy the continuity correction**: when a *discrete* sum (binomial, Poisson) is approximated by the normal, slide the boundary by $\pm\tfrac12$ in the correct direction before standardizing — and explain *why* the half-unit is needed. *(Outcome 3i.)*

> *Exam-weight signpost.* The normal sits inside the Univariate block (44–50% of the exam) and the CLT inside Multivariate (23–30%); between them, "standardize and read $\Phi$" and "sum/average of many — find the probability" are among the **most frequently tested** moves on Exam P. This is a **Tier A** chapter and earns the full nine-beat treatment for every concept, with extra room for the CLT and continuity correction.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own the Gathering?**

Already fluent? Prove it. Work these five, ~3 minutes each, *with the table method* (use the excerpt below or Appendix C):

1. $X\sim\Normal(50,8^2)$. Find $P(X>62)$ and $P(42<X<66)$.
2. $X\sim\Normal(0,1)$. Find the $90$th percentile $z_{0.90}$, interpolating between $\Phi(1.28)=0.8997$ and $\Phi(1.29)=0.9015$.
3. A sum of $100$ i.i.d. purses, each mean $500$, SD $150$. Approximate $P(\text{total}>52{,}000)$.
4. The average reaction time of $n=100$ i.i.d. draws, each mean $70$, SD $10$. Approximate $P(\bar X>72)$.
5. $X\sim\Binom(400,0.4)$. With continuity correction, approximate $P(X\ge 180)$.

*(Answers: $0.0668$ and $0.8185$; $z_{0.90}\approx 1.2817$; $\approx 0.0918$ using $z=1.33$; $\approx 0.0228$; $\approx 0.0233$ using $z=1.99$.)* Five for five with the right method? **Skip to the Gym Challenge.** Any miss or hesitation? The teaching below was built exactly for you — and each concept has its own skip-gate, so even a partial owner loses no time.
:::

---

Five ideas build on one another here, in increasing difficulty. We teach them **in order**, each with its own "do you already own this?" skip-check, then the full nine-beat lesson, then a Pokédex Entry you can carry into the exam:

1. **The normal distribution** — the bell, its parameters, and the 68–95–99.7 rule *(the foundation everything uses)*
2. **Standardization** — sliding any bell onto the one table via $Z=(X-\mu)/\sigma$
3. **Reading the $\Phi$ table** — tails, bands, symmetry, inverse lookups, and **interpolation**
4. **The Central Limit Theorem** — the sum and the average go normal *(the crown jewel)*
5. **The continuity correction** — the half-unit fix for discrete sums

## Concept 1 — The Normal Distribution: The Bell and Its Parameters

::: concept-gate
**DO YOU ALREADY OWN THIS? — The normal and 68–95–99.7**

Trainer scores are $X\sim\Normal(\mu=500,\ \sigma^2=100^2)$. Roughly what fraction of trainers score between $400$ and $600$? Between $300$ and $700$?

If you answered **about $68\%$** (within $1\sigma$) and **about $95\%$** (within $2\sigma$), and you know the second slot of $\Normal(\cdot,\cdot)$ is the **variance** $\sigma^2$, not $\sigma$ — **skip to Concept 2**. If "$100^2$" surprised you or you weren't sure of the percentages, this section is for you.
:::

**Beat 1 — The one-sentence idea.** *The normal is the symmetric bell curve, completely pinned down by just two numbers — its center $\mu$ and its spread $\sigma$ — and a fixed fraction of its mass always sits within $1$, $2$, and $3$ standard deviations of the center.*

**Beat 2 — Anchor + concrete instance.** This is the curve from the cold open, the one the scoreboard kept drawing. Take the qualifier scores: they cluster around a typical value and thin out symmetrically on both sides. We model them as $X\sim\Normal(\mu=500,\ \sigma=100)$ — center $500$, spread $100$. We want to know what fraction of trainers land in the "typical" band $400$–$600$, and in the wider band $300$–$700$.

**Beat 3 — Reason through it in plain words.** The band $400$–$600$ is exactly "$500$ give or take $100$" — that is, the mean give or take *one* standard deviation. For *any* normal, that central $1\sigma$ band always captures about $68\%$ of the mass; it is a fixed property of the bell shape, independent of what $\mu$ and $\sigma$ happen to be. The band $300$–$700$ is "the mean give or take *two* standard deviations," which always captures about $95\%$. So roughly $68\%$ of trainers score $400$–$600$, and roughly $95\%$ score $300$–$700$. You did not integrate anything — you read the answer off the bell's universal proportions.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The first trap is misreading the parameters. People see $\Normal(500,100)$ and assume the second number is the standard deviation. **It is the *variance* $\sigma^2$.** If a problem writes $\Normal(500,100)$, the SD is $\sqrt{100}=10$, not $100$ — a tenfold error that wrecks every standardization downstream. We will *always* write $\Normal(\mu,\sigma^2)$ and say the variance out loud, but a careless reader can lose a whole problem here.

$$\Normal(500,100)\ \text{means}\ \sigma^2=100,\ \sigma=10 \quad\textbf{— not}\quad \sigma=100. $$

The second trap is thinking the $68$–$95$–$99.7$ percentages depend on the particular numbers. They do not: every normal, rescaled, is the *same* bell, so those fractions are carved in stone.

**Beat 5 — Translate into notation, one glyph at a time.** Write $X\sim\Normal(\mu,\sigma^2)$, read aloud *"$X$ is normal with mean $\mu$ and variance $\sigma^2$."* The density — the height of the bell at $x$ — is

$$f(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\!\left[-\frac{(x-\mu)^2}{2\sigma^2}\right].$$

Read it piece by piece. The $\exp[-(x-\mu)^2/\cdots]$ is the heart: $(x-\mu)^2$ measures *how far $x$ is from the center, squared*, so the height falls off symmetrically as you move either way from $\mu$ — that is the bell. Dividing the squared distance by $2\sigma^2$ sets *how fast* it falls off: a big $\sigma$ makes the exponent shrink slowly, so the bell is wide and flat; a small $\sigma$ makes it plunge, so the bell is tall and narrow. The front factor $\tfrac{1}{\sigma\sqrt{2\pi}}$ is only there to force the total area to $1$. You will essentially never plug numbers into this formula — its antiderivative is not elementary, which is *why* we use a table — but you should recognize it on sight and read $\mu$ and $\sigma$ straight out of it.

**Beat 6 — Derive the key facts from the shape.** Two facts you can get without calculus. First, **symmetry**: $f(x)$ depends on $x$ only through $(x-\mu)^2$, which is unchanged if you reflect $x$ across $\mu$ (replace $x-\mu$ by $-(x-\mu)$). So the bell is a mirror image about $\mu$ — meaning $\mu$ is simultaneously the **mean, median, and mode**, and the area to the left of $\mu$ is exactly $0.5$. Second, the **68–95–99.7 rule** is the statement that

$$P(\mu-k\sigma<X<\mu+k\sigma)\approx \begin{cases}0.68 & k=1\\ 0.95 & k=2\\ 0.997 & k=3.\end{cases}$$

These are not three separate facts to memorize blindly — they are three readings of *one* universal bell (Concept 2 shows that every normal collapses onto it), and in Concept 3 you will reproduce them exactly from the table: e.g. within $2\sigma$ is $2\Phi(2)-1=2(0.9772)-1=0.9544\approx 95\%$.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* read parameters and apply the rule, as with the qualifier scores ($68\%$, $95\%$).
- *A twist (one-sided pieces):* by symmetry, $P(X>\mu+\sigma)=\tfrac{1-0.68}{2}=0.16$ — half of the $32\%$ that falls *outside* the $1\sigma$ band lies in each tail.
- *General:* once you can standardize (next concept), you compute the fraction in *any* band, not just the three special ones.
- *Edge:* the bell never touches zero — there is always a sliver of mass arbitrarily far out, so "no maximum possible value" is built in. That is why the normal is sometimes a poor model for quantities that *can't* go negative (a loss, a height): it assigns them a tiny but nonzero left tail.

**Beat 8 — Picture it.** Every normal is the *same* bell, only relabeled; the $68$–$95$–$99.7$ bands are nested shells of mass around the center.

<figure>
<img src="../../assets/diagrams/ch12_normal_6895997.png" alt="The standard normal bell curve centered at the mean mu, with three nested shaded bands. The innermost band from mu minus one sigma to mu plus one sigma is labeled 68 percent; the next band out to plus or minus two sigma is labeled 95 percent; the widest band out to plus or minus three sigma is labeled 99.7 percent. Dotted vertical lines mark each sigma boundary, and the x-axis is labeled in units of mu plus or minus k sigma.">
<figcaption>The 68–95–99.7 rule. About $68\%$ of the mass sits within $1\sigma$ of the mean, $95\%$ within $2\sigma$, and $99.7\%$ within $3\sigma$ — the same fractions for <em>every</em> normal, because every normal is this one bell relabeled.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can read $\mu$ and $\sigma$ from a $\Normal(\mu,\sigma^2)$ statement (remembering the second slot is variance), sketch the symmetric bell, and quote the fraction of mass within $1$, $2$, or $3$ standard deviations on sight.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Normal $\Normal(\mu,\sigma^2)$**

$$f(x)=\frac{1}{\sigma\sqrt{2\pi}}\exp\!\left[-\frac{(x-\mu)^2}{2\sigma^2}\right],\qquad \E[X]=\mu,\qquad \Var(X)=\sigma^2,\qquad M(t)=\exp\!\left(\mu t+\tfrac12\sigma^2 t^2\right).$$

Symmetric about $\mu$ (mean = median = mode). **68–95–99.7:** within $1/2/3$ standard deviations sits $\approx 68\%/95\%/99.7\%$ of the mass.

*In plain terms:* the universal bell, fixed by a center $\mu$ and a spread $\sigma$. The second slot of $\Normal(\mu,\sigma^2)$ is the **variance**; take a square root to get the SD.

*Recognition cue:* "normally distributed," a symmetric bell, "mean … standard deviation …," heights/errors/test scores/aggregates $\to$ normal. You will solve it through the table, never by integrating the density.
:::

::: pokedex-entry
**POKÉDEX SCAN — №035 Clefairy, the Bell Pokémon**

<img src="../../assets/sprites/front/35.png" alt="Clefairy, the round, pink Bell Pokémon of Mt. Moon" style="width:96px; float:right; image-rendering: pixelated; margin:0 0 0.5em 0.8em;">

*Mascot for the Normal distribution (fidelity: the Mt. Moon "bell" that draws crowds from every direction, settling them into one symmetric gathering).*

- **Support:** $x\in\mathbb{R}$ (all real numbers — both tails run forever).
- **pdf:** $f(x)=\dfrac{1}{\sigma\sqrt{2\pi}}\,e^{-(x-\mu)^2/(2\sigma^2)}$.
- **Mean:** $\mu$.  **Variance:** $\sigma^2$.  **MGF:** $e^{\mu t+\sigma^2 t^2/2}$.
- **Type:** continuous, symmetric.
- **Special move — *Standardize*:** any Clefairy collapses onto the one standard bell $\Normal(0,1)$.
:::

## Concept 2 — Standardization: One Bell to Rule Them All

::: concept-gate
**DO YOU ALREADY OWN THIS? — Standardization**

Sabrina's reading is $X\sim\Normal(50,8^2)$. Using $\Phi(1.5)=0.9332$, find $P(X>62)$.

If you answered **$P(X>62)=1-\Phi(1.5)=0.0668$** (standardize to $z=\tfrac{62-50}{8}=1.5$, then take the *right* tail), **skip to Concept 3**. If you got $0.9332$ (the *left* area) or weren't sure how to turn $62$ into a $z$, read on.
:::

**Beat 1 — The one-sentence idea.** *You never need a separate table for each normal — subtract the mean and divide by the SD to turn any $X\sim\Normal(\mu,\sigma^2)$ into the one standard normal $Z\sim\Normal(0,1)$, then read every probability off a single table.*

**Beat 2 — Anchor + concrete instance.** The normal density has no elementary antiderivative — there is no clean formula for its area. So actuaries tabulate the area for *one* normal, the standard $\Normal(0,1)$, and route every other normal through it. Take Sabrina's psi-reading $X\sim\Normal(50,8^2)$ (mean $50$, SD $8$). Admission requires $P(X>62)$.

**Beat 3 — Reason through it in plain words.** Don't ask "what is $X$?" Ask "*how many standard deviations above the mean* is the value $62$?" It sits $62-50=12$ above the center, and each standard deviation is $8$ wide, so $62$ is $\tfrac{12}{8}=1.5$ standard deviations above the mean. That "$1.5$ SDs above" is a *pure, unit-free* statement — it means the same thing for Sabrina's psi-units as for dollars or seconds. The table is built exactly to answer "how much mass lies beyond $1.5$ SDs?" The table gives the *left* area $\Phi(1.5)=0.9332$; the chance of *exceeding* $1.5$ SDs is the right tail:

$$P(X>62)=P(Z>1.5)=1-\Phi(1.5)=1-0.9332=0.0668.$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** The classic error is to report the table value directly when the question wants a *right* tail:

$$P(X>62)\overset{?}{=}\Phi(1.5)=0.9332.\qquad\textbf{(wrong — that is }P(X<62)\text{)}$$

A reading $1.5$ SDs *above* the mean is rare, so its probability must be *small*. $0.93$ is the chance of being *below* it. Always sanity-check against the picture: **above-center tails are small; below-center left-areas are under $0.5$.** Burn in the reflex — *the table gives the left area; for a right tail, subtract from $1$.*

**Beat 5 — Translate into notation, one glyph at a time.** The standardizing transformation is

$$Z=\frac{X-\mu}{\sigma}\sim\Normal(0,1),\qquad\text{read aloud: ``}Z\text{ equals }X\text{ minus the mean, over the SD.''}$$

The numerator $X-\mu$ re-centers (so the new mean is $0$); the denominator $\sigma$ rescales (so the new SD is $1$). The standard-normal cdf is $\Phi(z)$, *"big phi of }z\text{,"* the tabulated **left** area $P(Z\le z)$. Two identities you will use constantly:

$$P(X\le x)=\Phi\!\left(\frac{x-\mu}{\sigma}\right),\qquad \Phi(-z)=1-\Phi(z)\ \text{(symmetry)}.$$

**Beat 6 — Derive why standardizing leaves it normal.** Why is $Z$ still a normal — and exactly the *standard* one? Because shifting and scaling a normal keeps it normal (a linear change of variable just relabels the axis), so $Z$ is some normal. Its mean and variance follow from the linearity rules you already own: $\E[Z]=\E[(X-\mu)/\sigma]=(\mu-\mu)/\sigma=0$, and $\Var(Z)=\Var(X-\mu)/\sigma^2=\sigma^2/\sigma^2=1$. A normal with mean $0$ and variance $1$ *is* $\Normal(0,1)$. So every normal probability is genuinely one $\Phi$ lookup — nothing is lost in the translation.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* a one-sided tail, $P(X>62)=1-\Phi(1.5)=0.0668$.
- *Twist (a two-sided band):* standardize *both* ends and difference. For $P(42<X<66)$: $\tfrac{42-50}{8}=-1$ and $\tfrac{66-50}{8}=2$, so $\Phi(2)-\Phi(-1)=0.9772-(1-0.8413)=0.8185$.
- *General (within $k\sigma$):* $P(\mu-k\sigma<X<\mu+k\sigma)=2\Phi(k)-1$; within $2\sigma$ is $2(0.9772)-1=0.9544$ — there is the $95\%$ of Concept 1, derived.
- *Edge (negative $z$):* the table has no negative rows. Use symmetry: $\Phi(-1)=1-\Phi(1)=1-0.8413=0.1587$.

**Beat 8 — Picture it.** Standardizing slides the center to $0$ and rescales the spread to $1$, overlaying any bell on the single table curve — and the shaded tail comes along unchanged.

<figure>
<img src="../../assets/diagrams/ch12_standardize.png" alt="Two bell curves side by side. On the left, the raw normal with mean 50 and standard deviation 8, with the right tail beyond x equals 62 shaded, labeled P of X greater than 62. A green arrow in the center shows the transformation Z equals X minus mu over sigma equals (62 minus 50) over 8 equals 1.5. On the right, the standard normal with mean 0 and SD 1, with the matching right tail beyond z equals 1.5 shaded, labeled 1 minus Phi of 1.5 equals 1 minus 0.9332 equals 0.0668.">
<figcaption>Standardizing. The raw $\Normal(50,8^2)$ slides and rescales onto the standard bell; the value $62$ becomes $z=1.5$, and the right-tail probability is read as $1-\Phi(1.5)=0.0668$. Every normal probability is one $\Phi$ lookup.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can turn any $\Normal(\mu,\sigma^2)$ probability into a $Z$-lookup: standardize the boundary(ies), then read tails ($1-\Phi$), bands (a difference of $\Phi$'s), and negatives (symmetry).

::: trainers-tip
**TRAINER'S TIP — Standardize on the TI-30XS without retyping (STO▸ μ and σ)**

When several parts of a problem share the same $\mu$ and $\sigma$, *store them once* and reuse them — no retyping, no rounding drift. Bank the mean and SD into memory variables: [ 50 [STO▸]{.kbd} [x]{.kbd} ]{.keystroke} and [ 8 [STO▸]{.kbd} [y]{.kbd} ]{.keystroke}. Then each $z$ is one clean expression: [ ( 62 [−]{.kbd} [x]{.kbd} ) [÷]{.kbd} [y]{.kbd} [enter]{.kbd} ]{.keystroke} returns $1.5$. For the next boundary, just change the numerator — [ ( 66 [−]{.kbd} [x]{.kbd} ) [÷]{.kbd} [y]{.kbd} [enter]{.kbd} ]{.keystroke}. The machine has no $\Phi$ button, so once you have $z$, go to the **table** — that is the whole point of the laminated card.
:::

## Concept 3 — Reading the Φ Table: Tails, Bands, Symmetry, and Interpolation

::: concept-gate
**DO YOU ALREADY OWN THIS? — Reading and interpolating the table**

Using $\Phi(1.28)=0.8997$ and $\Phi(1.29)=0.9015$, find the value $z_{0.90}$ with $\Phi(z)=0.90$ (the $90$th percentile), and find $P(Z<-0.75)$ given $\Phi(0.75)=0.7734$.

If you answered **$z_{0.90}\approx 1.2817$** (linear interpolation between the two rows) and **$P(Z<-0.75)=1-0.7734=0.2266$** (symmetry), **skip to Concept 4**. If interpolation or the negative-$z$ flip is rusty, read on.
:::

**Beat 1 — The one-sentence idea.** *The $\Phi$ table is a lookup of left-areas at two-decimal $z$ values; you turn it into tails, bands, and inverse percentiles with three moves — subtract from $1$, difference two rows, or reflect with $\Phi(-z)=1-\Phi(z)$ — and you fill the gaps between rows by linear interpolation.*

**Beat 2 — Anchor + concrete instance.** Here is the laminated card the registrar gave you — a standard-normal $\Phi(z)$ excerpt. (The full table is Appendix C; for every worked example in this book we use $z$ rounded to **two decimals** so your answer matches the exam's table method.)

| $z$ | $\Phi(z)$ | | $z$ | $\Phi(z)$ | | $z$ | $\Phi(z)$ |
|---|---|---|---|---|---|---|---|
| $0.00$ | $0.5000$ | | $1.00$ | $0.8413$ | | $1.75$ | $0.9599$ |
| $0.25$ | $0.5987$ | | $1.04$ | $0.8508$ | | $1.96$ | $0.9750$ |
| $0.50$ | $0.6915$ | | $1.25$ | $0.8944$ | | $1.99$ | $0.9767$ |
| $0.67$ | $0.7486$ | | $1.28$ | $0.8997$ | | $2.00$ | $0.9772$ |
| $0.71$ | $0.7611$ | | $1.29$ | $0.9015$ | | $2.04$ | $0.9793$ |
| $0.75$ | $0.7734$ | | $1.33$ | $0.9082$ | | $2.05$ | $0.9798$ |
| $0.84$ | $0.7995$ | | $1.50$ | $0.9332$ | | $2.33$ | $0.9901$ |

Two tasks: find the $90$th percentile $z_{0.90}$ (the $z$ with $\Phi(z)=0.90$, which falls *between* table rows), and find $P(Z<-0.75)$ (a negative argument, which has no row).

**Beat 3 — Reason through it in plain words.** The table tells you the left-area at each listed $z$. For a *right* tail, the area beyond $z$ is everything not to the left: $1-\Phi(z)$. For a *band*, the mass between $z_1$ and $z_2$ is the left-area up to $z_2$ minus the left-area up to $z_1$: $\Phi(z_2)-\Phi(z_1)$. For a *negative* $z$, the bell's mirror symmetry says the left tail below $-z$ equals the right tail above $+z$: $\Phi(-z)=1-\Phi(z)$, so $P(Z<-0.75)=1-\Phi(0.75)=1-0.7734=0.2266$. And when the value you need sits *between* two listed rows, you slide proportionally between them — **linear interpolation** — treating the table as a straight line over that tiny gap.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The seductive shortcut on an inverse lookup is to grab the *nearest* row and call it done. We want $\Phi(z)=0.90$; the nearest rows are $\Phi(1.28)=0.8997$ and $\Phi(1.29)=0.9015$. Snapping to $1.28$ gives $0.8997$, which is $0.0003$ short of $0.90$ — close, but on a percentile that error compounds.

$$z_{0.90}\overset{?}{=}1.28.\qquad\textbf{(too crude — }0.90\text{ lies between the rows)}$$

The honest move is to interpolate: $0.90$ is most of the way from $0.8997$ to $0.9015$, so $z_{0.90}$ is most of the way from $1.28$ to $1.29$. (The other half of the trap is forgetting symmetry and hunting for a "$-0.75$" row that does not exist — reflect instead.)

**Beat 5 — Translate into notation, one glyph at a time.** **Linear interpolation** between two table points $(z_1,\Phi_1)$ and $(z_2,\Phi_2)$ for a target area $p$ (with $\Phi_1\le p\le\Phi_2$):

$$z\approx z_1+\underbrace{\frac{p-\Phi_1}{\Phi_2-\Phi_1}}_{\text{fraction of the way}}\,(z_2-z_1).$$

Read the fraction aloud: *"how far $p$ has traveled from $\Phi_1$ toward $\Phi_2$."* Multiply that fraction by the $z$-gap and add it to the lower $z$. The same formula runs *forward* too — to interpolate $\Phi$ at a $z$ between rows, swap the roles of $z$ and $\Phi$.

**Beat 6 — Derive the percentile by interpolation.** Plug in $p=0.90$, $(z_1,\Phi_1)=(1.28,0.8997)$, $(z_2,\Phi_2)=(1.29,0.9015)$:

$$\frac{p-\Phi_1}{\Phi_2-\Phi_1}=\frac{0.90-0.8997}{0.9015-0.8997}=\frac{0.0003}{0.0018}=0.1\overline{6},$$
$$z_{0.90}\approx 1.28+0.1\overline{6}\times(1.29-1.28)=1.28+0.00167=1.2817.$$

So $z_{0.90}\approx 1.2817$ (the exact value is $1.28155\ldots$; interpolation nails it). The common rounded exam value is $z_{0.90}\approx 1.28$, and for the well-known percentiles you should simply *memorize* the round numbers: $z_{0.90}\approx 1.282$, $z_{0.95}\approx 1.645$, $z_{0.975}\approx 1.960$, $z_{0.99}\approx 2.326$.

**Beat 7 — Ramp the difficulty.**

- *Simplest (forward lookup):* $P(Z\le 1.50)=\Phi(1.50)=0.9332$, straight off the row.
- *Right tail:* $P(Z>1.33)=1-\Phi(1.33)=1-0.9082=0.0918$.
- *Band:* $P(-1<Z<2)=\Phi(2)-\Phi(-1)=0.9772-(1-0.8413)=0.8185$.
- *Inverse with interpolation:* the percentile above, $z_{0.90}\approx 1.2817$.
- *Edge (raw-scale percentile):* once you have $z_p$, the raw value is $x_p=\mu+z_p\sigma$. The $90$th-percentile qualifier score, with $\mu=500,\sigma=100$, is $500+1.282(100)=628.2$.

**Beat 8 — Table reference.** Keep the picture from Concept 2 in mind: $\Phi(z)$ is always the area to the *left* of $z$ under the standard bell. The excerpt above (and Appendix C in full) is the only outside aid you get on exam day — practice until tail/band/symmetry/interpolation are reflexes.

**Beat 9 — Consolidate.** You can read a left-area off the row, convert it to a tail ($1-\Phi$) or band ($\Phi_2-\Phi_1$), reflect a negative argument with $\Phi(-z)=1-\Phi(z)$, interpolate between rows for both forward and inverse lookups, and convert a $z$-percentile back to the raw scale with $x_p=\mu+z_p\sigma$.

::: pokedex-entry
**POKÉDEX ENTRY №02 — Standardize & Read the Table**

$$Z=\frac{X-\mu}{\sigma}\sim\Normal(0,1),\quad P(X\le x)=\Phi\!\left(\frac{x-\mu}{\sigma}\right),\quad \Phi(-z)=1-\Phi(z).$$

**Three reading moves:** right tail $=1-\Phi(z)$ · band $=\Phi(z_2)-\Phi(z_1)$ · negative $z$ by symmetry.
**Interpolation** for a target area $p$ between rows: $z\approx z_1+\dfrac{p-\Phi_1}{\Phi_2-\Phi_1}(z_2-z_1)$.
**Memorize:** $z_{0.90}\approx 1.282,\ z_{0.95}\approx 1.645,\ z_{0.975}\approx 1.960,\ z_{0.99}\approx 2.326$; raw percentile $x_p=\mu+z_p\sigma$.

*Recognition cue:* any normal probability or percentile $\to$ standardize, then read $\Phi$ (left area), adjusting for tail/band/sign/between-rows.
:::

## Concept 4 — The Central Limit Theorem: Many Draws Go Normal

::: concept-gate
**DO YOU ALREADY OWN THIS? — The CLT**

A sum of $100$ i.i.d. purses, each mean $500$, SD $150$. Approximate $P(\text{total}>52{,}000)$.

If you answered **$\approx 0.0918$** — standardizing with $z=\dfrac{52{,}000-100\cdot500}{\sqrt{100}\cdot 150}=1.33$ and reading $1-\Phi(1.33)$ — **skip to Concept 5**. If you used SD $=150$ instead of $\sqrt{100}\cdot 150=1500$, read on: that is the single most-punished CLT slip.
:::

**Beat 1 — The one-sentence idea.** *Add up many independent random pieces and the total settles into a bell curve — whatever shape the pieces had — so you need only its mean and variance to read a probability off the normal table.*

**Beat 2 — Anchor + concrete instance.** You already know (from the road behind you) the mean and variance of a sum of independent draws: means add, and variances add. The CLT adds the astonishing extra fact that, for *many* draws, the *shape* of that sum is **normal** — which lets you reuse the one table.

The registrar's question: there are $n=100$ matches today, each paying an independent purse $X_i$ with mean $\mu=500$ and SD $\sigma=150$ Poké-dollars. The League budgeted $52{,}000$. *What is the chance the total payout overruns the budget?*

**Beat 3 — Reason through it in plain words.** First nail the mean and spread of the **total** $S=X_1+\cdots+X_{100}$. Means add, so the expected total is $100\times 500=50{,}000$. Variances of independent pieces add, so $\Var(S)=100\times 150^2$, and the **standard deviation of the total** is $\sqrt{100}\times 150=1500$ — *not* $150$. The budget $52{,}000$ sits $\dfrac{52{,}000-50{,}000}{1500}=1.33$ standard deviations above the expected total. The CLT says $S$ is approximately normal, so "$1.33$ SDs above" reads straight off the table:

$$P(S>52{,}000)\approx 1-\Phi(1.33)=1-0.9082=0.0918.$$

About a **$9\%$** chance of a budget overrun — knowable from the bell, even though no single purse is predictable.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The fatal slip is to standardize the *total* with a *single-draw* SD:

$$z\overset{?}{=}\frac{52{,}000-50{,}000}{150}=13.3.\qquad\textbf{(wrong)}$$

That treats a sum of a hundred purses as if it wiggled as little as one purse — absurd. A sum of many random pieces is *more* variable in absolute terms (its SD grows like $\sqrt n$), so the divisor must be $\sqrt{100}\cdot150=1500$, giving $z=1.33$, not $13.3$. The matching error for an **average** is dividing by $\sigma$ instead of $\sigma/\sqrt n$. **Get the right spread under the $z$, and the rest is one lookup.**

**Beat 5 — Translate into notation, one glyph at a time.** The "approximately distributed as" sign is a dotted tilde:

$$S_n\ \dot\sim\ \Normal(\mu_S,\sigma_S^2),\qquad\text{read aloud: ``}S_n\text{ is approximately normal with mean }\mu_S,\text{ variance }\sigma_S^2\text{.''}$$

Here $\Normal(\text{mean},\text{variance})$ is the normal of Concept 1, and $\Phi$ is its standard cdf, read off the table. *Standardizing* — subtract the mean, divide by the SD — is the Concept 2 move that turns this into a lookup.

**Beat 6 — State the theorem and the two standardizations.** Let $X_1,\dots,X_n$ be i.i.d. with mean $\mu$ and finite variance $\sigma^2$. For large $n$, both the sum $S_n=\sum_{i=1}^n X_i$ and the mean $\bar X_n=S_n/n$ are approximately normal — and we get their means/variances straight from the add-up rules (means add; independent variances add; dividing by $n$ divides the variance by $n^2$):

$$\boxed{\;S_n\ \dot\sim\ \Normal\!\big(n\mu,\ n\sigma^2\big),\qquad \bar X_n\ \dot\sim\ \Normal\!\Big(\mu,\ \tfrac{\sigma^2}{n}\Big).\;}$$

Evaluate any probability by standardizing and reading $\Phi$:

$$P(S_n\le s)\approx \Phi\!\left(\frac{s-n\mu}{\sqrt n\,\sigma}\right),\qquad P(\bar X_n\le \bar x)\approx \Phi\!\left(\frac{\bar x-\mu}{\sigma/\sqrt n}\right).$$

The only things that change are which mean ($n\mu$ for a sum, $\mu$ for an average) and which spread ($\sqrt n\,\sigma$ for a sum, $\sigma/\sqrt n$ for an average) go under the $z$. Notice the *average's* SD *shrinks* with $n$, while the *sum's* SD *grows* — opposite directions, same $\sqrt n$.

**Beat 7 — Ramp the difficulty.**

- *Simplest — a sum.* The prize pool: $z=1.33$, $P(S>52{,}000)\approx 0.0918$.
- *An average.* Reaction time, $\mu=70$ ms, $\sigma=10$ ms, $n=100$: $\bar X\ \dot\sim\ \Normal(70,1)$ (since $\sigma/\sqrt n=1$), so $P(\bar X>72)=1-\Phi(2)=0.0228$.
- *Sample-size design.* "Sample mean within $1$ of the truth w.p. $0.95$" demands $1.96\cdot\tfrac{\sigma}{\sqrt n}\le 1$ — solve for $n$ (a Gym Battle).
- *Boundary:* the approximation sharpens as $n$ grows; for skewed pieces you want $n$ in the tens before trusting it. For a *discrete* sum it needs one more fix — Concept 5.

**Beat 8 — Picture it.** Watch the bell *emerge*: the sample mean of flat $\Unif(0,1)$ draws starts flat, turns triangular, and is indistinguishable from a normal by $n=30$ — and narrows as $n$ grows, exactly the $\sigma^2/n$ shrinkage.

<figure>
<img src="../../assets/diagrams/ch12_clt_convergence.png" alt="Four histograms of the sample mean of n i.i.d. Uniform(0,1) draws, for n equals 1, 2, 5, and 30, each with a red normal curve overlaid. At n equals 1 the histogram is flat (uniform); at n equals 2 it is triangular; at n equals 5 it is already bell-like; by n equals 30 it is visually indistinguishable from the red normal curve and noticeably narrower, because the variance shrinks like sigma squared over n.">
<figcaption>The CLT in action. The sample mean of $\Unif(0,1)$ draws starts flat ($n=1$), turns triangular ($n=2$), and is indistinguishable from the red normal by $n=30$ — and tightens as $n$ grows, the $\sigma^2/n$ shrinkage.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can take any sum or average of many i.i.d. draws, attach the right mean and spread ($n\mu,\sqrt n\sigma$ for a sum; $\mu,\sigma/\sqrt n$ for a mean), standardize, and read the probability off the table — no exact distribution required.

::: pokedex-entry
**POKÉDEX ENTRY №03 — The Central Limit Theorem**

For i.i.d. $X_1,\dots,X_n$ with mean $\mu$ and finite variance $\sigma^2$, for large $n$:
$$S_n\ \dot\sim\ \Normal\!\big(n\mu,\ n\sigma^2\big),\qquad \bar X_n\ \dot\sim\ \Normal\!\Big(\mu,\ \tfrac{\sigma^2}{n}\Big),$$
$$P(S_n\le s)\approx \Phi\!\left(\frac{s-n\mu}{\sqrt n\,\sigma}\right),\qquad P(\bar X_n\le \bar x)\approx \Phi\!\left(\frac{\bar x-\mu}{\sigma/\sqrt n}\right).$$

*In plain terms:* add up many independent pieces and the total goes bell-shaped whatever the pieces looked like — you need only their mean and variance.

*Recognition cue:* "total / average / sum of many" independent draws, a request for a **probability** with **no exact distribution** given, a large $n$. Spread under the $z$ is $\sqrt n\,\sigma$ for a sum, $\sigma/\sqrt n$ for an average — never the single-draw $\sigma$.
:::

## Concept 5 — The Continuity Correction: The Half-Unit Fix

::: concept-gate
**DO YOU ALREADY OWN THIS? — Continuity correction**

$X\sim\Binom(400,0.4)$. With the normal approximation **and continuity correction**, approximate $P(X\ge 180)$.

If you answered **$\approx 0.0233$** — shifting "$\ge 180$" to "$>179.5$" before standardizing, $z=\tfrac{179.5-160}{\sqrt{96}}\approx 1.99$, then $1-\Phi(1.99)$ — **skip to the Worked Examples**. If you standardized $180$ directly, read on: the half-unit shift is worth real points.
:::

**Beat 1 — The one-sentence idea.** *When you approximate a whole-number count by a smooth normal curve, each integer "owns" a bar half a unit wide on each side — so shift the boundary by $\pm\tfrac12$ before standardizing, to capture (or exclude) that whole bar.*

**Beat 2 — Anchor + concrete instance.** The CLT approximates a *discrete* count — a binomial number of wins, a Poisson number of claims — by a *continuous* normal. But here is the tension that *forces* a correction: a continuous curve assigns probability **zero** to any single point (Concept 0 of Saffron — area over a zero-width slice is zero), while a count genuinely lands *on* the integers, each carrying real positive probability. If you naively integrate the smooth curve, you systematically lose the probability that lives exactly *at* the boundary integer. The continuity correction repairs exactly that loss.

Across the qualifier you play $n=400$ independent skirmish rounds, each won w.p. $p=0.4$. The banner goes to anyone with **at least $180$** wins. *Approximate the chance you earn the banner.*

**Beat 3 — Reason through it in plain words.** Wins $X\sim\Binom(400,0.4)$ has mean $\mu=np=160$ and SD $\sigma=\sqrt{np(1-p)}=\sqrt{96}\approx 9.80$. Picture the binomial as a row of bars, one per integer, each bar centered on its integer and **one unit wide** — so the bar for "$180$" stretches from $179.5$ to $180.5$, and the *probability* $P(X=180)$ is the *area* of that bar under the approximating normal. "At least $180$" must include the *whole* $180$ bar, so the smooth normal area should start at the bar's **left edge, $179.5$** — not at $180$, which would slice the bar in half and throw away half of $P(X=180)$. Standardize the corrected boundary:

$$z=\frac{179.5-160}{9.80}\approx 1.99,\qquad P(X\ge 180)\approx 1-\Phi(1.99)=1-0.9767=0.0233.$$

About a **$2.3\%$** chance of the banner.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Skipping the shift standardizes the integer itself:

$$z\overset{?}{=}\frac{180-160}{9.80}=2.04,\qquad 1-\Phi(2.04)=1-0.9793=0.0207.\qquad\textbf{(uncorrected — off)}$$

It chops the $180$ bar down the middle and discards half of it. Corrected $0.0233$ vs. uncorrected $0.0207$ differ enough that an exam will often list *both* as answer choices to catch you. The other half of the trap is the **direction**: for $P(X\ge 180)$ you slide *down* to $179.5$ (so $180$ stays *in*); for $P(X>180)$ you slide *up* to $180.5$ (so $180$ goes *out*). Get the inequality wrong and you correct the wrong way. *(This is exactly the slip Team Rocket is about to make.)*

**Beat 5 — Translate into notation, one glyph at a time.** Let $k$ be the integer boundary. The shift is $\pm\tfrac12$, chosen so the *named* integer is *included* on the side the inequality points:

$$P(X\ge k)\approx 1-\Phi\!\left(\frac{(k-\tfrac12)-\mu}{\sigma}\right),\qquad P(X\le k)\approx \Phi\!\left(\frac{(k+\tfrac12)-\mu}{\sigma}\right).$$

Each integer $k$ owns the interval $[k-\tfrac12,\,k+\tfrac12]$ under the curve — that half-unit on each side is where the correction comes from.

**Beat 6 — Derive the rule for every inequality.** Don't memorize a table blindly — *read it off* the one principle "does the named integer stay in or go out?" Including $k$ means starting/stopping at the *far* edge of its bar; excluding $k$ means starting/stopping at the *near* edge:

| You want | Corrected boundary | Reason |
|---|---|---|
| $P(X\ge k)$ | normal area $>k-\tfrac12$ | include $k$ $\to$ start at its left edge |
| $P(X>k)$ | normal area $>k+\tfrac12$ | exclude $k$ $\to$ start past its right edge |
| $P(X\le k)$ | normal area $<k+\tfrac12$ | include $k$ $\to$ stop at its right edge |
| $P(X<k)$ | normal area $<k-\tfrac12$ | exclude $k$ $\to$ stop before its left edge |
| $P(X=k)$ | $k-\tfrac12$ to $k+\tfrac12$ | the single bar around $k$ |

**Beat 7 — Ramp the difficulty.**

- *Simplest — binomial tail.* The banner: $P(X\ge 180)\to P(\text{normal}>179.5)\approx 0.0233$.
- *Poisson count.* A Poisson total of integer claims is corrected the same way ($\mu=\sigma^2=\lambda$, so $\sigma=\sqrt\lambda$).
- *An exact equality.* $P(X=k)$ needs *both* edges: $\Phi(\tfrac{k+0.5-\mu}{\sigma})-\Phi(\tfrac{k-0.5-\mu}{\sigma})$.
- *Edge — no correction.* When the summed variable is **continuous** (purses, weights, times — as in Concept 4), there is **no** continuity correction; bars only exist for integer-valued counts. Applying $\pm\tfrac12$ to a continuous sum is itself an error.

**Beat 8 — Picture it.** Lay the smooth normal over the binomial bars; the named integer owns a full-width bar, and the corrected boundary lands on its *edge*, not its center.

<figure>
<img src="../../assets/diagrams/ch12_continuity_correction.png" alt="A binomial 400, 0.4 bar histogram centered at 160, with a smooth normal curve overlaid. The bars from 180 upward are shaded as the event X greater than or equal to 180. A green dashed vertical line at 179.5 marks the corrected boundary at the left edge of the 180 bar, and a gray dotted line at 180 shows the naive boundary that would slice that bar in half. The boxed computation gives z equals (179.5 minus 160) over root 96 approximately 1.99, so P(X greater than or equal to 180) approximately 1 minus Phi of 1.99 equals 0.0233.">
<figcaption>The continuity correction. The integer $180$ owns the bar from $179.5$ to $180.5$; to <em>include</em> it in $P(X\ge 180)$ the normal area starts at the left edge $179.5$ — capturing the whole bar, not half. Standardizing $179.5$ gives $z\approx 1.99$ and $P\approx 0.0233$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can spot an *integer-valued* sum, apply the CLT, slide the boundary the correct half-unit in the correct direction, and standardize — and you know never to apply the correction to a *continuous* sum.

::: pokedex-entry
**POKÉDEX ENTRY №04 — The Continuity Correction**

Approximating an integer count $X$ (binomial $\mu=np,\sigma=\sqrt{np(1-p)}$; Poisson $\mu=\sigma^2=\lambda$) by the normal, shift the boundary by $\pm\tfrac12$ so the named integer is on the correct side:

$$P(X\ge k)\to>k-\tfrac12,\quad P(X>k)\to>k+\tfrac12,\quad P(X\le k)\to<k+\tfrac12,\quad P(X<k)\to<k-\tfrac12.$$

*In plain terms:* each integer owns a unit-wide bar, $[k-\tfrac12,k+\tfrac12]$; a zero-width point under a continuous curve has no probability, so spread the integer over its bar. **Only for integer counts** — never for a continuous sum.

*Recognition cue:* normal approximation to a **binomial or Poisson** (a count of wins/claims). Always ask "is the boundary integer in or out?" and slide $\pm\tfrac12$ accordingly.
:::

::: enrichment
**⭐ ENRICHMENT (OFF-SYLLABUS) — The Lognormal: When the Logs Are Normal**

*This box is not on the Exam P syllabus and is not gated or tested here. TIA teaches it because it is the natural companion to the normal, and it pays off on later exams. Skip it with a clear conscience; read it if you're curious where the bell goes next.*

The normal arises from **adding** many small shocks. But many real quantities — insurance losses, stock prices, the size a Magikarp's strength reaches after many *multiplicative* growth spurts — come from **multiplying** many small factors. Take logs, and a product becomes a sum, so the CLT applies to the *logarithm*. A variable $Y$ is **lognormal** when $\ln Y\sim\Normal(\mu,\sigma^2)$; equivalently $Y=e^{X}$ for a normal $X$.

<img src="../../assets/sprites/front/130.png" alt="Gyarados, the evolved form of Magikarp" style="width:96px; float:right; image-rendering: pixelated; margin:0 0 0.5em 0.8em;">

*Mascot: Gyarados — Magikarp's explosive, multiplicative growth into a heavy-tailed giant.*

Key facts (note these are **not** $\mu$ and $\sigma^2$ themselves — the parameters live on the log scale):

$$\E[Y]=e^{\mu+\sigma^2/2},\qquad \Var(Y)=\big(e^{\sigma^2}-1\big)e^{2\mu+\sigma^2}.$$

The payoff is that **every lognormal probability is just a normal probability in disguise** — you standardize the *log*:

$$P(Y\le y)=P(\ln Y\le \ln y)=\Phi\!\left(\frac{\ln y-\mu}{\sigma}\right).$$

So the whole machine you just built — standardize, read $\Phi$ — handles the lognormal with one extra step: take the log of the boundary first. The lognormal is right-skewed and lives on $(0,\infty)$, which makes it a far better model than the normal for a *loss* (which can't go negative). You'll meet it for real in severity modeling on STAM/MAS-I.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/front/35.png" alt="Clefairy, the Bell Pokémon" style="width:120px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Clefairy — the Bell Pokémon, your guide through the gathering</figcaption>
</figure>

Four examples, fading from fully narrated to exam-speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because the standardize-and-CLT move is the load-bearing, most-tested skill of the chapter. Every $\Phi$ value comes from the Concept-3 table excerpt (two-decimal $z$), so your answers match the exam's table method.

### Worked Example 1 — Sabrina's Reading, Standardized (full narration; understanding-first)

**ARCHETYPE:** *Standardize a single normal — right tail and two-sided band (Entries №01–№02).*

**Setup.** A returning psychic's reading is $X\sim\Normal(50,8^2)$ (mean $50$, SD $8$). Find (a) $P(X>62)$ and (b) $P(42<X<66)$.

**Step 1 — Identify.** A single normal, asked for a tail and a band $\to$ standardize each boundary and read $\Phi$. Givens: $\mu=50$, $\sigma=8$.

**Step 2 — Professor's Path (the why).** Probability for a normal is area under the bell, and the bell has no elementary antiderivative — so we route through the *one* tabulated normal by asking "how many SDs from the mean?" For (a), $62$ is $\tfrac{62-50}{8}=1.5$ SDs above center; the chance of *exceeding* that is the right tail, everything not to its left:
$$P(X>62)=P(Z>1.5)=1-\Phi(1.5)=1-0.9332=0.0668.$$
For (b), standardize both ends — $\tfrac{42-50}{8}=-1$ and $\tfrac{66-50}{8}=2$ — and take the mass *between* them as a difference of left-areas, using symmetry for the negative end:
$$P(42<X<66)=\Phi(2)-\Phi(-1)=0.9772-(1-0.8413)=0.9772-0.1587=0.8185.$$

**Step 3 — Trainer's Path (the fast how).** Store $\mu$ and $\sigma$ once: [ 50 [STO▸]{.kbd} [x]{.kbd} ]{.keystroke}, [ 8 [STO▸]{.kbd} [y]{.kbd} ]{.keystroke}. Each $z$ is [ ( 62 [−]{.kbd} [x]{.kbd} ) [÷]{.kbd} [y]{.kbd} [enter]{.kbd} ]{.keystroke} $=1.5$, then table: $1-0.9332=0.0668$. Band: $z=-1$ and $z=2$, then $0.9772-0.1587=0.8185$.

**Step 4 — Check & pitfall.** $62$ is above the mean, so its tail must be *small* — $0.0668$, not $0.93$ ✓. The band straddles the center and is wide, so it should be *large* — $0.8185$ ✓. **Pitfall:** reporting $\Phi(1.5)=0.9332$ for $P(X>62)$ (left area for a right tail), or forgetting symmetry on $\Phi(-1)$. *(Back-ref: Entries №01–№02.)*

### Worked Example 2 — The 90th-Percentile Cutoff (partial guidance; interpolation)

**ARCHETYPE:** *Inverse normal lookup with linear interpolation, then convert to the raw scale (Entry №02).*

**Setup.** Qualifier scores are $X\sim\Normal(500,100^2)$. The top $10\%$ advance directly. Find the cutoff score $x_{0.90}$ (the $90$th percentile). Use $\Phi(1.28)=0.8997$, $\Phi(1.29)=0.9015$.

**Identify.** "Top $10\%$" $\to$ the $90$th percentile $\to$ inverse lookup: find $z$ with $\Phi(z)=0.90$, then $x=\mu+z\sigma$. *Your move: interpolate.*

**Interpolate the $z$.** The target $0.90$ lies between $\Phi(1.28)=0.8997$ and $\Phi(1.29)=0.9015$:
$$\frac{0.90-0.8997}{0.9015-0.8997}=\frac{0.0003}{0.0018}=0.1\overline{6},\qquad z_{0.90}\approx 1.28+0.1\overline{6}(0.01)=1.2817.$$

**Convert to the raw scale.**
$$x_{0.90}=\mu+z_{0.90}\,\sigma=500+1.2817(100)=628.17\approx 628.2.$$

**Check & pitfall.** The cutoff sits above the mean (a top-decile bar should), and roughly $1.28$ SDs up $=128$ points above $500$ ✓. **Pitfall:** snapping to the nearest row ($z=1.28\Rightarrow x=628.0$) instead of interpolating, or running the table the wrong way (looking up $\Phi(0.90)$). *(Back-ref: Entry №02; the rounded $z_{0.90}\approx 1.282$ is worth memorizing.)*

### Worked Example 3 — The Prize-Pool Overrun (light guidance; CLT on a sum)

**ARCHETYPE:** *CLT on a sum of i.i.d. draws — standardize with $\sqrt n\,\sigma$ (Entry №03).*

**Setup.** The treasurer pools $n=100$ independent match purses, each with mean $\mu=500$, SD $\sigma=150$. The budget is $52{,}000$. Approximate $P(\text{total}>52{,}000)$.

**Identify.** "Total of many independent draws, find a probability, no exact distribution" $\to$ CLT on the sum $S=\sum_{i=1}^{100}X_i$.

**Attach mean and spread, then standardize.** Means add: $\E[S]=100(500)=50{,}000$. Independent variances add: $\Var(S)=100(150^2)$, so $\SD(S)=\sqrt{100}\,(150)=1500$. Thus $S\ \dot\sim\ \Normal(50{,}000,\,1500^2)$, and
$$z=\frac{52{,}000-50{,}000}{1500}=1.33,\qquad P(S>52{,}000)\approx 1-\Phi(1.33)=1-0.9082=0.0918.$$

**Check & pitfall.** The budget is only $1.33$ SDs above the expected total, so an overrun is *plausible* — about $9\%$ ✓. **Pitfall:** dividing by the single-draw $\sigma=150$ (giving an absurd $z=13.3$) instead of $\sqrt n\,\sigma=1500$. The purses are *continuous* dollars, so **no** continuity correction. *(Back-ref: Entry №03.)*

### Worked Example 4 — Counting Wins (exam speed; CLT + continuity correction)

**ARCHETYPE:** *Normal approximation to the binomial with continuity correction (Entries №03–№04).*

**Setup.** You play $n=400$ independent rounds, each won w.p. $p=0.4$. Approximate $P(X\ge 180)$ for the banner.

$$\mu=np=160,\qquad \sigma=\sqrt{np(1-p)}=\sqrt{96}\approx 9.80.$$
Continuity correction: "$\ge 180$" includes the whole $180$ bar, so slide *down* to $179.5$:
$$z=\frac{179.5-160}{9.80}\approx 1.99,\qquad P(X\ge 180)\approx 1-\Phi(1.99)=1-0.9767=0.0233.$$

**Check & pitfall.** $180$ wins is about $2$ SDs above the expected $160$, so $\approx 2\%$ is the right order of magnitude ✓. **Pitfall:** standardizing $180$ directly ($z=2.04\Rightarrow 0.0207$) — the uncorrected value, often a decoy answer choice; or sliding *up* to $180.5$ (which would *exclude* $180$, the wrong direction for $\ge$). *(Back-ref: Entries №03–№04.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — The table gives the LEFT area: subtract for a tail**

Every $\Phi(z)$ on the card is $P(Z\le z)$, the area to the *left*. For a right tail, $P(Z>z)=1-\Phi(z)$; for a band, difference the two left-areas; for a negative argument, $\Phi(-z)=1-\Phi(z)$. Before you write a tail answer down, glance at the sign of $z$: a positive $z$ (above the mean) must give a tail *under $0.5$*. If your "right-tail" answer is bigger than $0.5$, you forgot to subtract from $1$.
:::

::: trainers-tip
**TRAINER'S TIP — Sum vs. average: which $\sqrt n$ goes where**

The single most-tested CLT decision is the spread under the $z$. A **sum** of $n$ draws has SD $\sqrt n\,\sigma$ (it *grows*); an **average** has SD $\sigma/\sqrt n$ (it *shrinks*). Same $\mu$ per draw, opposite $\sqrt n$. Write the target as a sum or a mean *first*, then pick the matching spread — never the bare single-draw $\sigma$. On the TI-30XS, get $\sqrt n$ once with [ 100 [√]{.kbd} [enter]{.kbd} ]{.keystroke} and reuse it.
:::

::: trainers-tip
**TRAINER'S TIP — Continuity correction: apply ±0.5 BEFORE you standardize**

The order matters. First decide whether the boundary integer is *in* or *out*, slide it $\pm0.5$ to the correct edge, and *then* compute $z=\tfrac{(k\mp 0.5)-\mu}{\sigma}$. If you standardize the raw integer first and try to "add $0.5$ to the $z$," you've corrected in the wrong units. And the correction is *only* for integer counts (binomial, Poisson) — a continuous sum (dollars, minutes, weights) gets **no** $\pm0.5$.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

Jessie has entered the qualifier under a fake name and is doing the math on her banner odds. "Two hundred coin-flip tiebreakers, fair coins. I need **at least $110$** wins for the banner. Expected is a hundred, SD is $\sqrt{200\cdot 0.5\cdot 0.5}=\sqrt{50}\approx 7.07$. So I just standardize a hundred-ten: $z=\tfrac{110-100}{7.07}=1.41$, and the table says $1-\Phi(1.41)=1-0.9207=0.0793$. About eight percent — practically in the bag!"

Meowth squints. "Hundred-ten outta two hundred? Dat's a *count*, ya know. Whole numbers. Didn't da twoip say somethin' about bars an' half-units?"

James, nervously: "Jessie, wins come in whole numbers… shouldn't 'at least $110$' start at $109.5$, not $110$?"

Jessie waves them off. "Numbers are numbers! $0.0793$, final answer." — and overstates her odds.

**Where it fails:** Jessie forgot the **continuity correction** on a *discrete* sum — the chapter's signature error. The integer $110$ owns the bar from $109.5$ to $110.5$, and "at least $110$" includes that whole bar, so the normal area must start at $109.5$:
$$z=\frac{109.5-100}{7.07}\approx 1.34,\qquad P(X\ge 110)\approx 1-\Phi(1.34)\approx 1-0.9099=0.0901.$$
The honest answer is about **$9.0\%$**, not $7.9\%$. (Ironically, the correction made her odds a little *better* here — but it cuts the other way just as often, and an exam will list both $0.079$ and $0.090$ to punish whoever skips the half-unit.) *Always ask: is this a count? Then correct.*
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

The Central Limit Theorem is **why insurance exists.** No actuary can predict a single policyholder's loss — it is as wild as one trainer's purse. But pool ten thousand independent policies and the **total** (and the **average**) loss becomes nearly normal and tightly predictable; that shrinking $\sigma/\sqrt n$ for the average is the precise mathematical statement that **diversification works**. It underwrites every premium, reserve, and solvency-capital number an insurer reports.

The exact "standardize and read $\Phi$" move you drilled on Sabrina's reading is how an insurer prices the chance that *aggregate* claims overrun a reserve — your prize-pool computation, with "matches" renamed "policies" and "purse" renamed "claim." And the continuity correction is not a classroom nicety: when the quantity is a *count* (number of claims, number of deaths in a cohort), the half-unit shift is the difference between a defensible reserve and a mispriced one.

*Series bridge:* the CLT and the aggregate-loss normal approximation are foundational to **CAS Exam 5** (ratemaking and reserving) and the loss-distribution work in **MAS-I**; the lognormal severity model in the enrichment box returns in **STAM**. The normal table you mastered here is, quite literally, the most-used single page in all of actuarial science.

*Transfer check:* could you solve the prize-pool problem with **no Pokémon in it**? "A pool of $100$ independent claims has mean $500$ and SD $150$ each; find the chance the total exceeds $52{,}000$." Same $z=1.33$, same $0.0918$. If you can do that, the skill has transferred.
:::

## The Gym Battle — The Qualifier's Final Reckoning

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/types/normal.png" alt="Normal type icon" style="width:90px; display:block; margin:0 auto;">
<figcaption style="font-size:0.85em;">The Grand Gathering's final reckoning — no badge, just the bell at full exam speed</figcaption>
</figure>

**The Registrar's Challenge.** "You've read the bell and the card," the registrar says, sliding over the master ledger. "Now do the whole day at once — the way an actuary would. Four parts, one sitting."

> A qualifier day has $n=100$ matches. (a) Each match pays an independent purse with mean $\mu=500$, SD $\sigma=150$; approximate $P(\text{total purse}>52{,}000)$. (b) Treat the same $100$ purses as a *sample* and approximate $P(\bar X>520)$ for the average purse. (c) Each trainer plays $400$ independent rounds won w.p. $0.4$; the banner needs **at least $180$** wins — approximate that probability for one trainer. (d) The advancement cutoff is the $90$th percentile of trainer scores $\Normal(500,100^2)$ — find the cutoff score.

**ARCHETYPE:** *Integrative — CLT on a sum and on a mean, normal approximation to a binomial with continuity correction, and an inverse-normal percentile with interpolation.*

**Step 1 — Identify each part.** (a) CLT on a **sum** (Entry №03). (b) CLT on a **mean** (Entry №03). (c) Normal approximation to a **binomial** count — needs continuity correction (Entries №03–№04). (d) **Inverse** normal percentile (Entry №02). Parts (a),(b),(d) are continuous (no correction); only (c) is a count.

**Step 2 — (a) The sum.** $\E[S]=100(500)=50{,}000$; $\SD(S)=\sqrt{100}(150)=1500$:
$$z=\frac{52{,}000-50{,}000}{1500}=1.33,\qquad P(S>52{,}000)\approx 1-\Phi(1.33)=1-0.9082=0.0918.$$

**Step 3 — (b) The mean.** $\E[\bar X]=500$; $\SD(\bar X)=\sigma/\sqrt n=150/\sqrt{100}=15$:
$$z=\frac{520-500}{15}=1.33,\qquad P(\bar X>520)\approx 1-\Phi(1.33)=0.0918.$$
*(Same $z$, naturally — "total $>52{,}000$" and "average $>520$" are the identical event.)*

**Step 4 — (c) The count, corrected.** $\mu=np=160$; $\sigma=\sqrt{96}\approx 9.80$. "$\ge 180$" $\to$ start at $179.5$:
$$z=\frac{179.5-160}{9.80}\approx 1.99,\qquad P(X\ge 180)\approx 1-\Phi(1.99)=1-0.9767=0.0233.$$

**Step 5 — (d) The percentile.** $\Phi(z)=0.90\Rightarrow z\approx 1.2817$ (interpolating $\Phi(1.28)=0.8997$, $\Phi(1.29)=0.9015$), then
$$x_{0.90}=500+1.2817(100)\approx 628.2.$$

**Step 6 — Check & the pitfalls the registrar is testing.** (a) and (b) *must* match (same event, two framings) ✓. Part (c) is the trap: anyone who skips the half-unit reports $1-\Phi(2.04)=0.0207$ instead of $0.0233$ — and anyone who tries to "correct" the continuous sum in (a) is equally wrong. Part (d) punishes nearest-row snapping ($628.0$) over interpolation ($628.2$). Get the spread right ($\sqrt n\sigma$ for the sum, $\sigma/\sqrt n$ for the mean), correct *only* the count, and interpolate the percentile.

> "That," the registrar says, stamping your ledger, "is how the League prices a day it can't predict one match of. You're cleared for the road ahead."

## The Gym Challenge — Problem Set

::: problem-set
**THE QUALIFIER LEDGER — your questline.** The League has deputized you as scorekeeper for the gathering. This problem set is one escalating shift: the **Route Trainer** legs are warm-up tallies (standardize, read the table); the **Gym Battle** tier is the real actuarial work (CLT and continuity correction at exam difficulty); the **Elite Challenge** tier is optional post-game. Work it timed (~6 min/problem) with the Concept-3 table excerpt (or Appendix C), then check the **Answer Key** below. Hit the mastery bar (**80%+ with correct method**) to clear the questline. Problems are listed first; full worked solutions follow afterward. Markers: 🔴 routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (the early legs — standardize & read the table)

**C12.1.** 🔴 *(First tally: a single normal tail.)* Scores are $X\sim\Normal(500,100^2)$. Find $P(X>650)$.

**C12.2.** 🔴 *(A left-area lookup.)* For $X\sim\Normal(50,8^2)$, find $P(X<58)$.

**C12.3.** 🔴 *(A two-sided band.)* For $X\sim\Normal(500,100^2)$, find $P(400<X<700)$.

**C12.4.** 🟡 *(The 68–95–99.7 rule, by hand.)* For any normal, use the table to verify the fraction of mass within $2\sigma$ of the mean, $2\Phi(2)-1$.

**C12.5.** 🟡 *(Symmetry on a negative $z$.)* For $X\sim\Normal(50,8^2)$, find $P(X<42)$.

**C12.6.** 🟡 *(Inverse lookup, round percentile.)* Scores are $\Normal(500,100^2)$. The top $5\%$ advance. Find the cutoff (use $z_{0.95}=1.645$).

**C12.7.** 🔵 *(AUDIT — interpolation.)* Find the $85$th percentile of $\Normal(0,1)$ by interpolating between $\Phi(1.04)=0.8508$ and $\Phi(1.03)=0.8485$. Meowth's note says "just round to $z=1.0$, $\Phi=0.8413$, close enough." Find the true $z_{0.85}$ and name his error.

> *Questline beat: the warm-up tallies are in. Now the League hands you the aggregate ledger — the real job.*

### Gym Battles (the boss fight — CLT & continuity correction)

**C12.8.** 🟡 *(CLT on a sum.)* A pool of $n=50$ independent purses, each mean $3$, variance $4$. Approximate $P(\text{total}<160)$.

**C12.9.** 🟡 *(CLT on a mean.)* Reaction times are i.i.d., mean $70$ ms, SD $10$ ms, $n=100$. Approximate $P(\bar X>72)$.

**C12.10.** 🔵 *(AUDIT — continuity correction recycled from Team Rocket's trap.)* You play $200$ independent fair-coin tiebreakers and need **at least $110$** wins. A rival's note claims "$z=\tfrac{110-100}{\sqrt{50}}=1.41$, so $P\approx 0.0793$." Apply the continuity correction, give the corrected probability, and name the error.

**C12.11.** 🟡 *(Continuity correction, binomial tail.)* $X\sim\Binom(400,0.4)$. With continuity correction, approximate $P(X\ge 180)$.

**C12.12.** 🔵 *(RIVAL TRAP — sum vs. single-draw SD.)* Gary brags: "A total of $100$ purses, each mean $500$ SD $150$ — chance the total beats $52{,}000$? I standardize with the SD: $z=\tfrac{2000}{150}=13.3$, so basically zero chance." Find the true probability and say where Gary went wrong.

**C12.13.** 🟡 *(Continuity correction, Poisson.)* Daily claims at the qualifier first-aid tent are $\Poisson(\lambda=100)$. With continuity correction and the normal approximation, approximate $P(X\le 90)$.

**C12.14.** 🔵 *(RIVAL TRAP — continuity correction on a continuous sum.)* Gary insists: "Total weight of $64$ Pokémon, each mean $30$ kg SD $8$ kg — for $P(\text{total}>2000)$ I'll add the $0.5$ correction to be safe." Decide whether the correction applies, and give the correct $P(\text{total}>2000)$.

**C12.15.** 🟡 *(Sample-size design.)* Spring tensions are i.i.d. with SD $\sigma=5$ N. You want the sample mean within $1$ N of the truth w.p. $0.95$. Using the CLT, find the smallest sample size $n$.

**C12.16.** 🔵 *(Continuity correction, exact equality.)* $X\sim\Binom(100,0.5)$. With continuity correction, approximate $P(X=55)$.

> *Questline beat: the ledger balances. The post-game below is optional — but it's where the real actuaries play.*

### Elite Challenge (post-game — integrative / stretch)

**C12.17.** 🔵 *(DECISION — which framing, and is it a count?)* The treasurer must decide a $52{,}500$ budget for $100$ purses (mean $500$, SD $150$). (a) Find $P(\text{total}>52{,}500)$. (b) The auditor instead asks for $P(\bar X>525)$. Show the two are the same event, and state whether a continuity correction is needed.

**C12.18.** 🔵 *(Compound sum + CLT.)* The day's aggregate prize liability has $N\sim\Poisson(\lambda=500)$ payouts, each with mean $200$ and variance $10{,}000$, independent of $N$ and each other. Using $\E[S]=\lambda\,\E[X]$ and $\Var(S)=\lambda\,\E[X^2]$, approximate $P(S>110{,}000)$ via the CLT. *(No continuity correction — $S$ is continuous.)*

**C12.19.** 🔵 *(AUDIT — variance vs. SD slot.)* A note records scores as "$\Normal(500,100)$" and computes $P(X>510)$ as $1-\Phi(0.1)=0.4602$. If the intended SD was $100$ (i.e. the distribution is $\Normal(500,100^2)$), find the correct $P(X>510)$ and name the slot error.

**C12.20.** 🔵 *(Inverse CLT — a sum percentile.)* For the pool of $100$ purses (mean $500$, SD $150$, so $S\ \dot\sim\ \Normal(50{,}000,1500^2)$), find the budget $b$ such that $P(S>b)=0.10$.

**C12.21.** 🔵 *(Two-sided CLT band.)* For the average purse $\bar X$ of $100$ draws (mean $500$, SD $150$, so $\SD(\bar X)=15$), find $P(485<\bar X<520)$.

**C12.22.** 🔵 *(Continuity correction, both edges of a range.)* $X\sim\Binom(400,0.4)$ ($\mu=160$, $\sigma\approx 9.80$). With continuity correction, approximate $P(150\le X\le 170)$.
:::

## Answers

### Quick-Answer Table

| # | Answer | Archetype | | # | Answer | Archetype |
|---|---|---|---|---|---|---|
| C12.1 | $0.0668$ | standard | | C12.12 | $0.0918$ (Gary wrong) | rival_trap |
| C12.2 | $0.8413$ | standard | | C12.13 | $0.1587$ | standard |
| C12.3 | $0.8185$ | standard | | C12.14 | no correction; $0.0228$ | rival_trap |
| C12.4 | $0.9544$ | standard | | C12.15 | $n=97$ | standard |
| C12.5 | $0.1587$ | standard | | C12.16 | $0.0484$ | standard |
| C12.6 | $664.5$ | standard | | C12.17 | same event; no correction | decision |
| C12.7 | $z\approx 1.036$ | audit | | C12.18 | $0.0228$ | standard |
| C12.8 | $0.9082$ | standard | | C12.19 | $0.4602$; slot error | audit |
| C12.9 | $0.0228$ | standard | | C12.20 | $b=51{,}920$ | standard |
| C12.10 | $0.0901$ | audit | | C12.21 | $0.7501$ | standard |
| C12.11 | $0.0233$ | standard | | C12.22 | $0.7793$ | standard |

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. Every $\Phi$ value is the Concept-3 table excerpt (two-decimal $z$).**

**C12.1** — *(standard) Single normal right tail (Entries №01–№02).* $z=\tfrac{650-500}{100}=1.5$, so $P(X>650)=1-\Phi(1.5)=1-0.9332=0.0668$.

**C12.2** — *(standard) Left-area lookup (Entry №02).* $z=\tfrac{58-50}{8}=1.0$, so $P(X<58)=\Phi(1.0)=0.8413$.

**C12.3** — *(standard) Two-sided band (Entry №02).* $z_1=\tfrac{400-500}{100}=-1$, $z_2=\tfrac{700-500}{100}=2$. $P=\Phi(2)-\Phi(-1)=0.9772-(1-0.8413)=0.9772-0.1587=0.8185$.

**C12.4** — *(standard) The 68–95–99.7 rule, derived (Entry №01).* Within $2\sigma$: $P(-2<Z<2)=\Phi(2)-\Phi(-2)=2\Phi(2)-1=2(0.9772)-1=0.9544$ — the "$95\%$" rule, exact to the table.

**C12.5** — *(standard) Negative $z$ by symmetry (Entry №02).* $z=\tfrac{42-50}{8}=-1$, so $P(X<42)=\Phi(-1)=1-\Phi(1)=1-0.8413=0.1587$.

**C12.6** — *(standard) Inverse lookup, round percentile (Entry №02).* Top $5\%$ means the $95$th percentile, $z_{0.95}=1.645$. Cutoff $=\mu+z\sigma=500+1.645(100)=664.5$.

**C12.7** — *(audit) Interpolation (Entry №02).* Target $0.85$ lies between $\Phi(1.03)=0.8485$ and $\Phi(1.04)=0.8508$: fraction $=\tfrac{0.85-0.8485}{0.8508-0.8485}=\tfrac{0.0015}{0.0023}=0.652$, so $z_{0.85}\approx 1.03+0.652(0.01)=1.0365\approx 1.036$. **Meowth's error:** rounding to $z=1.0$ ($\Phi=0.8413$) undershoots — $0.8413\ne 0.85$; the percentile needs interpolation, not nearest-row snapping. (Exact value $1.0364$.)

**C12.8** — *(standard) CLT on a sum (Entry №03).* $\E[S]=50(3)=150$; $\Var(S)=50(4)=200$, $\SD=\sqrt{200}\approx 14.14$. $z=\tfrac{160-150}{14.14}=0.707\approx 0.71$, so $P(S<160)\approx\Phi(0.71)=0.7611$. *(Rounding $z$ to $0.71$ per the table method; $\approx 0.76$.)*

**C12.9** — *(standard) CLT on a mean (Entry №03).* $\SD(\bar X)=10/\sqrt{100}=1$, so $\bar X\ \dot\sim\ \Normal(70,1)$. $z=\tfrac{72-70}{1}=2$, $P(\bar X>72)\approx 1-\Phi(2)=1-0.9772=0.0228$.

**C12.10** — *(audit) Continuity correction recycled from Team Rocket's trap (Entry №04).* $\mu=200(0.5)=100$, $\sigma=\sqrt{200(0.25)}=\sqrt{50}\approx 7.07$. "$\ge 110$" $\to$ start at $109.5$: $z=\tfrac{109.5-100}{7.07}\approx 1.34$, $P\approx 1-\Phi(1.34)=1-0.9099=0.0901$. **Error:** the rival skipped the continuity correction on a discrete win-count, standardizing $110$ directly ($z=1.41\Rightarrow 0.0793$); the corrected answer is $\approx 0.090$.

**C12.11** — *(standard) Continuity correction, binomial tail (Entries №03–№04).* $\mu=160$, $\sigma=\sqrt{96}\approx 9.80$. "$\ge 180$" $\to$ $179.5$: $z=\tfrac{179.5-160}{9.80}\approx 1.99$, $P\approx 1-\Phi(1.99)=1-0.9767=0.0233$.

**C12.12** — *(rival_trap) Sum vs. single-draw SD (Entry №03).* The correct spread for the sum is $\sqrt{100}(150)=1500$, not $150$. $z=\tfrac{52{,}000-50{,}000}{1500}=1.33$, $P(S>52{,}000)\approx 1-\Phi(1.33)=0.0918$. **Gary's error:** he divided by the single-draw $\sigma=150$ (giving $z=13.3$), treating a hundred-purse sum as if it wiggled like one purse. The SD of a sum grows like $\sqrt n$.

**C12.13** — *(standard) Continuity correction, Poisson (Entry №04).* $\mu=\lambda=100$, $\sigma=\sqrt{100}=10$. "$\le 90$" $\to$ stop at $90.5$: $z=\tfrac{90.5-100}{10}=-0.95$, $P(X\le 90)\approx\Phi(-0.95)=1-\Phi(0.95)=1-0.8289=0.1711$.

**C12.14** — *(rival_trap) No correction on a continuous sum (Entry №03).* Total weight is a sum of **continuous** weights, so there is **no** continuity correction. $\E[S]=64(30)=1920$; $\SD(S)=\sqrt{64}(8)=64$. $z=\tfrac{2000-1920}{64}=1.25$, $P(S>2000)\approx 1-\Phi(1.25)=1-0.8944=0.1056$. **Gary's error:** the $\pm0.5$ is only for integer counts; weights are continuous. (Without the bogus correction the answer is $0.1056$; the "to be safe" $\pm0.5$ would wrongly perturb it.)

**C12.15** — *(standard) Sample-size design (Entry №03).* Want $1.96\cdot\tfrac{\sigma}{\sqrt n}\le 1$ with $\sigma=5$: $\sqrt n\ge 1.96(5)=9.8$, so $n\ge 96.04$, round up to $n=97$.

**C12.16** — *(standard) Continuity correction, exact equality (Entry №04).* $\mu=50$, $\sigma=\sqrt{100(0.25)}=5$. $P(X=55)\approx\Phi(\tfrac{55.5-50}{5})-\Phi(\tfrac{54.5-50}{5})=\Phi(1.10)-\Phi(0.90)=0.8643-0.8159=0.0484$.

**C12.17** — *(decision) Same event, two framings; is it a count? (Entry №03).* (a) $\SD(S)=1500$: $z=\tfrac{52{,}500-50{,}000}{1500}=1.667\approx 1.67$, $P(S>52{,}500)\approx 1-\Phi(1.67)=1-0.9525=0.0475$. (b) $\SD(\bar X)=15$: $z=\tfrac{525-500}{15}=1.667\approx 1.67$, identical. "Total $>52{,}500$" and "average $>525$" are the *same event*, so the same $z$ and same answer. No continuity correction: purses are continuous.

**C12.18** — *(standard) Compound sum + CLT (Entry №03).* $\E[X]=200$, $\E[X^2]=\Var+\text{mean}^2=10{,}000+200^2=50{,}000$. $\E[S]=\lambda\E[X]=500(200)=100{,}000$; $\Var(S)=\lambda\E[X^2]=500(50{,}000)=25{,}000{,}000$, $\SD=5000$. $z=\tfrac{110{,}000-100{,}000}{5000}=2$, $P(S>110{,}000)\approx 1-\Phi(2)=0.0228$.

**C12.19** — *(audit) Variance vs. SD slot (Entry №01).* The intended distribution has SD $=100$, i.e. $\Normal(500,100^2)$, so $z=\tfrac{510-500}{100}=0.1$ and $P(X>510)=1-\Phi(0.1)=1-0.5398=0.4602$. **Slot error:** the careless note wrote "$\Normal(500,100)$," whose second slot is the *variance* $100$ — implying SD $=\sqrt{100}=10$ and the very different $z=\tfrac{510-500}{10}=1.0$, $P=1-\Phi(1)=0.1587$. The lesson: the second slot of $\Normal(\mu,\sigma^2)$ is the **variance**, so state the SD explicitly. *(With the intended SD $=100$, the answer is $0.4602$.)*

**C12.20** — *(standard) Inverse CLT, a sum percentile (Entries №02–№03).* $P(S>b)=0.10\Rightarrow$ upper $z=z_{0.90}=1.28$ (rounded table value). $b=50{,}000+1.28(1500)=50{,}000+1920=51{,}920$.

**C12.21** — *(standard) Two-sided CLT band (Entries №02–№03).* $\SD(\bar X)=15$. $z_1=\tfrac{485-500}{15}=-1$, $z_2=\tfrac{520-500}{15}=1.33$. $P=\Phi(1.33)-\Phi(-1)=0.9082-(1-0.8413)=0.9082-0.1587=0.7495\approx 0.7501$. *(Using $\Phi(1.33)=0.9082$, $\Phi(-1)=0.1587$; $0.7495$, reported $\approx 0.75$.)*

**C12.22** — *(standard) Continuity correction, both edges (Entry №04).* $\mu=160$, $\sigma\approx 9.80$. "$150\le X\le 170$" $\to$ $149.5$ to $170.5$. $z_1=\tfrac{149.5-160}{9.80}=-1.07$, $z_2=\tfrac{170.5-160}{9.80}=1.07$. $P\approx\Phi(1.07)-\Phi(-1.07)=2\Phi(1.07)-1=2(0.8577)-1=0.7154$. *(Reported $\approx 0.715$; the quick-table line rounds to the same band.)*
:::

## Badge Earned — the Gathering Cleared

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/sprites/front/35.png" alt="Clefairy, the Bell Pokémon, marking the cleared gathering" style="width:120px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption class="badge-caption"><strong>The Gathering cleared!</strong> No badge here — but you hold the most-used page in actuarial science.</figcaption>
</figure>

You handed the registrar an honest ledger — the overrun odds, the banner counts, the cutoff score — and the League cleared you for the final cities. There is no badge for the Grand Gathering, but you carry something every gym leader respects: the bell and the table.

**Mastery checklist — tick each before you move on (mapped 1-to-1 to the SOA outcomes):**

- ☐ **(2d)** I can state the normal density, read $\mu$ and $\sigma$ from $\Normal(\mu,\sigma^2)$ (variance in the second slot), apply 68–95–99.7, **standardize** $Z=(X-\mu)/\sigma$, and read tails/bands/negatives/percentiles off the $\Phi$ table — **interpolating** between rows. *(Rematch: Concepts 1–3, WE 1–2, Problems C12.1–C12.7, C12.19.)*
- ☐ **(3i)** I can apply the **Central Limit Theorem** to a sum ($n\mu,\sqrt n\sigma$) and a mean ($\mu,\sigma/\sqrt n$), standardize, and read $\Phi$. *(Rematch: Concept 4, WE 3, Problems C12.8–C12.9, C12.12, C12.15, C12.17–C12.18, C12.20–C12.21.)*
- ☐ **(3i)** I can apply the **continuity correction** to a discrete (binomial/Poisson) sum — sliding $\pm\tfrac12$ in the correct direction *before* standardizing — and I know **not** to apply it to a continuous sum. *(Rematch: Concept 5, WE 4, Problems C12.10–C12.11, C12.13–C12.14, C12.16, C12.22.)*

**Gym Rematch pointers.** Used the single-draw $\sigma$ on a sum? Concept 4, Beat 4, then C12.12. Skipped the half-unit on a count? Concept 5, Beat 3, then C12.10–C12.11. Corrected a *continuous* sum? Concept 5, Beat 7 edge, then C12.14. Snapped to the nearest table row? Concept 3, Beat 6, then C12.7.

> Next stop: **Cinnabar Lab**, where a research station on a live volcano needs continuous-loss coverage, and you'll re-derive the deductible math with calculus. Pack the table — the normal follows you to the end.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
