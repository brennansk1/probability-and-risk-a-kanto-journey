<!--
  file: ch08_discrete
  tier: B
  outcomes: 2d2
  draft1_source: drafts/chapters_draft1/ch06_celadon_city.md
  maps_to: Lavender Tower & Celadon Game Corner, Erika
-->

# The Named Patterns I — Discrete Distributions {.type-grass}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with the route from Cerulean through Lavender Town to Celadon City highlighted; the Game Corner and Erika's gym are marked." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>Route to a 10 — past the haunted Pokémon Tower of Lavender Town to Celadon City, home of the Game Corner and the Rainbow Badge: the city of <em>named chance</em>.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Lull in the Tower"**

Lavender Town at dusk. The Pokémon Tower rises seven storeys into a violet sky, and the air hums with a static that makes Pikachu's cheeks spark on their own. You climb because Mr. Fuji is trapped on the top floor — but every landing, **Gastly** wink in and out of the candlelight, never the same number twice. On the third-floor stairwell you count: in the first minute, two appear. In the next, none. Then four. Then one.

"You can't fight what you can't *predict*," Misty whispers, gripping her Staryu.

But you *can* predict it — not the exact count, but the **pattern**. Brock crouches over the caretaker's old visitor's log, where sightings were tallied for years. "Look. Over thousands of minutes, the average barely moves: about **three Gastly a minute**. Whatever law governs this place, it's stable."

Your Pokédex flickers into Actuary Mode. *"Caretaker's request,"* it reads. *"To pass safely you must wait for a lull — a stretch with very few Gastly. Estimate the probability that the next five minutes bring fewer than ten of them, so the party can move."*

Three a minute, on average. Random, but lawful. You need the probability of a **count** — and the only tools you own so far describe a *single* random variable's center and spread, not the *shape* of the law that produces a tally with no upper limit.

Then Pikachu tugs your sleeve and points downhill, toward the neon glow of **Celadon City**, where a Game Corner slot machine is already eating Misty's coins one pull at a time. Counts everywhere — wins out of ten pulls, pulls until the first win, ghosts per minute. Each is random, yet each follows a *named law* you could read off a card if only you knew the card. *How do you put a named law to a thing you can only count?*
:::

## Where You Are — 60-Second Retrieval

You hold the **Marsh Badge** from Saffron, and behind you sits a far more important prize from the last two chapters: the **language of a random variable**. You learned that a discrete random variable $X$ carries a **probability mass function (pmf)**

$$p(k) = P(X = k), \qquad \sum_k p(k) = 1,$$

read *"little-p of $k$ is the probability that $X$ equals $k$, and the masses sum to one."* You learned to compute its **expectation** $\E[X] = \sum_k k\,p(k)$ (the long-run average) and its **variance** $\Var(X) = \E[X^2] - (\E[X])^2$ (the spread). You also met the **moment generating function** $M_X(t) = \E[e^{tX}]$, the bar $\given$ for "given," and the counting tool $\binom{n}{k}$ ("$n$ choose $k$").

That is the entire foundation this chapter stands on. This chapter does **not** teach you a new *kind* of object — it teaches you **seven specific pmfs that come up again and again**, each born from a different *story*. Prove you still own the machinery before reading on.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you still own the last chapters**

Answer from memory; if any feels shaky, flip back before continuing.

1. A spinner lands on $1,2,3$ with $p(1)=0.5,\ p(2)=0.3,\ p(3)=0.2$. What is $\E[X]$? *(Answer: $0.5+0.6+0.6 = 1.7$.)*
2. What is $\binom{4}{2}$, and what does it count? *(Answer: $6$ — the number of ways to choose $2$ items from $4$.)*
3. For any pmf, what must $\sum_k p(k)$ equal? *(Answer: exactly $1$.)*

All three instant? You're ready. Any hesitation? The retrieval *is* the lesson — go reclaim it, then come back.
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Professor Oak's voice crackles through the Pokédex's Actuary Mode as you climb past the candlelight.

"Celadon is the city of *named patterns*, Ash. There are only a handful of stories chance tells with whole-number counts — *fixed tries, waiting for a win, drawing without replacement, events in time* — and each story has a distribution with a name, a formula, a mean, and a variance. The exam will not ask you to *invent* these. It will hand you a **story** and reward you for **recognizing** which named law it is, in under a minute, then reading the answer off a card you carry in your head. Learn to hear the story behind the symbols, and half of Exam P's biggest section is yours."

By the end of this chapter you will be able to:

- **Recognize and apply** the seven in-scope discrete families — **Bernoulli, binomial, geometric, negative binomial, hypergeometric, Poisson,** and **discrete uniform** — from the *story* a problem tells. *(Outcome 2d2.)*
- **Compute** each family's pmf, mean, and variance, and read them off a problem in under a minute. *(Outcome 2d2.)*
- **Distinguish** the count-models by their *generating mechanism*: **fixed number of trials** (binomial) vs. **waiting for a success** (geometric / negative binomial) vs. **drawing without replacement** (hypergeometric) vs. **events over a window** (Poisson). *(Outcome 2d2.)*
- **Deploy the shortcuts** that separate a 6 from a 10: the **binomial-to-Poisson** limit, the **finite-population correction**, **geometric memorylessness**, and **Poisson additivity & thinning**. *(Outcome 2d2.)*

> *Exam-weight signpost.* The discrete families sit inside the **Univariate Random Variables** block, the **single largest** section of Exam P (≈44–50%). This is a **Tier B** chapter: the *machinery* (pmf/mean/variance) you already own from Ch 6–7, so the new work is **recognition and the four shortcuts** — and that is where the depth here is spent. The Poisson and the geometric earn the fullest treatment; the discrete uniform earns a card and a wave.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own All of Celadon?**

Already fluent with the named discrete laws? Prove it. Work these five, ~1–3 minutes each, *with the right family named*:

1. $X\sim\Binom(10,0.2)$. Find $\E[X]$ and $P(X\ge 3)$.
2. You throw until a wild Pokémon flees; each throw works w.p. $0.15$. Find $P(\text{more than }5\text{ throws})$.
3. From $12$ Pokémon, $4$ of a rare line, draw $3$ without replacement. Find $P(\text{at least }2\text{ rare})$.
4. Gastly appear at $3$/min (Poisson). Find $P(\ge 2\text{ in one minute})$ and $P(<10\text{ in five minutes})$.
5. You wait for your $3$rd win; each round wins w.p. $0.4$. Find $P(\text{exactly }2\text{ losses before the 3rd win})$.

*(Answers: $\E=2,\ P(X\ge3)=0.3222$; $0.4437$; $0.2364$; $0.8009$ and $0.0699$; $0.13824$.)* Five for five with the **right family named each time**? **Skip to the Gym Challenge** and claim the badge. Any miss or hesitation? Each family below has its own skip-gate, so even a partial owner loses no time.
:::

---

Seven families build here, ordered by **how much teaching each needs** — easiest mechanism first, hardest last:

1. **Bernoulli** — the single yes/no trial *(the atom everything is built from)*
2. **Binomial** — count successes in a *fixed* number of trials
3. **Geometric** — *wait* for the first success *(memoryless)*
4. **Negative binomial** — wait for the $r$-th success *(geometric, $r$ times over)*
5. **Hypergeometric** — draw *without replacement* from a finite pool
6. **Poisson** — count events over a *window* of time or space *(the crown of the chapter)*
7. **Discrete uniform** — every value equally likely *(a card and a wave)*

The whole game is **hearing which story you're in.** We teach each with its own skip-gate, the lesson, then a Pokédex Entry you carry into the exam.

## Concept 1 — The Bernoulli Trial: The Atom of Counting

::: concept-gate
**DO YOU ALREADY OWN THIS? — Bernoulli**

A single slot pull wins w.p. $0.2$. Let $X=1$ if it wins, $0$ if not. What are $\E[X]$ and $\Var(X)$?

If you answered **$\E[X]=0.2$** and **$\Var(X)=0.2\cdot0.8=0.16$** instantly, **skip to Concept 2**. Otherwise this one-minute section is the seed of all six that follow.
:::

> *This is the chapter's simplest atom, so it runs an **abbreviated arc** (beats 1–6, 8, 9): the ramp (Beat 7) would be empty — a single trial has nowhere to ramp to. Every richer family below runs the full nine.*

**Beat 1 — The one-sentence idea.** *A Bernoulli variable is a single yes/no trial scored $1$ for "success" and $0$ for "failure."*

**Beat 2 — Anchor + concrete instance.** This is the simplest possible random variable, and every other family in this chapter is built by **repeating, waiting for,** or **summing** Bernoulli trials. One pull of the Game Corner slot wins with probability $p = 0.2$. Score it $X = 1$ for a win, $X = 0$ for a loss.

**Beat 3 — Reason through it in words.** The average score is "how often you win," which is just $p = 0.2$ — you get $1$ a fraction $p$ of the time and $0$ the rest. So $\E[X] = p$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** It is tempting to say the variance *is also* $p$ — "the spread is the win-rate." It is not:

$$\Var(X) \overset{?}{=} p = 0.2. \qquad\textbf{(wrong — that's the mean, not the spread)}$$

Variance measures distance-squared from the mean, and a $0/1$ variable is most spread out when it is a true coin flip ($p = \tfrac12$, where it is genuinely unpredictable) and *least* spread out near $p = 0$ or $p = 1$ (where it is nearly certain). A quantity equal to $p$ would grow all the way to $1$ as $p \to 1$ — the opposite of what spread does. The right answer must *vanish* at both ends, which is exactly what $p(1-p)$ does — and Beat 6 derives it.

**Beat 5 — Translate into notation, one glyph at a time.** Write $q = 1 - p$ for the failure probability (we will reuse $q$ all chapter — *"$q$ is just one-minus-$p$"*). The shorthand

$$X \sim \operatorname{Bernoulli}(p) \qquad \text{read aloud: ``}X \text{ is distributed Bernoulli with parameter } p\text{,''}$$

where the tilde $\sim$ reads **"is distributed as"** — it names the law that produced $X$.

**Beat 6 — Derive the variance.** Use $\Var(X) = \E[X^2] - (\E[X])^2$. Because $X$ is only ever $0$ or $1$, squaring changes nothing — $0^2 = 0$ and $1^2 = 1$ — so $X^2 = X$ and therefore $\E[X^2] = \E[X] = p$. Substituting,

$$\Var(X) = \E[X^2] - (\E[X])^2 = p - p^2 = p(1-p) = pq.$$

This vanishes at $p = 0$ and $p = 1$ and peaks at $p = \tfrac12$ (value $0.25$) — exactly the shape Beat 4 demanded. We *derived* $pq$; we did not assert it.

**Beat 8 — Picture it.** Two bars, and nothing else: the whole distribution is mass $q$ at $0$ and mass $p$ at $1$.

<figure>
<img src="../../assets/diagrams/ch08_bernoulli_pmf.png" alt="A two-bar chart of the Bernoulli(0.2) probability mass function: a tall gray bar at k=0 with height 0.8 (loss), and a shorter blue bar at k=1 with height 0.2 (win)." style="width:50%; max-width:340px; display:block; margin:1em auto;">
<figcaption>$\operatorname{Bernoulli}(0.2)$: all the mass sits on two values — $q = 0.8$ at "loss" and $p = 0.2$ at "win." Every other family in this chapter is built from bars like these.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can score any single success/failure event as a Bernoulli and write its mean $p$ and variance $pq$ on sight. Now we ask the key question: *how are several Bernoulli trials combined?*

::: pokedex-entry
**POKÉDEX ENTRY №01 — The Bernoulli Distribution**

$X \sim \operatorname{Bernoulli}(p)$, $X \in \{0,1\}$:
$$p(1) = p, \qquad p(0) = 1 - p = q.$$
$$\E[X] = p, \qquad \Var(X) = pq, \qquad M_X(t) = q + p\,e^{t}.$$

*In plain terms:* one coin flip, one slot pull, one Poké Ball throw — scored $1$ or $0$.

*Recognition cue:* a **single** trial with two outcomes. Reach for it, then immediately ask *"how are these trials combined?"* — that question routes you to the next six families.
:::

## Concept 2 — The Binomial: A Fixed Number of Trials

::: concept-gate
**DO YOU ALREADY OWN THIS? — Binomial**

You pull a slot $10$ times; each wins w.p. $0.2$, independently. Let $X$ = wins. What are $\E[X]$, $\Var(X)$, and $P(X=2)$?

If you wrote **$\E=2$, $\Var=1.6$, $P(X=2)=\binom{10}{2}(0.2)^2(0.8)^8 = 0.3020$** (and can say *why the $\binom{10}{2}$ is there*), **skip to Concept 3**. If you forgot the $\binom{10}{2}$ or used $\Var=2$, read on.
:::

**Beat 1 — The one-sentence idea.** *Fix the number of trials in advance, run them independently, and count the successes — that count is binomial.*

**Beat 2 — Anchor + concrete instance.** This is Concept 1 repeated a fixed number of times and **added up**. Misty decides, firmly, to pull the slot exactly $n = 10$ times, each an independent win with $p = 0.2$, and count her wins $X$. *What is $P(X = 2)$?*

**Beat 3 — Reason through it in words.** First fix a *specific* pattern of $2$ wins and $8$ losses, say WWLLLLLLLL. Because the pulls are independent, that one exact sequence has probability

$$\underbrace{(0.2)(0.2)}_{\text{2 wins}}\underbrace{(0.8)(0.8)\cdots(0.8)}_{\text{8 losses}} = (0.2)^2(0.8)^8.$$

But the $2$ wins need not land in the first two slots — they could be *any* $2$ of the $10$ positions, and every such arrangement has the **same** probability $(0.2)^2(0.8)^8$. How many arrangements? Exactly $\binom{10}{2} = 45$ (choose which $2$ of the $10$ pulls are wins). Add them:

$$P(X = 2) = \binom{10}{2}(0.2)^2(0.8)^8 = 45 \cdot 0.04 \cdot 0.16777 = 0.3020.$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** The classic slip is to *forget the count* and report just $(0.2)^2(0.8)^8 = 0.00671$:

$$P(X=2) \overset{?}{=} (0.2)^2(0.8)^8. \qquad\textbf{(wrong — counts only ONE arrangement)}$$

That answers "the first two pulls win and the rest lose," a single sequence — not "exactly two of the ten win." There are $45$ equally likely ways to get two wins, so you must **multiply by $\binom{10}{2}$**. The binomial coefficient is the *bookkeeping for which trials succeeded.*

**Beat 5 — Notation, one glyph at a time.** Write

$$X \sim \Binom(n, p), \qquad p(k) = \binom{n}{k} p^{k} q^{\,n-k}, \quad k = 0,1,\dots,n.$$

Read the pmf aloud: *"choose which $k$ of the $n$ trials succeed ($\binom{n}{k}$), each success costs a factor $p$ ($p^k$), each of the remaining $n-k$ failures costs a factor $q$ ($q^{\,n-k}$)."* Three pieces: **arrangements × successes × failures.**

**Beat 6 — Derive the mean and variance.** A binomial is the sum of $n$ independent Bernoulli($p$) trials, $X = B_1 + \cdots + B_n$. Expectation is **linear** (Ch 7), so

$$\E[X] = \sum_{i=1}^{n}\E[B_i] = n p.$$

Because the trials are **independent**, variances also add:

$$\Var(X) = \sum_{i=1}^{n}\Var(B_i) = n\,pq.$$

We did not memorize $np$ and $npq$ — we *built* them from "sum of $n$ atoms." Notice $\Var = npq < np = \E[X]$ since $q < 1$: **the binomial's variance is always below its mean.** Hold that fact — it is exactly what separates the binomial from the Poisson later.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $P(X = 2)$, above.
- *Twist — a tail by complement:* "at least $3$ wins" is fastest from the small end. $P(X \ge 3) = 1 - [p(0)+p(1)+p(2)]$. With $p(0)=0.8^{10}=0.1074$, $p(1)=10(0.2)(0.8^9)=0.2684$, $p(2)=0.3020$, this is $1 - 0.6778 = 0.3222$. *(Trap preview: $P(X\ge 3)$ subtracts $P(X\le 2)$, **not** $P(X\le 3)$.)*
- *Edge:* "all ten win" is the single sequence $p^{10}=0.2^{10}$; "none win" is $q^{10}=0.8^{10}$. No coefficient needed — there is only one way each.

**Beat 8 — Picture it.** The pmf is a bar chart, tallest near the mean $np = 2$.

<figure>
<img src="../../assets/diagrams/ch08_binomial_pmf.png" alt="A bar chart of the Binomial(10, 0.2) probability mass function. Bars rise from k=0 (height about 0.107), peak at k=2 (height about 0.302), and fall off toward k=10. A dashed vertical line marks the mean at np=2, and the bar for k=2 is highlighted to match the worked value 0.3020." style="width:78%; max-width:560px; display:block; margin:1em auto;">
<figcaption>$\Binom(10,0.2)$: the count of wins clusters around the mean $np = 2$. Each bar is $\binom{10}{k}(0.2)^k(0.8)^{10-k}$; the highlighted $k=2$ bar is $0.3020$.</figcaption>
</figure>

**Beat 9 — Consolidate.** Whenever the number of trials is **fixed in advance** and you **count the successes**, it is binomial: pmf $\binom{n}{k}p^k q^{n-k}$, mean $np$, variance $npq$.

::: pokedex-entry
**POKÉDEX ENTRY №02 — The Binomial Distribution**

$X \sim \Binom(n, p)$ counts successes in $n$ **fixed**, independent Bernoulli($p$) trials, $X \in \{0,1,\dots,n\}$:
$$p(k) = \binom{n}{k} p^{k} q^{\,n-k}, \qquad q = 1 - p.$$
$$\E[X] = np, \qquad \Var(X) = npq, \qquad M_X(t) = (q + p\,e^{t})^{n}.$$

*In plain terms:* you decide *in advance* to run $n$ trials and count how many succeed. Trials fixed, successes random. $\Var = npq < np = \E[X]$ always.

*Recognition cue:* **"out of $n$ trials," "$n$ independent attempts," a fixed $n$, count the successes.** (Bernoulli is the $n=1$ case.)
:::

## Concept 3 — The Geometric: Waiting for the First Success

::: concept-gate
**DO YOU ALREADY OWN THIS? — Geometric**

A wild Pokémon flees on each throw w.p. $0.15$; you throw until it flees. Find $P(\text{it takes more than }5\text{ throws})$, and state which "geometric convention" you used.

If you wrote **$P(X>5)=0.85^5 = 0.4437$** and can name your convention (trials-to-first-success), **skip to Concept 4**. If you reached for a binomial coefficient, read on — *waiting* has no fixed $n$ to choose from.
:::

**Beat 1 — The one-sentence idea.** *Keep running independent trials until the first success, and count how long it took — the wait is geometric.*

**Beat 2 — Anchor + concrete instance.** The binomial fixed $n$ and let the successes float; the geometric does the opposite — it **fixes the success at "the first one"** and lets the number of trials float. On each pass through the Tower's top chamber, a vengeful Marowak ghost manifests w.p. $p = 0.15$, independently. You keep returning until it appears. Let $X$ = the pass on which it first shows. *What is $P(X > 5)$?*

**Beat 3 — Reason through it in words.** "$X > 5$" means *the ghost has not appeared in the first $5$ passes* — i.e. all $5$ passes **failed**. Each failure has probability $q = 0.85$, and the passes are independent, so

$$P(X > 5) = (0.85)^5 = 0.4437.$$

More generally, the first success lands *exactly* on pass $k$ when the first $k-1$ passes fail and the $k$-th succeeds: $q^{k-1}p$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Two traps live here. First, the **convention** trap: "the wait" can mean either the *trial number* of the first success ($X \in \{1,2,\dots\}$) or the *number of failures before* it ($Y = X-1 \in \{0,1,\dots\}$). These differ by exactly $1$, so their means differ by $1$ ($\E[X]=1/p$ vs. $\E[Y]=q/p$) while the **variance is identical**. Always *state your convention*. Second, the **binomial-coefficient** trap: there is no $\binom{\cdot}{\cdot}$ here, because the success position is *forced* to be last — there is only one arrangement of "$k-1$ failures then a success."

**Beat 5 — Notation, one glyph at a time.** *Trials version* ($X$ = trial of first success):

$$X \sim \Geom(p), \qquad p(k) = q^{\,k-1}p, \quad k = 1,2,3,\dots$$

Read aloud: *"$k-1$ failures, each a factor $q$, then one success, a factor $p$."* The **survival** function (probability of waiting *past* $m$) is especially clean:

$$P(X > m) = q^{m} \qquad \text{read aloud: ``the first } m \text{ trials all failed.''}$$

**Beat 6 — Derive the mean (and the memoryless property).** The survival form gives the mean cleanly by the **tail-sum** rule for nonnegative integers, $\E[X] = \sum_{m\ge 0}P(X>m) = \sum_{m\ge 0}q^m = \frac{1}{1-q} = \frac{1}{p}$ (a geometric *series* — the namesake). Now the signature property. Suppose you have already failed $m$ times and ask how much *longer* you must wait:

$$P(X > m+n \given X > m) = \frac{P(X > m+n)}{P(X > m)} = \frac{q^{m+n}}{q^{m}} = q^{n} = P(X > n).$$

The past evaporates: a ghost that has skipped your first $m$ passes is, going forward, **exactly as fresh as a brand-new wait.** This is **memorylessness** — the geometric is the *only* discrete law with it.

**Beat 7 — Ramp the difficulty.**

- *Simplest:* $P(X > 5) = q^5$.
- *Twist — memoryless in action:* $P(X > 8 \given X > 3) = P(X > 5) = 0.4437$. The three wasted passes are forgotten.
- *Edge — exact landing:* $P(X = 3) = q^2 p = 0.85^2(0.15) = 0.1084$.

**Beat 8 — Picture it.** The pmf decays geometrically — each bar is $q$ times the one before.

<figure>
<img src="../../assets/diagrams/ch08_geometric_pmf.png" alt="A bar chart of the Geometric(0.15) probability mass function in the trials convention. The tallest bar is at k=1 (height 0.15), and each subsequent bar is 0.85 times the previous one, decaying smoothly: 0.15, 0.1275, 0.1084, and so on. A bracket over k=1 through 5 is labeled 'all fail = survival q^5'." style="width:78%; max-width:560px; display:block; margin:1em auto;">
<figcaption>$\Geom(0.15)$: each bar is $q = 0.85$ times the previous one. The shaded right tail past $k=5$ has total probability $q^5 = 0.4437$.</figcaption>
</figure>

**Beat 9 — Consolidate.** Whenever you **wait for the first success**, it is geometric: tail $q^m$, mean $1/p$ (trials) or $q/p$ (failures), and **memoryless** — past failures never change the future wait.

::: pokedex-entry
**POKÉDEX ENTRY №03 — The Geometric Distribution**

Independent Bernoulli($p$) trials run until the **first** success. Two conventions:

*Trials version* ($X$ = trial of first success, $X \in \{1,2,\dots\}$):
$$p(k) = q^{\,k-1}p, \quad P(X>m) = q^{m}, \quad \E[X] = \frac1p, \quad \Var(X) = \frac{q}{p^{2}}.$$
*Failures version* ($Y$ = failures before first success, $Y \in \{0,1,\dots\}$):
$$p(k) = q^{k}p, \quad \E[Y] = \frac{q}{p}, \quad \Var(Y) = \frac{q}{p^{2}}.$$

**Memoryless:** $P(X > m+n \given X > m) = P(X > n)$.

*In plain terms:* keep trying until you finally win; count how long it took. Already-failed trials tell you nothing about the future — the count *forgets*.

*Recognition cue:* **"how many tries until the first…," "until it finally happens."** **State your convention** ($\Var$ is the same either way; only the mean shifts by $1$).
:::

## Concept 4 — The Negative Binomial: Waiting for the $r$-th Success

::: concept-gate
**DO YOU ALREADY OWN THIS? — Negative Binomial**

You win each round w.p. $0.4$ and stop at your $3$rd win. Let $X$ = losses before the $3$rd win. Find $\E[X]$ and $P(X=2)$.

If you wrote **$\E[X]=3(0.6)/0.4 = 4.5$** and **$P(X=2)=\binom{4}{2}(0.4)^3(0.6)^2 = 0.1382$** (and can say why it's $\binom{4}{2}$, not $\binom{5}{2}$), **skip to Concept 5**. Otherwise read on — the locked last trial is the whole subtlety.
:::

**Beat 1 — The one-sentence idea (advance organizer).** *The negative binomial is the geometric run $r$ times: wait not for one success but for the $r$-th.*

**Beat 2 — Concrete instance.** To unlock Erika's inner garden you must win $r = 3$ petal-tokens; each round wins w.p. $p = 0.4$. Let $X$ = losing rounds before your $3$rd win. *What is $P(X = 2)$* — i.e. exactly $2$ losses, so the $3$rd win lands on round $5$?

**Beat 3 — Reason through the concrete case in words.** Round $5$ **must** be a win — it's the *clinching* third one, by definition of "stop at the $3$rd win." So the first $4$ rounds contain exactly $2$ wins and $2$ losses *in any order*, and round $5$ is the locked win. The probability of any one such pattern (3 wins, 2 losses) is $(0.4)^3(0.6)^2$; we then count how many patterns put the $3$rd win exactly on round $5$. There are $\binom{4}{2} = 6$ ways to place the $2$ early losses among the first $4$ rounds, so

$$P(X = 2) = \underbrace{\binom{4}{2}}_{\text{arrange first 4}}\,\underbrace{(0.4)^3}_{\text{3 wins}}\,\underbrace{(0.6)^2}_{\text{2 losses}} = 6(0.064)(0.36) = 0.1382.$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is writing $\binom{5}{2}$, as if all five rounds were free to permute:

$$P(X=2) \overset{?}{=} \binom{5}{2}(0.4)^3(0.6)^2. \qquad\textbf{(wrong — frees the clinching trial)}$$

That would count arrangements like LLWWW, where the third win lands on round $3$ and rounds $4$–$5$ are surplus — but then you'd have *stopped already* at round $3$. **The defining $r$-th success is nailed to the last slot;** only the *earlier* trials are arrangeable. Free that last trial and you over-count by exactly the patterns that finish too soon.

**Beat 5 — Translate into notation, one glyph at a time.** Now turn the concrete count into the general coefficient. With $X = k$ failures before the $r$-th success, the clinching success sits on the **last** trial, so the total number of trials is $k + r$. The last one is fixed as a success; the **earlier $k + r - 1$ trials** must contain exactly the $k$ failures (the other $r-1$ being the early successes). The number of ways to place those $k$ failures among the $k+r-1$ early slots is

$$\binom{k+r-1}{k} \qquad \text{read aloud: ``}(k+r-1)\text{ choose }k\text{'' — arrange }k\text{ failures among the trials before the last.''}$$

Check it against the concrete case: $k = 2$ failures, $r = 3$ successes gives $\binom{2+3-1}{2} = \binom{4}{2} = 6$ ✓ — the same $\binom{4}{2}$ we counted by hand, now read off the general rule. The full pmf assembles as **arrangements × successes × failures**, exactly as the binomial did:

$$X \sim \NegBin(r, p), \qquad p(k) = \binom{k+r-1}{k}\,p^{r}\,q^{k}, \quad k = 0,1,2,\dots$$

Read aloud: *"choose which of the early trials are the $k$ failures ($\binom{k+r-1}{k}$), pay a factor $p$ for each of the $r$ successes ($p^r$), and a factor $q$ for each of the $k$ failures ($q^k$)."*

**Beat 6 — Generalize: derive the mean and variance.** Here is *why* you may simply scale the geometric. To collect $r$ successes you can run the trials in $r$ stages: wait for the $1$st success (a geometric wait), then **restart fresh** and wait for the next, and so on $r$ times. The memorylessness of Concept 3 guarantees each restart is a brand-new geometric, independent of the ones before. So if $Y_1, \dots, Y_r$ are the failure-counts in the $r$ stages — each $Y_i \sim \Geom(p)$ failures-version with $\E[Y_i] = q/p$ and $\Var(Y_i) = q/p^2$ — then $X = Y_1 + \cdots + Y_r$. Expectation is **linear** and, because the stages are **independent**, variances **add** (the same two moves we used for the binomial at Beat 6 of Concept 2):

$$\E[X] = \sum_{i=1}^{r}\E[Y_i] = r\cdot\frac{q}{p} = \frac{rq}{p}, \qquad \Var(X) = \sum_{i=1}^{r}\Var(Y_i) = r\cdot\frac{q}{p^{2}} = \frac{rq}{p^{2}}.$$

For our numbers $\E[X] = 3(0.6)/0.4 = 4.5$. ✓ ($r = 1$ recovers the geometric, failures version — one stage.)

**Beat 7 — Ramp the difficulty.**

- *Simplest:* exactly $2$ losses before the $3$rd win, $P(X=2) = \binom{4}{2}p^3 q^2 = 0.1382$, above.
- *Twist — switch to the trials convention:* if instead $T$ counts the **total trials** to the $r$-th success, then $T = X + r$ and $p(t) = \binom{t-1}{r-1}p^r q^{t-r}$ — the clinching win is on trial $t$, and the $r-1$ earlier wins sit among the first $t-1$ trials. (This is the form Problem C8.25 uses.)
- *Edge:* $r = 1$ collapses every formula to the geometric — $\binom{k}{k}=1$, $p(k)=pq^k$, $\E[X]=q/p$. The negative binomial is *literally* the geometric stacked $r$ deep.

**Beat 8 — Picture it.** Unlike the geometric's pure decay (tallest at $k=0$), the negative-binomial pmf **rises off $k=0$** — you almost never collect $r$ successes with *zero* losses — peaks, then decays with a geometric-like tail.

<figure>
<img src="../../assets/diagrams/ch08_negbin_pmf.png" alt="A bar chart of the Negative Binomial(r=3, p=0.4) probability mass function in the failures convention. Bars rise from k=0 (height about 0.064), climb to a broad peak near k=2 and k=3 (each about 0.138), then decay with a long right tail. A dashed vertical line marks the mean rq/p=4.5, and the k=2 bar is highlighted to match the worked value 0.1382." style="width:78%; max-width:560px; display:block; margin:1em auto;">
<figcaption>$\NegBin(3,0.4)$ (failures convention): the count of losses before the $3$rd win rises off $k=0$, peaks, then decays. The highlighted $k=2$ bar is $\binom{4}{2}(0.4)^3(0.6)^2 = 0.1382$; the dashed line marks the mean $rq/p = 4.5$.</figcaption>
</figure>

**Beat 9 — Consolidate.** Whenever you **wait for the $r$-th success**, it is negative binomial: pmf $\binom{k+r-1}{k}p^r q^k$ (failures) with the $r$-th success locked in the last trial, mean $rq/p$ and variance $rq/p^2$ — exactly $r$ independent geometrics summed.

::: pokedex-entry
**POKÉDEX ENTRY №04 — The Negative Binomial Distribution**

Run Bernoulli($p$) trials until the **$r$-th** success. With $X$ = failures before the $r$-th success, $X \in \{0,1,2,\dots\}$:
$$p(k) = \binom{k+r-1}{k} p^{r} q^{k}, \qquad \E[X] = \frac{rq}{p}, \qquad \Var(X) = \frac{rq}{p^{2}}.$$

*In plain terms:* the geometric, $r$ times over — sum of $r$ independent geometrics. The $r$-th success is **locked in the last trial**; only the earlier ones permute.

*Recognition cue:* **"until the $r$-th success," "how many attempts to collect $r$ of them."** ($r=1$ is the geometric, failures version.)
:::

## Concept 5 — The Hypergeometric: Drawing Without Replacement

::: concept-gate
**DO YOU ALREADY OWN THIS? — Hypergeometric**

From a bed of $12$ Pokémon, $4$ of a rare line, you draw $3$ **without replacement**. Find $P(\text{at least }2\text{ rare})$.

If you wrote **$\dfrac{\binom{4}{2}\binom{8}{1}+\binom{4}{3}\binom{8}{0}}{\binom{12}{3}} = \dfrac{52}{220}=0.2364$** (and know why this is *not* a binomial), **skip to Concept 6**. If you used $\binom{3}{2}(1/3)^2(2/3)+\dots$, read on — that silently refills the bed.
:::

**Beat 1 — The one-sentence idea.** *Draw a fixed number of items from a finite pool **without putting any back**, and count the successes — that count is hypergeometric.*

**Beat 2 — Concrete instance.** Erika's garden bed holds $N = 12$ Grass Pokémon: $K = 4$ are the prized Gloom line, $8$ are common Oddish-line fillers. For the battle she draws $n = 3$ at random **without replacement**. Let $X$ = Gloom-line drawn. *What is $P(X \ge 2)$?*

<figure style="margin:1.25em auto; max-width:380px; text-align:center;">
<div style="display:flex; gap:18px; flex-wrap:wrap; justify-content:center; align-items:flex-end;">
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/43.png" alt="Oddish" style="width:100px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">#043 Oddish — filler</figcaption>
</figure>
<figure style="margin:0; text-align:center;">
<img src="../../assets/sprites/front/44.png" alt="Gloom" style="width:100px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.8em;">#044 Gloom — the rare line</figcaption>
</figure>
</div>
<figcaption style="font-size:0.85em; color:#666; font-style:italic;">$4$ Gloom-line among $12$. Drawing without replacement is hypergeometric, not binomial.</figcaption>
</figure>

**Beat 3 — Reason in words.** Counting equally likely draws (Ch 4), there are $\binom{12}{3} = 220$ ways to pick $3$ of the $12$. To get *exactly* $2$ Gloom: choose $2$ of the $4$ Gloom **and** $1$ of the $8$ fillers, $\binom{4}{2}\binom{8}{1} = 6\cdot 8 = 48$ ways. For *exactly* $3$ Gloom: $\binom{4}{3}\binom{8}{0} = 4$ ways. So

$$P(X \ge 2) = \frac{48 + 4}{220} = \frac{52}{220} = 0.2364.$$

**Beat 4 — Surface and dismantle the tempting wrong idea (this chapter's headline trap).** It is tempting to call each draw a success w.p. $4/12 = 1/3$ and use a **binomial**:

$$P(X\ge2) \overset{?}{=} \binom{3}{2}\Big(\tfrac13\Big)^2\Big(\tfrac23\Big) + \Big(\tfrac13\Big)^3 = \tfrac{7}{27} = 0.2593. \qquad\textbf{(wrong)}$$

That *overstates* the true $0.2364$. Why? A binomial assumes the draws are **independent** — that the pool refills between draws. But without replacement, **every Gloom you pull makes the next Gloom rarer**: after one Gloom, only $3$ of the remaining $11$ are Gloom, not $4$ of $12$. The depletion makes clusters of successes *less* likely than the binomial predicts. **Without replacement ⇒ dependent draws ⇒ hypergeometric, not binomial.**

**Beat 5 — Notation, one glyph at a time.**

$$X \sim \HyperGeom(N, K, n), \qquad p(k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}.$$

Read aloud: *"out of all $\binom{N}{n}$ ways to draw $n$ from $N$, count the ways to take $k$ from the $K$ successes and the other $n-k$ from the $N-K$ failures."* It is pure equally-likely counting.

**Beat 6 — Mean and variance, and the correction.** Marginally, each single draw *is* a success with probability $K/N$ (it is equally likely to be any of the $N$ items), so by linearity of expectation — *which never cares about dependence* —

$$\E[X] = n\frac{K}{N}.$$

The variance, however, *does* feel the dependence. It is the binomial variance with $p = K/N$, **shrunk** by a factor:

$$\Var(X) = n\,\frac{K}{N}\,\frac{N-K}{N}\cdot\underbrace{\frac{N-n}{N-1}}_{\text{finite-population correction}}.$$

The correction $\frac{N-n}{N-1} \le 1$ is *why* the bed depleting makes the count less variable than a binomial. (When $N \to \infty$ with $K/N \to p$ fixed, the correction $\to 1$ and the hypergeometric *becomes* the binomial — drawing from an enormous pool is effectively with replacement.)

**Beat 7 — Ramp.**

- *Simplest:* $P(X \ge 2) = 0.2364$, above.
- *Twist — at least one, by complement:* from a deck of $20$ with $8$ Energy cards, a hand of $5$: $P(\ge 1\text{ Energy}) = 1 - \binom{12}{5}/\binom{20}{5} = 1 - 0.0511 = 0.9489$ (Problem C8.15).
- *Edge:* if $N$ dwarfs $n$, just use the binomial — the correction is $\approx 1$.

**Beat 8 — Picture it.** The pmf is a *ratio of counts*, so the right picture is the **structure of the count itself**: the pool splits into rare and filler, and your draw must take $k$ from one block and $n-k$ from the other. Read the formula straight off the diagram.

<figure>
<img src="../../assets/diagrams/ch08_hypergeom_split.png" alt="A structural diagram of the hypergeometric count. At the top, a pool of N=12 tokens is split into K=4 red hatched 'rare' tokens and 8 green 'filler' tokens. Below, a box labeled 'Draw n=3 without replacement, want k=2 rare' shows 2 rare tokens (labeled C(4,2)=6 ways) times 1 filler token (labeled C(8,1)=8 ways). At the bottom, the assembled probability P(X=2) = C(4,2)C(8,1)/C(12,3) = 48/220." style="width:80%; max-width:580px; display:block; margin:1em auto;">
<figcaption>The hypergeometric pmf is bookkeeping: choose $k$ of the $K$ rare <em>and</em> $n-k$ of the $N-K$ filler, over all $\binom{N}{n}$ equally likely draws. Here $\binom{4}{2}\binom{8}{1}\big/\binom{12}{3} = 48/220$ for exactly $2$ rare.</figcaption>
</figure>

**Beat 9 — Consolidate.** Whenever you **draw without replacement from a finite pool**, it is hypergeometric: count the ways with $\binom{K}{k}\binom{N-K}{n-k}/\binom{N}{n}$, mean $nK/N$, variance $npq$ shrunk by $\frac{N-n}{N-1}$.

::: pokedex-entry
**POKÉDEX ENTRY №05 — The Hypergeometric Distribution**

From $N$ items, $K$ of them successes, draw $n$ **without replacement**. $X$ = successes drawn:
$$p(k) = \frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}, \qquad \E[X] = n\frac{K}{N},$$
$$\Var(X) = n\,\frac{K}{N}\,\frac{N-K}{N}\cdot\frac{N-n}{N-1}.$$

*In plain terms:* the binomial's **without-replacement** cousin. Each draw depletes the pool, so trials are *dependent*; the correction $\frac{N-n}{N-1}$ shrinks the variance. Same mean as a binomial with $p=K/N$.

*Recognition cue:* **"without replacement," "draw $n$ from a fixed pool of $N$," "a bed/deck/garden containing exactly $K$."** If $N$ is far larger than $n$, the binomial approximates it.
:::

## Concept 6 — The Poisson: Counts Over a Window (the Crown of the Chapter)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Poisson**

Gastly appear at an average of $3$ per minute. Find $P(\ge 2\text{ in one minute})$ and $P(<10\text{ over five minutes})$.

If you wrote **$1 - 4e^{-3} = 0.8009$** and **$P(Y\le 9)$ with $\lambda = 15$ (=$0.0699$)** — rescaling $\lambda$ to the five-minute window — **skip to Concept 7**. If you used $\lambda = 3$ for the five-minute count, read on: rescaling is the single most-punished Poisson error.
:::

**Beat 1 — The one-sentence idea.** *The Poisson counts random events over a window of time or space when they arrive at a steady average rate with no upper limit.*

**Beat 2 — Anchor + concrete instance.** Unlike every family so far, the Poisson has **no fixed number of trials** — a count of Gastly per minute could be $0$, or $3$, or $20$; there is no natural ceiling. The caretaker's log gives a stable rate $\lambda = 3$ per minute. Let $X$ = Gastly in one minute. *What is $P(X \ge 2)$, and over five minutes, $P(\text{fewer than }10)$?*

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/front/92.png" alt="Gastly" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#092 Gastly</strong> — appearances per minute: a Poisson count.</figcaption>
</figure>

**Beat 3 — Reason in words, and where the formula comes from.** Picture the minute sliced into a *huge* number $n$ of tiny instants, each with a *tiny* chance $p$ of a Gastly winking in, so that $np = \lambda = 3$. The total count is then $\Binom(n, p)$. But as we slice finer ($n \to \infty$, $p \to 0$, product fixed at $\lambda$), the binomial pmf converges to

$$p(k) = \frac{e^{-\lambda}\lambda^{k}}{k!}.$$

So the Poisson is the **binomial in the limit of many rare trials** — that is its birth, and the source of the famous approximation. For the *signature* property, the mean and variance both inherit $\lambda$: from $\Binom(n,p)$, mean $np \to \lambda$ and variance $np(1-p)\to\lambda$ (since $p\to0$). **Mean equals variance — the Poisson's fingerprint.**

**Beat 4 — Surface and dismantle the tempting wrong idea (rescaling).** For *five* minutes the deadliest slip is to reuse $\lambda = 3$:

$$P(Y < 10) \overset{?}{=} \sum_{k=0}^{9}\frac{e^{-3}3^k}{k!}. \qquad\textbf{(wrong — that's the ONE-minute rate)}$$

The rate is **per minute**; over five minutes you expect $5 \times 3 = 15$ Gastly, so $\lambda$ for the window is $15$, not $3$. **Always scale $\lambda = \text{rate} \times \text{window}$.** A "lull" of fewer than $10$ in a window that averages $15$ should be *uncommon*, and indeed it is — about $7\%$. Using $\lambda=3$ would wrongly call it nearly certain.

**Beat 5 — Notation, one glyph at a time.**

$$X \sim \Poisson(\lambda), \qquad p(k) = \frac{e^{-\lambda}\lambda^{k}}{k!}, \quad k = 0,1,2,\dots$$

Read aloud: *"$e$-to-the-minus-lambda, times lambda-to-the-$k$, over $k$-factorial."* The $k!$ in the denominator is what makes the masses sum to $1$ (it is the Taylor series of $e^{\lambda}$ in disguise).

**Beat 6 — Compute both targets.** One minute, $\lambda = 3$, complement the small end:

$$P(X \ge 2) = 1 - p(0) - p(1) = 1 - e^{-3} - 3e^{-3} = 1 - 4e^{-3} = 1 - 4(0.04979) = 0.8009.$$

Five minutes, $\lambda = 15$:

$$P(Y < 10) = P(Y \le 9) = \sum_{k=0}^{9}\frac{e^{-15}15^{k}}{k!} = 0.0699.$$

**Beat 7 — Ramp the difficulty — the two power-tools.**

- *Additivity:* independent Poissons **add**. If Gastly arrive at $\lambda_G = 3$/min and Haunter at $\lambda_H = 1$/min independently, the *total* ghosts in a minute is $\Poisson(4)$ — over $2$ minutes, $\Poisson(8)$ (Problem C8.13). Just sum the rates.
- *Approximation:* $\Binom(n,p) \approx \Poisson(np)$ when $n$ is large and $p$ small. A slot pulled $40$ times at $p = 0.05$ is $\approx \Poisson(2)$ (Problem C8.7).
- *Thinning (capstone):* if a $\Poisson(\mu)$ stream is each independently kept w.p. $p$, the kept count is $\Poisson(\mu p)$ — proved in the Gym Battle.

**Beat 8 — Picture it.** The pmf peaks near $\lambda$ and, unlike the binomial, has **no right edge**.

<figure>
<img src="../../assets/diagrams/ch08_poisson_pmf.png" alt="Two side-by-side bar charts of Poisson probability mass functions. Left: lambda=3, peaking near k=3 with a long thin right tail. Right: lambda=15, a broader bell-like hump centered near 15, with the bars for k=0 through 9 shaded to show P(Y<10) is a small left-tail area totaling about 0.07. Both charts have no upper bound on k." style="width:82%; max-width:600px; display:block; margin:1em auto;">
<figcaption>Poisson counts have no upper limit. Left: $\lambda=3$ (one minute). Right: $\lambda=15$ (five minutes); the shaded left tail $k\le 9$ totals $0.0699$ — a genuine lull.</figcaption>
</figure>

**Beat 9 — Consolidate.** Whenever events arrive at a **steady rate over a window with no cap**, it is Poisson: pmf $e^{-\lambda}\lambda^k/k!$, mean $=$ variance $=\lambda$, **rescale $\lambda$ to the window**, and lean on additivity, the binomial limit, and thinning.

::: pokedex-entry
**POKÉDEX ENTRY №06 — The Poisson Distribution**

$X \sim \Poisson(\lambda)$ counts events at a constant average rate over a fixed window, $X \in \{0,1,2,\dots\}$:
$$p(k) = \frac{e^{-\lambda}\lambda^{k}}{k!}, \qquad \E[X] = \Var(X) = \lambda, \qquad M_X(t) = e^{\lambda(e^{t}-1)}.$$

**Additivity:** independent $\Poisson(\lambda_1)+\Poisson(\lambda_2) = \Poisson(\lambda_1+\lambda_2)$.
**Approximation:** $\Binom(n,p)\approx\Poisson(np)$ for large $n$, small $p$.
**Thinning:** keep each of a $\Poisson(\mu)$ stream w.p. $p$ $\Rightarrow$ kept count is $\Poisson(\mu p)$.

*In plain terms:* random events in a chunk of time/space with no ceiling. **Mean equals variance** — its signature. **Scale $\lambda = $ rate $\times$ window.**

*Recognition cue:* **"per minute / per year / per square mile," "average rate $\lambda$," a count with no natural maximum.**
:::

## Concept 7 — The Discrete Uniform: Every Value Equally Likely

::: concept-gate
**DO YOU ALREADY OWN THIS? — Discrete Uniform**

A fair $18$-slot roulette: $X$ = the slot. Find $\E[X]$ and $\Var(X)$.

If you wrote **$\E[X]=\frac{19}{2}=9.5$** and **$\Var(X)=\frac{18^2-1}{12}=26.92$**, **skip to the Worked Examples**. Otherwise the card below is one line.
:::

**Beat 1 — The one-sentence idea.** *When every value $1,\dots,m$ is equally likely, $X$ is discrete uniform.*

**Beat 2–3 — Concrete instance + reason.** The Game Corner roulette has $m = 18$ equally likely slots; $X$ = the landing slot. Each value has mass $1/m$. The mean is the midpoint $\frac{m+1}{2} = 9.5$; the variance — derivable from $\sum k^2$ but worth memorizing — is $\frac{m^2-1}{12} = \frac{323}{12} = 26.92$.

::: pokedex-entry
**POKÉDEX ENTRY №07 — The Discrete Uniform Distribution**

$X$ uniform on $\{1,2,\dots,m\}$:
$$p(k) = \frac1m, \qquad \E[X] = \frac{m+1}{2}, \qquad \Var(X) = \frac{m^2-1}{12}.$$

*In plain terms:* a fair $m$-faced die — every outcome equally likely. Mean is the midpoint; variance grows with the range.

*Recognition cue:* **"equally likely," "a fair spinner / die / one labelled ticket."**
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/erika.png" alt="Erika, Celadon Gym Leader" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Erika — Celadon Gym Leader (Grass), your guide to the named patterns</figcaption>
</figure>

Five examples, fading from fully narrated to exam-speed. The first leads with the **recognition** step done out loud, because *naming the family* is where this chapter's marks are won.

### Worked Example 8.1 — The Game Corner Slots (full narration; recognition-first)

**ARCHETYPE:** *Binomial — fixed trials, count successes; tail by complement.*

**Setup.** Misty pulls the slot exactly $n = 10$ times; each pull wins independently w.p. $p = 0.2$. Find $\E[X]$ and $P(X \ge 3)$.

**Step 1 — Recognize the family (the load-bearing step).** Read the story: the number of trials is **decided in advance** ($10$ pulls), trials are independent, and we **count successes**. *Fixed $n$, count successes ⇒ binomial.* So $X \sim \Binom(10, 0.2)$.

**Step 2 — Mean (read it off the card).** $\E[X] = np = 10(0.2) = 2$.

**Step 3 — Tail by complement.** "At least $3$" is fastest from the small end:
$$P(X \ge 3) = 1 - [p(0) + p(1) + p(2)].$$
$$p(0) = 0.8^{10} = 0.10737, \quad p(1) = 10(0.2)(0.8^9) = 0.26844, \quad p(2) = \binom{10}{2}(0.2)^2(0.8^8) = 0.30199.$$
$$P(X \ge 3) = 1 - 0.67780 = 0.3222.$$

**Step 4 — Check & pitfall.** $\Var(X) = npq = 1.6 < 2 = \E[X]$, consistent with a binomial (variance below mean) ✓. **Pitfall:** computing $1 - P(X \le 3)$ — but "$\ge 3$" *includes* $3$, so complement *strictly below*: $1 - P(X \le 2)$. *(Back-ref: Entry №02.)*

### Worked Example 8.2 — Waiting for the Marowak's Ghost (partial guidance)

**ARCHETYPE:** *Geometric — wait for the first success (trials convention); survival + memorylessness.*

**Setup.** Each pass through the top chamber, the ghost manifests w.p. $p = 0.15$. Find $\E[X]$ (the pass it first appears) and $P(X > 5)$.

**Identify.** *Waiting for the first success ⇒ geometric*, trials version: $X \sim \Geom(0.15)$. *Your move: read the mean and the survival off the card.*

$$\E[X] = \frac1p = \frac{1}{0.15} = 6.667 \text{ passes}, \qquad P(X > 5) = q^5 = 0.85^5 = 0.4437.$$

**Check & pitfall.** Memoryless check: $P(X > 8 \given X > 3) = P(X > 5) = 0.4437$ — three failed passes are forgotten ✓. **Pitfall:** mixing conventions. If instead $Y$ = *failures before* success, $\E[Y] = q/p = 5.667$ — exactly one less. State the convention first. *(Back-ref: Entry №03.)*

### Worked Example 8.3 — Erika's Garden Bed (without replacement; light guidance)

**ARCHETYPE:** *Hypergeometric — draw without replacement; contrast with the wrong binomial.*

**Setup.** Bed of $N = 12$: $K = 4$ Gloom-line, $8$ fillers. Draw $n = 3$ without replacement. Find $P(X \ge 2)$.

$$P(X \ge 2) = \frac{\binom{4}{2}\binom{8}{1} + \binom{4}{3}\binom{8}{0}}{\binom{12}{3}} = \frac{48 + 4}{220} = 0.2364.$$

**Why not binomial.** A binomial ($p = 1/3$) would give $\binom{3}{2}(1/3)^2(2/3) + (1/3)^3 = 7/27 = 0.2593$ — *too high*, because it ignores depletion. The same effect shrinks the variance: $\Var_{\text{hyper}} = 3\cdot\frac13\cdot\frac23\cdot\frac{9}{11} = 0.5455 < 0.6667 = npq$ via the correction $\frac{N-n}{N-1} = \frac{9}{11}$.

**Check & pitfall.** $0 \le 0.2364 \le 1$ and it sits *below* the binomial, as depletion predicts ✓. **Pitfall (this chapter's Team Rocket error):** using the binomial without replacement. *(Back-ref: Entry №05.)*

### Worked Example 8.4 — The Gastly Lull (Poisson, two windows; light guidance)

**ARCHETYPE:** *Poisson — rate over a window; rescale $\lambda$, then additivity.*

**Setup.** Gastly appear at $3$/min. Find $P(X \ge 2)$ in one minute and $P(Y < 10)$ over five minutes.

**One minute** ($\lambda = 3$):
$$P(X \ge 2) = 1 - e^{-3} - 3e^{-3} = 1 - 4e^{-3} = 0.8009.$$
**Five minutes** — *rescale* $\lambda = 5 \times 3 = 15$ (additivity of five independent one-minute counts):
$$P(Y < 10) = P(Y \le 9) = \sum_{k=0}^{9}\frac{e^{-15}15^k}{k!} = 0.0699.$$

**Check & pitfall.** Mean $=$ variance $= 15$, so fewer than $10$ in a window averaging $15$ is genuinely uncommon ($\approx 7\%$) ✓. **Pitfall:** forgetting to rescale $\lambda$ to $15$ — the single most common Poisson error. *(Back-ref: Entry №06.)*

### Worked Example 8.5 — Collecting Erika's Three Petals (negative binomial; exam speed)

**ARCHETYPE:** *Negative binomial — wait for the $r$-th success; the last trial is locked.*

**Setup.** Win $r = 3$ tokens; each round wins w.p. $p = 0.4$. Find $\E[X]$ (losses before the $3$rd win) and $P(X = 2)$ (third win on round $5$).

$$\E[X] = \frac{rq}{p} = \frac{3(0.6)}{0.4} = 4.5, \qquad P(X = 2) = \binom{4}{2}(0.4)^3(0.6)^2 = 6(0.064)(0.36) = 0.13824.$$

**Check & pitfall.** $\binom{4}{2}$ arranges the $2$ losses among the **first $4$** rounds; round $5$ is the locked clinching win ✓. **Pitfall:** writing $\binom{5}{2}$, as if all five rounds permuted. *(Back-ref: Entry №04.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — The family decision tree (run it before touching the calculator)**

**(1) With or without replacement?** Without → **hypergeometric**. **(2) If with replacement / independent: fixed number of trials, or are you waiting?** Fixed $n$ → **binomial**. Waiting for the $1$st success → **geometric**; for the $r$-th → **negative binomial**. **(3) No trials at all, just a rate over time/space?** → **Poisson**. **(4) All values equally likely?** → **discrete uniform**. Naming the family is 80% of the problem and costs ten seconds.
:::

::: trainers-tip
**TRAINER'S TIP — Mean vs. variance as a fingerprint**

If a problem hands you a mean and a variance and asks *which distribution*: **equal ⇒ Poisson** ($\Var=\lambda=\E$); **variance smaller ⇒ binomial** ($npq<np$); **variance larger ⇒ geometric-family** (over-dispersed). One comparison routes you to the family.
:::

::: trainers-tip
**TRAINER'S TIP — Poisson cdf by recursion on the TI-30XS**

There is no built-in Poisson cdf. For $P(Y\le 9)$ with $\lambda = 15$, compute $e^{-15}$ once, **STO→** it, then build terms recursively: $p(k) = p(k-1)\cdot \lambda/k$. Each new term is the previous times $\lambda/k$ — no factorials, no re-exponentiating, no rounding drift. This is the fastest reliable way to add a string of Poisson (or binomial) masses under the clock.
:::

::: trainers-tip
**TRAINER'S TIP — "At least one" and "more than $m$"**

For binomial/hypergeometric, $P(\ge 1) = 1 - P(0)$ — one term to compute instead of many. For the geometric, *"more than $m$ trials"* is just the survival $q^m$ — no summation at all. Reach for the complement before you sum a tail.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

Jessie and James are skimming Pokémon from Erika's bed of $12$ (four of them the rare Gloom line). "We snatch $3$ without putting any back," James schemes, "so the chance of grabbing at least $2$ Glooms is just a binomial — each grab's a one-in-three, so $\binom{3}{2}(1/3)^2(2/3) + (1/3)^3 = 7/27 \approx 0.259$. Easy money!"

Meowth nods along. They commit to the heist on those odds — and come up short, **again**, because the true chance is only $0.236$.

**Where it fails:** every Gloom they grab makes the *next* one rarer (after one Gloom, only $3$ of $11$ remain), so the draws are **dependent** — but a binomial pretends the bed refills between grabs. **The fix:** when you draw **without replacement** from a finite pool, use the **hypergeometric** pmf, not the binomial; the binomial overstates clustering because it never depletes the pool. The finite-population correction $\frac{N-n}{N-1}$ is the *same* depletion effect showing up in the variance.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

The Poisson is the **single most important count model in property-and-casualty insurance**: it models **claim frequency** — the number of accidents per policyholder per year. An auto insurer assumes each driver's annual claim count is $\Poisson(\lambda)$ with a rate $\lambda$ that depends on age, territory, and vehicle, then prices the policy from $\E[\text{claims}] = \lambda$ times the expected cost per claim. The **binomial-to-Poisson limit** is *why* this works: each of the millions of tiny moments a driver could crash is a near-zero-probability Bernoulli trial, and their sum is Poisson.

**Poisson additivity** is what lets an insurer pool a whole **portfolio**: the total claim count of $1{,}000$ independent drivers, each $\Poisson(\lambda_i)$, is itself $\Poisson(\sum_i \lambda_i)$ — one clean distribution for the entire book. And the **geometric / negative binomial** model "time to event" — claims until a policy lapses, trials until a system fails.

*Series bridge:* this frequency–severity split (a Poisson **count** of claims, each with a random **size**) is the spine of **CAS Exam 5 ratemaking** and of the **collective risk model** (the compound Poisson) you'll meet later.

*Transfer check:* could you solve this with **no Pokémon in it**? "Calls to a call center arrive at $4$ per hour; find the probability that fewer than $10$ arrive in a $5$-hour shift." Same Poisson, same rescaling ($\lambda = 20$), same method. If you can do that, the skill has transferred.
:::

## The Gym Battle — Rainbow Badge Capstone

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/sprites/front/45.png" alt="Vileplume" style="width:130px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>Erika's ace: #045 Vileplume</strong></figcaption>
</figure>

**Erika's Challenge.** "A true trainer reads the *whole* battlefield," Erika says, fanning herself. "My Vileplume releases spores. Over our battle it puffs spore-clouds at an average rate of $\lambda = 2$ per minute, and the battle lasts exactly $4$ minutes. Each spore-cloud *independently* poisons one of your Pokémon w.p. $0.25$. Tell me two things, and the Rainbow Badge is yours: **(a)** the probability your team weathers it with *at most one* poisoning, and **(b)** the variance of the number of poisonings."

**ARCHETYPE:** *Poisson thinning — a Poisson count of events, each independently kept, is itself Poisson.*

**Step 1 — Recognize and rescale.** Spore-clouds over $4$ minutes: number $N \sim \Poisson(\lambda\cdot 4) = \Poisson(8)$. Each cloud poisons independently w.p. $p = 0.25$. Let $X$ = poisonings.

**Step 2 — Trainer's Path (thinning shortcut).** Filtering a $\Poisson(\mu)$ stream by keeping each event w.p. $p$ yields $\Poisson(\mu p)$. So
$$X \sim \Poisson(8 \times 0.25) = \Poisson(2).$$
Then:
$$\text{(a)}\quad P(X \le 1) = p(0) + p(1) = e^{-2} + 2e^{-2} = 3e^{-2} = 0.4060.$$
$$\text{(b)}\quad \Var(X) = \lambda = 2 \quad(\text{mean} = \text{variance for a Poisson}).$$

**Step 3 — Professor's Path (prove the thinning is legitimate).** Condition on $N = n$. Given $n$ clouds, the poisonings are $X \given N=n \sim \Binom(n, 0.25)$, so
$$P(X = k) = \sum_{n=k}^{\infty}\underbrace{\binom{n}{k}(0.25)^k(0.75)^{n-k}}_{\text{binomial filter}}\cdot\underbrace{\frac{e^{-8}8^{n}}{n!}}_{\text{Poisson count}}.$$
Pull out constants and substitute $m = n-k$:
$$P(X=k) = \frac{(0.25\cdot 8)^k e^{-8}}{k!}\sum_{m=0}^{\infty}\frac{(0.75\cdot 8)^m}{m!} = \frac{2^k e^{-8}}{k!}\,e^{6} = \frac{e^{-2}2^k}{k!},$$
which is exactly $\Poisson(2)$. The shortcut is rigorous: **thinning a Poisson by $p$ scales its rate to $\mu p$.**

**Step 4 — Check & the pitfalls Erika is testing.** Mean $= \Var = 2$ confirms the Poisson identity ✓. Two traps: (i) forgetting to scale the rate to the $4$-minute window ($2/\text{min} \Rightarrow \mu = 8$); (ii) treating $X$ as $\Binom(8, 0.25)$ with a *fixed* $8$ — but $8$ is the *mean of a random count*, not a fixed number of trials, so the answer is $\Poisson(2)$, not a binomial.

> "That," Erika says, closing her fan, "is reading the whole field. The Rainbow Badge is yours."

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/rainbow_badge.png" alt="Rainbow Badge" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Rainbow Badge earned!</strong></figcaption>
</figure>

## The Gym Challenge — Problem Set

::: problem-set
**TEST-OUT INSTRUCTIONS.** Work this set timed (~6 min/problem), then check the **Answer Key** below. Hit the mastery bar (**80%+ with the right family named each time**) and you may move on. Problems are listed first; full worked solutions follow afterward (never interleaved). Markers: 🔴 Poké Ball = routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (mechanics)

**C8.1.** 🔴 On Route 7 you battle a trainer's $6$ Pokémon one at a time; each round you win independently w.p. $0.7$. Find the expected number of wins out of the $6$ rounds, and the probability you win all six.

**C8.2.** 🔴 A wild Bellsprout flees on each throw w.p. $0.4$, independently; you throw until it flees. Using the convention that $X$ counts the *throw on which it flees*, find $\E[X]$ and $P(X = 3)$.

**C8.3.** 🔴 The Game Corner roulette has $18$ numbered slots, each equally likely. Let $X$ be the landing slot. Treating $X$ as discrete uniform on $\{1,\dots,18\}$, find $\E[X]$ and $\Var(X)$.

**C8.4.** 🔴 Gastly drift through the Tower window at an average rate $\lambda = 1.5$ per minute (Poisson). For a single minute, find $P(\text{exactly }0)$ and $P(\text{exactly }2)$.

**C8.5.** 🟡 A grab-bag holds $10$ items: $3$ rare TMs and $7$ Potions. You pull $4$ at once (without replacement). Find the probability that exactly $2$ are TMs.

**C8.6.** 🟡 You need $r = 2$ Thunder Stones. Each shop independently has one in stock w.p. $0.3$. Let $X$ be the number of *out-of-stock shops* you visit before securing the second stone. Find $\E[X]$.

**C8.19.** 🔴 A single Poké Ball throw catches a Caterpie w.p. $p = 0.7$. Let $X = 1$ if caught, $0$ otherwise (a Bernoulli trial). Find $\E[X]$ and $\Var(X)$.

**C8.20.** 🔴 A wild Pidgey flees on the first turn w.p. $0.35$. Let $X$ be the Bernoulli indicator of fleeing. State $P(X=0)$ and $P(X=1)$, and report $\Var(X)$.

**C8.21.** 🟡 You make $3$ independent Quick Ball throws, each succeeding w.p. $p = 0.4$. Writing each as a Bernoulli indicator $X_i$, let $S = X_1+X_2+X_3$. Use linearity to find $\E[S]$ and $\Var(S)$.

**C8.25.** 🟡 Each Gym attempt succeeds independently w.p. $p = 0.5$. Let $X$ be the number of attempts needed to earn the $3$rd badge. Find $P(X = 5)$.

### Gym Battles (true SOA difficulty)

**C8.7.** 🟡 A slot pays out on each pull w.p. $p = 0.05$; Misty pulls $40$ times. Using the **Poisson approximation**, estimate $P(\text{at least two payouts})$, and state whether the approximation over- or under-estimates the true binomial tail.

**C8.8.** 🟡 Calls to the Pokémon Center arrive Poisson at $4$ per hour. Nurse Joy steps away for $15$ minutes. Find $P(\text{at least one call})$ and $P(\text{exactly three})$.

**C8.9.** 🟡 In a bed of $N = 15$ Pokémon, $K = 5$ are Grass/Poison dual types; Erika draws $n = 4$ without replacement. Let $X$ be the dual types drawn. Find $\E[X]$ and $\Var(X)$, and compare $\Var(X)$ to a binomial model.

**C8.10.** 🟡 You throw Poké Balls at a legendary bird; each throw catches w.p. $p = 0.1$. Let $X$ be the throw on which you catch it. Find $P(X > 10)$, then use memorylessness to find $P(X > 15 \given X > 5)$.

**C8.11.** 🔵 A binomial $X \sim \Binom(n,p)$ has $\E[X] = 6$ and $\Var(X) = 4.2$. Recover $n$ and $p$, then find $P(X = 0)$.

**C8.12.** 🟡 Defective Poké Balls occur at rate $2\%$. A shipment of $150$ arrives. Using the Poisson approximation, find $P(\text{no more than one defective})$.

**C8.13.** 🟡 Two independent Poisson streams converge on Lavender Town: Gastly at $\lambda_G = 3$/min and Haunter at $\lambda_H = 1$/min. Over a $2$-minute window, find the probability the **total** number of ghosts is exactly $5$.

**C8.14.** 🔵 A trainer challenges until her $4$th victory; each match is an independent win w.p. $0.6$. Let $X$ be the **total matches** played. Find $\E[X]$ and $P(X = 6)$.

**C8.15.** 🟡 From a deck of $20$ cards, $8$ are Energy. You are dealt $5$ without replacement. Find $P(\text{at least one Energy})$ using the complement.

**C8.22.** 🟡 On a route, each of $5$ independent encounters is Fire-type w.p. $0.2$. Let $X_i$ be the Bernoulli indicator that encounter $i$ is Fire-type and $N = \sum X_i$. Find $\E[N]$ and $P(N=0)$.

**C8.23.** 🟡 A gate opens ($X=1$) w.p. $p = 0.6$ and stays shut ($X=0$) otherwise. Write the Bernoulli MGF $M_X(t)$, use it to recover $\E[X]$ and $\E[X^2]$, and give $\Var(X)$.

**C8.26.** 🟡 Each throw catches independently w.p. $p = 0.25$. Let $Y$ be the number of *misses* before the $4$th catch (failures convention). Find $\E[Y]$ and $\Var(Y)$.

**C8.28.** 🟡 A fair die shows $X$ uniform on $\{1,\dots,6\}$. A prize pays $g(X)=X^2$ Poké-dollars. Find $\E[X^2]$ (the expected payout) and $P(X \ge 5)$.

### Elite Challenge (integrative / stretch)

**C8.16.** 🔵 *(Thinning.)* Vileplume spore-clouds arrive Poisson at $\lambda = 3$ per minute over a $5$-minute battle. Each independently lands on *your* side w.p. $0.4$. Let $X$ = clouds on your side. Identify the distribution of $X$, then find $P(X \ge 2)$ and $\Var(X)$.

**C8.17.** 🔵 *(Parameter from a probability + mode.)* Daily wild encounters on Route 8 are Poisson with mean $\lambda$, and $P(0\text{ encounters}) = 0.2$. Find $\lambda$, then $P(X \ge 2)$ and the most likely (modal) number of encounters.

**C8.18.** 🔵 *(With- vs. without-replacement.)* You draw single Pokémon *with replacement* from a pool that is $30\%$ Water-type, stopping at your $3$rd Water-type; let $N$ = total draws. Separately a rival draws $5$ *without replacement* from a pool of $10$ ($3$ Water). Find $\E[N]$ and $\E[\text{Water in the rival's 5}]$, and explain in one line why the without-replacement *mean* is unaffected by the correction even though the *variance* is.

**C8.24.** 🔵 *(Bernoulli with a hidden state.)* A capture succeeds w.p. $p$, where $p = 0.8$ in clear weather (chance $0.6$) and $p = 0.3$ in rain (chance $0.4$). Let $X$ be the Bernoulli success indicator. Find the unconditional $\E[X] = P(X=1)$ and $\Var(X)$.

**C8.27.** 🔵 *(Negative-binomial tail via the binomial.)* Each patrol independently yields a legendary sighting w.p. $p = 0.4$. Let $X$ be the number of patrols to reach the $2$nd sighting. Find $P(X > 6) = P(\text{at most }1\text{ sighting in the first }6\text{ patrols})$.
:::

## Answer Key

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

**C8.1** — *Binomial mean & all-successes (Entry №02).* $X \sim \Binom(6, 0.7)$. $\E[X] = np = 6(0.7) = 4.2$. $P(X = 6) = 0.7^6 = 0.1176$.

**C8.2** — *Geometric, trials convention (Entry №03).* $X \sim \Geom(0.4)$, trials. $\E[X] = 1/0.4 = 2.5$. $P(X = 3) = q^2 p = 0.6^2(0.4) = 0.144$.

**C8.3** — *Discrete uniform (Entry №07).* $m = 18$. $\E[X] = (m+1)/2 = 9.5$. $\Var(X) = (m^2-1)/12 = 323/12 = 26.9167$.

**C8.4** — *Poisson, single window (Entry №06).* $\lambda = 1.5$. $P(0) = e^{-1.5} = 0.2231$. $P(2) = e^{-1.5}(1.5)^2/2! = 0.2231(2.25)/2 = 0.2510$.

**C8.5** — *Hypergeometric (Entry №05).* $N=10, K=3, n=4$, $\binom{10}{4}=210$. $P(X=2) = \binom{3}{2}\binom{7}{2}/210 = (3)(21)/210 = 63/210 = 0.3000$.

**C8.6** — *Negative binomial, failures (Entry №04).* $r=2, p=0.3$, $X$ = failures before the $2$nd success. $\E[X] = rq/p = 2(0.7)/0.3 = 4.667$.

**C8.19** — *Bernoulli mean & variance (Entry №01).* $X \sim \mathrm{Bernoulli}(0.7)$: $\E[X] = p = 0.7$, $\Var(X) = p(1-p) = 0.7(0.3) = 0.21$.

**C8.20** — *Bernoulli pmf & variance (Entry №01).* $P(X=1) = 0.35$, $P(X=0) = 0.65$. $\Var(X) = p(1-p) = 0.35(0.65) = 0.2275$ (just below the maximum $0.25$ at $p=0.5$).

**C8.21** — *Sum of i.i.d. Bernoulli is binomial (Entries №01–02).* Each $X_i \sim \mathrm{Bernoulli}(0.4)$ with $\E=0.4$, $\Var=0.24$. By linearity/independence $\E[S] = 3(0.4) = 1.2$ and $\Var(S) = 3(0.24) = 0.72$. ($S \sim \Binom(3,0.4)$.)

**C8.25** — *Negative binomial pmf, trials form (Entry №04).* $P(X=k) = \binom{k-1}{r-1}p^r q^{k-r}$ with $r=3, p=0.5$. $P(X=5) = \binom{4}{2}(0.5)^3(0.5)^2 = 6(0.5)^5 = 6/32 = 0.1875$.

**C8.7** — *Binomial→Poisson approximation (Entry №06).* $\lambda = np = 40(0.05) = 2$. $P(X\ge2) = 1 - e^{-2} - 2e^{-2} = 1 - 3e^{-2} = 0.5940$. The Poisson **over**-estimates the true binomial tail here: the binomial variance $npq = 1.9 < 2$ makes it marginally more concentrated near the mean.

**C8.8** — *Poisson, rescale to window (Entry №06).* Rate $4$/hr over $0.25$ hr ⇒ $\lambda = 1$. $P(\ge 1) = 1 - e^{-1} = 0.6321$. $P(=3) = e^{-1}/3! = 0.3679/6 = 0.0613$.

**C8.9** — *Hypergeometric mean & variance with correction (Entry №05).* $N=15, K=5, n=4$. $\E[X] = nK/N = 20/15 = 1.3333$. $\Var(X) = 4\cdot\frac{5}{15}\cdot\frac{10}{15}\cdot\frac{11}{14} = 0.6984$. A binomial ($p=1/3$) gives $npq = 0.8889$, larger — the correction $11/14 = 0.7857$ shrinks it.

**C8.10** — *Geometric survival + memorylessness (Entry №03).* $X \sim \Geom(0.1)$, trials. $P(X > 10) = q^{10} = 0.9^{10} = 0.3487$. By memorylessness, $P(X > 15 \given X > 5) = P(X > 10) = 0.3487$.

**C8.11** — *Recover binomial parameters from moments (Entry №02).* $np = 6$, $npq = 4.2 \Rightarrow q = 4.2/6 = 0.7$, so $p = 0.3$ and $n = 6/0.3 = 20$. $P(X = 0) = q^{20} = 0.7^{20} = 0.000798$.

**C8.12** — *Binomial→Poisson approximation (Entry №06).* $\lambda = np = 150(0.02) = 3$. $P(X \le 1) = e^{-3} + 3e^{-3} = 4e^{-3} = 0.1991$.

**C8.13** — *Poisson additivity (Entry №06).* Over $2$ min: $\lambda_G = 6$, $\lambda_H = 2$; total $\sim \Poisson(8)$. $P(=5) = e^{-8}8^5/5! = 0.0916$.

**C8.14** — *Negative binomial, total-trials (Entry №04).* Let $Y$ = failures before the $4$th win, $X = Y + 4$. $\E[Y] = rq/p = 4(0.4)/0.6 = 2.667$, so $\E[X] = 6.667$. $P(X=6) \Leftrightarrow Y = 2$: $\binom{2+4-1}{2}p^4 q^2 = \binom{5}{2}(0.6)^4(0.4)^2 = 10(0.1296)(0.16) = 0.20736$.

**C8.15** — *Hypergeometric via complement (Entry №05).* $N=20, K=8, n=5$. $P(\ge 1) = 1 - \binom{12}{5}/\binom{20}{5} = 1 - 792/15504 = 1 - 0.05108 = 0.9489$.

**C8.22** — *Indicator-sum mean + all-zero probability (Entry №01).* Each $X_i \sim \mathrm{Bernoulli}(0.2)$; by linearity $\E[N] = 5(0.2) = 1$. By independence $P(N=0) = (0.8)^5 = 0.32768$.

**C8.23** — *Bernoulli MGF & moments (Entries №01, №04 method).* $M_X(t) = (1-p) + pe^t = 0.4 + 0.6e^t$. $M_X'(t) = 0.6e^t \Rightarrow \E[X] = 0.6$; $M_X''(t) = 0.6e^t \Rightarrow \E[X^2] = 0.6$ (since $X^2 = X$ for a $0/1$ variable). $\Var(X) = 0.6 - 0.6^2 = 0.24 = p(1-p)$.

**C8.26** — *Negative binomial mean & variance, failures (Entry №04).* $r=4, p=0.25, q=0.75$. $\E[Y] = rq/p = 4(0.75)/0.25 = 12$. $\Var(Y) = rq/p^2 = 4(0.75)/0.0625 = 48$.

**C8.28** — *Discrete uniform via LOTUS (Entry №07).* On $\{1,\dots,6\}$: $\E[X^2] = (1+4+9+16+25+36)/6 = 91/6 = 15.1667$. $P(X \ge 5) = P(X\in\{5,6\}) = 2/6 = 1/3 = 0.3333$.

**C8.16** — *Poisson thinning (Entry №06; capstone method).* Clouds over $5$ min: $\Poisson(15)$; thinned by $p = 0.4$ ⇒ $X \sim \Poisson(6)$. $P(X \ge 2) = 1 - e^{-6} - 6e^{-6} = 1 - 7e^{-6} = 0.9826$. $\Var(X) = 6$.

**C8.17** — *Poisson parameter from a probability + mode (Entry №06).* $P(0) = e^{-\lambda} = 0.2 \Rightarrow \lambda = -\ln 0.2 = 1.6094$. $P(X \ge 2) = 1 - e^{-\lambda} - \lambda e^{-\lambda} = 1 - 0.2 - 1.6094(0.2) = 0.4781$. Mode: $\lambda$ is non-integer, so the most likely value is $\lfloor \lambda \rfloor = 1$.

**C8.18** — *Integrative: negative binomial vs. hypergeometric (Entries №04, №05).* With replacement, wait for the $3$rd Water ($p = 0.3$): $\E[\text{failures}] = rq/p = 3(0.7)/0.3 = 7$, so $\E[N] = 7 + 3 = 10$. Rival, without replacement ($N=10, K=3, n=5$): $\E[\text{Water}] = nK/N = 15/10 = 1.5$. **One line:** the hypergeometric mean $nK/N$ equals the binomial mean $np$ with $p = K/N$ because expectation is **linear** — each individual draw is marginally a success w.p. $K/N$ regardless of replacement; only the **variance** picks up the finite-population correction, since dependence affects second moments, not first.

**C8.24** — *Bernoulli with a random success rate (Entry №01 + total probability).* By total probability $P(X=1) = 0.6(0.8) + 0.4(0.3) = 0.48 + 0.12 = 0.60$, so $\E[X] = 0.60$. Marginally $X \sim \mathrm{Bernoulli}(0.60)$, hence $\Var(X) = 0.6(0.4) = 0.24$.

**C8.27** — *Negative-binomial tail recast as a binomial CDF (Entries №04, №02).* "More than $6$ patrols for the $2$nd success" means the first $6$ patrols hold at most $1$ success: $P(X>6) = P(B \le 1)$, $B \sim \Binom(6, 0.4)$. $P(B=0) = 0.6^6 = 0.046656$; $P(B=1) = 6(0.4)(0.6^5) = 0.186624$. Sum $= 0.23328$.

### Quick-Answer Table

| # | Answer | | # | Answer |
|---|---|---|---|---|
| C8.1 | $\E=4.2$; $P=0.1176$ | | C8.10 | $0.3487$; $0.3487$ |
| C8.2 | $\E=2.5$; $P=0.144$ | | C8.11 | $n=20,\ p=0.3$; $0.000798$ |
| C8.3 | $\E=9.5$; $\Var=26.92$ | | C8.12 | $0.1991$ |
| C8.4 | $0.2231$; $0.2510$ | | C8.13 | $0.0916$ |
| C8.5 | $0.3000$ | | C8.14 | $\E=6.667$; $P=0.2074$ |
| C8.6 | $4.667$ | | C8.15 | $0.9489$ |
| C8.7 | $0.5940$ (over-est.) | | C8.16 | $\Poisson(6)$; $0.9826$; $\Var=6$ |
| C8.8 | $0.6321$; $0.0613$ | | C8.17 | $\lambda=1.609$; $0.4781$; mode $1$ |
| C8.9 | $\E=1.333$; $\Var=0.698$ | | C8.18 | $\E[N]=10$; $\E[\text{Water}]=1.5$ |
| C8.19 | $\E=0.7$; $\Var=0.21$ | | C8.20 | $P(0)=0.65,P(1)=0.35$; $\Var=0.2275$ |
| C8.21 | $\E[S]=1.2$; $\Var=0.72$ | | C8.22 | $\E[N]=1$; $P(N{=}0)=0.32768$ |
| C8.23 | $\E=\E[X^2]=0.6$; $\Var=0.24$ | | C8.24 | $\E=0.60$; $\Var=0.24$ |
| C8.25 | $0.1875$ | | C8.26 | $\E=12$; $\Var=48$ |
| C8.27 | $0.23328$ | | C8.28 | $\E[X^2]=91/6\approx15.17$; $P=1/3$ |
:::

## Badge Earned — Mastery Checklist

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/rainbow_badge.png" alt="Rainbow Badge" style="width:120px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Rainbow Badge</strong></figcaption>
</figure>

You earn the **Rainbow Badge** when you can, unaided:

1. **Name the family from the story** — classify any count problem as Bernoulli, binomial, geometric, negative binomial, hypergeometric, Poisson, or discrete uniform using the with/without-replacement and fixed-$n$/waiting decision tree. *(Outcome 2d2. → Entries №01–07, Trainer's Tips.)*
2. **Write each family's pmf, mean, and variance** from memory, and compute a tail via the complement. *(→ Worked Examples 8.1, 8.4.)*
3. **Apply geometric memorylessness** and **state the geometric/negative-binomial convention** you are using. *(→ Worked Examples 8.2, 8.5.)*
4. **Use the hypergeometric for without-replacement draws** and explain why the binomial overstates (finite-population correction). *(→ Worked Example 8.3, Team Rocket's Trap.)*
5. **Deploy the binomial→Poisson limit and Poisson additivity/thinning**, always rescaling $\lambda$ to the window. *(→ Worked Example 8.4, the Gym Battle.)*

> **Gym rematch pointers (🧴 Potion).** Miss item 1 → the decision-tree Trainer's Tip. Miss item 2 → Entries №02, №06 + WE 8.1. Miss item 3 → Concepts 3–4 + WE 8.2 / 8.5. Miss item 4 → Concept 5, WE 8.3, Team Rocket's Trap. Miss item 5 → Concept 6 + the Gym Battle, then retry C8.7, C8.13, C8.16.

---

*Next stop: Saffron City and beyond — where outcomes stop being countable and become **continuous**, and the bell curve begins to rule. (Chapter 9.)*

<!-- ===== CALLOUT BOX TEMPLATES (Pandoc fenced divs; styled by book/theme.css) =====
     ::: cold-open / pokedex-entry / trainers-tip / team-rocket / kanto-realworld
     Concept gate ("Do you already own this?") also uses a styled panel.
     Wrap the problem set in ::: problem-set and the key in ::: answer-key . -->
