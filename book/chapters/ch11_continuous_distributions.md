<!--
  file: ch11_continuous_distributions
  tier: B
  outcomes: 2d
  tia: B.3
  locale: the smooth continuous wilds (cross-Kanto travel; no gym)
  type: water
  maps_to: the smooth continuous wilds -> the four named continuous shapes
           (uniform, exponential, gamma, beta) + Pareto enrichment
-->

# The Four Wild Shapes — Key Continuous Distributions {.type-water}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with no single city circled; instead the long cross-region routes between towns are highlighted, the open water and wild roads you travel between gyms, labelled 'the smooth continuous wilds'." style="width:70%; max-width:520px; display:block; margin:1em auto;">
<figcaption>No gym this leg — just the open road. You are crossing <em>the smooth continuous wilds</em>: the long water-routes and wild stretches between Kanto's cities, where every quantity glides instead of ticking.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Long Way Round"**

There is no city today. Just the road between them — a ferry leg across open water, a march through tall grass, the un-glamorous *travel* that the cameras usually skip. And travel, you are discovering, is where the smooth math lives.

A wild **Porygon** glitches into being somewhere along the corridor ahead. Not *at* a tile — it could be anywhere on the stretch, every point as likely as any other. "Where, exactly?" you ask. Misty shrugs. "There is no *exactly*. Only a *band*. Ask me the chance it's in the next thirty paces and I can answer. Ask me the chance it's on one specific blade of grass and the answer is zero."

Further on, the ferry's hull pings — a sonar contact. The pings arrive at *random gaps*, and the navigator times them. "Average gap is six seconds," she says, eyes on the clock. The clock reads *eight* seconds since the last ping, and still nothing. "So it's nearly *due*, right?" you offer. She actually laughs. "This sea has no schedule. Waiting eight seconds buys you *nothing*. The next gap is still, on average, a full six seconds away — as if the clock never started."

That breaks something in your head. And it only gets stranger: the navigator wants the time until the *third* ping, the fraction of the hull that the barnacles cover, the chance a freak wave dwarfs anything on record. Four different questions, four different *shapes* — and each one is some smooth curve you can't yet name.

*Each wild shape answers a different question — a position with no preferred point, a wait that forgets, a sum of waits, a trapped fraction. What are the four curves, and how do you read each one?*
:::

## Where You Are — 60-Second Retrieval

**Rank: Ace Trainer · Badges: 6.** Six badges ride in your case — Cascade, Thunder, Boulder, Rainbow, Soul, and the Marsh Badge from Sabrina — and there is no seventh to win out here; the wilds hand out no badge. What you carry from the last leg is the **continuous-moment machinery**. For a continuous random variable $X$ with density $f$, you no longer *sum* — you *integrate*: probability is **area under the curve**, the mean is

$$E[X] = \int_{-\infty}^{\infty} x\,f(x)\,dx,$$

and for a non-negative $X$ you can also stack the survival function, $E[X] = \int_0^\infty S(x)\,dx$ — the continuous twin of the Darth-Vader sum. That single shift — *sum becomes integral, mass becomes area* — is the whole foundation the four wild shapes stand on. Each one below is just a *specific choice of $f(x)$*; the machinery is already yours.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the continuous world**

Answer from memory; if any feels shaky, flip back before reading on.

1. For a continuous $X$, what is $P(X = 3)$ exactly, and why? *(Answer: $0$ — a single point has zero width, hence zero area.)*
2. Write $E[X]$ for a continuous $X$ as an integral. *(Answer: $\int x\,f(x)\,dx$.)*
3. The total area under any density $f(x)$ must equal what? *(Answer: $1$.)*

All three instant? Every shape below is a new $f$ poured into the same machine. Any hesitation? Reclaim "area is probability" first — it is the only prerequisite here.
:::

::: now-playing
**📺 NOW PLAYING — Indigo League: the cross-Kanto travel episodes**

<figure><img src="../../assets/stills/ch11_now_playing.jpg" alt="Ash and friends on a cross-Kanto road in one of the travel episodes (Indigo League EP036, The Bridge Bike Gang)." style="width:60%; max-width:440px; display:block; margin:0.4em auto;"><figcaption style="font-size:0.8em; color:#555;">The road between towns, EP036 — distance and waiting time as smooth quantities: the uniform and the exponential.</figcaption></figure>

There is no single tied gym episode for this leg — it maps to the *travel* stretches of Season 1, the journeys **between** the badge cities (ferry crossings, forest roads, the long walks the show uses to move Ash from one town to the next). *Watch any one of those travel-heavy episodes alongside this chapter.* On screen, the throughline is honest: progress here is the **road itself**, not a boss. (The Porygon spawn, the sonar pings, and the barnacle fraction are **in-world extensions** built to carry the four shapes — they dramatize the math, not specific on-screen scenes.)
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice comes through the Pokédex over the slap of water on the hull.

"No gym today, Ash — but do not coast. The open road is where you meet the *named continuous shapes*, and an actuary lives among them. The **uniform** is the flat default; the **exponential** is every waiting time and the one curve that *forgets*; the **gamma** is the wait for several events stacked together; the **beta** is any random *fraction* trapped between $0$ and $1$. Four shapes, four recognition cues. Learn to name a distribution on sight and read its mean and variance without re-deriving them, and half of continuous Exam P becomes bookkeeping. This is a **Tier B** chapter — full nine-beat teaching for each shape, with a gentler ramp than the Tier-A proving grounds, but every idea is one you reuse downstream."

By the end of this chapter you will be able to:

- **State and use the continuous uniform** $\mathrm{Unif}(a,b)$ — its flat density, cdf, mean $\tfrac{a+b}{2}$, and variance $\tfrac{(b-a)^2}{12}$ — reading any probability as a **length ratio**. *(Outcome 2d.)*
- **State and use the exponential** $\mathrm{Exp}(\theta)$ — its survival $S(x)=e^{-x/\theta}$, mean $\theta$, variance $\theta^2$, MGF — and **exploit memorylessness** to collapse any "given it has already lasted $s$" condition. *(Outcome 2d.)*
- **State and use the gamma** $\mathrm{Gamma}(\alpha,\theta)$ as a **sum of $\alpha$ independent exponentials**, with mean $\alpha\theta$ and variance $\alpha\theta^2$, and connect the **exponential / gamma / Poisson** trio. *(Outcome 2d.)*
- **State and use the beta** $\mathrm{Beta}(\alpha,\beta)$ for a random proportion on $[0,1]$, with mean $\tfrac{\alpha}{\alpha+\beta}$, knowing $\mathrm{Beta}(1,1)=\mathrm{Unif}(0,1)$. *(Outcome 2d.)*

> *Exam-weight signpost.* The continuous families are a **steadily tested** slice of Exam P's Univariate section — the exponential especially, and its memorylessness above all. This is a **Tier B** chapter: each shape gets the full treatment because you will lean on every one of them in pricing, joint distributions, and the CLT. The Pareto at the end is **enrichment** — off-syllabus, not tested, there only for the bridge to the job.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own the Four Shapes?**

Already fluent? Prove it. Work these four, ~3 minutes each, *with correct method*:

1. $X\sim\mathrm{Unif}(2,10)$. Find $P(4<X<7)$, $E[X]$, and $\mathrm{Var}(X)$.
2. $X\sim\mathrm{Exp}(\theta=6)$ minutes, already running $4$ minutes with no event. Find $P(X>10\mid X>4)$ and the expected *remaining* wait.
3. $X\sim\mathrm{Gamma}(\alpha=3,\theta=2)$. Find $E[X]$, $\mathrm{Var}(X)$, and the value of $\int_0^\infty x^2 e^{-x/2}\,dx$.
4. $X\sim\mathrm{Beta}(\alpha=2,\beta=3)$. Find $E[X]$ and say whether it is above or below $\tfrac12$.

*(Answers: $0.375$, $E=6$, $\mathrm{Var}=64/12=5.\overline{3}$; $e^{-1}\approx 0.368$ and $6$ min; $E=6$, $\mathrm{Var}=12$, $\int = \Gamma(3)\,2^3 = 16$; $E=0.4$, below $\tfrac12$.)* Four for four with the right reasoning? **Skip to the Capstone Challenge.** Any miss or hesitation? The teaching below was built exactly for you — and each shape has its own skip-gate, so even a partial owner loses no time.
:::

---

Four shapes build in increasing difficulty, in TIA order. We teach them **in order**, each with its own "do you already own this?" skip-check, then the full nine-beat lesson, then a Pokédex Entry you can carry into the exam. A fifth box — the **Pareto** — is *enrichment*: off-syllabus, never gated, read only for the bridge.

1. **The continuous uniform** — the flat curve, where probability is a length ratio
2. **The exponential** — the waiting time, and the memory that resets *(the signature idea)*
3. **The gamma** — a sum of exponential waits, and the exponential/gamma/Poisson link
4. **The beta** — a random proportion trapped on $[0,1]$
5. **The Pareto** — *enrichment*: the heavy tail that keeps catastrophes on the table

## Concept 1 — The Continuous Uniform: the Flat Curve

::: concept-gate
**DO YOU ALREADY OWN THIS? — Uniform**

A glitching Porygon spawns at $X\sim\mathrm{Unif}(2,10)$ (equally likely anywhere on $[2,10]$). What is $P(4<X<7)$?

If you instantly said **$\tfrac{7-4}{10-2}=\tfrac{3}{8}=0.375$** (a length ratio) and can write $E[X]=6$, **skip to Concept 2**. If you weren't sure why it's a ratio of lengths — or you divided by $10$ instead of $8$ — read on; this is the gentlest curve in the chapter.
:::

**Beat 1 — The one-sentence idea.** *When every value in an interval is equally likely, the density is a flat rectangle, and any probability is just a ratio of lengths.*

**Beat 2 — Anchor + concrete instance.** This is the area-is-probability foundation with the simplest possible $f$: a constant. A glitching **Porygon** spawns somewhere along the corridor between coordinates $2$ and $10$, with **no point preferred**. Its position is $X\sim\mathrm{Unif}(2,10)$. To dodge it you need $P(4<X<7)$.

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/137.png" alt="Porygon, the polygonal mascot that spawns uniformly along the corridor" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#137 Porygon — spawns uniformly on the corridor</strong></figcaption>
</figure>

**Beat 3 — Reason through it in plain words.** The corridor is $10-2 = 8$ units long, and the probability is spread *evenly* across it. The dangerous band $(4,7)$ is $7-4 = 3$ units long. "Evenly spread" means probability is proportional to length, so

$$P(4<X<7) = \frac{\text{band length}}{\text{total length}} = \frac{3}{8} = 0.375.$$

For the density to enclose area $1$ over a length-$8$ interval, its constant height must be $\tfrac{1}{8}$ — then $\tfrac18\times 8 = 1$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** A common slip is to forget the interval doesn't start at $0$ and divide by the *upper endpoint*:

$$\frac{7-4}{10} = 0.30. \qquad\textbf{(wrong — the corridor starts at 2, not 0)}$$

The total length is $b-a = 10-2 = 8$, **not** $10$. Always measure both the band and the whole interval from the *true* lower endpoint $a$. (This off-by-the-lower-endpoint error is exactly what Team Rocket walks into later.)

**Beat 5 — Translate into notation, one glyph at a time.** Write $X\sim\mathrm{Unif}(a,b)$, read aloud *"$X$ is uniform on $a$ to $b$."* The flat density is

$$f(x) = \frac{1}{b-a}, \qquad a \le x \le b,$$

and zero elsewhere. Read $\tfrac{1}{b-a}$ as *"one over the width"* — the only height that makes the rectangle's area $1$. The cdf accumulates that constant linearly:

$$F(x) = P(X\le x) = \frac{x-a}{b-a}, \qquad a \le x \le b$$

— read *"how far into the interval $x$ has travelled, as a fraction."*

**Beat 6 — Derive the mean and variance.** The center of a flat rectangle is its midpoint, so by symmetry $E[X]=\tfrac{a+b}{2}$ — no integral needed. For the spread, integrate the second moment and subtract the square of the mean. With $f=\tfrac{1}{b-a}$,

$$E[X^2] = \int_a^b x^2\,\frac{1}{b-a}\,dx = \frac{1}{b-a}\cdot\frac{b^3-a^3}{3} = \frac{a^2+ab+b^2}{3},$$

using $b^3-a^3=(b-a)(a^2+ab+b^2)$. Then

$$\mathrm{Var}(X) = E[X^2]-(E[X])^2 = \frac{a^2+ab+b^2}{3} - \frac{(a+b)^2}{4} = \frac{(b-a)^2}{12}$$

after collecting terms over a common denominator of $12$. So both moments fall out cleanly:

$$\boxed{\;E[X] = \frac{a+b}{2}, \qquad \mathrm{Var}(X) = \frac{(b-a)^2}{12}.\;}$$

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the Porygon band, $P(4<X<7)=0.375$.
- *Twist (the standard uniform):* $\mathrm{Unif}(0,1)$ has $f(x)=1$, $E=\tfrac12$, $\mathrm{Var}=\tfrac{1}{12}$. It is the raw material every simulator uses to manufacture *every other* distribution (a uniform draw, pushed through an inverse-cdf, becomes whatever you like).
- *General (a sub-band):* $P(X>7) = \tfrac{10-7}{10-2} = \tfrac{3}{8}$ — still a length ratio, now of the upper piece.
- *Edge (the variance number):* for our Porygon, $\mathrm{Var} = \tfrac{(10-2)^2}{12} = \tfrac{64}{12} = 5.\overline{3}$, so $\mathrm{SD}\approx 2.31$ — a little over a quarter of the corridor, which matches the eye.

**Beat 8 — Picture it.** The density is literally a rectangle; probability is the sub-rectangle over your band.

<figure>
<img src="../../assets/diagrams/ch11_uniform.png" alt="A flat horizontal density of constant height one-eighth sitting above the interval from a=2 to b=10. The sub-rectangle above the band from 4 to 7 is shaded with diagonal hatching; an inset shows P(4<X<7) = (7-4)/(10-2) = 3/8. A Porygon sprite sits in the upper-left margin, clear of the rectangle." style="width:82%; max-width:660px; display:block; margin:1em auto;">
<figcaption>The uniform density is a flat rectangle of height $1/(b-a)$. A band's probability is its shaded sub-rectangle — a pure length ratio, $3/8$ here.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can read any uniform probability as a length ratio, and write its mean (the midpoint) and variance $\tfrac{(b-a)^2}{12}$ on sight — always measuring from the true lower endpoint $a$.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Continuous Uniform $\mathrm{Unif}(a,b)$**

$$f(x)=\frac{1}{b-a}\ (a\le x\le b),\quad F(x)=\frac{x-a}{b-a},\quad E[X]=\frac{a+b}{2},\quad \mathrm{Var}(X)=\frac{(b-a)^2}{12}.$$

*In plain terms:* every value on $[a,b]$ is equally likely; probability is a ratio of lengths.

*Recognition cue:* "equally likely anywhere between," "chosen at random from the interval," "no point preferred" → uniform. Mean = midpoint; the $/12$ in the variance is worth memorizing.
:::

## Concept 2 — The Exponential: Waiting Time and the Memory That Resets

::: concept-gate
**DO YOU ALREADY OWN THIS? — Exponential & memorylessness**

A sonar ping arrives after $X\sim\mathrm{Exp}(\theta=6)$ seconds. It has already been $4$ seconds with no ping. What is $P(X>10\mid X>4)$, and what is the expected *remaining* wait?

If you instantly said **$P(X>10\mid X>4) = P(X>6) = e^{-1}\approx 0.368$** (the clock resets) and **expected remaining $=\theta=6$ seconds**, you own memorylessness — **skip to Concept 3**. If you tried to subtract probabilities the long way, or expected the remaining time to shrink toward $2$, read on — this is the signature idea of the chapter.
:::

**Beat 1 — The one-sentence idea.** *The exponential is the waiting time until a purely random event, and it is **memoryless**: however long you've already waited, the remaining wait is a fresh exponential.*

**Beat 2 — Anchor + concrete instance.** Back among the discrete families, the **Poisson** counted how *many* random events happen in a fixed window. The exponential is the other side of the same coin: the *gap between* those events — a continuous waiting time. The ferry's sonar fires pings at random gaps averaging $\theta=6$ seconds; you've waited $4$ seconds since the last one. What's the chance the gap lasts past $10$ seconds, given it's still going — and how much longer should you expect?

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/101.png" alt="Electrode, the round timer-bomb mascot whose countdown is an exponential wait" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#101 Electrode — its random countdown is an exponential wait</strong></figcaption>
</figure>

**Beat 3 — Reason through it in plain words.** The exponential's defining feature is a **constant hazard**: at every instant the event is equally "due," no matter how long you've already waited. So waiting $4$ seconds gives you *no information* about how much longer it'll go. The remaining time behaves exactly as if you'd just started — a fresh $\mathrm{Exp}(6)$. Therefore the chance of lasting "$6$ more seconds" past the $4$ you've waited equals the plain chance a *fresh* exponential exceeds $6$:

$$P(X>10\mid X>4) = P(X>6) = e^{-6/6} = e^{-1} \approx 0.368,$$

and the expected remaining wait is the full mean again: $6$ seconds. *That* is why the navigator laughed — the sea has no schedule, and an exponential forgets.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The natural intuition is *"I've already waited $4$ of an expected $6$ seconds, so only $2$ should remain."*

$$E[\text{remaining}] \overset{?}{=} 6 - 4 = 2. \qquad\textbf{(wrong — that's how a fixed appointment works, not a memoryless wait)}$$

If the gap had a *fixed* duration, waiting would burn it down. But a constant-hazard process has no schedule to burn down: each new instant is a fresh roll of the same dice. The elapsed $4$ seconds are gone and irrelevant; the expected remaining wait is the full $6$. This is genuinely strange the first time — and it is *the* exponential pitfall on the exam.

**Beat 5 — Translate into notation, one glyph at a time.** Write $X\sim\mathrm{Exp}(\theta)$, read *"$X$ is exponential with mean $\theta$."* Its density, cdf, and survival are

$$f(x)=\frac{1}{\theta}e^{-x/\theta}\ (x>0), \qquad F(x)=1-e^{-x/\theta}, \qquad S(x)=e^{-x/\theta}.$$

That clean survival function $S(x)=e^{-x/\theta}$ is the workhorse — read it *"the chance of waiting longer than $x$."* Some texts use the **rate** $\lambda=1/\theta$ instead, writing $f(x)=\lambda e^{-\lambda x}$; same curve, reciprocal parameter. **Watch which one a problem hands you** — the mean $\theta$ or the rate $\lambda$. The memoryless property, in symbols, is

$$P(X > s+t \mid X > s) = P(X > t) \qquad \text{read: ``having survived } s\text{, the extra wait is a fresh } \mathrm{Exp}(\theta)\text{.''}$$

**Beat 6 — Derive memorylessness (it's just algebra).** Don't take it on faith — it falls straight out of the definition of conditional probability and the survival function. Since "$X>s+t$" already implies "$X>s$," their intersection is just "$X>s+t$":

$$P(X>s+t\mid X>s) = \frac{P(\{X>s+t\}\cap\{X>s\})}{P(X>s)} = \frac{P(X>s+t)}{P(X>s)} = \frac{e^{-(s+t)/\theta}}{e^{-s/\theta}} = e^{-t/\theta} = P(X>t).$$

The elapsed-$s$ factor $e^{-s/\theta}$ **cancels top and bottom** — that cancellation *is* the lost memory. (In fact the exponential is the *only* continuous distribution with this property; it is what the constant-hazard assumption forces.) The moments follow by integration: $E[X]=\int_0^\infty S(x)\,dx = \int_0^\infty e^{-x/\theta}\,dx = \theta$ (the survival-integral shortcut from last chapter), and a second integration gives $E[X^2]=2\theta^2$, so $\mathrm{Var}(X)=2\theta^2-\theta^2=\theta^2$.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* a survival probability, $P(X>x)=e^{-x/\theta}$ in one keystroke.
- *Twist (memoryless conditioning):* the sonar question — collapse "given it's lasted $s$" to a fresh exponential, as above.
- *General (the MGF):* $M(t)=\dfrac{1}{1-\theta t}$ for $t<\tfrac1\theta$; differentiating at $0$ regenerates $E[X]=\theta$, $E[X^2]=2\theta^2$.
- *Edge (minimum of exponentials):* if two independent exponentials race, the *first* to fire is itself exponential with the **rates added**: $\min(\mathrm{Exp}(\theta_1),\mathrm{Exp}(\theta_2))$ has rate $\tfrac{1}{\theta_1}+\tfrac{1}{\theta_2}$. (Two contacts each $\mathrm{Exp}(12)$: the first arrives as $\mathrm{Exp}(6)$.)

**Beat 8 — Picture it.** The exponential density is a decaying curve; the survival function is the area in its right tail. Re-anchoring that tail at any elapsed time $s$ reproduces the *identical* shape — that is memorylessness, drawn.

<figure>
<img src="../../assets/diagrams/ch11_exponential.png" alt="Two panels. Left: a decaying exponential density starting tall at x=0 and falling smoothly toward zero, with the right tail beyond x=s shaded and labelled survival S(x)=e^{-x/theta}; an Electrode sprite sits in the upper margin. Right: a survival curve where the conditional survival given X>s, re-anchored at s, lies exactly on top of the original survival shape, illustrating that the remaining wait is a fresh exponential." style="width:90%; max-width:740px; display:block; margin:1em auto;">
<figcaption>The exponential decays at a constant <em>relative</em> rate. Shaded right tail = $S(x)=e^{-x/\theta}$. Re-anchoring the survival curve at any elapsed $s$ reproduces the identical shape — the picture of memorylessness.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can compute exponential probabilities through $S(x)=e^{-x/\theta}$, and — the headline skill — collapse any "given it has already lasted $s$" condition to a fresh $\mathrm{Exp}(\theta)$ with expected remaining wait still $\theta$.

::: pokedex-entry
**POKÉDEX ENTRY №02 — Exponential $\mathrm{Exp}(\theta)$**

$$f(x)=\frac{1}{\theta}e^{-x/\theta},\quad S(x)=e^{-x/\theta},\quad E[X]=\theta,\quad \mathrm{Var}(X)=\theta^2,\quad M(t)=\frac{1}{1-\theta t}\ \left(t<\tfrac1\theta\right).$$
Memoryless: $\;P(X>s+t\mid X>s) = P(X>t)$.

*In plain terms:* the waiting time until the next purely random event; its single parameter $\theta$ is the mean wait. The gaps between Poisson events are exponential.

*Recognition cue:* "time until," "time between," "memoryless," "constant failure rate" → exponential. The instant you see "given it has already lasted $s$," reset the clock — the remaining wait is a fresh $\mathrm{Exp}(\theta)$.
:::

## Concept 3 — The Gamma: A Sum of Waits, and the Exponential/Gamma/Poisson Link

::: concept-gate
**DO YOU ALREADY OWN THIS? — Gamma**

A gate opens only after the **3rd** independent ping, each ping $\mathrm{Exp}(\theta=2)$ seconds apart. Let $X$ be the total time to the 3rd ping. What are $E[X]$ and $\mathrm{Var}(X)$? And what is $\int_0^\infty x^2 e^{-x/2}\,dx$?

If you instantly said **$E[X]=6$, $\mathrm{Var}(X)=12$** (it's a $\mathrm{Gamma}(3,2)$) and **$\int_0^\infty x^2 e^{-x/2}\,dx = \Gamma(3)\,2^3 = 2!\cdot 8 = 16$**, you own the gamma — **skip to Concept 4**. If the integral looked frightening, read on — there's a one-line trick.
:::

**Beat 1 — The one-sentence idea.** *The gamma is the total time to wait for the $\alpha$-th random event — a sum of $\alpha$ independent exponentials — and any integral shaped like its density evaluates in one line.*

**Beat 2 — Anchor + concrete instance.** This is the exponential, *stacked*. One exponential wait gets you to the first event; add $\alpha$ of them and you reach the $\alpha$-th. The ferry's gate unlocks only after the **3rd** sonar ping, with ticks independent and $\mathrm{Exp}(\theta=2)$ seconds apart. The total time $X$ to the 3rd ping is the sum of three independent $\mathrm{Exp}(2)$ waits.

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/front/82.png" alt="Magneton, three magnet units fused into one, the mascot for a gamma as three exponential waits stacked together" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#82 Magneton — three units fused: a sum of three exponential waits</strong></figcaption>
</figure>

**Beat 3 — Reason through it in plain words.** Means add: three waits, each averaging $2$ seconds, average $3\times 2 = 6$ seconds total. Variances of *independent* pieces add too: each $\mathrm{Exp}(2)$ has variance $\theta^2 = 4$, so three give $3\times 4 = 12$. So even before naming the curve, $E[X]=6$ and $\mathrm{Var}(X)=12$ — just "means add, and variances of independent things add."

**Beat 4 — Surface and dismantle the tempting wrong idea.** A frequent slip is miscounting the **shape** $\alpha$. The number of *waits* is $3$, so $\alpha=3$ — not $2$ (the count of *gaps between* the first and last ping, say) and not the exponent of $x$ in the density. Reading $\alpha$ off the wrong feature corrupts every moment. **$\alpha$ is the number of exponential waits summed; $\theta$ is each wait's mean.**

**Beat 5 — Translate into notation, one glyph at a time.** Write $X\sim\mathrm{Gamma}(\alpha,\theta)$, read *"gamma with shape $\alpha$, scale $\theta$."* Its density is

$$f(x) = \frac{1}{\Gamma(\alpha)\,\theta^{\alpha}}\,x^{\alpha-1}e^{-x/\theta}, \qquad x>0.$$

The new symbol $\Gamma(\alpha)$ is the **gamma function**, read *"gamma of $\alpha$"* — a smooth factorial. For a whole number it *is* a shifted factorial: $\Gamma(n)=(n-1)!$, and the one special value you'll need is $\Gamma(\tfrac12)=\sqrt{\pi}$. With $\alpha=1$ the density collapses to $\tfrac1\theta e^{-x/\theta}$ — exactly the exponential, as promised.

**Beat 6 — Derive the Master-Ball integral and the gamma/Poisson link.** Because the density integrates to $1$,

$$\int_0^\infty \frac{1}{\Gamma(\alpha)\theta^{\alpha}}\,x^{\alpha-1}e^{-x/\theta}\,dx = 1 \;\Longrightarrow\; \boxed{\;\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx = \Gamma(\alpha)\,\theta^{\alpha}.\;}$$

That boxed line — the **Master-Ball integral** — turns *any* integral of the form $x^{\text{power}}e^{-x/\theta}$ into a one-line lookup. Match the exponent of $x$ to "$\alpha-1$," read off $\alpha$, and the answer is $\Gamma(\alpha)\theta^{\alpha}$. The moments $E[X]=\alpha\theta$ and $\mathrm{Var}(X)=\alpha\theta^2$ pop straight out of it (and match "means/variances add" from Beat 3).

Now the **three-way link**, which the exam loves to test sideways. Picture random events arriving on a timeline at rate $\lambda=1/\theta$:

- **Poisson** counts *how many events* land in a fixed window of length $t$ — a discrete count, mean $\lambda t$.
- **Exponential** is the *gap between* consecutive events — a continuous wait, mean $\theta=1/\lambda$.
- **Gamma** with integer shape $\alpha$ is the *total time to the $\alpha$-th event* — a sum of $\alpha$ exponential gaps.

They are three views of one process. The bridge identity: *"the $\alpha$-th event hasn't happened by time $t$"* (a gamma statement, $X>t$) is the *same event* as *"fewer than $\alpha$ events occurred in $[0,t]$"* (a Poisson statement). That equivalence lets you evaluate an integer-shape gamma cdf by a short **Poisson sum** — no integration by parts:

$$P(X \le t) = 1 - \sum_{k=0}^{\alpha-1} \frac{(t/\theta)^k\,e^{-t/\theta}}{k!}.$$

**Beat 7 — Ramp the difficulty.**

- *Simplest:* read off $E[X]=\alpha\theta=6$, $\mathrm{Var}(X)=\alpha\theta^2 = 3\cdot 4 = 12$.
- *Twist (the scary integral, tamed):* $\int_0^\infty x^2 e^{-x/2}\,dx$ has exponent $2=\alpha-1$, so $\alpha=3$ and it equals $\Gamma(3)\,2^3 = 2!\cdot 8 = 16$. No integration by parts.
- *General (the gamma/Poisson cdf):* for our $\mathrm{Gamma}(3,2)$, $P(X<2) = 1 - e^{-1}\!\left(1 + 1 + \tfrac12\right) = 1 - 2.5\,e^{-1} = 1 - 0.9197 = 0.0803$ — read straight off the Poisson sum with $t/\theta=1$.
- *Edge (a higher moment):* $E[X^2]=\mathrm{Var}+(E)^2 = 12+36 = 48$ — or grind it: $E[X^2]=\int_0^\infty x^2\cdot\tfrac{1}{16}x^2 e^{-x/2}\,dx = \tfrac{1}{16}\,\Gamma(5)\,2^5 = \tfrac{1}{16}\cdot 24\cdot 32 = 48$. Same answer, the long way.

**Beat 8 — Picture it.** The gamma is a right-skewed hump whose shape $\alpha$ controls how peaked it is; $\alpha=1$ is the pure-decay exponential.

<figure>
<img src="../../assets/diagrams/ch11_gamma_shapes.png" alt="Three gamma densities with scale theta=2 and shapes alpha=1, 2, 3, each a different color and hatch. The alpha=1 curve is the pure-decay exponential; alpha=2 and alpha=3 rise to a hump that moves right and grows more symmetric. A dotted line marks the alpha=3 mean at 6, and a Magneton sprite sits in the upper-right margin." style="width:82%; max-width:660px; display:block; margin:1em auto;">
<figcaption>The gamma: a sum of $\alpha$ exponential waits. Larger $\alpha$ pushes the hump right and makes it more symmetric; $\alpha=1$ recovers the pure-decay exponential. The $\alpha=3$ mean sits at $\alpha\theta=6$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can recognize a sum of exponential waits as a gamma, write $E=\alpha\theta$ and $\mathrm{Var}=\alpha\theta^2$, evaluate any $\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx=\Gamma(\alpha)\theta^{\alpha}$ on sight, and switch between the gamma, exponential, and Poisson views of one event stream.

::: pokedex-entry
**POKÉDEX ENTRY №03 — Gamma $\mathrm{Gamma}(\alpha,\theta)$**

$$f(x)=\frac{1}{\Gamma(\alpha)\theta^{\alpha}}x^{\alpha-1}e^{-x/\theta}\ (x>0),\quad E[X]=\alpha\theta,\quad \mathrm{Var}(X)=\alpha\theta^2,\quad M(t)=(1-\theta t)^{-\alpha}.$$
**Master-Ball integral:** $\displaystyle\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx=\Gamma(\alpha)\theta^{\alpha}$, with $\Gamma(n)=(n-1)!$, $\Gamma(\tfrac12)=\sqrt\pi$.

*In plain terms:* the time until the $\alpha$-th random event — a sum of $\alpha$ independent $\mathrm{Exp}(\theta)$ waits. $\alpha=1$ is the exponential. Same event stream: Poisson counts events, exponential is the gap, gamma is the total to the $\alpha$-th.

*Recognition cue:* "time until the $k$-th event," "sum of $k$ exponential waits," or a density $\propto x^{\alpha-1}e^{-x/\theta}$ → gamma. Any $\int_0^\infty x^{k}e^{-x/\theta}\,dx = \Gamma(k{+}1)\theta^{k+1}=k!\,\theta^{k+1}$.
:::

## Concept 4 — The Beta: A Random Proportion on $[0,1]$

::: concept-gate
**DO YOU ALREADY OWN THIS? — Beta**

The fraction of the hull that barnacles cover is $X\sim\mathrm{Beta}(\alpha=2,\beta=3)$. What is $E[X]$, and is it above or below $\tfrac12$?

If you instantly said **$E[X]=\tfrac{\alpha}{\alpha+\beta}=\tfrac{2}{5}=0.4$**, below $\tfrac12$ (more mass toward $0$), **skip to the Pareto enrichment / Worked Examples**. If you're unsure how to get the mean of a proportion, read on — it's a short one.
:::

**Beat 1 — The one-sentence idea.** *The beta is the distribution of a random **proportion** — a flexible curve trapped between $0$ and $1$.*

**Beat 2 — Anchor + concrete instance.** Every distribution so far lived on an unbounded or arbitrary interval. But many real quantities are *fractions*: a percentage, a recovery rate, the share of something. The fraction $X$ of the ferry's hull that the barnacles **cover** is $X\sim\mathrm{Beta}(\alpha=2,\beta=3)$. We want its average and its shape.

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/front/113.png" alt="Chansey, the rounded mascot for a bounded random proportion on the unit interval" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#113 Chansey — a random proportion, trapped on $[0,1]$</strong></figcaption>
</figure>

**Beat 3 — Reason through it in plain words.** Think of $\alpha$ as "weight pulling toward $1$" and $\beta$ as "weight pulling toward $0$." With $\alpha=2$ and $\beta=3$, the pull toward $0$ is stronger, so the typical fraction should sit *below* $\tfrac12$ — the barnacles usually cover less than half. The center is the share of total weight on the $\alpha$ side: $\tfrac{2}{2+3} = 0.4$. That matches the picture.

**Beat 4 — Surface and dismantle the tempting wrong idea.** It is tempting to guess the mean is "halfway," $0.5$, just because the support is $[0,1]$.

$$E[X] \overset{?}{=} 0.5. \qquad\textbf{(wrong unless } \alpha=\beta\text{)}$$

The beta is only symmetric when $\alpha=\beta$. Here $\alpha\ne\beta$, so it tilts; the mean is $\tfrac{\alpha}{\alpha+\beta}=0.4$, not $0.5$. *Bounded support does not mean centered.*

**Beat 5 — Translate into notation, one glyph at a time.** Write $X\sim\mathrm{Beta}(\alpha,\beta)$, read *"beta with parameters $\alpha$, $\beta$."* Its density is

$$f(x) = \frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\,\Gamma(\beta)}\,x^{\alpha-1}(1-x)^{\beta-1}, \qquad 0<x<1.$$

The fraction out front (built from the same $\Gamma$ you just met) is only there to make the area equal $1$ — the *shape* lives entirely in $x^{\alpha-1}(1-x)^{\beta-1}$, the two "pulls" multiplied.

**Beat 6 — Derive the mean from the normalizing constant.** The mean is *not* something to take on faith — the same area-$1$ trick that tamed the gamma integral derives it in one line. Abbreviate the normalizer as $C(\alpha,\beta)=\tfrac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}$, the constant that makes $\int_0^1 x^{\alpha-1}(1-x)^{\beta-1}\,dx = 1/C(\alpha,\beta)$. Then $E[X]$ just bumps the $x$-exponent up by one — turning an $\alpha$-shape into an $(\alpha{+}1)$-shape — and re-uses the *same* integral identity:

$$E[X] = \int_0^1 x\cdot C(\alpha,\beta)\,x^{\alpha-1}(1-x)^{\beta-1}\,dx = C(\alpha,\beta)\int_0^1 x^{\alpha}(1-x)^{\beta-1}\,dx = \frac{C(\alpha,\beta)}{C(\alpha+1,\beta)}.$$

Expanding that ratio with $\Gamma(n{+}1)=n\,\Gamma(n)$, everything cancels except one factor, leaving the clean weight ratio (the variance follows by the same move, bumping the exponent twice):

$$\boxed{\;E[X] = \frac{\alpha}{\alpha+\beta}, \qquad \mathrm{Var}(X) = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}.\;}$$

For our hull: $E[X]=\tfrac{2}{5}=0.4$ and $\mathrm{Var}(X)=\tfrac{2\cdot 3}{5^2\cdot 6}=\tfrac{6}{150}=0.04$.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the mean as a weight ratio, $0.4$.
- *Twist (beta contains the uniform):* with $\alpha=\beta=1$, $x^{0}(1-x)^{0}=1$ and the normalizer is $1$, so $\mathrm{Beta}(1,1)=\mathrm{Unif}(0,1)$. The "flat curve" of Concept 1 is a beta in disguise.
- *General (a pure-power beta):* $\mathrm{Beta}(3,1)$ has $f(x)=3x^2$ on $(0,1)$, so $P(X>0.5)=\int_{0.5}^1 3x^2\,dx = 1-0.125 = 0.875$ and $E[X]=\tfrac{3}{4}$.
- *Edge (the mode):* for $\alpha,\beta>1$ the mode is $\tfrac{\alpha-1}{\alpha+\beta-2}$ — distinct from the mean unless symmetric; for $\mathrm{Beta}(5,2)$ the mode is $\tfrac{4}{5}=0.8$ while the mean is $\tfrac57\approx 0.714$.

**Beat 8 — Picture it.** The beta morphs from flat to leaning to symmetric as $\alpha,\beta$ change — all on $[0,1]$.

<figure>
<img src="../../assets/diagrams/ch11_beta_shapes.png" alt="Four beta densities on the unit interval, each a different color and hatch: Beta(1,1) is perfectly flat (the uniform); Beta(2,3) leans toward 0 with a dotted line marking its mean at 0.4; Beta(3,3) is symmetric and centered at one half; Beta(5,2) leans toward 1. A Chansey sprite sits in the upper-left margin." style="width:82%; max-width:660px; display:block; margin:1em auto;">
<figcaption>The beta family on $[0,1]$. $\alpha=\beta=1$ is the flat $\mathrm{Unif}(0,1)$; $\alpha<\beta$ leans toward $0$ (our barnacle hull, mean $0.4$); $\alpha=\beta$ is symmetric; $\alpha>\beta$ leans toward $1$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can recognize a "random fraction on $[0,1]$" as a beta and write its mean $\tfrac{\alpha}{\alpha+\beta}$ on sight, knowing it equals $0.5$ only when $\alpha=\beta$, and that $\mathrm{Beta}(1,1)$ *is* the uniform.

::: pokedex-entry
**POKÉDEX ENTRY №04 — Beta $\mathrm{Beta}(\alpha,\beta)$**

$$f(x)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}x^{\alpha-1}(1-x)^{\beta-1}\ (0<x<1),\quad E[X]=\frac{\alpha}{\alpha+\beta},\quad \mathrm{Var}(X)=\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}.$$

*In plain terms:* a random proportion/probability; the constant out front just normalizes the area. $\mathrm{Beta}(1,1)=\mathrm{Unif}(0,1)$.

*Recognition cue:* "a fraction between $0$ and $1$," "a random proportion/percentage," or a density $\propto x^{\alpha-1}(1-x)^{\beta-1}$ on $(0,1)$ → beta. Mean is the weight ratio $\alpha/(\alpha+\beta)$.
:::

## Concept 5 — The Pareto {#concept-5-pareto}

::: enrichment
**🔬 ENRICHMENT — The Pareto (off-syllabus; not tested on Exam P)**

This box is *beyond* the Exam P syllabus — it is here because it's the next thing you'll meet on the job (and on the later CAS/SOA loss-models exams), and it sits so naturally beside the exponential that skipping it would be a shame. **Nothing here is required; nothing here is gated or counted.** Read it for the bridge, not for the test.

**The idea.** The exponential's tail dies *fast* — geometrically — so it quietly assumes catastrophes basically never happen. But real losses have **heavy tails**: most claims are modest, yet a rare few are enormous, and they dominate the risk. The **Pareto** captures exactly that. With minimum scale $x_m$ and tail index $\alpha>0$,

$$S(x) = P(X>x) = \left(\frac{x_m}{x}\right)^{\alpha}, \qquad x \ge x_m, \qquad f(x) = \frac{\alpha\,x_m^{\alpha}}{x^{\alpha+1}}.$$

The tail decays as a *power* of $x$, not an exponential — so it stays high far out. A freak wave that an exponential would call impossible is merely *rare* under a Pareto.

**The mascot.** A **Snorlax** is the picture: usually nothing happens, but when it does, it is *immense* and immovable. The heavy tail is the Snorlax in the data.

<figure>
<img src="../../assets/diagrams/ch11_pareto_tail.png" alt="A log-scale survival plot comparing two tails: the Pareto survival (a power law) stays high and decays slowly, while the exponential survival (dashed) plunges toward zero. The gap shows that catastrophic losses are far more likely under the Pareto. A Snorlax sprite sits in the lower-right margin near the heavy tail." style="width:82%; max-width:640px; display:block; margin:1em auto;">
<figcaption>On a log scale the Pareto tail stays high while the exponential plunges. The heavy tail is why catastrophe models reach for the Pareto, not the exponential — the rare-but-enormous loss (the Snorlax) stays on the table.</figcaption>
</figure>

**The strange part — the mean can be infinite.** Because the tail is so heavy, the mean only exists when $\alpha>1$ (and the variance only when $\alpha>2$):

$$E[X] = \frac{\alpha\,x_m}{\alpha-1}\ \ (\alpha>1), \qquad \text{undefined for } \alpha \le 1.$$

A distribution with no finite mean is genuinely unsettling the first time — and it is exactly why heavy-tailed risk needs its own toolkit.

*Real-world hook:* actuaries fit Paretos to catastrophe and large-loss data constantly; reinsurance on the biggest losses is priced off the tail index $\alpha$. But for **Exam P**, the uniform, exponential, gamma, and beta are the load-bearing shapes — own those cold.
:::

## Worked Examples — Faded Guidance

Four examples, fading from fully narrated to exam-speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because the exponential and the gamma are where the points live.

### Worked Example 1 — The Sonar Gap That Forgets (full narration; exponential + memorylessness)

**ARCHETYPE:** *Exponential survival, then memoryless conditioning.*

**Setup.** A sonar gap is $X\sim\mathrm{Exp}(\theta=6)$ seconds. Find (a) $P(X>9)$, and (b) given it has already been $4$ seconds, the chance it lasts past $10$ total — and the expected *remaining* wait.

**Step 1 — Identify.** A waiting time → exponential. Part (b) says "given it has already lasted $s$" → reach for memorylessness.

**Step 2 — Professor's Path (the why).** The survival function is the whole tool: $S(x)=e^{-x/\theta}$. For (a),

$$P(X>9) = e^{-9/6} = e^{-1.5} \approx 0.2231.$$

For (b), memorylessness says the elapsed $4$ seconds wash out. Algebraically,

$$P(X>10\mid X>4) = \frac{S(10)}{S(4)} = \frac{e^{-10/6}}{e^{-4/6}} = e^{-6/6} = e^{-1} \approx 0.3679,$$

and the expected remaining wait is the full mean, $\theta = 6$ seconds — *not* $6-4=2$.

**Step 3 — Trainer's Path (the fast how).** Survival is one keystroke: $P(X>9)=e^{-1.5}$. For the conditional, *don't* divide — just **reset the clock**: the extra wait is a fresh $\mathrm{Exp}(6)$, so $P(\text{extra}>6)=e^{-1}$ and expected remaining $=6$.

**Step 4 — Check & pitfall.** Sanity: $9$ seconds is $1.5$ means out, so $P(X>9)\approx 0.22$ is a believable middling tail ✓. **Pitfall:** computing expected remaining as $6-4=2$ — the fixed-appointment intuition that memorylessness explicitly forbids. *(Back-ref: Entry №02.)*

### Worked Example 2 — The Gate at the Third Ping (full narration; gamma as a sum)

**ARCHETYPE:** *Gamma = sum of exponentials; moments, then a kernel integral via the Master-Ball identity.*

**Setup.** The gate opens after the **3rd** independent ping, ticks $\mathrm{Exp}(\theta=2)$ seconds apart. Let $X$ be the total time. Find (a) $E[X]$ and $\mathrm{Var}(X)$, (b) the normalizing constant of its density $f(x)=c\,x^2 e^{-x/2}$, and (c) $P(X<2)$.

**Step 1 — Identify.** "Total time to the 3rd event, a sum of $3$ exponentials" → $X\sim\mathrm{Gamma}(\alpha=3,\theta=2)$.

**Step 2 — Professor's Path (the why).** Means and independent variances add: $E[X]=\alpha\theta=3\cdot 2=6$ and $\mathrm{Var}(X)=\alpha\theta^2=3\cdot 4=12$. For (b), the density must integrate to $1$, and the Master-Ball integral evaluates the kernel: $\int_0^\infty x^2 e^{-x/2}\,dx = \Gamma(3)\,2^3 = 2!\cdot 8 = 16$, so $c=\tfrac{1}{16}$ (matching $\tfrac{1}{\Gamma(3)\theta^3}=\tfrac{1}{2\cdot 8}=\tfrac{1}{16}$). For (c), use the gamma/Poisson link with $t/\theta = 2/2 = 1$:

$$P(X<2) = 1 - e^{-1}\!\left(1 + 1 + \tfrac{1^2}{2}\right) = 1 - 2.5\,e^{-1} = 1 - 0.9197 = 0.0803.$$

**Step 3 — Trainer's Path (the fast how).** $E=\alpha\theta=6$, $\mathrm{Var}=\alpha\theta^2=12$ on sight. For the kernel integral, match exponent $2=\alpha-1\Rightarrow\alpha=3$, answer $\Gamma(3)2^3=16$. For $P(X<2)$, the integer-shape gamma cdf is "$1$ minus a Poisson($1$) sum over $k=0,1,2$."

**Step 4 — Check & pitfall.** $E[X]=6$ is exactly $3\times$ the single-wait mean of $2$ ✓ (means add). **Pitfall:** miscounting $\alpha$ — it's the number of *waits* ($3$), not the exponent of $x$ in the density ($2$). *(Back-ref: Entry №03.)*

### Worked Example 3 — Two Contacts Racing (light guidance; minimum of exponentials)

**ARCHETYPE:** *Minimum of independent exponentials — rates add.*

**Setup.** Two independent sonar contacts each arrive as $\mathrm{Exp}(\theta=12)$. Let $T$ be the time until the **first** one. Identify $T$'s distribution and find $E[T]$.

**Identify.** "Time until the first of several independent exponentials" → the minimum; rates add. *Your move: combine the survivals.*

$$S_T(t) = P(\text{both} > t) = e^{-t/12}\,e^{-t/12} = e^{-2t/12} = e^{-t/6},$$

so $T\sim\mathrm{Exp}(\theta=6)$ and $E[T]=6$ seconds. The combined rate is $\tfrac{1}{12}+\tfrac{1}{12}=\tfrac{1}{6}$, i.e. mean $6$.

**Check & pitfall.** Two equal racers should fire *sooner* than one alone, and $6 < 12$ ✓. **Pitfall:** averaging the *means* ($\tfrac{12+12}{2}=12$) instead of adding the *rates* — the minimum is faster than either, not their average. *(Back-ref: Entry №02.)*

### Worked Example 4 — The Barnacle Fraction (exam-speed; beta recognition)

**ARCHETYPE:** *Beta read-off; mean and a tail probability.*

**Setup.** Barnacle coverage is $X\sim\mathrm{Beta}(3,1)$, i.e. $f(x)=3x^2$ on $(0,1)$. Find $E[X]$ and $P(X>0.5)$.

**Solution.** Mean is the weight ratio: $E[X]=\tfrac{\alpha}{\alpha+\beta}=\tfrac{3}{4}=0.75$. The tail integrates the pure-power density: $P(X>0.5)=\int_{0.5}^1 3x^2\,dx = [x^3]_{0.5}^1 = 1 - 0.125 = 0.875$.

**Check & pitfall.** $\alpha>\beta$ so the mean should sit *above* $\tfrac12$, and $0.75$ does ✓. **Pitfall:** guessing the mean is $0.5$ because the support is $[0,1]$ — only true when $\alpha=\beta$. *(Back-ref: Entry №04.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — Name the shape from the cue, not the algebra**

Most continuous Exam P problems are won at the *recognition* step. Drill the four cues:

- "equally likely / chosen at random from the interval / no point preferred" → **uniform**; answer by length ratios.
- "time until / time between / memoryless / constant rate" → **exponential**; survival is $e^{-x/\theta}$, and "given it lasted $s$" means **reset the clock**.
- "time until the $k$-th event / sum of $k$ exponential waits" → **gamma**; $E=\alpha\theta$, $\mathrm{Var}=\alpha\theta^2$, and any $\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx=\Gamma(\alpha)\theta^{\alpha}$.
- "a fraction / proportion / percentage between $0$ and $1$" → **beta**; mean is the weight ratio $\tfrac{\alpha}{\alpha+\beta}$.

And one parameter trap that catches more candidates than any derivation: **mean $\theta$ vs rate $\lambda=1/\theta$.** If a problem says "rate $0.2$ per minute," the mean is $\theta=5$, and the survival is $e^{-x/5}=e^{-0.2x}$. Read which one you were handed *before* you plug in.
:::

## Team Rocket's Trap

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket — Jessie, James, and Meowth, about to misread a continuous density as a probability" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Team Rocket — about to read a density as a probability</figcaption>
</figure>

::: team-rocket
**TEAM ROCKET'S TRAP**

Team Rocket has a "loss table" for their next scheme, and a wild Porygon spawns uniformly on the corridor $X\sim\mathrm{Unif}(2,10)$. Jessie needs the chance it lands in the catch-net zone $(4,7)$.

**Meowth** scribbles: *"Easy! The zone runs to $7$ out of a corridor that runs to $10$, so the chance is $\tfrac{7-4}{10} = \tfrac{3}{10} = 0.30$. We catch it three times in ten, nyah!"*

**James** doubles down on the other end: *"And reading the density, $f(5)=\tfrac{1}{8}$ — so the probability the Porygon is exactly at position $5$ is $0.125$!"*

Both are wrong, in the two canonical continuous-uniform ways. Meowth **divided by the upper endpoint $10$ instead of the true width $b-a = 10-2 = 8$**: the right answer is $\tfrac{7-4}{10-2} = \tfrac{3}{8} = 0.375$. And James **read a density height as a probability** — but $f(5)=\tfrac18$ is a *rate*, not a chance, and $P(X=5)=0$ for any continuous variable, because a single point has zero width. *One-line fix:* measure the band against $b-a$, and remember density is probability *per unit length* — only an **area** (a width times a height) is ever a probability.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

These four shapes are the actuary's everyday vocabulary for *time-to-event* and *severity*. The **exponential** models time-to-failure and inter-claim gaps (and its memorylessness is precisely why a constant-hazard component is "as good as new" until it dies); the **gamma** models a total wait or an aggregate of several exponential stages, and underpins the gamma/Poisson frequency models; the **beta** models a random *proportion* — a loss ratio, a recovery rate, a credibility weight — and is the natural prior for a probability in Bayesian credibility. The **uniform** is the simulation primitive every Monte-Carlo pricing engine starts from. *Series bridge:* you meet all four again in **Loss Models (STAM/short-term)** as severity and frequency building blocks, and the gamma/Poisson link is the seed of the **compound models** and **credibility** theory on CAS MAS-I/II. Own the recognition cues now and those later exams are re-runs.
:::

## The Smooth Wilds — Capstone Challenge

There is no gym and no badge out here — the capstone is the wilds themselves, an exam-difficulty problem that braids three of the four shapes together, solved completely.

**The challenge.** On the ferry leg, three things run at once. (i) A wild Porygon's position is $X\sim\mathrm{Unif}(0,20)$ along the deck. (ii) The sonar gap is $T\sim\mathrm{Exp}(\theta=5)$ seconds, and it has already been $3$ seconds with no ping. (iii) The fraction of the deck the Porygon's glitch-field jams is $J\sim\mathrm{Beta}(2,2)$. You may act only if **all three** of the following hold, and they are independent: the Porygon is in the front half ($X<10$); the next ping is at least $5$ more seconds away (so you have time); and the jam fraction is under one half ($J<0.5$). Find the probability of your window.

**Solution.**

*Piece 1 — the uniform.* $P(X<10) = \dfrac{10-0}{20-0} = \dfrac{10}{20} = 0.5$ (a length ratio, measured from $a=0$).

*Piece 2 — the exponential, memoryless.* "At least $5$ more seconds, given $3$ have elapsed" resets the clock: $P(T>3+5\mid T>3) = P(T>5) = e^{-5/5} = e^{-1} \approx 0.3679$. The elapsed $3$ seconds are irrelevant.

*Piece 3 — the beta.* $\mathrm{Beta}(2,2)$ is symmetric (since $\alpha=\beta$), so by symmetry about $\tfrac12$, $P(J<0.5) = 0.5$. (Check via the density $f(x)=6x(1-x)$: $\int_0^{1/2} 6x(1-x)\,dx = [3x^2 - 2x^3]_0^{1/2} = \tfrac34 - \tfrac14 = 0.5$ ✓.)

*Combine — independence multiplies.*

$$P(\text{window}) = P(X<10)\,P(T>5)\,P(J<0.5) = 0.5 \times 0.3679 \times 0.5 = 0.0920.$$

So you get your window about **$9.2\%$** of the time. The three traps the wilds set — reading the uniform from the wrong endpoint, burning down a memoryless wait, and assuming a bounded mean must be $0.5$ — are each disarmed by a recognition cue, and independence stitches the pieces into one clean product.

## The Gym Challenge — Problem Set

::: problem-set
The questline runs from quick Route legs (mechanics) through harder Gym-difficulty problems (true SOA) to an integrative Elite Challenge. Each problem is numbered CN.k, archetype-tagged, and mirrors `problems/bank.d/ch11.yaml`. Pareto items are **enrichment** — not counted toward the syllabus quotas.

**Route Trainers (mechanics).**

- **C11.1** *(uniform)* A glitching Porygon spawns at $X\sim\mathrm{Unif}(2,10)$. Find $P(4<X<7)$, $E[X]$, $\mathrm{Var}(X)$.
- **C11.2** *(exponential)* A sonar gap is $X\sim\mathrm{Exp}(\theta=6)$ sec. Find $P(X>6)$ and $P(X\le 3)$.
- **C11.3** *(gamma)* A Magneton's charge time is $X\sim\mathrm{Gamma}(\alpha=2,\theta=3)$. State $E[X]$, $\mathrm{Var}(X)$, and write $f(x)$.
- **C11.4** *(beta)* The barnacle fraction is $X\sim\mathrm{Beta}(2,3)$. Find $E[X]$, $\mathrm{Var}(X)$, and say whether the mean is below or above $\tfrac12$.
- **C11.5** *(uniform — audit)* Catch the corridor-endpoint slip: a recorder claims $P(4<X<7)=0.30$ for $X\sim\mathrm{Unif}(2,10)$. Find the true value and name the error.
- **C11.6** *(uniform)* A coordinate $X\sim\mathrm{Unif}(0,1)$ is rescaled to $Y=8X+2$. Name $Y$'s distribution and give $E[Y]$, $\mathrm{Var}(Y)$.
- **C11.7** *(exponential — decision)* Two parts have the same mean life but Part A is $\mathrm{Exp}(\theta=10)$ while Part B has a *fixed* $10$-hour life. After $8$ hours of use, which has the longer expected remaining life? Justify.

**Gym Battles (true SOA difficulty).**

<figure style="margin:1.2em auto; max-width:150px; text-align:center;">
<img src="../../assets/vs/blue.png" alt="Gary Oak, the rival, smirking — he is about to drop the theta-squared factor and burn down a memoryless wait" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Gary's lying in wait — C11.12 and C11.14 are his rival-traps (a dropped $\theta^2$, a burned-down memoryless wait).</figcaption>
</figure>

- **C11.8** *(exponential — memorylessness)* A recovery time is $\mathrm{Exp}$ with mean $20$ min; it has rested $8$ min. Find $P(\text{extra}>15)$ and the expected additional time.
- **C11.9** *(gamma — kernel recognition)* A density is $f(x)=c\,x\,e^{-x/4}$ for $x>0$. Find $c$, name the distribution and its parameters, and compute $E[X]$.
- **C11.10** *(uniform — audit, recycled Team Rocket error)* Meowth says a Porygon at $X\sim\mathrm{Unif}(2,10)$ has $P(X=5)=f(5)=\tfrac18=0.125$. State the true $P(X=5)$ and name the error.
- **C11.11** *(exponential — minimum)* Two independent contacts are each $\mathrm{Exp}(\theta=12)$. Let $T$ be the time to the first. Identify $T$'s distribution and $E[T]$.
- **C11.12** *(gamma — rival_trap)* Gary claims the wait for the 3rd of three $\mathrm{Exp}(2)$ ticks has variance $2$ (just the count). Find the true $\mathrm{Var}$ and name his error.
- **C11.13** *(beta)* The controlled share is $\mathrm{Beta}(3,1)$, i.e. $f(x)=3x^2$. Find $P(X>0.5)$ and $E[X]$.
- **C11.14** *(exponential — rival_trap)* Gary says that after waiting $4$ of an expected $6$ minutes for an $\mathrm{Exp}(6)$ event, "only $2$ minutes remain on average." Find the true expected remaining wait and name his error.
- **C11.15** *(gamma — audit)* A note states a $\mathrm{Gamma}(3,2)$ has mean $3\cdot 2^2=12$. Find the true mean and variance and name the slip.
- **C11.16** *(uniform)* For $X\sim\mathrm{Unif}(2,10)$, find the $25$th and $75$th percentiles.

**Elite Challenge (integrative / stretch).**

- **C11.17** *(integrative — decision)* Porygon position $X\sim\mathrm{Unif}(0,20)$, sonar gap $T\sim\mathrm{Exp}(5)$ already running $3$ sec, jam fraction $J\sim\mathrm{Beta}(2,2)$, all independent. Find $P(X<10)$, $P(T>5\mid T>3)$, $P(J<0.5)$, and the joint window probability. Decide whether elapsed sonar time helps you.
- **C11.18** *(gamma/Poisson link — audit)* The total time to the 3rd of three $\mathrm{Exp}(2)$ ticks is $S$. Name $S$'s distribution, give $E[S]$ and $\mathrm{Var}(S)$, and evaluate $P(S<2)$ via the integer-shape gamma (Poisson-sum) cdf.
- **C11.19** *(Pareto — ENRICHMENT, not counted)* A loss has Pareto survival $S(x)=(1/x)^{2.5}$ for $x\ge 1$. Find $P(X>4)$ and $E[X]$.
:::

## Answers

### Quick-Answer Table

| Problem | Answer | Archetype |
|---|---|---|
| C11.1 | $P=0.375$; $E[X]=6$; $\mathrm{Var}=64/12=5.\overline{3}$ | uniform |
| C11.2 | $P(X>6)=e^{-1}=0.3679$; $P(X\le3)=1-e^{-0.5}=0.3935$ | exponential |
| C11.3 | $E[X]=6$; $\mathrm{Var}=18$; $f(x)=\tfrac19 x e^{-x/3}$ | gamma |
| C11.4 | $E[X]=0.4$ (below $\tfrac12$); $\mathrm{Var}=0.04$ | beta |
| C11.5 | true $0.375$; error: divided by $10$, not $b-a=8$ | uniform (audit) |
| C11.6 | $Y\sim\mathrm{Unif}(2,10)$; $E[Y]=6$; $\mathrm{Var}=64/12$ | uniform |
| C11.7 | Part A (exponential), remaining $=10$; B remaining $=2$ | exponential (decision) |
| C11.8 | $P(\text{extra}>15)=e^{-0.75}=0.4724$; expected $=20$ min | exponential |
| C11.9 | $c=1/16$; $\mathrm{Gamma}(2,4)$; $E[X]=8$ | gamma |
| C11.10 | $P(X=5)=0$; error: density read as probability | uniform (audit) |
| C11.11 | $T\sim\mathrm{Exp}(6)$; $E[T]=6$ | exponential |
| C11.12 | $\mathrm{Var}=\alpha\theta^2=12$; error: forgot $\theta^2$ | gamma (rival_trap) |
| C11.13 | $P(X>0.5)=0.875$; $E[X]=0.75$ | beta |
| C11.14 | expected remaining $=6$; error: memoryless, not fixed | exponential (rival_trap) |
| C11.15 | $E=\alpha\theta=6$, $\mathrm{Var}=\alpha\theta^2=12$; mean is $\alpha\theta$ not $\alpha\theta^2$ | gamma (audit) |
| C11.16 | $25$th $=4$; $75$th $=8$ | uniform |
| C11.17 | $0.5$; $e^{-1}=0.3679$; $0.5$; window $=0.0920$; elapsed time irrelevant | integrative (decision) |
| C11.18 | $\mathrm{Gamma}(3,2)$; $E=6$, $\mathrm{Var}=12$; $P(S<2)=0.0803$ | gamma/Poisson (audit) |
| C11.19 | $P(X>4)=4^{-2.5}=0.03125$; $E[X]=\tfrac{2.5}{1.5}=1.\overline{6}$ | Pareto (enrichment) |

**Worked solutions.**

**C11.1.** Length ratios, from the true lower endpoint $a=2$: $P(4<X<7)=\tfrac{7-4}{10-2}=\tfrac38=0.375$. $E[X]=\tfrac{a+b}{2}=6$; $\mathrm{Var}=\tfrac{(b-a)^2}{12}=\tfrac{64}{12}=5.\overline3$. *(Entry №01.)*

**C11.2.** Survival $S(x)=e^{-x/\theta}$: $P(X>6)=e^{-6/6}=e^{-1}=0.3679$. cdf $F(x)=1-e^{-x/\theta}$: $P(X\le3)=1-e^{-3/6}=1-e^{-0.5}=0.3935$. *(Entry №02.)*

**C11.3.** $E[X]=\alpha\theta=2\cdot3=6$; $\mathrm{Var}=\alpha\theta^2=2\cdot9=18$; $f(x)=\tfrac{1}{\Gamma(2)3^2}x^{1}e^{-x/3}=\tfrac19 x e^{-x/3}$, $x>0$ (since $\Gamma(2)=1$). *(Entry №03.)*

**C11.4.** $E[X]=\tfrac{\alpha}{\alpha+\beta}=\tfrac25=0.4$ — below $\tfrac12$ (leans toward $0$). $\mathrm{Var}=\tfrac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}=\tfrac{6}{25\cdot6}=0.04$. *(Entry №04.)*

**C11.5.** Audit. The true width is $b-a=10-2=8$, so $P(4<X<7)=\tfrac38=0.375$, not $0.30$. The recorder divided by the upper endpoint $10$ instead of the width $8$. *(Entry №01.)*

**C11.6.** A positive linear map of a uniform is uniform: $Y=8X+2$ runs $0\cdot8+2=2$ to $1\cdot8+2=10$, so $Y\sim\mathrm{Unif}(2,10)$. $E[Y]=8(\tfrac12)+2=6$; $\mathrm{Var}(Y)=8^2\cdot\tfrac{1}{12}=\tfrac{64}{12}=5.\overline3$. *(Entries №01; linear-transform rules.)*

**C11.7.** Decision. The exponential is memoryless: after $8$ hours, Part A's expected remaining life is still the full mean $\theta=10$ hours. Part B has a fixed $10$-hour life, so after $8$ hours only $10-8=2$ remain. Part A has the longer expected remaining life — the memoryless part is "as good as new." *(Entry №02.)*

**C11.8.** Memoryless: the extra wait is a fresh $\mathrm{Exp}(20)$. $P(\text{extra}>15)=e^{-15/20}=e^{-0.75}=0.4724$; expected additional $=\theta=20$ min. *(Entry №02.)*

**C11.9.** The kernel $x^1 e^{-x/4}$ is a $\mathrm{Gamma}(\alpha=2,\theta=4)$. Normalize with the Master-Ball integral $\int_0^\infty x e^{-x/4}\,dx=\Gamma(2)4^2=16$, so $c=\tfrac1{16}$. $E[X]=\alpha\theta=8$. *(Entry №03.)*

**C11.10.** Audit (recycled Team Rocket error). For a continuous variable $P(X=5)=0$ — a single point has zero width. The value $f(5)=\tfrac18$ is a density (probability *per unit length*), not a probability; only an area is a probability. *(Entry №01; Team Rocket's Trap.)*

**C11.11.** The minimum of independent exponentials adds rates: $S_T(t)=e^{-t/12}e^{-t/12}=e^{-2t/12}=e^{-t/6}$, so $T\sim\mathrm{Exp}(6)$ and $E[T]=6$. *(Entry №02.)*

**C11.12.** Rival trap. Variances of independent waits add: $\mathrm{Var}=\alpha\theta^2=3\cdot2^2=12$, not $2$. Gary used the *count* of waits and dropped the $\theta^2$. (The mean is $\alpha\theta=6$.) *(Entry №03.)*

**C11.13.** $P(X>0.5)=\int_{0.5}^1 3x^2\,dx=[x^3]_{0.5}^1=1-0.125=0.875$; $E[X]=\tfrac{\alpha}{\alpha+\beta}=\tfrac34=0.75$. *(Entry №04.)*

**C11.14.** Rival trap. The exponential forgets: the expected remaining wait is the full mean $\theta=6$ minutes, regardless of the $4$ already elapsed. Gary applied fixed-appointment intuition ($6-4=2$) to a memoryless wait. *(Entry №02.)*

**C11.15.** Audit. The gamma mean is $\alpha\theta=3\cdot2=6$ (not $\alpha\theta^2$); the *variance* is $\alpha\theta^2=3\cdot4=12$. The note swapped the mean and variance formulas. *(Entry №03.)*

**C11.16.** Invert the cdf $F(x)=\tfrac{x-2}{8}$. $F(x)=0.25\Rightarrow x=2+0.25\cdot8=4$; $F(x)=0.75\Rightarrow x=2+0.75\cdot8=8$. So the quartiles are $4$ and $8$. *(Entry №01.)*

**C11.17.** Integrative decision. $P(X<10)=\tfrac{10}{20}=0.5$. Memoryless: $P(T>5\mid T>3)=P(T>5)=e^{-5/5}=e^{-1}=0.3679$. $\mathrm{Beta}(2,2)$ symmetric ⇒ $P(J<0.5)=0.5$. Independent ⇒ window $=0.5\times0.3679\times0.5=0.0920$. The elapsed $3$ sonar seconds are irrelevant (memorylessness), so waiting longer does *not* improve your window. *(Entries №01, №02, №04.)*

**C11.18.** Audit / gamma-Poisson link. Sum of three independent $\mathrm{Exp}(2)$ ⇒ $S\sim\mathrm{Gamma}(3,2)$, $E[S]=\alpha\theta=6$, $\mathrm{Var}=\alpha\theta^2=12$. Integer-shape cdf via the Poisson sum with $t/\theta=2/2=1$: $P(S<2)=1-e^{-1}(1+1+\tfrac12)=1-2.5e^{-1}=1-0.9197=0.0803$. *(Entry №03; gamma/Poisson link.)*

**C11.19.** Enrichment (not counted). Pareto $S(x)=(1/x)^{2.5}$: $P(X>4)=4^{-2.5}=0.03125$. Since $\alpha=2.5>1$, $E[X]=\tfrac{\alpha x_m}{\alpha-1}=\tfrac{2.5\cdot1}{1.5}=\tfrac{5}{3}=1.\overline6$. *(Enrichment box.)*

## Trail Cleared — the Smooth Wilds

No badge is pinned out here — the wilds award none — but the road is behind you. You can now:

- **Read any continuous uniform** as a length ratio, with mean $\tfrac{a+b}{2}$ and variance $\tfrac{(b-a)^2}{12}$, always measuring from the true lower endpoint. *(Outcome 2d → Concept 1; rematch: Concept 1, Entry №01.)*
- **Work the exponential** through its survival $e^{-x/\theta}$, and **collapse any "given it lasted $s$"** to a fresh $\mathrm{Exp}(\theta)$ with expected remaining wait $\theta$. *(Outcome 2d → Concept 2; rematch: Concept 2, Entry №02.)*
- **Recognize a gamma** as a sum of $\alpha$ exponential waits, write $\alpha\theta$ and $\alpha\theta^2$, use the Master-Ball integral, and switch among the **exponential / gamma / Poisson** views of one event stream. *(Outcome 2d → Concept 3; rematch: Concept 3, Entry №03.)*
- **Recognize a beta** as a random proportion on $[0,1]$ with mean $\tfrac{\alpha}{\alpha+\beta}$, knowing $\mathrm{Beta}(1,1)=\mathrm{Unif}(0,1)$. *(Outcome 2d → Concept 4; rematch: Concept 4, Entry №04.)*

Ahead lies the Grand Gathering, where thousands of these wild outcomes pool into a single predictable **bell** — the Normal distribution and the Central Limit Theorem.
