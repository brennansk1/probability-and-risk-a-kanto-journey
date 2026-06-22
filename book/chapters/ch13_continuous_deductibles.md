<!--
  file: ch13_continuous_deductibles
  tier: B
  outcomes: 2e,2f
  tia: B.5 (B.5.1 deductibles calculus approach; B.5.2 deductibles cases approach;
       B.5.3 review of other continuous ideas — the Act II checkpoint fold)
  locale: Cinnabar Lab (volcano coverage) / Oak & Blaine / fire / no badge
  maps_to: the Cinnabar research-station coverage commission — a continuous loss X
           reshaped into a payment by a deductible (X-d)+, a limit X^u, and
           coinsurance, priced TWO ways: (1) the CALCULUS approach via survival
           integrals E[(X-d)+]=int_d^inf S(x)dx and E[X^u]=int_0^u S(x)dx with the
           master identity and the exponential memoryless shortcut; (2) the CASES
           approach, splitting the payment piecewise and integrating the loss
           density directly. Then a review of the continuous act (B.5.3).
  NOTE: this is the CONTINUOUS deductible chapter (densities, survival integrals).
        Its discrete twin is ch06 (Fuchsia / Safari Zone) — same four operations,
        sums instead of integrals.
-->

# A Payment Is a Reshaped Loss — Now with Integrals {.type-fire}

<figure>
<img src="../../assets/maps/kanto_ch13.png" alt="Kanto town map with Cinnabar Island highlighted off the southern coast: a volcanic island holding Blaine's fire gym, the Pokemon Lab, and the burned-out Pokemon Mansion, reached by sea after the Grand Gathering." style="width:70%; max-width:520px; display:block; margin:1em auto;">
<figcaption>Across the water to <strong>Cinnabar Island</strong> — a live volcano holding the <strong>Pokémon Lab</strong>, the burned-out Mansion, and Blaine's fire gym. Oak has a coverage job for you here before the gym; no badge is pinned in this chapter, but the math is the most directly actuarial you have met.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "Volcanic Panic"**

The ferry drops you on **Cinnabar Island** under a sky the color of ash. The ground is warm through your boots; far below the Pokémon Lab, the island's volcano grumbles. Professor Oak is here ahead of you, leaning over a bench of scorched equipment with a Lab researcher who looks like he hasn't slept.

"Ash — good. The Lab insures its field gear against the volcano," Oak says, tapping a charred spectrometer. "Eruptions, gas vents, lava spatter — every event damages equipment by some random amount. The Lab's old policy reimbursed *every* Poké-dollar of damage, and the volcano is about to bankrupt them. So they're rewriting the policy: the Lab eats the first few thousand of any damage itself" — **a deductible** — "the insurer caps what it records on any single event" — **a limit** — "and after that they split the cost" — **coinsurance**.

"You priced exactly this at the Safari Zone," Oak goes on, "back when the loss was a tidy little *table* you could sum by hand. But a volcano doesn't deal in tidy tables. The damage to a piece of gear is a **continuous** quantity — it can be any positive number — so its distribution is a smooth **density** $f(x)$, not a list of probabilities. The question the Lab needs is the same one the Warden asked: *when an event damages our gear, on average how much does the policy pay?*"

You open the Pokédex's Actuary Mode. The loss $X$ is a continuous random variable, and the payment is that loss with its bottom knocked off, its top capped, and the middle scaled — a brand-new random variable $Y$. At the Safari Zone you summed a payment table. Here there is no table to sum.

*How do you find the expected payment when the loss is a continuous density — and is there more than one road to the answer?*
:::

## Where You Are — 60-Second Retrieval

**Rank: Ace Trainer · Badges: 6 (Cascade, Thunder, Boulder, Rainbow, Soul, Marsh).** You are deep into Act II, the continuous world. Two tools you have carried across the smooth wilds now meet and combine here:

- From **Fuchsia (ch06)**, the **discrete deductible model**: a payment is a *function* $g(X)$ of the loss — knock off the bottom with $(X-d)_+$, cap the top with $X\wedge u=\min(X,u)$, scale by coinsurance $\alpha$ — and you average it. There you summed $\sum_k g(k)\,p(k)$.
- From **Saffron / Silph (ch10)**, the **continuous survival method**: for a non-negative loss, the mean is the area under the survival curve,
$$\E[X]=\int_0^\infty S(x)\,dx, \qquad S(x)=1-F(x)=P(X>x).$$

This chapter fuses them: the **same four operations** from the Safari Zone, computed with the **survival integral** instead of a sum. Every result is a piece of the area under $S(x)$. Take sixty seconds and prove you still own both halves.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own ch06 + ch10**

Answer from memory; if any feels shaky, flip back before continuing.

1. For $X\sim\Expo(\theta)$ with mean $\theta=10$, what is the survival function $S(x)=P(X>x)$? *(Answer: $e^{-x/10}$.)*
2. What does $\int_0^\infty S(x)\,dx$ compute, and what is it for that $\Expo(10)$? *(Answer: $\E[X]$; it equals $10$.)*
3. In the discrete chapter, the per-loss payment under a deductible was $(X-d)_+$. Is $\E[(X-d)_+]$ equal to $\E[X]-d$? *(Answer: **no** — losses below $d$ pay $0$, not a negative amount; the floor at zero makes the true payment larger than $\E[X]-d$.)*
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP059 "Volcanic Panic"**

<figure><img src="../../assets/stills/ch13_now_playing.jpg" alt="The live volcano venting steam and ash over Cinnabar Island (Indigo League EP059)." style="width:60%; max-width:440px; display:block; margin:0.4em auto;"><figcaption style="font-size:0.8em; color:#555;">Cinnabar's live volcano, EP059 — the uncapped loss the deductible and the policy limit are built to tame.</figcaption></figure>

In **EP059** Ash and friends reach **Cinnabar Island** and its rumbling volcano; the heroes explore the island and its scientific facilities while the volcano's activity drives the danger of the episode. (Our cold-open's "Lab insures its field gear against the volcano" coverage commission is an *in-world extension* invented to motivate the math — the on-screen events are the island visit and the volcanic threat, not an insurance bench. Blaine's fire gym and the Volcano Badge are the focus of the **next** chapter, ch14.) *Watch EP059 before this chapter for the Cinnabar setting and the live-volcano stakes the whole pricing problem rides on.*
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak straightens up from the charred bench and speaks into the Pokédex.

"Ash — this is the chapter where your continuous tools pay a real wage. The single idea is the one you already met at Fuchsia: **a payment is a transformation of a loss.** What's new is *the loss is now a density*, so the four operations — deductible, limit, coinsurance, inflation — are computed with **integrals**. And there are **two roads** to every answer, and a complete actuary owns both. The **calculus approach** turns each payment into an *area under the survival curve* — fast, and it's almost free for an exponential. The **cases approach** splits the loss into pieces and *integrates the density directly* on each piece — slower, but it works for *any* density, even ones with no shortcut. This is a **Tier B** chapter, but the two roads earn their full treatment."

By the end of this chapter you will be able to:

- **Use the calculus approach** to find the expected per-loss payment under an ordinary deductible, $\E[(X-d)_+]=\int_d^{\infty}S(x)\,dx$, and the limited expected value $\E[X\wedge u]=\int_0^{u}S(x)\,dx$, and deploy the **master identity** $\E[X]=\E[X\wedge u]+\E[(X-u)_+]$. *(Outcome 2e.)*
- **Use the cases approach** — split the per-loss payment into a piecewise function of $X$ and integrate the loss density on each case — to price a full policy (deductible, limit, **coinsurance** $\alpha$, **inflation** $(1+r)$) in the order **inflation → deductible → limit → coinsurance**, for *any* loss density. *(Outcome 2e.)*
- **Distinguish per-loss from per-payment** expectation (dividing by $S(d)=P(X>d)$), and exploit the **exponential memoryless shortcut** $\E[(X-d)_+]=\theta e^{-d/\theta}$, $\E[X-d\mid X>d]=\theta$. *(Outcome 2f.)*
- **Review and retrieve the whole continuous act** (Act II checkpoint) — densities, CDFs, moments, the survival method, and the key continuous distributions — at exam speed. *(B.5.3.)*

> *Exam-weight signpost.* Continuous severity-with-coverage-modifications is a small but **highly reliable** slice of Exam P (outcomes 2e–2f), and it rewards method-fluency over memorization. Almost every problem reduces to a choice you control: *take the area under $S(x)$ (calculus), or split into cases and integrate the density.* Pick the road that fits the loss in front of you. **Tier B:** full treatment of both roads, but the exponential keeps the arithmetic light.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own All of Cinnabar?**

Already fluent? Prove it. ~5 minutes each, *with correct method*.

1. $X\sim\Expo(\theta=10)$, ordinary deductible $d=3$. Find the expected payment **per loss**, $\E[(X-3)_+]$.
2. Same $X$ and $d$. Find the expected payment **per payment**.
3. $X\sim\Unif(0,20)$, deductible $d=5$, maximum covered loss $u=15$, $\alpha=1$. Find the expected payment per loss (the covered layer).
4. This year $X\sim\Expo(10)$ with a fixed deductible $d=4$; next year losses inflate $25\%$ but the deductible stays. Find next year's per-loss payment and the percentage rise over this year.

*(Answers: (1) $10e^{-0.3}\approx7.408$; (2) $\theta=10$; (3) $\E[X\wedge15]-\E[X\wedge5]=5.0$; (4) $12.5\,e^{-0.32}\approx9.077$, a $+35.4\%$ rise.)* Four for four with the right reasoning? **Skip to the Review (Concept 3) and the Gym Challenge.** Any miss or hesitation? Each concept below has its own skip-gate, so even a partial owner loses no time.
:::

---

We build three sections, in TIA's order (B.5.1 → B.5.2 → B.5.3) and increasing difficulty. The first two are the two *roads* to a continuous payment; the third reviews the continuous act.

1. **The calculus approach** — every payment is an *area under the survival curve* $S(x)$ *(B.5.1)*
2. **The cases approach** — split the payment into pieces and integrate the density directly; coinsurance, inflation, per-loss vs per-payment *(B.5.2)*
3. **Review of the continuous act** — a spaced-retrieval checkpoint over Act II *(B.5.3)*

**The chapter's loss random variable.** A volcanic event damages a piece of Lab gear by $X\ge 0$ (in **thousands** of Poké-dollars). The Lab's headline model is **exponential with mean $\theta=10$**, so
$$f(x)=\tfrac{1}{10}e^{-x/10},\qquad F(x)=1-e^{-x/10},\qquad S(x)=e^{-x/10},\qquad \E[X]=\theta=10.$$
A second piece of gear — a fragile core-sample drill — follows a **non-exponential** density we'll meet in Concept 2, precisely to show off the cases approach.

## Concept 1 — The Calculus Approach: Payments Are Areas Under $S(x)$ {#concept-1}

::: concept-gate
**DO YOU ALREADY OWN THIS? — The survival-integral approach**

A loss $X\sim\Expo(\theta=10)$ hits a policy with an ordinary deductible $d=4$ (no limit, no coinsurance). Find the expected payment **per loss**.

If you wrote **$\E[(X-4)_+]=\int_4^\infty e^{-x/10}\,dx = 10e^{-0.4}\approx6.703$** (and you know *why it is not* $\E[X]-d=6$), **skip to Concept 2**. If you reached for $10-4=6$, read on — that subtraction is the canonical trap, dismantled below.
:::

**Beat 1 — The one-sentence idea.** *The expected per-loss payment under a deductible is the area under the survival curve to the **right** of $d$; the limited expected value is the area to the **left** of $u$ — so every continuous payment is a slice of the same area that makes $\E[X]$.*

**Beat 2 — Anchor + concrete instance.** At Fuchsia you summed the survival $S(k)$ from $d$ onward to get $\E[(X-d)_+]$. The continuous world does the identical thing with the survival *curve*: replace the sum by an integral. Here is the Lab's cleanest case. A volcanic event damages gear by $X\sim\Expo(10)$, so $S(x)=e^{-x/10}$. The trial policy has an ordinary deductible $d=4$, no limit, no coinsurance. **When an event strikes, what does the policy pay on average?**

**Beat 3 — Reason through it in plain words.** Sort the events by how much gear they wrecked.

- If the damage is $\le 4$ thousand, the Lab absorbs the whole thing and the policy pays **nothing** — a flat $0$.
- If the damage is, say, $9$ thousand, the Lab eats the first $4$ and the policy pays the **excess**, $9-4=5$ thousand.

So the payment is the loss with its bottom $4$ knocked off, never below zero. Many events are small, so a big pile of them pay exactly $0$. The average payment must therefore be *smaller* than the average loss — but by how much? We need "loss minus $4$," summed only over the events that actually exceed $4$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** *(This is the first half of Team Rocket's trap for the chapter.)* The seductive move is to subtract the deductible from the *mean*:
$$\E[(X-d)_+]\stackrel{?}{=}\E[X]-d=10-4=6. \qquad\textbf{(wrong)}$$
This silently assumes *every* loss is at least $4$, so $4$ is shaved off all of them. But a loss of $0.5$ can't pay a *negative* $-3.5$ — it pays $0$. The floor at zero means the deductible removes *less* than $4$ on average, so the true payment is *bigger* than $6$. Subtracting $d$ from the mean over-counts the deductible. The correct answer, $6.703$, sits above $6$ for exactly this reason: **you cannot pay a negative amount, so the deductible's bite is blunted by the lump of probability at zero.**

**Beat 5 — Translate into notation, one glyph at a time.** Name the payment. Let $Y_L$ be the **per-loss payment** — the payment recorded for *every* event, counting the zeros. The notation is the **positive-part** symbol:
$$Y_L=(X-d)_+ \qquad\text{where}\quad (x-d)_+=\max(x-d,\,0).$$
Read $(X-d)_+$ aloud as "$X$ minus $d$, **floored at zero**." Its expectation, written as an integral, sums the payment $(x-d)$ against the density only where the payment is positive ($x>d$):
$$\E[(X-d)_+]=\int_d^{\infty}(x-d)\,f(x)\,dx.$$

**Beat 6 — Derive the survival-integral shortcut.** That integral drags a clumsy $(x-d)$ through it. Watch it collapse. Integrate by parts, with $u=(x-d)$ and $dv=f(x)\,dx$ (so $v=-S(x)$, since $S'(x)=-f(x)$):
$$\int_d^\infty (x-d)\,f(x)\,dx = \Big[-(x-d)\,S(x)\Big]_d^\infty + \int_d^\infty S(x)\,dx.$$
The boundary term vanishes at both ends — at $x=d$ the factor $(x-d)=0$, and at $\infty$ the survival $S(x)\to0$ faster than $(x-d)$ grows (true for every Exam-P loss). What's left is clean:
$$\boxed{\;\E[(X-d)_+]=\int_d^{\infty}S(x)\,dx.\;}$$
We did not assert this — we *derived* it. The expected per-loss payment is **the area under the survival curve, to the right of the deductible.** No more dragging $(x-d)$ through an integration by parts every time. The same parts argument run on $X\wedge u=\min(X,u)$ gives its mirror image (the capped variable's survival is $S(x)$ up to the cap, then $0$):
$$\boxed{\;\E[X\wedge u]=\int_0^{u}S(x)\,dx.\;}$$
The deductible keeps the area to the *right* of $d$; the limit keeps the area to the *left* of $u$. Finish the concrete case. For $\Expo(10)$, $S(x)=e^{-x/10}$:
$$\E[(X-4)_+]=\int_4^\infty e^{-x/10}\,dx=\Big[-10e^{-x/10}\Big]_4^\infty=10e^{-0.4}\approx 6.703\text{ (thousand)},$$
above the $6$ the wrong method gave, exactly as Beat 4 promised.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* read $S(x)$ off the distribution and integrate from $d$ to $\infty$, as above.
- *Twist — the master identity.* Put the two areas side by side. The deductible at $u$ uses $\int_u^\infty S(x)\,dx$; the limit uses $\int_0^u S(x)\,dx$. Add them and the whole survival curve reassembles:
$$\underbrace{\int_0^u S(x)\,dx}_{\E[X\wedge u]} + \underbrace{\int_u^\infty S(x)\,dx}_{\E[(X-u)_+]} = \int_0^\infty S(x)\,dx = \E[X].$$
So $\E[X]=\E[X\wedge u]+\E[(X-u)_+]$ — hand me any two, the identity returns the third with no distribution at all. For our $\Expo(10)$ with $u=12$: $\E[X\wedge12]=10(1-e^{-1.2})\approx6.988$ and $\E[(X-12)_+]=10e^{-1.2}\approx3.012$, and $6.988+3.012=10=\E[X]$ ✓.
- *General — the exponential memoryless shortcut.* For $X\sim\Expo(\theta)$, the integral has a one-line value: $\E[(X-d)_+]=\int_d^\infty e^{-x/\theta}\,dx=\theta e^{-d/\theta}$. And **memorylessness** says the conditional excess $(X-d\mid X>d)$ is *again* $\Expo(\theta)$, so the **per-payment** mean is simply $\theta$ — no integral at all.
- *Edge cases:* $d=0$ removes nothing, $\E[(X-0)_+]=\int_0^\infty S=\E[X]=10$; $d\to\infty$ pays $0$; $u\to\infty$ gives $\E[X\wedge u]\to\E[X]$.

**Beat 8 — Picture it.** The figure makes the shortcut literal: the expected per-loss payment is a shaded *area* under the survival curve, starting at the deductible.

<figure>
<img src="../../assets/diagrams/ch13_deductible_calculus.png" alt="The survival curve S(x) = e^{-x/10} for the Cinnabar exponential loss, drawn falling from 1 at x=0 toward 0 as x grows. The whole area under it from 0 to infinity is E[X] = theta = 10. A dashed vertical line at the deductible d = 4 splits the area: the small region to the LEFT of d (from 0 to 4) is shaded blue with a dotted hatch and labelled 'trainer absorbs' (the loss the Lab eats); the large region to the RIGHT of d (from 4 to infinity) is shaded orange with a diagonal hatch and labelled with the formula E[(X-d)+] = integral_d^infinity S(x) dx = theta e^{-d/theta} = 10 e^{-0.4} approximately 6.70. A real Growlithe sprite sits high-right in the empty region where the curve has decayed near zero." style="width:88%; max-width:680px; display:block; margin:1em auto;">
<figcaption>The calculus approach in one picture: $\E[(X-d)_+]$ is the area under $S(x)$ to the <strong>right</strong> of the deductible $d$; $\E[X\wedge u]$ is the area to the <strong>left</strong> of $u$; together they reassemble the whole area $\E[X]=\theta=10$. For $\Expo(10)$ with $d=4$, the orange area is $10e^{-0.4}\approx6.703$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now take any continuous loss with a known survival function, apply a deductible or a limit, and read off the expected payment as an *area under $S(x)$* — to the right of $d$, or to the left of $u$ — never confusing it with the over-counting $\E[X]-d$. For an exponential the area is the one-liner $\theta e^{-d/\theta}$, and the per-payment mean is just $\theta$. That single move — *integrate the survival curve* — is the seed of everything in the chapter.

::: pokedex-entry
**POKÉDEX ENTRY №46 — The Calculus Approach (Survival Integrals)**

$$\E[(X-d)_+]=\int_d^{\infty}S(x)\,dx, \qquad \E[X\wedge u]=\int_0^{u}S(x)\,dx,$$
$$\textbf{Master identity:}\quad \E[X]=\E[X\wedge u]+\E[(X-u)_+].$$
**Exponential shortcut** $X\sim\Expo(\theta)$: $\;\E[(X-d)_+]=\theta e^{-d/\theta}$ (per loss), $\;\E[X-d\mid X>d]=\theta$ (per payment, by memorylessness).

*In plain terms:* the deductible payment is the survival area right of $d$; the limited value is the survival area left of $u$; the two pieces add to the whole loss.

*Recognition cue:* "amount **in excess of** $d$," "after a deductible of $d$" → $\int_d^\infty S(x)\,dx$. "Maximum covered loss / policy records at most $u$" → $\int_0^u S(x)\,dx$. Exponential loss + deductible → write $\theta e^{-d/\theta}$ and $\theta$ on sight. If your payment comes out $\le\E[X]-d$ or negative, you forgot the floor at zero.
:::

## Concept 2 — The Cases Approach: Split, Then Integrate the Density {#concept-2}

::: concept-gate
**DO YOU ALREADY OWN THIS? — The cases approach (any density)**

A core-sample loss $W$ has density $f(w)=\tfrac{w}{50}$ on $[0,10]$ (and $0$ elsewhere). A policy has an ordinary deductible $d=2$. Find the expected payment **per loss** by splitting into cases and integrating the density.

If you wrote **$\E[(W-2)_+]=\int_2^{10}(w-2)\tfrac{w}{50}\,dw=4.693$** (and checked it against $\int_2^{10}S(w)\,dw$ with $S(w)=1-\tfrac{w^2}{100}$), **skip to Concept 3**. If splitting the integral, or where coinsurance and inflation go, is fuzzy, read on.
:::

**Beat 1 — The one-sentence idea.** *The per-loss payment is a **piecewise** function of the loss — flat $0$ below the deductible, a ramp of slope $\alpha$ through the covered layer, flat at the capped payment above $u$ — so you split the loss into those cases and integrate the density $f(x)$ over each piece; this works for **any** loss, even one with no survival-integral shortcut.*

**Beat 2 — Anchor + concrete instance.** The calculus approach was fast because the area-under-$S$ trick hid the piecewise structure. But sometimes you must face that structure head-on — when the density isn't exponential, when there's a limit *and* coinsurance, or when a problem hands you $f(x)$ directly and asks for $\E[g(X)]$. The cases approach is the honest, always-works road: write the payment $g(x)$ as a function of $x$ with one rule per region, then compute $\E[g(X)]=\int g(x)f(x)\,dx$ region by region.

The Lab's fragile **core-sample drill** has damage $W$ with density $f(w)=\tfrac{w}{50}$ on $[0,10]$ — small damages are rare, big damages more likely (the density *rises*). Its survival is $S(w)=1-F(w)=1-\tfrac{w^2}{100}$ and its mean is $\E[W]=\int_0^{10}w\cdot\tfrac{w}{50}\,dw=\tfrac{1000}{150}=\tfrac{20}{3}\approx6.667$. The full Cinnabar policy: deductible $d$, maximum covered loss $u$, coinsurance $\alpha$. **What does it pay on average per event?**

**Beat 3 — Reason through it in plain words.** Walk a single loss $x$ through the policy and see which of three things happens.

- **Case 1 — $x\le d$:** below the deductible. The Lab absorbs it; the policy pays $0$.
- **Case 2 — $d<x\le u$:** in the covered layer. The policy pays the excess above the deductible, scaled by coinsurance: $\alpha(x-d)$.
- **Case 3 — $x>u$:** above the cap. The covered layer is full; the policy pays the capped amount $\alpha(u-d)$ and ignores the rest.

So the payment is a *function* $g(x)$ with three pieces. To average it, integrate $g(x)f(x)$ over each region and add — Case 1 contributes nothing (it pays $0$), Case 2 contributes the ramp, Case 3 contributes the flat cap.

**Beat 4 — Surface and dismantle the tempting wrong idea.** *(This is the other half of Team Rocket's trap.)* The dangerous error is **applying the operations in the wrong order** — and the two classic slips are:

- *Coinsurance or inflation in the wrong place.* Coinsurance is the **last** operation, applied to the finished covered layer; you do *not* scale the loss first and then cap. Inflation is the **first**: it multiplies the **loss** $X$ by $(1+r)$, but the deductible is a fixed dollar amount written into the contract and **does not inflate**. (That single fact makes payments rise *faster* than losses — "deductible erosion.")
- *Deductible after the limit.* If $u$ caps the *payment* rather than the loss, the deductible still comes **first**: $\min((X-d)_+,\,u)$. Capping the loss first and *then* subtracting the deductible is a different, smaller number that can wrongly collapse to zero (the exact mistake Meowth makes below).

The fixed order is **inflation $(1+r)$ → deductible $d$ → limit $u$ → coinsurance $\alpha$.** Run it out of order and every individual step can look right while the answer is wrong.

**Beat 5 — Translate into notation, one glyph at a time.** The per-loss payment for a full policy, written piecewise, is exactly the three cases of Beat 3:
$$Y_L=g(X)=\begin{cases}0, & X\le d,\\[2pt]\alpha\,(X-d), & d<X\le u,\\[2pt]\alpha\,(u-d), & X>u.\end{cases}$$
Read aloud: "zero below the deductible; a ramp of slope $\alpha$ through the layer; flat at $\alpha(u-d)$ above the cap." Its expectation is the density integrated case by case (Case 1 drops out):
$$\E[Y_L]=\int_d^{u}\alpha\,(x-d)\,f(x)\,dx \;+\; \int_u^{\infty}\alpha\,(u-d)\,f(x)\,dx.$$
With **coinsurance** $\alpha$ pulled out front and **inflation** applied to the loss first, the same payment is the compact $Y_L=\alpha\big[((1+r)X\wedge u)-((1+r)X\wedge d)\big]$ — the *covered layer of the inflated loss*, scaled.

**Beat 6 — Derive the concrete case.** Take the core-sample drill $W$ with $f(w)=\tfrac{w}{50}$ on $[0,10]$, deductible $d=2$, no limit, $\alpha=1$ (we add the cap and scaling in Beat 7). Only Case 2 survives, and the upper end of the support is $10$:
$$\E[(W-2)_+]=\int_2^{10}(w-2)\,\frac{w}{50}\,dw=\frac{1}{50}\int_2^{10}(w^2-2w)\,dw=\frac{1}{50}\Big[\tfrac{w^3}{3}-w^2\Big]_2^{10}.$$
Evaluate: at $w=10$, $\tfrac{1000}{3}-100=233.\overline{3}$; at $w=2$, $\tfrac{8}{3}-4=-1.\overline{3}$. The difference is $234.\overline{6}$, so
$$\E[(W-2)_+]=\frac{234.\overline{6}}{50}=4.693\text{ (thousand)}.$$
**Cross-check with the calculus approach** (the two roads must agree): $S(w)=1-\tfrac{w^2}{100}$, so
$$\int_2^{10}\!\Big(1-\tfrac{w^2}{100}\Big)dw=\Big[w-\tfrac{w^3}{300}\Big]_2^{10}=\big(10-\tfrac{1000}{300}\big)-\big(2-\tfrac{8}{300}\big)=6.667-1.973=4.693.\ \checkmark$$
Same $4.693$, two roads — the cases approach integrating the density, the calculus approach integrating the survival curve. When a density has no clean survival shortcut, the cases approach is the one that always lands.

**Beat 7 — Ramp the difficulty.**

- *Add coinsurance:* a co-pay of $\alpha=0.75$ scales the finished layer: $0.75(4.693)=3.520$. (Scale **last**, never before integrating.)
- *Add a cap (the full three-case payment).* For the exponential headline loss $X\sim\Expo(10)$ with $d=4$, $u=12$, $\alpha=0.8$, the cases collapse to a difference of two limited values (Concept 1): $\E[Y_L]=\alpha(\E[X\wedge12]-\E[X\wedge4])=0.8(6.988-3.297)=0.8(3.691)=2.953$.
- *Per loss vs per payment.* A payment happens exactly when the loss clears the deductible, with probability $S(d)=P(X>d)$. So the **per-payment** average (the size of an *actual* cheque) divides the per-loss figure by $S(d)$:
$$\E[Y_P]=\frac{\E[Y_L]}{S(d)},\qquad S(d)=P(X>d).$$
For the full exponential policy, $S(4)=e^{-0.4}=0.6703$, so $\E[Y_P]=2.953/0.6703=4.405$. (Divide by the **deductible's** probability, never the limit's.)
- *Inflation (deductible erosion).* If next year the $\Expo(10)$ losses inflate $25\%$, then $(1+r)X\sim\Expo(12.5)$, but the fixed $d=4$ stays. Per loss: $12.5\,e^{-4/12.5}=12.5\,e^{-0.32}\approx9.077$ — a $+35.4\%$ jump over this year's $10e^{-0.4}=6.703$, *faster* than the $25\%$ loss inflation, because the fixed deductible erodes.

**Beat 8 — Picture it.** The payment as a function of the ground-up loss is the staircase of Beat 5: flat zero up to $d$, a ramp of slope $\alpha$ from $d$ to $u$, then flat at the capped payment $\alpha(u-d)$. The three shaded bands are the three cases you integrate over.

<figure>
<img src="../../assets/diagrams/ch13_cases_approach.png" alt="A graph with ground-up loss x on the horizontal axis and policy payment on the vertical axis, for the Cinnabar full policy with deductible d=4, maximum covered loss u=12, and coinsurance alpha=0.8. A dotted grey diagonal reference line shows what paying the full loss would give. The thick red payment function g(X) is flat at 0 from x=0 to d=4 (CASE 1, x at most d, pays 0, shaded grey), then ramps upward with slope alpha=0.8 from d=4 to u=12 (CASE 2, the covered layer, shaded orange), then goes flat at the capped payment alpha(u-d) = 0.8 times 8 = 6.4 for all x above u=12 (CASE 3, shaded blue). A dotted horizontal line marks the capped payment 6.4. Real Vulpix and Growlithe sprites sit low-right in the flat capped region, well clear of the red curve and all labels." style="width:90%; max-width:720px; display:block; margin:1em auto;">
<figcaption>The cases approach made visual: the per-loss payment $g(X)$ is piecewise — flat $0$ in <strong>Case 1</strong> ($x\le d$), a ramp of slope $\alpha$ through the covered layer in <strong>Case 2</strong> ($d<x\le u$), and flat at $\alpha(u-d)=6.4$ in <strong>Case 3</strong> ($x>u$). You integrate the loss density over each shaded band; Case 1 contributes nothing.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now price a continuous payment two ways and pick the better road for the loss in front of you: the **calculus** survival integral when $S(x)$ is clean (especially exponential), and the **cases** density integral when it isn't. You apply the operations in the fixed order **inflation → deductible → limit → coinsurance**, convert per-loss to per-payment by dividing by $S(d)$, and explain why a fixed deductible makes payments inflate faster than losses.

::: pokedex-entry
**POKÉDEX ENTRY №47 — The Cases Approach, Coinsurance, Inflation & Per-Payment**

Per-loss payment as a piecewise function of $X$, integrated case by case:
$$Y_L=\begin{cases}0,&X\le d\\ \alpha(X-d),& d<X\le u\\ \alpha(u-d),&X>u\end{cases}\qquad \E[Y_L]=\alpha\!\int_d^u(x-d)f(x)\,dx+\alpha(u-d)\!\int_u^\infty f(x)\,dx.$$
Order: **inflation $(1+r)$ → deductible $d$ → limit $u$ → coinsurance $\alpha$** (the deductible does **not** inflate). Per payment: $\;\E[Y_P]=\E[Y_L]/S(d)$, $\;S(d)=P(X>d)$.

*In plain terms:* split the loss into below-$d$ (pays $0$), the covered layer (a ramp), and above-$u$ (the capped payment); integrate the density on each. Works for any loss, shortcut or not.

*Recognition cue:* a density given directly, a non-exponential loss, or two-or-more of {deductible, limit, coinsurance, inflation} → split into cases and integrate $f(x)$. "Given a payment is made / among claims paid" → divide by $S(d)$. Inflation scales $X$; the deductible stays fixed.
:::

## Concept 3 — Review of the Continuous Act (Act II Checkpoint) {#concept-3}

This is the **Act II checkpoint**, folded in here per the syllabus (B.5.3): no new theory, a spaced-retrieval pass over everything from the calculus toolkit through the normal and CLT. The smooth world began at Bill's lighthouse and ends at Cinnabar's bench. Prove you still own it before the multivariate act.

::: trainers-tip
**60-SECOND RETRIEVAL GRID — the continuous act, end to end**

Answer each from memory; the bracketed home chapter tells you where to rematch if one is shaky.

1. **Density vs probability (ch09).** A continuous $X$ has $f(5)=2$. Is that a probability? *(No — $f$ is a density, probability per unit length; $P(X=5)=0$. Only an **area** $\int f$ is a probability, and a density may exceed $1$.)*
2. **CDF ↔ density (ch09).** How do you get $f$ from $F$, and $F$ from $f$? *(\,$f(x)=F'(x)$; $F(x)=\int_{-\infty}^x f(t)\,dt$.)*
3. **Moment by integral (ch10).** Write $\E[X]$ and $\E[g(X)]$ for a continuous $X$. *(\,$\E[X]=\int x f(x)\,dx$; $\E[g(X)]=\int g(x)f(x)\,dx$ — the continuous law of the unconscious statistician.)*
4. **Survival method (ch10).** For a non-negative $X$, $\E[X]=\,$? *(\,$\int_0^\infty S(x)\,dx$ — the engine of this whole chapter.)*
5. **Uniform (ch11).** $X\sim\Unif(a,b)$: mean, variance, and $P(c<X<d)$? *(\,$\tfrac{a+b}{2}$, $\tfrac{(b-a)^2}{12}$, $\tfrac{d-c}{b-a}$ — a length ratio.)*
6. **Exponential (ch11).** $X\sim\Expo(\theta)$: $S(x)$, mean, variance, and the memoryless property? *(\,$e^{-x/\theta}$, $\theta$, $\theta^2$; $(X-s\mid X>s)\sim\Expo(\theta)$ — the clock resets.)*
7. **Gamma (ch11).** A gamma is a sum of what, with mean and variance? *(A sum of $\alpha$ independent $\Expo(\theta)$ waits; mean $\alpha\theta$, variance $\alpha\theta^2$.)*
8. **Normal & standardizing (ch12).** How do you turn $X\sim\Normal(\mu,\sigma^2)$ into a table lookup? *(Standardize: $Z=\tfrac{X-\mu}{\sigma}\sim\Normal(0,1)$, then read $\Phi$.)*
9. **CLT (ch12).** Why does a sum or mean of many i.i.d. losses go normal, and what's the catch on a discrete sum? *(Sums of many independent pieces are approximately normal regardless of the parts; on a discrete sum apply the **continuity correction** $\pm0.5$ before standardizing.)*
10. **This chapter (ch13).** The two roads to a continuous payment? *(Calculus: area under $S(x)$ — right of $d$, left of $u$. Cases: split into pieces, integrate the density.)*
:::

::: pokedex-entry
**POKÉDEX ENTRY №48 — The Continuous Act on One Screen**

| Idea | Key form | Home |
|---|---|---|
| Density / CDF | $f=F'$, $F=\int f$, area $=$ probability | ch09 |
| Moments | $\E[g(X)]=\int g(x)f(x)\,dx$ | ch10 |
| Survival method | $\E[X]=\int_0^\infty S(x)\,dx$ | ch10 |
| Uniform | mean $\tfrac{a+b}{2}$, var $\tfrac{(b-a)^2}{12}$ | ch11 |
| Exponential | $S=e^{-x/\theta}$, memoryless, mean $\theta$ | ch11 |
| Gamma | sum of $\alpha$ exps; $\alpha\theta$, $\alpha\theta^2$ | ch11 |
| Normal / CLT | standardize $Z=\tfrac{X-\mu}{\sigma}$; pooling → bell | ch12 |
| Deductibles | $\int_d^\infty S$, $\int_0^u S$; cases; $\div S(d)$ | ch13 |

*You're ready for Act III when* every row above is instant. Any hesitation → rematch the home chapter, then retry this grid.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:170px; text-align:center;">
<img src="../../assets/sprites/front/58.png" alt="Growlithe, the fire-type Puppy Pokemon, mascot of the Cinnabar volcano-loss model" style="width:120px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Growlithe #58 — the Cinnabar volcano-loss mascot</figcaption>
</figure>

Three examples, fading from fully narrated to exam speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because choosing the right road — calculus or cases — is the load-bearing skill of the chapter. The exponential cases use $X\sim\Expo(10)$, $S(x)=e^{-x/10}$.

### Worked Example 1 — The Lab's First Quote (full narration; calculus, both roads)

**ARCHETYPE:** *Expected payment per loss and per payment — exponential loss + ordinary deductible.*

**Setup.** Volcanic damage to gear is $X\sim\Expo(\theta=10)$ (thousands). Trial policy: ordinary deductible $d=4$, no limit, no coinsurance. Find (a) the expected payment **per loss**; (b) the expected payment **per payment**.

**Step 1 — Identify (which road, which average?).** "Expected payment," no conditioning word → **per loss**. Exponential loss + deductible → the **calculus** road: $\E[(X-4)_+]=\int_4^\infty S(x)\,dx$, or the memoryless one-liner. "(b) per payment" conditions on a payment, so divide (a) by $S(d)$.

**Step 2 — Professor's Path (the why).** Build it from the survival integral. For $\Expo(10)$, $S(x)=e^{-x/10}$:
$$\E[(X-4)_+]=\int_4^\infty e^{-x/10}\,dx=\Big[-10e^{-x/10}\Big]_4^\infty=10e^{-0.4}\approx 6.703.$$
A payment happens iff $X>4$, with probability $S(4)=e^{-0.4}=0.6703$. Divide:
$$\E[X-4\mid X>4]=\frac{6.703}{0.6703}=10.$$

**Step 3 — Trainer's Path (the fast how).** Exponential + deductible → memoryless on sight, no integral. Per loss $=\theta e^{-d/\theta}=10e^{-0.4}\approx\mathbf{6.703}$; per payment $=\theta=\mathbf{10}$ (the extra damage past $d$ is a fresh $\Expo(10)$).

**Step 4 — Check & pitfall.** Per-loss $6.703<\E[X]=10$ ✓ (a deductible can only shrink the average); per-payment $10>6.703$ ✓ (the zeros are dropped). **Pitfalls:** reporting $\E[X]-d=6$ (the over-counting trap — the true answer sits *above* $6$ because of the floor at zero); dividing per-payment by $F(4)$ instead of $S(4)$. *(Back-ref: Entries №46, №47.)*

### Worked Example 2 — A Density with No Shortcut (cases approach; partial guidance)

**ARCHETYPE:** *Cases approach on a non-exponential density; deductible then coinsurance.*

**Setup.** A core-sample drill's damage $W$ has density $f(w)=\tfrac{w}{50}$ on $[0,10]$. A policy has deductible $d=2$ and coinsurance $\alpha=0.75$ (no limit). Find the expected payment **per loss**.

**Identify.** A non-exponential density given directly, with no clean memoryless shortcut → the **cases** road: split into $w\le2$ (pays $0$) and $w>2$ (pays the excess), integrate the density, then scale by $\alpha$ *last*.

**Cases integral.** Only the $w>2$ case pays, and the support stops at $10$:
$$\E[(W-2)_+]=\int_2^{10}(w-2)\,\frac{w}{50}\,dw=\frac{1}{50}\Big[\tfrac{w^3}{3}-w^2\Big]_2^{10}=\frac{234.\overline{6}}{50}=4.693.$$

**Apply coinsurance (last).** $\E[Y_L]=\alpha\,\E[(W-2)_+]=0.75(4.693)=\mathbf{3.520}.$

**Check & pitfall.** Cross-check the unscaled $4.693$ via the calculus road: $\int_2^{10}\big(1-\tfrac{w^2}{100}\big)dw=4.693$ ✓ — both roads agree. **Pitfall:** scaling by $\alpha$ *before* integrating (coinsurance is last), or integrating past the support's upper end $10$. *(Back-ref: Entry №47.)*

### Worked Example 3 — The Full Cinnabar Policy (exam speed)

**ARCHETYPE:** *Full policy — per loss, per payment, and the master identity, in one pass.*

**Setup.** Volcanic loss $X\sim\Expo(10)$. The Lab's final policy: deductible $d=4$, maximum covered loss $u=12$, coinsurance $\alpha=0.8$. Find (a) the expected payment **per loss**; (b) the expected payment **per payment**; (c) confirm $\E[X\wedge12]$ via the master identity.

**Limited values (calculus road).** $\E[X\wedge u]=\theta(1-e^{-u/\theta})$:
$$\E[X\wedge12]=10(1-e^{-1.2})\approx6.988,\qquad \E[X\wedge4]=10(1-e^{-0.4})\approx3.297.$$
**(a) Per loss.** $\E[Y_L]=\alpha(\E[X\wedge12]-\E[X\wedge4])=0.8(6.988-3.297)=0.8(3.691)=\mathbf{2.953}.$
**(b) Per payment.** A cheque is written iff $X>d=4$, so divide by $S(4)=e^{-0.4}=0.6703$ (the **deductible**, not the limit): $\E[Y_P]=\dfrac{2.953}{0.6703}=\mathbf{4.405}.$
**(c) Master identity.** $\E[(X-12)_+]=10e^{-1.2}\approx3.012$, and $\E[X\wedge12]+\E[(X-12)_+]=6.988+3.012=10=\E[X]$ ✓.

**Check & pitfall.** Per-loss $2.953<$ the deductible-only $6.703$ (the cap and the $0.8$ both shrink it) ✓; per-payment $4.405>2.953$ ✓. **Pitfall:** dividing per-payment by $S(u)=S(12)$ instead of $S(d)=S(4)$ — the deductible decides *whether* a cheque is written. *(Back-ref: Entries №46, №47.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — Pick the road that fits the loss**

Two roads, one answer; pick the cheaper. **Exponential loss?** Take the calculus road and write $\theta e^{-d/\theta}$ (per loss) and $\theta$ (per payment) on sight — no integral. **A clean survival curve but no memoryless shortcut (uniform, Pareto)?** Still calculus: integrate $S(x)$ — right of $d$, left of $u$. **A raw density handed to you, or a limit-and-coinsurance stack on an odd distribution?** Cases: split into below-$d$ / layer / above-$u$ and integrate $f(x)$. When unsure, the cases road *always* works; the calculus road is just faster when $S$ is clean.
:::

::: trainers-tip
**TRAINER'S TIP — Exponential survival on the calculator, in one keystroke**

Survival of an exponential is a single power of $e$. To get $S(d)=e^{-d/\theta}$, key [2nd]{.kbd} [e^x]{.kbd} [(-)]{.kbd} then $d \div \theta$ and [enter]{.kbd}:

[2nd]{.keystroke} [e^x]{.keystroke} [(-)]{.keystroke} [4]{.keystroke} [÷]{.keystroke} [10]{.keystroke} [enter]{.keystroke}

gives $e^{-0.4}=0.6703$. Store it with [STO▸]{.kbd} so the per-loss payment $\theta\cdot S(d)$ and the per-payment divide-by-$S(d)$ both reuse it without re-keying — store-don't-retype kills rounding drift.
:::

::: trainers-tip
**TRAINER'S TIP — The order is inflation → deductible → limit → coinsurance**

When a problem stacks modifications, run them in that fixed order. **Inflation hits the loss $X$ first** — and the deductible, a fixed contract dollar amount, **does not inflate** (that's why payments rise faster than losses). **Coinsurance is last**, applied to the finished covered layer; never scale the loss and then cap. And decide whether $u$ caps the **loss** (use $X\wedge u$ and the layer $\E[X\wedge u]-\E[X\wedge d]$) or the **payment** (cap *after* the deductible, $\min((X-d)_+,u)$).
:::

::: trainers-tip
**TRAINER'S TIP — Per-payment divides by the deductible's $S(d)$, always**

A payment occurs exactly when the loss **strictly exceeds the deductible**, so per-payment $=$ per-loss $\div\,S(d)=P(X>d)$ — never $F(d)$, never $S(u)$. The limit changes a payment's *size*, not *whether* it happens. A quick red flag: a per-payment average must always be **larger** than the per-loss average (the zeros are gone); if yours comes out smaller, you divided by the wrong probability.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

<figure style="margin:1em auto; max-width:150px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket — Jessie, James, and Meowth" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
</figure>

Team Rocket has slipped onto Cinnabar to sell the Lab a knock-off "volcano policy." Meowth runs the numbers on the exponential loss $X\sim\Expo(10)$. "Easy money," he announces. "Da deductible's **four** thousand, and da average damage is **ten**. So da policy pays ten minus four — **six** thousand a pop. We charge for six, pay for six, pocket da fees!"

Jessie frowns. "That sounds like *work*, Meowth. Can't we pay less?"

Meowth grins wider. "Even better — we cap what we *pay* at four thousand too. So I cap da loss at four first — nuthin' over four counts — *den* knock off da four-thousand deductible. Four minus four is *zero!* We pay **nuthin'!**"

James squints. "But James-from-the-future says… if the volcano wrecks twenty thousand of gear, surely we owe *something*?"

Meowth waves a paw. "Nah! Cap first, *den* deductible! Trust da Meowth!"

**Where it fails — twice.** First, $\E[X]-d=10-4=6$ is the **over-counting trap**: it assumes every loss clears the deductible, but losses below $4$ pay $0$, not a negative amount. The floor at zero pushes the true per-loss payment *above* $6$ — it's $\int_4^\infty e^{-x/10}\,dx=10e^{-0.4}\approx\mathbf{6.703}$, not $6$. Second, Meowth applied the **deductible after the payment cap**. The correct order caps the *payment* after the deductible: $\min((X-4)_+,\,4)$, which on $\Expo(10)$ averages
$$\E\big[\min((X-4)_+,4)\big]=\int_4^8(x-4)\tfrac{1}{10}e^{-x/10}dx+4\!\int_8^\infty\tfrac{1}{10}e^{-x/10}dx=10\big(e^{-0.4}-e^{-0.8}\big)\approx 2.21\text{ (thousand)},$$
not $0$. He convinced himself the policy pays nothing when it pays plenty. Two errors, both fatal to the scam: **floor at zero, and run the operations in order.** (You'll catch Meowth red-handed in Problem C13.8.)
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

This is the literal arithmetic of **continuous-loss insurance pricing** — the daily work of a property-casualty pricing actuary.

A homeowner's or commercial property policy faces losses that are genuinely continuous: a fire, a flood, an earthquake damages a building by *any* dollar amount, modeled by a severity density $f(x)$ (often exponential, gamma, lognormal, or Pareto). The policy carries a **deductible**, a **limit** (maximum covered loss), and frequently **coinsurance**; the premium is built from the **per-loss expected payment** $\E[Y_L]$, because the insurer must collect, across all policies sold, enough to cover the average payout *per policy* — including the many that never claim. The **survival-integral** identities $\E[(X-d)_+]=\int_d^\infty S\,dx$ and $\E[X\wedge u]=\int_0^u S\,dx$ are exactly how a pricing actuary splits a loss into the insured's **retained layer** and the insurer's (or reinsurer's) **excess layer**. **Inflation** on a fixed deductible is the well-known "deductible-erosion" effect that forces rate increases to outpace pure loss trend. And the **cases approach** is what you fall back on the moment the severity isn't a friendly exponential.

*Series bridge:* the discrete twin of this chapter was **ch06 (Fuchsia)** — same four operations, sums instead of integrals. From here these limited-expected-value and layer tools feed directly into **loss models and ratemaking** on the later actuarial exams (**STAM / FAM-Short / Exam 5**), where the full menu of severity distributions, policy modifications, and reinsurance structures lives.

*Transfer check:* could you solve this with no Pokémon in it? "A loss $X$ is exponential with mean $10$; a policy has deductible $4$, maximum covered loss $12$, and pays $80\%$ of the covered layer. Find the expected payment per loss." Same $2.953$. If you can do that, the skill has transferred.
:::

## The Gym Battle — The Lab's Coverage Sign-Off

<figure style="margin:1.5em auto; max-width:170px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak, here serving as the examiner for the Cinnabar Lab's coverage sign-off" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Oak's sign-off — the full policy, both roads, both averages</figcaption>
</figure>

There is **no badge** at Cinnabar Lab — Blaine's Volcano Badge waits in the next chapter. Instead, Oak holds the Lab's coverage sign-off: prove you can price the volcano policy completely, by *both* roads, before he certifies it.

**Oak's Challenge.** "A complete actuary, Ash, never trusts a single road. The Lab's spectrometer loss is $X\sim\Expo(\theta=10)$ (thousands). The final policy carries a deductible $d=4$, a maximum covered loss $u=12$, and coinsurance $\alpha=0.8$. Show me — in one pass:

(a) the expected payment **per loss**, by the **calculus** road (difference of two limited expected values);
(b) the expected payment **per payment** (so a claimant knows the typical cheque);
(c) and *verify* your $\E[X\wedge12]$ with the **master identity**.

Misprice the order of operations, or divide by the wrong probability, and the Lab stays uninsured."

**ARCHETYPE:** *Full continuous policy — per-loss, per-payment, and the master identity, in one pass.*

**Step 1 — Identify.** A full policy on an exponential loss: deductible, limit, coinsurance. Per-loss is the scaled covered layer $\alpha(\E[X\wedge u]-\E[X\wedge d])$; per-payment divides by $S(d)$; the master identity cross-checks the limited value.

**Step 2 — Calculus road: the two limited values.** $\E[X\wedge a]=\theta(1-e^{-a/\theta})$:
$$\E[X\wedge12]=10(1-e^{-1.2})\approx6.988,\qquad \E[X\wedge4]=10(1-e^{-0.4})\approx3.297.$$

**Step 3 — Solve.**
*(a) Per loss:*
$$\E[Y_L]=\alpha\big(\E[X\wedge12]-\E[X\wedge4]\big)=0.8(6.988-3.297)=0.8(3.691)=\boxed{2.953}.$$
*(b) Per payment:* a cheque is written iff $X>d=4$, probability $S(4)=e^{-0.4}=0.6703$:
$$\E[Y_P]=\frac{\E[Y_L]}{S(4)}=\frac{2.953}{0.6703}=\boxed{4.405}.$$
*(c) Master identity, proving $\E[X\wedge12]$:* the excess over $u=12$ is $\E[(X-12)_+]=10e^{-1.2}\approx3.012$, and
$$\E[X\wedge12]+\E[(X-12)_+]=6.988+3.012=10=\E[X].\ \checkmark$$

**Step 4 — Check, verdict & the pitfall Oak is testing.** Per-loss $2.953>0$ and below the deductible-only $6.703$ (cap and coinsurance both shrink it) ✓; per-payment $4.405>2.953$ ✓; the identity closes at $10$ ✓. The pitfall Oak probes is the **order and the divisor** — scale before the layer, or divide by $S(12)$ instead of $S(4)$, and the answer is wrong though every step looks right.

> "...Confirmed," Oak says, signing the Lab's ledger. "You ran the loss through the deductible, then the limit, then the coinsurance — by the calculus road *and* checked it against the identity — and divided the cheque by the right probability. The Lab is insured. The volcano can do its worst." He nods toward the gym across the island. "Now — Blaine is waiting."

## The Gym Challenge — Problem Set

::: problem-set
**THE CINNABAR LAB'S COVERAGE COMMISSION — your questline.** Oak has hired you to price the Lab's volcano-insurance scheme by *both* roads. First the **Route Trainer** legs (warming up the calculus and cases tools on single events), then the **Gym Battle** tier (the boss problems — full policies at exam difficulty, with Oak and Team Rocket), then the optional **Elite Challenge** post-game. Work it timed (~6 min/problem), then check the **Answers** below. Hit the mastery bar (**80%+ with correct method**) to clear the commission and certify the policy. Markers: 🔴 routine method · 🟡 routine-with-a-twist · 🔵 stretch.

The headline loss is $X\sim\Expo(\theta=10)$, $S(x)=e^{-x/10}$, $\E[X]=10$. A second loss $W$ has density $f(w)=\tfrac{w}{50}$ on $[0,10]$, $S(w)=1-\tfrac{w^2}{100}$, $\E[W]=\tfrac{20}{3}$. Each problem restates what it needs, so you can work them in any order.

### Route Trainers (the early legs — warming up your tools)

**C13.1.** 🔴 *(The Lab's first quote: calculus road.)* For $X\sim\Expo(10)$, an ordinary deductible $d=3$ applies. Find the expected payment **per loss**, $\E[(X-3)_+]=\int_3^\infty S(x)\,dx$.

**C13.2.** 🟡 *(How big is an actual cheque?)* For the same $d=3$ policy on $X\sim\Expo(10)$, find the expected payment **per payment**. (Memoryless — no integral.)

**C13.3.** 🔴 *(Capping the Lab's reserve.)* For $X\sim\Expo(10)$, find the limited expected value $\E[X\wedge8]=\int_0^8 S(x)\,dx$.

**C13.4.** 🔴 *(Cases road on a uniform loss.)* A loss $V\sim\Unif(0,20)$ (so $S(v)=1-\tfrac{v}{20}$ on $[0,20]$) has a deductible $d=4$. Find $\E[(V-4)_+]$ — either by integrating the density over $v>4$ or as $\int_4^{20}S(v)\,dv$.

**C13.5.** 🟡 *(Cases road, a rising density.)* For the core-sample loss $W$ with density $f(w)=\tfrac{w}{50}$ on $[0,10]$, deductible $d=2$, find $\E[(W-2)_+]$ by splitting into cases and integrating the density.

**C13.6.** 🔴 *(Coinsurance only.)* A bare co-pay plan covers $\alpha=0.7$ of every loss with no deductible and no cap, on $X\sim\Expo(10)$. Find the expected payment per loss.

**C13.7.** 🟡 *(Master identity — no new integral.)* Given $\E[X]=10$ and $\E[X\wedge8]=10(1-e^{-0.8})\approx5.507$ for $X\sim\Expo(10)$, find the expected excess $\E[(X-8)_+]$ using the master identity.

> *Questline beat: your quotes are warm and Oak is nodding along. But Team Rocket has slipped onto the island selling a knock-off policy, and Oak's full sign-off awaits. The boss problems begin.*

### Gym Battles (the boss fight — true SOA difficulty)

**C13.8.** 🟡 *(AUDIT — Team Rocket's knock-off policy.)* Team Rocket's policy on $X\sim\Expo(10)$ has deductible $d=4$ and a maximum **payment** of $u=4$. Meowth caps the loss at $4$ first, *then* subtracts the deductible, and declares "the policy pays $0$." Find the **correct** expected payment per loss, $\E[\min((X-4)_+,4)]$ (deductible first, then cap the payment), and name Meowth's error.

**C13.9.** 🟡 *(Oak's full policy, per loss.)* The sign-off policy on $X\sim\Expo(10)$ has $d=4$, $u=12$, $\alpha=0.8$. Given $\E[X\wedge12]=6.988$ and $\E[X\wedge4]=3.297$, find the expected payment per loss.

**C13.10.** 🟡 *(Oak's full policy, per payment.)* For the policy in C13.9 ($\E[Y_L]=2.953$ given), find the expected payment **per payment**. Use the deductible's probability $S(4)=e^{-0.4}=0.6703$.

**C13.11.** 🔵 *(Both roads must agree.)* For $W$ with density $f(w)=\tfrac{w}{50}$ on $[0,10]$ and deductible $d=2$, compute $\E[(W-2)_+]$ by the **cases** road ($\int_2^{10}(w-2)f(w)\,dw$) **and** verify it equals the **calculus** road ($\int_2^{10}S(w)\,dw$ with $S(w)=1-\tfrac{w^2}{100}$).

**C13.12.** 🟡 *(Exponential memoryless on sight.)* For $X\sim\Expo(\theta=10)$ with deductible $d=5$, write the per-loss and per-payment expected payments using the memoryless shortcut (no integral).

**C13.13.** 🔵 *(RIVAL TRAP — Gary brags about his "average claim.")* Gary buys the $d=4$ deductible policy on $X\sim\Expo(10)$ and crows: "My expected payment per loss is $6.703$, so when I file a claim I'll average a $6.703$-thousand cheque." Find the true expected payment **per payment** and explain Gary's error.

**C13.14.** 🟡 *(The covered layer, calculus road.)* For $X\sim\Expo(10)$, a policy pays the full layer between $d=4$ and $u=12$ ($\alpha=1$). Given $\E[X\wedge12]=6.988$ and $\E[X\wedge4]=3.297$, find the expected payment per loss.

**C13.15.** 🔵 *(DECISION — two policies, which costs the Lab more?)* For $X\sim\Expo(10)$ the Lab must pick one plan. **Plan A:** deductible $d=4$, no limit, $\alpha=1$. **Plan B:** no deductible, maximum covered loss $u=4$, $\alpha=1$. Compute the expected payment per loss for each (using $S(4)=e^{-0.4}=0.6703$) and recommend the *cheaper* plan for the Lab.

**C13.16.** 🟡 *(AUDIT — the "mean minus deductible" error.)* An apprentice records "deductible $d=4$ on $X\sim\Expo(10)$, so expected per-loss payment $=\E[X]-d=10-4=6$." Find the true per-loss payment ($\int_4^\infty e^{-x/10}\,dx$) and name the error.

> *Questline beat: the policy is signed and Team Rocket's scam is exposed. The post-game below is optional — the integrative challenges a league-bound actuary sharpens on.*

### Elite Challenge (post-game — integrative / stretch)

**C13.17.** 🔵 *(INFLATION — deductible erosion.)* This year $X\sim\Expo(10)$ with a fixed deductible $d=4$, so the per-loss payment is $10e^{-0.4}\approx6.703$. Next year losses inflate $25\%$ (so $(1+r)X\sim\Expo(12.5)$) but the deductible stays $4$. Find next year's per-loss payment and the percentage rise, and explain why it exceeds $25\%$.

**C13.18.** 🔵 *(RIVAL TRAP — Gary reverses the order.)* Gary prices a $\Expo(10)$ policy with deductible $d=4$ and maximum covered loss $u=12$ by capping the loss at $12$, then subtracting "$d\cdot S(d)$" to remove the deductible: $\E[X\wedge12]-4\,S(4)$. Find the **correct** per-loss layer $\E[X\wedge12]-\E[X\wedge4]$ (given $\E[X\wedge12]=6.988$, $\E[X\wedge4]=3.297$, $S(4)=0.6703$) and explain why Gary's shortcut is wrong.

**C13.19.** 🔵 *(AUDIT — the wrong-divisor per-payment error.)* A Team Rocket apprentice on the scam desk prices the $d=4$ policy's cheque on $X\sim\Expo(10)$. He has the per-loss figure $\E[(X-4)_+]=6.703$ and, to get the per-payment average, divides by $F(4)=P(X\le4)=1-e^{-0.4}=0.3297$: "$6.703/0.3297=20.33$ — declared safe." Find the **true** expected payment **per payment** and name the apprentice's error.
:::

## Answers

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

### Quick-Answer Table

| # | Answer | Archetype | | # | Answer | Archetype |
|---|---|---|---|---|---|---|
| C13.1 | $10e^{-0.3}\approx7.408$ | standard | | C13.11 | $4.693$ (both roads) | standard |
| C13.2 | $10$ | standard | | C13.12 | per loss $10e^{-0.5}\approx6.065$; per payment $10$ | standard |
| C13.3 | $10(1-e^{-0.8})\approx5.507$ | standard | | C13.13 | per payment $10$; Gary confused the two | rival_trap |
| C13.4 | $6.4$ | standard | | C13.14 | $3.691$ | standard |
| C13.5 | $4.693$ | standard | | C13.15 | A $6.703$, B $3.297$; choose B | decision |
| C13.6 | $7.0$ | standard | | C13.16 | $6.703$ (not $6$) | audit |
| C13.7 | $10e^{-0.8}\approx4.493$ | standard | | C13.17 | $9.077$; $+35.4\%$ | standard |
| C13.8 | $\approx2.21$ (not $0$) | audit | | C13.18 | $3.691$; Gary's shortcut wrong | rival_trap |
| C13.9 | $2.953$ | standard | | C13.19 | $10$ (not $20.33$) | audit |
| C13.10 | $4.405$ | standard | | | | |

**C13.1** — *(standard) Calculus road, deductible per loss (Entry №46).* $\E[(X-3)_+]=\int_3^\infty e^{-x/10}\,dx=\big[-10e^{-x/10}\big]_3^\infty=10e^{-0.3}\approx7.408.$ (Memoryless check: $\theta e^{-d/\theta}=10e^{-0.3}$ ✓.)

**C13.2** — *(standard) Per payment, memoryless (Entries №46, №47).* The conditional excess $(X-3\mid X>3)$ is a fresh $\Expo(10)$, so $\E[X-3\mid X>3]=\theta=10.$ (Equivalently $\E[(X-3)_+]/S(3)=7.408/e^{-0.3}=10$.)

**C13.3** — *(standard) Limited expected value, calculus road (Entry №46).* $\E[X\wedge8]=\int_0^8 e^{-x/10}\,dx=\big[-10e^{-x/10}\big]_0^8=10(1-e^{-0.8})\approx5.507.$

**C13.4** — *(standard) Cases/survival on a uniform (Entries №46, №47).* $\E[(V-4)_+]=\int_4^{20}\big(1-\tfrac{v}{20}\big)dv=\big[v-\tfrac{v^2}{40}\big]_4^{20}=(20-10)-(4-0.4)=10-3.6=6.4.$ (Direct density check: $\int_4^{20}(v-4)\tfrac{1}{20}dv=\tfrac{(16)^2}{2\cdot20}=6.4$ ✓.)

**C13.5** — *(standard) Cases road, rising density (Entry №47).* Only $w>2$ pays: $\E[(W-2)_+]=\int_2^{10}(w-2)\tfrac{w}{50}\,dw=\tfrac{1}{50}\big[\tfrac{w^3}{3}-w^2\big]_2^{10}=\tfrac{234.\overline{6}}{50}=4.693.$

**C13.6** — *(standard) Coinsurance only (Entry №47).* No deductible, no cap: $\E[\alpha X]=\alpha\E[X]=0.7(10)=7.0.$

**C13.7** — *(standard) Master identity (Entry №46).* $\E[(X-8)_+]=\E[X]-\E[X\wedge8]=10-5.507=4.493.$ (Direct check: $10e^{-0.8}\approx4.493$ ✓ — no new integral.)

**C13.8** — *(audit) Deductible-after-payment-cap order error (Entries №46, №47).* **Correct order — deductible first, then cap the payment at $u=4$:** $\E[\min((X-4)_+,4)]=\int_4^{8}(x-4)\tfrac{1}{10}e^{-x/10}dx+4\int_8^\infty\tfrac{1}{10}e^{-x/10}dx=10\big(e^{-0.4}-e^{-0.8}\big)\approx2.21.$ **Meowth's error:** he capped the *loss* at $4$ first ($\min(X,4)$), *then* subtracted the deductible $4$ and floored — giving $0$ for every loss. The deductible must come **before** the payment cap; the true per-loss payment is about $2.21$, not $0$.

**C13.9** — *(standard) Oak's full policy, per loss (Entry №46).* $\E[Y_L]=\alpha(\E[X\wedge12]-\E[X\wedge4])=0.8(6.988-3.297)=0.8(3.691)=2.953.$

**C13.10** — *(standard) Full policy, per payment (Entry №47).* A cheque is written iff $X>d=4$, so divide by $S(4)=e^{-0.4}=0.6703$ (the deductible, **not** the limit): $\E[Y_P]=2.953/0.6703=4.405.$

**C13.11** — *(standard) Both roads agree (Entries №46, №47).* Cases: $\int_2^{10}(w-2)\tfrac{w}{50}\,dw=4.693.$ Calculus: $\int_2^{10}\big(1-\tfrac{w^2}{100}\big)dw=\big[w-\tfrac{w^3}{300}\big]_2^{10}=6.667-1.973=4.693.$ ✓ Equal.

**C13.12** — *(standard) Memoryless on sight (Entry №46).* Per loss: $\theta e^{-d/\theta}=10e^{-0.5}\approx6.065.$ Per payment: $\theta=10.$

**C13.13** — *(rival_trap) Per-loss vs per-payment confusion (Entry №47).* The $6.703$ Gary quotes is the **per-loss** average — it already includes the events that pay $0$. The size of an *actual* cheque is the **per-payment** average: by memorylessness, $\E[X-4\mid X>4]=\theta=10.$ (Or $6.703/S(4)=6.703/0.6703=10$.) **Gary's error:** he read the per-loss figure (which averages over the zeros) as the typical cheque; the typical cheque is $10$ thousand.

**C13.14** — *(standard) Covered layer, calculus road (Entry №46).* $\E[X\wedge12]-\E[X\wedge4]=6.988-3.297=3.691.$

**C13.15** — *(decision) Compare two plans, pick the cheaper for the insurer (Entry №46).* **Plan A** (deductible $4$, no limit): $\E[(X-4)_+]=10e^{-0.4}=6.703.$ **Plan B** (no deductible, cap $u=4$): $\E[X\wedge4]=10(1-e^{-0.4})=3.297.$ Plan A costs the Lab $6.703$ per event; Plan B costs $3.297$. **Recommend Plan B** — here the low cap is cheaper than the deductible, because the heavy exponential tail makes the *uncapped* excess above the deductible expensive, while capping at $4$ throws away that whole tail. (Note A and B are the two halves of the master identity: $6.703+3.297=10=\E[X]$.)

**C13.16** — *(audit) Mean-minus-deductible error (Entry №46).* True per-loss payment: $\E[(X-4)_+]=\int_4^\infty e^{-x/10}\,dx=10e^{-0.4}\approx6.703.$ **The apprentice's error:** $\E[X]-d=10-4=6$ assumes every loss clears the deductible; losses below $4$ pay $0$, not a negative amount, so the floor at zero pushes the true payment *above* $6$. True payment $6.703$.

**C13.17** — *(standard) Inflation / deductible erosion (Entries №46, №47).* Next year $(1+r)X\sim\Expo(12.5)$ but the fixed $d=4$ stays, so per loss $=12.5\,e^{-4/12.5}=12.5\,e^{-0.32}\approx9.077.$ Rise over this year's $6.703$: $9.077/6.703-1\approx0.354$, a **$+35.4\%$** jump. It exceeds the $25\%$ loss inflation because the deductible *does not inflate* — a fixed $4$ is a smaller fraction of the (now larger) losses, so it removes proportionally less, and the payment grows faster than the loss.

**C13.18** — *(rival_trap) Bogus deductible-removal shortcut (Entry №46).* **Correct** layer between $d=4$ and $u=12$: $\E[X\wedge12]-\E[X\wedge4]=6.988-3.297=3.691.$ **Gary's shortcut** $\E[X\wedge12]-d\,S(d)=6.988-4(0.6703)=6.988-2.681=4.307$ is wrong: subtracting $d\,S(d)$ is *not* how a deductible removes the bottom of a capped loss. The deductible removes the limited value $\E[X\wedge d]=\E[X\wedge4]=3.297$, not $d\,S(d)=2.681$. The correct covered layer is the difference of two limited expected values, $3.691$.

**C13.19** — *(audit) Wrong-divisor per-payment error (Entry №47).* A payment occurs iff the loss **strictly exceeds** the deductible, $X>4$, so the divisor is $S(4)=e^{-0.4}=0.6703$, **not** $F(4)=0.3297$. The true per-payment cheque is $\E[X-4\mid X>4]=\E[(X-4)_+]/S(4)=6.703/0.6703=10$ (the memoryless mean $\theta$). **The apprentice's error:** he divided by $F(4)$ (the chance a loss does *not* clear the deductible) instead of $S(4)$ (the chance it does). His $20.33$ is absurdly large — a per-payment average can't exceed the loss's own mean-conditional structure like that, an immediate red flag. The true cheque is $10$, not $20.33$.
:::

> Next stop: **Cinnabar Mansion (ch14)** — Blaine's burned-out research logs open the multivariate act (Act III), where two quantities move *together* and you finally earn the **Volcano Badge**. Pack your survival integrals and your cases tables; the layer tools return whenever a loss meets a payment.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
