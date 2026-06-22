<!--
  file: ch05_discrete_distributions
  tier: B
  outcomes: 2d
  tia: A.5 (A.5.0a geometric series; A.5.0b Taylor series for e^x; A.5.1 geometric;
       A.5.2 memoryless; A.5.3 negative binomial; A.5.4 Poisson;
       A.5.5 sums of independent Poissons)
  locale: Lavender Town (Pokemon Tower) -> Celadon City
  type: ghost
  maps_to: Pokemon Tower ghost swarm (Poisson counts) + Celadon Game Corner (waiting
           games) + Erika's Rainbow Badge gym battle
-->

# The Waiting Games and the Ghost Count {.type-ghost}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with the route from Cerulean through Lavender Town to Celadon City highlighted; the haunted Pokemon Tower and Erika's gym at the Celadon Game Corner district are marked as the current destination." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 10 — past the haunted Pokémon Tower of Lavender Town to Celadon City, home of the Game Corner and the Rainbow Badge: the city of <em>named chance</em>.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Tower of Terror"**

Lavender Town at dusk. The Pokémon Tower rises seven storeys into a violet sky, and the air hums with a static that makes Pikachu's cheeks spark on their own. You climb because the candlelight keeps guttering — and on every landing, **Gastly** wink in and out of the dark, never the same number twice. On the third-floor stairwell you count: in the first minute, two appear. In the next, none. Then four. Then one.

"You can't fight what you can't *predict*," Misty whispers, gripping her Staryu.

But you *can* predict it — not the exact count, but the **pattern**. The tower caretaker has kept a visitor's log for years. "Look," he says, tapping a column of tallies. "Over thousands of minutes the average barely moves: about **three Gastly a minute**. Whatever law governs this place, it's *stable*."

Your Pokédex flickers into Actuary Mode. *"To pass the next floor safely you must wait for a lull — a stretch with very few ghosts. Estimate the probability that the next five minutes bring fewer than ten Gastly, so the party can move."*

Three a minute, on average. Random, but lawful. You need the probability of a **count** with no upper limit — and a count is a thing your moment tools from Vermilion can *summarize* but cannot *predict*. Then Pikachu tugs your sleeve and points downhill, toward the neon glow of **Celadon City**, where a Game Corner slot is already eating coins one pull at a time. Counts everywhere: ghosts per minute, pulls until the first win, rounds until the third. Each is random, yet each follows a *named law* you could read off a card — if only you knew the card.

*How do you put a named law to a thing you can only count — and answer "how many?" and "how long until?" before you've taken a single sample?*
:::

## Where You Are — 60-Second Retrieval

**Rank: Junior Trainer · Badges: 3 (Cascade, Thunder, Boulder).** You earned the **Boulder Badge** at Pewter by learning to **count by rule** — permutations, combinations, and the **binomial**: out of a *fixed* number $n$ of independent trials, the count of successes $X\sim\Binom(n,p)$ has $p(k)=\binom{n}{k}p^k q^{n-k}$, mean $np$, variance $npq$. That binomial is the load-bearing idea you carry into the Tower. Every distribution in this chapter is the binomial's machinery *re-pointed*: instead of fixing the trials and letting the successes float, you will **fix the success and let the trials float** (waiting games), or let the trials become **infinitely many and rare** (the ghost count). Hold the binomial in one hand; we re-aim it in the other.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own Pewter**

Answer from memory; if any feels shaky, flip back before continuing.

1. $X\sim\Binom(10,0.2)$. What are $E[X]$ and $\Var(X)$? *(Answer: $np=2$ and $npq=10(0.2)(0.8)=1.6$.)*
2. What does $\binom{n}{k}$ count, and what is $\binom{4}{2}$? *(Answer: the number of ways to choose $k$ of $n$ positions; $\binom{4}{2}=6$.)*
3. For any pmf, what must $\sum_k p(k)$ equal? *(Answer: exactly $1$.)*

All three instant? You're ready — the binomial reflex and "probabilities sum to 1" reflex are the entire foundation here. Any hesitation? Reclaim it first.
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP023 "The Tower of Terror" + EP024 "Haunter Versus Kadabra" + EP026 "Pokémon Scent-sation!"**

<figure><img src="../../assets/stills/ch05_now_playing.jpg" alt="Ash and Pikachu lifted off the floor by a Haunter inside the haunted Pokémon Tower (Indigo League EP023)." style="width:60%; max-width:440px; display:block; margin:0.4em auto;"><figcaption style="font-size:0.8em; color:#555;">Pokémon Tower, EP023 — ghosts arriving one by one at random: the Poisson count and the geometric wait.</figcaption></figure>

In **EP023** Ash climbs the haunted **Pokémon Tower** of Lavender Town, where **Gastly** (and a mischievous **Haunter**) flit in and out of the dark — the ghost *count* our cold open dramatizes (the caretaker's "three a minute" log is an in-world extension for the math, not an on-screen line). In **EP024** that **Haunter** follows Ash to Saffron and turns the tide of a gym battle, our living picture of *one more independent ghost added to the stream* (the Poisson-superposition beat). In **EP026** Ash reaches **Celadon City** and meets **Erika**, the Grass-type Gym Leader of the perfumed gym — the **Rainbow Badge** is the prize this chapter ends on, and the Game Corner next door is where every *waiting game* (slot pulls, rounds until a win) plays out. *Watch EP023 → EP024 → EP026 right before this chapter* — the ghost swarm, the extra Haunter, and Erika's gym are the three scenes the math lives in.
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice crackles through the Pokédex's Actuary Mode as you climb past the candlelight.

"Lavender and Celadon are the cities of *named patterns*, Ash. Chance tells only a handful of stories with whole-number counts — *wait for a win, wait for the $r$-th win, count events in a window* — and each story has a distribution with a name, a formula, a mean, and a variance. The exam will not ask you to *invent* these; it hands you a **story** and rewards you for **recognizing** which named law it is in under a minute. But two of these — the **geometric** and the **Poisson** — only make sense if you first own two pieces of pure algebra: the **geometric series** and the **Taylor series for $e^x$**. Sharpen those tools first; everything else falls out of them. This is a **Tier B** chapter — the machinery is light, the *recognition and the series* are where the depth goes."

By the end of this chapter you will be able to:

- **Sum a geometric series** $\sum_{k\ge0} ar^k=\dfrac{a}{1-r}$ (for $|r|<1$) and recognize the **Taylor series** $e^x=\sum_{k\ge0}\dfrac{x^k}{k!}$ — the two algebraic tools the named laws are built from. *(Outcome 2d, series toolkit A.5.0a/b.)*
- **Recognize and apply** the **geometric** distribution (wait for the first success), state its mean/variance in either convention, and exploit its **memorylessness**. *(Outcome 2d.)*
- **Recognize and apply** the **negative binomial** (wait for the $r$-th success) as $r$ independent geometrics summed, with the clinching success locked on the last trial. *(Outcome 2d.)*
- **Recognize and apply** the **Poisson** (counts over a window) — its pmf, mean $=$ variance $=\lambda$, the binomial limit, and the rule that $\lambda$ **scales with the window**. *(Outcome 2d.)*
- **Add independent Poissons** by **superposition** ($\Poisson(\lambda_1)+\Poisson(\lambda_2)=\Poisson(\lambda_1+\lambda_2)$). *(Outcome 2d.)*

> *Exam-weight signpost.* These count-and-wait families sit inside the **Univariate Random Variables** block — the **single largest** slice of Exam P (≈44–50%). This is a **Tier B** chapter: the pmf/mean/variance *machinery* you already own from ch03–ch04, so the new work is **recognition + the two series + the four shortcuts (memoryless, $r$-stacked geometrics, the binomial→Poisson limit, Poisson additivity)**, and that is where the depth here is spent.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own the Tower and the Game Corner?**

Already fluent with the waiting games and the ghost count? Prove it. Work these six, ~1–3 minutes each, *with the right family named*:

1. Sum $\sum_{k=0}^{\infty} 3(0.4)^k$ and state the convergence condition.
2. A slot wins each pull w.p. $0.15$; you pull until the first win. Find $P(\text{more than }5\text{ pulls})$.
3. Show $P(X>8\mid X>3)=P(X>5)$ for that geometric, and name the property.
4. You wait for your $3$rd win; each round wins w.p. $0.4$. Find $P(\text{exactly }2\text{ losses before the 3rd win})$ and $E[\text{losses}]$.
5. Gastly appear at $3$/min (Poisson). Find $P(\ge2\text{ in one minute})$ and $P(<10\text{ over five minutes})$.
6. Gastly at $3$/min and Haunter at $1$/min, independent. What is the distribution of *total* ghosts in one minute, and its mean?

*(Answers: (1) $\frac{3}{1-0.4}=5$, needs $|r|<1$; (2) $0.85^5=0.4437$; (3) both $=0.85^5$, memorylessness; (4) $\binom{4}{2}(0.4)^3(0.6)^2=0.1382$, mean $rq/p=4.5$; (5) $1-4e^{-3}=0.8009$ and $P(Y\le9),\lambda=15$, $=0.0699$; (6) $\Poisson(4)$, mean $4$.)* Six for six with the **right family named**? **Skip to the Gym Battle** and claim the badge. Any miss or hesitation? Each concept below has its own skip-gate, so even a partial owner loses no time.
:::

---

We build seven ideas, in TIA's order. The first two are the **series toolkit** — pure algebra the named laws stand on. Then four named laws, easiest mechanism first, and finally the Poisson's power-tool. Each gets a "do you already own this?" skip-check, the full lesson, and a Pokédex Entry.

0a. **The geometric series** — the sum $\sum ar^k=\frac{a}{1-r}$ *(A.5.0a)*
0b. **The Taylor series for $e^x$** — $e^x=\sum \frac{x^k}{k!}$ *(A.5.0b)*
1. **The geometric distribution** — wait for the first success *(A.5.1)*
2. **Memorylessness** — the geometric forgets its past *(A.5.2)*
3. **The negative binomial** — wait for the $r$-th success *(A.5.3)*
4. **The Poisson** — count events over a window *(A.5.4)*
5. **Sums of independent Poissons** — superposition *(A.5.5)*

## Concept 0a — The Geometric Series: The Sum Behind the Wait (A.5.0a)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Geometric series**

Sum $\sum_{k=0}^{\infty} (0.85)^k$, and say what goes wrong if the ratio were $r=1.2$ instead.

If you instantly wrote **$\frac{1}{1-0.85}=\frac{1}{0.15}\approx6.667$** (and know it **diverges** for $|r|\ge1$), **skip to Concept 0b**. If the closed form or the convergence condition is fuzzy, read on — every geometric-distribution formula in this chapter is this one sum in disguise.
:::

> *This is a toolkit interlude, not a distribution — but it is **fully derived and never skipped**, because the geometric pmf, its survival function, and its mean are all this single series.*

**Beat 1 — The one-sentence idea.** *When you add a number, then a fixed fraction of it, then the same fraction of that, forever, the running total settles on a finite limit — provided each step shrinks ($|r|<1$).*

**Beat 2 — Anchor + concrete instance.** On each pass through the Tower's top chamber, a ghost *fails* to appear with probability $q=0.85$. The chance it has still not appeared after $1, 2, 3,\dots$ passes is $0.85,\ 0.85^2,\ 0.85^3,\dots$ — a chain of numbers each $0.85$ times the one before. Sums like $1+0.85+0.85^2+\cdots$ run through every geometric calculation, so we need their value *once and for all*.

**Beat 3 — Reason through it in plain words.** Because each term is a fixed fraction $r$ of the previous one, the tail of the sum is a *scaled copy* of the whole sum. That self-similarity is the whole trick: if $S$ is the total, then "everything after the first term" is exactly $r\cdot S$, so $S = (\text{first term}) + rS$. Solve for $S$ and the infinite sum collapses to a single fraction. The condition $|r|<1$ is what makes the terms shrink to zero fast enough for $S$ to be finite at all — if $r\ge1$ the terms never die and the sum runs off to infinity.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The classic slips are about *where the sum starts* and *whether it converges*.

- **Forgetting the convergence condition.** $\sum r^k=\frac{1}{1-r}$ is **only** valid for $|r|<1$. Plug in $r=1.2$ and you'd get $\frac{1}{1-1.2}=-5$ — a *negative* sum of *positive* terms, which is nonsense. The formula has silently been used outside its domain.
- **Off-by-one on the starting index.** $\sum_{k=0}^{\infty}r^k=\frac{1}{1-r}$ starts at $k=0$ (first term $r^0=1$). If your sum starts at $k=1$, the first term is $r$, not $1$, so $\sum_{k=1}^{\infty}r^k=\frac{r}{1-r}$ — you must subtract the missing $k=0$ term. Always check the lower limit.

**Beat 5 — Translate into notation, one glyph at a time.** A **geometric series** has first term $a$ and common ratio $r$:

$$\sum_{k=0}^{\infty} a\,r^{k}=a+ar+ar^{2}+\cdots \qquad \text{read aloud: ``}a\text{, then }a\text{ times }r\text{, then }a\text{ times }r\text{ again, forever.''}$$

The symbol $r$ is the **ratio** of any term to the one before it; $a$ is the **first** term. Its sum, for $|r|<1$:

$$\boxed{\ \sum_{k=0}^{\infty} a\,r^{k}=\frac{a}{1-r}\ }\qquad(|r|<1).$$

**Beat 6 — Derive the closed form.** Let $S=\sum_{k=0}^{\infty}ar^k$. Multiply the whole series by $r$ — this shifts every term one slot to the right:

$$rS=ar+ar^{2}+ar^{3}+\cdots.$$

Subtract $rS$ from $S$: every term cancels except the very first $a$,

$$S-rS=a \;\Longrightarrow\; S(1-r)=a \;\Longrightarrow\; S=\frac{a}{1-r}.$$

(The subtraction is legitimate precisely because $|r|<1$ makes the leftover "tail at infinity" vanish.) We *derived* the fraction; we did not assert it. For our Tower number, $a=1,\ r=0.85$: $\sum_{k\ge0}0.85^k=\frac{1}{0.15}\approx6.667$. ✓

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $\sum_{k\ge0}(0.5)^k=\frac{1}{1-0.5}=2$.
- *Twist (start at $k=1$):* $\sum_{k=1}^{\infty}(0.5)^k=\frac{0.5}{1-0.5}=1$ — drop the $k=0$ term, or factor out one $r$.
- *General (a leading coefficient):* $\sum_{k\ge0}3(0.4)^k=\frac{3}{1-0.4}=5$.
- *Edge (divergence):* $\sum_{k\ge0}(1.2)^k$ has **no** finite value — terms grow, the formula does **not** apply.

**Beat 8 — Picture it.** Lay the terms down as bars and track the running total: the bars shrink geometrically, and the partial-sum staircase rises but flattens against a ceiling at $\frac{1}{1-r}$.

<figure>
<img src="../../assets/diagrams/ch05_geometric_series.png" alt="A bar-and-line chart of the geometric series with ratio r=0.6. Purple dotted bars show each successive new term r^k shrinking: 1, 0.6, 0.36, 0.216, and so on. A blue line with circle markers traces the partial sum S_n, climbing 1.00, 1.60, 1.96, 2.18, 2.30, ... and flattening toward a red dashed ceiling labeled 1/(1-r) = 2.5. A callout explains that because |r|<1 the terms shrink fast enough that the running total never exceeds 1/(1-r)." style="width:80%; max-width:600px; display:block; margin:1em auto;">
<figcaption>The geometric series with $r=0.6$: each new term (purple) is $r$ times the last, so the partial sums (blue) climb but flatten against the finite ceiling $\frac{1}{1-r}=2.5$. Convergence is exactly the $|r|<1$ condition.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now sum any geometric series in one step, watch the starting index, and refuse to apply the formula when $|r|\ge1$. This single identity computes the geometric distribution's survival function and mean in Concept 1.

::: pokedex-entry
**POKÉDEX ENTRY №01 — The Geometric Series**

$$\sum_{k=0}^{\infty} a\,r^{k}=\frac{a}{1-r}\quad(|r|<1); \qquad \sum_{k=1}^{\infty} a\,r^{k}=\frac{ar}{1-r}.$$

*In plain terms:* a sum whose terms each shrink by a fixed ratio $r$ collapses to "first term over $(1-r)$." It only converges when $|r|<1$.

*Recognition cue:* a sum of the form $a+ar+ar^2+\cdots$, or any "probability it keeps failing" tail. Match the **first term** to $a$ and watch the **starting index**.
:::

## Concept 0b — The Taylor Series for $e^x$: The Sum Behind the Ghost Count (A.5.0b)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Taylor series for $e^x$**

Write the series for $e^x$, and use it to evaluate $\sum_{k=0}^{\infty}\dfrac{\lambda^k}{k!}$.

If you instantly wrote **$e^x=\sum_{k\ge0}\frac{x^k}{k!}$**, so the sum is **$e^{\lambda}$**, **skip to Concept 1**. If the factorial series or that substitution is unfamiliar, read on — it is the *one* fact that makes the Poisson's masses sum to 1.
:::

> *A toolkit interlude, fully derived, never skipped: the Poisson pmf is legal **only because** of this series.*

**Beat 1 — The one-sentence idea.** *The exponential $e^x$ equals the infinite sum $1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots$ — each term the previous one times $\frac{x}{k}$.*

**Beat 2 — Anchor + concrete instance.** The caretaker's ghost count will turn out to have $p(k)=\frac{e^{-\lambda}\lambda^k}{k!}$. For those probabilities to be *legal* they must sum to $1$ — which forces $\sum_{k\ge0}\frac{\lambda^k}{k!}$ to equal $e^{\lambda}$. So before we can write the Poisson at all, we need this series.

**Beat 3 — Reason through it in plain words.** A Taylor series rebuilds a smooth function from its value and all its slopes at a single point. The exponential is the unique function that is *its own derivative* and equals $1$ at $x=0$. So every derivative of $e^x$ at $0$ is $1$, and the Taylor recipe "$k$-th term $=\frac{f^{(k)}(0)}{k!}x^k$" puts a clean $\frac{1}{k!}$ in front of each power. The factorials in the denominator grow so fast that the series converges for *every* $x$ — there is no convergence condition to remember, unlike the geometric series.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The tempting slip is to **drop the factorials** — to imagine $e^x$ behaves like a geometric series $1+x+x^2+\cdots$. It does not: $\sum_{k}x^k=\frac{1}{1-x}$ (and only for $|x|<1$), a completely different function that *blows up* at $x=1$. The $\frac{1}{k!}$ weights are exactly what tames the powers so the sum converges everywhere and reproduces $e^x$. A second slip: forgetting that the series starts at $k=0$ with the term $\frac{x^0}{0!}=1$ (recall $0!=1$).

**Beat 5 — Translate into notation, one glyph at a time.** The series, read one piece at a time:

$$e^{x}=\sum_{k=0}^{\infty}\frac{x^{k}}{k!}=\underbrace{1}_{k=0}+\underbrace{x}_{k=1}+\underbrace{\frac{x^{2}}{2!}}_{k=2}+\underbrace{\frac{x^{3}}{3!}}_{k=3}+\cdots$$

The denominator $k!$ ("$k$ factorial") is $1\cdot2\cdots k$; it is what each power is divided by. Read aloud: *"one, plus $x$, plus $x$-squared over two-factorial, plus $x$-cubed over six, …"*

**Beat 6 — Derive it from the slopes.** Taylor's recipe expands any smooth $f$ about $0$ as $f(x)=\sum_{k\ge0}\frac{f^{(k)}(0)}{k!}x^k$. For $f(x)=e^x$, differentiation does nothing — $\frac{d}{dx}e^x=e^x$ — so *every* derivative is $e^x$, and at $x=0$ every derivative equals $e^0=1$:

$$f^{(k)}(0)=1\ \text{for all }k \;\Longrightarrow\; e^{x}=\sum_{k=0}^{\infty}\frac{1}{k!}x^{k}=\sum_{k=0}^{\infty}\frac{x^{k}}{k!}.$$

Now the payoff that the Poisson needs: substitute $x=\lambda$,

$$\sum_{k=0}^{\infty}\frac{\lambda^{k}}{k!}=e^{\lambda}.$$

So $\sum_{k\ge0}\frac{e^{-\lambda}\lambda^k}{k!}=e^{-\lambda}\cdot e^{\lambda}=e^{0}=1$ — the Poisson masses sum to $1$. Derived, not asserted.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $e^0=1$ from the series (only the $k=0$ term survives).
- *Twist (the key substitution):* $\sum_{k\ge0}\frac{2^k}{k!}=e^2\approx7.389$.
- *General:* $\sum_{k\ge0}\frac{\lambda^k}{k!}=e^{\lambda}$ for any $\lambda$ — and it converges for *every* $\lambda$ (no $|r|<1$ needed).
- *Edge (a moment hidden inside):* $\sum_{k\ge0}k\cdot\frac{e^{-\lambda}\lambda^k}{k!}=\lambda$ — differentiating the series w.r.t. $\lambda$ is how the Poisson mean $\lambda$ pops out (Concept 4 Beat 6).

**Beat 8 — Picture it.** Stack the partial sums against the true curve: each new term lifts the polynomial to hug $e^x$ over a wider stretch, and the fit never stops improving.

<figure>
<img src="../../assets/diagrams/ch05_taylor_exp.png" alt="A line chart on x from -2 to 2. A thick red curve is the true e^x. Four partial-sum polynomials (up to x^1, x^2, x^3, x^5) in different colors and dash styles progressively hug the curve more closely as more terms are added; the degree-5 partial sum is nearly indistinguishable from e^x across the window. A callout notes that setting x=lambda gives sum lambda^k/k! = e^lambda, which is exactly why the Poisson masses sum to 1." style="width:80%; max-width:600px; display:block; margin:1em auto;">
<figcaption>Adding Taylor terms (each $\frac{x^k}{k!}$) makes the polynomial hug $e^x$ ever more tightly. Setting $x=\lambda$ gives $\sum_k \lambda^k/k!=e^{\lambda}$ — the identity that legalizes the Poisson pmf.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now write the $e^x$ series, see why the factorials (not powers alone) make it converge everywhere, and use $\sum_k\frac{\lambda^k}{k!}=e^{\lambda}$ to show the Poisson is a genuine distribution. With both series in hand, the named laws are now easy.

::: pokedex-entry
**POKÉDEX ENTRY №02 — The Taylor Series for $e^x$**

$$e^{x}=\sum_{k=0}^{\infty}\frac{x^{k}}{k!}=1+x+\frac{x^{2}}{2!}+\frac{x^{3}}{3!}+\cdots \quad(\text{all }x); \qquad \sum_{k=0}^{\infty}\frac{\lambda^{k}}{k!}=e^{\lambda}.$$

*In plain terms:* the exponential is a sum of powers each divided by $k!$. The factorials make it converge for **every** $x$. Setting $x=\lambda$ is what makes the Poisson masses total $1$.

*Recognition cue:* a sum with $\frac{(\cdot)^k}{k!}$ in it — collapse it to an exponential. (Contrast the geometric series, which has $r^k$ and needs $|r|<1$.)
:::

## Concept 1 — The Geometric Distribution: Waiting for the First Success (A.5.1)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Geometric**

A wild ghost manifests on each pass w.p. $0.15$; you return until it appears. Find $P(\text{it takes more than }5\text{ passes})$, and state which "geometric convention" you used.

If you wrote **$P(X>5)=0.85^5=0.4437$** and can name your convention (trials-to-first-success), **skip to Concept 2**. If you reached for a binomial coefficient, read on — *waiting* has no fixed $n$ to choose from.
:::

**Beat 1 — The one-sentence idea.** *Keep running independent trials until the first success, and count how long it took — the wait is geometric.*

**Beat 2 — Anchor + concrete instance.** The binomial (Pewter) fixed $n$ and let the successes float; the geometric does the opposite — it **fixes the success at "the first one"** and lets the number of trials float. On each pass through the Tower's top chamber a vengeful ghost manifests w.p. $p=0.15$, independently. You keep returning until it appears. Let $X$ = the pass on which it first shows. *What is $P(X>5)$?*

**Beat 3 — Reason through it in plain words.** "$X>5$" means *the ghost has not appeared in the first $5$ passes* — all $5$ failed. Each failure has probability $q=0.85$, and the passes are independent, so

$$P(X>5)=(0.85)^5=0.4437.$$

More generally, the first success lands *exactly* on pass $k$ when the first $k-1$ passes fail and the $k$-th succeeds: $q^{k-1}p$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two traps live here. First, the **convention** trap: "the wait" can mean the *trial number* of the first success ($X\in\{1,2,\dots\}$) or the *number of failures before* it ($Y=X-1\in\{0,1,\dots\}$). These differ by exactly $1$, so their means differ by $1$ ($E[X]=1/p$ vs. $E[Y]=q/p$) while the **variance is identical** $q/p^2$. Always *state your convention*. Second, the **binomial-coefficient** trap: there is **no** $\binom{\cdot}{\cdot}$ here, because the success position is *forced* to be last — there is only one arrangement of "$k-1$ failures then a success."

**Beat 5 — Translate into notation, one glyph at a time.** *Trials version* ($X$ = trial of first success):

$$X\sim\Geom(p), \qquad p(k)=q^{\,k-1}p, \quad k=1,2,3,\dots$$

Read aloud: *"$k-1$ failures, each a factor $q$, then one success, a factor $p$."* The **survival** function (probability of waiting *past* $m$) is especially clean:

$$P(X>m)=q^{m} \qquad \text{read aloud: ``the first } m \text{ trials all failed.''}$$

**Beat 6 — Derive the mean from the geometric series.** Use the tail-sum (Darth-Vader) rule from ch03 for non-negative integers, $E[X]=\sum_{m\ge0}P(X>m)$, and recognize the **geometric series** of Concept 0a (this is the namesake):

$$E[X]=\sum_{m=0}^{\infty}P(X>m)=\sum_{m=0}^{\infty}q^{m}=\frac{1}{1-q}=\frac{1}{p}.$$

(The series $\sum q^m$ converges because $q=1-p<1$ — exactly the condition Concept 0a demanded.) For $p=0.15$, $E[X]=1/0.15\approx6.67$ passes. The variance (derivable the same way, or quoted) is $\Var(X)=\frac{q}{p^2}=\frac{0.85}{0.0225}\approx37.8$.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $P(X>5)=q^5=0.4437$.
- *Twist (exact landing):* $P(X=3)=q^2p=0.85^2(0.15)=0.1084$ — first two fail, third succeeds.
- *General:* $P(X>m)=q^m$ for any $m$; the mean is $1/p$ (trials) or $q/p$ (failures).
- *Edge ($p=1$):* a sure-thing trial gives $E[X]=1$ — the very first attempt always succeeds.

**Beat 8 — Picture it.** The pmf decays geometrically — each bar is $q$ times the one before — and the right tail past $k=5$ is exactly the survival $q^5$.

<figure>
<img src="../../assets/diagrams/ch05_geometric_pmf.png" alt="A bar chart of the Geometric(0.15) probability mass function in the trials convention. The tallest bar is at k=1 (height 0.150), and each subsequent bar is 0.85 times the previous: 0.150, 0.128, 0.108, 0.092, 0.078, then a red hatched right tail from k=6 onward. A callout marks the shaded right tail k>5 as P(X>5)=q^5=0.4437, all first five throws failing. A small Meowth sprite sits in the upper-right margin, clear of the bars." style="width:80%; max-width:600px; display:block; margin:1em auto;">
<figcaption>$\Geom(0.15)$: each bar is $q=0.85$ times the previous one. The shaded right tail past $k=5$ totals $q^5=0.4437=P(X>5)$. (Meowth, the Game Corner's resident slot-puller, looks on from the margin.)</figcaption>
</figure>

**Beat 9 — Consolidate.** Whenever you **wait for the first success**, it is geometric: tail $q^m$, mean $1/p$ (trials) or $q/p$ (failures), variance $q/p^2$ — and the mean is just the geometric series summed.

::: pokedex-entry
**POKÉDEX ENTRY №03 — The Geometric Distribution**

Independent Bernoulli($p$) trials run until the **first** success. Two conventions:

*Trials version* ($X$ = trial of first success, $X\in\{1,2,\dots\}$):
$$p(k)=q^{\,k-1}p,\quad P(X>m)=q^{m},\quad E[X]=\frac1p,\quad \Var(X)=\frac{q}{p^{2}}.$$
*Failures version* ($Y$ = failures before first success, $Y\in\{0,1,\dots\}$):
$$p(k)=q^{k}p,\quad E[Y]=\frac{q}{p},\quad \Var(Y)=\frac{q}{p^{2}}.$$

*In plain terms:* keep trying until you finally win; count how long it took. The mean is the geometric series $\sum q^m=1/p$.

*Recognition cue:* **"how many tries until the first…," "until it finally happens."** **State your convention** ($\Var$ is identical either way; only the mean shifts by $1$). No binomial coefficient — the success is locked last.
:::

## Concept 2 — Memorylessness: The Geometric Forgets Its Past (A.5.2)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Memorylessness**

For the ghost wait ($p=0.15$), you have already returned $3$ times with no ghost. Find $P(X>8\mid X>3)$.

If you wrote **$P(X>8\mid X>3)=P(X>5)=0.85^5=0.4437$** (the three wasted passes don't matter), **skip to Concept 3**. If you tried to "use up" the failed passes to make a ghost *more* likely, read on — that's the gambler's fallacy, and it's exactly Team Rocket's trap.
:::

**Beat 1 — The one-sentence idea.** *A geometric wait that has already failed $m$ times is, going forward, exactly as fresh as a brand-new wait — the past is forgotten.*

**Beat 2 — Anchor + concrete instance.** You have climbed to the top chamber three times and seen no ghost. It *feels* like a ghost is "overdue." Is your remaining wait any shorter than when you started? Let $X\sim\Geom(0.15)$. The question is $P(X>3+5\mid X>3)$ — given $3$ failures, the chance of $5$ *more* failures.

**Beat 3 — Reason through it in plain words.** Each pass is independent of every other — the ghost has no memory of how many times you've already shown up. The three failed passes are spent and gone; they change nothing about the dice you roll on pass four. So the chance of $5$ more failures *given* $3$ already is the same as the chance of $5$ failures from a cold start. The wait "resets" every time you condition on having waited.

**Beat 4 — Surface and dismantle the tempting wrong idea.** *(This is the chapter's headline Team Rocket trap.)* The seductive error is the **gambler's fallacy** — "I've failed three times, so I'm *due*; a ghost is now more likely." For a memoryless process this is flatly false: past failures **never** raise (or lower) the future chance. The geometric is the **only** discrete distribution with this property, and "we're due" is precisely the reasoning it forbids. A slot that has gone cold is exactly as likely to pay on the next pull as a fresh one — the machine cannot remember your losses.

**Beat 5 — Translate into notation, one glyph at a time.** Memorylessness is the statement

$$P(X>m+n \mid X>m)=P(X>n) \qquad \text{read aloud: ``given you've waited past } m\text{, the extra wait behaves like a fresh wait of length } n\text{.''}$$

The bar $\mid$ reads "given." The left side conditions on $m$ already-failed trials; the right side is a brand-new wait of length $n$ — and they are equal.

**Beat 6 — Derive it from the survival function.** Use the conditional-probability definition and the clean survival form $P(X>k)=q^k$ from Concept 1:

$$P(X>m+n \mid X>m)=\frac{P(X>m+n \ \text{and}\ X>m)}{P(X>m)}=\frac{P(X>m+n)}{P(X>m)}=\frac{q^{m+n}}{q^{m}}=q^{n}=P(X>n).$$

(The event $\{X>m+n\}$ already implies $\{X>m\}$, so their intersection is just $\{X>m+n\}$.) The exponents *subtract* and the $q^m$ cancels — the algebraic fingerprint of "the past evaporates." For our numbers, $P(X>8\mid X>3)=q^{8}/q^{3}=q^{5}=0.4437=P(X>5)$. ✓

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $P(X>8\mid X>3)=P(X>5)=q^5=0.4437$.
- *Twist (different anchor):* $P(X>10\mid X>7)=P(X>3)=q^3=0.6141$ — only the *gap* $n=3$ matters, never the anchor $m=7$.
- *General:* for any $m$, $P(X>m+n\mid X>m)=q^n$, independent of $m$.
- *Edge (the converse):* memorylessness *characterizes* the geometric — it is the unique discrete law with it (its continuous twin, the exponential, is the unique continuous one; ch11).

**Beat 8 — Picture it.** Draw the survival of a fresh wait, and the survival of the *remaining* wait given $m=3$ failures. They are the *same* shape — re-anchored, the future is a perfect copy of a cold start.

<figure>
<img src="../../assets/diagrams/ch05_memoryless.png" alt="Two side-by-side bar charts of survival probability versus extra trials n. Left ('Fresh start'): bars q^n = 1, 0.85, 0.72, 0.61, ... for n=0..8. Right ('Already failed m=3'): the survival of the remaining wait given three prior failures, with identical bar heights q^n. A banner beneath shows the algebra P(X>m+n | X>m) = q^(m+n)/q^m = q^n = P(X>n), concluding the two charts are identical: the past evaporates." style="width:88%; max-width:720px; display:block; margin:1em auto;">
<figcaption>Memorylessness made visual: the survival of the <em>remaining</em> wait after $m=3$ failures (right) is identical to a brand-new wait (left). Conditioning on past failures resets the clock — the gambler's "I'm due" is an illusion.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now compute conditional waits in one line ($q^n$, anchor-free), and you will never fall for "we're due" — the geometric's past is gone the instant it passes.

::: pokedex-entry
**POKÉDEX ENTRY №04 — Memorylessness**

For $X\sim\Geom(p)$:
$$P(X>m+n \mid X>m)=P(X>n)=q^{n}.$$

*In plain terms:* a geometric wait that has already failed $m$ times is as fresh as a new one — the past is forgotten. Only the *remaining* gap $n$ matters.

*Recognition cue:* **"given it hasn't happened yet," "already waited $m$ and want the chance of $n$ more."** Discard the past; answer $q^n$. The geometric is the **only** discrete law with this — "we're due" is the fallacy it forbids.
:::

## Concept 3 — The Negative Binomial: Waiting for the $r$-th Success (A.5.3)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Negative Binomial**

You win each round w.p. $0.4$ and stop at your $3$rd win. Let $X$ = losses before the $3$rd win. Find $E[X]$ and $P(X=2)$.

If you wrote **$E[X]=3(0.6)/0.4=4.5$** and **$P(X=2)=\binom{4}{2}(0.4)^3(0.6)^2=0.1382$** (and can say why it's $\binom{4}{2}$, not $\binom{5}{2}$), **skip to Concept 4**. Otherwise read on — the locked last trial is the whole subtlety.
:::

**Beat 1 — The one-sentence idea (advance organizer).** *The negative binomial is the geometric run $r$ times: wait not for one success but for the $r$-th.*

**Beat 2 — Anchor + concrete instance.** To unlock Erika's inner garden you must win $r=3$ petal-tokens at the Game Corner; each round wins w.p. $p=0.4$, independently. Let $X$ = losing rounds before your $3$rd win. *What is $P(X=2)$* — exactly $2$ losses, so the $3$rd win lands on round $5$?

**Beat 3 — Reason through the concrete case in plain words.** Round $5$ **must** be a win — it's the *clinching* third one, by definition of "stop at the $3$rd win." So the first $4$ rounds contain exactly $2$ wins and $2$ losses *in any order*, and round $5$ is the locked win. The probability of any one such pattern ($3$ wins, $2$ losses) is $(0.4)^3(0.6)^2$; we then count how many patterns put the $3$rd win exactly on round $5$. There are $\binom{4}{2}=6$ ways to place the $2$ early losses among the first $4$ rounds, so

$$P(X=2)=\underbrace{\binom{4}{2}}_{\text{arrange first 4}}\underbrace{(0.4)^3}_{\text{3 wins}}\underbrace{(0.6)^2}_{\text{2 losses}}=6(0.064)(0.36)=0.1382.$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is writing $\binom{5}{2}$, as if all five rounds were free to permute:

$$P(X=2)\overset{?}{=}\binom{5}{2}(0.4)^3(0.6)^2. \qquad\textbf{(wrong — frees the clinching trial)}$$

That would count arrangements like LLWWW, where the third win lands on round $3$ and rounds $4$–$5$ are surplus — but then you'd have *stopped already* at round $3$. **The defining $r$-th success is nailed to the last trial;** only the *earlier* trials are arrangeable. Free that last trial and you over-count by exactly the patterns that finish too soon.

**Beat 5 — Translate into notation, one glyph at a time.** Turn the concrete count into the general coefficient. With $X=k$ failures before the $r$-th success, the clinching success sits on the **last** trial, so the total number of trials is $k+r$. The last one is fixed as a success; the **earlier $k+r-1$ trials** must contain exactly the $k$ failures (the other $r-1$ being early successes). The number of ways to place those $k$ failures among the $k+r-1$ early slots is

$$\binom{k+r-1}{k} \qquad \text{read aloud: ``}(k+r-1)\text{ choose }k\text{'' — arrange }k\text{ failures among the trials before the last.''}$$

Check it against the concrete case: $k=2,\ r=3$ gives $\binom{2+3-1}{2}=\binom{4}{2}=6$ ✓ — the same count, now read off the rule. The pmf assembles as **arrangements × successes × failures**:

$$X\sim\NegBin(r,p), \qquad p(k)=\binom{k+r-1}{k}\,p^{r}\,q^{k}, \quad k=0,1,2,\dots$$

**Beat 6 — Generalize: derive the mean and variance.** Here is *why* you may simply scale the geometric. To collect $r$ successes, run the trials in $r$ stages: wait for the $1$st success (a geometric wait), then **restart fresh** and wait for the next, $r$ times. **Memorylessness** (Concept 2) guarantees each restart is a brand-new geometric, independent of the ones before. So if $Y_1,\dots,Y_r$ are the failure-counts in the $r$ stages — each $Y_i\sim\Geom(p)$ failures-version with $E[Y_i]=q/p$ and $\Var(Y_i)=q/p^2$ — then $X=Y_1+\cdots+Y_r$. Expectation is **linear** and, because the stages are **independent**, variances **add** (the same two moves as the binomial in Pewter):

$$E[X]=\sum_{i=1}^{r}E[Y_i]=r\cdot\frac{q}{p}=\frac{rq}{p}, \qquad \Var(X)=\sum_{i=1}^{r}\Var(Y_i)=r\cdot\frac{q}{p^{2}}=\frac{rq}{p^{2}}.$$

For our numbers $E[X]=3(0.6)/0.4=4.5$. ✓ ($r=1$ recovers the geometric, failures version — one stage.)

**Beat 7 — Ramp the difficulty.**

- *Simplest:* exactly $2$ losses before the $3$rd win, $P(X=2)=\binom{4}{2}p^3q^2=0.1382$.
- *Twist (trials convention):* if $T$ counts the **total trials** to the $r$-th success, then $T=X+r$ and $p(t)=\binom{t-1}{r-1}p^rq^{t-r}$ — the clinching win on trial $t$, the $r-1$ earlier wins among the first $t-1$ trials.
- *General:* mean $rq/p$, variance $rq/p^2$ — both exactly $r$ times the geometric.
- *Edge:* $r=1$ collapses every formula to the geometric — $\binom{k}{k}=1$, $p(k)=pq^k$, $E[X]=q/p$.

**Beat 8 — Picture it.** Unlike the geometric's pure decay (tallest at $k=0$), the negative-binomial pmf **rises off $k=0$** — you almost never collect $r$ successes with *zero* losses — peaks, then decays with a geometric-like tail.

<figure>
<img src="../../assets/diagrams/ch05_negbin.png" alt="A bar chart of the Negative Binomial(r=3, p=0.4) probability mass function in the failures convention. Bars rise from k=0 (height 0.064), climb to a broad peak near k=2 and k=3 (each about 0.138), then decay with a long right tail. The k=2 bar is highlighted red to match the worked value 0.1382, and a blue dashed vertical line marks the mean rq/p=4.5. A small Dugtrio sprite (three heads, evoking wait-for-the-3rd) sits in the right margin clear of the bars." style="width:80%; max-width:600px; display:block; margin:1em auto;">
<figcaption>$\NegBin(3,0.4)$ (failures convention): the loss count rises off $k=0$, peaks, then decays. The highlighted $k=2$ bar is $\binom{4}{2}(0.4)^3(0.6)^2=0.1382$; the dashed line marks the mean $rq/p=4.5$. (Dugtrio's three heads — wait for the third — look on from the margin.)</figcaption>
</figure>

**Beat 9 — Consolidate.** Whenever you **wait for the $r$-th success**, it is negative binomial: pmf $\binom{k+r-1}{k}p^rq^k$ (failures) with the $r$-th success locked in the last trial, mean $rq/p$, variance $rq/p^2$ — exactly $r$ independent geometrics summed.

::: pokedex-entry
**POKÉDEX ENTRY №05 — The Negative Binomial Distribution**

Run Bernoulli($p$) trials until the **$r$-th** success. With $X$ = failures before the $r$-th success, $X\in\{0,1,2,\dots\}$:
$$p(k)=\binom{k+r-1}{k}p^{r}q^{k}, \qquad E[X]=\frac{rq}{p}, \qquad \Var(X)=\frac{rq}{p^{2}}.$$

*In plain terms:* the geometric, $r$ times over — sum of $r$ independent geometrics. The $r$-th success is **locked in the last trial**; only the earlier ones permute.

*Recognition cue:* **"until the $r$-th success," "how many attempts to collect $r$ of them."** ($r=1$ is the geometric, failures version.) Use $\binom{k+r-1}{k}$, never $\binom{k+r}{k}$.
:::

## Concept 4 — The Poisson: Counts Over a Window (the Crown of the Chapter) (A.5.4)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Poisson**

Gastly appear at an average of $3$ per minute. Find $P(\ge2\text{ in one minute})$ and $P(<10\text{ over five minutes})$.

If you wrote **$1-4e^{-3}=0.8009$** and **$P(Y\le9)$ with $\lambda=15$ ($=0.0699$)** — rescaling $\lambda$ to the five-minute window — **skip to Concept 5**. If you used $\lambda=3$ for the five-minute count, read on: rescaling is the single most-punished Poisson error.
:::

**Beat 1 — The one-sentence idea.** *The Poisson counts random events over a window of time or space when they arrive at a steady average rate with no upper limit.*

**Beat 2 — Anchor + concrete instance.** Unlike every family so far, the Poisson has **no fixed number of trials** — the count of Gastly per minute could be $0$, $3$, or $20$; there is no ceiling. The caretaker's log gives a stable rate $\lambda=3$ per minute. Let $X$ = Gastly in one minute. *What is $P(X\ge2)$, and over five minutes, $P(\text{fewer than }10)$?*

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/front/92.png" alt="Gastly, the Gas Pokemon, whose per-minute appearances in the Pokemon Tower follow a Poisson count" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#092 Gastly</strong> — appearances per minute: a Poisson count.</figcaption>
</figure>

**Beat 3 — Reason in plain words, and where the formula comes from.** Slice the minute into a *huge* number $n$ of tiny instants, each with a *tiny* chance $p$ of a Gastly winking in, so that $np=\lambda=3$. The total count is then $\Binom(n,p)$. As we slice finer ($n\to\infty,\ p\to0$, product fixed at $\lambda$), the binomial pmf converges to

$$p(k)=\frac{e^{-\lambda}\lambda^{k}}{k!}.$$

So the Poisson is the **binomial in the limit of many rare trials** — its birth, and the source of the famous approximation. The mean and variance both inherit $\lambda$: from $\Binom(n,p)$, mean $np\to\lambda$ and variance $np(1-p)\to\lambda$ (since $p\to0$). **Mean equals variance — the Poisson's fingerprint.** And the masses sum to $1$ exactly because of Concept 0b: $\sum_k\frac{e^{-\lambda}\lambda^k}{k!}=e^{-\lambda}e^{\lambda}=1$.

**Beat 4 — Surface and dismantle the tempting wrong idea (rescaling).** For *five* minutes the deadliest slip is to reuse $\lambda=3$:

$$P(Y<10)\overset{?}{=}\sum_{k=0}^{9}\frac{e^{-3}3^k}{k!}. \qquad\textbf{(wrong — that's the ONE-minute rate)}$$

The rate is **per minute**; over five minutes you expect $5\times3=15$ Gastly, so $\lambda$ for the window is $15$, not $3$. **Always scale $\lambda=\text{rate}\times\text{window}$.** A "lull" of fewer than $10$ in a window that averages $15$ should be *uncommon* — and indeed it is, about $7\%$. Using $\lambda=3$ would wrongly call it nearly certain.

**Beat 5 — Translate into notation, one glyph at a time.**

$$X\sim\Poisson(\lambda), \qquad p(k)=\frac{e^{-\lambda}\lambda^{k}}{k!}, \quad k=0,1,2,\dots$$

Read aloud: *"$e$-to-the-minus-lambda, times lambda-to-the-$k$, over $k$-factorial."* The $k!$ denominator is what makes the masses sum to $1$ (it is the Taylor series of $e^{\lambda}$ in disguise — Concept 0b).

**Beat 6 — Compute both targets, and derive the mean.** *Mean.* By definition and the $e^x$ series:

$$E[X]=\sum_{k=0}^{\infty}k\,\frac{e^{-\lambda}\lambda^{k}}{k!}=\sum_{k=1}^{\infty}\frac{e^{-\lambda}\lambda^{k}}{(k-1)!}=\lambda e^{-\lambda}\sum_{j=0}^{\infty}\frac{\lambda^{j}}{j!}=\lambda e^{-\lambda}e^{\lambda}=\lambda.$$

(The $k=0$ term vanishes; cancel one $\lambda$ and one factor of $k$; reindex $j=k-1$; the leftover sum is $e^\lambda$.) So the mean is $\lambda$ — derived straight from Concept 0b. Now the targets. One minute, $\lambda=3$, complement the small end:

$$P(X\ge2)=1-p(0)-p(1)=1-e^{-3}-3e^{-3}=1-4e^{-3}=1-4(0.04979)=0.8009.$$

Five minutes, $\lambda=15$:

$$P(Y<10)=P(Y\le9)=\sum_{k=0}^{9}\frac{e^{-15}15^{k}}{k!}=0.0699.$$

**Beat 7 — Ramp the difficulty — the two power-tools (the second is Concept 5).**

- *Approximation:* $\Binom(n,p)\approx\Poisson(np)$ when $n$ is large and $p$ small. A slot pulled $40$ times at $p=0.05$ is $\approx\Poisson(2)$.
- *Additivity (superposition):* independent Poissons **add** — the full subject of Concept 5.
- *Edge (rescaling, again):* over $\tfrac12$ minute the rate halves to $\lambda=1.5$; over an hour it is $\lambda=180$. The window scales $\lambda$ linearly — nothing else.

**Beat 8 — Picture it.** The pmf peaks near $\lambda$ and, unlike the binomial, has **no right edge**. Rescaling the window slides and broadens the hump.

<figure>
<img src="../../assets/diagrams/ch05_poisson_window.png" alt="Two side-by-side bar charts of Poisson probability mass functions. Left: lambda=3 (one minute), peaking near k=3 with a long thin right tail and a Gastly sprite in the upper-right margin. Right: lambda=15 (five minutes), a broad bell-like hump centered near 15, with the bars for k=0 through 9 shaded red to show P(Y<10) is a small left-tail area totaling 0.0699; a Haunter sprite sits in the right margin. Both charts have no upper bound on k, and a dashed line marks the mean lambda in each." style="width:84%; max-width:680px; display:block; margin:1em auto;">
<figcaption>Poisson counts have no upper limit, and $\lambda$ scales with the window. Left: $\lambda=3$ (one minute; Gastly). Right: $\lambda=5\times3=15$ (five minutes; Haunter joins); the shaded left tail $k\le9$ totals $0.0699$ — a genuine lull.</figcaption>
</figure>

**Beat 9 — Consolidate.** Whenever events arrive at a **steady rate over a window with no cap**, it is Poisson: pmf $e^{-\lambda}\lambda^k/k!$, mean $=$ variance $=\lambda$, **rescale $\lambda$ to the window**, and lean on the binomial limit and additivity.

::: pokedex-entry
**POKÉDEX ENTRY №06 — The Poisson Distribution**

$X\sim\Poisson(\lambda)$ counts events at a constant average rate over a fixed window, $X\in\{0,1,2,\dots\}$:
$$p(k)=\frac{e^{-\lambda}\lambda^{k}}{k!}, \qquad E[X]=\Var(X)=\lambda, \qquad M_X(t)=e^{\lambda(e^{t}-1)}.$$

**Approximation:** $\Binom(n,p)\approx\Poisson(np)$ for large $n$, small $p$.

*In plain terms:* random events in a chunk of time/space with no ceiling. **Mean equals variance** — its signature. **Scale $\lambda=$ rate $\times$ window.**

*Recognition cue:* **"per minute / per year / per square mile," "average rate $\lambda$," a count with no natural maximum.**
:::

## Concept 5 — Sums of Independent Poissons: Superposition (A.5.5)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Poisson sums**

Gastly arrive at $\lambda_G=3$/min and Haunter at $\lambda_H=1$/min, independently. What is the distribution of *total* ghosts in one minute, and over two minutes?

If you wrote **total $\sim\Poisson(4)$ in one minute, $\Poisson(8)$ over two** (just add the rates, then rescale), **skip to the Worked Examples**. If you tried to convolve two pmfs by hand, read on — superposition makes it a one-liner.
:::

**Beat 1 — The one-sentence idea.** *Add two independent Poisson counts and you get one Poisson count whose rate is the sum of the rates.*

**Beat 2 — Anchor + concrete instance.** The Tower has two ghost streams: **Gastly** at $\lambda_G=3$/min and **Haunter** at $\lambda_H=1$/min, arriving independently. For the lull question you care about *total* ghosts, $T=G+H$. *What law does $T$ follow?*

**Beat 3 — Reason in plain words.** Each stream is a steady rain of rare events; merging two independent steady rains gives one steadier rain at the combined rate. There is no interaction — a Gastly arriving says nothing about a Haunter — so the total is *still* a steady, capless count, i.e. still Poisson, now at rate $\lambda_G+\lambda_H$. The mean of the total is the sum of the means (always true by linearity), and the *shape* stays Poisson (special to independent Poissons).

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two slips. First, **adding the wrong thing**: you add the *rates* $\lambda$, not the *probabilities*. $P(T=k)$ is **not** $P(G=k)+P(H=k)$ — that isn't even a valid pmf (it sums to $2$). The clean fact is about the *parameter*: $\lambda_T=\lambda_G+\lambda_H$. Second, **forgetting independence**: superposition needs the streams independent. If Gastly and Haunter arrivals were correlated, the sum need not be Poisson at all — only the mean would still add.

**Beat 5 — Translate into notation, one glyph at a time.** For independent $G\sim\Poisson(\lambda_G)$ and $H\sim\Poisson(\lambda_H)$:

$$G+H\sim\Poisson(\lambda_G+\lambda_H) \qquad \text{read aloud: ``the sum of two independent Poissons is Poisson, rates added.''}$$

This extends to any number of streams: $\sum_i\Poisson(\lambda_i)=\Poisson(\sum_i\lambda_i)$.

**Beat 6 — Derive it from the MGF.** The slickest proof uses the Poisson MGF $M(t)=e^{\lambda(e^t-1)}$ (Entry №06) and the rule that the MGF of a **sum of independent** RVs is the **product** of their MGFs:

$$M_{G+H}(t)=M_G(t)\,M_H(t)=e^{\lambda_G(e^{t}-1)}\,e^{\lambda_H(e^{t}-1)}=e^{(\lambda_G+\lambda_H)(e^{t}-1)}.$$

The last expression is *exactly* the MGF of a $\Poisson(\lambda_G+\lambda_H)$ — and because an MGF determines its distribution uniquely, the sum **is** that Poisson. For the Tower, $T\sim\Poisson(3+1)=\Poisson(4)$ per minute; over two minutes, rescale to $\Poisson(8)$.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $\Poisson(3)+\Poisson(1)=\Poisson(4)$ (one minute).
- *Twist (then rescale):* over $2$ minutes the total rate is $4\times2=8$, so $T_2\sim\Poisson(8)$ — superpose first, then scale the window (or scale each, then superpose; same answer).
- *General:* $k$ independent streams add to $\Poisson(\lambda_1+\cdots+\lambda_k)$.
- *Edge (the converse — thinning):* if a $\Poisson(\mu)$ stream is each independently *kept* w.p. $p$, the kept count is $\Poisson(\mu p)$ — superposition run backwards, used heavily in insurance (covered claims out of all claims).

**Beat 8 — Picture it.** Two input streams flow into one merged stream whose rate is their sum.

<figure>
<img src="../../assets/diagrams/ch05_poisson_sums.png" alt="A flow diagram. Two rounded boxes on the left are labeled 'Gastly stream, rate lambda=3/min' (with a Gastly sprite) and 'Haunter stream, rate lambda=1/min' (with a Haunter sprite). Two purple arrows merge into a yellow box on the right labeled 'Total ghosts: Pois(3+1)=Pois(4), rate lambda=4/min, mean = var = 4; over 2 min: Pois(8)'. A caption beneath gives the MGF proof: M(t) = e^{lambda1(e^t-1)} e^{lambda2(e^t-1)} = e^{(lambda1+lambda2)(e^t-1)}." style="width:82%; max-width:660px; display:block; margin:1em auto;">
<figcaption>Superposition: the independent Gastly ($\lambda=3$) and Haunter ($\lambda=1$) streams merge into one $\Poisson(4)$ stream — just sum the rates. The MGF product makes it exact.</figcaption>
</figure>

**Beat 9 — Consolidate.** Whenever independent Poisson counts are **added**, the result is Poisson with the rates summed — combine first, rescale the window if needed, and read off mean $=$ variance $=$ the total rate.

::: pokedex-entry
**POKÉDEX ENTRY №07 — Sums of Independent Poissons (Superposition)**

For independent $X_i\sim\Poisson(\lambda_i)$:
$$\sum_i X_i \sim \Poisson\!\Big(\sum_i \lambda_i\Big).$$

*In plain terms:* merge independent Poisson streams and you get one Poisson at the **sum of the rates**. Add the $\lambda$'s, not the probabilities; independence is required.

*Recognition cue:* **"total of several independent counts," "combined arrivals," "claims from two independent sources."** Converse (**thinning**): keeping each event w.p. $p$ gives $\Poisson(\lambda p)$.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:170px; text-align:center;">
<img src="../../assets/vs/erika.png" alt="Erika, the Celadon City Gym Leader" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Erika — Celadon Gym Leader, your distributions mentor</figcaption>
</figure>

Four examples, fading from fully narrated to exam speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because **family recognition** is the load-bearing skill of the whole univariate act.

### Worked Example 1 — The Ghost Lull (full narration; recognition-first)

**ARCHETYPE:** *Recognize and compute a Poisson over a rescaled window — the bread-and-butter A.5.4 item.*

**Setup.** Gastly appear in the Tower at a steady $\lambda=3$ per minute. (a) Find $P(X\ge2)$ in one minute. (b) Find $P(Y<10)$ over five minutes. (c) A Haunter stream at $1$/min joins, independently; find the distribution and mean of the total ghosts in one minute.

**Step 1 — Identify (what's the question really asking?).** "Steady average rate, count with no ceiling" $\Rightarrow$ **Poisson** (Entry №06). Part (b) changes the *window*, so $\lambda$ must rescale. Part (c) **adds independent Poissons** $\Rightarrow$ superposition (Entry №07).

**Step 2 — Professor's Path (the why).**
*(a)* Complement the small end — faster than summing a tail:
$$P(X\ge2)=1-p(0)-p(1)=1-e^{-3}-3e^{-3}=1-4e^{-3}=0.8009.$$
*(b)* Rescale: five minutes at $3$/min means $\lambda=15$. Then $P(Y<10)=P(Y\le9)=\sum_{k=0}^{9}\frac{e^{-15}15^k}{k!}=0.0699$.
*(c)* Add rates: total $\sim\Poisson(3+1)=\Poisson(4)$, mean $=4$.

**Step 3 — Trainer's Path (the fast how).** For (a), keep $e^{-3}=0.049787$ in memory and compute $1-4(0.049787)$ directly. For (b), a cumulative-Poisson is a calculator/table lookup at $\lambda=15,\ k=9$ — *the only trap is feeding it $\lambda=15$, not $3$.* For (c), no computation beyond $3+1=4$: superposition is a recognition win, not an arithmetic one.

**Step 4 — Check & pitfall.** $0.8009\in[0,1]$ ✓ and "$\ge2$ when you expect $3$" should indeed be likely ✓. The lull probability $0.0699$ is small, as a below-average window should be ✓. **Pitfalls:** using $\lambda=3$ for the five-minute count (the headline Poisson error); adding *probabilities* instead of *rates* in (c). *(Back-ref: Entries №02, №06, №07.)*

### Worked Example 2 — Pulls Until the First Win (partial guidance)

**ARCHETYPE:** *Geometric wait + a memoryless conditional.*

**Setup.** A Game Corner slot wins each pull w.p. $p=0.2$. (a) Find $P(\text{more than }4\text{ pulls to the first win})$. (b) You've already pulled $6$ times with no win; find the chance of *more than $4$ more* losing pulls. (c) Find the expected number of pulls to the first win.

**Identify.** "Wait for the first success" $\Rightarrow$ **geometric** (Entry №03); part (b) is a **memoryless** conditional (Entry №04).

**(a)** $P(X>4)=q^4=0.8^4=0.4096.$
**(b)** Memorylessness: the $6$ wasted pulls vanish, so $P(X>10\mid X>6)=P(X>4)=0.8^4=0.4096$ — *identical to (a).*
**(c)** $E[X]=1/p=1/0.2=5$ pulls (trials convention).

**Check & pitfall.** (a) and (b) match, the signature of memorylessness ✓; $E[X]=5$ is plausible for a one-in-five win ✓. **Pitfall:** the gambler's fallacy — thinking the $6$ cold pulls make a win "due" and shrink the remaining wait. They don't. *(Back-ref: Entries №01, №03, №04.)*

### Worked Example 3 — Tokens for Erika's Garden (light guidance)

**ARCHETYPE:** *Negative binomial — exactly $k$ losses before the $r$-th win.*

**Setup.** Each Game Corner round wins a petal-token w.p. $p=0.4$; you need $r=3$ to enter Erika's inner garden. (a) Find $P(\text{exactly }2\text{ losses before the 3rd win})$. (b) Find the expected number of losses.

This is "wait for the $r$-th success" $\Rightarrow$ **negative binomial**, failures version (Entry №05), with the $3$rd win locked on the last trial.

**(a)** $P(X=2)=\binom{2+3-1}{2}p^3q^2=\binom{4}{2}(0.4)^3(0.6)^2=6(0.064)(0.36)=0.1382.$
**(b)** $E[X]=\dfrac{rq}{p}=\dfrac{3(0.6)}{0.4}=4.5$ losses.

**Check & pitfall.** $\binom{4}{2}=6$ uses $k+r-1=4$ early slots, not $5$ ✓; mean $4.5=3\times1.5$, three geometrics each averaging $q/p=1.5$ losses ✓. **Pitfall:** writing $\binom{5}{2}$ (freeing the clinching trial) — it over-counts patterns that finish too soon. *(Back-ref: Entry №05.)*

### Worked Example 4 — Two Streams, One Count (exam speed)

**ARCHETYPE:** *Superposition + rescaling — recognize, don't compute.*

<figure style="margin:1.25em auto; max-width:300px; text-align:center;">
<div style="display:flex; gap:18px; flex-wrap:wrap; justify-content:center; align-items:flex-end;">
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/92.png" alt="Gastly" style="width:90px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">#092 Gastly — $\lambda=2$/min</figcaption>
</figure>
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/93.png" alt="Haunter" style="width:90px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">#093 Haunter — $\lambda=1.5$/min</figcaption>
</figure>
</div>
</figure>

**Setup.** Gastly arrive at $2$/min and Haunter at $1.5$/min, independently. Find the distribution of total ghosts over a $4$-minute climb, and its mean and variance.

Superpose first (Entry №07): per minute, total $\sim\Poisson(2+1.5)=\Poisson(3.5)$. Rescale to $4$ minutes: $\lambda=3.5\times4=14$, so total $\sim\Poisson(14)$. For a Poisson, mean $=$ variance $=\lambda=14$.

**Check & pitfall.** Same answer if you rescale each stream first ($\Poisson(8)+\Poisson(6)=\Poisson(14)$) ✓. **Pitfall:** adding the per-minute rates but forgetting to multiply by the $4$-minute window. *(Back-ref: Entries №06, №07.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — Route the story to the family in under a minute**

Read the verb in the problem, not the nouns. **"Out of $n$ trials, count successes"** $\to$ binomial (Pewter). **"Until the first…"** $\to$ geometric. **"Until the $r$-th…"** $\to$ negative binomial. **"Per minute / per year, no ceiling"** $\to$ Poisson. **"Total of independent counts"** $\to$ add Poisson rates. Naming the family *first* turns every problem into "plug the card," and the card is the Pokédex Entry you carry in your head.
:::

::: trainers-tip
**TRAINER'S TIP — Always rescale $\lambda$ to the window**

The Poisson rate is *per unit*. The instant the problem changes the window — five minutes instead of one, a year instead of a month — set $\lambda=\text{rate}\times\text{window}$ *before* you touch the pmf. This single slip (reusing the per-unit rate) is the most-punished Poisson error on the exam. Write the new $\lambda$ down explicitly.
:::

::: trainers-tip
**TRAINER'S TIP — Memoryless conditionals: throw the past away**

If a geometric (or exponential, ch11) problem says "given it hasn't happened in the first $m$ trials, find the chance of $n$ more," do **not** carry the $m$. The answer is $q^n$ (or $e^{-\lambda n}$), depending only on the *gap* $n$. Spotting "given it hasn't happened yet" should trigger an instant "discard $m$" reflex — and immunize you against "we're due."
:::

::: trainers-tip
**TRAINER'S TIP — Tail probabilities by complement**

For "$\ge$" or "more than" with a small threshold, complement from the bottom: $P(X\ge2)=1-p(0)-p(1)$ beats summing an infinite tail. For the geometric, the survival is already closed-form ($q^m$), so use it directly rather than summing the pmf.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

<figure style="margin:1em auto; max-width:150px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket — Jessie, James, and Meowth" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
</figure>

At the Celadon Game Corner, Meowth is hunched over a slot machine that wins each pull with probability $p=0.2$. He has pulled it **nine times** with nothing.

"Nine losses in a row!" Meowth crows, rubbing his paws. "Da machine's *cold* — which means a win is way overdue. Da odds it pays on da *next* pull gotta be huge now. We're **due**, Jessie!"

Jessie shoves more coins in. "Empty the bag, James — we can't lose, the math says so."

James hesitates. "But… each pull is its own thing, isn't it? The machine doesn't *know* we've lost nine times…"

Meowth waves a paw. "Bah! Nine losses means a win's gotta come! Everybody knows dat!" — and bets the team's entire stash on the tenth pull.

**Where it fails:** the slot is a **geometric** (memoryless) wait. The nine cold pulls are spent and gone; they change *nothing* about the next pull, which still wins with probability exactly $p=0.2$ — same as the very first. Formally, $P(\text{win on pull }10\mid 9\text{ losses})=P(\text{win on pull }1)=0.2$, because $P(X>9{+}1\mid X>9)=P(X>1)=q$, independent of the nine. Meowth has committed the **gambler's fallacy** — reading a memoryless process as if losses "build up" toward a win. The machine has no memory; "we're due" is the exact reasoning the geometric forbids. The fix is one line: *for a memoryless wait, the past never changes the future — the next trial is always a fresh $p$.* (You'll catch Meowth red-handed in Problems C5.8 and C5.16.)
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

This is the literal arithmetic of **claim frequency** — how often losses happen.

An insurer cannot predict whether *you* will file a claim next year, but across a large book the **number of claims** in a period is the textbook **Poisson** count: many independent policyholders, each with a tiny per-instant chance of a loss, summing to a steady average rate $\lambda$. Pricing starts here — the *pure premium* is (expected claim **count**) $\times$ (expected cost **per** claim), and the count is Poisson. **Rescaling $\lambda$ to the window** is exactly how an actuary converts a monthly claim rate to an annual one. **Superposition** is how you combine independent risks: merge the auto and home claim streams of one household, or pool two independent regions, and the total is again Poisson at the summed rate — and its converse, **thinning**, splits a claim stream into "large" vs. "small" claims, each still Poisson. The **geometric/negative binomial** model *waiting*: rounds until a policy first lapses, or the number of failed quotes before the $r$-th sale — and **memorylessness** is the formal statement that a constant-hazard process has no "aging," the assumption (and its failure) at the heart of mortality and reliability models.

*Series bridge:* the **geometric series** and the **$e^x$ series** you sharpened here return constantly — the $e^x$ identity is the engine behind the Poisson, the exponential (ch11), and the gamma; the geometric series underlies every "sum of a memoryless tail." And $\Poisson(\lambda)$ claim counts feed directly into **aggregate loss models** and **compound distributions** on the later CAS/SOA exams (STAM, MAS-I), where the count and the severity are combined.

*Transfer check:* could you solve this with no Pokémon in it? "Calls arrive at a help line at $3$ per minute (Poisson); find the chance of fewer than $10$ in five minutes." Same $\lambda=15$, same $0.0699$. If you can do that, the skill has transferred.
:::

## The Gym Battle — Rainbow Badge Capstone

<figure style="margin:1.5em auto; max-width:170px; text-align:center;">
<img src="../../assets/vs/erika.png" alt="Erika, the Celadon Gym Leader, surrounded by Grass-type Pokemon" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Erika — Celadon Gym Leader, keeper of the Rainbow Badge</figcaption>
</figure>

**Erika's Challenge.** In the perfumed gym, Erika lowers her fan. "Two named laws govern my garden, Trainer. First, the *thinning* of a swarm. Show me you understand it, and the **Rainbow Badge** is yours."

> Pollen-spores drift through my greenhouse at a steady **$\lambda=10$ per minute** (Poisson). Each spore is, independently, a **rare perfume-grade** spore with probability **$p=0.2$** (the rest are common). (a) What is the distribution of the *number of perfume-grade spores* in one minute, and its mean? (b) Over a **three-minute** bloom, find the probability of **at least one** perfume-grade spore. (c) My Gloom only blooms on the *first* minute that contains a perfume-grade spore; treating minutes as independent, find the expected number of minutes I wait for that first qualifying minute.

<figure style="margin:1.25em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/44.png" alt="Gloom, Erika's Grass-and-Poison-type Pokemon" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">#044 Gloom — blooms on the first perfume-grade minute</figcaption>
</figure>

**ARCHETYPE:** *Poisson thinning + window rescaling + a geometric wait, chained — the integrative A.5 capstone.*

**Step 1 — Identify.** (a) "Keep each event of a Poisson stream w.p. $p$" $\Rightarrow$ **thinning** (Entry №07 converse): the kept count is Poisson at rate $\lambda p$. (b) "At least one over a window" $\Rightarrow$ rescale $\lambda p$ to three minutes, then complement. (c) "Minutes until the first qualifying minute" $\Rightarrow$ **geometric** wait over minutes (Entry №03), where a minute "succeeds" if it has $\ge1$ perfume-grade spore.

**Step 2 — Solve (a): thinning.** Thin the $\Poisson(10)$ spore stream by $p=0.2$:

$$\text{perfume-grade per minute}\sim\Poisson(\lambda p)=\Poisson(10\times0.2)=\Poisson(2), \qquad \text{mean}=2.$$

**Step 3 — Solve (b): rescale, then complement.** Over three minutes the perfume-grade rate is $\lambda'=2\times3=6$. "At least one" is the complement of "none":

$$P(\ge1\text{ in 3 min})=1-P(0)=1-e^{-6}=1-0.002479=0.9975.$$

**Step 4 — Solve (c): a geometric over minutes.** A single minute is a "success" (has $\ge1$ perfume-grade spore) with probability

$$p_{\min}=P(\ge1\text{ in 1 min})=1-e^{-2}=1-0.13534=0.86466.$$

The number of minutes until the first such minute is $\Geom(p_{\min})$ (trials convention), so the expected wait is

$$E[\text{minutes}]=\frac{1}{p_{\min}}=\frac{1}{0.86466}=1.1565\ \text{minutes}.$$

**Step 5 — Check, verdict & the pitfalls Erika is testing.** (a) Mean $2=10\times0.2$ ✓ and the kept stream is still capless/Poisson — thinning *preserves* the family. (b) $0.9975$ is near-certain, as a three-minute window averaging $6$ should be ✓. (c) $1.156$ minutes is just over one, sensible since most single minutes already qualify ($p_{\min}\approx0.865$) ✓. **Pitfalls Erika probes:** forgetting to thin (using $\lambda=10$ for perfume-grade); forgetting to rescale to three minutes in (b); and the chained recognition in (c) — that a *minute* is itself a Bernoulli trial whose success probability comes from a Poisson, feeding a geometric.

> Erika folds her fan with a small smile. "You thinned the swarm, scaled the window, and waited for the bloom — three laws, one chain, no slips. The **Rainbow Badge** is yours, Trainer." Gloom releases a contented cloud of spores.

*(If instead Erika asked for the wait until the **third** qualifying minute, the geometric becomes a* negative binomial *with $r=3$ and the same $p_{\min}$ — mean $r/p_{\min}\approx3.47$ minutes. The waiting-game family flexes with how many successes you need — see Problem C5.21.)*

## The Gym Challenge — Problem Set

::: problem-set
**THE POKÉMON TOWER & THE CELADON GAME CORNER — your questline.** Erika has set you a single escalating mission: first the **Route Trainer** legs (counting ghosts on the climb and warming up your waiting-game tools), then the **Gym Battle** tier (the boss fight — full Poisson/geometric/negative-binomial problems at exam difficulty), then the optional **Elite Challenge** post-game. Work it timed (~3–6 min/problem), then check the **Answers** below. Hit the mastery bar (**80%+ with the right family named**) to clear the questline and claim the Rainbow Badge. Problems are listed first; full worked solutions follow afterward. Markers: 🔴 routine method · 🟡 routine-with-a-twist · 🔵 stretch.

Several Tower problems share the ghost rate $\lambda=3$ Gastly/min (Poisson); several Game Corner problems share a slot that wins w.p. $0.2$ per pull (geometric). Each problem restates whatever it needs, so you can work them in any order.

### Route Trainers (the early legs — counting ghosts, warming up)

**C5.1.** 🔴 *(Sum the caretaker's failing-streak tail.)* Evaluate $\sum_{k=0}^{\infty}(0.7)^k$ and state the convergence condition.

**C5.2.** 🔴 *(The $e^x$ identity behind the ghost count.)* Use the Taylor series to evaluate $\sum_{k=0}^{\infty}\dfrac{2^k}{k!}$.

**C5.3.** 🔴 *(How long until the first ghost?)* A ghost manifests on each pass w.p. $0.15$. Find $P(\text{more than }5\text{ passes})$ to the first ghost.

**C5.4.** 🟡 *(The first-ghost mean.)* For that wait ($p=0.15$, trials convention), find $E[X]$ and $\Var(X)$.

**C5.5.** 🔴 *(Ghosts in a minute.)* Gastly appear at $\lambda=3$/min (Poisson). Find $P(X=2)$ in one minute.

**C5.6.** 🟡 *(Rescale to the window.)* For the same Gastly stream, find the expected number and the variance of Gastly over a $4$-minute climb.

**C5.7.** 🔴 *(Exactly two losses before the third token.)* Each Game Corner round wins w.p. $0.4$; you wait for the $3$rd win. Find $P(\text{exactly }2\text{ losses before the 3rd win})$.

**C5.26.** 🔴 *(DECISION — sum two streams or scale one?)* Gastly arrive at $2$/min and Haunter at $1$/min, independently. To get the *total* per minute, do you add the rates or the probabilities? Give the distribution of the total and its mean, and name the principle.

> *Questline beat: the ghosts are counted and your waiting tools are warm. Erika is waiting at the perfumed gym. The boss fights begin.*

### Gym Battles (the boss fight — true SOA difficulty)

**C5.8.** 🟡 *(AUDIT — Team Rocket's "we're due.")* A slot wins w.p. $0.2$ per pull (geometric). After **9** straight losses, Meowth claims "a win on the next pull is now overdue — way more than $20\%$." Find the true $P(\text{win on pull }10\mid 9\text{ losses})$ and name his error.

**C5.9.** 🟡 *(At least two ghosts, by complement.)* Gastly at $\lambda=3$/min. Find $P(X\ge2)$ in one minute.

**C5.10.** 🔵 *(The five-minute lull.)* Gastly at $3$/min. Find $P(Y<10)$ over five minutes — and state the $\lambda$ you used.

**C5.11.** 🟡 *(Superposition.)* Gastly at $3$/min and Haunter at $1$/min, independently. Find the distribution of total ghosts over a **two-minute** stretch and its mean.

**C5.12.** 🟡 *(Memoryless conditional.)* A slot wins w.p. $0.2$. Given you have pulled $6$ times with no win, find $P(\text{more than }4\text{ further losing pulls})$.

**C5.13.** 🔵 *(RIVAL TRAP — Gary's "binomial" wait.)* Gary models "the number of pulls until my first win" with a *binomial* coefficient, writing $P(\text{first win on pull }3)=\binom{3}{1}p\,q^2$. With $p=0.25$, find the correct $P(\text{first win on pull }3)$ and name Gary's error.

**C5.14.** 🟡 *(Thinning a swarm.)* Pollen drifts at $\lambda=10$/min (Poisson); each spore is perfume-grade w.p. $0.2$ independently. Find the distribution and mean of perfume-grade spores per minute.

**C5.15.** 🔵 *(Negative-binomial mean + a single pmf value.)* You wait for the $4$th win; each round wins w.p. $0.3$. Find $E[\text{losses before the 4th win}]$ and $P(\text{exactly }1\text{ loss before the 4th win})$.

**C5.16.** 🟡 *(AUDIT — the gambler's fallacy, again.)* A geometric wait has $p=0.1$. Jessie argues "after $20$ failures the chance of success within the next $5$ trials must be near certain." Find the true $P(\text{success within the next }5\mid 20\text{ failures})$ and name the error.

**C5.18.** 🔵 *(Binomial-to-Poisson limit.)* A slot pulled $n=50$ times wins each pull w.p. $p=0.04$. Approximate $P(\text{exactly }2\text{ wins})$ with a Poisson, and state the $\lambda$.

**C5.24.** 🟡 *(AUDIT — Poisson without rescaling.)* Gastly at $3$/min. Jessie computes $P(\text{fewer than }10\text{ over five minutes})$ using $\lambda=3$ and gets $\approx1$. Find the correct probability and name the error.

> *Questline beat: the Rainbow Badge is yours. The post-game below is optional — the integrative challenges where the league players sharpen up.*

### Elite Challenge (post-game — integrative / stretch)

**C5.19.** 🔵 *(Thinning + window + complement, chained.)* Pollen at $\lambda=10$/min; perfume-grade w.p. $0.2$. (a) Distribution of perfume-grade per minute. (b) Over **three** minutes, $P(\ge1\text{ perfume-grade})$.

**C5.20.** 🔵 *(Geometric mean derived from the series.)* For $X\sim\Geom(p)$ (failures version), derive $E[X]=q/p$ using $E[X]=\sum_{k\ge0}P(X>k)$ and the geometric series. Evaluate at $p=0.2$.

**C5.21.** 🔵 *(DECISION — first qualifying minute vs. third.)* A minute "qualifies" (has $\ge1$ perfume-grade spore) w.p. $p_{\min}=1-e^{-2}=0.8647$. (a) Expected minutes to the **first** qualifying minute. (b) Expected minutes to the **third**. Name the family in each and justify which model the question forces.

**C5.23.** 🔵 *(RIVAL TRAP — Gary adds Poisson probabilities.)* Gary has Gastly $\sim\Poisson(3)$ and Haunter $\sim\Poisson(1)$ independent, and computes $P(\text{total}=2)=P(G=2)+P(H=2)$. Explain why this is wrong, and give the correct distribution of the total and $P(\text{total}=2)$.

**C5.22.** 🔵 *(Wait for the 2nd Gastly captured.)* Each Gastly is captured w.p. $0.25$ per throw (independent throws); you hunt until the **2nd** capture. Find $P(\text{exactly }3\text{ escapes before the 2nd Gastly is captured})$.

**C5.25.** 🔵 *(DECISION — geometric or negative binomial?)* Each Game Corner round wins w.p. $0.4$; you wait for the **5th** win. Treating the count as losses before the 5th win, name the family, then find $E[\text{losses before the 5th win}]$ and $\Var(\text{losses})$.
:::

## Answers

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

### Quick-Answer Table

| # | Answer | Archetype | | # | Answer | Archetype |
|---|---|---|---|---|---|---|
| C5.1 | $\tfrac{1}{0.3}=3.333$ ($\lvert r\rvert<1$) | standard | | C5.13 | $0.1406$; geometric not binomial | rival_trap |
| C5.2 | $e^2=7.389$ | standard | | C5.14 | $\Poisson(2)$, mean $2$ | standard |
| C5.3 | $0.85^5=0.4437$ | standard | | C5.15 | $E=9.33$; $P(X{=}1)=0.0227$ | standard |
| C5.4 | $E=6.667$, $\Var=37.78$ | standard | | C5.16 | $1-0.9^5=0.4095$ (not $\approx1$) | audit |
| C5.5 | $0.2240$ | standard | | C5.18 | $\Poisson(2)$, $P(2)=0.2707$ | standard |
| C5.6 | mean $12$, var $12$ | standard | | C5.24 | $0.0699$ (not $\approx1$) | audit |
| C5.7 | $0.1382$ | standard | | C5.19 | $\Poisson(2)$; $1-e^{-6}=0.9975$ | standard |
| C5.8 | $0.2$ (memoryless) | audit | | C5.20 | $q/p$; $4.0$ | standard |
| C5.9 | $1-4e^{-3}=0.8009$ | standard | | C5.21 | (a) $1.156$ geom; (b) $3.47$ negbin | decision |
| C5.10 | $0.0699$, $\lambda=15$ | standard | | C5.23 | $\Poisson(4)$, $P(2)=0.1465$ | rival_trap |
| C5.11 | $\Poisson(8)$, mean $8$ | standard | | C5.26 | add rates: $\Poisson(3)$, mean $3$ | decision |
| C5.12 | $0.8^4=0.4096$ | standard | | C5.22 | $0.1055$ | standard |
| | | | | C5.25 | negbin: $E=7.5$, $\Var=18.75$ | decision |

**C5.1** — *(standard) Geometric series (Entry №01).* $\sum_{k\ge0}(0.7)^k=\frac{1}{1-0.7}=\frac{1}{0.3}=3.333$. Valid because $|r|=0.7<1$; for $|r|\ge1$ it diverges.

**C5.2** — *(standard) Taylor series for $e^x$ (Entry №02).* $\sum_{k\ge0}\frac{2^k}{k!}=e^{2}=7.389$ (set $x=2$).

**C5.3** — *(standard) Geometric survival (Entry №03).* $P(X>5)=q^5=0.85^5=0.4437$ — all five passes fail.

**C5.4** — *(standard) Geometric mean/variance (Entry №03).* $E[X]=1/p=1/0.15=6.667$; $\Var(X)=q/p^2=0.85/0.0225=37.78$.

**C5.5** — *(standard) Poisson pmf (Entry №06).* $P(X=2)=\frac{e^{-3}3^2}{2!}=\frac{9}{2}e^{-3}=4.5(0.049787)=0.2240$.

**C5.6** — *(standard) Poisson rescaling (Entry №06).* Over $4$ min, $\lambda=3\times4=12$. For a Poisson, mean $=$ variance $=\lambda=12$.

**C5.7** — *(standard) Negative binomial pmf (Entry №05).* $P(X=2)=\binom{4}{2}(0.4)^3(0.6)^2=6(0.064)(0.36)=0.1382$.

**C5.8** — *(audit) Gambler's fallacy / memorylessness (Entry №04).* The slot is geometric (memoryless): $P(\text{win on pull }10\mid 9\text{ losses})=P(\text{win on pull }1)=p=0.2$. **Meowth's error:** he treated past losses as "building up" to a win — the gambler's fallacy. A memoryless wait has no memory; the next pull is always a fresh $p=0.2$, never "overdue."

**C5.9** — *(standard) Poisson tail by complement (Entry №06).* $P(X\ge2)=1-p(0)-p(1)=1-e^{-3}-3e^{-3}=1-4e^{-3}=1-4(0.049787)=0.8009$.

**C5.10** — *(standard) Poisson with rescaling (Entry №06).* Five minutes at $3$/min $\Rightarrow\lambda=15$. $P(Y<10)=P(Y\le9)=\sum_{k=0}^{9}\frac{e^{-15}15^k}{k!}=0.0699$. The window forces $\lambda=15$, not $3$.

**C5.11** — *(standard) Superposition + rescaling (Entry №07).* Per minute, total $\sim\Poisson(3+1)=\Poisson(4)$. Over two minutes, $\lambda=4\times2=8$, so total $\sim\Poisson(8)$, mean $8$.

**C5.12** — *(standard) Memoryless conditional (Entry №04).* $P(X>10\mid X>6)=P(X>4)=q^4=0.8^4=0.4096$ — the $6$ prior pulls are discarded.

**C5.13** — *(rival_trap) Geometric vs. binomial coefficient (Entry №03).* The wait for the first win is **geometric**, with the success locked last: $P(\text{first win on pull }3)=q^2p=(0.75)^2(0.25)=0.1406$. **Gary's error:** he attached a binomial coefficient $\binom{3}{1}$, as if the single win could land in any of the three slots — but for "the *first* win," its position is forced to be last, so there is exactly one arrangement (no coefficient).

**C5.14** — *(standard) Poisson thinning (Entry №07 converse).* Keeping each spore w.p. $0.2$: perfume-grade $\sim\Poisson(10\times0.2)=\Poisson(2)$, mean $2$. Thinning preserves the Poisson family.

**C5.15** — *(standard) Negative binomial (Entry №05).* With $r=4,\ p=0.3,\ q=0.7$: $E[\text{losses}]=rq/p=4(0.7)/0.3=9.333$. $P(X=1)=\binom{1+4-1}{1}p^4q^1=\binom{4}{1}(0.3)^4(0.7)=4(0.0081)(0.7)=0.02268$. *(Rounded $0.0227$.)*

**C5.16** — *(audit) Gambler's fallacy (Entry №04).* Memorylessness: $P(\text{success within next }5\mid 20\text{ failures})=P(X\le5\text{ from a fresh start})=1-q^5=1-0.9^5=1-0.59049=0.4095$. **Jessie's error:** the $20$ failures do not raise the future chance — the answer is the same $0.4095$ as from a cold start, nowhere near certain.

**C5.18** — *(standard) Binomial-to-Poisson limit (Entry №06).* $\lambda=np=50(0.04)=2$. $P(\text{exactly }2)\approx\frac{e^{-2}2^2}{2!}=2e^{-2}=2(0.135335)=0.2707$.

**C5.24** — *(audit) Poisson without rescaling (Entry №06).* Correct $\lambda=3\times5=15$, giving $P(Y<10)=0.0699$. **Jessie's error:** she used the per-minute $\lambda=3$ for a five-minute window; $\sum_{k=0}^{9}\frac{e^{-3}3^k}{k!}\approx0.9989\approx1$ wrongly calls a below-average lull near-certain. Always rescale $\lambda=$ rate $\times$ window.

**C5.19** — *(standard) Thinning + window + complement (Entries №06, №07).* (a) Perfume-grade per minute $\sim\Poisson(10\times0.2)=\Poisson(2)$. (b) Over $3$ min, $\lambda=2\times3=6$; $P(\ge1)=1-e^{-6}=1-0.002479=0.9975$.

**C5.20** — *(standard) Geometric mean from the series (Entries №01, №03).* Failures version: $P(X>k)=q^{k+1}$ (more than $k$ failures means $\ge k+1$ failures). $E[X]=\sum_{k\ge0}P(X>k)=\sum_{k\ge0}q^{k+1}=q\sum_{k\ge0}q^k=q\cdot\frac{1}{1-q}=\frac{q}{p}$. At $p=0.2$: $E[X]=0.8/0.2=4.0$.

**C5.21** — *(decision) Geometric vs. negative binomial (Entries №03, №05).* (a) "First qualifying minute" $\Rightarrow$ **geometric** over minutes: $E=1/p_{\min}=1/0.8647=1.156$ minutes. (b) "Third qualifying minute" $\Rightarrow$ **negative binomial** with $r=3$ (trials convention): $E=r/p_{\min}=3/0.8647=3.470$ minutes. The question's *number of required successes* forces the family — one success is geometric, $r$ is negative binomial.

**C5.23** — *(rival_trap) Poisson superposition, not probability addition (Entry №07).* Independent Poissons add their **rates**: total $\sim\Poisson(3+1)=\Poisson(4)$, so $P(\text{total}=2)=\frac{e^{-4}4^2}{2!}=8e^{-4}=8(0.018316)=0.1465$. **Gary's error:** $P(G=2)+P(H=2)$ adds *probabilities*, which is meaningless (it isn't even a valid pmf) — you add the parameters, not the masses.

**C5.22** — *(standard) Negative binomial pmf (Entry №05).* Failures version with $r=2,\ p=0.25,\ q=0.75$: $P(X=3)=\binom{3+2-1}{3}p^2q^3=\binom{4}{3}(0.25)^2(0.75)^3=4(0.0625)(0.421875)=0.1055$. The clinching $2$nd capture is locked in the last throw; among the first four throws the single earlier capture can sit in any of $\binom{4}{3}=4$ positions, so there is no coefficient beyond $\binom{k+r-1}{k}$.

**C5.25** — *(decision) Negative binomial mean and variance (Entry №05).* Five required wins $\Rightarrow$ **negative binomial** (the geometric is just the $r=1$ special case). With $r=5,\ p=0.4,\ q=0.6$: $E[\text{losses}]=rq/p=5(0.6)/0.4=7.5$; $\Var(\text{losses})=rq/p^2=5(0.6)/0.16=18.75$.

**C5.26** — *(decision) Superposition principle (Entry №07).* Add the **rates**, not the probabilities: total per minute $\sim\Poisson(2+1)=\Poisson(3)$, mean $3$. The principle is superposition — independent Poisson streams merge into a Poisson at the summed rate. (Adding probabilities would be a category error; rates are what compose.)
:::

## Badge Earned — the Rainbow Badge

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/rainbow_badge.png" alt="The Rainbow Badge, a multicolored flower-shaped gym badge from Celadon City" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Rainbow Badge earned!</strong> Rank: Junior Trainer · 4 badges.</figcaption>
</figure>

You thinned Erika's pollen swarm, scaled the window, and waited for the bloom — three named laws in one clean chain — and she pressed the **Rainbow Badge** into your hand. **Rank: Junior Trainer · 4 badges** (Cascade, Thunder, Boulder, Rainbow). Four down, four to go on the road to the Indigo Plateau.

**Mastery checklist — tick each before you move on (mapped 1-to-1 to the outcomes):**

- ☐ **(A.5.0a/b)** I can **sum a geometric series** ($\frac{a}{1-r}$, $|r|<1$) and use the **$e^x$ Taylor series** ($\sum\lambda^k/k!=e^\lambda$) — the two algebraic tools the named laws stand on. *(Rematch: Concepts 0a–0b, Problems C5.1, C5.2, C5.20.)*
- ☐ **(A.5.1)** I can recognize and compute a **geometric** wait (pmf $q^{k-1}p$, survival $q^m$, mean $1/p$ or $q/p$), and state my convention. *(Rematch: Concept 1, WE 2, Problems C5.3, C5.4, C5.13.)*
- ☐ **(A.5.2)** I can apply **memorylessness** ($P(X>m+n\mid X>m)=q^n$) and refuse the gambler's "we're due." *(Rematch: Concept 2, WE 2, Problems C5.8, C5.12, C5.16.)*
- ☐ **(A.5.3)** I can recognize and compute a **negative binomial** (pmf $\binom{k+r-1}{k}p^rq^k$, mean $rq/p$) with the $r$-th success locked last. *(Rematch: Concept 3, WE 3, Problems C5.7, C5.15, C5.22, C5.25.)*
- ☐ **(A.5.4)** I can recognize and compute a **Poisson** (pmf $e^{-\lambda}\lambda^k/k!$, mean $=$ var $=\lambda$), **rescale $\lambda$ to the window**, and use the binomial limit. *(Rematch: Concept 4, WE 1, Problems C5.5, C5.6, C5.9, C5.10, C5.18, C5.24.)*
- ☐ **(A.5.5)** I can **add independent Poissons** by superposition ($\sum\lambda_i$) and **thin** a stream ($\lambda p$). *(Rematch: Concept 5, WE 1, 4, Problems C5.11, C5.14, C5.19, C5.23, C5.26.)*

**Gym Rematch pointers.** Said "we're due"? Concept 2 Beat 4 and the Team Rocket Trap, then C5.8, C5.16. Used $\lambda=3$ for a five-minute window? Concept 4 Beat 4, then C5.10, C5.24. Attached a binomial coefficient to a first-success wait? Concept 1 Beat 4, then C5.13. Added Poisson *probabilities* instead of rates? Concept 5 Beat 4, then C5.23.

> Next stop: **Fuchsia City and the Safari Zone**, where you'll learn to price *deductibles and limits* on the losses these counts produce — the bridge from "how many?" to "how much do we pay?" on the way to Koga's Soul Badge. Pack your named laws; the claim *count* you mastered here is half of every aggregate-loss model.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
