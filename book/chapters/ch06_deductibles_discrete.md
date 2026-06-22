<!--
  file: ch06_deductibles_discrete
  tier: B
  outcomes: 2e,2f
  tia: A.6
  locale: Fuchsia City / the Safari Zone
  type: poison
  maps_to: Koga's Fuchsia Gym + the Safari Zone Warden's coverage commission -- a payment
           is a transformation of a (discrete) loss: deductible (X-d)+, limit X^u, coinsurance,
           the budget identity E[X^u]+E[(X-d)+]=E[X], per-loss vs per-payment.
  NOTE: this is the DISCRETE deductible chapter (finite pmf, sums only). The continuous
        calculus version (survival integrals, exponential losses) is ch13.
-->

# A Payment Is a Reshaped Loss {.type-poison}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with the southern coast highlighted: Fuchsia City, home of Koga's poison-type gym, the Soul Badge, and the great fenced Safari Zone, marked as the current destination after Celadon." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 5th badge — you have left Celadon with the Rainbow Badge and reached <strong>Fuchsia City</strong>: Koga's ninja gym, the <strong>Soul Badge</strong>, and the sprawling, fenced <strong>Safari Zone</strong> where Pokémon flee instead of fight.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Ninja Poké-Showdown"**

The Safari Zone Warden meets you at the gate, ledger in hand. Inside the great fence, trainers don't *battle* the wild Pokémon — they stalk them, lob Safari Balls, and watch most of their quarry bolt for the tall grass. Every flee costs the trainer real money: spooked Tauros trample gear, startled Kangaskhan crush a pack. The Warden has a stack of past claims and a single number for each kind of mishap.

"Here's my problem," she says. "I want to *insure* my visitors. Charge a small fee at the gate, and when a Pokémon flees and wrecks their gear, the Zone reimburses them. But I can't reimburse *everything* — I'd go broke by lunch. So the policy will make the trainer eat the first couple of thousand themselves" — a **deductible** — "and I'll never pay out more than a set ceiling on any one flee" — a **limit** — "and I'll cover, say, eighty cents on the dollar of what's left" — **coinsurance**. "Tell me what the Zone pays *on average* per flee, so I know what to charge at the gate."

You open the Pokédex's Actuary Mode. The gear-loss is a random variable — you already know how to find its average. But the Warden isn't asking for the average *loss*. She's asking for the average *payment*, and the payment is not the loss: it's the loss with its bottom knocked off, its top capped, and the middle scaled down. The loss $X$ and the payment $Y$ are *two different random variables*.

*How do you find the expected value of the payment — when all you're handed is the distribution of the loss?*
:::

## Where You Are — 60-Second Retrieval

**Rank: Junior Trainer · Badges: 4 (Cascade, Thunder, Boulder, Rainbow).** You earned the **Rainbow Badge** at Celadon working with the geometric and Poisson distributions. But the load-bearing tool you carry into Fuchsia is older — it's from the **S.S. Anne and Vermilion (ch03)**: the **expected value of a discrete random variable**, and especially the fact that you can average *any function* of a loss. Recall two moves you already own:

- $E[X]=\sum_k k\,p(k)$ — the probability-weighted average of a discrete RV.
- $E[g(X)]=\sum_k g(k)\,p(k)$ — the **law of the unconscious statistician**: to average a *function* of $X$, weight the function's values by the same probabilities.

Hold onto that second line. This entire chapter is one idea: **the payment is a function $g(X)$ of the loss**, so its expected value is just $\sum_k g(k)\,p(k)$. Everything else — deductible, limit, coinsurance — is choosing *which* function $g$.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own ch03**

Answer from memory; if any feels shaky, flip back to the S.S. Anne chapter before continuing.

1. A loss $X$ has pmf $p(0)=0.3,\,p(1)=0.5,\,p(2)=0.2$. What is $E[X]$? *(Answer: $0(0.3)+1(0.5)+2(0.2)=0.9$.)*
2. For that same $X$, what is $E[X^2]$ — and is it the same as $(E[X])^2$? *(Answer: $0+1(0.5)+4(0.2)=1.3$; **no**, $(0.9)^2=0.81\ne1.3$ — you average the function's values, never plug the mean into the function.)*
3. The **survival function** is $S(k)=P(X>k)$. For the loss above, what is $S(0)$? *(Answer: $P(X>0)=0.5+0.2=0.70$.)*
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP032 "The Ninja Poké-Showdown" (with Safari Zone EP035 "The Legend of Dratini")**

In **EP032** Ash reaches **Fuchsia City** and faces **Koga**, the ninja Gym Leader, in a gym rigged with traps, hidden walls, and poison-type Pokémon (our cold-open's "Warden with a ledger" and the gate-fee insurance scheme are an *in-world extension* invented for the math — the on-screen events are Koga's trap-gym battle for the Soul Badge). **EP035** takes the heroes into the **Safari Zone**, where wild Pokémon — including the famous herd of Tauros and the elusive Dratini — roam a fenced reserve and trainers must catch them with limited Safari Balls rather than battling (the perfect setting for "losses you can't fully control, so you insure against them"). *Watch EP032 right before this chapter for Koga and the Soul Badge, and EP035 for the Safari Zone the drills live in.*
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice comes through the Pokédex as you study the Warden's claim ledger.

"Ash — Fuchsia is where probability starts to earn a paycheck. This is the chapter that connects most directly to a real actuarial job: *pricing coverage*. But hear the single idea underneath all of it: **a payment is a transformation of a loss.** The loss $X$ is one random variable; you reshape it — knock off the bottom with a deductible, chop the top with a limit, scale the middle with coinsurance — and the *payment* $Y$ is a brand-new random variable. You already know how to take the expected value of a function of $X$. Everything here is that one skill, applied a few ways. This is a **Tier B** chapter; the losses are **discrete** — finite tables, plain sums, no calculus. (The continuous version, with integrals, waits for Cinnabar in ch13.)"

By the end of this chapter you will be able to:

- **Compute** the per-loss payment under an **ordinary deductible** $d$, $(X-d)_+$, and recognize the lump of probability it creates at a payment of zero. *(Outcome 2e.)*
- **Compute** the **limited loss** $X\wedge u=\min(X,u)$ and its expected value $E[X\wedge u]$ (the **limited expected value**), and **assemble a full policy** — deductible, limit, and **coinsurance** $\alpha$ — in the correct order. *(Outcome 2e.)*
- **Use the budget identity** $E[X\wedge u]+E[(X-u)_+]=E[X]$ to get any one of the three pieces from the other two. *(Outcome 2e.)*
- **Distinguish the loss from the payment**, and **per-loss** expectation from **per-payment** expectation (dividing by $P(X>d)$). *(Outcome 2f.)*

> *Exam-weight signpost.* Deductibles and limits are a small but **highly reliable** slice of Exam P's univariate topic (outcomes 2e–2f) — and almost every problem reduces to two skills you already have: *build the right $g$, then sum $g(k)\,p(k)$.* Because the losses here are discrete, there is **no calculator distribution to memorize** — just careful bookkeeping on a table. This is a **Tier B** chapter: full treatment of every concept, but the tables keep the arithmetic light.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own All of Fuchsia?**

Already fluent? Prove it. Use the Safari loss $X\in\{0,1,2,3,4,5\}$ with pmf $p=0.30,0.25,0.20,0.13,0.08,0.04$ (so $E[X]=1.56$) for all five, ~3 minutes each.

1. With an ordinary deductible $d=2$, find the expected payment **per loss**, $E[(X-2)_+]$.
2. Find the **limited expected value** $E[X\wedge 3]$.
3. Verify the budget identity $E[X\wedge 3]+E[(X-3)_+]=E[X]=1.56$.
4. For the deductible $d=2$, find the expected payment **per payment** (i.e. $E[X-2\mid X>2]$).
5. A full policy has $d=2$, maximum covered loss $u=4$, coinsurance $\alpha=0.8$. Find the expected payment per loss.

*(Answers: (1) $0.41$; (2) $1.40$; (3) $1.40+0.16=1.56$ ✓; (4) $0.41/0.25=1.64$; (5) $0.8(E[X\wedge4]-E[X\wedge2])=0.8(1.52-1.11)=0.328$.)* Five for five with the right method? **Skip to the Gym Battle** and claim the badge. Any miss or hesitation? Each concept below has its own skip-gate, so even a partial owner loses no time.
:::

---

We build three concepts, in TIA's order (A.6.1 → A.6.2 → A.6.3) and increasing difficulty. Each gets a "do you already own this?" skip-check, the full nine-beat lesson, and a Pokédex Entry. One loss random variable runs through the whole chapter so the numbers chain.

1. **The ordinary deductible** $(X-d)_+$ — knocking off the bottom *(A.6.1)*
2. **The policy limit & limited expected value** $X\wedge u$, **coinsurance**, and the **budget identity** *(A.6.2)*
3. **Per-loss vs per-payment**, and the calculator/bookkeeping approach *(A.6.3)*

**The chapter's loss random variable.** A wild Pokémon flees in the Safari Zone and wrecks the trainer's gear. Let $X$ = the gear-loss, in **thousands** of Poké-dollars, $X\in\{0,1,2,3,4,5\}$:

| $k$ (loss, thousands) | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|---|
| $p(k)=P(X=k)$ | $0.30$ | $0.25$ | $0.20$ | $0.13$ | $0.08$ | $0.04$ |
| $S(k)=P(X>k)$ | $0.70$ | $0.45$ | $0.25$ | $0.12$ | $0.04$ | $0.00$ |

Check: the pmf sums to $1$, and the expected loss is
$$E[X]=\sum_k k\,p(k)=0(0.30)+1(0.25)+2(0.20)+3(0.13)+4(0.08)+5(0.04)=0.25+0.40+0.39+0.32+0.20=1.56.$$
The Warden's whole question is: *given this loss, what does the Zone pay?* The survival row $S(k)$ — which you built in ch03 — will earn its keep below.

## Concept 1 — The Ordinary Deductible (Knocking Off the Bottom) {#concept-1}

::: concept-gate
**DO YOU ALREADY OWN THIS? — Ordinary deductible**

For the Safari loss $X$ above, an ordinary deductible $d=2$ applies. Find the expected payment **per loss**, $E[(X-2)_+]$.

If you wrote **$E[(X-2)_+]=0(\text{for }k\le2)+1(0.13)+2(0.08)+3(0.04)=0.41$** (and you know it is **not** $E[X]-2$), **skip to Concept 2**. If you reached for $E[X]-2=-0.44$ (a *negative* "payment"), read on — that's exactly the trap.
:::

**Beat 1 — The one-sentence idea.** *An ordinary deductible $d$ makes the trainer eat the first $d$ of any loss; the policy pays whatever is left over, and pays exactly **zero** whenever the loss never clears $d$.*

**Beat 2 — Anchor + concrete instance.** The Warden's simplest policy: deductible $d=2$ (thousand), no limit, no coinsurance. When a Pokémon flees and wrecks $X$ of gear, the Zone pays $X-2$ — **but never less than zero.** A loss of $5$ pays $3$; a loss of $1$ pays $0$ (it never reached the deductible); a loss of $2$ pays $0$ (it just barely didn't clear it). The payment is the *excess of the loss over the deductible.*

**Beat 3 — Reason through it in plain words.** The deductible draws a floor under the *loss* before the policy responds. Two regions: below the deductible the policy pays nothing (the loss is the trainer's problem entirely); above it the policy pays the part that pokes above $d$. The key subtlety: a small loss cannot generate a *negative* payment. A loss of $0.5$ doesn't earn the trainer money — it pays $0$. So the deductible's bite is **blunted by a floor at zero**, and that floor is the whole reason the per-loss payment is not just "the mean minus $d$."

**Beat 4 — Surface and dismantle the tempting wrong idea.** *(This is one half of Team Rocket's trap for the chapter.)* The seductive move is to subtract the deductible straight from the mean:
$$E[(X-d)_+]\stackrel{?}{=}E[X]-d=1.56-2=-0.44.$$
A *negative* expected payment is nonsense — the policy can't claw money back. The error: $E[X]-d$ silently assumes *every* loss is at least $d$, so $d$ is shaved off all of them. But the losses at $k=0,1,2$ pay **zero**, not $k-2$ (which would be negative). You may only subtract $d$ from the losses that *clear* it. The correct per-loss payment is computed by running each loss through $(k-d)_+$ first — "negative? call it zero" — and *then* averaging.

**Beat 5 — Translate into notation, one glyph at a time.** Name the payment. Let $Y_L$ be the **per-loss payment** — the payment recorded for *every* flee, counting the zeros. The notation is the **positive-part** symbol:
$$Y_L=(X-d)_+ \qquad \text{where}\quad (x-d)_+=\max(x-d,\,0).$$
Read $(X-d)_+$ aloud as "$X$ minus $d$, **floored at zero**." The little $+$ subscript means *"if this would be negative, it's zero instead."* So $(X-d)_+$ is the per-loss payment in one symbol. Its expectation, by the law of the unconscious statistician, is just that function averaged against the pmf:
$$E[(X-d)_+]=\sum_k (k-d)_+\,p(k).$$

**Beat 6 — Derive it from the instance (two equal roads).** *Road 1 — direct LOTUS sum.* Build the payment $(k-2)_+$ for each loss, then weight by $p(k)$:

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|---|
| $(k-2)_+$ | $0$ | $0$ | $0$ | $1$ | $2$ | $3$ |
| $p(k)$ | $0.30$ | $0.25$ | $0.20$ | $0.13$ | $0.08$ | $0.04$ |

$$E[(X-2)_+]=0(0.30)+0(0.25)+0(0.20)+1(0.13)+2(0.08)+3(0.04)=0.13+0.16+0.12=0.41.$$

*Road 2 — the survival shortcut.* Exactly as the Darth-Vader rule summed the survival for $E[X]$ in ch03, the **excess** sums the survival from the deductible onward:
$$E[(X-d)_+]=\sum_{k\ge d} S(k)=S(2)+S(3)+S(4)=0.25+0.12+0.04=0.41.\ \checkmark$$
Same $0.41$, fewer products. (Why it works: $(X-d)_+=\sum_{k\ge d}\mathbf{1}\{X>k\}$ stacks one unit-block for every integer level above $d$ that the loss exceeds; averaging gives $\sum_{k\ge d}P(X>k)$.) Notice $0.41>0$ but far below $E[X]-d$: the deductible removed *less* than $2$ on average, because the small losses had nothing to remove.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $d=2$, $E[(X-2)_+]=0.41$ as above.
- *Twist (a different deductible):* $d=1$ gives $E[(X-1)_+]=\sum_{k\ge1}S(k)=0.45+0.25+0.12+0.04=0.86$ — a smaller deductible pays more, as it must.
- *General:* for any non-negative integer loss and integer $d$, $E[(X-d)_+]=\sum_{k\ge d}S(k)$; equivalently $E[(X-d)_+]=E[X]-E[X\wedge d]$ (Concept 2's identity).
- *Edge cases:* $d=0$ removes nothing, $E[(X-0)_+]=E[X]=1.56$ (the whole loss); a deductible $d\ge5$ (above the max loss) pays $0$.

**Beat 8 — Picture it.** Plot the per-loss *payment* against the *loss*: it sits flat at $0$ until the loss clears the deductible, then climbs one-for-one. (The figure also shows a maximum covered loss $u$, previewed in Concept 2 — note the payment goes flat again once the loss passes $u$.)

<figure>
<img src="../../assets/diagrams/ch06_deductible_limit.png" alt="Per-loss payment plotted against loss X for the Safari gear-loss, with deductible d=2 and maximum covered loss u=3. A dashed grey 45-degree reference line shows what a policy paying the full loss would pay. The purple step function (the actual per-loss payment) is flat at 0 from loss 0 up to the deductible at 2, then jumps up one-for-one through the shaded green covered layer between 2 and 3, then goes flat at the value u minus d = 1 for all losses above 3, because the excess over the maximum covered loss u is not covered. Vertical dotted lines mark the deductible at 2 and the maximum covered loss at 3. A real Safari Ball item glyph sits in the upper-left margin." style="width:88%; max-width:680px; display:block; margin:1em auto;">
<figcaption>The per-loss payment $g(X)=(X\wedge u)-(X\wedge d)$: flat at $0$ below the deductible $d$, rising one-for-one through the <strong>covered layer</strong>, then flat at $u-d$ once the loss passes the maximum covered loss $u$. The deductible knocks off the bottom; the limit (Concept 2) caps the top.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now take any discrete loss, apply an ordinary deductible, and find the expected per-loss payment two ways — the direct sum $\sum(k-d)_+p(k)$ or the survival shortcut $\sum_{k\ge d}S(k)$ — and you will never again report $E[X]-d$ with its impossible negative payment.

::: pokedex-entry
**POKÉDEX ENTRY №27 — The Ordinary Deductible**

A policy with ordinary deductible $d$ pays the **per-loss** amount
$$Y_L=(X-d)_+=\max(X-d,0), \qquad E[(X-d)_+]=\sum_k (k-d)_+\,p(k)=\sum_{k\ge d}S(k).$$

*In plain terms:* the trainer eats the first $d$; the policy pays the excess, floored at zero. The mean is the survival summed from $d$ onward — **not** $E[X]-d$.

*Recognition cue:* "the trainer covers the first ___," "**in excess of**," "after a deductible of $d$" → reach for $(X-d)_+$. If your "payment" comes out negative, you subtracted $d$ from the mean instead of flooring at zero.
:::

## Concept 2 — Policy Limit, Coinsurance, and the Budget Identity {#concept-2}

::: concept-gate
**DO YOU ALREADY OWN THIS? — Limit, coinsurance, identity**

For the Safari loss $X$: (a) find the limited expected value $E[X\wedge 3]$; (b) verify $E[X\wedge 3]+E[(X-3)_+]=E[X]=1.56$; (c) a full policy has $d=2$, max covered loss $u=4$, coinsurance $\alpha=0.8$ — find the expected per-loss payment.

If you wrote **(a) $E[X\wedge3]=1.40$**, **(b) $1.40+0.16=1.56$ ✓**, and **(c) $0.8(E[X\wedge4]-E[X\wedge2])=0.8(1.52-1.11)=0.328$**, **skip to Concept 3**. If the *order* of operations, or where the wedge $\wedge$ goes, is fuzzy, read on.
:::

**Beat 1 — The one-sentence idea.** *A policy limit caps the loss at $u$ — anything above $u$ is recorded as exactly $u$ — and the loss splits cleanly into "the part the cap keeps" plus "the part above the cap," which add back to the whole; coinsurance then scales the covered layer by a fraction $\alpha$.*

**Beat 2 — Anchor + concrete instance.** Concept 1 knocked off the *bottom*. The limit does the mirror move — it chops the *top*. The Warden's reserve fund can't absorb a freak $5{,}000$ loss, so she sets a **maximum covered loss** $u=3$: she'll record any loss as at most $3$. The capped loss is the smaller of $X$ and $u$ — for our table, $\min(0,3),\min(1,3),\dots=0,1,2,3,3,3$.

**Beat 3 — Reason through it in plain words.** Capping at $u$ replaces every big loss with the ceiling $u$. So the *limited loss* $X\wedge u$ keeps the small losses untouched and flattens all the big ones to $u$. Whatever the cap discards — the part of each loss poking above $u$ — is *exactly* the excess $(X-u)_+$ from Concept 1. The cap and the excess are two halves of the same loss: **what you keep plus what you cut equals the whole.** That is the budget identity, and it lets you compute any one of $\{E[X],\,E[X\wedge u],\,E[(X-u)_+]\}$ from the other two.

**Beat 4 — Surface and dismantle the tempting wrong idea.** *(This is the other half of Team Rocket's trap.)* The dangerous error is **applying the operations out of order** — specifically, **applying the deductible *after* the limit instead of before**, when $u$ is a cap on the *payment*. If the Warden caps what she'll *pay* at $u$, the correct sequence is **deductible first, then cap the payment**: $\min\big((X-d)_+,\,u\big)$. Capping the *loss* first and *then* subtracting the deductible — $(\,\min(X,u)-d\,)_+$ — is a different, smaller number, and with a tight cap it can wrongly collapse to **zero**. (We'll watch Team Rocket make exactly this mistake and conclude "the policy pays nothing.") Decide whether $u$ caps the **loss** (the standard "maximum covered loss," handled by the wedge) or the **payment**, and run the operations in the fixed order: **deductible → limit → coinsurance.**

**Beat 5 — Translate into notation, one glyph at a time.** "The smaller of $X$ and $u$" gets the **minimum**, written with a wedge $\wedge$:
$$X\wedge u=\min(X,u) \qquad \text{read aloud: ``}X \text{ capped at } u\text{,'' or ``}X \text{ wedge } u\text{.''}$$
Its expectation is the **limited expected value**:
$$E[X\wedge u]=\sum_k \min(k,u)\,p(k)=\sum_{k=0}^{u-1}S(k).$$
**Coinsurance** $\alpha$ (Greek "alpha") is the fraction of the covered layer the insurer pays — e.g. $\alpha=0.8$ means $80$ cents on the dollar. The **full per-loss payment** with a deductible $d$, maximum *covered loss* $u$, and coinsurance $\alpha$ is the **covered layer between $d$ and $u$**, scaled:
$$Y_L=\alpha\big[(X\wedge u)-(X\wedge d)\big], \qquad E[Y_L]=\alpha\big(E[X\wedge u]-E[X\wedge d]\big).$$

**Beat 6 — Derive the limited value, then the budget identity.** *Limited value (direct).* Cap each loss at $u=3$, then average:

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|---|
| $\min(k,3)$ | $0$ | $1$ | $2$ | $3$ | $3$ | $3$ |
| $p(k)$ | $0.30$ | $0.25$ | $0.20$ | $0.13$ | $0.08$ | $0.04$ |

$$E[X\wedge3]=0(0.30)+1(0.25)+2(0.20)+3(0.13)+3(0.08)+3(0.04)=0.25+0.40+0.39+0.24+0.12=1.40.$$
The survival shortcut agrees: $E[X\wedge3]=S(0)+S(1)+S(2)=0.70+0.45+0.25=1.40$. ✓

*Budget identity.* Add the limited value to the excess of Concept 1 (with $u$ in the deductible's old role):
$$E[X\wedge u]+E[(X-u)_+]=\underbrace{\sum_{k=0}^{u-1}S(k)}_{\text{cap keeps}}+\underbrace{\sum_{k\ge u}S(k)}_{\text{excess cut}}=\sum_{k\ge0}S(k)=E[X].$$
Numerically: $E[X\wedge3]+E[(X-3)_+]=1.40+0.16=1.56=E[X]$. ✓ The two survival sums simply partition the *same* full sum that makes $E[X]$.

*Full policy.* With $d=2$, $u=4$, $\alpha=0.8$, first the two limited values:
$$E[X\wedge2]=S(0)+S(1)=0.70+0.45=1.15? $$
— careful: that sum has only $u=2$ terms but we must double-check against the direct sum. Direct: $\min(k,2)=0,1,2,2,2,2$, so $E[X\wedge2]=0+0.25+2(0.20+0.13+0.08+0.04)=0.25+2(0.45)=0.25+0.90=1.15$? The survival form gives $S(0)+S(1)=1.15$ as well. Both agree at $E[X\wedge2]=1.15$. Wait — recompute with the table to be exact:
$$E[X\wedge2]=0(0.30)+1(0.25)+2(0.20)+2(0.13)+2(0.08)+2(0.04)=0.25+0.40+0.26+0.16+0.08=1.15.$$
And $E[X\wedge4]=S(0)+S(1)+S(2)+S(3)=0.70+0.45+0.25+0.12=1.52$. So the covered layer and the payment are
$$E[Y_L]=\alpha\big(E[X\wedge4]-E[X\wedge2]\big)=0.8\,(1.52-1.15)=0.8(0.37)=0.296.$$
(The Warden pays, on average, about $296$ Poké-dollars per flee under this policy — the number she needs to set the gate fee.)

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $E[X\wedge3]=1.40$ from the table or three survival terms.
- *Twist (use the identity backward):* told $E[X]=1.56$ and $E[X\wedge3]=1.40$, get the excess for free: $E[(X-3)_+]=1.56-1.40=0.16$ — no new sum.
- *General (full policy):* $E[Y_L]=\alpha\big(E[X\wedge u]-E[X\wedge d]\big)$ — the layer between $d$ and $u$, scaled by $\alpha$.
- *Edge:* $u\to\infty$ (no real cap) gives $E[X\wedge u]\to E[X]$ and the excess $\to 0$; $u=d$ gives a zero-width layer and zero payment.

**Beat 8 — Picture it.** The mean $E[X]$ is the total area of the survival bars. A cut at the limit $u$ splits that area into the part the cap *keeps* ($E[X\wedge u]$) and the *excess* it cuts ($E[(X-u)_+]$) — and the two add back to $E[X]$.

<figure>
<img src="../../assets/diagrams/ch06_safari_budget.png" alt="The survival function S(k) of the Safari loss drawn as a staircase of shaded unit-width bars: heights S(0)=0.70, S(1)=0.45, S(2)=0.25, S(3)=0.12, S(4)=0.04. A vertical dotted line marks the limit u=3. The three bars to the left of the cut (k=0,1,2) are shaded green and labelled 'kept by the limit, E[X wedge 3] = 1.40'; the two bars at and after the cut (k=3,4) are shaded red and labelled 'excess over u, E[(X-3)+] = 0.16'. A banner notes green plus red = 1.40 + 0.16 = 1.56 = E[X]. Real Tauros and Kangaskhan sprites sit in the right margin." style="width:88%; max-width:680px; display:block; margin:1em auto;">
<figcaption>The budget identity made visual: each survival bar $S(k)$ is one Poké-dollar of expected loss. The limit $u$ splits the total $E[X]=1.56$ into what the cap <strong>keeps</strong> ($E[X\wedge u]=1.40$, green) and the <strong>excess</strong> it cuts ($E[(X-u)_+]=0.16$, red). $1.40+0.16=1.56$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now cap a discrete loss with the wedge $X\wedge u$, compute its limited expected value by table or survival sum, scale a covered layer by coinsurance, and use the budget identity $E[X\wedge u]+E[(X-u)_+]=E[X]$ to get any piece from the other two — always running deductible → limit → coinsurance in that order.

::: pokedex-entry
**POKÉDEX ENTRY №28 — Limit, Coinsurance & the Budget Identity**

$$X\wedge u=\min(X,u),\qquad E[X\wedge u]=\sum_k\min(k,u)\,p(k)=\sum_{k=0}^{u-1}S(k).$$
$$\boxed{\,E[X\wedge u]+E[(X-u)_+]=E[X]\,}\qquad\text{Full policy: } E[Y_L]=\alpha\big(E[X\wedge u]-E[X\wedge d]\big).$$

*In plain terms:* the limit caps the loss at $u$; the cap-keeps and the excess add back to the whole loss. A full policy pays $\alpha$ times the covered layer between the deductible and the maximum covered loss.

*Recognition cue:* "maximum covered loss / policy limit / records at most ___" → $X\wedge u$. Given $E[X]$ and one of $\{E[X\wedge u],E[(X-u)_+]\}$, the identity hands you the other. Order is fixed: **deductible → limit → coinsurance.**
:::

## Concept 3 — Per-Loss vs Per-Payment (and the Bookkeeping Approach) {#concept-3}

::: concept-gate
**DO YOU ALREADY OWN THIS? — Per-loss vs per-payment**

For the Safari loss with deductible $d=2$, you found $E[(X-2)_+]=0.41$ **per loss**. Now find the expected payment **per payment** — the average size of an actual, nonzero payout.

If you wrote **$E[X-2\mid X>2]=\dfrac{E[(X-2)_+]}{P(X>2)}=\dfrac{0.41}{0.25}=1.64$**, **skip to the Worked Examples**. If you're unsure why we divide — or by *what* — read on.
:::

**Beat 1 — The one-sentence idea.** *The **per-loss** average counts every flee (including the zeros from losses below the deductible); the **per-payment** average counts only the flees that actually pay, so you divide the per-loss expectation by the probability a payment happens, $P(X>d)$.*

**Beat 2 — Anchor + concrete instance.** The Warden has two different questions, and they have two different answers. *"What does the Zone pay on average per flee?"* counts every flee, zeros and all → **per loss**, $0.41$. *"When the Zone actually cuts a cheque, how big is it on average?"* counts only the cheques → **per payment**. Since only $P(X>2)=S(2)=0.25$ of flees ever clear the deductible, the typical *cheque* is much bigger than the typical *flee-payment*.

**Beat 3 — Reason through it in plain words.** Per-loss spreads the total payout over *all* flees; per-payment spreads the same total over only the flees that paid. Same numerator (total expected dollars), smaller denominator (only the payers), so the per-payment figure is larger. The conversion is one division: drop the zeros and renormalize by their complement, $P(X>d)$. Per-loss is what the insurer needs to set the **premium** (it must cover every policy sold); per-payment is what a claimant experiences (the **average cheque**).

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two slips. First, **dividing by the wrong thing** — dividing by $P(X\ge d)$ or by $F(d)$ instead of $P(X>d)$. A payment occurs precisely when the loss *strictly exceeds* the deductible, so the denominator is $S(d)=P(X>d)$ (for our $d=2$, that's $0.25$, the chance the loss is $3,4,$ or $5$). Second, **confusing which average the problem wants** — "per loss" / "per claim filed" / "expected cost per policy" is per-loss; "per payment" / "average payment made" / "given a payment is made" is per-payment. Read the conditioning words.

**Beat 5 — Translate into notation, one glyph at a time.** The per-loss payment $Y_L=(X-d)_+$ counts zeros; the per-payment variable is $Y_L$ **conditioned on a payment occurring**:
$$\underbrace{E[(X-d)_+]}_{\text{per loss }(Y_L)} \qquad\text{vs}\qquad \underbrace{E\big[X-d \,\big|\, X>d\big]}_{\text{per payment }(Y_P)}=\frac{E[(X-d)_+]}{P(X>d)}.$$
Read the divisor aloud: "the probability the loss exceeds the deductible" — the fraction of flees that generate a cheque.

**Beat 6 — Derive it from the definition.** Conditioning shrinks the world to the flees with $X>d$. By the definition of conditional expectation,
$$E[X-d\mid X>d]=\frac{E\big[(X-d)\,\mathbf{1}\{X>d\}\big]}{P(X>d)}=\frac{E[(X-d)_+]}{P(X>d)},$$
because $(X-d)\mathbf{1}\{X>d\}$ and $(X-d)_+$ are the *same* random variable (both are $X-d$ where $X>d$ and $0$ elsewhere). For our policy:
$$E[X-2\mid X>2]=\frac{E[(X-2)_+]}{P(X>2)}=\frac{0.41}{0.25}=1.64.$$
So while the Zone pays $0.41$ *per flee*, the average *cheque it writes* is $1.64$ — four times larger, because three-quarters of flees never trigger a payment.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* per-payment $=$ per-loss $\div\,P(X>d)=0.41/0.25=1.64$.
- *Twist (full policy per-payment):* with a deductible *and* a limit, the per-payment average is still per-loss $\div\,P(X>d)$ — the denominator is set by the deductible (the thing that decides whether a payment happens), not the limit.
- *General:* per-payment $=\dfrac{E[Y_L]}{P(X>d)}$ for any policy whose payment is zero exactly when $X\le d$.
- *Edge:* $d=0$ makes every flee a payment, so $P(X>0)=0.70<1$ still (losses of $0$ pay $0$) — read the support carefully; here a loss of exactly $0$ pays $0$ even with no deductible.

**Beat 8 — Picture it.** Per-loss keeps the big lump of zero-payments; per-payment deletes that lump and renormalizes what's left. The two pmfs — and their two means — sit side by side.

<figure>
<img src="../../assets/diagrams/ch06_payment_per_loss.png" alt="Two bar charts side by side for the Safari policy with deductible d=2. Left ('PER LOSS, counts every flee, zeros included'): the per-loss payment pmf with a large grey bar of height 0.75 at payment 0 (the lump of losses that never clear the deductible), then small purple bars 0.13 at payment 1, 0.08 at 2, 0.04 at 3; the panel reports E[Y_L] = 0.41. Right ('PER PAYMENT, only the flees that actually pay'): the same distribution with the zero bar removed and the rest renormalized by P(X>d)=0.25, giving blue bars 0.52 at 1, 0.32 at 2, 0.16 at 3; the panel reports E[Y_P] = 1.64 and shows the conversion E[Y_P] = E[Y_L]/P(X>d) = 0.41/0.25 = 1.64. A real Poke Ball sits in the top-right margin." style="width:92%; max-width:760px; display:block; margin:1em auto;">
<figcaption>Per-loss (left) keeps the lump of zero payments (grey, $P(\text{pay}=0)=F(d)=0.75$) and averages to $E[Y_L]=0.41$. Per-payment (right) deletes the zeros and renormalizes by $P(X>d)=0.25$, averaging to $E[Y_P]=0.41/0.25=1.64$. Same total dollars, two denominators.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now tell per-loss from per-payment by reading the conditioning words, convert between them with a single division by $P(X>d)$, and explain why the per-payment cheque is larger — the zeros are gone. The whole chapter is now a tidy bookkeeping recipe: pick the function $g$, sum $g(k)\,p(k)$, and divide by $P(X>d)$ if (and only if) the question is per-payment.

::: pokedex-entry
**POKÉDEX ENTRY №29 — Per-Loss vs Per-Payment**

$$\text{per loss: } E[(X-d)_+]; \qquad \text{per payment: } E[X-d\mid X>d]=\frac{E[(X-d)_+]}{P(X>d)}.$$

*In plain terms:* per-loss averages over **every** loss (zeros included) — what the insurer needs for the premium. Per-payment averages over **only the flees that pay** — divide out the zeros by $P(X>d)$.

*Recognition cue:* "per loss / per policy / expected cost" → per-loss. "per payment / average payment made / given a payment occurs" → divide by $P(X>d)$. The denominator is always $P(X>d)$, the chance a loss clears the deductible.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:170px; text-align:center;">
<img src="../../assets/vs/koga.png" alt="Koga, the Fuchsia City Gym Leader, a ninja master of poison-type Pokemon" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Koga — Fuchsia Gym Leader, your coverage mentor</figcaption>
</figure>

Three examples, fading from fully narrated to exam speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast bookkeeping *how*), because the build-$g$-then-sum workflow is the load-bearing skill of the whole topic. All use the chapter loss $X\in\{0,\dots,5\}$ with pmf $0.30,0.25,0.20,0.13,0.08,0.04$ and survival $S=0.70,0.45,0.25,0.12,0.04$.

### Worked Example 1 — The Warden's Trial Policy (full narration; understanding-first)

**ARCHETYPE:** *Deductible-only policy — per-loss and per-payment, both roads.*

**Setup.** The Warden's trial policy has an ordinary deductible $d=2$, no limit, no coinsurance. Find (a) the expected payment **per loss**; (b) the expected payment **per payment**.

**Step 1 — Identify (what is the question really asking?).** "(a) per loss" = average over every flee, the function is $g(k)=(k-2)_+$. "(b) per payment" = average over only the flees that pay, so divide (a) by $P(X>2)$.

**Step 2 — Professor's Path (the why).**
*Per loss (direct LOTUS):* run each loss through $(k-2)_+ = 0,0,0,1,2,3$ and weight by $p(k)$:
$$E[(X-2)_+]=1(0.13)+2(0.08)+3(0.04)=0.13+0.16+0.12=0.41.$$
*Per loss (survival check):* $E[(X-2)_+]=S(2)+S(3)+S(4)=0.25+0.12+0.04=0.41.$ ✓ Same number, two roads.
*Per payment:* a payment occurs iff the loss clears $d=2$, i.e. with probability $P(X>2)=S(2)=0.25$. Divide:
$$E[X-2\mid X>2]=\frac{0.41}{0.25}=1.64.$$

**Step 3 — Trainer's Path (the fast bookkeeping).** Don't rebuild a payment pmf under time pressure. Make a four-row table — $k$, $p(k)$, $S(k)$, $(k-d)_+$ — once, and read everything off it. Per-loss is "sum the survival from $d$": $0.25+0.12+0.04=0.41$. Per-payment is "per-loss over $S(d)$": $0.41/0.25=1.64$. (On the TI-30XS you can even drop the payment values $(k-d)_+$ into L1 and the probabilities into L2 and run 1-Var Stats — $\bar x$ is the per-loss mean $0.41$ directly.)

**Step 4 — Check & pitfall.** Per-loss $0.41>0$ but well below $E[X]-d=-0.44$ (the impossible-negative trap) ✓; per-payment $1.64>0.41$ as it must be (fewer flees, same dollars) ✓. **Pitfalls:** reporting $E[X]-d$; dividing per-payment by $F(d)=0.75$ or by $P(X\ge d)$ instead of $P(X>d)=0.25$. *(Back-ref: Entries №27, №29.)*

### Worked Example 2 — Adding a Cap (partial guidance)

**ARCHETYPE:** *Limit + the budget identity; full policy with coinsurance.*

**Setup.** The Warden now caps coverage at a maximum covered loss $u=4$ and reimburses $\alpha=0.8$ of the covered layer, keeping the deductible $d=2$. (a) Find $E[X\wedge4]$ and $E[X\wedge2]$. (b) Find the expected per-loss payment. (c) Use the budget identity to find $E[(X-4)_+]$ without a new sum.

**Identify.** "Maximum covered loss" → wedge $X\wedge u$; "full policy" → $\alpha\,(E[X\wedge u]-E[X\wedge d])$; "without a new sum" → budget identity.

**(a) Limited values (survival sums).** $E[X\wedge4]=S(0)+S(1)+S(2)+S(3)=0.70+0.45+0.25+0.12=1.52.$ $E[X\wedge2]=S(0)+S(1)=0.70+0.45=1.15.$

**(b) Full policy.** $E[Y_L]=\alpha\big(E[X\wedge4]-E[X\wedge2]\big)=0.8(1.52-1.15)=0.8(0.37)=0.296.$

**(c) Budget identity.** $E[(X-4)_+]=E[X]-E[X\wedge4]=1.56-1.52=0.04.$ (Direct check: only $k=5$ contributes, $(5-4)(0.04)=0.04$ ✓.)

**Check & pitfall.** The covered layer $0.37$ is less than the deductible-only per-loss $0.41$ from WE 1 — the cap removed the bit above $u=4$ ✓; coinsurance shrinks it further to $0.296$ ✓. **Pitfall:** scaling by $\alpha$ *before* taking the layer, or capping the *payment* instead of the *loss*. *(Back-ref: Entry №28.)*

### Worked Example 3 — Which Average Does the Question Want? (exam speed)

**ARCHETYPE:** *Read the conditioning words; per-loss vs per-payment under a full policy.*

**Setup.** Under the policy of WE 2 ($d=2$, $u=4$, $\alpha=0.8$, so $E[Y_L]=0.296$), a trainer asks: "When the Zone *actually pays me*, how much do I get on average?" Find it.

A payment happens iff $X>d=2$, so $P(X>2)=S(2)=0.25$. The limit doesn't change *whether* a payment occurs — only its size. So
$$E[Y_P]=\frac{E[Y_L]}{P(X>d)}=\frac{0.296}{0.25}=1.184.$$

**Check & pitfall.** $1.184>0.296$ ✓ (zeros dropped). **Pitfall:** dividing by $P(X>u)$ (the limit) instead of $P(X>d)$ (the deductible) — the deductible decides whether a cheque is written. *(Back-ref: Entries №28, №29.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — Build the four-row table once, read everything off it**

For any discrete deductible/limit problem, write one table: $k$, $p(k)$, $S(k)=P(X>k)$, and the payment function $g(k)$. Then every quantity is a one-line read: $E[(X-d)_+]=\sum_{k\ge d}S(k)$; $E[X\wedge u]=\sum_{k=0}^{u-1}S(k)$; the full per-loss payment $=\alpha\big(E[X\wedge u]-E[X\wedge d]\big)$; per-payment $=$ per-loss $\div\,P(X>d)$. The survival row turns most sums into three or four additions — no products.
:::

::: trainers-tip
**TRAINER'S TIP — Never subtract the deductible from the mean**

$E[(X-d)_+]\ne E[X]-d$. Subtracting $d$ from the mean assumes *every* loss clears the deductible; the losses below $d$ pay $0$, not a negative amount. If your "expected payment" comes out negative (or even just suspiciously close to $E[X]-d$), you made this error. Floor at zero *first*, then average — or use $\sum_{k\ge d}S(k)$, which floors automatically.
:::

::: trainers-tip
**TRAINER'S TIP — The order is deductible → limit → coinsurance**

When a problem stacks modifications, apply them in that fixed order, and decide whether $u$ caps the **loss** (maximum covered loss → use $X\wedge u$ and the layer $E[X\wedge u]-E[X\wedge d]$) or the **payment** (maximum payment → cap *after* the deductible, $\min((X-d)_+,u)$). Capping the loss first and *then* subtracting the deductible is the canonical setup error — it can wrongly zero out the whole payment.
:::

::: trainers-tip
**TRAINER'S TIP — The budget identity is a free third value**

$E[X\wedge u]+E[(X-u)_+]=E[X]$ means any one of the three is the other two. If a problem hands you $E[X]$ and $E[X\wedge u]$ and asks for the expected excess, don't sum anything — subtract: $E[(X-u)_+]=E[X]-E[X\wedge u]$. This single identity short-circuits a large share of deductible/limit problems.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

<figure style="margin:1em auto; max-width:150px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket — Jessie, James, and Meowth" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
</figure>

Team Rocket has swiped a copy of the Warden's policy and plans to sell a knock-off coverage scheme to Safari tourists. Meowth does the pricing. "Da policy's got a deductible of **two** thousand and we'll never pay more than **two** thousand on one flee," he announces. "So here's da slick part: first I *cap* every loss at two — nuthin' over two thousand counts — den I knock off da two-thousand deductible. Two minus two is *zero!* We collect da gate fees and **pay out nuthin'!** We'll be rich by sundown!"

Jessie grins. "Free money. I love a deductible."

James squints at the figures. "But Jessie… if a Pokémon wrecks five thousand of gear, surely *some* of that gets paid…?"

Meowth waves a paw. "Nah! Cap first, *den* deductible! Da cap eats it all! Trust da Meowth!"

**Where it fails:** Meowth applied the **deductible *after* the limit** when the limit is a cap on the *payment*. The correct order is **deductible first, then cap the payment**: $\min\big((X-d)_+,\,u\big)$. With $d=2$ and a maximum *payment* of $u=2$:
$$\text{Correct: } E\big[\min((X-2)_+,2)\big]=\min(0,2)p_0+\cdots+\min(1,2)(0.13)+\min(2,2)(0.08)+\min(3,2)(0.04)$$
$$=1(0.13)+2(0.08)+2(0.04)=0.13+0.16+0.08=0.37.$$
But Meowth computed $E\big[(\min(X,2)-2)_+\big]$ — cap the *loss* at $2$ first (giving $0,1,2,2,2,2$), *then* subtract the deductible $2$ and floor — which is $0$ for **every** loss. He convinced himself the policy pays nothing when it actually pays $0.37$ per flee on average. Order matters: **deductible before limit.** (You'll catch Meowth red-handed in Problem C6.8.)
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

This is the literal arithmetic of **every auto and health insurance policy you will ever hold.**

Your car policy has a **deductible** (you pay the first \$500 of a fender-bender), a **policy limit** (the insurer won't pay above the coverage cap), and often **coinsurance** (after the deductible, you and the insurer split costs — the classic "80/20" health plan is $\alpha=0.8$). The premium you're quoted is built from the **per-loss expected payment** $E[Y_L]$ — the insurer must collect, across all policyholders, enough to cover the average payout *per policy sold*, including the many policies that never file a claim (the zeros). When you instead ask "if I actually file a claim, what does it pay?" you're asking the **per-payment** question, $E[Y_L]/P(X>d)$. The **budget identity** $E[X\wedge u]+E[(X-u)_+]=E[X]$ is how a pricing actuary moves between the insurer's retained layer and the reinsurer's excess layer in a single line. And the order-of-operations rule — deductible, then limit, then coinsurance — is written into the policy contract; reverse it (Team Rocket's mistake) and you misprice the cover.

*Series bridge:* here the loss is **discrete** so every expectation is a finite sum. In **ch13 (Cinnabar)** the same four operations return for **continuous** losses, where the sums become **survival integrals** $\int_d^\infty S(x)\,dx$ and $\int_0^u S(x)\,dx$ — identical ideas, calculus instead of tables. From there these limited-expected-value tools feed directly into **loss models and ratemaking** on the later actuarial exams (STAM/FAM-Short).

*Transfer check:* could you solve this with no Pokémon in it? "A discrete loss takes values $0$–$5$ with probabilities $0.30,0.25,0.20,0.13,0.08,0.04$; a policy has deductible $2$, maximum covered loss $4$, and pays $80\%$ of the covered layer. Find the expected payment per loss." Same $0.296$. If you can do that, the skill has transferred.
:::

## The Gym Battle — Soul Badge Capstone

<figure style="margin:1.5em auto; max-width:170px; text-align:center;">
<img src="../../assets/vs/koga.png" alt="Koga, the Fuchsia Gym Leader, ready for a battle" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Koga's challenge — the full policy, both averages</figcaption>
</figure>

**Koga's Challenge.** The ninja master steps from behind a hidden wall, the Warden's ledger in hand. "A true actuary, like a true ninja, must see the *whole* picture from a single sheet. The Safari loss $X$ takes values $0$ through $5$ thousand with probabilities $0.30,0.25,0.20,0.13,0.08,0.04$. My final policy carries a deductible $d=2$, a maximum covered loss $u=4$, and coinsurance $\alpha=0.8$. Tell me — in one pass:

(a) the expected payment **per loss** (so the Warden can price the gate fee);
(b) the expected payment **per payment** (so a claimant knows the typical cheque);
(c) and prove your limited value with the **budget identity**.

Falter on the order of operations, and you leave empty-handed."

**ARCHETYPE:** *Full discrete policy — per-loss, per-payment, and the identity, in one pass.*

**Step 1 — Identify.** A full policy: deductible, limit (maximum covered loss), coinsurance. Per-loss is the scaled covered layer; per-payment divides by $P(X>d)$; the identity cross-checks the limited value.

**Step 2 — Trainer's Path: the four-row table.**

| $k$ | $0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|---|
| $p(k)$ | $0.30$ | $0.25$ | $0.20$ | $0.13$ | $0.08$ | $0.04$ |
| $S(k)=P(X>k)$ | $0.70$ | $0.45$ | $0.25$ | $0.12$ | $0.04$ | $0$ |
| $\min(k,4)$ | $0$ | $1$ | $2$ | $3$ | $4$ | $4$ |
| $\min(k,2)$ | $0$ | $1$ | $2$ | $2$ | $2$ | $2$ |

**Step 3 — Solve.**
*Limited values (survival sums):*
$$E[X\wedge4]=S(0)+S(1)+S(2)+S(3)=0.70+0.45+0.25+0.12=1.52,$$
$$E[X\wedge2]=S(0)+S(1)=0.70+0.45=1.15.$$
*(a) Per loss:*
$$E[Y_L]=\alpha\big(E[X\wedge4]-E[X\wedge2]\big)=0.8(1.52-1.15)=0.8(0.37)=\boxed{0.296}.$$
*(b) Per payment:* a cheque is written iff $X>d=2$, probability $P(X>2)=S(2)=0.25$:
$$E[Y_P]=\frac{E[Y_L]}{P(X>2)}=\frac{0.296}{0.25}=\boxed{1.184}.$$
*(c) Budget identity, proving $E[X\wedge4]$:* the excess over $u=4$ is $E[(X-4)_+]=(5-4)(0.04)=0.04$, and
$$E[X\wedge4]+E[(X-4)_+]=1.52+0.04=1.56=E[X].\ \checkmark$$

**Step 4 — Check, verdict & the pitfall Koga is testing.** Per-loss $0.296>0$ and below the deductible-only $0.41$ (the cap and coinsurance both shrink it) ✓; per-payment $1.184>0.296$ ✓; the identity closes at $1.56$ ✓. The pitfall Koga is probing is the **order of operations** — a ninja who caps the loss first, subtracts the deductible, *then* scales would get a different (wrong) covered layer, and one who divides by $P(X>u)$ instead of $P(X>d)$ would misstate the cheque. **Verdict:** the Warden charges a gate fee built on $0.296$ per flee; a paying claimant averages $1.184$.

> "...Hmph," Koga murmurs, fading back into the shadows. "You ran the loss through the deductible, then the limit, then the coinsurance — and never once paid a negative amount. The **Soul Badge** is yours, Trainer."

## Badge Earned — the Soul Badge

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/soul_badge.png" alt="The Soul Badge, a pink heart-shaped gym badge awarded by Koga of Fuchsia City" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Soul Badge earned!</strong> Rank: Ace Trainer · 5 badges.</figcaption>
</figure>

You proved to Koga that a payment is just a loss run — in the right order — through a deductible, a limit, and a coinsurance factor, and he pressed the **Soul Badge** into your hand. **Rank: Ace Trainer · 5 badges** (Cascade + Thunder + Boulder + Rainbow + Soul). Five down, three to go on the road to the Indigo Plateau.

**Mastery checklist — tick each before you move on (mapped 1-to-1 to the SOA outcomes):**

- ☐ **(2e)** I can compute the per-loss payment under an **ordinary deductible**, $E[(X-d)_+]=\sum_{k\ge d}S(k)$, and I never report $E[X]-d$. *(Rematch: Concept 1, WE 1, Problems C6.1, C6.8.)*
- ☐ **(2e)** I can compute the **limited expected value** $E[X\wedge u]=\sum_{k=0}^{u-1}S(k)$ and assemble a **full policy** $\alpha\big(E[X\wedge u]-E[X\wedge d]\big)$ in the order deductible → limit → coinsurance. *(Rematch: Concept 2, WE 2, Problems C6.3, C6.5, C6.9.)*
- ☐ **(2e)** I can use the **budget identity** $E[X\wedge u]+E[(X-u)_+]=E[X]$ to get any piece from the other two. *(Rematch: Concept 2, WE 2(c), Problems C6.7, C6.16.)*
- ☐ **(2f)** I can distinguish the **loss** from the **payment** and convert **per-loss** to **per-payment** by dividing by $P(X>d)$. *(Rematch: Concept 3, WE 1, WE 3, Problems C6.2, C6.10, C6.13.)*

**Gym Rematch pointers.** Reported $E[X]-d$ as the payment? Concept 1 Beat 4 and the Team Rocket Trap, then C6.16. Capped the loss before the deductible? Concept 2 Beat 4, the Trap, then C6.8. Divided per-payment by the wrong probability? Concept 3 Beat 4, then C6.10. Summed instead of using the identity? Concept 2 Beat 7, then C6.7.

## The Gym Challenge — Problem Set

::: problem-set
**THE SAFARI ZONE WARDEN'S COVERAGE COMMISSION — your questline.** The Warden has hired you to price her visitor-insurance scheme. First the **Route Trainer** legs (warming up your deductible and limit tools on simple claims), then the **Gym Battle** tier (the boss fight — full policies at exam difficulty, with Koga and Team Rocket), then the optional **Elite Challenge** post-game. Work it timed (~6 min/problem), then check the **Answers** below. Hit the mastery bar (**80%+ with correct method**) to clear the commission and claim the Soul Badge. Markers: 🔴 routine method · 🟡 routine-with-a-twist · 🔵 stretch.

Several problems share the Safari loss $X\in\{0,1,2,3,4,5\}$, pmf $p=0.30,0.25,0.20,0.13,0.08,0.04$, survival $S=0.70,0.45,0.25,0.12,0.04,0$, and $E[X]=1.56$. Each problem restates whatever it needs, so you can work them in any order.

### Route Trainers (the early legs — warming up your tools)

**C6.1.** 🔴 *(The Warden's first quote: a flat deductible.)* For the Safari loss $X$, an ordinary deductible $d=1$ applies. Find the expected payment **per loss**, $E[(X-1)_+]$.

**C6.2.** 🟡 *(How big is an actual cheque?)* For the same policy ($d=1$, $E[(X-1)_+]=0.86$ given), find the expected payment **per payment**.

**C6.3.** 🔴 *(Capping the reserve.)* Find the limited expected value $E[X\wedge 3]$ for the Safari loss.

**C6.4.** 🔴 *(A different cap.)* Find $E[X\wedge 2]$ for the Safari loss.

**C6.5.** 🟡 *(A full trial policy.)* A policy has deductible $d=1$, maximum covered loss $u=3$, coinsurance $\alpha=0.9$. Given $E[X\wedge3]=1.40$ and $E[X\wedge1]=0.70$, find the expected payment per loss.

**C6.6.** 🔴 *(Uniform Safari critters.)* A different loss $Y$ is discrete uniform on $\{0,1,2,3,4\}$ (each w.p. $0.2$). With deductible $d=2$, find $E[(Y-2)_+]$ per loss.

**C6.7.** 🟡 *(Use the identity, don't sum.)* Given $E[X]=1.56$ and $E[X\wedge 4]=1.52$, find the expected excess $E[(X-4)_+]$ using the budget identity.

> *Questline beat: your quotes are warm and the Warden is pleased. But Koga guards the gym, and Team Rocket is selling a knock-off policy at the gate. The boss fights begin.*

### Gym Battles (the boss fight — true SOA difficulty)

**C6.8.** 🟡 *(AUDIT — Team Rocket's knock-off policy.)* Team Rocket's policy has deductible $d=2$ and a maximum **payment** of $u=2$. Meowth caps the loss at $2$ first, *then* subtracts the deductible, and declares "the policy pays $0$ per flee." Find the **correct** expected payment per loss (deductible first, then cap the payment) and name Meowth's error.

**C6.9.** 🟡 *(Koga's full policy, per loss.)* The Soul-Badge policy has $d=2$, maximum covered loss $u=4$, coinsurance $\alpha=0.8$. Given $E[X\wedge4]=1.52$ and $E[X\wedge2]=1.15$, find the expected payment per loss.

**C6.10.** 🟡 *(Koga's full policy, per payment.)* For the policy in C6.9 ($E[Y_L]=0.296$ given), find the expected payment **per payment**. (Careful which probability you divide by.)

**C6.11.** 🔵 *(Per loss, both roads, with a limit.)* For the Safari loss with deductible $d=2$ and maximum covered loss $u=4$ (no coinsurance), find the per-loss payment $E[X\wedge4]-E[X\wedge2]$ **and** verify it equals the direct sum $\sum_k\big(\min(k,4)-\min(k,2)\big)p(k)$.

**C6.12.** 🟡 *(Coinsurance only — no deductible, no limit.)* A simple co-pay plan covers $\alpha=0.75$ of every loss with no deductible and no cap. Find the expected payment per loss. (Hint: $E[\alpha X]=\alpha E[X]$.)

**C6.13.** 🔵 *(RIVAL TRAP — Gary brags about his "average claim.")* Gary buys the deductible-$2$ policy and crows: "My expected payment per loss is $0.41$, so when I file a claim I'll average a $0.41$-thousand cheque — barely worth it." Find the true expected payment **per payment** and explain Gary's error in confusing per-loss with per-payment.

**C6.14.** 🟡 *(Maximum covered loss vs deductible, per-loss layer.)* For the Safari loss, a policy pays the layer between $d=1$ and $u=4$ at full coinsurance ($\alpha=1$). Find the expected payment per loss.

**C6.15.** 🔵 *(DECISION — two policies, which costs the Warden more?)* The Warden must choose one of two reimbursement plans for the same loss $X$. **Plan A:** deductible $d=2$, no limit, $\alpha=1$. **Plan B:** no deductible, maximum covered loss $u=2$, $\alpha=1$. Compute the expected payment per loss for each and recommend the *cheaper* plan for the Warden.

**C6.16.** 🟡 *(AUDIT — the "mean minus deductible" error.)* An apprentice records "deductible $d=2$, so expected per-loss payment $=E[X]-d=1.56-2=-0.44$." Find the true per-loss payment and name the error.

> *Questline beat: the Soul Badge is yours and Team Rocket's scam is exposed. The post-game below is optional — the integrative challenges the league players sharpen up on.*

### Elite Challenge (post-game — integrative / stretch)

**C6.17.** 🔵 *(Full policy from scratch — both averages and the identity.)* For the Safari loss, a policy has $d=1$, maximum covered loss $u=4$, coinsurance $\alpha=0.9$. (a) Find $E[X\wedge4]$ and $E[X\wedge1]$ from the survival row. (b) Find the per-loss payment. (c) Find the per-payment payment. (d) Confirm $E[X\wedge4]+E[(X-4)_+]=E[X]$.

**C6.18.** 🔵 *(RIVAL TRAP — Gary reverses the order.)* Gary prices a policy with deductible $d=1$ and maximum covered loss $u=3$ by capping the loss at $3$, then computing $E[X\wedge3]-d\cdot P(X>d)$ "to remove the deductible." Find the **correct** per-loss payment $E[X\wedge3]-E[X\wedge1]$ and explain why Gary's shortcut is wrong.
:::

## Answers

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

### Quick-Answer Table

| # | Answer | Archetype | | # | Answer | Archetype |
|---|---|---|---|---|---|---|
| C6.1 | $0.86$ | standard | | C6.10 | $1.184$ | standard |
| C6.2 | $1.911$ | standard | | C6.11 | $0.37$ (both roads) | standard |
| C6.3 | $1.40$ | standard | | C6.12 | $1.17$ | standard |
| C6.4 | $1.15$ | standard | | C6.13 | per-payment $=1.64$; Gary confused the two | rival_trap |
| C6.5 | $0.63$ | standard | | C6.14 | $0.82$ | standard |
| C6.6 | $0.60$ | standard | | C6.15 | A $0.41$, B $1.15$; choose A | decision |
| C6.7 | $0.04$ | standard | | C6.16 | $0.41$ (not $-0.44$) | audit |
| C6.8 | $0.37$ (not $0$) | audit | | C6.17 | see below | standard |
| C6.9 | $0.296$ | standard | | C6.18 | $0.70$; Gary's shortcut wrong | rival_trap |

**C6.1** — *(standard) Ordinary deductible, per loss (Entry №27).* $E[(X-1)_+]=\sum_{k\ge1}S(k)=S(1)+S(2)+S(3)+S(4)=0.45+0.25+0.12+0.04=0.86.$ (Direct check: $(k-1)_+=0,0,1,2,3,4$, so $1(0.20)+2(0.13)+3(0.08)+4(0.04)=0.20+0.26+0.24+0.16=0.86$ ✓.)

**C6.2** — *(standard) Per payment (Entry №29).* A payment occurs iff $X>1$, so $P(X>1)=S(1)=0.45$. $E[X-1\mid X>1]=\dfrac{0.86}{0.45}=1.911.$

**C6.3** — *(standard) Limited expected value (Entry №28).* $E[X\wedge3]=\sum_{k=0}^{2}S(k)=S(0)+S(1)+S(2)=0.70+0.45+0.25=1.40.$

**C6.4** — *(standard) Limited expected value (Entry №28).* $E[X\wedge2]=S(0)+S(1)=0.70+0.45=1.15.$

**C6.5** — *(standard) Full policy, per loss (Entry №28).* $E[Y_L]=\alpha\big(E[X\wedge3]-E[X\wedge1]\big)=0.9(1.40-0.70)=0.9(0.70)=0.63.$

**C6.6** — *(standard) Deductible on a uniform loss (Entry №27).* $Y$ uniform on $\{0,1,2,3,4\}$, $p=0.2$ each. $(Y-2)_+=0,0,0,1,2$, so $E[(Y-2)_+]=1(0.2)+2(0.2)=0.6.$

**C6.7** — *(standard) Budget identity (Entry №28).* $E[(X-4)_+]=E[X]-E[X\wedge4]=1.56-1.52=0.04.$ (No new sum — the identity hands it over.)

**C6.8** — *(audit) Deductible-after-limit order error (Entries №27, №28).* **Correct order — deductible first, then cap the payment at $u=2$:** payment $=\min((X-2)_+,2)$. The values $(X-2)_+=0,0,0,1,2,3$ capped at $2$ are $0,0,0,1,2,2$, so $E[Y_L]=1(0.13)+2(0.08)+2(0.04)=0.13+0.16+0.08=0.37.$ **Meowth's error:** he capped the *loss* at $2$ first ($\min(X,2)=0,1,2,2,2,2$) and *then* subtracted the deductible $2$ and floored — $(\min(X,2)-2)_+=0$ for every loss — concluding the policy pays nothing. The deductible must be applied **before** the payment cap; the true per-loss payment is $0.37$, not $0$.

**C6.9** — *(standard) Koga's full policy, per loss (Entry №28).* $E[Y_L]=\alpha\big(E[X\wedge4]-E[X\wedge2]\big)=0.8(1.52-1.15)=0.8(0.37)=0.296.$

**C6.10** — *(standard) Full policy, per payment (Entry №29).* A cheque is written iff $X>d=2$, so divide by $P(X>2)=S(2)=0.25$ (the deductible, **not** the limit): $E[Y_P]=\dfrac{0.296}{0.25}=1.184.$

**C6.11** — *(standard) Covered layer, both roads (Entries №27, №28).* Layer via limited values: $E[X\wedge4]-E[X\wedge2]=1.52-1.15=0.37.$ Direct sum: $\min(k,4)-\min(k,2)=0,0,0,1,2,2$, so $1(0.13)+2(0.08)+2(0.04)=0.13+0.16+0.08=0.37.$ ✓ Equal.

**C6.12** — *(standard) Coinsurance only (Entry №28).* No deductible, no cap: $E[\alpha X]=\alpha E[X]=0.75(1.56)=1.17.$

**C6.13** — *(rival_trap) Per-loss vs per-payment confusion (Entry №29).* The $0.41$ Gary quotes is the **per-loss** average — it already includes the $75\%$ of flees that pay $0$. The size of an *actual cheque* is the **per-payment** average: $E[X-2\mid X>2]=\dfrac{0.41}{P(X>2)}=\dfrac{0.41}{0.25}=1.64.$ **Gary's error:** he read the per-loss figure as the typical payment. The typical *cheque* is $1.64$ thousand (four times larger), because most policies never pay and the per-loss number averages over those zeros.

**C6.14** — *(standard) Covered layer between $d=1$ and $u=4$ (Entry №28).* $E[X\wedge4]-E[X\wedge1]=1.52-0.70=0.82.$ (Direct: $\min(k,4)-\min(k,1)=0,0,1,2,3,3$, so $1(0.20)+2(0.13)+3(0.08)+3(0.04)=0.20+0.26+0.24+0.12=0.82$ ✓.)

**C6.15** — *(decision) Compare two plans, pick the cheaper for the insurer (Entries №27, №28).* **Plan A** (deductible $2$, no limit, $\alpha=1$): $E[(X-2)_+]=S(2)+S(3)+S(4)=0.25+0.12+0.04=0.41.$ **Plan B** (no deductible, cap $u=2$, $\alpha=1$): $E[X\wedge2]=S(0)+S(1)=0.70+0.45=1.15.$ Plan A costs the Warden $0.41$ per flee; Plan B costs $1.15$. **Recommend Plan A** — the deductible (which the trainer absorbs the bottom of) is far cheaper for the insurer than a low cap (which still pays out on every flee). Same loss, very different insurer cost.

**C6.16** — *(audit) Mean-minus-deductible error (Entry №27).* True per-loss payment: $E[(X-2)_+]=S(2)+S(3)+S(4)=0.25+0.12+0.04=0.41.$ **The apprentice's error:** $E[X]-d=1.56-2=-0.44$ assumes every loss clears the deductible, producing a nonsensical *negative* payment. Losses of $0,1,2$ pay $0$, not a negative amount; you must floor at zero before averaging. True payment $0.41$.

**C6.17** — *(standard) Full policy from scratch (Entries №27, №28, №29).* (a) $E[X\wedge4]=S(0)+S(1)+S(2)+S(3)=0.70+0.45+0.25+0.12=1.52$; $E[X\wedge1]=S(0)=0.70.$ (b) Per loss: $E[Y_L]=0.9(1.52-0.70)=0.9(0.82)=0.738.$ (c) Per payment: a cheque is written iff $X>1$, so divide by $P(X>1)=S(1)=0.45$: $E[Y_P]=\dfrac{0.738}{0.45}=1.64.$ (d) $E[(X-4)_+]=(5-4)(0.04)=0.04$, and $E[X\wedge4]+E[(X-4)_+]=1.52+0.04=1.56=E[X]$ ✓.

**C6.18** — *(rival_trap) Order/short-cut error (Entries №27, №28).* **Correct** per-loss payment for the layer between $d=1$ and $u=3$: $E[X\wedge3]-E[X\wedge1]=1.40-0.70=0.70.$ **Gary's shortcut** $E[X\wedge3]-d\cdot P(X>d)=1.40-1(0.45)=0.95$ is wrong: subtracting $d\cdot P(X>d)$ is *not* how a deductible removes the bottom of a capped loss. The deductible removes the limited value $E[X\wedge d]=E[X\wedge1]=0.70$, not $d\cdot P(X>d)=0.45$. The correct covered layer is the difference of two limited expected values, $0.70$.
:::

> Next stop: **Checkpoint A (ch07)** — a campfire on the route where you'll spaced-retrieve everything from the discrete act (Act I) before crossing into the continuous world. Pack your deductible-and-limit tools; the budget identity returns at Cinnabar (ch13) in calculus form.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
