<!--
  appendix: b_distribution_tables
  status: complete
-->

# Appendix B — Distribution Reference Tables

*Every in-scope family on one card: support, pmf/pdf, cdf, mean, variance, MGF, and the Recognition Cue that triggers it. All values match the in-chapter Pokédex Entries (Ch 8 discrete, Ch 9 continuous). Out-of-scope families are flagged as **enrichment** — know the name, not the formula.*

## B.1 Discrete distributions

### Bernoulli — $X\sim\operatorname{Bernoulli}(p)$
- **Support:** $X\in\{0,1\}$, with $q=1-p$.
- **pmf:** $p(1)=p,\ p(0)=q$.
- **cdf:** $F(0)=q,\ F(1)=1$.
- **Mean / Var:** $\E[X]=p,\quad \Var(X)=pq$.
- **MGF:** $M_X(t)=q+pe^{t}$.
- **Recognition cue:** a **single** trial with two outcomes (the $n=1$ binomial). Then ask "how are trials combined?" to route to the next families.

### Binomial — $X\sim\Binom(n,p)$
- **Support:** $X\in\{0,1,\dots,n\}$.
- **pmf:** $p(k)=\dbinom{n}{k}p^{k}q^{\,n-k}$.
- **cdf:** $F(k)=\sum_{j=0}^{k}\dbinom{n}{j}p^{j}q^{\,n-j}$ (no closed form).
- **Mean / Var:** $\E[X]=np,\quad \Var(X)=npq$ (so $\Var<\E$ always).
- **MGF:** $M_X(t)=(q+pe^{t})^{n}$.
- **Recognition cue:** "out of $n$ trials," a **fixed** $n$ independent attempts, count the successes.

### Geometric — $X\sim\Geom(p)$ *(trials convention: $X=$ trial of first success)*
- **Support:** $X\in\{1,2,3,\dots\}$.
- **pmf:** $p(k)=q^{\,k-1}p$.
- **Survival / cdf:** $P(X>m)=q^{m}$, so $F(m)=1-q^{m}$.
- **Mean / Var:** $\E[X]=\dfrac{1}{p},\quad \Var(X)=\dfrac{q}{p^{2}}$.
- **MGF:** $M_X(t)=\dfrac{pe^{t}}{1-qe^{t}}\ \ (t<-\ln q)$.
- **Failures convention** ($Y=X-1\in\{0,1,\dots\}$): $p(k)=q^{k}p$, $\E[Y]=\dfrac{q}{p}$, **same** $\Var=\dfrac{q}{p^2}$, $M_Y(t)=\dfrac{p}{1-qe^{t}}$.
- **Memoryless:** $P(X>m+n\given X>m)=P(X>n)$ — the only discrete law with it.
- **Recognition cue:** "how many tries until the first success." **State your convention** (mean shifts by $1$; variance is identical).

### Negative binomial — $X\sim\NegBin(r,p)$ *(failures before the $r$-th success)*
- **Support:** $X\in\{0,1,2,\dots\}$.
- **pmf:** $p(k)=\dbinom{k+r-1}{k}p^{r}q^{k}$.
- **Mean / Var:** $\E[X]=\dfrac{rq}{p},\quad \Var(X)=\dfrac{rq}{p^{2}}$.
- **MGF:** $M_X(t)=\left(\dfrac{p}{1-qe^{t}}\right)^{r}$.
- **Recognition cue:** "until the $r$-th success," "how many attempts to collect $r$ of them." Sum of $r$ independent geometrics; $r=1$ is the geometric (failures version).

### Hypergeometric — $X\sim\HyperGeom(N,K,n)$
- **Support:** $\max(0,n-(N-K))\le X\le\min(n,K)$.
- **pmf:** $p(k)=\dfrac{\dbinom{K}{k}\dbinom{N-K}{n-k}}{\dbinom{N}{n}}$.
- **Mean / Var:** $\E[X]=n\dfrac{K}{N},\quad \Var(X)=n\dfrac{K}{N}\dfrac{N-K}{N}\cdot\underbrace{\dfrac{N-n}{N-1}}_{\text{finite-pop. correction}}$.
- **MGF:** no useful closed form (not exam-tested).
- **Recognition cue:** "**without replacement**," "draw $n$ from a fixed pool of $N$ containing exactly $K$." If $N$ is far larger than $n$, the binomial ($p=K/N$) approximates it.

### Poisson — $X\sim\Poisson(\lambda)$
- **Support:** $X\in\{0,1,2,\dots\}$ (no upper bound).
- **pmf:** $p(k)=\dfrac{e^{-\lambda}\lambda^{k}}{k!}$.
- **cdf:** $F(k)=\sum_{j=0}^{k}\dfrac{e^{-\lambda}\lambda^{j}}{j!}$ (no closed form).
- **Mean / Var:** $\E[X]=\Var(X)=\lambda$ (its fingerprint).
- **MGF:** $M_X(t)=e^{\lambda(e^{t}-1)}$.
- **Power tools:** additivity $\Poisson(\lambda_1)+\Poisson(\lambda_2)=\Poisson(\lambda_1+\lambda_2)$; $\Binom(n,p)\approx\Poisson(np)$ for large $n$, small $p$; thinning keeps a $\Poisson(\mu)$ stream w.p. $p$ to give $\Poisson(\mu p)$.
- **Recognition cue:** "per minute / year / square mile," a steady rate $\lambda$, a count with no natural ceiling. **Scale $\lambda=\text{rate}\times\text{window}$.**

### Discrete uniform — $X$ uniform on $\{1,2,\dots,m\}$
- **Support:** $X\in\{1,2,\dots,m\}$.
- **pmf:** $p(k)=\dfrac{1}{m}$.
- **cdf:** $F(k)=\dfrac{k}{m}$.
- **Mean / Var:** $\E[X]=\dfrac{m+1}{2},\quad \Var(X)=\dfrac{m^{2}-1}{12}$.
- **MGF:** $M_X(t)=\dfrac{e^{t}(1-e^{mt})}{m(1-e^{t})}$.
- **Recognition cue:** "equally likely," a fair $m$-faced die / spinner / labelled ticket.

## B.2 Continuous distributions

### Continuous uniform — $X\sim\Unif(a,b)$
- **Support:** $a\le x\le b$.
- **pdf / cdf:** $f(x)=\dfrac{1}{b-a},\qquad F(x)=\dfrac{x-a}{b-a}$.
- **Mean / Var:** $\E[X]=\dfrac{a+b}{2},\quad \Var(X)=\dfrac{(b-a)^{2}}{12}$.
- **MGF:** $M_X(t)=\dfrac{e^{tb}-e^{ta}}{t(b-a)}\ (t\ne0)$.
- **Recognition cue:** "equally likely anywhere between," "chosen at random from the interval." Probability is a ratio of lengths; mean is the midpoint.

### Exponential — $X\sim\Expo(\theta)$ *(mean parametrization; rate $\lambda=1/\theta$)*
- **Support:** $x>0$.
- **pdf / cdf / survival:** $f(x)=\dfrac{1}{\theta}e^{-x/\theta},\quad F(x)=1-e^{-x/\theta},\quad S(x)=e^{-x/\theta}$.
- **Mean / Var:** $\E[X]=\theta,\quad \Var(X)=\theta^{2}$.
- **MGF:** $M_X(t)=\dfrac{1}{1-\theta t}\ \ \left(t<\tfrac1\theta\right)$.
- **Memoryless:** $P(X>s+t\given X>s)=P(X>t)$; the minimum of independent exponentials has the **rates added**.
- **Recognition cue:** "time until," "time between," "memoryless," "constant failure/hazard rate." Watch whether you are given mean $\theta$ or rate $\lambda$. It is $\GammaDist(1,\theta)$.

### Gamma — $X\sim\GammaDist(\alpha,\theta)$
- **Support:** $x>0$.
- **pdf:** $f(x)=\dfrac{1}{\Gamma(\alpha)\theta^{\alpha}}x^{\alpha-1}e^{-x/\theta}$.
- **cdf:** no elementary closed form for general $\alpha$ (integer $\alpha$: a finite Poisson-type sum).
- **Mean / Var:** $\E[X]=\alpha\theta,\quad \Var(X)=\alpha\theta^{2}$.
- **MGF:** $M_X(t)=(1-\theta t)^{-\alpha}\ \ \left(t<\tfrac1\theta\right)$.
- **Master-Ball integral:** $\displaystyle\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx=\Gamma(\alpha)\theta^{\alpha}$, with $\Gamma(n)=(n-1)!$, $\Gamma(\tfrac12)=\sqrt{\pi}$.
- **Recognition cue:** "time until the $\alpha$-th event," "sum of $\alpha$ exponential waits," or a density $\propto x^{\alpha-1}e^{-x/\theta}$. $\alpha=1$ is the exponential.

### Beta — $X\sim\BetaDist(\alpha,\beta)$
- **Support:** $0<x<1$.
- **pdf:** $f(x)=\dfrac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}x^{\alpha-1}(1-x)^{\beta-1}$.
- **cdf:** the (regularized incomplete-beta) integral; no elementary closed form for general $\alpha,\beta$.
- **Mean / Var:** $\E[X]=\dfrac{\alpha}{\alpha+\beta},\quad \Var(X)=\dfrac{\alpha\beta}{(\alpha+\beta)^{2}(\alpha+\beta+1)}$.
- **MGF:** no useful closed form (a confluent hypergeometric series — not exam-tested).
- **Recognition cue:** "a fraction between $0$ and $1$," "a random proportion/percentage," or a density $\propto x^{\alpha-1}(1-x)^{\beta-1}$. Mean is the weight ratio; symmetric only when $\alpha=\beta$. $\BetaDist(1,1)=\Unif(0,1)$.

### Normal — $X\sim\Normal(\mu,\sigma^{2})$
- **Support:** $-\infty<x<\infty$.
- **pdf:** $f(x)=\dfrac{1}{\sigma\sqrt{2\pi}}\exp\!\left[-\dfrac{(x-\mu)^{2}}{2\sigma^{2}}\right]$.
- **cdf:** $F(x)=\Phi\!\left(\dfrac{x-\mu}{\sigma}\right)$ (no elementary form; use the table, Appendix C).
- **Mean / Var:** $\E[X]=\mu,\quad \Var(X)=\sigma^{2}$ — note the **second parameter slot is the variance**.
- **MGF:** $M_X(t)=\exp\!\left(\mu t+\tfrac12\sigma^{2}t^{2}\right)$.
- **Standardize:** $Z=\dfrac{X-\mu}{\sigma}\sim\Normal(0,1)$; $\Phi(-z)=1-\Phi(z)$.
- **Recognition cue:** "bell curve," "normally distributed," "average of many" (CLT), or a $\mu,\sigma,\Phi$-table problem. Memorize 68–95–99.7.

## B.3 Summary grid (mean / variance / MGF)

| Family | Mean | Variance | MGF |
|---|---|---|---|
| $\operatorname{Bernoulli}(p)$ | $p$ | $pq$ | $q+pe^{t}$ |
| $\Binom(n,p)$ | $np$ | $npq$ | $(q+pe^{t})^{n}$ |
| $\Geom(p)$ (trials) | $1/p$ | $q/p^{2}$ | $pe^{t}/(1-qe^{t})$ |
| $\NegBin(r,p)$ (failures) | $rq/p$ | $rq/p^{2}$ | $\big(p/(1-qe^{t})\big)^{r}$ |
| $\HyperGeom(N,K,n)$ | $nK/N$ | $n\tfrac{K}{N}\tfrac{N-K}{N}\tfrac{N-n}{N-1}$ | — |
| $\Poisson(\lambda)$ | $\lambda$ | $\lambda$ | $e^{\lambda(e^{t}-1)}$ |
| Discrete unif. $\{1,\dots,m\}$ | $(m+1)/2$ | $(m^{2}-1)/12$ | — |
| $\Unif(a,b)$ | $(a+b)/2$ | $(b-a)^{2}/12$ | $\tfrac{e^{tb}-e^{ta}}{t(b-a)}$ |
| $\Expo(\theta)$ | $\theta$ | $\theta^{2}$ | $(1-\theta t)^{-1}$ |
| $\GammaDist(\alpha,\theta)$ | $\alpha\theta$ | $\alpha\theta^{2}$ | $(1-\theta t)^{-\alpha}$ |
| $\BetaDist(\alpha,\beta)$ | $\tfrac{\alpha}{\alpha+\beta}$ | $\tfrac{\alpha\beta}{(\alpha+\beta)^{2}(\alpha+\beta+1)}$ | — |
| $\Normal(\mu,\sigma^{2})$ | $\mu$ | $\sigma^{2}$ | $\exp(\mu t+\tfrac12\sigma^{2}t^{2})$ |

## B.4 Enrichment families (out of scope — name only)

These appear in later actuarial exams but are **not tested on Exam P**. Recognize the name; do not memorize the formulas.

- **Lognormal** — $\ln X\sim\Normal(\mu,\sigma^2)$; right-skewed positive values (asset prices, claim sizes).
- **Pareto** — heavy-tailed positive losses; the survival $S(x)=\big(\tfrac{\theta}{\theta+x}\big)^{\alpha}$ tail seen in Ch 7's Darth Vader ramp.
- **Weibull** — exponential with a power inside the exponent; flexible failure/hazard modeling.
- **Chi-square** (written $\text{chi}^2_k$) — the special case $\GammaDist(\alpha=k/2,\theta=2)$; arises from sums of squared normals.
