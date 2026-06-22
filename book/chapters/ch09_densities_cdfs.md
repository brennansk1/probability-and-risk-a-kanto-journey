<!--
  file: ch09_densities_cdfs
  tier: B
  outcomes: 2a
  tia: B.1
  locale: Saffron City / Sabrina / Marsh Badge
  type: psychic
  maps_to: Saffron's smooth psychic world -> probability as AREA; densities & CDFs
           (f=F', the normalizing constant, P(a<=X<=b)=integral); mixed distributions
-->

# Probability as Area — Densities & CDFs {.type-psychic}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with Saffron City at the center of the region circled as the current destination; Celadon lies to the west, Vermilion to the south, and the Silph Co. tower rises at Saffron's heart. The five earned badges are noted along the route from Cerulean." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 10 — five badges behind you, you reach <strong>Saffron City</strong>, the central hub of Kanto: the Silph Co. tower, Sabrina's Psychic gym, and the home of the <em>Marsh Badge</em> — where the countable world melts into a <em>smooth, continuous</em> one.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Tower of Smooth Things"**

You step off the maglev into **Saffron City**, and the world stops feeling *discrete*. Every leg until now came in countable chunks — *how many* Gastly, *how many* slot pulls, *how many* successful catches. You could line the answers up — $0, 1, 2, 3, \dots$ — and set a probability bar on each.

Here, inside the Silph Co. tower that **Sabrina's** mind has folded into a single endless gradient, nothing comes in chunks. A psychic meter on the wall does not *tick* from $4$ to $5$; it **glides**, settling anywhere between — $4.3$, $4.31$, $4.317\ldots$ — with no smallest step.

"Her power is a *quantity*," Misty whispers, watching the dial breathe. "Not a count. You can't list its values — there are too many, packed too tight. You can only ever ask how likely a *range* is."

A telepathic voice settles directly into your skull, calm and amused. *"My readings follow a curve, trainer. Tell me the chance my next reading lands in a band you choose, and I will let you challenge me. Fail, and the doll-dimension keeps you."*

Pikachu's cheeks spark — the intuition check. There's a wall chart of the dial's behavior, a smooth hump tailing off to either side, and a number printed beside its peak: **$f(2) = 0.27$.** "There!" you say. "The chance of a reading of $2$ is $0.27$." The dial flickers, *wrong*, and the floor lurches — because that number isn't a probability at all.

*The dial has no list of values to add up, and the curve's own height isn't a probability. So where does the probability even come from — and how do you read one off a smooth curve?*
:::

## Where You Are — 60-Second Retrieval

**Rank: Ace Trainer · Badges: 5 (Cascade, Thunder, Boulder, Rainbow, Soul).** Five badges ride in your case, and the load-bearing idea you carry into Saffron is the **discrete random variable** from the S.S. Anne. There, a quantity you couldn't predict was described by its **probability mass function** $p(x) = P(X=x)$ — a real probability sitting on each value, all of them summing to $1$, with the mean a *probability-weighted sum*:

$$\sum_x p(x) = 1, \qquad E[X] = \sum_x x\,p(x).$$

That world was **countable**: you could enumerate the values and *add up* their masses. Saffron breaks that. The dial's readings form an unbroken **continuum** — between any two values there is always another — so there is nothing to enumerate and nothing to add. The single move this entire chapter rests on is the pivot from *sum* to *area*: where the discrete world stacked bars and summed their heights, the continuous world draws a curve and measures the **area underneath it.** *Mass becomes area; the sum becomes an integral.* Everything below is that one idea, unfolded.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the discrete picture**

Answer from memory; if any feels shaky, flip back before reading on.

1. For a discrete $X$, what must $\sum_x p(x)$ equal, and why? *(Answer: $1$ — a complete list of disjoint outcomes carries all the probability.)*
2. Write $E[X]$ for a discrete $X$ as a sum. *(Answer: $\sum_x x\,p(x)$ — a probability-weighted average of the values.)*
3. In the discrete world, was $p(3) = P(X=3)$ a genuine probability? *(Answer: yes — a mass sitting on the single value $3$. Hold onto this; it is exactly what changes in Saffron.)*

All three instant? Good — every idea below is one of these, with the sum swapped for an integral. Any hesitation? Reclaim "$p(x)$ is a probability that sums to 1" first; the whole pivot is measured against it.
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP022 "Abra and the Psychic Showdown" + EP024 "Haunter Versus Kadabra"**

In **EP022** Ash reaches **Saffron City** and challenges **Sabrina**, the eerily powerful Psychic-type Gym Leader, whose mastery over a *continuous*, mind-bending reality (she even shrinks the heroes into a toy world) is the perfect skin for this chapter's smooth, gliding quantities — and whose **Kadabra** is our figure mascot, warping discrete bars into a flowing curve. Ash loses the first attempt and goes to find a Pokémon that can counter raw psychic power. In **EP024** he returns with a **Haunter**, and in the canonical beat that closes the arc, Haunter wins *not* by force but by making the unshakable Sabrina **laugh** — cracking her cold composure and earning the **Marsh Badge.** *Watch EP022 then EP024 right before this chapter* — the smooth psychic world and the Kadabra/Haunter showdown are the scenes the math lives in. (The wall-dial "density" and the doll-dimension wager are in-world extensions built to carry the math, not on-screen lines.)
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice crackles through the Pokédex's Actuary Mode as you stare at the gliding dial.

"Saffron is the *smooth* city, Ash. Everything you measure here — a time, a length, a temperature, a proportion of a loss — is **continuous**: it lives on a number line with no gaps, and a single exact value carries probability *zero*. That sounds strange the first time, but it is the gateway to almost all of actuarial science, where losses and waiting times are smooth quantities. Three ideas do the work. First, **probability is area** under a curve, not a sum of bars. Second, that curve is the **density** $f$, its accumulated area is the **cdf** $F$, and the two are linked by calculus — $F$ is the running total of $f$, and $f$ is the slope of $F$ — with any unknown constant pinned down by forcing the total area to $1$. Third, the real world is sometimes **mixed** — part smooth, part a lump of probability sitting on a single value, like an insurance payout that is *exactly zero* unless a loss occurs. This is a **Tier B** chapter; take it one idea at a time, and the rest of the continuous half of the exam stands on it."

By the end of this chapter you will be able to:

- **Read probability as area.** For a continuous $X$ with density $f$, compute $P(a\le X\le b)=\int_a^b f(x)\,dx$, explain why $P(X=c)=0$ and why endpoints never matter, and know that the density's *height* is a rate, not a probability (so $f(x)$ may exceed $1$). *(Outcome 2a.)*
- **Move fluently among the four faces of a continuous law** — the density $f$, the cdf $F(x)=\int_{-\infty}^x f$, the survival $S=1-F$, and band probabilities — using $f=F'$ and $F=\int f$, and **solve for a normalizing constant** by forcing total area to $1$. *(Outcome 2a.)*
- **Handle a mixed distribution** — part discrete (a **point mass** at a value) and part continuous (a density over a range) — reading its cdf as a *jump* of height equal to the mass followed by a smooth ramp, with all the probability totalling $1$. *(Outcome 2a.)*

> *Exam-weight signpost.* This is the doorway to **Univariate random variables, the single largest slice of Exam P (44–50%)** — every continuous distribution, moment, and pricing problem that follows reads a density or differences a cdf. The "area is probability" reflex and the normalize-first reflex are tested constantly, directly and as the hidden first step of harder problems. This is a **Tier B** chapter: full nine-beat teaching for each idea, with a gentler ramp than the Tier-A grounds, but every idea is reused downstream.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own the Smooth World?**

Already fluent with densities and cdfs? Prove it. Work these four, ~3 minutes each, *with correct method*:

1. A continuous $X$ has density $f(x)=\tfrac12$ on $0<x<2$ (and $0$ elsewhere). Find $P(X=1)$ and $P(0.5<X<1.5)$.
2. $f(x)=c\,x$ on $0<x<3$. Find $c$, then $P(X<2)$.
3. For $f(x)=2x$ on $0<x<1$, write the cdf $F(x)$ on $(0,1)$ and find $P(X>0.5)$.
4. A payout $Y$ is exactly $0$ with probability $0.4$, and otherwise uniform on $(0,4]$ with density $0.15$. Find $P(Y=0)$ and $P(Y\le 2)$.

*(Answers: $0$ and $0.5$; $c=\tfrac29$ and $P(X<2)=\tfrac49\approx0.44$; $F(x)=x^2$ and $P(X>0.5)=0.75$; $0.4$ and $0.4+0.15\cdot 2 = 0.7$.)* Four for four with the right reasoning? **Skip to the Gym Battle.** Any miss or hesitation? The teaching below was built exactly for you — and each idea has its own skip-gate, so even a partial owner loses no time.
:::

---

Three ideas build on one another here, in TIA order. We teach them **in order**, each with its own "do you already own this?" skip-check, then the full nine-beat lesson, then a Pokédex Entry you can carry into the exam.

1. **Continuous overview** — probability as **area**, and why a single point carries none *(the foundation everything uses)*
2. **Densities & CDFs** — the curve $f$, its running total $F$, the link $f=F'$, and the normalizing-constant solve
3. **Mixed distributions** — part smooth, part a lump: a point mass plus a continuous piece

## Concept 1 — The Continuous Overview: Probability Is Area

::: concept-gate
**DO YOU ALREADY OWN THIS? — Area vs. height**

A continuous $X$ has density $f(x) = \tfrac12$ on the interval $0 < x < 2$. What is $P(X = 1)$, and what is $P(0.5 < X < 1.5)$?

If you instantly said **$P(X=1) = 0$** (a single point has zero width, hence zero area) and **$P(0.5<X<1.5) = \tfrac12\cdot 1 = 0.5$** (area $=$ height $\times$ width), you own the foundation — **skip to Concept 2**. If "$P(X=1)=0$" surprised you, or you tried to read $f(1)=\tfrac12$ as a probability, this section is for you.
:::

**Beat 1 — The one-sentence idea.** *For a continuous variable, probability is not a number sitting on each value — it is the **area under a curve** over a range, and that curve is the density.*

**Beat 2 — Anchor + concrete instance.** On the S.S. Anne, a discrete $X$ had a *bar* of height $p(x)$ over each value, and a bar's height *was* its probability. Now picture Sabrina's dial, which can land *anywhere* in $0 < x < 2$, with no value preferred. There are infinitely many possible readings packed into that interval, so no single one can carry positive probability. Instead the probability is spread *smoothly* across the interval as a flat curve $f(x)$ of height $\tfrac12$.

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/64.png" alt="Kadabra, the psychic mascot that warps a discrete bar chart into a smooth continuous density curve" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#64 Kadabra — warps the countable bars into one smooth curve</strong></figcaption>
</figure>

**Beat 3 — Reason through it in plain words.** Ask: what's the chance the dial lands *exactly* on $1.000000\ldots$? Essentially impossible — it is one point out of an unbroken continuum, so $P(X=1)=0$. The right question is about a **band**: what's the chance it lands between $0.5$ and $1.5$? That band is $1$ unit wide, and the curve sits at height $\tfrac12$ across it, so the probability is the area of that rectangle:

$$\text{height}\times\text{width} = \tfrac12 \times 1 = 0.5.$$

Probability *is* that rectangle of area. And the whole interval $0<x<2$ has area $\tfrac12\times 2 = 1$ — as every probability total must.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The natural mistake, carried straight over from the discrete world, is to read **the height of the density as a probability** — exactly the slip the cold-open dial punished:

$$f(1) = \tfrac12 \;\overset{?}{=}\; P(X=1). \qquad\textbf{(wrong)}$$

It is *not*. A density can even **exceed $1$** — if $X$ is uniform on $(0, 0.5)$ the height is $\tfrac{1}{0.5}=2$, yet no probability is ever $2$ — which is the surest proof that a height is not a probability. The height is a *rate of probability per unit length*; only when you **multiply by a width** (integrate) does it become a probability. For a single point the width is $0$, so the probability is $0$. *Density is not probability; area is.* (This is the exact error Team Rocket walks into later — and the one the cold-open dial flickered at.)

**Beat 5 — Translate into notation, one glyph at a time.** Write the **probability density function** (pdf) as $f(x)$, read aloud *"the density of $X$ at $x$."* It must be non-negative everywhere and enclose total area $1$:

$$f(x) \ge 0, \qquad \int_{-\infty}^{\infty} f(x)\,dx = 1.$$

That $\displaystyle\int$ is the **integral sign**, read *"the integral of."* It is the continuous cousin of the summation $\sum$ from the S.S. Anne: where $\sum$ *adds up* values, $\int \ldots\,dx$ *accumulates area* under the curve, and the little $dx$ marks the variable you sweep across. The probability of a band is the integral over that band:

$$P(a < X < b) = \int_a^b f(x)\,dx \qquad \text{read: ``the area under } f \text{ from } a \text{ to } b\text{.''}$$

**Beat 6 — Derive the endpoint fact from the instance.** Nothing here is asserted; it falls out of "probability is area." Because a single point $\{c\}$ has zero width, its area — and so its probability — is $0$:

$$P(X=c) = \int_c^c f(x)\,dx = 0.$$

That single fact has a clean consequence: **including or excluding an endpoint never changes a continuous probability**, because the endpoint contributes zero area. So

$$P(a < X < b) = P(a \le X \le b) = P(a \le X < b) = P(a < X \le b).$$

(In the discrete world this was false — a mass *did* sit on each endpoint — and that contrast is a genuine, testable difference between the two worlds. Watch for it: a problem that hinges on $<$ versus $\le$ is testing whether you know which world you are in.)

**Beat 7 — Ramp the difficulty.**

- *Simplest:* a flat density, area $=$ height $\times$ width, as above — $P(0.5<X<1.5)=0.5$.
- *Twist (a curved density):* if $f(x)=2x$ on $(0,1)$, the region under it is no longer a rectangle, so you must integrate: $P(X<\tfrac12)=\int_0^{1/2}2x\,dx = \big[x^2\big]_0^{1/2}=\tfrac14$. The taller right side means values near $1$ are more likely.
- *General (a band of a curve):* for that same $f=2x$, $P(0.3<X<0.6)=\big[x^2\big]_{0.3}^{0.6}=0.36-0.09=0.27$ — a difference of two accumulated areas.
- *Edge (height above 1):* uniform on $(0,0.5)$ has $f=2>1$ everywhere, yet $P(0<X<0.5)=2\times 0.5 = 1$. A tall, narrow density is perfectly legal — only the *area* is capped at $1$.

**Beat 8 — Picture it.** The countable bars warp into a smooth curve; a band's probability is the shaded area beneath it, and the whole area is $1$.

<figure>
<img src="../../assets/diagrams/ch09_pdf_area.png" alt="Two panels. Left: a discrete bar chart whose bars echo a smooth red curve drawn over them, captioned that countable bars warp into a continuous density; a Kadabra sprite sits in the clear upper-left margin. Right: the smooth density curve with the region between a and b shaded by diagonal hatching and labelled P(a<X<b) equals the integral of f from a to b; an arrow notes that the whole area under the curve integrates to 1, and a note warns that the density height is a rate that can exceed 1 while only area is a probability." style="width:90%; max-width:760px; display:block; margin:1em auto;">
<figcaption>Probability is area. A band's chance is the shaded region under the density $f$ (here $P(a<X<b)=\int_a^b f$); the whole area is $1$. The curve's <em>height</em> is a rate per unit length — it may exceed $1$ — and is never itself a probability.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now read any continuous probability as an **area**: integrate the density over a band, total area is $1$, a single point carries $0$, and endpoints never matter. The density's height is a rate, not a probability. Every named continuous curve in the chapters ahead is just a specific choice of $f$.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Continuous Probability Is Area**

$$f(x)\ge 0,\quad \int_{-\infty}^{\infty} f(x)\,dx = 1, \qquad P(a<X<b)=\int_a^b f(x)\,dx.$$
$$P(X=c)=0 \;\Longrightarrow\; P(a<X<b)=P(a\le X\le b)\ \text{(endpoints don't matter).}$$

*In plain terms:* a continuous variable spreads its probability *smoothly* as area under the density $f$. The height $f(x)$ is a rate of probability per unit length — it can exceed $1$ — and only **area** (an integral over a range) is a probability.

*Recognition cue:* a smooth quantity ("a time / length / temperature / proportion"), "density $f(x)=\ldots$," or "find $P(a<X<b)$" → integrate the density over the band; a single point or a $<$-vs-$\le$ distinction → recall it carries zero probability.
:::

## Concept 2 — Densities & CDFs: $f = F'$ and the Normalizing Constant

::: concept-gate
**DO YOU ALREADY OWN THIS? — The $f \leftrightarrow F$ machinery**

A density is $f(x)=c\,x$ on $0<x<3$ (and $0$ elsewhere). Find the constant $c$, the cdf $F(x)$ on $(0,3)$, and $P(X<2)$.

If you instantly set $\int_0^3 c\,x\,dx = \tfrac{9c}{2}=1$ to get **$c=\tfrac29$**, then **$F(x)=\tfrac{x^2}{9}$** and **$P(X<2)=F(2)=\tfrac49\approx 0.44$**, you own the machinery — **skip to Concept 3**. If you computed a probability *before* solving for $c$, or weren't sure how $f$ and $F$ connect, read on.
:::

**Beat 1 — The one-sentence idea.** *The cdf $F$ is the running total of the density's area, the density $f$ is the slope of that running total ($f=F'$), and any unknown constant in $f$ is pinned down by forcing the total area to $1$.*

**Beat 2 — Anchor + concrete instance.** Concept 1 gave you band probabilities as areas. Now we name the *running total* of that area and tie it back to the curve. Take Sabrina's dial with a sloped density $f(x)=c\,x$ on $0<x<3$ — readings near $3$ more likely than readings near $0$, a triangle of probability. Two questions: what is $c$, and what is the chance of a reading below $2$?

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/64.png" alt="Kadabra, the psychic mascot, here accumulating the density's area into the cumulative distribution function" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#64 Kadabra — sweeps up the area into the running total $F$</strong></figcaption>
</figure>

**Beat 3 — Reason through it in plain words.** First, **normalize.** A density is only valid if its total area is $1$, and that requirement *is* the equation that pins down $c$: the triangle under $c\,x$ over $(0,3)$ must have area $1$. Solve it, and $c$ is fixed. Only *then* can you ask for a probability. The chance of "a reading below $2$" is the area swept from the left up to $2$ — and that running, swept-up area, as a function of where you stop, is exactly what we call the **cdf** $F$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The canonical trap is to **compute a probability before normalizing** — to treat the bare formula $c\,x$ as if $c$ were already known (or to ignore it):

$$P(X<2) \overset{?}{=} \int_0^2 x\,dx = 2. \qquad\textbf{(wrong — } c \text{ never solved, and a probability can't be } 2\text{)}$$

The instant a density carries an unknown constant, your *first* move is the normalizing equation, never the question asked. Every probability you write before $c$ is solved is wrong — and a "probability" of $2$ is the loud sign you skipped the step.

**Beat 5 — Translate into notation, one glyph at a time.** The **cumulative distribution function** (cdf), written $F(x)$ and read *"the cdf of $X$,"* is the area swept up *to* a point:

$$F(x) = P(X \le x) = \int_{-\infty}^{x} f(t)\,dt \qquad \text{read: ``all the area to the left of } x\text{.''}$$

Because differentiating undoes integrating, the density is the **slope** of the cdf:

$$f(x) = F'(x) \qquad \text{read: ``the density is how fast the cdf is climbing.''}$$

And the **survival function** $S(x)=P(X>x)=1-F(x)$ is everything to the *right* (the continuous twin of the discrete survival from the S.S. Anne). The **normalizing constant** is whatever value of the unknown makes $\int f = 1$ — read it as *"the height-scaler that forces the total area to one."*

**Beat 6 — Derive everything from the instance.** Take $f(x)=c\,x$ on $0<x<3$. Force the total area to $1$:

$$\int_0^3 c\,x\,dx = c\Big[\tfrac{x^2}{2}\Big]_0^3 = c\cdot\tfrac{9}{2} = 1 \;\Longrightarrow\; \boxed{\,c=\tfrac{2}{9}\,}.$$

Now the cdf is the running total of that normalized density:

$$F(x) = \int_0^x \tfrac{2}{9}\,t\,dt = \tfrac{2}{9}\Big[\tfrac{t^2}{2}\Big]_0^x = \frac{x^2}{9}, \qquad 0\le x\le 3,$$

with $F(x)=0$ below $0$ and $F(x)=1$ above $3$. Check the link in both directions: differentiate the cdf and you recover the density, $F'(x)=\tfrac{2x}{9}=f(x)$ ✓; and $F(3)=\tfrac{9}{9}=1$ ✓, so all the area is accounted for. Finally the question asked: $P(X<2)=F(2)=\tfrac{4}{9}\approx 0.44$ — a real probability, safely in $[0,1]$. Three facts, one triangle: $f$ is the slope, $F$ is the accumulated area, and the normalizer ties them to total $1$.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* differencing the cdf — for any $F$, $P(a<X<b)=F(b)-F(a)$, no integration needed once you have $F$.
- *Twist (normalize, then ask):* $f(x)=k(1-x)$ on $(0,1)$. Area $\int_0^1 k(1-x)\,dx = k\cdot\tfrac12 = 1$, so $k=2$; then $P(X<\tfrac12)=\int_0^{1/2}2(1-x)\,dx = \big[2x-x^2\big]_0^{1/2}=\tfrac34$.
- *General (go backward, $f=F'$):* given a cdf $F(x)=1-e^{-x/4}$ for $x>0$, differentiate to get the density $f(x)=F'(x)=\tfrac14 e^{-x/4}$ — recovering the curve from its running total.
- *Edge (a kink in $F$):* a density that jumps (say $f=\tfrac13$ on $(0,1)$ then $\tfrac{2}{3}$... — any piecewise $f$) gives a cdf that is continuous but **bends** where $f$ changes; $F$ is always continuous for a purely continuous $X$, with no vertical jumps. (Jumps are the signature of the *next* concept.)

**Beat 8 — Picture it.** The density and the cdf are two views of one law: the cdf's shaded area-to-the-left at $x_0$ is the *value* $F(x_0)$ below, and the cdf's *slope* at $x_0$ is the density's height $f(x_0)$ above.

<figure>
<img src="../../assets/diagrams/ch09_cdf_from_pdf.png" alt="Two stacked panels sharing an x-axis. Top: a smooth density curve f with the area to the left of a marked point x-zero shaded by diagonal hatching and labelled as F of x-zero, the integral of f up to x-zero; a Kadabra sprite sits in the clear upper-right margin. Bottom: the cumulative distribution function F rising smoothly from 0 to 1, with a red tangent line drawn at x-zero whose slope is labelled f of x-zero, illustrating that f equals F prime; a dashed line marks F equals 1 where all the area is accumulated." style="width:88%; max-width:720px; display:block; margin:1em auto;">
<figcaption>The cdf $F$ (bottom) is the running total of the density's area: $F(x_0)$ is the shaded left-area in the top panel. Running it the other way, the <em>slope</em> of $F$ at any point is the density there — $f(x)=F'(x)$. $F$ climbs from $0$ to $1$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can move freely among the four faces of a continuous law — $f$ (density / slope), $F$ (left area / running total), $S=1-F$ (right area), and a band probability $F(b)-F(a)$ — using $f=F'$ and $F=\int f$. And the instant a density carries an unknown, you solve $\int f = 1$ *first*, then answer.

::: pokedex-entry
**POKÉDEX ENTRY №02 — Density, CDF, Survival & the Normalizing Constant**

$$F(x)=P(X\le x)=\int_{-\infty}^{x} f(t)\,dt,\qquad f(x)=F'(x),\qquad S(x)=P(X>x)=1-F(x).$$
$$P(a<X<b)=\int_a^b f = F(b)-F(a);\qquad \text{unknown constant: solve } \int_{-\infty}^{\infty} f = 1.$$

*In plain terms:* the cdf accumulates the density's area from the left; the density is the cdf's slope. To find a band probability, integrate $f$ or difference $F$. To find an unknown constant in $f$, force the total area to $1$ and solve — always *before* computing any probability.

*Recognition cue:* "$f(x)=c\,\ldots$" or "$f(x)=k\,\ldots$" with an unknown letter → normalize first ($\int f =1$). "Given the cdf $F$, find the density" → differentiate ($f=F'$). "Given $f$, find $F$ or a probability" → integrate.
:::

## Concept 3 — Mixed Distributions: A Point Mass Plus a Continuous Part

::: concept-gate
**DO YOU ALREADY OWN THIS? — Mixed laws**

An insurance payout $Y$ is **exactly $0$** with probability $0.4$ (no loss occurs), and *otherwise* spreads uniformly over $(0,4]$ with density $0.15$. Find $P(Y=0)$, confirm the total probability is $1$, and find $P(Y\le 2)$.

If you instantly said **$P(Y=0)=0.4$** (a genuine point mass), saw that the continuous part carries $0.15\times 4 = 0.6$ so the total is $0.4+0.6=1$ ✓, and computed **$P(Y\le 2)=0.4 + 0.15\times 2 = 0.7$** (the mass *plus* the area up to $2$), you own mixed laws — **skip to the Gym Battle**. If a point having positive probability inside a "continuous" problem threw you, read on.
:::

**Beat 1 — The one-sentence idea.** *A mixed distribution is part discrete and part continuous: a lump of probability — a **point mass** — sits on one value, while the rest is spread smoothly as a density, and together they total $1$.*

**Beat 2 — Anchor + concrete instance.** Concepts 1 and 2 lived in a purely smooth world where every single point had probability $0$. But the real quantities an actuary prices are often *not* purely smooth. Sabrina's most actuarial creation is the clearest case: an **insurance payout** $Y$. Most policies pay *exactly nothing* — a sizable lump of probability sits on the single value $0$ — and pay a smooth, continuous amount *only when* a loss actually occurs. Say $P(Y=0)=0.4$ (no loss), and otherwise $Y$ is uniform on $(0,4]$ with density $0.15$. This is **mixed**: neither purely discrete nor purely continuous.

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/64.png" alt="Kadabra, the psychic mascot, presiding over a mixed law that is part lump and part smooth" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#64 Kadabra — half lump, half curve: the mixed law</strong></figcaption>
</figure>

**Beat 3 — Reason through it in plain words.** Add up where the probability lives. A chunk of size $0.4$ sits *on the single point* $0$ — a real, positive probability on one value, exactly like a discrete mass. The remaining $0.6$ is spread *smoothly* over $(0,4]$: a flat density of height $0.15$, whose area is $0.15\times 4 = 0.6$. The two pieces sum to $0.4+0.6=1$, as they must. So $Y$ is genuinely *both* — a discrete spike welded onto a continuous slab.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two opposite slips lurk here. The first is to insist, from Concept 1, that *every* point has probability $0$, and so report $P(Y=0)=0$:

$$P(Y=0) \overset{?}{=} 0. \qquad\textbf{(wrong — } Y \text{ is not purely continuous; a real mass sits at } 0\text{)}$$

The second is to **double-count or mis-add** the pieces when you want a cumulative probability — forgetting to include the lump. The fix is to keep the two parts separate and *add* them: a point mass contributes its full lump, the continuous part contributes its area. To get $P(Y\le 2)$ you take the mass at $0$ **plus** the continuous area from $0$ to $2$:

$$P(Y\le 2) = \underbrace{P(Y=0)}_{0.4} + \underbrace{\int_0^2 0.15\,dy}_{0.15\times 2\,=\,0.30} = 0.70.$$

**Beat 5 — Translate into notation, one glyph at a time.** A mixed law is described by listing its **point masses** $P(X=c_i)$ and its **continuous density** $f(x)$ on the rest. Its cdf still means the same thing — $F(x)=P(X\le x)$ — but it now has both a *smooth* part and *jumps*: at each point mass $c$, the cdf **jumps** by exactly that mass,

$$F(c) - F(c^-) = P(X=c) \qquad \text{read: ``the cdf leaps up by the lump at } c\text{.''}$$

Everything must still total $1$: $\sum_i P(X=c_i) + \int f(x)\,dx = 1$ (masses plus area). A general probability splits the same way — *masses that qualify, plus the integral over the qualifying band.*

**Beat 6 — Derive the cdf from the instance.** Build $F$ for our payout $Y$ piece by piece, left to right. Below $0$ there is no probability yet, so $F(y)=0$ for $y<0$. **At $y=0$** the point mass lands, so $F$ jumps from $0$ up to $0.4$: $F(0)=0.4$. On $(0,4]$ the continuous part accumulates its flat density on top of the lump:

$$F(y) = 0.4 + \int_0^y 0.15\,dt = 0.4 + 0.15\,y, \qquad 0\le y\le 4.$$

At $y=4$ this reaches $0.4 + 0.15\times 4 = 1.0$ ✓ — all the probability accounted for — and stays $1$ above. So the cdf is a **jump of height $0.4$ at $0$, then a straight ramp up to $1$.** Reading the worked question off it: $P(Y\le 2)=F(2)=0.4+0.15\times 2 = 0.70$ ✓, matching Beat 4. The jump *is* the discrete part; the ramp *is* the continuous part.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* read a mass directly — $P(Y=0)=0.4$, the height of the cdf's jump.
- *Twist (a band that includes the mass):* $P(0\le Y\le 1) = 0.4 + 0.15\times 1 = 0.55$ (lump plus area); but $P(0 < Y \le 1) = 0.15\times 1 = 0.15$ (area *only* — the strict $<$ excludes the mass at $0$). Here the $<$-vs-$\le$ distinction *matters again*, because a real mass sits at the endpoint.
- *General (mass not at the boundary):* a mass can sit anywhere — e.g. a capped payout that lumps probability at the policy limit $u$, so $P(Y=u)>0$ while $Y$ is continuous below $u$. The cdf jumps at $u$.
- *Edge (total check):* always confirm $\sum$ masses $+\int f = 1$. If a problem gives a mass $p_0$ at $0$ and a density on $(0,m)$, the density's area must be $1-p_0$ — a one-line sanity check that catches a mis-specified law.

**Beat 8 — Picture it.** The density picture is a *spike* (the point mass) standing beside a smooth slab (the continuous density); the cdf is a *jump* of that mass's height followed by a smooth climb to $1$.

<figure>
<img src="../../assets/diagrams/ch09_mixed_dist.png" alt="Two panels. Left: the density picture of a mixed law — a tall red arrow spike at x=0 labelled as the point mass P(X=0)=0.40, standing beside a flat blue density of height 0.15 over the interval (0,4] whose area 0.15 times 4 equals 0.60 is labelled; a Kadabra sprite sits in the clear upper-right corner. Right: the corresponding cdf, which is 0 to the left of 0, jumps vertically by 0.40 at x=0 (the point mass), then ramps smoothly upward as a straight line to reach 1 at x=4 and stays flat at 1 afterward; the jump and the ramp are each annotated." style="width:90%; max-width:760px; display:block; margin:1em auto;">
<figcaption>A mixed law (left): a probability <em>spike</em> of height $0.40$ at $0$ (the point mass) plus a continuous density of height $0.15$ on $(0,4]$ carrying area $0.60$ — total $1$. Its cdf (right) <em>jumps</em> by $0.40$ at the mass, then <em>ramps</em> smoothly to $1$: the jump is the discrete part, the ramp the continuous part.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can recognize a mixed law — a lump of probability on a value plus a density on the rest — read its cdf as a jump (height $=$ the mass) followed by a smooth ramp, and compute any probability by *adding* the qualifying masses to the integral over the qualifying band, with the whole thing totalling $1$.

::: pokedex-entry
**POKÉDEX ENTRY №03 — Mixed Distributions**

$$\sum_i P(X=c_i) + \int f(x)\,dx = 1; \qquad F(c)-F(c^-) = P(X=c)\ \text{(the cdf jumps by the mass).}$$
$$P(X\le t) = \!\!\sum_{c_i \le t}\!\! P(X=c_i) \;+\; \int_{-\infty}^{t} f(x)\,dx \quad(\text{masses + area}).$$

*In plain terms:* part discrete, part continuous. A **point mass** carries real probability on one value (so $P(X=c)>0$ there); the continuous part carries area. The cdf has a *jump* at each mass and a smooth ramp elsewhere. Always add the masses and the area; check they total $1$.

*Recognition cue:* "exactly $0$ with probability $p$, otherwise continuous," "a lump at the deductible / limit," a cdf with a vertical jump → a mixed law. Keep the mass and the integral as *separate* pieces, and mind $<$ vs $\le$ at a mass.
:::

## Worked Examples — Faded Guidance

Four examples, fading from fully narrated to exam-speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because normalizing-then-integrating is where the points live.

### Worked Example 1 — The Dial's Triangle (full narration; normalize, then read $f$, $F$, and a probability)

**ARCHETYPE:** *Solve a normalizing constant, build the cdf, read a band probability.*

**Setup.** Sabrina's dial has density $f(x)=c\,x$ on $0<x<3$ (and $0$ elsewhere). Find (a) $c$; (b) the cdf $F(x)$ on $(0,3)$; (c) $P(1<X<2)$; (d) $P(X=2)$.

**Step 1 — Identify.** A density with an unknown constant → *normalize first* ($\int f =1$), then everything else is bookkeeping.

**Step 2 — Professor's Path (the why).** A density is valid only if its total area is $1$, and that requirement is the equation for $c$:

$$\int_0^3 c\,x\,dx = c\Big[\tfrac{x^2}{2}\Big]_0^3 = \tfrac{9c}{2} = 1 \;\Longrightarrow\; c=\tfrac{2}{9}.$$

The cdf is the running total of the now-normalized density: $F(x)=\int_0^x \tfrac{2}{9}t\,dt = \tfrac{x^2}{9}$ on $[0,3]$. Then the band probability is a difference of accumulated areas, $P(1<X<2)=F(2)-F(1)=\tfrac{4}{9}-\tfrac{1}{9}=\tfrac{3}{9}=\tfrac13$. And $P(X=2)=0$: a single point in a purely continuous law carries no area.

**Step 3 — Trainer's Path (the fast how).** Normalize: triangle area $\tfrac12\cdot 3\cdot(3c)=\tfrac{9c}{2}=1\Rightarrow c=\tfrac29$. cdf $=\tfrac{x^2}{9}$. Band $=F(2)-F(1)=\tfrac{4-1}{9}=\tfrac13$. Point $=0$.

**Step 4 — Check & pitfall.** $F(3)=\tfrac{9}{9}=1$ ✓ (all area accounted for); $f=F'=\tfrac{2x}{9}$ ✓. **Pitfall:** integrating for $P(1<X<2)$ *before* solving for $c$ — every probability is wrong until the density is normalized. *(Back-ref: Entries №01, №02.)*

### Worked Example 2 — From CDF Back to Density (full narration; $f=F'$, and a survival)

**ARCHETYPE:** *Differentiate a cdf to recover the density; read a survival probability.*

**Setup.** A psychic reading has cdf $F(x)=1-e^{-x/4}$ for $x\ge 0$ (and $0$ below). Find (a) the density $f(x)$; (b) $P(X>4)$; (c) confirm $f$ integrates to $1$.

**Step 1 — Identify.** Given the cdf, "find the density" → differentiate ($f=F'$). "Find $P(X>4)$" → that's the survival $S(4)=1-F(4)$.

**Step 2 — Professor's Path (the why).** The density is the slope of the cdf:

$$f(x)=F'(x)=\frac{d}{dx}\big(1-e^{-x/4}\big)=\tfrac{1}{4}e^{-x/4}, \qquad x\ge 0.$$

The survival is everything to the right: $P(X>4)=S(4)=1-F(4)=e^{-4/4}=e^{-1}\approx 0.3679$. And the area check: $\int_0^\infty \tfrac14 e^{-x/4}\,dx = \big[-e^{-x/4}\big]_0^\infty = 0-(-1)=1$ ✓.

**Step 3 — Trainer's Path (the fast how).** $f=F'=\tfrac14 e^{-x/4}$ on sight. $P(X>4)=1-F(4)=e^{-1}\approx 0.368$. Area is $1$ because $F(\infty)=1$.

**Step 4 — Check & pitfall.** $F(0)=0$, $F(\infty)=1$, and $f\ge 0$ ✓ — a valid law. **Pitfall:** computing $P(X>4)$ as $F(4)$ instead of $1-F(4)$ — the survival is the *right* tail. *(Back-ref: Entry №02. You will meet this exact curve named — the exponential — in Chapter 11.)*

### Worked Example 3 — The Capped Payout (light guidance; a mixed law)

**ARCHETYPE:** *Mixed distribution — a point mass plus a continuous part; total-probability check and a cumulative read.*

**Setup.** A payout $Y$ is **exactly $0$** with probability $0.4$, and otherwise has density $f(y)=c$ (flat) on $(0,4]$. Find (a) $c$; (b) $P(Y\le 2)$; (c) $P(0<Y\le 2)$.

**Identify.** A lump at one value plus a smooth piece → mixed. The masses and the area must total $1$. *Your move: pin down $c$ from the total, then split each probability into mass-plus-area.*

The continuous part must carry the leftover probability $1-0.4=0.6$ over a width-$4$ band, so $c\times 4 = 0.6 \Rightarrow c=0.15$. Then

$$P(Y\le 2) = \underbrace{P(Y=0)}_{0.4} + \underbrace{\int_0^2 0.15\,dy}_{0.30} = 0.70, \qquad P(0<Y\le 2)=\int_0^2 0.15\,dy = 0.30.$$

**Check & pitfall.** Total $=0.4 + 0.15\times 4 = 1$ ✓. **Pitfall:** the two answers differ only because the strict $0<Y$ **excludes the mass at $0$** — at a point mass, $<$ vs $\le$ matters (unlike the purely continuous world). *(Back-ref: Entry №03.)*

### Worked Example 4 — Density Above One (exam-speed; height is not probability)

**ARCHETYPE:** *Read a density whose height exceeds $1$; only area is a probability.*

**Setup.** $X$ has density $f(x)=2$ on $0<x<0.5$ (and $0$ elsewhere). Is this a valid density? Find $P(X<0.25)$ and $P(X=0.25)$.

**Solution.** Valid: $f\ge 0$ and the area is $2\times 0.5 = 1$ ✓ — even though the *height* $2$ exceeds $1$. The probability is an area: $P(X<0.25)=2\times 0.25 = 0.5$. A single point carries none: $P(X=0.25)=0$.

**Check & pitfall.** Area $=1$, so it's a legal law. **Pitfall:** declaring $f(x)=2$ "impossible because a probability can't exceed $1$" — a density is a *rate*, not a probability, and may exceed $1$; only the integral is capped at $1$. *(Back-ref: Entry №01.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — Normalize first; only area is a probability**

Two reflexes win most density problems before the real work starts:

- **See an unknown constant ($c$, $k$) in a density? Your first keystroke is $\int f = 1$.** Solve for the constant, *then* answer the question. Every probability computed before normalizing is wrong. A "probability" that comes out above $1$ (or a density you read as a probability) is the alarm that you skipped the step.
- **A height is never a probability.** $f(x)$ is probability *per unit length* and can exceed $1$. Only an **area** — a height times a width, i.e. an integral over a range — is ever a probability. For a single point the width is $0$, so $P(X=c)=0$ for a purely continuous $X$.

And one move that saves time on the exam: if you already have the **cdf** $F$, don't integrate again — a band is just $P(a<X<b)=F(b)-F(a)$, and the right tail is $S(x)=1-F(x)$. Carry $f$, $F$, and $S$ as three views of one law and reach for whichever the problem hands you.
:::

## Team Rocket's Trap

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket — Jessie, James, and Meowth, about to misread a continuous density's height as a probability" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Team Rocket — about to read a density's height as a probability</figcaption>
</figure>

::: team-rocket
**TEAM ROCKET'S TRAP**

Team Rocket has stolen a "psychic loss curve" for their next scheme — a density $f(x)=c\,x$ on $0<x<3$ — and they want the chance a reading lands below $2$.

**James** skips straight to the question: *"Forget the $c$! The chance it's under $2$ is just $\int_0^2 x\,dx = \tfrac{x^2}{2}\big|_0^2 = 2$. A two-hundred-percent chance — we can't lose, nyah-ha!"*

**Jessie** snatches the curve and squints at its peak: *"And look — the curve sits at height $f(3)=3c$. So the probability of a reading of *exactly* $3$ is $3c$ — the most likely outcome by far!"*

Both are wrong, in the two canonical continuous ways. James **computed a probability before solving for the normalizing constant** — and got a "$2$," which is the dead giveaway: no probability exceeds $1$. The fix is two steps he skipped: first force the total area to $1$, $\int_0^3 c\,x\,dx=\tfrac{9c}{2}=1\Rightarrow c=\tfrac29$; *then* integrate, $P(X<2)=\int_0^2 \tfrac29 x\,dx = \tfrac29\cdot 2 = \tfrac49\approx 0.44$. And Jessie **read a density's height as a probability** — but $f(3)$ is a *rate* per unit length, not a chance, and $P(X=3)=0$ for any continuous variable, because a single point has zero width. *One-line fix:* normalize *before* you integrate, and remember density is probability *per unit length* — only an **area** is ever a probability.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

Densities and cdfs are the actuary's native language for **loss size**. A claim amount is a smooth, continuous quantity, and a **loss-size density** $f(x)$ is exactly how its risk is described — the chance a loss falls in a band is the area under $f$ over that band, and the cdf $F$ answers "what fraction of losses are below this threshold?" The **mixed distribution** is not a curiosity but the everyday shape of an insurance **payout**: a large lump of probability sits on *exactly $0$* (most policies pay nothing in a given period), with a continuous severity *only when* a loss occurs — and a policy limit puts a second mass right on the cap. Reading that payout means doing precisely what this chapter taught: keep the point mass and the continuous area as separate pieces and add them. *Series bridge:* every continuous family you meet next — uniform, exponential, gamma, beta, normal — is just a named choice of $f$, and the mixed-payout picture is the seed of the **deductible/limit** pricing in Chapter 13 and of the severity models on **Loss Models (STAM / CAS Exam 5)**. Own "area is probability" and "normalize first" now, and the rest of the continuous world is reading off the same curve.
:::

## The Gym Battle — Marsh Badge Capstone

<figure style="display:flex; gap:18px; flex-wrap:wrap; justify-content:center; align-items:flex-end; margin:1.5em auto;">
<figure style="margin:0; text-align:center;">
<img src="../../assets/vs/sabrina.png" alt="Sabrina, the Saffron City Gym Leader, master of Psychic-type Pokemon" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;"><strong>Sabrina</strong> — Saffron's Psychic Gym Leader</figcaption>
</figure>
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/93.png" alt="Haunter, the Ghost-type Pokemon Ash brings to counter Sabrina, who wins by making her laugh" style="width:120px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;"><strong>#93 Haunter</strong> — wins by making Sabrina laugh</figcaption>
</figure>
</figure>

**Sabrina's Challenge.** The doll-dimension folds away and Sabrina faces you, unsmiling, a smooth psychic dial glowing between you. *"You came back with a Ghost,"* she says flatly — and behind you Haunter is already pulling faces, the canonical beat that will crack her composure into a *laugh* and win the day. *"But first, read my curve, trainer."* She projects a payout law onto the air:

> A psychic-feedback payout $Y$ is **exactly $0$** with probability $0.5$ (the reading is calm — no feedback). Otherwise — with probability $0.5$ — the feedback amount is continuous on $(0,2]$ with density $f(y)=k\,y$. *"Find $k$. Then tell me the chance the payout is at most $1$, and the chance it lands strictly between $0$ and $1$. Confuse a height for a probability, or lose my point mass, and the doll-dimension keeps you."*

**ARCHETYPE:** *Mixed law — normalize the continuous part against the leftover probability, then split a cumulative probability into mass-plus-area, minding $<$ vs $\le$.*

**Step 1 — Identify.** A lump at $0$ plus a *sloped* continuous part → mixed. The continuous piece must carry the leftover probability $0.5$, which is what pins down $k$. Then each probability is "qualifying mass $+$ qualifying area."

**Step 2 — Professor's Path (normalize the continuous part).** The mass at $0$ is $0.5$, so the continuous density on $(0,2]$ must carry the remaining $0.5$ of probability — that requirement is the equation for $k$:

$$\int_0^2 k\,y\,dy = k\Big[\tfrac{y^2}{2}\Big]_0^2 = 2k = 0.5 \;\Longrightarrow\; k=0.25.$$

Check the total: mass $0.5 +$ area $2(0.25)=0.5$, summing to $1$ ✓.

**Step 3 — Trainer's Path (split mass-plus-area).** For "at most $1$," take the mass at $0$ **plus** the continuous area up to $1$:

$$P(Y\le 1) = \underbrace{P(Y=0)}_{0.5} + \int_0^1 0.25\,y\,dy = 0.5 + 0.25\Big[\tfrac{y^2}{2}\Big]_0^1 = 0.5 + 0.125 = 0.625.$$

For "strictly between $0$ and $1$," the strict $0<Y$ **excludes the mass at $0$**, so it's area only:

$$P(0<Y<1) = \int_0^1 0.25\,y\,dy = 0.125.$$

| Quantity | Value | Why |
|---|---|---|
| $k$ | $0.25$ | continuous part carries leftover $0.5$: $2k=0.5$ |
| $P(Y\le 1)$ | $0.625$ | mass $0.5$ **+** area $0.125$ |
| $P(0<Y<1)$ | $0.125$ | area only — strict $<$ drops the mass |

**Step 4 — Check, verdict & the pitfall Sabrina is testing.** Total probability is $1$ ✓; both answers lie in $[0,1]$ ✓; and $P(Y\le1)-P(0<Y<1)=0.5$ recovers exactly the point mass at $0$ ✓. **Verdict:** $k=0.25$, $P(Y\le 1)=0.625$, $P(0<Y<1)=0.125$. The pitfall Sabrina probes is the **two opposite mixed-law errors at once** — losing the point mass (reporting $P(Y\le1)=0.125$) *or* mistaking the density's height for a probability. Keep the lump and the area as separate pieces, and watch $<$ versus $\le$ at the mass.

> Sabrina's unblinking stare finally breaks — not at your math, but at Haunter's antics behind you — and she *laughs*, the cold psychic air warming all at once. *"...You read the curve, and you made me feel,"* she says, pressing the **Marsh Badge** into your hand. *"Both are harder than they look."*

## The Gym Challenge — Problem Set

::: problem-set
**THE SAFFRON DIAL & SABRINA'S GYM — your questline.** Sabrina has set you one escalating mission through Saffron's smooth world: first the **Route Trainer** legs (reading densities and cdfs, warming up the area-is-probability tools), then the **Gym Battle** tier (the boss fight — full normalize-then-integrate and mixed-law problems at exam difficulty), then the optional **Elite Challenge** post-game. Work it timed (~6 min/problem), then check the **Answers** below. Hit the mastery bar (**80%+ with correct method**) to clear the questline and claim the Marsh Badge. Problems are listed first; full worked solutions follow afterward. Markers: 🔴 routine method · 🟡 routine-with-a-twist · 🔵 stretch.

Each problem is numbered C9.k, archetype-tagged, and mirrors `problems/bank.d/ch09.yaml`. Each restates whatever it needs, so you can work them in any order.

### Route Trainers (the early legs — reading curves, warming up)

**C9.1.** 🔴 *(The dial reads a flat band — area is probability.)* A continuous $X$ has density $f(x)=\tfrac12$ on $0<x<2$. Find $P(0.5<X<1.5)$ and $P(X=1)$.

**C9.2.** 🔴 *(Normalize a sloped density.)* $f(x)=c\,x$ on $0<x<3$. Find $c$, then $P(X<2)$.

**C9.3.** 🟡 *(Build the cdf, then difference it.)* For $f(x)=2x$ on $0<x<1$, write $F(x)$ on $(0,1)$ and find $P(0.3<X<0.6)$.

**C9.4.** 🔴 *(Go backward: $f=F'$.)* A reading has cdf $F(x)=1-e^{-x/5}$ for $x\ge 0$. Find the density $f(x)$ and $P(X>5)$.

**C9.5.** 🟡 *(A first mixed law.)* A payout $Y$ is exactly $0$ w.p. $0.3$, otherwise uniform on $(0,5]$ with density $0.14$. Confirm the law totals $1$, then find $P(Y\le 5)$ and $P(Y=0)$.

**C9.6.** 🔴 *(AUDIT — catch the height-as-probability slip.)* A note claims that for $X\sim$ density $f(x)=\tfrac12$ on $(0,2)$, "$P(X=1)=f(1)=0.5$." State the true $P(X=1)$ and name the error.

**C9.7.** 🔴 *(DECISION — which world are you in?)* You must report $P(X<2)$ for two different variables: (i) a continuous $X$ with cdf $F$, and (ii) a discrete $X$ with a mass at $2$. For which does it matter whether you wrote $<$ or $\le$, and why?

> *Questline beat: the dial reads clean and your area-tools are warm. Sabrina is waiting at the gym. The boss fights begin.*

### Gym Battles (the boss fight — true SOA difficulty)

<figure style="margin:1.2em auto; max-width:150px; text-align:center;">
<img src="../../assets/vs/blue.png" alt="Gary Oak, the rival, smirking — he is about to skip the normalizing constant and misread a density height" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Gary's lying in wait — C9.11 and C9.14 are his rival-traps (a skipped normalizer, a density read as a probability).</figcaption>
</figure>

**C9.8.** 🟡 *(Normalize, cdf, band, point.)* $f(x)=c\,x$ on $0<x<4$. Find $c$, the cdf $F(x)$, $P(1<X<3)$, and $P(X=3)$.

**C9.9.** 🔴 *(Density above 1 is legal.)* $X$ has density $f(x)=4$ on $0<x<0.25$. Show it is a valid density, then find $P(X<0.1)$ and $P(X=0.1)$.

**C9.10.** 🟡 *(AUDIT — recycled Team Rocket error: skipped normalizer.)* Team Rocket computes $P(X<2)$ for $f(x)=c\,x$ on $(0,3)$ as $\int_0^2 x\,dx = 2$. Find the true value and name the error.

**C9.11.** 🟡 *(RIVAL_TRAP — Gary skips the constant.)* Gary says that for $f(x)=k\,x^2$ on $0<x<2$, $P(X<1)=\int_0^1 x^2\,dx = \tfrac13$. Find $k$ first, then the true $P(X<1)$, and name Gary's error.

**C9.12.** 🔵 *(Mixed law — full cdf and a cumulative read.)* A payout $Y$ is exactly $0$ w.p. $0.4$, otherwise has density $f(y)=k\,y$ on $(0,2]$. Find $k$, write the cdf $F(y)$ for all $y$, and find $P(Y\le 1)$.

**C9.13.** 🟡 *(Survival from a cdf.)* A loss has $F(x)=1-(1+x)^{-2}$ for $x\ge 0$. Find the density $f(x)$ and the survival $P(X>1)$.

**C9.14.** 🔴 *(RIVAL_TRAP — Gary reads a height as a probability.)* For $f(x)=3x^2$ on $(0,1)$, Gary says "the most likely value is $1$, and its probability is $f(1)=3$." State the true $P(X=1)$ and name both errors in his claim.

**C9.15.** 🟡 *(AUDIT — a point mass reported as zero.)* A claims note says that for the payout $Y$ (mass $0.4$ at $0$, density $0.15$ on $(0,4]$), "since $Y$ is continuous, $P(Y=0)=0$." Find the true $P(Y=0)$ and $P(Y\le 0)$, and name the error.

**C9.16.** 🟡 *(Solve a constant from a given probability.)* $f(x)=c$ on $(0,m)$ and it is known that $P(X<2)=0.5$ with $m=6$. Find $c$ and confirm the total area is $1$.

### Elite Challenge (post-game — integrative / stretch)

**C9.17.** 🔵 *(Integrative — mixed law with a limit mass, DECISION.)* An insurance payout pays $0$ w.p. $0.5$; otherwise it is the loss, continuous with density $f(y)=0.2$ on $(0,2)$, **capped at $2$** so that all loss probability above $2$ piles onto a point mass at $y=2$. (a) Find the mass at $2$. (b) Find $P(Y=0)$, $P(0<Y<2)$, $P(Y=2)$, and confirm they total $1$. (c) Decide: does $P(Y\le 2)$ depend on whether you write $\le$ or $<$ at $2$?

**C9.18.** 🔵 *(Piecewise density — normalize and difference.)* $f(x)=c$ on $(0,1)$ and $f(x)=c(2-x)$ on $[1,2)$ (and $0$ elsewhere). Find $c$, the cdf at $x=1$, and $P(0.5<X<1.5)$.

**C9.19.** 🔵 *(From scratch — derive a cdf and check both directions.)* A density is $f(x)=\tfrac{3}{8}x^2$ on $0<x<2$. Verify it integrates to $1$, derive $F(x)$ on $(0,2)$, confirm $f=F'$, and find the median (the value $m$ with $F(m)=0.5$).
:::

## Answers

### Quick-Answer Table

| Problem | Answer | Archetype |
|---|---|---|
| C9.1 | $P(0.5<X<1.5)=0.5$; $P(X=1)=0$ | standard |
| C9.2 | $c=\tfrac29$; $P(X<2)=\tfrac49\approx0.444$ | standard |
| C9.3 | $F(x)=x^2$; $P(0.3<X<0.6)=0.27$ | standard |
| C9.4 | $f(x)=\tfrac15 e^{-x/5}$; $P(X>5)=e^{-1}=0.3679$ | standard |
| C9.5 | total $=1$; $P(Y\le5)=1$; $P(Y=0)=0.3$ | standard |
| C9.6 | $P(X=1)=0$; error: density height read as probability | audit |
| C9.7 | matters for (ii), the discrete one (mass at 2); not for (i) | decision |
| C9.8 | $c=\tfrac18$; $F=\tfrac{x^2}{16}$; $P(1<X<3)=0.5$; $P(X=3)=0$ | standard |
| C9.9 | valid (area $4\cdot0.25=1$); $P(X<0.1)=0.4$; $P(X=0.1)=0$ | standard |
| C9.10 | true $\tfrac49\approx0.444$; error: integrated before normalizing | audit |
| C9.11 | $k=\tfrac38$; $P(X<1)=\tfrac18=0.125$; skipped the constant | rival_trap |
| C9.12 | $k=0.3$; $F(y)=0.4+0.15y^2$ on $(0,2]$; $P(Y\le1)=0.55$ | standard |
| C9.13 | $f(x)=2(1+x)^{-3}$; $P(X>1)=(2)^{-2}=0.25$ | standard |
| C9.14 | $P(X=1)=0$; height isn't a probability, and a point carries none | rival_trap |
| C9.15 | $P(Y=0)=P(Y\le0)=0.4$; error: mixed law, mass not zero | audit |
| C9.16 | the normalizer binds: $c=\tfrac16$, so $P(X<2)=\tfrac13$ (the $0.5$ given is inconsistent) | standard |
| C9.17 | mass at 2 $=0.1$; $0.5,0.4,0.1$ total $1$; yes it depends | decision |
| C9.18 | $c=\tfrac23$; $F(1)=\tfrac23$; $P(0.5<X<1.5)=\tfrac{7}{12}\approx0.583$ | standard |
| C9.19 | area $=1$; $F=\tfrac{x^3}{8}$; $f=F'$ ✓; median $=2^{2/3}\approx1.587$ | standard |

**Worked solutions.**

**C9.1.** Area is probability: $P(0.5<X<1.5)=\tfrac12\times(1.5-0.5)=\tfrac12\times1=0.5$. A single point has zero width, so $P(X=1)=0$. *(Entry №01.)*

**C9.2.** Normalize first: $\int_0^3 c\,x\,dx=\tfrac{9c}{2}=1\Rightarrow c=\tfrac29$. Then $P(X<2)=\int_0^2\tfrac29 x\,dx=\tfrac29\cdot\tfrac{4}{2}=\tfrac{4}{9}\approx0.444$. *(Entry №02.)*

**C9.3.** $F(x)=\int_0^x 2t\,dt=x^2$ on $(0,1)$. Then $P(0.3<X<0.6)=F(0.6)-F(0.3)=0.36-0.09=0.27$. *(Entry №02.)*

**C9.4.** $f(x)=F'(x)=\tfrac{d}{dx}\big(1-e^{-x/5}\big)=\tfrac15 e^{-x/5}$. Survival: $P(X>5)=1-F(5)=e^{-5/5}=e^{-1}\approx0.3679$. *(Entry №02.)*

**C9.5.** Continuous area $=0.14\times5=0.7$; with the mass $0.3$ the total is $0.3+0.7=1$ ✓. $P(Y\le5)$ collects all of it $=1$. $P(Y=0)=0.3$ (the point mass). *(Entry №03.)*

**C9.6.** Audit. For a continuous $X$, $P(X=1)=0$ — a single point has zero width. The note read the *density height* $f(1)=0.5$ (a rate per unit length) as a probability; only an area is a probability. *(Entry №01; Team Rocket's Trap.)*

**C9.7.** Decision. For the **continuous** $X$ (i), $P(X<2)=P(X\le2)$ because the single point $2$ carries zero probability — $<$ vs $\le$ does **not** matter. For the **discrete** $X$ (ii) with a mass at $2$, $P(X\le2)=P(X<2)+P(X=2)$ differs by that mass — $<$ vs $\le$ **does** matter. The distinction is exactly "which world (or, for mixed laws, which kind of point) am I at." *(Entries №01, №03.)*

**C9.8.** Normalize: $\int_0^4 c\,x\,dx=8c=1\Rightarrow c=\tfrac18$. cdf $F(x)=\int_0^x\tfrac18 t\,dt=\tfrac{x^2}{16}$ on $[0,4]$. $P(1<X<3)=F(3)-F(1)=\tfrac{9}{16}-\tfrac{1}{16}=\tfrac{8}{16}=0.5$. $P(X=3)=0$. *(Entry №02.)*

**C9.9.** Area $=4\times0.25=1$ and $f\ge0$, so it is valid *despite* the height $4>1$ (a density is a rate, not a probability). $P(X<0.1)=4\times0.1=0.4$; $P(X=0.1)=0$. *(Entry №01.)*

**C9.10.** Audit (recycled Team Rocket error). They **integrated before normalizing**. Solve $\int_0^3 c\,x\,dx=\tfrac{9c}{2}=1\Rightarrow c=\tfrac29$, *then* $P(X<2)=\int_0^2\tfrac29 x\,dx=\tfrac49\approx0.444$. The bare integral $\int_0^2 x\,dx=2$ ignores $c$ and even exceeds $1$ — the giveaway. *(Entry №02; Team Rocket's Trap.)*

**C9.11.** Rival trap. Gary skipped the constant. Normalize: $\int_0^2 k\,x^2\,dx=k\cdot\tfrac{8}{3}=1\Rightarrow k=\tfrac{3}{8}$. Then $P(X<1)=\int_0^1\tfrac38 x^2\,dx=\tfrac38\cdot\tfrac13=\tfrac18=0.125$, not $\tfrac13$. He integrated the un-normalized kernel. *(Entry №02.)*

**C9.12.** Continuous part carries leftover $1-0.4=0.6$: $\int_0^2 k\,y\,dy=2k=0.6\Rightarrow k=0.3$. Then $F(y)=0.4+\int_0^y 0.3\,t\,dt = 0.4+0.15y^2$ on $(0,2]$, with $F=0$ below $0$ and $F=1$ at/above $2$ (since $0.4+0.15\cdot4=1$ ✓). $P(Y\le1)=F(1)=0.4+0.15=0.55$. *(Entry №03.)*

**C9.13.** $f(x)=F'(x)=\tfrac{d}{dx}\big(1-(1+x)^{-2}\big)=2(1+x)^{-3}$. Survival $P(X>1)=1-F(1)=(1+1)^{-2}=2^{-2}=0.25$. *(Entry №02.)*

**C9.14.** Rival trap (two errors). First, for a continuous $X$, $P(X=1)=0$ — a single point carries no area — so there is no positive "probability of the most likely value." Second, $f(1)=3$ is a *density height* (a rate), not a probability, and it may exceed $1$. Both confuse a rate for a chance. *(Entry №01.)*

**C9.15.** Audit. The law is **mixed**, not purely continuous: a genuine point mass of $0.4$ sits at $0$. So $P(Y=0)=0.4$, and $P(Y\le0)=0.4$ as well (nothing below $0$). The note wrongly applied the purely-continuous rule $P(\text{point})=0$ to a value that carries a real mass. *(Entry №03.)*

**C9.16.** Standard, with a deliberate inconsistency to catch. For a flat density $c$ on $(0,6)$, the binding condition is always normalization: total area $c\times 6 = 1\Rightarrow c=\tfrac16$. This *forces* $P(X<2)=c\times 2 = \tfrac16\times 2 = \tfrac13$, so the stated "$P(X<2)=0.5$" cannot also hold — it would require $c=0.25$, whose total area $0.25\times 6 = 1.5\ne 1$ is not a valid density. The lesson: $\int f = 1$ governs; the answer is $c=\tfrac16$ and $P(X<2)=\tfrac13$, and a "given" probability that contradicts the normalizer is a planted error to reject. *(Entry №02.)*

**C9.17.** Integrative decision. (a) Continuous loss area on $(0,2)$ is $0.2\times2=0.4$; the total *non-zero-loss* probability is $0.5$, so the leftover $0.5-0.4=0.1$ piles onto the cap: mass at $2$ is $0.1$. (b) $P(Y=0)=0.5$, $P(0<Y<2)=0.4$, $P(Y=2)=0.1$; total $0.5+0.4+0.1=1$ ✓. (c) **Yes it depends:** because a real mass sits at $2$, $P(Y\le2)=1$ but $P(Y<2)=0.9$ — they differ by the $0.1$ cap mass. At a point mass, $\le$ vs $<$ matters. *(Entry №03.)*

**C9.18.** Normalize: $\int_0^1 c\,dx + \int_1^2 c(2-x)\,dx = c\cdot1 + c\cdot\tfrac12 = \tfrac{3c}{2}=1\Rightarrow c=\tfrac23$. cdf at $1$: $F(1)=\int_0^1\tfrac23\,dx=\tfrac23$. For the band, split at the kink $x=1$: the first piece is $\int_{0.5}^1\tfrac23\,dx=\tfrac23(0.5)=\tfrac13$; the second is $\int_1^{1.5}\tfrac23(2-x)\,dx=\tfrac23\big[2x-\tfrac{x^2}{2}\big]_1^{1.5}=\tfrac23\big[(3-1.125)-(2-0.5)\big]=\tfrac23(0.375)=0.25$. Total $P(0.5<X<1.5)=\tfrac13+0.25=\tfrac{7}{12}\approx0.583$. *(Entry №02.)*

**C9.19.** Area: $\int_0^2\tfrac38 x^2\,dx=\tfrac38\cdot\tfrac{8}{3}=1$ ✓. cdf: $F(x)=\int_0^x\tfrac38 t^2\,dt=\tfrac{x^3}{8}$ on $(0,2)$. Check $f=F'=\tfrac{3x^2}{8}$ ✓ and $F(2)=1$ ✓. Median: $F(m)=\tfrac{m^3}{8}=0.5\Rightarrow m^3=4\Rightarrow m=4^{1/3}=2^{2/3}\approx1.587$. *(Entries №01, №02.)*

## Badge Earned — the Marsh Badge

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/marsh_badge.png" alt="The Marsh Badge, the gold gym badge awarded by Sabrina of Saffron City" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Marsh Badge earned!</strong> Rank: Ace Trainer · 6 badges.</figcaption>
</figure>

You read Sabrina's smooth curve — normalizing first, treating height as a rate and area as probability, and keeping a mixed law's point mass separate from its continuous part — and Haunter's laughter did the rest. Sabrina pressed the **Marsh Badge** into your hand. **Rank: Ace Trainer · 6 badges** (Cascade, Thunder, Boulder, Rainbow, Soul, Marsh). Six down, two to go on the road to the Indigo Plateau.

**Mastery checklist — tick each before you move on (mapped 1-to-1 to the SOA outcome):**

- ☐ **(2a — area is probability)** I can compute $P(a\le X\le b)=\int_a^b f$, explain why $P(X=c)=0$ and why endpoints don't matter for a continuous $X$, and I never mistake the density's *height* (a rate, possibly $>1$) for a probability. *(Rematch: Concept 1, WE 4, Problems C9.1, C9.6, C9.9, C9.14.)*
- ☐ **(2a — the $f\leftrightarrow F$ machinery)** I can move among $f$, $F$, $S$, and band probabilities using $f=F'$ and $F=\int f$, difference a cdf ($F(b)-F(a)$), and read a survival $1-F$. *(Rematch: Concept 2, WE 1–2, Problems C9.3, C9.4, C9.8, C9.13.)*
- ☐ **(2a — the normalizing constant)** The instant a density carries an unknown ($c$, $k$), my first move is $\int f=1$; I solve for the constant *before* computing any probability. *(Rematch: Concept 2, WE 1, Problems C9.2, C9.10, C9.11, C9.16.)*
- ☐ **(2a — mixed distributions)** I can handle a law with a **point mass** plus a continuous part — total $=1$, the cdf jumps by the mass then ramps, and any probability is qualifying masses **plus** the integral over the qualifying band — minding $<$ vs $\le$ at a mass. *(Rematch: Concept 3, WE 3, Problems C9.5, C9.12, C9.15, C9.17.)*

**Gym Rematch pointers.** Read a density height as a probability? Concept 1 Beat 4 and the Team Rocket Trap, then C9.6, C9.14. Computed a probability before solving for the constant? Concept 2 Beat 4, then C9.10, C9.11. Reported a point mass as $0$? Concept 3 Beat 4, then C9.15, C9.17. Confused $<$ with $\le$? Concept 1 Beat 6 (continuous) and Concept 3 Beat 7 (at a mass), then C9.7.

> Next stop: still **Saffron / Silph Co.**, where you take these same smooth curves and ask the S.S. Anne's old questions of them — the **center and spread** of a continuous law, now with integrals: $E[X]=\int x\,f(x)\,dx$ and the survival-integral shortcut. Pack your density-reading reflexes; every moment ahead is an integral of the curve you just learned to read.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026). All sprite/anime assets are real assets sourced online, never generated.*
