<!--
  file: ch18_checkpoint_multivariate
  tier: (mixed — checkpoint)
  outcomes: 3a,3b,3c,3d,3e,3f,3g (review; no new outcomes)
  tia: C.4
  locale: Indigo Plateau — the night before the championship
  type: normal
  maps_to: Plateau eve — spaced-retrieval checkpoint over all of Act III (ch14-17); no new theory, no gym, no badge
  content_base: V3 §19 checkpoint design (mind-map -> 60-sec grid -> 12 mixed drills -> explicit pass gate + spaced-retrieval fail path)
-->

# Checkpoint B — The Night Before the Championship {.type-normal}

<figure>
<img src="../../assets/maps/kanto_ch18.png" alt="Kanto town map with the route traced all the way to the Indigo Plateau in the far corner; all eight badges earned, the journey complete, only the championship ahead." style="width:70%; max-width:520px; display:block; margin:1em auto;">
<figcaption>The whole road, behind you. Eight badges, Victory Road cleared — and at the very edge of the map, the Indigo Plateau. This is the last camp before the championship. No new road tonight; just everything you already know, laid out one more time.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Last Camp"**

The campfire at the foot of the Indigo Plateau throws long shadows up the stone steps. Tomorrow the championship begins. Tonight there is nothing left to learn — and that, Pikachu seems to understand, is exactly the point. It sits beside you, ears up, watching the embers.

You walk the whole of Act III back in your head. On Cinnabar, in Blaine's mansion, you first held a **pair** of variables under one law — power *and* stability, recorded together, a joint distribution. On Victory Road your six Pokémon stopped being six separate things and became a **sum of correlated parts**, where the cross-term between them was the difference between a real risk estimate and a dangerous lie. In Viridian, Giovanni hid his strength inside a **randomly chosen squad**, and you learned to average over a layer you could not see — and to split your fear into the part from his dice and the part from his Pokémon. And on the Plateau's own bracket, you stopped caring about any one competitor and started caring about the **extremes** — the strongest of the field, the first to fall.

Four ideas. One thread runs through all of them: **variables now move together.** A team is a sum. A threat is an average over a hidden tier. A champion is a maximum.

Oak's voice comes quiet through the Pokédex. "Tomorrow they'll throw all of it at you at once, Ash — joint, covariance, conditional, order statistics, with no label on which is which. So tonight we don't add anything. We just make sure that when a problem walks up wearing no name tag, you still know which of the four it is."

There is no gym here. No badge to win. Just one question, the only one that matters the night before the exam:

*When the four ideas of Act III come at you mixed and unlabeled, can you still tell them apart — and finish each one?*
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP077 "Round One – Begin!"**

<figure><img src="../../assets/stills/ch18_now_playing.jpg" alt="Ash arriving at the Indigo Plateau stadium as the League opens (Indigo League EP077)." style="width:60%; max-width:440px; display:block; margin:0.4em auto;"><figcaption style="font-size:0.8em; color:#555;">The League opens, EP077 — the four Act-III ideas come at you unlabeled, one after another.</figcaption></figure>

The Pokémon League opens at the Indigo Plateau: the torch is lit, the field of trainers is huge, and the first mixed rounds begin — exactly the spirit of this checkpoint, where the four Act-III ideas come at you unlabeled, one after another. Watch the opening rounds, then run the gauntlet below. *(The "mixed, no-warning" framing is our in-world extension of the tournament, not an on-screen line.)*
:::

## Where You Are — 60-Second Retrieval

**Rank: Champion-ready · Badges: 8 (all earned).** You have every badge Kanto offers. This is not a teaching chapter — it adds no new theory. It is a **spaced-retrieval checkpoint**: the single most reliable way to make Act III stick is to pull each idea out of memory cold, under mixed conditions, the way the exam will demand it. The mind-map below is the whole act on one page; the retrieval grid after it is the load-bearing idea from each of the four chapters. Reconstruct each from memory *before* you read the line that follows it.

<figure>
<img src="../../assets/diagrams/ch18_act3_mindmap.png" alt="A one-page concept map of Act III drawn as a single vertical spine with four stacked nodes joined by arrows. Node 1, Joint Distributions (ch14, outcomes 3a, 3b): joint density f(x,y) over a region with double integral equal to 1, marginal f_X equals the integral of the joint over y, and independence equivalent to the joint factoring into the product of marginals on a rectangle. Node 2, Joint Moments and Covariance (ch15, outcomes 3c, 3e, 3g, 3h): covariance equals E[XY] minus E[X]E[Y], correlation rho equals covariance over the product of standard deviations and lies in [-1,1], and the variance of aX+bY equals a-squared times Var(X) plus b-squared times Var(Y) plus 2ab times covariance. Node 3, Conditional and Double Expectation (ch16, outcomes 3c, 3d): E[X] equals the expectation of the conditional expectation E[X given Y], the law of total variance splits Var(X) into expected conditional variance plus variance of the conditional mean, and the compound model gives E[S] equals E[N] times mu and Var(S) equals E[N] sigma-squared plus Var(N) mu-squared. Node 4, Order Statistics (ch17, outcome 3f): the CDF of the maximum is F to the n, the CDF of the minimum is one minus the survival function to the n, the minimum of independent exponentials has rates that add, and series systems equal the minimum while parallel systems equal the maximum. Real mascot sprites Charmander, Rhyhorn, and Lapras decorate the outer margins. A banner at the bottom reads: variables now move together — a team is a sum of correlated parts, a threat is averaged over a hidden tier, a champion is the maximum of the field.">
<figcaption>The whole of Act III on one page. Read it top to bottom as a dependency chain: you need a <em>joint</em> law before you can ask how the pair <em>co-moves</em>; co-movement feeds the <em>variance of a sum</em>; conditioning on a hidden layer drives <em>double expectation and total variance</em>; and sorting a draw gives the <em>order statistics</em>. One spine, four landmarks.</figcaption>
</figure>

::: trainers-tip
**60-SECOND RETRIEVAL — one load-bearing idea per Act-III chapter**

Cover the italic answer. Reconstruct each from memory; if any feels shaky, flip back to that chapter *before* the drills.

1. **(ch14 — joint → marginal.)** You have a joint density $f_{X,Y}(x,y)$. How do you get the marginal $f_X(x)$, and what must $\iint f_{X,Y}$ equal over the whole support? *(Answer: integrate the joint over the other variable, $f_X(x)=\int f_{X,Y}(x,y)\,dy$; the total double integral is $1$.)*
2. **(ch15 — covariance & the cross term.)** Write $\Cov(X,Y)$ in terms of expectations, and $\Var(aX+bY)$ in full. *(Answer: $\Cov(X,Y)=\E[XY]-\E[X]\E[Y]$; $\Var(aX+bY)=a^2\Var(X)+b^2\Var(Y)+2ab\,\Cov(X,Y)$ — the cross term vanishes only when uncorrelated.)*
3. **(ch16 — double expectation & total variance.)** State both laws. *(Answer: $\E[X]=\E[\E[X\mid Y]]$; $\Var(X)=\E[\Var(X\mid Y)]+\Var(\E[X\mid Y])$ — process plus parameter, **added**, never averaged.)*
4. **(ch17 — order statistics.)** Give the CDF of the maximum and of the minimum of $n$ i.i.d. variables, and the rule for the min of independent exponentials. *(Answer: $F_{\max}(x)=[F(x)]^n$; $F_{\min}(x)=1-[S(x)]^n$; the minimum of independent exponentials is exponential whose **rate is the sum of the rates**.)*

All four instant? You're ready for mixed fire. Any hesitation? The retrieval *is* the diagnosis — go reclaim that one chapter, then come back. This checkpoint is built to find exactly the idea you haven't locked yet.
:::

## The Qualifier — How This Checkpoint Works

There is no Oak's Briefing of new outcomes here and no test-out gate, because there is nothing new to test out *of*: every outcome below (3a, 3b, 3c, 3d, 3e, 3f, 3g) was discharged in ch14–ch17. What this chapter does is **interleave** them. The exam never tells you "this is a covariance problem"; it hands you a scenario and you must *recognize* the structure. Interleaved, unlabeled retrieval is harder than blocked practice — and that difficulty is precisely why it builds exam-durable memory.

The twelve drills are one connected **League-qualifier mission**, the night's final preparation, escalating in three rounds:

- **Round 1 — Route Trainers (C18.1–C18.6):** one warm-up per landmark, lightly scaffolded — joint marginal, covariance, variance of a combination, compound moments, total variance, the maximum.
- **Round 2 — Gym Battles (C18.7–C18.11):** true exam difficulty, fully unlabeled, including the act's two recycled traps (the "zero covariance means independent" audit and the dropped-cross-term rival trap) and the dropped-count-term compound audit.
- **Round 3 — Elite Challenge (C18.12):** the Plateau-grade synthesis — every Act-III idea nested into one two-layer threat.

> **Read each scenario and decide *which of the four landmarks* it is before you compute.** That recognition step is the whole skill this checkpoint trains.

## The Gym Challenge — The League-Qualifier Gauntlet

::: problem-set
**THE LEAGUE-QUALIFIER GAUNTLET — your final-night mission.** No badge rides on this — all eight are already yours. What rides on it is the championship tomorrow. Work each problem **timed (~6 min)**, deciding first which Act-III landmark it belongs to, then solving. Full worked solutions follow in **Answers** (never interleaved). Markers: 🔴 routine method · 🟡 routine-with-a-twist · 🔵 stretch. Source tags name the chapter each problem retrieves.

### Round 1 — Route Trainers (one warm-up per landmark)

**C18.1.** 🟡 *(ch14 — joint distribution.)* Two paired battle readings $(X,Y)$ have joint density $f(x,y)=x+y$ on the unit square $0<x<1,\ 0<y<1$ (and $0$ elsewhere). Find the marginal density $f_X(x)$, then $\E[X]$.

**C18.2.** 🔴 *(ch15 — covariance.)* Contenders $X\in\{0,1,2\}$ and $Y\in\{0,1\}$ have joint pmf $P(0,0)=0.30,\ P(0,1)=0.10,\ P(1,0)=0.10,\ P(1,1)=0.20,\ P(2,0)=0.05,\ P(2,1)=0.25$. Find $\Cov(X,Y)$ and state the sign of the association.

**C18.3.** 🔴 *(ch15 — variance of a linear combination.)* A vanguard's net effect is $2X-Y$, where $\Var(X)=4$, $\Var(Y)=9$, $\Cov(X,Y)=-2$. Find $\Var(2X-Y)$.

**C18.4.** 🔴 *(ch16 — compound distribution.)* An opponent lands $N\sim\Poisson(\lambda{=}4)$ strikes; each does i.i.d. damage with $\mu=10$, $\sigma^2=25$. Let $S=\sum_{i=1}^N X_i$. Find $\E[S]$ and $\Var(S)$.

**C18.5.** 🟡 *(ch16 — law of total variance.)* Match difficulty $X$ depends on the arena $Y$: arena 1 ($P=0.6$) has $\E[X\mid 1]=30$, $\Var(X\mid 1)=16$; arena 2 ($P=0.4$) has $\E[X\mid 2]=50$, $\Var(X\mid 2)=36$. Find $\E[X]$ and $\Var(X)$, and state which source dominates.

**C18.6.** 🔴 *(ch17 — the maximum.)* Four trainers post i.i.d. scores $X_i\sim\Unif(0,1)$. Let $M=\max$ of the four. Find the CDF of $M$ and $\E[M]$.

> *Questline beat: the four landmarks are warm. Now they come unlabeled and at exam speed.*

### Round 2 — Gym Battles (true exam difficulty, unlabeled)

**C18.7.** 🟡 *(ch17 — min of exponentials.)* Two independent attacks have charge times $T_1\sim\Expo(\text{mean}{=}10)$ and $T_2\sim\Expo(\text{mean}{=}15)$ seconds. The first to fire is $W=\min(T_1,T_2)$. Find the distribution of $W$ and $\E[W]$.

**C18.8.** 🟡 *(AUDIT — ch15: independence vs zero correlation.)* A reading $X$ is uniform on $\{-1,0,1\}$ (each prob. $1/3$), and $Y=X^2$. A Rocket analyst writes: "$\Cov(X,Y)=0$, therefore $X$ and $Y$ are independent." Compute $\Cov(X,Y)$, decide whether $X$ and $Y$ are independent, and name the error.

**C18.9.** 🟡 *(RIVAL TRAP — ch15: dropped cross term.)* Gary's two lead Pokémon have scores $X$ and $Y$ with $\Var(X)=\Var(Y)=25$ and correlation $\rho=0.6$. Gary brags: "Combined variance? Just $25+25=50$." Find the true $\Var(X+Y)$ and say where he erred.

**C18.10.** 🔵 *(AUDIT — ch16: dropped count term.)* Total strike damage is $S=\sum_{i=1}^N X_i$ with $N\sim\Poisson(\lambda{=}6)$ and i.i.d. severities $\mu=20$, $\sigma^2=100$. A Rocket memo reports "$\Var(S)=\E[N]\sigma^2=6(100)=600$." Find the true $\E[S]$ and $\Var(S)$ and name the dropped term.

**C18.11.** 🔵 *(ch17 — series reliability = minimum.)* A relay has three independent components in **series** with exponential lifetimes of means $4$, $6$, and $12$ minutes. The relay fails when the first component fails, i.e. $L=\min$ of the three. Find the distribution of $L$ and $\E[L]$.

> *Questline beat: the traps are sprung and survived. One synthesis problem stands between you and the championship.*

### Round 3 — Elite Challenge (Plateau-grade synthesis)

**C18.12.** 🔵 *(ch16 + ch15 — two-layer compound mixture.)* The anchor's tier $Y$ is drawn with $P(Y{=}1)=0.5$, $P(Y{=}2)=0.3$, $P(Y{=}3)=0.2$. Given tier $y$, damage $X$ is compound-Poisson with attack-count mean $\lambda_y$ and per-attack severity mean $\mu_y$, variance $\sigma_y^2$:

| Tier $y$ | $P(Y{=}y)$ | $\lambda_y$ | $\mu_y$ | $\sigma_y^2$ |
|---|---|---|---|---|
| 1 | $0.5$ | $2$ | $10$ | $25$ |
| 2 | $0.3$ | $3$ | $15$ | $49$ |
| 3 | $0.2$ | $5$ | $20$ | $100$ |

Find $\E[X]$, $\Var(X)$, and the fraction of total variance attributable to *which tier* fights.
:::

## Answers

::: answer-key
**Full worked solution per problem, source-chapter labeled. Each opens by naming which of the four Act-III landmarks it is — the recognition step the exam demands. A quick-answer table closes the section.**

**C18.1** — *(ch14 · joint → marginal → mean.)* **Landmark: joint distribution.** Marginalize out $Y$:
$$f_X(x)=\int_0^1 (x+y)\,dy = x + \tfrac12, \qquad 0<x<1.$$
$$\E[X]=\int_0^1 x\Big(x+\tfrac12\Big)\,dx = \int_0^1\Big(x^2+\tfrac{x}{2}\Big)dx = \tfrac13+\tfrac14 = \tfrac{7}{12}\approx 0.5833.$$

**C18.2** — *(ch15 · covariance from a joint table.)* **Landmark: joint moments.** Marginals: $P(X{=}0,1,2)=0.4,0.3,0.3\Rightarrow\E[X]=0.9$; $P(Y{=}0,1)=0.45,0.55\Rightarrow\E[Y]=0.55$. Only the $(1,1)$ and $(2,1)$ cells contribute to $\E[XY]$:
$$\E[XY]=(1)(1)(0.20)+(2)(1)(0.25)=0.70.$$
$$\Cov(X,Y)=0.70-(0.9)(0.55)=0.70-0.495=0.205\;(>0,\text{ positive association}).$$

**C18.3** — *(ch15 · variance of a linear combination.)* **Landmark: variance of a sum.** With $a=2$, $b=-1$:
$$\Var(2X-Y)=2^2\Var(X)+(-1)^2\Var(Y)+2(2)(-1)\Cov(X,Y)=16+9+8=33.$$
(The cross term $2ab\,\Cov=(-4)(-2)=+8$ — note both the coefficient sign and the negative covariance flip it positive.)

**C18.4** — *(ch16 · compound-Poisson moments.)* **Landmark: compound distribution.**
$$\E[S]=\lambda\mu=4(10)=40.$$
$$\Var(S)=\lambda\,\E[X^2]=\lambda(\sigma^2+\mu^2)=4(25+100)=4(125)=500.$$

**C18.5** — *(ch16 · law of total variance.)* **Landmark: conditional / total variance.**
$$\E[X]=30(0.6)+50(0.4)=38.$$
Term 1 (process): $\E[\Var(X\mid Y)]=16(0.6)+36(0.4)=24$. Term 2 (parameter): means $30,50\Rightarrow\E[g^2]=900(0.6)+2500(0.4)=1540$, $\Var(g)=1540-38^2=96$.
$$\Var(X)=24+96=120.$$
The **between-arena spread ($96$)** dominates the within-arena noise ($24$) — most of the uncertainty is *which* arena, not the arena's own variability.

**C18.6** — *(ch17 · the maximum of i.i.d. variables.)* **Landmark: order statistics.** Independent maxima multiply CDFs:
$$F_M(x)=[F(x)]^4=x^4 \quad (0<x<1), \qquad f_M(x)=4x^3.$$
$$\E[M]=\int_0^1 x(4x^3)\,dx=\tfrac{4}{5}=0.8 \quad\Big(\text{general: } \tfrac{n}{n+1}\Big).$$

**C18.7** — *(ch17 · minimum of independent exponentials.)* **Landmark: order statistics (the min).** For independent exponentials the minimum is exponential with rate = **sum of the rates**:
$$\text{rate}=\tfrac{1}{10}+\tfrac{1}{15}=\tfrac{3}{30}+\tfrac{2}{30}=\tfrac{5}{30}=\tfrac16 \;\Rightarrow\; W\sim\Expo(\text{mean}{=}6),\quad \E[W]=6\text{ s}.$$

**C18.8** — *(audit · ch15: independence vs zero correlation.)* **Landmark: joint moments / the one-way street.** $\E[X]=0$, $\E[X^2]=\tfrac23$, and $\E[XY]=\E[X^3]=\tfrac{(-1)+0+1}{3}=0$, so
$$\Cov(X,Y)=\E[XY]-\E[X]\E[Y]=0-0=0.$$
**Yet $X$ and $Y$ are not independent:** $Y=X^2$ is a *deterministic function of $X$* — knowing $X$ pins $Y$ exactly. **The error:** zero covariance only rules out a *linear* relationship; it never implies independence. The implication runs **one way only**: independence $\Rightarrow\Cov=0$, but $\Cov=0\not\Rightarrow$ independence.

**C18.9** — *(rival_trap · ch15: dropped cross term.)* **Landmark: variance of a sum.** First the covariance from the correlation:
$$\Cov(X,Y)=\rho\,\sigma_X\sigma_Y=0.6(5)(5)=15.$$
$$\Var(X+Y)=\Var(X)+\Var(Y)+2\Cov(X,Y)=25+25+2(15)=80.$$
**Gary is wrong.** He used $\Var(X+Y)=\Var(X)+\Var(Y)=50$, valid only when **uncorrelated**. With $\rho=0.6$ the team is positively correlated, so the dropped cross term $2\Cov=30$ pushes the true variance to $80$ — $60\%$ above his estimate.

**C18.10** — *(audit · ch16: dropped count term.)* **Landmark: compound distribution.**
$$\E[S]=\E[N]\mu=6(20)=120.$$
$$\Var(S)=\E[N]\sigma^2+\Var(N)\mu^2=6(100)+6(400)=600+2400=3000.$$
(Compound-Poisson shortcut: $\lambda\,\E[X^2]=6(100+400)=3000$ ✓.) **Dropped term:** the memo kept only the size-noise term $\E[N]\sigma^2=600$ and ignored the **count-noise term $\Var(N)\mu^2=2400$** — that the *number* of strikes is itself random. The true variance is $3000$, five times the claimed $600$.

**C18.11** — *(ch17 · series reliability = minimum.)* **Landmark: order statistics (the min).** A series system fails at the *first* component failure, so its lifetime is the **minimum**. For independent exponentials the rates add:
$$\text{rate}=\tfrac14+\tfrac16+\tfrac{1}{12}=\tfrac{3+2+1}{12}=\tfrac{6}{12}=\tfrac12 \;\Rightarrow\; L\sim\Expo(\text{mean}{=}2),\quad \E[L]=2\text{ min}.$$

**C18.12** — *(elite · ch16 + ch15: two-layer compound mixture.)* **Landmark: every Act-III idea at once — compound damage nested in a tier mixture.** Within a tier, $X$ is compound-Poisson, so (ch16) the conditional mean is $\lambda_y\mu_y$ and the conditional variance is $\lambda_y(\sigma_y^2+\mu_y^2)$.

Conditional means $\lambda_y\mu_y$: $2(10)=20$, $3(15)=45$, $5(20)=100$.
$$\E[X]=20(0.5)+45(0.3)+100(0.2)=10+13.5+20=43.5.$$
Conditional variances $\lambda_y(\sigma_y^2+\mu_y^2)$: $2(125)=250$, $3(274)=822$, $5(500)=2500$.
Term 1 (within-tier, process): $250(0.5)+822(0.3)+2500(0.2)=125+246.6+500=871.6$.
Term 2 (between-tier, parameter): $\E[g^2]=20^2(0.5)+45^2(0.3)+100^2(0.2)=200+607.5+2000=2807.5$; $\Var(g)=2807.5-43.5^2=2807.5-1892.25=915.25$.
$$\Var(X)=871.6+915.25=1786.85.$$
Tier fraction $=915.25/1786.85\approx 0.512$ — **about $51\%$** of the variance is *which tier* fights, the other $\approx 49\%$ the within-tier compound noise. The two layers are nearly balanced: fear the dice and the Pokémon about equally.

### Quick-Answer Table

| # | Answer | | # | Answer |
|---|---|---|---|---|
| C18.1 | $f_X=x+\tfrac12;\ \E[X]=\tfrac{7}{12}$ | | C18.7 | $W\sim\Expo(\text{mean}{=}6);\ \E[W]=6$ |
| C18.2 | $\Cov=0.205$ (positive) | | C18.8 | $\Cov=0$ but **dependent** ($Y{=}X^2$) |
| C18.3 | $\Var(2X-Y)=33$ | | C18.9 | $\Var(X+Y)=80$ (Gary dropped $2\Cov$) |
| C18.4 | $\E[S]=40,\ \Var(S)=500$ | | C18.10 | $\E[S]=120,\ \Var(S)=3000$ (dropped $\Var(N)\mu^2$) |
| C18.5 | $\E[X]=38,\ \Var(X)=120$ (arena) | | C18.11 | $L\sim\Expo(\text{mean}{=}2);\ \E[L]=2$ |
| C18.6 | $F_M=x^4;\ \E[M]=0.8$ | | C18.12 | $\E[X]=43.5,\ \Var(X)=1786.85,\ \approx 51\%$ tier |
:::

## The Pass Gate — Are You Champion-Ready?

::: concept-gate
**CHECKPOINT B PASS GATE — the readiness bar**

This is the explicit bar for Act III. Score yourself on the twelve drills, **correct method required** (a right number by a wrong route does not count — the exam will punish the route on the next variant).

- **PASS — Champion-ready (10–12 / 12 with correct method).** Including **both** recycled traps (C18.8 the false "uncorrelated ⇒ independent," C18.9 the dropped cross term) and **both** compound audits (C18.10 the dropped count term, C18.12 the nested synthesis). Act III is exam-durable. **Proceed to ch19 — the Championship.**
- **NOT YET — review and re-test (≤ 9 / 12, or any landmark missed by method).** This is information, not failure: the miss tells you exactly which of the four landmarks hasn't locked. Do the **spaced-retrieval fail path** below, then retake this gauntlet **in two days** (spacing the retest is what converts it to long-term memory — not cramming it again tonight).

**Diagnostic — map each miss to its repair:**

| If you missed… | The landmark that slipped | Go back to | Then re-drill |
|---|---|---|---|
| C18.1, C18.6 | joint density / marginals / max CDF | ch14 Concept 2, ch17 Concept 1 | C18.1, C18.6 |
| C18.2, C18.3, C18.8, C18.9 | covariance, the cross term, the one-way street | ch15 Concepts 2, 4, 5 | C18.2, C18.3, C18.9 |
| C18.4, C18.5, C18.10, C18.12 | total variance / compound / mixture | ch16 Concepts 3, 4 | C18.5, C18.10 |
| C18.7, C18.11 | min of exponentials / reliability | ch17 Concepts 2, 3, 5 | C18.7, C18.11 |

**Spaced-retrieval fail path:** review the one chapter your misses point to (not all four — target the gap). Sleep on it. In **two days**, redo the *full* gauntlet cold, no notes. Two-day spacing on a re-test outperforms a second pass tonight by a wide margin — that delay is the lesson, not a delay *to* the lesson.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

Everything Act III taught is **portfolio thinking**, and an actuary lives in it. A book of insurance policies is exactly a sum of correlated risks: the **variance of a sum with its cross term** (ch15) is *the* reason diversification works — independent risks let variances simply add, so pooling shrinks relative risk, while correlated risks (a regional storm hitting many policies at once) keep the cross term alive and limit the benefit. The **law of total variance** (ch16) is the engine of **credibility theory** — splitting a risk's variability into process (within-class) and parameter (between-class) pieces. **Compound models** price a year of aggregate claims — a random *number* of claims, each a random *size*. And **order statistics** (ch17) price **reinsurance on the largest loss** and model **system reliability**, where a series of components fails at the first failure (a minimum) and redundant parallel components last until the last failure (a maximum).

The interleaving you just practiced is itself the real skill: a working actuarial problem never arrives labeled "this is a covariance question." You read the situation and recognize the structure — exactly the recognition step this checkpoint drilled.

*Series bridge:* this multivariate toolkit is the direct on-ramp to **CAS Exam MAS-I/MAS-II** (credibility, aggregate loss models) and the loss-modeling content of the SOA's later exams. The "process vs. parameter" split and the frequency-severity decomposition you used in C18.10 and C18.12 are used verbatim there.
:::

## Checkpoint Cleared — On to the Championship

You sat by the fire and walked all of Act III back, mixed and unlabeled, and told each landmark apart on sight. There is no badge for tonight — there was never meant to be. **Rank: Champion-ready · Badges: 8 (all earned).** The only thing left to earn is the title itself.

**Act III mastery checklist — tick each before the championship (mapped to the SOA outcomes):**

- ☐ **(3a, 3b)** Given a joint pmf/pdf, I can find marginals, conditionals, and probabilities over a region, and test independence. *(Drills C18.1; ch14.)*
- ☐ **(3c, 3e, 3g)** I can compute $\E[XY]$ and $\Cov(X,Y)$, read correlation, and find $\Var(aX+bY)$ with its cross term — and I know zero covariance does **not** mean independent. *(Drills C18.2, C18.3, C18.8, C18.9; ch15.)*
- ☐ **(3c, 3d)** I can apply double expectation and the law of total variance, and set up a compound/mixture model with both variance terms. *(Drills C18.4, C18.5, C18.10, C18.12; ch16.)*
- ☐ **(3f)** I can find the distribution and mean of the maximum and minimum of $n$ i.i.d. variables, including the min of independent exponentials and series/parallel reliability. *(Drills C18.6, C18.7, C18.11; ch17.)*

> Next stop: the **Indigo Plateau championship — ch19**, where there are no warm-ups and no labels: three full, weight-matched mock exams under six-minute pacing. You've cleared every gym, every gauntlet, and every checkpoint. Go become the Champion.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
