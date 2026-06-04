<!--
  appendix: a_formula_sheet
  status: complete
-->

# Appendix A — Master Formula Sheet & Shortcut Catalog

*One page to carry into the final week. Everything here is derived in the chapters; this is the compression, not the teaching. The Recognition Cue is printed beside each shortcut so you can pattern-match at exam speed.*

## A.1 Probability foundations

$$P(A\cup B)=P(A)+P(B)-P(A\cap B),\qquad P(A^{c})=1-P(A).$$
$$P(A\given B)=\frac{P(A\cap B)}{P(B)},\qquad P(A\cap B)=P(A\given B)\,P(B).$$

**Independence:** $P(A\cap B)=P(A)P(B)\iff P(A\given B)=P(A)$.

**Law of total probability** (partition $B_1,\dots,B_n$):
$$P(A)=\sum_{i}P(A\given B_i)\,P(B_i).$$

**Bayes' theorem:**
$$P(B_k\given A)=\frac{P(A\given B_k)\,P(B_k)}{\sum_{i}P(A\given B_i)\,P(B_i)}.$$

**Counting:** permutations $\dfrac{n!}{(n-r)!}$; combinations $\dbinom{n}{r}=\dfrac{n!}{r!\,(n-r)!}$.

## A.2 Random-variable machinery

| Object | Discrete | Continuous |
|---|---|---|
| Normalization | $\sum_x p(x)=1$ | $\int f(x)\,dx=1$ |
| CDF | $F(x)=\sum_{t\le x}p(t)$ | $F(x)=\int_{-\infty}^{x}f(t)\,dt,\ f=F'$ |
| Survival | $S(x)=1-F(x)=P(X>x)$ | $S(x)=1-F(x)$ |
| Expectation | $\E[X]=\sum_x x\,p(x)$ | $\E[X]=\int x\,f(x)\,dx$ |
| LOTUS | $\E[g(X)]=\sum_x g(x)\,p(x)$ | $\E[g(X)]=\int g(x)\,f(x)\,dx$ |

**Variance:** $\Var(X)=\E[X^2]-\big(\E[X]\big)^2,\qquad \SD(X)=\sqrt{\Var(X)},\qquad \mathrm{CV}=\dfrac{\SD(X)}{\E[X]}.$

**Linearity / scaling:** $\E[aX+b]=a\,\E[X]+b,\qquad \Var(aX+b)=a^2\,\Var(X).$

> *Beware:* $\E[g(X)]\ne g(\E[X])$ whenever $g$ curves — e.g. $\E[1/X]\ne 1/\E[X]$, $\E[e^X]\ne e^{\E[X]}$.

## A.3 Multivariate

$$\E[aX+bY]=a\,\E[X]+b\,\E[Y]\quad\text{(always).}$$
$$\Cov(X,Y)=\E[XY]-\E[X]\E[Y],\qquad \Corr(X,Y)=\frac{\Cov(X,Y)}{\SD(X)\,\SD(Y)}\in[-1,1].$$
$$\Var(aX+bY)=a^2\Var(X)+b^2\Var(Y)+2ab\,\Cov(X,Y).$$

Independent $\Rightarrow\Cov=0$ and $\Var(X+Y)=\Var(X)+\Var(Y)$ (converse false).

**Conditional & double expectation (Tier A):**
$$\E[X]=\E\big[\,\E[X\given Y]\,\big]\quad\text{(tower / Adam's law),}$$
$$\Var(X)=\E\big[\Var(X\given Y)\big]+\Var\big(\E[X\given Y]\big)\quad\text{(EVVE / Eve's law).}$$

**Joint:** marginal $f_X(x)=\int f(x,y)\,dy$; conditional $f_{X\given Y}(x\given y)=\dfrac{f(x,y)}{f_Y(y)}$; independence $\iff f(x,y)=f_X(x)f_Y(y)$.

## A.4 Insurance / pricing layer

Deductible $d$, limit $u$, payment per loss on a loss $X\ge0$:
$$Y=\dplus{X}{d}=\max(X-d,0),\qquad \E[Y]=\limexp{X}{\infty}-\limexp{X}{d}.$$
$$\E\!\left[\dplus{X}{d}\right]=\int_d^\infty S(x)\,dx\quad(X\ge0).$$
Limited expected value: $\limexp{X}{u}=\displaystyle\int_0^u S(x)\,dx$ for $X\ge0$.

## A.5 The shortcut catalog (the Master Balls)

::: trainers-tip
**SHORTCUT 1 — The Gamma (Master-Ball) Integral**

$$\boxed{\;\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx=\Gamma(\alpha)\,\theta^{\alpha},\qquad \Gamma(n)=(n-1)!,\quad \Gamma\!\left(\tfrac12\right)=\sqrt{\pi}.\;}$$

Equivalently, with the power on $x$ written directly: $\displaystyle\int_0^\infty x^{k}e^{-x/\theta}\,dx=\Gamma(k+1)\,\theta^{k+1}=k!\,\theta^{k+1}.$

*Recognition cue:* a power of $x$ times a decaying exponential, swept $0\to\infty$. **Set $\alpha=(\text{power on }x)+1$**, then write the answer in one line — no integration by parts. Off-by-one on $\alpha$ is the most-punished slip.
:::

::: trainers-tip
**SHORTCUT 2 — The Darth Vader (Survival-Function) Rule**

For a **nonnegative** $X\ge0$:
$$\boxed{\;\E[X]=\int_0^\infty S(x)\,dx=\int_0^\infty P(X>x)\,dx,\qquad \E[X^k]=\int_0^\infty k\,x^{k-1}S(x)\,dx.\;}$$
Discrete analog for $X\in\{0,1,2,\dots\}$: $\displaystyle \E[X]=\sum_{k=0}^{\infty}P(X>k)=\sum_{k=1}^{\infty}P(X\ge k).$

*Recognition cue:* you are handed $S(x)$ (or only the cdf $F$) and asked for a mean, and $X\ge0$. Integrate the survival curve directly — skip recovering the density. For bounded support, integrate **only over the support**.
:::

::: trainers-tip
**SHORTCUT 3 — MGF Kernel Recognition**

$$M_X(t)=\E[e^{tX}],\qquad \E[X^n]=M_X^{(n)}(0),\qquad M_{aX+b}(t)=e^{bt}M_X(at),\qquad M_{X+Y}(t)=M_X(t)M_Y(t)\ \text{(indep.).}$$

By **uniqueness**, matching the kernel *identifies* the distribution — read parameters off the labeled slot:

| Kernel | Family | Mean | Variance |
|---|---|---|---|
| $(1-\theta t)^{-\alpha}$ | $\GammaDist(\alpha,\theta)$ | $\alpha\theta$ | $\alpha\theta^2$ |
| $(1-\theta t)^{-1}$ | $\Expo(\theta)$ | $\theta$ | $\theta^2$ |
| $e^{\lambda(e^{t}-1)}$ | $\Poisson(\lambda)$ | $\lambda$ | $\lambda$ |
| $(1-p+pe^{t})^{n}$ | $\Binom(n,p)$ | $np$ | $npq$ |
| $e^{\mu t+\sigma^2 t^2/2}$ | $\Normal(\mu,\sigma^2)$ | $\mu$ | $\sigma^2$ |

*Recognition cue:* "given the MGF," an $e^{tX}$ expectation, or a factored MGF matching a family above. **Normalize to the standard kernel before reading $\alpha,\theta$** ($\theta$ is the coefficient of $t$; $\alpha$ is the positive exponent). Mis-slotting flips the mean.
:::

::: trainers-tip
**SHORTCUT 4 — Memorylessness**

$$\boxed{\;P(X>s+t\given X>s)=P(X>t).\;}$$
Continuous: the **exponential** is the only continuous law with it — given it has lasted $s$, the remaining wait is a fresh $\Expo(\theta)$, expected remaining $=\theta$. Discrete: the **geometric** is the only discrete law with it.

*Recognition cue:* "given it has already lasted $s$ …" with an exponential or geometric. **Reset the clock** — do not subtract; the elapsed time is irrelevant. (Expected remaining is the *full* mean, not mean $-\,s$.)
:::

::: trainers-tip
**SHORTCUT 5 — The Continuity Correction**

Approximating a **discrete** count (binomial, Poisson) by the normal, shift the integer boundary by a half-unit *toward the values you want to include*:

| Discrete event | Corrected normal boundary |
|---|---|
| $P(X\ge a)$ | $P\!\big(Z>\tfrac{(a-0.5)-\mu}{\sigma}\big)$ |
| $P(X>a)$ | $P\!\big(Z>\tfrac{(a+0.5)-\mu}{\sigma}\big)$ |
| $P(X\le a)$ | $P\!\big(Z<\tfrac{(a+0.5)-\mu}{\sigma}\big)$ |
| $P(X<a)$ | $P\!\big(Z<\tfrac{(a-0.5)-\mu}{\sigma}\big)$ |
| $P(X=a)$ | $P\!\big(\tfrac{(a-0.5)-\mu}{\sigma}<Z<\tfrac{(a+0.5)-\mu}{\sigma}\big)$ |

*Recognition cue:* a normal approximation to a binomial or Poisson **count**. Slide $\ge$/$\le$ to include the boundary integer's whole bar; slide $>$/$<$ to exclude it. The half-unit is worth real points — exams list the uncorrected answer as a distractor.
:::

## A.6 The Central Limit Theorem

For i.i.d. $X_1,\dots,X_n$ with mean $\mu$, variance $\sigma^2$:
$$\sum_{i=1}^{n}X_i\ \dot\sim\ \Normal(n\mu,\,n\sigma^2),\qquad \bar X\ \dot\sim\ \Normal\!\left(\mu,\,\frac{\sigma^2}{n}\right),\qquad Z=\frac{\sum X_i-n\mu}{\sigma\sqrt{n}}.$$
Apply Shortcut 5 when the $X_i$ are integer counts.

## A.7 Standard-normal quick reference

$$\Phi(-z)=1-\Phi(z),\qquad P(\mu-k\sigma<X<\mu+k\sigma)=2\Phi(k)-1.$$
$$\Phi(1.282)=0.90,\quad \Phi(1.645)=0.95,\quad \Phi(1.960)=0.975,\quad \Phi(2.326)=0.99.$$
68–95–99.7 rule: $\approx68\%$ within $1\sigma$, $95\%$ within $2\sigma$, $99.7\%$ within $3\sigma$. (Full table: Appendix C. Per-family facts: Appendix B.)
