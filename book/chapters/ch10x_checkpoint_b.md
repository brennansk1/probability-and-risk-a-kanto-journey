<!--
  file: ch10x_checkpoint_b
  tier: C
  outcomes: review
  draft1_source: drafts/chapters_draft1/.md
  maps_to: Spaced-retrieval review of Topic 2 (Univariate)
  status: draft
-->

# Checkpoint B — The Univariate World {.type-normal}

::: cold-open
**▶ COLD OPEN — EPISODE: "Stakeout at the Rocket Hideout"**

Five towns are behind you. You came into Kanto knowing how to read a clue backward with Bayes; you leave the univariate stretch able to take *any* single uncertain quantity — a damage roll, a waiting time, a claim size — and name its distribution, price it, and quote it.

Tonight you are parked outside the Celadon hideout with Officer Jenny, waiting. Stakeouts are long. To stay sharp you do what every trainer does before a gym: you run the tape back. Pikachu curls on the dashboard; you flip through your Pokédex's *Actuary Mode* log and quiz yourself, town by town — the random-variable language of the S.S. Anne, the expectation-and-variance drills of Vermilion, the named distributions of Lavender and Saffron, and the deductible math of Fuchsia's Safari Zone.

No new moves here. This is a **review montage**: prove you still own each idea cold, then fight a few mixed battles that pull from all five chapters at once — the way the real exam will.
:::

## Checkpoint — Spaced Retrieval

*(A short, no-new-content review: retrieval prompts and a few mixed problems that force
recall across Topic 2. Per MASTER_PLAN_V2 Part 6 / doctrine rule 8.)*

You learn by **retrieving**, not by re-reading. Answer each prompt below *from memory*, out loud or on paper, **before** you peek. A prompt you can answer in one breath, you own — move on. A prompt that makes you hesitate is a flashing signpost back to the chapter named in its tag. The point of the gap before the answer is the struggle itself: that effort is what burns the idea in.

::: trainers-tip
**RETRIEVAL ROUND — say the answer before you read it. Tags point to the source chapter.**

1. **(Ch 6 — RV language.)** What three objects fully describe a discrete random variable's distribution, and what is the one-line "is this a valid pmf" check? *(Answer: the pmf $p(x)=P(X=x)$, the cdf $F(x)=P(X\le x)$, and the survival $S(x)=P(X>x)=1-F(x)$. Valid pmf: every $p(x)\ge 0$ **and** they sum to $1$, $\sum_x p(x)=1$. For a pdf the analogue is $f(x)\ge 0$ and $\int_{-\infty}^{\infty} f(x)\,dx = 1$.)*

2. **(Ch 6.)** How do you recover $\E[X]$ for a **nonnegative** variable straight from the survival function? *(Answer: integrate/sum the survival function — $\E[X]=\int_0^\infty S(x)\,dx$ continuous, $\E[X]=\sum_{k\ge 0} S(k)=\sum_{k\ge 1}P(X\ge k)$ for nonnegative integers. Area under the survival curve **is** the mean.)*

3. **(Ch 7 — center & spread.)** State the two equivalent forms of variance and the linear-transform rule. *(Answer: $\Var(X)=\E[(X-\mu)^2]=\E[X^2]-(\E[X])^2$; and $\Var(aX+b)=a^2\Var(X)$ — the shift $b$ does nothing, the scale $a$ comes out **squared**. So $\SD(aX+b)=|a|\,\SD(X)$.)*

4. **(Ch 7 — MGFs.)** What is $M_X(t)$, and how do you get the mean and variance from it? *(Answer: $M_X(t)=\E[e^{tX}]$. Differentiate and set $t=0$: $\E[X]=M_X'(0)$, $\E[X^2]=M_X''(0)$, then $\Var(X)=M_X''(0)-\big(M_X'(0)\big)^2$. Moments live in the derivatives at zero.)*

5. **(Ch 8 — discrete patterns.)** Match the story to the distribution: (i) number of successes in $n$ fixed independent trials; (ii) number of trials until the first success; (iii) count of rare events in a fixed window; (iv) successes when drawing **without replacement** from a finite pool. *(Answer: (i) Binomial, (ii) Geometric, (iii) Poisson, (iv) Hypergeometric.)*

6. **(Ch 8.)** Give the mean and variance of $\Binom(n,p)$ and of $\Poisson(\lambda)$ from memory. *(Answer: Binomial $\E=np$, $\Var=np(1-p)$. Poisson $\E=\Var=\lambda$ — equal mean and variance is the Poisson fingerprint.)*

7. **(Ch 9 — continuous patterns.)** State the **memoryless** property of the exponential in one sentence, and give $\E[X]$ and $\Var(X)$ for $\Expo(\theta)$ (mean parameterization). *(Answer: $P(X>s+t\mid X>s)=P(X>t)$ — having waited already buys you nothing. $\E[X]=\theta$, $\Var(X)=\theta^2$.)*

8. **(Ch 9 — transformations.)** To find the pdf of $Y=g(X)$ for a monotonic $g$, what is the two-step recipe? *(Answer: cdf method or the change-of-variables formula $f_Y(y)=f_X\!\big(g^{-1}(y)\big)\,\left|\dfrac{d}{dy}g^{-1}(y)\right|$ — invert, then multiply by the Jacobian $|dx/dy|$. Don't forget the absolute-value Jacobian.)*

9. **(Ch 10 — pricing the risk.)** Write the payment under an **ordinary deductible** $d$, and what $\E[(X-d)_+]$ means in words. *(Answer: payment $=(X-d)_+=\max(X-d,0)$; $\E[(X-d)_+]$ is the average amount paid per loss after the deductible swallows the first $d$ and the payment is never negative.)*

10. **(Ch 10.)** For a **policy limit** $u$, what is the capped payment, and how does the limited expected value relate to survival? *(Answer: capped payment $=X\wedge u=\min(X,u)$; $\E[X\wedge u]=\int_0^u S(x)\,dx$ — area under survival up to the cap. A deductible-$d$, max-covered-loss-$u$ layer pays $\E[X\wedge u]-\E[X\wedge d]$.)*
:::

If any of those ten made you stall, that chapter is your evening's homework before the mixed problems below. If all ten came easily, you have the univariate toolkit loaded — go fight.

## Mixed Retrieval Problems

These eight problems are deliberately **interleaved**: consecutive ones come from different towns, so you must first *recognize* which tool the situation calls for — exactly the recognition the exam tests. No problem needs a method you have not already seen in Chapters 6–10. Work them timed (~5 min each), then check the key.

::: problem-set
**MIXED REVIEW — Topic 2 (Univariate).** Problems first; full worked solutions follow in the Answer Key (never interleaved). Markers: 🔴 routine · 🟡 routine-with-a-twist · 🔵 stretch.

**B.1.** 🔴 *(Ch 6 — valid pmf + cdf.)* A Magikarp's number of useless flops $X$ before it finally lands has pmf $p(x)=c\,(1/2)^x$ for $x=0,1,2,\dots$. Find the constant $c$, then $P(X\le 2)$.

**B.2.** 🔴 *(Ch 7 — variance and a linear transform.)* A wild Pokémon's base attack roll $X$ has $\E[X]=20$ and $\Var(X)=9$. A held item rescales the roll to $Y=1.5X-4$. Find $\E[Y]$ and $\SD(Y)$.

**B.3.** 🟡 *(Ch 8 — Binomial vs. its complement.)* You throw $6$ Poké Balls at identical wild Pokémon, each catching independently w.p. $0.3$. Find the probability you catch **at least one**.

**B.4.** 🟡 *(Ch 8 — Poisson.)* Bug Catchers wander onto your route as a Poisson process averaging $\lambda = 2$ per hour. Over one hour, find the probability that **exactly two** Bug Catchers appear, and the probability that **at least one** appears.

**B.5.** 🟡 *(Ch 9 — exponential, survival & memoryless.)* The time $T$ (in minutes) until a Snorlax stirs from its nap is $\Expo$ with mean $\theta = 5$. Find $P(T > 8)$, and given it has already slept $3$ minutes, the probability it sleeps at least $8$ more.

**B.6.** 🔵 *(Ch 9 — transformation.)* Let $U \sim \Unif(0,1)$. Define $X = -\theta \ln U$ with $\theta = 4$. Find the pdf of $X$ and name the distribution. *(This is the inverse-transform trick for simulating losses.)*

**B.7.** 🟡 *(Ch 10 — ordinary deductible on an exponential loss.)* A fled-Pokémon replacement cost $X$ (in thousands) is $\Expo$ with mean $4$. The warden's policy has an ordinary deductible $d = 2$. Find the expected payment **per loss**, $\E[(X-2)_+]$.

**B.8.** 🔵 *(Ch 10 + Ch 8 integrative — limit + expectation.)* A trainer's monthly Potion expense $X$ (in hundreds) is discrete: $X=0,1,2,3$ with probabilities $0.4,0.3,0.2,0.1$. A reimbursement plan pays $X$ capped at a limit $u=2$, i.e. it pays $X\wedge 2$. Find the expected reimbursement $\E[X\wedge 2]$ and the expected **out-of-pocket** amount the trainer still bears, $\E[X] - \E[X\wedge 2]$.
:::

## Answer Key

::: answer-key
**Full worked solution per problem, tagged to its source chapter. A quick-answer table closes the section.**

**B.1** — *(Ch 6) Normalize a geometric-type pmf, then sum the cdf.* The pmf must sum to $1$. Using the geometric series $\sum_{x=0}^{\infty} (1/2)^x = \dfrac{1}{1-1/2} = 2$,
$$\sum_{x=0}^{\infty} c\,(1/2)^x = 2c = 1 \;\Longrightarrow\; c = \tfrac12.$$
Then $p(0)=\tfrac12,\ p(1)=\tfrac14,\ p(2)=\tfrac18$, so
$$P(X\le 2) = \tfrac12 + \tfrac14 + \tfrac18 = \tfrac78 = 0.875.$$

**B.2** — *(Ch 7) Linear-transform rules: shift moves the mean, scale squares the variance.*
$$\E[Y] = 1.5\,\E[X] - 4 = 1.5(20) - 4 = 26.$$
$$\Var(Y) = 1.5^2\,\Var(X) = 2.25(9) = 20.25 \;\Longrightarrow\; \SD(Y) = \sqrt{20.25} = 4.5.$$
The $-4$ shift is invisible to spread; only the $1.5$ scaling touches $\SD$.

**B.3** — *(Ch 8) "At least one" of a Binomial via the complement.* With $X\sim\Binom(6,0.3)$,
$$P(X\ge 1) = 1 - P(X=0) = 1 - (0.7)^6 = 1 - 0.117649 = 0.882351 \approx 0.8824.$$

**B.4** — *(Ch 8) Poisson pmf and its complement.* With $\lambda = 2$ and $P(N=k)=e^{-\lambda}\lambda^k/k!$,
$$P(N=2) = \frac{e^{-2} 2^2}{2!} = 2e^{-2} \approx 0.2707,$$
$$P(N\ge 1) = 1 - P(N=0) = 1 - e^{-2} \approx 0.8647.$$

**B.5** — *(Ch 9) Exponential survival, then memorylessness.* For $\Expo(\theta=5)$, $S(t)=e^{-t/\theta}$:
$$P(T>8) = e^{-8/5} = e^{-1.6} \approx 0.2019.$$
By the **memoryless** property the $3$ minutes already slept are forgotten:
$$P(T > 3+8 \mid T > 3) = P(T > 8) = e^{-8/5} \approx 0.2019.$$

**B.6** — *(Ch 9) Change of variables — the inverse-transform that makes an exponential.* $X=-\theta\ln U$ is monotone decreasing on $(0,1)$. Invert: $U = e^{-X/\theta}$, so $x$ ranges over $(0,\infty)$, and the Jacobian is
$$\left|\frac{dU}{dx}\right| = \left|-\tfrac{1}{\theta}e^{-x/\theta}\right| = \tfrac{1}{\theta}e^{-x/\theta}.$$
Since $f_U(u)=1$ on $(0,1)$,
$$f_X(x) = f_U\big(e^{-x/\theta}\big)\cdot \tfrac{1}{\theta}e^{-x/\theta} = \tfrac{1}{\theta}e^{-x/\theta}, \quad x>0.$$
That is the **Exponential** pdf with mean $\theta = 4$. (This is exactly how a simulator turns a uniform random number into an exponential loss.)

**B.7** — *(Ch 10) Expected payment per loss, exponential + ordinary deductible.* For an exponential loss with mean $\theta$ and ordinary deductible $d$, the memoryless property gives the clean closed form
$$\E[(X-d)_+] = \theta\, e^{-d/\theta} = 4\,e^{-2/4} = 4\,e^{-0.5} \approx 2.4261.$$
(Equivalently $\E[(X-d)_+] = \E[X] - \E[X\wedge d]$; the exponential just collapses it to $\theta e^{-d/\theta}$.)

**B.8** — *(Ch 10 + Ch 8) Capped expectation and the leftover out-of-pocket.* The capped variable $X\wedge 2$ takes values $0,1,2,2$ when $X=0,1,2,3$ (the $X=3$ outcome is clipped to $2$):

| $X$ | prob | $X\wedge 2$ |
|---|---|---|
| $0$ | $0.4$ | $0$ |
| $1$ | $0.3$ | $1$ |
| $2$ | $0.2$ | $2$ |
| $3$ | $0.1$ | $2$ |

$$\E[X\wedge 2] = 0(0.4) + 1(0.3) + 2(0.2) + 2(0.1) = 0.3 + 0.4 + 0.2 = 0.9.$$
The full expected expense is $\E[X] = 0(0.4)+1(0.3)+2(0.2)+3(0.1) = 1.0$, so the trainer's expected out-of-pocket (the part above the limit) is
$$\E[X] - \E[X\wedge 2] = 1.0 - 0.9 = 0.1.$$

### Quick-Answer Table

| Problem | Source | Answer |
|---|---|---|
| B.1 | Ch 6 | $c=\tfrac12$; $P(X\le 2)=0.875$ |
| B.2 | Ch 7 | $\E[Y]=26$; $\SD(Y)=4.5$ |
| B.3 | Ch 8 | $P(X\ge 1)\approx 0.8824$ |
| B.4 | Ch 8 | $P(N=2)\approx 0.2707$; $P(N\ge1)\approx 0.8647$ |
| B.5 | Ch 9 | $P(T>8)\approx 0.2019$ (same after memoryless) |
| B.6 | Ch 9 | $f_X(x)=\tfrac14 e^{-x/4}$, $x>0$ — Exponential, mean $4$ |
| B.7 | Ch 10 | $\E[(X-2)_+]=4e^{-0.5}\approx 2.4261$ |
| B.8 | Ch 10 | $\E[X\wedge 2]=0.9$; out-of-pocket $=0.1$ |
:::

## Badge Check — Univariate Mastery

If you cleared the retrieval round cold and hit the mixed set at $80\%+$ with the right method each time, the univariate badges are yours: you can name a single random quantity's distribution, read its center and spread, and price a payment off it. Pikachu hops back to the dashboard. Down the alley, a light flicks on inside the hideout — Topic 3, the **multivariate** world where variables move *together*, starts the moment you step through that door.
