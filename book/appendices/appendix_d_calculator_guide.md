<!--
  file: appendix_d_calculator_guide
  kind: appendix
  letter: D
  title: The Trainer's Calculator — TI-30XS MultiView Field Manual
  purpose: single-calculator deep reference for the TI-30XS MultiView; every Exam-P-relevant keystroke, organized by operation; ends with a tear-out quick-reference card and exam-day protocol
  sources: ch00 (Trainer's-Calculator primer), ch03 (flagship 1-Var Stats workflow)
  plan: MASTER_PLAN_V3 §13, §18, §23
-->

# Appendix D — The Trainer's Calculator: TI-30XS MultiView Field Manual {.type-electric}

> **What this is.** Oak issues every trainer one machine for the road, and this book teaches that machine to mastery: the **TI-30XS MultiView**. Its MathPrint display, one-press `nCr`/`nPr`, and data-list **1-Var Stats** engine make it the best-suited calculator the SOA permits for Exam P. This appendix is the field manual — every Exam-P-relevant keystroke, organized *by operation*, each section opening with a key-cap strip and a one-line "when you use it on Exam P." It assumes the setup taught once in `ch00` (the Trainer's-Calculator primer) and the flagship workflow taught in `ch03`; here they live side by side, in the order your exam-day brain reaches for them. Keys are written as little key-caps — [2nd]{.kbd}, [data]{.kbd}, [STO▸]{.kbd} — distinct from math type and from code; a sequence is just key-caps in a row, sometimes wrapped as a strip.

---

## 1. Setup & Hygiene — the habits that come first

[ [mode]{.kbd} → MathPrint · Float ]{.keystroke}  ·  [ between problems: [clear]{.kbd} then [2nd]{.kbd} [clear var]{.kbd} ]{.keystroke}  ·  [ [STO▸]{.kbd} [x]{.kbd} ]{.keystroke}  ·  [ [2nd]{.kbd} [ans]{.kbd} ]{.keystroke}  ·  [ [F◂▸D]{.kbd} ]{.keystroke}

> *When you use it on Exam P:* once at the start (set the mode), then on **every** problem (clear, store, recall) — this section is the difference between a calculator that helps and one that quietly corrupts an answer.

**Modes & MathPrint.** Press [mode]{.kbd} once. For Exam P the defaults are correct and you should leave them: **MathPrint** (fractions, exponents, and roots display the way they are written, so what you see matches what you mean), and **Float** decimal display (full precision — *not* a fixed two places, which would round mid-problem). The Degree/Radian setting is irrelevant to probability. The whole point of opening [mode]{.kbd} is to *confirm where it sits* — set it once and forget it.

**Clear before each problem.** The single cheapest error-prevention habit on the exam. Two different clears do two different jobs:

- [clear]{.kbd} wipes the current entry line (the scratch you can see).
- [2nd]{.kbd} [clear var]{.kbd} wipes the **stored memory variables** (the values you *can't* see). A stale number left in a memory slot is invisible until it silently poisons your next answer.

Make both a reflex between problems — like recalling a Pokémon before the next battle. If you stored anything during a problem, clear the variables before the next one begins.

**The seven memory variables + store, don't retype.** The TI-30XS holds **seven memory slots** — $x,\ y,\ z,\ t,\ a,\ b,\ c$. To bank a computed value, press [STO▸]{.kbd} then the variable key; to use it later, just type that variable and it stands in for the full stored number.

Why this matters more than it looks: when a multi-step problem produces an ugly intermediate — say $E[X]=2.15384\ldots$ — you can either write down a rounded "$2.15$" and re-type it later (introducing **rounding drift** that can shove your answer into the wrong multiple-choice bucket), or press [STO▸]{.kbd} [x]{.kbd} once and carry the *full-precision* value forward untouched. Always do the second. **Store, don't retype** is the habit that most reliably separates a right answer from a "close, but not option C."

*A worked feel for it.* Compute $(0.2)(0.5)+(0.7)(0.05)$, press [STO▸]{.kbd} [a]{.kbd} to bank the full result; now [a]{.kbd} *is* that number in every later keystroke — no copying, no rounding, no drift.

**Recall — reading a slot back.** To see what a slot currently holds, press [2nd]{.kbd} [recall]{.kbd} and choose the variable; the stored value drops onto the entry line. Use it to confirm you stored what you meant to before you build on it.

**The answer toggle [2nd]{.kbd} [ans]{.kbd}.** The calculator always remembers your **last result**. Press [2nd]{.kbd} [ans]{.kbd} to drop it into a new expression — or simply start an entry with an operator (e.g. press [×]{.kbd} right after a result) and `ans` is inserted for you. This chains a calculation without re-typing the previous answer, the same drift-killing idea as [STO▸]{.kbd} but for the *immediately* preceding step.

**The fraction toggle [F◂▸D]{.kbd}.** Press [F◂▸D]{.kbd} to flip the displayed answer between its **fraction** and **decimal** forms. Got $\tfrac{3}{8}$ and want $0.375$? One press. Probabilities are often cleaner to *enter* as fractions and cleaner to *report* as decimals — this key moves between them instantly.

**Order of operations.** The TI-30XS obeys standard algebraic precedence (powers, then $\times\,\div$, then $+\,-$), so an unparenthesized expression can evaluate in an order you didn't intend. The fix is mechanical: **wrap any grouped numerator, denominator, or exponent in parentheses.** $(x-\mu)\div\sigma$ must be typed with the subtraction *inside* parentheses, or the machine divides only $\mu$ by $\sigma$. When in doubt, over-parenthesize — it never costs you anything.

> *Recognition cue:* an ugly intermediate → [STO▸]{.kbd} it. A grouped expression → parenthesize it. A new problem → clear first.

---

## 2. The Probability Menu [prb]{.kbd} — counting in one press

[ $n$ [prb]{.kbd} → nCr → $r$ [enter]{.kbd} ]{.keystroke}  ·  [ $n$ [prb]{.kbd} → nPr → $r$ [enter]{.kbd} ]{.keystroke}  ·  [ $n$ [prb]{.kbd} → ! → [enter]{.kbd} ]{.keystroke}

> *When you use it on Exam P:* binomial coefficients $\binom{n}{r}$ for binomial/hypergeometric probabilities and any "how many ways" counting question — the most-pressed menu on the General-Probability and discrete-distribution problems.

Press [prb]{.kbd} to open the probability menu. It holds three operators you will use constantly:

- **`nCr`** — combinations, $\binom{n}{r}=\dfrac{n!}{r!\,(n-r)!}$, order *doesn't* matter. This is the binomial coefficient.
- **`nPr`** — permutations, $\dfrac{n!}{(n-r)!}$, order *does* matter.
- **`!`** — the factorial $n!$ on its own.

All three are written **infix**: you type the left operand *first*, then open the menu and pick the operator, then type the right operand. The factorial takes only the left operand.

**Worked keystroke — $\binom{12}{6}$.** Say a problem needs the number of ways to choose $6$ Pokémon from a roster of $12$ (a binomial coefficient that also shows up as the leading factor in $\Binom(12,p)$ at $k=6$):

[ 12 [prb]{.kbd} → nCr → 6 [enter]{.kbd} ]{.keystroke}

The screen reads $924$. To turn that into a binomial probability $P(X=6)$ for $X\sim\Binom(12,0.4)$, continue on the same line — multiply by $p^6 q^6$ using the powers in §4 — or store the $924$ with [STO▸]{.kbd} [a]{.kbd} and build the rest around [a]{.kbd}.

> *Trainer's note.* `nCr` is symmetric: $\binom{12}{6}=\binom{12}{6}$ trivially, but $\binom{12}{2}=\binom{12}{10}=66$ — pick the smaller $r$ to keep the numbers friendly, though the calculator doesn't care.

---

## 3. Exponential & Logarithm — $e^x$, $\ln$, $10^x$, $\log$

[ [2nd]{.kbd} [ln]{.kbd} $=e^x$ ]{.keystroke}  ·  [ [ln]{.kbd} ]{.keystroke}  ·  [ [2nd]{.kbd} [log]{.kbd} $=10^x$ ]{.keystroke}  ·  [ [log]{.kbd} ]{.keystroke}

> *When you use it on Exam P:* the Poisson factor $e^{-\lambda}$, exponential survival $S(x)=e^{-x/\theta}$, and anything where solving for a rate or time needs a logarithm — the workhorse of the distribution chapters.

**The exponential $e^x$ — [2nd]{.kbd} [ln]{.kbd}.** The $e^x$ function is the printed *second* function above the [ln]{.kbd} key, so you reach it through the gateway: press [2nd]{.kbd}, then [ln]{.kbd}. A negative exponent needs the **negation** key [(-)]{.kbd} (not the subtraction [−]{.kbd}):

[ [2nd]{.kbd} [ln]{.kbd} [(-)]{.kbd} 2.3 [enter]{.kbd} ]{.keystroke}  gives  $e^{-2.3}\approx 0.1003$.

That is exactly the Poisson factor $e^{-\lambda}$ for $\lambda=2.3$, and exactly the exponential survival $S(x)=e^{-x/\theta}$ once you've formed the exponent.

**Exponential survival in one shot.** For $X\sim\Expo(\theta)$, $S(x)=P(X>x)=e^{-x/\theta}$. Type the whole exponent inside the parentheses so precedence can't bite:

[ [2nd]{.kbd} [ln]{.kbd} [(-)]{.kbd} ( $x$ [÷]{.kbd} $\theta$ ) [enter]{.kbd} ]{.keystroke}

For $x=5,\ \theta=4$: $S(5)=e^{-5/4}=e^{-1.25}\approx 0.2865$. (The parentheses around $x\div\theta$ are doing real work — without them you'd exponentiate $-x$ and *then* divide.)

**The natural log [ln]{.kbd}.** Its own key, used to *invert* an exponential — solving for a time or rate. To find the $x$ with $S(x)=0.2$ under $\theta=4$: from $e^{-x/4}=0.2$ you get $x=-4\ln(0.2)$:

[ [(-)]{.kbd} 4 [×]{.kbd} [ln]{.kbd} 0.2 [enter]{.kbd} ]{.keystroke}  $\approx 6.44$.

**Base-ten $10^x$ and $\log$.** Less common on Exam P but present: $10^x$ is the second function above [log]{.kbd} (so [2nd]{.kbd} [log]{.kbd}), and [log]{.kbd} is base-ten logarithm. Reach for them only when a problem is genuinely stated in powers of ten; the natural pair $e^x/\ln$ covers the probability work.

**The Poisson recursion — a stored $e^{-\lambda}$ that pays off every term.** Computing a Poisson cdf $P(X\le k)=\sum_{j=0}^{k} e^{-\lambda}\lambda^{j}/j!$ term by term wastes keystrokes, because each term shares the factor $e^{-\lambda}$ and each is the previous one nudged by a single ratio:
$$p(0)=e^{-\lambda},\qquad p(k)=p(k-1)\cdot\frac{\lambda}{k}.$$
Drive it like this. First bank $e^{-\lambda}$ — that's $p(0)$:

[ [2nd]{.kbd} [ln]{.kbd} [(-)]{.kbd} $\lambda$ [STO▸]{.kbd} [a]{.kbd} [enter]{.kbd} ]{.keystroke}

Now [a]{.kbd} holds $p(0)$ at full precision. Each next term is one multiplication — multiply the current term by $\lambda$ and divide by the new $k$ — and you can re-store into [a]{.kbd} as you climb so [a]{.kbd} always holds the latest $p(k)$:

[ [a]{.kbd} [×]{.kbd} $\lambda$ [÷]{.kbd} 1 [STO▸]{.kbd} [a]{.kbd} [enter]{.kbd} ]{.keystroke}  gives $p(1)$;  then  [ [a]{.kbd} [×]{.kbd} $\lambda$ [÷]{.kbd} 2 [STO▸]{.kbd} [a]{.kbd} [enter]{.kbd} ]{.keystroke}  gives $p(2)$, and so on.

Running them into a memory sum (say [b]{.kbd}) as you go builds the cdf with no rounding drift and a handful of presses. For $\lambda=2.3$: $p(0)\approx0.1003$, $p(1)\approx0.2306$, $p(2)\approx0.2652$, so $P(X\le2)\approx0.5960$.

---

## 4. Powers & Roots — $x^2$, $\hat{\ }$, $\sqrt{\ }$, $x^{-1}$

[ [x²]{.kbd} ]{.keystroke}  ·  [ base [^]{.kbd} exponent ]{.keystroke}  ·  [ [2nd]{.kbd} [x²]{.kbd} $=\sqrt{\ }$ ]{.keystroke}  ·  [ [x⁻¹]{.kbd} ]{.keystroke}

> *When you use it on Exam P:* squaring a standard deviation into a variance (or $\sigma x$ into $\Var$), raising $p^k q^{n-k}$ in a binomial, square-rooting a variance back to an SD, and reciprocals like $1/\theta$.

- **[x²]{.kbd}** — squares whatever is on the line. The fastest path from $\sigma$ to $\sigma^2$: read $\sigma x$ off the 1-Var Stats screen (§5), then [x²]{.kbd} gives the variance.
- **[^]{.kbd}** — general power, typed infix: `base` [^]{.kbd} `exponent`. For a binomial term you'll type $p$ [^]{.kbd} $k$ and $q$ [^]{.kbd} $(n-k)$; parenthesize the exponent if it's an expression.
- **[2nd]{.kbd} [x²]{.kbd}** — the square root $\sqrt{\ }$ is the second function over [x²]{.kbd}. Use it to go *back* from a variance to a standard deviation.
- **[x⁻¹]{.kbd}** — the reciprocal $1/x$. Handy for $1/\theta$ (the exponential *rate*), $1/n$, and inverting any single value without typing `1 ÷`.

*Worked feel.* If 1-Var Stats reports $\sigma x \approx 1.195$, then [x²]{.kbd} gives $\Var\approx 1.4280$. If a problem hands you $\Var=4$ and asks for the SD, [2nd]{.kbd} [x²]{.kbd} on $4$ returns $2$.

---

## 5. The Flagship — 1-Var Stats from a pmf

[ [data]{.kbd} → L1: values · L2: probabilities ]{.keystroke}  ·  [ [2nd]{.kbd} [stat]{.kbd} → 1-Var Stats · DATA: L1 · FRQ: L2 · CALC ]{.keystroke}  ·  read $\bar x$ and $\sigma x$

> *When you use it on Exam P:* **every** "find $E[X]$ and $\Var(X)$ from this table" question — and that is a huge slice of Topic 2 (Univariate RVs, 44–50% of the exam). This is the single highest-leverage technique in the book.

This is the workflow taught in full in `ch03`; here is the field-manual version. The whole computation of a mean and variance from a probability mass function collapses onto **one screen**.

**Step 1 — enter the distribution.** Press [data]{.kbd} to open the list editor. Type the **values** the RV can take into **L1** and their **probabilities** into **L2**, lined up row for row. (Frequencies work identically — if a problem gives raw counts instead of probabilities, those go in L2 just the same.) For the ledger RV $X$ with pmf $p(0)=.10,\ p(1)=.20,\ p(2)=.30,\ p(3)=.25,\ p(4)=.15$:

[ L1: 0  1  2  3  4   ·   L2: .10  .20  .30  .25  .15 ]{.keystroke}

**Step 2 — run 1-Var Stats and point it at L2.** The statistics menu is the *second* function over [data]{.kbd}/stat, so press [2nd]{.kbd} [stat]{.kbd}. Choose **1-Var Stats**, then set **DATA: L1** and — the step everyone forgets — **FRQ: L2** so the calculator weights each value by its probability. Select **CALC**:

[ [2nd]{.kbd} [stat]{.kbd} → 1-Var Stats · DATA: L1 · FRQ: L2 · CALC ]{.keystroke}

**Step 3 — read the answers off the screen.** The results screen shows, among other lines:

- $\bar x = 2.15$ — this **is** $E[X]$, the mean.
- $\sigma x \approx 1.195$ — the **population** standard deviation. Its square is the variance: [x²]{.kbd} gives $\Var(X)=\sigma x^2 \approx 1.4280$.

So a pmf that would take a column of hand-multiplications becomes $E[X]=2.15$ and $\Var(X)\approx1.43$ in seconds.

> **Use $\sigma x$, NOT $sx$ — this is the one trap.** The screen also prints $sx$, the *sample* standard deviation, which divides by $n-1$ instead of $n$. For a probability distribution that is simply **wrong** — you want the population SD, $\sigma x$. Reading $sx$ by reflex is the most common way this workflow fails. **Variance $=\sigma x^2$, always.**

**Clear the lists between problems.** Old values left in L1/L2 will silently corrupt the next distribution. Clear them with [2nd]{.kbd} [data]{.kbd} → **ClrL1/L2** (or overwrite every used row). This is the list-editor cousin of the [2nd]{.kbd} [clear var]{.kbd} hygiene from §1.

> *Transformations need no re-entry.* For a payout $Y=aX+b$, don't rebuild a list — use linearity off the values you already have: $E[Y]=a\bar x+b$ and $\Var(Y)=a^2\sigma x^2$. E.g. $Y=3X+2$ gives $E[Y]=3(2.15)+2=8.45$ and $\Var(Y)=9(1.4280)\approx12.85$, each one line on the calculator.

---

## 6. Standardization & Continuity Correction

[ ( $x$ [−]{.kbd} $\mu$ ) [÷]{.kbd} $\sigma$ [enter]{.kbd} ]{.keystroke}  ·  store $\mu,\sigma$ with [STO▸]{.kbd}  ·  apply $\pm0.5$ **before** standardizing

> *When you use it on Exam P:* every Normal-distribution lookup — convert $X\sim\Normal(\mu,\sigma^2)$ to a $z$-score before reading Appendix C; the continuity correction rides along whenever you approximate a discrete count by the Normal.

**The $z$-score.** To standardize, compute $z=\dfrac{x-\mu}{\sigma}$. The parentheses around the numerator are mandatory — without them the machine divides only $\mu$ by $\sigma$ and then subtracts, giving nonsense:

[ ( $x$ [−]{.kbd} $\mu$ ) [÷]{.kbd} $\sigma$ [enter]{.kbd} ]{.keystroke}

For $X\sim\Normal(100,15^2)$ and $x=130$: $(130-100)\div15=2.00$, so $P(X\le130)=\Phi(2.00)=0.9772$ from Appendix C.

**Store $\mu$ and $\sigma$ once when you'll standardize several $x$'s.** If a problem asks for probabilities at several cutoffs, bank the parameters: [STO▸]{.kbd} [a]{.kbd} for $\mu$ and [STO▸]{.kbd} [b]{.kbd} for $\sigma$. Then each new $z$ is just [ ( $x$ [−]{.kbd} [a]{.kbd} ) [÷]{.kbd} [b]{.kbd} [enter]{.kbd} ]{.keystroke} — same precision, no re-typed parameters, no drift.

**Continuity correction — apply $\pm0.5$ BEFORE standardizing.** When you approximate a **discrete** sum (a binomial count, a Poisson total, a sum of integer payouts) by the Normal, first widen the region by $0.5$ to the outer edge of every bar you keep, *then* compute the $z$-score. The half-step goes on the **raw** scale — never after dividing by $\sigma$:
$$P(S\le k)\approx\Phi\!\Big(\frac{k+0.5-\mu}{\sigma}\Big),\qquad P(S\ge k)\approx 1-\Phi\!\Big(\frac{k-0.5-\mu}{\sigma}\Big).$$
On the keys, that means the $+0.5$ or $-0.5$ goes *inside* the numerator parentheses, before the [÷]{.kbd}:

[ ( $k$ [+]{.kbd} 0.5 [−]{.kbd} $\mu$ ) [÷]{.kbd} $\sigma$ [enter]{.kbd} ]{.keystroke}

Get the half-step in first, then standardize. (See `ch12` for the full derivation.)

---

## 7. The Keypad — eight keys that win Exam P

You do not need most of the keypad. These eight do the actuarial work; learn where each one sits and you can drive the machine without looking down.

| Key | Where it is | What it does | First taught |
|---|---|---|---|
| [2nd]{.kbd} | top-left, the gateway | reaches the small *above-the-key* function printed over any key ($e^x$, stat, clear var, recall) | ch00 |
| [prb]{.kbd} | probability menu | `nCr`, `nPr`, `!` — binomial coefficients & counting | ch04 |
| [data]{.kbd} | list editor | enter a pmf into L1 (values) and L2 (probabilities) | ch03 |
| [stat]{.kbd} | [2nd]{.kbd} [data]{.kbd} = stat | launches **1-Var Stats** — reads $\bar x=E[X]$, $\sigma x$ (so $\Var=\sigma x^2$) | ch03 |
| [STO▸]{.kbd} | store-arrow | banks a value into one of seven memories — *store, don't retype* | ch00 |
| [F◂▸D]{.kbd} | fraction toggle | flips the answer between fraction and decimal | ch00 |
| [e^x]{.kbd} | [2nd]{.kbd} [ln]{.kbd} | $e^x$ in one reach — Poisson $e^{-\lambda}$, exponential survival | ch05 |
| [ln]{.kbd} | its own key | natural log — inverts an exponential to solve for a rate/time | ch05 |

Think of [2nd]{.kbd} as the gateway: three of the eight ([stat]{.kbd}, [e^x]{.kbd}, and the clears/recall) live *above* their keys and are reached through it. If a keystroke ever returns something unexpected, the usual cause is a missing or stray [2nd]{.kbd} — glance at whether you wanted the printed-*on* function or the printed-*above* one.

---

## 8. Tear-Out Quick-Reference Card

Cut along the margin. One operation per row, the canonical keystroke beside it.

| Operation | Keystroke |
|---|---|
| Set display mode | [mode]{.kbd} → MathPrint · Float (set once) |
| Clear entry / clear memory | [clear]{.kbd}  /  [2nd]{.kbd} [clear var]{.kbd} |
| Store a value | [STO▸]{.kbd} + variable ($x,y,z,t,a,b,c$) |
| Recall a value | [2nd]{.kbd} [recall]{.kbd} → variable |
| Reuse last answer | [2nd]{.kbd} [ans]{.kbd} |
| Fraction ↔ decimal | [F◂▸D]{.kbd} |
| Binomial coefficient $\binom{n}{r}$ | $n$ [prb]{.kbd} → nCr → $r$ [enter]{.kbd} |
| Permutation $_nP_r$ | $n$ [prb]{.kbd} → nPr → $r$ [enter]{.kbd} |
| Factorial $n!$ | $n$ [prb]{.kbd} → ! → [enter]{.kbd} |
| $e^{x}$ (Poisson, survival) | [2nd]{.kbd} [ln]{.kbd} [(-)]{.kbd} value [enter]{.kbd} |
| Natural log (solve for rate/time) | [ln]{.kbd} value [enter]{.kbd} |
| Square / square root | [x²]{.kbd}  /  [2nd]{.kbd} [x²]{.kbd} |
| General power | base [^]{.kbd} exponent |
| Reciprocal $1/x$ | [x⁻¹]{.kbd} |
| **Mean & variance from a pmf** | [data]{.kbd} L1=values, L2=probs → [2nd]{.kbd} [stat]{.kbd} → 1-Var Stats · FRQ: L2 → read $\bar x$, $\sigma x$ (var $=\sigma x^2$) |
| Clear stat lists | [2nd]{.kbd} [data]{.kbd} → ClrL1/L2 |
| Standardize $z=(x-\mu)/\sigma$ | ( $x$ [−]{.kbd} $\mu$ ) [÷]{.kbd} $\sigma$ [enter]{.kbd} |
| Continuity correction | apply $\pm0.5$ **before** standardizing |

> **The one warning to memorize:** on the 1-Var Stats screen use **$\sigma x$ (population SD), never $sx$ (sample SD)** — variance is $\sigma x^2$.

---

## 9. Exam-Day Calculator Protocol

The calculator is gear, and gear is checked the night before — never on the road.

1. **Bring TWO TI-30XS MultiView units.** A primary and a backup. Calculators fail, batteries die, keys stick; a dead machine mid-exam with no spare can end a sitting. Two identical units means a failure costs you seconds, not the exam. (Both must be the *same* model you trained on — your fingers know the keypad blind, and exam day is the worst time to learn a new layout.)

2. **Memory-clear both units the night before.** Run [2nd]{.kbd} [clear var]{.kbd} (stored variables) and [2nd]{.kbd} [data]{.kbd} → ClrL1/L2 (the stat lists) on each unit so neither carries a stale value into question one. The **cleared-memory rule:** you may bring the calculator, but it must hold **no stored data** when the exam begins — clearing it yourself the night before keeps you compliant and starts you clean.

3. **Display settings are not memory.** Setting MathPrint and Float (§1) is *not* stored data — you're allowed to have the mode configured. Confirm both units sit in MathPrint · Float before you pack them, so neither surprises you at the desk.

4. **The backup-unit rule in practice.** Keep the spare on the desk, powered off, within reach. If the primary misbehaves — a frozen screen, a fading display, a stuck key — switch immediately rather than fighting it; you lose a few seconds, not a question. Because both are memory-cleared and mode-matched, the swap is seamless.

> *Trainer's send-off.* You trained one machine to mastery, drilled the flagship workflow until 1-Var Stats is muscle memory, and you carry two of them cleared and ready. Every keystroke you've made automatic is a question you won't run out of time on. Press [clear]{.kbd}, breathe, and begin.
