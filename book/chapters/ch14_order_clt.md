<!--
  file: ch14_order_clt
  tier: A
  outcomes: 3f,3i
  draft1_source: drafts/chapters_draft1/ch12_indigo_plateau.md
  maps_to: Indigo Plateau approach — order stats & CLT
-->

# Order From Chaos {.type-psychic}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with the journey now at the Indigo Plateau, beyond Victory Road at the northwest of the region; all eight badges collected." style="width:78%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 10 — beyond Victory Road, the Indigo Plateau, where the League field converges and the last two ideas of your journey wait: the <em>extreme</em> and the <em>aggregate</em>.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Field of Champions"**

The doors of the Indigo Plateau stadium swing open and the noise hits you like a wave. Below, on the registration floor, a thousand trainers are checking in — the largest League field in years. You've earned all eight badges; now you're one face in a sea of them, Pikachu tense on your shoulder.

The League treasurer, a harried woman with a clipboard, spots your Pokédex's glowing Actuary Mode and waves you over. "You — you do the risk math, right? I have two problems and the opening ceremony is in an hour."

"First," she says, "the seeding committee wants to know how strong the *single toughest challenger* in the bracket is likely to be. Not the average trainer — the *maximum*. We know the strength of a typical entrant. Out of all those draws, how strong is the strongest one going to be?"

She flips a page. "Second — and this is the one that keeps me up at night — the prize pool. Every match pays out a random purse. We're running a hundred matches. Each purse averages five hundred Poké-dollars but swings wildly. The League budgeted fifty-two thousand. What's the chance we blow through it?" She taps the figure. "I can't simulate a thousand brackets by hand. I need a *number*, and I need it before that ceremony."

Pikachu looks up at you. You realize the two questions are secretly the same *kind* of question — both ask what happens when you take *many* independent draws and look at either the **extreme** or the **aggregate**. The strongest challenger is a maximum over a huge field. The total payout is a sum over a hundred purses. You have priced single random variables all journey long. You have never had a tool for the *largest* of many, or the *total* of many.

The treasurer's pen hovers. **How strong is the strongest of a thousand, and how do you find the chance a sum of a hundred random purses overruns a fixed budget — without simulating anything?**
:::

## Where You Are — 60-Second Retrieval

Eight badges sit in your case. The last few chapters armed you with everything this one needs. From **Chapter 7** you carry the **cdf** $F(x) = P(X \le x)$ — "the chance $X$ lands at or below $x$" — and its mirror the **survival function** $S(x) = P(X > x) = 1 - F(x)$ — "the chance $X$ exceeds $x$." From **Chapter 5** you carry **independence**: independent events *multiply*, $P(A \cap B) = P(A)\,P(B)$. From **Chapter 13** you carry the mean and variance of a **sum**: for independent draws, **variances add**.

That is the entire foundation. The maximum and minimum of many draws are built by *multiplying* cdfs and survival functions (independence). The Central Limit Theorem is built on the mean and variance of a *sum*. Take sixty seconds and prove you still own these three before reading on.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the tools this chapter stands on**

Answer from memory; if any feels shaky, flip back before continuing.

1. If $F(x) = P(X \le x)$, what is $P(X > x)$ in terms of $F$? *(Answer: $S(x) = 1 - F(x)$, the survival function.)*
2. Two independent circuits work w.p. $0.9$ and $0.8$. What is $P(\text{both work})$? *(Answer: $0.9 \times 0.8 = 0.72$ — independent events multiply.)*
3. $X$ and $Y$ are independent with $\Var(X) = \Var(Y) = 4$. What is $\Var(X+Y)$? *(Answer: $4 + 4 = 8$ — independent variances add.)*
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice crackles through the Pokédex as you step onto the stadium floor. "Ash — this is the last content chapter of your journey, and it has two ideas that *feel* unrelated but share one root: **what happens when independence piles up.** Order statistics tell you about the **extremes** — the best and worst of many draws. The Central Limit Theorem tells you about the **aggregate** — the sum and the average of many draws. Master both and you can price the strongest opponent and the riskiest payout pool with nothing but a survival function and the standard normal table. Take it slowly. This is where the whole syllabus comes together."

By the end of this chapter you will be able to:

- **Derive and use** the distribution of the **maximum** and **minimum** of $n$ independent draws — $F_{\max}(x) = [F(x)]^n$ and $S_{\min}(x) = [S(x)]^n$ — including their densities and expectations. *(Outcome 3f.)*
- **Find** the density and expectation of a **general $k$-th order statistic**, recognize the **minimum of independent exponentials** as exponential with the summed rate, and **map** *series* and *parallel* **system reliability** to min and max. *(Outcome 3f.)*
- **Apply** the **Central Limit Theorem**: standardize a sum or mean of i.i.d. draws to the normal and read the probability off the table. *(Outcome 3i.)*
- **Deploy** the **continuity correction** when a *discrete* sum (binomial, Poisson) is approximated by the normal. *(Outcome 3i.)*

> *Exam-weight signpost.* The CLT (with continuity correction) is a **Tier A**, frequently tested idea — nearly every exam has a "sum/average of many, find the probability" item. Order statistics are **Tier B**, but the max/min mechanics are quick points once the one derivation clicks. This chapter earns the full treatment.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own the Indigo Plateau?**

Already fluent? Prove it. Work these four with *correct method*:

1. Eight independent qualifiers each have strength $X_i \sim \Unif(0,30)$. Find $\E[\max]$ and $P(\max > 27)$.
2. Three independent exponential clocks have means $4, 6, 12$ minutes. Find the mean of the *first* to ring and $P(\text{first} > 3)$.
3. A sum of $100$ i.i.d. purses, each mean $500$, SD $150$. Approximate $P(\text{sum} > 52{,}000)$.
4. $X \sim \Binom(400, 0.4)$. Using the normal approximation **with continuity correction**, approximate $P(X \ge 180)$.

*(Answers: $\E[\max] = \tfrac{8}{9}\cdot 30 = 26.\overline{6}$ and $1 - 0.9^8 \approx 0.570$; rates add to $\tfrac12$, mean $2$, $e^{-1.5} \approx 0.223$; $z = 1.33$, $\approx 0.091$; $z = \tfrac{179.5-160}{\sqrt{96}} \approx 1.99$, $\approx 0.023$.)* Four for four with the right reasoning? **Skip to the Gym Challenge** and claim the badge. Any miss or hesitation? The teaching below was built exactly for you — and each concept has its own skip-gate, so a partial owner loses no time.
:::

---

Throughout, suppose $X_1, X_2, \dots, X_n$ are **independent and identically distributed** — "**i.i.d.**," read aloud *"independent, all from the same distribution"* — with common cdf $F(x)$ and survival function $S(x) = 1 - F(x)$. We teach five ideas, in increasing difficulty, each with its own skip-check and its own Pokédex Entry:

1. **The maximum** — the strongest of many *(the foundational order-statistic derivation)*
2. **The minimum** — the weakest of many, and the exponential race
3. **The general $k$-th order statistic** — any rank, plus series/parallel reliability
4. **The Central Limit Theorem** — the sum and average go normal *(the crown jewel)*
5. **The continuity correction** — the half-unit fix for discrete sums

## Concept 1 — The Maximum: Strongest of the Field

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Maximum**

Five independent rookies each score $X_i \sim \Unif(0,1)$. The scout flags the highest score. What is $P(\text{highest} \le 0.8)$?

If you instantly answered **$0.8^5 = 0.32768$** — and can say *why it is the single-draw cdf raised to the fifth power* — **skip to Concept 2**. If you wrote $0.8$, or you're unsure where the exponent comes from, this section is for you.
:::

**Beat 1 — The one-sentence idea.** *The largest of $n$ independent draws is at most $x$ exactly when **every** draw is at most $x$ — so you raise the single-draw cdf to the $n$-th power.*

**Beat 2 — Anchor + concrete instance.** Recall the cdf $F(x) = P(X \le x)$ from Chapter 7 and the multiplying-independence rule from Chapter 5. The maximum just stacks them together. Here is the story, with real numbers.

The seeding committee hands you the file on $n = 3$ regional qualifiers (we keep it small enough to picture; the thousand comes later). Each qualifier's strength $X_i$ is independent and **Uniform on $[0,1]$**, so the single-draw cdf is $F(x) = P(X_i \le x) = x$ on $[0,1]$. The top seed must face the **strongest** of the three. *What is the chance the strongest of the three scores at most $0.8$?*

**Beat 3 — Reason through it in plain words.** Call the maximum $M$. When is the *strongest* of the three at most $0.8$? Only when *all three* are at most $0.8$ — if even one qualifier scored above $0.8$, the maximum would exceed $0.8$. So "the max is $\le 0.8$" is the *same event* as "draw 1 is $\le 0.8$ **and** draw 2 is $\le 0.8$ **and** draw 3 is $\le 0.8$." Because the three draws are independent, those three chances multiply:

$$P(M \le 0.8) = \underbrace{P(X_1 \le 0.8)}_{0.8} \cdot \underbrace{P(X_2 \le 0.8)}_{0.8} \cdot \underbrace{P(X_3 \le 0.8)}_{0.8} = 0.8^3 = 0.512.$$

The exponent $3$ is *not* decoration — it is one factor of $0.8$ for each independent draw that has to fall in line.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The natural mistake is to report the single-draw chance:

$$P(M \le 0.8) \overset{?}{=} 0.8. \qquad\textbf{(wrong)}$$

But $0.8$ is the chance *one* draw is at most $0.8$. The maximum being small is a *much* stronger demand — *all three* must cooperate, and asking three independent things to all happen makes the probability *smaller*, not the same. ($0.512 < 0.8$, exactly as it must be.) The deeper version of this error shows up at the other end: people report the population mean for the strongest of a crowd. The strongest of many is far *above* the typical draw — never confuse "a draw" with "the biggest draw."

**Beat 5 — Translate into notation, one glyph at a time.** The maximum is the **$n$-th order statistic**, written

$$X_{(n)} \qquad \text{read aloud: ``}X\text{ sub-paren-}n\text{,'' the largest of the }n\text{ draws.}$$

The parentheses around the subscript are the tell: $X_{(n)}$ means *"the value that lands in position $n$ after sorting,"* not "the $n$-th draw you happened to make." We name its cdf $F_{\max}(x) = P(X_{(n)} \le x)$. Translating Beat 3's plain reasoning — "the max is $\le x$ iff every draw is $\le x$, and independent chances multiply" — into symbols:

$$F_{\max}(x) = P(X_1 \le x,\, X_2 \le x,\, \dots,\, X_n \le x) = \prod_{i=1}^{n} P(X_i \le x) = [F(x)]^n.$$

The product sign $\prod$ reads *"the product of"* — multiply these together (the multiplicative cousin of the summation $\sum$). Because the draws are identically distributed, every factor is the same $F(x)$, and the product collapses to $[F(x)]^n$.

**Beat 6 — Generalize: derive the formula from the instance.** We did not assert $[F(x)]^n$ — we built it: "all $n$ at most $x$" is an intersection of independent events, so its probability is the product of $n$ identical factors $F(x)$. To get the **density**, differentiate the cdf (the chain rule from Chapter 7), since the density is the derivative of the cdf:

$$\boxed{\,F_{\max}(x) = [F(x)]^n, \qquad f_{\max}(x) = \frac{d}{dx}[F(x)]^n = n\,[F(x)]^{n-1}\,f(x).\,}$$

The factor $n[F(x)]^{n-1}$ comes from the power rule; the trailing $f(x)$ is the inner derivative $F'(x) = f(x)$.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* read $F$, raise to the $n$. For our three uniforms, $P(M \le 0.8) = 0.8^3 = 0.512$.
- *A twist — the tail.* "At least one above the bar" is the *complement* of the max being below it: $P(M > x) = 1 - [F(x)]^n$. For three uniforms, $P(M > 0.9) = 1 - 0.9^3 = 0.271$.
- *General — the expectation.* For $n$ i.i.d. $\Unif(0,1)$ the mean of the max is $\dfrac{n}{n+1}$ (derived in the Entry below); on $\Unif(0,b)$ it scales to $\dfrac{n}{n+1}\,b$. For our three uniforms, $\E[M] = \tfrac34$. Notice it climbs toward the ceiling as $n$ grows — the bigger the field, the closer the strongest sits to the top.
- *Boundary:* with $n = 1$ the formula gives $F_{\max} = F$ and $\E[M] = \tfrac{1}{2}b$ — one draw *is* its own maximum. Sanity holds.

**Beat 8 — Picture it.** The figure shows *why* the density of the max piles up near the top: with more draws, it becomes ever more likely that *at least one* lands high, dragging the maximum toward the ceiling.

<figure>
<img src="../../assets/diagrams/ch14_max_density.png" alt="Three density curves of the maximum of n i.i.d. Uniform(0,1) draws, for n=1 (flat line at height 1), n=3 (rising curve 3x^2), and n=8 (sharply rising curve 8x^7), all on [0,1]. As n grows the density's mass shifts hard toward x=1, and a dashed vertical line marks the mean n/(n+1) creeping toward 1." style="width:80%; max-width:560px; display:block; margin:1em auto;">
<figcaption>Density of the maximum of $n$ i.i.d. $\Unif(0,1)$ draws: $f_{\max}(x) = n x^{n-1}$. As the field grows, the strongest is almost certainly near the ceiling; the mean $\tfrac{n}{n+1}$ creeps toward $1$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now take any "the strongest / highest / longest-lasting / last to fail of $n$ independent draws" and write its cdf ($[F(x)]^n$), its density ($n[F(x)]^{n-1}f(x)$), and — for uniforms — its mean ($\tfrac{n}{n+1}b$) without grinding an integral.

::: pokedex-entry
**POKÉDEX ENTRY №01 — The Maximum (the $n$-th order statistic)**

For i.i.d. $X_1, \dots, X_n$ with cdf $F$, the maximum $M = X_{(n)} = \max_i X_i$ has
$$F_{\max}(x) = [F(x)]^n, \qquad f_{\max}(x) = n\,[F(x)]^{n-1}\,f(x).$$
For $n$ i.i.d. $\Unif(0,b)$: $\;\E[\max] = \dfrac{n}{n+1}\,b$. *(Derivation: $\E[M] = \int_0^b x \cdot n(x/b)^{n-1}\tfrac1b\,dx = \tfrac{n}{n+1}b$.)*

*In plain terms:* the largest value is at most $x$ exactly when **every** draw is at most $x$ — independent events multiply, so raise the single-draw cdf to the $n$-th power.

*Recognition cue:* **"strongest," "highest," "longest-lasting," "last to fail,"** or a *parallel* system $\to$ reach for $[F(x)]^n$.
:::

## Concept 2 — The Minimum: Weakest of the Field, and the Exponential Race

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Minimum**

Three independent exponential clocks have means $4$, $6$, and $12$ minutes. Find the mean time until the *first* one rings.

If you answered **$2$ minutes** — by adding the *rates* $\tfrac14 + \tfrac16 + \tfrac1{12} = \tfrac12$ and inverting — **skip to Concept 3**. If you averaged the means to $7.\overline{3}$, or summed them, read on: the minimum is governed by the *survival* function, and exponentials race in a special way.
:::

**Beat 1 — The one-sentence idea.** *The smallest of $n$ independent draws exceeds $x$ exactly when **every** draw exceeds $x$ — so you raise the single-draw **survival** function to the $n$-th power.*

**Beat 2 — Anchor + concrete instance.** This is Concept 1's mirror image. There, "max $\le x$" meant *all* below $x$, multiplying cdfs. Here, "min $> x$" means *all* above $x$, multiplying **survival** functions $S(x) = 1 - F(x)$.

Three of your Pokémon hold a defensive line. Their independent times-until-they-break are exponential. For the warm-up, take them **i.i.d. exponential with mean $10$ seconds** each (rate $\lambda = \tfrac1{10}$, so $S(x) = e^{-x/10}$). The line collapses the instant the *first* one breaks. *What is the chance the line survives past $x = 5$ seconds?*

**Beat 3 — Reason through it in plain words.** Call the minimum $m$. When does the *first to break* hold out past $5$ seconds? Only when *all three* hold out past $5$ — if any single one breaks earlier, the line is already down. So "the min $> 5$" is the same event as "draw 1 $> 5$ **and** draw 2 $> 5$ **and** draw 3 $> 5$," and independence multiplies:

$$P(m > 5) = \big[S(5)\big]^3 = \big(e^{-5/10}\big)^3 = e^{-15/10} = e^{-1.5} \approx 0.223.$$

One survival factor per independent draw that must hold out.

**Beat 4 — Surface and dismantle the tempting wrong idea.** When the draws are exponential, the seductive error is to handle the *minimum* by averaging or summing the *means*:

$$\E[\text{first to ring}] \overset{?}{=} \frac{4 + 6 + 12}{3} = 7.\overline{3} \quad\text{or}\quad 4+6+12 = 22. \qquad\textbf{(both wrong)}$$

But a *race* finishes *faster* than any single runner — the first of several clocks rings *sooner* than the average clock, not later, and certainly not as slow as the sum. The fix is the survival-function rule plus one exponential fact you will derive in Beat 6: for exponentials, **the rates add, not the means.** Adding rates makes the combined clock *faster* (shorter mean), exactly as a race should be.

**Beat 5 — Translate into notation, one glyph at a time.** The minimum is the **first order statistic**,

$$X_{(1)} \qquad \text{read aloud: ``}X\text{ sub-paren-one,'' the smallest of the }n\text{ draws.}$$

Translating Beat 3 — "the min $> x$ iff every draw $> x$, multiply" — into symbols, naming the minimum's survival function $S_{\min}(x) = P(X_{(1)} > x)$:

$$S_{\min}(x) = P(X_1 > x,\, \dots,\, X_n > x) = \prod_{i=1}^{n} P(X_i > x) = [S(x)]^n.$$

Its cdf is the complement, $F_{\min}(x) = 1 - [S(x)]^n$, and differentiating gives the density.

**Beat 6 — Generalize: derive both the general formula and the exponential shortcut.** The general min, derived just like the max but from survival functions:

$$\boxed{\,S_{\min}(x) = [S(x)]^n, \qquad F_{\min}(x) = 1 - [S(x)]^n, \qquad f_{\min}(x) = n\,[S(x)]^{n-1}\,f(x).\,}$$

Now the exponential special case — the *one to memorize*. If $X_i \sim \Expo(\text{rate }\lambda_i)$ independently, then $S_i(x) = e^{-\lambda_i x}$, and the minimum's survival is the product:

$$S_{\min}(x) = \prod_{i=1}^{n} e^{-\lambda_i x} = e^{-(\lambda_1 + \cdots + \lambda_n)\,x}.$$

That is *exactly* the survival function of one exponential with rate $\sum_i \lambda_i$. So **the minimum of independent exponentials is itself exponential, with rate equal to the sum of the rates** — the hazards stack. For $n$ i.i.d. exponentials each with mean $\theta$ (rate $1/\theta$), the minimum is exponential with rate $n/\theta$, hence mean $\theta/n$.

Back to the gate's three clocks, means $4, 6, 12 \Rightarrow$ rates $\tfrac14, \tfrac16, \tfrac1{12}$:

$$\lambda_{\min} = \tfrac14 + \tfrac16 + \tfrac1{12} = \tfrac{3+2+1}{12} = \tfrac{6}{12} = \tfrac12 \;\Rightarrow\; \E[\text{first}] = \frac{1}{1/2} = 2 \text{ min}, \qquad P(\text{first} > 3) = e^{-3/2} \approx 0.223.$$

**Beat 7 — Ramp the difficulty.**

- *Simplest:* i.i.d. exponentials — add $n$ equal rates. Three mean-$10$ clocks $\to$ rate $\tfrac{3}{10}$, mean $\tfrac{10}{3}$ s.
- *Twist — unequal rates.* The gate's $4,6,12$ clocks: convert to rates, add, invert (mean $2$). Never average the means.
- *General — non-exponential min.* For $n$ i.i.d. $\Unif(0,1)$, $S(x) = 1 - x$, so $f_{\min}(x) = n(1-x)^{n-1}$ and $\E[\min] = \tfrac{1}{n+1}$ — the mirror of the max's $\tfrac{n}{n+1}$.
- *Boundary:* one clock ($n=1$) gives back the original exponential; sanity holds.

**Beat 8 — Picture it.**

<figure>
<img src="../../assets/diagrams/ch14_min_exponential_race.png" alt="A timeline race diagram: three exponential clocks with rates 1/4, 1/6, 1/12 each shown as a horizontal arrow with a randomly-placed ring-time marker; a vertical line marks the earliest of the three (the minimum). A small inset overlays the survival curves and shows the combined minimum clock as a single steeper exponential with rate 1/2, ringing sooner." style="width:80%; max-width:560px; display:block; margin:1em auto;">
<figcaption>The exponential race: the first clock to ring is itself exponential, with the rates <em>added</em> ($\tfrac14+\tfrac16+\tfrac1{12}=\tfrac12$). Adding rates makes the combined clock faster — mean $2$, below every individual mean.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now write the distribution of the *weakest / first / soonest* of $n$ draws via $[S(x)]^n$, and — the high-value shortcut — collapse a *race of independent exponentials* into a single exponential by **adding the rates**.

::: pokedex-entry
**POKÉDEX ENTRY №02 — The Minimum (the first order statistic)**

For i.i.d. $X_1, \dots, X_n$ with survival function $S$, the minimum $m = X_{(1)} = \min_i X_i$ has
$$S_{\min}(x) = [S(x)]^n, \qquad F_{\min}(x) = 1 - [S(x)]^n, \qquad f_{\min}(x) = n\,[S(x)]^{n-1}\,f(x).$$
**Memorize the exponential case:** if $X_i \sim \Expo(\text{rate }\lambda_i)$ independently, then
$$\min_i X_i \sim \Expo\!\Big(\textstyle\sum_i \lambda_i\Big), \qquad S_{\min}(x) = e^{-(\sum_i \lambda_i)x}.$$
For $n$ i.i.d. exponentials with mean $\theta$: $\;\min \sim \Expo$ with **mean $\theta/n$.** For $n$ i.i.d. $\Unif(0,b)$: $\;\E[\min] = \tfrac{b}{n+1}$.

*In plain terms:* the smallest exceeds $x$ only when **every** draw does — raise the *survival* function to the $n$-th. Several exponential clocks racing: the first to ring is exponential, and *faster*, because the rates add.

*Recognition cue:* **"weakest," "first to fail," "soonest," "shortest,"** the *first* of several exponential waits, or a *series* system $\to$ reach for $[S(x)]^n$ (and add rates for exponentials).
:::

## Concept 3 — The General $k$-th Order Statistic & System Reliability

::: concept-gate
**DO YOU ALREADY OWN THIS? — General Rank & Reliability**

(a) Four judges each score $X_i \sim \Unif(0,1)$ independently; the final uses the **second-lowest** ($k=2$) score. What is its expected value? (b) Three components each work w.p. $0.9$; wired **in parallel** (any one suffices), what is the system's reliability?

If you answered **$\tfrac{2}{5} = 0.4$** (using $\E[X_{(k)}] = \tfrac{k}{n+1}$) and **$1 - 0.1^3 = 0.999$**, **skip to Concept 4** — the crown jewel. Otherwise, read on.
:::

**Beat 1 — The one-sentence idea.** *To be the $k$-th smallest of $n$ draws, one draw lands at $x$, exactly $k-1$ fall below it, and the remaining $n-k$ fall above — and a counting coefficient tallies the arrangements.*

**Beat 2 — Anchor + concrete instance.** Max ($k=n$) and min ($k=1$) were the easy ends. Now we want any rank in between — a median, a second-best, a second-worst. The tool is the same "events multiply" idea, plus the **multinomial counting** you met back in Chapter 4.

Four judges score a performance, each $X_i \sim \Unif(0,1)$ independently. The final score *drops the lowest and uses the second-lowest* — the $k = 2$ order statistic, $X_{(2)}$, of $n = 4$. *What is its expected value?*

**Beat 3 — Reason through it in plain words.** Picture the density at a point $x$. For $X_{(2)}$ to sit right at $x$, three things must line up at once: **one** of the four draws is at $x$ (density $f(x)$), exactly **$k-1 = 1$** of the others falls *below* $x$ (each with chance $F(x)$), and the remaining **$n - k = 2$** fall *above* $x$ (each with chance $1 - F(x)$). But *which* draw is the one at $x$, and *which* land below, can be arranged in several ways — that is where the counting coefficient comes in.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The tempting shortcut is to forget the coefficient and write $f(x)\,F(x)^{k-1}(1-F(x))^{n-k}$ alone. But that prices *one specific labeling* — "draw #1 is the one at $x$, draws #2 below, #3 and #4 above." There are many equally valid labelings, and ignoring them undercounts the density. The number of ways to choose which draw sits at $x$, which $k-1$ go below, and which $n-k$ go above is the **multinomial coefficient** $\dfrac{n!}{(k-1)!\,1!\,(n-k)!}$. Leave it out and your density won't integrate to $1$.

**Beat 5 — Translate into notation, one glyph at a time.** The $k$-th smallest value is $X_{(k)}$, read *"$X$ sub-paren-$k$,"* the value in sorted position $k$. The factorial $n!$ reads *"$n$ factorial"* — the count of ways to order $n$ items (Chapter 4). Assembling the three pieces with their count:

$$f_{X_{(k)}}(x) = \frac{n!}{(k-1)!\,(n-k)!}\,[F(x)]^{k-1}\,[1 - F(x)]^{\,n-k}\,f(x).$$

Read it left to right: *the number of arrangements*, times *$k-1$ draws below*, times *$n-k$ draws above*, times *one draw right here*.

**Beat 6 — Generalize: the uniform mean drops out for free.** For i.i.d. $\Unif(0,1)$ ($F(x) = x$, $f(x) = 1$), that density is the **Beta** density $\BetaDist(k,\,n-k+1)$, whose mean is a clean ratio:

$$\boxed{\;\E\!\big[X_{(k)}\big] = \frac{k}{n+1} \quad \text{for i.i.d. } \Unif(0,1).\;}$$

Check the ends: $k=n$ gives $\tfrac{n}{n+1}$ (the max, Entry №01) and $k=1$ gives $\tfrac{1}{n+1}$ (the min, Entry №02) — the general formula contains both. For the four judges, $\E[X_{(2)}] = \tfrac{2}{5} = 0.4$.

**Beat 7 — Ramp the difficulty, and bridge to reliability.**

- *Simplest:* uniform mean of any rank, $\tfrac{k}{n+1}$. Median of $5$ draws ($k=3$): $\tfrac{3}{6} = \tfrac12$.
- *General density:* plug any $F$ into the $k$-th-order formula.
- *The reliability bridge.* A system of independent components is just an order-statistic question in disguise. A **series** system (a chain — all must work; it fails when the *first* component fails) has lifetime $= \min_i X_i$, so its reliability is $R_{\text{series}}(t) = \prod_i S_i(t)$. A **parallel** system (backups everywhere — works while *any* component works; fails when the *last* dies) has lifetime $= \max_i X_i$, so $R_{\text{parallel}}(t) = 1 - \prod_i F_i(t)$. Three components each working w.p. $0.9$: series $0.9^3 = 0.729$; parallel $1 - 0.1^3 = 0.999$.

**Beat 8 — Picture it.**

<figure>
<img src="../../assets/diagrams/ch14_series_parallel.png" alt="Two circuit schematics. Left: three components drawn in a single line (series) labeled lifetime = min, reliability = product of survivals = 0.729. Right: three components drawn as three parallel branches (parallel) labeled lifetime = max, reliability = 1 minus product of failure probs = 0.999. Below, a strip showing four sorted dots on [0,1] with the second-from-left circled as X_(2)." style="width:82%; max-width:600px; display:block; margin:1em auto;">
<figcaption>Reliability as order statistics: a <em>series</em> chain dies with the <strong>minimum</strong> (weakest link); a <em>parallel</em> bank survives to the <strong>maximum</strong> (last backup). Below: the $k$-th order statistic is the $k$-th sorted dot.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now write the density of *any* rank, read off $\tfrac{k}{n+1}$ for uniform means, and translate series/parallel reliability into min/max.

::: pokedex-entry
**POKÉDEX ENTRY №03 — General $k$-th Order Statistic & Reliability**

$$f_{X_{(k)}}(x) = \frac{n!}{(k-1)!\,(n-k)!}\,[F(x)]^{k-1}\,[1-F(x)]^{\,n-k}\,f(x).$$
For i.i.d. $\Unif(0,1)$: $\;\E[X_{(k)}] = \dfrac{k}{n+1}$ (the Beta$(k, n-k+1)$ mean), with max ($k=n$) and min ($k=1$) as special cases.

**Reliability:** *series* (all must work) $\to$ lifetime $= \min$, $R = \prod_i S_i(t)$; *parallel* (any one suffices) $\to$ lifetime $= \max$, $R = 1 - \prod_i F_i(t)$.

*Recognition cue:* a **specific rank** (median, second-best, second-worst) $\to$ the $k$-th-order density. **"In series"** $\to$ min; **"in parallel," "with backups," "redundant"** $\to$ max.
:::

## Concept 4 — The Central Limit Theorem (Many Draws Go Normal)

::: concept-gate
**DO YOU ALREADY OWN THIS? — The CLT**

A sum of $100$ i.i.d. purses, each mean $500$, SD $150$. Approximate $P(\text{total} > 52{,}000)$.

If you answered **$\approx 0.091$** — standardizing with $z = \dfrac{52{,}000 - 100\cdot 500}{\sqrt{100}\cdot 150} = 1.33$ and reading $1 - \Phi(1.33)$ — **skip to Concept 5**. If you used SD $= 150$ instead of $\sqrt{100}\cdot 150 = 1500$, read on: that is the single most-punished CLT slip.
:::

**Beat 1 — The one-sentence idea.** *Add up many independent random pieces and the total settles into a bell curve — no matter what shape the pieces had — so you only need the mean and variance to read a probability off the normal table.*

**Beat 2 — Anchor + concrete instance.** From Chapter 13 you know the mean and variance of a sum of independent draws: means add, and variances add. The CLT adds the astonishing extra fact that, for *many* draws, the *shape* of that sum is **normal**. That lets you reuse the standard normal table from Chapter 9.

The treasurer's prize pool: $n = 100$ matches, each paying an independent purse $X_i$ with mean $\mu = 500$ and SD $\sigma = 150$ Poké-dollars. The League budgeted $52{,}000$. *What is the chance the total payout overruns the budget?*

**Beat 3 — Reason through it in plain words.** First nail the mean and spread of the **total** $S = X_1 + \cdots + X_{100}$, using Chapter 13. Means add, so the expected total is $100 \times 500 = 50{,}000$. *Variances* add (independence), so the variance of the total is $100 \times 150^2$, and the **standard deviation of the total** is $\sqrt{100}\times 150 = 1500$ — *not* $150$. The budget $52{,}000$ sits $\dfrac{52{,}000 - 50{,}000}{1500} = 1.33$ standard deviations above the expected total. The CLT says the total is *approximately normal*, so that "$1.33$ SDs above" reads straight off the standard normal table: the chance of exceeding it is $1 - \Phi(1.33) \approx 0.091$. About a **$9\%$** chance of a budget overrun.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The fatal slip is to standardize the *total* with a *single-draw* SD:

$$z \overset{?}{=} \frac{52{,}000 - 50{,}000}{150} = 13.3. \qquad\textbf{(wrong)}$$

That treats a sum of a hundred purses as if it wiggled as little as one purse — absurd. A sum of many random pieces is *more* variable in absolute terms (the SD grows like $\sqrt{n}$), so the divisor must be $\sqrt{100}\cdot 150 = 1500$, giving $z = 1.33$, not $13.3$. The matching error for an *average*: dividing by $\sigma$ instead of $\sigma/\sqrt{n}$. Get the right spread under the $z$, and the rest is a table lookup.

**Beat 5 — Translate into notation, one glyph at a time.** The "approximately distributed as" sign is a dotted-tilde:

$$S_n \;\dot\sim\; \Normal(\mu_S, \sigma_S^2) \qquad \text{read aloud: ``}S_n\text{ is approximately normal with mean }\mu_S\text{ and variance }\sigma_S^2\text{.''}$$

Here $\Normal(\text{mean}, \text{variance})$ is the normal from Chapter 9, and $\Phi$ (capital phi) is its standard-normal cdf, read *"the chance a standard normal is at most $z$,"* taken from the table. **Standardizing** — subtract the mean, divide by the SD — is the move from Chapter 9 that turns any normal into a table lookup.

**Beat 6 — Generalize: state the theorem and the two standardizations.** Let $X_1, \dots, X_n$ be i.i.d. with mean $\mu$ and finite variance $\sigma^2$. For large $n$, both the sum $S_n = \sum_{i=1}^n X_i$ and the mean $\bar X_n = S_n/n$ are approximately normal — and we get their means and variances straight from Chapter 13 (means add; independent variances add; dividing by $n$ divides the variance by $n^2$):

$$\boxed{\;S_n \;\dot\sim\; \Normal\!\big(n\mu,\; n\sigma^2\big), \qquad \bar X_n \;\dot\sim\; \Normal\!\Big(\mu,\; \tfrac{\sigma^2}{n}\Big).\;}$$

Evaluate any probability by standardizing and reading $\Phi$:

$$P(S_n \le s) \approx \Phi\!\left(\frac{s - n\mu}{\sqrt{n}\,\sigma}\right), \qquad P(\bar X_n \le \bar x) \approx \Phi\!\left(\frac{\bar x - \mu}{\sigma/\sqrt{n}}\right).$$

The only two things that ever change are which mean ($n\mu$ for a sum, $\mu$ for an average) and which spread ($\sqrt{n}\,\sigma$ for a sum, $\sigma/\sqrt{n}$ for an average) go under the $z$.

**Beat 7 — Ramp the difficulty.**

- *Simplest — a sum.* The prize pool: $z = 1.33$, $P(S > 52{,}000) \approx 0.091$.
- *An average.* Reaction time, $\mu = 70$ ms, $\sigma = 10$ ms, $n = 100$: $\bar X \;\dot\sim\; \Normal(70, 1)$ (since $\sigma/\sqrt n = 1$), so $P(\bar X > 72) = 1 - \Phi(2) \approx 0.023$.
- *Sample-size design.* "Sample mean within $1$ of the truth w.p. $0.95$" demands $1.96\cdot\tfrac{\sigma}{\sqrt n} \le 1$ — solve for $n$ (a Gym Battle).
- *Boundary:* the approximation sharpens as $n$ grows; for skewed pieces you want $n$ in the tens before trusting it. For a *discrete* sum it needs one more fix — Concept 5.

**Beat 8 — Picture it.**

<figure>
<img src="../../assets/diagrams/ch14_clt_convergence.png" alt="Four histograms of the sample mean of n i.i.d. Uniform(0,1) draws for n=1, 2, 5, 30, with a red normal curve overlaid on each. At n=1 the histogram is flat (uniform); at n=2 it is triangular; by n=30 it is visually indistinguishable from the bell curve, and noticeably narrower because the variance shrinks like sigma^2/n." style="width:88%; max-width:640px; display:block; margin:1em auto;">
<figcaption>The CLT in action: the sample mean of $\Unif(0,1)$ draws starts flat ($n=1$), turns triangular ($n=2$), and is indistinguishable from the red normal by $n=30$. The bell also narrows — variance shrinks like $\sigma^2/n$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now take any sum or average of many i.i.d. draws, attach the right mean and spread, standardize, and read the probability off the table — no exact distribution required.

::: pokedex-entry
**POKÉDEX ENTRY №04 — The Central Limit Theorem**

For i.i.d. $X_1, \dots, X_n$ with mean $\mu$ and finite variance $\sigma^2$, for large $n$:
$$S_n \;\dot\sim\; \Normal\!\big(n\mu,\; n\sigma^2\big), \qquad \bar X_n \;\dot\sim\; \Normal\!\Big(\mu,\; \tfrac{\sigma^2}{n}\Big),$$
$$P(S_n \le s) \approx \Phi\!\left(\frac{s - n\mu}{\sqrt{n}\,\sigma}\right), \qquad P(\bar X_n \le \bar x) \approx \Phi\!\left(\frac{\bar x - \mu}{\sigma/\sqrt{n}}\right).$$

*In plain terms:* add up many independent pieces and the total goes bell-shaped, whatever the pieces looked like — you need only their mean and variance.

*Recognition cue:* the **total / average / sum of many** independent draws, a request for a **probability** with **no exact distribution** given, a large count $n$. Spread under the $z$ is $\sqrt{n}\,\sigma$ for a sum, $\sigma/\sqrt{n}$ for an average — never the single-draw $\sigma$.
:::

## Concept 5 — The Continuity Correction (the Half-Unit Fix)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Continuity Correction**

$X \sim \Binom(400, 0.4)$. Using the normal approximation **with continuity correction**, approximate $P(X \ge 180)$.

If you answered **$\approx 0.023$** — shifting "$\ge 180$" to "$> 179.5$" before standardizing, $z = \tfrac{179.5 - 160}{\sqrt{96}} \approx 1.99$ — **skip to the Worked Examples**. If you standardized $180$ directly, read on: the half-unit shift is worth real points.
:::

**Beat 1 — The one-sentence idea.** *When you approximate a whole-number count by a smooth normal curve, each integer "owns" a bar half a unit wide on each side — so shift the boundary by $\pm\tfrac12$ before standardizing to capture that bar.*

**Beat 2 — Anchor + concrete instance.** The CLT (Concept 4) approximates a *discrete* count (a binomial number of wins, a Poisson number of claims) by a *continuous* normal. But a continuous curve assigns zero probability to any single point, while a count genuinely lands *on* integers. The continuity correction reconciles the two.

Across the tournament you play $n = 400$ independent skirmish rounds, each won w.p. $p = 0.4$. The League awards a banner for **at least $180$** wins. *Approximate the chance you earn the banner.*

**Beat 3 — Reason through it in plain words.** Wins $X \sim \Binom(400, 0.4)$ has mean $\mu = np = 160$ and SD $\sigma = \sqrt{np(1-p)} = \sqrt{96} \approx 9.80$. Picture the binomial as a row of bars, one per integer, each bar centered on its integer and one unit wide — so the bar for "$180$" stretches from $179.5$ to $180.5$. "At least $180$" must include the *whole* $180$ bar, so the smooth normal curve should be integrated from the bar's **left edge, $179.5$** — not from $180$, which would slice the bar in half. Standardize the corrected boundary:

$$z = \frac{179.5 - 160}{9.80} \approx 1.99, \qquad P(X \ge 180) \approx 1 - \Phi(1.99) \approx 0.023.$$

About a **$2.3\%$** chance of the banner.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Skipping the shift standardizes the integer itself:

$$z \overset{?}{=} \frac{180 - 160}{9.80} = 2.04, \qquad 1 - \Phi(2.04) \approx 0.021. \qquad\textbf{(uncorrected — off)}$$

It chops the $180$ bar down the middle and discards half of it. The corrected $0.023$ and uncorrected $0.021$ differ enough that an exam will often list *both* as choices to catch you. The other half of the trap is the **direction**: for $P(X \ge 180)$ you slide *down* to $179.5$ (include $180$); for $P(X > 180)$ you slide *up* to $180.5$ (exclude $180$). Get the inequality wrong and you correct the wrong way.

**Beat 5 — Translate into notation, one glyph at a time.** Let $k$ be the integer boundary. The shift is $\pm\tfrac12$, chosen so the *named* integer is *included* on the side the inequality points:

$$P(X \ge k) \approx 1 - \Phi\!\left(\frac{(k - \tfrac12) - \mu}{\sigma}\right), \qquad P(X \le k) \approx \Phi\!\left(\frac{(k + \tfrac12) - \mu}{\sigma}\right).$$

Each integer $k$ owns the interval $[k - \tfrac12,\, k + \tfrac12]$ under the curve.

**Beat 6 — Generalize: the rule for every inequality.** Reading off "does the named integer stay in or go out?":

| You want | Corrected boundary | Reason |
|---|---|---|
| $P(X \ge k)$ | $> k - \tfrac12$ | include $k$ $\to$ start at its left edge |
| $P(X > k)$ | $> k + \tfrac12$ | exclude $k$ $\to$ start past its right edge |
| $P(X \le k)$ | $< k + \tfrac12$ | include $k$ $\to$ stop at its right edge |
| $P(X < k)$ | $< k - \tfrac12$ | exclude $k$ $\to$ stop before its left edge |
| $P(X = k)$ | $k - \tfrac12$ to $k + \tfrac12$ | the single bar around $k$ |

**Beat 7 — Ramp the difficulty.**

- *Simplest — binomial tail.* The banner: $P(X \ge 180) \to P(X > 179.5)$, $\approx 0.023$.
- *Poisson count.* A Poisson total of integer claims is corrected the same way ($\mu = \sigma^2 = \lambda$).
- *An exact equality.* $P(X = k)$ needs *both* edges: $\Phi(\tfrac{k+0.5 - \mu}{\sigma}) - \Phi(\tfrac{k-0.5 - \mu}{\sigma})$.
- *Edge:* when the summed variable is **continuous** (purses, weights, times), there is **no** correction — bars only exist for integer-valued counts.

**Beat 8 — Picture it.**

<figure>
<img src="../../assets/diagrams/ch14_continuity_correction.png" alt="A binomial(400, 0.4) bar histogram with a smooth normal curve overlaid, centered at 160. The bars at and above 180 are shaded. A dashed vertical line at 179.5 marks the left edge of the 180 bar, showing that the normal area for P(X>=180) is integrated from 179.5, capturing the full 180 bar rather than slicing it at 180." style="width:80%; max-width:560px; display:block; margin:1em auto;">
<figcaption>The continuity correction: the integer $180$ owns the bar from $179.5$ to $180.5$. To include it in $P(X \ge 180)$, the normal area starts at the left edge $179.5$ — capturing the whole bar, not half.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now spot an *integer-valued* sum, apply the CLT, and slide the boundary the correct half-unit in the correct direction before standardizing.

::: pokedex-entry
**POKÉDEX ENTRY №05 — The Continuity Correction**

When a **discrete** integer count (binomial, Poisson, sum of integer draws) is approximated by a continuous normal, shift the boundary by $\pm\tfrac12$ so the named integer is included on the side the inequality points:
$$P(X \ge k) \approx 1 - \Phi\!\left(\frac{(k - \tfrac12) - \mu}{\sigma}\right), \qquad P(X \le k) \approx \Phi\!\left(\frac{(k + \tfrac12) - \mu}{\sigma}\right).$$

*In plain terms:* each integer owns a unit-wide bar centered on it; to capture that bar with a smooth curve, integrate to its edge, half a unit out.

*Recognition cue:* the summed variable is **integer-valued** (wins, claims, defects, successes) and you want $P(X \ge k)$, $P(X \le k)$, or $P(X = k)$ $\to$ shift by $\pm\tfrac12$. **Continuous** sums get **no** correction.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/lance.png" alt="Lance of the Elite Four" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Lance — the Dragon master, your final mentor</figcaption>
</figure>

Four examples, fading from fully narrated to exam-speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because the CLT standardization is the load-bearing, most-tested move.

### Worked Example 14.1 — Will the Prize Pool Hold? (full narration; understanding-first)

**ARCHETYPE:** *CLT on a sum — standardize with $\sqrt{n}\,\sigma$ and read the table (Entry №04).*

**Setup.** The treasurer's prize pool: $n = 100$ matches, each paying an independent purse $X_i$ with mean $\mu = 500$ and SD $\sigma = 150$, and a budget of $52{,}000$. Approximate $P(\text{total} > 52{,}000)$.

**Step 1 — Identify.** "Total of many independent draws, find a probability, no exact distribution given" $\to$ CLT on the **sum** $S = \sum_{i=1}^{100} X_i$.

**Step 2 — Professor's Path (the why).** Build the sum's mean and spread from Chapter 13. Means add:
$$\E[S] = 100 \times 500 = 50{,}000.$$
Independent **variances** add, so $\Var(S) = 100 \times 150^2 = 2{,}250{,}000$, and the **standard deviation of the total** is
$$\SD(S) = \sqrt{100}\times 150 = 1500 \quad(\text{not } 150).$$
The CLT promises $S \;\dot\sim\; \Normal(50{,}000,\, 1500^2)$. Standardize the budget (Chapter 9):
$$z = \frac{52{,}000 - 50{,}000}{1500} = \frac{2000}{1500} = 1.333.$$

**Step 3 — Trainer's Path (the fast how).**
$$P(S > 52{,}000) \approx 1 - \Phi(1.33) \approx 1 - 0.9082 = 0.0918.$$
Tell the treasurer: roughly a **$9\%$** chance of an overrun.

**Step 4 — Check & pitfall.** A positive $z$ with a tail under $50\%$ is consistent with a budget set *above* the expected payout ✓. **Pitfall:** dividing by the single-draw SD $150$ (giving $z = 13.3$) instead of $\sqrt{n}\,\sigma = 1500$ — variance of a sum scales with $n$, SD with $\sqrt{n}$. *(Back-ref: Entry №04.)*

### Worked Example 14.2 — The First Pokémon to Faint (partial guidance)

**ARCHETYPE:** *Minimum of independent exponentials — rates add (Entry №02).*

**Setup.** Three Pokémon battle at once; their times-to-faint are independent exponentials with means $4$, $6$, and $12$ minutes. Find the distribution and mean of the *first* faint, and $P(\text{first} > 3)$.

<figure style="margin:1.5em auto; max-width:150px; text-align:center;">
<img src="../../assets/sprites/front/26.png" alt="Raichu" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#026 Raichu</strong> — one of the three on the mat.</figcaption>
</figure>

**Identify.** "First to faint" is the **minimum** of independent exponentials. *Your move: convert means to rates, then add the rates.*

Means $4, 6, 12 \Rightarrow$ rates $\lambda_1 = \tfrac14,\ \lambda_2 = \tfrac16,\ \lambda_3 = \tfrac1{12}$. Rates add:
$$\lambda = \tfrac14 + \tfrac16 + \tfrac1{12} = \tfrac{3+2+1}{12} = \tfrac12.$$
So the first faint is $\Expo(\text{rate }\tfrac12)$, i.e. **mean $= 1/\lambda = 2$ minutes**, with
$$P(\text{first} > 3) = e^{-\lambda \cdot 3} = e^{-1.5} \approx 0.2231.$$

**Check & pitfall.** The minimum's mean ($2$) is *below* the smallest individual mean ($4$) — correct: a race finishes faster than its quickest runner. **Pitfall:** averaging the means ($\tfrac{4+6+12}{3} = 7.33$) or summing them — add the **rates**, not the means. *(Back-ref: Entry №02.)*

### Worked Example 14.3 — The Strongest of the Field (light guidance)

**ARCHETYPE:** *Expectation and tail of a maximum of i.i.d. uniforms (Entry №01).*

**Setup.** Each of $n = 8$ qualifiers has strength $X_i \sim \Unif(0,30)$, independent. Find $\E[\max]$ and $P(\max > 27)$.

Single-draw cdf on $[0,30]$: $F(x) = x/30$. Uniform max shortcut:
$$\E[\max] = \frac{n}{n+1}\cdot 30 = \frac{8}{9}\cdot 30 = 26.\overline{6}.$$
Tail via the complement of the max-cdf:
$$P(\max > 27) = 1 - \Big(\tfrac{27}{30}\Big)^8 = 1 - 0.9^8 = 1 - 0.4305 = 0.5695.$$

**Check & pitfall.** $26.67$ sits just below the ceiling $30$, exactly where the strongest of eight belongs ✓. **Pitfall:** reporting the single-draw mean $15$ for the maximum — the strongest of a crowd is far above the typical entrant. *(Back-ref: Entry №01.)*

### Worked Example 14.4 — Counting Wins (exam speed; CLT + continuity correction)

**ARCHETYPE:** *Normal approximation to the binomial with continuity correction (Entries №04–№05).*

**Setup.** $X \sim \Binom(400, 0.4)$ wins. The banner needs **at least $180$**. Approximate $P(X \ge 180)$.

$$\mu = np = 160, \qquad \sigma = \sqrt{np(1-p)} = \sqrt{96} \approx 9.798.$$
Correct "$\ge 180$" to "$> 179.5$" (include the $180$ bar), then standardize:
$$z = \frac{179.5 - 160}{9.798} \approx 1.99, \qquad P(X \ge 180) \approx 1 - \Phi(1.99) \approx 0.0233.$$
About a **$2.3\%$** chance.

**Check & pitfall.** $180$ is two SDs above the mean of $160$, so a $\sim 2\%$ tail is sensible ✓. **Pitfall:** wrong correction *direction* — for $P(X \ge 180)$ go *down* to $179.5$; for $P(X > 180)$ go *up* to $180.5$. *(Back-ref: Entries №04, №05.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — Max vs. min, in one breath**

Read the verb. **"Strongest / last / longest / parallel"** $\to$ maximum $\to$ raise the **cdf**: $[F(x)]^n$. **"Weakest / first / soonest / series"** $\to$ minimum $\to$ raise the **survival**: $[S(x)]^n$. Get the right function under the power and the rest is mechanical.
:::

::: trainers-tip
**TRAINER'S TIP — Uniform order-statistic means for free**

For $n$ i.i.d. $\Unif(0,1)$, $\E[X_{(k)}] = \dfrac{k}{n+1}$: max $= \tfrac{n}{n+1}$, min $= \tfrac{1}{n+1}$, median (odd $n$) $= \tfrac12$. Scale by the interval width for $\Unif(0,b)$. This kills any "expected best/worst/$k$-th of $n$ uniforms" item with no integral.
:::

::: trainers-tip
**TRAINER'S TIP — CLT keystrokes and the spread**

For a **sum**, $z = \dfrac{x - n\mu}{\sqrt{n}\,\sigma}$; for a **mean**, $z = \dfrac{\bar x - \mu}{\sigma/\sqrt{n}}$. On the TI-30XS, store $\sqrt{n}\,\sigma$ with **STO→** before dividing so you don't re-key it. For an integer count, do the $\pm\tfrac12$ shift *before* you standardize — never after.
:::

::: trainers-tip
**TRAINER'S TIP — Exponential race: add rates, not means**

The minimum of independent exponentials is exponential with the **summed rate**. Convert every mean $\theta$ to a rate $1/\theta$, add the rates, and invert once at the end for the minimum's mean. Adding means is the classic wrong move — it makes the race *slower*, which can never be right.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

Jessie has a plan to skim the prize pool. "We win at least *one hundred ten* of two hundred rigged rounds," she announces, "and the bonus is ours. I did the normal approximation — mean a hundred, standard deviation about seven-oh-seven." James scribbles: $z = \tfrac{110 - 100}{7.07} = 1.41$, giving $1 - \Phi(1.41) \approx 0.079$. "Eight percent, boss!" Meowth cheers.

But the win count is a *whole number*, and Jessie forgot the **continuity correction**. The bar for "at least $110$" starts at $109.5$, not $110$:
$$z = \frac{109.5 - 100}{7.07} = 1.34, \qquad 1 - \Phi(1.34) \approx 0.090.$$
The true approximation is **nine percent, not eight.** They under-estimated their own odds, low-balled the bribe to the referee, and the scheme collapsed when the referee held out for more.

**Where it fails:** when the summed variable is integer-valued, shift the boundary by $\pm\tfrac12$ *before* standardizing — "$\ge k$" becomes "$> k - \tfrac12$." (And get the *direction* right: include the named integer on the side the inequality points.)
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

The Central Limit Theorem is **why insurance exists.** No actuary can predict a single policyholder's loss — it is as wild as one battle purse. But pool ten thousand independent policies and the **average** loss becomes nearly normal and tightly predictable; that shrinking $\sigma/\sqrt{n}$ is the mathematical statement that **diversification works**, and it underwrites every premium, reserve, and solvency-capital calculation. The exact same standardize-and-look-up move prices the chance that *aggregate* claims overrun a reserve — your prize-pool computation, with "matches" renamed "policies."

Order statistics do the complementary job. The **maximum** loss governs **catastrophe layers** and **excess-of-loss reinsurance** ("pay only the single largest claim above a retention"); the **minimum** lifetime is exactly a **series-system failure** in reliability engineering, and the min-of-exponentials rate-sum is how engineers combine independent failure hazards.

*Series bridge:* the CLT and the aggregate-loss normal approximation are foundational to **CAS Exam 5** (ratemaking and reserving) and the loss-distribution work in **MAS-I**; order statistics and reliability reappear in **STAM/Exam 5** severity modeling.

*Transfer check:* could you solve this with **no Pokémon in it**? "A portfolio of $100$ independent claims, each mean $500$, SD $150$; the reserve is $52{,}000$ — find the probability claims exceed the reserve." Same $z = 1.33$, same $0.091$. If you can do that, the skill has transferred.
:::

## The Gym Battle — League Finalist Capstone

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/lance.png" alt="Lance of the Elite Four" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Lance — the final gate before the Champion's chamber</figcaption>
</figure>

**Lance's Challenge.** Lance, the final member of the Elite Four, blocks the door to the Champion's chamber. "Numbers won you the badges," he says. "Let's see if they get you past me." He lays out the League's master file: $n = 144$ challengers in the open bracket, each with strength $X_i$ independent and **Uniform on $[0,100]$.** He fires five questions in sequence:

> (a) the expected strength of the **strongest** challenger; (b) the probability the strongest's strength is **below $95$**; (c) the expected strength of the **weakest** challenger; (d) treating each of $100$ scheduled matches as an independent purse with mean $500$, SD $150$, approximate $P(\text{total purse} > 52{,}000)$ via the CLT; (e) the chamber gate is a pair of independent locks, each opening after an $\Expo(\text{mean }10\text{ min})$ delay, and the gate opens when the **faster** lock trips — give the expected time until it opens, and reconcile it as a minimum.

**ARCHETYPE:** *Integrative — maximum, minimum, uniform order-statistic means, CLT on a sum, and a min-of-exponentials reliability reconciliation.*

**Step 1 — Identify.** Parts (a)–(c) are order statistics of i.i.d. uniforms (Entries №01–№03); (d) is the CLT on a sum (Entry №04); (e) is the minimum of independent exponentials (Entry №02).

**Step 2 — Trainer's Path.**

*(a) Strongest, expected.* Max of $144$ uniforms on $[0,100]$:
$$\E[X_{(144)}] = \frac{n}{n+1}\cdot 100 = \frac{144}{145}\cdot 100 \approx 99.31.$$

*(b) Strongest below $95$.* $F_{\max}(x) = (x/100)^{144}$, so
$$P(X_{(144)} < 95) = 0.95^{144} \approx 0.00062.$$
The strongest of $144$ is essentially never below $95$ — about a $0.06\%$ chance.

*(c) Weakest, expected.* Min of $144$ uniforms on $[0,100]$:
$$\E[X_{(1)}] = \frac{1}{n+1}\cdot 100 = \frac{100}{145} \approx 0.69.$$

*(d) Total purse, CLT.* Sum of $100$ purses, $\mu = 500$, $\sigma = 150$:
$$\E[S] = 50{,}000, \quad \SD(S) = \sqrt{100}\cdot 150 = 1500, \quad z = \frac{52{,}000 - 50{,}000}{1500} = 1.33,$$
$$P(S > 52{,}000) \approx 1 - \Phi(1.33) \approx 0.0918.$$

*(e) The gate — the twist.* Read carefully: the gate opens when the **faster** lock trips — the *minimum* of the two delays. Two independent $\Expo(\text{mean }10)$ delays have rate $\tfrac1{10}$ each; the minimum has rate $\tfrac1{10} + \tfrac1{10} = \tfrac15$, so
$$\E[\text{gate opens}] = \frac{1}{1/5} = 5 \text{ minutes}.$$
Equivalently, $n$ i.i.d. exponentials with mean $\theta$ have minimum-mean $\theta/n = 10/2 = 5$. ✓

**Step 3 — Professor's Path (part (c), exact integral).** Confirm the uniform-min mean from the min density $f_{\min}(x) = n[S(x)]^{n-1}f(x)$ with $S(x) = 1 - x/100$, $f(x) = 1/100$:
$$\E[X_{(1)}] = \int_0^{100} x\cdot 144\Big(1 - \tfrac{x}{100}\Big)^{143}\tfrac{1}{100}\,dx \overset{u = x/100}{=} 100\int_0^1 u\cdot 144(1-u)^{143}\,du = 100\cdot\frac{1}{145} = \frac{100}{145} \approx 0.69,$$
the $\BetaDist(2,144)$ mean — matching the shortcut.

**Step 4 — Check, verdict & the pitfall Lance is testing.** Every probability lands in $[0,1]$; the strongest of $144$ ($\approx 99.3$) hugs the ceiling and the weakest ($\approx 0.69$) hugs the floor, as they must; the $9\%$ overrun matches WE 14.1. **Pitfall:** part (e)'s wording — "two locks" tempts a *max*, but the gate opens at the *first* success, which is a **minimum**. Always map the *verb* ("opens when the faster trips") to the order statistic, not the physical layout. Lance nods and steps aside.

> "That," Lance says, "is how you read chaos. You found the extreme, you found the aggregate, and you never let a word trick you into the wrong tail. The chamber is yours."

## The Gym Challenge — Problem Set

::: problem-set
**TEST-OUT INSTRUCTIONS.** Work this set timed (~6 min/problem), then check the **Answer Key** below. Hit the mastery bar (**80%+ with correct method**) and you may move on. Problems are listed first; full worked solutions follow afterward (never interleaved). Markers: 🔴 Poké Ball = routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (mechanics)

**C14.1.** 🔴 Five rookies each post an independent score $X_i \sim \Unif(0,1)$. The scout flags the *highest*. Find $P(\text{highest} \le 0.8)$.

**C14.2.** 🔴 Three Pokémon hold a line; their independent break-times are exponential, each with mean $10$ seconds. The line collapses when the *first* breaks. Find the expected time to collapse.

**C14.3.** 🔴 Four sensor pods each report $X_i$ with cdf $F(x) = x^2$ on $[0,1]$, independently. The panel shows the *maximum*. Find $P(\text{max} \le 0.5)$.

**C14.4.** 🟡 A Pokémon's reaction time per drill is i.i.d. with mean $70$ ms and SD $10$ ms. Over $n = 100$ drills, approximate $P(\text{average} > 72\text{ ms})$.

**C14.5.** 🟡 A route delivers $50$ independent Berry shipments, each mean $3$ kg with variance $4$. Approximate $P(\text{total weight} < 160\text{ kg})$.

**C14.6.** 🔴 Nine independent qualifiers each have strength $X_i \sim \Unif(0,20)$. Find the expected strength of the *strongest* using the uniform shortcut.

**C14.7.** 🔴 A relay has three independent components, each working w.p. $0.9$. Find the reliability (i) *in series* and (ii) *in parallel*.

### Gym Battles (true SOA difficulty)

**C14.8.** 🟡 Agatha sets three independent ghostly trials, each scored $X_i \sim \Unif(0,1)$. Find (i) the expected *best* score and (ii) $P(\text{best} > 0.9)$.

**C14.9.** 🟡 Two of Lorelei's Pokémon thaw at independent exponential times with means $5$ and $8$ minutes. The combo fires when the *first* thaws. Find (i) the distribution of the first-thaw time, (ii) its mean, and (iii) $P(\text{first} > 3)$.

**C14.10.** 🟡 Bruno wagers you win **at least $110$** of $200$ independent fair coin-flip tiebreakers. Using the normal approximation *with continuity correction*, find the probability you win the wager.

**C14.11.** 🟡 The League insures $2000$ independent trainers; each files a mean-$1000$ claim with SD $4000$. Approximate $P(\text{aggregate claims} > 2.1\text{ million})$.

**C14.12.** 🟡 Four judges independently score $X_i \sim \Unif(0,1)$; the final drops the lowest and uses the *second-lowest* ($k=2$). Find its expected value.

**C14.13.** 🔵 Three backup generators have independent exponential lifetimes, each mean $10$ years. The bunker keeps power until the *last* dies (parallel). Find the expected time to blackout. *(Hint: $\E[\max]$ of $n$ i.i.d. exponentials with mean $\theta$ is $\theta\sum_{j=1}^{n}\tfrac1j$.)*

**C14.14.** 🔵 A quality auditor measures spring tension, i.i.d. with SD $\sigma = 5$ N. He wants the sample mean within $1$ N of the truth w.p. $0.95$. Using the CLT, find the smallest sample size $n$.

**C14.15.** 🟡 Two challengers each have strength $X_i \sim \Unif(0,1)$. The *weaker* goes to consolation. Find the expected strength of the weaker challenger and the density of that minimum.

### Elite Challenge (integrative / stretch)

**C14.16.** 🔵 Ten finalists each post an independent $X_i \sim \Unif(0,1)$. The League reports the **range** — the gap between strongest and weakest. Find $\E[X_{(10)} - X_{(1)}]$.

**C14.17.** 🔵 *(Compound sum + CLT.)* The season's aggregate prize liability has $N \sim \Poisson(\lambda = 500)$ payouts, each with mean $200$ and variance $10{,}000$, independent of $N$ and each other. Using $\E[S] = \lambda\,\E[X]$ and $\Var(S) = \lambda\,\E[X^2]$ with a CLT normal approximation, find $P(S > 110{,}000)$.
:::

## Answer Key

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

**C14.1** — *cdf of a maximum (Entry №01).* $F_{\max}(x) = x^5$ on $[0,1]$, so $P(\max \le 0.8) = 0.8^5 = 0.32768 \approx \mathbf{0.328}$.

**C14.2** — *minimum of i.i.d. exponentials (Entry №02).* Three rate-$\tfrac1{10}$ clocks; minimum rate $= \tfrac{3}{10}$, mean $= \tfrac{10}{3} \approx \mathbf{3.33}$ s.

**C14.3** — *cdf of a maximum (Entry №01).* $F_{\max}(x) = (x^2)^4 = x^8$, so $P(\max \le 0.5) = 0.5^8 = \tfrac{1}{256} \approx \mathbf{0.0039}$.

**C14.4** — *CLT on a sample mean (Entry №04).* $\bar X \;\dot\sim\; \Normal(70, 10^2/100) = \Normal(70, 1)$, SD $= 1$. $z = \tfrac{72-70}{1} = 2$, so $P(\bar X > 72) \approx 1 - \Phi(2) = 1 - 0.9772 = \mathbf{0.0228}$.

**C14.5** — *CLT on a sum (Entry №04).* $\E[S] = 50\cdot 3 = 150$, $\Var(S) = 50\cdot 4 = 200$, $\SD = \sqrt{200} \approx 14.14$. $z = \tfrac{160-150}{14.14} = 0.707$, so $P(S < 160) \approx \Phi(0.71) \approx \mathbf{0.760}$.

**C14.6** — *expected max of i.i.d. uniforms (Entry №01 shortcut).* $\E[\max] = \tfrac{n}{n+1}b = \tfrac{9}{10}\cdot 20 = \mathbf{18}$.

**C14.7** — *reliability ↔ order statistics (Entry №03).* (i) Series: $0.9^3 = \mathbf{0.729}$. (ii) Parallel: $1 - 0.1^3 = \mathbf{0.999}$.

**C14.8** — *max of i.i.d. uniforms, mean and tail (Entry №01).* (i) $\E[\max] = \tfrac{3}{4} = \mathbf{0.75}$. (ii) $P(\max > 0.9) = 1 - 0.9^3 = \mathbf{0.271}$.

**C14.9** — *minimum of independent exponentials (Entry №02).* Rates $\tfrac15, \tfrac18$; sum $= \tfrac{13}{40} = 0.325$. (i) First-thaw $\sim \Expo(0.325)$. (ii) mean $= \tfrac{1}{0.325} = \tfrac{40}{13} \approx \mathbf{3.08}$ min. (iii) $P(\min > 3) = e^{-0.325\cdot 3} = e^{-0.975} \approx \mathbf{0.377}$.

**C14.10** — *normal approx. to binomial, continuity correction (Entries №04–№05).* $X \sim \Binom(200, 0.5)$: $\mu = 100$, $\sigma = \sqrt{50} \approx 7.071$. Correct: $P(X \ge 110) \to P(X > 109.5)$, $z = \tfrac{109.5-100}{7.071} = 1.34$, so $P \approx 1 - \Phi(1.34) \approx \mathbf{0.090}$.

**C14.11** — *CLT on a sum (Entry №04).* $\E[S] = 2000\cdot 1000 = 2{,}000{,}000$; $\SD = \sqrt{2000}\cdot 4000 \approx 178{,}885$. $z = \tfrac{2{,}100{,}000 - 2{,}000{,}000}{178{,}885} = 0.559$, so $P(S > 2.1\text{M}) \approx 1 - \Phi(0.56) \approx \mathbf{0.288}$.

**C14.12** — *general $k$-th order statistic of uniforms (Entry №03).* $\E[X_{(k)}] = \tfrac{k}{n+1} = \tfrac{2}{5} = \mathbf{0.4}$.

**C14.13** — *expected max of i.i.d. exponentials, harmonic sum (Entries №01, №03).* $\E[\max] = \theta\sum_{j=1}^{3}\tfrac1j = 10\big(1 + \tfrac12 + \tfrac13\big) = 10\cdot\tfrac{11}{6} = \tfrac{110}{6} \approx \mathbf{18.33}$ years.

**C14.14** — *CLT sample-size design (Entry №04).* Need $1.96\cdot\tfrac{\sigma}{\sqrt n} \le 1$, so $\sqrt n \ge 1.96\cdot 5 = 9.8$, $n \ge 96.04$. Smallest integer: $n = \mathbf{97}$.

**C14.15** — *minimum of i.i.d. uniforms, mean and density (Entries №02–№03).* $\E[\min] = \tfrac{1}{n+1} = \tfrac13 \approx \mathbf{0.333}$. Density $f_{\min}(x) = n[1-x]^{n-1} = \mathbf{2(1-x)}$ on $[0,1]$.

**C14.16** — *expected range via order-statistic means (Entries №01–№03).* For $n$ i.i.d. $\Unif(0,1)$, $\E[X_{(n)}] = \tfrac{n}{n+1}$ and $\E[X_{(1)}] = \tfrac{1}{n+1}$, so $\E[\text{range}] = \tfrac{n-1}{n+1} = \tfrac{9}{11} \approx \mathbf{0.818}$.

**C14.17** — *compound-distribution moments + CLT (Entry №04; Ch. 10 compound bridge).* $\E[X] = 200$, $\Var(X) = 10{,}000 \Rightarrow \E[X^2] = 10{,}000 + 200^2 = 50{,}000$. Then $\E[S] = 500\cdot 200 = 100{,}000$ and $\Var(S) = 500\cdot 50{,}000 = 25{,}000{,}000$, $\SD = 5000$. $z = \tfrac{110{,}000 - 100{,}000}{5000} = 2$, so $P(S > 110{,}000) \approx 1 - \Phi(2) \approx \mathbf{0.0228}$.

### Quick-Answer Table

| # | Answer | | # | Answer |
|---|---|---|---|---|
| C14.1 | $0.8^5 \approx 0.328$ | | C14.10 | $\approx 0.090$ |
| C14.2 | $10/3 \approx 3.33$ s | | C14.11 | $\approx 0.288$ |
| C14.3 | $0.5^8 \approx 0.0039$ | | C14.12 | $0.4$ |
| C14.4 | $\approx 0.0228$ | | C14.13 | $\approx 18.33$ yr |
| C14.5 | $\approx 0.760$ | | C14.14 | $n = 97$ |
| C14.6 | $18$ | | C14.15 | $\E = 1/3,\ f_{\min} = 2(1-x)$ |
| C14.7 | series $0.729$, parallel $0.999$ | | C14.16 | $9/11 \approx 0.818$ |
| C14.8 | $\E = 0.75,\ P(\max>0.9) = 0.271$ | | C14.17 | $\approx 0.0228$ |
| C14.9 | $\Expo(0.325)$, mean $\approx 3.08$, $P \approx 0.377$ | | | |
:::

## Badge Earned — Mastery Checklist

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/earth_badge.png" alt="League Finalist medallion" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>League Finalist — order statistics &amp; the CLT cleared!</strong></figcaption>
</figure>

You earn the **League Finalist** standing when you can, unaided:

1. **Derive** the cdf, density, and expectation of the **maximum** ($[F(x)]^n$) and **minimum** ($[S(x)]^n$) of $n$ independent draws, and apply the uniform shortcut $\E[X_{(k)}] = \tfrac{k}{n+1}$. *(Outcome 3f.)*
2. **Recognize** the **minimum of independent exponentials** as exponential with the summed rate, and **map** series/parallel **reliability** to min/max. *(Outcome 3f.)*
3. **Write** the general $k$-th **order-statistic** density and use it for medians, second-bests, and ranges. *(Outcome 3f.)*
4. **Apply** the **CLT** to a sum or mean of many i.i.d. draws — standardize with $\sqrt{n}\,\sigma$ (sum) or $\sigma/\sqrt{n}$ (mean) and read $\Phi$. *(Outcome 3i.)*
5. **Deploy** the **continuity correction** ($\pm\tfrac12$, correct direction) whenever the summed variable is integer-valued. *(Outcome 3i.)*

> **Gym rematch pointers (🧴 Potion).** Miss item 1 $\to$ re-read Concepts 1–2 + WE 14.3. Miss item 2 $\to$ Concept 2 + WE 14.2 + C14.9. Miss item 3 $\to$ Concept 3 + C14.12 / C14.16. Miss item 4 $\to$ Concept 4 + WE 14.1 + capstone (d). Miss item 5 $\to$ Concept 5 + WE 14.4 + the Team Rocket trap, then retry C14.10.

*Onward — one gate remains. Beyond this door, the Champion waits, and everything you have built across sixteen chapters meets its final test.*

---

<!-- ===== CALLOUT BOX TEMPLATES (Pandoc fenced divs; styled by book/theme.css) =====
     ::: cold-open / pokedex-entry / trainers-tip / team-rocket / kanto-realworld
     Concept gate ("Do you already own this?") also uses a styled panel.
     Wrap the problem set in ::: problem-set and the key in ::: answer-key . -->
