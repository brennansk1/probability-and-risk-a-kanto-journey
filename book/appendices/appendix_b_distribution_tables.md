<!--
  file: appendix_b_distribution_tables
  kind: appendix
  letter: B
  title: The Distribution Pokédex (Field Guide)
  purpose: one full collectible profile per in-scope distribution; every stat block matches the chapters' Pokédex Entries and Appendix A exactly
  sources: ch03, ch04, ch05, ch11, ch12
  plan: MASTER_PLAN_V3 §17 (locked roster + Gen-1 mascots + stat blocks), §23 (appendix spec)
-->

# Appendix B — The Distribution Pokédex (Field Guide) {.type-water}

> **What this is.** The book's full **distribution roster** in one place — a collectible Field Guide, one profile per in-scope distribution, in the order an exam-day brain meets them: the discrete families first, then the continuous. Each profile is a compact "dex entry": the behavior-matched **Gen-1 mascot** (§17), a one-line **category** flavor, the **stat block** (support · pmf/pdf · cdf where clean · mean · variance · MGF where standard), the **recognition cue** ("when you see ___, reach for this"), and a **fidelity note** (why the mascot behaves the way the math behaves). Every formula here matches its chapter's **Pokédex Entry** and the Appendix A formula sheet exactly. Notation follows the book: $\E[\cdot]$ expectation, $\Var(\cdot)$ variance, $S(\cdot)$ survival, $q=1-p$ throughout. *(Generated Pokédex-scan figures are added in a later chrome pass; this Field Guide reads complete as text.)*

---

## Part I — The Discrete Roster *(Act I — the Countable Road)*

---

### Bernoulli$(p)$ — Voltorb {.type-electric}

*The One-Shock Pokémon.* A single trial: it either goes off ($1$) or it doesn't ($0$).

**Stat block.**
$$\text{Support: } \{0,1\}\qquad p(x)=p^{x}q^{1-x}\quad(x\in\{0,1\}).$$
$$\E[X]=p,\qquad \Var(X)=pq,\qquad M_X(t)=q+pe^{t}.$$

**Recognition cue.** A single yes/no, success/fail, on/off trial with success probability $p$ → Bernoulli. *(With $n=1$ it **is** the binomial; everything counted in the binomial is a sum of $n$ independent Bernoullis.)*

**Fidelity.** A Voltorb is one charge waiting to discharge: poke it and it either explodes or it doesn't — a single $0/1$ outcome with a fixed go-off probability $p$. No counting, no waiting; just one shock. *(ch04)*

---

### Binomial$(n,p)$ — Pidgey flock {.type-flying}

*The Flock-Count Pokémon.* Count the successes in a flock of $n$ independent, identical trials.

**Stat block.**
$$\text{Support: } 0,1,\dots,n\qquad p(k)=\binom{n}{k}p^{k}q^{\,n-k}.$$
$$\E[X]=np,\qquad \Var(X)=npq,\qquad M_X(t)=\big(q+pe^{t}\big)^{n}.$$

**Recognition cue.** A **fixed** number $n$ of **independent** trials, each with the **same** success probability $p$, and you want "how many succeeded?" → binomial. Keywords: "out of $n$," "exactly $k$ of them," "at least one of $n$."

**Fidelity.** A flock of $n$ Pidgey each independently does-or-doesn't (take off, peck, flee) with the same probability $p$; the number that act is a sum of $n$ Bernoullis — exactly the binomial. *(ch04)*

---

### Hypergeometric$(N,K,n)$ — Magikarp pond {.type-water}

*The Draw-Without-Replacement Pokémon.* Scoop $n$ from a pond of $N$ (of which $K$ are "good"); count the good ones caught.

**Stat block.**
$$\text{Support: } \max(0,\,n-N+K)\le k\le \min(n,K)\qquad p(k)=\dfrac{\binom{K}{k}\binom{N-K}{\,n-k}}{\binom{N}{n}}.$$
$$\E[X]=n\frac{K}{N},\qquad \Var(X)=n\frac{K}{N}\cdot\frac{N-K}{N}\cdot\frac{N-n}{N-1}.$$
*(No standard closed-form MGF; the trailing factor $\tfrac{N-n}{N-1}$ is the **finite-population correction**.)*

**Recognition cue.** Drawing a sample **without replacement** from a finite pool of fixed composition → hypergeometric. Keywords: "without replacement," "from a group of $N$ of which $K$ are…," "selected at once." *(Replacement would make it binomial.)*

**Fidelity.** A Magikarp pond has a **fixed stock**: every Magikarp you net is one fewer left, so each draw changes the odds for the next — sampling without replacement. That depletion is the whole difference from the Pidgey flock. *(ch04)*

---

### Geometric$(p)$ — Meowth {.type-normal}

*The Keep-Trying Pokémon.* Trials repeat until the first success; count how long that takes.

**Stat block (trials form — trial of the first success).**
$$\text{Support: } 1,2,3,\dots\qquad p(k)=q^{\,k-1}p\qquad S(k)=P(X>k)=q^{k}.$$
$$\E[X]=\frac1p,\qquad \Var(X)=\frac{q}{p^{2}},\qquad M_X(t)=\frac{pe^{t}}{1-qe^{t}}.$$

**Stat block (failures form — failures before the first success).**
$$\text{Support: } 0,1,2,\dots\qquad p(k)=q^{k}p\qquad \E[X]=\frac{q}{p},\qquad \Var(X)=\frac{q}{p^{2}},\qquad M_X(t)=\frac{p}{1-qe^{t}}.$$

**Recognition cue.** "Number of trials until the first success," "keep trying until it works" → geometric. The signature is **memorylessness**: $P(X>m+n\mid X>m)=P(X>n)$ — past failures don't change the future. *(Read the problem to fix which form: counting the trials, or counting the failures.)*

**Fidelity.** Meowth keeps trying the same scheme until it finally lands — and each fresh attempt has the same success probability $p$ regardless of how many times he's already flopped. The coin has no memory of past failures; neither does Meowth. *(ch05)*

---

### Negative binomial$(r,p)$ — Dugtrio {.type-ground}

*The Wait-for-the-$r$-th Pokémon.* Keep going until the $r$-th success; count the failures along the way.

**Stat block (failures before the $r$-th success).**
$$\text{Support: } 0,1,2,\dots\qquad p(k)=\binom{k+r-1}{k}p^{r}q^{k}.$$
$$\E[X]=\frac{rq}{p},\qquad \Var(X)=\frac{rq}{p^{2}},\qquad M_X(t)=\left(\frac{p}{1-qe^{t}}\right)^{\!r}.$$

**Recognition cue.** "Number of trials/failures until the **$r$-th** success" → negative binomial. With $r=1$ it collapses to the geometric; a sum of $r$ independent geometrics **is** a negative binomial.

**Fidelity.** Dugtrio is three Diglett fused — you wait not for one success but for the **third** to surface. The negative binomial stacks $r$ independent geometric waits into a single "wait for $r$" Pokémon. *(ch05)*

---

### Poisson$(\lambda)$ — Gastly swarm {.type-ghost}

*The Swarm-Count Pokémon.* A random count of events appearing in a fixed window.

**Stat block.**
$$\text{Support: } 0,1,2,\dots\qquad p(k)=\frac{e^{-\lambda}\lambda^{k}}{k!}.$$
$$\E[X]=\lambda,\qquad \Var(X)=\lambda,\qquad M_X(t)=e^{\lambda(e^{t}-1)}.$$
*Mean equals variance — the Poisson signature.* **Superposition:** independent $X_i\sim\Poisson(\lambda_i)\Rightarrow\sum_i X_i\sim\Poisson\!\big(\sum_i\lambda_i\big)$.

**Recognition cue.** A **count** of rare events over a fixed window of time/space/exposure — "how many per hour/page/region" — with no fixed upper bound → Poisson. If a count's mean and variance match, suspect Poisson. Large-$n$, small-$p$ binomial $\approx\Poisson(np)$.

**Fidelity.** In the Pokémon Tower, **Gastly** materialize out of the dark in unpredictable numbers over any given stretch — you can't bound how many, only their average rate $\lambda$ per window. A swarm whose count per window is governed by a single rate is exactly Poisson. *(ch05)*

---

### Discrete uniform$\{1,\dots,n\}$ — Ditto {.type-normal}

*The Any-Form Pokémon.* $n$ values, each equally likely.

**Stat block.**
$$\text{Support: } 1,2,\dots,n\qquad p(k)=\frac1n.$$
$$\E[X]=\frac{n+1}{2},\qquad \Var(X)=\frac{n^{2}-1}{12},\qquad M_X(t)=\frac1n\sum_{k=1}^{n}e^{tk}.$$
*For a uniform on $\{a,\dots,b\}$ with $m=b-a+1$ values: mean $\tfrac{a+b}{2}$, variance $\tfrac{m^{2}-1}{12}$.*

**Recognition cue.** A finite list of outcomes, **all equally likely**, no value preferred → discrete uniform. Keywords: "equally likely," "chosen at random from $\{1,\dots,n\}$," "a fair $n$-sided die."

**Fidelity.** **Ditto** can become any Pokémon, and no form is favored — every option carries the same weight. Equal probability across $n$ forms is the discrete uniform. *(ch03)*

---

## Part II — The Continuous Roster *(Act II — the Smooth World)*

---

### Continuous uniform$(a,b)$ — Porygon {.type-normal}

*The Flat-Band Pokémon.* Equally likely anywhere on an interval; probability is length.

**Stat block.**
$$\text{Support: } [a,b]\qquad f(x)=\frac{1}{b-a}\qquad F(x)=\frac{x-a}{b-a}\ \ (a\le x\le b).$$
$$\E[X]=\frac{a+b}{2},\qquad \Var(X)=\frac{(b-a)^{2}}{12},\qquad M_X(t)=\frac{e^{tb}-e^{ta}}{t(b-a)}\ (t\ne0).$$

**Recognition cue.** "Equally likely anywhere between $a$ and $b$," "chosen at random from the interval," "no point preferred" → continuous uniform. Then $P(c<X<d)=\dfrac{d-c}{b-a}$ — a ratio of lengths. Mean is the midpoint; remember the $/12$.

**Fidelity.** A glitching **Porygon** spawns *somewhere* along the corridor with no tile preferred — every point as likely as the next, and the chance of any single exact point is zero. A flat, digital, position-anywhere spawn is the continuous uniform. *(ch11)*

---

### Exponential$(\theta)$ — Electrode {.type-electric}

*The Memoryless-Timer Pokémon.* A continuous waiting time with a constant failure rate.

**Stat block.**
$$\text{Support: } [0,\infty)\qquad f(x)=\frac1\theta e^{-x/\theta}\qquad S(x)=e^{-x/\theta},\quad F(x)=1-e^{-x/\theta}.$$
$$\E[X]=\theta,\qquad \Var(X)=\theta^{2},\qquad M_X(t)=\frac{1}{1-\theta t}\ \ \left(t<\tfrac1\theta\right).$$
**Memorylessness:** $P(X>s+t\mid X>s)=P(X>t)=e^{-t/\theta}.$

**Recognition cue.** "Time until," "time between," "lifetime," "memoryless," "constant failure rate" → exponential. The instant you read "given it has already lasted $s$," reset the clock — the remaining wait is a fresh $\Expo(\theta)$. *(The continuous twin of the geometric.)*

**Fidelity.** An **Electrode**'s self-destruct countdown is random, and watching it tick down tells you nothing about how much longer it'll take — the remaining wait looks like a brand-new timer. That forgetfulness is exactly the exponential's memoryless property. *(ch11)*

---

### Gamma$(\alpha,\theta)$ — Magneton {.type-electric}

*The Stacked-Wait Pokémon.* A sum of $\alpha$ independent exponential waits — the time until the $\alpha$-th event.

**Stat block.**
$$\text{Support: } (0,\infty)\qquad f(x)=\frac{x^{\alpha-1}e^{-x/\theta}}{\Gamma(\alpha)\,\theta^{\alpha}}.$$
$$\E[X]=\alpha\theta,\qquad \Var(X)=\alpha\theta^{2},\qquad M_X(t)=(1-\theta t)^{-\alpha}\ \ \left(t<\tfrac1\theta\right).$$
*With $\alpha=1$ it is the exponential. **Additive in shape** at a common scale: $\GammaDist(\alpha_1,\theta)+\GammaDist(\alpha_2,\theta)=\GammaDist(\alpha_1+\alpha_2,\theta)$.*

**Recognition cue.** "Time until the $k$-th event," "sum of $k$ exponential waits," or a density $\propto x^{\alpha-1}e^{-x/\theta}$ → gamma. The gamma integral handles any $\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx=\Gamma(\alpha)\theta^{\alpha}$ in one line.

**Fidelity.** A **Magneton** is three Magnemite fused into one body — a sum of identical units. Stacking $\alpha$ independent exponential (Electrode) waits end-to-end gives the gamma: the time to accumulate $\alpha$ events. *(ch11)*

---

### Beta$(\alpha,\beta)$ — Chansey {.type-normal}

*The Random-Proportion Pokémon.* A fraction trapped on $[0,1]$, its shape set by two counts.

**Stat block.**
$$\text{Support: } [0,1]\qquad f(x)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}\,x^{\alpha-1}(1-x)^{\beta-1}.$$
$$\E[X]=\frac{\alpha}{\alpha+\beta},\qquad \Var(X)=\frac{\alpha\beta}{(\alpha+\beta)^{2}(\alpha+\beta+1)}.$$
*(No standard closed-form MGF examined on Exam P. $\BetaDist(1,1)$ is the continuous uniform on $[0,1]$.)*

**Recognition cue.** "A fraction/proportion/percentage between $0$ and $1$," "a random share," or a density $\propto x^{\alpha-1}(1-x)^{\beta-1}$ on $(0,1)$ → beta. The mean is the weight ratio $\alpha/(\alpha+\beta)$: more $\alpha$ pulls mass toward $1$, more $\beta$ toward $0$.

**Fidelity.** **Chansey**'s gift is a matter of luck — a proportion that lands somewhere between none and all, never outside $[0,1]$. Two shape parameters bend that bounded fraction toward either end. A random share confined to the unit interval is the beta. *(ch11)*

---

### Normal$(\mu,\sigma^{2})$ — Clefairy {.type-fairy}

*The Bell-Curve Pokémon.* The symmetric bell that pooled i.i.d. sums and averages converge to.

**Stat block.**
$$\text{Support: } (-\infty,\infty)\qquad f(x)=\frac{1}{\sigma\sqrt{2\pi}}\,e^{-(x-\mu)^{2}/(2\sigma^{2})}.$$
$$\E[X]=\mu,\qquad \Var(X)=\sigma^{2},\qquad M_X(t)=e^{\mu t+\frac12\sigma^{2}t^{2}}.$$
**Standardize:** $Z=\dfrac{X-\mu}{\sigma}\sim\Normal(0,1)$, so $P(X\le x)=\Phi\!\big(\tfrac{x-\mu}{\sigma}\big)$ with $\Phi(-z)=1-\Phi(z)$. **CLT:** $S_n=\sum X_i\overset{\text{approx}}{\sim}\Normal(n\mu,n\sigma^{2})$ and $\bar X\overset{\text{approx}}{\sim}\Normal(\mu,\sigma^{2}/n)$. Sums of independent normals are normal: $\Normal(\mu_1,\sigma_1^2)+\Normal(\mu_2,\sigma_2^2)=\Normal(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2)$.

**Recognition cue.** "Bell-shaped," "approximately normal," a sum/average of **many** i.i.d. pieces, or anything paired with the $\Phi(z)$ table → normal. On a discrete sum approximated by a normal, apply the **continuity correction** ($\pm0.5$) *before* standardizing.

**Fidelity.** The **Clefairy** of Mt. Moon gather under the moonstone in a bell — most clustered at the center, fewer at each fringe, symmetric about the peak. Pool enough independent results and they always settle into that same bell, whatever the parts looked like: the Central Limit Theorem. *(ch12)*

---

::: enrichment
**🔬 OFF-SYLLABUS ENRICHMENT — flagged, never gated.** The pair below is taught because TIA covers it and because it bridges to later exams and the job. **Neither is examined on Exam P** — read them for the bridge, not the test. They are not on the mastery checklist and carry no problem-bank minimum.

---

### Pareto — Snorlax *(heavy tail)*

*The Heavy-Tail Pokémon.* Usually nothing; rarely, something immense.

**Stat block.** With minimum scale $x_m$ and tail index $\alpha>0$, for $x\ge x_m$:
$$S(x)=\left(\frac{x_m}{x}\right)^{\!\alpha},\qquad f(x)=\frac{\alpha\,x_m^{\alpha}}{x^{\alpha+1}},\qquad \E[X]=\frac{\alpha\,x_m}{\alpha-1}\ \ (\alpha>1,\ \text{undefined for }\alpha\le1).$$
The tail decays as a **power** of $x$, not an exponential, so it stays high far out — and the mean is finite only when $\alpha>1$ (the variance only when $\alpha>2$).

**Recognition cue.** Loss data where most claims are modest but a rare few are catastrophic — "heavy tail," "large-loss/catastrophe," "the mean might not even exist" → Pareto.

**Fidelity.** A **Snorlax** does nothing almost all the time, but when it stirs it is *immense and immovable*. That is the heavy tail: a freak loss an exponential would call impossible is merely rare under a Pareto. Actuaries fit Paretos to catastrophe data and price reinsurance off the tail index $\alpha$.

---

### Lognormal — Gyarados *(multiplicative)*

*The Multiplicative-Growth Pokémon.* The log is normal; the variable itself is the exponential of a bell.

**Stat block.** $X$ is lognormal iff $\ln X\sim\Normal(\mu,\sigma^{2})$; equivalently $X=e^{Y}$ with $Y\sim\Normal(\mu,\sigma^{2})$. Then
$$\E[X]=e^{\mu+\frac12\sigma^{2}},\qquad \Var(X)=\big(e^{\sigma^{2}}-1\big)e^{2\mu+\sigma^{2}},\qquad P(X\le x)=\Phi\!\left(\frac{\ln x-\mu}{\sigma}\right).$$
Support $(0,\infty)$; right-skewed with a heavy-ish tail.

**Recognition cue.** A positive quantity built by **multiplying** many independent factors (growth rates, repeated percentage changes), or "the log of the loss is normal" → lognormal. Solve probabilities by taking logs and falling back on the normal table.

**Fidelity.** **Gyarados** is what a humble **Magikarp** becomes through compounding growth — small multiplicative steps stacking into something enormous. Where the normal is the limit of *additive* pieces, the lognormal is the limit of *multiplicative* ones: take logs and the multiplication becomes addition, landing you back on Clefairy's bell. *(ch12)*
:::

---

> **Gotta catalogue 'em all.** Twelve in-scope Pokémon — seven discrete, five continuous — plus the two off-syllabus rares. Match the recognition cue to the situation, reach for the mascot, and the stat block is already in hand. That is the whole Field Guide: see the behavior, name the Pokémon, read the math.
