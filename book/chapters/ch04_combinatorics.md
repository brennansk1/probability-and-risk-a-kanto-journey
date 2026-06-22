<!--
  file: ch04_combinatorics
  tier: B
  outcomes: 1b,2d
  tia: A.4
  locale: Viridian Forest -> Pewter
  type: rock
  maps_to: Viridian Forest crossing + Pewter Gym, Brock -- counting the uncountable (permutations, combinations, binomial, multinomial, hypergeometric)
-->

# Counting Machines — From Arrangements to the Hypergeometric {.type-rock}

<figure>
<img src="../../assets/maps/kanto_ch04.png" alt="Kanto town map with Pewter City highlighted; the trail runs out of Viridian Forest to Brock's Gym at the edge of town, the next destination after Vermilion." style="width:70%; max-width:520px; display:block; margin:1em auto;">
<figcaption>Route to a 10 — with the Cascade and Thunder Badges already won, you double back through Viridian Forest to Pewter City, home of the Boulder Badge and the gym where you learn to <em>count</em>.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "Showdown in Pewter City"**

You step under the canopy of Viridian Forest and the daylight dies to a green dusk. Somewhere overhead a Pidgey rustles; somewhere ahead, a bug-catcher is already reaching for a Poké Ball. A cluster of identical Caterpie inches along a branch, indistinguishable from one another. Your Pokédex chimes into **Actuary Mode**.

"Three trails fork ahead," Brock says, catching up out of the trees, his pack rattling with rock samples. "The left branch splits again. Each split ends at a different clearing." He folds his arms. "Pick wrong and you'll wander till nightfall."

You crouch over the dirt and try to count the routes by eye — left, then left-or-right, then this clearing or that one — and your head spins before you reach a dozen. There are too many to list.

At the forest's edge, Brock turns, and his easy grin hardens into the look of a Gym Leader. "Before I hand anyone the Boulder Badge, they prove they can *count* — not guess. My Pokémon can be sent out in any **order**. A team can be **chosen** a thousand ways. A flock can hold *some number* of one species, drawn one by one without putting any back. A trainer who can't count the possibilities can't see the battle." He tosses a smooth stone in his palm. "So here's the toll: tell me *exactly* how many distinct ways — or *exactly* what chance — for the things I ask. No 'about.' No 'roughly.' The number — or no badge."

Pikachu's ears flatten. It feels the trap in the question: the gap between *seems like a lot* and *is exactly this many*. The screen fills with branching paths, ordered rosters, clusters of identical Caterpie, and a hand of Pokémon scooped blind from a tree — all waiting to be enumerated.

*You can't list them one by one — there are far too many. So how do you count a thing you can't see all of at once, and turn that count into a probability?*
:::

## Where You Are — 60-Second Retrieval

**Rank: Rookie Trainer · Badges: 2 (Cascade, Thunder).** You earned the **Thunder Badge** at Vermilion by describing a whole population with two summary numbers — its **mean** (a *weighted average*: each value times its probability) and its **variance**. The load-bearing idea you carry into the forest is the one underneath the mean: $E[X]=\sum_k k\,p(k)$ rests on knowing each value's **probability**, and for *equally likely* outcomes a probability is just

$$P(A) = \frac{\text{number of outcomes in } A}{\text{number of outcomes in } S}.$$

That formula has a quiet demand hidden inside it: to use it, you must *count the outcomes in $A$ and the outcomes in $S$.* In tiny examples you listed them by hand. But "how many ordered battle line-ups of $3$ from $8$ Pokémon?" has $336$ outcomes, and "how many $6$-Pokémon teams from $12$ species?" has $924$ — far too many to list. **This chapter is the machinery for counting when listing is impossible**, and the payoff is the **hypergeometric** probability — a count over a count — which feeds straight into the distributions to come.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the last chapter**

Answer from memory; if any feels shaky, flip back before continuing.

1. A pmf puts $p(0)=0.5,\,p(1)=0.3,\,p(2)=0.2$. What is $E[X]$? *(Answer: $0(0.5)+1(0.3)+2(0.2)=0.7$ — a weighted average.)*
2. If every outcome in $S$ is equally likely, how do you get $P(A)$? *(Answer: count $A$, count $S$, divide.)*
3. What does it mean for two events to be **mutually exclusive**, and how do their probabilities combine? *(Answer: they can't both happen; for an "or" you **add** the disjoint probabilities.)*

All three instant? You're ready — "count favorable, count total, divide" and "disjoint cases add" are the two reflexes this whole chapter leans on. Any hesitation? The retrieval *is* the lesson — go reclaim it, then come back.
:::

::: now-playing
**📺 NOW PLAYING — Indigo League EP003 "Ash Catches a Pokémon" + EP004 "Challenge of the Samurai" + EP005 "Showdown in Pewter City"**

<figure><img src="../../assets/stills/ch04_now_playing.jpg" alt="Brock and Ash at sunset as Ash leaves Pewter City (Indigo League EP005)." style="width:60%; max-width:440px; display:block; margin:0.4em auto;"><figcaption style="font-size:0.8em; color:#555;">Pewter City, EP005 — Brock's rock-solid logic: counting by rule.</figcaption></figure>

In **EP003–EP004** Ash crosses **Viridian Forest** — catching a Caterpie, weathering a swarm of Weedle, and dueling a bug-catcher *Samurai* — a forest literally full of clusters of look-alike bug Pokémon, the exact "draw-without-replacement" world this chapter counts. In **EP005** he reaches **Pewter City** and challenges **Brock** for the **Boulder Badge**, losing his first attempt against Brock's rock-solid **Onix** before adapting — a fitting picture of a chapter where the whole skill is *picking the right counting machine on sight*. *Watch EP003–EP005 right before this chapter* — the forest clusters and the Pewter gym are the two scenes the math lives in. (Our cold-open dramatizes Brock's forest-edge challenge; the "count exactly, or no badge" toll is an in-world framing for the math, not an on-screen line.)
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice crackles through the Pokédex, calm against the forest gloom.

"Counting, Ash, is the floor beneath all of probability. Every 'equally likely' problem is secretly a counting problem in a costume — and every discrete distribution in the chapters ahead is a counting machine with probabilities bolted on. There are only a handful of these machines, and the entire art is knowing **which one** a problem is asking for. Master that, and you'll never fear a 'how many ways' or a 'what's the chance of exactly $x$' question again — and you'll compute combinatorial probabilities in seconds while everyone else is still scribbling lists. This is a **Tier B** chapter; take it one machine at a time."

By the end of this chapter you will be able to:

- **Apply** the **fundamental counting principle** to multi-stage choices, and decide when stages *multiply* and when you *add* instead. *(Outcome 1b.)*
- **Compute permutations** $P(n,k)$ — ordered selections without replacement, where rearranging the chosen items is a *new* outcome. *(Outcome 1b.)*
- **Compute combinations** $\binom{n}{k}$ — unordered selections without replacement, where rearranging the chosen items is the *same* outcome — and **classify** any problem with the *ordered/unordered × with/without-replacement* grid. *(Outcome 1b.)*
- **Use the binomial** model $\binom{n}{x}p^x(1-p)^{n-x}$ to count successes in $n$ independent, **with-replacement** trials. *(Outcomes 1b, 2d.)*
- **Count arrangements with repeated items** with the **multinomial** coefficient $\dfrac{n!}{n_1!\,n_2!\cdots n_r!}$. *(Outcome 1b.)*
- **Turn a without-replacement count into a probability** — the **hypergeometric** $\dfrac{\binom{K}{x}\binom{N-K}{k-x}}{\binom{N}{k}}$ — and tell it apart from the binomial on sight. *(Outcomes 1b, 2d.)*

> *Exam-weight signpost.* Counting is a **Tier B** topic: it carries direct weight in Exam P's General Probability section (1b) *and* it is the silent engine behind the **binomial** and **hypergeometric** distributions (2d) you will use throughout Topic 2 (univariate RVs, 44–50% of the exam). The single highest-leverage move in the whole chapter is **telling a combination from a permutation — and a hypergeometric from a binomial — on sight**: roughly four of five exam counting questions are an unordered, without-replacement choice (a $\binom{n}{k}$) in disguise.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own All of Pewter?**

Already fluent? Prove it. Work these six, ~2 minutes each, *with the correct machine*:

1. A 4-digit code allows digits $0$–$9$ in each slot, repeats allowed. How many codes? *(Answer: $10^4 = 10{,}000$.)*
2. From $8$ Pokémon, how many ordered battle line-ups of $3$? *(Answer: $P(8,3)=336$.)*
3. From $12$ species, how many unordered teams of $6$? *(Answer: $\binom{12}{6}=924$.)*
4. A Pidgey flushes (success) w.p. $0.5$; in a flock of $6$, find $P(\text{exactly }3\text{ flush})$. *(Answer: $\binom{6}{3}(0.5)^3(0.5)^3=0.3125$.)*
5. How many distinguishable arrangements of the letters in **CATERPIE** (two E's)? *(Answer: $8!/2!=20{,}160$.)*
6. A cluster of $10$ has $4$ Caterpie and $6$ others; grab $3$ without replacement. $P(\text{exactly }2\text{ Caterpie})$? *(Answer: $\binom{4}{2}\binom{6}{1}/\binom{10}{3}=0.30$.)*

Six for six with the right method? **Skip to the Gym Challenge** and claim the badge. Any miss or hesitation — especially confusing #4 (with replacement) with #6 (without) — the teaching below was built exactly for you, and each concept has its *own* skip-gate, so even a partial owner loses no time.
:::

---

Six counting machines build on one another, in TIA's order and increasing difficulty. Each gets a "do you already own this?" skip-check, the full nine-beat lesson, and a Pokédex Entry you can carry into the exam:

0. **The fundamental counting principle** — multiply across stages *(the engine everything else is built from)*
1. **Permutations** *(A.4.1)* — ordered selections, where order makes a new outcome
2. **Combinations** *(A.4.2)* — unordered selections, where order is thrown away — plus the **ordered/unordered × replacement classifier**
3. **The binomial** *(A.4.3)* — count successes in $n$ independent, *with-replacement* trials
4. **The multinomial** *(A.4.4)* — arrangements when some items are identical
5. **The hypergeometric** *(A.4.5)* — turn a *without-replacement* count into a probability *(the payoff)*

## Concept 0 — The Fundamental Counting Principle: Multiply Across Stages

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Multiplication Principle**

A forest path forks into $3$ main trails; each main trail splits into $2$ sub-trails; each sub-trail ends at one of $4$ clearings. How many distinct entrance-to-clearing routes are there?

If you instantly answered **$3 \times 2 \times 4 = 24$** (and you'd never write $3+2+4=9$), you own this — **skip to Concept 1**. If you reached for addition, or you're unsure why the stages multiply, this section is for you.
:::

**Beat 1 — The one-sentence idea.** *If a task is a sequence of choices and each choice has its own menu, the number of ways to do the whole task is the menus multiplied together.*

**Beat 2 — Anchor + concrete instance.** This is the engine. Permutations, combinations, the binomial, the multinomial — every formula ahead is this one rule with bookkeeping bolted on. So we start with Brock's literal forest. From the entrance you pick **1 of 3** main trails. Each main trail then splits into **2** sub-trails, and each sub-trail ends at one of **4** clearings where wild Pokémon gather. *How many distinct entrance-to-clearing routes are there?*

**Beat 3 — Reason through it in plain words.** Don't try to picture all of them at once — build *one* route and watch how many ways each step could have gone. Pick a main trail: $3$ ways. For *each* of those $3$, the sub-trail can go $2$ ways — so after two steps there are $3 \times 2 = 6$ partial routes. For *each* of those $6$, the clearing can be any of $4$ — so $6 \times 4 = 24$ complete routes. The phrase **"for each"** is the whole secret: every earlier choice fans out into the full menu of the next.

$$3 \times 2 \times 4 = 24 \text{ routes.}$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** The natural slip is to *add* the menus:

$$3 + 2 + 4 = 9. \qquad\textbf{(wrong)}$$

But $9$ answers a *different* question — "how many trail-pieces are there in total?" A *route* is one main trail **and then** one sub-trail **and then** one clearing — three choices that all happen together. Here is the rule that keeps you straight: **"and then" (this stage *and* that stage) multiplies; "either/or" (this *or* that, one single choice) adds.** Adding throws away every combination.

**Beat 5 — Translate into notation, one glyph at a time.** Suppose the task has $k$ stages. Call the number of choices at stage $i$ by the symbol $n_i$:

$$n_i \quad \text{read aloud: ``} n\text{-sub-}i\text{''} \;=\; \text{the number of choices available at stage } i.$$

The subscript $i$ is just a *label* — $n_1$ is the first stage's menu, $n_2$ the second's (here $n_1=3,\ n_2=2,\ n_3=4$). The total is every menu multiplied:

$$N = n_1 \times n_2 \times \cdots \times n_k.$$

**Beat 6 — Derive the formula from the instance.** We didn't assert this — we *built* it. With one stage there are $n_1$ ways. Adding a second stage replaces each of those $n_1$ partial outcomes with $n_2$ continuations, giving $n_1 \times n_2$. Each further stage multiplies the running count by its own menu size, for the same "for each" reason. So $N = n_1 n_2 \cdots n_k$ — provided each stage's menu size doesn't depend on *which* earlier choices were made.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the forest routes, $3 \times 2 \times 4 = 24$.
- *Twist — does the menu shrink?* A $4$-digit lock with digits $0$–$9$ and **repeats allowed** is $10 \times 10 \times 10 \times 10 = 10^4 = 10{,}000$, because each slot still has all $10$ digits. But if **no digit may repeat**, the menu shrinks: $10 \times 9 \times 8 \times 7 = 5040$. The principle still holds — you just feed it the *remaining* menu each stage. (That shrinking menu is exactly the next concept, permutations.)
- *Edge — equal menus:* $k$ stages each with the same $n$ choices give $n^k$. A $5$-question true/false quiz has $2^5 = 32$ answer keys.

**Beat 8 — Picture it.** Equal menus repeated $k$ times give $n^k$; shrinking menus give a permutation. The two tips of the same engine show up in the classifier figure of Concept 2 (the "with replacement, order matters" cell is $n^k$).

**Beat 9 — Consolidate.** You can take any multi-stage task, identify the menu size at each stage, and multiply — adding only when the choice is a single "either/or." This one rule generates every formula that follows.

::: pokedex-entry
**POKÉDEX ENTRY №01 — The Fundamental Counting Principle**

If a task is built from $k$ stages, where stage $i$ can be done in $n_i$ ways *regardless of the earlier choices*,

$$N = n_1 \times n_2 \times \cdots \times n_k \text{ ways.}$$

*In plain terms:* a sequence of choices, each with its own menu — multiply the menu sizes. Equal menus ($n$ each, $k$ stages) give $n^k$.

*Recognition cue:* **"first… then…," slots to fill in sequence, "how many ways in total."** "And then" $\to$ **multiply**. A single "either this or that" $\to$ **add**.
:::

## Concept 1 — Permutations: Order Matters, No Repeats (A.4.1)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Permutations**

Brock keeps $8$ Pokémon and battles with $3$, *sent out in a definite order*. How many distinct ordered line-ups can he form?

If you wrote **$P(8,3) = 8 \cdot 7 \cdot 6 = 336$** (and can say *why* the factors march down $8, 7, 6$), **skip to Concept 2**. If you wrote $8^3$ or $\binom{8}{3}$, read on.
:::

**Beat 1 — The one-sentence idea.** *To fill $k$ ordered slots from $n$ distinct items with no repeats, multiply the shrinking menu — $n$ choices for the first slot, $n-1$ for the next, and so on.*

**Beat 2 — Anchor + concrete instance.** This is Concept 0 with a *shrinking* menu: each item used is gone, so the next slot has one fewer choice. "I keep **8** trained Pokémon," Brock says, "but I battle with **3**, sent out in sequence — and the *order* I send them changes everything." A different lead means a different strategy. *How many distinct ordered line-ups of $3$ can Brock form from his $8$ Pokémon?*

**Beat 3 — Reason through it in plain words.** Fill the slots left to right. The **lead** can be any of the $8$. Once it's chosen, that Pokémon is on the field, so the **second** slot has only the $7$ remaining. The **anchor** then has $6$ left. By the multiplication principle, multiply the shrinking menu:

$$8 \times 7 \times 6 = 336 \text{ ordered line-ups.}$$

The menu marches *down* — $8, 7, 6$ — because each pick removes itself from the pool.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two slips lurk. First, reusing the full menu:

$$8 \times 8 \times 8 = 512. \qquad\textbf{(wrong — assumes repeats / replacement)}$$

That would be right only if Brock could send the *same* Pokémon to multiple slots — he can't; it's already on the field. Second, *forgetting that order counts* and writing $\binom{8}{3}=56$. But $56$ counts the **roster** of three; it ignores that lead-vs-anchor is a different battle. Here, order is part of the answer, so $336$, not $56$. (We'll see exactly how those two numbers relate in the next concept.)

**Beat 5 — Translate into notation, one glyph at a time.** First, the **factorial**. For a whole number $n$,

$$n! \quad \text{read aloud: ``}n \text{ factorial''} \;=\; n \times (n-1) \times \cdots \times 2 \times 1,$$

the product of every whole number from $n$ down to $1$ (and by convention $0! = 1$). It is exactly "arrange all $n$ distinct things in a row": $n$ choices, then $n-1$, all the way down. Now the **permutation count** — ordered, without repeats, $k$ from $n$:

$$P(n,k) \quad \text{read aloud: ``the number of permutations of } n \text{ things taken } k \text{ at a time.''}$$

Our line-up was $P(8,3) = 8 \cdot 7 \cdot 6 = 336$.

**Beat 6 — Derive the formula from the instance.** We multiplied $8 \cdot 7 \cdot 6$ — that's $8!$ with the unused tail $5! = 5\cdot4\cdot3\cdot2\cdot1$ chopped off. Multiply and divide by that tail to write it cleanly:

$$P(8,3) = 8\cdot7\cdot6 = \frac{8\cdot7\cdot6\cdot 5!}{5!} = \frac{8!}{5!} = \frac{8!}{(8-3)!}.$$

The same bookkeeping for general $n,k$ gives

$$\boxed{\,P(n,k) = n(n-1)\cdots(n-k+1) = \frac{n!}{(n-k)!}.\,}$$

The denominator $(n-k)!$ is just the part of the factorial you *didn't* use — the items left in the pool after filling all $k$ slots. The special case $k=n$ gives $P(n,n) = n!/0! = n!$: arrange *all* of them.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the $3$-of-$8$ line-up, $P(8,3)=336$.
- *Full arrangement:* arrange all $6$ Poké Balls on a belt — $P(6,6)=6!=720$.
- *Edge / sanity:* $P(n,1)=n$ (one slot, $n$ choices) and $P(n,0)=1$ (one way to choose nothing — the empty arrangement). Both fall straight out of $n!/(n-k)!$.

**Beat 8 — Picture it.** A permutation is ordered slots with a shrinking menu; throwing away the order collapses each group of $k!$ orderings to one — exactly the left half (and the collapse band) of the figure in Concept 2.

**Beat 9 — Consolidate.** You can count ordered selections without repeats: fill the slots with a shrinking menu, or compute $n!/(n-k)!$ directly. The trigger is **order matters**.

::: pokedex-entry
**POKÉDEX ENTRY №02 — Permutations (Order Matters, No Repeats)**

$$P(n,k) = \frac{n!}{(n-k)!} = n(n-1)\cdots(n-k+1), \qquad P(n,n)=n!.$$

*In plain terms:* fill $k$ ordered slots from $n$ distinct items, no reuse — the menu shrinks by one each slot.

*Recognition cue:* **"arrange," "line up," "order," "rank 1st/2nd/3rd," "schedule," "seat," "battle order."** If rearranging the chosen items is a *new* outcome, it's a permutation.
:::

## Concept 2 — Combinations: Order Does Not Matter (A.4.2)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Combinations**

From $12$ species you must **choose** a $6$-Pokémon team; the order on the team sheet is irrelevant. How many distinct teams?

If you wrote **$\binom{12}{6} = 924$** (and can explain *why you divide $P(12,6)$ by $6!$*), **skip to Concept 3**. If you wrote $P(12,6)=665{,}280$, read on — you counted each team $720$ times.
:::

**Beat 1 — The one-sentence idea.** *A combination is a permutation with the internal ordering thrown away — count the ordered selections, then divide out the $k!$ orderings of each chosen group.*

**Beat 2 — Anchor + concrete instance.** This is Concept 1 with one correction: now reshuffling the chosen items is the **same** outcome, so we've over-counted and must divide. By the time you reach Pewter you've caught **12** distinct species. To register for the Gym you must **choose** which **6** make your team — order on the sheet doesn't matter, a team is a *set*. *How many distinct teams are there?*

**Beat 3 — Reason through it in plain words.** Pretend for a moment that order *did* matter. Then you'd be filling $6$ ordered slots from $12$: that's $P(12,6) = 12\cdot11\cdot10\cdot9\cdot8\cdot7 = 665{,}280$ ordered cards. But a *team* doesn't care about order — the same six Pokémon in any sequence is one team. How many sequences does each team get counted as? Exactly $6!$, the number of ways to arrange six items (Concept 1's $P(6,6)$). So every team was counted $6! = 720$ times. Divide it back out:

$$\frac{P(12,6)}{6!} = \frac{665{,}280}{720} = 924 \text{ teams.}$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** *(This is Team Rocket's trap for the chapter.)* The classic error is stopping at the permutation:

$$P(12,6) = 665{,}280. \qquad\textbf{(wrong — counts each team } 6! \text{ times)}$$

That's the answer to "how many ordered *cards*," not "how many *teams*." {Squirtle, Pikachu, …} in one order is the same team as in any other; the permutation counts all $720$ orderings as distinct. The fix is always the same: **if reshuffling the picked items changes nothing, divide the permutation count by $k!$.** (Treating an unordered choice as ordered — over-counting by $k!$ — is the single most common counting error on the exam.)

**Beat 5 — Translate into notation, one glyph at a time.** The **binomial coefficient**:

$$\binom{n}{k} \quad \text{read aloud: ``}n \text{ choose } k\text{''} \;=\; \text{the number of unordered } k\text{-subsets of } n \text{ distinct items.}$$

Read it top-to-bottom as "from $n$, choose $k$." It is *not* a fraction — the stacked $n$ over $k$ inside the parentheses is one symbol meaning "choose."

**Beat 6 — Derive the formula from the instance.** We divided the ordered count by $k!$. So

$$\binom{n}{k} = \frac{P(n,k)}{k!} = \frac{n!/(n-k)!}{k!} = \boxed{\;\frac{n!}{k!\,(n-k)!}\;}.$$

Read the bottom as a balance sheet: $k!$ removes the ordering *inside* the chosen group, and $(n-k)!$ removes the ordering of the items you *left behind*. Check our case: $\binom{12}{6} = \frac{12!}{6!\,6!} = 924.$ Two identities fall straight out and save real time:

$$\binom{n}{k} = \binom{n}{n-k} \quad(\text{choosing who's *in* = choosing who's *out*}), \qquad \binom{n}{0}=\binom{n}{n}=1.$$

**Beat 7 — Ramp the difficulty.**

- *Simplest:* the $6$-of-$12$ team, $\binom{12}{6}=924$.
- *Symmetry shortcut:* to count $4$-person panels from $12$ compute $\binom{12}{4}=495$; note $\binom{12}{4}=\binom{12}{8}$, so always choose the *smaller* bottom to multiply fewer terms.
- *Choose-then-arrange (uniting Concepts 1 and 2):* pick the team **and then** order it. $\binom{12}{6}\cdot 6! = 924 \times 720 = 665{,}280 = P(12,6)$ — the two routes agree, the identity $P(n,k)=\binom{n}{k}\,k!$ read forward.

**Beat 8 — Picture it.** Order matters (permutation) vs. order discarded (combination) is the same pick seen two ways; the figure makes the $k!$ collapse literal, then shows the two questions that classify *any* problem.

<figure>
<img src="../../assets/diagrams/ch04_perm_vs_comb.png" alt="A side-by-side of one pick of 3 from 5. Left, labeled 'Order MATTERS (permutation)': three slots Lead, Second, Anchor with shrinking menus 5, 4, 3 above them, multiplying to P(5,3)=60 ordered cards. Right, labeled 'Order DOESN'T (combination)': a single unordered set {A,B,C} = one team, with C(5,3)=10 teams. A bottom band titled 'Why divide by k!' shows the six orderings ABC, ACB, BAC, BCA, CAB, CBA of one team collapsing to a single set, with C(5,3)=P(5,3)/3!=60/6=10. A small Pidgey sprite sits in the top-right margin." style="width:90%; max-width:720px; display:block; margin:1em auto;">
<figcaption>One pick of $3$ from $5$, two ways: the permutation counts $60$ ordered cards; discarding order divides by $3!=6$ to give $\binom{5}{3}=10$ teams.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can count unordered selections, convert between $P(n,k)$ and $\binom{n}{k}$ via the $\times k!$ / $\div k!$ bridge, and use $\binom{n}{k}=\binom{n}{n-k}$ to compute fewer terms. The trigger is **order does not matter**.

::: pokedex-entry
**POKÉDEX ENTRY №03 — Combinations (Order Doesn't Matter, No Repeats)**

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!} = \frac{P(n,k)}{k!}, \qquad \binom{n}{k}=\binom{n}{n-k}, \quad \binom{n}{0}=\binom{n}{n}=1.$$

*In plain terms:* a combination is a permutation with the $k!$ internal orderings divided out — a *set*, not a sequence.

*Recognition cue:* **"select," "choose," "a team / committee / hand / sample of $k$," "group."** If reshuffling the chosen items gives the *same* outcome, it's $\binom{n}{k}$.
:::

::: trainers-tip
**TRAINER'S TIP — The $2\times2$ Classifier (pick your machine on sight)**

Before you write a single factorial, drop the problem into this grid by asking **two questions** — *does order matter?* and *can items repeat (replacement)?*

| | **Order matters** | **Order doesn't matter** |
|---|---|---|
| **Without replacement** | $P(n,k)=\dfrac{n!}{(n-k)!}$ | $\dbinom{n}{k}=\dfrac{n!}{k!\,(n-k)!}$ |
| **With replacement** | $n^k$ | $\dbinom{n+k-1}{k}$ (stars & bars) |

The lower-right cell (with-replacement, unordered / "stars & bars") is rare on Exam P. The upper-right — **unordered, without replacement, a $\binom{n}{k}$** — is where roughly four of five counting questions live. The two probability models ahead live one in each replacement row: the **binomial** (Concept 3) is *with*-replacement counting of successes; the **hypergeometric** (Concept 5) is *without*-replacement. Telling those two apart is the same "replacement?" question that splits this grid.

<figure>
<img src="../../assets/diagrams/ch04_2x2_classifier.png" alt="A 2-by-2 grid. Columns: 'Order MATTERS' and 'Order DOESN'T matter'. Rows: 'Without replacement' and 'With replacement'. Cells: top-left Permutation P(n,k)=n!/(n-k)! (arrange, line up, rank, seat); top-right Combination C(n,k)=n!/(k!(n-k)!) (choose a team/hand/sample), outlined with a dashed highlight; bottom-left Sequences with repeats n^k (PIN, lock, digit string); bottom-right Stars and bars C(n+k-1,k) (multiset, rare on P). A caption notes ~4 of 5 exam counting questions live in the unordered, without-replacement cell." style="width:88%; max-width:680px; display:block; margin:1em auto;">
<figcaption>Two questions place any counting problem: order? and replacement? The dashed cell — unordered, without replacement, a $\binom{n}{k}$ — is the exam's home.</figcaption>
</figure>
:::

## Concept 3 — The Binomial: Successes in $n$ Independent Trials (A.4.3)

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Binomial**

You flush a flock of $6$ Pidgey one at a time; each *independently* takes flight (a "success") with probability $p=0.5$. What is $P(\text{exactly }3\text{ take flight})$?

If you wrote **$\binom{6}{3}(0.5)^3(0.5)^3 = 20(0.015625) = 0.3125$** (and can say *why* the $\binom{6}{3}$ is there), **skip to Concept 4**. If you wrote just $(0.5)^3(0.5)^3$ or $\binom{6}{3}$ alone, read on — you're missing a factor.
:::

**Beat 1 — The one-sentence idea.** *When you run $n$ independent trials that each succeed with the same probability $p$, the chance of exactly $x$ successes is the number of ways to choose **which** $x$ trials succeed, times the probability of any one such pattern.*

**Beat 2 — Anchor + concrete instance.** A flock of **6** Pidgey roosts in a tree. You clap once; each Pidgey *independently* takes flight (a "success") with probability $p=0.5$, or stays put with probability $1-p=0.5$. The Pidgey don't deplete — each is its own trial, with the same odds, regardless of the others. *What is the probability exactly $3$ of the $6$ take flight?*

<figure style="display:flex; gap:14px; flex-wrap:wrap; justify-content:center; align-items:flex-end; margin:1.25em auto;">
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/16.png" alt="Pidgey" style="width:110px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">#016 Pidgey — each flush is one independent Bernoulli trial</figcaption>
</figure>
</figure>

**Beat 3 — Reason through it in plain words.** First fix *one* particular pattern — say Pidgey $1,2,3$ fly and $4,5,6$ stay. Because the trials are independent, that exact pattern has probability $p\cdot p\cdot p\cdot(1-p)(1-p)(1-p)=p^3(1-p)^3$. But "exactly $3$ fly" doesn't care *which* three — any of the $\binom{6}{3}=20$ ways to choose the trio of flyers gives a different but **equally likely** pattern. They're disjoint, so **add** them — which, since each has the same probability, just multiplies:

$$P(\text{exactly }3)=\binom{6}{3}\,p^3(1-p)^3=20\,(0.5)^3(0.5)^3=20(0.015625)=0.3125.$$

The $\binom{6}{3}$ is the counting machine (Concept 2) doing the bookkeeping; $p^3(1-p)^3$ is the probability of one pattern.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two slips. First, *forgetting the count* and writing $p^3(1-p)^3=0.0156$ — that's the chance of **one specific** pattern, not "exactly $3$ in any order." Second — the big one for this chapter — using the binomial when the trials are **not** independent, i.e. when you draw *without replacement.* If you grabbed Pidgey out of a finite cluster and *removed* each one, the success probability would shift with every draw, and the binomial would be wrong. The binomial demands **independent, identical, with-replacement** trials. (When the draws deplete a finite pool, you need the *hypergeometric* of Concept 5 — keep these two in separate boxes.)

**Beat 5 — Translate into notation, one glyph at a time.** Let $X$ count the successes in $n$ independent trials, each succeeding w.p. $p$. Then $X$ is **Binomial$(n,p)$**, written $X\sim\text{Bin}(n,p)$, with

$$P(X=x)=\binom{n}{x}\,p^{x}(1-p)^{\,n-x}, \qquad x=0,1,\dots,n.$$

Read it as: $\binom{n}{x}$ = "which $x$ trials succeed"; $p^{x}$ = "those $x$ all succeed"; $(1-p)^{n-x}$ = "the other $n-x$ all fail."

**Beat 6 — Derive the formula.** Every outcome of exactly $x$ successes is one choice of *which* $x$ of the $n$ trials succeed — $\binom{n}{x}$ ways — paired with the probability of that pattern, $p^{x}(1-p)^{n-x}$ (independence multiplies the per-trial probabilities). Those $\binom{n}{x}$ patterns are disjoint and equally likely, so add them:

$$P(X=x)=\underbrace{\binom{n}{x}}_{\text{which trials}}\;\underbrace{p^{x}(1-p)^{\,n-x}}_{\text{one pattern}}.$$

A free sanity check that it's a real pmf: $\sum_{x=0}^{n}\binom{n}{x}p^x(1-p)^{n-x}=(p+(1-p))^n=1^n=1$ by the binomial theorem — which is *why* it's called the binomial distribution. The mean and variance (proved in ch05's distribution work, quoted here) are

$$E[X]=np, \qquad \Var(X)=np(1-p).$$

**Beat 7 — Ramp the difficulty.**

- *Simplest:* exactly $3$ of $6$ flush at $p=0.5$, $0.3125$.
- *Twist (at least one):* $P(\text{at least one flushes})=1-P(\text{none})=1-(1-p)^n=1-(0.5)^6=1-\tfrac{1}{64}=\tfrac{63}{64}\approx0.984$. "At least one" is almost always fastest by complement.
- *General $p$:* if $p=0.3$, $P(\text{exactly }2\text{ of }6)=\binom{6}{2}(0.3)^2(0.7)^4=15(0.09)(0.2401)\approx0.324$.
- *Edge:* $n=1$ is a single **Bernoulli** trial — $P(X=1)=p$, $P(X=0)=1-p$ — the atom the binomial is built from.

**Beat 8 — Picture it.** The flock's success-count is a pmf bar chart: each bar is $\binom{n}{x}p^x(1-p)^{n-x}$, peaked near the mean $np$.

<figure>
<img src="../../assets/diagrams/ch04_binomial_flock.png" alt="A bar chart of the Binomial(6, 0.5) pmf for x = 0..6, with bars 0.016, 0.094, 0.234, 0.312, 0.234, 0.094, 0.016, symmetric and peaked at x = 3. A boxed legend gives P(X=x) = C(n,x) p^x (1-p)^(n-x), notes C(n,x) is 'which x of the n flushed', and E[X]=np, Var(X)=np(1-p). A note marks E[X]=np=3. A small flock of Pidgey sits in the top margin." style="width:84%; max-width:640px; display:block; margin:1em auto;">
<figcaption>Binomial$(6,0.5)$: the count of successes among $6$ independent, equal-probability trials, symmetric and peaked at the mean $np=3$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can compute the chance of exactly $x$ successes in $n$ independent, with-replacement trials with $\binom{n}{x}p^x(1-p)^{n-x}$, handle "at least one" by complement, and — crucially — you will reach for the binomial *only* when trials are independent (with replacement), never for a depleting draw.

::: pokedex-entry
**POKÉDEX ENTRY №04 — The Binomial Distribution (with-replacement successes)**

For $n$ independent trials, each a success w.p. $p$,

$$P(X=x)=\binom{n}{x}p^{x}(1-p)^{\,n-x}, \qquad E[X]=np,\ \ \Var(X)=np(1-p).$$

*In plain terms:* count *which* $x$ trials succeed ($\binom{n}{x}$), times the probability of one such pattern ($p^x(1-p)^{n-x}$).

*Recognition cue:* **"$n$ independent trials," "each with the same probability," "with replacement," "exactly / at least $x$ successes."** If the draws **deplete** a finite pool, it is *not* binomial — use the hypergeometric.
:::

## Concept 4 — Arrangements with Repeats: The Multinomial (A.4.4)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Arrangements with Repeats**

How many *distinguishable* arrangements of the letters in **CATERPIE** are there? (Eight letters: C, A, T, E, R, P, I, E — note the **two E's**.)

If you wrote **$\dfrac{8!}{2!} = 20{,}160$** (and can say *why* you divide by $2!$), **skip to Concept 5**. If you wrote $8! = 40{,}320$, read on — you counted every word twice.
:::

**Beat 1 — The one-sentence idea.** *Start from all $n!$ orderings as if every item were distinct, then divide out the rearrangements within each block of identical items — because shuffling identical things changes nothing you can see.*

**Beat 2 — Anchor + concrete instance.** This is Concept 2's "divide out what you can't tell apart," now applied to *repeated items* instead of unordered groups. The Pokédex wants to scramble the letters of **CATERPIE** into a registration cipher. *How many distinguishable letter-arrangements exist?* The catch: there are **two E's**, and the two E's look identical.

**Beat 3 — Reason through it in plain words.** Pretend the two E's are secretly different — paint one $\text{E}_1$ and one $\text{E}_2$. Then all eight letters are distinct and there are $8! = 40{,}320$ arrangements. But you *can't* see the paint: $\text{E}_1\text{E}_2$ and $\text{E}_2\text{E}_1$ in the same positions are the **same visible word**. The two E's can be ordered $2! = 2$ ways, and those two ways are indistinguishable. So every real arrangement was counted twice. Divide it out:

$$\frac{8!}{2!} = \frac{40{,}320}{2} = 20{,}160 \text{ distinguishable arrangements.}$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** The slip is to forget the repeat:

$$8! = 40{,}320. \qquad\textbf{(wrong — double-counts every word)}$$

That treats the two E's as if you could tell them apart, so it lists each visible word twice. The rule generalizes: **every block of identical items inflates the count by the factorial of its size — divide each block back out.**

**Beat 5 — Translate into notation, one glyph at a time.** Suppose $n$ items split into $r$ types: $n_1$ identical of type 1, …, $n_r$ of type $r$, with $n_1 + \cdots + n_r = n$. The **multinomial coefficient**:

$$\binom{n}{n_1,\,n_2,\,\ldots,\,n_r} \quad \text{read aloud: ``}n \text{ choose } n_1, n_2, \ldots, n_r\text{''} \;=\; \frac{n!}{n_1!\,n_2!\cdots n_r!}.$$

For CATERPIE the types are "two E's" and six singletons: $\dfrac{8!}{2!\,1!\,1!\,1!\,1!\,1!\,1!} = \dfrac{8!}{2!}$, since $1!=1$ contributes nothing.

**Beat 6 — Derive the formula from the instance.** All $n!$ orderings over-count by exactly the rearrangements *within* each identical block. Type $i$ can be internally shuffled $n_i!$ ways with no visible change, and these inflations multiply across types (Concept 0), so the total over-count factor is $n_1!\,n_2!\cdots n_r!$. Divide it out:

$$\boxed{\;\binom{n}{n_1,\ldots,n_r} = \frac{n!}{n_1!\,n_2!\cdots n_r!}.\;}$$

Notice the two-type case $\dfrac{n!}{k!\,(n-k)!}$ is exactly $\binom{n}{k}$ — the binomial coefficient is the multinomial with just two blocks ("chosen" and "not chosen"). The multinomial is the same idea, generalized.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* one repeated letter — CATERPIE, $8!/2! = 20{,}160$.
- *Several blocks:* line up $3$ identical Water Stones, $2$ identical Thunder Stones, $1$ Leaf Stone — $\dfrac{6!}{3!\,2!\,1!} = \dfrac{720}{12} = 60$ ways.
- *Surprising twist — lattice paths:* a shortest grid walk that is $4$ blocks East and $3$ blocks North is just an arrangement of $4$ E's and $3$ N's: $\dfrac{7!}{4!\,3!} = \binom{7}{3} = 35$ paths. "Choose which $3$ of the $7$ steps are North" — a multinomial *is* a combination in disguise.

**Beat 8 — Picture it.** The collapse band of the Concept 2 figure ($k!$ orderings of one set $\to$ one set) is the same move as the multinomial's: $2!$ orderings of the identical E's $\to$ one visible word. Same engine — divide out what you can't tell apart.

**Beat 9 — Consolidate.** You can count distinguishable arrangements when some items repeat: take $n!$, then divide by the factorial of each identical block — and you recognize lattice-path problems as the same machine.

::: pokedex-entry
**POKÉDEX ENTRY №05 — Arrangements with Repeats (Multinomial)**

For $n$ items of which $n_1$ are alike of type 1, …, $n_r$ alike of type $r$ ($n_1+\cdots+n_r=n$):

$$\binom{n}{n_1,\ldots,n_r} = \frac{n!}{n_1!\,n_2!\cdots n_r!}.$$

*In plain terms:* all $n!$ orderings, divided by the factorial of each identical block (shuffling identical items changes nothing). With two blocks this *is* $\binom{n}{k}$.

*Recognition cue:* **"distinguishable arrangements," repeated identical items, "split into groups of sizes…," lattice / grid-path problems.**
:::

## Concept 5 — The Hypergeometric: Without-Replacement Probability (A.4.5)

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Hypergeometric**

A tree cluster holds $10$ look-alike grass Pokémon: $4$ Caterpie and $6$ others. You blindly grab $3$ at once (without replacement). What is $P(\text{exactly } 2 \text{ Caterpie})$?

If you wrote **$\dfrac{\binom{4}{2}\binom{6}{1}}{\binom{10}{3}} = \dfrac{6\cdot6}{120} = 0.30$**, you own this chapter end to end — **skip to the Gym Battle** for one expert rep, or to the **Gym Challenge** for the badge. If you reached for a binomial $\binom{3}{2}(0.4)^2(0.6)$, read on — that silently assumes replacement.
:::

**Beat 1 — The one-sentence idea.** *When you draw without replacement and every outcome is equally likely, a probability is a count over a count: choose your successes **and** choose your failures, over all possible hands — using the combination machine to count.*

**Beat 2 — Anchor + concrete instance.** This closes the loop with $P(A)=\#A/\#S$ — except now you *count* $\#A$ and $\#S$ with $\binom{n}{k}$ instead of listing them. A cluster on a tree holds **10** look-alike grass Pokémon: **4** are Caterpie and **6** are others (Weedle and Metapod). You blindly grab **3** at once (without replacement). *What is the probability you grabbed exactly $2$ Caterpie?*

<figure style="display:flex; gap:18px; flex-wrap:wrap; justify-content:center; align-items:flex-end; margin:1.25em auto;">
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/10.png" alt="Caterpie" style="width:96px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">#010 Caterpie (4 — the "successes")</figcaption>
</figure>
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/13.png" alt="Weedle" style="width:96px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">#013 Weedle</figcaption>
</figure>
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/11.png" alt="Metapod" style="width:96px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">#011 Metapod (the $6$ "failures")</figcaption>
</figure>
</figure>

**Beat 3 — Reason through it in plain words.** Every set of $3$ Pokémon you could grab is equally likely, so the probability is (favorable grabs) $\div$ (total grabs).

- **Total grabs:** any $3$ of the $10$, order irrelevant — $\binom{10}{3} = 120$.
- **Favorable grabs:** exactly $2$ Caterpie *and* exactly $1$ other. Choose $2$ of the $4$ Caterpie — $\binom{4}{2}=6$ — **and then** $1$ of the $6$ others — $\binom{6}{1}=6$. By the multiplication principle, $6 \times 6 = 36$ favorable grabs.

$$P(\text{exactly } 2 \text{ Caterpie}) = \frac{\binom{4}{2}\binom{6}{1}}{\binom{10}{3}} = \frac{6 \cdot 6}{120} = \frac{36}{120} = 0.30.$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** The seductive slip is to treat the three grabs as independent trials with a fixed $40\%$ Caterpie rate — the **binomial**:

$$\binom{3}{2}(0.4)^2(0.6) = 3(0.16)(0.6) = 0.288. \qquad\textbf{(wrong — assumes replacement)}$$

But you grabbed *without replacement*: pulling a Caterpie *depletes* the cluster, so the chance the next is a Caterpie drops. The fraction of Caterpie isn't a fixed $0.4$ across draws — it changes with every grab. The combination count handles that automatically by counting actual hands. (The binomial $0.288$ and the correct $0.30$ are close here only because the cluster is small; the gap widens fast as draws pile up. This with-vs-without-replacement split is exactly the bottom-vs-top row of the $2\times2$ classifier — and the binomial-vs-hypergeometric decision you must make on sight.)

**Beat 5 — Translate into notation, one glyph at a time.** Let the population be $N$ items containing $K$ "successes" and $N-K$ "failures"; draw $k$ without replacement and ask for exactly $x$ successes. The favorable count is "choose your successes **and** choose your failures":

$$\underbrace{\binom{K}{x}}_{\text{choose the } x \text{ successes}} \cdot \underbrace{\binom{N-K}{k-x}}_{\text{choose the } k-x \text{ failures}} \quad\text{over}\quad \underbrace{\binom{N}{k}}_{\text{all hands}}.$$

This is the **hypergeometric** probability; we write $X\sim\text{HG}(N,K,k)$.

**Beat 6 — Derive the formula.** Every favorable hand is *one* choice of $x$ successes paired with *one* choice of $k-x$ failures, and those two choices are independent stages — multiply (Concept 0). All hands are $\binom{N}{k}$, equally likely. So

$$\boxed{\;P(X=x) = \frac{\binom{K}{x}\binom{N-K}{k-x}}{\binom{N}{k}}.\;}$$

This is the model for *any* without-replacement draw counted by exact type. It returns by name as a full distribution in ch05; here it is favorable-over-total, the chapter's payoff. (Its mean is $E[X]=k\,\frac{K}{N}$ — the same $np$ shape with $p=K/N$, but its variance carries a *finite-population correction* $\frac{N-k}{N-1}$ that the binomial lacks — the price of depletion.)

**Beat 7 — Ramp the difficulty.**

- *Simplest:* exactly $2$ Caterpie, $0.30$.
- *"At least / at most" — sum the cases:* there is no single $\binom{}{}$ for "$\ge 2$." Add the disjoint exact-counts, or complement. For the cluster, $P(\ge 2 \text{ Caterpie}) = P(2)+P(3) = \tfrac{36}{120}+\tfrac{\binom{4}{3}\binom{6}{0}}{120} = \tfrac{36+4}{120} = \tfrac13$.
- *Sanity boundary:* the four exact-counts must sum to $\binom{N}{k}$ — $\dfrac{\binom60\binom63+\binom41\binom62+\binom42\binom61+\binom43\binom60}{120}=\dfrac{20+60+36+4}{120}=1$. If your exact-counts don't sum to $\binom{N}{k}$, you miscounted.

**Beat 8 — Picture it.** The figure splits the cluster into the "success" pile and the "failure" pile, choosing from each.

<figure>
<img src="../../assets/diagrams/ch04_hypergeo_forest.png" alt="The cluster of 10 split into two boxes. Left box, green, 'SUCCESSES: 4 Caterpie' with four Caterpie sprites, labeled choose C(4,2)=6. Right box, red, 'FAILURES: 6 others' with Weedle and Metapod sprites, labeled choose C(6,1)=6. A multiplication sign joins them. A result band shows favorable = C(4,2)C(6,1)=6*6=36 over all hands C(10,3)=120, giving P(exactly 2 Caterpie) = 36/120 = 0.30." style="width:86%; max-width:680px; display:block; margin:1em auto;">
<figcaption>Hypergeometric probability: choose $x$ from the successes $\times$ choose $k-x$ from the failures, over all hands — $\dfrac{6\cdot6}{120}=0.30$.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can turn any equal-likelihood, without-replacement count into a probability: favorable hands over total hands, with the $\binom{K}{x}\binom{N-K}{k-x}/\binom{N}{k}$ form for exact type-counts, and "at least/at most" handled by summing cases or complementing. And you can tell it from the binomial on sight: **deplete the pool $\to$ hypergeometric; replace each draw $\to$ binomial.**

::: pokedex-entry
**POKÉDEX ENTRY №06 — The Hypergeometric (without-replacement probability)**

For a without-replacement draw of $k$ from $N$ items containing $K$ successes,

$$P(X=x) = \frac{\binom{K}{x}\binom{N-K}{k-x}}{\binom{N}{k}}, \qquad E[X]=k\frac{K}{N}.$$

*In plain terms:* count the good hands, count all hands, divide — "choose your successes **and** your failures, over all possible hands."

*Recognition cue:* **"drawn at random," "without replacement," "exactly / at least $x$ of a type."** Depleting draws $\Rightarrow$ hypergeometric (not binomial). Sum cases (or complement) for "at least / at most."
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/vs/brock.png" alt="Brock, Pewter City Gym Leader" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Brock — Pewter City Gym Leader, your counting mentor</figcaption>
</figure>

Six examples, fading from fully narrated to exam-speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because telling a combination from a permutation — and a hypergeometric from a binomial — is the load-bearing skill.

### Worked Example 4.1 — Building a Team of Six (full narration; understanding-first)

**ARCHETYPE:** *Choose-then-arrange — combination, then the $P(n,k)=\binom{n}{k}\,k!$ bridge.*

**Setup.** From $12$ caught species: (a) how many distinct **teams** of $6$ (order irrelevant), and (b) how many distinct **ordered cards** of those $6$?

**Step 1 — Identify (which machine, and does order matter?).** Part (a): "team," order irrelevant $\to$ combination, $\binom{12}{6}$. Part (b): "ordered card" $\to$ arrange the chosen $6$, an extra $6!$, or equivalently $P(12,6)$ directly. The whole point is watching one number turn into the other.

**Step 2 — Professor's Path (the why).** A *team* is a set: reshuffling its six members is the same team. An *ordered card* distinguishes those reshuffles. Each team corresponds to exactly $6!$ ordered cards (the arrangements of its members, Concept 1). So
$$\text{(ordered cards)} = \text{(teams)} \times 6! \quad\Longrightarrow\quad \binom{12}{6}\cdot 6! = P(12,6).$$
That *is* the identity $\binom{n}{k}\,k! = P(n,k)$ — choosing-then-arranging and arranging-directly are the same count, partitioned two ways.

**Step 3 — Trainer's Path (the fast how).**
$$\text{(a)}\;\; \binom{12}{6} = \frac{12!}{6!\,6!} = 924. \qquad \text{(b)}\;\; 924 \times 6! = 924 \times 720 = 665{,}280 = P(12,6).$$
On the TI-30XS: [12]{.keystroke} [prb]{.kbd} → nCr [6]{.keystroke} [=]{.kbd} gives `924`.

**Step 4 — Check & pitfall.** $\binom{12}{6}=924$ is the *central* (largest) binomial coefficient for $n=12$, a good sanity check. **Pitfall:** multiplying $\binom{12}{6}$ by $12!$ instead of $6!$ — you arrange only the *chosen* six, not all twelve. *(Back-ref: Entries №02, №03.)*

### Worked Example 4.2 — Brock's Battle Order (partial guidance)

**ARCHETYPE:** *Ordered selection without replacement — permutation $P(n,k)$.*

**Setup.** Brock keeps $8$ Pokémon and battles with $3$, sent out in order. How many distinct ordered line-ups?

**Identify.** Three ordered battle slots, no reuse, **order matters** (lead vs. anchor differ). Permutation. *Your move: fill the shrinking menu.*

$$P(8,3) = \underbrace{8}_{\text{lead}} \times \underbrace{7}_{\text{second}} \times \underbrace{6}_{\text{anchor}} = \frac{8!}{5!} = 336.$$
On the TI-30XS: [8]{.keystroke} [prb]{.kbd} → nPr [3]{.keystroke} [=]{.kbd} gives `336`.

**Check & pitfall.** $P(8,3)$ should exceed the unordered $\binom{8}{3}=56$ by exactly $3!=6$, and $56\times6=336$ ✓. **Pitfall:** using $\binom{8}{3}$ — that counts the *roster*, ignoring send-out order. *(Back-ref: Entry №02.)*

### Worked Example 4.3 — The Pidgey Flock (binomial; light guidance)

**ARCHETYPE:** *Successes in $n$ independent with-replacement trials — binomial.*

**Setup.** A flock of $6$ Pidgey; each independently flushes w.p. $p=0.3$. Find (a) $P(\text{exactly }2\text{ flush})$ and (b) $P(\text{at least one flushes})$.

**(a)** Independent, identical, with-replacement trials — binomial. Count *which* $2$, times one pattern:
$$P(2)=\binom{6}{2}(0.3)^2(0.7)^4 = 15(0.09)(0.2401) \approx 0.3241.$$

**(b)** "At least one" by complement:
$$P(\ge 1) = 1 - P(0) = 1 - (0.7)^6 = 1 - 0.117649 \approx 0.8824.$$

**Check & pitfall.** Each binomial probability lies in $[0,1]$ ✓; "at least one" $0.88$ is large, as expected for six tries ✓. **Pitfall:** dropping the $\binom{6}{2}$ in (a) (that gives one *specific* pattern, $0.0216$), or modelling this **without** replacement (the flock doesn't deplete — independence holds). *(Back-ref: Entry №04.)*

### Worked Example 4.4 — The Caterpie Cluster (hypergeometric; light guidance)

**ARCHETYPE:** *Without-replacement exact type-count — hypergeometric probability.*

**Setup.** Cluster of $10$: $4$ Caterpie, $6$ others. Grab $3$ without replacement. Find (a) $P(\text{exactly }2\text{ Caterpie})$ and (b) $P(\text{at least }2\text{ Caterpie})$.

**(a)** Favorable = choose $2$ of $4$ Caterpie **and** $1$ of $6$ others, over all $3$-of-$10$ hands:
$$P(2) = \frac{\binom{4}{2}\binom{6}{1}}{\binom{10}{3}} = \frac{6\cdot6}{120} = 0.30.$$

**(b)** "At least $2$" = exact-$2$ plus exact-$3$:
$$P(\ge2) = P(2) + P(3) = \frac{36}{120} + \frac{\binom{4}{3}\binom{6}{0}}{120} = \frac{36+4}{120} = \frac{40}{120} = \frac{1}{3} \approx 0.333.$$

**Check & pitfall.** The four type-counts sum to $\binom{10}{3}$: $\tfrac{20+60+36+4}{120}=1$ ✓. **Pitfall:** modelling this **with** replacement (binomial) — wrong model, since grabbing a Caterpie depletes the cluster. Contrast WE 4.3: same "exactly $x$" language, opposite machine. *(Back-ref: Entry №06.)*

### Worked Example 4.5 — Arranging "CATERPIE" (multinomial; exam speed)

**ARCHETYPE:** *Arrangement with a repeated element — multinomial.*

**Setup.** Distinguishable arrangements of the $8$ letters in **CATERPIE** (two E's)?

<figure style="margin:1em auto; max-width:120px; text-align:center;">
<img src="../../assets/sprites/front/10.png" alt="Caterpie" style="width:96px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;"><strong>#010 Caterpie</strong> — eight letters, two of them E</figcaption>
</figure>

$$\frac{8!}{2!} = \frac{40{,}320}{2} = 20{,}160.$$

**Check & pitfall.** All distinct would be $8!$; the two identical E's collapse each pair to one, so divide by $2!$. **Pitfall:** reporting $40{,}320$ — that double-counts every word by swapping indistinguishable E's. *(Back-ref: Entry №05.)*

### Worked Example 4.6 — The Forest Lock (counting principle; exam speed)

**ARCHETYPE:** *Multi-stage choice — fundamental counting principle, with vs. without repeats.*

**Setup.** A forest gate has $4$ dial positions, each showing a digit $0$–$9$. How many codes (a) if repeats are allowed, (b) if no digit may repeat?

$$\text{(a)}\;\; 10^4 = 10{,}000. \qquad \text{(b)}\;\; 10 \times 9 \times 8 \times 7 = P(10,4) = 5040.$$

**Check & pitfall.** Without repeats must be *fewer* than with repeats, and $5040 < 10{,}000$ ✓. **Pitfall:** writing $10^4$ when the problem forbids repeats (or $P(10,4)$ when it allows them) — read the replacement condition first. *(Back-ref: Entries №01, №02.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — The "would reshuffling change the answer?" test**

When you can't tell a permutation from a combination, ask one question: *if I rearrange the items I picked, is that a new outcome?* **Yes** $\to$ permutation ($P(n,k)$ or $n!$). **No** $\to$ combination ($\binom{n}{k}$). "Battle order," "podium," "PIN," "schedule" = yes. "Team," "hand," "committee," "sample" = no. This one question resolves the great majority of counting questions before you write anything.
:::

::: trainers-tip
**TRAINER'S TIP — Binomial or hypergeometric? Ask "does the pool deplete?"**

The two probability models look identical in words ("exactly $x$ of a type") but split on one question: **is each draw put back (replacement)?** *Yes / independent trials with a fixed $p$* $\to$ **binomial** $\binom{n}{x}p^x(1-p)^{n-x}$. *No / the pool shrinks each draw* $\to$ **hypergeometric** $\binom{K}{x}\binom{N-K}{k-x}/\binom{N}{k}$. "Flips," "rolls," "each customer independently," "with replacement" = binomial. "Drawn from a box / cluster / urn without replacement," "a committee from a group" = hypergeometric. When $N$ is huge relative to the draw, the two nearly agree — but on the exam, draw the line by replacement.
:::

::: trainers-tip
**TRAINER'S TIP — nCr / nPr keystrokes (TI-30XS MultiView)**

For $\binom{n}{k}$: type $n$, press [prb]{.kbd}, select nCr, type $k$, press [=]{.kbd}. For $P(n,k)$: same path, select nPr. Example: [12]{.keystroke} [prb]{.kbd} nCr [6]{.keystroke} [=]{.kbd} → `924`. For a combinatorial probability, compute numerator and denominator separately and store the denominator with [sto▸]{.kbd} to avoid retyping and rounding drift.
:::

::: trainers-tip
**TRAINER'S TIP — "At least / at most" = sum the cases (or complement)**

There is no single binomial coefficient for "$\ge 2$" or "$\le 1$." Either **add the disjoint exact-counts**, or take **$1$ minus the complement** — whichever has fewer terms. "At least $1$" is almost always fastest as $1 - P(\text{none})$. And remember: for a hypergeometric your exact type-counts must sum to $\binom{N}{k}$ — a free error check.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

<figure style="margin:1em auto; max-width:150px; text-align:center;">
<img src="../../assets/characters/rocket.png" alt="Team Rocket — Jessie, James, and Meowth" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
</figure>

"Easy, twerps!" James crows, spreading a blueprint. "We pick **3** Pokémon from our stash of **6** to ambush the brat. So the number of evil schemes is $P(6,3) = 6\cdot5\cdot4 = 120$! A hundred and twenty plots!"

"A hundred and twenty?!" Meowth's eyes gleam. "We're geniuses!"

Jessie frowns. "But James — Weezing-then-Arbok-then-Lickitung is the *same ambush squad* as Lickitung-then-Arbok-then-Weezing. They all attack at once. We just counted each squad six times over."

James's grin curdles.

**Where it fails:** James used a **permutation** for an **unordered** choice. A simultaneous ambush squad is a *set*, not a sequence — order doesn't matter, so reshuffling the three is the *same* plot. Their "$120$ schemes" are really $\binom{6}{3} = 20$; they multiplied by the $3! = 6$ orderings of a group whose order is irrelevant. The fix is the whole of Concept 2: if rearranging the chosen items changes nothing, use $\binom{n}{k}$, not $P(n,k)$ — divide the permutation count by $k!$. (Counting an ordered arrangement when order doesn't matter — double-counting by $k!$ — is the single most common counting error on the exam, and it cost Team Rocket a factor of six. You'll catch them red-handed in Problem C4.8.)
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

Counting is the skeleton of **risk classification and selection odds**.

When an auto insurer prices a policy, it sorts each driver into a **rating cell** defined by a *combination* of factors — age band × territory × vehicle class × prior-claims tier. Counting how many distinct cells a model produces is a pure fundamental-counting-principle calculation: multiply the number of levels in each factor. That count tells the actuary how *thinly* the data is spread — if six factors with a handful of levels each produce thousands of cells, many cells will hold too few policies to be credible, and the model must be coarsened. Multiplication across stages literally sizes the rating plan.

The same machines price **selection odds**: the astronomically small chance behind a lottery jackpot ($1/\binom{49}{6}$-style counts) is favorable-over-total exactly like the Caterpie cluster; and the **without-replacement** structure — auditing a finite batch of policies, sampling defective parts from a finite lot — is *hypergeometric*, while **independent repeated trials** (each of a million policyholders independently filing or not) is *binomial*. Telling those two apart is the same "does the pool deplete?" question you drilled here.

*Series bridge:* the rating-cell count returns in **CAS Exam 5** (ratemaking) and in the design matrices of the **predictive-analytics** exams; the **binomial** and **hypergeometric** you built here reappear by name as discrete distributions in ch05 and feed aggregate-loss and credibility models on **STAM / MAS-I**.

*Transfer check:* could you solve this with **no Pokémon in it**? "An urn holds $4$ red and $6$ white balls; draw $3$ without replacement — find $P(\text{exactly } 2 \text{ red})$." Same machine, same $0.30$. And "flip a fair coin $6$ times — find $P(\text{exactly }3\text{ heads})$" is the Pidgey flock, $0.3125$. If you can do those, the skill has transferred.
:::

## The Gym Battle — Boulder Badge Capstone

<figure style="display:flex; gap:18px; flex-wrap:wrap; justify-content:center; align-items:flex-end; margin:1.5em auto;">
<figure style="margin:0; text-align:center;">
<img src="../../assets/vs/brock.png" alt="Brock, the Pewter City Gym Leader" style="width:150px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;"><strong>Brock</strong> — the Boulder Badge challenge</figcaption>
</figure>
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/95.png" alt="Onix, Brock's anchor Pokemon" style="width:160px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;"><strong>#095 Onix</strong> — Brock's anchor</figcaption>
</figure>
</figure>

**Brock's Challenge.** "One question for the Boulder Badge, Ash — and it's four counts in one. Count, don't guess. And know *which machine* each part wants."

> From a pool of **5 Rock-type trainers** and **7 non-Rock trainers** ($12$ distinct people), Brock forms a **panel of 4**.
>
> **(a)** How many distinct panels are possible?
> **(b)** How many panels contain **at least 2** Rock-type trainers?
> **(c)** If the panel is drawn *at random* from the $12$, what is $P(\text{exactly 2 Rock-types})$?
> **(d)** Once a $4$-person panel is chosen, in how many ways can they be seated in $4$ distinct chairs (Lead, Second, Third, Anchor)?

**ARCHETYPE:** *Integrative — combination counting, "at least" by casework, hypergeometric probability, and choose-then-seat.*

**Step 1 — Identify each part.** (a) unordered choice of $4$ from $12$ $\to \binom{12}{4}$. (b) "at least $2$ of $5$ Rock" $\to$ sum the favorable Rock-counts $\{2,3,4\}$ with $\binom{K}{x}\binom{N-K}{k-x}$, or complement. (c) divide the exact-$2$ count by $\binom{12}{4}$ — a hypergeometric, because the panel is drawn *without replacement*. (d) seat the chosen $4$ $\to 4!$.

**Step 2 — Trainer's Path.**

**(a)** Total panels:
$$\binom{12}{4} = \frac{12\cdot11\cdot10\cdot9}{4!} = \frac{11{,}880}{24} = 495.$$

**(b)** "At least $2$ Rock" = exactly $2$, $3$, or $4$ Rock (rest from the $7$ non-Rock):
$$\binom{5}{2}\binom{7}{2} + \binom{5}{3}\binom{7}{1} + \binom{5}{4}\binom{7}{0} = (10)(21)+(10)(7)+(5)(1) = 210+70+5 = 285.$$
*Faster by complement* — total minus ($0$ Rock) minus ($1$ Rock):
$$495 - \binom{5}{0}\binom{7}{4} - \binom{5}{1}\binom{7}{3} = 495 - 35 - 5\cdot35 = 495 - 35 - 175 = 285. \;\checkmark$$

**(c)** Probability of exactly $2$ Rock under random draw (hypergeometric):
$$P(\text{exactly 2 Rock}) = \frac{\binom{5}{2}\binom{7}{2}}{\binom{12}{4}} = \frac{(10)(21)}{495} = \frac{210}{495} = \frac{14}{33} \approx 0.4242.$$

**(d)** Seat the chosen $4$ in $4$ labeled chairs:
$$4! = 24.$$

**Step 3 — Professor's Path (cross-check on (b)).** The full Rock-count distribution must total $\binom{12}{4}=495$:
$$\sum_{x=0}^{4}\binom{5}{x}\binom{7}{4-x} = 35 + 175 + 210 + 70 + 5 = 495. \;\checkmark$$
"At least $2$" is the last three terms, $210+70+5 = 285$ — the Trainer's Path confirmed.

**Step 4 — Check, verdict & the pitfalls Brock is testing.** Every probability sits in $[0,1]$, and the counts in (b)/(c) are bounded by $495$ ✓. **Pitfalls Brock is probing:** in (b), there is no single $\binom{}{}$ for "$\ge 2$" — sum disjoint cases or complement; in (c), the without-replacement draw is *hypergeometric*, not a binomial $\binom{4}{2}(5/12)^2(7/12)^2$; and in (d), seating only the *four* chosen panelists means $4!$, not $12!$ or $4^4$.

> "You counted," Brock says, unclipping a stone-gray badge. "You didn't guess — and you knew which machine each part wanted. The Boulder Badge is yours."

## The Gym Challenge — Problem Set

::: problem-set
**THE VIRIDIAN FOREST & THE PEWTER GYM — your questline.** Brock has set you a single escalating mission: first the **Route Trainer** legs (crossing the forest — warming up the counting machines), then the **Gym Battle** tier (the boss fight — true SOA-difficulty counts and probabilities), then the optional **Elite Challenge** post-game. Work it timed (~5 min/problem), then check the **Answers** below. Hit the mastery bar (**80%+ with correct method**) to clear the questline and claim the Boulder Badge. Problems are listed first; full worked solutions follow afterward. Markers: 🔴 routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (the early legs — crossing the forest, warming up)

**C4.1.** 🔴 *(Brute-forcing the forest gate's lock.)* The gate has $4$ dial positions, each an independent digit $0$–$9$ with repeats allowed. How many distinct codes must you be prepared to try?

**C4.2.** 🔴 *(Posing your caught Pokémon for Oak.)* You've caught $7$ distinct Pokémon and display $3$ of them left-to-right in a photo (order is part of the picture). How many distinct photos?

**C4.3.** 🔴 *(Picking a team where order is irrelevant.)* From the same $7$ caught Pokémon you select a $3$-Pokémon team for a battle (order on the sheet doesn't matter). How many distinct teams?

**C4.4.** 🔴 *(Scrambling a name into a cipher.)* How many distinguishable arrangements of the letters in **WEEDLE** are there? (W, E, E, D, L, E — note the repeated letter.)

**C4.5.** 🟡 *(Lining up Misty's evolution stones.)* Misty packs $3$ identical Water Stones, $2$ identical Thunder Stones, and $1$ Leaf Stone into a row of $6$ slots. How many distinguishable line-ups?

**C4.6.** 🔴 *(A flock warm-up — independent flushes.)* A flock of $5$ Pidgey each independently flushes w.p. $p=0.4$. Find $P(\text{exactly }2\text{ flush})$.

**C4.26.** 🔴 *(DECISION — which counter fits the scene?)* You must find "$P(\text{exactly }2\text{ Caterpie})$" in two scenarios: **(i)** grab $3$ from a cluster of $10$ ($4$ Caterpie) **without replacement**; **(ii)** spot $3$ Caterpie-or-not sightings, each *independently* Caterpie w.p. $0.4$. State which machine each needs (hypergeometric vs. binomial) and why — no need to finish the arithmetic.

> *Questline beat: the forest thins and your machines are warm. Brock is waiting at the gym. The boss fights begin.*

### Gym Battles (the boss fight — true SOA difficulty)

**C4.7.** 🟡 *(Scooping grass Pokémon — exactly one Oddish.)* A cluster of $9$ grass Pokémon holds $4$ Oddish and $5$ Bellsprout. You scoop $3$ at random without replacement. Find $P(\text{exactly 1 Oddish})$.

**C4.8.** 🟡 *(AUDIT — Team Rocket's ambush count.)* James boasts that picking $3$ of Team Rocket's $6$ Pokémon for a *simultaneous* ambush gives $P(6,3)=120$ "schemes." Find the correct number of distinct squads and name James's error.

**C4.9.** 🟡 *(At-least-one badge holder, by complement.)* A study group of $10$ trainers — $6$ Boulder-Badge holders and $4$ without — randomly selects a $3$-trainer panel. Find $P(\text{at least 1 holder})$ using the complement.

**C4.10.** 🟡 *(Shortest grid walks to Pewter.)* You walk a grid from camp (bottom-left) to Pewter (top-right) taking only steps East or North, on a $4$-block-East by $3$-block-North grid. How many distinct shortest paths? *(Each path is an arrangement of $4$ E's and $3$ N's.)*

**C4.11.** 🟡 *(A type-balanced team with fixed counts.)* From $5$ Fire, $4$ Water, and $3$ Grass distinct Pokémon ($12$ total), assemble a team of $5$ with **exactly** $2$ Fire, $2$ Water, $1$ Grass. How many such teams?

**C4.12.** 🟡 *(Binomial — at least one flush.)* A flock of $6$ Pidgey each independently flushes w.p. $p=0.3$. Find $P(\text{at least one flushes})$ by the complement.

**C4.13.** 🔵 *(RIVAL TRAP — Gary picks the wrong machine.)* A box holds $10$ Poké Balls: $3$ Master and $7$ regular. You draw $4$ **without replacement**. Gary insists "each draw is Master w.p. $0.3$, so $P(\text{exactly 2 Master})=\binom{4}{2}(0.3)^2(0.7)^2$." Compute Gary's binomial value *and* the correct hypergeometric value, and name his error.

**C4.14.** 🔵 *(AUDIT — a double-counted committee.)* A trainer's notes claim "the number of $3$-trainer panels from $9$ people is $P(9,3)=504$." Find the correct count and name the error.

**C4.15.** 🟡 *(Choose-then-assign positions.)* Brock fields $9$ Pokémon, chooses $4$ to battle, then assigns them to $4$ *distinct* positions (Lead, Second, Third, Anchor). In how many ways can he both choose and assign?

**C4.24.** 🟡 *(AUDIT — an "at least" treated as one combination.)* A note computes "$P(\text{at least }2\text{ Caterpie})$" from the cluster of $10$ ($4$ Caterpie, grab $3$) as the single term $\binom{4}{2}\binom{6}{1}/\binom{10}{3}=0.30$. Find the correct $P(\ge 2)$ and name the error.

> *Questline beat: the Boulder Badge is yours. The post-game below is optional — the integrative challenges where the league players sharpen up.*

### Elite Challenge (post-game — integrative / stretch)

**C4.16.** 🔵 *(Rare Master Balls — at least/at most by casework.)* A box holds $13$ Poké Balls: $3$ Master, $4$ Ultra, $6$ Great. Draw $5$ at random without replacement. Find $P(\text{at least 2 Master})$ and $P(\text{at most 1 Master})$, and confirm they sum to $1$.

**C4.17.** 🔵 *(RIVAL TRAP — Gary forgets to discard order.)* Ten distinct trainers, including you and Gary, are seated at random in a row of $10$ chairs. Gary claims "$P(\text{we sit together})$ needs permutations of all $10$, so it's $1/10!$ — basically zero." Find the correct probability and name Gary's error.

**C4.18.** 🔵 *(Integrative — choose-then-seat, all-one-type, exactly-$k$.)* From $6$ Rock-type and $6$ non-Rock distinct trainers ($12$ total), a $4$-person squad is chosen at random and seated in $4$ labeled chairs. **(a)** How many seated arrangements in total? **(b)** $P(\text{all 4 chairs filled by Rock-types})$? **(c)** $P(\text{the squad contains exactly 2 Rock-types})$ (seating irrelevant for (c)).
:::

## Answers

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

### Quick-Answer Table

| # | Answer | Archetype | | # | Answer | Archetype |
|---|---|---|---|---|---|---|
| C4.1 | $10{,}000$ | standard | | C4.13 | binomial $0.2646$ vs. correct $0.30$; wrong model | rival_trap |
| C4.2 | $210$ | standard | | C4.14 | $\binom{9}{3}=84$ (not $504$) | audit |
| C4.3 | $35$ | standard | | C4.15 | $3024$ | standard |
| C4.4 | $120$ | standard | | C4.16 | $P(\ge2)\approx0.3147;\ P(\le1)\approx0.6853$ | standard |
| C4.5 | $60$ | standard | | C4.17 | $1/5=0.2$ (not $1/10!$) | rival_trap |
| C4.6 | $0.3456$ | standard | | C4.18 | (a) $11{,}880$; (b) $1/33$; (c) $5/11$ | standard |
| C4.7 | $10/21\approx0.4762$ | standard | | C4.24 | $P(\ge2)=1/3$ (not $0.30$) | audit |
| C4.8 | $\binom{6}{3}=20$ (not $120$) | audit | | C4.26 | (i) hypergeometric; (ii) binomial | decision |
| C4.9 | $29/30\approx0.9667$ | standard | | | | |
| C4.10 | $35$ | standard | | | | |
| C4.11 | $180$ | standard | | | | |
| C4.12 | $1-(0.7)^6\approx0.8824$ | standard | | | | |

**C4.1** — *(standard) With-replacement ordered count (Entry №01).* Four independent dials, $10$ choices each, repeats allowed: $10\times10\times10\times10 = 10^4 = 10{,}000$ codes.

**C4.2** — *(standard) Ordered selection without replacement (Entry №02).* $P(7,3) = 7\cdot6\cdot5 = 210$ photos.

**C4.3** — *(standard) Unordered selection (Entry №03).* $\binom{7}{3} = \frac{7\cdot6\cdot5}{3!} = \frac{210}{6} = 35$ teams. (Note $35 = P(7,3)/3!$ — the same scene as C4.2 with order discarded.)

**C4.4** — *(standard) Arrangement with repeats (Entry №05).* WEEDLE has $6$ letters with **E repeated $3$ times**: $\frac{6!}{3!} = \frac{720}{6} = 120$.

**C4.5** — *(standard) Multinomial arrangement (Entry №05).* Six items in blocks $3,2,1$: $\binom{6}{3,2,1} = \frac{6!}{3!\,2!\,1!} = \frac{720}{12} = 60$ ways.

**C4.6** — *(standard) Binomial pmf (Entry №04).* $\binom{5}{2}(0.4)^2(0.6)^3 = 10(0.16)(0.216) = 0.3456$.

**C4.7** — *(standard) Hypergeometric exact count (Entry №06).* $P(\text{1 Oddish}) = \frac{\binom{4}{1}\binom{5}{2}}{\binom{9}{3}} = \frac{4\cdot10}{84} = \frac{40}{84} = \frac{10}{21} \approx 0.4762$.

**C4.8** — *(audit) Permutation used for an unordered choice (Entries №02, №03).* A *simultaneous* ambush squad is a **set** — order doesn't matter — so the count is $\binom{6}{3} = \frac{6\cdot5\cdot4}{3!} = 20$ squads, not $P(6,3)=120$. **James's error:** he used a permutation (ordered) for an unordered choice, over-counting each squad by $3!=6$ times ($120 = 20\times6$). This is the chapter's Team Rocket trap.

**C4.9** — *(standard) "At least one" via complement (Entries №03, №06).* Complement = panel of $3$ entirely from the $4$ non-holders: $P(\ge1) = 1 - \frac{\binom{4}{3}}{\binom{10}{3}} = 1 - \frac{4}{120} = 1 - \frac{1}{30} = \frac{29}{30} \approx 0.9667$.

**C4.10** — *(standard) Lattice path = multinomial (Entry №05).* Each path is a sequence of $4$ E's and $3$ N's: $\frac{7!}{4!\,3!} = \binom{7}{3} = 35$ paths.

**C4.11** — *(standard) Independent group choices, multiply combinations (Entries №01, №03).* $\binom{5}{2}\binom{4}{2}\binom{3}{1} = 10\cdot6\cdot3 = 180$ teams.

**C4.12** — *(standard) Binomial "at least one" by complement (Entry №04).* $P(\ge1) = 1 - P(0) = 1 - (0.7)^6 = 1 - 0.117649 \approx 0.8824$.

**C4.13** — *(rival_trap) Binomial used for a without-replacement draw (Entries №04, №06).* Gary's binomial: $\binom{4}{2}(0.3)^2(0.7)^2 = 6(0.09)(0.49) = 0.2646$. Correct **hypergeometric** (the draw depletes the box): $\frac{\binom{3}{2}\binom{7}{2}}{\binom{10}{4}} = \frac{3\cdot21}{210} = \frac{63}{210} = 0.30$. **Gary's error:** he used the binomial (fixed $p$, with replacement) for a *without-replacement* draw — the success probability shifts as Master Balls are removed, so the right model is the hypergeometric. ($0.2646 \ne 0.30$.)

**C4.14** — *(audit) Permutation used for an unordered committee (Entries №02, №03).* A *panel* is unordered: $\binom{9}{3} = \frac{9\cdot8\cdot7}{3!} = \frac{504}{6} = 84$. **The error:** the note used $P(9,3)=504$ — the ordered count — over-counting each panel by $3!=6$. ($504/6 = 84$.)

**C4.15** — *(standard) Choose-then-arrange / ordered selection (Entries №02, №03).* $\binom{9}{4}\cdot 4! = 126\cdot24 = 3024 = P(9,4) = 9\cdot8\cdot7\cdot6$.

**C4.16** — *(standard) "At least"/"at most" by casework; totals sum to $1$ (Entry №06).* Total $=\binom{13}{5}=1287$; let $M$ = Master Balls drawn ($M\le3$).
$$P(M\le1)=\frac{\binom{3}{0}\binom{10}{5}+\binom{3}{1}\binom{10}{4}}{1287}=\frac{252+630}{1287}=\frac{882}{1287}\approx0.6853,$$
$$P(M\ge2)=\frac{\binom{3}{2}\binom{10}{3}+\binom{3}{3}\binom{10}{2}}{1287}=\frac{360+45}{1287}=\frac{405}{1287}\approx0.3147.$$
Check: $882+405=1287$, so the two sum to $1$. ✓

**C4.17** — *(rival_trap) Forgetting the right sample space / glued block (Entries №02, №06).* Total seatings $=10!$. Glue you-and-Gary into one block ($2$ internal orders), arranging $9$ units: favorable $=2\cdot9!$. $P = \frac{2\cdot9!}{10!} = \frac{2}{10} = \frac{1}{5} = 0.2$. **Gary's error:** $1/10!$ is the chance of *one specific full seating*, not the event "we sit together"; the event spans $2\cdot9!$ equally likely seatings. The correct probability is $0.2$, not "basically zero."

**C4.18** — *(standard) Integrative: choose-then-seat, all-one-type, exactly-$k$ (Entries №02, №03, №06).*
**(a)** Choose $4$ of $12$ and seat them: $\binom{12}{4}\cdot4! = 495\cdot24 = 11{,}880 = P(12,4)$.
**(b)** All $4$ Rock; seating cancels (identical in favorable and total), so it equals the unordered version: $P(\text{all Rock}) = \frac{\binom{6}{4}}{\binom{12}{4}} = \frac{15}{495} = \frac{1}{33} \approx 0.0303$.
**(c)** Exactly $2$ Rock (hypergeometric): $P = \frac{\binom{6}{2}\binom{6}{2}}{\binom{12}{4}} = \frac{15\cdot15}{495} = \frac{225}{495} = \frac{5}{11} \approx 0.4545$.

**C4.24** — *(audit) An "at least" reported as a single exact-count (Entry №06).* "At least $2$" is *not* one combination — it's exact-$2$ plus exact-$3$: $P(\ge2) = P(2)+P(3) = \frac{\binom42\binom61}{\binom{10}{3}} + \frac{\binom43\binom60}{\binom{10}{3}} = \frac{36+4}{120} = \frac{40}{120} = \frac13 \approx 0.333$. **The error:** the note reported only the exact-$2$ term ($0.30$) for an "at least $2$" question; sum the disjoint cases (or complement).

**C4.26** — *(decision) Pick the machine by replacement (Entries №04, №06).* **(i)** Grabbing $3$ from a finite cluster *without replacement* depletes the pool, so the success rate shifts each draw — **hypergeometric**, $\binom{4}{2}\binom{6}{1}/\binom{10}{3}$. **(ii)** Three *independent* sightings each Caterpie w.p. a fixed $0.4$ are repeated trials with replacement — **binomial**, $\binom{3}{2}(0.4)^2(0.6)$. The deciding question is always "does the pool deplete?": yes $\to$ hypergeometric, no $\to$ binomial.
:::

## Badge Earned — the Boulder Badge

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/boulder_badge.png" alt="The Boulder Badge, a gray octagonal gym badge" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Boulder Badge earned!</strong> Rank: Junior Trainer · 3 badges (Cascade, Thunder, Boulder).</figcaption>
</figure>

You proved to Brock that you can *count* — not guess — and that you know *which machine* each question wants, and he pressed the **Boulder Badge** into your hand. **Rank: Junior Trainer · 3 badges** (Cascade + Thunder + Boulder). Three down, five to go on the road to the Indigo Plateau.

**Mastery checklist — tick each before you move on (mapped 1-to-1 to the SOA outcomes):**

- ☐ **(1b)** I can **multiply across stages** with the fundamental counting principle, choosing *multiply* (AND) over *add* (OR). *(Rematch: Concept 0, WE 4.6, Problems C4.1.)*
- ☐ **(1b)** I can tell a **permutation** from a **combination** on sight and compute $P(n,k)$ or $\binom{n}{k}$, including the bridge $P(n,k)=\binom{n}{k}\,k!$. *(Rematch: Concepts 1–2, WE 4.1–4.2, Problems C4.2, C4.3, C4.8, C4.14.)*
- ☐ **(1b)** I can **classify** any task with the ordered/unordered × with/without-replacement $2\times2$ grid before computing. *(Rematch: the $2\times2$ classifier tip, Problem C4.26.)*
- ☐ **(1b, 2d)** I can use the **binomial** $\binom{n}{x}p^x(1-p)^{n-x}$ for successes in $n$ independent, with-replacement trials, and handle "at least one" by complement. *(Rematch: Concept 3, WE 4.3, Problems C4.6, C4.12.)*
- ☐ **(1b)** I can count **distinguishable arrangements** with the multinomial $\frac{n!}{n_1!\cdots n_r!}$ (including lattice-path problems). *(Rematch: Concept 4, WE 4.5, Problems C4.4, C4.5, C4.10.)*
- ☐ **(1b, 2d)** I can turn a **without-replacement** count into a probability — the **hypergeometric** $\binom{K}{x}\binom{N-K}{k-x}/\binom{N}{k}$ — handle "at least/at most" by casework, and tell it from the binomial by asking "does the pool deplete?" *(Rematch: Concept 5, WE 4.4, Problems C4.7, C4.9, C4.13, C4.16, C4.18, C4.24, C4.26.)*

**Gym Rematch pointers.** Counted an ordered arrangement when order didn't matter? Concept 2 Beat 4 and the Team Rocket Trap, then C4.8, C4.14. Used a binomial for a depleting draw? Concept 5 Beat 4 and the binomial-or-hypergeometric tip, then C4.13, C4.26. Reported an "at least" as one combination? Concept 5 Beat 7, then C4.24. Forgot to divide $n!$ by an identical block? Concept 4 Beat 4, then C4.4, C4.5.

> Next stop: **Lavender Tower and Celadon City**, where the wild things appear on a *timer* — first successes, waits, and rare-event counts — and you'll meet the geometric and Poisson on the way to Erika's Rainbow Badge. Pack your counting machines; every distribution there is a count with probabilities attached.

*Pokémon is owned by Nintendo / Game Freak / Creatures Inc.; this is an educational, non-commercial work. Exam details verified against the SOA Exam P syllabus (September 2026).*
