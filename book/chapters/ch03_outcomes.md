<!--
  file: ch03_outcomes
  tier: C
  outcomes: 1a
  draft1_source: drafts/chapters_draft1/ch02_route_1.md
  maps_to: Route 1 — the Spearow swarm
-->

# The Space of Possible Outcomes {.type-normal}

<figure>
<img src="../../assets/maps/kanto_town_map.png" alt="Kanto town map with Pallet Town and Route 1 highlighted at the southern edge; the road north toward Viridian and Pewter stretches ahead, still unwalked." style="width:70%; max-width:520px; display:block; margin:1em auto; image-rendering: pixelated;">
<figcaption>The journey to a 10 starts here — Pallet Town and Route 1, where every probability you will ever compute first needs a <em>place to live</em>.</figcaption>
</figure>

::: cold-open
**▶ COLD OPEN — EPISODE: "The Sky Turns Black"**

You are ten years old, and the Poké Ball will not close.

Professor Oak warned you the last starter was unusual. You toss the ball anyway, and a small yellow Pokémon — **Pikachu, #025** — bats it aside and folds its arms. You sling it onto your shoulder and step out of Pallet Town onto **Route 1**.

Tall grass. Somewhere in it: a Pidgey, maybe a Rattata, maybe nothing at all — you can't see which. You throw a rock at a tree to scare something up, and you hit a **Spearow**.

That was a mistake.

The Spearow shrieks, and the sky answers. Not one bird but a *flock* — a dozen, two dozen, more — lifts off the treeline and wheels toward Pikachu, who is hurt, slow, and still refusing the ball that would protect it. Each diving Spearow may or may not strike. You cannot track every bird. You cannot list every dive. But you must decide *now* whether to run or make a stand, and that decision hinges on one number:

*What is the probability that **at least one** Spearow reaches Pikachu?*

The Pokédex chirps to **Actuary Mode**. Oak's voice crackles through: "You'll never get there by counting birds, Ash. First, count the **space** — the list of everything that *could* happen. Then count what you *don't* want, and subtract."

You have no idea what that means yet. You will by the end of this chapter.
:::

## Where You Are — 60-Second Retrieval

This is the first real chapter of the journey, so there is no prior *probability* chapter to retrieve — but everything here stands on the **Toolkit** you already built: a **set** is just a collection of things, and you can read a fraction. That is all you need. Take sixty seconds and prove you still own it before reading on.

::: trainers-tip
**60-SECOND RETRIEVAL — prove you own the toolkit**

Answer from memory; if any feels shaky, flip back to the Toolkit chapter before continuing.

1. A bag holds 4 red and 6 blue lures. You draw one at random. What is $P(\text{red})$? *(Answer: $4/10 = 0.4$ — favorable over total.)*
2. What does the word **set** mean? *(Answer: an unordered collection of distinct things, written in braces $\{\dots\}$.)*
3. What is $1 - 0.3$? *(Answer: $0.7$. Yes — the whole chapter leans on subtraction this easy.)*

All three instant? You're ready. Any hesitation? Reclaim it, then come back.
:::

## Oak's Briefing — Learning Outcomes & Test-Out Gate

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/characters/oak.png" alt="Professor Oak" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;">Professor Oak — the formalizer</figcaption>
</figure>

Oak's hologram flickers up from the Pokédex as you run.

"Before you can ever ask *what's the chance*, Ash, you must answer *the chance — out of **what**?* Every probability in this book lives inside a **space of possible outcomes**. Today you build that space, learn its three unbreakable rules, and learn the two pieces of bookkeeping — *not* and *or* — that turn a hopeless count of diving Spearow into one clean subtraction. Master this and you'll save Pikachu. Get sloppy with it, and you'll spend the rest of the syllabus double-counting."

By the end of this chapter you will be able to:

- **Describe** a **sample space** $S$, list its outcomes, and write events as subsets of $S$. *(Outcome 1a.)*
- **State** the three probability **axioms** and **derive** their consequences: $P(\varnothing)=0$, the **complement rule**, and monotonicity. *(Outcome 1a.)*
- **Manipulate** set operations — union, intersection, complement — and **use** De Morgan's laws to rewrite "none / neither." *(Outcome 1a.)*
- **Compute** probabilities with **inclusion–exclusion** for two and three events, and deploy the **complement trick** $P(\text{at least one}) = 1 - P(\text{none})$. *(Outcome 1a.)*
- **Distinguish** *mutually exclusive* from *independent* — the year's single most-confused pair. *(Outcome 1a.)*

> *Exam-weight signpost.* This is **General Probability — Outcome 1a**, the foundation under every later chapter. It is a **Tier C** chapter: the ideas are not hard, so we move briskly. But two of them — inclusion–exclusion and the mutually-exclusive-vs-independent trap — are tested *constantly* and trip up the unwary, so those get the full treatment.

::: concept-gate
**CHAPTER TEST-OUT GATE — Do You Already Own All of Route 1?**

Already fluent? Prove it. Work these four, about 2 minutes each, *with correct method*:

1. A wild slot is Pidgey ($0.45$), Rattata ($0.30$), Spearow ($0.15$), or nothing. Find $P(\text{some Pokémon appears})$.
2. $P(A)=0.6$, $P(B)=0.5$, $P(A\cap B)=0.2$. Find $P(A\cup B)$.
3. Pikachu refuses each of $3$ independent throws w.p. $0.5$. Find $P(\text{the ball closes at least once})$.
4. $A,B$ each have positive probability and are *mutually exclusive*. Can they be *independent*? One word, with the reason.

*(Answers: $0.90$; $0.90$; $0.875$; **no** — disjoint positive-probability events are maximally dependent.)* Four for four with the right reasoning? **Skip to the Gym Challenge** and claim the badge. Any miss or hesitation? The teaching below was built exactly for you — and each concept has its own skip-gate, so even a partial owner loses no time.
:::

---

Five ideas build on one another here, in increasing difficulty. We teach them **in order**, each with its own "do you already own this?" skip-check, then a lesson sized to its difficulty, then a Pokédex Entry you can carry into the exam:

1. **The sample space** — naming the world of outcomes *(the foundation everything uses)*
2. **The three axioms** — the unbreakable rules, and what they force to be true
3. **Set operations & De Morgan** — *and*, *or*, *not*, and rewriting "none"
4. **Inclusion–exclusion** — "or," and the overlap you must not double-count
5. **Mutually exclusive vs. independent** — the trap that sinks people all year

## Concept 1 — The Sample Space: Naming the World

::: concept-gate
**DO YOU ALREADY OWN THIS? — Sample Space**

A single Route 1 encounter yields a Pidgey, a Rattata, a Spearow, or nothing. Write the sample space $S$, and write the event "a bird appears" as a subset of it.

If you instantly wrote $S=\{\text{Pidgey},\text{Rattata},\text{Spearow},\text{nothing}\}$ and the event as $\{\text{Pidgey},\text{Spearow}\}$, you own this — **skip to Concept 2**. If "sample space" or "event as a subset" felt unfamiliar, read on.
:::

**Beat 1 — The one-sentence idea.** *Before you can measure a chance, you list every outcome that could happen; that complete list is the world the probability lives in.*

**Beat 2 — Anchor + concrete instance.** A **set** (from the Toolkit) is just a collection. Here the collection is *everything that could happen* on one wild encounter. Step into the Route 1 grass. Exactly one of four things greets you: a Pidgey, a Rattata, a Spearow, or nothing rustles.

**Beat 3 — Reason through it in plain words.** Write that complete list inside braces. Nothing outside the list can happen; the list misses nothing. *That* list — the universe of outcomes — is the thing every later probability is measured against. A *single outcome* is one item in the list (say, "Spearow"). An **event** is any yes/no question you can ask about the outcome — "did a bird appear?" — which corresponds to the *subset* of outcomes for which the answer is yes: $\{\text{Pidgey},\text{Spearow}\}$.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The beginner's slip is to forget an outcome — to write $S=\{\text{Pidgey},\text{Rattata},\text{Spearow}\}$ and quietly drop "nothing." But if "nothing" can happen, it *must* be in the space, or your probabilities won't sum to $1$ and every later answer inherits the error. **The space must be exhaustive: list everything, even the boring outcome.**

**Beat 4b — Picture it.** Think of $S$ as a box and each outcome as a labeled chip dropped inside. The space is exhaustive exactly when no chip is missing — including the dull "nothing" chip it is so easy to forget.

<figure>
<img src="../../assets/diagrams/ch03_sample_space.png" alt="A rounded rectangle labeled 'S — the sample space (every outcome, nothing missing)' containing four labeled outcome chips in a row: Pidgey, Rattata, Spearow, and nothing. A red arrow points up at the 'nothing' chip with the warning 'don't drop the boring outcome', stressing that the easy-to-forget no-encounter outcome still belongs inside the space." style="width:70%; max-width:520px; display:block; margin:1em auto;">
<figcaption>The world $S$ as a box of outcome chips. Every chip that <em>can</em> happen must be in the box — drop the boring "nothing" chip and your probabilities no longer sum to $1$.</figcaption>
</figure>

**Beat 5 — Translate into notation, one glyph at a time.** We name the space with a capital $S$ (for *sample Space*). Braces $\{\ \}$ hold a set. The symbol $\subseteq$, read aloud **"is a subset of,"** says one set sits entirely inside another. And $\in$, read **"is an element of,"** says a single thing is a member.

$$S = \{s_1, s_2, \dots\}, \qquad A \subseteq S \ \ (\text{``}A \text{ is a subset of } S\text{''}), \qquad s \in A \ \ (\text{``}s \text{ is in } A\text{''}).$$

We say "**event $A$ occurs**" exactly when the realized outcome $s$ lands inside $A$ — that is, when $s \in A$.

**Beat 6 — Generalize.** There is nothing to derive here: the sample space is a *definition*, the starting board on which the whole game is played. Every other concept in this chapter is a move on this board.

**Beat 7 — Ramp.** *Simplest:* a four-outcome encounter, above. *Twist:* the space can be huge or even infinite — "how many Spearow dive before one hits Pikachu?" has space $\{1,2,3,\dots\}$. *Edge:* the **empty set** $\varnothing$ (read "the empty set") is the event with no outcomes — the *impossible* event, e.g. "the encounter is both a Pidgey and a Rattata at once."

**Beat 8 — Consolidate.** You can now take any random situation, name its sample space $S$, and write any event as a subset of $S$. That single move — *name the world first* — is the discipline the entire book is built on.

::: pokedex-entry
**POKÉDEX ENTRY №01 — Sample Space, Outcome, Event**

$$S = \{\,s_1, s_2, \dots\,\}, \qquad A \subseteq S, \qquad A \text{ occurs} \iff s \in A.$$

*In plain terms:* $S$ is the complete, exhaustive list of everything that could happen; an **outcome** is one item; an **event** is a yes/no question, i.e. the subset of outcomes that answer "yes."

*Recognition cue:* whenever a problem describes a random situation and asks "what is the chance of…," your **first move** is to name $S$ — the universe the probability lives in. If "nothing" can happen, put it in.
:::

## Concept 2 — The Three Axioms (and What They Force)

::: concept-gate
**DO YOU ALREADY OWN THIS? — The Axioms**

State the three probability axioms from memory, then use them to prove $P(A^c) = 1 - P(A)$.

If you can rattle off "non-negative · whole space has mass $1$ · disjoint events add" and derive the complement rule in two lines, **skip to Concept 3**. Otherwise, read on — this is the bedrock and the proof is short.
:::

**Beat 1 — The one-sentence idea.** *Three simple rules pin down what the word "probability" is allowed to mean — and everything else in the chapter is squeezed out of those three lines.*

**Beat 2 — Anchor + concrete instance.** You already used these rules without naming them: on Route 1 the four encounter masses $0.45, 0.30, 0.15, 0.10$ are each $\ge 0$ and add to $1$. The axioms just *state out loud* what made that a legitimate assignment.

**Beat 3 — Reason through it in plain words.** What must any sensible "chance" obey? (i) A chance is never negative — there's no such thing as $-20\%$. (ii) *Something* in the space is certain to happen, so the whole space has chance $1$. (iii) If two events can't both occur, the chance that *one or the other* happens is just their two chances added — no overlap to worry about.

**Beat 4 — Surface and dismantle the tempting wrong idea.** The trap is to think rule (iii) lets you *always* add: "$P(\text{Water-type}) + P(\text{lives in grass})$." No — rule (iii) only grants addition when the events are **disjoint** (cannot co-occur). Adding overlapping events double-counts the middle, and the axiom gives you *no* license to do it. (Fixing that overlap is Concept 4.) Whenever you add probabilities, silently check: *are these pieces really disjoint?*

**Beat 5 — Translate into notation, one glyph at a time.** The symbol $\varnothing$ is the empty set; $A \cap B = \varnothing$ (read "$A$ and $B$ are **disjoint**") says they share no outcome.

$$\textbf{(A1)}\ P(A) \ge 0, \qquad \textbf{(A2)}\ P(S) = 1, \qquad \textbf{(A3)}\ A\cap B=\varnothing \Rightarrow P(A\cup B)=P(A)+P(B).$$

(A3 extends to any countable pile of pairwise-disjoint events.)

**Beat 6 — Derive the consequences (this is the payoff).** We don't *assume* the complement rule — we *prove* it. An event $A$ and its opposite $A^c$ ("not $A$") are disjoint and together fill the whole space, so $A \cup A^c = S$. Apply A3 to the disjoint pair, then A2:

$$P(A) + P(A^c) = P(A \cup A^c) = P(S) = 1 \quad\Longrightarrow\quad \boxed{P(A^c) = 1 - P(A)}.$$

Set $A = S$ (so $A^c = \varnothing$) and you also get $P(\varnothing) = 1 - P(S) = 0$ — the impossible event has chance zero. And if $A$ sits inside $B$ ($A \subseteq B$), then $B$ is "$A$ plus the disjoint leftover $B\cap A^c$," so $P(B) = P(A) + P(B\cap A^c) \ge P(A)$ — **monotonicity**: a bigger event is at least as likely. Three free theorems, all from three lines.

**Beat 7 — Ramp.** *Simplest:* read $P(A^c)=1-P(A)$ off a single given. *Twist:* the complement rule is the chapter's workhorse — "at least one" is almost always faster as $1 - P(\text{none})$ (Concept 4). *Edge:* monotonicity instantly bounds anything: since $A\cap B \subseteq A$, you always have $P(A\cap B) \le P(A)$, a free sanity check on every answer.

**Beat 8 — Consolidate.** You can now state the three axioms and derive the complement rule, $P(\varnothing)=0$, and monotonicity on demand — and you know that adding probabilities is *only* licensed for disjoint events.

::: pokedex-entry
**POKÉDEX ENTRY №02 — The Axioms & Their Consequences**

$$\textbf{(A1)}\ P(A)\ge 0, \quad \textbf{(A2)}\ P(S)=1, \quad \textbf{(A3)}\ A\cap B=\varnothing \Rightarrow P(A\cup B)=P(A)+P(B).$$

Forced consequences: $\;P(A^c)=1-P(A)$ (complement rule), $\;P(\varnothing)=0$, $\;A\subseteq B\Rightarrow P(A)\le P(B)$ (monotonicity), $\;0\le P(A)\le 1$.

*In plain terms:* chances are never negative, the whole space is certain, and *disjoint* chances add. Everything else is squeezed out of those three.

*Recognition cue:* the words **"not," "at least," "complement"** call for $1-P(A)$. And before you *ever* add two probabilities, confirm the pieces are disjoint — A3 is the only rule that lets you add.
:::

## Concept 3 — Set Operations & De Morgan: *and*, *or*, *not*

::: concept-gate
**DO YOU ALREADY OWN THIS? — Set Operations & De Morgan**

Rewrite "**neither** $A$ **nor** $B$ happens" as an intersection of complements, and evaluate it given $P(A\cup B)=0.72$.

If you wrote $(A\cup B)^c = A^c\cap B^c$ and got $1-0.72 = 0.28$, **skip to Concept 4**. If "De Morgan" or "neither" felt slippery, read on.
:::

**Beat 1 — The one-sentence idea.** *Events combine with three operations — and, or, not — and one law (De Morgan) that turns any "none/neither" into an "and not… and not…".*

**Beat 2 — Anchor + concrete instance.** On Route 1, let $G$ = "the encounter is a Pidgey" and $W$ = "the encounter is a Spearow." From these you can build new events: "a bird (Pidgey *or* Spearow)," "*not* a Pidgey," and so on.

**Beat 3 — Reason through it in plain words.** "$A$ **or** $B$" (at least one happens) collects the outcomes in either event. "$A$ **and** $B$" (both happen) collects the outcomes in both. "**not** $A$" collects everything in $S$ outside $A$. The subtle one is **"neither / none."** "Neither $A$ nor $B$" means "$A$ didn't happen *and* $B$ didn't happen." So a statement about a *union* ("not even one of them") secretly becomes a statement about an *intersection* of "didn'ts." That swap — *negation flips* or *into* and — is **De Morgan's law**, and it is the single most useful rewrite in the chapter.

**Beat 4 — Surface and dismantle the tempting wrong idea.** Tempting but wrong: "$(A\cup B)^c = A^c \cup B^c$." Test it in words: $(A\cup B)^c$ is "neither happened." $A^c \cup B^c$ is "at least one *didn't* happen" — which is true even if the *other* one did! Those are different events. The correct flip turns the *union's* complement into an *intersection*: $(A\cup B)^c = A^c \cap B^c$.

**Beat 5 — Translate into notation, one glyph at a time.** The union symbol $\cup$ reads **"or / union"**; the intersection $\cap$ reads **"and / intersect"**; the superscript $c$ in $A^c$ reads **"$A$-complement"** ("not $A$"). Backslash: $A\setminus B = A\cap B^c$ reads "$A$ but not $B$."

$$A\cup B\ (\text{or}), \quad A\cap B\ (\text{and}), \quad A^c = S\setminus A\ (\text{not}).$$

**De Morgan's first law, derived by an element chase (not asserted).** Take any outcome $s$ and ask what it means to live in each side. To say $s \in (A\cup B)^c$ is to say $s$ is *not* in the union — $s$ is in **neither** circle. But "neither" unpacks directly: $s \notin A$ **and** $s \notin B$, i.e. $s \in A^c$ **and** $s \in B^c$, which is exactly $s \in A^c\cap B^c$. Every step was an "if and only if," so the two sides contain the *same* outcomes — they are the same set. Run the identical chase starting from $s \in (A\cap B)^c$ ("not in both" $=$ "missing from at least one") and you get the second law. So, read aloud as "the complement of an *or* is the *and* of the complements," and vice versa:

$$\boxed{(A\cup B)^c = A^c\cap B^c, \qquad (A\cap B)^c = A^c\cup B^c.}$$

**Beat 6 — Picture it.** A Venn diagram makes "or," "and," and "neither" literal regions inside the rectangle $S$.

<figure>
<img src="../../assets/diagrams/ch03_venn_two.png" alt="A two-circle Venn diagram inside a rectangle labeled S. The left circle is event A, the right circle is event B, their lens-shaped overlap is A-intersect-B, the combined shaded area is A-union-B, and the region outside both circles is the complement of the union, labeled (A union B)-complement = A-complement intersect B-complement, which is the 'neither' region." style="width:70%; max-width:520px; display:block; margin:1em auto;">
<figcaption>Two events in $S$. "Or" is both circles together; "and" is the overlap; "neither" is the region <em>outside</em> both — which De Morgan names $A^c\cap B^c$.</figcaption>
</figure>

**Beat 7 — Consolidate.** You can now translate any English event into set notation, and the instant you read "none" or "neither," reach for De Morgan and the complement rule together: $P(\text{neither}) = P((A\cup B)^c) = 1 - P(A\cup B)$.

::: pokedex-entry
**POKÉDEX ENTRY №03 — Set Operations & De Morgan's Laws**

$$A\cup B\ (\text{or}), \quad A\cap B\ (\text{and}), \quad A^c\ (\text{not}), \quad A\setminus B = A\cap B^c.$$
$$(A\cup B)^c = A^c\cap B^c, \qquad (A\cap B)^c = A^c\cup B^c.$$

*In plain terms:* "none of them happened" $=$ "this one didn't *and* that one didn't." Negation flips unions to intersections and back.

*Recognition cue:* the words **"none," "neither," "not any"** are De Morgan announcing itself — rewrite as an intersection of complements, then usually finish with $1-P(\cup)$.
:::

## Concept 4 — Inclusion–Exclusion: "Or," and the Overlap

::: concept-gate
**DO YOU ALREADY OWN THIS? — Inclusion–Exclusion**

You log $100$ Route 1 Pokémon: $40$ are Water-type, $30$ live in tall grass, $12$ are *both*. Pick one log at random. What is $P(\text{Water } \textbf{or}\text{ grass})$?

If you answered **$0.58$** (not $0.70$) and can say *why you subtract the $12$*, **skip to Concept 5**. If you got $0.70$, you double-counted the overlap — read on.
:::

**Beat 1 — The one-sentence idea.** *The chance of $A$ **or** $B$ is the two pieces added together, minus the overlap you'd otherwise count twice.*

**Beat 2 — Anchor + concrete instance.** This is axiom A3 with the *disjoint* restriction lifted. Two circles, $A$ (Water-type) and $B$ (tall grass), inside the rectangle of $100$ logs, **overlapping** in the $12$ that are both.

You log **$100$ Pokémon**: **$40$ Water-type**, **$30$ live in tall grass**, **$12$ are both**. *What fraction is Water-type or grass-dwelling (at least one)?*

**Beat 3 — Reason through it in plain words.** Just add the piles and you get $40 + 30 = 70$ — but you've counted the **$12$ "both" Pokémon twice**, once in each pile. Each is one Pokémon, not two. Subtract the $12$ back out, once:

$$40 + 30 - 12 = 58 \quad\Longrightarrow\quad P(\text{Water or grass}) = \frac{58}{100} = 0.58.$$

**Beat 4 — Surface and dismantle the tempting wrong idea.** The tempting answer is the bare sum:

$$P(A) + P(B) = 0.40 + 0.30 = 0.70. \qquad\textbf{(wrong — double-counts the 12)}$$

That over-counts by exactly the overlap $\tfrac{12}{100} = 0.12$, leaving the correct $0.58$. The bare sum is right *only* when the circles don't overlap. The reverse error is just as common — *assuming* events can't overlap when they can. Don't assume the overlap is zero; **check it**.

**Beat 5 — Translate into notation, one glyph at a time.** "$A$ or $B$" is the union $A\cup B$; "$A$ and $B$" is the intersection $A\cap B$. "Subtract the overlap once" becomes the **two-event** rule:

$$P(A\cup B) = P(A) + P(B) - P(A\cap B).$$

**Beat 6 — Derive it from the Venn partition (don't just assert it).** Split the union into three *disjoint* regions: "$A$ only" $(A\cap B^c)$, "$B$ only" $(A^c\cap B)$, and "both" $(A\cap B)$. Because they're disjoint, A3 lets their probabilities add: $P(A\cup B) = P(A\cap B^c) + P(A^c\cap B) + P(A\cap B)$. Now $P(A) = P(A\cap B^c) + P(A\cap B)$ and $P(B) = P(A^c\cap B) + P(A\cap B)$ — each single event is "its own-only part plus the shared middle." Add those two and the middle gets counted **twice**; subtract one copy to recover the union. The "$-P(A\cap B)$" isn't a rule to memorize — it's exactly the over-count you created.

**Beat 7 — Ramp.** *Three events* repeat the bookkeeping: add the singles, subtract every pair, add back the triple (the center got subtracted one time too many):

$$P(A\cup B\cup C) = P(A)+P(B)+P(C) - P(A\cap B) - P(A\cap C) - P(B\cap C) + P(A\cap B\cap C).$$

*Twist (the complement is often faster):* $P(\text{neither}) = 1 - P(A\cup B) = 1 - 0.58 = 0.42$. *Edge:* if you're *told* the events are disjoint, the overlap is $0$ and the subtraction vanishes (back to A3) — but never *assume* disjointness; that's the trap of Concept 5.

**Beat 8 — Picture it.**

<figure>
<img src="../../assets/diagrams/ch03_venn_three.png" alt="A three-circle Venn diagram inside rectangle S, with circles A, B, C. Seven labeled cells: three 'only' regions, three pairwise-overlap lens regions, and the central triple-overlap region. Plus and minus signs annotate the inclusion-exclusion bookkeeping: singles added, pairwise overlaps subtracted, the central triple overlap added back once." style="width:62%; max-width:480px; display:block; margin:1em auto;">
<figcaption>The seven cells of a three-event diagram. Inclusion–exclusion's $+$singles $-$pairs $+$triple guarantees every cell is counted exactly once.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now compute "or" for two or three events by adding and removing overlaps, isolate a single Venn cell, and switch to the complement when it's faster.

::: pokedex-entry
**POKÉDEX ENTRY №04 — Inclusion–Exclusion**

$$P(A\cup B) = P(A) + P(B) - P(A\cap B).$$
$$P(A\cup B\cup C) = \sum P(\text{singles}) - \sum P(\text{pairs}) + P(A\cap B\cap C).$$

*In plain terms:* "or" adds the pieces but subtracts the overlaps you counted twice; for three events, add the triple back. The pattern is $+$singles, $-$pairs, $+$triple.

*Recognition cue:* **"at least one of," "either…or," "$A$ or $B$"** with overlapping events → inclusion–exclusion. Drop the overlap term *only* if you're told the events can't co-occur. For "at least one," check whether $1 - P(\text{none})$ is the faster road.
:::

## Concept 5 — Mutually Exclusive vs. Independent (The Trap)

::: concept-gate
**DO YOU ALREADY OWN THIS? — Mutually Exclusive vs. Independent**

Two events $A,B$ each have positive probability and are *mutually exclusive*. Can they ever be *independent*?

If you answered **"no — disjoint positive-probability events are maximally *dependent*,"** and can say why in one sentence, **skip to the Worked Examples**. If you hesitated, or thought "mutually exclusive sounds like independent," this section is the most important one in the chapter.
:::

**Beat 1 — The one-sentence idea.** *"Mutually exclusive" means two events can't both happen; "independent" means one happening tells you nothing about the other — and for positive-probability events these are opposites, never the same.*

**Beat 2 — Anchor + concrete instance.** You met disjointness in A3 (the overlap is $\varnothing$). Independence is new: it's the condition under which a joint chance *factors* into a product. Picture two of Ash's traps. **Trap A** springs w.p. $0.5$, **Trap B** w.p. $0.5$. Two scenarios: (i) only one trap can fire because they share a single spring — *mutually exclusive*; (ii) the traps are on opposite ends of the route and don't talk — *independent*.

**Beat 3 — Reason through it in plain words.** *Mutually exclusive* (scenario i): if A fires, B *cannot* — so learning "A fired" tells you *everything* about B (it didn't). That's the opposite of "tells you nothing." *Independent* (scenario ii): learning "A fired" leaves B's chance untouched at $0.5$, so the chance both fire is $0.5$ of $0.5 = 0.25$. The two scenarios give wildly different math from the *same two numbers* — which is exactly why confusing them is so costly.

**Beat 4 — Surface and dismantle the tempting wrong idea (the canonical misconception).** Here is the error that haunts the entire syllabus: **treating "mutually exclusive" and "independent" as synonyms.** They are nearly opposites. Suppose $A$ and $B$ each have positive probability and are mutually exclusive. Then if $A$ happens, $B$ is now *impossible* — knowing $A$ told you *everything* about $B$. Check the algebra: independence would require $P(A\cap B) = P(A)P(B) > 0$, but disjointness forces $P(A\cap B) = 0$. Contradiction. **Disjoint positive-probability events are maximally *dependent*, never independent.** And the practical fallout: for disjoint events you may *add* but never *multiply*; for independent events you may *multiply* but must *not* assume they're disjoint.

**Beat 5 — Translate into notation, one glyph at a time.** Two definitions, side by side:

$$\textbf{Mutually exclusive:}\ A\cap B = \varnothing \ \Rightarrow\ P(A\cap B) = 0.$$
$$\textbf{Independent:}\ P(A\cap B) = P(A)\,P(B).$$

Read the second aloud: "the chance both happen equals the chance of one *times* the chance of the other." Equivalently, "knowing $B$ doesn't change $A$": $P(A\given B) = P(A)$ (the bar $\given$ reads "given that" — you'll build it fully in the Bayes chapter).

**Beat 6 — These are definitions, not theorems.** Neither is derived: mutual exclusivity is a *fact about the outcomes* (the overlap is empty); independence is a *defining product condition*. The only content is keeping them straight — which the algebra in Beat 4 does permanently.

**Beat 7 — Ramp.** *Simplest:* classify a stated pair. *Twist:* the test cuts both ways — given $P(A)=0.5$, $P(B)=0.4$, $P(A\cup B)=0.7$, back out $P(A\cap B) = 0.5+0.4-0.7 = 0.2$ and compare to $P(A)P(B) = 0.2$; equal, so **independent** (Worked Example 3.4). *Edge:* if two *disjoint* events have positive marginals, asking "are they independent?" is a trick — the answer is always **no**.

**Beat 8 — Picture it.** The Venn picture nails the contrast: mutually exclusive circles *don't touch*; independent circles *overlap by exactly $P(A)P(B)$* — the overlap is forced to a specific size, not zero.

<figure>
<img src="../../assets/diagrams/ch03_me_vs_independent.png" alt="Two side-by-side Venn panels inside rectangle S. Left panel, 'Mutually exclusive': two non-touching circles A and B with no overlap, labeled P(A and B)=0, captioned 'no overlap, may ADD'. Right panel, 'Independent': two overlapping circles whose lens area equals exactly P(A) times P(B), labeled P(A and B)=P(A)P(B), captioned 'forced nonzero overlap, may MULTIPLY', emphasizing the overlap is a forced nonzero size, not empty." style="width:80%; max-width:620px; display:block; margin:1em auto;">
<figcaption>Mutually exclusive (no overlap, so you may add) versus independent (overlap forced to $P(A)P(B)$, so you may multiply). They are opposite situations, never the same.</figcaption>
</figure>

**Beat 9 — Consolidate.** You can now classify any stated pair, test independence with the product rule, and — crucially — you will never again multiply disjoint events or assume that "can't both happen" means "tells you nothing."

::: pokedex-entry
**POKÉDEX ENTRY №05 — Mutually Exclusive vs. Independent**

$$\textbf{Mutually exclusive:}\ P(A\cap B)=0 \quad(\text{may } \textit{add}). \qquad \textbf{Independent:}\ P(A\cap B)=P(A)P(B) \quad(\text{may } \textit{multiply}).$$

*In plain terms:* mutually exclusive = "can't both happen"; independent = "one tells you nothing about the other." Two positive-probability events **cannot be both** — disjoint ones are maximally dependent.

*Recognition cue:* **"cannot both occur," "disjoint," "either…or but not both"** → mutually exclusive (multiplying is *forbidden*). **"does not affect," "separate mechanisms," "with replacement"** → independent (multiplying is *required*). Never assume either; you must be told it or derive it.
:::

## Worked Examples — Faded Guidance

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/front/25.png" alt="Pikachu" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#025 Pikachu</strong> — refusing the ball, counting on your math</figcaption>
</figure>

Four examples, fading from fully narrated to exam speed. The first leads with the **Professor's Path** (the rigorous *why*) before the **Trainer's Path** (the fast *how*), because the "at least one" complement is the move you'll reuse most all year.

### Worked Example 3.1 — Saving Pikachu from the Flock (full narration; understanding-first)

**ARCHETYPE:** *"At least one" via the complement of independent events.*

**Setup.** This is the Cold Open, now a clean exam item. The Pokédex estimates each of the $n=12$ Spearow independently reaches Pikachu w.p. $p=0.20$. Find $P(\text{at least one reaches Pikachu})$.

**Step 1 — Identify (which move?).** Let $A_i$ = "Spearow $i$ reaches Pikachu," $P(A_i)=0.2$, independent. We want $P(A_1\cup\cdots\cup A_{12})$. Inclusion–exclusion over $12$ events is hopeless. The phrase **"at least one"** is the tell: complement it.

**Step 2 — Professor's Path (the why).** "At least one reaches" is the opposite of "**none** reaches." First, three glyphs you'll meet stretched over many events — each is just a Concept-3 operator repeated. The big union $\bigcup_i A_i$ reads **"the union over all $i$"** — the *or* of Concept 3 run across every bird ("$A_1$ or $A_2$ or … or $A_{12}$"). The big intersection $\bigcap_i A_i^c$ reads **"the intersection over all $i$"** — the *and* across every bird ("$A_1^c$ and $A_2^c$ and …"). And the capital pi $\prod_{i=1}^{12}$ reads **"the product of"** — just multiply the twelve terms together, the multiplicative cousin of a sum.

Now the move. By De Morgan (Entry №03), stretched from two events to twelve, $\left(\bigcup_i A_i\right)^c = \bigcap_i A_i^c$ — "none reaches" is the *and* of all the "didn't reach"s. Because the dives are independent, that intersection's probability **factors** into a product:

$$P(\text{none}) = P\!\left(\bigcap_{i=1}^{12} A_i^c\right) = \prod_{i=1}^{12} P(A_i^c) = \underbrace{(0.8)(0.8)\cdots(0.8)}_{12 \text{ terms}} = (1-0.2)^{12} = (0.8)^{12}.$$

Then the complement rule (Entry №02) gives the answer in one subtraction.

**Step 3 — Trainer's Path (the fast how).**
$$P(\text{at least one}) = 1 - P(\text{none}) = 1 - (0.8)^{12} = 1 - 0.0687 = 0.9313.$$

**Step 4 — Check & pitfall.** With $12$ chances at $20\%$ each, "at least one" should be high — $0.93$ feels right ✓. **Pitfall:** *adding* the $A_i$ ($12\times 0.2 = 2.4 > 1$, impossible) — overlapping events can't be summed. The complement sidesteps every overlap. *(Back-ref: Entries №02, №03.)*

### Worked Example 3.2 — Oak's Two-Species Census (partial guidance)

**ARCHETYPE:** *Two-event inclusion–exclusion; "exactly one."*

**Setup.** Over the morning, $P(\text{Pidgey seen})=0.6$, $P(\text{Rattata seen})=0.5$, $P(\text{both})=0.3$. Find $P(\text{at least one})$ and $P(\text{exactly one})$.

**Identify.** Let $G$ = Pidgey, $R$ = Rattata; want $P(G\cup R)$ and $P(\text{exactly one})$. *Your move: apply Entry №04, then peel off the "both."*

$$P(G\cup R) = P(G)+P(R)-P(G\cap R) = 0.6+0.5-0.3 = 0.8.$$
"Exactly one" is the union with the "both" cell removed:
$$P(\text{exactly one}) = P(G\cup R) - P(G\cap R) = 0.8 - 0.3 = 0.5.$$

**Check & pitfall.** $P(\text{exactly one}) + P(\text{both}) = 0.5 + 0.3 = 0.8 = P(G\cup R)$ ✓. **Pitfall:** reading "at least one" when the problem says "exactly one" — they differ by $P(\text{both})$, here a full $0.3$. *(Back-ref: Entry №04.)*

### Worked Example 3.3 — The Three-Species Survey (light guidance)

**ARCHETYPE:** *Three-event inclusion–exclusion + complement.*

**Setup.** $P(P)=0.5,\ P(R)=0.4,\ P(W)=0.3$; pairs $P(P\cap R)=0.2,\ P(P\cap W)=0.15,\ P(R\cap W)=0.1$; triple $P(P\cap R\cap W)=0.05$. Find $P(\text{at least one species seen})$ and $P(\text{none})$.

$$P(P\cup R\cup W) = (0.5+0.4+0.3) - (0.2+0.15+0.1) + 0.05 = 1.2 - 0.45 + 0.05 = 0.80.$$
$$P(\text{none}) = 1 - 0.80 = 0.20.$$

**Check & pitfall.** Sanity-check a single cell: "$P$ only" $= 0.5 - 0.2 - 0.15 + 0.05 = 0.20 \ge 0$ ✓. **Pitfall:** forgetting to *add back* the triple — drop it and you'd get $0.75$, because the center was subtracted three times but added only twice. *(Back-ref: Entry №04.)*

### Worked Example 3.4 — Independent, or Just Disjoint? (exam speed)

**ARCHETYPE:** *Independence test via inclusion–exclusion.*

**Setup.** $P(A)=0.5$, $P(B)=0.4$, $P(A\cup B)=0.7$. Are $A$ and $B$ independent?

$$P(A\cap B) = P(A)+P(B)-P(A\cup B) = 0.5+0.4-0.7 = 0.2, \qquad P(A)P(B) = (0.5)(0.4) = 0.2.$$
Since $P(A\cap B) = P(A)P(B)$, the events **are independent**.

**Check & pitfall.** They are *not* disjoint ($P(A\cap B)=0.2\neq 0$), which is consistent — disjoint would have *forbidden* independence. **Pitfall:** eyeballing "they overlap, so dependent" — independence is a *numeric* test ($P(A\cap B)$ vs. $P(A)P(B)$), not a yes/no-overlap question. *(Back-ref: Entries №04, №05.)*

## Trainer's Tips

::: trainers-tip
**TRAINER'S TIP — "At least one" → complement, every time**

The instant you read **"at least one,"** write $1 - P(\text{none})$ before anything else. A direct union of three or more events costs minutes; the complement is one line. On the TI-30XS, $1-(0.8)^{12}$ is `1 - 0.8` `^` `12` `=` — one keystroke chain, no parentheses gymnastics.
:::

::: trainers-tip
**TRAINER'S TIP — Build a Venn ledger for three events**

For any three-event problem, write the seven region values (three "only," three "pair-only," one triple) and confirm they sum to $\le 1$ and each is $\ge 0$. A negative cell means you misread a given — catch it *before* you compute, not in the answer choices.
:::

::: trainers-tip
**TRAINER'S TIP — Before you add or multiply, name the relationship**

Adding requires **disjoint**; multiplying requires **independent**. They are different licenses. The fastest way to lose a point is to multiply two events that merely "can't both happen," or add two that merely "don't affect each other." Say which one you've been told *out loud* before you reach for an operation.
:::

## Team Rocket's Trap

::: team-rocket
**TRANSMISSION INTERCEPTED — Team Rocket's Trap**

Jessie has rigged a net to catch Pikachu. "Two snares!" she crows. "Snare A catches it with probability $0.5$, snare B with probability $0.5$ — and they're *mutually exclusive*, James, so that means they're *independent*, so the chance we catch it is $0.5 \times 0.5 = 0.25$… no wait, that's *worse*. Ugh — just add them: $0.5 + 0.5 = 1$, guaranteed!"

Meowth nods sagely. Pikachu strolls between both snares untouched, and the net snaps shut on James.

**Where it fails:** Jessie committed the canonical error twice. **Mutually exclusive is the *opposite* of independent** — disjoint positive-probability events are maximally *dependent*, so you may **never** multiply their chances. And $P(A)+P(B)$ equals $P(A\cup B)$ *only because* the snares are disjoint, never because they're "independent"; here it lands at $1.0$, which should have screamed *impossible* (two single-spring snares can't guarantee a catch). Name the relationship first, *then* pick the operation — exactly the habit the last Trainer's Tip drilled.
:::

## From Kanto to the Real World

::: kanto-realworld
**⬛ FROM KANTO TO THE REAL WORLD**

This is the literal first move of **insurance pricing.**

Every policy an actuary prices begins exactly the way you began Route 1: by defining the **sample space** of loss events. A homeowner's policy might cover fire, theft, and water damage — *overlapping* events, because a burst pipe during a fire is both. **Inclusion–exclusion** is precisely how an actuary computes "the probability of **at least one** covered loss this year" without double-counting the households that suffer two at once, and the **complement trick** — $1 - P(\text{no claims})$ — is the single fastest route to a loss frequency.

The mutually-exclusive-vs-independent distinction is not academic here: modeling two perils as "independent" when a single storm causes both (so they're *positively dependent*) **under-prices the catastrophe** and can sink an insurer. The very same arithmetic you used to save Pikachu — $1-(1-q)^n$ — is how a reinsurer estimates the chance a portfolio suffers at least one large catastrophe across many regions in a year.

*Series bridge:* this set-and-axiom foundation is the bedrock under every later CAS exam; you'll rebuild it as "events" grow up into "loss **random variables**" in Chapter 6, and as conditioning shrinks these very spaces in Chapter 5.

*Transfer check:* could you solve this with **no Pokémon in it**? "$P(\text{fire})=0.04$, $P(\text{theft})=0.03$, $P(\text{both})=0.01$ — find the probability of at least one claim." Same inclusion–exclusion: $0.04+0.03-0.01 = 0.06$. If you can do that, the skill has transferred.
:::

## The Gym Battle — Boulder Badge Capstone

<figure style="margin:1.5em auto; max-width:160px; text-align:center;">
<img src="../../assets/sprites/front/21.png" alt="Spearow" style="width:140px; display:block; margin:0 auto; image-rendering: pixelated;">
<figcaption style="font-size:0.85em;"><strong>#021 Spearow</strong> — one bird from the flock, fully classified</figcaption>
</figure>

**The Challenge.** Back on Route 1, with Pikachu cornered, Oak poses the integrative problem that decides whether you stand or flee. You've classified each Spearow's dive by the threats it carries:

- $T$ = "targets Pikachu," $P(T)=0.40$;
- $L$ = "comes in low (hard to dodge)," $P(L)=0.35$;
- $F$ = "is a fast diver," $P(F)=0.30$.

The Pokédex's threat model gives the overlaps:
$$P(T\cap L)=0.18,\quad P(T\cap F)=0.12,\quad P(L\cap F)=0.10,\quad P(T\cap L\cap F)=0.05.$$

A Spearow is **"dangerous"** if it satisfies *at least one* of $T,L,F$. Answer three questions to choose your move:

1. $P(\text{a random Spearow is dangerous}) = P(T\cup L\cup F)$.
2. $P(\text{it targets Pikachu but is neither low nor fast})$ — the "pure $T$" cell.
3. With $n=12$ independent Spearow, $P(\text{at least one dangerous})$.

**ARCHETYPE:** *Three-event inclusion–exclusion + a single Venn cell + the "at least one" complement, integrated.*

**Step 1 — Identify.** Part 1 is Entry №04. Part 2 is one Venn cell built from the same givens. Part 3 chains the per-bird danger probability into the complement trick of Entry №02.

**Step 2 — Trainer's Path.**

*Part 1 — inclusion–exclusion.*
$$P(T\cup L\cup F) = (0.40+0.35+0.30) - (0.18+0.12+0.10) + 0.05 = 1.05 - 0.40 + 0.05 = 0.70.$$

*Part 2 — the pure-$T$ cell.* "Targets, but not low and not fast" is $P(T\cap L^c\cap F^c)$. Apply inclusion–exclusion *inside* $T$:
$$P(T\cap L^c\cap F^c) = P(T) - P(T\cap L) - P(T\cap F) + P(T\cap L\cap F) = 0.40 - 0.18 - 0.12 + 0.05 = 0.15.$$

*Part 3 — at least one dangerous.* Each bird is dangerous w.p. $q = 0.70$, independently, so
$$P(\text{at least one dangerous}) = 1 - (1-q)^{12} = 1 - (0.30)^{12} \approx 1 - 5.3\times 10^{-7} \approx 1.$$

**Step 3 — Professor's Path (Part 2, the long way, to prove the one-liner).** Decompose $T$ into four sub-regions by membership in $L$ and $F$: pure-$T$, "$T\cap L$ only," "$T\cap F$ only," and the triple. Their probabilities are $P(T\cap L\text{ only}) = 0.18 - 0.05 = 0.13$, $P(T\cap F\text{ only}) = 0.12 - 0.05 = 0.07$, triple $= 0.05$, and the four must sum to $P(T) = 0.40$. So pure-$T$ $= 0.40 - 0.13 - 0.07 - 0.05 = 0.15$ ✓ — matching the one-line formula.

**Step 4 — Check, verdict & pitfall.** $P(T\cup L\cup F) = 0.70 \le 1$ ✓; pure-$T$ $= 0.15 \le P(T) = 0.40$ ✓ (monotonicity). The flock's danger is essentially **certain**: twelve independent $0.70$ chances leave a vanishing "none" probability — so you make your stand, and Pikachu's Thundershock does the rest. **Pitfall:** in Part 3, using $P(T)=0.40$ instead of the *danger* probability $q=0.70$ — always read which event "at least one" refers to.

> Oak's hologram dims with a satisfied flicker. "You counted the space, then counted what you didn't want. That's the whole game, Ash. The **Boulder Badge** is as good as yours."

## The Gym Challenge — Problem Set

::: problem-set
**TEST-OUT INSTRUCTIONS.** Work this set timed (~5 min/problem), then check the **Answer Key** below. Hit the mastery bar (**80%+ with correct method**) and you may move on. Miss it, and the chapter is waiting. Problems are listed first; full worked solutions follow afterward (never interleaved). Markers: 🔴 Poké Ball = routine method · 🟡 routine-with-a-twist · 🔵 stretch.

### Route Trainers (mechanics)

**C3.1.** 🔴 The next Route 1 encounter is Pidgey ($0.45$), Rattata ($0.30$), Spearow ($0.15$), or "nothing rustles" otherwise. Write the sample space and find $P(\text{some Pokémon appears})$.

**C3.2.** 🔴 Let $A$ = "the sighting is a bird-type," $P(A)=0.55$. Using only the axioms, find $P(A^c)$ and name the rule you used.

**C3.3.** 🔴 $G$ = "it's a Pidgey" ($0.45$), $S$ = "it's a Spearow" ($0.15$). One wild slot holds one Pokémon, so both cannot appear. Find $P(G\cup S)$ and state whether $G,S$ are mutually exclusive, independent, or both.

**C3.4.** 🟡 $P(\text{rain})=0.40$, $P(\text{berry})=0.50$, and the two are **independent**. Find $P(\text{rain and berry})$, then $P(\text{at least one})$.

**C3.5.** 🟡 Given $P(A)=0.6$, $P(B)=0.5$, $P(A\cap B)=0.2$, fill the four-cell ledger $P(A\cap B^c),\,P(A^c\cap B),\,P(A\cap B),\,P(A^c\cap B^c)$ and confirm they sum to $1$.

**C3.6.** 🟡 Pikachu refuses each of $3$ independent throws w.p. $0.5$. Using the complement, find $P(\text{the ball closes at least once})$.

**C3.7.** 🔴 Rewrite $P(\text{neither } A \text{ nor } B)$ using De Morgan's law, then evaluate it given $P(A\cup B)=0.72$.

### Gym Battles (true SOA difficulty)

**C3.8.** 🟡 Among Pokémon brought to the Center, $70\%$ need a Potion, $40\%$ a status cure, $25\%$ both. For a random arrival find (a) $P(\text{at least one treatment})$, (b) $P(\text{exactly one})$, (c) $P(\text{neither})$.

**C3.9.** 🟡 Catches are logged by habitat: $P(F)=0.5,\,P(W)=0.4,\,P(C)=0.3$; pairs $0.2,\,0.15,\,0.1$; triple $0.05$. Find $P(\text{at least one habitat})$ and $P(\text{none})$.

**C3.10.** 🟡 Misty's challengers use a Water-type w.p. $0.6$, an Electric-type w.p. $0.5$, and *both* w.p. $p$; every challenger uses at least one (so the union is $1$). Find $p$ and $P(\text{exactly one type})$.

**C3.11.** 🟡 A slot pull wins the jackpot ($0.02$) or a small prize ($0.15$), mutually exclusive. Find $P(\text{win something on one pull})$ and $P(\text{win something at least once over two independent pulls})$.

**C3.12.** 🔵 $P(T)=0.40$, $P(L)=0.35$, but the overlap $P(T\cap L)$ is unrecorded. Find the smallest and largest possible values of $P(T\cup L)$, and of $P(T\cap L)$.

**C3.13.** 🟡 In a forest survey, $P(\text{Caterpie})=0.55$, $P(\text{Weedle})=0.45$, $P(\text{both})=0.30$. Find $P(\text{Caterpie but not Weedle})$ and $P(\text{at most one of the two species})$.

**C3.14.** 🟡 Given $P(A)=0.5$, $P(B)=0.4$, $P(A\cup B)=0.7$, decide whether $A,B$ are independent by computing $P(A\cap B)$ and comparing it to $P(A)P(B)$.

**C3.15.** 🔵 Trainers carry Potions ($0.8$), Antidotes ($0.5$), a map ($0.6$); pairs $P(\text{Pot}\cap\text{Anti})=0.4,\,P(\text{Pot}\cap\text{map})=0.5,\,P(\text{Anti}\cap\text{map})=0.35$; all three $0.3$. Find $P(\text{at least one item})$ and $P(\text{none})$.

### Elite Challenge (integrative / stretch)

**C3.16.** 🔵 *(The full flock.)* $n=12$ independent Spearow. Per bird: $P(T)=0.40,\,P(L)=0.35,\,P(F)=0.30$; pairs $0.18,\,0.12,\,0.10$; triple $0.05$. "Dangerous" = at least one of $T,L,F$. Find (a) the per-bird danger probability $q$; (b) $P(\text{none of the 12 dangerous})$; (c) $P(\text{purely fast: } F \text{ but neither } T \text{ nor } L)$ for one bird.

**C3.17.** 🔵 *(Solve, test, and check feasibility.)* Two traps: $P(A)=0.6$, $P(B)=0.5$, $P(\text{at least one})=0.8$. (a) Find $P(\text{both})$. (b) Are the traps independent? (c) If instead the traps were *mutually exclusive*, could $P(\text{at least one})=0.8$ hold? Explain via the axioms.
:::

## Answer Key

::: answer-key
**Full worked solution per problem, archetype-labeled and back-referenced to the Pokédex Entry used. A quick-answer table closes the section.**

**C3.1** — *Sample space + complement (Entries №01, №02).* $S=\{\text{Pidgey},\text{Rattata},\text{Spearow},\text{nothing}\}$ with masses $0.45,0.30,0.15,0.10$ (the last fills to $1$). "Some Pokémon appears" is the complement of "nothing":
$$P(\text{some}) = 1 - P(\text{nothing}) = 1 - 0.10 = 0.90.$$

**C3.2** — *Complement rule from the axioms (Entry №02).* $P(A^c) = 1 - P(A) = 1 - 0.55 = 0.45$, by the **complement rule**, itself a consequence of A2 ($P(S)=1$) and A3 applied to the disjoint pair $A, A^c$.

**C3.3** — *Disjoint union; ME vs. independent (Entries №02, №05).* One slot holds one Pokémon, so $G\cap S = \varnothing$ — **mutually exclusive**. By A3, $P(G\cup S) = 0.45 + 0.15 = 0.60$. They are **not** independent: $P(G\cap S) = 0 \neq P(G)P(S) = 0.0675$. Disjoint positive-probability events are never independent.

**C3.4** — *Independent intersection, then union (Entries №04, №05).* Independence factors the joint: $P(\text{rain}\cap\text{berry}) = (0.40)(0.50) = 0.20$. Union: $P(\text{rain}\cup\text{berry}) = 0.40 + 0.50 - 0.20 = 0.70$.

**C3.5** — *Four-cell Venn ledger (Entry №04).*
$$P(A\cap B^c) = 0.6 - 0.2 = 0.4, \quad P(A^c\cap B) = 0.5 - 0.2 = 0.3,$$
$$P(A\cap B) = 0.2, \quad P(A^c\cap B^c) = 1 - (0.4+0.3+0.2) = 0.1.$$
Sum: $0.4+0.3+0.2+0.1 = 1.0$ ✓.

**C3.6** — *"At least one" complement, independent trials (Entry №02).*
$$P(\text{closes at least once}) = 1 - P(\text{refuses all three}) = 1 - (0.5)^3 = 1 - 0.125 = 0.875.$$

**C3.7** — *De Morgan + complement (Entries №02, №03).*
$$P(\text{neither}) = P(A^c\cap B^c) = P\!\left((A\cup B)^c\right) = 1 - P(A\cup B) = 1 - 0.72 = 0.28.$$

**C3.8** — *Two-event inclusion–exclusion: all three quantities (Entries №02, №04).* Let $P$ = Potion ($0.70$), $S$ = status cure ($0.40$), $P\cap S = 0.25$.
(a) At least one: $0.70 + 0.40 - 0.25 = 0.85$.
(b) Exactly one: $0.85 - 0.25 = 0.60$.
(c) Neither: $1 - 0.85 = 0.15$.

**C3.9** — *Three-event inclusion–exclusion + complement (Entries №02, №04).*
$$P(F\cup W\cup C) = (0.5+0.4+0.3) - (0.2+0.15+0.1) + 0.05 = 1.2 - 0.45 + 0.05 = 0.80,$$
$$P(\text{none}) = 1 - 0.80 = 0.20.$$

**C3.10** — *Solve for an unknown overlap given the union (Entry №04).* "At least one type" means $P(W\cup E) = 1$, so $1 = 0.6 + 0.5 - p \Rightarrow p = 0.10$. Exactly one: $P(W\cup E) - P(W\cap E) = 1 - 0.10 = 0.90$.

**C3.11** — *Disjoint union + "at least once" over two independent trials (Entries №02, №04, №05).* Single pull (disjoint prizes): $P(\text{win}) = 0.02 + 0.15 = 0.17$. Two independent pulls, at least once: $1 - (1-0.17)^2 = 1 - (0.83)^2 = 1 - 0.6889 = 0.3111$.

**C3.12** — *Bounding union and intersection with unknown overlap (Entries №02, №04).* The overlap satisfies $P(T\cap L)\in[\max(0,\,0.40+0.35-1),\ \min(0.40,0.35)] = [0,\,0.35]$. Since $P(T\cup L) = 0.75 - P(T\cap L)$,
$$P(T\cup L)\in[0.75-0.35,\ 0.75-0] = [0.40,\ 0.75].$$
So $0.40\le P(T\cup L)\le 0.75$ and $0\le P(T\cap L)\le 0.35$.

**C3.13** — *Single Venn cell + "at most one" (Entries №02, №04).* Caterpie but not Weedle: $P(C) - P(C\cap W) = 0.55 - 0.30 = 0.25$. "At most one" is the complement of "both": $1 - P(\text{both}) = 1 - 0.30 = 0.70$.

**C3.14** — *Independence test via inclusion–exclusion (Entries №04, №05).* From inclusion–exclusion, $P(A\cap B) = P(A)+P(B)-P(A\cup B) = 0.5+0.4-0.7 = 0.2$. Compare $P(A)P(B) = (0.5)(0.4) = 0.2$. Since they're **equal**, $A$ and $B$ **are independent**.

**C3.15** — *Three-event inclusion–exclusion (Entry №04).*
$$P(\cup) = (0.8+0.5+0.6) - (0.4+0.5+0.35) + 0.3 = 1.9 - 1.25 + 0.3 = 0.95,$$
$$P(\text{none}) = 1 - 0.95 = 0.05.$$

**C3.16** — *Inclusion–exclusion + complement over $n$ trials, integrated (Entries №02, №04).*
(a) $q = (0.40+0.35+0.30) - (0.18+0.12+0.10) + 0.05 = 1.05 - 0.40 + 0.05 = 0.70$.
(b) $P(\text{none of 12 dangerous}) = (1-q)^{12} = (0.30)^{12} \approx 5.31\times 10^{-7} \approx 0$.
(c) Purely fast $= P(F\cap T^c\cap L^c) = P(F) - P(F\cap T) - P(F\cap L) + P(T\cap L\cap F) = 0.30 - 0.12 - 0.10 + 0.05 = 0.13$.

**C3.17** — *Solve overlap, independence test, axiom feasibility (Entries №02, №04, №05).*
(a) $P(\text{both}) = P(A) + P(B) - P(\text{at least one}) = 0.6 + 0.5 - 0.8 = 0.3$.
(b) Independent? $P(A)P(B) = (0.6)(0.5) = 0.30 = P(A\cap B)$, so **yes, independent**.
(c) If mutually exclusive, $P(A\cap B) = 0$, forcing $P(\text{at least one}) = P(A) + P(B) = 1.1 > 1$ — impossible by A1/A2. So disjoint traps could **not** give $0.8$ with these marginals.

### Quick-Answer Table

| # | Answer | | # | Answer |
|---|---|---|---|---|
| C3.1 | $0.90$ | | C3.10 | $p=0.10$; exactly one $0.90$ |
| C3.2 | $0.45$ (complement rule) | | C3.11 | $0.17$; $0.3111$ |
| C3.3 | $0.60$; ME, not independent | | C3.12 | $P(\cup)\in[0.40,0.75]$; $P(\cap)\in[0,0.35]$ |
| C3.4 | $0.20$; $0.70$ | | C3.13 | $0.25$; $0.70$ |
| C3.5 | $0.4,\,0.3,\,0.2,\,0.1$ | | C3.14 | $P(A\cap B)=0.2=P(A)P(B)$ → independent |
| C3.6 | $0.875$ | | C3.15 | $0.95$; none $0.05$ |
| C3.7 | $0.28$ | | C3.16 | $q=0.70$; none $\approx 5.3\times10^{-7}$; purely fast $0.13$ |
| C3.8 | $0.85$; $0.60$; $0.15$ | | C3.17 | $0.3$; independent; (c) impossible |
| C3.9 | $0.80$; none $0.20$ | | | |
:::

## Badge Earned — Mastery Checklist

<figure style="text-align:center; margin:1.5em auto;">
<img src="../../assets/badges/boulder_badge.png" alt="Boulder Badge" style="width:140px; display:block; margin:0 auto;">
<figcaption class="badge-caption"><strong>Boulder Badge earned!</strong></figcaption>
</figure>

You earn the **Boulder Badge** when you can, unaided:

1. **Name a sample space** $S$ from a word problem, write events as subsets, and apply set operations and De Morgan's laws to rewrite "none / neither / not both." *(Outcome 1a.)*
2. **State the three axioms** and **derive** $P(\varnothing)=0$, the complement rule, and monotonicity on demand. *(Outcome 1a.)*
3. **Execute inclusion–exclusion** for two and three events — isolating a single Venn cell and bounding a union when the overlap is unknown. *(Outcome 1a.)*
4. **Reach for the complement** the instant you read "at least one," computing $1 - P(\text{none})$. *(Outcome 1a.)*
5. **Distinguish mutually exclusive from independent** instantly — never multiplying disjoint events nor adding overlapping ones. *(Outcome 1a.)*

> **Gym rematch pointers (🧴 Potion).** Miss item 1 → re-read Concepts 1 & 3. Miss item 2 → Concept 2 + its derivation. Miss item 3 → Concept 4 + WE 3.2–3.3, then retry C3.9 / C3.15. Miss item 4 → WE 3.1 + the Gym Battle, then C3.6. Miss item 5 → Concept 5 + Team Rocket's Trap, then redo C3.3 and C3.17(c).

*Onward to Pewter City — where the question stops being "what could happen?" and becomes "how many ways can it happen?": the art of **counting**.*

---

<!-- ===== CALLOUT BOX TEMPLATES (Pandoc fenced divs; styled by book/theme.css) =====
     ::: cold-open / pokedex-entry / trainers-tip / team-rocket / kanto-realworld
     Concept gate ("Do you already own this?") also uses a styled panel.
     Wrap the problem set in ::: problem-set and the key in ::: answer-key . -->
