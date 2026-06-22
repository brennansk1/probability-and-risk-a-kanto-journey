<!--
  file: appendix_g_glossary
  kind: appendix
  letter: G
  title: Glossary — Kanto term ↔ formal term, and Exam P formal definitions
  purpose: (1) a two-column key mapping every in-world coinage to its standard actuarial/probability term; (2) an alphabetized formal glossary of ~60 core Exam P terms with concise definitions
  sources: ch00–ch19 (in-world coinages), syllabus/outcomes.yaml, book/mathjax-preamble.md, MASTER_PLAN_V3 §23
  plan: MASTER_PLAN_V3 §23
-->

# Appendix G — Glossary {.type-normal}

> **What this is.** Two things in one appendix. **Part 1** is a lookup key: every in-world Kanto coinage this book uses, mapped to the standard actuarial or probability term it stands for. If you see "Darth-Vader rule" in a chapter and want the textbook name, this table has it. **Part 2** is a compact formal glossary of roughly sixty core Exam P terms, alphabetized, with precise one-to-two-sentence definitions. Use Part 1 while you read; use Part 2 as a quick-reference on anything that feels slightly fuzzy before the exam.

---

## Part 1 — Kanto Term ↔ Formal Term

The left column is the in-world name exactly as it appears in the book. The right column is the standard probability or actuarial term — the word an Exam P problem will use.

| Kanto term (in-world) | Formal term |
|---|---|
| **The Indigo Plateau** | SOA Exam P (the goal of the whole journey) |
| **Eight Gym Badges** | The eight thematic blocks of the Exam P syllabus |
| **Trainer Rank** (Rookie → Champion-ready) | Self-assessment level; a progress ladder tied to badges earned and mock exams cleared |
| **Pokédex Entry** (blue box) | Definition / summary box — a sealed statement of a concept's formula, meaning, and recognition cue |
| **Trainer's Tip** (yellow box) | Technique reminder — a practical shorthand or calculator workflow |
| **Transmission Intercepted — Team Rocket's Trap** (red box) | Common error analysis — the single most tempting wrong move, named and dissected |
| **From Kanto to the Real World** (green box) | Real-world actuarial application — the bridge from the in-world scenario to practice |
| **Now Playing** (purple box) | Episode cross-reference — ties the chapter's story to the Indigo League anime |
| **Beyond the Syllabus** (grey box) | Enrichment / off-syllabus material (not tested on Exam P) |
| **Concept Gate** ("Do you already own this?") | Test-out check — a short diagnostic at the top of each concept; pass it and skip ahead |
| **Chapter Test-Out Gate** | Chapter-level test-out check — pass and skip the entire chapter |
| **Gym Battle** (capstone problem) | Boss-level exam-difficulty problem that closes a chapter's questline |
| **Route Trainers** (problem tier) | Routine-method practice problems — lightly scaffolded warmups |
| **Elite Challenge** (problem tier) | Optional post-chapter stretch problems — harder than exam difficulty |
| **Gym Rematch** | Remediation pointer — tells you exactly where to return if you missed a specific sub-skill |
| **The nine-beat lesson arc** | Structured concept presentation: plain sentence → instance → reasoning → wrong idea → notation → derivation → difficulty ramp → picture → Pokédex Entry |
| **Professor's Path** | The rigorous derivation-first explanation of a technique (the "why") |
| **Trainer's Path** | The fast calculator or bookkeeping workflow for the same technique (the "how") |
| **Gary's Rival Trap** (problem label) | Plausible-but-wrong claim to audit — you find the correct answer and name Gary's error |
| **Audit** (problem label) | Error-finding problem — detect and correct a given wrong calculation |
| **The journey convention** | The book's deliberate reordering of gym badges to follow mathematical dependency rather than show canon |
| **Darth-Vader rule** | Survival-function shortcut for the mean: $\E[X]=\sum_{k\ge0}S(k)$ (discrete) or $\E[X]=\int_0^\infty S(x)\,dx$ (continuous) |
| **The bell of thousands** | Central Limit Theorem (CLT) — the bell curve that emerges when many independent quantities are averaged |
| **The Master Ball of integrals** | Gamma integral identity: $\displaystyle\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx=\Gamma(\alpha)\,\theta^{\alpha}$ |
| **HM: Calculus** (ch08) | Calculus prerequisite toolkit — differentiation, improper integrals, integration by parts, the gamma identity |
| **1-Var Stats** (calculator workflow) | TI-30XS MultiView data-list workflow for computing $\E[X]$ and $\Var(X)$ from a pmf |
| **The budget identity** | $\E[X\wedge u]+\E[(X-u)_+]=\E[X]$ — the additive decomposition of a loss into its limited portion and its excess |
| **Per-loss expected payment** | $\E[Y_L]=\E[(X-d)_+]$ — expected payment per policy sold, including policies that pay zero |
| **Per-payment expected payment** | $\E[Y_P]=\E[Y_L]/P(X>d)$ — expected payment given that the loss actually exceeds the deductible |
| **Pushing $E$ through a square** | The error of writing $\E[X^2]=(\E[X])^2$ (false for nonlinear functions; Jensen's inequality governs) |
| **Team Rocket's order-of-operations mistake** | Applying the policy limit before the deductible instead of after — systematically mispricing coverage |
| **The four-row table** | Compact bookkeeping table for discrete deductible/limit problems: $k$, $p(k)$, $S(k)$, $(k-d)_+$ |
| **Oak's Briefing** | Learning outcomes and test-out gate section at the top of each chapter |
| **Badge Earned** | Chapter-closing mastery checklist and rank update |
| **Questline** | The chapter's problem set framed as a connected narrative mission |
| **The bell-shaped mascot** (#35 Clefairy) | Normal distribution — the bell-shaped, symmetric density |
| **The Stacked-Wait Pokémon** (Magneton, ch11) | Gamma distribution — a sum of $\alpha$ independent exponential waiting times |
| **The Forgetful Timer** (Electrode, ch11) | Exponential distribution — memoryless continuous waiting time |
| **The Swarm-Count Pokémon** (Gastly, ch05) | Poisson distribution — count of rare events over a fixed window |
| **The Equal-Probability Transformer** (Ditto, ch03/ch11) | Uniform distribution (discrete or continuous) — all values equally likely |

---

## Part 2 — Formal Glossary

Terms are alphabetized by their standard name. Inline math uses the book's notation: $\E[\cdot]$ expectation, $\Var(\cdot)$ variance, $S(\cdot)$ survival function, $F(\cdot)$ cdf, $f(\cdot)$ density, $p(\cdot)$ pmf.

---

**Axioms of probability.** The three Kolmogorov axioms that define a probability measure $P$ on a sample space $\Omega$: (1) $P(A)\ge 0$ for all events $A$; (2) $P(\Omega)=1$; (3) $P\!\left(\bigcup_i A_i\right)=\sum_i P(A_i)$ when the $A_i$ are mutually exclusive. All other probability rules follow from these three.

**Bayes' theorem.** A rule for inverting conditional probabilities: given a partition $B_1,\dots,B_n$ of $\Omega$ and an event $A$ with $P(A)>0$,
$$P(B_j\mid A)=\frac{P(B_j)\,P(A\mid B_j)}{\displaystyle\sum_i P(B_i)\,P(A\mid B_i)}.$$
The numerator is the prior probability of $B_j$ times the likelihood of $A$ under $B_j$; the denominator is the total probability of $A$.

**Beta distribution.** A continuous distribution on $(0,1)$ with two positive shape parameters $\alpha,\beta$: $f(x)\propto x^{\alpha-1}(1-x)^{\beta-1}$. Mean $\alpha/(\alpha+\beta)$; variance $\alpha\beta/[(\alpha+\beta)^2(\alpha+\beta+1)]$. Used to model random proportions or probabilities.

**Binomial distribution, $\Binom(n,p)$.** The count of successes in $n$ independent Bernoulli trials, each with success probability $p$. $p(k)=\binom{n}{k}p^k(1-p)^{n-k}$, $\E[X]=np$, $\Var(X)=np(1-p)$.

**CDF (cumulative distribution function).** $F(x)=P(X\le x)$. For a discrete $X$, $F(k)=\sum_{j\le k}p(j)$; for a continuous $X$, $F(x)=\int_{-\infty}^x f(t)\,dt$. Right-continuous, non-decreasing, with $F(-\infty)=0$ and $F(\infty)=1$.

**Central Limit Theorem (CLT).** If $X_1,\dots,X_n$ are i.i.d. with mean $\mu$ and variance $\sigma^2$, then for large $n$ the sample mean $\bar X$ is approximately $\mathcal{N}(\mu,\sigma^2/n)$ and the sum $S_n=\sum X_i$ is approximately $\mathcal{N}(n\mu,n\sigma^2)$. The parent distribution's shape is irrelevant; only $\mu$, $\sigma^2$, and $n$ survive.

**Coefficient of variation (CV).** $\SD(X)/\E[X]=\sigma/\mu$ — a dimensionless measure of relative spread. Useful for comparing variability across distributions with different scales; requires $\E[X]>0$.

**Coinsurance.** A factor $\alpha\in(0,1]$ by which the insurer's share of the net loss (after deductible and before limit) is scaled. If the covered layer is $L$, the payment is $\alpha L$.

**Compound distribution.** A distribution for a random sum $S=X_1+\cdots+X_N$ where both the count $N$ and the individual terms $X_i$ are random. $\E[S]=\E[N]\,\E[X]$; $\Var(S)=\E[N]\Var(X)+\Var(N)(\E[X])^2$. When $N\sim\Poisson(\lambda)$, the second formula simplifies to $\Var(S)=\lambda\E[X^2]$.

**Conditional probability.** $P(A\mid B)=P(A\cap B)/P(B)$, defined when $P(B)>0$. It re-weights the probability of $A$ to the universe where $B$ has already occurred.

**Conditional distribution.** For discrete $(X,Y)$: $p_{X\mid Y}(x\mid y)=p(x,y)/p_Y(y)$. For continuous: $f_{X\mid Y}(x\mid y)=f(x,y)/f_Y(y)$. These are proper probability distributions in $x$ for each fixed $y$.

**Continuity correction.** When approximating a discrete count $X$ by a continuous normal, replace the integer boundary $k$ with $k\pm 0.5$ — the half-step to the outer edge of the unit-wide bar — before standardizing. E.g., $P(X\ge 56)\approx P(Z\ge(55.5-\mu)/\sigma)$.

**Correlation.** $\Corr(X,Y)=\rho_{XY}=\Cov(X,Y)/[\SD(X)\SD(Y)]$. Always in $[-1,1]$; equals $\pm1$ iff $Y=aX+b$ for some constants; equals $0$ for independent variables (but $0$ correlation does not imply independence).

**Covariance.** $\Cov(X,Y)=\E[(X-\mu_X)(Y-\mu_Y)]=\E[XY]-\E[X]\E[Y]$. Measures the direction of linear dependence; $\Cov(X,X)=\Var(X)$. For independent variables, $\Cov(X,Y)=0$.

**Deductible (ordinary).** An amount $d$ the policyholder absorbs before the insurer pays. The per-loss payment random variable is $(X-d)_+=\max(X-d,0)$. The mean is $\E[(X-d)_+]=\E[X]-\E[X\wedge d]$, or equivalently $\sum_{k>d}S(k)$ (discrete) or $\int_d^\infty S(x)\,dx$ (continuous).

**De Morgan's laws.** $(A\cup B)^c=A^c\cap B^c$ and $(A\cap B)^c=A^c\cup B^c$. Used to convert unions to intersections and vice versa in complement calculations.

**Discrete uniform distribution.** A distribution on $\{1,2,\dots,n\}$ (or any finite set of equally spaced values) assigning probability $1/n$ to each value. Mean $(n+1)/2$; variance $(n^2-1)/12$.

**Event.** A subset of the sample space $\Omega$ to which a probability can be assigned. Simple events are singletons; compound events are unions or intersections of simpler events.

**Expectation (expected value, mean).** For a discrete $X$: $\E[X]=\sum_k k\,p(k)$. For a continuous $X$: $\E[X]=\int_{-\infty}^\infty x\,f(x)\,dx$. The probability-weighted average of all possible values; also the balance point of the distribution. Linearity: $\E[aX+b]=a\E[X]+b$.

**Exponential distribution, $\Expo(\theta)$.** A continuous distribution on $(0,\infty)$ with pdf $f(x)=\tfrac{1}{\theta}e^{-x/\theta}$. Mean $\theta$; variance $\theta^2$; MGF $(1-\theta t)^{-1}$. The only continuous memoryless distribution. Models waiting times under a constant failure rate.

**Gamma distribution, $\GammaDist(\alpha,\theta)$.** A continuous distribution on $(0,\infty)$ with pdf $f(x)=x^{\alpha-1}e^{-x/\theta}/[\Gamma(\alpha)\theta^\alpha]$. Mean $\alpha\theta$; variance $\alpha\theta^2$. Equal to the distribution of a sum of $\alpha$ independent $\Expo(\theta)$ variables when $\alpha$ is a positive integer.

**Gamma function.** $\Gamma(\alpha)=\int_0^\infty x^{\alpha-1}e^{-x}\,dx$ for $\alpha>0$. Key facts: $\Gamma(\alpha)=(\alpha-1)\Gamma(\alpha-1)$; $\Gamma(n)=(n-1)!$ for positive integers; $\Gamma(1/2)=\sqrt{\pi}$. Enables the gamma integral identity $\int_0^\infty x^{\alpha-1}e^{-x/\theta}\,dx=\Gamma(\alpha)\theta^\alpha$.

**Geometric distribution, $\Geom(p)$.** The number of trials until the first success in independent Bernoulli trials. Two conventions: $p(k)=(1-p)^{k-1}p$ for $k=1,2,\dots$ (count trials) or $p(k)=(1-p)^k p$ for $k=0,1,\dots$ (count failures). Mean $1/p$ or $(1-p)/p$ respectively; variance $(1-p)/p^2$. The only discrete memoryless distribution.

**Hypergeometric distribution, $\HyperGeom(N,K,n)$.** The count of successes when drawing $n$ items without replacement from a population of $N$ containing $K$ successes. $\E[X]=nK/N$; $\Var(X)=n\tfrac{K}{N}\tfrac{N-K}{N}\tfrac{N-n}{N-1}$.

**Independence (events).** Events $A$ and $B$ are independent iff $P(A\cap B)=P(A)P(B)$, equivalently $P(A\mid B)=P(A)$. Mutually exclusive events with positive probability are dependent, not independent.

**Independence (random variables).** $X$ and $Y$ are independent iff their joint distribution factors: $f(x,y)=f_X(x)f_Y(y)$ (continuous) or $p(x,y)=p_X(x)p_Y(y)$ (discrete). Equivalent to: knowing $Y$ gives no information about $X$. Independence implies $\Cov(X,Y)=0$, but not conversely.

**Joint distribution.** A probability distribution over two or more variables simultaneously. Characterized by the joint pmf $p(x,y)=P(X=x,Y=y)$ or joint pdf $f(x,y)$ satisfying $\int\!\int f=1$. The individual ("marginal") distributions are recovered by summing or integrating out the other variable.

**Law of total expectation (double expectation).** $\E[X]=\E[\E[X\mid Y]]$ — the unconditional mean equals the mean of the conditional means. Used to compute $\E[X]$ when the problem is naturally stratified by a conditioning variable $Y$.

**Law of total probability.** For a partition $B_1,\dots,B_n$ of $\Omega$: $P(A)=\sum_i P(B_i)\,P(A\mid B_i)$. A weighted average of conditional probabilities, where the weights are the partition probabilities.

**Law of total variance.** $\Var(X)=\E[\Var(X\mid Y)]+\Var(\E[X\mid Y])$. The first term is the average within-group variance ("process variance"); the second is the variance of the conditional means across groups ("parameter variance"). Both terms are non-negative; ignoring either one systematically underestimates $\Var(X)$.

**Limited expected value (LEV).** $\E[X\wedge u]=\E[\min(X,u)]$. For a continuous $X$: $\int_0^u S(x)\,dx$. The expected loss retained by the insurer when no payment exceeds $u$. Used in the budget identity $\E[X\wedge u]+\E[(X-u)_+]=\E[X]$.

**Loss elimination ratio (LER).** $\mathrm{LER}(d)=1-\E[(X-d)_+]/\E[X]=\E[X\wedge d]/\E[X]$ — the fraction of expected loss eliminated by imposing a deductible $d$. Ranges from $0$ (deductible eliminates nothing) to $1$ (deductible covers all losses).

**Loss random variable.** The underlying ground-up loss $X$ before any policy modifications. Contrasted with the payment random variable, which reflects the policy's deductible, limit, and coinsurance.

**Marginal distribution.** The distribution of one variable obtained from a joint distribution by summing (discrete) or integrating (continuous) over all values of the other variable. $p_X(x)=\sum_y p(x,y)$; $f_X(x)=\int f(x,y)\,dy$.

**Median.** The value $m$ such that $P(X\le m)\ge 1/2$ and $P(X\ge m)\ge 1/2$; equivalently, the $50$th percentile. For a continuous distribution, the unique solution to $F(m)=1/2$.

**Memorylessness.** The property that past experience does not change the future distribution: $P(X>s+t\mid X>s)=P(X>t)$ for all $s,t\ge0$. The exponential is the only continuous memoryless distribution; the geometric is the only discrete memoryless distribution.

**MGF (moment generating function).** $M_X(t)=\E[e^{tX}]$, defined on an interval around $0$. The $n$-th raw moment is $\E[X^n]=M_X^{(n)}(0)$. If two distributions share an MGF on an open interval, they are identical. Used to identify distributions and derive moments.

**Mode.** The value (or values) at which the pmf or pdf is maximized — the most probable outcome. For a unimodal continuous distribution, found by setting $f'(x)=0$. The mode and mean coincide for symmetric distributions but can differ substantially for skewed ones.

**Moment.** The $n$-th raw moment is $\E[X^n]$; the $n$-th central moment is $\E[(X-\mu)^n]$. The first raw moment is the mean; the second central moment is the variance.

**Mutually exclusive (disjoint) events.** Events that cannot both occur: $A\cap B=\varnothing$, so $P(A\cap B)=0$. For disjoint events, $P(A\cup B)=P(A)+P(B)$.

**Negative binomial distribution, $\NegBin(r,p)$.** The number of trials (or failures) until the $r$-th success in independent Bernoulli trials. Reduces to the geometric when $r=1$; a sum of $r$ independent geometric variables.

**Normal distribution, $\mathcal{N}(\mu,\sigma^2)$.** The symmetric bell-shaped distribution with pdf $f(x)=\tfrac{1}{\sigma\sqrt{2\pi}}\exp\!\left(-\tfrac{(x-\mu)^2}{2\sigma^2}\right)$. Mean $\mu$; variance $\sigma^2$. Standardized by $Z=(X-\mu)/\sigma\sim\mathcal{N}(0,1)$; probabilities read from the $\Phi$ table. Characterized by the 68–95–99.7 rule.

**Order statistic.** The $k$-th order statistic $X_{(k)}$ is the $k$-th smallest value in a random sample of size $n$. Its cdf is $F_{(k)}(x)=\sum_{j=k}^n\binom{n}{j}[F(x)]^j[1-F(x)]^{n-j}$. The minimum is $X_{(1)}$; the maximum is $X_{(n)}$.

**Payment random variable.** The amount the insurer actually pays under a policy with deductible $d$, maximum covered loss $u$, and coinsurance $\alpha$. Per-loss: $Y_L=\alpha\cdot[\min(X,u)-\min(X,d)]_+$, or equivalently the covered layer scaled by $\alpha$. Per-payment: $Y_P=Y_L/(P(X>d))$, conditioned on a positive payment occurring.

**PDF (probability density function).** A non-negative function $f(x)$ such that $P(a\le X\le b)=\int_a^b f(x)\,dx$ and $\int_{-\infty}^\infty f(x)\,dx=1$. For a continuous random variable, $P(X=c)=0$ for any single point $c$; probability lives in intervals, not at points.

**Percentile.** The $p$-th percentile (or $100p$-th) is the smallest value $x$ such that $F(x)\ge p$. The $25$th, $50$th, and $75$th percentiles are the quartiles; the $50$th is the median.

**Per-loss vs. per-payment.** A per-loss calculation averages over all losses, including those below the deductible (which contribute zero payment). A per-payment calculation averages only over losses that exceed the deductible, i.e., over actual nonzero payments. They are related by $\E[Y_P]=\E[Y_L]/P(X>d)$.

**PMF (probability mass function).** For a discrete random variable, $p(k)=P(X=k)\ge 0$ with $\sum_k p(k)=1$. Fully specifies the distribution; each probability is a specific positive value at a point.

**Poisson distribution, $\Poisson(\lambda)$.** The distribution of the count of rare independent events in a fixed window at rate $\lambda>0$. $p(k)=e^{-\lambda}\lambda^k/k!$; mean $=$ variance $=\lambda$. Superposition: independent Poisson counts add to a Poisson sum.

**Policy limit.** A cap on the insurer's payment. Under a maximum covered loss $u$, the payment from the covered layer is $\min(X,u)-\min(X,d)$, equivalently $\E[X\wedge u]-\E[X\wedge d]$ for the expected payment (no coinsurance). A cap on the payment itself is $\min((X-d)_+, u_{\text{pay}})$.

**Random variable.** A function $X:\Omega\to\mathbb{R}$ that assigns a numerical value to each outcome in the sample space. It is discrete if it takes countably many values (each with positive probability) and continuous if its probabilities are given by integrating a density function.

**Sample space.** The set $\Omega$ of all possible outcomes of a random experiment. An event is any subset of $\Omega$.

**$\sigma$-algebra (informal).** A collection of subsets of $\Omega$ that is closed under complements and countable unions — the family of sets to which probabilities can coherently be assigned. On Exam P, every set of interest is implicitly measurable; the formalism matters mainly for understanding why "all subsets" can fail for uncountable spaces.

**Standard deviation.** $\SD(X)=\sigma=\sqrt{\Var(X)}$. Has the same units as $X$; measures spread around the mean. Less sensitive than variance to the scale of $X$.

**Survival function.** $S(x)=P(X>x)=1-F(x)$. Gives the probability the variable exceeds $x$. For the Darth-Vader mean formula: $\E[X]=\int_0^\infty S(x)\,dx$ (continuous, non-negative $X$); $\E[X]=\sum_{k=0}^\infty S(k)$ (non-negative integer-valued $X$).

**Uniform distribution, continuous, $\Unif(a,b)$.** A distribution with constant density $f(x)=1/(b-a)$ on $(a,b)$. Mean $(a+b)/2$; variance $(b-a)^2/12$. Any interval of equal length within $(a,b)$ has equal probability.

**Variance.** $\Var(X)=\E[(X-\mu)^2]=\E[X^2]-(\E[X])^2$. Measures average squared deviation from the mean. Linearity: $\Var(aX+b)=a^2\Var(X)$. For independent $X,Y$: $\Var(X+Y)=\Var(X)+\Var(Y)$.

---

*Term count: 57 formal glossary entries + 42 Kanto-term mappings.*
