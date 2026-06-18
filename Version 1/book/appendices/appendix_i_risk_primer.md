<!--
  appendix: i_risk_primer
  status: done
-->

# Appendix I — "Risk and Insurance" Study-Note Primer {.type-normal}

The SOA assumes every Exam P candidate has read its short **"Risk and Insurance"** study note before reaching the insurance-application outcomes (Topic 2(e)–(f)). That note is not mathematics — it is the *vocabulary and the picture* of how insurance works, so that when Chapter 10 (*Pricing the Risk*) turns a loss into a payment, you already know what a deductible, a limit, and coinsurance *are* in the real world. This appendix is that background, told in Kanto terms and kept strictly to what Chapter 10 needs. Read it before Chapter 10; nothing here is itself a graded computation, but every term here is load-bearing for the graded computations there.

::: cold-open
**▶ COLD OPEN — EPISODE: "Why the Warden Needs a Word for Everything"**

Before the Safari Zone warden can ask you for a number, he and Brock keep reaching for words — *deductible, limit, eighty percent* — as if everyone already knows them. They are the everyday machinery of insurance, and an actuary who does not own these words cannot price anything. This page hands you the words, in order, so that when Chapter 10 asks "on average, how much does the Zone pay?", every term in the question is already familiar.
:::

## I.1 — The one idea: insurance is pooling and transfer

::: pokedex-entry
**POKÉDEX ENTRY — What insurance *is***

An **insurer** collects a small, certain payment (the **premium**) from many people facing the same kind of uncertain, occasional large loss, and promises to pay (a **claim**) to whoever the loss actually strikes. Risk is **transferred** from each individual to the pool, and **pooled** across many so that the insurer's *total* payout is far more predictable than any one person's loss.

*Recognition cue:* whenever a problem says "a policy," "a premium," "covers losses," or "the insurer pays" — you are in this world, and the quantity you compute is almost always an **expected payment**.
:::

The **policyholder** (the trainer) trades an uncertain loss for a certain premium. The **insurer** (the Safari Zone) takes on many such uncertain losses at once. The reason this works at all is the very pooling effect Chapter 14 proves with the Central Limit Theorem: average a lot of independent losses and the average becomes stable and predictable, even though each one is not.

## I.2 — Loss versus payment: two different random variables

This is the single most important distinction in Chapter 10, and the place candidates most often go wrong.

::: pokedex-entry
**POKÉDEX ENTRY — Loss $X$ is not payment $Y$**

The **loss** $X$ is what actually goes wrong — the full Poké-dollar value of the gear a fleeing Pokémon takes. The **payment** $Y$ is what the *insurer* hands over after the policy's terms (deductible, limit, coinsurance) are applied to that loss. They are **two different random variables**, and a policy is precisely a *rule that turns $X$ into $Y$*.

$$X \;=\; \text{the loss that occurred}, \qquad Y \;=\; \text{what the insurer pays on it}, \qquad Y = g(X).$$

*Recognition cue:* read the question's verb. "Expected **loss**" wants $\E[X]$. "Expected **payment**," "expected **claim**," "what the insurer **pays**" wants $\E[Y]$ — and $Y$ has been reshaped by the policy terms.
:::

## I.3 — The four policy modifications (the vocabulary you must own)

These are the terms the warden, Brock, and Misty throw around in Chapter 10's cold open. Each one *modifies* how the loss $X$ becomes the payment $Y$.

::: pokedex-entry
**POKÉDEX ENTRY — Deductible $d$**

The policyholder pays the **first $d$ of every loss** out of pocket; the insurer pays only the excess. A loss smaller than $d$ produces **no payment at all**.

$$\text{insurer pays } \;=\; \dplus{X}{d} \;=\; \max(X-d,\,0).$$

*In plain terms:* the deductible is the trainer "eating the first few thousand themselves." It filters out small, frequent, nuisance claims so the insurer only pays for losses that actually hurt.

*Recognition cue:* "the policyholder pays the first \$$d$," "after a deductible of $d$" — reach for $\dplus{X}{d}$.
:::

::: pokedex-entry
**POKÉDEX ENTRY — Policy limit / maximum covered loss**

The insurer caps what it will pay. A **policy limit** is the most the insurer will *ever pay on one loss*; a **maximum covered loss** $u$ is the loss value beyond which extra loss earns no extra payment. With no deductible, a maximum covered loss $u$ makes the payment the **limited loss**

$$\limexp{X}{u} \;=\; \min(X,\,u),$$

read aloud "the loss, but capped at $u$."

*In plain terms:* the cap is the warden refusing to "pay back everything." It bounds the insurer's worst case on any single claim.

*Recognition cue:* "the insurer pays at most," "policy limit," "capped at" — reach for $\min(X,u)$, i.e. $\limexp{X}{u}$.
:::

::: pokedex-entry
**POKÉDEX ENTRY — Coinsurance factor $\alpha$**

After the deductible and limit have shaped the loss, the insurer pays only a **fraction $\alpha$** of what remains (e.g. $\alpha=0.8$, "eighty cents on the dollar"); the policyholder absorbs the rest. Coinsurance simply scales the post-deductible, post-limit amount by $\alpha$.

*In plain terms:* the "eighty percent" Misty suggests, so trainers stay careful with their gear because they always share in the loss.

*Recognition cue:* "the insurer pays $\alpha$ of," "coinsurance of $\alpha$," a stated percentage of the covered amount.
:::

::: trainers-tip
**THE FULL POLICY, IN ORDER**

When a policy stacks all three, the operations apply in a fixed order — **deductible first, then the limit/cap, then the coinsurance scaling** — turning the loss $X$ into the payment $Y$. Chapter 10 builds the exact formula and derives its expectation with the survival-function (Darth Vader) method; this primer only fixes *what each piece means*. Get the order wrong and you compute a different policy than the one in the question.
:::

## I.4 — Per-loss versus per-payment (the averaging base)

A second distinction the SOA note assumes, and Chapter 10 makes precise.

::: pokedex-entry
**POKÉDEX ENTRY — Two ways to average a payment**

- **Per loss (per-loss basis):** average the payment over **every loss that occurs**, *including the ones below the deductible that pay nothing*. The zeros are in the average. This is $\E[Y]$ where $Y=0$ on small losses.
- **Per payment (per-payment basis):** average the payment over **only the losses large enough to trigger a payment** — you condition on a payment having happened, $X > d$. The zeros are excluded, so the per-payment average is **larger**, obtained by dividing the per-loss expected payment by the survival probability $S(d)=P(X>d)$.

*Recognition cue:* "average over all losses" / "per loss" → keep the zeros. "given that a payment is made" / "per payment" / "for losses exceeding the deductible" → condition on $X>d$ and divide by $S(d)$.
:::

## I.5 — Frequency and severity (why losses have two random pieces)

::: pokedex-entry
**POKÉDEX ENTRY — Frequency × Severity**

A pool's total claim cost has two random ingredients:

- **Frequency** — *how many* losses occur (a count; Chapter 8's Poisson and binomial live here).
- **Severity** — *how large* each loss is (an amount; Chapter 9's continuous distributions and Chapter 10's modified payment live here).

The **pure premium** — the average cost per policy before expenses and margin — is, in words, *expected frequency times expected severity*. Exam P tests the two pieces separately (a count distribution, or a single severity's expected payment); putting them together is the work of later exams, but the *vocabulary* belongs here.

*Recognition cue:* "number of claims" → frequency (a count RV). "size of a claim" / "amount of a loss" → severity (an amount RV).
:::

## I.6 — Why the modifications exist (moral hazard & adverse selection, in one breath)

You do not compute these on Exam P, but the SOA note names them and they explain *why* deductibles and coinsurance exist at all:

- **Moral hazard** — being insured can make a policyholder *less careful* (a trainer who'll be fully reimbursed takes reckless risks in the Safari Zone). Deductibles and coinsurance keep the policyholder sharing the loss, so they stay careful.
- **Adverse selection** — the people most eager to buy coverage tend to be the *highest-risk* ones, which can push the pool's average loss up. Pricing and policy design exist partly to counter this.

::: kanto-realworld
**FROM KANTO TO THE REAL WORLD**

Every term on this page is on your own insurance documents. Your auto and health policies have a **deductible** (you pay the first slice), often a **coinsurance** share or copay (you pay a percentage), and frequently an out-of-pocket **maximum** or coverage **limit** (the cap). An actuary pricing those policies computes exactly the **expected payment per loss** the Safari Zone warden asks you for in Chapter 10 — the loss distribution run through the deductible, limit, and coinsurance, then averaged. The Kanto story is the real job with the serial numbers filed off.
:::

::: trainers-tip
**WHAT TO CARRY INTO CHAPTER 10**

You are ready for *Pricing the Risk* once you can, unaided, (1) say why the **payment $Y$ differs from the loss $X$**; (2) state in words what a **deductible**, a **limit/maximum covered loss**, and a **coinsurance factor** each do, and the order they apply; (3) explain the difference between a **per-loss** and a **per-payment** average; and (4) name **frequency** vs **severity**. Chapter 10 supplies all the mathematics — $\dplus{X}{d}$, $\limexp{X}{u}$, the survival-function method, and the variance of the payment — on top of this vocabulary.
:::
