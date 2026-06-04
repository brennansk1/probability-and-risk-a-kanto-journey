# Notation Ledger — *A Kanto Journey*

> **What this file is.** A single authoritative list of every mathematical symbol used in the book: its **spoken name** (how to read it aloud), its **plain meaning** (one phrase, no symbols), and the **chapter of first introduction** (where the reader is first taught to read it). This ledger powers two things: the **notation-before-introduction build check** (Master Plan Part 8, gate 3 — no symbol may appear in a chapter before its "first-introduction" chapter), and **Appendix G** (the glossary, which is generated to agree with this file).
>
> **How "first introduction" is assigned.** A symbol's home chapter is where it receives **Beat-5 treatment** — named, read aloud, motivated by translating English → symbol (Master Plan Part 4, first-use law). Chapter 0 ("Reading the Symbols" primer) deliberately *previews* a handful of symbols ($\sum$, $\given$, $P(\cdot)$, $\E[\cdot]$, subscripts, $\in$, $\int$) so the reader can read a formula aloud on night one; for those, the "Primer (Ch 0)" preview and the full-lesson chapter are both noted. Macros are defined in `book/mathjax-preamble.md` (see column "Macro").
>
> **House rule reminder.** The conditional bar is `\mid` (`\given`), **never** `\middle`. Operators (`\E`, `\Var`, …) are `\operatorname`, so they upright-set and never read as multiplication.

---

## 1 — Core reading symbols (the Chapter 0 primer five, + two preview)

| Symbol | Macro | Spoken name | Plain meaning | First introduced |
|---|---|---|---|---|
| $X,\,Y,\,N,\,L$ | — | "the variable $X$" (capital) | The **name** of an uncertain quantity — a labeled slot whose value is not yet pinned down. | **Ch 0**, Concept 1 (convention used everywhere; random variables formalized Ch 6) |
| $x,\,y,\,n,\,\ell$ | `\ell` | "a value of $X$" (lowercase) | **One particular value** the matching variable could take. | **Ch 0**, Concept 1 |
| $a_i,\;L_i,\;p_k$ | — | "$a$-sub-$i$," "the $i$-th $a$" | A **subscript** — a label saying *which member* of a numbered family (never multiply, never a power). | **Ch 0**, Concept 2 |
| $\sum$ | `\sum` | "the sum of" (capital sigma) | A long-handled plus sign: **add up the listed terms**, from the start label (below) to the stop label (above). | **Ch 0**, Concept 3 (full lesson Ch 1, Entry №06) |
| $\prod$ | `\prod` | "the product of" (capital pi) | Like $\sum$ but **multiplies** the terms instead of adding. | **Ch 0**, Concept 3 (full lesson Ch 1, Entry №06) |
| $f(x)$ | — | "$f$ of $x$" | A **named function** applied to input $x$ — *not* "$f$ times $x$." | **Ch 0**, Concept 4 (functions taught Ch 1, Entry №05) |
| $P(\cdot)$ | — | "the probability of …" | The **probability operator**: feed it an event, read out a number in $[0,1]$. | **Ch 0**, Concept 4 (formalized Ch 3) |
| $\E[\cdot]$ | `\E` | "the expected value of …," "the average of …" | The **expectation operator**: the long-run (probability-weighted) average of a random variable. | **Ch 0**, Concept 4 (full lesson Ch 7, Entry №01) |
| $\mid$ (the bar) | `\given` | "given that" | **Conditioning**: everything to the *right* is the world assumed true; the *left* is what you find inside it. Not symmetric: $P(A\mid B)\neq P(B\mid A)$. | **Ch 0**, Concept 5 (full lesson Ch 5) |
| $\in$ | `\in` | "is in," "belongs to" | **Set membership**: the left-hand thing is one of the elements of the right-hand collection. | **Ch 0** preview ("Two More Symbols"); full lesson Ch 1 / Ch 3 |
| $\int$ | `\int` | "the integral of," "the continuous sum of" | The continuous cousin of $\sum$: **area under a curve** / total of a smoothly varying quantity. | **Ch 0** preview ("Two More Symbols"); full lesson Ch 2 |

---

## 2 — Algebra & number toolkit (Ch 1)

| Symbol | Macro | Spoken name | Plain meaning | First introduced |
|---|---|---|---|---|
| $<,\,>,\,\le,\,\ge$ | `\le \ge` | "less than," "greater than," "at most," "at least" | Order comparisons; $\le$ allows equality. | **Ch 1** (Entry №01) |
| $[a,b],\,(a,b)$ | — | "the closed / open interval $a$ to $b$" | All numbers between $a$ and $b$; square = endpoint included, round = excluded. | **Ch 1** (Entry №01) |
| $=,\,\neq,\,\approx$ | `\neq \approx` | "equals," "is not equal to," "is approximately" | Exact equality / inequality / rounded near-equality. | **Ch 1** ($\neq$ previewed Ch 0) |
| $\tfrac{a}{b},\,\dfrac{a}{b}$ | `\tfrac \dfrac \frac` | "$a$ over $b$" | A **fraction** / ratio / proportion. (`\dfrac` = display size, `\tfrac` = inline size; same meaning.) | **Ch 1** (Entry №02) |
| $\%$ | — | "percent" | Per hundred: $35\% = 0.35$. | **Ch 1** (Entry №02) |
| $a^n,\;a^{-1}$ | — | "$a$ to the $n$," "$a$ inverse" | **Exponent** (above the line): repeated multiplication; negative power = reciprocal. | **Ch 1** (Entry №03) |
| $\sqrt{\,\cdot\,}$ | `\sqrt` | "the square root of" | The non-negative number whose square is the input. | **Ch 1** (Entry №03) |
| $\ln,\,\log,\,\exp$ | `\ln \exp` | "natural log," "log," "exp" / "$e$ to the" | Logarithm (the inverse of exponentiation) and the exponential function. | **Ch 1** (`\exp` form Ch 7) |
| $\to$ | `\to` | "approaches," "goes to" | A quantity tending toward a value (used for limits and mappings). | **Ch 1** |
| $\Rightarrow,\,\Longrightarrow$ | `\Rightarrow` | "implies," "therefore" | Logical consequence: the left forces the right. | **Ch 1** |
| $\cdot,\,\times,\,\div$ | `\cdot \times \div` | "times," "times," "divided by" | Multiplication (two notations) and division. | **Ch 1** ($\cdot,\times$ previewed Ch 0) |
| $\infty$ | `\infty` | "infinity" | Unbounded / without limit (a direction, not a number). | **Ch 1** |
| $n!$ | — | "$n$ factorial" | $n\times(n-1)\times\cdots\times1$ — the number of orderings of $n$ items. | **Ch 1** (full use Ch 4) |
| $\theta$ | `\theta` | "theta" | A generic **parameter** placeholder (later: a scale/mean parameter). | **Ch 1** |
| $\pm$ | `\pm` | "plus or minus" | Both the $+$ and $-$ cases (later: a margin around a center). | **Ch 1** (heavy use Ch 13–14) |

---

## 3 — Sets, outcomes & events (Ch 3)

| Symbol | Macro | Spoken name | Plain meaning | First introduced |
|---|---|---|---|---|
| $\{\,\cdots\}$ | — | "the set containing …" | A **set**: an unordered collection of distinct outcomes. | **Ch 3** (Entry №01) |
| $S$ (or $\Omega$) | — | "the sample space" | The set of **all** possible outcomes of an experiment. | **Ch 3** (Entry №01) |
| $\in,\;\notin$ | `\in \not\in` | "is in," "is not in" | Membership / non-membership of an outcome in a set. | **Ch 3** (previewed Ch 0) |
| $\subseteq$ | `\subseteq` | "is a subset of" | Every element of the left set is also in the right set. | **Ch 3** |
| $\cap$ | `\cap` | "intersect," "and" | Outcomes in **both** events at once. | **Ch 3** (Entry №03) |
| $\cup$ | `\cup` | "union," "or" | Outcomes in **either** event (or both). | **Ch 3** (Entry №03) |
| $A^c$ | — | "$A$-complement," "not $A$" | Every outcome **not** in $A$. | **Ch 3** (previewed Ch 0, WE 0.2c) |
| $A\setminus B$ | `\setminus` | "$A$ minus $B$" | Outcomes in $A$ but not in $B$. | **Ch 3** |
| $\varnothing$ | `\varnothing` | "the empty set" | The set with no outcomes; the impossible event. | **Ch 3** |
| $A\cap B=\varnothing$ | — | "mutually exclusive / disjoint" | The two events cannot both occur. | **Ch 3** (Entry №05) |
| $\iff,\,\Leftrightarrow$ | `\iff` | "if and only if" | Two-way logical equivalence. | **Ch 3** |
| $\max$ | `\max` | "the maximum of" | The largest value in a set. | **Ch 3** |

---

## 4 — Probability rules & independence (Ch 4–5)

| Symbol | Macro | Spoken name | Plain meaning | First introduced |
|---|---|---|---|---|
| $P(A\cap B)$ | — | "the probability of $A$ and $B$" | Joint probability of both events. | **Ch 4** (Entry №02) |
| $P(A\mid B)$ | `\given` | "the probability of $A$ given $B$" | Conditional probability (full lesson; previewed Ch 0). | **Ch 5** (Entry №01) |
| $P(A\cup B)$ | — | "the probability of $A$ or $B$" | Addition rule / inclusion–exclusion. | **Ch 4** (Entry №03) |
| $\binom{n}{k}$ | `\binom \dbinom` | "$n$ choose $k$" | The number of ways to choose $k$ items from $n$ (combinations). | **Ch 4** (Entry №03; previewed Ch 1) |
| $A\perp B$ | `\perp` | "$A$ is independent of $B$" | One event's occurrence does not change the other's probability. (For RVs, Ch 11.) | **Ch 4** (Entry №04; symbol Ch 11) |
| $\propto$ | `\propto` | "is proportional to" | Equal up to a constant multiplier. | **Ch 6** |

---

## 5 — Random variables & their functions (Ch 6)

| Symbol | Macro | Spoken name | Plain meaning | First introduced |
|---|---|---|---|---|
| $p(x),\,p_X(x)$ | — | "the pmf of $X$ at $x$" | **Probability mass function**: $P(X=x)$ for a discrete variable. | **Ch 6** (Entry №02) |
| $f(x),\,f_X(x)$ | — | "the pdf / density of $X$ at $x$" | **Probability density function**: height of the density curve (continuous). | **Ch 6** (Entry №03) |
| $F(x),\,F_X(x)$ | — | "the cdf of $X$ at $x$" | **Cumulative distribution function**: $P(X\le x)$, the running total. | **Ch 6** (Entry №04) |
| $S(x),\,S_X(x)$ | — | "the survival function of $X$ at $x$" | $P(X>x)=1-F(x)$, the tail probability. | **Ch 6** (Entry №05) |
| $X\sim \text{Dist}$ | `\sim` | "$X$ is distributed as," "$X$ follows" | $X$ has the named distribution (e.g. $X\sim\Normal(\mu,\sigma^2)$). | **Ch 6** (symbol previewed Ch 2) |
| $\lfloor x\rfloor$ | `\lfloor \rfloor` | "the floor of $x$" | The greatest integer $\le x$. | **Ch 8** |
| $g(X)$ | — | "$g$ of $X$" | A function/transformation **of** a random variable (still random). | **Ch 6** (LOTUS, Ch 7 Entry №02) |

---

## 6 — Summaries: expectation, spread, MGF (Ch 7)

| Symbol | Macro | Spoken name | Plain meaning | First introduced |
|---|---|---|---|---|
| $\E[X]$ | `\E` | "the expected value of $X$" | The probability-weighted average (full lesson; previewed Ch 0). | **Ch 7** (Entry №01) |
| $\mu$ | `\mu` | "mu" | The **mean** $\E[X]$ as a named constant. | **Ch 7** |
| $\Var(X)$ | `\Var` | "the variance of $X$" | Average squared distance from the mean: $\E[(X-\mu)^2]$. | **Ch 7** (Entry №03; previewed Ch 0) |
| $\sigma,\,\sigma^2$ | `\sigma` | "sigma," "sigma-squared" | Standard deviation and variance as named constants. | **Ch 7** |
| $\SD(X)$ | `\SD` | "the standard deviation of $X$" | $\sqrt{\Var(X)}$, spread in the original units. | **Ch 7** (Entry №03) |
| $\text{CV}$ | — | "the coefficient of variation" | $\SD(X)/\E[X]$, relative spread. | **Ch 7** (Entry №03) |
| $M_X(t)$ | — | "the MGF of $X$," "$M$-sub-$X$ of $t$" | **Moment generating function** $\E[e^{tX}]$; its derivatives at 0 give the moments. | **Ch 7** (Entry №04) |
| $e^{tX},\,\exp(tX)$ | `\exp` | "$e$ to the $tX$" | The exponential inside the MGF. | **Ch 7** |

---

## 7 — Named distributions (Ch 8 discrete, Ch 9 continuous)

| Symbol | Macro | Spoken name | Plain meaning | First introduced |
|---|---|---|---|---|
| $\Binom(n,p)$ | `\Binom` | "Binomial $n$, $p$" | Count of successes in $n$ independent trials. | **Ch 8** (Entry №02) |
| $\Geom(p)$ | `\Geom` | "Geometric $p$" | Trials until the first success. | **Ch 8** (Entry №03) |
| $\NegBin(r,p)$ | `\NegBin` | "Negative Binomial $r$, $p$" | Trials until the $r$-th success. | **Ch 8** (Entry №04; symbol Ch 13) |
| $\HyperGeom$ | `\HyperGeom` | "Hypergeometric" | Successes drawn without replacement. | **Ch 8** (Entry №05) |
| $\Poisson(\lambda)$ | `\Poisson` | "Poisson lambda" | Count of rare events in a fixed interval. | **Ch 8** (Entry №06) |
| $\lambda$ | `\lambda` | "lambda" | The Poisson **rate** (mean count per interval). | **Ch 8** (symbol previewed Ch 2) |
| $\Unif(a,b)$ | `\Unif` | "Uniform $a$ to $b$" | Equally likely over an interval. | **Ch 9** (Entry №02) |
| $\Expo(\theta)$ | `\Expo` | "Exponential theta" | Waiting time with constant hazard; memoryless. | **Ch 9** (Entry №03) |
| $\GammaDist(\alpha,\theta)$ | `\GammaDist` | "Gamma alpha, theta" | Sum of $\alpha$ exponentials; shape $\alpha$, scale $\theta$. | **Ch 9** (Entry №04) |
| $\alpha$ | `\alpha` | "alpha" | A **shape** parameter (Gamma/Beta). | **Ch 9** (symbol previewed Ch 2) |
| $\BetaDist(\alpha,\beta)$ | `\BetaDist` | "Beta alpha, beta" | A distribution on $[0,1]$; shapes $\alpha,\beta$. | **Ch 9** (Entry №05) |
| $\beta$ | `\beta` | "beta" | A second **shape** parameter (Beta). | **Ch 9** |
| $\Normal(\mu,\sigma^2)$ | `\Normal` | "Normal mu, sigma-squared" | The bell curve; mean $\mu$, variance $\sigma^2$. | **Ch 9** (Entry №06) |
| $\Phi(z)$ | `\Phi` | "Phi of $z$," "the standard normal cdf" | $P(Z\le z)$ for the standard normal — the table value. | **Ch 9** |
| $Z$ | — | "$Z$," "the standard normal / $z$-score" | A $\Normal(0,1)$ variable; $(X-\mu)/\sigma$. | **Ch 9** |
| $\Gamma(\alpha)$ | `\Gamma` | "the Gamma function of alpha" | The continuous factorial: $\Gamma(n)=(n-1)!$. | **Ch 2** (Entry №04, the Master Ball) |

---

## 8 — Calculus toolkit (Ch 2)

| Symbol | Macro | Spoken name | Plain meaning | First introduced |
|---|---|---|---|---|
| $\int_a^b f(x)\,dx$ | `\int` | "the integral from $a$ to $b$ of $f$ of $x$, $dx$" | Area under $f$ between $a$ and $b$ (full lesson; previewed Ch 0). | **Ch 2** (Entry №03) |
| $\int_0^\infty$ | `\int \infty` | "the integral from 0 to infinity" | An **improper integral** (used to normalize densities, find survival). | **Ch 2** (Entry №03) |
| $dx,\,dt$ | — | "$dx$," "with respect to $x$" | The variable being swept across in an integral. | **Ch 2** |
| $\lim$ | `\lim` | "the limit of" | The value a quantity approaches. | **Ch 2** (Entry №02) |
| $f'(x),\,\dfrac{d}{dx}$ | — | "$f$-prime of $x$," "$d$ by $dx$" | The **derivative** — instantaneous rate of change / slope. | **Ch 2** (Entry №02) |
| $\left|\dfrac{d}{dy}g^{-1}(y)\right|$ | `\left| \right|` | "the Jacobian," "how much the axis stretches" | The **change-of-variable stretch factor**: how much a transformation $y=g(x)$ squeezes or stretches length, rescaling the density so area (probability) is conserved. | **Ch 9** (Concept 6, Entry №07) |
| $\min$ | `\min` | "the minimum of" | The smallest value in a set. | **Ch 2** |

---

## 9 — Insurance / payment operators (Ch 10)

| Symbol | Macro | Spoken name | Plain meaning | First introduced |
|---|---|---|---|---|
| $(X-d)_+$ | `\dplus{X}{d}` | "$X$ minus $d$, plus" | The payment after deductible $d$: the positive part, never below zero. | **Ch 10** (Entry №01) |
| $X\wedge u$ | `\wedge` | "$X$ wedge $u$," "$X$ capped at $u$" | The minimum of $X$ and $u$ — a policy limit. | **Ch 10** (Entry №02) |
| $\E[X\wedge u]$ | `\limexp{X}{u}` | "the limited expected value" | Expected loss capped at $u$. | **Ch 10** (Entry №02) |
| $\mathbf{1}\{A\}$ | `\indicator{A}` | "the indicator of $A$" | $1$ if event $A$ happens, $0$ otherwise. | **Ch 10** |
| $\E[X\mid Y]$ | `\E \given` | "the conditional expectation of $X$ given $Y$" | The mean of $X$ within each value of $Y$ (itself random). | **Ch 10** (full lesson Ch 12) |

---

## 10 — Joint, conditional & double expectation (Ch 11–12)

| Symbol | Macro | Spoken name | Plain meaning | First introduced |
|---|---|---|---|---|
| $f_{X,Y}(x,y)$ | — | "the joint density of $X$ and $Y$" | Density over a pair of variables. | **Ch 11** (Entry №01) |
| $f_X(x)$ (marginal) | — | "the marginal density of $X$" | One variable's density, summing/integrating the other out. | **Ch 11** (Entry №02) |
| $f_{Y\mid X}(y\mid x)$ | `\given` | "the conditional density of $Y$ given $X=x$" | Density of $Y$ within a fixed $X$. | **Ch 11** (Entry №04) |
| $\iint$ | `\iint` | "the double integral of" | Integrate over a two-dimensional region. | **Ch 11** (Entry №03; previewed Ch 2) |
| $\partial$ | `\partial` | "partial" | A **partial derivative** (differentiate one variable, hold others). | **Ch 11** |
| $X\perp Y$ | `\perp` | "$X$ and $Y$ are independent" | The joint factors into the product of marginals. | **Ch 11** (Entry №05) |
| $\E[X\mid Y]$ | `\E \given` | "the conditional expectation of $X$ given $Y$" | Random variable: the mean of $X$ in each $Y$-slice. | **Ch 12** (full lesson) |
| $\E\big[\E[X\mid Y]\big]=\E[X]$ | — | "the law of iterated / total expectation" | Average the conditional means to recover the overall mean. | **Ch 12** |
| $\Var(X\mid Y)$ | `\Var \given` | "the conditional variance of $X$ given $Y$" | Spread of $X$ within each $Y$-slice. | **Ch 12** |
| $\Lambda,\,\Theta$ | `\Lambda \Theta` | "capital lambda," "capital theta" | Random **parameters** (a mixing/prior variable). | **Ch 12** |

---

## 11 — Covariance, sums & limit theorems (Ch 13–14)

| Symbol | Macro | Spoken name | Plain meaning | First introduced |
|---|---|---|---|---|
| $\Cov(X,Y)$ | `\Cov` | "the covariance of $X$ and $Y$" | How two variables move together: $\E[XY]-\E[X]\E[Y]$. | **Ch 13** (Entry №01; previewed Ch 0) |
| $\Corr(X,Y),\,\rho$ | `\Corr \rho` | "the correlation of $X$ and $Y$," "rho" | Covariance rescaled to $[-1,1]$. | **Ch 13** (Entry №02) |
| $\bar X$ | `\bar` | "$X$-bar" | The **sample mean** of $n$ observations. | **Ch 14** |
| $\xrightarrow{d},\,\to$ | `\xrightarrow \to` | "converges in distribution to" | A sequence of distributions approaches a limiting one (CLT). | **Ch 14** (Entry №04) |
| $\overline{X}_n$ | `\overline` | "$X$-bar-sub-$n$" | Sample mean of the first $n$ terms. | **Ch 14** |

---

## 12 — Layout / structural glyphs (not "math," but read)

| Symbol | Macro | Spoken name | Plain meaning | First introduced |
|---|---|---|---|---|
| $:=$ | — | "is defined to be" | Introduces a definition (left defined by right). | **Ch 0** (Entry №00.3) |
| $\overset{?}{=}$ | `\overset` | "does this equal?" | A *claimed* equality being tested (often the wrong-idea beat). | **Ch 0** |
| $\boxed{\;}$ | `\boxed` | "the boxed result" | A keeper formula highlighted as the destination. | **Ch 2** |
| $\underbrace{\;}$ | `\underbrace` | "the underbraced piece, namely…" | Annotates a sub-expression with its meaning. | **Ch 2** |
| $\checkmark$ | `\checkmark` | "check" | A verified / satisfied condition. | **Ch 2** |
| $\dots,\,\cdots,\,\ldots$ | `\dots \cdots \ldots` | "and so on," "dot-dot-dot" | Omitted terms following the established pattern. | **Ch 0** (Concept 2) |

---

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; educational, non-commercial work. Symbols verified against `book/mathjax-preamble.md` and SOA Exam P syllabus (2026).*
