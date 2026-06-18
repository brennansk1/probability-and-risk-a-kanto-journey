<!--
  appendix: d_calculator_guide
  status: done
-->

# Appendix D — Calculator Guide (TI-30XS MultiView & BA II Plus) {.type-normal}

The SOA lets you bring exactly one of a short list of calculators to Exam P. This book assumes the two that matter: the **TI-30XS MultiView** (recommended — a true two-line scientific calculator with `nCr`, `nPr`, stat lists, and a fraction/decimal toggle) and the **BA II Plus** (the financial calculator most actuarial students already own). Either one will pass the exam; neither one will do the thinking for you. This appendix is a keystroke dictionary for *every computation that recurs in the book*, so you never lose a mark to a fumbled button.

Read it once now, drill the boxed sequences until they are muscle memory, then keep it as a lookup table. Keystrokes are written `[KEY]` for a physical button and `[2nd][KEY]` for a shifted function. On the TI-30XS the shift key is green and labelled **2nd**; on the BA II Plus it is yellow and also labelled **2nd**.

::: trainers-tip
**FIRST, THE TWO HABITS THAT SAVE MARKS**

1. **Store, don't re-type.** Every intermediate value goes into memory, never back through the keypad. Re-typing a rounded number is the single most common silent error on Exam P. TI-30XS: `[STO▸]` then a variable key (`x`, `y`, `z`, `t`, `a`, `b`, `c`). BA II Plus: `[STO][0]` … `[STO][9]`, recall with `[RCL][0]`.
2. **Clear before you start a new problem.** A leftover value in a register is a trap. TI-30XS: `[2nd][CLEAR]` clears all. BA II Plus: `[2nd][MEM]` then `[2nd][CLR Work]`, and `[2nd][CLR TVM]` before any time-value work.
:::

## D.1 — Setup (do this once, before the exam)

The SOA requires a **cleared** calculator at the start of the session (see Appendix E). But the *mode* settings below are not memory — they are display preferences, and you set them so the machine reads out numbers the way you expect.

**TI-30XS MultiView.**

- Press `[mode]`. Choose **FLOAT** (not a fixed number of decimals) so you never lose precision mid-problem; you round only at the very end.
- On the same screen, leave the angle setting on **DEG** (Exam P never uses radians) and the number format on **DEC**.
- The fraction/decimal toggle is the key marked `F◂▸D` (`[2nd]` then the toggle): it flips the answer line between an exact fraction and its decimal. Use it to read $\tfrac{7}{15}$ and $0.4\overline{6}$ off the same result.

**BA II Plus.**

- Set the decimal display to floating with `[2nd][FORMAT]`, key in `9`, then `[ENTER]` (nine places is effectively "show everything"). `[2nd][QUIT]` to exit.
- Confirm the calculation method: `[2nd][FORMAT]`, then `[▼]` repeatedly to the `Chn`/`AOS` line. **AOS** ("algebraic operating system") respects order of operations the way you wrote the expression and is the safer choice; press `[2nd][SET]` to toggle, then `[2nd][QUIT]`.

::: team-rocket
**TRANSMISSION INTERCEPTED — "The calculator does order of operations for me."**

On the BA II Plus in **Chn** (chain) mode it does *not*: `2` `[+]` `3` `[×]` `4` `[=]` returns `20`, not `14`, because chain mode evaluates strictly left to right with no precedence. Team Rocket priced a whole policy this way and quoted twenty Poké-dollars too high. Use **AOS** mode, or wrap every sum in parentheses before you multiply. The TI-30XS always honors precedence — one more reason it is the recommended machine.
:::

## D.2 — Arithmetic, powers, and roots

| Computation | TI-30XS MultiView | BA II Plus |
|---|---|---|
| A power $a^b$ (e.g. $0.9^{10}$) | `0.9` `[^]` `10` `[enter]` | `0.9` `[y^x]` `10` `[=]` |
| A square $a^2$ | `a` `[x²]` | `a` `[x²]` |
| A square root | `[2nd][√ ]` `a` `[enter]` | `a` `[2nd][√x]` |
| A reciprocal $1/a$ | `a` `[x⁻¹]` | `a` `[1/x]` |
| $e^x$ (e.g. $e^{-1.5}$) | `[2nd][eˣ]` `[(-)]` `1.5` `[enter]` | `1.5` `[+/-]` `[2nd][eˣ]` |
| Natural log $\ln$ | `[ln]` `a` `[enter]` | `a` `[LN]` |

The **negative sign** is the dedicated `[(-)]` key on the TI-30XS (and `[+/-]` on the BA II Plus), *not* the subtraction `[−]` key. Confusing them is the second-most-common keypad error; the calculator will error or silently misread.

::: pokedex-entry
**KEYSTROKE №D1 — "At least one" via the complement**

The recurring shape $P(\text{at least one}) = 1 - (\text{miss})^{n}$ — e.g. $1 - 0.9^{10}$ from the Spearow swarm (Chapter 3):

TI-30XS: `1` `[−]` `0.9` `[^]` `10` `[enter]` $\;\to\; 0.6513$.
BA II Plus (AOS): `1` `[−]` `0.9` `[y^x]` `10` `[=]` $\;\to\; 0.6513$.

*Recognition cue:* whenever the question says "at least one," compute the **opposite** — the product of the misses — and subtract from $1$.
:::

## D.3 — Factorials, permutations, and combinations (Chapters 4, 8)

These are the engine of counting and of the binomial and hypergeometric distributions.

| Computation | TI-30XS MultiView | BA II Plus |
|---|---|---|
| Factorial $n!$ | `n` `[2nd][x!]` | `n` `[2nd][x!]` |
| Permutations $\,_nP_r$ | `n` `[prb]` → `nPr` `[enter]` `r` `[enter]` | `n` `[2nd][nPr]` `r` `[=]` |
| Combinations $\binom{n}{r}=\,_nC_r$ | `n` `[prb]` → `nCr` `[enter]` `r` `[enter]` | `n` `[2nd][nCr]` `r` `[=]` |

On the TI-30XS, `[prb]` opens a menu; arrow to `nCr` or `nPr` and press `[enter]`, then type $r$. You type the **$n$ first**, the operator, then the **$r$** — exactly as you read $\binom{n}{r}$ aloud, "$n$ choose $r$."

::: pokedex-entry
**KEYSTROKE №D2 — A binomial probability $\binom{n}{k}p^{k}(1-p)^{\,n-k}$**

For $X\sim\Binom(n=5,\,p=0.3)$, the chance of exactly $k=2$ successes:

TI-30XS: `5` `[prb]`→`nCr` `2` `[×]` `0.3` `[^]` `2` `[×]` `0.7` `[^]` `3` `[enter]` $\;\to\; 0.3087$.

*Recognition cue:* "exactly $k$ of $n$ independent trials" — three factors: the count $\binom{n}{k}$, the successes $p^{k}$, the failures $(1-p)^{n-k}$. Store $\binom{n}{k}$ first if you will reuse it for the next $k$.
:::

## D.4 — One-variable statistics from a list (pmf sums, means, variances)

This is the most under-used feature on the exam and the biggest time-saver for discrete random variables (Chapters 7, 8). You enter the outcomes and their probabilities (as "frequencies") into two lists, and the calculator returns $\E[X]$ and $\SD(X)$ directly — no by-hand summation.

**TI-30XS MultiView.**

1. `[data]` opens the list editor. Clear old data with `[data][data]` → **Clear ALL**.
2. In list **L1**, key the outcome values $x_i$, each followed by `[enter]`.
3. In list **L2**, key the probabilities $p_i$ (they are your frequencies).
4. `[2nd][stat]` → choose **1-Var Stats**. Set `DATA: L1`, `FRQ: L2`, then arrow to **CALC** and `[enter]`.
5. Read off $\bar x = \E[X]$ and $\sigma x$. **Variance is $(\sigma x)^2$** — square the population standard deviation. (Use $\sigma x$, the row marked with the lowercase sigma, *not* $sx$; $sx$ is the sample version with the $n-1$ divisor, which is wrong for a known pmf.)

**BA II Plus.**

1. `[2nd][DATA]` opens the editor; `[2nd][CLR Work]` to clear.
2. Enter each $x_i$ at the `X01`, `X02`, … prompts (press `[ENTER]` after each), and each probability — scaled to a whole-number frequency if the machine balks at decimals — at the `Y01`, `Y02`, … prompts.
3. `[2nd][STAT]`, then `[▼]` to read `n`, `x̄`, `σx`, `sx`. Again $\Var(X)=(\sigma x)^2$.

::: trainers-tip
**WHEN TO REACH FOR THE LIST**

Any time a discrete random variable is given by a small table — Game Corner payouts, a custom pmf, an order-statistic distribution — entering it as a list and squaring $\sigma x$ is faster and far less error-prone than hand-summing $\sum x_i p_i$ and $\sum x_i^2 p_i$. If the probabilities are fractions like $\tfrac{1}{6}$, enter the *counts* (1,1,1,1,1,1) as frequencies; the calculator normalizes them.
:::

## D.5 — The normal distribution and the Z-table (Chapters 9, 14)

Exam P gives you a printed standard-normal table (this book's Appendix C), and **neither calculator computes $\Phi(z)$ directly on the exam** — you look it up. What the calculator does is the *standardization* arithmetic around it.

::: pokedex-entry
**KEYSTROKE №D3 — Standardize then look up: $P(X \le x) = \Phi\!\big(\tfrac{x-\mu}{\sigma}\big)$**

For $X\sim\Normal(\mu=70,\sigma=8)$, find $P(X\le 82)$:

1. Compute $z=\dfrac{82-70}{8}$. TI-30XS: `(` `82` `[−]` `70` `)` `[÷]` `8` `[enter]` $\to 1.50$. **Store it**: `[STO▸][x]`.
2. Look up $\Phi(1.50)=0.9332$ in Appendix C.

For the CLT (Chapter 14), the only change is the denominator: standardize the **sample mean** with $\sigma/\sqrt{n}$, or the **sum** with $\sigma\sqrt{n}$. Compute $\sigma/\sqrt n$ as `8` `[÷]` `[2nd][√ ]` `n` `[enter]` and store it before dividing.
:::

For a **continuity correction** (a normal approximation to a discrete count), add or subtract $0.5$ to the boundary *before* you standardize — see Chapter 14. The keystrokes are identical; only the numerator changes by $0.5$.

## D.6 — Integrals you do by hand, checks you do by calculator

Exam P expects you to integrate pdfs by hand (the calculators on the approved list have no symbolic integrator). The calculator's job is to **evaluate** the antiderivative at the limits without rounding drift.

::: pokedex-entry
**KEYSTROKE №D4 — Evaluating an exponential probability $e^{-a/\theta}$**

The exponential survival probability $P(X>a)=e^{-a/\theta}$ for $X\sim\Expo(\theta)$. With $\theta=5$, $a=3$:

TI-30XS: `[2nd][eˣ]` `[(-)]` `3` `[÷]` `5` `[enter]` $\;\to\; e^{-0.6}=0.5488$.

*Recognition cue:* exponential probabilities are *always* a single $e^{-(\text{limit})/\theta}$ — never an integral you grind out on the exam. Memorize $P(X>a)=e^{-a/\theta}$ and just key the exponent.
:::

For a definite integral $\int_a^b f(x)\,dx$ where you have already found the antiderivative $F$, compute $F(b)$, store it, compute $F(a)$, and subtract — never copy a rounded $F(b)$ back into the keypad.

## D.7 — Time value of money (only where the book uses it)

Exam P itself does not test finance, but a few real-world bridges (and any reader continuing to Exam FM) touch present value. On the BA II Plus the `[N] [I/Y] [PV] [PMT] [FV]` keys solve the time-value equation: enter four, then press `[CPT]` and the fifth. Always `[2nd][CLR TVM]` first. The TI-30XS has no TVM keys — compute present value as a plain power, $PV = FV\,(1+i)^{-n}$, using `[^]` with a negative exponent.

## D.8 — Master quick-reference card

::: trainers-tip
**TEAR-OUT CARD — the keystrokes worth memorizing cold**

| You need… | TI-30XS | BA II Plus |
|---|---|---|
| Clear all memory | `[2nd][CLEAR]` | `[2nd][MEM]` `[2nd][CLR Work]` |
| Store / recall | `[STO▸][x]` / `[x]` | `[STO][0]` / `[RCL][0]` |
| $\binom{n}{r}$ | `n [prb]→nCr r` | `n [2nd][nCr] r` |
| $n!$ | `n [2nd][x!]` | `n [2nd][x!]` |
| $e^{x}$ | `[2nd][eˣ]` | `[2nd][eˣ]` |
| $\ln$ | `[ln]` | `[LN]` |
| $a^{b}$ | `a [^] b` | `a [y^x] b` |
| Mean & SD of a pmf | `[data]` then `[2nd][stat]` 1-Var | `[2nd][DATA]` then `[2nd][STAT]` |
| Variance | square $\sigma x$ | square $\sigma x$ |
| Standardize $z$ | `(x−μ)÷σ`, `[STO▸]` | `(x−μ)÷σ`, `[STO]` |

Two laws above all: **store every intermediate value**, and **clear between problems**.
:::
