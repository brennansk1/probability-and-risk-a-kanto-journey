<!--
  file: ch17_order_statistics
  tier: B
  outcomes: 3f
  tia: C.3.1-C.3.2
  locale: Indigo Plateau / the Elite Four (the League; no gym badge)
  type: ice
  maps_to: the Elite Four bracket — the extreme of many draws
           (max [F]^n, min [S]^n, k-th order statistic, min of exponentials,
           series/parallel reliability)
  content_base: Version 1/book/chapters/ch14_order_clt.md (ORDER-STATISTICS portion
                only; the CLT lives in ch12) — re-skinned to the Elite Four,
                lifted to the V3 ch02/ch11 gold standard
-->

# The Extreme of Many — Order Statistics {.type-ice}

<figure>
<img src="../../assets/maps/kanto_ch17.png" alt="Kanto town map with the journey at its end: beyond Victory Road, at the northwest tip of the region, the Indigo Plateau, where the Pokémon League and the Elite Four await; all eight gym badges collected." style="width:72%; max-width:520px; display:block; margin:1em auto;">
<figcaption>The end of the road. Beyond Victory Road waits the <strong>Indigo Plateau</strong> — the Pokémon League itself, where the <em>Elite Four</em> stand between you and the Champion. No badge is handed out here; this is the League. The question now is never the typical challenger, but the <em>extreme</em> one.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Strongest of a Thousand"**

The doors of the Indigo Plateau stadium swing open and the roar of the crowd hits you like a wave. Below, on the registration floor, a thousand trainers are checking in — the largest League field in years. Eight badges ride in your case; now you are one face in a sea of them, Pikachu tense on your shoulder.

The League seeding officer, a harried woman with a clipboard, spots your Pokédex's glowing Actuary Mode and waves you over. "You — you do the risk math, right? The committee has a problem and the opening ceremony is in an hour."

"We know how strong a *typical* entrant is," she says. "But the bracket doesn't care about typical. The first trainer you could face in the gauntlet is the **strongest** of a whole pool of draws — the single toughest challenger out of all those entries. Out of a thousand independent entrants, how strong is the *strongest* one going to be? Not the average. The maximum."

She flips a page. "And it cuts the other way, too. The Elite Four chamber gate is sealed by a bank of independent locks; it opens the instant the *first* one trips — the **minimum** of their delays. The defensive wall the challenger must break holds until its *weakest* component gives. I keep asking about the best and the worst of many, and I have no formula for either."

Pikachu looks up at you. You realize every one of her questions is the *same kind* of question — what happens when you take *many* independent draws and look not at a typical one, but at an **extreme**: the largest, the smallest, or some specific rank in the sorted line-up. You have priced single random variables all journey long. You have never had a tool for the *biggest of many*, or the *first of many*.

The officer's pen hovers. **How strong is the strongest of a thousand, how soon is the first of many, and how do you price any rank in between — without sorting a single bracket by hand?**
:::

## Where You Are — 60-Second Retrieval

**Rank: Champion-ready · Badges: 8.** All eight badges are in your case — Cascade, Thunder, Boulder, Rainbow, Soul, Marsh, Volcano, and Giovanni's Earth Badge, earned on the climb through ch16. There is no ninth badge to win: the Indigo Plateau is the **League**, not a gym. What you carry into this final content chapter is exactly the machinery the extremes are built from.

From the joint-distribution chapters (**ch14**) you carry **independence**: independent events *multiply*,

$$P(A_1 \cap A_2 \cap \cdots \cap A_n) = P(A_1)\,P(A_2)\cdots P(A_n).$$

From the cdf/survival work you carry the **cdf** $F(x) = P(X \le x)$ — "the chance $X$ lands at or below $x$" — and its mirror the **survival function** $S(x) = P(X > x) = 1 - F(x)$ — "the chance $X$ exceeds $x$."

That is the entire foundation. The maximum and minimum of many draws are nothing but *multiplied* cdfs and survival functions. Take sixty seconds and prove you still own these before reading on.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the tools this chapter stands on**

Answer from memory; if any feels shaky, flip back before continuing.

1. If $F(x) = P(X \le x)$, what is $P(X > x)$ in terms of $F$? *(Answer: $S(x) = 1 - F(x)$, the survival function.)*
2. Two independent locks open w.p. $0.9$ and $0.8$. What is $P(\text{both open})$? *(Answer: $0.9 \times 0.8 = 0.72$ — independent events multiply.)*
3. Three independent draws are each $\le 0.5$ with probability $0.5$ apiece. What is $P(\text{all three} \le 0.5)$? *(Answer: $0.5^3 = 0.125$ — the same multiply, three times.)*

All three instant? Every formula below is one of these multiplications dressed up. Any hesitation? Reclaim "independent events multiply" first — it is the only prerequisite here.
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP077–EP080 (the League rounds: *"Round One — Begin!"* through the Elite-bracket matches)**

<figure><img src="../../assets/stills/ch17_now_playing.jpg" alt="Ash facing a rival across the battlefield in a League round (Indigo League EP078, Fire and Ice)." style="width:60%; max-width:440px; display:block; margin:0.4em auto;"><figcaption style="font-size:0.8em; color:#555;">A League round, EP078 — the bracket sorts a giant field and all that matters is its extreme: order statistics.</figcaption></figure>

These four episodes run the Indigo League conference — the packed stadium, the qualifying rounds, and the bracket narrowing a thousand entrants down to the few who face the toughest opponents. *Watch them alongside this chapter.* On screen the throughline is honest: a giant field is sorted, and all anyone cares about is the **extreme** end of it — who is left standing, who falls first. That is precisely our subject. (The seeding officer's "thousand draws," the sealed-gate locks, and the defensive-wall components are **in-world extensions** built to carry the order-statistics math — they dramatize the bracket, not specific on-screen scenes.)
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice crackles through the Pokédex as you step onto the stadium floor.

"Ash — this is the last *content* chapter of your journey, and it has one root idea: **what happens at the extremes when independence piles up.** Order statistics tell you about the best and the worst of many draws — and any rank in between. The whole engine is the multiply-independence rule you already own: the *maximum* is small only when *every* draw is small, so you raise the **cdf** to the $n$-th power; the *minimum* is large only when *every* draw is large, so you raise the **survival** to the $n$-th. Get the right function under the power and the rest is mechanical. This is a **Tier B** chapter — quick points once the one derivation clicks — but it underlies how an insurer prices its single largest loss, so do not coast."

By the end of this chapter you will be able to:

- **Derive and use** the distribution of the **maximum** and **minimum** of $n$ independent draws — $F_{\max}(x) = [F(x)]^n$ and $S_{\min}(x) = [S(x)]^n$ — including their densities and expectations. *(Outcome 3f.)*
- **Recognize** the **minimum of independent exponentials** as exponential with the **summed rate** (the hazards stack), and compute its mean and tail. *(Outcome 3f.)*
- **Write** the density and expectation of a **general $k$-th order statistic**, including the $\tfrac{k}{n+1}$ uniform mean for any rank. *(Outcome 3f.)*
- **Map** *series* and *parallel* **system reliability** to the minimum and the maximum, and compute each. *(Outcome 3f.)*

> *Exam-weight signpost.* Order statistics are a **Tier B** slice of Exam P's multivariate section: max/min mechanics, the min-of-exponentials shortcut, and the reliability mapping are quick, reliable points once the single derivation clicks. The general $k$-th-order density is rarer but worth the page. There is no continuity correction or CLT here — those live with the Normal in **ch12**.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own the Extremes?**

Already fluent? Prove it. Work these four with *correct method*, ~3 minutes each:

1. Eight independent qualifiers each have strength $X_i \sim \Unif(0,30)$. Find $\E[\max]$ and $P(\max > 27)$.
2. Three independent exponential locks have mean delays $4, 6, 12$ minutes. Find the mean time until the *first* trips and $P(\text{first} > 3)$.
3. Four judges each score $X_i \sim \Unif(0,1)$; the final uses the **second-lowest** ($k=2$). Find its expected value.
4. Three components each work w.p. $0.9$. Find the reliability **in series** and **in parallel**.

*(Answers: $\E[\max] = \tfrac{8}{9}\cdot 30 = 26.\overline{6}$ and $1 - 0.9^8 \approx 0.570$; rates add to $\tfrac12$, mean $2$ min, $e^{-1.5} \approx 0.223$; $\tfrac{2}{5} = 0.4$; series $0.9^3 = 0.729$, parallel $1 - 0.1^3 = 0.999$.)* Four for four with the right reasoning? **Skip to the Gym Battle** and clear the bracket. Any miss or hesitation? The teaching below was built exactly for you — and each concept has its own skip-gate, so a partial owner loses no time.
:::

---

Throughout, suppose $X_1, X_2, \dots, X_n$ are **independent and identically distributed** — "**i.i.d.**," read aloud *"independent, all from the same distribution"* — with common cdf $F(x)$ and survival function $S(x) = 1 - F(x)$. We teach five ideas, in increasing difficulty, each with its own skip-check and its own Pokédex Entry:

1. **The maximum** — the strongest of many *(the foundational order-statistic derivation)*
2. **The minimum** — the first of many, by the survival function
3. **The minimum of independent exponentials** — the exponential race, where rates add *(the one to memorize)*
4. **The general $k$-th order statistic** — any rank, by a counting coefficient
5. **System reliability** — series is the minimum, parallel is the maximum

## Concept 1 — The Maximum: Strongest of the Field

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Maximum**

Three independent rookies each score $X_i \sim \Unif(0,1)$. The scout flags the highest score. What is $P(\text{highest} \le 0.8)$?

If you instantly said **$0.8^3 = 0.512$** — and can say *why it is the single-draw cdf raised to the third power* — **skip to Concept 2**. If you wrote $0.8$, or you're unsure where the exponent comes from, this section is for you.
:::

**Beat 1 — The one-sentence idea.** *The largest of $n$ independent draws is at most $x$ exactly when **every** draw is at most $x$ — so you raise the single-draw cdf to the $n$-th power.*

**Beat 2 — Anchor + concrete instance.** Recall the cdf $F(x) = P(X \le x)$ and the multiply-independence rule from ch14. The maximum just stacks them together. Here is the story, with real numbers.

The seeding committee hands you the file on $n = 3$ regional qualifiers (we keep it small enough to picture; the thousand comes back at the Gym Battle). Each qualifier's strength $X_i$ is independent and **Uniform on $[0,1]$**, so the single-draw cdf is $F(x) = P(X_i \le x) = x$ on $[0,1]$. The top seed must face the **strongest** of the three. *What is the chance the strongest of the three scores at most $0.8$?*

**Beat 3 — Reason through it in plain words.** Call the maximum $M$. When is the *strongest* of the three at most $0.8$? Only when *all three* are at most $0.8$ — if even one qualifier scored above $0.8$, the maximum would exceed $0.8$. So "the max is $\le 0.8$" is the *same event* as "draw 1 is $\le 0.8$ **and** draw 2 is $\le 0.8$ **and** draw 3 is $\le 0.8$." Because the three draws are independent, those three chances multiply:

$$P(M \le 0.8) = \underbrace{P(X_1 \le 0.8)}_{0.8} \cdot \underbrace{P(X_2 \le 0.8)}_{0.8} \cdot \underbrace{P(X_3 \le 0.8)}_{0.8} = 0.8^3 = 0.512.$$

The exponent $3$ is *not* decoration — it is one factor of $0.8$ for each independent draw that has to fall in line.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The natural mistake is to report the single-draw chance, or — worse — to *multiply $F$ by $n$* instead of raising it to the $n$:

$$P(M \le 0.8) \overset{?}{=} 0.8 \qquad \text{or} \qquad P(M \le 0.8) \overset{?}{=} n\,F(0.8) = 3(0.8) = 2.4. \qquad\textbf{(both wrong)}$$

The first ($0.8$) is the chance *one* draw is at most $0.8$; the maximum being small is a *much* stronger demand — *all three* must cooperate, and asking three independent things to all happen makes the probability *smaller*, not the same ($0.512 < 0.8$). The second ($n\,F$) is the error to brand on your memory: cdfs of independent events **multiply**, they do not add or scale — and $2.4$ isn't even a valid probability, which is the instant tell that $n\cdot F$ is nonsense. It is $[F]^n$, never $nF$. (This is exactly the slip Team Rocket walks into later.) The deeper version of the first error shows up at the other end: people report the population *mean* for the strongest of a crowd. The strongest of many sits far *above* the typical draw — never confuse "a draw" with "the biggest draw."

**Beat 5 — Translate into notation, one glyph at a time.** The maximum is the **$n$-th order statistic**, written

$$X_{(n)} \qquad \text{read aloud: ``}X\text{ sub-paren-}n\text{,'' the largest of the }n\text{ draws.}$$

The parentheses around the subscript are the tell: $X_{(n)}$ means *"the value that lands in sorted position $n$,"* not "the $n$-th draw you happened to make." We name its cdf $F_{\max}(x) = P(X_{(n)} \le x)$. Translating Beat 3's plain reasoning — "the max is $\le x$ iff every draw is $\le x$, and independent chances multiply" — into symbols:

$$F_{\max}(x) = P(X_1 \le x,\, X_2 \le x,\, \dots,\, X_n \le x) = \prod_{i=1}^{n} P(X_i \le x) = [F(x)]^n.$$

The product sign $\prod$ reads *"the product of"* — multiply these together (the multiplicative cousin of the summation $\sum$). Because the draws are identically distributed, every factor is the same $F(x)$, and the product collapses to $[F(x)]^n$.

**Beat 6 — Derive the density from the cdf.** We did not assert $[F(x)]^n$ — we built it: "all $n$ at most $x$" is an intersection of independent events, so its probability is the product of $n$ identical factors $F(x)$. To get the **density**, differentiate the cdf (the density is the derivative of the cdf), using the power rule and the chain rule $F'(x) = f(x)$:

$$\boxed{\,F_{\max}(x) = [F(x)]^n, \qquad f_{\max}(x) = \frac{d}{dx}[F(x)]^n = n\,[F(x)]^{n-1}\,f(x).\,}$$

The factor $n[F(x)]^{n-1}$ comes from the power rule; the trailing $f(x)$ is the inner derivative.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* read $F$, raise to the $n$. For our three uniforms, $P(M \le 0.8) = 0.8^3 = 0.512$.
- *A twist — the tail.* "At least one above the bar" is the *complement* of the max being below it: $P(M > x) = 1 - [F(x)]^n$. For three uniforms, $P(M > 0.9) = 1 - 0.9^3 = 0.271$.
- *General — the expectation.* For $n$ i.i.d. $\Unif(0,1)$ the mean of the max is $\dfrac{n}{n+1}$ (derived in the Entry below); on $\Unif(0,b)$ it scales to $\dfrac{n}{n+1}\,b$. For our three uniforms, $\E[M] = \tfrac34$. It climbs toward the ceiling as $n$ grows — the bigger the field, the closer the strongest sits to the top.
- *Boundary:* with $n = 1$ the formula gives $F_{\max} = F$ and $\E[M] = \tfrac{1}{2}b$ — one draw *is* its own maximum. Sanity holds.

**Beat 8 — Picture it.** The figure shows both extremes side by side: the max-cdf $[F]^n$ hugs the floor and only climbs near the ceiling, while (Concept 2's) min-survival $[S]^n$ drops toward the floor — both pulled to the edges as the field $n$ grows.

<figure>
<img src="../../assets/diagrams/ch17_order_max_min.png" alt="Two panels for n i.i.d. Uniform(0,1) draws. Left: the cdf of the maximum F_max(x) = [F(x)]^n = x^n, drawn for n=1 (the diagonal), n=3, and n=8; larger n bows the curve hard toward the floor so the max is rarely small, with a marked point showing F_max(0.8)=0.8^8 about 0.17. Right: the survival of the minimum S_min(x) = [S(x)]^n = (1-x)^n for the same n, dropping ever faster toward the floor; a marked point shows S_min(0.2)=0.8^8 about 0.17. A Lapras sprite sits in the clear lower margin of the left panel." style="width:90%; max-width:740px; display:block; margin:1em auto;">
<figcaption>The bracket. <strong>Left:</strong> the maximum's cdf $[F(x)]^n$ — more challengers push the strongest toward the ceiling ($F_{\max}(0.8)=0.8^8\approx0.17$: the max of eight is almost never below $0.8$). <strong>Right:</strong> the minimum's survival $[S(x)]^n$ — more challengers push the first-to-fall toward the floor. Both come from one move: multiplying independent factors.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now take any "the strongest / highest / longest-lasting / last to fail of $n$ independent draws" and write its cdf ($[F(x)]^n$), its density ($n[F(x)]^{n-1}f(x)$), and — for uniforms — its mean ($\tfrac{n}{n+1}b$) without grinding an integral.

::: pokedex-entry
**POKÉDEX ENTRY №01 — The Maximum (the $n$-th order statistic)**

For i.i.d. $X_1, \dots, X_n$ with cdf $F$, the maximum $M = X_{(n)} = \max_i X_i$ has
$$F_{\max}(x) = [F(x)]^n, \qquad f_{\max}(x) = n\,[F(x)]^{n-1}\,f(x), \qquad P(M > x) = 1 - [F(x)]^n.$$
For $n$ i.i.d. $\Unif(0,b)$: $\;\E[\max] = \dfrac{n}{n+1}\,b$. *(Derivation: $\E[M] = \int_0^b x \cdot n(x/b)^{n-1}\tfrac1b\,dx = \tfrac{n}{n+1}b$.)*

*In plain terms:* the largest value is at most $x$ exactly when **every** draw is at most $x$ — independent events multiply, so raise the single-draw cdf to the $n$-th power. **It is $[F]^n$, never $nF$.**

*Recognition cue:* **"strongest," "highest," "longest-lasting," "last to fail,"** or a *parallel* system $\to$ reach for $[F(x)]^n$.
:::

## Concept 2 — The Minimum: First of the Field

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Minimum**

Three components each fail with survival function $S(x) = e^{-x/10}$ (mean-$10$ lifetimes), independently. What is the chance *all three* survive past $x = 5$ — i.e. the *first* failure is after $5$?

If you instantly said **$[S(5)]^3 = (e^{-0.5})^3 = e^{-1.5} \approx 0.223$** — by raising the *survival* function to the third power — **skip to Concept 3**. If you reached for the cdf instead of the survival, read on: the minimum is governed by $S$, not $F$.
:::

**Beat 1 — The one-sentence idea.** *The smallest of $n$ independent draws exceeds $x$ exactly when **every** draw exceeds $x$ — so you raise the single-draw **survival** function to the $n$-th power.*

**Beat 2 — Anchor + concrete instance.** This is Concept 1's mirror image. There, "max $\le x$" meant *all* below $x$, multiplying cdfs. Here, "min $> x$" means *all* above $x$, multiplying **survival** functions $S(x) = 1 - F(x)$.

Three of your Pokémon hold a defensive line against the Elite Four's opening assault. Their independent times-until-they-break are i.i.d. with survival $S(x) = e^{-x/10}$ (mean $10$ seconds each). The line collapses the instant the *first* one breaks. *What is the chance the line survives past $x = 5$ seconds?*

**Beat 3 — Reason through it in plain words.** Call the minimum $m$. When does the *first to break* hold out past $5$ seconds? Only when *all three* hold out past $5$ — if any single one breaks earlier, the line is already down. So "the min $> 5$" is the same event as "draw 1 $> 5$ **and** draw 2 $> 5$ **and** draw 3 $> 5$," and independence multiplies:

$$P(m > 5) = \big[S(5)\big]^3 = \big(e^{-5/10}\big)^3 = e^{-15/10} = e^{-1.5} \approx 0.223.$$

One survival factor per independent draw that must hold out.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The seductive error is to reuse the *maximum's* machinery — raising the **cdf** to the $n$ — for the minimum:

$$P(m > 5) \overset{?}{=} [F(5)]^3 \qquad\text{or}\qquad F_{\min}(x) \overset{?}{=} [F(x)]^n. \qquad\textbf{(wrong — that's the maximum)}$$

The minimum being *large* is about *all draws being large*, which is a statement about the **survival** function, not the cdf. Use $[S(x)]^n$ for "min $>$" and only then convert: $F_{\min}(x) = 1 - [S(x)]^n$. Reaching for $[F]^n$ on a minimum problem prices the *maximum* instead — the exact opposite tail.

**Beat 5 — Translate into notation, one glyph at a time.** The minimum is the **first order statistic**,

$$X_{(1)} \qquad \text{read aloud: ``}X\text{ sub-paren-one,'' the smallest of the }n\text{ draws.}$$

Translating Beat 3 — "the min $> x$ iff every draw $> x$, multiply" — into symbols, naming the minimum's survival function $S_{\min}(x) = P(X_{(1)} > x)$:

$$S_{\min}(x) = P(X_1 > x,\, \dots,\, X_n > x) = \prod_{i=1}^{n} P(X_i > x) = [S(x)]^n.$$

Its cdf is the complement, $F_{\min}(x) = 1 - [S(x)]^n$, and differentiating gives the density.

**Beat 6 — Derive the general formula.** The general min, derived just like the max but from survival functions (differentiate $F_{\min} = 1 - [S(x)]^n$, with $S'(x) = -f(x)$):

$$\boxed{\,S_{\min}(x) = [S(x)]^n, \qquad F_{\min}(x) = 1 - [S(x)]^n, \qquad f_{\min}(x) = n\,[S(x)]^{n-1}\,f(x).\,}$$

For $n$ i.i.d. $\Unif(0,b)$, $S(x) = 1 - x/b$, giving the mirror of the max: $\E[\min] = \tfrac{b}{n+1}$. (For our line of three mean-$10$ exponentials, the next concept hands you the minimum's whole distribution in one line.)

**Beat 7 — Ramp the difficulty.**

- *Simplest:* survival of the min, $[S(x)]^n$. Three mean-$10$ lines past $5$: $(e^{-0.5})^3 = e^{-1.5} \approx 0.223$.
- *Twist — the cdf.* "The first breaks by time $x$" is $F_{\min}(x) = 1 - [S(x)]^n$. By $x=5$: $1 - 0.223 = 0.777$.
- *General — uniform min.* For $n$ i.i.d. $\Unif(0,1)$, $S(x) = 1 - x$, so $f_{\min}(x) = n(1-x)^{n-1}$ and $\E[\min] = \tfrac{1}{n+1}$.
- *Boundary:* with $n=1$ the formula gives back the original $S$; one draw is its own minimum. Sanity holds.

**Beat 8 — Picture it.** The right-hand panel of the Concept-1 figure is exactly this: the min-survival $[S(x)]^n$ plunges toward the floor as the field grows — the first failure comes sooner and sooner. (The exponential *race* gets its own picture in the next concept.)

**Beat 9 — Consolidate.** You can now write the distribution of the *weakest / first / soonest* of $n$ draws via $[S(x)]^n$, take its complement for the cdf, and differentiate for the density.

::: pokedex-entry
**POKÉDEX ENTRY №02 — The Minimum (the first order statistic)**

For i.i.d. $X_1, \dots, X_n$ with survival function $S$, the minimum $m = X_{(1)} = \min_i X_i$ has
$$S_{\min}(x) = [S(x)]^n, \qquad F_{\min}(x) = 1 - [S(x)]^n, \qquad f_{\min}(x) = n\,[S(x)]^{n-1}\,f(x).$$
For $n$ i.i.d. $\Unif(0,b)$: $\;\E[\min] = \tfrac{b}{n+1}$.

*In plain terms:* the smallest exceeds $x$ only when **every** draw does — raise the *survival* function to the $n$-th, not the cdf.

*Recognition cue:* **"weakest," "first to fail," "soonest," "shortest,"** or a *series* system $\to$ reach for $[S(x)]^n$.
:::

## Concept 3 — The Minimum of Independent Exponentials: The Race Where Rates Add

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Exponential Race**

Three independent exponential locks have mean delays $4$, $6$, and $12$ minutes. Find the mean time until the *first* one trips.

If you answered **$2$ minutes** — by adding the *rates* $\tfrac14 + \tfrac16 + \tfrac1{12} = \tfrac12$ and inverting — **skip to Concept 4**. If you averaged the means to $7.\overline{3}$, or summed them, read on: exponentials race in a special way.
:::

**Beat 1 — The one-sentence idea.** *The minimum of independent exponentials is itself exponential, with rate equal to the **sum** of the rates — so the hazards stack and the race finishes fast.*

**Beat 2 — Anchor + concrete instance.** Concept 2 handed you $S_{\min}(x) = [S(x)]^n$ for any distribution. When the draws are *exponential*, that general rule collapses into something far cleaner — the single most-tested order-statistic fact on the exam.

The Elite Four chamber gate is sealed by three independent locks. Their trip-times are exponential with mean delays $4$, $6$, and $12$ minutes (so rates $\tfrac14$, $\tfrac16$, $\tfrac1{12}$ per minute). The gate opens the instant the **first** lock trips — the *minimum* of the three delays. *How long until the gate opens, on average, and what is $P(\text{first} > 3)$?*

**Beat 3 — Reason through it in plain words.** A *race* finishes *faster* than any single runner — the first of several clocks rings *sooner* than the average clock, not later. Each exponential has a constant hazard (a per-minute "rate" of tripping); when several run at once, those hazards **stack**, so the combined clock is faster. Adding rates is what "stacking hazards" means in symbols, and it makes the combined mean *shorter*, exactly as a race should.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The classic error is to handle the *minimum* by averaging or summing the *means*:

$$\E[\text{first to trip}] \overset{?}{=} \frac{4 + 6 + 12}{3} = 7.\overline{3} \quad\text{or}\quad 4+6+12 = 22. \qquad\textbf{(both wrong)}$$

But the first of several to fire happens *sooner* than the typical one, and far sooner than the sum. The fix is the survival-function rule plus the one exponential fact below: **the rates add, not the means.** Adding rates makes the combined clock *faster* (shorter mean), exactly as a race should.

**Beat 5 — Translate into notation, one glyph at a time.** Write $X_i \sim \Expo(\text{rate }\lambda_i)$, where $\lambda_i = 1/\theta_i$ is the **rate** (events per unit time) and $\theta_i$ the **mean**, so the survival is $S_i(x) = e^{-\lambda_i x}$. Read $\lambda$ as *"how fast this clock ticks"* and $\theta = 1/\lambda$ as *"how long on average until it does."*

**Beat 6 — Derive the rate-sum.** Apply Concept 2's rule with exponential survivals. The minimum's survival is the product:

$$S_{\min}(x) = \prod_{i=1}^{n} e^{-\lambda_i x} = e^{-(\lambda_1 + \cdots + \lambda_n)\,x}.$$

That is *exactly* the survival function of one exponential with rate $\sum_i \lambda_i$. So **the minimum of independent exponentials is itself exponential, with rate equal to the sum of the rates** — the hazards stack:

$$\boxed{\,\min_i X_i \sim \Expo\!\Big(\textstyle\sum_i \lambda_i\Big), \qquad \E[\min] = \frac{1}{\sum_i \lambda_i}.\,}$$

For $n$ i.i.d. exponentials each with mean $\theta$ (rate $1/\theta$), the minimum is exponential with rate $n/\theta$, hence **mean $\theta/n$**. Back to the gate's three locks, means $4, 6, 12 \Rightarrow$ rates $\tfrac14, \tfrac16, \tfrac1{12}$:

$$\lambda_{\min} = \tfrac14 + \tfrac16 + \tfrac1{12} = \tfrac{3+2+1}{12} = \tfrac{6}{12} = \tfrac12 \;\Rightarrow\; \E[\text{first}] = \frac{1}{1/2} = 2 \text{ min}, \qquad P(\text{first} > 3) = e^{-\frac12\cdot 3} = e^{-1.5} \approx 0.223.$$

**Beat 7 — Ramp the difficulty.**

- *Simplest:* i.i.d. exponentials — add $n$ equal rates. Three mean-$10$ clocks $\to$ rate $\tfrac{3}{10}$, mean $\tfrac{10}{3} \approx 3.33$ s.
- *Twist — unequal rates.* The gate's $4,6,12$ clocks: convert to rates, add, invert (mean $2$). Never average the means.
- *General — the tail.* Since the minimum is itself exponential, any tail is one keystroke: $P(\min > t) = e^{-(\sum\lambda_i)t}$.
- *Boundary:* one clock ($n=1$) gives back the original exponential; sanity holds.

**Beat 8 — Picture it.** The exponential race, drawn: three clocks of different rates, and their minimum a single steeper exponential that rings sooner than any of them.

<figure>
<img src="../../assets/diagrams/ch17_reliability_series_parallel.png" alt="Two circuit schematics used here for the series case. Left: three components drawn in a single line (series) labeled lifetime = min, reliability = product of survivals = 0.729 — the structure whose lifetime is the minimum of the component lifetimes. Right: a parallel bank labeled lifetime = max. A Lapras sprite sits in the upper margin." style="width:82%; max-width:660px; display:block; margin:1em auto;">
<figcaption>A <em>series</em> chain (left) fails the instant its <strong>first</strong> component fails — its lifetime is the <strong>minimum</strong>, and when the components are exponential, that minimum is itself exponential with the rates added. (The same figure's parallel bank, right, is Concept 5's maximum.)</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now collapse a *race of independent exponentials* into a single exponential by **adding the rates**, read off its mean as $1/\sum\lambda_i$, and compute any tail in one keystroke.

::: pokedex-entry
**POKÉDEX ENTRY №03 — The Minimum of Independent Exponentials**

If $X_i \sim \Expo(\text{rate }\lambda_i)$ independently, then
$$\min_i X_i \sim \Expo\!\Big(\textstyle\sum_i \lambda_i\Big), \qquad S_{\min}(x) = e^{-(\sum_i \lambda_i)x}, \qquad \E[\min] = \frac{1}{\sum_i \lambda_i}.$$
For $n$ i.i.d. exponentials with mean $\theta$: $\;\min \sim \Expo$ with **mean $\theta/n$**.

*In plain terms:* several exponential clocks racing — the first to ring is exponential, and *faster*, because the rates add (the hazards stack).

*Recognition cue:* the *first* of several independent exponential waits, or a *series* of exponential components $\to$ **add the rates**, then invert once for the mean. Never average the means.
:::

## Concept 4 — The General $k$-th Order Statistic

::: concept-gate
**DO YOU ALREADY OWN THIS? — General Rank**

Four judges each score $X_i \sim \Unif(0,1)$ independently; the final drops the lowest and uses the **second-lowest** ($k=2$). What is its expected value?

If you answered **$\tfrac{2}{5} = 0.4$** — using $\E[X_{(k)}] = \tfrac{k}{n+1}$ — **skip to Concept 5**. If you weren't sure how to handle a rank that's neither the max nor the min, read on.
:::

**Beat 1 — The one-sentence idea.** *To be the $k$-th smallest of $n$ draws, one draw lands at $x$, exactly $k-1$ fall below it, and the remaining $n-k$ fall above — and a counting coefficient tallies the arrangements.*

**Beat 2 — Anchor + concrete instance.** Max ($k=n$) and min ($k=1$) were the easy ends. Now we want any rank in between — a median, a second-best, a second-worst. The tool is the same "events multiply" idea, plus the **multinomial counting** from the combinatorics chapter.

Four judges score the Elite-Four exhibition match, each $X_i \sim \Unif(0,1)$ independently. The final score *drops the lowest and uses the second-lowest* — the $k = 2$ order statistic, $X_{(2)}$, of $n = 4$. *What is its expected value?*

**Beat 3 — Reason through it in plain words.** Picture the density at a point $x$. For $X_{(2)}$ to sit right at $x$, three things must line up at once: **one** of the four draws is at $x$ (density $f(x)$), exactly **$k-1 = 1$** of the others falls *below* $x$ (each with chance $F(x)$), and the remaining **$n - k = 2$** fall *above* $x$ (each with chance $1 - F(x)$). But *which* draw is the one at $x$, and *which* land below, can be arranged in several ways — that is where the counting coefficient comes in.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The tempting shortcut is to forget the coefficient and write $f(x)\,F(x)^{k-1}(1-F(x))^{n-k}$ alone. But that prices *one specific labeling* — "draw #1 is the one at $x$, draws #2 below, #3 and #4 above." There are many equally valid labelings, and ignoring them undercounts the density. The number of ways to choose which draw sits at $x$, which $k-1$ go below, and which $n-k$ go above is the **multinomial coefficient** $\dfrac{n!}{(k-1)!\,1!\,(n-k)!}$. Leave it out and your density won't integrate to $1$.

**Beat 5 — Translate into notation, one glyph at a time.** The $k$-th smallest value is $X_{(k)}$, read *"$X$ sub-paren-$k$,"* the value in sorted position $k$. The factorial $n!$ reads *"$n$ factorial"* — the count of ways to order $n$ items. Assembling the three pieces with their count:

$$f_{X_{(k)}}(x) = \frac{n!}{(k-1)!\,(n-k)!}\,[F(x)]^{k-1}\,[1 - F(x)]^{\,n-k}\,f(x).$$

Read it left to right: *the number of arrangements*, times *$k-1$ draws below*, times *$n-k$ draws above*, times *one draw right here*.

**Beat 6 — Derive the uniform mean for free.** For i.i.d. $\Unif(0,1)$ ($F(x) = x$, $f(x) = 1$), that density is exactly the **Beta** density $\BetaDist(k,\,n-k+1)$, whose mean is a clean ratio:

$$\boxed{\;\E\!\big[X_{(k)}\big] = \frac{k}{n+1} \quad \text{for i.i.d. } \Unif(0,1).\;}$$

Check the ends: $k=n$ gives $\tfrac{n}{n+1}$ (the max, Entry №01) and $k=1$ gives $\tfrac{1}{n+1}$ (the min, Entry №02) — the general formula contains both. For the four judges, $\E[X_{(2)}] = \tfrac{2}{5} = 0.4$.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* uniform mean of any rank, $\tfrac{k}{n+1}$. Median of $5$ draws ($k=3$): $\tfrac{3}{6} = \tfrac12$.
- *Twist — a tail probability.* $X_{(2)}$ density of four uniforms is $\BetaDist(2,3)$: $f(x) = 12\,x(1-x)^2$ — integrate it for any probability.
- *General density:* plug any $F$ and $f$ into the $k$-th-order formula; it works for any continuous distribution.
- *Edge — the range.* The expected gap between strongest and weakest of $n$ uniforms is $\E[X_{(n)}] - \E[X_{(1)}] = \tfrac{n-1}{n+1}$.

**Beat 8 — Picture it.** The figure sorts four draws onto a line, circles the $k=2$ dot, and overlays the $\BetaDist(k,\,n-k+1)$ density of each rank — every mean sitting at $\tfrac{k}{n+1}$.

<figure>
<img src="../../assets/diagrams/ch17_kth_order.png" alt="Top: a number line from 0 to 1 with four sorted dots labeled X_(1) through X_(4); the second dot, X_(2), is enlarged and red, with brackets marking k-1=1 draw below it and n-k=2 draws above it. Bottom: four density curves for the k-th order statistic of n=4 i.i.d. Uniform(0,1) draws, each a Beta(k, n-k+1): k=1 (mean 1/5) peaks left, k=2 (mean 2/5), k=3 (mean 3/5), k=4 (mean 4/5) peaks right; a dotted line marks the k=2 mean at 0.4. A Lapras sprite sits in the lower-left margin." style="width:84%; max-width:680px; display:block; margin:1em auto;">
<figcaption>The $k$-th order statistic: sort the draws (top), and the value in position $k$ has density $\BetaDist(k,\,n-k+1)$ (bottom), with mean $\tfrac{k}{n+1}$. The max ($k=n$) and min ($k=1$) are just the two ends of this same family.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now write the density of *any* rank, read off $\tfrac{k}{n+1}$ for uniform means, and recover the max and min as the two endpoints $k=n$ and $k=1$.

::: pokedex-entry
**POKÉDEX ENTRY №04 — The General $k$-th Order Statistic**

$$f_{X_{(k)}}(x) = \frac{n!}{(k-1)!\,(n-k)!}\,[F(x)]^{k-1}\,[1-F(x)]^{\,n-k}\,f(x).$$
For i.i.d. $\Unif(0,1)$: $\;\E[X_{(k)}] = \dfrac{k}{n+1}$ (the $\BetaDist(k,\,n-k+1)$ mean), with max ($k=n$) and min ($k=1$) as special cases.

*In plain terms:* one draw lands at $x$, $k-1$ fall below, $n-k$ fall above; a multinomial coefficient counts the labelings.

*Recognition cue:* a **specific rank** (median, second-best, second-worst) $\to$ the $k$-th-order density; for uniform draws, the mean is the clean ratio $\tfrac{k}{n+1}$.
:::

## Concept 5 — System Reliability: Series is Min, Parallel is Max

::: concept-gate
**DO YOU ALREADY OWN THIS? — Reliability**

Three components each work with probability $0.9$, independently. Wired **in parallel** (any one suffices), what is the system's reliability? And **in series** (all must work)?

If you answered **parallel $1 - 0.1^3 = 0.999$** and **series $0.9^3 = 0.729$**, **skip to the Worked Examples**. If you mixed up which structure uses which formula, read on — it's a two-line mapping.
:::

**Beat 1 — The one-sentence idea.** *A series system lives only as long as its **weakest** component (the minimum); a parallel system lives until its **last** component dies (the maximum).*

**Beat 2 — Anchor + concrete instance.** A system of independent components is just an order-statistic question in disguise — and it's the named real-world use of this whole chapter. The challenger's defensive wall and the Elite-Four chamber's lock bank are both systems of independent parts.

Three independent components each work with probability $0.9$ (equivalently, each survives to time $t$ with $S_i(t) = 0.9$). *Find the system reliability wired (i) in series and (ii) in parallel.*

**Beat 3 — Reason through it in plain words.** A **series** system is a chain: every link must hold, so it fails the instant the *first* component fails. Its lifetime is therefore the **minimum** of the component lifetimes — and by Concept 2 it survives only when *all* survive, so its reliability multiplies the survivals. A **parallel** system has backups everywhere: it works as long as *any* component works, and fails only when the *last* one dies. Its lifetime is the **maximum** — and by Concept 1 it fails only when *all* fail, so we take one minus the product of the failure probabilities.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is to swap the two — to multiply survivals for a *parallel* bank ("$0.9^3$") or to use $1 - 0.1^3$ for a *series* chain. That inverts the answer: a redundant parallel bank should be *more* reliable than one component ($0.999 > 0.9$), while a series chain should be *less* reliable ($0.729 < 0.9$). If your "redundant" system came out *less* reliable than a single part, you mapped it backwards. **Series multiplies survivals (min); parallel multiplies failures and subtracts (max).**

**Beat 5 — Translate into notation, one glyph at a time.** Let $S_i(t) = P(X_i > t)$ be component $i$'s survival and $F_i(t) = 1 - S_i(t)$ its failure probability by time $t$. "Reliability" $R(t)$ is just the system's survival function.

**Beat 6 — Derive both formulas.** A series system survives iff *all* survive (the minimum exceeds $t$), so by Concept 2:

$$R_{\text{series}}(t) = P(\min_i X_i > t) = \prod_{i=1}^{n} S_i(t).$$

A parallel system fails iff *all* fail (the maximum is below $t$), so by Concept 1:

$$R_{\text{parallel}}(t) = 1 - P(\max_i X_i \le t) = 1 - \prod_{i=1}^{n} F_i(t).$$

For three components each at $0.9$:

$$\boxed{\;R_{\text{series}} = 0.9^3 = 0.729, \qquad R_{\text{parallel}} = 1 - 0.1^3 = 0.999.\;}$$

**Beat 7 — Ramp the difficulty.**

- *Simplest:* identical components — series $0.9^3 = 0.729$, parallel $1 - 0.1^3 = 0.999$.
- *Twist — unequal components.* Series of $0.95, 0.90, 0.80$: $R = 0.95\cdot0.90\cdot0.80 = 0.684$. Parallel: $1 - 0.05\cdot0.10\cdot0.20 = 0.999$.
- *General — exponential components.* Series of $n$ exponential parts: lifetime is the min, so (Concept 3) it is exponential with the rates added. Parallel of $n$ i.i.d. exponentials with mean $\theta$: expected time-to-blackout is $\theta\sum_{j=1}^n \tfrac1j$ (a harmonic sum).
- *Edge — mixed structures.* Real systems nest series and parallel blocks; collapse each block to a single reliability, then combine.

**Beat 8 — Picture it.** The figure draws both structures: a series chain whose lifetime is the minimum, and a parallel bank whose lifetime is the maximum.

<figure>
<img src="../../assets/diagrams/ch17_reliability_series_parallel.png" alt="Two circuit schematics. Left: three components drawn in a single line (series) labeled lifetime = min, reliability = product of survivals = 0.9^3 = 0.729. Right: three components drawn as three parallel branches (parallel) labeled lifetime = max, reliability = 1 minus product of failure probs = 1 - 0.1^3 = 0.999. A Lapras sprite sits in the upper margin." style="width:82%; max-width:660px; display:block; margin:1em auto;">
<figcaption>Reliability as order statistics: a <em>series</em> chain dies with the <strong>minimum</strong> (the weakest link), so its reliability is $\prod_i S_i = 0.729$; a <em>parallel</em> bank survives to the <strong>maximum</strong> (the last backup), so its reliability is $1 - \prod_i F_i = 0.999$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now translate any "in series" / "in parallel" wording into min / max, multiply the right factors, and sanity-check by the direction (redundancy raises reliability, chaining lowers it).

::: pokedex-entry
**POKÉDEX ENTRY №05 — System Reliability (Series = Min, Parallel = Max)**

For independent components with survivals $S_i(t)$ and failures $F_i(t) = 1 - S_i(t)$:
$$R_{\text{series}}(t) = P(\min_i X_i > t) = \prod_i S_i(t), \qquad R_{\text{parallel}}(t) = 1 - P(\max_i X_i \le t) = 1 - \prod_i F_i(t).$$

*In plain terms:* a chain dies with its weakest link (minimum); a redundant bank survives on its last backup (maximum).

*Recognition cue:* **"in series," "all must work," "chain"** $\to$ minimum, $\prod S_i$. **"In parallel," "with backups," "redundant," "any one suffices"** $\to$ maximum, $1 - \prod F_i$. Sanity: redundancy *raises* reliability; chaining *lowers* it.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/vs/lorelei-gen3.png" alt="Lorelei of the Elite Four, the ice-type specialist" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Lorelei — first of the Elite Four, the ice master who opens the gauntlet</figcaption>
</figure>

Four examples, fading from fully narrated to exam-speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because the max/min derivation is the load-bearing move.

### Worked Example 17.1 — Lorelei and the Strongest of the Field (full narration; understanding-first)

**ARCHETYPE:** *Expectation and tail of a maximum of i.i.d. uniforms (Entry №01).*

**Setup.** Lorelei opens the bracket. Each of $n = 8$ qualifiers in the opening pool has strength $X_i \sim \Unif(0,30)$, independent. Find (a) $\E[\max]$, the expected strength of the strongest qualifier, and (b) $P(\max > 27)$, the chance the strongest tops $27$.

**Step 1 — Identify.** "The *strongest* of many independent draws" $\to$ the **maximum**, the $n$-th order statistic. Reach for $[F(x)]^n$.

**Step 2 — Professor's Path (the why).** The single-draw cdf on $[0,30]$ is $F(x) = x/30$. The max-cdf raises it to the $n$: $F_{\max}(x) = (x/30)^8$. For the mean, the uniform shortcut comes from $\E[\max] = \int_0^{30} x\,f_{\max}(x)\,dx$ with $f_{\max}(x) = 8(x/30)^7\tfrac1{30}$, which integrates to $\tfrac{n}{n+1}b$:

$$\E[\max] = \frac{n}{n+1}\cdot 30 = \frac{8}{9}\cdot 30 = 26.\overline{6}.$$

For the tail, use the complement of the max-cdf:

$$P(\max > 27) = 1 - F_{\max}(27) = 1 - \Big(\tfrac{27}{30}\Big)^8 = 1 - 0.9^8 = 1 - 0.4305 = 0.5695.$$

**Step 3 — Trainer's Path (the fast how).** $\E[\max] = \tfrac{8}{9}\cdot 30 = 26.67$ on sight. Tail: $1 - 0.9^8 \approx 0.570$.

**Step 4 — Check & pitfall.** $26.67$ sits just below the ceiling $30$, exactly where the strongest of eight belongs ✓. **Pitfall:** reporting the single-draw mean $15$ for the maximum — the strongest of a crowd is far above the typical entrant. The other pitfall: writing $n\,F = 8(0.9) = 7.2$ instead of $0.9^8$ — cdfs *multiply*. *(Back-ref: Entry №01.)*

### Worked Example 17.2 — Bruno's Chamber Gate (partial guidance; min of exponentials)

**ARCHETYPE:** *Minimum of independent exponentials — rates add (Entry №03).*

**Setup.** Past Lorelei, Bruno's chamber gate is sealed by three independent locks; their trip-times are exponential with means $4$, $6$, and $12$ minutes. The gate opens when the *first* lock trips. Find the distribution and mean of the first-trip time, and $P(\text{first} > 3)$.

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/vs/bruno.png" alt="Bruno of the Elite Four, the fighting-type specialist" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>Bruno</strong> — second of the Elite Four; his sealed chamber gate is the exponential race.</figcaption>
</figure>

**Identify.** "First to trip" is the **minimum** of independent exponentials. *Your move: convert means to rates, then add the rates.*

Means $4, 6, 12 \Rightarrow$ rates $\lambda_1 = \tfrac14,\ \lambda_2 = \tfrac16,\ \lambda_3 = \tfrac1{12}$. Rates add:

$$\lambda = \tfrac14 + \tfrac16 + \tfrac1{12} = \tfrac{3+2+1}{12} = \tfrac12.$$

So the first trip is $\Expo(\text{rate }\tfrac12)$, i.e. **mean $= 1/\lambda = 2$ minutes**, with

$$P(\text{first} > 3) = e^{-\lambda \cdot 3} = e^{-1.5} \approx 0.2231.$$

**Check & pitfall.** The minimum's mean ($2$) is *below* the smallest individual mean ($4$) — correct: a race finishes faster than its quickest runner. **Pitfall:** averaging the means ($\tfrac{4+6+12}{3} = 7.33$) or summing them — add the **rates**, not the means. *(Back-ref: Entry №03.)*

### Worked Example 17.3 — Agatha's Second-Worst Trial (light guidance; $k$-th order statistic)

**ARCHETYPE:** *Expectation of a general $k$-th order statistic of uniforms (Entry №04).*

**Setup.** Agatha sets four independent ghostly trials, each scored $X_i \sim \Unif(0,1)$. The final drops the best and the worst and reports the **second-worst** ($k=2$). Find its expected value and its density.

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/vs/agatha-gen3.png" alt="Agatha of the Elite Four, the ghost-type specialist" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>Agatha</strong> — third of the Elite Four; her trials test a middle rank.</figcaption>
</figure>

**Identify.** A *specific rank* (second-worst of four) $\to$ the $k$-th order statistic with $k=2$, $n=4$.

Uniform shortcut for the mean:

$$\E[X_{(2)}] = \frac{k}{n+1} = \frac{2}{5} = 0.4.$$

Density via the $k$-th-order formula with $F(x)=x$, $f(x)=1$ (a $\BetaDist(2,3)$):

$$f_{X_{(2)}}(x) = \frac{4!}{1!\,2!}\,x^{1}(1-x)^{2} = 12\,x(1-x)^2, \qquad 0<x<1.$$

**Check & pitfall.** $0.4$ sits below the middle, exactly where the second-lowest of four belongs ✓, and lands between the min's $\tfrac15$ and the max's $\tfrac45$. **Pitfall:** dropping the coefficient $\tfrac{4!}{1!2!}=12$ — the bare $x(1-x)^2$ doesn't integrate to $1$. *(Back-ref: Entry №04.)*

### Worked Example 17.4 — Lance's Redundant Defense (exam speed; reliability)

**ARCHETYPE:** *Series vs parallel reliability $\to$ min vs max (Entry №05).*

**Setup.** Lance's final defense uses three independent shields, each holding (working) with probability $0.95$. Find the defense reliability if the shields are wired (a) **in series** (a breach anywhere drops the whole defense) and (b) **in parallel** (the defense holds while any one shield holds).

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/vs/lance.png" alt="Lance of the Elite Four, the dragon master" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>Lance</strong> — last of the Elite Four; the dragon master and final gate before the Champion.</figcaption>
</figure>

**Identify.** "In series" $\to$ minimum, multiply survivals; "in parallel" $\to$ maximum, $1 -$ product of failures.

$$R_{\text{series}} = 0.95^3 = 0.857, \qquad R_{\text{parallel}} = 1 - 0.05^3 = 1 - 0.000125 = 0.999875.$$

**Check & pitfall.** The parallel (redundant) defense ($\approx0.9999$) beats a single shield ($0.95$), and the series chain ($0.857$) is worse than a single shield — both directions correct ✓. **Pitfall:** swapping the two structures, which would make the "redundant" defense come out *less* reliable. *(Back-ref: Entry №05.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — Max vs. min, in one breath**

Read the verb. **"Strongest / last / longest / parallel"** $\to$ maximum $\to$ raise the **cdf**: $[F(x)]^n$. **"Weakest / first / soonest / series"** $\to$ minimum $\to$ raise the **survival**: $[S(x)]^n$. Get the right function under the power and the rest is mechanical. And it is the cdf/survival *raised to the $n$*, never *multiplied by $n$*.
:::

::: trainers-tip
**TRAINER'S TIP — Uniform order-statistic means for free**

For $n$ i.i.d. $\Unif(0,1)$, $\E[X_{(k)}] = \dfrac{k}{n+1}$: max $= \tfrac{n}{n+1}$, min $= \tfrac{1}{n+1}$, median (odd $n$) $= \tfrac12$. Scale by the interval width for $\Unif(0,b)$. This kills any "expected best / worst / $k$-th of $n$ uniforms" item with no integral.
:::

::: trainers-tip
**TRAINER'S TIP — Exponential race: add rates, not means**

The minimum of independent exponentials is exponential with the **summed rate**. Convert every mean $\theta$ to a rate $1/\theta$, add the rates, and invert once at the end for the minimum's mean. On the TI-30XS, store the rate-sum with **STO▸** before inverting so you don't re-key it. Adding means is the classic wrong move — it makes the race *slower*, which can never be right.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

<figure style="margin:1em auto; max-width:150px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket — Jessie, James, and Meowth" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>Team Rocket</strong> — scheming over the bracket odds again.</figcaption>
</figure>

Jessie has a plan to rig the seeding. "There are *ten* rigged entrants," she announces, "each independently scoring $X_i \sim \Unif(0,1)$. We need the *strongest* of them to come in at or below $0.8$ so our plant draws the top seed. I did the math — the chance is *ten times* the single-draw chance: $P(\max \le 0.8) = 10 \times 0.8 = 8$." James scribbles it down. "Eight hundred percent, boss — a sure thing!" Meowth cheers.

But a probability can never exceed $1$ — and $8$ should have stopped them cold. The maximum's cdf is the single-draw cdf **raised to the $n$th power**, not *multiplied* by $n$:

$$P(\max \le 0.8) = [F(0.8)]^{10} = 0.8^{10} \approx 0.107.$$

The true chance is about **eleven percent**, not a certainty. They staked the whole scheme on an "$800\%$" sure thing, their plant drew a brutal first-round opponent, and the plan collapsed in the opening match.

**Where it fails:** for the maximum, raise the cdf to the $n$ — $[F(x)]^n$ — never scale it by $n$. The instant a "probability" climbs above $1$, you have added or multiplied where you should have taken a power.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

Order statistics do the job no average can. The **maximum** loss governs **catastrophe layers** and **excess-of-loss reinsurance** — a treaty that pays only on the *single largest* claim above a retention is priced directly off $F_{\max}(x) = [F(x)]^n$, the distribution of the biggest of many independent losses. The **minimum** lifetime is exactly a **series-system failure** in reliability engineering, and the min-of-exponentials rate-sum is how engineers combine independent failure hazards into one system hazard. The general $k$-th order statistic underlies trimmed estimators and percentile-based risk measures (a $95$th-percentile loss is an order statistic of the loss sample).

*Series bridge:* order statistics and reliability reappear throughout **STAM / Exam 5** severity and large-loss modeling, and the extreme-value tail work seeds the heavy-tail methods of the loss-models exams. Every "what is the worst we should plan for?" question an insurer asks is, underneath, a maximum.

*Transfer check:* could you solve this with **no Pokémon in it**? "A reinsurer covers the single largest of $n = 50$ independent losses, each $\Unif(0, 1\text{M})$; find the expected largest loss." Same shortcut: $\tfrac{n}{n+1}\cdot b = \tfrac{50}{51}\cdot 1\text{M} \approx 980{,}000$. If you can do that, the skill has transferred.
:::

## The Gym Battle — the Elite Four Bracket Capstone

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/vs/lance.png" alt="Lance of the Elite Four, the final gate before the Champion's chamber" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Lance — the final gate before the Champion's chamber</figcaption>
</figure>

**Lance's Challenge.** Lance, the last member of the Elite Four, blocks the door to the Champion's chamber. "Numbers won you the badges," he says. "Let's see if they get you past me." He lays out the League's master file: $n = 144$ challengers in the open bracket, each with strength $X_i$ independent and **Uniform on $[0,100]$**. He fires five questions in sequence:

> (a) the expected strength of the **strongest** challenger; (b) the probability the strongest's strength is **below $95$**; (c) the expected strength of the **weakest** challenger; (d) his chamber gate has a pair of independent locks, each tripping after an $\Expo(\text{mean }10\text{ min})$ delay, and the gate opens when the **faster** lock trips — give the expected time until it opens, and reconcile it as a minimum; (e) his three-shield defense (each shield independently holds w.p. $0.9$) — give the reliability **in series** and **in parallel**.

**ARCHETYPE:** *Integrative — maximum, minimum, uniform order-statistic means, min-of-exponentials, and series/parallel reliability.*

**Step 1 — Identify.** Parts (a)–(c) are order statistics of i.i.d. uniforms (Entries №01, №02, №04); (d) is the minimum of independent exponentials (Entry №03); (e) is series/parallel reliability (Entry №05).

**Step 2 — Trainer's Path.**

*(a) Strongest, expected.* Max of $144$ uniforms on $[0,100]$:
$$\E[X_{(144)}] = \frac{n}{n+1}\cdot 100 = \frac{144}{145}\cdot 100 \approx 99.31.$$

*(b) Strongest below $95$.* $F_{\max}(x) = (x/100)^{144}$, so
$$P(X_{(144)} < 95) = 0.95^{144} \approx 0.00062.$$
The strongest of $144$ is essentially never below $95$ — about a $0.06\%$ chance.

*(c) Weakest, expected.* Min of $144$ uniforms on $[0,100]$:
$$\E[X_{(1)}] = \frac{1}{n+1}\cdot 100 = \frac{100}{145} \approx 0.69.$$

*(d) The gate — the twist.* The gate opens when the **faster** lock trips — the *minimum* of the two delays. Two independent $\Expo(\text{mean }10)$ delays have rate $\tfrac1{10}$ each; the minimum has rate $\tfrac1{10} + \tfrac1{10} = \tfrac15$, so
$$\E[\text{gate opens}] = \frac{1}{1/5} = 5 \text{ minutes}.$$
Equivalently, $n$ i.i.d. exponentials with mean $\theta$ have minimum-mean $\theta/n = 10/2 = 5$. ✓

*(e) The shields.* Three independent shields at $0.9$:
$$R_{\text{series}} = 0.9^3 = 0.729, \qquad R_{\text{parallel}} = 1 - 0.1^3 = 0.999.$$

**Step 3 — Professor's Path (part (c), exact integral).** Confirm the uniform-min mean from the min density $f_{\min}(x) = n[S(x)]^{n-1}f(x)$ with $S(x) = 1 - x/100$, $f(x) = 1/100$:
$$\E[X_{(1)}] = \int_0^{100} x\cdot 144\Big(1 - \tfrac{x}{100}\Big)^{143}\tfrac{1}{100}\,dx \overset{u = x/100}{=} 100\int_0^1 u\cdot 144(1-u)^{143}\,du = 100\cdot\frac{1}{145} = \frac{100}{145} \approx 0.69,$$
the $\BetaDist(1,144)$ mean — matching the shortcut.

**Step 4 — Check, verdict & the pitfall Lance is testing.** Every probability lands in $[0,1]$; the strongest of $144$ ($\approx 99.3$) hugs the ceiling and the weakest ($\approx 0.69$) hugs the floor, as they must; the parallel defense ($0.999$) beats the series chain ($0.729$). **Pitfall:** part (d)'s wording — "two locks" tempts a *max*, but the gate opens at the *first* success, which is a **minimum**. Always map the *verb* ("opens when the faster trips") to the order statistic, not the physical layout. Lance nods and steps aside.

> "That," Lance says, "is how you read the extremes. You found the strongest, the weakest, and the first — and you never let a word trick you into the wrong tail. The Champion's chamber is yours."

## The Gym Challenge — Problem Set

::: problem-set
**TEST-OUT INSTRUCTIONS.** Work this set timed (~6 min/problem), then check the **Answers** below. Hit the mastery bar (**80%+ with correct method**) and you may move on. Problems are listed first; full worked solutions follow afterward (never interleaved). Markers: 🔴 Poké Ball = routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (mechanics)

**C17.1.** 🔴 Five rookies each post an independent score $X_i \sim \Unif(0,1)$. The scout flags the *highest*. Find $P(\text{highest} \le 0.8)$.

**C17.2.** 🔴 Three Pokémon hold a line; their independent break-times are exponential, each with mean $10$ seconds. The line collapses when the *first* breaks. Find the expected time to collapse.

**C17.3.** 🔴 Four sensor pods each report $X_i$ with cdf $F(x) = x^2$ on $[0,1]$, independently. The panel shows the *maximum*. Find $P(\text{max} \le 0.5)$.

**C17.4.** 🔴 Nine independent qualifiers each have strength $X_i \sim \Unif(0,20)$. Find the expected strength of the *strongest* using the uniform shortcut.

**C17.5.** 🟡 A field log states "for $5$ i.i.d. $\Unif(0,1)$ rookies, $P(\max \le 0.8) = 5 \times 0.8 = 4$." Find the true probability and name the error.

**C17.6.** 🔴 A relay has three independent components, each working w.p. $0.9$. Find the reliability (i) *in series* and (ii) *in parallel*.

**C17.7.** 🟡 Two challengers each have strength $X_i \sim \Unif(0,1)$. The *weaker* goes to consolation. Find the expected strength of the weaker challenger and the density of that minimum.

### Gym Battles (true SOA difficulty)

**C17.8.** 🟡 Agatha sets three independent ghostly trials, each scored $X_i \sim \Unif(0,1)$. Find (i) the expected *best* score and (ii) $P(\text{best} > 0.9)$.

**C17.9.** 🟡 Two of Lorelei's Pokémon thaw at independent exponential times with means $5$ and $8$ minutes. The combo fires when the *first* thaws. Find (i) the distribution of the first-thaw time, (ii) its mean, and (iii) $P(\text{first} > 3)$.

**C17.10.** 🟡 Four judges independently score $X_i \sim \Unif(0,1)$; the final drops the lowest and uses the *second-lowest* ($k=2$). Find its expected value and its density.

**C17.11.** 🟡 Gary boasts about a $6$-entrant bracket of i.i.d. $\Unif(0,1)$ strengths: "the strongest is below $0.5$ with chance $6 \times 0.5 = 3$." Find the true $P(\max < 0.5)$ and name Gary's error.

**C17.12.** 🟡 Bruno's chamber has four independent locks, each $\Expo(\text{mean }8\text{ min})$. The gate opens at the *first* trip. Find the distribution and mean of the opening time, and $P(\text{open} > 4)$.

**C17.13.** 🔵 Three backup generators have independent exponential lifetimes, each mean $10$ years. The bunker keeps power until the *last* dies (parallel). Find the expected time to blackout. *(Hint: $\E[\max]$ of $n$ i.i.d. exponentials with mean $\theta$ is $\theta\sum_{j=1}^{n}\tfrac1j$.)*

**C17.14.** 🟡 Lance wires three shields with reliabilities $0.95$, $0.90$, and $0.80$. Find the system reliability (i) *in series* and (ii) *in parallel*.

### Elite Challenge (integrative / stretch)

**C17.15.** 🔵 Ten finalists each post an independent $X_i \sim \Unif(0,1)$. The League reports the **range** — the gap between strongest and weakest. Find $\E[X_{(10)} - X_{(1)}]$.

**C17.16.** 🔵 Gary, picking his squad, declares "of my $3$ Pokémon (independent exponential faint-times, means $4, 6, 12$ min), the *first* to faint averages the mean of the means, $\tfrac{4+6+12}{3} = 7.33$ minutes." Find the true expected first-faint time and name his error.

**C17.17.** 🔵 *(Integrative.)* The Champion's defense is a series chain of two blocks. Block A is a *parallel* bank of two shields, each holding w.p. $0.9$. Block B is a single shield holding w.p. $0.95$. The defense holds only if **both blocks** hold. Find (i) Block A's reliability, (ii) the whole defense's reliability, and (iii) the expected time to the first failure if instead the two Block-A shields and the Block-B shield were three independent $\Expo(\text{mean }10\text{ yr})$ components all wired *in series*.
:::

## Answers

### Quick-Answer Table

| # | Answer | Archetype | | # | Answer | Archetype |
|---|---|---|---|---|---|---|
| C17.1 | $0.8^5 \approx 0.328$ | order_statistic (max) | | C17.10 | $0.4$; $f=12x(1-x)^2$ | order_statistic ($k$-th) |
| C17.2 | $10/3 \approx 3.33$ s | order_statistic (min) | | C17.11 | $0.5^6 \approx 0.0156$ | rival_trap |
| C17.3 | $0.5^8 \approx 0.0039$ | order_statistic (max) | | C17.12 | $\Expo(\tfrac12)$, mean $2$, $0.135$ | exponential (min) |
| C17.4 | $18$ | order_statistic (max) | | C17.13 | $\approx 18.33$ yr | order_statistic (max) |
| C17.5 | $0.8^5 \approx 0.328$ | audit | | C17.14 | series $0.684$, parallel $0.999$ | reliability |
| C17.6 | series $0.729$, parallel $0.999$ | reliability | | C17.15 | $9/11 \approx 0.818$ | order_statistic (range) |
| C17.7 | $\E=1/3$, $f=2(1-x)$ | order_statistic (min) | | C17.16 | $2$ min | rival_trap |
| C17.8 | $\E=0.75$, $P=0.271$ | order_statistic (max) | | C17.17 | $0.99$; $0.9405$; $\Expo(\tfrac{3}{10})$, mean $3.33$ yr | reliability |
| C17.9 | $\Expo(0.325)$, mean $\approx 3.08$, $0.377$ | exponential (min) | | | | |

**C17.1** — *cdf of a maximum (Entry №01).* $F_{\max}(x) = x^5$ on $[0,1]$, so $P(\max \le 0.8) = 0.8^5 = 0.32768 \approx \mathbf{0.328}$.

**C17.2** — *minimum of i.i.d. exponentials (Entry №03).* Three rate-$\tfrac1{10}$ clocks; minimum rate $= \tfrac{3}{10}$, mean $= \tfrac{10}{3} \approx \mathbf{3.33}$ s.

**C17.3** — *cdf of a maximum (Entry №01).* $F_{\max}(x) = (x^2)^4 = x^8$, so $P(\max \le 0.5) = 0.5^8 = \tfrac{1}{256} \approx \mathbf{0.0039}$.

**C17.4** — *expected max of i.i.d. uniforms (Entry №01 shortcut).* $\E[\max] = \tfrac{n}{n+1}b = \tfrac{9}{10}\cdot 20 = \mathbf{18}$.

**C17.5** — *audit; the canonical $[F]^n$-vs-$nF$ error (Entry №01).* The recorder multiplied the cdf by $n$ instead of raising it to the $n$ — and $4$ isn't even a valid probability, the instant tell. The truth is $P(\max \le 0.8) = 0.8^5 = \mathbf{0.328}$. **It is $[F]^n$, never $nF$.**

**C17.6** — *reliability ↔ order statistics (Entry №05).* (i) Series: $0.9^3 = \mathbf{0.729}$. (ii) Parallel: $1 - 0.1^3 = \mathbf{0.999}$.

**C17.7** — *minimum of i.i.d. uniforms, mean and density (Entries №02, №04).* $\E[\min] = \tfrac{1}{n+1} = \tfrac13 \approx \mathbf{0.333}$. Density $f_{\min}(x) = n[1-x]^{n-1} = \mathbf{2(1-x)}$ on $[0,1]$.

**C17.8** — *max of i.i.d. uniforms, mean and tail (Entry №01).* (i) $\E[\max] = \tfrac{3}{4} = \mathbf{0.75}$. (ii) $P(\max > 0.9) = 1 - 0.9^3 = \mathbf{0.271}$.

**C17.9** — *minimum of independent exponentials (Entry №03).* Rates $\tfrac15, \tfrac18$; sum $= \tfrac{13}{40} = 0.325$. (i) First-thaw $\sim \Expo(0.325)$. (ii) mean $= \tfrac{1}{0.325} = \tfrac{40}{13} \approx \mathbf{3.08}$ min. (iii) $P(\min > 3) = e^{-0.325\cdot 3} = e^{-0.975} \approx \mathbf{0.377}$.

**C17.10** — *general $k$-th order statistic of uniforms (Entry №04).* $\E[X_{(2)}] = \tfrac{k}{n+1} = \tfrac{2}{5} = \mathbf{0.4}$. Density $f_{X_{(2)}}(x) = \tfrac{4!}{1!\,2!}x(1-x)^2 = \mathbf{12x(1-x)^2}$ on $(0,1)$.

**C17.11** — *rival_trap; the $[F]^n$-vs-$nF$ error (Entry №01).* Gary multiplied by $n$; $3$ exceeds $1$, the instant tell. The truth raises the cdf to the $n$: $P(\max < 0.5) = 0.5^6 = \tfrac{1}{64} \approx \mathbf{0.0156}$. **Cdfs of independent draws multiply (a power), never scale by $n$.**

**C17.12** — *minimum of i.i.d. exponentials (Entry №03).* Four rate-$\tfrac18$ locks; minimum rate $= \tfrac{4}{8} = \tfrac12$, so $\Expo(\tfrac12)$, **mean $= 2$ min**. $P(\text{open} > 4) = e^{-\frac12\cdot 4} = e^{-2} \approx \mathbf{0.135}$.

**C17.13** — *expected max of i.i.d. exponentials, harmonic sum (Entries №01, №05).* $\E[\max] = \theta\sum_{j=1}^{3}\tfrac1j = 10\big(1 + \tfrac12 + \tfrac13\big) = 10\cdot\tfrac{11}{6} = \tfrac{110}{6} \approx \mathbf{18.33}$ years.

**C17.14** — *unequal-component reliability (Entry №05).* (i) Series: $0.95\cdot0.90\cdot0.80 = \mathbf{0.684}$. (ii) Parallel: $1 - (0.05)(0.10)(0.20) = 1 - 0.001 = \mathbf{0.999}$.

**C17.15** — *expected range via order-statistic means (Entries №01, №02).* For $n$ i.i.d. $\Unif(0,1)$, $\E[X_{(n)}] = \tfrac{n}{n+1}$ and $\E[X_{(1)}] = \tfrac{1}{n+1}$, so $\E[\text{range}] = \tfrac{n-1}{n+1} = \tfrac{9}{11} \approx \mathbf{0.818}$.

**C17.16** — *rival_trap; min of exponentials, add rates not means (Entry №03).* Convert means $4,6,12$ to rates $\tfrac14,\tfrac16,\tfrac1{12}$; sum $=\tfrac12$; the first faint is $\Expo(\tfrac12)$, **mean $= 2$ minutes** — below the smallest individual mean, as a race must be. Gary averaged the *means*; you add the *rates*.

**C17.17** — *integrative reliability (Entry №05).* (i) Block A (parallel of two at $0.9$): $R_A = 1 - 0.1^2 = \mathbf{0.99}$. (ii) Series of Block A and Block B: $R = R_A\cdot R_B = 0.99\cdot 0.95 = \mathbf{0.9405}$. (iii) Three independent $\Expo(\text{mean }10)$ in series $\to$ minimum $\to$ rates add: $\tfrac1{10}+\tfrac1{10}+\tfrac1{10} = \tfrac{3}{10}$, so $\Expo(\tfrac{3}{10})$, **mean $= \tfrac{10}{3} \approx 3.33$ yr**.

## Badge Earned — League Bracket Cleared

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with the Indigo Plateau reached and the Elite Four bracket cleared; the Champion's chamber lies just beyond." style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Elite Four Bracket — order statistics cleared.</strong> No badge is handed out at the League; you earn the right to face the Champion.</figcaption>
</figure>

There is no ninth badge — this is the League. You earn the right to face the Champion when you can, unaided:

**Mastery checklist — tick each before you move on (mapped 1-to-1 to the SOA outcome 3f):**

- ☐ **(3f)** I can **derive and use** the cdf, density, and expectation of the **maximum** ($[F(x)]^n$) and **minimum** ($[S(x)]^n$) of $n$ independent draws, and I know it is a *power*, never $n\cdot F$. *(Rematch: Concepts 1–2, WE 17.1, Problems C17.1, C17.3, C17.4, C17.7, C17.8.)*
- ☐ **(3f)** I can **recognize the minimum of independent exponentials** as exponential with the **summed rate**, find its mean ($1/\sum\lambda_i$) and tail. *(Rematch: Concept 3, WE 17.2, Problems C17.2, C17.9, C17.12, C17.16.)*
- ☐ **(3f)** I can **write the general $k$-th-order density** and use the uniform mean $\tfrac{k}{n+1}$ for medians, second-bests, second-worsts, and ranges. *(Rematch: Concept 4, WE 17.3, Problems C17.10, C17.15.)*
- ☐ **(3f)** I can **map series/parallel reliability** to minimum/maximum and compute each, sanity-checking by direction (redundancy raises reliability). *(Rematch: Concept 5, WE 17.4, Problems C17.6, C17.14, C17.17.)*

> **Gym rematch pointers (🧴 Potion).** Miss item 1 $\to$ re-read Concepts 1–2 + WE 17.1, then C17.1/C17.4. Miss item 2 $\to$ Concept 3 + WE 17.2 + C17.9/C17.12. Miss item 3 $\to$ Concept 4 + WE 17.3 + C17.10/C17.15. Miss item 4 $\to$ Concept 5 + WE 17.4 + C17.6/C17.14/C17.17. Caught by the $[F]^n$-vs-$nF$ trap? Re-run the Team Rocket trap, then C17.5 and C17.11.

*Onward — one gate remains. Beyond this door, the Champion waits, and everything you have built across seventeen content chapters meets its final test.*

---

<!-- ===== CALLOUT BOX TEMPLATES (Pandoc fenced divs; styled by book/theme.css) =====
     ::: cold-open / pokedex-entry / trainers-tip / team-rocket / kanto-realworld
     Concept gate ("Do you already own this?") also uses a styled panel.
     Wrap the problem set in ::: problem-set and the answers in ## Answers . -->

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
