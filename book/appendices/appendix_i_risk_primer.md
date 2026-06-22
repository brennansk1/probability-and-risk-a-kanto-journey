<!--
  file: appendix_i_risk_primer
  kind: appendix
  letter: I
  title: Risk & Insurance — A Trainer's Primer
  purpose: the SOA-assumed insurance/risk background behind the loss-and-payment outcomes;
           supports ch06 (discrete deductibles) and ch13 (continuous deductibles).
           A reader who has never seen insurance should finish able to follow every
           loss/payment problem in the book.
  sources: ch06, ch13
  plan: MASTER_PLAN_V3 §23 (appendix spec, item I)
  NOTE: notation matches ch06/ch13 exactly — per-loss Y_L, per-payment Y_P,
        deductible (X-d)+, limit X^u, coinsurance alpha, the budget/master identity,
        the per-payment divisor S(d)=P(X>d). No new mathematics; context only.
-->

# Appendix I — Risk & Insurance: A Trainer's Primer {.type-normal}

> **What this is — and who it's for.** Exam P teaches you to *compute* the expected payment under a deductible, a limit, and coinsurance (outcomes 2e–2f, the engine of **ch06** and **ch13**). What it quietly *assumes* — and never pauses to teach — is the insurance world those formulas live in: what a "loss" is, why anyone pools risk, why a deductible lowers a premium, and what the difference between "per loss" and "per payment" actually means to an insurer. This appendix supplies exactly that assumed background, in plain words, so a reader who has never held a policy can follow every loss/payment problem. **No new mathematics lives here** — every formula below is taught in its home chapter; this is the *context* that makes those formulas mean something. Notation matches the chapters throughout: $X$ the loss, $Y_L$ the per-loss payment, $Y_P$ the per-payment payment, $S(\cdot)$ the survival function, and the wedge $X \wedge u = \min(X,u)$.

We frame it through the **Pokémon Insurance Agency** and the **Safari Zone Warden**, who must price coverage against escaped, panicking, gear-wrecking Pokémon — the same Warden whose discrete claim table runs through ch06, now seen from the underwriter's chair.

---

## 1. What Insurance Is, in One Idea

A single trainer cannot predict their own bad luck. On any given Safari run, a spooked Tauros might trample nothing — or it might crush five thousand Poké-dollars of gear. For *one* trainer, the loss is a wild, unpredictable random variable. There is no "expected loss" they can feel in their pocket; there is only the run that happened.

The whole magic of insurance is this: **pool many independent risks, and the *average* loss becomes predictable even though each individual loss is not.** The Warden does not insure one trainer; she insures *thousands*. And while she cannot say what any single trainer will lose, she can say — with startling accuracy — what the *average* loss across all of them will be. The wilder each trainer's luck, the smoother their collective total.

That is not a slogan; it is a theorem, and you meet it head-on in **ch12**: the **Central Limit Theorem**. Add up many independent losses and the total (or the average) clusters tightly around its mean, in a bell shape, with relative spread that *shrinks* as the pool grows. The Agency sells unpredictability *to each customer* and buys predictability *for itself*, simply by adding up enough independent copies. Pooling converts a frightening individual gamble into a near-certain group average — the single idea the entire industry is built on.

Once the average payout per policy is predictable, pricing is almost arithmetic:

$$\text{Premium} \;=\; \underbrace{\E[\text{payment}]}_{\text{pure premium}} \;+\; \underbrace{\text{load}}_{\substack{\text{expenses, capital,}\\ \text{profit, risk margin}}}.$$

The first term — the **pure premium**, the expected amount the Agency pays out per policy — is the *entire point* of computing $\E[Y_L]$ in ch06 and ch13. The **load** covers everything else: the Agency's salaries, the cost of holding capital against a bad year, a margin for the risk that the pool is smaller or wilder than assumed, and profit. Exam P concerns itself with the first term; the load is the business wrapped around it. When you compute an expected payment, you are computing the raw material of a price.

::: trainers-tip
**THE ONE-LINE VERSION** — Insurance pools many independent risks so the *average* becomes predictable (the CLT, ch12). Once the average payout is known, **premium = expected payment (pure premium) + load.** Everything else in this appendix is detail on that expected payment.
:::

---

## 2. The Loss Random Variable $X$

Everything starts with the **ground-up loss**, written $X$. This is the *full* size of the damage, measured from zero, **before any policy provision touches it** — the raw severity of the event. By convention $X \ge 0$: a loss is never negative.

"Ground-up" is the word to remember. When a Tauros wrecks gear, $X$ is the entire repair bill — every Poké-dollar — regardless of who ends up paying it. The deductible, the limit, and the coinsurance are operations applied *to* $X$ to produce the payment; $X$ itself is innocent of all of them. Keeping $X$ (the loss) and $Y$ (the payment) strictly separate is the discipline ch06 opens with, and it is the discipline that keeps every later computation honest.

**Its distribution.** The loss $X$ carries a probability distribution like any random variable:

- **Discrete** (ch06): a finite table of possible losses with probabilities — the Warden's claim ledger, $X \in \{0,1,2,3,4,5\}$ thousand with a pmf $p(k)=P(X=k)$. Expectations are **sums**.
- **Continuous** (ch13): a smooth density $f(x)$ on $[0,\infty)$ — the Cinnabar volcano's damage, $X \sim \Expo(\theta)$. Any positive amount is possible. Expectations are **integrals**.

The two chapters are the same four operations on these two kinds of loss; this appendix's language covers both. The survival function $S(x)=P(X>x)=1-F(x)$ — "the chance the loss exceeds $x$" — is the workhorse in both, because expected payments turn out to be areas (or sums) *of the survival function* (the budget identity, §4 below).

**Frequency vs severity.** A subtlety the exam leans on: the loss an insurer faces over a period is really two random things stacked together.

- **Frequency** $N$ — *how many* claims occur (a count: $0, 1, 2, \dots$, often Poisson, ch05). How many Pokémon escaped and wrecked something this month?
- **Severity** $X$ — *how large* each individual claim is (the loss random variable above). When one *does* wreck gear, how much?

The **aggregate loss** is the total over a period — sum the severities of all the claims that happened:

$$S_{\text{agg}} \;=\; X_1 + X_2 + \dots + X_N \qquad (\text{the random number } N \text{ of claims, each a severity } X_i).$$

When you read "a Pokémon flees and wrecks $X$ of gear," that is *one severity draw* — the ch06/ch13 object. The full aggregate (random *count* of claims, each a random *size*) is the seed of the later actuarial exams (§6). For Exam P, the load-bearing object is the **single severity $X$** and the payment carved out of it — but knowing that $X$ is the *severity* leg of a frequency-severity pair tells you exactly where these problems sit in the larger picture.

---

## 3. Policy Provisions That Modify the Payment

A policy is a contract that reshapes the ground-up loss $X$ into a **payment** $Y$. There are four levers, and the whole of ch06/ch13 is learning what each does to the math. We define each precisely, then state the identity that ties them together.

Throughout, the **per-loss payment** is written $Y_L$ — the amount the insurer pays, recorded for *every* loss including the ones that pay zero. (The per-*payment* view, $Y_P$, is §5.)

### Ordinary deductible $d$ — knock off the bottom

The insured absorbs the first $d$ of any loss themselves; the insurer pays only the **excess** above $d$. Crucially, the payment is **floored at zero** — a loss smaller than $d$ pays nothing, never a negative amount:

$$Y_L \;=\; \dplus{X}{d} \;=\; \max(X-d,\,0).$$

The Agency pays $X-d$ when the loss clears the deductible and $0$ when it doesn't. The floor at zero is *the* recurring trap of both chapters: the expected payment is **not** $\E[X]-d$ (that would let small losses pay negative amounts), but rather

$$\E\!\left[\dplus{X}{d}\right] \;=\; \sum_{k\ge d} S(k) \quad(\text{discrete}) \qquad\text{or}\qquad \int_d^{\infty} S(x)\,dx \quad(\text{continuous}).$$

The deductible exists to make insurance affordable: it removes the flood of tiny claims (cheap to occur, expensive to administer) and lowers the premium, because the insurer now pays less on average. It also keeps the insured invested in avoiding losses — they have skin in the game up to $d$.

### Policy limit / maximum covered loss $u$ — cap the top

The insurer will not record more than $u$ on a single loss; everything above the ceiling is the insured's problem. The capped loss is the **limited loss**, written with the wedge:

$$X \wedge u \;=\; \min(X,\,u).$$

Its expectation, the **limited expected value** $\E[X \wedge u]$, is the area (or sum) of survival *up to* the cap:

$$\E[X \wedge u] \;=\; \sum_{k=0}^{u-1} S(k) \quad(\text{discrete}) \qquad\text{or}\qquad \int_0^{u} S(x)\,dx \quad(\text{continuous}).$$

The limit caps the insurer's exposure to a catastrophic single event — a freak volcanic eruption, a once-a-decade rampage — so the Agency can hold less capital against ruin.

### Coinsurance $\alpha$ — split what's left

After the deductible and limit, the insurer pays only a **fraction** $\alpha$ of the remaining covered amount; the insured keeps the complementary $1-\alpha$. The classic "80/20" health plan is $\alpha = 0.8$. Coinsurance multiplies the covered layer:

$$Y_L \;=\; \alpha \times (\text{covered amount}).$$

It exists to keep the insured price-conscious even *after* the deductible is met — they still bear a slice of every additional Poké-dollar, so they don't over-claim.

### Inflation $(1+r)$ — apply it *before* the deductible

When losses inflate by a factor $1+r$ between policy periods, the **loss** grows but the **deductible is a fixed dollar amount written into the contract — it does not inflate.** So inflation is applied to $X$ *first*, then the (unchanged) deductible bites:

$$X \longmapsto (1+r)X, \qquad\text{then}\qquad Y_L = \big((1+r)X - d\big)_+.$$

This ordering produces **deductible erosion**: because the fixed $d$ is now a *smaller* fraction of the (larger) loss, it removes proportionally less, and the **payment rises faster than the loss**. A $25\%$ loss-inflation with a fixed deductible can push the expected payment up by *more* than $25\%$ — the effect ch13 quantifies, and a favorite exam twist.

### Combined — layering, and the budget identity

A full policy stacks all four, in a **fixed order** — *inflation → deductible → limit → coinsurance* — and the payment becomes the **covered layer** between $d$ and $u$, scaled by $\alpha$:

$$Y_L \;=\; \alpha\big[(X \wedge u) - (X \wedge d)\big], \qquad \E[Y_L] \;=\; \alpha\big(\E[X \wedge u] - \E[X \wedge d]\big).$$

Read $(X \wedge u)-(X \wedge d)$ as "the part of the loss that lives *between* the deductible and the limit" — the slice the policy is responsible for. Below $d$ the insured pays; above $u$ the insured pays; the insurer owns the middle band, times $\alpha$.

Holding the whole thing together is the identity both chapters call the **budget identity** (ch06) / **master identity** (ch13) — what the limit keeps, plus what it cuts, reassembles the whole loss:

$$\boxed{\;\E[X \wedge u] \;+\; \E\!\left[\dplus{X}{u}\right] \;=\; \E[X].\;}$$

Hand it any two of $\{\E[X],\,\E[X \wedge u],\,\E[(X-u)_+]\}$ and it returns the third with no further computation. It is the line a pricing actuary uses to split a loss into the insured's **retained layer** ($\E[X \wedge u]$, the bottom) and the insurer's or reinsurer's **excess layer** ($\E[(X-u)_+]$, the top) in one stroke.

::: trainers-tip
**THE FOUR LEVERS, ON ONE CARD**

| Lever | Symbol | What it does | Why it exists |
|---|---|---|---|
| Deductible | $\dplus{X}{d}$ | insured eats first $d$; pay the excess, floored at $0$ | kills tiny claims, lowers premium, skin in the game |
| Limit | $X \wedge u$ | cap recorded loss at $u$ | caps catastrophe exposure / capital |
| Coinsurance | $\alpha$ | pay fraction $\alpha$ of the covered layer | keeps insured price-conscious |
| Inflation | $(1+r)X$ | grow the loss; **deductible stays fixed** | causes deductible erosion (payment outpaces loss) |

**Order:** inflation → deductible → limit → coinsurance. **Tie:** $\E[X \wedge u]+\E[(X-u)_+]=\E[X]$.
:::

---

## 4. Per-Loss vs Per-Payment

This is the distinction that trips more readers than any single formula, and the one Exam P checks relentlessly. The same policy answers *two different questions*, and they have *two different numbers*.

**Per-loss** ($Y_L$) averages the payment over **every loss event** — including the many that pay exactly zero because they never cleared the deductible. This is what the **insurer** needs: the premium must cover the average payout *per policy sold*, and most policies sit quiet, contributing a zero to the average. The pure premium of §1 is a per-loss expectation.

**Per-payment** ($Y_P$) averages only over the losses that **actually generate a cheque** — it conditions on a payment occurring. This is what the **claimant** experiences: "when the Agency actually pays me, how big is the cheque?" The zeros are thrown out, so the remaining average is larger.

A payment happens exactly when the loss **strictly exceeds the deductible**, with probability $S(d)=P(X>d)$. Conditioning on that event means dividing the per-loss expectation by the chance it occurred:

$$\boxed{\;\E[Y_P] \;=\; \frac{\E[Y_L]}{S(d)}, \qquad S(d)=P(X>d).\;}$$

The divisor is **always** the deductible's survival $S(d)$ — never $F(d)$ (the chance the loss *fails* to clear $d$), and never the limit's $S(u)$. The limit changes a payment's *size*; only the deductible decides *whether* a payment happens at all.

**Why $\E[Y_P] > \E[Y_L]$ — always.** Same total expected dollars, but per-payment spreads them over a *smaller* set (only the payers, not everyone). Smaller denominator, same numerator, bigger quotient. A quick sanity check you can run on any answer: **a per-payment average must exceed its per-loss average.** If yours comes out smaller, you divided by the wrong probability.

::: trainers-tip
**WHICH AVERAGE DOES THE PROBLEM WANT?** — Read the conditioning words. *"per loss / per policy / expected cost / pure premium"* → **per loss** ($Y_L$, keep the zeros). *"per payment / average payment made / given a payment is made / the typical cheque"* → **per payment** ($Y_P$): divide by $S(d)=P(X>d)$. The denominator is the **deductible's** survival, never the limit's.
:::

---

## 5. Loss Elimination Ratio and the Limited Loss

Two named quantities round out the toolkit; both are just the budget identity wearing different clothes.

**The limited expected value $\E[X \wedge d]$.** Cap the loss at $d$ and average. From §3, this is the expected amount of loss the insured **retains** under a deductible $d$ — the bottom slice the insurer never pays. It is the survival summed (or integrated) up to $d$, and by the budget identity it is precisely the part of $\E[X]$ that the deductible *removes* from the insurer's bill:

$$\E[X] \;=\; \underbrace{\E[X \wedge d]}_{\text{eliminated by the deductible}} \;+\; \underbrace{\E\!\left[\dplus{X}{d}\right]}_{\text{paid by the insurer}}.$$

**The Loss Elimination Ratio (LER).** A deductible's job is to *eliminate* some of the expected loss from the insurer's responsibility. The LER measures **what fraction** it eliminates:

$$\mathrm{LER}(d) \;=\; \frac{\E[X \wedge d]}{\E[X]} \;=\; \frac{\E[X] - \E\!\left[\dplus{X}{d}\right]}{\E[X]} \;=\; 1 - \frac{\E\!\left[\dplus{X}{d}\right]}{\E[X]}.$$

In words: *of every expected Poké-dollar of ground-up loss, the deductible removes $\mathrm{LER}(d)$ of it from the insurer's expected payout.* A deductible of $d=0$ eliminates nothing, $\mathrm{LER}(0)=0$; a deductible above the largest possible loss eliminates everything, $\mathrm{LER} \to 1$. The LER is exactly how much a deductible **lowers the pure premium**, expressed as a fraction — which is why it sits at the heart of pricing a deductible (§6). The three names — limited expected value, eliminated loss, retained layer — are the *same number* $\E[X \wedge d]$ seen from the insured's, the underwriter's, and the reinsurer's chairs.

---

## 6. Why an Actuary Computes All This

Step back from the algebra. Every formula in ch06 and ch13 is a tool in two daily jobs of an insurance actuary.

**Pricing (ratemaking).** Before a policy is sold, someone must decide its price. That price starts from the **pure premium** $\E[Y_L]$ — the expected payout per policy — computed *exactly* the way ch06/ch13 compute it, then wrapped in the load of §1. Change the deductible, the limit, or the coinsurance, and $\E[Y_L]$ changes, and so does the quoted price. The reason **a higher deductible lowers the premium** is now fully visible: a larger $d$ raises $\E[X \wedge d]$, so by the budget identity it lowers $\E[(X-d)_+]=\E[Y_L]$ — the insurer pays less on average — and the LER of §5 measures precisely how much. This is not a marketing claim; it is the budget identity read aloud.

**Reserving.** After policies are sold, the insurer must hold money — **reserves** — against claims that will come due. The expected aggregate payout, built from these same per-loss expectations summed over the book, is the backbone of how much to set aside. Get $\E[Y_L]$ wrong and you under- or over-reserve; either way the company is mispriced and at risk.

**Why the layers matter.** The retained/excess split (§3) is how primary insurers and **reinsurers** share a risk: the primary insurer keeps $\E[X \wedge u]$, the reinsurer takes the dangerous tail $\E[(X-u)_+]$, and the budget identity guarantees the two pieces add back to the whole. Every line of that arithmetic is something you can already do.

::: kanto-realworld
**⬛ THE SERIES BRIDGE — where this grows up**

What ch06, ch13, and this appendix teach is the *seed* of an entire later actuarial exam. On Exam P you price a **single severity** $X$ reshaped by a deductible, a limit, and coinsurance. The next exam in the series — **Short-Term Actuarial Mathematics (STAM / FAM-Short / CAS Exam 5)** — takes exactly these objects and scales them up:

- the **full menu of severity distributions** (lognormal, Pareto, Weibull, and the heavy tails real losses follow);
- the **frequency-severity** pair of §2 combined into the genuine **aggregate loss** model $S_{\text{agg}}=X_1+\dots+X_N$;
- the **full reinsurance and layering** structures the budget identity only hints at here;
- **credibility and ratemaking** — turning data into prices, with the pure-premium-plus-load logic of §1 made rigorous.

Every limited-expected-value, deductible, and coinsurance computation you master here is *literally the same machinery* you will deploy there, just with more distributions and a random claim count layered on top. When ch06 and ch13 feel like bookkeeping, remember: you are laying the foundation of how the entire short-term insurance world is priced. Master the Warden's gate fee, and you have started down the road to pricing real cover.
:::

---

> **In one breath:** insurance pools independent risks so the average payout is predictable (ch12's CLT); that average payout — the pure premium $\E[Y_L]$ — is what ch06 and ch13 compute. A policy reshapes the ground-up loss $X$ with four levers (deductible $\dplus{X}{d}$, limit $X \wedge u$, coinsurance $\alpha$, inflation $(1+r)X$), tied together by $\E[X \wedge u]+\E[(X-u)_+]=\E[X]$. Read the conditioning words to choose per-loss ($Y_L$) or per-payment ($Y_P=Y_L/S(d)$). The deductible's LER is how much it lowers the price. That is the whole insurance world the exam assumes — and the doorway to the actuarial exams beyond P.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
