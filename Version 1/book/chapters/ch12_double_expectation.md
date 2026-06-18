<!--
  file: ch12_double_expectation
  tier: A
  outcomes: 3c,3d
  draft1_source: drafts/chapters_draft1/ch10_viridian_gym.md
  maps_to: Viridian Gym, Giovanni — the hidden-layer proving ground
-->

# Expectation Within Expectation {.type-ground}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with Viridian City highlighted; seven badges already earned, the route now looping back to the gym that was skipped at the very start." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 10 — seven badges in hand, you double back to Viridian City, the one gym you skipped on the way out of Pallet. Behind its doors waits Giovanni, and the last idea that stands between you and the Plateau: averaging over a layer you cannot see.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Boss Behind the Badge"**

You come back to Viridian City for the eighth badge — the one gym you walked past on the way out of Pallet Town, all those routes ago. The doors slide open onto a hall of polished black stone, and the leader is waiting in the dark at the far end. He does not introduce himself. He does not need to. Meowth, perched on a railing above, freezes mid-grin. Pikachu's ears flatten. You already know.

"Giovanni," you say. The Viridian Gym Leader — and, you now understand, the head of Team Rocket.

He gestures, and a grunt steps forward with a Pokémon — but you cannot tell *which* Pokémon, because the lights stay low and concealment is his whole strategy. "My grunts draw from three squads," he says. "A *random* squad reports to each round. You will not know which until the attack lands. One squad fields weak Pokémon; one, average; one, my elites. The squad is chosen by a roll you never see."

He lets that settle. "So tell me, challenger. Before the first ball is thrown — what is the *expected* strength of the Pokémon I send out? And how *uncertain* should you be about it? Some of your fear comes from not knowing which squad shows up. Some comes from the squad itself being unpredictable. Separate those two, and you will know exactly how afraid to be."

Pikachu looks up at you. The strength depends on a tier you can't observe — a **hidden layer**. You can't just average the Pokémon. You'd have to average *over the squad first*, then average *over which squad it was*. And the total dread has to split into "fear from Giovanni's hidden dice" and "fear from the Pokémon's own randomness."

You've computed expectations before. You've never computed an expectation *inside* another expectation, where the inner answer is itself a random thing — changing depending on a roll you'll never see.

*How do you find the strength of an opponent whose very identity is left to chance?*
:::

## Where You Are — 60-Second Retrieval

In Cinnabar, last chapter, you learned to read a **joint distribution** of two random variables $X$ and $Y$ at once, and — the load-bearing idea — to **slice** it. Given a value $Y = y$, you cropped the joint down to a single row or column and renormalized it into a **conditional distribution**,

$$f_{X\mid Y}(x \mid y) = \frac{f_{X,Y}(x,y)}{f_Y(y)},$$

read aloud *"the density of $X$ given that $Y$ equals $y$."* That slice is an honest, complete probability distribution in its own right — it has its own shape, its own center, its own spread.

That is exactly the foundation this chapter stands on. Everything in Viridian is built on one move: **take the mean (or the variance) of that conditional slice, and then watch what happens when you let $y$ vary.** Take sixty seconds and prove you still own the slice before reading on.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the last chapter**

Answer from memory; if any feels shaky, flip back before continuing.

1. A joint table gives $P(X{=}2, Y{=}1) = 0.12$ and the column total $P(Y{=}1) = 0.30$. What is $P(X{=}2 \mid Y{=}1)$? *(Answer: $0.12/0.30 = 0.4$.)*
2. In words, what does conditioning on $Y = y$ do to a joint distribution? *(Answer: it crops to the $Y=y$ slice and renormalizes it to sum/integrate to one.)*
3. The mean of a discrete distribution is $\sum_x x\,p(x)$. What is the mean of the slice $p(x) = \{x{=}10:0.5,\ x{=}20:0.5\}$? *(Answer: $10(0.5)+20(0.5)=15$.)*

All three instant? You're ready. Any hesitation? The retrieval *is* the lesson — go reclaim the conditional slice, then come back. Conditional **expectation** is nothing more than question 3 applied to the slice from question 1.
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice crackles through the Pokédex's Actuary Mode, low so Giovanni won't hear. "This is the last gym, Ash. The math here is the *layered* kind — and it is the bridge to everything actuaries do with mixed risk. Condition first, then average over the condition. Do it for the mean, do it for the variance, and you can price a risk whose true level is hidden, or a year of claims whose very *count* is unknown. Take it slowly; what you build here you will use until the day you pass."

By the end of this chapter you will be able to:

- **Compute** a conditional expectation $\E[X \mid Y]$ and conditional variance $\Var(X \mid Y)$, and recognize each as a **function of $Y$** — hence itself a random variable, not a fixed number. *(Outcome 3c.)*
- **Apply** the **Law of Total Expectation** (double expectation), $\E[X] = \E\!\big[\E[X \mid Y]\big]$, to recover an unconditional mean by averaging over a hidden layer. *(Outcome 3c.)*
- **Apply** the **Law of Total Variance**, $\Var(X) = \E\!\big[\Var(X \mid Y)\big] + \Var\!\big(\E[X \mid Y]\big)$, splitting total uncertainty into a *within-group* (process) piece and a *between-group* (parameter) piece. *(Outcome 3d.)*
- **Model** a **compound** random variable $S = \sum_{i=1}^{N} X_i$ — a random *count* of random *sizes* — by conditioning on $N$, and find its mean and variance. *(Outcomes 3c, 3d.)*

> *Exam-weight signpost.* Double expectation and total variance are **frequently tested** in Exam P's Multivariate section, and compound models are a perennial favorite. This is a **Tier A** chapter: it earns the full treatment, and it is the direct on-ramp to credibility theory on later actuarial exams.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own All of Viridian?**

Already fluent? Prove it. Work these four with *correct method*, ~3 minutes each:

1. $\E[X \mid Y{=}1]=40$, $\E[X \mid Y{=}2]=70$, $\E[X \mid Y{=}3]=120$, with $P(Y) = 0.5, 0.3, 0.2$. Find $\E[X]$.
2. For that same $X$, the conditional variances are $25, 64, 400$. Find $\Var(X)$.
3. $X \mid \Lambda \sim \Expo(\text{mean}{=}\Lambda)$ with $\Lambda \sim \Unif(10,20)$. Find $\E[X]$ and $\Var(X)$.
4. $N \sim \Poisson(3)$, severities i.i.d. with $\mu=50$, $\sigma^2=900$. Find $\E[S]$ and $\Var(S)$ for $S=\sum_1^N X_i$.

*(Answers: $65$; $1036.7$; $15$ and $241.\overline{6}$; $150$ and $10{,}200$.)* Four for four with the right reasoning? **Skip to the Gym Challenge** and claim the badge. Any miss or hesitation? The teaching below was built exactly for you — and each concept has its own skip-gate, so even a partial owner loses no time.
:::

---

Four ideas build on one another here, in increasing difficulty. We teach them **in order**, each with its own skip-check, then the full nine-beat lesson, then a Pokédex Entry you can carry into the exam:

1. **Conditional expectation** — the mean of a slice, which becomes random when the slice is random *(the floor everything stands on)*
2. **The Law of Total Expectation** — peel one layer, average over it
3. **Conditional variance & the Law of Total Variance** — splitting fear into two sources
4. **Compound random variables** — a random number of random sizes *(the actuary's workhorse)*

## Concept 1 — Conditional Expectation: The Mean of a Slice That Can Move

::: concept-gate
**DO YOU ALREADY OWN THIS? — Conditional Expectation**

Giovanni's squad $Y$ takes the value $1$, $2$, or $3$. The expected Pokémon strength *inside* each squad is $\E[X\mid Y{=}1]=40$, $\E[X\mid Y{=}2]=70$, $\E[X\mid Y{=}3]=120$. Someone asks: "What is $\E[X \mid Y]$?"

If you can say **"that's not a single number — it's a rule that outputs $40$, $70$, or $120$ depending on which squad $Y$ turns out to be, so $\E[X\mid Y]$ is itself a random variable,"** you own this idea — **skip to Concept 2**. If you wanted to answer with one number, this section is for you.
:::

**Beat 1 — The one-sentence idea.** *Once you are told $Y = y$, average $X$ the ordinary way inside that one slice; the answer is a number — but because the slice depends on $y$, that number changes as $y$ changes, so the "answer" is itself a random variable.*

**Beat 2 — Anchor + concrete instance.** This is precisely the conditional slice from Cinnabar, now with its mean taken. Recall: conditioning on $Y=y$ crops the joint down to one slice $f_{X\mid Y}(x\mid y)$, a complete distribution. Take *its* mean and you have a conditional expectation.

Here is Giovanni's setup, with real numbers. The squad $Y$ is drawn with $P(Y{=}1)=0.5$, $P(Y{=}2)=0.3$, $P(Y{=}3)=0.2$. Within each squad, the Pokémon's battle strength $X$ has a known average:

$$\E[X \mid Y{=}1]=40, \qquad \E[X \mid Y{=}2]=70, \qquad \E[X \mid Y{=}3]=120.$$

*If you knew the squad, what strength would you expect?*

**Beat 3 — Reason through it in plain words.** If Giovanni's grunt reports *"squad 1,"* your world collapses to squad 1 and the expected strength is just $40$. If it's squad 2, it's $70$. If squad 3, it's $120$. Each is an honest, ordinary average — you computed the mean *inside* a single slice, exactly question 3 from the retrieval. There is nothing new in the arithmetic.

What *is* new is this: **the answer you get depends on the roll you never saw.** Before the squad is revealed, "the expected strength given the squad" is not yet pinned to one value. It is $40$ with probability $0.5$, $70$ with probability $0.3$, and $120$ with probability $0.2$. That is the definition of a random variable — a quantity that takes different numeric values with different probabilities.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The natural mistake is to treat $\E[X\mid Y]$ as one fixed number by plugging the *average squad* into the strength rule. The average squad index is $0.5(1)+0.3(2)+0.2(3)=1.7$, so it is tempting to report something like "the strength of squad $1.7$," roughly $\tfrac{40+70}{2}\approx 55$.

$$\E[X\mid Y] \overset{?}{=} \E\big[X \mid Y = \E[Y]\big] \approx 55. \qquad\textbf{(wrong)}$$

This is nonsense for two reasons. First, *there is no squad $1.7$* — Giovanni fields whole squads, not blends. Second, and deeper: $\E[X\mid Y]$ is a **function of the random $Y$**, and you may not collapse a random input to its average before the function runs, because the function isn't linear in the squad index. Plugging in $\E[Y]$ throws away the very randomness the symbol is built to carry. (This exact error has a name — Jensen's trap — and Team Rocket will walk straight into it later.) Keep the picture: **$\E[X\mid Y]$ is a slot machine, not a single coin.**

**Beat 5 — Translate into notation, one glyph at a time.** Start with a *fixed* told value. We write

$$\E[X \mid Y = y] \qquad \text{read aloud: ``the expected value of } X \text{ given that } Y \text{ equals } y\text{.''}$$

Everything to the right of the bar $\mid$ ("given that," exactly as in Bayes) is the slice you have cropped into. By the ordinary definition of a mean, applied to the conditional slice,

$$\E[X \mid Y = y] = \sum_x x\, p_{X\mid Y}(x \mid y) \quad\text{(discrete)}, \qquad \E[X \mid Y = y] = \int_{-\infty}^{\infty} x\, f_{X\mid Y}(x \mid y)\, dx \quad\text{(continuous)}.$$

For each fixed $y$ this is just a number. Now name that number as a function of $y$:

$$g(y) = \E[X \mid Y = y].$$

In Giovanni's case $g(1)=40$, $g(2)=70$, $g(3)=120$. Finally — the one genuinely new glyph — drop the "$= y$" and feed the *random* $Y$ into $g$:

$$\E[X \mid Y] = g(Y) \qquad \text{read aloud: ``the expected value of } X \text{ given } Y\text{''} \;\;(\text{a random variable}).$$

Lowercase $y$ means "a specific told value, answer is a number." Capital $Y$ means "the value is still random, answer is a random variable." That single capitalization carries the whole idea.

**Beat 6 — Generalize: derive the distribution of $g(Y)$ from the instance.** We did not assert that $\E[X\mid Y]$ is random — we *built* it. The function $g$ assigns a number to each possible $y$; since $Y$ is random, $g(Y)$ inherits $Y$'s randomness. Its distribution is read straight off the table:

$$g(Y) = \E[X\mid Y] = \begin{cases} 40 & \text{w.p. } 0.5 \\ 70 & \text{w.p. } 0.3 \\ 120 & \text{w.p. } 0.2 \end{cases}$$

That is an ordinary discrete random variable. We can take *its* mean and *its* variance like any other — which is precisely what the next two concepts do.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the table above — read $g(y)$ off the three given conditional means.
- *Twist (a formula, not a table):* sometimes $g$ is given as an expression. If a trainer's prize satisfies $\E[X \mid Y] = 100\,Y$, then $g(y)=100y$ and $\E[X\mid Y]=100Y$ is random whenever $Y$ is. You don't need a table — you carry the function.
- *Continuous inner slice:* if $X \mid \Lambda \sim \Expo(\text{mean}{=}\Lambda)$, then the *known mean of an exponential* gives $g(\lambda) = \E[X\mid\Lambda{=}\lambda] = \lambda$, so $\E[X\mid\Lambda]=\Lambda$ — the conditional mean literally *is* the random parameter.
- *Edge:* if $X$ doesn't depend on $Y$ at all (independence), then $g(y)=\E[X]$ for every $y$ — a constant. A constant is the degenerate random variable; conditioning told you nothing.

**Beat 8 — Picture it.** The figure makes "a mean that moves" literal: three slices, three centers, and one slot machine that lands on one center per spin.

<figure>
<img src="../../assets/diagrams/ch12_conditional_slices.png" alt="Three stacked conditional distributions of X, one per squad. The Y=1 slice is a narrow bump centered at 40; the Y=2 slice a bump centered at 70; the Y=3 slice a wider bump centered at 120. A vertical tick marks each center. To the right, a single axis labeled E[X|Y] shows three dots at 40, 70, 120 tagged with probabilities 0.5, 0.3, 0.2, depicting the conditional mean as its own random variable." style="width:82%; max-width:600px; display:block; margin:1em auto;">
<figcaption>Conditioning on $Y=y$ selects one slice; its center is $g(y)=\E[X\mid Y{=}y]$. Because $Y$ is random, the center $\E[X\mid Y]$ is itself a random variable taking $40, 70, 120$ with probabilities $0.5, 0.3, 0.2$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now take any conditioning value $Y=y$, average $X$ inside that slice to get the number $g(y)$, and — crucially — recognize that letting $y$ vary turns $g(Y) = \E[X\mid Y]$ into a *random variable* with its own distribution. That single shift is the seed of both laws ahead.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Conditional Expectation $\E[X \mid Y]$**

For a fixed value $Y=y$:
$$\E[X \mid Y = y] = \sum_x x\, p_{X\mid Y}(x \mid y) \quad\text{or}\quad \int_{-\infty}^{\infty} x\, f_{X\mid Y}(x \mid y)\, dx.$$
Writing $g(y) = \E[X\mid Y{=}y]$, the quantity $\E[X\mid Y] = g(Y)$ is a **function of $Y$** — hence a **random variable**.

*In plain terms:* once you're told $Y$, average $X$ the usual way inside that slice. The answer changes as the told value changes, so until $Y$ is revealed the answer is itself random.

*Recognition cue:* "given that," "if it turns out that," or a *parameter that is itself drawn at random* ("the squad / rate / region is selected, then…"). The instant a conditioning variable is described as random, write $\E[X\mid Y]$ as a function of $Y$ — never collapse $Y$ to its average first.
:::

## Concept 2 — The Law of Total Expectation: Peel One Layer, Average Over It

::: concept-gate
**DO YOU ALREADY OWN THIS? — Total Expectation**

Using Giovanni's $\E[X\mid Y{=}y] = 40, 70, 120$ for squads with $P(Y) = 0.5, 0.3, 0.2$: before any squad is revealed, what is the overall expected strength $\E[X]$?

If you answered **$65$** via $40(0.5)+70(0.3)+120(0.2)$ — and you know *why you weight by the squad probabilities and don't just average $40, 70, 120$* — **skip to Concept 3**. If you reached for the plain average $\tfrac{40+70+120}{3}\approx 76.7$, read on.
:::

**Beat 1 — The one-sentence idea.** *To get the overall average of $X$, first average $X$ inside each layer $Y=y$, then average those answers — weighting each by how likely its layer is.*

**Beat 2 — Anchor + concrete instance.** Concept 1 gave you the random variable $\E[X\mid Y]$, taking $40, 70, 120$ with probabilities $0.5, 0.3, 0.2$. This concept does the most natural thing in the world: it takes the **mean of that random variable**. Averaging a thing that takes $40, 70, 120$ with those weights is exactly the law of total probability's weighted-average move (Cerulean), now applied to expectations.

Giovanni's question, formally: the squad $Y$ has $P(Y{=}1)=0.5$, $P(Y{=}2)=0.3$, $P(Y{=}3)=0.2$, with conditional means $40, 70, 120$. *Before the first ball is thrown, what strength should you expect?*

**Beat 3 — Reason through it in plain words.** The Pokémon's strength is large along three different roads:

- Squad 1 shows up (chance $0.5$) and its average strength is $40$: contributes $0.5 \times 40 = 20$.
- Squad 2 shows up (chance $0.3$), average $70$: contributes $0.3 \times 70 = 21$.
- Squad 3 shows up (chance $0.2$), average $120$: contributes $0.2 \times 120 = 24$.

Add the three contributions:

$$\E[X] = 20 + 21 + 24 = 65.$$

Each term is "how likely this layer is" times "the average inside it" — a **weighted average of the conditional means**.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The tempting shortcut is the **plain average** of the three conditional means:

$$\frac{40 + 70 + 120}{3} = 76.7. \qquad\textbf{(wrong — ignores the weights)}$$

That would be right only if all three squads were equally likely. They aren't — squad 1 reports half the time, squad 3 only a fifth. The weak squad's low strength of $40$ should count *more* than the elites' $120$, because it appears more often. The plain average secretly assumes a uniform squad distribution and throws away the actual weights, inflating the answer from $65$ to $76.7$.

**Beat 5 — Translate into notation, one glyph at a time.** From Concept 1, $\E[X\mid Y]$ is a random variable. "Average that random variable" is just an expectation *of* it — an expectation of an expectation:

$$\E\big[\,\E[X\mid Y]\,\big] \qquad \text{read aloud: ``the expected value of the conditional expectation.''}$$

Read it inside-out: the **inner** $\E[X\mid Y]$ produces the random center; the **outer** $\E[\cdot]$ averages those centers over $Y$. Spelled out as a sum over the discrete outer layer (the most common exam form):

$$\E\big[\,\E[X\mid Y]\,\big] = \sum_y \E[X\mid Y{=}y]\, P(Y=y) = (40)(0.5)+(70)(0.3)+(120)(0.2) = 65.$$

**Beat 6 — Generalize: derive the formula.** We don't assert the law — we *build* it from the law of total probability you already own. Take the definition of $\E[X]$ and split each outcome by which layer $Y=y$ it fell in (the layers are disjoint and exhaustive, exactly a partition):

$$\E[X] = \sum_x x\,P(X{=}x) = \sum_x x \sum_y P(X{=}x, Y{=}y) = \sum_y \underbrace{\Big(\sum_x x\,P(X{=}x\mid Y{=}y)\Big)}_{\E[X\mid Y=y]} P(Y{=}y) = \sum_y \E[X\mid Y{=}y]\,P(Y{=}y).$$

The middle step swaps the order of summation and pulls out $P(Y{=}y)$ via $P(X{=}x,Y{=}y) = P(X{=}x\mid Y{=}y)\,P(Y{=}y)$ — the multiplication rule. The bracketed inner sum *is* $\E[X\mid Y{=}y]$. Compressing the outer sum back into an expectation gives the boxed law:

$$\boxed{\;\E[X] = \E\!\big[\,\E[X \mid Y]\,\big]\;}$$

It is the law of total probability with $x$-weights — nothing more exotic.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the three-squad sum, $65$.
- *Continuous outer layer:* if $\E[X\mid\Lambda]=\Lambda$ and $\Lambda \sim \Unif(10,20)$, then $\E[X] = \E[\Lambda] = 15$ — the outer "sum" becomes an integral, handled by knowing $\E[\Lambda]$.
- *Function form:* if $\E[X\mid Y] = 100Y$ and $Y\sim\Poisson(2)$, then $\E[X]=\E[100Y]=100\,\E[Y]=200$ — push the expectation through the linear function.
- *Sanity boundary:* a weighted average must land **between** the smallest and largest conditional mean. Our $65$ sits between $40$ and $120$. If a "total expectation" ever falls outside that range, you slipped.

**Beat 8 — Picture it.** Total expectation is a one-stage tree: each leaf is layer-weight $\times$ in-layer mean; sum the leaves.

<figure>
<img src="../../assets/diagrams/ch12_total_expectation_tree.png" alt="A one-stage fan diagram. A root node branches to three leaves: Squad 1 (0.5), Squad 2 (0.3), Squad 3 (0.2). Each leaf carries its conditional mean (40, 70, 120) and the product on its branch: 20, 21, 24. The three products are summed at the bottom to 65." style="width:78%; max-width:560px; display:block; margin:1em auto;">
<figcaption>Total expectation as a one-stage tree: each leaf is $P(Y{=}y)\times\E[X\mid Y{=}y]$; the leaves sum to $\E[X]=65$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now recover an unconditional mean from a hidden layer: compute the conditional means, weight each by its layer probability, and add. You "peeled one layer." This is half of what Giovanni asked — the *expected* strength. The other half, how *uncertain* you should be, needs variance, which is next.

::: pokedex-entry
**POKÉDEX ENTRY №02 — Law of Total Expectation (Double Expectation)**

$$\E[X] = \E\!\big[\,\E[X \mid Y]\,\big].$$
Discrete outer layer (the common exam form):
$$\E[X] = \sum_y \E[X\mid Y{=}y]\, P(Y=y).$$

*In plain terms:* average $X$ inside each layer, then average those answers, weighting each layer by how likely it is. A weighted average of conditional means — so the result always lands **between** the smallest and largest conditional mean.

*Recognition cue:* the distribution of $X$ depends on a quantity $Y$ that is *also* random — a random rate, count, tier, or region. Reach for this whenever you can write "the mean of $X$ given the thing, times the chance of the thing."
:::

## Concept 3 — Conditional Variance & the Law of Total Variance: Two Sources of Fear

::: concept-gate
**DO YOU ALREADY OWN THIS? — Total Variance**

Giovanni's squads have conditional means $40, 70, 120$ *and* conditional variances $25, 64, 400$ (the elites are stronger *and* more erratic), with $P(Y) = 0.5, 0.3, 0.2$. What is $\Var(X)$?

If you answered **$1036.7$** by adding $\E[\Var(X\mid Y)] = 111.7$ to $\Var(\E[X\mid Y]) = 925$ — and you know *why you add the two pieces rather than average them* — **skip to Concept 4**. If you only computed $111.7$ (the weighted average of the conditional variances) and stopped, read on: you just discarded the dominant source of risk.
:::

**Beat 1 — The one-sentence idea.** *Total uncertainty in $X$ comes from two separate sources — how noisy each layer is on its own, and how much the layers differ from one another — and you must **add** them, never average them.*

**Beat 2 — Anchor + concrete instance.** Concept 1 gave you two random functions of $Y$: the conditional mean $\E[X\mid Y]$ and now the conditional variance $\Var(X\mid Y)$, the spread *inside* a slice. Total variance combines them. Continue Giovanni's setup: alongside the means $40, 70, 120$, the within-squad strength spreads are

$$\Var(X\mid Y{=}1)=25, \qquad \Var(X\mid Y{=}2)=64, \qquad \Var(X\mid Y{=}3)=400.$$

*How uncertain should you be about the strength overall — and how much of that uncertainty is "which squad" versus "the squad's own noise"?*

**Beat 3 — Reason through it in plain words.** Picture the three slices from Concept 1's figure. Your total uncertainty about a randomly drawn Pokémon's strength has two honest ingredients:

1. **Within-squad noise.** Even if you *knew* the squad, the strength still wobbles around that squad's mean — by variance $25$, $64$, or $400$. On average across squads, that wobble is $25(0.5)+64(0.3)+400(0.2) = 111.7$. Call this the *expected* within-squad variance.
2. **Between-squad spread.** The squad centers themselves are scattered: $40$, $70$, $120$ are far apart. Even with *zero* internal noise, you'd be uncertain simply because you don't know *which* center you're aiming at. That scatter is the variance of the centers $\E[X\mid Y]$, which (from Concept 1, it takes $40,70,120$ with weights $0.5,0.3,0.2$) is $925$.

Total uncertainty stacks both: $111.7 + 925 = 1036.7$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The single most-punished error in this topic is to compute only the first piece and stop:

$$\Var(X) \overset{?}{=} \E[\Var(X\mid Y)] = 111.7. \qquad\textbf{(wrong — drops the between-group spread)}$$

This pretends the only uncertainty is each squad's internal wobble, as if you already knew which squad would show up. But you *don't* — and not knowing is itself a huge source of uncertainty here ($925$, nearly nine times bigger than $111.7$). The reverse error — keeping only $\Var(\E[X\mid Y]) = 925$ — is just as wrong; it pretends each squad is perfectly predictable internally. Total variance is the **sum**: *expected within-group variance plus variance of the group means.* Drop either piece and you mis-state the risk.

**Beat 5 — Translate into notation, one glyph at a time.** First, conditional variance. The variance of $X$ *inside* a slice is an ordinary variance, computed in the slice:

$$\Var(X\mid Y) = \E\big[X^2 \mid Y\big] - \big(\E[X\mid Y]\big)^2 \qquad \text{read aloud: ``the variance of } X \text{ given } Y\text{,''}$$

itself a function of $Y$, hence random. Now the two ingredients become two expressions:

- *Expected within-group variance:* average the conditional variances over $Y$ —
$$\E\big[\Var(X\mid Y)\big] = \sum_y \Var(X\mid Y{=}y)\,P(Y{=}y) = (25)(0.5)+(64)(0.3)+(400)(0.2) = 111.7.$$
- *Variance of the group means:* take the variance of the random center $\E[X\mid Y]$, which takes $40,70,120$ with weights $0.5,0.3,0.2$. Using $\Var(W) = \E[W^2] - (\E[W])^2$ with $\E[W]=65$ from Concept 2,
$$\E\big[(\E[X\mid Y])^2\big] = (40^2)(0.5)+(70^2)(0.3)+(120^2)(0.2) = 800+1470+2880 = 5150,$$
$$\Var\big(\E[X\mid Y]\big) = 5150 - 65^2 = 5150 - 4225 = 925.$$

Add them:

$$\Var(X) = \underbrace{111.7}_{\E[\Var(X\mid Y)]} + \underbrace{925}_{\Var(\E[X\mid Y])} = 1036.7, \qquad \SD(X) = \sqrt{1036.7} \approx 32.2.$$

**Beat 6 — Generalize: derive the formula.** We *build* the law, not assert it. Start from the definition $\Var(X) = \E[X^2] - (\E[X])^2$ and apply total expectation (Concept 2) to $\E[X^2]$:

$$\E[X^2] = \E\big[\,\E[X^2\mid Y]\,\big].$$

Inside each slice, rearrange the conditional-variance definition: $\E[X^2\mid Y] = \Var(X\mid Y) + (\E[X\mid Y])^2$. Substitute:

$$\E[X^2] = \E\big[\Var(X\mid Y)\big] + \E\big[(\E[X\mid Y])^2\big].$$

Also $\E[X] = \E[\E[X\mid Y]]$, so $(\E[X])^2 = \big(\E[\E[X\mid Y]]\big)^2$. Subtract:

$$\Var(X) = \E\big[\Var(X\mid Y)\big] + \underbrace{\Big(\E\big[(\E[X\mid Y])^2\big] - \big(\E[\E[X\mid Y]]\big)^2\Big)}_{=\,\Var(\E[X\mid Y])}.$$

The grouped term is exactly $\Var(\E[X\mid Y])$ — the variance of the random center. That gives the boxed law:

$$\boxed{\;\Var(X) = \underbrace{\E\!\big[\Var(X \mid Y)\big]}_{\text{expected within-group variance}} + \underbrace{\Var\!\big(\E[X \mid Y]\big)}_{\text{variance of the group means}}\;}$$

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the two-row table above, $1036.7$.
- *Cross-check via the other route:* compute $\E[X^2] = \E[\E[X^2\mid Y]]$ directly. Per squad $\E[X^2\mid Y] = \Var + \text{mean}^2$: $25+1600=1625$, $64+4900=4964$, $400+14400=14800$. Then $\E[X^2] = 1625(0.5)+4964(0.3)+14800(0.2) = 5261.7$, so $\Var(X)=5261.7-65^2=1036.7$. ✓ Same answer — a perfect exam self-check.
- *Continuous inner:* if $X\mid\Lambda\sim\Expo(\text{mean}{=}\Lambda)$ then $\Var(X\mid\Lambda)=\Lambda^2$ (exponential variance is mean-squared), and total variance reads $\E[\Lambda^2]+\Var(\Lambda)$.
- *Edge:* if $X$ is independent of $Y$, the centers don't move, so $\Var(\E[X\mid Y])=0$ and $\Var(X)=\E[\Var(X\mid Y)]$ — the second term vanishes only under independence.

**Beat 8 — Picture it.** A two-row table is the entire method: row of conditional means (its *variance* is Term 2), row of conditional variances (its *weighted average* is Term 1).

<figure>
<img src="../../assets/diagrams/ch12_total_variance_table.png" alt="A table with weights 0.5, 0.3, 0.2 across the top. Row 1 holds conditional means 40, 70, 120; an arrow labels its variance as Term 2 = 925. Row 2 holds conditional variances 25, 64, 400; an arrow labels its weighted average as Term 1 = 111.7. A stacked bar on the right shows a small segment (111.7, within-squad noise) atop a large segment (925, which-squad spread), summing to 1036.7, illustrating that the between-squad term dominates." style="width:84%; max-width:620px; display:block; margin:1em auto;">
<figcaption>Total variance from a two-row table: Term 1 is the weighted average of the conditional variances ($111.7$); Term 2 is the variance of the conditional means ($925$). The stacked bar shows that here $\approx 89\%$ of the fear is *which squad shows up*, not the Pokémon's own noise.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now answer Giovanni's full question. You decompose total uncertainty into *process* variance (each squad's own wobble) and *parameter* variance (not knowing the squad), compute both, and add. And you can read off *which dominates*: here $925$ of $1036.7$, about $89\%$, is the hidden squad choice — your nerves are mostly about Giovanni's concealed dice, not the Pokémon.

::: pokedex-entry
**POKÉDEX ENTRY №03 — Conditional Variance & Law of Total Variance**

Conditional variance (a function of $Y$, hence random):
$$\Var(X\mid Y) = \E\big[X^2\mid Y\big] - \big(\E[X\mid Y]\big)^2.$$
Law of Total Variance:
$$\Var(X) = \underbrace{\E\!\big[\Var(X\mid Y)\big]}_{\text{process / within-group}} + \underbrace{\Var\!\big(\E[X\mid Y]\big)}_{\text{parameter / between-group}}.$$

*In plain terms:* total spread has two sources — the *average* spread inside each group, plus the spread of the group *averages*. **Add** them, never average. Term 2 vanishes only when $X$ is independent of $Y$.

*Recognition cue:* you're given, for each value of $Y$, both a conditional mean and a conditional spread (or a named conditional distribution whose variance you know); or the words "process variance and parameter variance," or "how much variability comes from A vs. B." Both terms are required — dropping either is the classic miss.
:::

## Concept 4 — Compound Random Variables: A Random Number of Random Sizes

::: concept-gate
**DO YOU ALREADY OWN THIS? — Compound Variables**

Giovanni's Rhydon lands $N\sim\Poisson(3)$ "Horn Drill" hits before you can switch out; each hit costs i.i.d. item-damage with mean $\mu=50$, variance $\sigma^2=900$. Let $S=\sum_{i=1}^{N}X_i$ be your total damage. Find $\E[S]$ and $\Var(S)$.

If you answered **$\E[S]=150$** and **$\Var(S)=10{,}200$** — and you can say *why the variance has both a "size-noise" piece and a "count-noise" piece* — you own the chapter end to end; **skip to the Gym Battle** for one expert rep, or head straight to the **Gym Challenge**. If you wrote $\Var(S)=\E[N]\sigma^2=2700$ and stopped, read on.
:::

**Beat 1 — The one-sentence idea.** *When you add up a random number $N$ of i.i.d. random pieces, the expected total is "expected count times expected size," and the variance picks up two terms — one for how the sizes vary, one for how the count varies.*

**Beat 2 — Anchor + concrete instance.** This is the two laws of this chapter applied with $Y = N$, the count, as the hidden layer. Condition on $N$, use total expectation and total variance, and the answer falls out — but the result is so common that we'll harden it into a memorized pair of formulas.

During the battle, Giovanni's Rhydon lands a random number $N \sim \Poisson(\lambda = 3)$ of Horn Drill hits before you can switch out. Each hit costs you item-damage $X_i$, independent and identically distributed, with $\E[X_i]=\mu=50$ and $\Var(X_i)=\sigma^2=900$ ($\SD = 30$). Your total damage is

$$S = \sum_{i=1}^{N} X_i.$$

*Find $\E[S]$ and $\Var(S)$.*

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/112.png" alt="Rhydon" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#112 Rhydon — lands a Poisson number of Horn Drills</strong></figcaption>
</figure>

**Beat 3 — Reason through it in plain words.** Suppose for a moment you *knew* the count — say $N=4$ hits. Then $S$ is a sum of $4$ i.i.d. damages: its mean is $4\mu = 200$, and (independent pieces add variances) its variance is $4\sigma^2$. In general, *given* $N$, the conditional mean is $N\mu$ and the conditional variance is $N\sigma^2$ — both functions of the random $N$. Now you don't know $N$, so average over it. Expected total damage is expected-count $\times$ expected-size:

$$\E[S] = \E[N]\,\mu = 3 \times 50 = 150.$$

For the spread, two things vary: *how big* each hit is, and *how many* hits land. Total variance must capture both — and it does.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The tempting move is to use only the size-noise term:

$$\Var(S) \overset{?}{=} \E[N]\,\sigma^2 = 3(900) = 2700. \qquad\textbf{(wrong — forgets the count varies)}$$

This treats $N$ as if it were fixed at its mean. But $N$ is random: some rounds Rhydon lands $1$ hit, some rounds $6$, and that *variation in the number of hits* is its own source of spread. Forgetting it badly understates the risk — here the true variance is $10{,}200$, nearly four times $2700$, because how *many* hits land is the bigger driver. You must add the count-noise term $\Var(N)\,\mu^2$.

**Beat 5 — Translate into notation, one glyph at a time.** Condition on the count $N$ (the hidden layer). For the mean inside a layer, $\E[S\mid N] = N\mu$ (a sum of $N$ averages-of-$\mu$). For the spread inside a layer, $\Var(S\mid N) = N\sigma^2$ (variances of $N$ independent pieces add). Feed these into the two laws:

$$\E[S] = \E\big[\E[S\mid N]\big] = \E[N\mu] = \mu\,\E[N],$$
$$\Var(S) = \E\big[\Var(S\mid N)\big] + \Var\big(\E[S\mid N]\big) = \E[N\sigma^2] + \Var(N\mu) = \sigma^2\,\E[N] + \mu^2\,\Var(N).$$

The last step uses $\E[N\sigma^2] = \sigma^2\E[N]$ (pull out the constant $\sigma^2$) and $\Var(N\mu) = \mu^2\Var(N)$ (a constant comes out of variance squared). Read the two pieces aloud: $\sigma^2\E[N]$ is *"size noise, summed over the expected number of hits"*; $\mu^2\Var(N)$ is *"count noise, scaled by the squared average size."*

**Beat 6 — Generalize: derive the formulas, then specialize to Poisson.** We just derived the general compound formulas straight from the two laws:

$$\boxed{\;\E[S] = \E[N]\,\mu, \qquad \Var(S) = \E[N]\,\sigma^2 + \Var(N)\,\mu^2.\;}$$

Now plug in the numbers. For $N\sim\Poisson(3)$, a Poisson has $\E[N]=\Var(N)=\lambda=3$:

$$\E[S] = 3 \times 50 = 150, \qquad \Var(S) = 3(900) + 3(50^2) = 2700 + 7500 = 10{,}200.$$

When $N$ is Poisson, the two variance terms *merge* into a clean shortcut. Since $\E[N]=\Var(N)=\lambda$,

$$\Var(S) = \lambda\sigma^2 + \lambda\mu^2 = \lambda(\sigma^2+\mu^2) = \lambda\,\E[X^2].$$

Here $\E[X^2] = \sigma^2+\mu^2 = 900+2500 = 3400$, so $\Var(S) = 3(3400) = 10{,}200$ ✓ — same answer, one multiplication. **Memorize: for a compound Poisson, $\Var(S) = \lambda\,\E[X^2]$.**

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the Poisson Rhydon, $\E[S]=150$, $\Var(S)=10{,}200$.
- *Non-Poisson count:* if $N$ is geometric with $\E[N]=2.5$, $\Var(N)=3.75$ and $\mu=60$, $\sigma^2=100$, then $\E[S]=150$ and $\Var(S)=2.5(100)+3.75(3600)=13{,}750$ — use the *general* formula; the Poisson shortcut no longer applies.
- *Exponential severity:* if $X_i\sim\Expo(\text{mean}{=}200)$ then $\E[X^2]=2\theta^2=80{,}000$, so a compound Poisson with $\lambda=10$ has $\Var(S)=10(80{,}000)=800{,}000$.
- *Edge (fixed count):* if $N$ is a constant $n$ (not random), $\Var(N)=0$ and the count term disappears: $\Var(S)=n\sigma^2$, the ordinary sum-of-$n$-i.i.d. result. The count term is the *whole* novelty here.

**Beat 8 — Picture it.** A compound sum is a tree whose *number* of branches is itself random.

<figure>
<img src="../../assets/diagrams/ch12_compound_tree.png" alt="A diagram showing a random count N branching at the top into possible values 0, 1, 2, 3, ... with Poisson weights, and below each, that many i.i.d. damage blocks X1, X2, ... stacked to form the total S. A bracket on the right decomposes Var(S) into two stacked bars: size-noise lambda*sigma^2 = 2700 and count-noise lambda*mu^2 = 7500, summing to 10200." style="width:84%; max-width:620px; display:block; margin:1em auto;">
<figcaption>A compound sum: $N$ random pieces, each random in size. The variance splits into size-noise $\E[N]\sigma^2 = 2700$ and count-noise $\Var(N)\mu^2 = 7500$, summing to $10{,}200$ — the count term dominates.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now model a random number of random sizes: condition on the count, apply the two laws, and land on $\E[S]=\E[N]\mu$ and $\Var(S)=\E[N]\sigma^2+\Var(N)\mu^2$ — with the $\lambda\E[X^2]$ shortcut when the count is Poisson. This is the actuary's aggregate-loss model, and it completes your Viridian toolkit.

::: pokedex-entry
**POKÉDEX ENTRY №04 — Compound Random Variable $S = \sum_{i=1}^{N} X_i$**

Let $N$ be a random count and $X_1, X_2, \dots$ i.i.d. severities, independent of $N$, with $\E[X_i]=\mu$, $\Var(X_i)=\sigma^2$. Then
$$\E[S] = \E[N]\,\mu, \qquad \Var(S) = \E[N]\,\sigma^2 + \Var(N)\,\mu^2.$$
If $N\sim\Poisson(\lambda)$, the variance collapses to $\;\Var(S) = \lambda\,\E[X^2] = \lambda(\sigma^2+\mu^2).$

*In plain terms:* a random number of hits, each of random size. Expected total $=$ expected count $\times$ expected size. The variance carries a size-noise term ($\E[N]\sigma^2$) and a count-noise term ($\Var(N)\mu^2$).

*Recognition cue:* "a random number $N$ of events, each contributing a random amount" — total damage from a random number of attacks, total claims from a random number of accidents. Condition on $N$; reach for the two boxed formulas, and the Poisson shortcut if $N$ is Poisson.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/giovanni.png" alt="Giovanni, Viridian Gym Leader and Team Rocket boss" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Giovanni — the leader whose true strength is hidden inside a randomly chosen squad.</figcaption>
</figure>

Four examples, fading from fully narrated to exam speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because total variance is the hard, load-bearing idea.

### Worked Example 12.1 — How Afraid Should You Be? (full narration; understanding-first)

**ARCHETYPE:** *Law of total variance — decompose into expected conditional variance + variance of the conditional mean.*

**Setup.** Giovanni's squad $Y$ is drawn with $P(Y) = 0.5, 0.3, 0.2$. Conditional means $\E[X\mid Y]=40,70,120$; conditional variances $\Var(X\mid Y)=25,64,400$. Find $\E[X]$, then $\Var(X)$, and report which source of uncertainty dominates.

**Step 1 — Identify (which law, and is the conditioning variable random?).** $X$'s mean *and* spread both depend on the random squad $Y$. We're asked for an unconditional mean and variance over a hidden layer $\to$ total expectation, then total variance. Givens are already in two-row form: means and variances per squad.

**Step 2 — Mean by total expectation (warm-up).** Weight each conditional mean by its squad probability:
$$\E[X] = (40)(0.5)+(70)(0.3)+(120)(0.2) = 20+21+24 = 65.$$

**Step 3 — Professor's Path (the why).** Total variance has two pieces. *Within-squad noise* is the expected conditional variance:
$$\E[\Var(X\mid Y)] = (25)(0.5)+(64)(0.3)+(400)(0.2) = 12.5+19.2+80 = 111.7.$$
*Between-squad spread* is the variance of the conditional means $g(Y)$, which takes $40,70,120$ with weights $0.5,0.3,0.2$ and has mean $65$:
$$\E[g(Y)^2] = (40^2)(0.5)+(70^2)(0.3)+(120^2)(0.2) = 800+1470+2880 = 5150,$$
$$\Var(g(Y)) = 5150 - 65^2 = 5150-4225 = 925.$$
Add the two sources:
$$\Var(X) = 111.7 + 925 = 1036.7, \qquad \SD(X) = \sqrt{1036.7} \approx 32.2.$$

**Step 4 — Trainer's Path (the fast cross-check, via $\E[X^2]$).** Per squad, $\E[X^2\mid Y]=\Var+\text{mean}^2$: $25+1600=1625$, $64+4900=4964$, $400+14400=14800$. Then $\E[X^2]=1625(0.5)+4964(0.3)+14800(0.2)=5261.7$, so $\Var(X)=5261.7-65^2=1036.7$ ✓.

**Step 5 — Check, verdict & pitfall.** Sanity: $\E[X]=65$ lies between $40$ and $120$ ✓; $\Var(X)=1036.7$ exceeds both Term 1 alone and the within-squad piece ✓. **Verdict:** $925/1036.7 \approx 89\%$ of the fear is *which squad shows up*; only $\approx 11\%$ is the Pokémon's own noise. **Pitfall:** reporting only $\E[\Var(X\mid Y)]=111.7$ and stopping — that throws away the dominant $925$. *(Back-ref: Entry №03.)*

### Worked Example 12.2 — A Random Recovery Rate (partial guidance; continuous layer)

**ARCHETYPE:** *Continuous mixture — total expectation and total variance with a random parameter; exponential inner.*

**Setup.** A captured Nidoking's recovery time $X$ (minutes) is exponential, but the *rate* depends on how injured it is: $X \mid \Lambda \sim \Expo(\text{mean}{=}\Lambda)$, where the random mean $\Lambda \sim \Unif(10,20)$. Find $\E[X]$ and $\Var(X)$.

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/34.png" alt="Nidoking" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#34 Nidoking — recovery time with a random rate $\Lambda$</strong></figcaption>
</figure>

**Identify.** Inner is exponential with mean $\Lambda$, so (exponential facts) $\E[X\mid\Lambda]=\Lambda$ and $\Var(X\mid\Lambda)=\Lambda^2$. Outer $\Lambda\sim\Unif(10,20)$: $\E[\Lambda]=15$, $\Var(\Lambda)=\tfrac{(20-10)^2}{12}=\tfrac{100}{12}=8.3\overline{3}$. *Your move: feed these into the two laws.*

**Mean (total expectation).**
$$\E[X] = \E[\E[X\mid\Lambda]] = \E[\Lambda] = 15 \text{ minutes}.$$

**Variance (total variance).** Term 1 needs $\E[\Lambda^2] = \Var(\Lambda)+\E[\Lambda]^2 = 8.3\overline{3}+225 = 233.3\overline{3}$:
$$\Var(X) = \E[\Var(X\mid\Lambda)] + \Var(\E[X\mid\Lambda]) = \E[\Lambda^2] + \Var(\Lambda) = 233.3\overline{3}+8.3\overline{3} = 241.6\overline{6}.$$

**Check & pitfall.** If $\Lambda$ were *fixed* at $15$, an exponential would have variance $15^2=225$. Letting the rate itself vary *adds* $\Var(\Lambda)=8.33$ on top, giving $241.67 > 225$ — uncertainty in the rate can only increase total spread ✓. **Pitfall:** writing $\Var(X)=\Var(\Lambda)=8.33$, forgetting the within-rate exponential noise $\E[\Lambda^2]$. *(Back-ref: Entry №03.)*

### Worked Example 12.3 — Compound Damage From a Random Number of Attacks (light guidance)

**ARCHETYPE:** *Compound distribution — random Poisson count times random severity.*

**Setup.** Giovanni's Rhydon lands $N\sim\Poisson(\lambda{=}3)$ Horn Drills; each costs i.i.d. damage with $\mu=50$, $\sigma^2=900$. Let $S=\sum_{i=1}^N X_i$. Find $\E[S]$ and $\Var(S)$.

**Identify.** Compound sum; $\Poisson(3)$ gives $\E[N]=\Var(N)=3$.

$$\E[S] = \E[N]\mu = 3(50) = 150.$$
$$\Var(S) = \E[N]\sigma^2 + \Var(N)\mu^2 = 3(900)+3(2500) = 2700+7500 = 10{,}200.$$

**Poisson shortcut (cross-check).** $\E[X^2]=\sigma^2+\mu^2=3400$, so $\Var(S)=\lambda\E[X^2]=3(3400)=10{,}200$ ✓.

**Check & pitfall.** Both pieces present: $2700$ from severity noise, $7500$ from count noise. **Pitfall:** using $\Var(S)=\E[N]\sigma^2=2700$ alone — that understates the risk nearly four-fold, because how *many* hits land dominates. *(Back-ref: Entry №04.)*

### Worked Example 12.4 — Prize That Scales With the Round (exam speed)

**ARCHETYPE:** *Total variance with a Poisson outer layer and linear conditional moments.*

**Setup.** A trainer's prize $X$ given the round reached $Y$ has $\E[X\mid Y]=100Y$ and $\Var(X\mid Y)=400Y$, with $Y\sim\Poisson(\lambda{=}2)$. Find $\E[X]$ and $\Var(X)$.

$$\E[X] = \E[100Y] = 100\,\E[Y] = 100(2) = 200.$$
$$\text{Term 1: } \E[\Var(X\mid Y)] = \E[400Y] = 400(2) = 800.$$
$$\text{Term 2: } \Var(\E[X\mid Y]) = \Var(100Y) = 100^2\,\Var(Y) = 10000(2) = 20000.$$
$$\Var(X) = 800 + 20000 = 20800.$$

**Check & pitfall.** Both terms kept; $\Var(X)=20800 > 800$ ✓. **Pitfall:** $\Var(100Y)=100\Var(Y)$ instead of $100^2\Var(Y)$ — constants leave a variance *squared*. *(Back-ref: Entry №03.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — Spot the hidden layer instantly**

If a parameter — rate, mean, count, tier, region — is *itself described as random*, condition on it first. Write $\E[X\mid Y]$ and $\Var(X\mid Y)$ as **functions of $Y$**, then feed them into the two laws. Never plug the *average* parameter into a nonlinear formula — that is Jensen's trap and the single most common total-expectation error.
:::

::: trainers-tip
**TRAINER'S TIP — Build the two-row table for total variance**

Make a small table: weights $P(Y{=}y)$ across the top, conditional means in row 1, conditional variances in row 2. **Term 1** is the weighted average of row 2; **Term 2** is the *variance* of row 1 (use $\E[g^2]-(\E g)^2$). On the TI-30XS, enter the conditional means as a data list with frequencies $P(Y{=}y)\times 100$ and read the *population* variance $\sigma_x^2$ directly — that is Term 2, computed for you.
:::

::: trainers-tip
**TRAINER'S TIP — Memorize the compound pair (and the Poisson shortcut)**

$\E[S]=\E[N]\mu$ and $\Var(S)=\E[N]\sigma^2+\Var(N)\mu^2$ appear almost every sitting. If $N$ is **Poisson**, collapse the variance to $\Var(S)=\lambda\,\E[X^2]=\lambda(\sigma^2+\mu^2)$ — recognizing "$N$ is Poisson" can save you two minutes. Keep both the general form and the shortcut at your fingertips.
:::

::: trainers-tip
**TRAINER'S TIP — Sanity-bound the conditional mean**

$\E[X]$ from total expectation is a weighted average of the conditional means, so it must land **between** the smallest and largest of them. If your overall mean falls outside that range, stop — you have an arithmetic slip before you even reach the variance.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

"Boss wants the expected strength of his own Pokémon," Jessie announces, "so we just plug the *average* squad into the strength rule. Average squad index is $0.5(1)+0.3(2)+0.2(3)=1.7$ — so the answer's the strength of squad $1.7$, somewhere between $40$ and $70$, call it $55$!" James writes down $55$. Meowth squints: "But da squad's gotta be a *whole* squad — dere ain't no squad one-point-seven." Jessie waves him off. Their estimate of $55$ is well under the true $65$, and when Giovanni's elites actually show up, the Rockets are flattened.

**Where it fails:** Jessie computed $\E\big[X \mid Y = \E[Y]\big]$ instead of $\E\big[\E[X\mid Y]\big]$ — she collapsed the random $Y$ to its average $\E[Y]=1.7$ *before* applying the conditional mean. But $\E[X\mid Y]$ is a *random variable* (Entry №01), and you must average the conditional **means** themselves, each weighted by $P(Y{=}y)$: $40(0.5)+70(0.3)+120(0.2)=65$. This is **Jensen's trap** — plugging the mean of an input into a nonlinear rule. Meowth's instinct was right: there is no squad $1.7$. The fix is the Law of Total Expectation, never the "average squad."
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

The Law of Total Variance is the mathematical heart of **credibility theory** — how an insurer blends one policyholder's own claim history with the experience of the whole class.

The decomposition $\Var(X)=\E[\Var(X\mid Y)]+\Var(\E[X\mid Y])$ splits a risk's variability into **process variance** — the irreducible randomness of claims *given* the true risk level $Y$ (the within-squad noise) — and **parameter variance** — the uncertainty about *which* risk level the policyholder actually is (the between-squad spread). The credibility weight $Z$ assigned to an individual's own data is built directly from the ratio of these two pieces: when parameter variance dominates (policyholders differ a lot, like Giovanni's squads), you trust the individual's data more; when process variance dominates, you lean on the class average.

**Compound models** — a random *number* of claims, each of random *size* — are exactly how insurers price and reserve **aggregate annual losses**. The compound Poisson $\Var(S)=\lambda\E[X^2]$ you derived is the standard frequency-severity model for a year of claims on a policy.

*Series bridge:* this exact decomposition reappears as **Bühlmann credibility** on CAS Exam MAS-II, and compound aggregate-loss models anchor CAS Exam 5 ratemaking.

*Transfer check:* could you solve this with **no Pokémon in it**? "A driver's annual claim count is $N\sim\Poisson(3)$; each claim's cost has mean $\$50$ and variance $\$900$. Find the mean and variance of total annual cost." Same $\E[S]=150$, $\Var(S)=10{,}200$. If you can do that, the skill has transferred to the day job.
:::

## The Gym Battle — Earth Badge Capstone

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/types/ground.png" alt="Ground type icon" style="width:90px; display:block; margin:0 auto;">
<figcaption style="font-size:0.85em;">Giovanni's Ground-type Gym — the Earth Badge challenge</figcaption>
</figure>

**Giovanni's Challenge.** "Enough talk," Giovanni says, the full Rocket payroll on the line. "My threat this round is built in two layers. Find its expected damage and its variance — and tell me which layer you should fear more."

*Layer 1 (which squad fights).* The tier $Y$ is drawn: $P(Y{=}1)=0.5$ (Diglett-line scouts), $P(Y{=}2)=0.3$ (Nidoking-line regulars), $P(Y{=}3)=0.2$ (Rhydon-line elites).

*Layer 2 (compound damage within the squad).* Given the tier, the number of attacks $N$ this round is $\Poisson(\lambda_Y)$, and each attack's damage is i.i.d. with mean $\mu_Y$ and variance $\sigma_Y^2$:

| Tier $y$ | $P(Y{=}y)$ | $\lambda_y$ | $\mu_y$ | $\sigma_y^2$ |
|---|---|---|---|---|
| 1 | $0.5$ | $2$ | $10$ | $25$ |
| 2 | $0.3$ | $3$ | $20$ | $100$ |
| 3 | $0.2$ | $4$ | $30$ | $225$ |

Find the overall expected damage $\E[X]$ and variance $\Var(X)$, and say which layer dominates the risk.

**ARCHETYPE:** *Two-layer integrative — compound (Poisson) damage nested inside a random-tier mixture; total expectation and total variance applied across both layers.*

**Step 1 — Identify the two nested layers.** Within a tier, $X$ is a compound-Poisson sum, so (Entry №04) the conditional mean is $\E[X\mid Y{=}y]=\lambda_y\mu_y$ and, by the Poisson shortcut, the conditional variance is $\Var(X\mid Y{=}y)=\lambda_y(\sigma_y^2+\mu_y^2)$. Then apply total expectation and total variance over the tier $Y$.

**Step 2 — Conditional means $\E[X\mid Y{=}y]=\lambda_y\mu_y$.**
$$y{=}1:\ 2(10)=20, \qquad y{=}2:\ 3(20)=60, \qquad y{=}3:\ 4(30)=120.$$

**Step 3 — Overall mean (total expectation).**
$$\E[X] = 20(0.5)+60(0.3)+120(0.2) = 10+18+24 = 52.$$

**Step 4 — Conditional variances $\Var(X\mid Y{=}y)=\lambda_y(\sigma_y^2+\mu_y^2)$.**
$$y{=}1:\ 2(25+100)=250, \qquad y{=}2:\ 3(100+400)=1500, \qquad y{=}3:\ 4(225+900)=4500.$$

**Step 5 — Term 1, expected conditional variance (within-tier).**
$$\E[\Var(X\mid Y)] = 250(0.5)+1500(0.3)+4500(0.2) = 125+450+900 = 1475.$$

**Step 6 — Term 2, variance of the conditional means $20,60,120$ (between-tier), mean $52$.**
$$\E[g(Y)^2] = 20^2(0.5)+60^2(0.3)+120^2(0.2) = 200+1080+2880 = 4160,$$
$$\Var(g(Y)) = 4160 - 52^2 = 4160-2704 = 1456.$$

**Step 7 — Total variance.**
$$\Var(X) = \underbrace{1475}_{\text{within-tier}} + \underbrace{1456}_{\text{between-tier}} = 2931, \qquad \SD(X)=\sqrt{2931}\approx 54.1.$$

**Step 8 — Verdict & pitfalls.** Sanity: $\E[X]=52$ sits between $20$ and $120$ ✓; $\Var(X)=2931$ exceeds Term 1 alone ✓. **Which layer dominates?** The two terms are nearly equal — $1475$ within-tier versus $1456$ between-tier — so about half the threat's variability comes from the compound randomness *inside* a tier and half from *which tier* Giovanni deploys. Both layers matter, exactly as he was testing. **Pitfall #1:** using $\Var(X\mid Y)=\lambda_y\sigma_y^2$ — for compound Poisson it must be $\lambda_y(\sigma_y^2+\mu_y^2)$. **Pitfall #2:** forgetting Term 2 and reporting $1475$, discarding nearly half the risk.

> "That," Giovanni says, the lights coming up at last, "is how you read a hidden risk. You separated the fear from my dice from the fear from my Pokémon. The Earth Badge is yours." Eight badges. The Plateau is next.

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/earth_badge.png" alt="Earth Badge" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Earth Badge earned!</strong> All eight badges — on to Victory Road.</figcaption>
</figure>

## The Gym Challenge — Problem Set

::: problem-set
**TEST-OUT INSTRUCTIONS.** Work this set timed (~6 min/problem), then check the **Answer Key** below. Hit the mastery bar (**80%+ with correct method**) and you may move on. Problems are listed first; full worked solutions follow afterward (never interleaved). Markers: 🔴 Poké Ball = routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (mechanics)

**C12.1.** 🔴 A Rocket scout reports from one of two camps: forest ($P=0.6$) or cave ($P=0.4$). The grunt count $X$ has $\E[X\mid\text{forest}]=4$ and $\E[X\mid\text{cave}]=9$. Find $\E[X]$.

**C12.2.** 🔴 A wild Diglett's burrow depth $X$ given soil type $Y$ has $\E[X\mid\text{soft}]=30$ cm ($P=0.7$) and $\E[X\mid\text{rocky}]=12$ cm ($P=0.3$). Find the unconditional mean depth.

**C12.3.** 🔴 Hourly Marowak count $X$ given the tower floor $Y$ has conditional means $20, 35, 50$ on floors with probabilities $0.5, 0.3, 0.2$. Find $\E[X]$.

**C12.4.** 🟡 A Rhyhorn's charge distance $X$ given anger $Y\in\{1,2,3\}$ (each $P=1/3$) has conditional variances $4, 9, 16$. Find $\E[\Var(X\mid Y)]$ (Term 1 of total variance only).

**C12.5.** 🟡 For the same Rhyhorn, the conditional means are $5, 11, 20$ (each $P=1/3$) and conditional variances $4, 9, 16$. Find $\Var(\E[X\mid Y])$ (Term 2), then state $\Var(X)$.

**C12.6.** 🟡 A Nidoran's recovery time is $X\mid\Lambda \sim \Expo(\text{mean}{=}\Lambda)$ with $\Lambda$ equal to $4$ or $8$, each w.p. $1/2$. Find $\E[X]$.

**C12.7.** 🔴 A team lands $N$ attacks with $\E[N]=5$; each attack does damage with mean $\mu=8$, independent of $N$. Find the expected total damage $\E[S]$.

### Gym Battles (true SOA difficulty)

**C12.8.** 🟡 The payout $X$ of a rigged Game Corner wheel given setting $Y$: setting A ($P=0.5$) has $\E[X\mid A]=2$, $\Var(X\mid A)=1$; setting B ($P=0.5$) has $\E[X\mid B]=10$, $\Var(X\mid B)=4$. Find $\E[X]$, $\Var(X)$, and state whether within-setting noise or setting choice dominates.

**C12.9.** 🟡 A Sandslash's daily foraging mass $X\mid\Theta \sim \Expo(\text{mean}{=}\Theta)$ with scale $\Theta \sim \Unif(2,6)$. Find $\E[X]$ and $\Var(X)$.

**C12.10.** 🟡 A grunt fires $N\sim\Poisson(\lambda{=}4)$ smoke bombs; each obscures by an i.i.d. amount with $\mu=3$, $\sigma^2=5$. Let $S$ be total obscuration. Find $\E[S]$ and $\Var(S)$.

**C12.11.** 🔵 Encounters per hour $N\mid\Lambda \sim \Poisson(\Lambda)$, where the local density $\Lambda \sim \GammaDist(\alpha{=}3,\theta{=}2)$, so $\E[\Lambda]=6$, $\Var(\Lambda)=12$. Find $\E[N]$ and $\Var(N)$. *(This is the negative-binomial-as-mixture setup.)*

**C12.12.** 🟡 A trainer's prize $X$ given round $Y$ has $\E[X\mid Y]=100Y$ and $\Var(X\mid Y)=400Y$, with $Y\sim\Poisson(\lambda{=}2)$. Find $\E[X]$ and $\Var(X)$.

**C12.13.** 🔵 Roll a fair die $Y\in\{1,\dots,6\}$, then draw a card worth $X\sim\Unif(0,Y)$, so $\E[X\mid Y]=Y/2$ and $\Var(X\mid Y)=Y^2/12$. Find $\E[X]$ and $\Var(X)$.

**C12.14.** 🔵 Each grunt commands $N$ Pokémon, $N$ geometric on $\{1,2,3,\dots\}$ with $P(N{=}n)=(0.4)(0.6)^{n-1}$, so $\E[N]=2.5$, $\Var(N)=3.75$. Each Pokémon's strength is i.i.d. with $\mu=60$, $\sigma^2=100$. Find $\E[S]$ and $\Var(S)$ for total squad strength.

### Elite Challenge (integrative / stretch)

**C12.15.** 🔵 Giovanni's two-layer threat. Tier $Y$: $P(Y{=}1)=0.5$, $P(Y{=}2)=0.3$, $P(Y{=}3)=0.2$. Given tier $y$, damage $X$ is compound-Poisson with attack-count mean $\lambda_y$ and per-attack severity mean $\mu_y$, variance $\sigma_y^2$:

| $y$ | $\lambda_y$ | $\mu_y$ | $\sigma_y^2$ |
|---|---|---|---|
| 1 | $2$ | $12$ | $36$ |
| 2 | $4$ | $18$ | $81$ |
| 3 | $5$ | $25$ | $144$ |

Find $\E[X]$, $\Var(X)$, and the fraction of total variance attributable to *which tier* fights.

**C12.16.** 🔵 A Rocket scientist's experiment yields $X\mid Y \sim \Normal(\mu{=}Y, \sigma^2{=}4)$ where the random center $Y \sim \Normal(50, 9)$. Find $\E[X]$ and $\Var(X)$, identify the unconditional distribution of $X$, and find $P(X > 56)$.

**C12.17.** 🔵 Aggregate annual claims on a Rocket insurance scam: $N\sim\Poisson(\lambda{=}10)$ claims, each severity $X_i\sim\Expo(\text{mean}{=}200)$, independent. Find $\E[S]$, $\Var(S)$, the coefficient of variation $\SD(S)/\E[S]$, and — treating $S$ as approximately normal (CLT for aggregate losses) — estimate $P(S > 2600)$.
:::

## Answer Key

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

**C12.1** — *Total expectation, two-group discrete (Entry №02).*
$$\E[X] = 4(0.6)+9(0.4) = 2.4+3.6 = 6 \text{ grunts}.$$

**C12.2** — *Total expectation, two-group discrete (Entry №02).*
$$\E[X] = 30(0.7)+12(0.3) = 21+3.6 = 24.6 \text{ cm}.$$

**C12.3** — *Total expectation, three-group discrete (Entry №02).*
$$\E[X] = 20(0.5)+35(0.3)+50(0.2) = 10+10.5+10 = 30.5.$$

**C12.4** — *Expected conditional variance, Term 1 (Entry №03).*
$$\E[\Var(X\mid Y)] = \tfrac13(4+9+16) = \tfrac{29}{3} \approx 9.667.$$

**C12.5** — *Variance of the conditional mean, Term 2, then total variance (Entry №03).* Means $5,11,20$, each weight $\tfrac13$:
$$\E[g]=\tfrac{5+11+20}{3}=12, \quad \E[g^2]=\tfrac{25+121+400}{3}=\tfrac{546}{3}=182, \quad \Var(g)=182-144=38.$$
$$\Var(X) = \tfrac{29}{3}+38 = 9.667+38 = 47.667.$$

**C12.6** — *Total expectation, exponential with random mean (Entries №01, №02).* $\E[X\mid\Lambda]=\Lambda$, so
$$\E[X]=\E[\Lambda]=\tfrac12(4)+\tfrac12(8)=6.$$

**C12.7** — *Compound mean (Entry №04).*
$$\E[S]=\E[N]\mu = 5(8) = 40.$$

**C12.8** — *Total variance, two-group decomposition with interpretation (Entry №03).*
$$\E[X]=2(0.5)+10(0.5)=6.$$
Term 1: $\E[\Var(X\mid Y)]=1(0.5)+4(0.5)=2.5$. Term 2: means $2,10 \Rightarrow \E[g^2]=4(0.5)+100(0.5)=52$, $\Var(g)=52-36=16$.
$$\Var(X)=2.5+16=18.5.$$
The **setting choice ($16$)** dominates the within-setting noise ($2.5$).

**C12.9** — *Continuous mixture, exponential with uniform scale (Entries №01, №03).* $\E[X\mid\Theta]=\Theta$, $\Var(X\mid\Theta)=\Theta^2$. With $\Theta\sim\Unif(2,6)$: $\E[\Theta]=4$, $\Var(\Theta)=\tfrac{(6-2)^2}{12}=\tfrac{16}{12}=1.333$, $\E[\Theta^2]=1.333+16=17.333$.
$$\E[X]=4, \qquad \Var(X)=\E[\Theta^2]+\Var(\Theta)=17.333+1.333=18.667.$$

**C12.10** — *Compound Poisson mean and variance (Entry №04).*
$$\E[S]=\lambda\mu=4(3)=12, \qquad \Var(S)=\lambda(\sigma^2+\mu^2)=4(5+9)=4(14)=56.$$

**C12.11** — *Poisson–Gamma mixture / negative binomial (Entries №02, №03).* Poisson inner: $\E[N\mid\Lambda]=\Var(N\mid\Lambda)=\Lambda$.
$$\E[N]=\E[\Lambda]=6, \qquad \Var(N)=\E[\Lambda]+\Var(\Lambda)=6+12=18.$$
Variance exceeds the mean — overdispersion, the negative-binomial signature.

**C12.12** — *Total variance, Poisson outer with linear conditionals (Entry №03).*
$$\E[X]=\E[100Y]=100(2)=200.$$
Term 1: $\E[400Y]=400(2)=800$. Term 2: $\Var(100Y)=100^2\Var(Y)=10000(2)=20000$.
$$\Var(X)=800+20000=20800.$$

**C12.13** — *Continuous mixture over a discrete outer layer (Entries №02, №03).* Die: $\E[Y]=3.5$, $\E[Y^2]=\tfrac{91}{6}=15.1\overline{6}$, $\Var(Y)=15.1667-12.25=2.9167$.
$$\E[X]=\E[Y/2]=1.75.$$
Term 1: $\E[Y^2/12]=15.1667/12=1.2639$. Term 2: $\Var(Y/2)=\tfrac14\Var(Y)=\tfrac14(2.9167)=0.7292$.
$$\Var(X)=1.2639+0.7292\approx 1.993.$$

**C12.14** — *Compound with geometric count (Entry №04).*
$$\E[S]=\E[N]\mu=2.5(60)=150.$$
$$\Var(S)=\E[N]\sigma^2+\Var(N)\mu^2=2.5(100)+3.75(3600)=250+13500=13{,}750.$$

**C12.15** — *Two-layer integrative: compound Poisson nested in a tier mixture (Entries №03, №04).* Conditional means $\lambda_y\mu_y$: $2(12)=24$, $4(18)=72$, $5(25)=125$.
$$\E[X]=24(0.5)+72(0.3)+125(0.2)=12+21.6+25=58.6.$$
Conditional variances (Poisson shortcut $\lambda_y(\sigma_y^2+\mu_y^2)$): $2(36+144)=360$, $4(81+324)=1620$, $5(144+625)=3845$.
Term 1: $360(0.5)+1620(0.3)+3845(0.2)=180+486+769=1435$.
Term 2: $\E[g^2]=24^2(0.5)+72^2(0.3)+125^2(0.2)=288+1555.2+3125=4968.2$; $\Var(g)=4968.2-58.6^2=4968.2-3433.96=1534.24$.
$$\Var(X)=1435+1534.24=2969.24.$$
Fraction from *which tier*: $1534.24/2969.24\approx 0.517$ (about $52\%$).

**C12.16** — *Normal–normal mixture; recognize the convolution (Entries №02, №03).*
$$\E[X]=\E[Y]=50, \qquad \Var(X)=\E[\Var(X\mid Y)]+\Var(\E[X\mid Y])=4+9=13.$$
A normal mean with a normal center stays normal: $X\sim\Normal(50,13)$, $\sigma=\sqrt{13}=3.606$.
$$P(X>56)=1-\Phi\!\Big(\tfrac{56-50}{3.606}\Big)=1-\Phi(1.664)\approx 1-0.9519=0.0481.$$

**C12.17** — *Compound Poisson with exponential severity + CLT (Entry №04).* Exponential mean $200$: $\mu=200$, $\sigma^2=40000$, $\E[X^2]=\sigma^2+\mu^2=80000$ ($=2\theta^2$).
$$\E[S]=\lambda\mu=10(200)=2000, \qquad \Var(S)=\lambda\,\E[X^2]=10(80000)=800{,}000, \quad \SD(S)=\sqrt{800000}=894.4.$$
$$\text{CV}=894.4/2000=0.447.$$
$$P(S>2600)\approx 1-\Phi\!\Big(\tfrac{2600-2000}{894.4}\Big)=1-\Phi(0.671)\approx 1-0.7488=0.2512.$$

### Quick-Answer Table

| # | Answer | | # | Answer |
|---|---|---|---|---|
| C12.1 | $6$ | | C12.10 | $\E[S]=12,\ \Var(S)=56$ |
| C12.2 | $24.6$ cm | | C12.11 | $\E[N]=6,\ \Var(N)=18$ |
| C12.3 | $30.5$ | | C12.12 | $\E[X]=200,\ \Var(X)=20800$ |
| C12.4 | $9.667$ | | C12.13 | $\E[X]=1.75,\ \Var(X)\approx 1.993$ |
| C12.5 | $\Var(g)=38,\ \Var(X)=47.667$ | | C12.14 | $\E[S]=150,\ \Var(S)=13750$ |
| C12.6 | $6$ | | C12.15 | $\E[X]=58.6,\ \Var(X)\approx 2969.2$ ($\approx 52\%$ tier) |
| C12.7 | $40$ | | C12.16 | $X\sim\Normal(50,13),\ P(X{>}56)\approx 0.048$ |
| C12.8 | $\E[X]=6,\ \Var(X)=18.5$ (setting) | | C12.17 | $\E[S]=2000,\ \Var(S)=800000,\ P{\approx}0.251$ |
| C12.9 | $\E[X]=4,\ \Var(X)=18.667$ | | | |
:::

## Badge Earned — Mastery Checklist

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/earth_badge.png" alt="Earth Badge" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Earth Badge earned!</strong></figcaption>
</figure>

You earn the **Earth Badge** when you can, unaided:

1. **Compute** a conditional expectation $\E[X\mid Y]$ and conditional variance $\Var(X\mid Y)$ for a given inner distribution, and recognize each as a *function of* $Y$ — a random variable, not a constant. *(Outcome 3c.)*
2. **Apply** the **Law of Total Expectation** $\E[X]=\E[\E[X\mid Y]]$ to recover an unconditional mean by weighting conditional means by $P(Y{=}y)$ (or integrating over a continuous $Y$), and sanity-bound it between the smallest and largest conditional mean. *(Outcome 3c.)*
3. **Apply** the **Law of Total Variance** $\Var(X)=\E[\Var(X\mid Y)]+\Var(\E[X\mid Y])$, computing *both* terms and interpreting them as within-group (process) and between-group (parameter) variance. *(Outcome 3d.)*
4. **Set up and solve** a compound/mixture model with $\E[S]=\E[N]\mu$ and $\Var(S)=\E[N]\sigma^2+\Var(N)\mu^2$ — and the compound-Poisson shortcut $\Var(S)=\lambda\,\E[X^2]$. *(Outcomes 3c, 3d.)*

> **Gym rematch pointers (🧴 Potion).** Miss item 1 $\to$ re-read Concept 1 and the Team Rocket Trap. Miss item 2 $\to$ Concept 2 + WE 12.1's mean step / C12.1–C12.3. Miss item 3 $\to$ Concept 3 + WE 12.1–12.2 and the Gym Battle, then retry C12.8 and C12.13. Miss item 4 $\to$ Concept 4 + WE 12.3 / C12.10 and C12.14.

*Eight badges earned. Onward — to where many random variables move **together**, and the covariance that measures it.*
