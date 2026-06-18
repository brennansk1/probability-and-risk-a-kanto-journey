<!--
  appendix: g_glossary
  status: complete
-->

# Appendix G — Glossary & Notation Index {.type-normal}

*Two reference tables for the whole journey. **Part 1** is the **Kanto ↔ Formal dictionary**: every narrative name this book uses for a real probability idea, paired with the term an actuary or exam writer would use, and the chapter where you first met it. **Part 2** is the **Notation index**: every symbol, how to read it aloud, what it means in one plain phrase, and where it is first taught. Both are cross-referenced to first appearance so you can jump back to the full lesson.*

> **How to use this.** Stuck on a symbol mid-problem? Part 2, find the glyph, read its plain meaning, follow the chapter link to the nine-beat lesson. Translating a Pokémon-flavored idea into "real exam" language (the *Transfer Test*, Master Plan Part 13)? Part 1 gives you the de-skinned term. The notation index agrees line-for-line with the build's `notation_ledger.md`.

---

## Part 1 — The Kanto ↔ Formal Dictionary

*Read it as: "When the book says **[Kanto term]**, an actuary says **[formal term]**." First-appearance chapter in the last column.*

### The world & the cast (the teaching frame)

| Kanto term | Formal term / job | First appears |
|---|---|---|
| The journey to the Indigo Plateau | The Exam P syllabus, start to finish | Ch 0 |
| A Gym Badge | Mastery of one chapter's outcomes | Ch 0 |
| **Exam P** (the toughest trainer) | The SOA probability exam itself | Ch 0 |
| Professor Oak | The *formalizer* — states each definition rigorously | Ch 0 |
| Your rival (Gary) | The *expert model* — the fast, exam-speed solution path | Ch 0 |
| **Team Rocket** | The *misconception* — embodies the single most tempting wrong move | Ch 0 |
| The Pokédex / "Actuary Mode" | The device that *poses* each problem | Ch 0 |
| **Pokédex Entry** (blue) | A keeper formula + plain meaning + recognition cue | Ch 0 |
| **Trainer's Tip** (yellow) | Exam craft: a shortcut, keystroke, or pacing trick | Ch 0 |
| **Team Rocket's Trap** (red) | A canonical mistake, surfaced and dismantled | Ch 0 |
| **From Kanto to the Real World** (green) | The real actuarial use + a transfer check | Ch 0 |
| **Concept Gate** ("Do you already own this?") | A skip-check / test-out gate | Ch 0 |
| **Master Ball** ⚪ | The highest-leverage shortcut (e.g. the Gamma integral) | Ch 2 |
| Poké Ball 🔴 | A routine method / routine-difficulty problem | Ch 0 |
| Potion 🧴 | A "rematch pointer" back to a lesson | Ch 0 |

### The core ideas (concept ↔ formal name)

| Kanto term | Formal term | First appears |
|---|---|---|
| The spinning Poké Ball (the slot) | A **random variable** (uncertain quantity) | Ch 0 (formalized Ch 6) |
| What filled the slot this run | A **realized value** (outcome) | Ch 0 |
| The tall grass / which Pokémon appears | An **experiment** and its **sample space** | Ch 3 |
| One thing that can happen | An **outcome**; a set of them is an **event** | Ch 3 |
| The Spearow swarm (Route 1) | **Independent repeated trials** / counting | Ch 3–4 |
| "Given this clue, how likely…" (shrinking the world) | **Conditional probability** $P(A\mid B)$ | Ch 5 |
| Reasoning backward from evidence | **Bayes' theorem** / total probability | Ch 5 |
| The long-run average / "what you'd expect" | **Expectation** $\E[X]$ (the mean) | Ch 7 |
| How spread-out / unpredictable a quantity is | **Variance** and **standard deviation** | Ch 7 |
| The fingerprint that pins down a distribution | The **moment generating function** (MGF) | Ch 7 |
| A **named pattern** of chance (discrete) | A discrete distribution (Binomial, Poisson, …) | Ch 8 |
| A **named pattern** of chance (smooth) | A continuous distribution (Normal, Exponential, …) | Ch 9 |
| "Counts of rare events in a fixed window" | The **Poisson** distribution | Ch 8 |
| "Waiting time with no memory" | The **Exponential** distribution; **memorylessness** | Ch 9 |
| The bell curve | The **Normal** distribution | Ch 9 |
| The **Darth Vader rule** | The survival-function method for $\E[X]$ | Ch 7 |
| The **kernel** (recognize-and-skip-the-integral trick) | Matching a density's functional form to a known family | Ch 9 |
| The **deductible** | The amount the insured pays before coverage; $(X-d)_+$ | Ch 10 |
| The **policy limit** / cap | The maximum payment; $X\wedge u$ | Ch 10 |
| "Per loss vs. per payment" | Unconditional vs. conditional-on-a-claim expectation | Ch 10 |
| **Two fates entwined** | A **joint distribution** of two variables | Ch 11 |
| Looking at one variable, ignoring the other | A **marginal distribution** | Ch 11 |
| **Expectation within expectation** | **Conditional & double (iterated) expectation** | Ch 12 |
| Splitting spread into "within" and "between" | The **law of total variance** | Ch 12 |
| **Combining forces** (the team's total) | Sums of random variables; **covariance** & variance of sums | Ch 13 |
| Moving together / moving apart | **Covariance** and **correlation** | Ch 13 |
| The strongest / weakest Pokémon on the team | The **maximum / minimum** (order statistics) | Ch 14 |
| **Order from chaos** (pooling settles down) | The **Central Limit Theorem** | Ch 14 |
| The half-step fix when a smooth curve approximates counts | The **continuity correction** | Ch 14 |

---

## Part 2 — Notation Index (read-aloud + plain meaning)

*Every symbol, its spoken name, a one-phrase meaning, and the chapter that first teaches it. Conditional bar is $\mid$ ("given"); operators are upright and never mean multiplication. Agrees with `notation_ledger.md`.*

### Reading-the-symbols core (Ch 0 primer)

| Symbol | Read aloud | Plain meaning | First |
|---|---|---|---|
| $X,\,N,\,L$ | "the variable $X$" | Name of an uncertain quantity (a slot) | Ch 0 |
| $x,\,n,\,\ell$ | "a value of $X$" | One particular value the variable could take | Ch 0 |
| $a_i,\,p_k$ | "$a$-sub-$i$," "the $i$-th $a$" | A **subscript** label — which member of a family (never $\times$, never a power) | Ch 0 |
| $\sum$ | "the sum of" | Add the listed terms (start below, stop above) | Ch 0 |
| $\prod$ | "the product of" | Multiply the listed terms | Ch 0 |
| $f(x)$ | "$f$ of $x$" | Function $f$ applied to $x$ (not "$f$ times $x$") | Ch 0 |
| $P(\cdot)$ | "the probability of …" | Probability operator → a number in $[0,1]$ | Ch 0 |
| $\E[\cdot]$ | "the expected value of …" | The long-run average | Ch 0 |
| $\mid$ | "given that" | Conditioning bar — right = assumed world, left = the question | Ch 0 |
| $\in$ | "is in / belongs to" | Set membership | Ch 0 |
| $\int$ | "the integral of" | Continuous sum / area under a curve | Ch 0 |

### Algebra & numbers (Ch 1)

| Symbol | Read aloud | Plain meaning | First |
|---|---|---|---|
| $\le,\,\ge$ | "at most," "at least" | Order comparison allowing equality | Ch 1 |
| $[a,b],\,(a,b)$ | "closed / open interval" | Numbers between $a$ and $b$ (endpoint in / out) | Ch 1 |
| $\approx$ | "is approximately" | Near-equality / rounded | Ch 1 |
| $\dfrac{a}{b}$ | "$a$ over $b$" | A fraction / ratio | Ch 1 |
| $a^n$ | "$a$ to the $n$" | Exponent (above the line) | Ch 1 |
| $\sqrt{\,}$ | "the square root of" | Non-negative root | Ch 1 |
| $\ln,\,\exp$ | "natural log," "$e$ to the" | Logarithm and exponential | Ch 1 |
| $\to$ | "approaches / goes to" | Tends toward a value | Ch 1 |
| $\Rightarrow$ | "implies" | Logical consequence | Ch 1 |
| $\infty$ | "infinity" | Unbounded | Ch 1 |
| $n!$ | "$n$ factorial" | $n(n-1)\cdots 1$ | Ch 1 |
| $\pm$ | "plus or minus" | Both signs / a margin | Ch 1 |

### Sets, outcomes & probability rules (Ch 3–5)

| Symbol | Read aloud | Plain meaning | First |
|---|---|---|---|
| $\{\cdots\}$ | "the set containing…" | An unordered collection | Ch 3 |
| $S$ | "the sample space" | All possible outcomes | Ch 3 |
| $\subseteq$ | "is a subset of" | Contained within | Ch 3 |
| $\cap$ | "intersect / and" | In both events | Ch 3 |
| $\cup$ | "union / or" | In either event | Ch 3 |
| $A^c$ | "$A$-complement / not $A$" | Everything not in $A$ | Ch 3 |
| $A\setminus B$ | "$A$ minus $B$" | In $A$ but not $B$ | Ch 3 |
| $\varnothing$ | "the empty set" | No outcomes; impossible event | Ch 3 |
| $\iff$ | "if and only if" | Two-way equivalence | Ch 3 |
| $P(A\mid B)$ | "probability of $A$ given $B$" | Conditional probability | Ch 5 |
| $\binom{n}{k}$ | "$n$ choose $k$" | Number of size-$k$ subsets of $n$ | Ch 4 |
| $A\perp B$ | "$A$ independent of $B$" | Occurrence doesn't change the other's chance | Ch 4 (symbol Ch 11) |
| $\propto$ | "is proportional to" | Equal up to a constant | Ch 6 |

### Random variables & distributions (Ch 6–9)

| Symbol | Read aloud | Plain meaning | First |
|---|---|---|---|
| $p(x)$ | "the pmf at $x$" | $P(X=x)$, discrete mass | Ch 6 |
| $f(x)$ | "the pdf / density at $x$" | Height of the density curve | Ch 6 |
| $F(x)$ | "the cdf at $x$" | $P(X\le x)$, running total | Ch 6 |
| $S(x)$ | "the survival function at $x$" | $P(X>x)=1-F(x)$ | Ch 6 |
| $X\sim\text{Dist}$ | "$X$ is distributed as" | $X$ follows the named distribution | Ch 6 |
| $\lfloor x\rfloor$ | "the floor of $x$" | Greatest integer $\le x$ | Ch 8 |
| $\Binom(n,p)$ | "Binomial $n$, $p$" | Successes in $n$ trials | Ch 8 |
| $\Geom(p)$ | "Geometric $p$" | Trials to first success | Ch 8 |
| $\Poisson(\lambda)$ | "Poisson lambda" | Rare-event counts; rate $\lambda$ | Ch 8 |
| $\HyperGeom$ | "Hypergeometric" | Successes drawn without replacement | Ch 8 |
| $\Unif(a,b)$ | "Uniform $a$ to $b$" | Equally likely on an interval | Ch 9 |
| $\Expo(\theta)$ | "Exponential theta" | Memoryless waiting time | Ch 9 |
| $\GammaDist(\alpha,\theta)$ | "Gamma alpha, theta" | Shape $\alpha$, scale $\theta$ | Ch 9 |
| $\BetaDist(\alpha,\beta)$ | "Beta alpha, beta" | Distribution on $[0,1]$ | Ch 9 |
| $\Normal(\mu,\sigma^2)$ | "Normal mu, sigma-squared" | The bell curve | Ch 9 |
| $\Phi(z)$ | "Phi of $z$" | Standard-normal cdf (table value) | Ch 9 |
| $\Gamma(\alpha)$ | "the Gamma function" | Continuous factorial; $\Gamma(n)=(n-1)!$ | Ch 2 |

### Summaries, calculus & operators (Ch 2, 7)

| Symbol | Read aloud | Plain meaning | First |
|---|---|---|---|
| $\E[X]$ | "the expected value of $X$" | Probability-weighted average | Ch 7 |
| $\mu$ | "mu" | The mean as a constant | Ch 7 |
| $\Var(X)$ | "the variance of $X$" | $\E[(X-\mu)^2]$ | Ch 7 |
| $\sigma,\,\sigma^2$ | "sigma," "sigma-squared" | SD and variance constants | Ch 7 |
| $\SD(X)$ | "the standard deviation of $X$" | $\sqrt{\Var(X)}$ | Ch 7 |
| $M_X(t)$ | "the MGF of $X$" | $\E[e^{tX}]$; generates moments | Ch 7 |
| $\int_a^b f\,dx$ | "the integral from $a$ to $b$" | Area under $f$ | Ch 2 |
| $\lim$ | "the limit of" | Value approached | Ch 2 |
| $f'(x)$ | "$f$-prime of $x$" | Derivative / slope | Ch 2 |
| $\min,\,\max$ | "minimum," "maximum" | Smallest / largest value | Ch 2–3 |

### Insurance, joint & multivariate (Ch 10–14)

| Symbol | Read aloud | Plain meaning | First |
|---|---|---|---|
| $(X-d)_+$ | "$X$ minus $d$, plus" | Payment after deductible $d$ (≥ 0) | Ch 10 |
| $X\wedge u$ | "$X$ capped at $u$" | $\min(X,u)$ — policy limit | Ch 10 |
| $\E[X\wedge u]$ | "the limited expected value" | Expected loss capped at $u$ | Ch 10 |
| $\mathbf{1}\{A\}$ | "the indicator of $A$" | $1$ if $A$ occurs, else $0$ | Ch 10 |
| $f_{X,Y}(x,y)$ | "the joint density" | Density over a pair | Ch 11 |
| $f_X(x)$ (marginal) | "the marginal density of $X$" | One variable, other summed out | Ch 11 |
| $f_{Y\mid X}(y\mid x)$ | "conditional density of $Y$ given $X$" | $Y$'s density within fixed $X$ | Ch 11 |
| $\iint$ | "the double integral" | Integrate over a 2-D region | Ch 11 |
| $\partial$ | "partial" | Partial derivative | Ch 11 |
| $X\perp Y$ | "$X$ and $Y$ independent" | Joint factors into marginals | Ch 11 |
| $\E[X\mid Y]$ | "conditional expectation of $X$ given $Y$" | Mean of $X$ in each $Y$-slice (random) | Ch 12 |
| $\Var(X\mid Y)$ | "conditional variance" | Spread of $X$ in each $Y$-slice | Ch 12 |
| $\Cov(X,Y)$ | "covariance of $X$, $Y$" | $\E[XY]-\E[X]\E[Y]$ | Ch 13 |
| $\Corr(X,Y),\,\rho$ | "correlation," "rho" | Covariance rescaled to $[-1,1]$ | Ch 13 |
| $\bar X$ | "$X$-bar" | The sample mean | Ch 14 |
| $\xrightarrow{d}$ | "converges in distribution to" | Distributions approach a limit (CLT) | Ch 14 |

### Structural glyphs

| Symbol | Read aloud | Plain meaning | First |
|---|---|---|---|
| $:=$ | "is defined to be" | Introduces a definition | Ch 0 |
| $\overset{?}{=}$ | "does this equal?" | A claimed equality being tested | Ch 0 |
| $\boxed{\ }$ | "the boxed result" | A keeper formula | Ch 2 |
| $\dots,\,\cdots$ | "and so on" | Omitted terms in the pattern | Ch 0 |

---

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; educational, non-commercial work. Notation verified against `book/mathjax-preamble.md` and the SOA Exam P syllabus (2026).*
