<!--
  file: appendix_a_formula_sheet
  kind: appendix
  letter: A
  title: Master Formula Sheet
  purpose: one-stop exam-day reference; every formula matches the chapters' Pokédex Entries exactly
  sources: ch03, ch04, ch05, ch06, ch09, ch10, ch11, ch12, ch14, ch15, ch16, ch17
  plan: MASTER_PLAN_V3 §17 (distribution roster), §23 (appendix spec)
-->

# Appendix A — The Master Formula Sheet {.type-electric}

> **What this is.** Every formula the book teaches, on one fold-out, in the order an exam-day brain reaches for it: general probability → the random-variable toolkit → a reference card for every in-scope distribution → insurance loss/payment → the multivariate machinery → the shortcut catalog. Each entry matches its chapter's **Pokédex Entry** exactly; the parenthetical tag (e.g. *ch11*) is where it was taught. Notation follows the book: $\E[\cdot]$ expectation, $\Var(\cdot)$ variance, $\SD(\cdot)=\sigma$, $\Cov(\cdot,\cdot)$ covariance, $\Corr(\cdot,\cdot)=\rho$, $S(\cdot)$ survival, $\mid$ "given," and $q=1-p$ throughout.

---

## 1. General Probability *(ch01–ch02)*

**Axioms & basic rules.** For events in a sample space $\Omega$,
$$0\le P(A)\le 1,\qquad P(\Omega)=1,\qquad P(A^c)=1-P(A).$$
$$P(\varnothing)=0,\qquad A\subseteq B\ \Rightarrow\ P(A)\le P(B).$$

**Addition rule (inclusion–exclusion).**
$$P(A\cup B)=P(A)+P(B)-P(A\cap B).$$
$$P(A\cup B\cup C)=P(A)+P(B)+P(C)-P(A\cap B)-P(A\cap C)-P(B\cap C)+P(A\cap B\cap C).$$

For **mutually exclusive** (disjoint) events the intersection terms vanish: $P(A\cup B)=P(A)+P(B)$.

**De Morgan.**
$$(A\cup B)^c=A^c\cap B^c,\qquad (A\cap B)^c=A^c\cup B^c.$$

**Conditional probability & the multiplication rule.**
$$P(A\mid B)=\frac{P(A\cap B)}{P(B)}\quad(P(B)>0);\qquad P(A\cap B)=P(B)\,P(A\mid B)=P(A)\,P(B\mid A).$$

**Independence.** $A,B$ are independent iff any (hence all) of:
$$P(A\cap B)=P(A)P(B),\qquad P(A\mid B)=P(A),\qquad P(B\mid A)=P(B).$$

> **Trap (ch01):** *mutually exclusive $\ne$ independent.* Disjoint events with $P(A),P(B)>0$ are in fact **dependent** ($P(A\mid B)=0$).

**Law of total probability.** For a partition $B_1,\dots,B_n$ of $\Omega$,
$$P(A)=\sum_{i} P(B_i)\,P(A\mid B_i).$$

**Bayes' theorem.**
$$P(B_j\mid A)=\frac{P(B_j)\,P(A\mid B_j)}{\displaystyle\sum_i P(B_i)\,P(A\mid B_i)}=\frac{P(B_j)\,P(A\mid B_j)}{P(A)}.$$

> **Trap (ch02):** the prosecutor's fallacy — $P(A\mid B)\ne P(B\mid A)$. Bayes is the conversion factor between them.

---

## 2. Random-Variable Toolkit *(ch03, ch09–ch10)*

**Discrete: pmf, cdf, survival.** *(ch03)*
$$p(k)=P(X=k)\ge0,\qquad \sum_k p(k)=1;$$
$$F(k)=P(X\le k)=\sum_{j\le k}p(j),\qquad S(k)=P(X>k)=1-F(k).$$
Endpoint care: $P(X<k)=F(k)-p(k)$, and $P(X\ge k)=S(k)+p(k)=1-F(k-1)$.

**Continuous: pdf, cdf, survival.** *(ch09)*
$$f(x)\ge0,\quad \int_{-\infty}^{\infty} f(x)\,dx=1,\qquad F(x)=\int_{-\infty}^{x} f(t)\,dt,\quad f(x)=F'(x),$$
$$S(x)=1-F(x),\qquad P(a<X<b)=\int_a^b f(x)\,dx=F(b)-F(a).$$
For a continuous $X$, $P(X=c)=0$, so $<$ and $\le$ are interchangeable. Solve for an unknown constant by forcing $\int f=1$.

**Mixed distributions.** *(ch09)* Masses plus density integrate to one:
$$\sum_i P(X=c_i)+\int f(x)\,dx=1,\qquad F(c)-F(c^-)=P(X=c)\ \text{(the cdf jumps by the mass)}.$$

**Expectation & LOTUS.** *(ch03, ch10)*
$$\E[X]=\sum_k k\,p(k)\quad\text{or}\quad \int_{-\infty}^{\infty} x\,f(x)\,dx;\qquad \E[g(X)]=\sum_k g(k)\,p(k)\quad\text{or}\quad \int g(x)\,f(x)\,dx.$$

**Linearity (always — no independence needed).**
$$\E[aX+b]=a\,\E[X]+b,\qquad \E[a]=a.$$

> **Trap (ch03):** for **nonlinear** $g$, $\E[g(X)]\ne g(\E[X])$. In particular $\E[X^2]\ne(\E[X])^2$; the gap *is* the variance.

**Variance & standard deviation.** *(ch03, ch10)*
$$\Var(X)=\E\big[(X-\mu)^2\big]=\E[X^2]-(\E[X])^2=\sigma^2,\qquad \SD(X)=\sigma=\sqrt{\Var(X)},$$
$$\Var(aX+b)=a^2\Var(X),\qquad \SD(aX+b)=|a|\,\SD(X).$$
Always $\Var(X)\ge0$, with $\Var(X)=0$ iff $X$ is constant.

**Moment generating function.** *(ch03)*
$$M_X(t)=\E\big[e^{tX}\big],\qquad \E[X^n]=M_X^{(n)}(0)=\left.\frac{d^n}{dt^n}M_X(t)\right|_{t=0},\qquad M_X(0)=1.$$
In particular $\E[X]=M_X'(0)$, $\E[X^2]=M_X''(0)$, so $\Var(X)=M_X''(0)-\big(M_X'(0)\big)^2$.

**Survival ("Darth-Vader") expectation.** *(ch03, ch10)* For a non-negative variable,
$$\text{discrete: }\E[X]=\sum_{k=0}^{\infty} S(k)=\sum_{k\ge0}P(X>k);\qquad \text{continuous: }\E[X]=\int_0^\infty S(x)\,dx.$$
Higher moments (continuous): $\E[X^k]=\displaystyle\int_0^\infty k\,x^{k-1}S(x)\,dx.$

**Mode, median, percentiles.** *(ch03)*
$$\text{mode}=\arg\max_k p(k)\quad\text{(tallest bar; ties}\Rightarrow\text{multimodal);}$$
$$\pi_p=\min\{k:F(k)\ge p\}\ \text{(discrete)},\qquad \text{median}=\pi_{0.5}.$$
Continuous: solve $F(\pi_p)=p$. The median is **robust** to tails; the mean is pulled by them.

---

## 3. Distribution Reference Cards *(ch03–ch05, ch11–ch12)*

> Conventions matching the chapters: $q=1-p$; the **exponential and gamma are parameterized by scale $\theta$** (so the exponential mean is $\theta$); the **geometric** appears in both a trials version and a failures version; the **negative binomial** counts *failures before the $r$-th success*. Recognition cues are one-liners for fast exam triage.

### Discrete distributions

| Distribution *(ch)* | Support | pmf | Mean | Variance | MGF | Recognition cue |
|---|---|---|---|---|---|---|
| **Bernoulli$(p)$** *(ch04)* | $\{0,1\}$ | $p^x q^{1-x}$ | $p$ | $pq$ | $q+pe^{t}$ | one success/fail trial ($n=1$ binomial) |
| **Binomial$(n,p)$** *(ch04)* | $0,\dots,n$ | $\binom{n}{x}p^x q^{\,n-x}$ | $np$ | $npq$ | $(q+pe^{t})^{n}$ | count of successes in $n$ **independent, fixed** trials |
| **Hypergeometric$(N,K,n)$** *(ch04)* | $\max(0,n{-}N{+}K)\dots\min(n,K)$ | $\dfrac{\binom{K}{x}\binom{N-K}{\,n-x}}{\binom{N}{n}}$ | $n\dfrac{K}{N}$ | $n\dfrac{K}{N}\dfrac{N-K}{N}\dfrac{N-n}{N-1}$ | — | draw $n$ **without replacement** from $N$ ($K$ "good") |
| **Geometric$(p)$ — trials** *(ch05)* | $1,2,\dots$ | $q^{\,k-1}p$ | $\dfrac1p$ | $\dfrac{q}{p^{2}}$ | $\dfrac{pe^{t}}{1-qe^{t}}$ | trial of the **first** success; $P(X>m)=q^{m}$ |
| **Geometric$(p)$ — failures** *(ch05)* | $0,1,2,\dots$ | $q^{k}p$ | $\dfrac{q}{p}$ | $\dfrac{q}{p^{2}}$ | $\dfrac{p}{1-qe^{t}}$ | **failures** before the first success |
| **Neg. binomial$(r,p)$** *(ch05)* | $0,1,2,\dots$ | $\binom{k+r-1}{k}p^{r}q^{k}$ | $\dfrac{rq}{p}$ | $\dfrac{rq}{p^{2}}$ | $\left(\dfrac{p}{1-qe^{t}}\right)^{\!r}$ | **failures** before the $r$-th success |
| **Poisson$(\lambda)$** *(ch05)* | $0,1,2,\dots$ | $\dfrac{e^{-\lambda}\lambda^{k}}{k!}$ | $\lambda$ | $\lambda$ | $e^{\lambda(e^{t}-1)}$ | random **count per window**; mean $=$ variance |
| **Discrete uniform$\{1,\dots,n\}$** *(ch03)* | $1,\dots,n$ | $\dfrac1n$ | $\dfrac{n+1}{2}$ | $\dfrac{n^{2}-1}{12}$ | $\dfrac{1}{n}\displaystyle\sum_{k=1}^{n}e^{tk}$ | **equally likely** over $n$ values |

*Bernoulli is the binomial with $n=1$. For a uniform on $\{a,\dots,b\}$ with $m=b-a+1$ values: mean $\tfrac{a+b}{2}$, variance $\tfrac{m^2-1}{12}$.*

**Memorylessness (geometric).** *(ch05)* $\;P(X>m+n\mid X>m)=P(X>n)=q^{n}.$

**Poisson superposition.** *(ch05)* Independent $X_i\sim\Poisson(\lambda_i)\Rightarrow \sum_i X_i\sim\Poisson\!\big(\sum_i\lambda_i\big)$.

**Poisson approximation to the binomial.** *(ch05)* $\Binom(n,p)\approx\Poisson(np)$ for large $n$, small $p$.

### Continuous distributions

| Distribution *(ch)* | Support | pdf | Mean | Variance | MGF | Recognition cue |
|---|---|---|---|---|---|---|
| **Uniform$(a,b)$** *(ch11)* | $[a,b]$ | $\dfrac{1}{b-a}$ | $\dfrac{a+b}{2}$ | $\dfrac{(b-a)^{2}}{12}$ | $\dfrac{e^{tb}-e^{ta}}{t(b-a)}$ | flat density on an interval |
| **Exponential$(\theta)$** *(ch11)* | $[0,\infty)$ | $\dfrac{1}{\theta}e^{-x/\theta}$ | $\theta$ | $\theta^{2}$ | $\dfrac{1}{1-\theta t}\ (t<\tfrac1\theta)$ | **memoryless** waiting time; $S(x)=e^{-x/\theta}$ |
| **Gamma$(\alpha,\theta)$** *(ch11)* | $(0,\infty)$ | $\dfrac{x^{\alpha-1}e^{-x/\theta}}{\Gamma(\alpha)\,\theta^{\alpha}}$ | $\alpha\theta$ | $\alpha\theta^{2}$ | $(1-\theta t)^{-\alpha}\ (t<\tfrac1\theta)$ | **sum of $\alpha$** exponentials; waiting for $\alpha$ events |
| **Beta$(\alpha,\beta)$** *(ch11)* | $[0,1]$ | $\dfrac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}x^{\alpha-1}(1-x)^{\beta-1}$ | $\dfrac{\alpha}{\alpha+\beta}$ | $\dfrac{\alpha\beta}{(\alpha+\beta)^{2}(\alpha+\beta+1)}$ | — | a **proportion** on $[0,1]$ |
| **Normal$(\mu,\sigma^{2})$** *(ch12)* | $(-\infty,\infty)$ | $\dfrac{1}{\sigma\sqrt{2\pi}}e^{-(x-\mu)^{2}/(2\sigma^{2})}$ | $\mu$ | $\sigma^{2}$ | $e^{\mu t+\frac12\sigma^{2}t^{2}}$ | bell curve; sums/averages of many i.i.d. |

**Exponential memorylessness.** *(ch11)* $\;P(X>s+t\mid X>s)=P(X>t)=e^{-t/\theta}.$

**Exponential / gamma / Poisson link.** *(ch11)* A sum of $\alpha$ i.i.d. $\Expo(\theta)$ waits is $\GammaDist(\alpha,\theta)$; the **count** of such events in a window is $\Poisson$.

::: enrichment
**OFF-SYLLABUS ENRICHMENT — flagged, never gated.** Taught because TIA covers them; **not** examined on Exam P.

**Pareto** *(ch11)* — Snorlax, the heavy tail. For $x\ge x_m$:
$$S(x)=\left(\frac{x_m}{x}\right)^{\!\alpha},\qquad f(x)=\frac{\alpha\,x_m^{\alpha}}{x^{\alpha+1}},\qquad \E[X]=\frac{\alpha\,x_m}{\alpha-1}\ (\alpha>1).$$

**Lognormal** *(ch12)* — Gyarados, multiplicative growth. $X$ is lognormal iff $\ln X\sim\Normal(\mu,\sigma^{2})$; equivalently $X=e^{Y}$ with $Y\sim\Normal(\mu,\sigma^{2})$.
:::

---

## 4. Insurance Loss & Payment *(ch06, ch13)*

For a ground-up loss $X$ with deductible $d$, policy limit (max covered loss) $u$, and coinsurance factor $\alpha$:

**Ordinary deductible — per-loss payment.**
$$\dplus{X}{d}=\max(X-d,\,0),\qquad \E\!\big[\dplus{X}{d}\big]=\sum_{k\ge d} S(k)\ \text{or}\ \int_d^\infty S(x)\,dx.$$

**Limit (capped loss).**
$$X\wedge u=\min(X,u),\qquad \limexp{X}{u}=\sum_{k=0}^{u-1}S(k)\ \text{or}\ \int_0^u S(x)\,dx.$$

**The budget identity** (split a loss at the cap):
$$\limexp{X}{u}+\E\!\big[\dplus{X}{u}\big]=\E[X].$$

**Full coverage with deductible, limit, and coinsurance.**
$$\E[\text{payment}]=\alpha\big(\limexp{X}{u}-\limexp{X}{d}\big).$$

**Per-loss vs. per-payment.** Per-loss averages over *all* losses (including zeros below $d$); per-payment conditions on a payment occurring, dividing by $S(d)=P(X>d)$:
$$\text{per loss: }\E\!\big[\dplus{X}{d}\big];\qquad \text{per payment: }\E[X-d\mid X>d]=\frac{\E\!\big[\dplus{X}{d}\big]}{S(d)}.$$

> **Trap (ch06):** apply the **deductible before the limit**, never after.

**Inflation.** If losses inflate by a factor $(1+r)$, replace $X$ by $(1+r)X$; deductible and limit stay fixed in dollars, so
$$\E\!\big[((1+r)X-d)_+\big]=(1+r)\,\E\!\Big[\big(X-\tfrac{d}{1+r}\big)_+\Big].$$

**Loss elimination ratio (LER).** The fraction of expected loss removed by a deductible $d$:
$$\text{LER}(d)=\frac{\limexp{X}{d}}{\E[X]}=\frac{\E[X]-\E\!\big[\dplus{X}{d}\big]}{\E[X]}.$$

---

## 5. Multivariate *(ch14–ch17, ch12)*

**Joint, marginal, conditional.** *(ch14)*
$$\text{joint pmf/pdf: }p(x,y)\ \text{or}\ f(x,y)\ge0,\qquad \sum_x\sum_y p=1\ \text{or}\ \iint_S f\,dA=1,\qquad f(x,y)=\frac{\partial^{2}}{\partial x\,\partial y}F(x,y).$$
$$\text{marginals: }f_X(x)=\int f(x,y)\,dy,\quad f_Y(y)=\int f(x,y)\,dx\quad(\text{sum out for pmf}).$$
$$\text{conditional: }f_{Y\mid X}(y\mid x)=\frac{f(x,y)}{f_X(x)},\qquad \E[Y\mid X=x]=\int y\,f_{Y\mid X}(y\mid x)\,dy.$$

**Independence.** *(ch14)* $X\perp Y$ iff the density **factors over a rectangular (product) support**:
$$f(x,y)=f_X(x)\,f_Y(y)\quad\text{on a rectangle.}$$

> **Trap (ch14):** over a **triangular** support $0<x<y<1$, integrate with matched limits — $\int_0^1\!\int_0^y g\,dx\,dy=\int_0^1\!\int_x^1 g\,dy\,dx$ — never as a rectangle.

**Joint moments, covariance, correlation.** *(ch15)*
$$\E[g(X,Y)]=\sum_x\sum_y g\,p(x,y)\ \text{or}\ \iint g\,f(x,y)\,dA,\qquad \E[XY]=\iint xy\,f(x,y)\,dA.$$
$$\Cov(X,Y)=\E[(X-\mu_X)(Y-\mu_Y)]=\E[XY]-\E[X]\E[Y],$$
$$\Cov(X,X)=\Var(X),\qquad \Cov(X,Y)=\Cov(Y,X),\qquad \Cov(aX+b,\,cY+d)=ac\,\Cov(X,Y).$$
$$\Corr(X,Y)=\rho=\frac{\Cov(X,Y)}{\SD(X)\,\SD(Y)},\qquad -1\le\rho\le1,\qquad \Cov(X,Y)=\rho\,\SD(X)\SD(Y).$$

**Variance of a sum / linear combination.** *(ch15)*
$$\Var(X\pm Y)=\Var(X)+\Var(Y)\pm2\Cov(X,Y),$$
$$\Var\!\left(\sum_{i=1}^{n}a_iX_i\right)=\sum_{i=1}^{n}a_i^{2}\Var(X_i)+2\!\!\sum_{1\le i<j\le n}\!\!a_i a_j\Cov(X_i,X_j).$$
Means are always additive (no covariance term): $\E\!\big[\sum a_iX_i+b\big]=\sum a_i\E[X_i]+b.$

> **Independence vs. zero correlation (ch15):** $X\perp Y\Rightarrow\Cov=0\Rightarrow\rho=0$, but $\rho=0\not\Rightarrow$ independence — **except** for **jointly normal** variables, where $\rho=0$ *does* imply independence.

**Sums staying in-family** (independent summands). *(ch15, ch05, ch11)*
$$\Normal(\mu_1,\sigma_1^2)+\Normal(\mu_2,\sigma_2^2)=\Normal(\mu_1+\mu_2,\sigma_1^2+\sigma_2^2);$$
$$\Poisson(\lambda_1)+\Poisson(\lambda_2)=\Poisson(\lambda_1+\lambda_2);\qquad \GammaDist(\alpha_1,\theta)+\GammaDist(\alpha_2,\theta)=\GammaDist(\alpha_1+\alpha_2,\theta);$$
$$\Binom(n_1,p)+\Binom(n_2,p)=\Binom(n_1+n_2,p);\qquad \NegBin(r_1,p)+\NegBin(r_2,p)=\NegBin(r_1+r_2,p).$$
(Gamma requires a **common scale $\theta$**; binomial/neg-binomial a **common $p$**.)

**Conditional & total moments.** *(ch16)*
$$\E[X\mid Y]=g(Y)\ \text{(a random variable)},\qquad \E[X]=\E\big[\E[X\mid Y]\big]\ \text{(law of total expectation)}.$$
$$\Var(X\mid Y)=\E[X^2\mid Y]-(\E[X\mid Y])^2,$$
$$\boxed{\;\Var(X)=\E\big[\Var(X\mid Y)\big]+\Var\big(\E[X\mid Y]\big)\;}\quad\text{(process variance + parameter variance)}.$$

**Compound / mixture $S=\sum_{i=1}^{N}X_i$** ($N$ random, $X_i$ i.i.d. with mean $\mu$, variance $\sigma^2$). *(ch16)*
$$\E[S]=\E[N]\,\mu,\qquad \Var(S)=\E[N]\,\sigma^{2}+\Var(N)\,\mu^{2};\qquad N\sim\Poisson(\lambda)\Rightarrow\Var(S)=\lambda\,\E[X^2]=\lambda(\sigma^2+\mu^2).$$

**Order statistics** (i.i.d. $X_1,\dots,X_n$ with cdf $F$, survival $S$, density $f$). *(ch17)*
$$F_{\max}(x)=[F(x)]^{n},\qquad f_{\max}(x)=n[F(x)]^{n-1}f(x);$$
$$S_{\min}(x)=[S(x)]^{n},\qquad F_{\min}(x)=1-[S(x)]^{n},\qquad f_{\min}(x)=n[S(x)]^{n-1}f(x);$$
$$f_{X_{(k)}}(x)=\frac{n!}{(k-1)!\,(n-k)!}\,[F(x)]^{k-1}[1-F(x)]^{n-k}f(x).$$
For $n$ i.i.d. $\Unif(0,1)$: $\E[X_{(k)}]=\dfrac{k}{n+1}$ (so $\E[\min]=\tfrac{1}{n+1}$, $\E[\max]=\tfrac{n}{n+1}$).

> **Trap (ch17):** the max's cdf is $[F(x)]^n$, **not** $n\,F(x)$.

**Minimum of independent exponentials** (rate $\lambda_i$, i.e. mean $1/\lambda_i$). *(ch17)*
$$\min_i X_i\sim\Expo\!\Big(\text{rate }\textstyle\sum_i\lambda_i\Big),\qquad S_{\min}(x)=e^{-(\sum_i\lambda_i)x},\qquad \E[\min]=\frac{1}{\sum_i\lambda_i}.$$
($n$ i.i.d. exponentials of mean $\theta$: $\min$ has mean $\theta/n$.)

**System reliability.** *(ch17)*
$$R_{\text{series}}(t)=P(\min_i X_i>t)=\prod_i S_i(t),\qquad R_{\text{parallel}}(t)=1-P(\max_i X_i\le t)=1-\prod_i F_i(t).$$

**Normal & the Central Limit Theorem.** *(ch12)* If $X\sim\Normal(\mu,\sigma^{2})$,
$$Z=\frac{X-\mu}{\sigma}\sim\Normal(0,1),\qquad P(X\le x)=\Phi\!\left(\frac{x-\mu}{\sigma}\right),\qquad \Phi(-z)=1-\Phi(z).$$
**68–95–99.7:** $\approx68\%,95\%,99.7\%$ within $\pm1,\pm2,\pm3$ standard deviations.
**CLT** (i.i.d. mean $\mu$, variance $\sigma^2$, large $n$):
$$S_n=\sum X_i\ \overset{\text{approx}}{\sim}\ \Normal(n\mu,\,n\sigma^{2}),\qquad \bar X\ \overset{\text{approx}}{\sim}\ \Normal\!\left(\mu,\,\tfrac{\sigma^{2}}{n}\right),$$
$$Z=\frac{S_n-n\mu}{\sigma\sqrt{n}}\quad\text{(sum)},\qquad Z=\frac{\bar X-\mu}{\sigma/\sqrt{n}}\quad\text{(mean)}.$$
**Table interpolation:** $\Phi(z)\approx\Phi(z_0)+\dfrac{z-z_0}{z_1-z_0}\big[\Phi(z_1)-\Phi(z_0)\big]$. Useful pegs: $\Phi(1.28)\approx0.90$, $\Phi(1.645)\approx0.95$, $\Phi(1.96)\approx0.975$, $\Phi(2.33)\approx0.99$.

**Continuity correction** (integer $X$ approximated by normal $Y$). *(ch12)*
$$P(X\ge a)\approx P(Y>a-0.5),\qquad P(X\le b)\approx P(Y<b+0.5),$$
$$P(X=k)\approx P(k-0.5<Y<k+0.5),\qquad P(a\le X\le b)\approx P(a-0.5<Y<b+0.5).$$

---

## 6. Shortcut Catalog *(ch19 finale)*

The seven moves that turn a six-minute problem into a one-line answer.

**1. The gamma (Master-Ball) integral.** *(ch08, ch11)*
$$\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx=\Gamma(\alpha)\,\theta^{\alpha},\qquad \Gamma(n)=(n-1)!,\qquad \Gamma\!\left(\tfrac12\right)=\sqrt{\pi},\qquad \Gamma(\alpha+1)=\alpha\,\Gamma(\alpha).$$
Recognize any "$x^{\alpha-1}e^{-x/\theta}$" integrand and read off the answer — no integration by parts.

**2. The Darth-Vader (survival) expectation.** *(ch03, ch10)* When handed $S$ or $F$ instead of the density,
$$\E[X]=\sum_{k\ge0}S(k)\quad\text{or}\quad\int_0^\infty S(x)\,dx\qquad(X\ge0).$$

**3. MGF kernel recognition.** *(ch03, ch05, ch11–ch12)* Match a given $M_X(t)$ to a card above to read off the distribution and its moments; or use $\E[X^n]=M_X^{(n)}(0)$ directly. (Independent sum $\Rightarrow$ MGFs **multiply**.)

**4. Memorylessness.** *(ch05, ch11)* For geometric or exponential, condition away the past: $P(X>s+t\mid X>s)=P(X>t)$. The remaining wait has the *same* distribution.

**5. Poisson mean $=$ variance.** *(ch05)* If $\E[X]=\Var(X)$ for a count, suspect $\Poisson(\lambda)$ with $\lambda$ equal to both.

**6. Binomial $\to$ Poisson.** *(ch05)* Large $n$, small $p$: $\Binom(n,p)\approx\Poisson(np)$ — replace a messy $\binom{n}{x}$ with a clean $e^{-\lambda}\lambda^x/x!$.

**7. Continuity correction ($\pm0.5$).** *(ch12)* Before standardizing a *discrete* sum against the normal, widen the region by $0.5$ to the outer edge of every bar kept.

> **Sanity reflexes.** $0\le P\le1$; the mean lies between the smallest and largest possible value; $\Var\ge0$ (so $\E[X^2]\ge(\E[X])^2$); $|\rho|\le1$; a pmf/pdf integrates to $1$. If any fails, a number is wrong — find it before moving on.
