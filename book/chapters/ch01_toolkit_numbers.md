<!--
  file: ch01_toolkit_numbers
  tier: C
  outcomes: prereq
  draft1_source: drafts/chapters_draft1/ch01_trainer_school.md
  maps_to: Trainer School, part one — numbers, variables, functions & notation
-->

# The Toolkit I — Numbers, Variables, Functions & Notation {.type-normal}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with Pallet Town highlighted at the start of the journey; Route 1 leads north toward Viridian City." style="width:62%; max-width:420px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 10 — the journey starts in <strong>Pallet Town</strong>, the night before you receive your first Pokémon. First, the tools.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Night Before the Journey"**

It is nearly midnight in Pallet Town. Tomorrow morning you walk into Professor Oak's lab and receive your first Pokémon — and you cannot sleep. So you are *here* instead, in the lab, under a single desk lamp, with Oak's worn copy of *Risk Theory for Trainers* open to a page you do not understand.

Oak slides a Poké Ball across the table, then pulls it back before you can grab it.

"Not yet," he says. "A trainer who can't throw a ball loses in Viridian Forest. A trainer who can't read the *language the exam is written in* loses the moment the first problem appears — and on this journey, it always does." He taps the page. Your Pokédex has an **Actuary Mode**; it poses problems, and solving them earns money, wins battles, and keeps your friends safe. "But the Pokédex assumes you already own the tools. The SOA assumes the same on Exam P — they will *not* teach you the basics. They expect them in your bag already."

He writes a single line on the chalkboard and circles three pieces of it:

$$P(X = k) = \binom{n}{k}\,p^{k}(1-p)^{\,n-k}.$$

"You don't need to *solve* this tonight. But look at it. There is a **letter that stands for a number you don't know yet** — that's $X$. There is a **fraction**, $p$ between $0$ and $1$. There is a thing **raised to a power**, $p^k$. And there is a piece of *notation* you've never seen — $\binom{n}{k}$. Four small languages, braided into one sentence. A trainer who can read each strand reads the whole exam. A trainer who freezes at a fraction or a symbol loses six minutes to panic before the real question even starts."

Pikachu — not yet *your* Pikachu, but watching from a charging cradle on the shelf — cocks its head, unconvinced you can read it.

"So," Oak says, the lamp flickering. "Before I hand you a Pokémon at dawn: prove you can read the instruments. What *is* a variable? What does it mean to raise something to a power, or to write $\sum$? Tonight we make sure that when the exam speaks, you already understand the words."
:::

## Where You Are — 60-Second Retrieval

This is the first chapter, so there is nothing earlier to retrieve — but there is one thing you must already own from grade-school arithmetic, because *everything* below leans on it: you can **add, subtract, multiply, and divide whole numbers and fractions**, and you know that $\tfrac12 = 0.5 = 50\%$ are three names for one quantity. That is the entire floor. If you can do the retrieval below, you are ready; if any line makes you hesitate, that line *is* the lesson, and it is taught in full just ahead.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own arithmetic**

Answer from memory; if any feels shaky, the section that teaches it is below.

1. Compute $\dfrac{3}{4} + \dfrac{1}{8}$. *(Answer: $\tfrac{7}{8}$.)*
2. Write $\tfrac{3}{20}$ as a decimal and a percent. *(Answer: $0.15 = 15\%$.)*
3. What is $2 \times 2 \times 2$? *(Answer: $8$.)*

All three instant? Good — you have the floor. Any hesitation? Don't worry; this whole chapter is built to put it back.
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer, and your first instructor</figcaption>
</figure>

This chapter discharges the **prerequisite language** the SOA assumes but never teaches: the numbers, the variables, the functions, and the symbols every later chapter is written in. Nothing here is a numbered SOA *topic*; it is the alphabet the rest of the book spells with. Treat it as your **Trainer's License** — clear it, and the road north is open.

By the end of this chapter you will be able to:

- **Read the number line** — place numbers, compare them with $<$ and $>$, and write a range of values in **interval notation** like $[0,1]$ or $(0,\infty)$. **[prereq]**
- **Move fluently between fractions, decimals, and percents**, and set up a **proportion** — the native tongue of probability. **[prereq]**
- **Manipulate exponents and logarithms** by their laws, and **solve for a variable trapped in an exponent** by taking logs. **[prereq]**
- **Treat a variable as a stand-in for an unknown number**, build and read an **algebraic expression**, and **rearrange an equation** to isolate any letter. **[prereq]**
- **Read and use function notation** $f(x)$ — including **piecewise** functions — and identify a function's **domain** (allowed inputs) and **range** (possible outputs). **[prereq]**
- **Read and expand summation $\sum$ and product $\prod$ notation** — the single most important symbolic skill for the entire exam. **[prereq]**

> *Exam-weight signpost.* None of this is *tested directly* — but **all** of it is assumed on **every** question. This is a **Tier C** chapter: each idea is taught thoroughly but kept short, and **every piece is independently skippable.** If you already own a concept, its gate lets you prove it in under a minute and move on. Notation introduced here (especially $\sum$ and $\prod$) is reused in literally every chapter that follows.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own the Whole Toolkit?**

Fluent already? Prove it. Work these six, about a minute each, *with correct method*:

1. Write "all $x$ greater than $2$ and at most $5$" in interval notation.
2. Convert $\tfrac{7}{8}$ to a decimal and a percent.
3. Simplify $\dfrac{e^{-3}\,e^{5}}{e^{2}}$ to a single power of $e$, then solve $e^{-x/4} = 0.5$ for $x$ in terms of $\ln$.
4. Solve $A = \dfrac{P}{1+r}$ for $r$.
5. For $f(x) = \begin{cases} 2x & x < 1 \\ x+1 & x \ge 1 \end{cases}$, find $f(0)$ and $f(3)$.
6. Expand and evaluate $\displaystyle\sum_{k=1}^{3} 2k$ and $\displaystyle\prod_{k=1}^{3} k$.

*(Answers: $(2,5]$; $0.875 = 87.5\%$; $e^{0}=1$ and $x = -4\ln 0.5 = 4\ln 2 \approx 2.77$; $r = \tfrac{P}{A}-1$; $f(0)=0,\ f(3)=4$; $\sum = 2+4+6 = 12$, $\prod = 1\cdot2\cdot3 = 6$.)*

Six for six with correct reasoning? **Skip straight to the Gym Challenge** and claim the license. Any miss or hesitation? The teaching below was built for exactly that gap — and each concept has its own one-minute skip-gate, so even a partial owner loses no time.
:::

---

Six tools build the toolkit, in increasing difficulty. We teach them **in order**, each with its own "do you already own this?" skip-check, then a short lesson, then a Pokédex Entry you can carry into the exam:

1. **Numbers & intervals** — the number line and how to name a *range* of values
2. **Fractions, decimals, percents & proportions** — the language of probability
3. **Exponents & logarithms** — powers, their laws, and freeing a trapped variable
4. **Variables & equations** — a letter for an unknown, and how to rearrange a formula
5. **Functions** — the input-output machine, and reading $f(x)$
6. **Summation & product notation** — $\sum$ and $\prod$, the symbols of the whole exam

## Concept 1 — Numbers & Intervals: Naming a Range of Values

::: concept-gate
**DO YOU ALREADY OWN THIS? — Intervals**

A wild Pokémon's level can be anything from $5$ up to *but not including* $20$. Write that set of levels in interval notation.

If you immediately wrote **$[5, 20)$** — square bracket because $5$ *is* allowed, round bracket because $20$ is *not* — you own this. **Skip to Concept 2.** If you're unsure when a bracket is square versus round, this section is for you.
:::

**The one-sentence idea.** *Every quantity in this book lives somewhere on a single left-to-right number line, and a "range" of allowed values is named by its two endpoints plus a bracket that says whether each endpoint is included.*

**A concrete instance.** Picture a ruler stretching forever in both directions: $0$ in the middle, positives to the right, negatives to the left. A probability always sits between $0$ and $1$ — somewhere on the stretch from "impossible" to "certain." A Pokémon's level sits between $1$ and $100$. Each is a *range* carved out of the line.

Take the level example. The wild Pokémon can be level $5, 6, 7, \dots$ up to *just under* $20$. We need a way to write "from $5$ to $20$, including $5$ but not $20$" without listing every value.

**Reason it through in words.** Two things fully describe a range: *where it starts*, *where it ends*, and — for each endpoint — *is that exact value in or out?* "Level $5$ is allowed" means $5$ is **in**. "Up to but not including $20$" means $20$ is **out**. So: start at $5$ (in), end at $20$ (out).

**Surface the tempting wrong idea.** The natural slip is to use the same bracket on both ends — to write $[5,20]$ and call it done. But $[5,20]$ claims level $20$ *is* allowed, which contradicts "but not including $20$." The bracket is not decoration; it carries meaning. **Square bracket $[\,$ = endpoint included; round bracket $(\,$ = endpoint excluded.** Mixing them up changes the answer.

**Translate into notation, one glyph at a time.**

- The symbol $<$ reads **"is less than"**; $>$ reads **"is greater than."** Tip: the *small* end of the wedge points at the *smaller* number, so $3 < 7$ ("three is less than seven").
- Add a bar underneath — $\le$ ("**less than or equal to**") and $\ge$ ("**greater than or equal to**") — to *include* the endpoint.
- An **interval** packs two of these into a pair of brackets. "$5 \le x < 20$" (read "$x$ is at least $5$ and less than $20$") becomes
$$[5, 20) \qquad \text{read aloud: ``the interval from } 5 \text{ included to } 20 \text{ excluded.''}$$
- The symbol $\infty$ reads **"infinity"** — not a number, but "keeps going forever." Because you can never *reach* infinity, its bracket is **always round**: "all values greater than $0$" is $(0, \infty)$.

**The four bracket combinations.** A range $a$ to $b$ has exactly four flavours, depending on which endpoints are in:

| Inequality | Interval | Endpoints included? | Read aloud |
|---|---|---|---|
| $a \le x \le b$ | $[a, b]$ | both | "$a$ to $b$, both ends in" |
| $a \le x < b$ | $[a, b)$ | left only | "$a$ in, $b$ out" |
| $a < x \le b$ | $(a, b]$ | right only | "$a$ out, $b$ in" |
| $a < x < b$ | $(a, b)$ | neither | "strictly between" |

**Ramp the difficulty.**

- *Simplest:* a probability lives in $[0,1]$ — both ends reachable (impossible and certain are real).
- *Twist with infinity:* a Pokémon's weight is some positive number with no upper cap: $(0, \infty)$. The $0$ is excluded (a weight of exactly zero isn't a real Pokémon) and $\infty$ is always round.
- *Edge:* the whole number line is $(-\infty, \infty)$.

**Picture it.** The bracket style *is* the dot style on the line: a filled dot includes the endpoint (square bracket), a hollow dot excludes it (round bracket).

```
   [5, 20)        ●━━━━━━━━━━━━━━━○        (filled 5, hollow 20)
                  5                20
```

**Consolidate.** You can now read any inequality, translate it to interval notation, and — crucially — choose the right bracket for each end. Probabilities will live in $[0,1]$, supports of continuous distributions in things like $(0,\infty)$, all over this book.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Inequalities & Interval Notation**

$$a \le x \le b \;\Leftrightarrow\; [a,b], \qquad a < x < b \;\Leftrightarrow\; (a,b), \qquad x > a \;\Leftrightarrow\; (a, \infty).$$

*In plain terms:* a range is named by its two endpoints; a **square** bracket includes that endpoint, a **round** bracket excludes it. Infinity is unreachable, so its bracket is always round.

*Recognition cue:* the words **"at least / at most"** (included, square) versus **"more than / less than / strictly"** (excluded, round); **"positive"** $\to (0,\infty)$; **"a probability"** $\to [0,1]$.
:::

## Concept 2 — Fractions, Decimals, Percents & Proportions

::: concept-gate
**DO YOU ALREADY OWN THIS? — Fractions, Decimals, Percents**

In a bag of $40$ Poké Balls, $9$ are Great Balls. Express the fraction that are Great Balls as a decimal and a percent. Then: if the *same* proportion held in a bag of $200$, how many would be Great Balls?

If you wrote **$\tfrac{9}{40} = 0.225 = 22.5\%$**, and **$45$** (because $0.225 \times 200 = 45$), you own this. **Skip to Concept 3.** Otherwise, read on.
:::

**The one-sentence idea.** *A fraction, a decimal, and a percent are three different costumes worn by the very same number, and a proportion is the statement that two such numbers are equal — the engine behind almost every probability.*

**A concrete instance.** Brock empties a bag for the road: $40$ balls, of which $9$ are Great Balls. "What share are Great Balls?" he asks. The share is $9$ out of $40$.

**Reason it through in words.** "$9$ out of $40$" is a *fraction*: $\tfrac{9}{40}$ — the part on top, the whole on the bottom. To get its *decimal* costume, you do exactly what the fraction bar tells you to: **divide** $9$ by $40$, giving $0.225$. To get its *percent* costume, "percent" means "per hundred," so you multiply the decimal by $100$ and tack on a $\%$: $0.225 \times 100 = 22.5\%$. Same number, three outfits.

**Surface the tempting wrong idea.** A classic slip is to convert a percent to a decimal by *forgetting to divide by $100$* — reading "$22.5\%$" as the decimal $22.5$. But $22.5$ would be a share of *twenty-two and a half wholes*, which is nonsense for "$9$ out of $40$." **A percent is always the decimal $\times 100$; to undo it, divide by $100$ (slide the point two places left).** So $22.5\% = 0.225$, never $22.5$.

**Translate into notation, one glyph at a time.**

- The fraction bar means *divide*: $\dfrac{a}{b} = a \div b$. The top is the **numerator** (the part), the bottom the **denominator** (the whole).
- $\%$ reads **"percent"** and *means* "$\div 100$": $x\% = \dfrac{x}{100}$.
- A **proportion** is two equal fractions, written with an $=$:
$$\frac{9}{40} = \frac{?}{200} \qquad \text{read aloud: ``9 is to 40 as how-many is to 200.''}$$

**Reason out the proportion (the actual workhorse).** If the *same* share of Great Balls held in a bag of $200$, how many would there be? Two fractions are equal, and you want the unknown top. The clean move is **cross-multiply**: multiply each numerator by the *other* denominator,
$$\frac{9}{40} = \frac{x}{200} \;\Longrightarrow\; 40\,x = 9 \times 200 = 1800 \;\Longrightarrow\; x = \frac{1800}{40} = 45.$$
Or, faster: the share is $0.225$, and $0.225 \times 200 = 45$. Either way, **$45$ Great Balls.**

**Ramp the difficulty.**

- *Simplest:* convert $\tfrac{1}{4}$ → $0.25$ → $25\%$.
- *Twist:* go *backward* — "$\tfrac{1}{8}$ of trainers carry a Potion; how many in a town of $96$?" $\to \tfrac18 \times 96 = 12$.
- *Edge:* a probability is *exactly* a fraction whose value lands in $[0,1]$ (Concept 1) — "favorable outcomes over total outcomes." Every probability you ever compute is one of these three costumes.

**Consolidate.** You can now slide any quantity between fraction, decimal, and percent, and solve a proportion for a missing piece. This is the native arithmetic of probability: $P(\text{Great Ball}) = \tfrac{9}{40} = 0.225$ is a sentence you'll write a thousand times.

::: pokedex-entry
**POKÉDEX ENTRY №02 — Fractions, Decimals, Percents & Proportions**

$$\frac{a}{b} = a \div b, \qquad x\% = \frac{x}{100}, \qquad \frac{a}{b} = \frac{c}{d} \;\Longleftrightarrow\; ad = bc.$$

*In plain terms:* a fraction *is* a division; a percent *is* a number over $100$; a proportion sets two fractions equal, and **cross-multiplying** solves for the missing one.

*Recognition cue:* **"what share / what fraction / what percent"** $\to$ part over whole. **"the same rate applied to a different total"** $\to$ set up a proportion and cross-multiply. A **probability** is just a fraction living in $[0,1]$.
:::

## Concept 3 — Exponents & Logarithms

::: concept-gate
**DO YOU ALREADY OWN THIS? — Exponents & Logs**

Simplify $\dfrac{2^{5}}{2^{2}}$ to a single power of $2$. Then solve $e^{-x/3} = 0.4$ for $x$, leaving your answer in terms of $\ln$.

If you wrote **$2^{3}$** (subtract the exponents) and **$x = -3\ln 0.4 = 3\ln 2.5 \approx 2.75$**, you own this. **Skip to Concept 4.** If the log step felt like a wall, this section is for you.
:::

**The one-sentence idea.** *An exponent is shorthand for repeated multiplication, the exponent laws are just bookkeeping for that repetition, and a logarithm is the tool that pulls a variable back out when it's stuck up in an exponent.*

**A concrete instance.** A line of evolving Pokémon doubles its power each stage: stage $0$ has power $1$, stage $1$ has $2$, stage $2$ has $4$, stage $3$ has $8$. That's $2$ multiplied by itself again and again — exactly what $2^3 = 2\times2\times2 = 8$ means. The little raised number, the **exponent**, just counts *how many copies* of the **base** $2$ are multiplied.

**Reason through the laws in words.** Why do the laws look the way they do? Count copies.

- $2^{5}\cdot 2^{2}$ is "five $2$'s" times "two $2$'s" — **seven** $2$'s in all, so $2^{5+2}=2^{7}$. Multiplying powers **adds** exponents.
- $\dfrac{2^{5}}{2^{2}}$ is five $2$'s with two cancelled off the bottom — **three** left, so $2^{5-2}=2^{3}$. Dividing **subtracts**.
- $\left(2^{2}\right)^{3}$ is "two $2$'s," three times over — **six** $2$'s, so $2^{2\cdot 3}=2^{6}$. A power of a power **multiplies**.
- $2^{0}$: dividing $2^{2}$ by $2^{2}$ leaves *no* copies and equals $1$, so **anything to the zero is $1$.**

These aren't rules to memorize cold — they're just careful counting of copies.

**Surface the tempting wrong idea.** The seductive error is to *multiply the bases* when you multiply powers: writing $2^{5}\cdot 2^{2} = 4^{7}$. But the base never changes — you're still multiplying $2$'s, just *more* of them. **Same base: add the exponents, keep the base.** $2^{5}\cdot 2^{2} = 2^{7} = 128$, not $4^{7}$.

**Now the logarithm — translate one glyph at a time.** Often a variable is *trapped* in the exponent, like $e^{-x/3} = 0.4$, and no amount of exponent arithmetic frees it. We need the inverse operation.

- $e$ is a fixed number, $e \approx 2.718$ — the most common base in this book (it makes exponential decay clean). $e^{t}$ reads "**$e$ to the $t$**."
- The **natural logarithm** $\ln$ is the *undo button* for $e^{(\cdot)}$. By definition, $\ln\!\left(e^{t}\right) = t$: it reaches into the exponent and hands you back whatever was up there. Read $\ln y$ as "**the power you must raise $e$ to in order to get $y$.**"
- The log laws mirror the exponent laws — logs turn products into sums and pull powers out front:
$$\ln(xy) = \ln x + \ln y, \qquad \ln\!\frac{x}{y} = \ln x - \ln y, \qquad \ln\!\left(x^{r}\right) = r\,\ln x.$$

**Derive the solving move from the instance.** To free $x$ from $e^{-x/3} = 0.4$, apply the undo button to *both* sides — take $\ln$ of each:
$$\ln\!\left(e^{-x/3}\right) = \ln(0.4) \;\Longrightarrow\; -\frac{x}{3} = \ln(0.4) \;\Longrightarrow\; x = -3\ln(0.4) \approx 2.75.$$
The $\ln$ cancelled the $e$ and dropped the exponent down to ground level, where ordinary algebra finishes the job.

**Ramp the difficulty.**

- *Simplest:* $\dfrac{a^{m}}{a^{n}} = a^{m-n}$, e.g. $\tfrac{e^{5}}{e^{2}} = e^{3}$.
- *Twist:* a product of exponentials with the *same* base, $e^{-x/\theta}\cdot e^{-d/\theta} = e^{-(x+d)/\theta}$ — add the exponents (this exact move recurs in the exponential distribution, later).
- *Edge:* a *negative* exponent means reciprocal: $2^{-3} = \tfrac{1}{2^{3}} = \tfrac18$. And $a^{1/2} = \sqrt{a}$ — a fractional exponent is a root.

**Consolidate.** You can now combine powers by their laws, recognize $a^{0}=1$ and $a^{-n} = 1/a^{n}$, and — the load-bearing skill — solve for a variable buried in an exponent by taking $\ln$ of both sides.

::: pokedex-entry
**POKÉDEX ENTRY №03 — Exponents & Logarithms**

$$a^{m}a^{n} = a^{m+n}, \quad \frac{a^{m}}{a^{n}} = a^{m-n}, \quad \left(a^{m}\right)^{n} = a^{mn}, \quad a^{0}=1, \quad a^{-n} = \frac{1}{a^{n}}.$$
$$\ln(xy)=\ln x + \ln y, \quad \ln\frac{x}{y} = \ln x - \ln y, \quad \ln\!\left(x^{r}\right) = r\ln x, \quad \ln\!\left(e^{t}\right) = t.$$

*In plain terms:* an exponent counts repeated multiplications; same-base products **add** exponents (never multiply the base). A logarithm is the inverse of an exponential — it frees a variable trapped in the exponent.

*Recognition cue:* a product of same-base exponentials $\to$ **add** exponents. A variable **stuck in an exponent** you must solve for $\to$ **take $\ln$ of both sides.**
:::

## Concept 4 — Variables & Equations: A Letter for an Unknown

::: concept-gate
**DO YOU ALREADY OWN THIS? — Rearranging Equations**

The relationship between an item's list price $P$, a discount rate $r$, and its sale price $A$ is $A = P(1 - r)$. Solve this for $r$ in terms of $A$ and $P$.

If you wrote **$r = 1 - \dfrac{A}{P}$** (divide by $P$, then isolate $r$), you own this. **Skip to Concept 5.** If isolating the trapped letter felt uncertain, read on.
:::

**The one-sentence idea.** *A variable is just a placeholder letter standing in for a number you don't yet know, and "solving" an equation means peeling operations off that letter — doing the same thing to both sides — until it stands alone.*

**A concrete instance.** At the Celadon department store, a TM's sale price is its list price knocked down by a discount rate. List price $P$, discount rate $r$ (a fraction like $0.2$ for "$20\%$ off"), sale price $A$. The store's sign states the rule:
$$A = P(1 - r).$$
Here $P, r, A$ are **variables** — letters that hold whatever the actual numbers turn out to be. If $P = 50$ and $r = 0.2$, then $A = 50(1 - 0.2) = 50(0.8) = 40$. The same one rule covers *every* item in the store; that reuse is the entire point of a variable.

**Reason through "solving" in words.** Now flip the question: you *see* the sale price $A$ and the list price $P$, and want the discount rate $r$. You must get $r$ alone. Look at what is "stacked on" $r$: it's wrapped in $(1-r)$, and that whole thing is *multiplied* by $P$. Undo the operations in reverse order, doing the same to both sides to keep the scale balanced:

1. $r$ is multiplied by $P$ (inside the parentheses). **Divide both sides by $P$:**
$$\frac{A}{P} = 1 - r.$$
2. $r$ is subtracted from $1$. **Move it across:** add $r$ to both sides and subtract $\tfrac{A}{P}$:
$$r = 1 - \frac{A}{P}.$$

The letter now stands alone — *solved*.

**Surface the tempting wrong idea.** A frequent slip is to do an operation to *one* term instead of the *whole side*. For instance, from $A = P(1-r)$, "cancelling" the $P$ on the right by simply deleting it: $A = 1 - r$. But the $P$ multiplies the *entire* parenthesis, so it must be divided out of the *entire* other side too. **Whatever you do, do it to the whole side — an equation is a balance scale, not a single pan.** The correct first step is $\tfrac{A}{P} = 1 - r$.

**Translate into notation.** The two moves above are the only two you ever need:

- **Inverse operations undo each other:** $+$ undoes $-$, $\times$ undoes $\div$, $\ln$ undoes $e^{(\cdot)}$ (Concept 3). To strip an operation off your target letter, apply its inverse to *both* sides.
- The phrase **"solve for $r$"** means: rearrange until the equation reads $r = (\text{stuff with no } r \text{ in it})$.

**Ramp the difficulty.**

- *Simplest:* solve $2x = 10$ → divide by $2$ → $x = 5$.
- *Twist (fraction):* solve $A = \dfrac{P}{1+r}$ for $r$. Multiply by $(1+r)$: $A(1+r) = P$; divide by $A$: $1 + r = \tfrac{P}{A}$; subtract $1$: $r = \tfrac{P}{A} - 1$.
- *Edge (the variable appears twice):* if a letter shows up in two places, first **gather** all its terms on one side, then **factor it out** before dividing — e.g. $xy + x = 5 \Rightarrow x(y+1) = 5 \Rightarrow x = \tfrac{5}{y+1}$.

**Consolidate.** You can now read a formula as a reusable rule, plug numbers in, and — the real skill — *rearrange* it to isolate any letter you want. Every "given the formula for the mean, solve for the parameter" step later in the book is exactly this move.

::: pokedex-entry
**POKÉDEX ENTRY №04 — Variables & Rearranging Equations**

To **solve for a target letter**: do the *same operation to both whole sides*, using inverse operations ($+\!/\!-$, $\times\!/\!\div$, $e^{(\cdot)}\!/\ln$) to peel everything off the target until it stands alone. If the letter appears twice, **gather then factor**.

*In plain terms:* a variable is a stand-in for an unknown number; an equation is a balance; "solving" is unwrapping the target letter one inverse operation at a time, applied to the entire side.

*Recognition cue:* **"solve for ___," "express ___ in terms of ___," "find the parameter given the formula."** Identify the trapped letter, then peel off its operations in reverse.
:::

## Concept 5 — Functions: The Input-Output Machine

::: concept-gate
**DO YOU ALREADY OWN THIS? — Functions**

A Poké Mart charges a flat $\$200$ for any order of $5$ or fewer Potions, and $\$35$ per Potion for larger orders: $\;C(n) = \begin{cases} 200 & n \le 5 \\ 35n & n > 5 \end{cases}.$ Find $C(4)$ and $C(10)$, and state the domain (allowed values of $n$).

If you wrote **$C(4) = 200$, $C(10) = 350$**, and domain "$n$ a non-negative integer," you own this. **Skip to Concept 6.** If function notation or the piecewise pick felt shaky, read on.
:::

**The one-sentence idea.** *A function is a machine with one input slot and one output: feed it a number, it returns exactly one number by a fixed rule, and $f(x)$ is just the name for "the output when the input is $x$."*

**A concrete instance.** The Poké Mart's pricing is a rule: put in a *number of Potions*, get out a *cost*. Feed it $3$, it returns the cost of $3$ Potions. That is a function. We give the rule a name, $C$ (for cost), and write $C(n)$ — read "**$C$ of $n$**" — meaning "the cost when you order $n$ Potions." The letter $n$ in the parentheses is the **input**; the value $C(n)$ is the **output**.

**Reason it through in words.** Say the rule is $C(n) = 35n$ ($\$35$ each). To find the cost of $4$ Potions, you **substitute** $4$ wherever $n$ appears: $C(4) = 35 \times 4 = 140$. The notation $C(4)$ does *not* mean "$C$ times $4$" — the parentheses here mean "*evaluate the rule at input $4$*." That distinction trips up nearly everyone at first, so say it out loud: "$C$ **of** four," not "$C$ **times** four."

**Surface the tempting wrong idea.** The big one: reading $f(x)$ as multiplication, $f \cdot x$. It isn't. $f$ is the *name of a machine*, not a number, and $f(x)$ means "run the machine on $x$." A second slip, for **piecewise** functions (different rules on different input ranges): using the wrong piece. The pricing above is piecewise — flat for small orders, per-unit for large — and you must first check *which range your input falls in* before applying a rule.

**Translate into notation, one glyph at a time.**

- $f(x)$ reads "**$f$ of $x$**" = the output of function $f$ at input $x$. To evaluate, *substitute* the input everywhere $x$ appears.
- The **domain** is the set of inputs the function is *allowed* to take (you can't order $-3$ Potions, so $n \ge 0$). The **range** is the set of outputs it can *produce*.
- A **piecewise** function lists several rules with the input-conditions they apply to, stacked inside a big brace:
$$C(n) = \begin{cases} 200 & n \le 5 \\ 35n & n > 5. \end{cases}$$
Read it: "$C(n)$ equals $200$ **when** $n \le 5$, and equals $35n$ **when** $n > 5$."

**Work the concrete instance fully.** For the piecewise mart rule:

- $C(4)$: the input $4$ satisfies $n \le 5$, so use the **top** piece: $C(4) = 200$.
- $C(10)$: the input $10$ satisfies $n > 5$, so use the **bottom** piece: $C(10) = 35 \times 10 = 350$.

Pick the piece *first* (by checking the condition), then evaluate.

**Ramp the difficulty.**

- *Simplest:* $f(x) = x^{2}$, so $f(3) = 9$.
- *Twist (domain matters):* $g(x) = \tfrac{1}{x}$ has domain "all $x$ except $0$" — you can't divide by zero, so $0$ is *excluded* from the inputs.
- *Edge (the function we'll live in):* a **probability density** is a function $f(x)$ whose output is never negative and whose support (the inputs where it's positive) is an interval from Concept 1 — every distribution in this book is "a function with a domain and a range." This is the bridge into the whole second half of the course.

**Consolidate.** You can now read $f(x)$ as "run machine $f$ on input $x$," evaluate it by substitution, choose the right branch of a piecewise function, and state a domain and range. Probability mass functions, density functions, and cumulative distribution functions are *all* just functions you'll feed numbers into.

::: pokedex-entry
**POKÉDEX ENTRY №05 — Functions & Function Notation**

$f(x)$ = the **one output** of the rule $f$ at **input** $x$ (read "$f$ of $x$" — *not* "$f$ times $x$"). Evaluate by substituting the input everywhere $x$ appears. The **domain** is the allowed inputs; the **range** is the possible outputs. A **piecewise** function applies a different rule on each input range.

*In plain terms:* a function is a one-in, one-out machine; the parentheses mean "evaluate at," not "multiply." For piecewise rules, first find which range the input is in, *then* apply that piece.

*Recognition cue:* anytime you see $f(x), P(x), F(x), S(x)$ — these are **functions**: substitute the input. A $\begin{cases}\cdots\end{cases}$ brace means **piecewise** — check the condition first.
:::

## Concept 6 — Summation $\sum$ and Product $\prod$ Notation

::: concept-gate
**DO YOU ALREADY OWN THIS? — Sigma & Pi Notation**

Expand and evaluate $\displaystyle\sum_{k=1}^{4} k^{2}$ and $\displaystyle\prod_{k=1}^{4} k$.

If you wrote **$1 + 4 + 9 + 16 = 30$** and **$1 \cdot 2 \cdot 3 \cdot 4 = 24$**, you own the single most important notation in this book. **Skip to the Gym Challenge.** If $\sum$ or $\prod$ looks like a hieroglyph, read on — this is the one section you cannot afford to skim.
:::

**The one-sentence idea.** *The big sigma $\sum$ is nothing but shorthand for "add up a list," and the big pi $\prod$ is shorthand for "multiply a list" — you read either by letting a counter walk through every value and gluing the terms together with $+$ or $\times$.*

**A concrete instance.** You've caught four Pokémon with experience points $30, 30, 60, 120$. Their total experience is $30 + 30 + 60 + 120 = 240$. Easy to write with four terms — but distributions in this book sometimes add *infinitely* many terms, and writing them all out is impossible. We need a compact instruction that says "add up this whole pattern." That instruction is $\sum$.

**Reason through how to read it.** A summation has four parts working together — think of it as a tiny machine with a counter:

$$\sum_{k=1}^{4} a_k.$$

- $\sum$ (capital Greek **sigma**) means **"add up."**
- $k$ is the **index** — a temporary counter, like a loop variable.
- $k=1$ below the sigma is where the counter **starts**.
- $4$ above the sigma is where it **stops**.
- $a_k$ is the **term** — the thing you compute for each value of $k$.

To *expand* it, let $k$ march from the bottom number to the top, plug each into the term, and join with $+$:
$$\sum_{k=1}^{4} a_k = a_1 + a_2 + a_3 + a_4.$$
For our experience points ($a_1=30,\ a_2=30,\ a_3=60,\ a_4=120$): the sum is $240$. The notation said exactly that, just compactly.

**Surface the tempting wrong idea.** Two classic misreadings. First, treating the index $k$ as if it were a fixed number that survives the sum — it does **not**; $k$ is a *temporary counter* that's used up inside, so the answer never contains a $k$. Second, getting the **count of terms** wrong: $\sum_{k=1}^{4}$ has **four** terms ($k=1,2,3,4$), but $\sum_{k=0}^{4}$ has **five** ($k=0,1,2,3,4$). Always check both endpoints; off-by-one here corrupts every later total. **The number of terms is (top $-$ bottom $+ 1$).**

**Translate the product symbol.** Swap "add" for "multiply" and you get the **product**:

$$\prod_{k=1}^{4} a_k = a_1 \cdot a_2 \cdot a_3 \cdot a_4 \qquad (\Pi \text{ is capital Greek ``pi'' — read ``the product of''}).$$

Everything else — index, start, stop, term — works identically; you just glue with $\times$ instead of $+$. For $a_k = k$:
$$\prod_{k=1}^{4} k = 1 \cdot 2 \cdot 3 \cdot 4 = 24.$$
That pattern — "multiply the whole numbers from $1$ up to $n$" — is so common it has its own name and symbol, the **factorial** $n!$, so $4! = 24$. (You'll meet $n!$ everywhere in counting.)

**Ramp the difficulty.**

- *Simplest:* $\displaystyle\sum_{k=1}^{3} k = 1 + 2 + 3 = 6$.
- *Twist (a term with a formula):* $\displaystyle\sum_{k=1}^{3} 2k = 2 + 4 + 6 = 12$ — substitute the *whole* term $2k$ at each step, not just $k$.
- *Twist (a constant term):* $\displaystyle\sum_{k=1}^{5} 7 = 7+7+7+7+7 = 35$ — when the term doesn't mention $k$, you just add the constant once per step: $5 \times 7$.
- *Edge (infinite sum):* $\displaystyle\sum_{k=0}^{\infty} a_k$ means "keep going forever"; whether it adds up to a finite number is a question for Chapter 2 (series). For now, just *read* it: "add $a_0 + a_1 + a_2 + \cdots$ without stopping."

**Picture it (the index as a walking counter).** Lay the steps in a table — this is exactly how to expand any sum or product by hand under exam pressure:

| step $k$ | term $2k$ | running sum | term $k$ | running product |
|---|---|---|---|---|
| $1$ | $2$ | $2$ | $1$ | $1$ |
| $2$ | $4$ | $6$ | $2$ | $2$ |
| $3$ | $6$ | $12$ | $3$ | $6$ |
| $4$ | $8$ | $20$ | $4$ | $24$ |

The counter walks down the rows; the last "running" cell is your answer.

**Consolidate.** You can now read any $\sum$ or $\prod$, expand it by walking the index from start to stop, count the terms correctly, and recognize $\prod_{k=1}^{n} k = n!$. Every expectation, every variance, every distribution total in this book is written with one of these two symbols — owning them now means the rest of the course speaks a language you already read.

::: pokedex-entry
**POKÉDEX ENTRY №06 — Summation & Product Notation**

$$\sum_{k=m}^{n} a_k = a_m + a_{m+1} + \cdots + a_n, \qquad \prod_{k=m}^{n} a_k = a_m \cdot a_{m+1} \cdots a_n, \qquad \prod_{k=1}^{n} k = n!.$$

*In plain terms:* $\sum$ says "**add up** the terms," $\prod$ says "**multiply** the terms," as the index $k$ walks from the bottom value to the top. The index is temporary — it never appears in the answer.

*Recognition cue:* the symbol $\sum$ $\to$ **add**; $\prod$ $\to$ **multiply**. The number of terms is **(top $-$ bottom $+1$)** — watch the endpoints to avoid off-by-one. $\prod_{1}^{n} k$ is the factorial $n!$.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Oak drills the toolkit before you leave Pallet Town</figcaption>
</figure>

Four examples, fading from fully narrated to exam-speed. Each names its archetype and back-references the Pokédex Entry it exercises.

### Worked Example 1.1 — Reading the Number Line (full narration; understanding-first)

**ARCHETYPE:** *translate a verbal range into interval notation, choosing brackets.*

**Setup.** The Pokédex reports that a wild encounter's level is "at least $10$ but below $40$," and that its probability of fleeing is "somewhere strictly between $0$ and $1$." Write each as an interval.

**Step 1 — Identify what's included.** Take the levels first. *"At least $10$"* means $10$ **is allowed** — endpoint *included* — so the left bracket is **square**: $[10,\dots$. *"Below $40$"* means $40$ is **not** reached — endpoint *excluded* — so the right bracket is **round**: $\dots 40)$.

**Step 2 — Assemble.** Combining: $[10, 40)$. Read aloud, "ten included to forty excluded." Sanity check against the words: level $10$? allowed ✓. Level $39$? allowed ✓. Level $40$? not allowed ✓.

**Step 3 — The flee probability.** *"Strictly between $0$ and $1$"* — the word *strictly* excludes **both** endpoints, so both brackets are round: $(0, 1)$.

**Step 4 — Check & pitfall.** Endpoints match the words in every case. **Pitfall:** defaulting to square brackets on both ends out of habit — here that would wrongly *include* level $40$ and a flee probability of exactly $0$ or $1$. The bracket carries meaning; read the words *"at least / below / strictly"* before choosing. *(Back-ref: Entry №01.)*

### Worked Example 1.2 — One Number, Three Costumes (partial guidance)

**ARCHETYPE:** *convert among fraction/decimal/percent and scale a proportion.*

**Setup.** Of $25$ Pokémon logged on Route 1, $4$ are Pidgey. (a) Express the Pidgey share as a fraction, decimal, and percent. (b) If the same share held over a full day's $300$ encounters, how many Pidgey would you expect?

**(a)** *Your move: form the part-over-whole fraction, then divide, then $\times 100$.*
$$\frac{4}{25} = 4 \div 25 = 0.16 = 16\%.$$

**(b)** Same rate, bigger total — a proportion. Either cross-multiply $\tfrac{4}{25} = \tfrac{x}{300}$, or just scale the decimal:
$$x = 0.16 \times 300 = 48 \text{ Pidgey}.$$

**Check & pitfall.** $48$ out of $300$ is indeed $\tfrac{48}{300} = 0.16$ ✓. **Pitfall:** reading $16\%$ as the decimal $16$ (forgetting the $\div 100$); that would predict $16 \times 300 = 4800$ Pidgey, absurd for $300$ encounters. *(Back-ref: Entry №02.)*

### Worked Example 1.3 — Freeing a Trapped Variable (light guidance)

**ARCHETYPE:** *solve for a variable stuck in an exponent via logarithms.*

**Setup.** A fainted Pokémon's remaining-energy fraction after time $t$ is $e^{-t/5}$. At what time $t$ is exactly $30\%$ of its energy left? Leave the answer in terms of $\ln$, then give a decimal.

Set the model equal to $0.30$ and take $\ln$ of both sides to drop the exponent:
$$e^{-t/5} = 0.30 \;\Longrightarrow\; -\frac{t}{5} = \ln(0.30) \;\Longrightarrow\; t = -5\ln(0.30) \approx 6.02.$$

**Check & pitfall.** At $t=0$, $e^{0}=1$ (full energy) ✓; energy falls as $t$ grows, so reaching $30\%$ at a positive $t \approx 6$ is sensible ✓. **Pitfall:** forgetting that $\ln(0.30)$ is *negative*, so the two minus signs combine to give a *positive* $t$. *(Back-ref: Entry №03.)*

### Worked Example 1.4 — A Function and a Sum at Exam Speed

**ARCHETYPE:** *evaluate a piecewise function, then total its outputs with $\sum$.*

**Setup.** A Pokémon Center charges a healing fee $f(p) = \begin{cases} 0 & p \le 2 \\ 50(p-2) & p > 2 \end{cases}$ for a party of $p$ Pokémon (the first two are free). You bring parties of sizes $1, 3$, and $5$ over three visits. Find the total fee $\displaystyle\sum_{i} f(p_i)$.

Evaluate each by picking the right piece, then sum:
$$f(1) = 0,\quad f(3) = 50(3-2) = 50,\quad f(5) = 50(5-2) = 150,$$
$$\sum f = 0 + 50 + 150 = 200.$$

**Check & pitfall.** Each input routed to the correct branch ($1 \le 2$ → free; $3,5 > 2$ → charged) ✓; three terms summed, total $\$200$. **Pitfall:** applying the $50(p-2)$ rule to $p=1$ (which would give a *negative* fee) instead of checking the condition first. *(Back-ref: Entries №05, №06.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — say the bracket out loud**

Under time pressure, read every range as a sentence before choosing brackets: *"at least"* and *"at most"* are **square** (included); *"more than," "less than," "strictly," "positive"* are **round** (excluded); **infinity is always round**. Saying it aloud kills the reflex to slap square brackets on both ends.
:::

::: trainers-tip
**TRAINER'S TIP — percent ↔ decimal in one motion**

To convert a percent to a decimal, slide the point **two places left** ($22.5\% \to 0.225$); to go back, slide it two places right. On the TI-30XS the `%` key does this automatically — but knowing the slide means you never trust a mis-keyed entry.
:::

::: trainers-tip
**TRAINER'S TIP — take $\ln$ the instant a variable is in an exponent**

If your unknown is *upstairs* in an exponent, no factoring will free it — apply $\ln$ to both sides immediately. On the calculator, $-5\ln(0.30)$ is `5` `×` `LN` `0.30` `=` then negate; expect a *positive* result because $\ln$ of a number below $1$ is negative.
:::

::: trainers-tip
**TRAINER'S TIP — count the terms in a $\sum$ before you add**

The number of terms in $\sum_{k=m}^{n}$ is $n - m + 1$, **not** $n - m$. A sum from $k=0$ to $k=4$ has **five** terms. Miscounting here silently breaks every expectation and variance you'll compute later — verify both endpoints first, every time.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

Team Rocket has rigged a balloon that "guarantees" catching a rare Pokémon. Meowth reads the Pokédex's flee model off the screen: the chance of fleeing each turn is $e^{-t/4}$, and he wants the turn $t$ at which the flee chance drops to half.

"Easy!" Meowth crows. "We just plug in! $e^{-t/4} = 0.5$, so… uh… $t = 0.5$! Half a turn!"

"Half a turn?!" James squints. "That doesn't even — there's no such thing as half a turn."

"Details!" Meowth waves him off, sets the trap for turn "$0.5$," and of course it fires at the wrong moment. The Pokémon strolls away untouched. "Looks like Team Rocket's *blasting off* again!"

**Where it fails:** Meowth treated the variable $t$ as if it were sitting at ground level, just *reading off* the right-hand side. But $t$ is **trapped in the exponent** — you cannot free it by inspection. You must take $\ln$ of both sides (Entry №03): $-\tfrac{t}{4} = \ln(0.5)$, so $t = -4\ln(0.5) = 4\ln 2 \approx 2.77$ turns. **The fix:** the instant your unknown is upstairs in an exponent, reach for the logarithm — never just "plug and read."
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

These six tools are not busywork — they are the literal *reading skills* of an actuary's day.

An insurance policy is described almost entirely in the language of this chapter. A **deductible** and a **policy limit** define an *interval* of losses the insurer actually pays — exactly the bracket notation of Concept 1. A **loss ratio** ("claims paid as a share of premium collected") is a *fraction / percent / proportion*, Concept 2, and an actuary slides between those costumes all day. The premium an insurer charges is a *function* of the insured's risk characteristics — Concept 5's $f(x)$, fed a customer's profile, returning a price. And the **expected claim cost** — the number every premium is built on — is a *sum* $\sum_{k} (\text{outcome}_k)\cdot(\text{its probability})$ over all the ways a loss can happen, which is Concept 6's $\sum$ made flesh. The exponential decay you solved with a logarithm (Concept 3) is how mortality and lapse rates are modeled.

*Series bridge:* the $\sum$ and $\prod$ notation you just learned to read is the backbone of every formula on **Exam P**, **Exam FM** (annuities are sums), and **Exam STAM** (loss models are sums and integrals). Owning the notation now is owning the alphabet of the entire credentialing path.

*Transfer check:* could you do this with **no Pokémon in it?** "A policy pays losses between a \$500 deductible and a \$10{,}000 limit; write that payment interval, and if 12 of 80 claims hit the limit, what percent is that?" Interval $[500, 10000]$ on the loss, $\tfrac{12}{80} = 0.15 = 15\%$. If you can do that, the skill has transferred.
:::

## The Gym Battle — Trainer's License Capstone

**Oak's License Exam.** This is not a gym badge — it is your **Trainer's License**, and Oak administers it personally at first light. He poses one integrated problem that fuses every tool in the chapter. Clear it, and you may take a Pokémon onto Route 1.

> **Oak's problem.** "A traveling merchant on Route 1 prices Repels by a rule. For an order of $n$ Repels, the per-unit price (in Poké-dollars) is
> $$f(n) = \begin{cases} 30 & n \le 3 \\ 30\,(0.9)^{\,n-3} & n > 3, \end{cases}$$
> so beyond three units each *additional* unit shaves the price by a factor of $0.9$. Four tasks, one breath each:
> **(a)** State the domain of $n$ (what inputs make sense).
> **(b)** Compute the per-unit price for an order of $5$, i.e. $f(5)$.
> **(c)** Beyond what order size does the per-unit price first drop **below** $20$? Set up $30(0.9)^{n-3} < 20$ and solve for the threshold using a logarithm; report the smallest whole $n$.
> **(d)** A buyer purchases orders of sizes $2, 4$, and $6$. Using your prices, write the *total* per-unit-price they were quoted as a sum $\sum_{i} f(n_i)$ and evaluate it."

**ARCHETYPE:** *integrative — domain + piecewise evaluation + exponent/log solve + summation.*

**Identify.** (a) is a domain statement (Concept 5); (b) is a piecewise evaluation (Concept 5) using a power (Concept 3); (c) frees a variable from an exponent with a log (Concept 3) inside an inequality (Concept 1); (d) totals function outputs with $\sum$ (Concept 6).

**Step-by-step solution.**

**(a)** You can only order a whole, non-negative number of Repels, so the domain is the non-negative integers: $n \in \{0, 1, 2, \dots\}$. (In interval shorthand for the *continuous* relaxation, $[0, \infty)$ — but the real inputs are whole numbers.)

**(b)** Input $5$ satisfies $n > 3$, so use the bottom piece with exponent $n - 3 = 2$:
$$f(5) = 30\,(0.9)^{5-3} = 30\,(0.9)^{2} = 30(0.81) = 24.30.$$

**(c)** Solve $30(0.9)^{n-3} < 20$. Divide both sides by $30$ (Concept 4):
$$(0.9)^{n-3} < \frac{20}{30} = 0.6\overline{6}.$$
The unknown is *trapped in the exponent*, so take $\ln$ of both sides (Concept 3) — and note $\ln(0.9)$ is **negative**, so dividing by it **flips the inequality**:
$$(n-3)\ln(0.9) < \ln(0.6\overline{6}) \;\Longrightarrow\; n - 3 > \frac{\ln(0.6\overline{6})}{\ln(0.9)} = \frac{-0.4055}{-0.1054} \approx 3.85.$$
So $n - 3 > 3.85$, i.e. $n > 6.85$. The smallest **whole** order size is $n = 7$. *(Check: $f(7) = 30(0.9)^{4} = 30(0.6561) = 19.68 < 20$ ✓, while $f(6) = 30(0.9)^{3} = 21.87 > 20$.)*

**(d)** Evaluate each price by piece, then sum (Concept 6). Input $2 \le 3$ uses the flat piece; inputs $4, 6 > 3$ use the decay piece:
$$f(2) = 30, \quad f(4) = 30(0.9)^{1} = 27, \quad f(6) = 30(0.9)^{3} = 21.87.$$
$$\sum_{i} f(n_i) = 30 + 27 + 21.87 = 78.87.$$

**Check & pitfall.** Prices fall as orders grow past $3$ (✓ with the "$0.9$ shaves it" story), and each input was routed to the correct piece. **The capstone trap** is part (c): forgetting that $\ln(0.9) < 0$ and *not flipping the inequality* when dividing by it — which would give the wrong threshold direction. Whenever you divide an inequality by a negative number, the $<$ becomes $>$. Clear all four and the **Trainer's License** is yours — Route 1 is open.

> "That," Oak says, pocketing the chalk, "is reading the instruments. You didn't freeze at a single symbol. Take your Pokémon — and *go*."

## The Gym Challenge — Problem Set

::: problem-set
**TEST-OUT INSTRUCTIONS.** Work this set timed (about $3$–$4$ min/problem; these are mechanics, not marathons), then check the **Answer Key** below. Hit the mastery bar (**80%+ with correct method**) and the license is yours. Problems are listed first; full worked solutions follow afterward (never interleaved). Markers: 🔴 Poké Ball = routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (mechanics)

**C1.1.** 🔴 A wild Pokémon's catch rate is "at least $0.2$ and at most $0.55$." Write this set of catch rates in interval notation.

**C1.2.** 🔴 Of $50$ encounters on Route 1, $7$ are Rattata. Express the Rattata share as a fraction, a decimal, and a percent.

**C1.3.** 🔴 Simplify $\dfrac{e^{6}\,e^{-2}}{e^{3}}$ to a single power of $e$, and give its decimal value.

**C1.4.** 🔴 Solve $2L + 5 = 17$ for $L$.

**C1.5.** 🔴 For $f(x) = 3x - 4$, compute $f(2)$ and $f(0)$.

**C1.6.** 🔴 Expand and evaluate $\displaystyle\sum_{k=1}^{4} (2k + 1)$.

**C1.7.** 🟡 A potion's price is $\$15$, marked down by $40\%$. Find the sale price two ways: as $15 \times (1 - 0.40)$, and by subtracting "$40\%$ of $15$."

### Gym Battles (true SOA difficulty)

**C1.8.** 🟡 Solve $e^{-t/6} = 0.25$ for $t$, leaving the answer in terms of $\ln$, then give a decimal.

**C1.9.** 🟡 The relationship between premium $P$, claim cost $C$, and expense load $e$ is $P = \dfrac{C}{1 - e}$. Solve for $e$ in terms of $P$ and $C$.

**C1.10.** 🟡 For the piecewise fee $g(n) = \begin{cases} 0 & n \le 2 \\ 25(n - 2) & n > 2 \end{cases}$, compute $g(2)$, $g(5)$, and the total $g(1) + g(3) + g(6)$.

**C1.11.** 🟡 Evaluate $\displaystyle\sum_{k=0}^{3} 4 \cdot (0.5)^{k}$ by expanding all four terms (do **not** use a series shortcut — just add the terms).

**C1.12.** 🟡 Evaluate the product $\displaystyle\prod_{k=1}^{5} k$ and state which factorial it equals.

**C1.13.** 🔵 A Pokémon's remaining-HP fraction after $t$ turns is $(0.8)^{t}$. After how many *whole* turns does it first drop below $0.5$? Set up $(0.8)^{t} < 0.5$ and solve with a logarithm.

### Elite Challenge (integrative / stretch)

**C1.14.** 🔵 *(Notation + functions.)* Define $a_k = k(k+1)$ for $k = 1, 2, 3, 4$. (a) Write out the four terms. (b) Evaluate $\displaystyle\sum_{k=1}^{4} a_k$. (c) Evaluate $\displaystyle\prod_{k=1}^{2} a_k$.

**C1.15.** 🔵 *(Proportion + interval + percent.)* A policy pays a loss only on the interval $[200, 5000]$ (a \$200 deductible and a \$5000 limit). Of $80$ recorded losses, $20$ fall *below* \$200 (the insurer pays nothing) and $8$ exceed \$5000 (capped at the limit). (a) What percent of losses fall *inside* the paid interval $[200, 5000]$? (b) Write that count as a fraction in lowest terms.

**C1.16.** 🔵 *(Capstone in miniature — exponent solve feeding a decision.)* A Repel's effectiveness $t$ steps after use is $E(t) = (0.95)^{t}$. The trainer re-applies once effectiveness drops below $0.60$. (a) Solve $(0.95)^{t} < 0.60$ for the threshold $t$ with a logarithm. (b) Report the smallest whole number of steps at which they re-apply.

:::

## Answer Key

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry it exercises. A quick-answer table closes the section.**

**C1.1** — *Verbal range to interval (Entry №01).* "At least $0.2$" includes $0.2$ (square); "at most $0.55$" includes $0.55$ (square). Both endpoints in:
$$[0.2,\ 0.55].$$

**C1.2** — *Fraction → decimal → percent (Entry №02).*
$$\frac{7}{50} = 7 \div 50 = 0.14 = 14\%.$$

**C1.3** — *Exponent laws (Entry №03).* Add then subtract exponents: $6 + (-2) - 3 = 1$, so
$$\frac{e^{6}e^{-2}}{e^{3}} = e^{1} = e \approx 2.718.$$

**C1.4** — *Rearrange a linear equation (Entry №04).* Subtract $5$, then divide by $2$:
$$2L + 5 = 17 \;\Rightarrow\; 2L = 12 \;\Rightarrow\; L = 6.$$

**C1.5** — *Evaluate a function (Entry №05).* Substitute the input:
$$f(2) = 3(2) - 4 = 2, \qquad f(0) = 3(0) - 4 = -4.$$

**C1.6** — *Expand a summation (Entry №06).* Walk $k = 1,2,3,4$, term $2k+1$:
$$\sum_{k=1}^{4}(2k+1) = 3 + 5 + 7 + 9 = 24.$$

**C1.7** — *Percent of a quantity, two ways (Entry №02).*
$$15(1 - 0.40) = 15(0.60) = 9.00; \qquad 15 - (0.40 \times 15) = 15 - 6 = 9.00.$$
Both give a sale price of $\$9.00$.

**C1.8** — *Solve for a variable in an exponent (Entry №03).* Take $\ln$ of both sides:
$$e^{-t/6} = 0.25 \;\Rightarrow\; -\frac{t}{6} = \ln(0.25) \;\Rightarrow\; t = -6\ln(0.25) = 6\ln 4 \approx 8.318.$$

**C1.9** — *Rearrange a formula with a fraction (Entry №04).* Multiply by $(1-e)$, then isolate $e$:
$$P = \frac{C}{1-e} \;\Rightarrow\; P(1-e) = C \;\Rightarrow\; 1 - e = \frac{C}{P} \;\Rightarrow\; e = 1 - \frac{C}{P}.$$

**C1.10** — *Piecewise evaluation + sum (Entries №05, №06).* Check each condition first.
$$g(2) = 0 \ (2 \le 2), \qquad g(5) = 25(5-2) = 75.$$
$$g(1) = 0,\quad g(3) = 25(1) = 25,\quad g(6) = 25(4) = 100 \;\Rightarrow\; \text{total } 0 + 25 + 100 = 125.$$

**C1.11** — *Expand a finite sum term by term (Entry №06).* Four terms, $k = 0,1,2,3$:
$$\sum_{k=0}^{3} 4(0.5)^{k} = 4(1) + 4(0.5) + 4(0.25) + 4(0.125) = 4 + 2 + 1 + 0.5 = 7.5.$$

**C1.12** — *Product / factorial (Entry №06).*
$$\prod_{k=1}^{5} k = 1\cdot2\cdot3\cdot4\cdot5 = 120 = 5!.$$

**C1.13** — *Exponent solve via logarithm (Entry №03).* Take $\ln$; since $\ln(0.8) < 0$, dividing flips the inequality:
$$(0.8)^{t} < 0.5 \;\Rightarrow\; t\ln(0.8) < \ln(0.5) \;\Rightarrow\; t > \frac{\ln(0.5)}{\ln(0.8)} = \frac{-0.6931}{-0.2231} \approx 3.106.$$
The smallest whole turn is $t = 4$. (Check: $0.8^{4} = 0.4096 < 0.5$; $0.8^{3} = 0.512 > 0.5$.)

**C1.14** — *Index notation, sum and product (Entry №06).*
(a) $a_1 = 1\cdot2 = 2,\ a_2 = 2\cdot3 = 6,\ a_3 = 3\cdot4 = 12,\ a_4 = 4\cdot5 = 20$.
(b) $\sum_{k=1}^{4} a_k = 2 + 6 + 12 + 20 = 40$.
(c) $\prod_{k=1}^{2} a_k = a_1 \cdot a_2 = 2 \cdot 6 = 12$.

**C1.15** — *Interval, count, percent, fraction (Entries №01, №02).*
(a) Inside $[200,5000]$: total $80$ minus the $20$ below and $8$ above = $80 - 28 = 52$. Percent: $\tfrac{52}{80} = 0.65 = 65\%$.
(b) $\dfrac{52}{80} = \dfrac{13}{20}$ in lowest terms.

**C1.16** — *Exponent solve feeding a decision (Entries №03, №01).*
(a) $\ln$ both sides; $\ln(0.95) < 0$ flips the inequality:
$$(0.95)^{t} < 0.60 \;\Rightarrow\; t > \frac{\ln(0.60)}{\ln(0.95)} = \frac{-0.5108}{-0.05129} \approx 9.96.$$
(b) Smallest whole number of steps: $t = 10$. (Check: $0.95^{10} \approx 0.599 < 0.60$; $0.95^{9} \approx 0.630 > 0.60$.)

### Quick-Answer Table

| # | Answer | | # | Answer |
|---|---|---|---|---|
| C1.1 | $[0.2,\ 0.55]$ | | C1.9 | $e = 1 - C/P$ |
| C1.2 | $\tfrac{7}{50} = 0.14 = 14\%$ | | C1.10 | $0;\ 75;$ total $125$ |
| C1.3 | $e^{1} = e \approx 2.718$ | | C1.11 | $7.5$ |
| C1.4 | $L = 6$ | | C1.12 | $120 = 5!$ |
| C1.5 | $f(2)=2,\ f(0)=-4$ | | C1.13 | $t = 4$ |
| C1.6 | $24$ | | C1.14 | $\{2,6,12,20\};\ 40;\ 12$ |
| C1.7 | $\$9.00$ | | C1.15 | $65\% = \tfrac{13}{20}$ |
| C1.8 | $6\ln 4 \approx 8.318$ | | C1.16 | $t = 10$ |
:::

## Badge Earned — Mastery Checklist

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map — the journey begins at Pallet Town, with Route 1 now open to the north." style="width:58%; max-width:380px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption class="badge-caption"><strong>Trainer's License stamped — Toolkit I cleared! Pallet Town → Route 1.</strong></figcaption>
</figure>

You earn your **Trainer's License (Toolkit I)** when you can, unaided:

1. **Place numbers on the line** and write any range in **interval notation**, choosing square (included) versus round (excluded) brackets correctly — and remember infinity is always round. *(prereq — numbers & intervals; Entry №01.)*
2. **Move freely among fraction, decimal, and percent**, and **solve a proportion** by cross-multiplying. *(prereq — fractions/percents; Entry №02.)*
3. **Apply the exponent and log laws**, and **free a variable trapped in an exponent** by taking $\ln$ of both sides (flipping the inequality when the log is negative). *(prereq — exponents & logs; Entry №03.)*
4. **Read a formula as a reusable rule** and **rearrange it** to isolate any letter, applying each inverse operation to the whole side. *(prereq — variables & equations; Entry №04.)*
5. **Read and evaluate function notation $f(x)$**, including **piecewise** functions, and state a **domain** and **range**. *(prereq — functions; Entry №05.)*
6. **Read and expand $\sum$ and $\prod$ notation**, counting the terms correctly and recognizing $\prod_{1}^{n} k = n!$. *(prereq — summation & product; Entry №06.)*

> **Gym rematch pointers (🧴 Potion).** Miss item 1 → re-read Concept 1 + WE 1.1. Miss item 2 → Concept 2 + WE 1.2 + C1.2. Miss item 3 → Concept 3 + WE 1.3 + the Team Rocket trap. Miss item 4 → Concept 4 + C1.9. Miss item 5 → Concept 5 + WE 1.4. Miss item 6 → Concept 6 + C1.11 / C1.14, and re-count the terms in every sum.

*Onward to Route 1 — where the toolkit grows teeth: **series and the calculus of probability.***

---

<!-- ===== CALLOUT BOX TEMPLATES (Pandoc fenced divs; styled by book/theme.css) =====
     ::: cold-open / pokedex-entry / trainers-tip / team-rocket / kanto-realworld
     Concept gate ("Do you already own this?") also uses a styled panel.
     Wrap the problem set in ::: problem-set and the key in ::: answer-key . -->
