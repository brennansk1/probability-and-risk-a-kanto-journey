<!--
  file: ch10_continuous_moments
  tier: B
  outcomes: 2c,2d
  tia: B.2
  locale: Saffron City / Silph Co. (Sabrina arc continued)
  type: psychic
  maps_to: Saffron / Silph Co. -- the center and spread of a CONTINUOUS loss:
           E[X]=int x f, E[g(X)]=int g f, Var=int x^2 f - mu^2; moments of MIXED
           distributions; the continuous survival method E[X]=int_0^inf S(x) dx.
-->

# The Center of a Smooth Crowd — Continuous Moments {.type-psychic}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with Saffron City circled at the center of the region; the towering Silph Co. headquarters sits at its heart. No gym leg is marked -- the journey lingers in Saffron after the Marsh Badge." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Still in <strong>Saffron City</strong> — no new badge this leg. You have your Marsh Badge from Sabrina, and now you climb the <em>Silph Co.</em> tower, where every loss the company books is a <em>smooth</em> random number and the actuaries upstairs need its center and spread.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Tower of Smooth Numbers"**

The Silph Co. lobby is all glass and quiet hum. Upstairs, on the actuarial floor, a claims model glows on the wall — not a tidy table of "0 decks, 1 deck, 2 decks" like the purser's ledger on the S.S. Anne, but a single unbroken **curve.** A loss can be *any* amount now: $\$3.14$ thousand, $\$3.141$ thousand, $\$\pi$ thousand. There is no list to add up.

A Silph analyst slides a tablet across the desk. "Every policy we write pays out some random loss $X$," she says. "Most of the curve is a smooth density — but look here." She taps a sharp **vertical spike** sitting on top of the curve at exactly zero. "A big chunk of policies pay *nothing at all*. That spike is a lump of probability with no width — a *point mass* — bolted onto the smooth part. I need one honest number: the **expected loss** per policy. The whole curve *and* that spike, collapsed to a single average. Marketing already quoted a premium off the *peak* of the curve. I think they're about to bankrupt a floor of this building."

Then the lights stutter. A psychic pressure rolls through the floor — **Sabrina's** influence still lingers in Saffron, bending the room. The curve on the wall *warps*, and for a moment the discrete bars you knew from the ship melt into the smooth density and back again, as if to whisper: *it's the same idea, just poured into an integral.*

You realize the analyst is asking the Vermilion question — *where is the center, how wide is the spread* — but the crowd is no longer countable. It's a *continuum* with a spike welded on.

*How do you find the average of a number that can take infinitely many values — when part of its probability is smeared smoothly and part is nailed to a single point?*
:::

## Where You Are — 60-Second Retrieval

**Rank: Ace Trainer · Badges: 6** (Cascade, Thunder, Boulder, Rainbow, Soul, Marsh). You earned the **Marsh Badge** from Sabrina by learning the *language* of continuous chance: a continuous random variable is described by a **density** $f(x)$, where **area is probability** — $P(a<X<b)=\int_a^b f(x)\,dx$ — and you move fluently among the density $f$, the cdf $F(x)=P(X\le x)=\int_{-\infty}^x f$, and the survival function $S(x)=P(X>x)=1-F(x)$. You also met the **mixed distribution**: a curve with a point mass spiked on it, where the discrete atoms and the smooth part each carry their own share of the total probability $1$.

The other thing you carry comes from all the way back at Vermilion. On the S.S. Anne you learned the **survival (Darth-Vader) method** for a *discrete* non-negative variable: $E[X]=\sum_{k\ge0}S(k)$ — the mean is the *sum* of the survival function. Hold that phrase. This chapter is the Vermilion lesson *poured into the continuous mold*: every $\sum$ becomes an $\int$, every point mass keeps its own term, and the Darth-Vader sum becomes the Darth-Vader **integral** $E[X]=\int_0^\infty S(x)\,dx$.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the continuous setup**

Answer from memory; if any feels shaky, flip back before continuing.

1. For a continuous $X$, what is $P(X=3)$ exactly, and why? *(Answer: $0$ — a single point has zero width, hence zero area.)*
2. The total area under any density $f(x)$ must equal what? *(Answer: $1$.)*
3. Discrete twin: a non-negative integer RV has $S(0)=0.7,\,S(1)=0.4,\,S(2)=0.1$. What is $E[X]$? *(Answer: the Darth-Vader sum $0.7+0.4+0.1=1.2$.)*

All three instant? Then you're ready: this chapter swaps the sum for an integral and the lone point for a smeared continuum. Any hesitation? Reclaim "area is probability" and "the mean is a probability-weighted total" first — they are the whole foundation here.
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP022 "Abra and the Psychic Showdown," EP023 "The Tower of Terror," EP024 "Haunter versus Kadabra" (the Saffron / Sabrina arc)**

<figure><img src="../../assets/stills/ch10_now_playing.jpg" alt="Sabrina, the psychic Gym Leader of Saffron City, holding her doll (Indigo League EP024)." style="width:60%; max-width:440px; display:block; margin:0.4em auto;"><figcaption style="font-size:0.8em; color:#555;">Saffron Gym, EP024 — Sabrina bends the solid into the fluid: the discrete bars melt into a smooth density.</figcaption></figure>

Across these three episodes Ash arrives at **Saffron City**, meets **Sabrina** — a Gym Leader whose raw psychic power warps the world around her — and is sent away to find a Ghost-type before he can win the Marsh Badge; the detour through Lavender's tower (EP023–024) is all about a single *Haunter* that finally unsettles Sabrina. *Watch EP022 then EP024 alongside this chapter.* On screen, the throughline is **psychic force bending what's solid into something fluid** — exactly this chapter's move, where the countable bars of the discrete world melt into a smooth density you must integrate. (The Silph Co. claims model, the spiked mixed-loss curve, and the "expected loss" framing are **in-world extensions** built to carry the math — they dramatize the integral, not a specific on-screen line. No badge is on the table this leg; you already hold the Marsh Badge.)
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice comes through the Pokédex's Actuary Mode as you ride the Silph Co. elevator up.

"Ash — you already know how to find the center and spread of a *countable* random variable. Up in this tower the variable is **smooth**, and the only thing that changes is the machinery: where you summed, you now **integrate**. Master that one substitution — $\sum \to \int$, mass $\to$ density — and every continuous distribution in the next towns hands you its mean and variance the same way. Then there's the wrinkle the analyst spotted: a **mixed** loss, part smooth and part spiked. You handle it by *adding the two pieces* — the point masses summed, the smooth part integrated. And finally the elegant shortcut: for a non-negative loss, the mean is just the **area under the survival curve**. This is a **Tier B** chapter — full nine-beat teaching for each idea, a gentler ramp than the Tier-A proving grounds, but every tool here you reuse in every pricing problem you will ever solve."

By the end of this chapter you will be able to:

- **Compute the moments of a continuous random variable** — the mean $E[X]=\int x f(x)\,dx$, any $E[g(X)]=\int g(x)f(x)\,dx$ by LOTUS, and the variance $\Var(X)=\int x^2 f(x)\,dx-(E[X])^2$ — and apply linearity $E[aX+b]=aE[X]+b$ and $\Var(aX+b)=a^2\Var(X)$. *(Outcome 2c.)*
- **Compute the moments of a mixed distribution** by combining the smooth part (an integral) with the discrete point masses (a sum), each weighted by its own probability. *(Outcomes 2c, 2d.)*
- **Use the survival-function method** $E[X]=\int_0^\infty S(x)\,dx$ for a non-negative continuous variable — the continuous twin of the discrete Darth-Vader sum — derived by swapping the order of a double integral. *(Outcome 2c.)*

> *Exam-weight signpost.* Univariate random variables are the **single largest slice of Exam P (44–50%)**, and continuous mean/variance computations sit at its center — every severity model, every expected-loss calculation runs through the integrals below. The **survival-integral shortcut** is a recurring time-saver, and **mixed distributions** show up the instant a policy has a deductible or a limit. This is a **Tier B** chapter, fully derived, reused everywhere downstream.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own All of Silph Co.?**

Already fluent? Prove it. Work these four, ~3 minutes each, *with correct method*.

1. $X$ has density $f(x)=\tfrac{3}{8}x^2$ on $0\le x\le 2$. Find $E[X]$ and $\Var(X)$.
2. The same $X$; a payout is $Y=5X+3$. Find $E[Y]$ and $\Var(Y)$ *without* re-integrating.
3. A loss $X$ is **mixed**: with probability $0.4$ it is exactly $0$ (a point mass), and with probability $0.6$ it is uniform on $[0,10]$. Find $E[X]$.
4. A non-negative $X$ has survival $S(x)=e^{-x/8}$ for $x\ge0$. Find $E[X]$ **without** recovering the density.

*(Answers: $E[X]=1.5,\ \Var(X)=3/20=0.15$; $E[Y]=10.5,\ \Var(Y)=25(0.15)=3.75$; $E[X]=0.4(0)+0.6(5)=3$; $E[X]=\int_0^\infty e^{-x/8}\,dx=8$.)* Four for four with the right reasoning? **Skip to the Capstone Challenge.** Any miss or hesitation? The teaching below was built exactly for you — and each concept has its own skip-gate, so even a partial owner loses no time.
:::

---

Three ideas build in increasing difficulty, in TIA's order. We teach them **in order**, each with its own "do you already own this?" skip-check, then the full nine-beat lesson, then a Pokédex Entry you can carry into the exam. Each one is the Vermilion lesson with a single substitution made: $\sum \to \int$.

1. **Moments of a continuous random variable** — $E[X]=\int x f$, LOTUS $E[g(X)]=\int g\,f$, and the variance — *the foundation everything else uses* *(B.2.1)*
2. **Moments of a mixed distribution** — sum the spiked point masses, integrate the smooth part *(B.2.2)*
3. **The survival-function method** — the mean as the area under $S$, the continuous Darth-Vader twin *(B.2.3)*

## Concept 1 — Moments of a Continuous Random Variable (B.2.1)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Continuous moments**

A loss $X$ (in \$thousands) has density $f(x)=\tfrac{3}{8}x^2$ on $0\le x\le 2$. Find $E[X]$ and $\Var(X)$.

If you instantly set up $E[X]=\int_0^2 x\cdot\tfrac38 x^2\,dx=\tfrac32$ and $\Var(X)=\int_0^2 x^2\cdot\tfrac38 x^2\,dx-(\tfrac32)^2=\tfrac{12}{5}-\tfrac94=\tfrac{3}{20}=0.15$, **skip to Concept 2**. If you weren't sure where the $x$ (or the $x^2$) goes inside the integral, read on — it's the discrete formula with $\sum$ swapped for $\int$.
:::

**Beat 1 — The one-sentence idea.** *The mean of a continuous random variable is its values weighted by probability and totalled — the same weighted average as before, but with the sum replaced by an integral and the probability $p(k)$ replaced by the density slice $f(x)\,dx$.*

**Beat 2 — Anchor + concrete instance.** On the S.S. Anne you found $E[X]=\sum_k k\,p(k)$ — value times probability, added up. Up in Silph Co. the loss $X$ can be *any* number in $[0,2]$ (thousands of Poké-dollars), with density $f(x)=\tfrac38 x^2$ — heavier toward the right end, so larger losses are more common than small ones. There's no list of values to add. But each sliver of width $dx$ at position $x$ carries probability $f(x)\,dx$, so we do the *exact same thing*: weight each value $x$ by its probability slice and total — and "total over a continuum" is what $\int$ means.

**Beat 3 — Reason through it in plain words.** Imagine chopping $[0,2]$ into a thousand tiny bins. Bin number $i$ sits near value $x_i$ and holds probability $f(x_i)\,\Delta x$ (its height times its width). Treat that bin like a discrete value: its contribution to the average is $x_i\times f(x_i)\,\Delta x$. Add all thousand contributions — that's a Riemann sum — and as the bins shrink the sum *becomes* the integral $\int_0^2 x\,f(x)\,dx$. The continuous mean isn't a new idea; it's the discrete weighted-average in the limit of infinitely many infinitely thin values.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The classic slip is to integrate the **density alone** and call that the mean:

$$E[X]\overset{?}{=}\int_0^2 f(x)\,dx=\int_0^2 \tfrac38 x^2\,dx=1. \qquad\textbf{(wrong — that's the total probability, not the mean)}$$

That integral is always $1$ (the area under any density), so it can *never* be the mean — it carries no information about *where* the probability sits. You must include the **lever arm** $x$: it's $\int x\,f(x)\,dx$, value-times-probability, not probability alone. (The second, nastier version of this trap — writing $E[X^2]=(E[X])^2$ — is exactly the one that bit us in the discrete world, and it's still false here. We dismantle it in Beat 6.)

**Beat 5 — Translate into notation, one glyph at a time.** The continuous mean, the **law of the unconscious statistician (LOTUS)**, and the variance — each the discrete formula with $\sum_k(\cdots)p(k)$ replaced by $\int(\cdots)f(x)\,dx$:

$$E[X]=\int_{-\infty}^{\infty} x\,f(x)\,dx \qquad \text{read aloud: ``the integral of } x \text{ times its density, over all } x.\text{''}$$

$$E[g(X)]=\int_{-\infty}^{\infty} g(x)\,f(x)\,dx \qquad \text{(LOTUS: average a function by weighting its values by the density).}$$

$$\Var(X)=E\big[(X-\mu)^2\big]=\int_{-\infty}^{\infty}(x-\mu)^2 f(x)\,dx=E[X^2]-(E[X])^2.$$

Read the integral sign $\int$ as "add up, over a continuum." The slice $f(x)\,dx$ is "the probability $X$ sits in a sliver near $x$," and $x\cdot f(x)\,dx$ is that sliver's contribution to the average. (In practice the limits run only over the **support** — where $f>0$ — here $0$ to $2$.)

**Beat 6 — Derive the moments from the instance.** Take our loss $f(x)=\tfrac38 x^2$ on $[0,2]$. First the mean — pull the constant out and use the power rule $\int x^n\,dx=\tfrac{x^{n+1}}{n+1}$:

$$E[X]=\int_0^2 x\cdot\tfrac38 x^2\,dx=\tfrac38\int_0^2 x^3\,dx=\tfrac38\cdot\Big[\tfrac{x^4}{4}\Big]_0^2=\tfrac38\cdot\tfrac{16}{4}=\tfrac38\cdot 4=\tfrac{3}{2}=1.5.$$

Now the **second moment** by LOTUS with $g(x)=x^2$:

$$E[X^2]=\int_0^2 x^2\cdot\tfrac38 x^2\,dx=\tfrac38\int_0^2 x^4\,dx=\tfrac38\cdot\Big[\tfrac{x^5}{5}\Big]_0^2=\tfrac38\cdot\tfrac{32}{5}=\tfrac{12}{5}=2.4.$$

And here is the trap dismantled in numbers: $E[X^2]=2.4$, but $(E[X])^2=1.5^2=2.25$ — **not equal.** Their gap *is* the variance:

$$\Var(X)=E[X^2]-(E[X])^2=2.4-2.25=0.15=\tfrac{3}{20},\qquad \sigma=\sqrt{0.15}\approx 0.387.$$

Two integrals, one subtraction — *exactly* the discrete recipe, with $\int$ where the $\sum$ used to be.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the loss above, $E[X]=1.5$, $\Var(X)=0.15$.
- *Twist (linearity, no re-integration):* a payout is $Y=5X+3$. Then $E[Y]=5E[X]+3=5(1.5)+3=10.5$ and $\Var(Y)=5^2\Var(X)=25(0.15)=3.75$ — the $+3$ adds *no* variance, the $5$ gets *squared*. Linearity and the $a^2$ rule are **identical** to the discrete world; they never cared whether $X$ was countable.
- *General (any density / any $g$):* $E[g(X)]=\int g(x)f(x)\,dx$ handles a squared loss, a $\sqrt{X}$ payoff, an $e^{tX}$ (the MGF) — weight the function's values by $f$ and integrate.
- *Edge (symmetry shortcut):* if $f$ is **symmetric** about a point $c$, then $E[X]=c$ with no integral — e.g. $f(x)=\tfrac34 x(2-x)$ on $[0,2]$ mirrors about $x=1$, so $E[X]=1$ on sight. And a sanity bound: the mean must lie inside the support, $0\le 1.5\le 2$ ✓.

**Beat 8 — Picture it: the mean is the balance point of the density.** The discrete bars of the S.S. Anne have melted into a smooth curve, but the mean is still the *fulcrum* — the place the probability balances. A long, thin upper tail tugs that fulcrum to the **right** of the peak.

<figure>
<img src="../../assets/diagrams/ch10_continuous_moments.png" alt="A right-skewed continuous density f(x) over the interval from 0 to 6, shaded under the curve. A red triangular fulcrum sits on the x-axis directly under the mean (about 2.06), with a red vertical line and the equation E[X] equals the integral of x times f(x) dx. A green dashed line marks the lower mode (about 1.10) to the left of the mean. A thin shaded slice f(x) dx is marked out in the tail with a callout that its lever arm is x and its weight is the area f(x) dx. A callout notes that the rare, heavy upper tail tugs the balance point to the right of the peak. A Kadabra sprite sits in the upper-left margin, clear of the curve and equations, warping the discrete bars into a smooth curve." style="width:88%; max-width:720px; display:block; margin:1em auto;">
<figcaption>Continuous expectation is the <strong>balance point</strong> of the density: $E[X]=\int x\,f(x)\,dx$ is the fulcrum where the probability balances. Each slice $f(x)\,dx$ contributes "value $\times$ probability"; the rare heavy upper tail pulls the mean to the <em>right</em> of the peak (the mode) — the continuous echo of "mean $\ne$ mode."</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now compute the mean of any continuous RV as $\int x\,f(x)\,dx$, any $E[g(X)]$ by weighting $g$ with the density, and the variance as $E[X^2]-(E[X])^2$ — then transform both with $E[aX+b]=aE[X]+b$ and $\Var(aX+b)=a^2\Var(X)$. It is the Vermilion toolkit with one substitution: $\sum \to \int$.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Moments of a Continuous RV**

$$E[X]=\int_{-\infty}^{\infty} x\,f(x)\,dx;\quad E[g(X)]=\int_{-\infty}^{\infty} g(x)\,f(x)\,dx;\quad \Var(X)=E[X^2]-(E[X])^2.$$
$$E[aX+b]=aE[X]+b;\qquad \Var(aX+b)=a^2\Var(X).$$

*In plain terms:* the discrete moment formulas with $\sum_k(\cdots)p(k)$ replaced by $\int(\cdots)f(x)\,dx$. The mean is the balance point of the density; LOTUS averages a function by weighting it with $f$; variance is "mean of the square minus square of the mean."

*Recognition cue:* a **density $f(x)$** and a request for "average / expected / mean / variance / spread." Integrate $x\,f$ (or $x^2 f$); never integrate $f$ alone, and never write $E[X^2]=(E[X])^2$.
:::

## Concept 2 — Moments of a Mixed Distribution (B.2.2)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Mixed moments**

A loss $X$ is **mixed**: with probability $0.4$ it is exactly $\$0$ (a point mass), and with probability $0.6$ it is uniform on $[0,10]$. Find $E[X]$.

If you instantly wrote $E[X]=\underbrace{0.4\cdot 0}_{\text{point mass}}+\underbrace{0.6\cdot 5}_{\text{smooth part}}=3$ (the atom contributes its value times its mass; the continuous piece contributes its conditional mean times its share), **skip to Concept 3**. If you tried to integrate a single clean density and the spike at $0$ tripped you up, read on.
:::

**Beat 1 — The one-sentence idea.** *A mixed distribution's mean is just the sum of two contributions — the discrete point masses (each value times its lump of probability) **plus** the smooth part (its integral) — because expectation is a weighted total and you simply total over both kinds of probability.*

**Beat 2 — Anchor + concrete instance.** Back in Sabrina's chapter you met the **mixed** random variable: a curve with a spike welded on. The Silph analyst's claim model is exactly this. Let $X$ be the loss a policy pays:

- with probability $0.4$, the policy pays **exactly $\$0$** — a *point mass* (an atom) of size $0.4$ sitting on the value $0$;
- with probability $0.6$, the loss is spread **uniformly on $[0,10]$** thousand — a smooth slab.

The two probabilities total $0.4+0.6=1$ ✓, as any distribution must. The analyst wants the **expected loss** $E[X]$.

**Beat 3 — Reason through it in plain words.** Expectation is "value weighted by probability, totalled" — and it does not care whether the probability arrives as a *lump* or as a *smear*. So total over **both** kinds. The atom at $0$ contributes its value times its mass: $0\times 0.4=0$. The smooth slab contributes the average of its values, weighted by how much probability lives there: the uniform on $[0,10]$ averages $5$, and it owns a $0.6$ share, so it contributes $0.6\times 5=3$. Add the two pieces: $E[X]=0+3=3$. The grand mean is a *weighted blend* of the atom's value and the smooth part's conditional mean, with weights equal to each piece's probability.

**Beat 4 — Surface and dismantle the tempting wrong idea.** *(This is Team Rocket's trap for the chapter.)* The seductive error is to **ignore the point mass entirely** — to treat the $[0,10]$ uniform as if it were the *whole* story and report its mean, $5$, as the expected loss. That double-counts the smooth part's probability (pretending it's $1$ when it's only $0.6$) and silently throws away the $0.4$ of policies that pay nothing. The mass at $0$ is *real probability*; it must carry its own weight in the average. The fix: **the smooth part is only $60\%$ of the distribution, so weight it by $0.6$, then add the atom's $0.4\times 0$.** A close cousin of the slip is forgetting to *renormalize* the conditional mean — but the clean way avoids that entirely: weight each piece by its *unconditional* probability and add. (We'll catch Team Rocket making this exact mistake later.)

**Beat 5 — Translate into notation, one glyph at a time.** Write a mixed $X$ as a set of atoms (values $x_i$ with masses $p_i$) plus a sub-density $f(x)$ over the continuous region. The expectation totals both:

$$E[X]=\underbrace{\sum_i x_i\,p_i}_{\text{point masses}}\ +\ \underbrace{\int x\,f(x)\,dx}_{\text{smooth part}} \qquad \text{read aloud: ``sum the atoms, integrate the smooth piece, add.''}$$

Here the masses $p_i$ and the sub-density $f$ together carry the total probability $1$: $\sum_i p_i+\int f(x)\,dx=1$. The same split works for any $E[g(X)]$ — replace $x_i$ by $g(x_i)$ and $x$ by $g(x)$:

$$E[g(X)]=\sum_i g(x_i)\,p_i+\int g(x)\,f(x)\,dx.$$

**Beat 6 — Derive the moments of the analyst's loss.** The atom contributes its value times its mass; the smooth slab contributes its integral. The $[0,10]$ uniform, restricted to the $0.6$ share, has sub-density $f(x)=0.6\times\tfrac{1}{10}=0.06$ on $[0,10]$ (height $=$ share $\times$ the unit-uniform height $\tfrac{1}{b-a}$). Then:

$$E[X]=\underbrace{0\cdot 0.4}_{\text{atom}}+\underbrace{\int_0^{10} x\,(0.06)\,dx}_{\text{smooth}}=0+0.06\cdot\Big[\tfrac{x^2}{2}\Big]_0^{10}=0.06\cdot 50=3.$$

The integral $0.06\cdot 50=3$ is just $0.6\times 5$ — the slab's share times its conditional mean of $5$, exactly as the plain-words argument promised.

For the **variance**, get the second moment the same two-piece way, then subtract the squared mean:

$$E[X^2]=\underbrace{0^2\cdot 0.4}_{\text{atom}}+\int_0^{10} x^2\,(0.06)\,dx=0+0.06\cdot\Big[\tfrac{x^3}{3}\Big]_0^{10}=0.06\cdot\tfrac{1000}{3}=20.$$

$$\Var(X)=E[X^2]-(E[X])^2=20-3^2=20-9=11,\qquad \sigma=\sqrt{11}\approx 3.317.$$

Notice the variance is *large* relative to the mean — the big spike of zeros plus the wide smooth slab makes the loss very spread out, which is precisely why the analyst can't price off a single typical value.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the analyst's loss, $E[X]=3$.
- *Twist (atom not at zero — a policy limit):* losses are uniform on $[0,10]$ but **capped at $\$8$** — everything above $8$ piles into an atom at $8$. The smooth part is $f(x)=\tfrac{1}{10}$ on $[0,8]$ (mass $0.8$) and an atom of mass $P(X>8)=0.2$ at the value $8$: $E[X]=\int_0^8 x\tfrac{1}{10}\,dx+8(0.2)=3.2+1.6=4.8$. (This *is* a capped loss $E[X\wedge 8]$ — the next deductibles chapter.)
- *General (several atoms):* a loss that is $0$ w.p. $0.5$, $\$100$ (a fixed franchise payout) w.p. $0.2$, and otherwise exponential with mean $\$50$ on the remaining $0.3$: sum the two atoms, weight the exponential's mean by $0.3$, add.
- *Edge / sanity:* the masses and the area under the sub-density must total $1$ before you start — if they don't, you've mis-stated the distribution. And the mean must lie between the smallest and largest possible value ($0\le 3\le 10$ ✓).

**Beat 8 — Picture it.** The two pieces of probability — a spike and a slab — each contribute to the balance point. (The continuous balance-point figure of Concept 1 shows the smooth half of the picture; for the mixed loss, add a fulcrum-weight at the atom's location with weight equal to its mass, and the combined balance point shifts toward the heavier piece.) The grand mean is the *probability-weighted blend* of the atom's value ($0$, weight $0.4$) and the slab's conditional mean ($5$, weight $0.6$), landing at $3$.

**Beat 9 — Consolidate.** You can now find the mean and variance of a mixed distribution by treating it as two distributions glued together: **sum** the discrete atoms (value $\times$ mass), **integrate** the smooth part ($x$ or $x^2$ against its sub-density), and **add** — never dropping the point mass and never letting the smooth part pretend it owns all the probability.

::: pokedex-entry
**POKÉDEX ENTRY №02 — Moments of a Mixed Distribution**

$$E[X]=\sum_i x_i\,p_i+\int x\,f(x)\,dx;\qquad E[g(X)]=\sum_i g(x_i)\,p_i+\int g(x)\,f(x)\,dx,$$
with $\sum_i p_i+\int f(x)\,dx=1$, and $\Var(X)=E[X^2]-(E[X])^2$ as usual.

*In plain terms:* a curve with a spike on it. Total over both kinds of probability — sum the atoms (each value times its lump of mass), integrate the smooth part, add. Each piece is weighted by its own probability.

*Recognition cue:* "**pays nothing / exactly $0$ with probability $p$**," a **capped or floored** loss, "a spike on the density," or any **deductible/limit** setup. Split into atoms $+$ smooth, weight each by its probability, and add — never ignore the point mass.
:::

## Concept 3 — The Survival-Function Method: $E[X]=\int_0^\infty S(x)\,dx$ (B.2.3)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Continuous Darth-Vader**

A non-negative loss $X$ has survival function $S(x)=e^{-x/8}$ for $x\ge0$. Find $E[X]$ **without** recovering the density.

If you instantly wrote $E[X]=\int_0^\infty S(x)\,dx=\int_0^\infty e^{-x/8}\,dx=8$ (and you know this needs $X\ge0$), **skip to the Worked Examples**. If you reached to differentiate $S$ into a density $f$ first, read on — this shortcut deletes two error-prone steps, and it's the exact continuous twin of the Darth-Vader *sum* you used on the S.S. Anne.
:::

**Beat 1 — The one-sentence idea.** *For a non-negative random variable, the mean is simply the area under its survival curve, $E[X]=\int_0^\infty S(x)\,dx$ — the continuous twin of the discrete Darth-Vader sum $\sum_{k\ge0}S(k)$, with the sum melted into an integral.*

**Beat 2 — Anchor + concrete instance.** On the S.S. Anne, when the captain handed you the survival function — "the chance the ship holds past deck $k$" — you found the mean by *summing* it: $E[X]=\sum_{k\ge0}S(k)$, no $k\,p(k)$ products. Up in Silph Co. the analyst often hands you a **survival function** $S(x)=P(X>x)$ for a continuous loss (or only the cdf $F$), and asks for the mean. You *could* recover the density $f=F'=-S'$ and integrate $x\,f$. The survival method skips all of that. For a loss with $S(x)=e^{-x/8}$ (an exponential, mean $8$), the mean is just the area under that decaying curve.

**Beat 3 — Reason through it in plain words.** Picture the loss $X$ as "how far a marker travels along the axis." For every position $x$, the marker is still going *past* $x$ with probability $S(x)=P(X>x)$. The expected distance travelled is built by adding up, over every position, the chance the marker is *still moving* there — because each unit of distance counts toward the average only while the marker survives it. Summing "probability still going at $x$" over all $x$ — i.e. integrating $S(x)$ — gives the expected total distance, the mean. It's the same layer-by-layer counting as the discrete Darth-Vader rule: there you stacked unit *blocks* $S(0),S(1),\dots$; here you stack infinitely thin *strips* $S(x)\,dx$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two guardrails. First, the rule needs $X\ge0$:

$$E[X]\overset{?}{=}\int_0^\infty S(x)\,dx \quad\text{even when } X<0 \text{ is possible.} \qquad\textbf{(wrong — drops the negative tail)}$$

The clean identity holds *only* for a non-negative $X$; if $X$ can go negative, the area-under-$S$ picture misses the part below zero and needs a correction term $-\int_{-\infty}^0 F(x)\,dx$. Happily almost every actuarial quantity — a time, a loss, a claim size — *is* non-negative, so the simple rule applies; just **check $X\ge0$** first. Second, integrate the **survival** $S(x)=P(X>x)$, *not* the cdf $F(x)$ — they decay in opposite directions, and integrating $F$ gives nonsense (it grows). (The discrete twin had the matching pitfall: sum $S$, not $F$, and start at $0$.)

**Beat 5 — Translate into notation, one glyph at a time.** The continuous survival ("Darth-Vader") rule, and its higher-moment form:

$$E[X]=\int_0^\infty S(x)\,dx=\int_0^\infty P(X>x)\,dx,\qquad X\ge0,$$

$$E[X^k]=\int_0^\infty k\,x^{k-1}S(x)\,dx \qquad \text{(the matching higher-moment version).}$$

Read it aloud: "the mean is the total area to the right, under the survival curve." Beside its discrete twin $E[X]=\sum_{k\ge0}S(k)$ from Vermilion, the two are *one rule* in two notations — the sum of survival values, melted into an integral of the survival curve.

**Beat 6 — Derive it by swapping the order of integration.** Don't take it on faith — it's the ordinary mean with a double integral flipped, the exact continuous mirror of the discrete derivation (where we swapped the order of two *sums*). Start from $E[X]=\int_0^\infty x\,f(x)\,dx$ for $X\ge0$, and rewrite the value $x$ as an integral of $1$: $x=\int_0^x 1\,dt$. Substitute, then swap the order of the two integrals over the region $0\le t\le x<\infty$:

$$E[X]=\int_0^\infty\!\!\Big(\int_0^x 1\,dt\Big)f(x)\,dx=\int_0^\infty\!\!\Big(\int_t^\infty f(x)\,dx\Big)dt=\int_0^\infty P(X>t)\,dt=\int_0^\infty S(t)\,dt.$$

The inner integral $\int_t^\infty f(x)\,dx$ is exactly $P(X>t)=S(t)$. So the rule is no magic — it is the value-times-density mean with the order of integration reversed, just as the discrete rule was $\sum k\,p(k)$ with the order of two sums reversed. Apply it to our loss:

$$E[X]=\int_0^\infty e^{-x/8}\,dx=\big[-8\,e^{-x/8}\big]_0^\infty=0-(-8)=8.$$

Hand the analyst **$\$8$ thousand** — straight off the survival curve, no density recovered.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $S(x)=e^{-x/8}\Rightarrow E[X]=8$ by direct integration.
- *Twist (bounded support):* if $X$ lives on $[0,2]$ with $S(x)=1-\tfrac{x^3}{8}$, integrate $S$ **only over $[0,2]$** (where $S>0$): $\int_0^2\big(1-\tfrac{x^3}{8}\big)dx=2-\tfrac{16}{32}=\tfrac32=1.5$ — and this matches the $f(x)=\tfrac38 x^2$ density of Concept 1, two roads to the same mean.
- *General (a heavy-ish tail):* $S(x)=\big(\tfrac{2}{2+x}\big)^3$ gives $E[X]=\int_0^\infty\big(\tfrac{2}{2+x}\big)^3 dx=1$ — finite only because the tail decays fast enough; an even heavier tail can make the area (the mean) *infinite*.
- *Edge (the discrete twin, side by side):* for a non-negative integer RV the same idea is the *sum* $E[X]=\sum_{k\ge0}S(k)$ — same rule, the integral replaced by a sum. If a problem gives you $S$ (continuous) or a survival table (discrete), reach for this either way.

**Beat 8 — Picture it: the mean is the area under the survival curve.** Two roads to the same mean. The long road weights every value by its density; the survival road just measures the area under $S$ — and skips the density entirely.

<figure>
<img src="../../assets/diagrams/ch10_survival_integral.png" alt="Two side-by-side panels for a non-negative loss with an exponential law of mean 4. Left ('the long road'): the decaying density f(x) is shaded under the curve, with a red vertical line at the mean E[X]=theta=4, labelled E[X]=int x f(x) dx. Right ('the shortcut'): the survival curve S(x)=P(X>x) falls from 1 at x=0 toward 0, with the entire region beneath it shaded with diagonal hatching and labelled area = int_0^inf S(x) dx = E[X] = 4; a callout notes each strip of width dx at height S(x) adds S(x) dx and the total area is the mean. A Mr. Mime sprite sits in the upper-right margin of the right panel, clear of the curve and the area label, propping up the shaded survival region." style="width:90%; max-width:740px; display:block; margin:1em auto;">
<figcaption>The continuous Darth-Vader rule made visual: for $X\ge0$, the shaded area under the survival curve $S(x)=P(X>x)$ <strong>is</strong> $E[X]$. The left panel weights every value by its density (the long road); the right just integrates $S$ (the shortcut) — same mean, no density required. Each strip of width $dx$ and height $S(x)$ is the continuous echo of one Darth-Vader block $S(k)$.</figcaption>
</figure>

**Beat 9 — Consolidate.** When a problem hands you the survival function (or only the cdf) of a non-negative continuous variable and asks for a mean, you can integrate $S$ directly — skipping the density entirely — knowing to stop the integral at the top of a bounded support, and knowing it's the same rule as the discrete Darth-Vader sum with $\sum$ swapped for $\int$.

::: pokedex-entry
**POKÉDEX ENTRY №03 — Survival-Function (Darth-Vader) Method, Continuous**

For a **non-negative** $X\ge0$:
$$E[X]=\int_0^\infty S(x)\,dx=\int_0^\infty P(X>x)\,dx,\qquad E[X^k]=\int_0^\infty k\,x^{k-1}S(x)\,dx.$$
Discrete twin (ch03): $E[X]=\sum_{k\ge0}S(k)$.

*In plain terms:* the mean is the area under the survival curve — no density needed. It is the discrete Darth-Vader sum with the sum melted into an integral, derived by swapping the order of a double integral.

*Recognition cue:* you're **given $S$ or $F$** (not the density), or the problem is naturally "lasts longer than $x$" / "loss exceeds $x$." Integrate $S$ directly — and confirm $X\ge0$ first.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:170px; text-align:center;">
<img src="../../assets/vs/sabrina.png" alt="Sabrina, the Saffron City Gym Leader" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Sabrina — Saffron's psychic, whose power bent the discrete world smooth</figcaption>
</figure>

Four examples, fading from fully narrated to exam speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because the continuous mean/variance integral is the load-bearing skill of the whole continuous act.

### Worked Example 1 — The Silph Severity Curve (full narration; continuous mean + variance + transform)

**ARCHETYPE:** *Full center + spread of a continuous RV from its density, then a linear payout transform — the bread-and-butter Topic-2 item.*

**Setup.** A Silph policy's loss (in \$thousands) has density $f(x)=\tfrac38 x^2$ on $0\le x\le 2$ and $0$ elsewhere. Find $E[X]$, $E[X^2]$, $\Var(X)$, and $\sigma$. Then a reinsurance payout is $Y=5X+3$; find $E[Y]$ and $\Var(Y)$.

**Step 1 — Identify (what's the question really asking?).** A density with no point mass → pure continuous moments. "$E[X]$/$\Var$" = center by integral and spread; "$Y=5X+3$" = a *linear transform*, so use linearity and the $a^2$ rule, not a new integral.

**Step 2 — Professor's Path (the why).**
*Mean (value $\times$ density, integrated):*
$$E[X]=\int_0^2 x\cdot\tfrac38 x^2\,dx=\tfrac38\Big[\tfrac{x^4}{4}\Big]_0^2=\tfrac38\cdot 4=1.5.$$
*Second moment (LOTUS with $g=x^2$):*
$$E[X^2]=\int_0^2 x^2\cdot\tfrac38 x^2\,dx=\tfrac38\Big[\tfrac{x^5}{5}\Big]_0^2=\tfrac38\cdot\tfrac{32}{5}=2.4.$$
*Variance (computational formula):*
$$\Var(X)=E[X^2]-(E[X])^2=2.4-1.5^2=2.4-2.25=0.15,\qquad \sigma=\sqrt{0.15}\approx 0.387.$$
*Transform (linearity + $a^2$ rule):*
$$E[Y]=5E[X]+3=5(1.5)+3=10.5,\qquad \Var(Y)=5^2\Var(X)=25(0.15)=3.75.$$

**Step 3 — Trainer's Path (the fast how).** For a power-law density $cx^n$ on $[0,b]$, the moments are pure power-rule integrals — don't expand anything. $E[X]=\tfrac38\cdot\tfrac{2^4}{4}$ and $E[X^2]=\tfrac38\cdot\tfrac{2^5}{5}$ are each one line. For the payout, **don't re-integrate**: the $+3$ slides the mean and adds *zero* variance; the $5$ scales the mean and *squares* into the variance. $E[Y]=5(1.5)+3=10.5$, $\Var(Y)=25(0.15)=3.75$.

**Step 4 — Check & pitfall.** Mean $1.5\in[0,2]$ ✓, and it sits in the upper half because $f$ leans right (larger losses heavier) ✓. $E[X^2]=2.4\ge(E[X])^2=2.25$, so $\Var=0.15\ge0$ ✓. **Pitfalls:** integrating $f$ alone (that's $1$, not the mean); writing $\Var=E[X^2]=2.4$ (dropping $-(E[X])^2$); writing $\Var(Y)=5\Var(X)$ or $25\Var(X)+3$. *(Back-ref: Entry №01.)*

### Worked Example 2 — The Claim That Sometimes Pays Nothing (full narration; mixed distribution)

**ARCHETYPE:** *Mean and variance of a mixed distribution — sum the atom, integrate the smooth part, add.*

**Setup.** A policy's loss $X$ (in \$thousands) is **mixed**: with probability $0.4$ it pays exactly $\$0$ (a point mass), and with probability $0.6$ it is uniform on $[0,10]$. Find $E[X]$ and $\Var(X)$.

**Step 1 — Identify.** A spike at $0$ plus a smooth slab → mixed. Split into an **atom** (value $0$, mass $0.4$) and a **sub-density** (the $0.6$ share of a $[0,10]$ uniform).

**Step 2 — Professor's Path (the why).** The sub-density is $f(x)=0.6\cdot\tfrac{1}{10}=0.06$ on $[0,10]$ (share $\times$ unit-uniform height). Total both pieces:
$$E[X]=\underbrace{0\cdot 0.4}_{\text{atom}}+\int_0^{10}x(0.06)\,dx=0+0.06\cdot 50=3.$$
$$E[X^2]=\underbrace{0^2\cdot 0.4}_{\text{atom}}+\int_0^{10}x^2(0.06)\,dx=0+0.06\cdot\tfrac{1000}{3}=20.$$
$$\Var(X)=E[X^2]-(E[X])^2=20-3^2=11,\qquad \sigma=\sqrt{11}\approx 3.317.$$

**Step 3 — Trainer's Path (the fast how).** Weight each piece's *conditional mean* by its probability: atom contributes $0.4\times 0=0$; the $[0,10]$ uniform has conditional mean $5$, contributing $0.6\times 5=3$. So $E[X]=3$ in one line — no integral needed once you recognize the uniform's mean. (For the variance you still need $E[X^2]$, so integrate or use the uniform's $E[X^2]=\tfrac{(b-a)^2}{12}+\bar x^2$ on its share.)

**Step 4 — Check & pitfall.** Masses total $0.4+0.6=1$ ✓; mean $3\in[0,10]$ ✓. **Pitfall:** reporting the uniform's mean $5$ as the answer — that ignores the $0.4$ atom of zero-payouts and pretends the smooth part owns all the probability. The atom must carry its weight: weight the smooth mean by $0.6$. *(Back-ref: Entry №02.)*

### Worked Example 3 — The Mean Straight From the Survival Curve (light guidance; survival method)

**ARCHETYPE:** *Darth-Vader integral when only the survival function (or cdf) is given.*

**Setup.** A non-negative loss $X$ has survival function $S(x)=e^{-x/8}$ for $x\ge0$. Find $E[X]$ **without** recovering the density — then re-find it the long way to confirm.

**Identify.** Given $S$, non-negative $X$ → integrate the survival curve. *Your move: integrate $S$ over $[0,\infty)$.*

$$E[X]=\int_0^\infty S(x)\,dx=\int_0^\infty e^{-x/8}\,dx=\big[-8e^{-x/8}\big]_0^\infty=0-(-8)=8.$$

**Confirm (the long way).** The density is $f(x)=-S'(x)=\tfrac18 e^{-x/8}$, so $E[X]=\int_0^\infty x\cdot\tfrac18 e^{-x/8}\,dx=8$ (the gamma identity $\int_0^\infty x e^{-x/\theta}\,dx=\theta^2$ with $\theta=8$). Same $8$, two roads. ✓

**Check & pitfall.** $S(x)=e^{-x/8}$ is an exponential with mean $8$, so $E[X]=8$ is exactly right ✓. **Pitfall:** integrating the cdf $F(x)=1-e^{-x/8}$ instead of $S$ — that integral diverges (nonsense). Integrate **survival**, not the cdf, and only for $X\ge0$. *(Back-ref: Entry №03.)*

### Worked Example 4 — A Capped Loss (exam speed; mixed via a policy limit)

**ARCHETYPE:** *A continuous loss with an atom created by a cap — recognize the mixed structure and total both pieces.*

**Setup.** Losses are uniform on $[0,10]$ thousand, but the policy **caps the payout at $\$8$** thousand — so any loss above $8$ pays exactly $8$. Let $X$ be the payout. Find $E[X]$.

The cap creates an **atom at $8$** of mass $P(\text{loss}>8)=\tfrac{2}{10}=0.2$, plus the smooth uniform on $[0,8]$ with sub-density $\tfrac{1}{10}$ (mass $0.8$):

$$E[X]=\underbrace{\int_0^8 x\,\tfrac{1}{10}\,dx}_{\text{smooth}}+\underbrace{8\cdot 0.2}_{\text{atom}}=\tfrac{1}{10}\cdot\tfrac{64}{2}+1.6=3.2+1.6=4.8.$$

**Check & pitfall.** Without the cap the uniform mean is $5$; the cap can only *lower* it, and $4.8<5$ ✓. **Pitfall:** forgetting the atom at $8$ (summing only the $[0,8]$ integral gives $3.2$, far too low) — the capped probability $0.2$ must pay its full $8$. *(This is the capped expectation $E[X\wedge 8]$ — the deductibles-and-limits chapter ahead. Back-ref: Entry №02.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — The mean is $\int x\,f$, never $\int f$ (and the second moment is $\int x^2 f$)**

Every continuous-moment problem is a power-rule integral. To get $E[X]$, multiply the density by $x$ *first*, then integrate — $\int f$ alone is always $1$ and is never the mean. For $E[X^2]$, multiply by $x^2$. Keep the slogan from Vermilion: variance is $E[X^2]-(E[X])^2$ — compute both moments, subtract, and never report the raw second moment as the variance. If a "variance" comes out negative, you mis-integrated a moment ($E[X^2]\ge(E[X])^2$ always).
:::

::: trainers-tip
**TRAINER'S TIP — Linearity and the $a^2$ rule don't care if $X$ is continuous**

$E[aX+b]=aE[X]+b$ and $\Var(aX+b)=a^2\Var(X)$ are the *same* in the smooth world as in the countable one — never re-integrate for a rescaled payout. The $+b$ shifts the mean and adds **zero** variance; the $a$ scales the mean and *squares* into the variance. This single habit turns most "payout $=aX+b$" parts into one line.
:::

::: trainers-tip
**TRAINER'S TIP — For a mixed loss, split into atoms + smooth, weight each by its probability**

The instant a loss "pays exactly $c$ with probability $p$" (a deductible refund, a policy cap, a "pays nothing" clause), you have a **mixed** distribution. Don't try to force it into one clean density. Sum the atoms (value $\times$ mass), integrate the smooth sub-density ($x$ or $x^2$ against it), and add — making sure the masses plus the smooth area total $1$. The smooth part is only *its share* of the probability, so weight it accordingly.
:::

::: trainers-tip
**TRAINER'S TIP — Handed $S$ or $F$? Integrate the survival curve**

If a problem gives you the **survival function or cdf** of a non-negative loss and asks for the mean, go straight to $E[X]=\int_0^\infty S(x)\,dx$ (convert $S=1-F$ first if you were given $F$). It deletes the error-prone "differentiate $F$ into $f$, then integrate $xf$" detour. Just confirm $X\ge0$, integrate **survival** (not the cdf), and stop at the top of a bounded support.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

<figure style="margin:1em auto; max-width:150px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket — Jessie, James, and Meowth" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
</figure>

In a Silph Co. supply closet, Meowth has swiped the analyst's claim model. "Lookit dis! Da losses are uniform on zero to ten thousand — so da *average* loss is five grand. We sell 'protection' for a flat six grand a policy, pocket da extra thousand each. Easy money!"

Jessie purrs. "Five grand average, six grand price. We're printing Poké-dollars."

James squints at the screen. "But Jessie… there's a great big *spike* sitting on zero. It says **forty percent of policies pay nothing at all.** Doesn't that drag the average *down*…?"

Meowth waves a paw. "Bah! Da curve is uniform, da uniform averages five! Dat spike's just decoration!" — and prices the whole scheme off a $\$5$k expected loss.

**Where it fails:** Meowth **ignored the point mass.** The loss is *mixed* — an atom of mass $0.4$ at $\$0$ plus a $0.6$ share of the $[0,10]$ uniform — so the smooth part is only $60\%$ of the story. The true expected loss is the weighted total
$$E[X]=\underbrace{0.4\cdot 0}_{\text{atom}}+\underbrace{0.6\cdot 5}_{\text{smooth}}=3\ (\$\text{k}),$$
not $\$5$k. Pricing off $\$5$k overstates the expected loss by two-thirds and leaves $\$3$k of margin *uncollected per policy* — Meowth would actually be *undercutting* a fair price into the ground if the spike sat on the high end instead. The fix is one line: *a mixed mean sums the atoms and integrates the smooth part — weight the smooth piece by its own probability $0.6$, and never treat a point mass as decoration.* (You'll catch Meowth red-handed in Problem C10.8.)
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

This is the literal arithmetic of **pricing a continuous loss.**

An insurer covering property, liability, or health losses models the **severity** $X$ — the size of a claim — as a *continuous* random variable with density $f(x)$, and prices off its **expected value** $E[X]=\int x f(x)\,dx$: the pure premium per claim is the expected claim size. The **variance** $\Var(X)=\int x^2 f-\mu^2$ then drives the risk load and the capital held against a bad year — center *and* spread, exactly as Lt. Surge taught with magnitude and reliability, now for a smooth loss.

**Mixed distributions are not an edge case — they are how every real policy pays.** The moment a contract has a **deductible** (losses below $d$ pay nothing — an atom at $0$) or a **policy limit** (losses above $u$ pay exactly $u$ — an atom at $u$), the *payment* is a mixed random variable: a smooth body with point masses welded on. Computing $E[\text{payment}]$ is precisely the "sum the atoms, integrate the smooth part" move of Concept 2 — and it is the entire engine of the deductibles-and-limits chapter ahead. Meowth's mistake — pricing off the smooth curve and ignoring the spike of zero-payouts — is the exact error that bankrupts a careless insurer.

The **survival-integral** $E[X]=\int_0^\infty S(x)\,dx$ is just as practical: actuaries compute expected lifetimes, expected time-to-failure, and expected losses straight off the survival curve all day — it is the continuous foundation of **life contingencies** and reliability, and it dodges the density entirely when the survival function is what the data hand you.

*Series bridge:* the mean and variance are the first two **moments** — the start of a ladder (skewness, kurtosis) that runs through all of probability. $E[X]$ and $\Var(X)$ for continuous losses feed directly into **loss models** and **aggregate-claims** theory on the later CAS/SOA exams (STAM, MAS-I), where the deductible/limit atoms of this chapter become daily bread.

*Transfer check:* could you solve this with no Pokémon in it? "A random variable has density $f(x)=\tfrac38 x^2$ on $[0,2]$; find its mean and variance." Same $1.5$ and $0.15$. "A loss is $0$ with probability $0.4$ and uniform on $[0,10]$ otherwise; find the mean." Same $3$. If you can do those, the skill has transferred.
:::

## The Gym Battle — Sabrina's Psychic Challenge (no new badge)

<figure style="margin:1.5em auto; max-width:170px; text-align:center;">
<img src="../../assets/sprites/front/122.png" alt="Mr. Mime, Sabrina's Psychic-type Pokemon and the survival-area mascot" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">#122 Mr. Mime — Sabrina's barrier-builder, who props up the survival area</figcaption>
</figure>

You already hold the **Marsh Badge** — there is no new badge to win in Saffron. But Sabrina, amused that you climbed her tower to study the smooth world, sets you a *psychic challenge* on the Silph Co. claim model: solve it and she'll concede you've mastered continuous moments. (No badge image, no gym battle on the line — just the hardest problem on the floor, at exam difficulty.)

**Sabrina's Challenge.** "Three of my analysts each described the *same* policy's loss $X$ a different way," she says, the room bending faintly. "Reconcile them, then price it."

- **Analyst A** gives the **density**: $f(x)=\tfrac{1}{8}e^{-x/8}$ on $x\ge0$ — a pure exponential severity (in \$thousands).
- **Analyst B** gives only the **survival function**: $S(x)=e^{-x/8}$, and dares you to find $E[X]$ *without touching the density*.
- **Analyst C** says the *policy* only pays after a clause kicks in: it pays **nothing** if the loss is below $\$8$k (probability $P(X<8)$), and otherwise pays the loss minus $\$8$k. Find the **expected payment** of Analyst C's policy.

"Show me $E[X]$ two ways agree, then the expected payment. Convince me, Trainer."

**ARCHETYPE:** *Continuous mean by two routes (density integral **and** survival integral) that must agree, then a mixed/conditional payment with an atom at $0$ — an integrative Topic-2/2e item.*

**Step 1 — Identify.** A, B describe the *same* exponential loss two ways — the means must match. C is a **deductible**: a payment that is $0$ for losses below $8$ (an atom at $0$) and $(\text{loss}-8)$ above it (a smooth part) → mixed.

**Step 2 — $E[X]$ two ways (A and B must agree).**
*Survival road (B):* $E[X]=\int_0^\infty S(x)\,dx=\int_0^\infty e^{-x/8}\,dx=8.$
*Density road (A):* $E[X]=\int_0^\infty x\cdot\tfrac18 e^{-x/8}\,dx=8$ (gamma identity $\int_0^\infty x e^{-x/\theta}dx=\theta^2$, $\theta=8$).
Both give $E[X]=\$8$k. ✓ The survival road is the one-line shortcut; the density road confirms it.

**Step 3 — Analyst C's expected payment (the deductible — a mixed payment).** The payment is $X-8$ when $X>8$ and $0$ otherwise: a payment random variable $(X-8)_+$. By memorylessness of the exponential, *given* the loss exceeds $8$, the excess $X-8$ is itself a fresh $\mathrm{Exp}(8)$ with mean $8$; and $P(X>8)=S(8)=e^{-8/8}=e^{-1}\approx0.3679$. So the expected payment is the probability of paying times the conditional mean payment — the smooth part — plus the atom at $0$ (which contributes nothing):

$$E[(X-8)_+]=\underbrace{P(X<8)\cdot 0}_{\text{atom at }0}+\underbrace{P(X>8)\cdot E[X-8\mid X>8]}_{\text{smooth part}}=e^{-1}\cdot 8\approx 0.3679\cdot 8\approx \$2.94\text{k}.$$

Equivalently, by the survival method shifted by the deductible, $E[(X-8)_+]=\int_8^\infty S(x)\,dx=\int_8^\infty e^{-x/8}\,dx=8e^{-1}\approx 2.94$ — same answer, straight off the survival tail.

**Step 4 — Check, verdict & the pitfall Sabrina is testing.** The two $E[X]$ routes agree at $\$8$k ✓. The expected payment $\$2.94$k is far below the full $\$8$k mean — most policies (about $63\%$) pay nothing, dragging the average payment down — exactly the **mixed/atom** effect. **Verdict:** price the deductible policy off $\$2.94$k, not $\$8$k. The pitfall Sabrina probes is *ignoring the atom of zero-payouts* (Meowth's exact error) — the deductible creates a point mass at $0$, and the expected payment must weight the smooth part by $P(X>8)$, never report the full-loss mean.

> "...You reconciled all three and never lost the spike at zero," Sabrina says, the room settling. "The smooth world is yours, Trainer. Go — the open road is waiting."

*(The deductible payment $(X-d)_+$ and the capped payment $X\wedge u$ get their own full chapter ahead; here they're a worked sighting of the mixed-moment machinery you just built.)*

## The Gym Challenge — Problem Set

::: problem-set
**THE SILPH CO. CLAIM FLOOR — your questline.** No badge rides on this leg, but Sabrina has set you a single escalating mission on the smooth-world claim model: first the **Route Trainer** legs (warming up continuous integrals on simple densities), then the **Gym Battle** tier (the boss fight — full mean/variance/mixed/survival problems at exam difficulty), then the optional **Elite Challenge** post-game. Work it timed (~6 min/problem), then check the **Answers** below. Hit the mastery bar (**80%+ with correct method**) to clear the questline. Problems are listed first; full worked solutions follow afterward. Markers: 🔴 routine method · 🟡 routine-with-a-twist · 🔵 stretch.

Several problems share the **Silph severity density** $f(x)=\tfrac38 x^2$ on $[0,2]$ (so $E[X]=1.5$, $E[X^2]=2.4$, $\Var(X)=0.15$ as derived in Concept 1) and the **mixed analyst loss** ($0$ w.p. $0.4$; uniform on $[0,10]$ w.p. $0.6$). Each problem restates whatever it needs, so you can work them in any order.

### Route Trainers (the early legs — warming up the integrals)

**C10.1.** 🔴 *(A simple uniform severity.)* A loss $X$ is uniform on $[0,6]$ (in \$thousands), $f(x)=\tfrac16$. Find $E[X]$ and $\Var(X)$.

**C10.2.** 🔴 *(Mean of a triangular density.)* $X$ has density $f(x)=\tfrac{x}{2}$ on $0\le x\le 2$. Find $E[X]$.

**C10.3.** 🔴 *(Survival straight to the mean.)* A non-negative loss has survival $S(x)=e^{-x/5}$, $x\ge0$. Find $E[X]$ by the survival method.

**C10.4.** 🟡 *(Second moment, then variance.)* For the Silph density $f(x)=\tfrac38 x^2$ on $[0,2]$ (given $E[X]=1.5$), find $E[X^2]$ and $\Var(X)$.

**C10.5.** 🟡 *(Rescale a continuous payout.)* For the Silph loss ($E[X]=1.5$, $\Var(X)=0.15$ — both given), a payout is $Y=4X+2$. Find $E[Y]$ and $\Var(Y)$ without re-integrating.

**C10.6.** 🔴 *(A bare point mass plus a uniform.)* $X$ is $0$ with probability $0.5$ and uniform on $[0,4]$ with probability $0.5$. Find $E[X]$.

**C10.7.** 🟡 *(LOTUS — a nonlinear payoff.)* For $X$ uniform on $[0,3]$, find $E[X^2]$ by LOTUS, and note it is **not** $(E[X])^2$.

**C10.26.** 🔴 *(DECISION — two severities, same mean, pick the steadier.)* Loss $A$ is uniform on $[2,6]$; loss $B$ is uniform on $[0,8]$. Find each mean (they match) and each variance, then say which an insurer prefers for predictability.

> *Questline beat: the integrals are warm and the spikes make sense. The boss fights begin.*

### Gym Battles (the boss fight — true SOA difficulty)

**C10.8.** 🟡 *(AUDIT — Team Rocket ignores the point mass.)* The mixed loss is $0$ w.p. $0.4$ and uniform on $[0,10]$ w.p. $0.6$. Meowth's note declares "the loss is uniform, so the average is **$\$5$k**." Find the true $E[X]$ and name Meowth's error.

**C10.9.** 🟡 *(Full center + spread of a continuous severity.)* A loss has density $f(x)=2(1-x)$ on $0\le x\le 1$. Find $E[X]$, $E[X^2]$, $\Var(X)$.

**C10.10.** 🟡 *(Mean from a cdf via survival.)* A loss has cdf $F(x)=1-e^{-x/4}$ on $x\ge0$. Find $E[X]$ by the survival method (convert $S=1-F$ first).

**C10.11.** 🔵 *(Mixed mean AND variance.)* A loss is $0$ w.p. $0.3$ and exponential with mean $10$ w.p. $0.7$. Find $E[X]$ and $E[X^2]$, then $\Var(X)$. *(Use $E[\text{Exp}]=\theta$, $E[\text{Exp}^2]=2\theta^2$.)*

**C10.12.** 🟡 *(Survival method on a bounded support.)* A loss lives on $[0,3]$ with survival $S(x)=1-\tfrac{x^2}{9}$. Find $E[X]=\int_0^3 S(x)\,dx$.

**C10.13.** 🔵 *(RIVAL TRAP — Gary prices off the peak.)* Gary's loss model has density $f(x)=\tfrac38 x^2$ on $[0,2]$. He says "the density peaks at $x=2$, so the expected loss is about $2$ — price it there." Find the true $E[X]$, compare to his $2$, and name his error (mode-vs-mean, now continuous).

**C10.14.** 🟡 *(LOTUS — a nonlinear continuous payout.)* For the Silph loss $f(x)=\tfrac38 x^2$ on $[0,2]$, a bonus pays $g(X)=X^2$. Find $E[g(X)]=E[X^2]$ and note why it is **not** $(E[X])^2$.

**C10.15.** 🔵 *(A capped loss — atom at the cap.)* Losses are uniform on $[0,12]$ but the payout is capped at $\$9$k (loss above $9$ pays $9$). Find the expected payout $E[X\wedge 9]$.

**C10.16.** 🔵 *(AUDIT — a dropped variance term, continuous.)* An analyst computes $E[X]=1.5$ and $E[X^2]=2.4$ for a severity, then writes "so $\Var(X)=2.4$." Find the true variance and name the error.

**C10.17.** 🟡 *(Transform then report.)* For a loss with $E[X]=10$ and $\Var(X)=25$ (both given), a reinsurance payment is $Y=0.8X+1$. Find $E[Y]$ and $\Var(Y)$.

**C10.24.** 🟡 *(AUDIT — Team Rocket integrates the cdf.)* A non-negative loss has $S(x)=e^{-x/6}$. Jessie computes "$\int_0^\infty F(x)\,dx$" to get the mean and finds it blows up. Find the true $E[X]$ and name Jessie's error.

> *Questline beat: you reconciled densities, survivals, and spikes. The post-game below is optional — the integrative stretch problems.*

### Elite Challenge (post-game — integrative / stretch)

**C10.19.** 🔵 *(Survival + transform together.)* A non-negative loss has $S(x)=e^{-x/4}$, $x\ge0$. (a) Find $E[X]$ by the survival method. (b) If $Y=3X$, find $E[Y]$. (c) Given additionally $E[X^2]=32$, find $\Var(Y)$.

**C10.20.** 🔵 *(Two roads to one mean.)* For $f(x)=\tfrac38 x^2$ on $[0,2]$, its survival is $S(x)=1-\tfrac{x^3}{8}$ on $[0,2]$. Find $E[X]$ **both** by $\int_0^2 x f(x)\,dx$ and by $\int_0^2 S(x)\,dx$, and confirm they agree.

**C10.21.** 🔵 *(DECISION — a deductible's effect on expected payment.)* A loss is exponential with mean $8$. A policy pays the loss minus a $\$8$k deductible, $0$ if the loss is smaller. Given $E[(X-8)_+]=\int_8^\infty e^{-x/8}\,dx$, find the expected payment, and decide: is pricing this policy off the full mean ($\$8$k) too high or too low, and by how much?

**C10.23.** 🔵 *(RIVAL TRAP — Gary forgets to square the scale, continuous.)* A continuous severity has $\Var(X)=9$. Gary doubles every payout, $Y=2X$, and says "the variance just doubles too, so $\Var(Y)=18$." Find the true $\Var(Y)$ and name Gary's error.
:::

## Answers

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

### Quick-Answer Table

| # | Answer | Archetype | | # | Answer | Archetype |
|---|---|---|---|---|---|---|
| C10.1 | $E=3,\ \Var=3$ | standard | | C10.13 | $E[X]=1.5<2$; Gary wrong | rival_trap |
| C10.2 | $4/3\approx1.333$ | standard | | C10.14 | $2.4\ne 2.25$ | standard |
| C10.3 | $5$ | standard | | C10.15 | $E[X\wedge 9]=5.625$ | standard |
| C10.4 | $E[X^2]=2.4,\ \Var=0.15$ | standard | | C10.16 | $\Var=0.15$ (not $2.4$) | audit |
| C10.5 | $E=8,\ \Var=2.4$ | standard | | C10.17 | $E=9,\ \Var=16$ | standard |
| C10.6 | $1.0$ | standard | | C10.24 | $E[X]=6$ (integrate $S$, not $F$) | audit |
| C10.7 | $E[X^2]=3\ne 2.25$ | standard | | C10.19 | $4;\ 12;\ 144$ | standard |
| C10.8 | $E[X]=3$ (not $5$) | audit | | C10.20 | $1.5$ both ways | standard |
| C10.9 | $E=1/3,\ \Var=1/18$ | standard | | C10.21 | $\approx 2.94$; full mean too high | decision |
| C10.10 | $4$ | standard | | C10.23 | $\Var(Y)=36$ (forgot the square) | rival_trap |
| C10.11 | $E=7,\ E[X^2]=140,\ \Var=91$ | standard | | C10.26 | mean $4$; $\Var_A=4/3<\Var_B=16/3$; pick A | decision |
| C10.12 | $2.0$ | standard | | | | |

**C10.1** — *(standard) Uniform moments (Entry №01).* $E[X]=\int_0^6 x\tfrac16\,dx=\tfrac16\cdot 18=3$. $E[X^2]=\int_0^6 x^2\tfrac16\,dx=\tfrac16\cdot 72=12$, so $\Var(X)=12-3^2=3$. (Matches $\tfrac{(b-a)^2}{12}=\tfrac{36}{12}=3$.)

**C10.2** — *(standard) Mean of a density (Entry №01).* $E[X]=\int_0^2 x\cdot\tfrac{x}{2}\,dx=\tfrac12\int_0^2 x^2\,dx=\tfrac12\cdot\tfrac{8}{3}=\tfrac{4}{3}\approx1.333.$

**C10.3** — *(standard) Survival method (Entry №03).* $E[X]=\int_0^\infty e^{-x/5}\,dx=\big[-5e^{-x/5}\big]_0^\infty=5.$

**C10.4** — *(standard) Second moment + variance (Entry №01).* $E[X^2]=\int_0^2 x^2\cdot\tfrac38 x^2\,dx=\tfrac38\cdot\tfrac{32}{5}=2.4$; $\Var(X)=2.4-1.5^2=0.15.$

**C10.5** — *(standard) Linear transform (Entry №01).* $E[Y]=4E[X]+2=4(1.5)+2=8$; $\Var(Y)=4^2\Var(X)=16(0.15)=2.4.$ (The $+2$ adds no variance.)

**C10.6** — *(standard) Mixed mean (Entry №02).* Atom $0\cdot 0.5=0$; smooth $0.5\times(\text{mean of }[0,4]=2)=1.0$. $E[X]=0+1.0=1.0.$

**C10.7** — *(standard) LOTUS, nonlinear $g$ (Entry №01).* $E[X^2]=\int_0^3 x^2\tfrac13\,dx=\tfrac13\cdot 9=3$. This is **not** $(E[X])^2=1.5^2=2.25$ — average the square, don't square the average. (Their gap, $0.75$, is the variance.)

**C10.8** — *(audit) Ignored point mass (Entry №02).* True mean: atom $0.4\cdot 0=0$ plus smooth $0.6\times 5=3$, so $E[X]=3$ (not $5$). **Meowth's error:** he treated the smooth uniform as the whole distribution and ignored the $0.4$ atom of zero-payouts; the smooth part is only $60\%$ of the probability, so its mean of $5$ must be weighted by $0.6$.

**C10.9** — *(standard) Full center + spread (Entry №01).* $E[X]=\int_0^1 x\cdot 2(1-x)\,dx=2\big(\tfrac12-\tfrac13\big)=2\cdot\tfrac16=\tfrac13.$ $E[X^2]=\int_0^1 x^2\cdot2(1-x)\,dx=2\big(\tfrac13-\tfrac14\big)=2\cdot\tfrac{1}{12}=\tfrac16.$ $\Var(X)=\tfrac16-(\tfrac13)^2=\tfrac16-\tfrac19=\tfrac{1}{18}\approx0.0556.$

**C10.10** — *(standard) Survival from a cdf (Entry №03).* $S(x)=1-F(x)=e^{-x/4}$; $E[X]=\int_0^\infty e^{-x/4}\,dx=4.$

**C10.11** — *(standard) Mixed mean + variance (Entry №02).* Atom $0$; exponential mean $\theta=10$ on share $0.7$: $E[X]=0.7\cdot 10=7.$ Second moment: $E[\text{Exp}^2]=2\theta^2=200$ on share $0.7$, so $E[X^2]=0.7\cdot 200=140.$ $\Var(X)=140-7^2=140-49=91.$

**C10.12** — *(standard) Survival on bounded support (Entry №03).* $E[X]=\int_0^3\big(1-\tfrac{x^2}{9}\big)dx=3-\tfrac19\cdot\tfrac{27}{3}=3-1=2.0.$

**C10.13** — *(rival_trap) Mode-vs-mean, continuous (Entries №01).* The density's peak ("mode") is at $x=2$, but the *mean* is $E[X]=\int_0^2 x\tfrac38 x^2\,dx=1.5$. **Gary is wrong:** the peak of the density is not the expected value; $E[X]=1.5$, not $2$. Pricing at the mode overstates the expected loss. (Continuous echo of the discrete mode-as-mean trap.)

**C10.14** — *(standard) LOTUS, nonlinear $g$ (Entry №01).* $E[X^2]=\int_0^2 x^2\cdot\tfrac38 x^2\,dx=2.4.$ This is **not** $(E[X])^2=1.5^2=2.25$ — you must average the squares, not square the average. Their gap, $0.15$, is exactly the variance.

**C10.15** — *(standard) Capped loss / atom at the cap (Entry №02).* Smooth part $\int_0^9 x\tfrac{1}{12}\,dx=\tfrac{1}{12}\cdot\tfrac{81}{2}=3.375$; atom at $9$ of mass $P(\text{loss}>9)=\tfrac{3}{12}=0.25$ contributes $9(0.25)=2.25$. So $E[X\wedge 9]=3.375+2.25=5.625.$ Cross-check via the survival form $E[X\wedge u]=\int_0^u S(x)\,dx$ with $S(x)=1-\tfrac{x}{12}$: $\int_0^9\big(1-\tfrac{x}{12}\big)dx=9-3.375=5.625$ ✓ — both roads agree.

**C10.16** — *(audit) Dropped $(E[X])^2$ term (Entry №01).* $\Var(X)=E[X^2]-(E[X])^2=2.4-1.5^2=2.4-2.25=0.15.$ The analyst reported the **raw second moment** $2.4$ as the variance, forgetting to subtract $(E[X])^2$. True $\Var=0.15.$

**C10.17** — *(standard) Linear transform of a known mean/variance (Entry №01).* $E[Y]=0.8E[X]+1=0.8(10)+1=9$; $\Var(Y)=0.8^2\Var(X)=0.64(25)=16.$ (The $+1$ contributes no variance.)

**C10.24** — *(audit) Integrated the cdf, not survival (Entry №03).* The mean is $\int_0^\infty S(x)\,dx=\int_0^\infty e^{-x/6}\,dx=6.$ **Jessie's error:** she integrated the **cdf** $F(x)=1-e^{-x/6}$, which grows toward $1$ and gives a divergent integral — you integrate the **survival** $S$, not $F$. True $E[X]=6.$

**C10.19** — *(standard) Survival + transform (Entries №03, №01).* (a) $E[X]=\int_0^\infty e^{-x/4}\,dx=4.$ (b) $E[Y]=3E[X]=12.$ (c) $\Var(X)=E[X^2]-(E[X])^2=32-16=16$; $\Var(Y)=3^2\Var(X)=9(16)=144.$

**C10.20** — *(standard) Two roads to one mean (Entries №01, №03).* Density road: $\int_0^2 x\tfrac38 x^2\,dx=1.5.$ Survival road: $\int_0^2\big(1-\tfrac{x^3}{8}\big)dx=2-\tfrac18\cdot\tfrac{16}{4}=2-0.5=1.5.$ Both give $E[X]=1.5$ ✓.

**C10.21** — *(decision) Deductible's effect on expected payment (Entries №02, №03).* $E[(X-8)_+]=\int_8^\infty e^{-x/8}\,dx=\big[-8e^{-x/8}\big]_8^\infty=8e^{-1}\approx 8(0.3679)=2.943.$ **Decision:** pricing off the full mean $\$8$k is **far too high** — the deductible creates an atom of zero-payouts (about $63\%$ of losses pay nothing), so the expected *payment* is only $\approx\$2.94$k. Pricing at $\$8$k overstates the expected payment by about $\$5.06$k per policy.

**C10.23** — *(rival_trap) Forgetting to square the scale (Entry №01).* $\Var(2X)=2^2\Var(X)=4(9)=36$, not $18$. **Gary's error:** a scale factor $a$ multiplies the variance by $a^2$, not by $a$ — he doubled when he should have multiplied by four.

**C10.26** — *(decision) Equal means, choose by variance (Entries №01).* Means: $A$ uniform on $[2,6]$ has $E=4$; $B$ uniform on $[0,8]$ has $E=4$ — identical. Variances: $\Var_A=\tfrac{(6-2)^2}{12}=\tfrac{16}{12}=\tfrac43\approx1.33$; $\Var_B=\tfrac{(8-0)^2}{12}=\tfrac{64}{12}=\tfrac{16}{3}\approx5.33$. An insurer **prefers loss $A$** for predictability — same expected loss, one-quarter the variance. Same mean, different spread — the magnitude-vs-reliability theme, now continuous.
:::

## Badge Earned — Continuous Moments Mastered (no new badge this leg)

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/sprites/front/64.png" alt="Kadabra, the Psychic-type Pokemon that warped the discrete world into a smooth curve" style="width:120px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption class="badge-caption"><strong>Continuous moments mastered.</strong> Rank: Ace Trainer · 6 badges (no new badge — you already hold the Marsh Badge).</figcaption>
</figure>

You climbed the Silph Co. tower and learned to find the center and spread of a *smooth* loss — and to handle the spike welded onto it. There's **no new badge** here (Saffron's Marsh Badge is already in your case), but Sabrina conceded you've mastered the continuous moment machinery. **Rank: Ace Trainer · 6 badges.** Six down — the road out of Saffron leads to the smooth continuous wilds.

**Mastery checklist — tick each before you move on (mapped 1-to-1 to the SOA outcomes):**

- ☐ **(2c)** I can compute the **mean** $E[X]=\int x f\,dx$, any $E[g(X)]=\int g\,f\,dx$ (LOTUS), and the **variance** $E[X^2]-(E[X])^2$ of a continuous RV, and apply $E[aX+b]=aE[X]+b$ and $\Var(aX+b)=a^2\Var(X)$. *(Rematch: Concept 1, WE 1, Problems C10.1, C10.4, C10.5, C10.9, C10.14.)*
- ☐ **(2c/2d)** I can compute the moments of a **mixed distribution** by summing the point masses and integrating the smooth part, each weighted by its probability. *(Rematch: Concept 2, WE 2 & 4, Problems C10.6, C10.8, C10.11, C10.15.)*
- ☐ **(2c)** I can use the **survival-function method** $E[X]=\int_0^\infty S(x)\,dx$ for a non-negative loss, derived by swapping the order of integration, and know it's the continuous twin of $\sum_{k\ge0}S(k)$. *(Rematch: Concept 3, WE 3, Problems C10.3, C10.10, C10.12, C10.20.)*
- ☐ **(2c)** I never report $\int f$ as the mean, never write $E[X^2]=(E[X])^2$, never drop the $-(E[X])^2$ term, never ignore a point mass, and never integrate the cdf for the survival method. *(Rematch: the four Trainer's Tips; Problems C10.8, C10.16, C10.24.)*

**Gym Rematch pointers.** Ignored a point mass? Concept 2 Beat 4 and the Team Rocket Trap, then C10.8. Reported the density peak as the mean? Concept 1 Beat 8 (mean vs mode), then C10.13. Dropped the $(E[X])^2$ term? Concept 1 Beat 6, then C10.16. Integrated the cdf instead of the survival? Concept 3 Beat 4, then C10.24. Forgot to square the scale on a transform? Concept 1 Beat 7, then C10.23.

> Next stop: **the smooth continuous wilds**, the long water-routes and wild stretches between Kanto's cities, where you'll meet the four named continuous shapes — uniform, exponential, gamma, and beta — each just a specific $f(x)$ poured into the very machine you built here. Pack your integrals; every shape comes with a mean and a variance.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
