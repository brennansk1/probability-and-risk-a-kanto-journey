<!--
  file: appendix_c_normal_table
  kind: appendix
  letter: C
  title: The Standard Normal Table
  purpose: the on-screen Φ(z)=P(Z≤z) cumulative table the SOA provides, plus the lookup techniques to wield it on exam day
  sources: ch12
  plan: MASTER_PLAN_V3 §23 (appendix spec)
-->

# Appendix C — The Standard Normal Table {.type-normal}

> **What this is.** The cumulative distribution of the standard normal, $\Phi(z)=P(Z\le z)$ for $Z\sim\Normal(0,1)$ — the same table the SOA hands you on-screen for Exam P. Every value below is the *computed* CDF $\Phi(z)=\tfrac12\!\left[1+\operatorname{erf}\!\left(z/\sqrt2\right)\right]$, rounded to four decimals. Read the **whole units and tenths** of $z$ down the left edge, the **hundredths** across the top, and the body cell is $\Phi(z)$ — the area under the bell **to the left** of $z$. The table only lists $z\ge0$; for negative $z$ you flip with the symmetry rule. Before any lookup, standardize: $Z=(X-\mu)/\sigma$ *(ch12, "The Bell of Thousands")*.

---

## The Table — $\Phi(z)=P(Z\le z)$

| $z$ | .00 | .01 | .02 | .03 | .04 | .05 | .06 | .07 | .08 | .09 |
|---|---|---|---|---|---|---|---|---|---|---|
| **0.0** | 0.5000 | 0.5040 | 0.5080 | 0.5120 | 0.5160 | 0.5199 | 0.5239 | 0.5279 | 0.5319 | 0.5359 |
| **0.1** | 0.5398 | 0.5438 | 0.5478 | 0.5517 | 0.5557 | 0.5596 | 0.5636 | 0.5675 | 0.5714 | 0.5753 |
| **0.2** | 0.5793 | 0.5832 | 0.5871 | 0.5910 | 0.5948 | 0.5987 | 0.6026 | 0.6064 | 0.6103 | 0.6141 |
| **0.3** | 0.6179 | 0.6217 | 0.6255 | 0.6293 | 0.6331 | 0.6368 | 0.6406 | 0.6443 | 0.6480 | 0.6517 |
| **0.4** | 0.6554 | 0.6591 | 0.6628 | 0.6664 | 0.6700 | 0.6736 | 0.6772 | 0.6808 | 0.6844 | 0.6879 |
| **0.5** | 0.6915 | 0.6950 | 0.6985 | 0.7019 | 0.7054 | 0.7088 | 0.7123 | 0.7157 | 0.7190 | 0.7224 |
| **0.6** | 0.7257 | 0.7291 | 0.7324 | 0.7357 | 0.7389 | 0.7422 | 0.7454 | 0.7486 | 0.7517 | 0.7549 |
| **0.7** | 0.7580 | 0.7611 | 0.7642 | 0.7673 | 0.7704 | 0.7734 | 0.7764 | 0.7794 | 0.7823 | 0.7852 |
| **0.8** | 0.7881 | 0.7910 | 0.7939 | 0.7967 | 0.7995 | 0.8023 | 0.8051 | 0.8078 | 0.8106 | 0.8133 |
| **0.9** | 0.8159 | 0.8186 | 0.8212 | 0.8238 | 0.8264 | 0.8289 | 0.8315 | 0.8340 | 0.8365 | 0.8389 |
| **1.0** | 0.8413 | 0.8438 | 0.8461 | 0.8485 | 0.8508 | 0.8531 | 0.8554 | 0.8577 | 0.8599 | 0.8621 |
| **1.1** | 0.8643 | 0.8665 | 0.8686 | 0.8708 | 0.8729 | 0.8749 | 0.8770 | 0.8790 | 0.8810 | 0.8830 |
| **1.2** | 0.8849 | 0.8869 | 0.8888 | 0.8907 | 0.8925 | 0.8944 | 0.8962 | 0.8980 | 0.8997 | 0.9015 |
| **1.3** | 0.9032 | 0.9049 | 0.9066 | 0.9082 | 0.9099 | 0.9115 | 0.9131 | 0.9147 | 0.9162 | 0.9177 |
| **1.4** | 0.9192 | 0.9207 | 0.9222 | 0.9236 | 0.9251 | 0.9265 | 0.9279 | 0.9292 | 0.9306 | 0.9319 |
| **1.5** | 0.9332 | 0.9345 | 0.9357 | 0.9370 | 0.9382 | 0.9394 | 0.9406 | 0.9418 | 0.9429 | 0.9441 |
| **1.6** | 0.9452 | 0.9463 | 0.9474 | 0.9484 | 0.9495 | 0.9505 | 0.9515 | 0.9525 | 0.9535 | 0.9545 |
| **1.7** | 0.9554 | 0.9564 | 0.9573 | 0.9582 | 0.9591 | 0.9599 | 0.9608 | 0.9616 | 0.9625 | 0.9633 |
| **1.8** | 0.9641 | 0.9649 | 0.9656 | 0.9664 | 0.9671 | 0.9678 | 0.9686 | 0.9693 | 0.9699 | 0.9706 |
| **1.9** | 0.9713 | 0.9719 | 0.9726 | 0.9732 | 0.9738 | 0.9744 | 0.9750 | 0.9756 | 0.9761 | 0.9767 |
| **2.0** | 0.9772 | 0.9778 | 0.9783 | 0.9788 | 0.9793 | 0.9798 | 0.9803 | 0.9808 | 0.9812 | 0.9817 |
| **2.1** | 0.9821 | 0.9826 | 0.9830 | 0.9834 | 0.9838 | 0.9842 | 0.9846 | 0.9850 | 0.9854 | 0.9857 |
| **2.2** | 0.9861 | 0.9864 | 0.9868 | 0.9871 | 0.9875 | 0.9878 | 0.9881 | 0.9884 | 0.9887 | 0.9890 |
| **2.3** | 0.9893 | 0.9896 | 0.9898 | 0.9901 | 0.9904 | 0.9906 | 0.9909 | 0.9911 | 0.9913 | 0.9916 |
| **2.4** | 0.9918 | 0.9920 | 0.9922 | 0.9925 | 0.9927 | 0.9929 | 0.9931 | 0.9932 | 0.9934 | 0.9936 |
| **2.5** | 0.9938 | 0.9940 | 0.9941 | 0.9943 | 0.9945 | 0.9946 | 0.9948 | 0.9949 | 0.9951 | 0.9952 |
| **2.6** | 0.9953 | 0.9955 | 0.9956 | 0.9957 | 0.9959 | 0.9960 | 0.9961 | 0.9962 | 0.9963 | 0.9964 |
| **2.7** | 0.9965 | 0.9966 | 0.9967 | 0.9968 | 0.9969 | 0.9970 | 0.9971 | 0.9972 | 0.9973 | 0.9974 |
| **2.8** | 0.9974 | 0.9975 | 0.9976 | 0.9977 | 0.9977 | 0.9978 | 0.9979 | 0.9979 | 0.9980 | 0.9981 |
| **2.9** | 0.9981 | 0.9982 | 0.9982 | 0.9983 | 0.9984 | 0.9984 | 0.9985 | 0.9985 | 0.9986 | 0.9986 |
| **3.0** | 0.9987 | 0.9987 | 0.9987 | 0.9988 | 0.9988 | 0.9989 | 0.9989 | 0.9989 | 0.9990 | 0.9990 |
| **3.1** | 0.9990 | 0.9991 | 0.9991 | 0.9991 | 0.9992 | 0.9992 | 0.9992 | 0.9992 | 0.9993 | 0.9993 |
| **3.2** | 0.9993 | 0.9993 | 0.9994 | 0.9994 | 0.9994 | 0.9994 | 0.9994 | 0.9995 | 0.9995 | 0.9995 |
| **3.3** | 0.9995 | 0.9995 | 0.9995 | 0.9996 | 0.9996 | 0.9996 | 0.9996 | 0.9996 | 0.9996 | 0.9997 |
| **3.4** | 0.9997 | 0.9997 | 0.9997 | 0.9997 | 0.9997 | 0.9997 | 0.9997 | 0.9997 | 0.9997 | 0.9998 |

> For $z\ge3.50$, take $\Phi(z)\approx1.0000$ (the right tail is below $0.0002$). For $z\le-3.50$, take $\Phi(z)\approx0.0000$.

---

## How to Read It — Seven Moves

**1. Direct lookup $\Phi(z)$.** Split $z$ into tenths (row) and hundredths (column). The cell is the area to the **left**.
$$\Phi(1.23)=P(Z\le 1.23)=0.8907.$$
Walk down to row **1.2**, across to column **.03**.

**2. Symmetry — the negative half $\Phi(-z)=1-\Phi(z)$.** The bell is mirror-symmetric about $0$, so area left of $-z$ equals area right of $+z$.
$$\Phi(-1.23)=1-\Phi(1.23)=1-0.8907=0.1093.$$
This is the *only* way to handle negative $z$ — the table never prints them.

**3. Right tail $P(Z>z)=1-\Phi(z)$.** Total area is $1$, so the right tail is one minus the table value.
$$P(Z>1.23)=1-0.8907=0.1093.$$
(Notice it equals $\Phi(-1.23)$ — symmetry again.) For continuous $Z$, $>$ and $\ge$ are interchangeable: $P(Z\ge z)=P(Z>z)$.

**4. Interval $P(a\le Z\le b)=\Phi(b)-\Phi(a)$.** Subtract the smaller cumulative from the larger.
$$P(-0.50\le Z\le 1.23)=\Phi(1.23)-\Phi(-0.50)=0.8907-(1-0.6915)=0.8907-0.3085=0.5822.$$
The handy central cases: $P(|Z|\le1)\approx0.6827$, $P(|Z|\le1.96)=0.9500$, $P(|Z|\le2)\approx0.9545$, $P(|Z|\le3)\approx0.9973$ — the **68–95–99.7** rule.

**5. Inverse lookup — find $z$ for a given $\Phi$.** Hunt the **body** for the target probability, then read the row+column back out as $z$.
$$\Phi(z)=0.9750\ \Rightarrow\ z=1.96\quad(\text{row }1.9,\ \text{col }.06).$$
If the area you want is below $0.5$, the $z$ is negative: solve $\Phi(z)=0.10$ as $\Phi(-z)=1-0.10=0.90\Rightarrow -z\approx1.28\Rightarrow z\approx-1.28$.

**6. Linear interpolation between cells.** When the target sits *between* two listed values, interpolate proportionally. To find $z$ with $\Phi(z)=0.9000$: the table straddles $\Phi(1.28)=0.8997$ and $\Phi(1.29)=0.9015$, a gap of $0.0018$ over $\Delta z=0.01$. You need $0.9000-0.8997=0.0003$ more:
$$z\approx1.28+\frac{0.0003}{0.0018}(0.01)=1.28+0.0017\approx1.2817\ \ (\text{round to }1.28).$$
The same proportional step works forward (interpolating $\Phi$ for a $z$ between hundredths). On Exam P the nearest cell is almost always close enough; interpolate only when a problem's answer choices are tight.

**7. Standardize first — then look up.** The table is for $\Normal(0,1)$ only. For $X\sim\Normal(\mu,\sigma^2)$, convert to a $z$-score before any lookup:
$$Z=\frac{X-\mu}{\sigma},\qquad P(X\le x)=\Phi\!\left(\frac{x-\mu}{\sigma}\right).$$
*Example:* $X\sim\Normal(100,15^2)$, find $P(X\le 130)$. Standardize: $z=(130-100)/15=2.00$, so $P=\Phi(2.00)=0.9772$.

> **Continuity correction ($\pm0.5$) — apply it BEFORE standardizing.** *(ch12)* When approximating a **discrete** sum (a binomial count, a Poisson total, a sum of integer payouts) by the normal, first widen the region by $0.5$ to the outer edge of every bar you keep, *then* compute the $z$-score. E.g. for a count $S$, $P(S\le k)\approx\Phi\!\big((k+0.5-\mu)/\sigma\big)$ and $P(S\ge k)\approx 1-\Phi\!\big((k-0.5-\mu)/\sigma\big)$. The half-step goes on the *raw* scale, never after dividing by $\sigma$. See ch12 for the full derivation.

---

## Critical Values — Quick Box

The $z$ cutoffs the exam reaches for most often. **One-sided** $z_\alpha$ satisfies $\Phi(z_\alpha)=1-\alpha$ (area $\alpha$ in one tail); **two-sided** $z_{\alpha/2}$ satisfies $\Phi(z_{\alpha/2})=1-\alpha/2$ (area $\alpha$ split between both tails, leaving the stated confidence in the middle).

| Confidence / level | One-sided $z$ ($\Phi(z)=c$) | Two-sided $z$ ($\Phi(z)=\tfrac{1+c}{2}$) |
|---|---|---|
| 0.90 | 1.282 | 1.645 |
| 0.95 | 1.645 | 1.960 |
| 0.975 | 1.960 | 2.241 |
| 0.99 | 2.326 | 2.576 |

> **Read it right.** The *one-sided* column answers "what $z$ leaves area $c$ to its left?" — so $\Phi(1.645)=0.95$. The *two-sided* column answers "what $\pm z$ traps central probability $c$?" — so $P(|Z|\le1.960)=0.95$, the famous **1.96**. The two anchors actuaries quote from memory: **1.645** (one-sided 95% / two-sided 90%) and **1.96** (two-sided 95%).
