<!--
  file: ch12_normal_clt
  tier: A
  outcomes: 2d,3i
  tia: B.4
  locale: the Grand Gathering (Indigo League qualifier crowd)
  maps_to: the smooth continuous wilds -> the Grand Gathering — the Normal distribution & the Central Limit Theorem (why the crowd is a bell)
-->

# The Bell of Thousands {.type-normal}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with the long route from the continuous wilds converging on the Indigo Plateau, where the Grand Gathering — the League qualifier — is staged." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>The road has converged: you have crossed the smooth continuous wilds and arrived at the <em>Grand Gathering</em> — the League qualifier, where thousands of trainers pool into one predictable crowd.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "Round One — Begin!"**

The Indigo Plateau stadium is a wall of noise. Thousands of trainers have streamed in from every route in Kanto for the qualifier, and the registration board can't possibly track them one by one. Yet the League's quartermaster — a calm woman with a clipboard — is *unbothered*. She has to order the exact right number of healing potions, allot battle slots, and predict how many qualifiers will clear the first round. With ten thousand strangers in the building.

"How can you possibly plan for a crowd you've never met?" you ask.

She doesn't even look up. "Because a crowd isn't ten thousand surprises. It's one *shape*." She turns her clipboard around. On it is a curve you half-recognize — a single smooth hump, fat in the middle, thin at the tails. "Every trainer's score is its own little story — some scrappy, some lucky, some terrible. But add them up, or average them, and the chaos cancels. What's left is *this*. Always this. I don't know any one trainer. I know the **bell**."

She taps the center. "Average qualifying score lands here. I can tell you, to within a fraction of a percent, how many trainers will score above the cutoff, how many potions Round One will burn, how many upsets to expect — all from one curve and one little table." She finally looks at you. "The League is predictable *precisely because* it's enormous. The bigger the crowd, the sharper the bell."

Pikachu stares at the curve. It *feels* like magic — wildly different trainers, wildly different stories, and yet the aggregate is law-like, smooth, forecastable. There must be a reason the messy individual dissolves into a clean shape the moment you pool enough of them.

And you don't yet know it. *Why does adding up thousands of unpredictable results produce one predictable bell — and how do you read it?*
:::

## Where You Are — 60-Second Retrieval

**Rank: Ace Trainer · Badges: 6.** Six badges are pinned to your case — Cascade, Thunder, Boulder, Rainbow, Soul, and the Marsh Badge you took from Sabrina back in Saffron — and the Plateau is finally in sight. Across the continuous Act you learned that a continuous random variable has no probability *at a point*; instead, probability is **area under a density curve** $f(x)$, and the **cumulative distribution function** $F(x) = P(X \le x)$ is the running area from the left. You computed $P(a \le X \le b) = \int_a^b f(x)\,dx = F(b) - F(a)$, and you found means by $E[X] = \int x\,f(x)\,dx$.

That is the entire foundation the bell stands on. The normal distribution is just *one specific density* $f(x)$ — a particularly important one — and everything you'll do here is reading **area under it**. You will not integrate it by hand (no one can), but every idea is the area-is-probability picture you already own. Sixty seconds to confirm it before the crowd swallows you.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the continuous world**

Answer from memory; if any feels shaky, flip back before reading on.

1. For a continuous $X$, what is $P(X = 3)$ exactly? *(Answer: $0$ — a single point has zero width, hence zero area.)*
2. If $F$ is the CDF, write $P(a \le X \le b)$ in terms of $F$. *(Answer: $F(b) - F(a)$.)*
3. What does the total area under any density $f(x)$ equal? *(Answer: $1$.)*

All three instant? The bell is just a new $f$. Any hesitation? Reclaim the area picture first — it's the only prerequisite here.
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP077 "Round One — Begin!"**

Ash reaches the Indigo Plateau and the Pokémon League conference opens: thousands of qualifiers, a packed stadium, and the first preliminary round of four-on-four matches begins. *Watch this before the chapter.* On screen, no one tracks competitors individually — the conference is a sea of trainers whose **aggregate** is orderly and scheduled. That sea is exactly our subject: pool enough independent results and the crowd becomes a predictable **bell**. (The quartermaster's potion-and-slot planning is an *in-world extension* of the conference's logistics, not a scene from the episode.)
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice comes through the Pokédex over the roar of the crowd.

"The Plateau is where everything you learned about *one* random outcome pays off across *many*, Ash. The **normal distribution** is the single most important curve in all of probability — and the **Central Limit Theorem** is the reason it's everywhere. Master this and you understand why an insurer can pool thousands of unpredictable policies into a near-certain total, why a poll of a few thousand people pins down a nation, why the League can plan around ten thousand strangers. This is a **Tier A** chapter. The exam tests it directly, and every applied science downstream leans on it."

By the end of this chapter you will be able to:

- **Describe** the normal distribution $N(\mu, \sigma^2)$, **standardize** any value to a $Z$-score, and apply the **68–95–99.7 rule** for quick mental estimates. *(Outcome 2d.)*
- **Look up** normal probabilities in the standard normal ($Z$) table and **interpolate** between table rows when a $z$ falls between them. *(Outcome 2d.)*
- **State and apply the Central Limit Theorem** to a **sum** or **mean** of independent random variables — getting the mean, variance, and the standardizing $z$ right. *(Outcome 3i.)*
- **Apply the continuity correction** ($\pm 0.5$) when approximating a *discrete* sum by the normal, and **explain why** the half-step is there. *(Outcome 3i.)*

> *Exam-weight signpost.* The normal distribution and the CLT are **bread-and-butter Exam P**, and the continuity correction is a classic source of one-step-off errors that the exam loves to punish. This is a **Tier A** chapter; the CLT and the continuity correction get the most space because they are where points are won and lost.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own the Bell?**

Already fluent? Prove it. Work these four, ~3 minutes each, *with correct method* (use the $Z$-table in Appendix C, two-decimal $z$):

1. $X \sim N(50, 8^2)$. Find $P(X \le 62)$.
2. The qualifying-score average of $36$ independent trainers each has mean $30$, sd $12$. Find $P(\bar X > 33)$.
3. A player wins each of $100$ independent matches w.p. $0.5$. Using the normal approximation **with** continuity correction, find $P(X \ge 56)$ wins.
4. True or false: averaging more independent results makes the sample mean's *standard deviation* larger.

*(Answers: $0.9332$; $0.0668$; $\approx 0.1357$; **false** — it shrinks like $1/\sqrt{n}$.)* Four for four with the right reasoning? **Skip to the Gym Challenge.** Any miss or hesitation? The teaching below was built exactly for you — and each concept has its own skip-gate, so even a partial owner loses no time.
:::

---

Five ideas build on one another here, in TIA order and in increasing difficulty. We teach them **in order**, each with its own "do you already own this?" skip-check, then the full nine-beat lesson, then a Pokédex Entry you can carry into the exam:

1. **The normal distribution** — the bell, standardization, and the 68–95–99.7 rule
2. **Reading the $Z$-table** — and interpolating between rows
3. **The Central Limit Theorem** — why sums and means of *anything* go normal *(the engine)*
4. **The continuity correction** — the $\pm 0.5$ half-step when a discrete sum borrows the bell
5. **The lognormal** — *enrichment*: what happens when you exponentiate a normal

## Concept 1 — The Normal Distribution: the Bell, Standardized

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Normal & the Z-score**

A trainer's score is $X \sim N(\mu = 70, \sigma^2 = 64)$. A score of $86$ is how many standard deviations above the mean — and roughly what fraction of trainers score below it?

If you instantly said **$z = (86-70)/8 = 2.0$**, and "about $97.7\%$ score below" (from the 68–95–99.7 rule, since $\pm 2\sigma$ holds $95\%$, leaving $2.5\%$ in the upper tail), you own this — **skip to Concept 2**. If the $\sigma = 8$ (not $64$) tripped you, or you couldn't place $z = 2$ on the rule, read on.
:::

**Beat 1 — The one-sentence idea.** *The normal distribution is one specific bell-shaped density, fully pinned down by its center $\mu$ and spread $\sigma$; once you measure any value in "standard deviations from the mean," every normal becomes the* same *standard bell.*

**Beat 2 — Anchor + concrete instance.** This is just a new density $f(x)$ to put under the area-is-probability machine you already own. The League's quartermaster says qualifying scores are $X \sim N(\mu = 50, \sigma = 8)$ — centered at $50$, with a typical wobble of $8$ points. A trainer scores $62$. *How unusual is that, and what fraction of the field did they beat?*

**Beat 3 — Reason through it in plain words.** A raw score of $62$ means nothing until you ask *how far from the center, in units of the natural wobble*. The mean is $50$, the spread is $8$, so $62$ sits $62 - 50 = 12$ points above the mean — which is $12 / 8 = 1.5$ "spreads" up. That number, $1.5$, is the only thing that matters: a score $1.5$ standard deviations above the mean is in the same *relative* position whether the test was scored out of $100$ or out of a million. Convert to that universal scale and you can read everything off **one** curve.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is using the **variance** where the **standard deviation** belongs. The problem may hand you $\sigma^2 = 64$, and it is desperately tempting to write

$$z = \frac{62 - 50}{64} = 0.1875. \qquad\textbf{(wrong — divided by the variance)}$$

But the $z$-score measures distance in **standard deviations**, and $\sigma = \sqrt{64} = 8$, not $64$. The correct $z = (62-50)/8 = 1.5$. Whenever a normal is written $N(\mu, \sigma^2)$, the **second number is the variance** — take its square root before you standardize. Mixing up $\sigma$ and $\sigma^2$ is the single most common normal-distribution slip.

**Beat 5 — Translate into notation, one glyph at a time.** We write

$$X \sim N(\mu, \sigma^2) \qquad \text{read aloud: ``}X \text{ is normal with mean } \mu \text{ and variance } \sigma^2\text{.''}$$

The squiggle $\sim$ reads **"is distributed as."** The density itself is

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2},$$

but you will **never integrate this by hand** — it has no elementary antiderivative. That is *exactly why* the table exists. The move that rescues you is the **standardization**:

$$Z = \frac{X - \mu}{\sigma} \qquad \text{read aloud: ``}Z \text{ is } X \text{, minus its mean, divided by its standard deviation.''}$$

Subtracting $\mu$ **slides** the curve so its center sits at $0$; dividing by $\sigma$ **squeezes** it so its spread becomes $1$. The result is the **standard normal**, written $Z \sim N(0,1)$, whose CDF gets its own symbol:

$$\Phi(z) = P(Z \le z) \qquad \text{read aloud: ``capital Phi of } z\text{'' = the area under the standard bell to the left of } z.$$

**Beat 6 — Derive why standardizing preserves the probability.** This is not a magic trick — the area is genuinely the same. Take any event $X \le x$ and run both sides through the *same* operation: subtract $\mu$, divide by $\sigma$ (a positive number, so the inequality direction holds):

$$P(X \le x) = P\!\left(\frac{X - \mu}{\sigma} \le \frac{x - \mu}{\sigma}\right) = P\!\left(Z \le \frac{x-\mu}{\sigma}\right) = \Phi\!\left(\frac{x-\mu}{\sigma}\right).$$

Every step is an *equivalent rewriting of the same event* — we didn't change which outcomes are included, only the ruler we measure them with. The shaded area is literally unchanged; we just relabeled the axis from "battle-points" to "standard deviations." That is why **one** table for $N(0,1)$ answers questions about **every** normal.

<figure>
<img src="../../assets/diagrams/ch12_standardize.png" alt="Two side-by-side bell curves. Left: a normal centered at mu=50 with sigma=8, shaded from the left up to x=62. Right: the standard normal N(0,1), shaded from the left up to z=1.5. A green arrow connects them with the label z=(62-50)/8=1.5, and a note 'same shaded area' shows the probability is identical in both pictures." style="width:88%; max-width:680px; display:block; margin:1em auto;">
<figcaption>Standardizing slides the curve by $\mu$ and squeezes it by $\sigma$. The shaded probability is the same in both pictures — so one $Z$-table serves every normal.</figcaption>
</figure>

**Beat 7 — Ramp the difficulty.**

- *Simplest:* convert one value. $X \sim N(50, 8^2)$, $x = 62 \Rightarrow z = 1.5$; the rule (next bullet) or table gives the area.
- *The 68–95–99.7 rule (memorize this):* for **any** normal, about **$68\%$** of the mass lies within $\pm 1\sigma$ of the mean, **$95\%$** within $\pm 2\sigma$, and **$99.7\%$** within $\pm 3\sigma$. So a value $2\sigma$ above the mean beats about $97.5\%$ of the field ($95\%$ in the middle, plus half the remaining $5\%$ below). This is your no-table sanity check.
- *Twist (the tail and symmetry):* the bell is symmetric, so $P(Z \le -z) = P(Z \ge z) = 1 - \Phi(z)$. To find an *upper* tail $P(X > x)$, compute $1 - \Phi(z)$.
- *Edge (interval):* $P(a \le X \le b) = \Phi\!\left(\tfrac{b-\mu}{\sigma}\right) - \Phi\!\left(\tfrac{a-\mu}{\sigma}\right)$ — standardize both ends, subtract the areas.

**Beat 8 — Picture it.** The figure below makes the 68–95–99.7 rule concrete: three nested bands under the same bell, each labeled with the fraction of trainers it holds.

<figure>
<img src="../../assets/diagrams/ch12_normal_6895997.png" alt="A standard bell curve with three nested shaded bands: the innermost (plus or minus one standard deviation) labeled 68 percent, the next (plus or minus two) labeled 95 percent, and the widest (plus or minus three) labeled 99.7 percent. The horizontal axis is marked mu minus 3 sigma through mu plus 3 sigma." style="width:84%; max-width:640px; display:block; margin:1em auto;">
<figcaption>The 68–95–99.7 rule: the share of any normal population within $1$, $2$, and $3$ standard deviations of the mean. Memorize it — it is your mental check before you ever reach for the table.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now turn any normal value into a $z$-score (dividing by $\sigma$, never $\sigma^2$), use the 68–95–99.7 rule for an instant estimate, and convert a probability question about $X$ into an area $\Phi(z)$ under the one standard bell. Reading that area off the table is Concept 2.

::: pokedex-entry
**POKÉDEX ENTRY №01 — The Normal Distribution & Standardization**

If $X \sim N(\mu, \sigma^2)$ then
$$Z = \frac{X - \mu}{\sigma} \sim N(0,1), \qquad P(X \le x) = \Phi\!\left(\frac{x - \mu}{\sigma}\right).$$

**68–95–99.7 rule:** $\approx 68\%$ within $\pm 1\sigma$, $\approx 95\%$ within $\pm 2\sigma$, $\approx 99.7\%$ within $\pm 3\sigma$. **Symmetry:** $\Phi(-z) = 1 - \Phi(z)$, and $P(X > x) = 1 - \Phi(z)$.

*In plain terms:* measure every value in standard deviations from the mean, and every normal collapses onto one curve you can look up.

*Recognition cue:* the words **"normally distributed," "$N(\mu,\sigma^2)$," "bell-shaped,"** or a mean-and-sd pair with a "find the probability" — **standardize first.** Beware: the second argument is the **variance**; square-root it.
:::

## Concept 2 — Reading the $Z$-Table (and Interpolating)

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Z-table**

You've standardized to $z = 1.5$. Using the table, $\Phi(1.5) = 0.9332$. Now you need $\Phi(0.83)$, but your table only prints $\Phi(0.80) = 0.7881$ and $\Phi(0.90) = 0.8159$. What's $\Phi(0.83)$, to four decimals, by **linear interpolation**?

If you got **$\approx 0.7964$** (going $30\%$ of the way from $0.7881$ toward $0.8159$), **skip to Concept 3**. If you grabbed the nearer row's value, or weren't sure how to weight, read on.
:::

**Beat 1 — The one-sentence idea.** *The $Z$-table is a lookup of $\Phi(z) = P(Z \le z)$; when your $z$ lands between two printed rows, slide proportionally between their two areas.*

**Beat 2 — Anchor + concrete instance.** Concept 1 turned every probability into "find $\Phi(z)$." Now we actually fetch the number. Suppose a trainer's standardized score is $z = 1.23$. The table prints rows at $z = 1.2$ and $z = 1.3$ but nothing in between. *What is $\Phi(1.23)$?*

**Beat 3 — Reason through it in plain words.** Read the two bracketing rows: $\Phi(1.20) = 0.8849$ and $\Phi(1.30) = 0.9032$. Your target $1.23$ sits **three-tenths of the way** from $1.20$ to $1.30$ (because $1.23 - 1.20 = 0.03$ is $30\%$ of the $0.10$ gap). So $\Phi(1.23)$ should sit about three-tenths of the way from $0.8849$ up to $0.9032$. The two areas differ by $0.9032 - 0.8849 = 0.0183$; take $30\%$ of that, $0.30 \times 0.0183 = 0.0055$, and add it on:

$$\Phi(1.23) \approx 0.8849 + 0.0055 = 0.8904.$$

(The exact value is $0.8907$; linear interpolation is plenty accurate for the exam, where the printed table-method answer is what's graded.)

**Beat 4 — Surface and dismantle the tempting wrong idea.** Under time pressure people **round $z$ to the nearer printed row** and read that:

$$z = 1.23 \to \text{``nearest row } 1.2\text{''} \Rightarrow \Phi \approx 0.8849. \qquad\textbf{(crude — off by } 0.006\text{)}$$

That can shift your final answer enough to land on the wrong multiple-choice option. The fix is to **interpolate**, not snap. (When a question *gives* you a table that already prints two decimals of $z$, just read it directly — interpolation is for the gap between rows.)

**Beat 5 — Translate into notation, one glyph at a time.** Suppose your $z$ falls between two table entries $z_0 < z < z_1$ with known $\Phi(z_0)$ and $\Phi(z_1)$. The **interpolation fraction** is

$$t = \frac{z - z_0}{z_1 - z_0} \qquad \text{read aloud: ``how far along the gap } z \text{ sits, as a fraction.''}$$

Then the **linear interpolation** is

$$\Phi(z) \approx \Phi(z_0) + t\,\big[\Phi(z_1) - \Phi(z_0)\big] \qquad \text{read aloud: ``start value plus } t \text{ of the rise.''}$$

**Beat 6 — Derive it from "constant slope between rows."** Over a tiny interval, treat $\Phi$ as a straight line connecting the two known points $(z_0, \Phi(z_0))$ and $(z_1, \Phi(z_1))$. A straight line has constant slope

$$\text{slope} = \frac{\Phi(z_1) - \Phi(z_0)}{z_1 - z_0},$$

so the value at $z$ is the start value plus slope times the horizontal step $(z - z_0)$:

$$\Phi(z) \approx \Phi(z_0) + \frac{\Phi(z_1) - \Phi(z_0)}{z_1 - z_0}\,(z - z_0) = \Phi(z_0) + t\,\big[\Phi(z_1) - \Phi(z_0)\big].$$

That is the formula in Beat 5 — it is nothing but "rise over run, applied a fraction $t$ of the way along."

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $z$ already on a printed row — read it straight, no interpolation.
- *Standard:* $z = 1.23$ between rows — interpolate, as above, $\approx 0.8904$.
- *Twist (negative $z$ / upper tail):* tables often print only $z \ge 0$. For $z < 0$ use symmetry $\Phi(-z) = 1 - \Phi(z)$; for an upper tail $P(Z > z) = 1 - \Phi(z)$.
- *Edge (inverse lookup — find $z$ from a probability):* for a percentile, scan the table *body* for the area and read off the $z$. The exam-critical ones to **memorize**: $\Phi(1.28) \approx 0.90$, $\Phi(1.645) \approx 0.95$, $\Phi(1.96) \approx 0.975$, $\Phi(2.33) \approx 0.99$.

**Beat 8 — Picture it (the table excerpt).** Here is the slice of the standard normal table you most often need, with the interpolation worked example highlighted.

<figure>
<table style="margin:1em auto; border-collapse:collapse; font-size:0.92em; text-align:center;">
<caption style="caption-side:top; font-style:italic; font-size:0.85em; padding-bottom:6px;">Excerpt of the standard normal table $\Phi(z) = P(Z \le z)$ (full table in Appendix C).</caption>
<thead>
<tr style="background:#A8A878; color:white;"><th style="padding:4px 12px;">$z$</th><th style="padding:4px 12px;">$0.0$</th><th style="padding:4px 12px;">$0.2$</th><th style="padding:4px 12px;">$0.5$</th><th style="padding:4px 12px;">$1.0$</th><th style="padding:4px 12px;">$1.2$</th><th style="padding:4px 12px;">$1.3$</th><th style="padding:4px 12px;">$1.5$</th><th style="padding:4px 12px;">$1.645$</th><th style="padding:4px 12px;">$1.96$</th><th style="padding:4px 12px;">$2.0$</th></tr>
</thead>
<tbody>
<tr><td style="padding:4px 12px;">$\Phi(z)$</td><td style="padding:4px 12px;">$.5000$</td><td style="padding:4px 12px;">$.5793$</td><td style="padding:4px 12px;">$.6915$</td><td style="padding:4px 12px;">$.8413$</td><td style="padding:4px 12px; background:#FFF6D6;">$.8849$</td><td style="padding:4px 12px; background:#FFF6D6;">$.9032$</td><td style="padding:4px 12px;">$.9332$</td><td style="padding:4px 12px;">$.9500$</td><td style="padding:4px 12px;">$.9750$</td><td style="padding:4px 12px;">$.9772$</td></tr>
</tbody>
</table>
<figcaption>To get $\Phi(1.23)$, interpolate between the two highlighted cells: $0.8849 + 0.30(0.9032 - 0.8849) \approx 0.8904$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now fetch any $\Phi(z)$ — straight off a row, interpolated between rows, flipped by symmetry for the lower/upper tail, or run *backward* to find a $z$ from a target probability. With Concepts 1–2 you can answer any "normal probability" question. Concept 3 is the reason normality shows up at all.

::: pokedex-entry
**POKÉDEX ENTRY №02 — The $Z$-Table & Interpolation**

For $z_0 < z < z_1$:
$$\Phi(z) \approx \Phi(z_0) + \underbrace{\frac{z - z_0}{z_1 - z_0}}_{t}\,\big[\Phi(z_1) - \Phi(z_0)\big].$$

Symmetry: $\Phi(-z) = 1 - \Phi(z)$; upper tail $P(Z > z) = 1 - \Phi(z)$. Memorize: $\Phi(1.28)\approx 0.90$, $\Phi(1.645)\approx 0.95$, $\Phi(1.96)\approx 0.975$, $\Phi(2.33)\approx 0.99$.

*In plain terms:* the table gives left-tail area; when your $z$ is between rows, slide proportionally between the two areas.

*Recognition cue:* you have a $z$ and need a probability (or vice-versa) → **look it up; interpolate if between rows; use symmetry for tails.**
:::

## Concept 3 — The Central Limit Theorem (the Engine)

::: concept-gate
**DO YOU ALREADY OWN THIS? — The CLT**

A trainer's match length has mean $\mu = 30$ min and sd $\sigma = 12$ min — and a *skewed*, non-normal shape. You average the lengths of $36$ independent matches. What are the mean and standard deviation of that average $\bar X$, and why may you treat $\bar X$ as approximately normal?

If you said **mean $30$, sd $12/\sqrt{36} = 2$, approximately normal by the CLT because $\bar X$ is an average of many independent pieces (the parent's skew doesn't matter)**, **skip to Concept 4**. If you wrote sd $= 12$, or thought the parent had to be normal, this is the most important section in the chapter.
:::

**Beat 1 — The one-sentence idea.** *Add up (or average) enough independent random variables and the result is approximately normal — no matter what shape the individual pieces had — with a mean and variance you can compute exactly.*

**Beat 2 — Anchor + concrete instance.** This is the answer to the cold open. One trainer's score is unpredictable and lopsided; pool thousands and the lopsidedness *cancels*, leaving a bell. Concretely: each qualifying match runs $\mu = 30$ minutes on average with sd $\sigma = 12$, but the distribution is right-skewed (most matches are quick, a few drag on forever). The League schedules $36$ matches on a court and cares about the **average** match length $\bar X$. *What is the distribution of $\bar X$?*

**Beat 3 — Reason through it in plain words.** Each match is its own little gamble — short or long, you can't predict one. But when you average $36$ of them, a freakishly long match gets diluted by the quick ones around it; the high and low surprises *partially cancel*. The more matches you average, the more the cancellation, and the tighter and more symmetric the average becomes. The CLT promises three things: (1) the average is centered exactly at the per-match mean $\mu = 30$; (2) its spread is *smaller* than a single match's — specifically $\sigma/\sqrt{n} = 12/\sqrt{36} = 2$; and (3) its shape is approximately a **bell**, even though one match's shape is skewed. So $\bar X \approx N(30, 2^2)$, and now everything from Concepts 1–2 applies.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The killer error is keeping the **single-item standard deviation** for the average:

$$\text{sd}(\bar X) \overset{?}{=} 12. \qquad\textbf{(wrong — that's the spread of ONE match)}$$

Averaging *reduces* variability — that's the entire point of pooling. The variance of the **mean** is the variance of one item *divided by $n$*: $\text{Var}(\bar X) = \sigma^2/n = 144/36 = 4$, so $\text{sd}(\bar X) = \sqrt{4} = 2$, not $12$. (The mirror error appears for **sums**: $\text{sd}(\text{sum}) = \sigma\sqrt{n}$, which *grows*. Confusing the sum's $\sqrt{n}$ with the mean's $1/\sqrt{n}$ is the second-most-common CLT mistake.) Always ask: am I standardizing a **sum** or a **mean**?

**Beat 5 — Translate into notation, one glyph at a time.** Let $X_1, X_2, \dots, X_n$ be **independent and identically distributed** (i.i.d.) with mean $\mu$ and variance $\sigma^2$. The two quantities the CLT speaks about:

$$S_n = \sum_{i=1}^{n} X_i \quad (\text{the sum}), \qquad \bar X = \frac{S_n}{n} \quad (\text{the mean}).$$

The CLT says that for large $n$,

$$S_n \;\overset{\text{approx}}{\sim}\; N\!\big(n\mu,\; n\sigma^2\big), \qquad \bar X \;\overset{\text{approx}}{\sim}\; N\!\left(\mu,\; \frac{\sigma^2}{n}\right).$$

The symbol $\overset{\text{approx}}{\sim}$ reads **"is approximately distributed as."** To find a probability, **standardize** exactly as in Concept 1, but with the *right* mean and sd:

$$Z = \frac{\bar X - \mu}{\sigma/\sqrt{n}} \quad (\text{for a mean}), \qquad Z = \frac{S_n - n\mu}{\sigma\sqrt{n}} \quad (\text{for a sum}).$$

**Beat 6 — Derive the mean and variance (the parts you *can* prove).** The CLT's *shape* claim (that it goes normal) is deep and we state it as a theorem. But the **mean and variance are not magic** — they follow from rules you already have. Using linearity of expectation and the variance rule for sums of *independent* variables:

$$E[S_n] = \sum_{i=1}^n E[X_i] = n\mu, \qquad \text{Var}(S_n) = \sum_{i=1}^n \text{Var}(X_i) = n\sigma^2$$

(the variance adds because the $X_i$ are independent — no covariance cross-terms). For the **mean** $\bar X = S_n/n$, pull the constant $1/n$ out, squaring it inside the variance:

$$E[\bar X] = \frac{1}{n}\,E[S_n] = \mu, \qquad \text{Var}(\bar X) = \frac{1}{n^2}\,\text{Var}(S_n) = \frac{1}{n^2}\cdot n\sigma^2 = \frac{\sigma^2}{n}.$$

So $\text{sd}(\bar X) = \sigma/\sqrt{n}$ — derived, not asserted. The $1/n^2$ comes from $\text{Var}(aX) = a^2\text{Var}(X)$ with $a = 1/n$; that squared constant is *exactly* why the spread shrinks like $1/\sqrt{n}$ rather than $1/n$.

**Beat 7 — Ramp the difficulty.**

- *Simplest (a mean):* $\bar X \approx N(\mu, \sigma^2/n)$; standardize with sd $\sigma/\sqrt{n}$. (The match-length example, $\bar X \approx N(30, 4)$.)
- *A sum:* total of $n$ items $\approx N(n\mu, n\sigma^2)$; standardize with sd $\sigma\sqrt{n}$. (Total claims, total match time on a court.)
- *Twist (how big must $n$ be?):* a common rule of thumb is $n \ge 30$; the more skewed the parent, the larger $n$ you want. If the parent is *already* normal, the sum/mean is **exactly** normal for any $n$.
- *Edge (a discrete parent):* if the $X_i$ are integer-valued (coin flips, claim counts), the sum is discrete and the smooth normal needs the **continuity correction** of Concept 4.

**Beat 8 — Picture it.** The figure shows the engine in action: start with a clearly *skewed* parent, average more and more of them, and watch the bell emerge — tighter each time.

<figure>
<img src="../../assets/diagrams/ch12_clt_convergence.png" alt="Three histograms side by side, all built from the same right-skewed parent distribution. For n=1 the histogram is sharply skewed and a red CLT-normal curve fits poorly. For n=5 the histogram of sample means is less skewed and the normal fits better. For n=30 the histogram is symmetric and tightly matches the red normal curve, and is much narrower. Real Pokemon sprites float above each panel to represent pooling many independent trainers." style="width:92%; max-width:760px; display:block; margin:1em auto;">
<figcaption>The CLT in action: averaging a skewed parent. As $n$ grows, the distribution of $\bar X$ becomes more bell-shaped *and* narrower (spread $\propto 1/\sqrt{n}$). The parent's shape is irrelevant — only $\mu$, $\sigma$, and $n$ survive.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now take a sum or a mean of many independent pieces, write down its exact mean and variance, recognize it's approximately normal, and standardize with the **right** sd ($\sigma\sqrt{n}$ for a sum, $\sigma/\sqrt{n}$ for a mean). This is the workhorse of the entire chapter — and when the pieces are discrete, you'll add the half-step correction next.

::: pokedex-entry
**POKÉDEX ENTRY №03 — The Central Limit Theorem**

For i.i.d. $X_1,\dots,X_n$ with mean $\mu$, variance $\sigma^2$, and large $n$:
$$S_n = \sum X_i \;\overset{\text{approx}}{\sim}\; N(n\mu,\, n\sigma^2), \qquad \bar X \;\overset{\text{approx}}{\sim}\; N\!\left(\mu,\, \tfrac{\sigma^2}{n}\right).$$
Standardize: $\;Z = \dfrac{S_n - n\mu}{\sigma\sqrt{n}}\;$ (sum) or $\;Z = \dfrac{\bar X - \mu}{\sigma/\sqrt{n}}\;$ (mean).

*In plain terms:* sums and averages of many independent things are approximately normal, *whatever* the parent's shape. A sum's spread **grows** like $\sqrt{n}$; a mean's spread **shrinks** like $1/\sqrt{n}$.

*Recognition cue:* **"sum / total / average of $n$ independent…," "large sample," "approximately."** Decide sum-vs-mean, plug in $n\mu, n\sigma^2$ or $\mu, \sigma^2/n$, then standardize.
:::

## Concept 4 — The Continuity Correction (the $\pm 0.5$ Half-Step)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Continuity Correction**

A player wins each of $100$ independent matches with probability $0.5$; let $X$ be the number of wins, so $\mu = 50$, $\sigma = 5$. Approximate $P(X \ge 56)$ by the normal — *with* the continuity correction.

If you wrote **$P(X \ge 56) \approx P(Y > 55.5) = 1 - \Phi(1.10) = 0.1357$** (note the $55.5$, not $56$), **skip to Concept 5**. If you used $56$ and got $1 - \Phi(1.20) = 0.1151$, read on — that's the exact error Team Rocket is about to make.
:::

**Beat 1 — The one-sentence idea.** *When a smooth normal stands in for a discrete (integer-valued) sum, each integer secretly occupies a bar of width $1$, so you must stretch the boundary by a half-step ($\pm 0.5$) to capture the whole bar.*

**Beat 2 — Anchor + concrete instance.** The CLT (Concept 3) told us a sum of $100$ wins is approximately normal. But "number of wins" is a **discrete** count — $55, 56, 57$ — while the normal is a **smooth** curve over all real numbers. Concretely: $X = $ wins out of $100$ at $p = 0.5$, so $\mu = np = 50$ and $\sigma = \sqrt{np(1-p)} = \sqrt{25} = 5$. *What is $P(X \ge 56)$?*

**Beat 3 — Reason through it in plain words.** Picture the discrete probabilities as a row of bars, one centered on each integer, each **one unit wide**. The bar for "$56$" isn't a thin spike at $56$ — it stretches from $55.5$ to $56.5$. So when you ask for $P(X \ge 56)$ — every bar from $56$ upward — those bars begin at the **left edge** of the $56$ bar, which is $55.5$, *not* $56$. If you start the smooth curve's area at $56$, you slice the $56$ bar in half and throw away the left portion. To capture the *whole* bars from $56$ on, the normal area must start at $55.5$. That half-unit is the continuity correction.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The natural move is to standardize the integer boundary directly:

$$P(X \ge 56) \overset{?}{\approx} P(Y \ge 56) = 1 - \Phi\!\left(\tfrac{56 - 50}{5}\right) = 1 - \Phi(1.20) = 0.1151. \qquad\textbf{(wrong — chops off half the 56-bar)}$$

This undercounts, because it ignores the left half of the $56$ bar (from $55.5$ to $56$). The correct version stretches to the bar's edge:

$$P(X \ge 56) \approx P(Y > 55.5) = 1 - \Phi\!\left(\tfrac{55.5 - 50}{5}\right) = 1 - \Phi(1.10) = 0.1357.$$

The gap ($0.1151$ vs $0.1357$) is large enough to change a multiple-choice answer. **Forgetting the half-step is the single most punished error in normal approximation** — and it's exactly what Team Rocket does below.

**Beat 5 — Translate into notation, one glyph at a time.** Let $X$ be an integer-valued sum approximated by $Y \sim N(\mu, \sigma^2)$. The correction always **expands the region by $0.5$ on each included end.** The four cases you must keep straight:

| Discrete event | Continuity-corrected normal event |
|---|---|
| $P(X \ge a)$ ("$a$ or more") | $P(Y > a - 0.5)$ |
| $P(X > a)$ ("more than $a$", i.e. $\ge a+1$) | $P(Y > a + 0.5)$ |
| $P(X \le b)$ ("$b$ or fewer") | $P(Y < b + 0.5)$ |
| $P(X = k)$ (exactly $k$) | $P(k - 0.5 < Y < k + 0.5)$ |

The rule of thumb that generates every row: **draw the bars you want to include, then push the boundary out to the *outer edge* of the last bar you're keeping.** "$\ge 56$" keeps bar $56$, whose left edge is $55.5$; "$> 56$" excludes bar $56$ and starts at bar $57$, whose left edge is $56.5$.

**Beat 6 — Derive *why* it's exactly $0.5$.** The discrete pmf assigns all of integer $k$'s probability to the single point $k$. To approximate that point-mass with a smooth density, you spread $k$'s probability **uniformly over the unit interval centered at $k$** — from $k - \tfrac12$ to $k + \tfrac12$ — because that interval is the set of real numbers that round to $k$. (Each integer "owns" the territory within half a unit of itself; that's the definition of rounding.) So the discrete event "$X \ge 56$" maps to the continuous region "$Y$ in any bar from $56$ up" = "$Y > 55.5$." The half comes directly from the unit width of each bar split evenly around its center — there's nothing arbitrary about it.

**Beat 7 — Ramp the difficulty.**

- *Simplest (one-sided):* $P(X \ge 56) \approx P(Y > 55.5)$, as above $= 0.1357$.
- *Two-sided interval:* $P(54 \le X \le 56) \approx P(53.5 < Y < 56.5) = \Phi(1.30) - \Phi(0.70) = 0.9032 - 0.7580 = 0.1452$. Stretch the *lower* end down by $0.5$ and the *upper* end up by $0.5$.
- *Exactly-one-value:* $P(X = 55) \approx P(54.5 < Y < 55.5) = \Phi(1.10) - \Phi(0.90) = 0.8643 - 0.8159 = 0.0484$ — a sliver one bar wide.
- *Edge (when to skip it):* if the underlying variable is **already continuous** (a sum of continuous claim sizes, say), there are no bars — **no correction**. The half-step is *only* for discrete counts.

**Beat 8 — Picture it.** The figure overlays the discrete bars on the smooth normal, with the half-step boundaries marked, so you can *see* the bar edges the correction is reaching for.

<figure>
<img src="../../assets/diagrams/ch12_continuity_correction.png" alt="A discrete binomial probability histogram (n=100, p=0.5) drawn as unit-width bars, overlaid with a smooth red normal curve of the same mean 50 and standard deviation 5. The bars for 54, 55, and 56 are highlighted, and dashed lines at 53.5 and 56.5 mark how those three unit-width bars span from the left edge of the 54 bar to the right edge of the 56 bar." style="width:88%; max-width:680px; display:block; margin:1em auto;">
<figcaption>Each discrete bar has width $1$, centered on its integer. To capture bars $54$–$56$ with the smooth curve, the area must run from $53.5$ to $56.5$ — the outer edges. That stretch is the continuity correction.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now approximate any discrete sum by the normal and adjust the boundary by the right $\pm 0.5$ — expanding to the outer edge of every bar you keep. Decide *discrete vs continuous* first (only discrete gets the correction), draw the bars if unsure, then standardize the half-stepped boundary.

::: pokedex-entry
**POKÉDEX ENTRY №04 — The Continuity Correction**

When an integer-valued $X$ is approximated by $Y \sim N(\mu, \sigma^2)$, **expand the region by $0.5$ to the outer edge of every bar you keep:**
$$P(X \ge a) \approx P(Y > a - 0.5), \quad P(X \le b) \approx P(Y < b + 0.5),$$
$$P(X = k) \approx P(k - 0.5 < Y < k + 0.5), \quad P(a \le X \le b) \approx P(a - 0.5 < Y < b + 0.5).$$

*Why $0.5$:* each integer's probability is spread over the unit interval $[k - \tfrac12, k + \tfrac12]$ that rounds to it. *When to skip:* never use it for an already-continuous variable.

*Recognition cue:* a **discrete count** (binomial, Poisson, "number of…") approximated by the normal → **add the half-step.** Draw the bars and reach for their outer edges.
:::

## Concept 5 — The Lognormal {#concept-5-lognormal}

::: enrichment
**🔬 ENRICHMENT — The Lognormal (off-syllabus; not tested on Exam P)**

This box is *beyond* the Exam P syllabus — it is here because it's the next thing you'll meet on the job (and on later CAS/SOA exams), and it falls out of the normal so naturally that skipping it would be a shame. **Nothing here is required; nothing here is gated.** Read it for the bridge, not for the test.

**The idea.** Some quantities can't go normal because they can't be negative and they have a long right tail — insurance **losses**, stock prices, rare-but-huge damages. The normal, symmetric and unbounded below, is the wrong shape. But there's a beautiful fix: model the **logarithm** as normal. If

$$\ln L \sim N(\mu, \sigma^2), \qquad \text{equivalently} \qquad L = e^{Y}, \;\; Y \sim N(\mu, \sigma^2),$$

then $L$ is called **lognormal**. Because $e^{Y}$ is always positive, $L > 0$ automatically; and because exponentiating stretches the upper end far more than the lower, $L$ is **right-skewed** — exactly the shape of a loss curve, where most claims are modest but a few are catastrophic.

**Why it's natural.** Multiply many independent positive factors together (a chain of percentage shocks, say) and take the log: the log turns the product into a *sum*, the CLT (Concept 3!) makes that sum normal, so the original product is lognormal. The lognormal is to **products** what the normal is to **sums**.

**The skew ordering.** Unlike the symmetric normal (where mean = median = mode), the lognormal has $\text{mode} < \text{median} < \text{mean}$ — the long right tail drags the mean upward. The median is simply $e^{\mu}$, and the mean is $e^{\mu + \sigma^2/2}$ (the variance inflates the mean).

<figure>
<img src="../../assets/diagrams/ch12_lognormal.png" alt="A right-skewed lognormal density curve rising sharply from zero, peaking early, then trailing off in a long tail to the right. Three dashed vertical lines mark the mode (leftmost), the median, and the mean (rightmost), illustrating mode less than median less than mean. A Gyarados sprite decorates the long right tail to represent a rare, enormous loss." style="width:84%; max-width:640px; display:block; margin:1em auto;">
<figcaption>Exponentiate a normal and the symmetric bell becomes a positive, right-skewed loss curve. The long tail (where a rare Gyarados-sized loss lives) drags $\text{mean} > \text{median} > \text{mode}$.</figcaption>
</figure>

*Real-world hook:* actuaries fit lognormals to claim-severity data constantly; you'll see it again in Loss Models. But for **Exam P**, the normal and the CLT are the load-bearing ideas — own those cold.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/front/35.png" alt="Clefairy, the round, normal-type mascot of the bell curve" style="width:120px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">#35 Clefairy — the bell-shaped mascot of the Grand Gathering</figcaption>
</figure>

Five examples, fading from fully narrated to exam-speed. The first two lead with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because the CLT and the continuity correction are the load-bearing, point-scoring ideas.

### Worked Example 1 — A Single Qualifying Score (full narration; understanding-first)

**ARCHETYPE:** *Standardize a single normal value and read the table.*

**Setup.** Qualifying scores are $X \sim N(\mu = 50, \sigma = 8)$. Find (a) $P(X \le 62)$ and (b) the fraction of trainers scoring **above** $62$.

**Step 1 — Identify.** One normal variable, one value — standardize and look up. No CLT, no correction (a single continuous score).

**Step 2 — Professor's Path (the why).** Standardizing rewrites the event in standard-deviation units without changing its probability:
$$z = \frac{62 - 50}{8} = \frac{12}{8} = 1.5, \qquad P(X \le 62) = \Phi(1.5).$$
From the table, $\Phi(1.5) = 0.9332$. The upper tail is the complement: $P(X > 62) = 1 - 0.9332 = 0.0668$.

**Step 3 — Trainer's Path (the fast how, on the TI-30XS MultiView).** Store $\mu$ and $\sigma$ so you never retype them: [ 50 [STO▸]{.kbd} [x]{.kbd} [enter]{.kbd} ]{.keystroke} then [ 8 [STO▸]{.kbd} [y]{.kbd} [enter]{.kbd} ]{.keystroke}. Now the $z$-score is one expression: [ ( 62 [−]{.kbd} [x]{.kbd} ) [÷]{.kbd} [y]{.kbd} [enter]{.kbd} ]{.keystroke} returns $1.5$. Look up $\Phi(1.5) = 0.9332$ in the table.

**Step 4 — Check & pitfall.** Sanity-check with the 68–95–99.7 rule: $z = 1.5$ is between $1$ and $2$ standard deviations, so the left area should sit between $\approx 0.84$ (at $z=1$) and $\approx 0.975$ (at $z=2$) — and $0.9332$ does ✓. **Pitfall:** dividing by $\sigma^2 = 64$ instead of $\sigma = 8$ (giving a bogus $z = 0.19$). *(Back-ref: Entries №01, №02.)*

### Worked Example 2 — Planning the Court's Total Time (full narration; CLT for a sum)

**ARCHETYPE:** *CLT for a sum; standardize with $\sigma\sqrt{n}$.*

**Setup.** Each match runs $\mu = 30$ min on average with sd $\sigma = 12$ min (skewed). A court hosts $36$ independent matches. The court is booked for $1{,}140$ minutes. Find the probability the $36$ matches **overrun** the booking, i.e. $P(S_{36} > 1140)$.

**Step 1 — Identify.** A **sum** of $n = 36$ i.i.d. matches → CLT, sum form. Continuous parent, so no continuity correction.

**Step 2 — Professor's Path (the why).** The sum's exact mean and variance come from linearity and independence (Concept 3, Beat 6):
$$E[S_{36}] = n\mu = 36 \times 30 = 1080, \qquad \text{Var}(S_{36}) = n\sigma^2 = 36 \times 144 = 5184,$$
so $\text{sd}(S_{36}) = \sqrt{5184} = 72$. By the CLT, $S_{36} \approx N(1080, 72^2)$. Standardize the booking limit:
$$z = \frac{1140 - 1080}{72} = \frac{60}{72} = 0.83, \qquad P(S_{36} > 1140) = 1 - \Phi(0.83).$$
$\Phi(0.83) \approx 0.7967$ (interpolating between $\Phi(0.8) = 0.7881$ and $\Phi(0.9) = 0.8159$: $0.7881 + 0.3(0.0278) = 0.7964$ — round to the table-method $0.7967$). So $P(\text{overrun}) = 1 - 0.7967 \approx 0.2033$.

**Step 3 — Trainer's Path (the fast how).** Sum mean $= 36 \times 30 = 1080$; sum sd $= 12\sqrt{36} = 12 \times 6 = 72$. On the TI-30XS: [ ( 1140 [−]{.kbd} 1080 ) [÷]{.kbd} 72 [enter]{.kbd} ]{.keystroke} $= 0.83$; then $1 - \Phi(0.83) \approx 0.203$.

**Step 4 — Check & pitfall.** $z \approx 0.83$ is just under one sd, so the overrun probability should be a bit above $\Phi(-1)$'s $0.16$ — and $0.20$ fits ✓. **Pitfall:** using the *mean's* sd $\sigma/\sqrt{n} = 2$ instead of the *sum's* sd $\sigma\sqrt{n} = 72$. A sum's spread **grows** with $n$. *(Back-ref: Entry №03.)*

### Worked Example 3 — Did Enough Qualifiers Clear the Cut? (partial guidance; CLT for a mean)

**ARCHETYPE:** *CLT for a mean; standardize with $\sigma/\sqrt{n}$.*

**Setup.** The $36$ match lengths from WE 2 ($\mu = 30$, $\sigma = 12$). Find $P(\bar X > 33)$ — the chance the **average** match runs over $33$ minutes.

**Identify.** A **mean** of $n = 36$ → CLT, mean form, sd $= \sigma/\sqrt{n}$. *Your move: fill in the standardization.*

$$E[\bar X] = 30, \qquad \text{sd}(\bar X) = \frac{12}{\sqrt{36}} = \frac{12}{6} = 2, \qquad z = \frac{33 - 30}{2} = 1.5.$$
$$P(\bar X > 33) = 1 - \Phi(1.5) = 1 - 0.9332 = 0.0668.$$

**Check & pitfall.** Same numbers as WE 2's parent, but the **mean** has a far smaller sd ($2$, vs the sum's $72$) — averaging tightens, summing widens. **Pitfall:** using sd $= 12$ (one match) for the average. *(Back-ref: Entry №03.)*

### Worked Example 4 — The Coin-Flip Count (light guidance; CLT + continuity correction)

**ARCHETYPE:** *Normal approximation to a discrete (binomial) sum, with continuity correction.*

**Setup.** A player wins each of $100$ independent matches w.p. $0.5$; $X = $ number of wins. Find (a) $P(X \ge 56)$ and (b) $P(54 \le X \le 56)$, normal-approximated.

A binomial sum: $\mu = np = 50$, $\sigma = \sqrt{np(1-p)} = \sqrt{100(0.5)(0.5)} = 5$. **Discrete count → continuity correction.**

**(a)** Keep bars $56$ and up; left edge of bar $56$ is $55.5$:
$$P(X \ge 56) \approx P(Y > 55.5) = 1 - \Phi\!\left(\tfrac{55.5 - 50}{5}\right) = 1 - \Phi(1.10) = 1 - 0.8643 = 0.1357.$$

**(b)** Keep bars $54$–$56$; stretch to outer edges $53.5$ and $56.5$:
$$P(54 \le X \le 56) \approx \Phi\!\left(\tfrac{56.5 - 50}{5}\right) - \Phi\!\left(\tfrac{53.5 - 50}{5}\right) = \Phi(1.30) - \Phi(0.70) = 0.9032 - 0.7580 = 0.1452.$$

**Check & pitfall.** Without the correction (a) would be $1 - \Phi(1.20) = 0.1151$ — visibly different. **Pitfall:** forgetting the half-step, or stepping the wrong way ($+0.5$ where $-0.5$ belongs). *(Back-ref: Entries №03, №04.)*

### Worked Example 5 — The Percentile Cutoff (exam speed; inverse lookup)

**ARCHETYPE:** *Inverse normal — find a value from a target probability.*

**Setup.** Qualifying scores $X \sim N(50, 8^2)$. The League advances the **top $5\%$**. What is the cutoff score $c$?

Top $5\%$ means $P(X > c) = 0.05$, i.e. $\Phi(z) = 0.95$, so $z = 1.645$ (a memorized inverse value). Un-standardize:
$$c = \mu + z\sigma = 50 + 1.645(8) = 50 + 13.16 = 63.16.$$

**Check & pitfall.** A cutoff $\approx 1.6\sigma$ above the mean for the top $5\%$ matches the rule (top $\approx 2.5\%$ is at $2\sigma$, so $5\%$ is a bit below $2\sigma$) ✓. **Pitfall:** using $z = 1.96$ (that's two-tailed $5\%$) instead of the one-tailed $1.645$. *(Back-ref: Entry №02.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — Store $\mu$ and $\sigma$, then standardize in one keystroke**

Don't retype the mean and sd for every value. On the TI-30XS MultiView, bank them once: [ 50 [STO▸]{.kbd} [x]{.kbd} [enter]{.kbd} ]{.keystroke} and [ 8 [STO▸]{.kbd} [y]{.kbd} [enter]{.kbd} ]{.keystroke}. Then each $z$-score is just [ ( value [−]{.kbd} [x]{.kbd} ) [÷]{.kbd} [y]{.kbd} [enter]{.kbd} ]{.keystroke}. For a **CLT sum**, store $n\mu$ and $\sigma\sqrt n$ instead; for a **mean**, store $\mu$ and $\sigma/\sqrt n$ — pick the right pair *before* you start punching keys.
:::

::: trainers-tip
**TRAINER'S TIP — Continuity correction: apply the $\pm 0.5$ BEFORE you standardize**

The order matters. First shift the integer boundary by the half-step *(to the outer edge of every bar you keep)*, *then* divide by $\sigma$. If you standardize $56$ first and try to fudge the $z$ afterward, you'll botch the scale. Decide the corrected boundary ($55.5$, $56.5$, …) in plain integers, *then* run [ ( 55.5 [−]{.kbd} 50 ) [÷]{.kbd} 5 [enter]{.kbd} ]{.keystroke}. And the gate: **discrete count → correct; already continuous → don't.**
:::

::: trainers-tip
**TRAINER'S TIP — Sum or mean? The sd tells you which**

The most common CLT slip is the wrong standard deviation. Burn in the contrast: a **sum** spreads *wider* with more terms, sd $= \sigma\sqrt{n}$; a **mean** spreads *tighter*, sd $= \sigma/\sqrt{n}$. If your "average of 1000 trainers" has a *bigger* spread than one trainer, you've used the sum formula by mistake. Averaging always shrinks the spread.
:::

::: trainers-tip
**TRAINER'S TIP — The 68–95–99.7 sanity check**

Before trusting any table lookup, place your $z$ on the rule. A left-tail area must sit near $0.84$ at $z=1$, $0.975$ at $z=2$, $0.9985$ at $z=3$ (and the mirror tails below the mean). If your computed probability is wildly off the rule's neighborhood, you mis-standardized — likely a $\sigma$-vs-$\sigma^2$ or sum-vs-mean error.
:::

## Team Rocket's Trap

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Team Rocket — about to forget the half-step</figcaption>
</figure>

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

Team Rocket is running an illegal betting pool on the qualifier. "Da twerp wins each match fifty-fifty, an' dere's a hundred matches," Meowth crows, scribbling. "We pay out big if he gets fifty-six wins or more. I'll normal-approximate it — mean fifty, standard deviation five. So I just standardize fifty-six: $z = (56 - 50)/5 = 1.2$, an' da chance is $1 - \Phi(1.2) = 0.115$. Barely eleven percent! Set da odds, we'll clean up!"

Jessie nods. "Eleven percent. Print the tickets."

James, squinting at the ledger, hesitates. "But… wins come in whole numbers. Doesn't the bar for *fifty-six* start at *fifty-five-point-five*? Shouldn't we…"

Meowth waves a paw. "Bah! Half a win? Dere's no half a win! Fifty-six is fifty-six!" — and he prices the bet at the wrong number.

**Where it fails:** Meowth standardized the **integer** $56$ instead of the bar's **left edge** $55.5$ — he forgot the **continuity correction**. Wins are *discrete*, so the bar for $56$ runs from $55.5$ to $56.5$; "$56$ or more" starts at $55.5$. The honest value is $1 - \Phi(1.10) = 0.1357$, not $0.1151$ — nearly **$2$ percentage points higher**. James had it right. Meowth's odds underprice the payout, and the twerp's backers clean *him* out. **The fix:** for any discrete count approximated by the normal, push the boundary a half-step to the outer edge of every bar you keep — *before* standardizing.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

This is the literal reason **pooling risk works** — the foundation under every insurance company.

An insurer holds thousands of independent policies, each an unpredictable little gamble: most pay nothing, a few pay a lot. One policy is pure noise. But the **total** claims across the whole book is a *sum* of thousands of independent pieces — and by the **Central Limit Theorem**, that total is approximately **normal**, with mean $n\mu$ and standard deviation $\sigma\sqrt{n}$. The mean grows like $n$ while the sd grows only like $\sqrt{n}$, so the *relative* uncertainty (sd ÷ mean $\propto 1/\sqrt{n}$) **shrinks** as the book grows. That is the whole game: an insurer can't predict one claim, but it can predict the aggregate of a million to within a fraction of a percent — and price premiums, set reserves, and satisfy regulators against that near-certain total. The bigger the pool, the sharper the bell. Exactly the quartermaster's "the League is predictable *because* it's enormous."

The **continuity correction** shows up the instant the count is discrete — number of claims, number of deaths in a mortality table, number of lapses — where actuaries normal-approximate a binomial or Poisson and must half-step the boundary or misstate a reserve.

*Series bridge:* the CLT is the gateway to **all of statistical inference** — confidence intervals and hypothesis tests (CAS MAS-I / SOA SRM) are built on "the sample mean is approximately normal," and **aggregate loss models** (Loss Models / STAM) lean on normal and **lognormal** approximations to the total. The normal is not a one-chapter curve; it is the spine of applied actuarial science.

*Transfer check:* could you solve this with **no Pokémon in it**? "$10{,}000$ independent auto policies each have expected annual claim \$$400$ with sd \$$1{,}200$; find the probability total claims exceed \$$4.1$M." Same CLT-for-a-sum: mean $= 10000 \times 400 = 4{,}000{,}000$, sd $= 1200\sqrt{10000} = 120{,}000$, $z = (4.1\text{M} - 4.0\text{M})/120000 \approx 0.83$, $P \approx 1 - \Phi(0.83) \approx 0.203$. Identical to Worked Example 2. The skill has transferred.
:::

## The Gym Battle — the Grand Gathering Capstone

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/types/normal.png" alt="Normal type icon" style="width:90px; display:block; margin:0 auto;">
<figcaption style="font-size:0.85em;">The Grand Gathering — no badge here, just the bell of thousands.</figcaption>
</figure>

There is **no gym leader and no badge** at the Grand Gathering — this is the League qualifier, and the challenge is set by the field itself. (You keep your six badges; the next badge waits at Cinnabar.) The quartermaster lays down the real planning problem.

**The Quartermaster's Challenge.** "Round One is $2{,}500$ independent matches," she says. "Each match consumes a number of healing potions that averages $\mu = 4$ with standard deviation $\sigma = 3$ — a lumpy, skewed distribution; some matches burn nothing, a few burn a dozen. I've stocked **$10{,}150$** potions for the round. Two questions before I sign the order: (a) What's the probability Round One **runs out** of potions? (b) For a *single* featured court hosting exactly $100$ matches, what's the probability that court uses **at least $420$** potions, counting potions in whole units?"

**ARCHETYPE:** *CLT for a large sum (a), then a discrete-count CLT with continuity correction (b).*

**Step 1 — Identify both parts.** Both are **sums** of i.i.d. per-match potion use → CLT. Part (a) is a continuous-style aggregate over $n = 2500$ (no correction — we treat the large aggregate total as continuous). Part (b) is a sum over $n = 100$ asked about a discrete **count of potions** ("at least $420$, in whole units") → continuity correction.

**Step 2 — Part (a): the whole round.** Sum mean and sd:
$$E[S_{2500}] = n\mu = 2500 \times 4 = 10{,}000, \qquad \text{sd} = \sigma\sqrt{n} = 3\sqrt{2500} = 3 \times 50 = 150.$$
Standardize the stock level $10{,}150$:
$$z = \frac{10{,}150 - 10{,}000}{150} = \frac{150}{150} = 1.00, \qquad P(S_{2500} > 10{,}150) = 1 - \Phi(1.00) = 1 - 0.8413 = 0.1587.$$
So there's about a **$15.9\%$** chance Round One runs short — high enough that the quartermaster orders a buffer.

**Step 3 — Part (b): the featured court, with the half-step.** Sum over $n = 100$ matches:
$$E[S_{100}] = 100 \times 4 = 400, \qquad \text{sd} = 3\sqrt{100} = 3 \times 10 = 30.$$
The count of potions is discrete; "at least $420$" keeps bar $420$ and up, whose left edge is $419.5$:
$$P(S_{100} \ge 420) \approx P(Y > 419.5) = 1 - \Phi\!\left(\frac{419.5 - 400}{30}\right) = 1 - \Phi(0.65).$$
From the table, $\Phi(0.65) = 0.7422$, so $P \approx 1 - 0.7422 = 0.2578$ — about **$25.8\%$**.

**Step 4 — Check, verdict & the pitfall the quartermaster is testing.** Part (a): stock sits exactly $1$ sd above the mean, so the shortfall probability is the upper-tail-at-$z=1$, $0.1587$ — straight off the 68–95–99.7 rule (half of the $\approx 32\%$ outside $\pm 1\sigma$) ✓. Part (b): without the correction you'd get $1 - \Phi\!\left(\tfrac{420-400}{30}\right) = 1 - \Phi(0.67) = 0.2514$ — the half-step nudges it to $0.2578$, the exact Team-Rocket trap. The quartermaster is checking that you (1) use $\sigma\sqrt{n}$ for a sum, not $\sigma$, and (2) half-step the discrete count. Miss either and you mis-order the potions.

> "That," the quartermaster says, signing the order with a buffer, "is how you plan for ten thousand strangers. You never met one of them. You knew the bell." You've cleared the Grand Gathering — Cinnabar and the Volcano Badge are next.

## The Gym Challenge — Problem Set

::: problem-set
**THE GRAND GATHERING QUESTLINE — your mission.** The League quartermaster has deputized you as her forecasting analyst for the qualifier. This problem set is one escalating mission: the **Route Trainer** legs are warm-up forecasts (single scores, table lookups, one-shot standardizations); the **Gym Battle** tier is the real planning work (CLT sums and means, the continuity correction at exam difficulty); the **Elite Challenge** tier is optional post-game once the round is staffed. Work it timed (~6 min/problem), then check the **Answers** below. Hit the mastery bar (**80%+ with correct method**) to clear the questline. Problems first; full worked solutions follow afterward (never interleaved). Use the $Z$-table in Appendix C, **two-decimal $z$** (so your answer matches the printed table method). Markers: 🔴 routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (the early legs — single-value forecasts)

**C12.1.** 🔴 *(The quartermaster's first task: rank one qualifier.)* Qualifying scores are $X \sim N(\mu = 70, \sigma = 10)$. Find $P(X \le 85)$.

**C12.2.** 🔴 *(How rare is a top performer?)* With $X \sim N(70, 10^2)$, find $P(X > 90)$ — the fraction scoring above $90$.

**C12.3.** 🔴 *(Reading between the table rows.)* You've standardized to $z = 1.13$. Using $\Phi(1.10) = 0.8643$ and $\Phi(1.20) = 0.8849$, interpolate for $\Phi(1.13)$.

**C12.4.** 🟡 *(A score below the mean.)* With $X \sim N(70, 10^2)$, find $P(X < 58)$. *(Hint: $z$ is negative; use symmetry.)*

**C12.5.** 🟡 *(The 68–95–99.7 rule, no table.)* Scores are $N(70, 10^2)$. Using only the empirical rule, what fraction of trainers score between $50$ and $90$? Between $60$ and $80$?

**C12.6.** 🟡 *(Setting the advancement cutoff — inverse lookup.)* With $X \sim N(70, 10^2)$, the League advances the **top $10\%$**. Find the cutoff score. *(Use $\Phi(1.28) = 0.90$.)*

**C12.7.** 🔴 *(An interval of scores.)* With $X \sim N(70, 10^2)$, find $P(60 \le X \le 85)$.

> *Questline beat: the warm-up forecasts check out. The quartermaster hands you the real planning brief. The Gym Battle is the boss.*

### Gym Battles (the boss fight — true SOA difficulty)

**C12.8.** 🟡 *(CLT for a sum — total match time on a court.)* Each match runs $\mu = 25$ min, sd $\sigma = 10$ min (skewed), independent. A court hosts $n = 64$ matches. Find $P(\text{total time} > 1{,}680 \text{ min})$.

**C12.9.** 🟡 *(CLT for a mean — average wait time.)* Trainers wait $\mu = 8$ min, sd $\sigma = 6$ min for a healing slot, independent. Over $n = 100$ trainers, find $P(\bar X < 7)$ — the chance the average wait is under $7$ minutes.

**C12.10.** 🟡 *(AUDIT — Team Rocket's betting pool forgets the half-step.)* A trainer wins each of $n = 144$ independent matches w.p. $p = 0.5$; $X = $ wins. Team Rocket's note prices "$X \ge 80$" as $1 - \Phi\!\left(\tfrac{80 - 72}{6}\right) = 1 - \Phi(1.33) = 0.0918$. Find the **continuity-corrected** $P(X \ge 80)$ and name Team Rocket's error.

**C12.11.** 🟡 *(Continuity correction — exactly-a-count.)* With the same $X \sim$ Binomial$(144, 0.5)$ ($\mu = 72$, $\sigma = 6$), approximate $P(X = 75)$ using the continuity correction.

**C12.12.** 🔵 *(RIVAL TRAP — Gary brags about averaging.)* Match scores have mean $\mu = 60$, sd $\sigma = 20$. Gary says: "I'll average $25$ matches; my average is just as spread out as one match — sd still $20$ — so scoring above $70$ on average is as likely as on one match." Find the true $P(\bar X > 70)$ for $n = 25$, and explain Gary's error.

**C12.13.** 🟡 *(Poisson count, normal-approximated with correction.)* Daily potion demand is Poisson with mean $\lambda = 100$ (so $\mu = 100$, $\sigma = \sqrt{100} = 10$). Using the normal approximation **with** continuity correction, find $P(X \le 110)$.

**C12.14.** 🔵 *(RIVAL TRAP — Gary mis-reads the variance.)* Scores are $X \sim N(\mu = 50, \sigma^2 = 100)$. Gary computes the $z$-score for $x = 65$ as $z = (65 - 50)/100 = 0.15$ and concludes "basically average." Find the correct $z$ and $P(X > 65)$, and name Gary's error.

**C12.15.** 🟡 *(AUDIT — a forecast claims the sum's spread shrinks.)* An intern's report on the total potion use of $n = 400$ matches (per-match $\mu = 4$, $\sigma = 3$) states "the total has standard deviation $\sigma/\sqrt{n} = 3/20 = 0.15$." Compute the **correct** standard deviation of the total and name the intern's error.

**C12.16.** 🔵 *(Two-sided count interval with correction.)* With $X \sim$ Binomial$(100, 0.5)$ ($\mu = 50$, $\sigma = 5$), find $P(45 \le X \le 55)$ using the continuity correction.

### Elite Challenge (post-game — integrative / stretch)

**C12.17.** 🔵 *(DECISION — how many potions to stock?)* Round One is $n = 900$ independent matches, per-match potion use $\mu = 4$, $\sigma = 3$. The quartermaster wants the stock level $c$ such that the probability of running out is only $5\%$, i.e. $P(S_{900} > c) = 0.05$. Find $c$. *(Use $z = 1.645$.)*

**C12.18.** 🔵 *(AUDIT — combining a sum and the empirical rule.)* The total score of $n = 100$ independent trainers (per-trainer $\mu = 70$, $\sigma = 10$) is reported as "almost surely within $[6{,}800,\ 7{,}200]$." Using the CLT and the 68–95–99.7 rule, what fraction of the time does the total actually fall in that interval? Is "almost surely" justified?

**C12.19.** 🔵 *(DECISION — quartermaster picks a court size.)* Per-match potion use is $\mu = 4$, $\sigma = 3$. The quartermaster will run either one big court of $n = 100$ matches or stock each court so that total use exceeds its stock only $2.5\%$ of the time ($z = 1.96$). For $n = 100$, find the stock level $c$ with $P(S_{100} > c) = 0.025$, applying a continuity correction for the discrete potion count.
:::

## Answers

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.** All probabilities use two-decimal $z$ and the Appendix C table.

**C12.1** — *(standard) Standardize a single normal value (Entry №01).*
$$z = \frac{85 - 70}{10} = 1.50, \qquad P(X \le 85) = \Phi(1.50) = 0.9332.$$

**C12.2** — *(standard) Upper tail via complement (Entries №01, №02).*
$$z = \frac{90 - 70}{10} = 2.00, \qquad P(X > 90) = 1 - \Phi(2.00) = 1 - 0.9772 = 0.0228.$$

**C12.3** — *(standard) Linear interpolation in the $Z$-table (Entry №02).* $t = (1.13 - 1.10)/(0.10) = 0.30$:
$$\Phi(1.13) \approx 0.8643 + 0.30(0.8849 - 0.8643) = 0.8643 + 0.30(0.0206) = 0.8643 + 0.0062 = 0.8705.$$

**C12.4** — *(standard) Negative $z$ via symmetry (Entries №01, №02).*
$$z = \frac{58 - 70}{10} = -1.20, \qquad P(X < 58) = \Phi(-1.20) = 1 - \Phi(1.20) = 1 - 0.8849 = 0.1151.$$

**C12.5** — *(standard) The 68–95–99.7 rule (Entry №01).* $[50, 90] = [\mu - 2\sigma, \mu + 2\sigma] \Rightarrow \approx 95\%$. $[60, 80] = [\mu - \sigma, \mu + \sigma] \Rightarrow \approx 68\%$.

**C12.6** — *(standard) Inverse normal — percentile cutoff (Entry №02).* Top $10\%$: $\Phi(z) = 0.90 \Rightarrow z = 1.28$.
$$c = \mu + z\sigma = 70 + 1.28(10) = 70 + 12.8 = 82.8.$$

**C12.7** — *(standard) Interval — standardize both ends (Entries №01, №02).*
$$z_1 = \frac{60 - 70}{10} = -1.00, \quad z_2 = \frac{85 - 70}{10} = 1.50.$$
$$P(60 \le X \le 85) = \Phi(1.50) - \Phi(-1.00) = 0.9332 - (1 - 0.8413) = 0.9332 - 0.1587 = 0.7745.$$

**C12.8** — *(standard) CLT for a sum; sd $= \sigma\sqrt{n}$ (Entry №03).* $E[S] = 64 \times 25 = 1600$, sd $= 10\sqrt{64} = 80$.
$$z = \frac{1680 - 1600}{80} = 1.00, \qquad P(S > 1680) = 1 - \Phi(1.00) = 1 - 0.8413 = 0.1587.$$

**C12.9** — *(standard) CLT for a mean; sd $= \sigma/\sqrt{n}$ (Entry №03).* $E[\bar X] = 8$, sd $= 6/\sqrt{100} = 0.6$.
$$z = \frac{7 - 8}{0.6} = -1.67, \qquad P(\bar X < 7) = \Phi(-1.67) = 1 - \Phi(1.67) = 1 - 0.9525 = 0.0475.$$

**C12.10** — *(audit) Continuity correction on a binomial sum (Entries №03, №04).* $\mu = 144(0.5) = 72$, $\sigma = \sqrt{144(0.5)(0.5)} = 6$. "$\ge 80$" → left edge $79.5$:
$$P(X \ge 80) \approx 1 - \Phi\!\left(\frac{79.5 - 72}{6}\right) = 1 - \Phi(1.25) = 1 - 0.8944 = 0.1056.$$
**Team Rocket's error:** they standardized the integer $80$ (getting $z = 1.33$, $0.0918$) instead of the bar's left edge $79.5$ — they **forgot the continuity correction**. The honest value $0.1056$ is higher, so their odds underprice the payout.

**C12.11** — *(standard) Continuity correction for an exact count (Entry №04).* $P(X = 75) \approx P(74.5 < Y < 75.5)$ with $\mu = 72$, $\sigma = 6$:
$$\Phi\!\left(\frac{75.5 - 72}{6}\right) - \Phi\!\left(\frac{74.5 - 72}{6}\right) = \Phi(0.58) - \Phi(0.42) = 0.7190 - 0.6628 = 0.0562.$$

**C12.12** — *(rival_trap) CLT for a mean; sd shrinks like $1/\sqrt{n}$ (Entry №03).* sd$(\bar X) = 20/\sqrt{25} = 4$.
$$z = \frac{70 - 60}{4} = 2.50, \qquad P(\bar X > 70) = 1 - \Phi(2.50) = 1 - 0.9938 = 0.0062.$$
**Gary is wrong.** He kept the single-match sd of $20$; the **average** of $25$ matches has sd $20/\sqrt{25} = 4$, *five times tighter*. Scoring above $70$ on average ($0.0062$) is far rarer than on one match (which would be $1 - \Phi(0.5) = 0.3085$). Averaging shrinks the spread.

**C12.13** — *(standard) Normal approximation to a Poisson, with correction (Entries №03, №04).* $\mu = 100$, $\sigma = 10$. "$\le 110$" → right edge $110.5$:
$$P(X \le 110) \approx \Phi\!\left(\frac{110.5 - 100}{10}\right) = \Phi(1.05) = 0.8531.$$

**C12.14** — *(rival_trap) $\sigma$ vs $\sigma^2$ in standardization (Entry №01).* $\sigma = \sqrt{100} = 10$, so
$$z = \frac{65 - 50}{10} = 1.50, \qquad P(X > 65) = 1 - \Phi(1.50) = 1 - 0.9332 = 0.0668.$$
**Gary's error:** he divided by the **variance** $100$ instead of the **standard deviation** $10$, getting a bogus $z = 0.15$. A score $1.5\sigma$ above the mean is *not* "basically average" — only the top $6.7\%$ beat it.

**C12.15** — *(audit) Sum's sd grows like $\sigma\sqrt{n}$ (Entry №03).* The **sum** of $400$ matches has
$$\text{sd}(S) = \sigma\sqrt{n} = 3\sqrt{400} = 3 \times 20 = 60.$$
**The intern's error:** they used the **mean's** formula $\sigma/\sqrt{n} = 0.15$ for the **total**. A sum's spread *grows*, not shrinks; the correct sd is $60$, four hundred times larger.

**C12.16** — *(standard) Two-sided count with correction (Entry №04).* $\mu = 50$, $\sigma = 5$; "$45 \le X \le 55$" → edges $44.5$ and $55.5$:
$$\Phi\!\left(\frac{55.5 - 50}{5}\right) - \Phi\!\left(\frac{44.5 - 50}{5}\right) = \Phi(1.10) - \Phi(-1.10) = 0.8643 - (1 - 0.8643) = 0.8643 - 0.1357 = 0.7286.$$

**C12.17** — *(decision) Inverse CLT for a sum (Entries №02, №03).* $E[S] = 900 \times 4 = 3600$, sd $= 3\sqrt{900} = 90$. Want $P(S > c) = 0.05 \Rightarrow z = 1.645$:
$$c = \mu + z\sigma = 3600 + 1.645(90) = 3600 + 148.05 = 3748.05 \approx 3748 \text{ potions}.$$
Stock $\approx 3{,}748$ to keep the run-out risk at $5\%$.

**C12.18** — *(audit) CLT sum + empirical rule (Entries №01, №03).* $E[S] = 100 \times 70 = 7000$, sd $= 10\sqrt{100} = 100$. The interval $[6800, 7200] = [\mu - 2\sigma, \mu + 2\sigma]$, which by the $68$–$95$–$99.7$ rule holds $\approx 95\%$. **The report's error:** "almost surely" overstates it — there's still a $\approx 5\%$ chance the total falls outside. (Two sd is $95\%$, not near-certainty; near-certainty would need $\pm 3\sigma = [6700, 7300]$.)

**C12.19** — *(decision) Inverse CLT for a sum with continuity correction (Entries №03, №04).* $E[S] = 100 \times 4 = 400$, sd $= 3\sqrt{100} = 30$. Want $P(S > c) = 0.025 \Rightarrow z = 1.96$ at the corrected boundary. Solve for the corrected edge $c + 0.5$ (since "$> c$" for a discrete count uses $c + 0.5$):
$$c + 0.5 = \mu + z\sigma = 400 + 1.96(30) = 400 + 58.8 = 458.8 \Rightarrow c = 458.3 \approx 458 \text{ potions}.$$
Stock $\approx 458$ per court for a $2.5\%$ run-out risk. *(Without the half-step you'd report $c = 458.8 \approx 459$; the correction shaves it to $458$.)*

### Quick-Answer Table

| # | Answer | | # | Answer |
|---|---|---|---|---|
| C12.1 | $0.9332$ | | C12.11 | $\approx 0.0562$ |
| C12.2 | $0.0228$ | | C12.12 | $\approx 0.0062$ (Gary wrong) |
| C12.3 | $\approx 0.8705$ | | C12.13 | $\approx 0.8531$ |
| C12.4 | $0.1151$ | | C12.14 | $z=1.5,\ 0.0668$ (Gary wrong) |
| C12.5 | $\approx 95\%;\ \approx 68\%$ | | C12.15 | sd $= 60$ (intern wrong) |
| C12.6 | $82.8$ | | C12.16 | $\approx 0.7286$ |
| C12.7 | $0.7745$ | | C12.17 | $\approx 3748$ potions |
| C12.8 | $0.1587$ | | C12.18 | $\approx 95\%$; "almost surely" unjustified |
| C12.9 | $\approx 0.0475$ | | C12.19 | $\approx 458$ potions |
| C12.10 | $\approx 0.1056$ (Rocket wrong) | | | |
:::

## Badge Earned — the Grand Gathering Cleared

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/sprites/front/35.png" alt="Clefairy, the bell-shaped mascot of the Grand Gathering" style="width:120px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption class="badge-caption"><strong>Grand Gathering cleared!</strong> No badge here — but you can now read the bell of thousands. Rank holds: Ace Trainer · 6 badges.</figcaption>
</figure>

You signed the quartermaster's order with the right buffer, planned a round of ten thousand strangers, and never once needed to know a single trainer. **Rank: Ace Trainer (6 badges).** The qualifier is behind you; Cinnabar and the Volcano Badge are next.

**Mastery checklist — tick each before you move on (mapped 1-to-1 to the SOA outcomes):**

- ☐ **(2d)** I can describe $N(\mu, \sigma^2)$, **standardize** with $z = (x - \mu)/\sigma$ (dividing by $\sigma$, never $\sigma^2$), apply the **68–95–99.7 rule**, and read the $Z$-table — straight, interpolated, by symmetry, or backward to a percentile. *(Rematch: Concepts 1–2, WE 1 & 5, Problems C12.1–C12.7.)*
- ☐ **(3i)** I can apply the **CLT** to a **sum** ($N(n\mu, n\sigma^2)$, sd $\sigma\sqrt{n}$) or a **mean** ($N(\mu, \sigma^2/n)$, sd $\sigma/\sqrt{n}$), choosing the right standard deviation every time. *(Rematch: Concept 3, WE 2 & 3, Problems C12.8, C12.9, C12.12, C12.15.)*
- ☐ **(3i)** I can apply the **continuity correction** to a discrete count approximated by the normal — half-stepping to the outer edge of every bar I keep, *before* standardizing — and I can explain *why* it's $0.5$. *(Rematch: Concept 4, WE 4, the Gym Battle, Problems C12.10, C12.11, C12.13, C12.16, C12.19.)*
- ☐ *(Enrichment, untested)* I can explain what makes a variable **lognormal** ($\ln L$ normal) and why it's right-skewed. *(Rematch: Concept 5.)*

**Gym Rematch pointers.** Used the single-item sd for an average? Concept 3, Beat 4, then C12.12. Forgot the half-step? Concept 4, Beat 4, the Team Rocket trap, then C12.10. Divided by $\sigma^2$? Concept 1, Beat 4, then C12.14. Mixed up sum-vs-mean spread? Trainer's Tip "Sum or mean?", then C12.15.

> Next stop: **Cinnabar Island**, where Blaine's volcano and Oak's lab turn the loss-and-payment ideas continuous — deductibles and limits by calculus. Pack the bell; you'll approximate aggregate losses with it for the rest of the journey.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
